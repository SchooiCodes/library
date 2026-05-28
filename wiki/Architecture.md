# Architecture

## Directory Structure

```
library/
├── index.html               # Landing page
├── assets/
│   ├── style.css            # Full stylesheet — 10 themes, dark/light
│   ├── scripts.js           # Search, lexicon, themes, assistant init
│   ├── assistant.js         # AI chat assistant (Cloudflare Worker client)
│   ├── theme.js             # Theme + dark mode manager
│   └── favicon.svg          # SVG favicon
├── tutorials/               # 190+ step-by-step tutorials
├── survival/                # Emergency digital resources
├── piracy/                  # Educational file-sharing resources
├── lexicon/                 # Tech glossary (240+ terms)
├── resources/               # Curated links and references
├── buying-guide/            # Hardware buying guides
├── smt/                     # SMT multitool docs
├── docs/                    # Legacy documentation
├── admin/                   # Flask web editor
│   ├── app.py
│   └── templates/
├── build.py                 # Unified build system
├── update_nav.py            # Navigation syncer
└── update_headers.py        # Title/meta updater
```

## Data Flow

1. **Static HTML** — every page is a standalone HTML file with `<!-- @category -->` markers and front-matter `<meta>` tags
2. **`build.py`** — reads all HTML files, builds `search-index.json`, embeds the index into `scripts.js`, updates landing page stats, injects breadcrumbs + footer + assistant script
3. **Browser** — loads `scripts.js` which reads `window.__TL.searchIndex` (embedded), enabling instant client-side search without network requests
4. **AI Assistant** — `assistant.js` reads the same embedded search index for RAG, queries a Cloudflare Worker for AI responses via SSE streaming

## Key Design Decisions

- **No framework, no bundler** — plain HTML/CSS/JS for maximum portability and zero-build workflow
- **`file://` compatible** — all internal links are relative; search index is embedded directly in JS (no `fetch`)
- **Mobile first** — responsive grid, hamburger menu, bottom nav bar for phones
- **Low-end hardware friendly** — no `backdrop-filter`, throttled scroll handlers, `display=optional` fonts
