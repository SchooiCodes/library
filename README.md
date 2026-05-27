<div align="center">
  <a href="https://schooicodes.github.io/library/">
    <picture>
      <img src="assets/favicon.svg" width="80" height="80" alt="Tech Library logo" style="margin-bottom:8px;">
    </picture>
  </a>
  <h1 style="font-size:2.4rem;margin:8px 0 4px;font-weight:800;letter-spacing:-0.02em;">
    <span style="background:linear-gradient(135deg,#667eea,#764ba2);-webkit-background-clip:text;-webkit-text-fill-color:transparent;">Tech Library</span>
  </h1>
  <p style="font-size:1.1rem;max-width:600px;margin:8px auto;color:#888;">
    A beginner-friendly collection of <strong>120+ pages</strong> covering tutorials, tools, programming, security, and more — all in one place, zero build step.
  </p>
  <br>
  <a href="https://schooicodes.github.io/library/">
    <img src="https://img.shields.io/badge/🌐_View_Live-Site-667eea?style=for-the-badge&logo=githubpages&logoColor=white" alt="View Live">
  </a>
  &nbsp;
  <a href="https://github.com/SchooiCodes/library">
    <img src="https://img.shields.io/badge/📦_GitHub-Repo-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  </a>
  <br><br>
  <img src="https://img.shields.io/github/repo-size/SchooiCodes/library?style=flat&label=Repo%20Size&labelColor=1a1a2e&color=667eea" alt="Repo Size">
  &nbsp;
  <img src="https://img.shields.io/github/last-commit/SchooiCodes/library?style=flat&label=Last%20Commit&labelColor=1a1a2e&color=764ba2" alt="Last Commit">
  &nbsp;
  <img src="https://img.shields.io/github/stars/SchooiCodes/library?style=flat&label=Stars&labelColor=1a1a2e&color=667eea" alt="Stars">
  &nbsp;
  <img src="https://img.shields.io/badge/Pages-121+-667eea?style=flat&labelColor=1a1a2e" alt="121+ Pages">
  &nbsp;
  <img src="https://img.shields.io/badge/Tutorials-84-764ba2?style=flat&labelColor=1a1a2e" alt="84 Tutorials">
  &nbsp;
  <img src="https://img.shields.io/badge/Themes-6-f59e0b?style=flat&labelColor=1a1a2e" alt="6 Themes">
  <br><br>
</div>

---

> **🎯 What is this?** A living knowledge base that started as a personal reference library and grew into a full documentation hub. Built for learners, tinkerers, self-hosting enthusiasts, and anyone who prefers their docs offline and fast.

---

## ✨ Features

<table>
  <tr>
    <td width="50%">
      <h3>📚 84 Tutorials</h3>
      Git, Python, Linux, Docker, networking, security, Minecraft modding, Kali Linux — each with auto-generated <strong>Table of Contents</strong>, <strong>navigation buttons</strong>, and curated <strong>further reading references</strong>.
    </td>
    <td width="50%">
      <h3>🎨 6 Color Themes</h3>
      Default, Ocean, Forest, Sunset, Midnight, Mono — each with <strong>light & dark variants</strong>. Pick your vibe via the palette button in the navbar. Saved to <code>localStorage</code>.
    </td>
  </tr>
  <tr>
    <td>
      <h3>📱 Mobile-First</h3>
      Fully responsive with hamburger menu, bottom navigation bar, and touch-friendly layouts. Works on phones, tablets, and that old laptop in the drawer.
    </td>
    <td>
      <h3>⚡ Performance Tuned</h3>
      Tested on a <strong>2013 Intel Core i3-4130</strong> with Intel HD 4400 graphics. No <code>backdrop-filter</code>, no heavy frameworks, throttled scroll handlers, <code>display=optional</code> fonts.
    </td>
  </tr>
  <tr>
    <td>
      <h3>🔌 Zero Build Step</h3>
      Clone and open <code>index.html</code> — that&rsquo;s it. No npm, no bundler, no server required. Works offline. The web as it was meant to be.
    </td>
    <td>
      <h3>🛠️ Admin Panel</h3>
      Optional Flask-based web editor with CodeMirror syntax highlighting, live preview, AJAX save, unsaved-changes warning, and template-based page creation.
    </td>
  </tr>
