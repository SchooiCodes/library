(function(){
  var els = document.querySelectorAll('[data-aos]');
  if (els.length) {
    var obs = new IntersectionObserver(function(entries) {
      entries.forEach(function(e) {
        if (e.isIntersecting) {
          var el = e.target;
          var d = parseInt(el.getAttribute('data-aos-delay')) || 0;
          setTimeout(function(){ el.classList.add('aos-animate'); }, d);
          obs.unobserve(el);
        }
      });
    }, { threshold: 0.05, rootMargin: '0px 0px -20px 0px' });
    els.forEach(function(el) { obs.observe(el); });
  }
})();

(function(){
  var THEMES = [
    { id: '', name: 'Default', desc: 'Purple & blue', swatch: ['#667eea','#764ba2'] },
    { id: 'ocean', name: 'Ocean', desc: 'Teal & sky', swatch: ['#0ea5e9','#06b6d4'] },
    { id: 'forest', name: 'Forest', desc: 'Earthy green', swatch: ['#22c55e','#16a34a'] },
    { id: 'sunset', name: 'Sunset', desc: 'Orange & red', swatch: ['#f97316','#ef4444'] },
    { id: 'midnight', name: 'Midnight', desc: 'Deep indigo', swatch: ['#6366f1','#4f46e5'] },
    { id: 'mono', name: 'Mono', desc: 'Grayscale', swatch: ['#6b7280','#4b5563'] },
    { id: 'aurora', name: 'Aurora', desc: 'Pink & purple', swatch: ['#ec4899','#8b5cf6'] },
    { id: 'lava', name: 'Lava', desc: 'Red & orange', swatch: ['#ef4444','#f97316'] },
    { id: 'nord', name: 'Nord', desc: 'Arctic blue', swatch: ['#5e81ac','#81a1c1'] },
    { id: 'dracula', name: 'Dracula', desc: 'Dark purple', swatch: ['#bd93f9','#ff79c6'] },
  ];

  var savedTheme = localStorage.getItem('colorTheme') || '';
  if (savedTheme) document.body.classList.add('theme-' + savedTheme);

  var navMenu = document.querySelector('.nav-menu');
  var toggle = document.getElementById('theme-toggle');
  if (navMenu && toggle) {
    var pickerLi = document.createElement('li');
    pickerLi.style.position = 'relative';
    var pickerBtn = document.createElement('button');
    pickerBtn.className = 'theme-picker-btn';
    pickerBtn.setAttribute('aria-label', 'Choose theme');
    pickerBtn.innerHTML = '<i class="fas fa-palette"></i>';
    pickerLi.appendChild(pickerBtn);

    var dropdown = document.createElement('div');
    dropdown.className = 'theme-picker-dropdown';
    THEMES.forEach(function(th) {
      var opt = document.createElement('button');
      opt.className = 'theme-option' + (th.id === savedTheme ? ' active' : '');
      opt.setAttribute('data-theme', th.id);
      var swatch = th.swatch.length === 2
        ? 'background:linear-gradient(135deg,' + th.swatch[0] + ',' + th.swatch[1] + ')'
        : 'background:' + th.swatch[0];
      opt.innerHTML = '<span class="theme-swatch" style="' + swatch + '"></span>'
        + '<span class="theme-label"><span class="theme-name">' + th.name + '</span><span class="theme-desc">' + th.desc + '</span></span>';
      opt.addEventListener('click', function() {
        dropdown.querySelectorAll('.theme-option').forEach(function(o) { o.classList.remove('active'); });
        opt.classList.add('active');
        var tid = opt.getAttribute('data-theme');
        THEMES.forEach(function(t) {
          document.body.classList.remove('theme-' + t.id);
        });
        if (tid) document.body.classList.add('theme-' + tid);
        localStorage.setItem('colorTheme', tid);
        dropdown.classList.remove('open');
      });
      dropdown.appendChild(opt);
    });
    pickerLi.appendChild(dropdown);
    pickerBtn.addEventListener('click', function(e) { e.stopPropagation(); dropdown.classList.toggle('open'); });
    document.addEventListener('click', function() { dropdown.classList.remove('open'); });
    dropdown.addEventListener('click', function(e) { e.stopPropagation(); });
    navMenu.insertBefore(pickerLi, toggle.parentNode);
  }

  var t = document.getElementById('theme-toggle');
  if (t) {
    var s = localStorage.getItem('theme');
    if (s === null || s === 'dark') {
      document.body.classList.add('dark-mode');
      if (s === null) localStorage.setItem('theme', 'dark');
    }
    t.innerHTML = document.body.classList.contains('dark-mode')
      ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
    t.addEventListener('click', function() {
      document.body.classList.toggle('dark-mode');
      var d = document.body.classList.contains('dark-mode');
      localStorage.setItem('theme', d ? 'dark' : 'light');
      t.innerHTML = d ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
    });
  }
})();

