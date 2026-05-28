#!/usr/bin/env python3
"""Unified build system for Tech Library — generates search index, stats, embedded data, and more."""
import os, re, json, html as html_mod, datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
EXCLUDE_DIRS = {'.git', 'admin', 'opencode', '__pycache__', '.venv'}
EXCLUDE_FILES = {'index.html'}

def get_all_html_files():
    files = []
    for f in sorted(BASE.rglob("*.html")):
        rel = f.relative_to(BASE)
        parts = rel.parts
        if any(p in EXCLUDE_DIRS for p in parts):
            continue
        files.append(f)
    return files

def count_tutorials():
    """Count actual tutorial content pages (not index pages)."""
    count = 0
    for f in sorted(BASE.rglob("*.html")):
        rel = str(f.relative_to(BASE))
        if '/index.html' in rel and rel != 'index.html':
            continue
        if rel.startswith('tutorials/') and not rel.endswith('index.html'):
            count += 1
    return count

def count_lexicon_entries():
    """Count lexicon terms from scripts.js."""
    scripts_js = BASE / "assets" / "scripts.js"
    if not scripts_js.exists():
        return 0
    content = scripts_js.read_text(encoding='utf-8')
    # Find the LEXICON object and count keys
    m = re.search(r'var LEXICON\s*=\s*\{(.*?)\};', content, re.DOTALL)
    if m:
        # Count lines that have a quoted key (lexicon entry)
        entries = re.findall(r'"[^"]+"\s*:', m.group(1))
        return len(entries)
    return 0

def count_category_pages():
    """Count pages per category directory."""
    counts = {}
    for f in sorted(BASE.rglob("*.html")):
        rel = str(f.relative_to(BASE))
        if rel.startswith('admin/') or '/index.html' in rel:
            continue
        parts = rel.split(os.sep)
        if len(parts) > 1:
            cat = parts[0]
            counts[cat] = counts.get(cat, 0) + 1
    return counts

