<div align="center">
  <br>
  <img src="assets/favicon.svg" width="72" height="72" alt="Tech Library logo">
  <h1 align="center">Tech Library</h1>
  <p align="center">A beginner-friendly collection of tutorials, tools, programming guides, and resources — all in one place, no internet required after first load.</p>
  <br>
  <p>
    <a href="https://schooicodes.github.io/library/">View Live</a> ·
    <a href="https://github.com/SchooiCodes/library">GitHub</a>
  </p>
  <br>
</div>

## Overview

Tech Library is a static HTML documentation hub built for learners, tinkerers, and self-hosting enthusiasts. It started as a personal knowledge base and grew into 120+ pages covering everything from Git and Python to Kali Linux, Minecraft modding, privacy tools, and hardware diagnostics.

Optimized for low-end hardware — runs smoothly on an Intel Core i3-4130 with Intel HD 4400 integrated graphics, no JavaScript framework overhead, no build step.

## Features

- **120+ pages** across 15+ categories
- **84 tutorials** with auto-generated Table of Contents, navigation buttons, and further reading references
- **6 color themes** — Default, Ocean, Forest, Sunset, Midnight, Mono (light & dark variants)
- **Mobile-responsive** with hamburger menu and bottom nav
- **Offline-friendly** — no build tools, just open `index.html`
- **Admin panel** — web-based content editor with live preview (optional)
- **SVG favicon** — crisp at any resolution
- **Performance tuned** — no `backdrop-filter`, minimal GPU compositing, throttled scroll handlers, `display=optional` fonts

## Categories

| Category | Description |
|---|---|
| [Tutorials](tutorials/) | 84 guides — Git, Python, Linux, Docker, networking, security, Minecraft, and more |
| [Programming](programming/) | Languages, scripting, automation |
| [Resources](resources/) | Curated links, cheat sheets, references |
| [Projects](projects/) | Project ideas and build logs |
| [Tools](tools/) | CLI tool guides and walkthroughs |
| [Security](security/) | Privacy, encryption, hardening |
| [Survival](survival/) | Digital survival and self-hosting |
| [Piracy](piracy/) | Educational resource on file sharing (disclaimer included) |
| [Minecraft](minecraft/) | Server setup, commands, modding |
| [Gaming](gaming/) | Game servers and tweaks |
| [SMT](smt/) | SMT tool documentation |
| [Crib](docs/crib.html) | Original reference page |

## Quick Start

1. **Clone the repo:**
   ```bash
   git clone https://github.com/SchooiCodes/library.git
   cd library
   ```

2. **Open `index.html`** in your browser — that's it. No server, no build step, no dependencies.

3. **Optional: Run the admin panel** for web-based editing:
   ```bash
   bash admin/run.sh
   ```
   Then open `http://127.0.0.1:5050` (login: `admin` / `admin123`).

## Project Structure

```
├── index.html                 # Home page
├── assets/
│   ├── style.css              # Main stylesheet (~1100 lines, 6 themes)
│   ├── scripts.js             # Dark/light toggle, theme picker, scroll reveal, mobile nav
│   └── favicon.svg            # SVG favicon
├── tutorials/                 # 84 tutorial pages + index
├── programming/               # Programming guides & references
├── resources/                 # Curated resource links
├── projects/                  # Project documentation
├── tools/                     # CLI tool guides
├── security/                  # Security & privacy resources
├── survival/                  # Digital survival guides
├── piracy/                    # Educational file-sharing info
├── minecraft/                 # Minecraft server setup & commands
├── gaming/                    # Gaming server guides
├── docs/                      # Core reference (Crib, etc.)
├── smt/                       # SMT tool documentation
├── creatives/                 # Creative resources
├── opencode/                  # OpenCode documentation
├── admin/                     # Web-based admin panel (Flask)
│   ├── app.py                 # Flask application
│   ├── templates/             # Jinja2 templates
│   └── config.json            # Admin credentials (gitignored)
└── .gitignore
```

## Admin Panel

The admin panel provides a web UI for editing pages without touching the command line.

**Features:**
- Dashboard with page stats and recently edited list
- Sidebar with searchable/filterable page tree
- CodeMirror editor with HTML syntax highlighting and live preview
- AJAX auto-save with unsaved-changes warning
- Create new pages from templates (blank, tutorial, basic)
- Rename and delete pages
- Change admin credentials

```bash
bash admin/run.sh
# → http://127.0.0.1:5050
# → admin / admin123
```

## Theme System

6 color themes, each with light and dark variants:

| Theme | Accent | CSS class |
|---|---|---|
| Default | Purple/Blue gradient | (default) |
| Ocean | Teal/Cyan | `body.theme-ocean` |
| Forest | Green | `body.theme-forest` |
| Sunset | Orange/Red | `body.theme-sunset` |
| Midnight | Indigo | `body.theme-midnight` |
| Mono | Grayscale | `body.theme-mono` |

Theme preference is saved to `localStorage`. The palette button in the navbar opens the theme picker.

## Performance Notes

This site targets low-end hardware (tested on a 2013-era i3-4130 with Intel HD 4400 graphics):
- No `backdrop-filter: blur()` — extremely expensive on Intel HD 4400
- CSS transitions limited to specific properties (`transform`, `opacity`, `color`, `background`, `box-shadow`)
- Scroll listeners throttled with `requestAnimationFrame` + `passive: true`
- Google Fonts uses `display=optional` to prevent layout reflow
- Preconnect to all CDN origins (fonts.googleapis, cdnjs.cloudflare)

## License

This project is for educational purposes. Content is licensed under MIT unless otherwise noted.

## Acknowledgments

- Font Awesome for icons
- Inter and Fira Code typefaces
- The open-source community for the knowledge compiled here
