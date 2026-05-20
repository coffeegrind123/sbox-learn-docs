#!/usr/bin/env python3
"""
Scrape https://sbox.game/learn into a tree of frontmatter-annotated markdown
files under <repo>/docs/<author>/<slug>.md.

sbox.game is a Blazor Server SPA: the listing page renders tutorial cards
client-side over SignalR after the empty HTML shell, and individual tutorial
bodies are streamed in the same way. Raw HTTP scraping sees only the 3KB
shell — we need a real browser.

We use Camoufox (fingerprint-resistant Firefox + Playwright bindings) the
same way the user's other GitHub-Actions scrapers do: a prebuilt binary is
checked out into `backend/camoufox_build/camoufox-bin` and discovered here.

Output layout mirrors Facepunch/sbox-docs so the addon-side LearnRepoCache
can copy DocsRepoCache verbatim (tarball download → strip leading dir +
`docs/` prefix → walk *.md → BM25 index).

Each output file:
    ---
    title: "🎓 Freaks Beginner Resources"
    slug: frxxks/beginner-resources
    url: https://sbox.game/learn/frxxks/beginner-resources
    author: Frxxks
    author_slug: frxxks
    difficulty: Beginner
    topic: Editor
    content_type: Video
    tags: [beginner, collection, compilation, first]
    rating: 4
    views: 372
    updated: "yesterday"
    summary: "A comprehensive..."
    scraped_at: 2026-05-20T06:00:00Z
    ---

    # 🎓 Freaks Beginner Resources

    > A comprehensive...

    ... body markdown ...

Usage:
    python3 scrape.py [--output DIR] [--limit N] [--single SLUG]
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

sys.stdout.reconfigure(line_buffering=True)

import yaml
from markdownify import markdownify as html_to_md

SCRIPT_DIR = Path(__file__).resolve().parent          # backend/src
BACKEND_DIR = SCRIPT_DIR.parent                       # backend
REPO_DIR = BACKEND_DIR.parent                         # repo root
DEFAULT_OUT = REPO_DIR / "docs"

# Camoufox binary discovery — same conventions as the user's other scrapers.
# In CI the binary is unpacked to backend/camoufox_build/camoufox-bin and
# also symlinked to platformdirs(camoufox) so the Python camoufox package
# finds it automatically. Locally, `python -m camoufox fetch` drops it under
# ~/.cache/camoufox/camoufox-bin. We honor all three.
def _discover_camoufox_bin() -> Path | None:
    candidates = [
        Path("/opt/camoufox/camoufox-bin"),
        BACKEND_DIR / "camoufox_build" / "camoufox-bin",
    ]
    try:
        from platformdirs import user_cache_dir
        candidates.append(Path(user_cache_dir("camoufox")) / "camoufox-bin")
    except Exception:
        pass
    for c in candidates:
        if c.exists():
            return c
    return None


CAMOUFOX_BIN = _discover_camoufox_bin()

DEFAULT_HTTP_PROXY = os.environ.get("SCRAPER_HTTP_PROXY")

BASE = "https://sbox.game"
LIST_URL = f"{BASE}/learn?sort=newest"
NAV_TIMEOUT_MS = 45_000
WAIT_FOR_CARDS_MS = 25_000
WAIT_FOR_ARTICLE_MS = 30_000

# Brix editor stamps scoped-CSS markers like b-t37lsqnz4e="" on every tag.
# They're pure visual noise once we convert to markdown — strip them so
# diffs stay readable when the editor reshuffles its build hash.
BRIX_ATTR_RX = re.compile(r' b-[a-z0-9]+=""')


def log(msg: str) -> None:
    print(f"[scrape] {msg}", file=sys.stderr, flush=True)


# ─────────────────────────── Defender bridge ───────────────────────────
#
# @stackone/defender is a TypeScript/Node package that detects indirect
# prompt-injection attacks in arbitrary text (role markers, instruction-
# override patterns, unicode homoglyph attacks, base64-encoded payloads,
# etc.) using a two-tier pipeline: pattern detection + a fine-tuned ML
# classifier (22MB ONNX model). We pipe each tutorial's rendered markdown
# body through it before writing to disk so an attacker who lands a
# malicious tutorial on sbox.game can't leak instructions into a Claude
# Code session via the learn_* MCP tools the addon exposes.
#
# We spawn the Node bridge once per scrape run (cold-start: ~200-400ms
# for ONNX model load) and JSONL-pipe each tutorial through it. The
# bridge process exits cleanly when we close its stdin at scrape end.
#
# Failure modes:
#   - Bridge fails to start (Node missing, defender not installed):
#     scrape continues with `defender_active=False` and a loud warning;
#     every tutorial is treated as if it passed the scan but the manifest
#     records `defender: unavailable` so consumers can tell.
#   - Bridge crashes mid-run: scrape aborts. We never silently let
#     unscanned docs through after the bridge has been seen to work
#     once — that would be a security regression.
#   - A single tutorial fails to scan (timeout, malformed response):
#     skip-with-log; don't write the file. Same posture as a hard block.
class DefenderBridge:
    BRIDGE_SCRIPT = SCRIPT_DIR / "defender_bridge.mjs"

    def __init__(self) -> None:
        self.proc: subprocess.Popen | None = None
        self.active: bool = False
        self.fatal: bool = False
        self.blocked: list[dict] = []   # populated as scanners reject docs
        self.scanned: int = 0
        self.passed: int = 0
        self._next_id: int = 0

    def start(self) -> bool:
        """Spawn the Node bridge subprocess + wait for its `ready` line.
        Returns True if the bridge is live, False if Node or defender is
        unavailable (scrape continues with no scanning, loudly flagged)."""
        node = shutil.which("node")
        if not node:
            log("WARN: `node` not found on PATH — defender scan will be SKIPPED.")
            log("WARN: install Node 20+ and run `npm install` in backend/ to enable filtering.")
            return False
        if not self.BRIDGE_SCRIPT.exists():
            log(f"WARN: bridge script missing at {self.BRIDGE_SCRIPT} — defender scan SKIPPED.")
            return False
        try:
            self.proc = subprocess.Popen(
                [node, str(self.BRIDGE_SCRIPT)],
                cwd=BACKEND_DIR,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                bufsize=1,
                text=True,
                encoding="utf-8",
            )
        except Exception as e:
            log(f"WARN: failed to spawn defender bridge: {e} — scan SKIPPED.")
            return False

        # Drain stderr in the background so a chatty Node process doesn't
        # block on a full pipe. We surface stderr lines to our own log
        # so warmup warnings are visible.
        import threading

        def _drain_stderr():
            assert self.proc and self.proc.stderr
            for line in self.proc.stderr:
                log(f"  defender(stderr): {line.rstrip()}")

        threading.Thread(target=_drain_stderr, daemon=True).start()

        # Wait for the readiness line. The bridge prints {"ready": true, ...}
        # before reading stdin so we don't race the first send.
        assert self.proc.stdout
        ready_line = self.proc.stdout.readline()
        if not ready_line:
            log("WARN: defender bridge exited before emitting ready line — scan SKIPPED.")
            self.proc = None
            return False
        try:
            ready = json.loads(ready_line.strip())
        except Exception as e:
            log(f"WARN: bridge sent malformed ready line ({e!r}): {ready_line!r} — scan SKIPPED.")
            self.proc = None
            return False
        if not ready.get("ready"):
            log(f"WARN: bridge readiness line was unexpected: {ready_line!r} — scan SKIPPED.")
            self.proc = None
            return False
        self.active = True
        log(f"defender bridge ready (modelLoaded={ready.get('modelLoaded')})")
        return True

    def scan(self, md: str, source: str) -> tuple[bool, dict | None]:
        """Send one tutorial's markdown for scanning. Returns
        (allowed, result_dict). When the bridge is inactive returns
        (True, None) — never-scanned docs pass by default *only* if
        defender wasn't running in the first place; once start()
        succeeded, a scan error returns (False, …) so the doc gets
        skipped rather than silently letting an unknown-state body
        through."""
        if not self.active or not self.proc or not self.proc.stdin or not self.proc.stdout:
            return (True, None)
        if self.fatal:
            # Once we've seen the bridge die, refuse every subsequent
            # scan instead of silently passing. Caller will skip the doc.
            return (False, {"error": "bridge previously failed", "fatal": True})

        self._next_id += 1
        req = {"id": self._next_id, "md": md, "source": source}
        try:
            self.proc.stdin.write(json.dumps(req, ensure_ascii=False) + "\n")
            self.proc.stdin.flush()
            line = self.proc.stdout.readline()
        except BrokenPipeError as e:
            log(f"  defender bridge pipe broken: {e}")
            self.fatal = True
            return (False, {"error": str(e), "fatal": True})

        if not line:
            log("  defender bridge closed stdout unexpectedly")
            self.fatal = True
            return (False, {"error": "bridge eof", "fatal": True})

        try:
            result = json.loads(line.strip())
        except Exception as e:
            log(f"  defender bridge sent malformed json: {line!r} ({e})")
            self.fatal = True
            return (False, {"error": f"malformed json: {e}", "fatal": True})

        # Fatal-bridge-error response — bridge will exit, fail all
        # subsequent scans.
        if result.get("fatal"):
            log(f"  defender FATAL: {result.get('error')}")
            self.fatal = True
            return (False, result)

        if "error" in result:
            # Per-doc error (not fatal). Treat as "could not scan, skip".
            log(f"  defender scan error for {source}: {result['error']}")
            return (False, result)

        self.scanned += 1
        allowed = bool(result.get("allowed", False))
        if allowed:
            self.passed += 1
        else:
            self.blocked.append({
                "source": source,
                "riskLevel": result.get("riskLevel"),
                "tier2Score": result.get("tier2Score"),
                "detections": result.get("detections", []),
                "patternsByField": result.get("patternsByField", {}),
            })
            log(
                f"  defender BLOCKED {source}: "
                f"risk={result.get('riskLevel')} "
                f"score={result.get('tier2Score')} "
                f"detections={result.get('detections')}"
            )
        return (allowed, result)

    def close(self, timeout: float = 5.0) -> None:
        """Send EOF and wait for the bridge to exit. Idempotent."""
        if not self.proc:
            return
        try:
            if self.proc.stdin:
                self.proc.stdin.close()
        except Exception:
            pass
        try:
            self.proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            log("  defender bridge didn't exit on stdin close; killing")
            self.proc.kill()
            self.proc.wait(timeout=2.0)
        self.proc = None


def parse_proxy_url(proxy_url: str) -> dict | None:
    """http://user:pass@host:port → Playwright/Camoufox proxy config."""
    try:
        parsed = urlparse(proxy_url)
        if not parsed.hostname or not parsed.port:
            return None
        config = {"server": f"http://{parsed.hostname}:{parsed.port}"}
        if parsed.username:
            config["username"] = parsed.username
        if parsed.password:
            config["password"] = parsed.password
        return config
    except Exception:
        return None


