#!/usr/bin/env python3
"""Update nav and footer across all HTML files. Add Lexicon, remove merged sections."""

import os, re

BASE = "/home/user/open-code/personal_library_site_v2"

REMOVED_SECTIONS = [
    'programming/index.html',
    'projects/index.html',
    'security/index.html',
    'gaming/index.html',
    'creatives/index.html',
    'tools/index.html',
    'docs/crib.html',
]

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # Determine prefix based on depth
    rel = os.path.relpath(filepath, BASE)
    depth = rel.count(os.sep)
    prefix = '../' * depth if depth > 0 else ''

    # --- Update nav-menu ---
    nav_match = re.search(r'(<ul class="nav-menu">)(.*?)(</ul>)', content, re.DOTALL)
    if nav_match:
        open_tag, inner, close_tag = nav_match.groups()
        
        # Parse existing LIs
        li_pattern = re.compile(r'<li[^>]*>.*?</li>', re.DOTALL)
        existing_lis = li_pattern.findall(inner)
        
        new_lis = []
        has_lexicon = False
        for li in existing_lis:
            skip = False
            for section in REMOVED_SECTIONS:
                if section in li:
                    skip = True
                    break
            if skip:
                continue
            if 'lexicon/index.html' in li:
                has_lexicon = True
            new_lis.append(li)
        
        # Add Lexicon if missing (insert after Resources or Tutorials)
        if not has_lexicon:
            lexicon_li = '<li><a href="' + prefix + 'lexicon/index.html"><i class="fas fa-book-open"></i> Lexicon</a></li>'
            # Try to insert after Resources, or after Tutorials
            inserted = False
            for i, li in enumerate(new_lis):
                if 'resources/index.html' in li:
                    new_lis.insert(i + 1, lexicon_li)
                    inserted = True
                    break
            if not inserted:
                for i, li in enumerate(new_lis):
                    if 'tutorials/index.html' in li:
                        new_lis.insert(i + 1, lexicon_li)
                        inserted = True
                        break
            if not inserted:
                new_lis.append(lexicon_li)
        
        new_inner = '\n          ' + '\n          '.join(new_lis) + '\n        '
        new_nav = open_tag + new_inner + close_tag
        content = content[:nav_match.start()] + new_nav + content[nav_match.end():]

    # --- Update footer links ---
    # Find footer <div class="footer-links"> block
    footer_match = re.search(r'(<div class="footer-links">)(.*?)(</div>\s*</div>\s*<div class="footer-bottom">)', content, re.DOTALL)
    if footer_match:
        open_div, inner, rest = footer_match.groups()
        
        # Parse existing <a> tags
        a_pattern = re.compile(r'<a[^>]*>.*?</a>', re.DOTALL)
        existing_as = a_pattern.findall(inner)
        
        new_as = []
        has_lexicon = False
        for a in existing_as:
            skip = False
            for section in REMOVED_SECTIONS:
                if section in a:
                    skip = True
                    break
            if skip:
                continue
            if 'lexicon/index.html' in a:
                has_lexicon = True
            new_as.append(a)
        
        # Add Lexicon to footer if missing
        if not has_lexicon:
            lexicon_a = '<a href="' + prefix + 'lexicon/index.html">Lexicon</a>'
            # Insert before Crib or at end
            inserted = False
            for i, a in enumerate(new_as):
                if 'docs/crib.html' in a or 'crib.html' in a:
                    new_as.insert(i, lexicon_a)
                    inserted = True
                    break
            if not inserted:
                new_as.append(lexicon_a)
        
        new_inner = '\n          ' + '\n          '.join(new_as) + '\n        '
        new_footer = open_div + new_inner + rest
        content = content[:footer_match.start()] + new_footer + content[footer_match.end():]

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

count = 0
errors = []
for root, dirs, files in os.walk(BASE):
    if '.git' in root or '__pycache__' in root or '.venv' in root:
        continue
    for fname in files:
        if fname.endswith('.html'):
            path = os.path.join(root, fname)
            try:
                if update_file(path):
                    count += 1
            except Exception as e:
                errors.append(f"{os.path.relpath(path, BASE)}: {e}")

print(f"Updated {count} files")
if errors:
    print(f"Errors ({len(errors)}):")
    for e in errors[:5]:
        print(f"  {e}")
