(function(){
  try {
    var els = document.querySelectorAll('[data-aos]');
    if (els.length && typeof IntersectionObserver !== 'undefined') {
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
  } catch(e) {}
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
    "NCS": "NoCopyrightSounds — a label releasing copyright-free music for creators",

    "IoT": "Internet of Things — network of physical devices embedded with sensors and software",
    "SaaS": "Software as a Service — cloud-based software accessed via subscription",
    "PaaS": "Platform as a Service — cloud platform for developing, running, and managing apps",
    "IaaS": "Infrastructure as a Service — cloud-based virtualized computing resources",
    "SLA": "Service Level Agreement — a contract defining expected service quality and uptime",
    "API Gateway": "A server that acts as an API frontend for routing, auth, and rate limiting",
    "Webhook": "An HTTP callback that sends real-time data to another service when an event occurs",
    "Rate Limiting": "Restricting the number of requests a client can make in a given time period",
    "Edge Computing": "Processing data near the source rather than in a centralized cloud",
    "Cloud Computing": "On-demand delivery of computing resources over the internet",

    "Agile": "An iterative software development methodology focused on flexibility and feedback",
    "Scrum": "An Agile framework with sprints, daily standups, and defined roles",
    "Kanban": "A visual workflow management method for continuous delivery",
    "MVC": "Model-View-Controller — an architectural pattern separating data, UI, and logic",
    "MVVM": "Model-View-ViewModel — an architectural pattern for data-binding UIs",
    "Microservices": "An architecture where apps are composed of small, independent services",
    "Monolith": "A traditional application architecture where all components are tightly coupled",
    "Functional": "A programming paradigm using pure functions and avoiding state mutation",
    "Duck Typing": "An object's suitability is determined by its methods, not its type",
    "Static Typing": "Type checking at compile-time, catching errors before runtime",
    "Dynamic Typing": "Type checking at runtime, allowing more flexibility but fewer guarantees",
    "Type Inference": "The compiler automatically deducing the type of an expression",
    "Generics": "Allow writing code that works with any type while maintaining type safety",
    "Interface": "A contract defining a set of methods that a class must implement",
    "Abstract Class": "A class that cannot be instantiated and may contain abstract methods",
    "Observable": "A data source that emits values over time, used in reactive programming",
    "Promise": "An object representing the eventual completion or failure of an async operation",
    "Callback Hell": "Nested callbacks creating deeply indented, unreadable code",
    "Deadlock": "Two processes each waiting for a resource held by the other, causing a standstill",
    "Race Condition": "Unpredictable behavior when timing affects the outcome of concurrent operations",
    "Thread": "The smallest unit of execution within a process, sharing the same memory space",
    "Process": "An instance of a running program with its own memory space and resources",
    "Mutex": "Mutual Exclusion — a synchronization primitive preventing concurrent access",
    "Coroutine": "A lightweight cooperative thread that can suspend and resume execution",

    "GraphQL": "A query language for APIs that lets clients request exactly the data they need",
    "gRPC": "A high-performance RPC framework using HTTP/2 and Protocol Buffers",
    "WebRTC": "Web Real-Time Communication — peer-to-peer audio, video, and data sharing",
    "WASM": "WebAssembly — a binary instruction format for high-performance web apps",
    "Cookie": "A small piece of data stored by the browser for session management and tracking",
    "LocalStorage": "A web storage API for persisting key-value data with no expiration",
    "SessionStorage": "A web storage API for data that persists only for the current session",
    "Service Worker": "A script that runs in the background, enabling offline and push notification features",
    "Virtual DOM": "A lightweight copy of the DOM used by React to optimize re-renders",
    "Shadow DOM": "A browser API for encapsulating DOM and CSS within web components",
    "SSG": "Static Site Generator — builds HTML pages at compile time for fast delivery",
    "ISR": "Incremental Static Regeneration — allows updating static content without rebuilding",

    "SSRF": "Server-Side Request Forgery — exploiting a server to make requests to internal resources",
    "IDOR": "Insecure Direct Object Reference — accessing unauthorized data by modifying a parameter",
    "XXE": "XML External Entity — an attack exploiting XML parsers to read files or execute code",
    "Buffer Overflow": "Writing data beyond a buffer's boundary, often leading to code execution",
    "ASLR": "Address Space Layout Randomization — randomizes memory addresses to prevent exploits",
    "Sandbox": "An isolated environment for running untrusted code safely",
    "Container": "A lightweight, portable unit that packages code and dependencies together",
    "Hypervisor": "Software that creates and manages virtual machines on a host system",
    "TPM": "Trusted Platform Module — a hardware chip for secure cryptographic operations",
    "HSM": "Hardware Security Module — a dedicated device for managing encryption keys",
    "PKI": "Public Key Infrastructure — a system for managing digital certificates and encryption",

    "QoS": "Quality of Service — managing network traffic to prioritize critical data",
    "BGP": "Border Gateway Protocol — the routing protocol that governs internet traffic between ASes",
    "VLAN": "Virtual Local Area Network — logically segments a network into isolated broadcast domains",
    "SDN": "Software-Defined Networking — separates the control plane from the data plane",
    "MPLS": "Multiprotocol Label Switching — directs data using labels rather than IP lookups",
    "IPsec": "Internet Protocol Security — encrypts and authenticates IP packets for secure VPNs",
    "LACP": "Link Aggregation Control Protocol — bundles multiple network links for redundancy",

    "apparmor": "AppArmor — a Linux kernel security module that restricts programs via profiles",
    "selinux": "Security-Enhanced Linux — a kernel security module with mandatory access controls",
    "strace": "A Linux diagnostic tool that traces system calls made by a process",
    "auditd": "The Linux audit daemon for logging system calls and security events",
    "logrotate": "A tool that automatically rotates, compresses, and removes log files",
    "iptables": "The classic Linux firewall utility for filtering packets and NAT",
    "nftables": "The modern Linux firewall framework replacing iptables",
    "htop": "An interactive process viewer for Linux with a colorful interface",
    "perf": "A powerful Linux profiling tool for performance analysis",
    "ZFS": "An advanced filesystem with volume management, snapshots, and data integrity",
    "Btrfs": "A Linux copy-on-write filesystem with snapshots and self-healing",
    "LVM": "Logical Volume Manager — flexible disk partitioning and management for Linux",
    "RAID": "Redundant Array of Independent Disks — combining drives for redundancy or performance",
    "NFS": "Network File System — a protocol for sharing files over a network",
    "SMB": "Server Message Block — a protocol for sharing files and printers on a network",

    "TDP": "Thermal Design Power — the maximum heat a component generates under load",
    "SFF": "Small Form Factor — a compact computer case design standard",
    "ATX": "Advanced Technology Extended — the standard motherboard form factor",
    "RAID": "Redundant Array of Independent Disks — combining drives for speed or redundancy",
    "JBOD": "Just a Bunch Of Disks — multiple drives treated as independent volumes",
    "iSCSI": "Internet Small Computer System Interface — storage networking over IP",
    "NIC": "Network Interface Card — hardware that connects a computer to a network",

    "K/D": "Kill/Death Ratio — a measure of player performance in competitive games",
    "TTK": "Time to Kill — the time required to eliminate an opponent in a game",
    "DPS": "Damage Per Second — a measure of weapon or character damage output",
    "AoE": "Area of Effect — attacks that affect all targets within a specified area",
    "DoT": "Damage over Time — gradual damage applied to a target over a period",
    "CC": "Crowd Control — abilities that limit enemy movement or actions",
    "BR": "Battle Royale — a last-player-standing game mode",
    "FFA": "Free For All — a game mode where every player fights for themselves",
    "TDM": "Team Deathmatch — a game mode where teams compete for the most kills",
    "CTF": "Capture The Flag — a game mode where teams compete to capture each other's flag",
    "RPG": "Role-Playing Game — a game where players assume roles in a fictional setting",
    "RTS": "Real-Time Strategy — a game where players build and command armies in real time",
    "MOBA": "Multiplayer Online Battle Arena — team-based strategy games like League of Legends",
    "FOV": "Field of View — the extent of the observable game world visible at any moment",
    "HP": "Hit Points — a measure of how much damage a character can take before dying",
    "XP": "Experience Points — points earned for progressing and leveling up",
    "HUD": "Heads-Up Display — the on-screen interface showing health, ammo, map, etc.",
    "Hitbox": "The invisible collision area around a character that determines if hits land",

    "Algorithm": "A step-by-step set of instructions for solving a specific problem or computation",
    "Bug": "An error or flaw in software that causes unexpected behavior or incorrect results",
    "Certificate": "A digital document that verifies the identity of a website or entity using cryptography",
    "Client": "A device or program that requests services or resources from a server",
    "Compression": "Encoding data to use fewer bits, reducing file size for storage or transmission",
    "Cryptography": "The practice of securing communication by encoding data so only intended parties can read it",
    "Data Structure": "A specialized format for organizing, processing, and storing data (e.g. arrays, trees, queues)",
    "Database": "An organized collection of structured data stored and accessed electronically",
    "Debugging": "The process of identifying and fixing errors or bugs in software",
    "Digital Signature": "A cryptographic method used to verify the authenticity and integrity of a message or document",
    "Encryption": "The process of converting data into a coded form to prevent unauthorized access",
    "Firmware": "Permanent software programmed into read-only memory that controls hardware devices",
    "Frontend": "The client-side part of an application that users interact with directly (UI/UX)",
    "Backend": "The server-side part of an application that handles data processing, storage, and logic",
    "Full-Stack": "Development that encompasses both frontend and backend technologies",
    "Hash": "A fixed-size string generated from input data using a one-way mathematical function",
    "Middleware": "Software that acts as a bridge between different applications, services, or components",
    "Open Source": "Software whose source code is publicly available for use, modification, and distribution",
    "Operating System": "System software that manages hardware, software resources, and provides common services for programs",
    "Patch": "A piece of code designed to fix bugs, vulnerabilities, or improve software after release",
    "Port": "A virtual endpoint for network communication identified by a number (e.g. port 80 for HTTP)",
    "Programming Language": "A formal system of rules for writing instructions that a computer can execute",
    "Proprietary Software": "Software owned by an individual or company with restricted use, modification, and distribution",
    "Protocol": "A set of rules and conventions that define how data is transmitted and received over a network",
    "Proxy": "An intermediary server that forwards requests between clients and other servers",
    "Repository": "A storage location for software packages, source code, or data with version history",
    "Server": "A computer or program that provides services, resources, or data to other computers (clients)",
    "Version Control": "A system that tracks changes to files over time, allowing collaboration and rollback",
    "Windows Registry": "A hierarchical database in Windows that stores configuration settings for the OS and applications",

    "Bandwidth": "The maximum data transfer rate of a network connection, measured in bits per second",
    "Gateway": "A network node that connects two different networks and translates data between them",
    "Loopback": "A virtual network interface (127.0.0.1) used for testing network software on the local machine",
    "Packet": "A small unit of data transmitted over a network, containing headers and payload",
    "Router": "A networking device that forwards data packets between different computer networks",
    "Subnet": "A logical subdivision of an IP network that improves routing efficiency and security",
    "Switch": "A networking device that connects devices within a LAN and forwards data based on MAC addresses",
    "Throughput": "The actual amount of data successfully transmitted over a network in a given time",

    "Malware": "Malicious software designed to damage, disrupt, or gain unauthorized access to a system",
    "Phishing": "A social engineering attack where attackers impersonate legitimate entities to steal credentials",
    "Ransomware": "Malware that encrypts files and demands payment for decryption",
    "Social Engineering": "Manipulating people into divulging confidential information or performing actions",
    "Spyware": "Malware that secretly monitors user activity and collects personal information",
    "Trojan": "Malware disguised as legitimate software to trick users into installing it",
    "Worm": "Self-replicating malware that spreads across networks without user interaction"
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

  function addLexiconSources() {
    if (!document.querySelector('body.lexicon-page')) return;
    var dds = document.querySelectorAll('.lexicon-list dd');
    dds.forEach(function(dd) {
      if (dd.querySelector('.lexicon-source')) return;
      var dt = dd.previousElementSibling;
      if (!dt || !dt.id) return;
      var term = decodeURIComponent(dt.id.replace('term-', ''));
      var q = encodeURIComponent(term);
      var wiki = 'https://en.wikipedia.org/wiki/' + q;
      var urban = 'https://www.urbandictionary.com/define.php?term=' + q;
      var wikt = 'https://en.wiktionary.org/wiki/' + q;
      var mdntech = 'https://developer.mozilla.org/en-US/search?q=' + q;
      var src = document.createElement('div');
      src.className = 'lexicon-source';
      src.innerHTML =
        '<a href="' + wiki + '" target="_blank" rel="noopener" title="Wikipedia"><i class="fab fa-wikipedia-w"></i></a>' +
        '<a href="' + urban + '" target="_blank" rel="noopener" title="Urban Dictionary"><i class="fas fa-book"></i></a>' +
        '<a href="' + wikt + '" target="_blank" rel="noopener" title="Wiktionary"><i class="fas fa-book-open"></i></a>' +
        '<a href="' + mdntech + '" target="_blank" rel="noopener" title="MDN"><i class="fas fa-file-code"></i></a>';
      dd.appendChild(src);
    });
  }

  addLexiconSources();
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
  try {

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

  var overlay, input, resultsEl, filterPillsEl, sortSelectEl, clearBtnEl, searchIndex = null;
  var activeFilter = 'all', activeSort = 'popularity';

  function getSiteRoot() {
    var scripts = document.querySelectorAll('script[src*="scripts.js"]');
    if (scripts.length) {
      var src = scripts[0].src;
      var idx = src.indexOf('/assets/');
      if (idx !== -1) return src.substring(0, idx);
    }
    return '';
  }
  var SITE_ROOT = getSiteRoot();

  function resolveUrl(url) {
    if (!url) return '';
    if (url.indexOf('://') !== -1) return url;
    return SITE_ROOT + (url.charAt(0) === '/' ? url : '/' + url);
  }

  var EMBEDDED_INDEX = [{"title": "Creatives", "url": "/creatives/index.html", "desc": "Music tools, digital art, video editing, AI generators, and fun creative websites.", "cat": "creatives", "popularity": 90, "date": "2026-05-28"}, {"title": "Documentation Archive", "url": "/docs/index.html", "desc": "This section preserves legacy documentation from the websites merged to create this library \u2014 tutorials, Minecraft guides, and more.", "cat": "docs", "popularity": 90, "date": "2026-05-28"}, {"title": "Minecraft Server Guides", "url": "/docs/minecraft.html", "desc": "", "cat": "docs", "popularity": 70, "date": "2026-05-28"}, {"title": "Windows Tutorials", "url": "/docs/tutorials.html", "desc": "", "cat": "docs", "popularity": 70, "date": "2026-05-28"}, {"title": "Gaming", "url": "/gaming/index.html", "desc": "Minecraft servers, Roblox scripts, unblocked games, browser games, and PC gaming optimizations.", "cat": "gaming", "popularity": 90, "date": "2026-05-28"}, {"title": "Tech Library \u2014 Tutorials, Tools, Lexicon & Resources", "url": "/index.html", "desc": "Tutorials, tech lexicon, emergency survival resources, free media alternatives, and curated resources \u2014 all free, all organized.", "cat": "home", "popularity": 100, "date": "2026-05-28"}, {"title": "Tech Lexicon", "url": "/lexicon/index.html", "desc": "227+ tech terms defined \u2014 programming, security, networking, Linux, hardware, gaming, and general tech.", "cat": "lexicon", "popularity": 90, "date": "2025-01-01"}, {"title": "All-In-One Book", "url": "/minecraft/commands/all-in-one-book/index.html", "desc": "/give @p written_book{pages:['[\"\",{\"text\":\"Hey! This is a list of some commands\\\\nhaloboyyetheck \\\\nand giorgakis made:\\\\n\\\\nClick on them to do the command.\\\\n\\\\n\"},{\"text\":\"End Portal spawn egg\",\"cl", "cat": "minecraft", "popularity": 90, "date": "2026-05-28"}, {"title": "Minecraft", "url": "/minecraft/index.html", "desc": "Official Minecraft Wiki \u2014 blocks, items, mechanics, and more.", "cat": "minecraft", "popularity": 90, "date": "2026-05-28"}, {"title": "Minecraft Commands", "url": "/minecraft/commands/index.html", "desc": "Skull giver:", "cat": "minecraft", "popularity": 90, "date": "2026-05-28"}, {"title": "Piracy Resources", "url": "/piracy/index.html", "desc": "Sites, tools, and guides for streaming, downloading, torrenting, gaming, and more \u2014 organized and updated.", "cat": "piracy", "popularity": 90, "date": "2025-01-01"}, {"title": "Databases \u2014 Programming", "url": "/programming/databases.html", "desc": "", "cat": "programming", "popularity": 70, "date": "2026-05-28"}, {"title": "DevOps \u2014 Programming", "url": "/programming/devops.html", "desc": "", "cat": "programming", "popularity": 70, "date": "2026-05-28"}, {"title": "Frameworks \u2014 Programming", "url": "/programming/frameworks.html", "desc": "", "cat": "programming", "popularity": 70, "date": "2026-05-28"}, {"title": "Languages \u2014 Programming", "url": "/programming/languages.html", "desc": "", "cat": "programming", "popularity": 70, "date": "2026-05-28"}, {"title": "Programming", "url": "/programming/index.html", "desc": "Languages, frameworks, databases, DevOps, and learning paths \u2014 everything you need to level up as a developer.", "cat": "programming", "popularity": 90, "date": "2026-05-28"}, {"title": "Projects", "url": "/projects/index.html", "desc": "Tools and projects created and maintained by the community \u2014 SMT, OpenCode, Minecraft resources, and more.", "cat": "projects", "popularity": 90, "date": "2026-05-28"}, {"title": "Browser Extensions", "url": "/resources/extensions.html", "desc": "", "cat": "resources", "popularity": 70, "date": "2026-05-28"}, {"title": "Browser Recommendations", "url": "/resources/browsers.html", "desc": "", "cat": "resources", "popularity": 70, "date": "2026-05-28"}, {"title": "Color & Design Tools", "url": "/resources/color-tools.html", "desc": "", "cat": "resources", "popularity": 70, "date": "2026-05-28"}, {"title": "Cool GitHub Repos", "url": "/resources/github-repos.html", "desc": "", "cat": "resources", "popularity": 70, "date": "2026-05-28"}, {"title": "Cool Websites", "url": "/resources/websites.html", "desc": "", "cat": "resources", "popularity": 70, "date": "2026-05-28"}, {"title": "Design Inspiration", "url": "/resources/design-inspiration.html", "desc": "", "cat": "resources", "popularity": 70, "date": "2026-05-28"}, {"title": "Developer Cheatsheets", "url": "/resources/cheatsheets.html", "desc": "", "cat": "resources", "popularity": 70, "date": "2026-05-28"}, {"title": "Font Resources", "url": "/resources/fonts.html", "desc": "", "cat": "resources", "popularity": 70, "date": "2026-05-28"}, {"title": "Free APIs for Developers", "url": "/resources/free-apis.html", "desc": "", "cat": "resources", "popularity": 70, "date": "2026-05-28"}, {"title": "Free Media & Alternatives", "url": "/resources/freemedia.html", "desc": "", "cat": "resources", "popularity": 70, "date": "2026-05-28"}, {"title": "Free Stock Resources", "url": "/resources/free-stock.html", "desc": "", "cat": "resources", "popularity": 70, "date": "2026-05-28"}, {"title": "Learning Platforms", "url": "/resources/learning-platforms.html", "desc": "", "cat": "resources", "popularity": 70, "date": "2026-05-28"}, {"title": "Resources", "url": "/resources/index.html", "desc": "Curated collections of browser extensions, free media alternatives, learning platforms, design tools, and more.", "cat": "resources", "popularity": 90, "date": "2025-01-01"}, {"title": "Tech Podcasts", "url": "/resources/podcasts.html", "desc": "", "cat": "resources", "popularity": 70, "date": "2026-05-28"}, {"title": "Security", "url": "/security/index.html", "desc": "Guides and resources for DNS privacy, secure browsing, VPNs, password security, and Windows hardening.", "cat": "security", "popularity": 90, "date": "2026-05-28"}, {"title": "All 90+ Tools \u2014 SMT", "url": "/smt/features/index.html", "desc": "Every tool from v1.1 through v2.3 &#8212; networking, activation, system utilities, developer tools, and more.", "cat": "smt", "popularity": 90, "date": "2026-05-28"}, {"title": "SMT \u2014 System Multitool", "url": "/smt/index.html", "desc": "Over 90 powerful tools for Windows &#8212; IP Geolocation, Activation, USB Creator, DNS Changer, and more.", "cat": "smt", "popularity": 90, "date": "2026-05-28"}, {"title": "Emergency Local Servers \u2014 Survival Kit", "url": "/survival/servers.html", "desc": "", "cat": "survival", "popularity": 70, "date": "2026-05-28"}, {"title": "Offline Knowledge Bases \u2014 Survival Kit", "url": "/survival/knowledge-bases.html", "desc": "", "cat": "survival", "popularity": 70, "date": "2026-05-28"}, {"title": "Offline Maps & Navigation \u2014 Survival Kit", "url": "/survival/maps.html", "desc": "", "cat": "survival", "popularity": 70, "date": "2026-05-28"}, {"title": "Offline Wikis & Knowledge \u2014 Survival Kit", "url": "/survival/offline-wikis.html", "desc": "", "cat": "survival", "popularity": 70, "date": "2026-05-28"}, {"title": "Portable Toolkit \u2014 Survival Kit", "url": "/survival/tools.html", "desc": "", "cat": "survival", "popularity": 70, "date": "2026-05-28"}, {"title": "Survival Kit", "url": "/survival/index.html", "desc": "Emergency digital resources \u2014 offline tools, data recovery, system rescue, security breach response, and essential bookmarks.", "cat": "survival", "popularity": 90, "date": "2025-01-01"}, {"title": "Tools", "url": "/tools/index.html", "desc": "A curated collection of batch scripts, online utilities, developer tools, and the legendary SMT.", "cat": "tools", "popularity": 90, "date": "2026-05-28"}, {"title": "API Testing Guide", "url": "/tutorials/api-testing.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Ad Blocking Guide", "url": "/tutorials/adblocking.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Advanced Git", "url": "/tutorials/git-advanced.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Advanced Python", "url": "/tutorials/python-advanced.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "All Tutorials", "url": "/tutorials/index.html", "desc": "Browse step-by-step tech tutorials covering Windows, Linux, programming, networking, and more.", "cat": "tutorials", "popularity": 90, "date": "2025-01-01"}, {"title": "Ansible Automation", "url": "/tutorials/ansible.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Arch Linux Installation Guide", "url": "/tutorials/arch-linux.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Backup Strategies", "url": "/tutorials/backup-strategies.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Bash Scripting Guide", "url": "/tutorials/bash-scripting.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Basics of JavaScript", "url": "/tutorials/JS.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "BitLocker Guide", "url": "/tutorials/bitlocker.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Bootable USB Guide", "url": "/tutorials/bootable-usb.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Browser Privacy Guide", "url": "/tutorials/browser-privacy.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "CI/CD Pipeline Guide", "url": "/tutorials/ci-cd-pipeline.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "CSS Animations Guide", "url": "/tutorials/css-animations.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "CachyOS Installation Guide", "url": "/tutorials/cachyos.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Chromebook Firmware Guide", "url": "/tutorials/chromebook-firmware.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Creating a Basic Batch File", "url": "/tutorials/Batchfile.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Cross\u2011play Minecraft Server Guide", "url": "/tutorials/hajcacmcs.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "DNS Privacy & Filtering Guide", "url": "/tutorials/dns-privacy-guide.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Database Design", "url": "/tutorials/database-design.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Docker & Containerization", "url": "/tutorials/docker.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Docker Compose", "url": "/tutorials/docker-compose.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Emergency USB Toolkit", "url": "/tutorials/emergency-usb-toolkit.html", "desc": "A step-by-step guide to building a portable USB drive loaded with essential software for diagnostics, recovery, productivity, and privacy \u2014 ready for any situation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Encryption Guide", "url": "/tutorials/encryption-guide.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Essential Linux CLI Tools", "url": "/tutorials/linux-cli.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Essential Windows Applications", "url": "/tutorials/windows-apps.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "FFmpeg Guide", "url": "/tutorials/ffmpeg-guide.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Fail2ban", "url": "/tutorials/fail2ban.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "File Sharing with Samba & NFS", "url": "/tutorials/file-sharing-samba-nfs.html", "desc": "This guide covers setting up Samba (SMB/CIFS) and NFS file sharing on a Linux server, configuring shares, securing access, and connecting from Windows, macOS, and Linux clients.", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Firewall Setup Guide", "url": "/tutorials/firewall-setup.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "GitHub Actions", "url": "/tutorials/github-actions.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "HTML & CSS Basics", "url": "/tutorials/html-css-basics.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Hardware Diagnostics Guide", "url": "/tutorials/hardware-diagnostics.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Hiren's Boot CD PE Guide", "url": "/tutorials/hirens-boot-cd.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Home Lab Guide", "url": "/tutorials/homelab-guide.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "How to BSOD your computer/laptop in 2023", "url": "/tutorials/BSOD.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "How to Create High\u2011Quality Embeds (Not GIFs)", "url": "/tutorials/embeds.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "How to Use and Type the ESC Character", "url": "/tutorials/ESC.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Hyprland Tutorial", "url": "/tutorials/hyprland.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "IP Obtainer (Legacy)", "url": "/tutorials/IP-Obtainer.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "ImageMagick Guide", "url": "/tutorials/imagemagick-guide.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Introduction to Python", "url": "/tutorials/Python.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "JavaScript Basics", "url": "/tutorials/javascript-basics.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Kali Linux Basics", "url": "/tutorials/kali-linux.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Kiwix & ZIM Offline Server", "url": "/tutorials/kiwix-zim-server.html", "desc": "Serve Wikipedia, WikiHow, Stack Exchange, and other knowledge bases entirely offline using Kiwix and ZIM files. Perfect for areas with limited or no internet.", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Kubernetes Basics", "url": "/tutorials/kubernetes-basics.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Linux Containers (LXC/LXD)", "url": "/tutorials/linux-containers.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Linux File Permissions", "url": "/tutorials/linux-permissions.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Linux Filesystem Hierarchy", "url": "/tutorials/linux-filesystem.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Linux Networking Guide", "url": "/tutorials/linux-networking.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Linux Overview", "url": "/tutorials/linux.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Linux Package Management", "url": "/tutorials/linux-package-management.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Linux SSH Tips & Tricks", "url": "/tutorials/linux-ssh-tips.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Linux Server Administration", "url": "/tutorials/linux-server.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Load Balancing & Reverse Proxy Guide", "url": "/tutorials/load-balancing.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "MariaDB / MySQL Setup & Administration", "url": "/tutorials/mariadb-setup.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Markdown Guide", "url": "/tutorials/markdown-guide.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Media Server Automation Stack", "url": "/tutorials/media-server-automation.html", "desc": "Automate your entire media library \u2014 from searching and downloading to organizing and streaming. This guide covers the \"*arr\" stack with qBittorrent, Prowlarr, Bazarr, and Stremio integration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Minecraft Server Hosting (Aternos)", "url": "/tutorials/minecraft-aternos.html", "desc": "Aternos is a free Minecraft server hosting service. This guide covers setup, cross-version support, Bedrock crossplay, cracked mode, and common workarounds.", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Neovim/Vim Editor Guide", "url": "/tutorials/neovim.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Network Troubleshooting Guide", "url": "/tutorials/network-troubleshooting.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Networking Basics", "url": "/tutorials/networking-basics.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "NextDNS Setup Guide", "url": "/tutorials/nextdns.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Nginx Web Server", "url": "/tutorials/nginx.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Node.js Guide", "url": "/tutorials/nodejs-guide.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "OSINT Basics", "url": "/tutorials/osint-guide.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Off-Grid Messaging (Briar, Meshtastic, Yggdrasil)", "url": "/tutorials/offgrid-messaging.html", "desc": "Communicate when the internet goes down. These tools let you message others over Bluetooth, LoRa radio, or mesh networking without relying on cell towers or ISPs.", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Offline Developer Knowledge Bases", "url": "/tutorials/offline-dev-knowledge-bases.html", "desc": "Access API documentation, cheat sheets, and developer references without an internet connection. Essential for remote work, travel, or disaster scenarios.", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Offline Maps & Navigation", "url": "/tutorials/offline-maps-navigation.html", "desc": "Navigate anywhere without an internet connection. This guide covers the best tools for downloading maps, importing GPX tracks, and navigating offline.", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Password Security Guide", "url": "/tutorials/password-security.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "PostgreSQL", "url": "/tutorials/postgresql.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "PowerShell Basics", "url": "/tutorials/powershell.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "PowerShell Scripting", "url": "/tutorials/windows-powershell-scripting.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Proxmox VE Setup & Management", "url": "/tutorials/proxmox-setup.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Proxy Guide", "url": "/tutorials/proxy-guide.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "REST API Basics", "url": "/tutorials/api-basics.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Raspberry Pi Setup Guide", "url": "/tutorials/raspberry-pi-setup.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "React Basics", "url": "/tutorials/react-basics.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Redis", "url": "/tutorials/redis.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Regular Expressions Guide", "url": "/tutorials/regex.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "RethinkDNS Tutorial", "url": "/tutorials/rethinkdns.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "SMT System Multitool Guide", "url": "/tutorials/smt-multitool.html", "desc": "SMT (System Multitool) is a batch-powered Windows utility collection with over 90 tools for networking, system configuration, activation, security research, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "SQL Database Basics", "url": "/tutorials/sql-basics.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "SSH Guide", "url": "/tutorials/ssh-guide.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "SSL & HTTPS Certificates", "url": "/tutorials/ssl-certificates.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Security Breach Response", "url": "/tutorials/security-breach-response.html", "desc": "A comprehensive step-by-step guide for identifying, containing, and recovering from a security breach \u2014 from immediate triage to full system restoration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Server Monitoring", "url": "/tutorials/monitoring.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Systemd Service Guide", "url": "/tutorials/systemd-guide.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Tails OS Guide", "url": "/tutorials/tails.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Task Automation Guide", "url": "/tutorials/automation.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Terminal Color Schemes & Themes", "url": "/tutorials/color-schemes.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Tmux Guide", "url": "/tutorials/tmux-guide.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "TypeScript", "url": "/tutorials/typescript.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "VPN Setup Guide", "url": "/tutorials/vpn-setup.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "VS Code Setup & Extensions", "url": "/tutorials/vscode.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Ventoy Advanced Guide", "url": "/tutorials/ventoy.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Virtual Machines Guide", "url": "/tutorials/virtual-machines.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Web Scraping with Python", "url": "/tutorials/web-scraping.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Wi-Fi Security Guide", "url": "/tutorials/wifi-security.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Windows Debloating & Optimization", "url": "/tutorials/windows-debloat.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Windows Deployment Guide", "url": "/tutorials/windows-deployment.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Windows Environment Variables", "url": "/tutorials/windows-environment-variables.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Windows Hardening Guide", "url": "/tutorials/windows-hardening.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Windows Keyboard Shortcuts", "url": "/tutorials/windows-shortcuts.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Windows Recovery & Rescue", "url": "/tutorials/windows-rescue.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Windows Registry Guide", "url": "/tutorials/windows-registry.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Windows Subsystem for Linux (WSL)", "url": "/tutorials/wsl.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "Windows Task Automation", "url": "/tutorials/windows-task-automation.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "WireGuard VPN", "url": "/tutorials/wireguard.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "curl & wget Guide", "url": "/tutorials/curl-wget-guide.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "jq Guide", "url": "/tutorials/jq-guide.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "rsync", "url": "/tutorials/rsync.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}, {"title": "systemd Services", "url": "/tutorials/systemd-services.html", "desc": "", "cat": "tutorials", "popularity": 70, "date": "2026-05-28"}];

  function openSearch() {
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.className = 'search-overlay';
      overlay.innerHTML =
        '<div class="search-modal">' +
          '<div class="search-modal-header">' +
            '<i class="fas fa-search"></i>' +
            '<input type="text" id="search-input" placeholder="Search tutorials, resources, terms..." autocomplete="off" spellcheck="false">' +
            '<button class="search-clear-btn" id="search-clear" aria-label="Clear search"><i class="fas fa-times-circle"></i></button>' +
            '<span class="kbd-hint">ESC</span>' +
            '<button class="search-modal-close" id="search-close"><i class="fas fa-times"></i></button>' +
          '</div>' +
          '<div class="search-toolbar" id="search-toolbar">' +
            '<div class="search-filter-pills" id="search-filter-pills"></div>' +
            '<div class="search-sort-group">' +
              '<label>Sort</label>' +
              '<select class="search-sort-select" id="search-sort-select">' +
                '<option value="popularity" selected>Popularity</option>' +
                '<option value="alpha-asc">A-Z</option>' +
                '<option value="alpha-desc">Z-A</option>' +
                '<option value="date-desc">Recent</option>' +
                '<option value="date-asc">Oldest</option>' +
              '</select>' +
            '</div>' +
          '</div>' +
          '<div class="search-results" id="search-results">' +
            '<div class="search-result-empty"><i class="fas fa-search"></i><p>Start typing to search...</p></div>' +
          '</div>' +
        '</div>';
      document.body.appendChild(overlay);

      input = document.getElementById('search-input');
      resultsEl = document.getElementById('search-results');
      filterPillsEl = document.getElementById('search-filter-pills');
      sortSelectEl = document.getElementById('search-sort-select');
      clearBtnEl = document.getElementById('search-clear');

      document.getElementById('search-close').addEventListener('click', closeSearch);
      clearBtnEl.addEventListener('click', function() { input.value = ''; clearBtnEl.classList.remove('visible'); doSearch(''); input.focus(); });
      overlay.addEventListener('click', function(e) {
        if (e.target === overlay) closeSearch();
      });
      resultsEl.addEventListener('click', function(e) {
        var link = e.target.closest('.search-result-item');
        if (link) {
          closeSearch();
          window.location.href = link.getAttribute('data-href') || link.getAttribute('href');
          e.preventDefault();
        }
      });
      var searchKeydown = function(e) {
        if (e.key === 'Escape') { closeSearch(); return; }
        var items = resultsEl.querySelectorAll('.search-result-item');
        if (!items.length) return;
        if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
          e.preventDefault();
          var active = resultsEl.querySelector('.search-result-item.active');
          var idx = -1;
          if (active) { idx = Array.prototype.indexOf.call(items, active); items[idx].classList.remove('active'); }
          if (e.key === 'ArrowDown') idx = Math.min(idx + 1, items.length - 1);
          else idx = Math.max(idx - 1, 0);
          items[idx].classList.add('active');
          items[idx].scrollIntoView({ block: 'nearest' });
        } else if (e.key === 'Enter') {
          e.preventDefault();
          var active = resultsEl.querySelector('.search-result-item.active') || items[0];
          if (active) { closeSearch(); window.location.href = active.getAttribute('data-href') || active.getAttribute('href'); }
        }
      };
      document.addEventListener('keydown', searchKeydown);

      var debounceTimer;
      input.addEventListener('input', function() {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(function() { doSearch(input.value); }, 150);
      });
      input.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === 'ArrowDown' || e.key === 'ArrowUp') {
          e.preventDefault();
          var ev = new KeyboardEvent('keydown', { key: e.key });
          document.dispatchEvent(ev);
        }
      });

      sortSelectEl.addEventListener('change', function() {
        activeSort = sortSelectEl.value;
        doSearch(input.value);
      });
    }

    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    // Sync sort select with activeSort
    if (sortSelectEl) sortSelectEl.value = activeSort;
    setTimeout(function() {
      var inp = document.getElementById('search-input');
      if (inp) inp.focus();
    }, 200);

    if (!searchIndex) {
      resultsEl.innerHTML = '<div class="search-result-empty"><i class="fas fa-spinner fa-pulse"></i><p>Loading index...</p></div>';
      if (EMBEDDED_INDEX.length) {
        searchIndex = EMBEDDED_INDEX;
        var val = document.getElementById('search-input');
        if (val && val.value) doSearch(val.value);
        else resultsEl.innerHTML = '<div class="search-result-empty"><i class="fas fa-search"></i><p>Start typing to search...</p></div>';
      }
      var scriptTag = document.querySelector('script[src*="scripts.js"]');
      var indexUrl = '';
      if (scriptTag) {
        var scriptDir = scriptTag.src.substring(0, scriptTag.src.lastIndexOf('/'));
        indexUrl = scriptDir.substring(0, scriptDir.lastIndexOf('/') + 1) + 'search-index.json';
      }
      if (indexUrl && SITE_ROOT.indexOf('://') !== -1) {
        fetch(indexUrl).then(function(r) { return r.json(); }).then(function(data) {
          searchIndex = data;
          var val = document.getElementById('search-input');
          if (val && val.value) doSearch(val.value);
        }).catch(function() {});
      }
    }
  }

  function closeSearch() {
    if (overlay) {
      overlay.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  function hlight(text, query) {
    if (!query || !text) return text;
    var re = new RegExp('(' + query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'gi');
    return text.replace(re, '<mark class="search-hl">$1</mark>');
  }

  function renderResultItem(item, query, cat) {
    var icon = CATEGORY_ICONS[cat] || 'fa-file';
    var resolvedUrl = resolveUrl(item.url);
    var titleHtml = hlight(escHtml(item.title), query);
    var descHtml = item.desc ? hlight(escHtml(item.desc.substring(0, 140)), query) : '';
    return '<a href="' + resolvedUrl + '" class="search-result-item" tabindex="-1" data-href="' + resolvedUrl + '">'
      + '<span class="result-icon"><i class="fas ' + icon + '"></i></span>'
      + '<span class="result-info">'
      + '<span class="result-title">' + titleHtml + '</span>'
      + (descHtml ? '<span class="result-desc">' + descHtml + '</span>' : '')
      + '</span></a>';
  }

  function renderFilterPills(categories) {
    if (!filterPillsEl) return;
    var html = '<button class="search-filter-pill' + (activeFilter === 'all' ? ' active' : '') + '" data-filter="all">All</button>';
    var order = ['tutorials', 'resources', 'lexicon', 'survival', 'piracy', 'smt', 'docs', 'programming', 'security', 'tools', 'gaming', 'creatives', 'projects', 'minecraft', 'home'];
    order.forEach(function(cat) {
      if (categories.indexOf(cat) === -1) return;
      var label = cat.charAt(0).toUpperCase() + cat.slice(1);
      html += '<button class="search-filter-pill' + (activeFilter === cat ? ' active' : '') + '" data-filter="' + cat + '">' + label + '</button>';
    });
    filterPillsEl.innerHTML = html;

    // Event delegation for filter pills
    Array.from(filterPillsEl.children).forEach(function(pill) {
      pill.addEventListener('click', function() {
        activeFilter = pill.getAttribute('data-filter');
        var val = input ? input.value : '';
        doSearch(val);
      });
    });
  }

  function doSearch(query) {
    var q = query.trim().toLowerCase();

    // Show/hide clear button
    if (clearBtnEl) {
      if (q) clearBtnEl.classList.add('visible');
      else clearBtnEl.classList.remove('visible');
    }

    if (!q || !searchIndex) {
      resultsEl.innerHTML = '<div class="search-result-empty"><i class="fas fa-search"></i><p>Start typing to search...</p></div>';
      if (filterPillsEl) filterPillsEl.innerHTML = '';
      return;
    }

    // Filter by query
    var results = searchIndex.filter(function(item) {
      return item.title.toLowerCase().indexOf(q) !== -1 ||
             item.desc.toLowerCase().indexOf(q) !== -1;
    });

    // Apply category filter
    if (activeFilter !== 'all') {
      results = results.filter(function(item) { return (item.cat || 'other') === activeFilter; });
    }

    // Collect unique categories for filter pills
    var catsInResults = [];
    results.forEach(function(item) {
      var c = item.cat || 'other';
      if (catsInResults.indexOf(c) === -1) catsInResults.push(c);
    });
    renderFilterPills(catsInResults);

    if (results.length === 0) {
      resultsEl.innerHTML = '<div class="search-result-empty"><i class="fas fa-search-minus"></i><p>No results found for "' + query + '"</p></div>';
      return;
    }

    // Apply sort
    var sorted = results.slice(); // copy
    if (activeSort === 'alpha-asc') {
      sorted.sort(function(a, b) { return a.title.localeCompare(b.title); });
    } else if (activeSort === 'alpha-desc') {
      sorted.sort(function(a, b) { return b.title.localeCompare(a.title); });
    } else if (activeSort === 'date-desc') {
      sorted.sort(function(a, b) { return (b.date || '').localeCompare(a.date || ''); });
    } else if (activeSort === 'date-asc') {
      sorted.sort(function(a, b) { return (a.date || '').localeCompare(b.date || ''); });
    }
    // For popularity, keep original order (category-grouped)

    var html = '<div class="search-result-count">' + results.length + ' result' + (results.length !== 1 ? 's' : '') + '</div>';

    if (activeSort === 'popularity') {
      // Group by category in fixed order
      var groups = {};
      sorted.forEach(function(item) {
        var cat = item.cat || 'other';
        if (!groups[cat]) groups[cat] = [];
        groups[cat].push(item);
      });
      var order = ['tutorials', 'resources', 'lexicon', 'survival', 'piracy', 'smt', 'docs', 'programming', 'security', 'tools', 'gaming', 'creatives', 'projects', 'minecraft', 'home'];
      order.forEach(function(cat) {
        if (!groups[cat]) return;
        html += '<div class="search-result-group"><h3>' + cat.charAt(0).toUpperCase() + cat.slice(1) + '</h3>';
        groups[cat].forEach(function(item) { html += renderResultItem(item, query, cat); });
        html += '</div>';
      });
    } else {
      // Flat list sorted by selected criteria
      sorted.forEach(function(item) {
        var cat = item.cat || 'other';
        html += renderResultItem(item, query, cat);
      });
    }

    resultsEl.innerHTML = html;
    resultsEl.scrollTop = 0;
  }

  function escHtml(str) {
    if (!str) return '';
    return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  // Trigger search from the nav search bar
  var searchBar = document.getElementById('search-bar');
  if (searchBar) {
    searchBar.addEventListener('click', function(e) {
      if (e.target.tagName !== 'INPUT') openSearch();
    });
    var barInput = document.getElementById('search-bar-input');
    if (barInput) {
      barInput.addEventListener('focus', openSearch);
      barInput.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') { e.preventDefault(); openSearch(); }
      });
    }
  }

  // Also support old search-toggle for pages not yet updated
  var oldToggle = document.getElementById('search-toggle');
  if (oldToggle) oldToggle.addEventListener('click', openSearch);

  document.addEventListener('keydown', function(e) {
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
      e.preventDefault();
      openSearch();
    }
  });

  // Preload search index in background
  if (EMBEDDED_INDEX.length) {
    searchIndex = EMBEDDED_INDEX;
  } else if ('requestIdleCallback' in window) {
    requestIdleCallback(function() {
      var stag = document.querySelector('script[src*="scripts.js"]');
      if (stag) {
        var sdir = stag.src.substring(0, stag.src.lastIndexOf('/'));
        var sroot = sdir.substring(0, sdir.lastIndexOf('/') + 1);
        fetch(sroot + 'search-index.json').then(function(r) { return r.json(); }).then(function(data) { searchIndex = data; }).catch(function() {});
      }
    });
  }

  } catch(e) {}
})();

