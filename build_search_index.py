#!/usr/bin/env python3
"""Build search-index.json from all HTML pages."""
import os, re, json

BASE = os.path.dirname(os.path.abspath(__file__))
EXCLUDE_DIRS = {'.git', 'admin', 'opencode'}
EXCLUDE_FILES = {'index.html'}

pages = []
for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        rel = os.path.relpath(fpath, BASE)

        with open(fpath, encoding='utf-8', errors='ignore') as f:
            content = f.read()

        # Skip listing/index pages for tutorials/resources (they're navigational)
        skip_indexes = {'tutorials/index.html', 'resources/index.html', 'survival/index.html',
                        'piracy/index.html', 'lexicon/index.html'}
        if rel in skip_indexes:
            continue

        # Extract title
        title_m = re.search(r'<title>(.*?)</title>', content, re.DOTALL)
        if not title_m:
            continue
        title = title_m.group(1).strip()
        title = re.sub(r'\s*—\s*Tech Library.*$', '', title).strip()
        if not title:
            continue

        # Extract description: first <p> after <main> or first meta description
        desc = ''
        desc_m = re.search(r'<meta\s+name="description"\s+content="([^"]+)"', content)
        if desc_m:
            desc = desc_m.group(1)
        else:
            # Get first meaningful paragraph
            p_m = re.search(r'<p[^>]*>(.*?)</p>', content, re.DOTALL)
            if p_m:
                desc = re.sub(r'<[^>]+>', '', p_m.group(1)).strip()
                desc = desc[:200]

        # Category from directory
        parts = rel.split(os.sep)
        cat = parts[0] if len(parts) > 1 else 'home'

        pages.append({
            'title': title,
            'url': '/' + rel,
            'desc': desc[:300],
            'cat': cat
        })

# Also add listing pages with explicit descriptions
listing_pages = {
    'tutorials/index.html': ('All Tutorials', 'Browse 100+ step-by-step tech tutorials covering Windows, Linux, programming, networking, and more.'),
    'resources/index.html': ('Resources', 'Curated collections of browser extensions, free media alternatives, learning platforms, design tools, and more.'),
    'survival/index.html': ('Survival Kit', 'Emergency digital resources — offline tools, data recovery, system rescue, security breach response, and essential bookmarks.'),
    'piracy/index.html': ('Piracy Resources', 'Sites, tools, and guides for streaming, downloading, torrenting, gaming, and more — organized and updated.'),
    'lexicon/index.html': ('Tech Lexicon', '156+ tech terms defined — programming, security, networking, Linux, hardware, gaming, and general tech.'),
}
for rel, (title, desc) in listing_pages.items():
    fpath = os.path.join(BASE, rel)
    if os.path.exists(fpath):
        parts = rel.split(os.sep)
        cat = parts[0] if len(parts) > 1 else 'home'
        pages.append({
            'title': title,
            'url': '/' + rel,
            'desc': desc,
            'cat': cat
        })

# Sort by category then title
pages.sort(key=lambda p: (p['cat'], p['title']))

out = os.path.join(BASE, 'search-index.json')
with open(out, 'w', encoding='utf-8') as f:
    json.dump(pages, f, indent=2, ensure_ascii=False)

print(f"Search index built: {len(pages)} pages → {out}")