</table>

---

## 🗂️ Categories

<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;">

### 📘 Tutorials
Guides on Git, Python, Linux, Docker, networking, security, Minecraft, and more. [Browse →](tutorials/)

### 💻 Programming
Languages, scripting, automation, and software development references. [Browse →](programming/)

### 📎 Resources
Curated links, cheat sheets, and reference materials across topics. [Browse →](resources/)

### 🚀 Projects
Project ideas, build logs, and step-by-step construction guides. [Browse →](projects/)

### 🛠️ Tools
CLI tool guides, walkthroughs, and command references. [Browse →](tools/)

### 🔒 Security
Privacy guides, encryption tutorials, system hardening, and safe practices. [Browse →](security/)

### 🏕️ Survival
Digital survival skills, self-hosting, backup strategies, and resilience. [Browse →](survival/)

### ☠️ Piracy
Educational resource on file-sharing (with disclaimer). [Browse →](piracy/)

### 🎮 Minecraft
Server setup, commands, redstone, modding, and world management. [Browse →](minecraft/)

### 🎯 Gaming
Game servers, tweaks, and performance optimization. [Browse →](gaming/)

### 📦 SMT
SMT tool documentation and usage guides. [Browse →](smt/)

### 📋 Crib
Original reference page — the heart of the library. [View →](docs/crib.html)

</div>

---

## 🚀 Quick Start

```bash
# 1. Grab the repo
git clone https://github.com/SchooiCodes/library.git
cd library

# 2. Open it (that's literally it)
open index.html     # macOS
xdg-open index.html # Linux
start index.html    # Windows

# 3. (Optional) Fire up the admin panel for web-based editing
bash admin/run.sh
# → http://127.0.0.1:5050
# → login: admin / admin123
```

---

## 🧭 Project Structure

```
📂 library/
├── 📄 index.html               # Home page
├── 📁 assets/
│   ├── 🎨 style.css            # Full stylesheet (~1100 lines, 6 themes)
│   ├── ⚡ scripts.js           # Theme picker, dark toggle, scroll reveal, nav
│   └── ✨ favicon.svg          # SVG favicon
├── 📁 tutorials/               # 84 tutorial pages + index
├── 📁 programming/             # Programming guides & references
├── 📁 resources/               # Curated resource links
├── 📁 projects/                # Project documentation
├── 📁 tools/                   # CLI tool guides
├── 📁 security/                # Security & privacy resources
├── 📁 survival/                # Digital survival guides
├── 📁 piracy/                  # Educational file-sharing info
├── 📁 minecraft/               # Minecraft server setup & commands
├── 📁 gaming/                  # Gaming server guides
├── 📁 docs/                    # Core reference (Crib, etc.)
├── 📁 smt/                     # SMT tool documentation
├── 📁 creatives/               # Creative resources
├── 📁 opencode/                # OpenCode documentation
├── 📁 admin/                   # Web-based admin panel
│   ├── 🐍 app.py               # Flask application
│   ├── 📁 templates/           # Jinja2 templates
│   └── 🔒 config.json          # Credentials (gitignored)
└── 📄 .gitignore
```

---

## 🎨 Theme System