# ─────────────────────────── In-page extraction ───────────────────────────

LIST_JS = r"""
(function () {
    const cards = Array.from(document.querySelectorAll('a.tutorialcard'));
    return cards.map(card => {
        const href = card.getAttribute('href') || '';
        const title = card.querySelector('.title')?.innerText?.trim() || '';
        const summary = card.querySelector('.summary')?.innerText?.trim() || '';
        const author_text = card.querySelector('.author')?.innerText?.trim() || '';
        const author = author_text.replace(/^by\s+/i, '').trim();
        const readers = card.querySelector('.readers')?.innerText?.trim() || '';
        const viewsMatch = readers.match(/([\d,]+)\s*views?/i);
        const views = viewsMatch ? parseInt(viewsMatch[1].replace(/,/g, ''), 10) : null;
        const tags = Array.from(card.querySelectorAll('.tags .tag')).map(t => t.innerText.trim()).filter(Boolean);
        const stars = card.querySelectorAll('.stars .star.filled').length;
        return { href, title, summary, author, views, tags, rating: stars };
    });
})()
"""

DETAIL_JS = r"""
(function () {
    const hero = document.querySelector('.tutorial-hero');
    const article = document.querySelector('article.tutorial-body');
    if (!hero || !article) return null;

    const chips = Array.from(hero.querySelectorAll('.eyebrow-chip')).map(c => ({
        text: c.innerText.trim(),
        cls: (c.className || '').toString(),
    }));
    let difficulty = null, topic = null, content_type = null;
    for (const c of chips) {
        if (/is-(beginner|capable|expert)/i.test(c.cls)) {
            difficulty = c.text;
        } else if (['text', 'video'].includes(c.text.toLowerCase())) {
            content_type = c.text;
        } else if (!topic) {
            topic = c.text;
        }
    }

    const title = hero.querySelector('h1')?.innerText?.trim() || '';
    const summary = hero.querySelector('.hero-summary')?.innerText?.trim() || '';
    const author_pill = hero.querySelector('.author-pill');
    const author = author_pill?.innerText?.trim() || '';
    const author_href = author_pill?.getAttribute('href') || '';
    const author_slug_match = author_href.match(/[?&]org=([^&]+)/);
    const author_slug = author_slug_match ? decodeURIComponent(author_slug_match[1]) : '';

    const metas = Array.from(hero.querySelectorAll('.meta')).map(m => m.innerText.trim());
    const updated_meta = metas.find(t => /updated/i.test(t)) || '';
    const views_meta = metas.find(t => /views?/i.test(t)) || '';
    const viewsMatch = views_meta.match(/([\d,]+)/);
    const views = viewsMatch ? parseInt(viewsMatch[1].replace(/,/g, ''), 10) : null;

    const footer = article.querySelector('footer.tutorial-footer');
    const up_btn = footer?.querySelector('.btn.like .label');
    const down_btn = footer?.querySelector('.btn.dislike .label');
    const up = up_btn ? parseInt(up_btn.innerText.trim() || '0', 10) : 0;
    const down = down_btn ? parseInt(down_btn.innerText.trim() || '0', 10) : 0;

    // Body = article minus voting footer. Unwrap the .pageditor/.brix
    // wrappers so the markdown comes out as plain content with no extra divs.
    const clone = article.cloneNode(true);
    clone.querySelector('footer.tutorial-footer')?.remove();
    const inner = clone.querySelector('.brix') || clone.querySelector('.pageditor') || clone;
    const html = inner.innerHTML;

    return {
        title, summary, difficulty, topic, content_type,
        author, author_slug,
        updated: updated_meta.replace(/^update\s*/i, '').trim(),
        views, up, down, html,
    };
})()
"""


