#!/usr/bin/env python3
"""Remove the added disclaimer banners from all sub-pages, keep only on piracy/index.html."""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

# The exact disclaimer block we added
DISCLAIMER_PATTERN = re.compile(
    r'<div class="alert alert-danger" style="margin-bottom:24px;border-left:4px solid #dc2626;background:var\(--code-bg\);border-radius:8px;padding:16px 20px;">\s*'
    r'<h4 style="margin:0 0 8px 0;color:#dc2626;font-size:1rem;"><i class="fas fa-exclamation-triangle"></i> Legal &amp; Safety Disclaimer</h4>\s*'
    r'<p style="margin:0;font-size:0.9rem;">This content is provided for <strong>educational purposes only</strong>.*?</p>\s*'
    r'</div>\s*',
    re.DOTALL
)

# Also remove the outer version (placed before container)
OUTER_DISCLAIMER = re.compile(
    r'<div class="alert alert-danger" style="margin-bottom:0;border-left:4px solid #dc2626;background:var\(--code-bg\);border-radius:8px;padding:16px 20px;margin:16px 24px 0 24px;">\s*'
    r'<h4 style="margin:0 0 8px 0;color:#dc2626;font-size:1rem;"><i class="fas fa-exclamation-triangle"></i> Legal &amp; Safety Disclaimer</h4>\s*'
    r'<p style="margin:0;font-size:0.9rem;">.*?</p>\s*'
    r'</div>\s*',
    re.DOTALL
)

TARGETS = []

# All piracy pages except index.html
piracy_dir = os.path.join(BASE, 'piracy')
for fname in os.listdir(piracy_dir):
    if not fname.endswith('.html') or fname == 'index.html':
        continue
    TARGETS.append(os.path.join(piracy_dir, fname))

# Tutorial pages that got the banner
TARGETS.append(os.path.join(BASE, 'tutorials', 'smt-multitool.html'))
TARGETS.append(os.path.join(BASE, 'tutorials', 'repacking-guide.html'))
# Also office activation guide (has the outer-style banner)
TARGETS.append(os.path.join(BASE, 'piracy', 'office-activation-guide.html'))

count = 0
for fpath in TARGETS:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    content = DISCLAIMER_PATTERN.sub('', content)
    content = OUTER_DISCLAIMER.sub('', content)
    
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  REMOVED: {os.path.relpath(fpath, BASE)}")
        count += 1
    else:
        print(f"  SKIP (no disclaimer found): {os.path.relpath(fpath, BASE)}")

print(f"\n=== Removed disclaimers from {count} pages ===")