| Theme | Preview | Light | Dark | CSS Class |
|---|---|---|---|---|
| **Default** | ![#667eea](https://via.placeholder.com/16/667eea/667eea) ![#764ba2](https://via.placeholder.com/16/764ba2/764ba2) | ✅ | ✅ | *(default)* |
| **Ocean** | ![#0ea5e9](https://via.placeholder.com/16/0ea5e9/0ea5e9) ![#06b6d4](https://via.placeholder.com/16/06b6d4/06b6d4) | ✅ | ✅ | `body.theme-ocean` |
| **Forest** | ![#22c55e](https://via.placeholder.com/16/22c55e/22c55e) ![#16a34a](https://via.placeholder.com/16/16a34a/16a34a) | ✅ | ✅ | `body.theme-forest` |
| **Sunset** | ![#f97316](https://via.placeholder.com/16/f97316/f97316) ![#ef4444](https://via.placeholder.com/16/ef4444/ef4444) | ✅ | ✅ | `body.theme-sunset` |
| **Midnight** | ![#6366f1](https://via.placeholder.com/16/6366f1/6366f1) ![#4f46e5](https://via.placeholder.com/16/4f46e5/4f46e5) | ✅ | ✅ | `body.theme-midnight` |
| **Mono** | ![#6b7280](https://via.placeholder.com/16/6b7280/6b7280) ![#4b5563](https://via.placeholder.com/16/4b5563/4b5563) | ✅ | ✅ | `body.theme-mono` |

> 🎨 Themes are independent of dark/light mode. You can use Dark Mode + Ocean theme, or Light Mode + Midnight theme — any combination works.

---

## 🛠️ Admin Panel

The admin panel gives you a proper CMS-like experience for editing the library without touching the command line.

```
bash admin/run.sh
# → http://127.0.0.1:5050
# → admin / admin123
```

| Feature | Description |
|---|---|
| **📊 Dashboard** | Stats overview, recently edited pages, directory breakdown |
| **🔍 Sidebar** | Searchable, collapsible page tree — all 120+ pages at a glance |
| **✏️ CodeMirror Editor** | HTML syntax highlighting, line numbers, bracket matching, auto-close tags |
| **👁️ Live Preview** | Renders the page with the actual site CSS in a side-by-side view |
| **💾 AJAX Save** | Ctrl+S saves via XHR with toast notification + unsaved-changes warning |
| **📄 Create Page** | Path picker + template selector (Blank / Tutorial / Basic) |
| **🗑️ Rename/Delete** | Full page management from the UI |
| **⚙️ Settings** | Change admin credentials (logs out on update) |

---

## ⚡ Performance Notes

This site is tuned specifically for **low-end hardware** — it was tested and developed on:

<div align="center">
  <table>
    <tr>
      <th>Component</th>
      <th>Spec</th>
    </tr>
    <tr>
      <td>💻 CPU</td>
      <td>Intel Core i3-4130 (Haswell, 2C/4T, 3.4GHz)</td>
    </tr>
    <tr>
      <td>🧠 RAM</td>
      <td>8GB DDR3</td>
    </tr>
    <tr>
      <td>🎨 GPU</td>
      <td>Intel HD 4400 (integrated, no VRAM)</td>
    </tr>
    <tr>
      <td>🖥️ OS</td>
      <td>Linux Mint 22.3</td>
    </tr>
  </table>
</div>

### Optimizations

- ❌ **No `backdrop-filter: blur()`** — extremely expensive on Intel HD 4400
- 🎯 CSS transitions limited to `transform`, `opacity`, `color`, `background`, `box-shadow`
- 🐌 Scroll listeners throttled with `requestAnimationFrame` + `passive: true`
- 📄 Google Fonts uses `display=optional` to prevent layout reflow
- 🔗 Preconnect to all CDN origins (fonts.googleapis, cdnjs.cloudflare)
- 📦 No JavaScript frameworks, no build tools, no bundler

---

## 🤝 Contributing

This is a personal project, but contributions, suggestions, and bug reports are welcome:

1. [Open an issue](https://github.com/SchooiCodes/library/issues) for bugs or ideas
2. [Fork the repo](https://github.com/SchooiCodes/library/fork) and send a PR
3. Or just [star the repo](https://github.com/SchooiCodes/library/stargazers) if you find it useful ⭐

---

## 📜 License

Content is licensed under **MIT** unless otherwise noted. This project is for educational purposes.

---

<div align="center">
  <sub>
    Built with ❤️ using vanilla HTML, CSS & JS · 
    <a href="https://fontawesome.com">Font Awesome</a> · 
    <a href="https://fonts.google.com/specimen/Inter">Inter</a> · 
    <a href="https://fonts.google.com/specimen/Fira+Code">Fira Code</a>
  </sub>
  <br>
  <sub>SchooiCodes &copy; 2024-2025</sub>
</div>