async def enumerate_tutorials(page) -> list[dict]:
    log(f"loading listing: {LIST_URL}")
    await page.goto(LIST_URL, wait_until="domcontentloaded", timeout=NAV_TIMEOUT_MS)
    # Cards are inserted into the DOM by Blazor SignalR but may not be fully
    # "visible" by Playwright's default heuristic (they're inside a filter
    # overlay container that animates in). state="attached" is enough — we
    # just need to scrape them, not click them.
    await page.wait_for_selector("a.tutorialcard", state="attached", timeout=WAIT_FOR_CARDS_MS)
    # Small additional settle so child content (.title, .tags, etc) populates.
    await page.wait_for_timeout(750)
    cards = await page.evaluate(LIST_JS)
    log(f"found {len(cards)} tutorials on listing")
    return cards


async def fetch_tutorial(page, href: str) -> dict | None:
    """Fetch a single tutorial. One transparent retry on transient SignalR
    render timeouts — empirically the second load almost always succeeds
    because the connection is already warm.
    """
    url = BASE + href if href.startswith("/") else href
    for attempt in (1, 2):
        log(f"fetching: {url}" + (f" (retry {attempt})" if attempt > 1 else ""))
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=NAV_TIMEOUT_MS)
            await page.wait_for_selector("article.tutorial-body", state="attached", timeout=WAIT_FOR_ARTICLE_MS)
            await page.wait_for_timeout(500)  # Brix child-render settle
            data = await page.evaluate(DETAIL_JS)
            if not data:
                log(f"  WARN: detail extraction returned null for {url}")
                if attempt == 1: continue
                return None
            data["url"] = url
            return data
        except Exception as e:
            log(f"  WARN: render failed at {url}: {type(e).__name__}: {str(e)[:120]}")
            if attempt == 1:
                continue
            return None
    return None