(function(){
  var n = document.getElementById('navbar');
  if (n) {
    var ticking = false;
    window.addEventListener('scroll', function() {
      if (!ticking) {
        requestAnimationFrame(function() {
          if (window.scrollY > 50) n.classList.add('scrolled');
          else n.classList.remove('scrolled');
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }

  var h = document.getElementById('hamburger');
  var m = document.querySelector('.nav-menu');
  if (h && m) {
    var bd = document.createElement('div');
    bd.className = 'nav-backdrop';
    document.body.appendChild(bd);

    var closeMenu = function() {
      h.classList.remove('active');
      m.classList.remove('active');
      bd.classList.remove('active');
      document.body.style.overflow = '';
    };

    h.addEventListener('click', function() {
      h.classList.toggle('active');
      m.classList.toggle('active');
      bd.classList.toggle('active');
      document.body.style.overflow = h.classList.contains('active') ? 'hidden' : '';
    });

    bd.addEventListener('click', closeMenu);
    Array.from(m.querySelectorAll('a')).forEach(function(l) {
      l.addEventListener('click', closeMenu);
    });
  }

  (function(){
    var bn = document.querySelector('.mobile-bottom-nav');
    if (!bn) {
      bn = document.createElement('nav');
      bn.className = 'mobile-bottom-nav';
      var inner = document.createElement('div');
      inner.className = 'bn-inner';
      bn.appendChild(inner);
      document.body.appendChild(bn);
    }
    var inner = bn.querySelector('.bn-inner');
    if (inner && !inner.children.length) {
      var links = document.querySelectorAll('.nav-menu a');
      var html = '';
      links.forEach(function(l) {
        var href = l.getAttribute('href');
        var icon = l.querySelector('i');
        var cls = icon ? icon.className : 'fas fa-link';
        var text = l.textContent.trim();
        html += '<a href="' + href + '"><i class="' + cls + '"></i><span>' + text + '</span></a>';
      });
      inner.innerHTML = html;
      var cur = window.location.pathname.split('/').pop() || 'index.html';
      inner.querySelectorAll('a').forEach(function(a) {
        if (a.getAttribute('href') === cur || a.getAttribute('href') === './' + cur) {
          a.classList.add('active');
        }
      });
    }
  })();

  var sb = document.querySelector('.sidebar');
  var st = document.querySelector('.sidebar-toggle');
  if (sb && !st) {
    var btn = document.createElement('button');
    btn.className = 'sidebar-toggle';
    btn.innerHTML = '<span><i class="fas fa-bars"></i> On this page</span><i class="fas fa-chevron-down"></i>';
    btn.setAttribute('aria-label', 'Toggle sidebar');
    sb.insertBefore(btn, sb.firstChild);
    var content = document.createElement('div');
    content.className = 'sidebar-content';
    while (sb.children.length > 1) {
      content.appendChild(sb.children[1]);
    }
    sb.appendChild(content);
    btn.addEventListener('click', function() {
      btn.classList.toggle('open');
      sb.classList.toggle('collapsed');
    });
  }
})();

(function(){
  var LEXICON = {
    "API": "Application Programming Interface — a set of rules for interacting with software",
    "CLI": "Command-Line Interface — text-based interface for running commands",
    "CSS": "Cascading Style Sheets — a language for styling HTML documents",
    "HTML": "HyperText Markup Language — the standard language for creating web pages",
    "HTTP": "HyperText Transfer Protocol — the foundation of data communication on the web",
    "HTTPS": "HTTP Secure — encrypted HTTP using TLS/SSL",
    "JS": "JavaScript — a high-level programming language for the web",
    "JSON": "JavaScript Object Notation — a lightweight data interchange format",
    "CRUD": "Create, Read, Update, Delete — the four basic operations for data storage",
    "DOM": "Document Object Model — a programming interface for HTML documents",
    "GUI": "Graphical User Interface — visual interface for interacting with software",
    "IDE": "Integrated Development Environment — a software application for coding",
    "REST": "Representational State Transfer — an architectural style for APIs",
    "SDK": "Software Development Kit — a set of tools for building software",
    "SEO": "Search Engine Optimization — practices to improve visibility in search results",
    "SPA": "Single Page Application — a web app that loads one page and updates content dynamically",
    "PWA": "Progressive Web App — a web app that behaves like a native app with offline support",
    "SSR": "Server-Side Rendering — generating HTML on the server rather than in the browser",
    "CSR": "Client-Side Rendering — rendering pages in the browser using JavaScript",
    "TTFB": "Time to First Byte — time between a request and the first byte of the response",
    "2FA": "Two-Factor Authentication — a second layer of security beyond just a password",
    "CVE": "Common Vulnerabilities and Exposures — a catalog of publicly known security flaws",
    "DDoS": "Distributed Denial of Service — overwhelming a server with traffic to make it unavailable",
    "E2EE": "End-to-End Encryption — encryption where only communicating parties can read messages",
    "MITM": "Man-in-the-Middle — attack where the attacker secretly intercepts communications",
    "RCE": "Remote Code Execution — vulnerability allowing code execution on a remote system",
    "XSS": "Cross-Site Scripting — injecting malicious scripts into otherwise trusted websites",
    "CSRF": "Cross-Site Request Forgery — tricking a user into unwanted actions on a site",
    "JWT": "JSON Web Token — a compact token format for securely transmitting claims between parties",
    "OAuth": "Open Authorization — open standard for token-based authentication and authorization",
    "HSTS": "HTTP Strict Transport Security — forces browsers to connect over HTTPS only",
    "SQL Injection": "Injecting SQL queries through input fields to manipulate a database",
    "Zero-Day": "A vulnerability unknown to the vendor with no available fix",
    "OWASP": "Open Web Application Security Project — nonprofit for improving software security",
    "CDN": "Content Delivery Network — a distributed network of servers that deliver content closer to users",
    "DHCP": "Dynamic Host Configuration Protocol — automatically assigns IP addresses on a network",
    "DNS": "Domain Name System — translates human-readable domain names into IP addresses",
    "LAN": "Local Area Network — a network connecting devices within a limited area",
    "NAT": "Network Address Translation — maps private IPs to a public IP for internet access",
    "TCP": "Transmission Control Protocol — a reliable, connection-oriented transport protocol",
    "UDP": "User Datagram Protocol — a fast, connectionless transport protocol",
    "VPN": "Virtual Private Network — encrypts traffic and routes it through a remote server",
    "SSL": "Secure Sockets Layer — a deprecated cryptographic protocol superseded by TLS",
    "TLS": "Transport Layer Security — the modern cryptographic protocol for secure communication",
    "SSH": "Secure Shell — a cryptographic network protocol for secure remote access",
    "grep": "A command-line utility for searching text using regular expression patterns",
    "bash": "Bourne Again SHell — the default command shell on most Linux distributions",
    "cron": "A time-based job scheduler in Unix-like systems for running tasks at intervals",
    "daemon": "A background process that runs continuously and handles service requests",
    "kernel": "The core of an operating system that manages hardware and system resources",
    "symlink": "Symbolic link — a file that points to another file or directory",
    "pipe": "A mechanism for passing output of one command as input to another (using |)",
    "sudo": "Superuser Do — allows executing commands with elevated privileges",
    "chmod": "Changes file permissions (read, write, execute) for owner, group, and others",
    "chroot": "Changes the root directory for a process, creating an isolated filesystem environment",
    "rsync": "A fast file-syncing and transfer tool that copies only differences",
    "systemd": "A system and service manager for Linux, used as the init system",
    "FIFO": "First In, First Out — a named pipe used for inter-process communication",
    "inode": "A data structure that stores metadata about a file on a Unix filesystem",
    "BIOS": "Basic Input/Output System — firmware that initializes hardware during boot",
    "DDR": "Double Data Rate — a type of memory that transfers data on both clock edges",
    "GPU": "Graphics Processing Unit — a processor optimized for rendering graphics",
    "PCIe": "Peripheral Component Interconnect Express — a high-speed expansion bus standard",
    "NVMe": "Non-Volatile Memory Express — a fast protocol for SSDs over PCIe",
    "SSD": "Solid-State Drive — a storage device using flash memory with no moving parts",
    "HDD": "Hard Disk Drive — a storage device with spinning magnetic platters",
    "RAM": "Random Access Memory — fast volatile memory for active data and applications",
    "CPU": "Central Processing Unit — the primary processor that executes instructions",
    "USB": "Universal Serial Bus — a standard interface for connecting peripherals",
    "UEFI": "Unified Extensible Firmware Interface — modern replacement for BIOS",
    "FPS": "Frames Per Second — measures how many frames are rendered each second",
    "RNG": "Random Number Generator — used for randomized outcomes like loot drops",
    "Ping": "The round-trip time for data to travel from a client to a server and back",
    "AFK": "Away From Keyboard — a player who is not actively playing",
    "NPC": "Non-Player Character — characters controlled by the game, not by players",
    "PvP": "Player versus Player — combat between human players",
    "DLC": "Downloadable Content — additional content released after a game's launch",
    "MMO": "Massively Multiplayer Online — games with large numbers of players in the same world",
    "NCS": "NoCopyrightSounds — a label releasing copyright-free music for creators"
  };

  var TERMS = Object.keys(LEXICON).sort(function(a, b) { return b.length - a.length; });

  var tooltip = document.createElement('div');
  tooltip.className = 'lexicon-tooltip';
  document.body.appendChild(tooltip);

  var activeWord = null;

  function showTooltip(el, def) {
    if (activeWord === el) return;
    hideTooltip();
    tooltip.textContent = def;
    activeWord = el;
    var rect = el.getBoundingClientRect();
    var top = rect.top + window.scrollY - tooltip.offsetHeight - 8;
    if (top < window.scrollY) {
      top = rect.bottom + window.scrollY + 8;
    }
    tooltip.style.left = rect.left + rect.width / 2 + 'px';
    tooltip.style.top = top + 'px';
    tooltip.classList.add('visible');
  }

  function hideTooltip() {
    tooltip.classList.remove('visible');
    activeWord = null;
  }

  function bindLexiconWords() {
    var words = document.querySelectorAll('.lexicon-word');
    words.forEach(function(el) {
      if (el._lexiconBound) return;
      el._lexiconBound = true;
      var term = el.getAttribute('data-term') || el.textContent.trim();
      var def = LEXICON[term];
      if (def) {
        el.setAttribute('title', def);
        el.addEventListener('mouseenter', function(e) { showTooltip(el, def); });
        el.addEventListener('mouseleave', hideTooltip);
        el.addEventListener('click', function(e) {
          if (document.querySelector('body.lexicon-page')) {
            e.preventDefault();
            showTooltip(el, def);
            return;
          }
          e.preventDefault();
          var term = el.getAttribute('data-term') || el.textContent.trim();
          window.location.href = 'lexicon/index.html#term-' + encodeURIComponent(term);
        });
      }
    });
  }

  function autoHighlight() {
    if (document.querySelector('body.lexicon-page')) return;
    var main = document.querySelector('main');
    if (!main) return;

    var walker = document.createTreeWalker(main, NodeFilter.SHOW_TEXT, {
      acceptNode: function(node) {
        var parent = node.parentNode;
        if (!parent) return NodeFilter.FILTER_REJECT;
        var tag = parent.tagName ? parent.tagName.toLowerCase() : '';
        if (tag === 'code' || tag === 'pre' || tag === 'a' || tag === 'script' || tag === 'style') return NodeFilter.FILTER_REJECT;
        if (parent.classList && parent.classList.contains('lexicon-word')) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });

    var nodesToReplace = [];
    while (walker.nextNode()) { nodesToReplace.push(walker.currentNode); }

    nodesToReplace.forEach(function(textNode) {
      var text = textNode.textContent;
      var frag = document.createDocumentFragment();

      var escaped = TERMS.map(function(t) { return t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); });
      var re = new RegExp('\\b(' + escaped.join('|') + ')\\b', 'gi');
      var lastIdx = 0;
      var match;

      while ((match = re.exec(text)) !== null) {
        var idx = match.index;
        var matchedText = match[0];
        var canon = TERMS.find(function(t) { return t.toUpperCase() === matchedText.toUpperCase(); });
        if (!canon) continue;

        if (idx > lastIdx) {
          frag.appendChild(document.createTextNode(text.substring(lastIdx, idx)));
        }

        var def = LEXICON[canon] || '';
        var span = document.createElement('span');
        span.className = 'lexicon-word';
        span.setAttribute('data-term', canon);
        span.textContent = matchedText;
        if (def) span.setAttribute('title', def);
        frag.appendChild(span);

        lastIdx = idx + matchedText.length;
      }

      if (lastIdx < text.length) {
        frag.appendChild(document.createTextNode(text.substring(lastIdx)));
      }

      textNode.parentNode.replaceChild(frag, textNode);
    });

    bindLexiconWords();
  }

  function initSearch() {
    var input = document.getElementById('lexicon-search');
    if (!input) return;
    var count = document.getElementById('lexicon-count');
    var items = document.querySelectorAll('.lexicon-list dt');

    function filter() {
      var q = input.value.trim().toLowerCase();
      var visible = 0;
      items.forEach(function(dt) {
        var term = dt.textContent.trim().toLowerCase();
        var dd = dt.nextElementSibling;
        var match = !q || term.indexOf(q) !== -1;
        dt.style.display = match ? '' : 'none';
        if (dd) dd.style.display = match ? '' : 'none';
        if (match) visible++;
      });
      if (count) count.textContent = 'Showing ' + visible + ' of ' + items.length + ' terms';
    }

    input.addEventListener('input', filter);
    filter();
  }

  bindLexiconWords();
  autoHighlight();
  initSearch();
})();

(function(){
  var CATEGORY_MAP = {
    'nginx': 'web-servers', 'docker-compose': 'containers', 'docker': 'containers',
    'ansible': 'automation', 'github-actions': 'ci-cd', 'monitoring': 'monitoring',
    'postgresql': 'databases', 'redis': 'databases', 'sql-basics': 'databases',
    'database-design': 'databases',
    'typescript': 'programming', 'javascript-basics': 'programming',
    'html-css-basics': 'programming', 'css-animations': 'programming',
    'react-basics': 'programming', 'nodejs-guide': 'programming',
    'python-advanced': 'programming', 'PY': 'programming', 'JS': 'programming',
    'web-scraping': 'programming', 'api-basics': 'programming', 'api-testing': 'programming',
    'bash-scripting': 'linux', 'linux': 'linux', 'linux-cli': 'linux',
    'linux-filesystem': 'linux', 'linux-permissions': 'linux',
    'linux-package-management': 'linux', 'linux-containers': 'linux',
    'linux-networking': 'linux', 'linux-ssh-tips': 'linux',
    'linux-server': 'linux', 'systemd-guide': 'linux', 'systemd-services': 'linux',
    'cachyos': 'linux', 'arch-linux': 'linux', 'hyprland': 'linux',
    'curl-wget-guide': 'cli-tools', 'ffmpeg-guide': 'cli-tools',
    'tmux-guide': 'cli-tools', 'jq-guide': 'cli-tools',
    'git-advanced': 'cli-tools', 'imagemagick-guide': 'cli-tools', 'rsync': 'cli-tools',
    'ssl-certificates': 'security', 'wireguard': 'security', 'fail2ban': 'security',
    'wifi-security': 'security', 'firewall-setup': 'security', 'vpn-setup': 'security',
    'proxy-guide': 'security', 'encryption-guide': 'security', 'password-security': 'security',
    'kali-linux': 'security', 'tails': 'security', 'bitlocker': 'security',
    'windows-hardening': 'security', 'browser-privacy': 'security',
    'nextdns': 'privacy', 'rethinkdns': 'privacy', 'adblocking': 'privacy',
    'networking-basics': 'networking', 'network-troubleshooting': 'networking',
    'backup-strategies': 'backup',
    'windows-debloat': 'windows', 'windows-registry': 'windows',
    'windows-rescue': 'windows', 'windows-apps': 'windows',
    'windows-shortcuts': 'windows', 'windows-hardening': 'windows',
    'windows-deployment': 'windows', 'windows-powershell-scripting': 'windows',
    'windows-environment-variables': 'windows', 'windows-task-automation': 'windows',
    'powershell': 'windows', 'Batchfile': 'windows',
    'virtual-machines': 'hardware', 'homelab-guide': 'hardware',
    'raspberry-pi-setup': 'hardware', 'hardware-diagnostics': 'hardware',
    'chromebook-firmware': 'hardware', 'ventoy': 'hardware',
    'hirens-boot-cd': 'rescue', 'bootable-usb': 'rescue',
    'automation': 'automation',
    'markdown-guide': 'writing', 'regex': 'writing',
    'neovim': 'editors', 'vscode': 'editors',
  };

  var TITLES = {
    'nginx': 'Nginx Web Server', 'docker-compose': 'Docker Compose', 'docker': 'Docker',
    'ansible': 'Ansible', 'github-actions': 'GitHub Actions', 'monitoring': 'Server Monitoring',
    'postgresql': 'PostgreSQL', 'redis': 'Redis', 'sql-basics': 'SQL Basics',
    'database-design': 'Database Design',
    'typescript': 'TypeScript', 'javascript-basics': 'JavaScript',
    'html-css-basics': 'HTML & CSS', 'css-animations': 'CSS Animations',
    'react-basics': 'React', 'nodejs-guide': 'Node.js',
    'python-advanced': 'Advanced Python',
    'web-scraping': 'Web Scraping', 'api-basics': 'REST APIs', 'api-testing': 'API Testing',
    'bash-scripting': 'Bash Scripting', 'linux': 'Linux Guide', 'linux-cli': 'CLI Tools',
    'linux-filesystem': 'Linux Filesystem', 'linux-permissions': 'Linux Permissions',
    'linux-package-management': 'Package Management', 'linux-containers': 'Linux Containers',
    'linux-networking': 'Linux Networking', 'linux-ssh-tips': 'SSH Tips',
    'linux-server': 'Linux Server Admin', 'systemd-guide': 'systemd Guide',
    'systemd-services': 'systemd Services',
    'cachyos': 'CachyOS', 'arch-linux': 'Arch Linux', 'hyprland': 'Hyprland',
    'curl-wget-guide': 'curl & wget', 'ffmpeg-guide': 'FFmpeg', 'tmux-guide': 'Tmux',
    'jq-guide': 'jq', 'git-advanced': 'Advanced Git', 'imagemagick-guide': 'ImageMagick',
    'rsync': 'rsync',
    'ssl-certificates': 'SSL Certificates', 'wireguard': 'WireGuard', 'fail2ban': 'Fail2ban',
    'wifi-security': 'Wi-Fi Security', 'firewall-setup': 'Firewall', 'vpn-setup': 'VPN Setup',
    'proxy-guide': 'Proxy Guide', 'encryption-guide': 'Encryption', 'password-security': 'Password Security',
    'kali-linux': 'Kali Linux', 'tails': 'Tails OS', 'bitlocker': 'BitLocker',
    'windows-hardening': 'Windows Hardening', 'browser-privacy': 'Browser Privacy',
    'nextdns': 'NextDNS', 'rethinkdns': 'RethinkDNS', 'adblocking': 'Adblocking',
    'networking-basics': 'Networking Basics', 'network-troubleshooting': 'Network Troubleshooting',
    'ssh-guide': 'SSH Guide', 'backup-strategies': 'Backup Strategies',
    'windows-debloat': 'Windows Debloating', 'windows-registry': 'Windows Registry',
    'windows-rescue': 'Windows Recovery', 'windows-apps': 'Essential Windows Apps',
    'windows-shortcuts': 'Keyboard Shortcuts', 'windows-deployment': 'Windows Deployment',
    'windows-powershell-scripting': 'PowerShell Scripting',
    'windows-environment-variables': 'Environment Variables',
    'windows-task-automation': 'Task Automation', 'powershell': 'PowerShell Basics',
    'Batchfile': 'Batchfile Basics',
    'virtual-machines': 'Virtual Machines', 'homelab-guide': 'Homelab',
    'raspberry-pi-setup': 'Raspberry Pi', 'hardware-diagnostics': 'Hardware Diagnostics',
    'chromebook-firmware': 'Chromebook Firmware', 'ventoy': 'Ventoy',
    'hirens-boot-cd': "Hiren's Boot CD", 'bootable-usb': 'Bootable USB',
    'automation': 'Automation Guide', 'markdown-guide': 'Markdown',
    'regex': 'Regex Guide', 'neovim': 'Neovim', 'vscode': 'VS Code Setup',
  };

  function getPageName() {
    var path = window.location.pathname;
    var match = path.match(/\/([^\/]+)\.html$/);
    return match ? match[1] : null;
  }

  function injectSimilarArticles() {
    if (document.querySelector('body.lexicon-page')) return;
    var page = getPageName();
    if (!page) return;
    var cat = CATEGORY_MAP[page];
    if (!cat) return;

    var main = document.querySelector('.main-content');
    if (!main) return;
    if (document.getElementById('similar-articles-section')) return;

    var similar = [];
    for (var key in CATEGORY_MAP) {
      if (CATEGORY_MAP[key] === cat && key !== page) {
        similar.push(key);
      }
    }
    if (similar.length === 0) return;

    var section = document.createElement('div');
    section.id = 'similar-articles-section';
    section.style.cssText = 'margin-top:48px;padding-top:32px;border-top:1px solid var(--card-border);';

    var html = '<h2><i class="fas fa-link"></i> Similar Articles</h2>';
    html += '<div class="card-grid" style="grid-template-columns:repeat(auto-fill,minmax(200px,1fr));">';

    similar.slice(0, 6).forEach(function(key) {
      var title = TITLES[key] || key;
      html += '<div class="card" style="padding:20px;text-align:center;">';
      html += '<div class="card-icon" style="margin:0 auto 12px;"><i class="fas fa-file"></i></div>';
      html += '<h3 style="font-size:0.95rem;">' + title + '</h3>';
      html += '<a href="' + key + '.html" class="card-link" style="font-size:0.85rem;">Read <i class="fas fa-arrow-right"></i></a>';
      html += '</div>';
    });

    html += '</div>';
    section.innerHTML = html;
    main.appendChild(section);
  }

  injectSimilarArticles();
})();

(function(){
  var CATEGORY_ICONS = {
    'tutorials': 'fa-book', 'resources': 'fa-folder-open',
    'survival': 'fa-life-ring', 'piracy': 'fa-skull',
    'lexicon': 'fa-book-open', 'smt': 'fa-cube',
    'docs': 'fa-archive', 'programming': 'fa-code',
    'security': 'fa-shield-alt', 'tools': 'fa-tools',
    'gaming': 'fa-gamepad', 'creatives': 'fa-paint-brush',
    'projects': 'fa-project-diagram', 'minecraft': 'fa-tree',
    'home': 'fa-home'
  };

  var overlay, input, resultsEl, searchIndex = null;

  function openSearch() {
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.className = 'search-overlay';
      overlay.innerHTML =
        '<div class="search-modal">' +
          '<div class="search-modal-header">' +
            '<i class="fas fa-search"></i>' +
            '<input type="text" id="search-input" placeholder="Search tutorials, resources, terms..." autocomplete="off" spellcheck="false">' +
            '<span class="kbd-hint">ESC</span>' +
            '<button class="search-modal-close" id="search-close"><i class="fas fa-times"></i></button>' +
          '</div>' +
          '<div class="search-results" id="search-results">' +
            '<div class="search-result-empty"><i class="fas fa-search"></i><p>Start typing to search...</p></div>' +
          '</div>' +
        '</div>';
      document.body.appendChild(overlay);

      input = document.getElementById('search-input');
      resultsEl = document.getElementById('search-results');

      document.getElementById('search-close').addEventListener('click', closeSearch);
      overlay.addEventListener('click', function(e) {
        if (e.target === overlay) closeSearch();
      });
      document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') closeSearch();
      });

      var debounceTimer;
      input.addEventListener('input', function() {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(function() { doSearch(input.value); }, 150);
      });
      input.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') {
          var first = resultsEl.querySelector('.search-result-item');
          if (first) { closeSearch(); window.location.href = first.getAttribute('href'); }
        }
      });
    }

    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    setTimeout(function() {
      var inp = document.getElementById('search-input');
      if (inp) inp.focus();
    }, 200);

    if (!searchIndex) {
      resultsEl.innerHTML = '<div class="search-result-empty"><i class="fas fa-spinner fa-pulse"></i><p>Loading index...</p></div>';
      var scriptTag = document.querySelector('script[src*="scripts.js"]');
      var scriptUrl = scriptTag ? scriptTag.src : '';
      var basePath = scriptUrl.substring(0, scriptUrl.lastIndexOf('/') + 1);
      var indexUrl = basePath + '../search-index.json';
      fetch(indexUrl).then(function(r) { return r.json(); }).then(function(data) {
        searchIndex = data;
        var val = document.getElementById('search-input');
        if (val && val.value) doSearch(val.value);
        else resultsEl.innerHTML = '<div class="search-result-empty"><i class="fas fa-search"></i><p>Start typing to search...</p></div>';
      }).catch(function() {
        resultsEl.innerHTML = '<div class="search-result-empty"><i class="fas fa-exclamation-triangle"></i><p>Failed to load search index.</p></div>';
      });
    }
  }

  function closeSearch() {
    if (overlay) {
      overlay.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  function doSearch(query) {
    var q = query.trim().toLowerCase();
    if (!q || !searchIndex) {
      resultsEl.innerHTML = '<div class="search-result-empty"><i class="fas fa-search"></i><p>Start typing to search...</p></div>';
      return;
    }

    var results = searchIndex.filter(function(item) {
      return item.title.toLowerCase().indexOf(q) !== -1 ||
             item.desc.toLowerCase().indexOf(q) !== -1;
    });

    if (results.length === 0) {
      resultsEl.innerHTML = '<div class="search-result-empty"><i class="fas fa-search-minus"></i><p>No results found for "' + query + '"</p></div>';
      return;
    }

    // Group by category
    var groups = {};
    results.forEach(function(item) {
      var cat = item.cat || 'other';
      if (!groups[cat]) groups[cat] = [];
      groups[cat].push(item);
    });

    var order = ['tutorials', 'resources', 'lexicon', 'survival', 'piracy', 'smt', 'docs', 'programming', 'security', 'tools', 'gaming', 'creatives', 'projects', 'minecraft', 'home'];
    var html = '';
    order.forEach(function(cat) {
      if (!groups[cat]) return;
      html += '<div class="search-result-group"><h3>' + cat.charAt(0).toUpperCase() + cat.slice(1) + '</h3>';
      groups[cat].forEach(function(item) {
        var icon = CATEGORY_ICONS[cat] || 'fa-file';
        html += '<a href="' + item.url + '" class="search-result-item" onclick="document.body.style.overflow=\'\'">';
        html += '<span class="result-icon"><i class="fas ' + icon + '"></i></span>';
        html += '<span class="result-info">';
        html += '<span class="result-title">' + item.title + '</span>';
        if (item.desc) html += '<span class="result-desc">' + item.desc.substring(0, 120) + '</span>';
        html += '</span></a>';
      });
      html += '</div>';
    });

    resultsEl.innerHTML = html;
  }

  // Bind search toggle
  var searchToggle = document.getElementById('search-toggle');
  if (searchToggle) {
    searchToggle.addEventListener('click', openSearch);
  }

  // Ctrl+K / Cmd+K
  document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      openSearch();
    }
  });

  // Preload index when idle
  if ('requestIdleCallback' in window) {
    requestIdleCallback(function() {
      var stag = document.querySelector('script[src*="scripts.js"]');
      var surl = stag ? stag.src : '';
      var bpath = surl.substring(0, surl.lastIndexOf('/') + 1);
      fetch(bpath + '../search-index.json').then(function(r) { return r.json(); }).then(function(data) { searchIndex = data; });
    });
  }
})();