def build_search_index():
    """Build search-index.json from all HTML pages."""
    pages = []
    for fpath in get_all_html_files():
        rel = str(fpath.relative_to(BASE))
        skip_indexes = {'tutorials/index.html', 'resources/index.html', 'survival/index.html',
                        'piracy/index.html', 'lexicon/index.html'}
        if rel in skip_indexes:
            continue

        content = fpath.read_text(encoding='utf-8', errors='ignore')

        title_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
        if not title_m:
            continue
        title = title_m.group(1).strip()
        title = re.sub(r'\s*—\s*Tech Library.*$', '', title).strip()
        if not title:
            continue

        desc = ''
        desc_m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', content)
        if desc_m:
            desc = desc_m.group(1)
        else:
            p_m = re.search(r'<p[^>]*>(.*?)</p>', content, re.DOTALL)
            if p_m:
                desc = re.sub(r'<[^>]+>', '', p_m.group(1)).strip()[:200]

        parts = rel.split(os.sep)
        cat = parts[0] if len(parts) > 1 else 'home'

        # Popularity heuristic
        if rel == 'index.html':
            pop = 100
        elif rel.endswith('/index.html'):
            pop = 90
        elif rel.count(os.sep) <= 1:
            pop = 70
        else:
            pop = 50

        try:
            mtime = os.path.getmtime(fpath)
            date = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
        except OSError:
            date = '2025-01-01'

        pages.append({
            'title': title,
            'url': '/' + rel,
            'desc': desc[:300],
            'cat': cat,
            'popularity': pop,
            'date': date
        })

    listing_pages = {
        'tutorials/index.html': ('All Tutorials', 'Browse step-by-step tech tutorials covering Windows, Linux, programming, networking, and more.'),
        'resources/index.html': ('Resources', 'Curated collections of browser extensions, free media alternatives, learning platforms, design tools, and more.'),
        'survival/index.html': ('Survival Kit', 'Emergency digital resources — offline tools, data recovery, system rescue, security breach response, and essential bookmarks.'),
        'piracy/index.html': ('Piracy Resources', 'Sites, tools, and guides for streaming, downloading, torrenting, gaming, and more — organized and updated.'),
        'lexicon/index.html': ('Tech Lexicon', f'{count_lexicon_entries()}+ tech terms defined — programming, security, networking, Linux, hardware, gaming, and general tech.'),
    }
    for rel, (title, desc) in listing_pages.items():
        fpath = BASE / rel
        if fpath.exists():
            parts = rel.split(os.sep)
            cat = parts[0] if len(parts) > 1 else 'home'
            pages.append({
                'title': title,
                'url': '/' + rel,
                'desc': desc,
                'cat': cat,
                'popularity': 90,
                'date': '2025-01-01'
            })

    pages.sort(key=lambda p: (p['cat'], p['title']))

    out = BASE / 'search-index.json'
    out.write_text(json.dumps(pages, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"  search-index.json: {len(pages)} pages")
    return pages

def embed_search_index(scripts_js_path, pages):
    """Embed the search index into scripts.js for file:// compatibility."""
    content = scripts_js_path.read_text(encoding='utf-8')
    embedded = json.dumps(pages)
    marker = 'var EMBEDDED_INDEX = '
    start = content.find(marker)
    if start == -1:
        print(f"  ERROR: EMBEDDED_INDEX marker not found in scripts.js")
        return
    # Find ]; which terminates the array — avoids matching ; inside HTML entities
    end = content.find('];', start)
    if end == -1:
        print(f"  ERROR: end of EMBEDDED_INDEX array not found")
        return
    end += 1  # include the ]
    content = content[:start] + marker + embedded + ';' + content[end+1:]
    scripts_js_path.write_text(content, encoding='utf-8')
    print(f"  scripts.js: embedded {len(pages)} search entries")

def update_landing_stats(index_html_path, tutorial_count, lexicon_count, category_counts):
    """Update hardcoded stats on the landing page."""
    content = index_html_path.read_text(encoding='utf-8')
    original = content

    total_pages = sum(category_counts.values()) + 1  # +1 for home
    categories = len(category_counts)

    # Update hero stats
    content = re.sub(
        r'<span class="stat-number">\d+\+</span><span class="stat-label">Guides & Tutorials</span>',
        f'<span class="stat-number">{tutorial_count}+</span><span class="stat-label">Guides & Tutorials</span>',
        content
    )
    content = re.sub(
        r'<span class="stat-number">\d+</span><span class="stat-label">Categories</span>',
        f'<span class="stat-number">{categories}</span><span class="stat-label">Categories</span>',
        content
    )

    # Update "100+ Tutorials" in the free section
    content = re.sub(
        r'<h3>\d+\+ Tutorials</h3>',
        f'<h3>{tutorial_count}+ Tutorials</h3>',
        content
    )

    # Update lexicon card count
    content = re.sub(
        r'\d+\+ tech terms defined',
        f'{lexicon_count}+ tech terms defined',
        content
    )

    # Update lexicon page description
    lexicon_html = BASE / 'lexicon' / 'index.html'
    if lexicon_html.exists():
        lc = lexicon_html.read_text(encoding='utf-8')
        lc = re.sub(
            r'\d+\+ tech (slang )?terms',
            f'{lexicon_count}+ tech terms',
            lc
        )
        lexicon_html.write_text(lc, encoding='utf-8')

    # Update search-index.json hardcoded description for lexicon
    search_index = BASE / 'search-index.json'
    if search_index.exists():
        si_content = search_index.read_text(encoding='utf-8')
        si_content = re.sub(
            r'\d+\+ tech terms defined',
            f'{lexicon_count}+ tech terms defined',
            si_content
        )
        search_index.write_text(si_content, encoding='utf-8')

    if content != original:
        index_html_path.write_text(content, encoding='utf-8')
        print(f"  index.html: stats updated ({tutorial_count}+ tutorials, {lexicon_count}+ lexicon, {categories} categories)")
        return True
    return False

def update_nav_all():
    """Run update_nav.py to sync navigation."""
    nav_script = BASE / 'update_nav.py'
    if nav_script.exists():
        import subprocess
        result = subprocess.run(['python3', str(nav_script)], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"  nav: {result.stdout.strip()}")
        else:
            print(f"  nav error: {result.stderr.strip()}")

SEARCH_BAR_HTML = (
    '<li class="nav-search-item"><div class="nav-search-bar" id="search-bar">'
    '<i class="fas fa-search"></i>'
    '<input type="text" id="search-bar-input" placeholder="Search tutorials, terms..." autocomplete="off">'
    '<span class="kbd-hint">\u2318K</span></div></li>'
)

def propagate_search_bar():
    """Replace old search toggle button with inline search bar across all HTML files."""
    old_pattern = re.compile(
        r'<li><button\s+id="search-toggle"[^>]*><i\s+class="fas\s+fa-search"></i></button></li>'
    )
    count = 0
    for f in sorted(BASE.rglob("*.html")):
        if "admin" in str(f) or ".git" in str(f):
            continue
        content = f.read_text(encoding='utf-8')
        new_content, n = old_pattern.subn(SEARCH_BAR_HTML, content)
        if n > 0 and new_content != content:
            f.write_text(new_content, encoding='utf-8')
            count += 1
    print(f"  search bar: Updated {count} files")

BREADCRUMB_SECTIONS = {
    'tutorials': 'Tutorials',
    'survival': 'Survival Kit',
    'docs': 'Documentation',
    'piracy': 'Piracy',
    'smt': 'SMT',
    'resources': 'Resources',
    'programming': 'Programming',
    'security': 'Security',
    'gaming': 'Gaming',
    'creatives': 'Creatives',
    'tools': 'Tools',
    'projects': 'Projects',
    'minecraft': 'Minecraft',
    'lexicon': 'Lexicon',
    'buying-guide': 'Buyer\'s Guide',
}

def section_label(section):
    return BREADCRUMB_SECTIONS.get(section, section.capitalize())

def inject_breadcrumbs():
    """Inject breadcrumb nav before the first <h1> in content pages."""
    SECTIONS = set(BREADCRUMB_SECTIONS.keys())
    count = 0
    for f in sorted(BASE.rglob("*.html")):
        rel = str(f.relative_to(BASE))
        parts = rel.split(os.sep)
        section = parts[0]
        if section not in SECTIONS:
            continue
        if rel == 'index.html' or rel.endswith('/index.html'):
            continue
        if 'admin' in rel or '.git' in rel:
            continue
        content = f.read_text(encoding='utf-8')
        if 'class="breadcrumb"' in content:
            continue

        depth = len(parts) - 1
        prefix = '../' * depth if depth > 0 else ''
        title_m = re.search(r'<title>(.*?)</title>', content)
        page_title = title_m.group(1).strip() if title_m else ''

        # Determine section index path
        section_path = prefix + section + '/index.html'

        breadcrumb = (
            '<nav class="breadcrumb" aria-label="Breadcrumb">'
            '<a href="' + prefix + 'index.html"><i class="fas fa-home"></i> Home</a>'
            '<span class="breadcrumb-sep">›</span>'
            '<a href="' + section_path + '">' + section_label(section) + '</a>'
            '<span class="breadcrumb-sep">›</span>'
            '<span>' + html_mod.escape(page_title) + '</span>'
            '</nav>'
        )

        new_content = re.sub(
            r'(<main[^>]*>\s*)',
            r'\1' + breadcrumb + '\n',
            content, count=1
        )
        if new_content != content:
            f.write_text(new_content, encoding='utf-8')
            count += 1
    print(f"  breadcrumbs: Injected into {count} files")

FOOTER_BOTTOM_HTML = (
    '<div class="footer-bottom">'
    '<p>&copy; 2026 Tech Library. Made with <i class="fas fa-heart" style="color:#ef4444;"></i> by '
    '<a href="https://github.com/SchooiCodes" target="_blank" style="color:rgba(255,255,255,0.7);text-decoration:underline;">SchooiCodes</a></p>'
    '<div class="footer-social-inline">'
    '<a href="https://github.com/SchooiCodes" class="social-link github" target="_blank" rel="noopener" title="GitHub @SchooiCodes">'
    '<i class="fab fa-github"></i></a>'
    '<span class="social-link discord" title="Discord @schooi."><i class="fab fa-discord"></i></span>'
    '<a href="https://youtube.com/@SchooiYT" class="social-link youtube" target="_blank" rel="noopener" title="YouTube @SchooiYT">'
    '<i class="fab fa-youtube"></i></a>'
    '</div>'
    '<a href="#" class="back-to-top" aria-label="Back to top" title="Back to top"><i class="fas fa-arrow-up"></i></a>'
    '</div>'
)

def propagate_footer():
    """Replace footer-bottom content with social links and back-to-top across all HTML files."""
    old_pattern = re.compile(
        r'<div class="footer-bottom">.*?</div>(?=\s*</div>\s*</footer>)',
        re.DOTALL
    )
    count = 0
    for f in sorted(BASE.rglob("*.html")):
        if "admin" in str(f) or ".git" in str(f):
            continue
        content = f.read_text(encoding='utf-8')
        new_content, n = old_pattern.subn(FOOTER_BOTTOM_HTML, content)
        if n > 0 and new_content != content:
            f.write_text(new_content, encoding='utf-8')
            count += 1
    print(f"  footer: Updated {count} files")

def inject_assistant():
    """Add assistant.js script tag before </body> on all HTML pages."""
    count = 0
    for f in sorted(BASE.rglob("*.html")):
        rel = str(f.relative_to(BASE))
        if "admin" in rel or ".git" in rel:
            continue
        content = f.read_text(encoding='utf-8')
        if 'assistant.js' in content:
            continue
        depth = rel.count(os.sep)
        prefix = '../' * depth if depth > 0 else ''
        script_tag = '<script src="' + prefix + 'assets/assistant.js" defer></script>\n</body>'
        new_content, n = re.subn(
            r'(<script src="[^"]*scripts\.js"[^>]*>.*?</script>)\s*</body>',
            r'\1\n' + script_tag,
            content, count=1
        )
        if n > 0:
            f.write_text(new_content, encoding='utf-8')
            count += 1
    print(f"  assistant: Injected into {count} files")

def run():
    print("=== Tech Library Build System ===")
    
    print("\n[1/9] Counting...")
    tut_count = count_tutorials()
    lex_count = count_lexicon_entries()
    cat_counts = count_category_pages()
    total = sum(cat_counts.values()) + 1
    print(f"  Tutorials: {tut_count}+")
    print(f"  Lexicon entries: {lex_count}+")
    print(f"  Categories: {len(cat_counts)}")
    print(f"  Total pages: {total}")
    
    print("\n[2/9] Building search index...")
    pages = build_search_index()
    
    print("\n[3/9] Embedding search index into scripts.js...")
    scripts_js = BASE / 'assets' / 'scripts.js'
    if scripts_js.exists():
        embed_search_index(scripts_js, pages)
    
    print("\n[4/9] Updating landing page stats...")
    index_html = BASE / 'index.html'
    if index_html.exists():
        update_landing_stats(index_html, tut_count, lex_count, cat_counts)
    
    print("\n[5/9] Propagating search bar...")
    propagate_search_bar()
    
    print("\n[6/9] Injecting breadcrumbs...")
    inject_breadcrumbs()
    
    print("\n[7/9] Updating footer...")
    propagate_footer()
    
    print("\n[8/9] Syncing navigation...")
    update_nav_all()
    
    print("\n[9/9] Injecting assistant script...")
    inject_assistant()
    
    print("\n=== Build complete ===")

if __name__ == '__main__':
    import subprocess
    run()