# ────────────────────────────── HTML → MD ──────────────────────────────


def html_to_markdown(html: str) -> str:
    """Brix outputs use <div> as paragraph separators and wrap images in
    <figure class="attachment image"><a><img></a></figure>. markdownify
    handles all of that natively once we strip the b-xxxxx CSS scoping
    attributes for diff cleanliness.
    """
    html = BRIX_ATTR_RX.sub("", html)
    md = html_to_md(
        html,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style", "noscript"],
        escape_underscores=False,
        escape_asterisks=False,
    )
    # Collapse runs of 3+ blank lines down to one blank line.
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    return md


# ──────────────────────────── Frontmatter ────────────────────────────


def slug_from_href(href: str) -> tuple[str, str]:
    """'/learn/frxxks/beginner-resources' → ('frxxks', 'beginner-resources')."""
    parts = [p for p in href.strip("/").split("/") if p]
    if len(parts) < 3 or parts[0] != "learn":
        raise ValueError(f"unexpected tutorial href: {href!r}")
    return parts[1], parts[2]


def build_frontmatter(card: dict, detail: dict, scraped_at: str) -> dict:
    """Listing card has rating, tags, and a fresh view count; detail page has
    difficulty/topic/content_type and the author_slug. Both contribute.
    """
    author_slug, slug = slug_from_href(card["href"])
    title = detail.get("title") or card.get("title", "")
    summary = detail.get("summary") or card.get("summary", "")

    fm = {
        "title": title,
        "slug": f"{author_slug}/{slug}",
        "url": detail["url"],
        "author": detail.get("author") or card.get("author") or author_slug,
        "author_slug": detail.get("author_slug") or author_slug,
        "difficulty": detail.get("difficulty"),
        "topic": detail.get("topic"),
        "content_type": detail.get("content_type"),
        "tags": card.get("tags") or [],
        "rating": card.get("rating"),
        "views": detail.get("views") or card.get("views"),
        "upvotes": detail.get("up", 0),
        "downvotes": detail.get("down", 0),
        "updated": detail.get("updated") or "",
        "summary": summary,
        "scraped_at": scraped_at,
    }
    return {k: v for k, v in fm.items() if v not in (None, "", [], {})}


