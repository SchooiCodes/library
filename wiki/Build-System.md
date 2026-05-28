# Build System

The build system is a single Python script: `build.py`.

## What It Does

| Step | Action |
|---|---|
| 1 | Count tutorials, lexicon entries, categories |
| 2 | Build `search-index.json` from all HTML pages |
| 3 | Embed search index into `assets/scripts.js` |
| 4 | Update landing page stats |
| 5 | Propagate search bar (replace old toggle buttons) |
| 6 | Inject breadcrumbs into content pages |
| 7 | Update footer across all pages |
| 8 | Sync navigation via `update_nav.py` |
| 9 | Inject `assistant.js` script tag into all pages |

## Usage

```bash
python3 build.py
```

Run this after:
- Adding or removing any HTML page
- Updating page titles or descriptions
- Changing the site's category structure

## Search Index Format

The index is an array of objects:

```json
{
  "title": "Docker Tutorial",
  "url": "/tutorials/docker.html",
  "desc": "Learn Docker from scratch...",
  "cat": "tutorials",
  "popularity": 70,
  "date": "2025-03-15"
}
```

This is embedded into `scripts.js` as `window.__TL.searchIndex` for zero-latency client-side search.
