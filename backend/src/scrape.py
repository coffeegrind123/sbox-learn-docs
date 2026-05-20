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

    # _manifest.json next to the docs tree — invaluable when debugging the
    # CI output without checking out every .md file.
    index_path = output_dir / "_manifest.json"
    index_path.write_text(
        json.dumps({
            "scraped_at": scraped_at,
            "count": len(index_rows),
            "tutorials": index_rows,
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