def render_page(fm: dict, body_md: str) -> str:
    # Emit each field independently so we can keep scalars in block style but
    # force `tags` into flow form (`[a, b, c]`). The addon's LearnEntry.cs
    # frontmatter parser is intentionally small and only understands flow-form
    # lists — keeping the on-disk emit constrained avoids dragging a real YAML
    # parser into the addon.
    lines: list[str] = []
    for k, v in fm.items():
        if isinstance(v, list):
            inner = ", ".join(yaml.safe_dump(item, default_flow_style=True, allow_unicode=True).strip().rstrip("...").strip() for item in v)
            lines.append(f"{k}: [{inner}]")
        else:
            scalar = yaml.safe_dump({k: v}, default_flow_style=False, sort_keys=False, allow_unicode=True).strip()
            lines.append(scalar)
    fm_yaml = "\n".join(lines)
    lines = ["---", fm_yaml, "---", ""]
    lines.append(f"# {fm.get('title', '')}")
    lines.append("")
    if fm.get("summary"):
        lines.append(f"> {fm['summary']}")
        lines.append("")
    lines.append(body_md.rstrip())
    lines.append("")
    return "\n".join(lines)


# ──────────────────────────── Orchestration ────────────────────────────


async def scrape_all(output_dir: Path, limit: int | None, single: str | None) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    scraped_at = (
        datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    )

    camoufox_path = str(CAMOUFOX_BIN) if CAMOUFOX_BIN else None
    if not camoufox_path:
        log("ERROR: camoufox binary not found in any candidate location")
        return 0
    log(f"using camoufox: {camoufox_path}")

    try:
        from camoufox.async_api import AsyncCamoufox
    except ImportError:
        log("ERROR: camoufox not installed (pip install camoufox)")
        return 0

    proxy_config = parse_proxy_url(DEFAULT_HTTP_PROXY) if DEFAULT_HTTP_PROXY else None
    kwargs = {
        "headless": True,
        "humanize": False,
        "enable_cache": True,
        "timeout": 60_000,
        "executable_path": camoufox_path,
    }
    if proxy_config:
        kwargs["proxy"] = proxy_config

    # Spin up the prompt-injection defender BEFORE the browser so a setup
    # failure surfaces fast and doesn't waste a Camoufox session. If the
    # bridge is unavailable (no Node, no defender install) we proceed with
    # `defender.active=False` — every doc passes through and the manifest
    # records the unavailability so consumers can tell.
    defender = DefenderBridge()
    defender.start()

    written = 0
    index_rows: list[dict] = []

    async with AsyncCamoufox(**kwargs) as browser:
        page = await browser.new_page()

        if single:
            href = single if single.startswith("/") else f"/learn/{single}"
            cards = [{
                "href": href, "title": "", "summary": "", "author": "",
                "views": None, "tags": [], "rating": None,
            }]
        else:
            cards = await enumerate_tutorials(page)
            # The listing renders each tutorial twice — once in a "Popular
            # Tutorials" rail at the top and once in the full grid below.
            # Dedupe by href, keeping the first (richer-card) occurrence.
            seen = set()
            unique = []
            for c in cards:
                href = c.get("href")
                if not href or href in seen:
                    continue
                seen.add(href)
                unique.append(c)
            log(f"  deduped: {len(cards)} → {len(unique)} unique tutorials")
            cards = unique
            if limit:
                cards = cards[:limit]

        for i, card in enumerate(cards, 1):
            href = card.get("href")
            if not href or not href.startswith("/learn/"):
                log(f"  skipping non-tutorial card #{i}: {href!r}")
                continue

            try:
                detail = await fetch_tutorial(page, href)
            except Exception as e:
                log(f"  ERROR fetching {href}: {e}")
                continue
            if not detail:
                continue

            try:
                fm = build_frontmatter(card, detail, scraped_at)
            except ValueError as e:
                log(f"  skipping malformed: {e}")
                continue

            body_md = html_to_markdown(detail["html"])

            # Scan the rendered body for prompt-injection patterns BEFORE
            # writing. The body is what reaches an LLM via the addon's
            # learn_search / learn_get tools, so it's the attack surface
            # we care about. Title/summary/tags also pass through but
            # they're short and structured; scanning the body covers the
            # interesting payload.
            allowed, scan = defender.scan(body_md, fm["slug"])
            if not allowed:
                # Either the doc was actively blocked (high/critical
                # risk + blockHighRisk:true) or the bridge failed to
                # scan it. In both cases we skip the write — never let
                # an unverified body land on disk where the addon's
                # tarball consumer will pull it into Claude Code.
                continue

            page_text = render_page(fm, body_md)

            author_slug = fm["author_slug"]
            slug = fm["slug"].split("/", 1)[1]
            out_path = output_dir / author_slug / f"{slug}.md"
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(page_text, encoding="utf-8")
            written += 1
            index_rows.append({
                "path": fm["slug"],
                "title": fm["title"],
                "difficulty": fm.get("difficulty"),
                "topic": fm.get("topic"),
                "content_type": fm.get("content_type"),
                "tags": fm.get("tags", []),
                "author": fm.get("author"),
                "url": fm["url"],
            })
            rel = out_path.relative_to(output_dir.parent) if out_path.is_relative_to(output_dir.parent) else out_path
            log(f"  wrote {rel}")

        await page.close()

    # Shut down the defender bridge cleanly. Safe to call even when
    # start() failed — it's a no-op then.
    defender.close()

    if defender.active:
        log(
            f"defender summary: scanned={defender.scanned} "
            f"passed={defender.passed} blocked={len(defender.blocked)}"
        )
    else:
        log("defender summary: bridge unavailable; NO scanning performed")

    # _manifest.json next to the docs tree — invaluable when debugging the
    # CI output without checking out every .md file. Defender summary is
    # included so downstream consumers can detect "the corpus was emitted
    # without scanning" vs "scanning passed cleanly" vs "N docs were held
    # back this run" without grepping CI logs.
    index_path = output_dir / "_manifest.json"
    index_path.write_text(
        json.dumps({
            "scraped_at": scraped_at,
            "count": len(index_rows),
            "tutorials": index_rows,
            "defender": {
                "active": defender.active,
                "scanned": defender.scanned,
                "passed": defender.passed,
                "blocked": defender.blocked,
            },
        }, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    log(f"wrote manifest: {index_path}")

    return written


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--single", type=str, default=None, help="Scrape only 'author/slug'")
    args = ap.parse_args()

    written = asyncio.run(scrape_all(args.output, args.limit, args.single))
    log(f"done: wrote {written} tutorials to {args.output}")
    sys.exit(0 if written > 0 else 1)


if __name__ == "__main__":
    main()
