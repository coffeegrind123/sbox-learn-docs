# sbox-learn-docs (mirror)

Automated daily mirror of community tutorials from [sbox.game/learn](https://sbox.game/learn), converted to YAML-fronted Markdown files committed to `docs/`.

Consumed by the [claude-sbox](https://sbox.game/ghage/claude-sbox) addon's `learn_search` / `learn_get` / `learn_list` / `learn_refresh` MCP tools — the addon downloads this repo as a tarball, walks the `docs/` tree, and builds a BM25 index over title + tags + body.

## Why this exists

`sbox.game` is a Blazor Server SPA — tutorial content is streamed via SignalR after the initial HTML shell loads. A raw `curl https://sbox.game/learn` returns only ~3KB of empty markup. An in-editor scraper would have to embed a full browser; mirroring out-of-band keeps the addon thin and the corpus pre-rendered.

This mirror was modeled after Facepunch's own [`sbox-docs`](https://github.com/Facepunch/sbox-docs) repo so the addon's `LearnRepoCache` could clone the existing `DocsRepoCache` pattern verbatim.

## Layout

```
sbox-learn-docs/
├── backend/
│   ├── requirements.txt        # camoufox, markdownify, PyYAML
│   └── src/scrape.py           # entry point
├── docs/                       # CC-BY-4.0 — mirror output, committed
│   ├── <author>/<slug>.md      # one tutorial per file (frontmatter + body)
│   └── _manifest.json          # debug index of everything scraped this run
└── .github/workflows/scrape.yml  # daily @ 06:00 UTC
```

Each `.md` file:

```yaml
---
title: "🎓 Freaks Beginner Resources"
slug: frxxks/beginner-resources
url: https://sbox.game/learn/frxxks/beginner-resources
author: Frxxks
author_slug: frxxks
difficulty: Beginner            # Beginner | Capable | Expert
topic: Editor                   # Effects, Physics, Gameplay, Design, UI, ...
content_type: Video             # Text | Video
tags: [beginner, collection, compilation, first]
rating: 4
views: 372
upvotes: 14
downvotes: 0
updated: "yesterday"
summary: "A comprehensive beginners resource collection..."
scraped_at: 2026-05-20T06:00:00Z
---

# 🎓 Freaks Beginner Resources

> A comprehensive beginners resource collection...

... body markdown ...
```

## Running locally

```bash
cd backend
pip install -r requirements.txt
# Camoufox needs a prebuilt binary. CI uses the patched fork at
# coffeegrind123/camoufox-beta; locally you can either fetch the same
# release or use a system-installed camoufox.
mkdir -p camoufox_build
curl -L -o camoufox.zip "https://github.com/coffeegrind123/camoufox-beta/releases/download/v146.0.1-beta.25-patched/camoufox-146.0.1-beta.25-lin.x86_64.zip"
unzip camoufox.zip -d camoufox_build && rm camoufox.zip
chmod +x camoufox_build/camoufox-bin

python src/scrape.py --output ../docs
# Or scrape a single tutorial:
python src/scrape.py --single frxxks/beginner-resources --output /tmp/test-out
```

## License

The scraper code in this repo is MIT. The scraped content under `docs/` is mirrored from sbox.game/learn — community-submitted tutorials whose copyright lies with their respective authors. Treat the mirror as CC-BY-4.0 (attribute the original author and link to the source URL in `frontmatter.url`).
