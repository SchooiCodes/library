# Admin Panel

The admin panel is a Flask web application in `admin/` that provides a CMS-like interface for editing the library from a browser.

## Quick Start

```bash
bash admin/run.sh
# → http://127.0.0.1:5050
# → login: admin / admin123
```

## Features

| Feature | Description |
|---|---|
| **Dashboard** | Stats, recently edited, directory breakdown |
| **Sidebar** | Searchable collapsible page tree |
| **CodeMirror Editor** | HTML syntax highlighting, line numbers, bracket matching |
| **Live Preview** | Side-by-side preview with actual site CSS |
| **AJAX Save** | `Ctrl+S` saves via XHR with toast notification |
| **Create Page** | Path picker + template selector |
| **Settings** | Change admin credentials |

## Architecture

- `admin/app.py` — Flask application
- `admin/templates/` — Jinja2 templates
- `admin/config.json` — Credentials (gitignored)