/* ===== Copy Code Button ===== */
(function(){
  try {
    document.addEventListener('click', function(e) {
      var btn = e.target.closest('.copy-code-btn');
      if (!btn) return;
      var code = btn.parentNode.querySelector('code');
      if (!code) return;
      var text = code.textContent;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function() {
          var orig = btn.innerHTML;
          btn.innerHTML = '<i class="fas fa-check"></i>';
          setTimeout(function() { btn.innerHTML = orig; }, 2000);
        });
      }
    });

    var pres = document.querySelectorAll('pre');
    pres.forEach(function(pre) {
      if (pre.querySelector('.copy-code-btn')) return;
      var btn = document.createElement('button');
      btn.className = 'copy-code-btn';
      btn.innerHTML = '<i class="fas fa-copy"></i>';
      btn.setAttribute('aria-label', 'Copy code');
      pre.style.position = 'relative';
      pre.appendChild(btn);
    });
  } catch(e) {}
})();

/* ===== Search Modal Focus Trap ===== */
(function(){
  try {
    document.addEventListener('keydown', function(e) {
      if (e.key !== 'Tab') return;
      var overlay = document.querySelector('.search-overlay.open');
      if (!overlay) return;
      var focusable = overlay.querySelectorAll('input, button, select, [tabindex]:not([tabindex="-1"])');
      if (!focusable.length) return;
      var first = focusable[0];
      var last = focusable[focusable.length - 1];
      if (e.shiftKey) {
        if (document.activeElement === first) {
          e.preventDefault();
          last.focus();
        }
      } else {
        if (document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    });
  } catch(e) {}
})();
