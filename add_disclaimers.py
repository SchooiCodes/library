#!/usr/bin/env python3
"""Add safety/legal disclaimer banners to piracy-related pages."""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

DISCLAIMER = '''<div class="alert alert-danger" style="margin-bottom:24px;border-left:4px solid #dc2626;background:var(--code-bg);border-radius:8px;padding:16px 20px;">
 <h4 style="margin:0 0 8px 0;color:#dc2626;font-size:1rem;"><i class="fas fa-exclamation-triangle"></i> Legal &amp; Safety Disclaimer</h4>
 <p style="margin:0;font-size:0.9rem;">This content is provided for <strong>educational purposes only</strong>. Accessing or distributing copyrighted material without permission may violate laws in your jurisdiction. You are solely responsible for complying with all applicable laws. Using unlicensed software or media obtained through unauthorized channels carries security risks including malware infection. <strong>Proceed at your own risk.</strong></p>
</div>'''

def has_existing_disclaimer(content):
    """Check if content already has a disclaimer within the main content area."""
    patterns = [
        r'Legal.*Disclaimer',
        r'SAFETY.*WARNING',
        r'educational purposes.*only',
        r'IMPORTANT SAFETY',
    ]
    for p in patterns:
        if re.search(p, content, re.IGNORECASE):
            return True
    return False

def remove_wrongly_placed_disclaimers(content):
    """Remove disclaimer blocks that were placed before <div class='container'>."""
    # Pattern matches the disclaimer block followed by whitespace before <div class="container"
    pattern = re.compile(
        r'<div class="alert alert-danger"[^>]*>.*?Legal &amp; Safety Disclaimer.*?</div>\s*\n',
        re.DOTALL
    )
    # Only remove if followed by <div class="container" (means it's outside)
    cleaned = pattern.sub('', content)
    if cleaned != content:
        print("    Removed wrongly placed disclaimer")
    return cleaned

def add_disclaimer(filepath):
    """Add disclaimer banner after the breadcrumb nav."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove any wrongly placed disclaimers first
    content = remove_wrongly_placed_disclaimers(content)
    
    # Insert after breadcrumb </nav> and before <div class="section-header"> or <h1
    # Match the breadcrumb nav element specifically
    pattern = r'(class="breadcrumb[^>]*>.*?</nav>\s*\n)(\s*<(?:div|h1))'
    
    new_content = re.sub(pattern, r'\1' + DISCLAIMER + '\n' + r'\2', content, count=1, flags=re.DOTALL)
    
    if new_content == content:
        print(f"  FAIL (no breadcrumb pattern found): {os.path.relpath(filepath, BASE)}")
        return False
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"  ADDED: {os.path.relpath(filepath, BASE)}")
    return True

def main():
    count = 0
    
    # All piracy pages
    piracy_dir = os.path.join(BASE, 'piracy')
    for fname in sorted(os.listdir(piracy_dir)):
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(piracy_dir, fname)
        if add_disclaimer(fpath):
            count += 1
    
    # Tutorial pages that need disclaimers
    tutorial_targets = [
        'tutorials/repacking-guide.html',
        'tutorials/smt-multitool.html',
    ]
    for relpath in tutorial_targets:
        fpath = os.path.join(BASE, relpath)
        if add_disclaimer(fpath):
            count += 1
    
    print(f"\n=== Added disclaimers to {count} pages ===")

if __name__ == '__main__':
    main()
