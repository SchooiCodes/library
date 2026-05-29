#!/usr/bin/env python3
"""Shared helper functions for tutorial generation."""
import os
import html as html_mod

BASE = os.path.dirname(os.path.abspath(__file__))
TUTS = os.path.join(BASE, "tutorials")

NAV = '''     <nav class="navbar" id="navbar">
   <div class="nav-container">
    <a href="../index.html" class="nav-logo"><i class="fas fa-cube"></i> Tech Library</a>
    <ul class="nav-menu">
           <li><a href="../index.html"><i class="fas fa-home"></i> Home</a></li>
           <li><a href="../tutorials/index.html" class="active"><i class="fas fa-book"></i> Tutorials</a></li>
           <li><a href="../resources/index.html"><i class="fas fa-folder-open"></i> Resources</a></li>
           <li><a href="../lexicon/index.html"><i class="fas fa-book-open"></i> Lexicon</a></li>
           <li><a href="../survival/index.html"><i class="fas fa-life-ring"></i> Survival</a></li>
           <li><a href="../piracy/index.html"><i class="fas fa-skull"></i> Piracy</a></li>
           <li class="nav-search-item"><div class="nav-search-bar" id="search-bar"><i class="fas fa-search"></i><input type="text" id="search-bar-input" placeholder="Search tutorials, terms..." autocomplete="off"><span class="kbd-hint">\u2318K</span></div></li>
           <li><button id="theme-toggle" class="theme-toggle" aria-label="Toggle dark mode"><i class="fas fa-moon"></i></button></li>
         </ul>
    <div class="hamburger" id="hamburger">
     <span></span>
     <span></span>
     <span></span>
    </div>
   </div>
  </nav>'''

FOOTER = '''     <footer class="footer">
   <div class="container">
    <div class="footer-content">
     <div class="footer-brand">
      <h3><i class="fas fa-cube"></i> Tech Library</h3>
      <p>Free tech tutorials, tools, and resources \u2014 curated and organized.</p>
     </div>
     <div class="footer-links">
           <a href="../index.html">Home</a>
           <a href="../tutorials/index.html">Tutorials</a>
           <a href="../resources/index.html">Resources</a>
           <a href="../survival/index.html">Survival</a>
           <a href="../piracy/index.html">Piracy</a>
           <a href="../lexicon/index.html">Lexicon</a>
         </div>
    </div>
    <div class="footer-bottom"><p>&copy; 2026 Tech Library. Made with <i class="fas fa-heart" style="color:#ef4444;"></i> by <a href="https://github.com/SchooiCodes" target="_blank" style="color:rgba(255,255,255,0.7);text-decoration:underline;">SchooiCodes</a></p><div class="footer-social-inline"><a href="https://github.com/SchooiCodes" class="social-link github" target="_blank" rel="noopener" title="GitHub @SchooiCodes"><i class="fab fa-github"></i></a><span class="social-link discord" title="Discord @schooi."><i class="fab fa-discord"></i></span><a href="https://youtube.com/@SchooiYT" class="social-link youtube" target="_blank" rel="noopener" title="YouTube @SchooiYT"><i class="fab fa-youtube"></i></a></div><a href="#" class="back-to-top" aria-label="Back to top" title="Back to top"><i class="fas fa-arrow-up"></i></a></div>
   </div>
  </footer>'''


