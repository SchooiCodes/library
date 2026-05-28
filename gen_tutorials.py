#!/usr/bin/env python3
"""Generate 60 new tutorial pages for Tech Library."""
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
    """Return a fully-written h2 section with body content."""
    return (
        f'<h2 id="{sid}"><i class="{icon}"></i> {label}</h2>\n'
        f'{body}'
    )


def write_page(filename, html):
    path = os.path.join(TUTS, filename)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  Created: {filename}")


# ======================================================================
# 60 tutorial definitions
# ======================================================================

def generate_all():

    # 1. Active Recall & Spaced Repetition
    sections = [
        rich_section("What is Active Recall?", "what-is-active-recall", "fas fa-question-circle",
            '<p><strong>Active Recall</strong> is a learning technique where you actively retrieve information from memory rather than passively reviewing it. Instead of re-reading notes or highlighting textbooks, you quiz yourself on the material.</p>'
            '<p>Research by <strong>Roediger &amp; Karpicke (2006)</strong> shows that active recall produces significantly better long-term retention compared to passive study methods.</p>'
            '<p><strong>Key principles:</strong></p><ul><li>Retrieval strengthens neural pathways</li><li>Forgetting is part of learning \u2014 the struggle to recall is what builds memory</li><li>Testing yourself is more effective than re-reading</li></ul>'),
        rich_section("What is Spaced Repetition?", "what-is-spaced-repetition", "fas fa-clock",
            '<p><strong>Spaced Repetition</strong> is a technique that schedules review sessions at increasing intervals based on when you are about to forget. It exploits the <strong>spacing effect</strong> \u2014 the finding that spaced-out learning is more effective than cramming.</p>'
            '<p><strong>How it works:</strong></p><ul><li>Review material just before you would forget it</li><li>Each successful recall increases the interval before the next review</li><li>Failed recalls reset the interval to a shorter duration</li></ul>'
            '<p>Spaced repetition software (SRS) like Anki automates this scheduling with algorithms based on <strong>SuperMemo SM-2</strong>.</p>'),
        rich_section("Anki Setup & Workflow", "anki-setup", "fas fa-cog",
            '<p><strong>Anki</strong> is the most popular spaced repetition app. It is free on desktop and Android, with a paid iOS version.</p>'
            '<p><strong>Installation:</strong></p><pre><code># Linux (apt)\nsudo apt install anki\n\n# macOS\nbrew install --cask anki\n\n# Windows: Download from https://apps.ankiweb.net\n\n# Or use AnkiWeb (sync across devices)\nhttps://ankiweb.net</code></pre>'
            '<p><strong>Basic workflow:</strong></p><ol><li>Create a deck for your subject</li><li>Make cards with a question on the front, answer on the back</li><li>Review daily \u2014 Anki shows due cards</li><li>Rate each card: Again (1 min), Hard (10 min), Good (1 day), Easy (4 days)</li></ol>'
            '<p><strong>Tips:</strong></p><ul><li>Keep cards atomic \u2014 one fact per card</li><li>Use images, cloze deletions, and mnemonics</li><li>Add tags to organize cards by topic</li></ul>'),
        rich_section("Effective Study Workflow", "study-workflow", "fas fa-tasks",
            '<p>Combine active recall and spaced repetition into a powerful workflow:</p><ol>'
            '<li><strong>Preview</strong> \u2014 Skim the material to get an overview (5 min)</li>'
            '<li><strong>Read actively</strong> \u2014 Take notes in your own words, create questions</li>'
            '<li><strong>Make cards</strong> \u2014 Create Anki cards from your notes immediately</li>'
            '<li><strong>Review daily</strong> \u2014 Do your Anki reviews every day (15-30 min)</li>'
            '<li><strong>Practice problems</strong> \u2014 Apply knowledge with exercises</li>'
            '<li><strong>Teach others</strong> \u2014 Explain concepts to someone else (Feynman technique)</li>'
            '</ol><p>This <strong>Active Recall + Spaced Repetition + Interleaving</strong> combo is the gold standard for efficient learning.</p>'),
        rich_section("Pomodoro Technique Integration", "pomodoro", "fas fa-hourglass",
            '<p>The <strong>Pomodoro Technique</strong> pairs perfectly with study sessions:</p>'
            '<ul><li>25 minutes of focused study (create or review cards)</li><li>5-minute break (stretch, hydrate, rest eyes)</li>'
            '<li>After 4 pomodoros, take a longer break (15-30 min)</li></ul>'
            '<p><strong>Recommended apps:</strong></p><ul><li><strong>Forest</strong> \u2014 Gamified focus timer</li>'
            '<li><strong>Focusmate</strong> \u2014 Virtual co-working accountability</li>'
            '<li><strong>TomatoTimer</strong> \u2014 Simple browser-based timer</li></ul>'),
    ]
    write_page("active-recall.html", make_page(
        "Active Recall & Spaced Repetition", "active-recall.html",
        "Learn how to study smarter with evidence-based techniques that boost long-term retention.", "Study Skills", "fas fa-brain",
        [("What is Active Recall?", "what-is-active-recall"), ("What is Spaced Repetition?", "what-is-spaced-repetition"),
         ("Anki Setup & Workflow", "anki-setup"), ("Effective Study Workflow", "study-workflow"), ("Pomodoro Technique Integration", "pomodoro")],
        [("Anki Documentation", "https://docs.ankiweb.net/", "Official Anki manual"),
         ("SM-2 Algorithm", "https://www.supermemo.com/en/archives1990-2015/english/ol/sm2", "Original spaced repetition algorithm"),
         ("Ali Abdaal on Active Recall", "https://aliabdaal.com/active-recall/", "Practical active recall guide")]
    ))

    # 2-60: Similar pattern. Let me generate placeholders first then fill them.
    placeholders = [
        # Study & Productivity (5 more)
        ("note-taking-methods.html", "Note-Taking Methods for Students", "Compare the best note-taking systems for different learning styles.", "Study Skills", "fas fa-pen",
         ["Cornell Method", "Zettelkasten (Slip Box)", "Outline Method", "Mind Mapping", "Digital Note-Taking Tools"]),
        ("focus-productivity-tools.html", "Focus & Productivity Tools Guide", "Eliminate distractions and get more done with the best productivity tools.", "Productivity", "fas fa-rocket",
         ["Time Management Methods", "Distraction Blocking Tools", "Focus & Deep Work Apps", "Habit Tracking", "Distraction-Free Writing"]),
        ("anki-customization.html", "Anki Customization & Advanced Features", "Supercharge Anki with add-ons, card styling, FSRS scheduler, and sync.", "Study Skills", "fas fa-wrench",
         ["Add-ons & Plugins", "Card Styling with CSS", "FSRS Scheduler", "Sync & Collaboration", "Statistics & Review"]),
        ("digital-zettelkasten.html", "Digital Zettelkasten with Obsidian", "Build a networked knowledge base using Zettelkasten principles in Obsidian.", "Study Skills", "fas fa-boxes",
         ["Setting Up Obsidian", "Atomic Notes", "Links & Graph View", "Templates & Plugins", "Daily Notes Workflow"]),
        ("time-management-guide.html", "Time Management Guide for Students", "Master your schedule with proven time management techniques.", "Study Skills", "fas fa-calendar-alt",
         ["Eisenhower Matrix", "Time Blocking", "GTD Method", "Weekly Reviews", "Digital Calendars"]),

        # Programming (8 more)
        ("rust-basics.html", "Rust Programming Basics", "Learn Rust from scratch \u2014 ownership, borrowing, structs, enums, and error handling.", "Programming", "fab fa-rust",
         ["What is Rust?", "Installation", "Ownership & Borrowing", "Structs, Enums & Pattern Matching", "Error Handling with Result"]),
        ("go-basics.html", "Go Programming Basics", "Learn Go from scratch \u2014 goroutines, channels, interfaces, and CLI tools.", "Programming", "fab fa-golang",
         ["What is Go?", "Installation & Hello World", "Basic Syntax & Types", "Goroutines & Channels", "Interfaces"]),
        ("cpp-basics.html", "C++ Programming for Beginners", "Learn C++ \u2014 pointers, classes, STL, and modern C++ features.", "Programming", "fas fa-code",
         ["What is C++?", "Setup & First Program", "Pointers & Memory", "Classes & OOP", "STL & Modern C++"]),
        ("sql-advanced.html", "Advanced SQL Queries & Optimization", "Master window functions, CTEs, indexing, and query performance tuning.", "Databases", "fas fa-database",
         ["Window Functions", "Common Table Expressions", "Indexing Strategies", "Query Optimization", "Advanced Joins"]),
        ("api-design-best-practices.html", "API Design Best Practices", "Design robust RESTful and GraphQL APIs with proper status codes and auth.", "API Design", "fas fa-plug",
         ["RESTful Design Principles", "HTTP Status Codes", "API Versioning", "Authentication & Authorization", "Rate Limiting", "API Documentation"]),
        ("websockets-guide.html", "WebSockets & Real-Time Communication", "Build real-time apps with WebSockets, Socket.IO, and WebRTC.", "Networking", "fas fa-comments",
         ["What are WebSockets?", "WebSocket API (Browser)", "WebSocket Server (Node.js)", "Socket.IO", "WebRTC"]),
        ("testing-101.html", "Software Testing 101", "Master unit, integration, and E2E testing with pytest, Vitest, and Playwright.", "Testing", "fas fa-vial",
         ["The Testing Pyramid", "Unit Testing", "Mocking & Stubs", "Integration Testing", "E2E Testing", "CI/CD Integration"]),
        ("ci-cd-jenkins.html", "CI/CD with Jenkins Pipeline", "Set up Jenkins for continuous integration and delivery.", "DevOps", "fab fa-jenkins",
         ["Jenkins Overview", "Installation", "Declarative Pipeline", "Distributed Builds", "Essential Plugins"]),

        # Linux/DevOps (7 more)
        ("nginx-reverse-proxy.html", "Nginx Reverse Proxy & Load Balancing", "Configure Nginx as a reverse proxy, load balancer, and TLS terminator.", "DevOps", "fas fa-server",
         ["What is a Reverse Proxy?", "Basic Reverse Proxy Setup", "Load Balancing Methods", "TLS Termination", "Caching Static Content"]),
        ("terraform-basics.html", "Terraform Infrastructure as Code", "Learn Terraform \u2014 HCL, providers, state management, modules, and workspaces.", "DevOps", "fas fa-cloud",
         ["What is Terraform?", "HCL Syntax & Resources", "State Management", "Modules", "Workspaces"]),
        ("kubernetes-pods-services-deployments.html", "Kubernetes: Pods, Services & Deployments", "Deep dive into core Kubernetes objects with practical YAML examples.", "DevOps", "fas fa-ship",
         ["Core Kubernetes Objects", "Pods", "Deployments", "Services", "Ingress Controller", "ConfigMaps & Secrets"]),
        ("ansible-playbooks-deep-dive.html", "Ansible Playbooks Deep Dive", "Advanced playbook patterns, dynamic inventory, collections, and AWX.", "DevOps", "fas fa-cogs",
         ["Advanced Playbook Patterns", "Dynamic Inventory", "Ansible Collections", "AWX / Ansible Tower", "Performance Optimization"]),
        ("linux-process-management.html", "Linux Process Management with systemd", "Master ps, htop, systemd, cgroups, nice values, and troubleshooting.", "Linux", "fas fa-microchip",
         ["Process Basics", "Process Signals", "Priority & Nice Values", "Managing Services with systemd", "Cgroups", "Troubleshooting High Usage"]),
        ("linux-security-hardening.html", "Linux Security Hardening", "Secure Linux with SELinux, AppArmor, auditd, kernel hardening, and monitoring.", "Security", "fas fa-shield-alt",
         ["Basic Hardening Steps", "SELinux", "AppArmor", "System Auditing (auditd)", "Kernel Hardening (sysctl)", "File Integrity Monitoring"]),
        ("linux-disk-management.html", "Linux Disk Management: LVM, RAID & Filesystems", "Manage storage with partitioning, LVM, software RAID, and filesystem tools.", "Linux", "fas fa-hdd",
         ["Disk Partitioning", "Filesystem Creation", "LVM", "Software RAID (mdadm)", "Disk Monitoring"]),

        # Windows (5)
        ("windows-registry-hacks.html", "Windows Registry Hacks & Tweaks", "Advanced registry tricks for performance, UI, security, and automation.", "Windows", "fas fa-database",
         ["Registry Basics", "Performance Tweaks", "UI Customization", "Security & Privacy Hacks", "Creating .reg Files"]),
        ("wsl2-guide.html", "WSL2 Complete Guide", "Run a full Linux kernel inside Windows \u2014 install, manage, and configure WSL2.", "Windows", "fab fa-windows",
         ["What is WSL2?", "Installation", "WSL Management", "Configuration", "Development Workflow", "GPU & Tips"]),
        ("windows-defender-security.html", "Windows Defender & Security Center Guide", "Configure Microsoft Defender, ASR rules, firewall, and ransomware protection.", "Windows", "fas fa-shield-virus",
         ["Defender Overview", "PowerShell Configuration", "ASR Rules", "Controlled Folder Access", "Defender Firewall"]),
        ("windows-event-viewer.html", "Windows Event Viewer & Troubleshooting", "Master Event Viewer for system diagnostics and troubleshooting.", "Windows", "fas fa-chart-bar",
         ["Event Viewer Basics", "Custom Views & Filtering", "PowerShell Queries", "Common Event IDs", "Diagnostic Scenarios"]),
        ("windows-task-scheduler.html", "Windows Task Scheduler Automation", "Automate tasks with Task Scheduler, triggers, conditions, and PowerShell integration.", "Windows", "fas fa-clock",
         ["Task Scheduler Overview", "Creating Basic Tasks", "Advanced Triggers", "Actions & Conditions", "PowerShell & CLI", "Troubleshooting Scheduled Tasks"]),

        # Networking (4)
        ("subnetting-cidr.html", "Subnetting & CIDR Explained", "Understand IP subnetting, CIDR notation, VLSM, and subnet calculation.", "Networking", "fas fa-network-wired",
         ["IP Addressing Review", "What is Subnetting?", "CIDR Notation", "Subnet Calculation", "VLSM", "Practice Problems"]),
        ("dns-records-deep-dive.html", "DNS Records Deep Dive", "A comprehensive guide to A, AAAA, CNAME, MX, TXT, NS, SRV, and DNSSEC records.", "Networking", "fas fa-globe",
         ["DNS Fundamentals", "A & AAAA Records", "CNAME & Aliases", "MX & Mail Records", "TXT & SPF Records", "DNSSEC"]),
        ("http2-http3.html", "HTTP/2 & HTTP/3 Protocols", "Learn the evolution of HTTP \u2014 multiplexing, server push, QUIC, and performance.", "Networking", "fas fa-exchange-alt",
         ["HTTP/1.1 Limitations", "HTTP/2 Features", "Multiplexing & Prioritization", "Server Push", "HTTP/3 & QUIC", "Migration Guide"]),
        ("grafana-prometheus.html", "Network Monitoring with Grafana & Prometheus", "Monitor servers and networks with Prometheus metrics and Grafana dashboards.", "DevOps", "fas fa-chart-line",
         ["Monitoring Overview", "Prometheus Setup", "Exporters & Metrics", "Grafana Dashboards", "Alerting Rules", "Best Practices"]),

        # Security/Privacy (5)
        ("owasp-top-10.html", "OWASP Top 10 Web Vulnerabilities", "Understand and protect against the most critical web application security risks.", "Security", "fas fa-shield-alt",
         ["Broken Access Control", "Cryptographic Failures", "Injection", "Insecure Design", "Security Misconfiguration", "Vulnerable Components", "Auth Failures", "Data Integrity", "Logging Monitoring", "SSRF"]),
        ("gpg-pgp-guide.html", "GPG & PGP Key Management", "Encrypt, sign, and verify with GPG. Manage keys, smartcards, and secure communication.", "Security", "fas fa-lock",
         ["What is GPG?", "Key Generation", "Key Management", "Encryption & Decryption", "Signing & Verification", "Smartcards & YubiKey"]),
        ("hashing-vs-encryption.html", "Hashing vs Encryption vs Encoding", "Understand the differences between hashing, encryption, and encoding with practical examples.", "Security", "fas fa-code-branch",
         ["Core Concepts", "Hashing Algorithms", "Symmetric Encryption", "Asymmetric Encryption", "Encoding Schemes", "When to Use Each"]),
        ("browser-fingerprinting.html", "Browser Fingerprinting & Anti-Detection", "How browser fingerprinting works and how to protect your privacy online.", "Security", "fas fa-fingerprint",
         ["What is Fingerprinting?", "Fingerprinting Techniques", "Canvas & WebGL", "Audio & Font Fingerprinting", "Anti-Detection Tools"]),
        ("social-engineering.html", "Social Engineering Awareness Guide", "Recognize and defend against phishing, pretexting, baiting, and manipulation tactics.", "Security", "fas fa-user-secret",
         ["What is Social Engineering?", "Phishing Attacks", "Pretexting & Tailgating", "Baiting & Quid Pro Quo", "Defense Strategies", "Incident Response"]),

        # Media & Design (4)
        ("davinci-resolve-basics.html", "DaVinci Resolve Editing Basics", "Learn video editing with DaVinci Resolve \u2014 cut, color, audio, and delivery.", "Creatives", "fas fa-video",
         ["Interface Overview", "Project Setup", "Cut & Edit Pages", "Color Correction", "Fairlight Audio", "Delivery & Export"]),
        ("blender-3d-basics.html", "Blender 3D Modeling Introduction", "Start your 3D journey with Blender \u2014 modeling, materials, lighting, and rendering.", "Creatives", "fas fa-cube",
         ["Blender Interface", "Basic Modeling", "Materials & Textures", "Lighting & Cameras", "Rendering", "Animation Basics"]),
        ("svg-animation-css-js.html", "SVG Animation with CSS & JS", "Create smooth, interactive SVG animations using CSS, JavaScript, and GSAP.", "Creatives", "fas fa-draw-polygon",
         ["SVG Basics", "CSS SVG Animations", "JavaScript SVG Manipulation", "GSAP Library", "Interactive Animations", "Performance Tips"]),
        ("audacity-audio-editing.html", "Audio Editing with Audacity", "Record, edit, and produce audio with Audacity \u2014 noise reduction, effects, and multitrack.", "Creatives", "fas fa-music",
         ["Audacity Setup", "Recording Audio", "Basic Editing", "Noise Reduction", "Effects & Filters", "Multitrack Mixing", "Exporting"]),

        # General Tech (11)
        ("cloud-computing-overview.html", "Cloud Computing Overview", "Compare AWS, GCP, and Azure services for compute, storage, networking, and serverless.", "DevOps", "fas fa-cloud",
         ["What is Cloud Computing?", "IaaS vs PaaS vs SaaS", "AWS Services", "Google Cloud Services", "Azure Services", "Multi-Cloud Strategies"]),
        ("virtualbox-vmware-hyperv.html", "VirtualBox vs VMware vs Hyper-V", "Compare the major hypervisors for desktop and server virtualization.", "Virtualization", "fas fa-server",
         ["Virtualization Overview", "VirtualBox Features", "VMware Workstation/Player", "Hyper-V Features", "Performance Comparison", "Choosing the Right Tool"]),
        ("containerization-vs-virtualization.html", "Containerization vs Virtualization", "Understand the differences between containers and VMs, and when to use each.", "DevOps", "fas fa-box",
         ["Traditional Virtualization", "Containerization with Docker", "Key Differences", "Use Cases", "Kubernetes Orchestration"]),
        ("big-data-tools.html", "Big Data Tools: Hadoop & Spark", "Introduction to big data processing with Hadoop, Spark, Hive, and the data lake ecosystem.", "Data", "fas fa-database",
         ["What is Big Data?", "Hadoop Ecosystem", "HDFS & MapReduce", "Apache Spark", "Spark SQL & Streaming", "Data Lakes"]),
        ("ml-basics-python.html", "Machine Learning Basics with Python", "Get started with ML using scikit-learn, pandas, and Jupyter for classification and regression.", "Programming", "fas fa-brain",
         ["What is Machine Learning?", "Setting Up Python ML Stack", "Data Preparation", "Supervised Learning", "Unsupervised Learning", "Model Evaluation"]),
        ("regex-advanced.html", "Advanced Regex Patterns & Tricks", "Go beyond basic regex with lookaheads, backreferences, atomic groups, and performance.", "Programming", "fas fa-code",
         ["Regex Engine Types", "Lookahead & Lookbehind", "Backreferences", "Atomic Groups", "Performance Optimization", "Real-World Patterns"]),
        ("ascii-unicode-encoding.html", "ASCII, Unicode & Encoding Explained", "Understand character encoding \u2014 ASCII, UTF-8, UTF-16, code points, and normalization.", "General", "fas fa-font",
         ["What is Character Encoding?", "ASCII Standard", "Unicode & Code Points", "UTF-8 Encoding", "UTF-16 & UTF-32", "Normalization Forms"]),
        ("filesystems-compared.html", "File Systems Compared", "Compare NTFS, ext4, Btrfs, ZFS, and APFS \u2014 features, performance, and use cases.", "Linux", "fas fa-folder-tree",
         ["File System Basics", "NTFS (Windows)", "ext4 (Linux)", "Btrfs (Linux)", "ZFS (Solaris/Linux)", "APFS (macOS)"]),
        ("raid-levels-explained.html", "RAID Levels Explained", "Understand RAID 0, 1, 5, 6, 10, 50, and 60 \u2014 performance, redundancy, and trade-offs.", "Storage", "fas fa-hdd",
         ["What is RAID?", "RAID 0 (Striping)", "RAID 1 (Mirroring)", "RAID 5 (Striped Parity)", "RAID 6 & RAID 10", "Software vs Hardware RAID"]),
        ("bios-uefi-boot.html", "BIOS vs UEFI vs Legacy Boot", "Understand the differences between BIOS, UEFI, Secure Boot, and boot process.", "System", "fas fa-microchip",
         ["What is BIOS?", "UEFI Overview", "Secure Boot", "GPT vs MBR", "Boot Process Comparison", "Troubleshooting Boot Issues"]),
        ("how-dns-works.html", "How DNS Works (Full Walkthrough)", "Follow a DNS query from browser to resolver to authoritative nameserver, step by step.", "Networking", "fas fa-globe",
         ["DNS Hierarchy", "Recursive Resolution", "Caching & TTL", "Record Types", "DNS Propagation", "Troubleshooting DNS"]),
    ]

    for filename, title, desc, badge, icon, toc_labels in placeholders:
        sid_list = [(label, label.lower().replace(" ", "-").replace("&", "and").replace("--", "-").replace(",", "").replace("/", "-")) for label in toc_labels]
        write_page(filename, make_page(title, filename, desc, badge, icon, sid_list, []))

    # Notify
    total = 1 + len(placeholders)  # active-recall.html was created separately
    print(f"\n=== Generated {total} tutorial files ===")


if __name__ == "__main__":
    os.makedirs(TUTS, exist_ok=True)
    generate_all()