def make_page(title, filename, desc, badge, icon, sections, further):
    page_title = f"{title} \u2014 Tech Library"

    toc_items = []
    for label, sid in sections:
        toc_items.append(f'  <li><a href="#{sid}">{label}</a></li>')
    toc_html = (
        '<div class="toc" style="background:var(--code-bg);border:1px solid var(--border-color);'
        'border-radius:12px;padding:20px 24px;margin-bottom:32px;">\n'
        f' <h3 style="margin:0 0 8px 0;font-size:1.1rem;"><i class="fas fa-list"></i> Table of Contents'
        f' <span style="font-weight:400;font-size:0.85rem;color:var(--text-secondary);">'
        f'({len(sections)} sections)</span></h3>\n'
        f' <ul style="columns:2 280px;column-gap:32px;margin:8px 0 0 0;padding-left:20px;">\n'
        f'{chr(10).join(toc_items)}\n'
        f' </ul>\n'
        f'</div>'
    )

    further_html = ""
    if further:
        items = "\n".join(
            f' <li><a href="{f[2]}" target="_blank" rel="noopener"><strong>{f[0]}</strong></a> \u2014 {f[1]}</li>'
            for f in further
        )
        further_html = (
            '<hr style="margin:48px 0;border-color:var(--border-color);">\n'
            '<h2><i class="fas fa-book-open"></i> Further Reading &amp; References</h2>\n'
            '<p>Expand your knowledge with these official documentation and community resources:</p>\n'
            f'<ul>\n{items}\n</ul>\n'
            '<div class="alert alert-info" style="margin-top:16px;">\n'
            ' <i class="fas fa-info-circle alert-icon"></i>\n'
            ' <div><strong>Note:</strong> Links were current at the time of writing. Some resources may have moved \u2014 use your search engine if a link is broken.</div>\n'
            '</div>'
        )

    body_parts = []
    for label, sid in sections:
        body_parts.append(
            f'<h2 id="{sid}"><i class="{icon}"></i> {label}</h2>\n'
            f'<p>Content for this section goes here. This is a placeholder for the {label} section.</p>'
        )
    body = "\n\n".join(body_parts)

    page = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        ' <meta charset="UTF-8">\n <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f' <title>{html_mod.escape(page_title)}</title>\n'
        ' <link rel="preconnect" href="https://fonts.googleapis.com">\n'
        ' <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        ' <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Fira+Code&display=optional" rel="stylesheet">\n'
        ' <link rel="preconnect" href="https://cdnjs.cloudflare.com">\n'
        ' <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n'
        ' <link rel="stylesheet" href="../assets/style.css">\n'
        ' <link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">\n'
        '</head>\n<body>\n'
        f'{NAV}\n'
        '<div class="container" style="padding-top:100px;padding-bottom:60px;">\n'
        '<main class="main-content" style="max-width:960px;margin:0 auto;">\n'
        '<nav class="breadcrumb" aria-label="Breadcrumb">'
        '<a href="../index.html"><i class="fas fa-home"></i> Home</a>'
        '<span class="breadcrumb-sep">\u203a</span>'
        '<a href="../tutorials/index.html">Tutorials</a>'
        '<span class="breadcrumb-sep">\u203a</span>'
        f'<span>{html_mod.escape(page_title)}</span>'
        '</nav>\n'
        '<div class="section-header" style="text-align:left;margin-bottom:32px;">\n'
        f'<span class="section-badge"><i class="{icon}"></i> {badge}</span>\n'
        f'<h1 class="section-title" style="font-size:2rem;">{title}</h1>\n'
        f'<p style="color:var(--text-secondary);">{desc}</p>\n'
        f'{toc_html}\n'
        '</div>\n\n'
        f'{body}\n\n'
        f'{further_html}\n'
        '<hr style="margin:32px 0;border-color:var(--border-color);">\n'
        '<div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;align-items:center;">\n'
        '<a href="index.html" class="card-link" style="font-size:1rem;">'
        '<i class="fas fa-arrow-left"></i> Back to Tutorials</a>\n'
        '<div style="display:flex;gap:10px;">\n'
        '<a href="../index.html" class="card-link"><i class="fas fa-home"></i> Home</a>\n'
        '<a href="../resources/index.html" class="card-link"><i class="fas fa-folder-open"></i> Resources</a>\n'
        '</div>\n</div>\n'
        '</main>\n</div>\n\n'
        f'{FOOTER}\n'
        '<script src="../assets/scripts.js" defer></script>\n'
        '<script src="../assets/assistant.js" defer></script>\n'
        '</body>\n</html>'
    )
    return page


def rich_section(label, sid, icon, body):
    return (
        f'<h2 id="{sid}"><i class="{icon}"></i> {label}</h2>\n'
        f'{body}'
    )


def write_page(filename, html):
    path = os.path.join(TUTS, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Created: {filename}")


def build_page(title, filename, desc, badge, icon, sections, further):
    """Build a complete tutorial HTML page from structured data.
    
    Args:
        title: Page title
        filename: Output filename
        desc: Short description
        badge: Category badge string
        icon: Font Awesome icon class
        sections: list of (label, body_html) tuples
        further: list of (name, url, desc) tuples
    """
    sid_list = []
    rich_sections = []
    for label, body in sections:
        sid = (label.lower().replace(" ", "-").replace("&", "and")
               .replace("--", "-").replace(",", "").replace("/", "-")
               .replace("'", "").replace(".", ""))
        sid_list.append((label, sid))
        rich_sections.append(rich_section(label, sid, icon, body))

    body_content = "\n\n".join(rich_sections)
    
    toc_items = []
    for label, sid in sid_list:
        toc_items.append(f'  <li><a href="#{sid}">{label}</a></li>')
    toc_html = (
        '<div class="toc" style="background:var(--code-bg);border:1px solid var(--border-color);'
        'border-radius:12px;padding:20px 24px;margin-bottom:32px;">\n'
        f' <h3 style="margin:0 0 8px 0;font-size:1.1rem;"><i class="fas fa-list"></i> Table of Contents'
        f' <span style="font-weight:400;font-size:0.85rem;color:var(--text-secondary);">'
        f'({len(sections)} sections)</span></h3>\n'
        f' <ul style="columns:2 280px;column-gap:32px;margin:8px 0 0 0;padding-left:20px;">\n'
        f'{chr(10).join(toc_items)}\n'
        f' </ul>\n'
        f'</div>'
    )
    
    page_title = f"{title} \u2014 Tech Library"

    further_html = ""
    if further:
        items = "\n".join(
            f' <li><a href="{f[2]}" target="_blank" rel="noopener"><strong>{f[0]}</strong></a> \u2014 {f[1]}</li>'
            for f in further
        )
        further_html = (
            '<hr style="margin:48px 0;border-color:var(--border-color);">\n'
            '<h2><i class="fas fa-book-open"></i> Further Reading &amp; References</h2>\n'
            '<p>Expand your knowledge with these official documentation and community resources:</p>\n'
            f'<ul>\n{items}\n</ul>\n'
            '<div class="alert alert-info" style="margin-top:16px;">\n'
            ' <i class="fas fa-info-circle alert-icon"></i>\n'
            ' <div><strong>Note:</strong> Links were current at the time of writing. Some resources may have moved \u2014 use your search engine if a link is broken.</div>\n'
            '</div>'
        )

    page = (
        '<!DOCTYPE html>\n<html lang="en">\n<head>\n'
        ' <meta charset="UTF-8">\n <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
        f' <title>{html_mod.escape(page_title)}</title>\n'
        ' <link rel="preconnect" href="https://fonts.googleapis.com">\n'
        ' <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        ' <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Fira+Code&display=optional" rel="stylesheet">\n'
        ' <link rel="preconnect" href="https://cdnjs.cloudflare.com">\n'
        ' <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">\n'
        ' <link rel="stylesheet" href="../assets/style.css">\n'
        ' <link rel="icon" type="image/svg+xml" href="../assets/favicon.svg">\n'
        '</head>\n<body>\n'
        f'{NAV}\n'
        '<div class="container" style="padding-top:100px;padding-bottom:60px;">\n'
        '<main class="main-content" style="max-width:960px;margin:0 auto;">\n'
        '<nav class="breadcrumb" aria-label="Breadcrumb">'
        '<a href="../index.html"><i class="fas fa-home"></i> Home</a>'
        '<span class="breadcrumb-sep">\u203a</span>'
        '<a href="../tutorials/index.html">Tutorials</a>'
        '<span class="breadcrumb-sep">\u203a</span>'
        f'<span>{html_mod.escape(page_title)}</span>'
        '</nav>\n'
        '<div class="section-header" style="text-align:left;margin-bottom:32px;">\n'
        f'<span class="section-badge"><i class="{icon}"></i> {badge}</span>\n'
        f'<h1 class="section-title" style="font-size:2rem;">{title}</h1>\n'
        f'<p style="color:var(--text-secondary);">{desc}</p>\n'
        f'{toc_html}\n'
        '</div>\n\n'
        f'{body_content}\n\n'
        f'{further_html}\n'
        '<hr style="margin:32px 0;border-color:var(--border-color);">\n'
        '<div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:space-between;align-items:center;">\n'
        '<a href="index.html" class="card-link" style="font-size:1rem;">'
        '<i class="fas fa-arrow-left"></i> Back to Tutorials</a>\n'
        '<div style="display:flex;gap:10px;">\n'
        '<a href="../index.html" class="card-link"><i class="fas fa-home"></i> Home</a>\n'
        '<a href="../resources/index.html" class="card-link"><i class="fas fa-folder-open"></i> Resources</a>\n'
        '</div>\n</div>\n'
        '</main>\n</div>\n\n'
        f'{FOOTER}\n'
        '<script src="../assets/scripts.js" defer></script>\n'
        '<script src="../assets/assistant.js" defer></script>\n'
        '</body>\n</html>'
    )
    write_page(filename, page)
