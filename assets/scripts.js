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
    "Worm": "Self-replicating malware that spreads across networks without user interaction",

    "Vencord": "A Discord client mod that adds plugins, themes, and quality-of-life features through a browser extension or standalone client",
    "Vesktop": "A standalone desktop client for Discord that bundles Vencord mods, offering enhanced functionality over the official app",
    "Spicetify": "A command-line tool for customizing the Spotify desktop client with themes, extensions, and ad-blocking capabilities",
    "ReVanced": "A tool that patches Android APKs to add features, remove ads, and modify app behavior without requiring root access",
    "MicroG": "An open-source reimplementation of Google Play Services that enables ReVanced and other modded apps to work",
    "F-Droid": "An open-source app store for Android that hosts only free and open-source software with verified repositories",
    "Aurora Store": "An alternative Google Play client for Android that allows anonymous account access and app downloads without tracking",
    "Shizuku": "An Android system tool that provides app permissions via ADB without requiring root, enabling advanced app management",
    "Hail": "An Android app freezer that disables or hides unwanted apps without uninstalling them, using Shizuku or root",
    "LocalSend": "An open-source cross-platform file transfer app that works over the local network without internet, similar to AirDrop",
    "Croc": "A CLI file transfer tool that uses end-to-end encryption and a relay server for secure peer-to-peer transfers",
    "Chitralaya": "An Android app for backing up media to Telegram chats, using Telegram's free cloud storage as a backup backend",
    "Morphe": "A peer-to-peer file synchronization tool for Android that transfers data directly between devices without cloud servers",
    "Paysafe": "A prepaid online payment method that allows anonymous transactions without linking a bank account or credit card"
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

  window.__TL = window.__TL || {};
  window.__TL.lexicon = LEXICON;
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
    'windows-shortcuts': 'windows',
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
    'home': 'fa-home',
    'buying-guide': 'fa-shopping-cart'
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

  var EMBEDDED_INDEX = [{"title": "Accessories Buyer's Guide", "url": "/buying-guide/accessories.html", "desc": "Keyboards, mice, webcams, microphones, docks, and cables \u2014 the gear that completes your setup.", "cat": "buying-guide", "popularity": 70, "date": "2026-05-29"}, {"title": "Audio Buyer's Guide", "url": "/buying-guide/audio.html", "desc": "IEMs, headphones, speakers, DACs, and amps \u2014 navigate the world of personal audio with confidence.", "cat": "buying-guide", "popularity": 70, "date": "2026-05-29"}, {"title": "Desktop Buyer's Guide", "url": "/buying-guide/desktops.html", "desc": "Office, Gaming, Creator, or Server \u2014 choose your next desktop build with confidence.", "cat": "buying-guide", "popularity": 70, "date": "2026-05-29"}, {"title": "Laptop Buyer's Guide", "url": "/buying-guide/laptops.html", "desc": "Chromebook, Ultrabook, Gaming, or Workstation \u2014 find the right portable powerhouse for your workflow.", "cat": "buying-guide", "popularity": 70, "date": "2026-05-29"}, {"title": "Phone Buyer's Guide", "url": "/buying-guide/phones.html", "desc": "From budget workhorses to flagship cameras \u2014 find the right phone for your needs and budget.", "cat": "buying-guide", "popularity": 70, "date": "2026-05-29"}, {"title": "Tablet Buyer's Guide", "url": "/buying-guide/tablets.html", "desc": "iPad, Android, or Windows \u2014 choose the right tablet for creativity, productivity, or entertainment.", "cat": "buying-guide", "popularity": 70, "date": "2026-05-29"}, {"title": "Tech Buyer's Guide", "url": "/buying-guide/index.html", "desc": "Smart recommendations across every budget tier. Whether you are stretching every dollar or building a no-compromise setup, these guides cover phones, laptops, desktops, tablets, audio gear, and access", "cat": "buying-guide", "popularity": 90, "date": "2026-05-29"}, {"title": "Creatives", "url": "/creatives/index.html", "desc": "Music tools, digital art, video editing, AI generators, and fun creative websites.", "cat": "creatives", "popularity": 90, "date": "2026-05-29"}, {"title": "Documentation Archive", "url": "/docs/index.html", "desc": "This section preserves legacy documentation from the websites merged to create this library \u2014 tutorials, Minecraft guides, and more.", "cat": "docs", "popularity": 90, "date": "2026-05-29"}, {"title": "Minecraft Server Guides", "url": "/docs/minecraft.html", "desc": "How to host a crossplay, any-version, and cracked Minecraft server for free \u2014 originally from schooicodes.github.io/hajcacmcs.", "cat": "docs", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Tutorials", "url": "/docs/tutorials.html", "desc": "This section preserves the legacy tutorials from the original site.", "cat": "docs", "popularity": 70, "date": "2026-05-29"}, {"title": "Gaming", "url": "/gaming/index.html", "desc": "Minecraft servers, Roblox scripts, unblocked games, browser games, and PC gaming optimizations.", "cat": "gaming", "popularity": 90, "date": "2026-05-29"}, {"title": "404 \u2014 Page Not Found", "url": "/404.html", "desc": "Page Not Found", "cat": "home", "popularity": 70, "date": "2026-05-29"}, {"title": "Tech Library \u2014 Tutorials, Tools, Lexicon & Resources", "url": "/index.html", "desc": "Tutorials, tech lexicon, emergency survival resources, free media alternatives, and curated resources \u2014 all free, all organized.", "cat": "home", "popularity": 100, "date": "2026-05-29"}, {"title": "Tech Lexicon", "url": "/lexicon/index.html", "desc": "240+ tech terms defined \u2014 programming, security, networking, Linux, hardware, gaming, and general tech.", "cat": "lexicon", "popularity": 90, "date": "2025-01-01"}, {"title": "All-In-One Book", "url": "/minecraft/commands/all-in-one-book/index.html", "desc": "/give @p written_book{pages:['[\"\",{\"text\":\"Hey! This is a list of some commands\\\\nhaloboyyetheck \\\\nand giorgakis made:\\\\n\\\\nClick on them to do the command.\\\\n\\\\n\"},{\"text\":\"End Portal spawn egg\",\"cl", "cat": "minecraft", "popularity": 90, "date": "2026-05-29"}, {"title": "Minecraft", "url": "/minecraft/index.html", "desc": "Official Minecraft Wiki \u2014 blocks, items, mechanics, and more.", "cat": "minecraft", "popularity": 90, "date": "2026-05-29"}, {"title": "Minecraft Commands", "url": "/minecraft/commands/index.html", "desc": "Skull giver:", "cat": "minecraft", "popularity": 90, "date": "2026-05-29"}, {"title": "Additional Piracy Sources", "url": "/piracy/additional-sources.html", "desc": "Expanded list of sources organized by type \u2014 direct download, torrent, DDL forums, scene trackers, and safety-rated recommendations. Always use a VPN and exercise caution.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Android Piracy Guide &#8212; Piracy", "url": "/piracy/android-piracy-guide.html", "desc": "Comprehensive guide to Android piracy: Aurora Store, modded APKs, Lucky Patcher, ReVanced, Shizuku, and the best APK sites.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Anime Piracy Guide &#8212; Piracy", "url": "/piracy/anime-piracy-guide.html", "desc": "Complete guide to anime piracy: streaming sites, download groups (SubsPlease, Erai), Nyaa torrents, fansub groups, and automation with SeaDex.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Complete Torrenting Guide &#8212; Piracy", "url": "/piracy/torrenting-guide.html", "desc": "The definitive guide to torrenting: clients, trackers, safety, and full automation with Sonarr/Radarr. Everything you need to know to torrent safely and effectively.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Debrid Services Comparison &#8212; Piracy", "url": "/piracy/debrid-services.html", "desc": "Compare the major debrid services: features, pricing, speed tests, and which one to choose for your use case.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Direct Download Sites & Tools &#8212; Piracy", "url": "/piracy/direct-download-guide.html", "desc": "Master direct downloads: top DDL sites, JDownloader2, IDM setup, bypassing limits, and staying safe while downloading.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Ebook & Audiobook Piracy &#8212; Piracy", "url": "/piracy/ebook-piracy-guide.html", "desc": "Everything for book pirates: Z-Library, Anna\u2019s Archive, LibGen, MyAnonamouse (MAM), Readarr automation, and more.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Gaming Piracy Guide &#8212; Piracy", "url": "/piracy/gaming-piracy-guide.html", "desc": "Your complete guide to gaming piracy: FitGirl, DODI repacks, SteamRIP, console emulation, ROMs, and staying safe.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Media Servers for Piracy &#8212; Piracy", "url": "/piracy/media-server-piracy.html", "desc": "Plex, Jellyfin, Sonarr/Radarr, Prowlarr, Overseerr, Usenet/Torrent integration for the ultimate media setup.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Music Piracy Guide &#8212; Piracy", "url": "/piracy/music-piracy-guide.html", "desc": "Complete guide to music piracy: Soulseek, Deemix, Lucida, BlockTheSpot, Freezer, Telegram bots for music, and more.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Piracy Resources", "url": "/piracy/index.html", "desc": "Sites, tools, and guides for streaming, downloading, torrenting, gaming, and more \u2014 organized and updated.", "cat": "piracy", "popularity": 90, "date": "2025-01-01"}, {"title": "Private Tracker Guide &#8212; Piracy", "url": "/piracy/private-trackers.html", "desc": "Everything about private trackers: ratio systems, getting invited, the top trackers, maintaining ratio, and using seedboxes.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Real-Debrid Guide &#8212; Piracy", "url": "/piracy/real-debrid-guide.html", "desc": "Unlock premium file hosting with Real-Debrid. Learn setup, Stremio integration, JDownloader, and how it compares to alternatives like AllDebrid and Premiumize.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Scene Release Groups & Standards &#8212; Piracy", "url": "/piracy/scene-releases.html", "desc": "The inner workings of the warez scene: release naming conventions, types, groups, P2P vs Scene, and how to find scene releases.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Software Piracy Guide &#8212; Piracy", "url": "/piracy/software-piracy-guide.html", "desc": "Complete guide to pirating software: FileCR, WAREZ, DDoSecrets, portable apps, safe cracking, and Microsoft activation tools.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Staying Safe While Pirating &#8212; Piracy", "url": "/piracy/safe-piracy.html", "desc": "Antivirus setup, sandboxing, fake sites, VirusTotal, adblockers, DNS over HTTPS, separate browser profile.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Streaming Sites Guide &#8212; Piracy", "url": "/piracy/streaming-sites-guide.html", "desc": "Top streaming sites, anime streaming, live TV, sports streaming, ad blocking, and backup sites.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Stremio + Torrentio Setup &#8212; Piracy", "url": "/piracy/stremio-setup.html", "desc": "Transform Stremio into a Netflix-like experience with Torrentio and Real-Debrid. Watch any movie or show instantly with premium cached streams.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Torrent Automation Suite &#8212; Piracy", "url": "/piracy/torrent-automation.html", "desc": "Sonarr, Radarr, Prowlarr, qBittorrent, Overseerr, Usenet automation, and the complete Docker Compose stack.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Usenet Guide &#8212; Piracy", "url": "/piracy/usenet-guide.html", "desc": "Learn about Usenet: providers, indexers, download clients, and how to automate everything with Radarr/Sonarr. The superior alternative to torrenting for many users.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "VPN Guide for Piracy &#8212; Piracy", "url": "/piracy/vpn-for-piracy.html", "desc": "Why you need a VPN, features for piracy, top VPNs (Mullvad, Proton, AirVPN), port forwarding, split tunneling, kill switch.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "iOS Piracy Guide &#8212; Piracy", "url": "/piracy/ios-piracy-guide.html", "desc": "Master iOS piracy: AltStore, SideStore, TrollStore, signing services, AppCake, and emulators on iPhone and iPad.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Databases \u2014 Programming", "url": "/programming/databases.html", "desc": "Relational, NoSQL, and NewSQL databases \u2014 understanding their trade-offs and choosing the right one for your project.", "cat": "programming", "popularity": 70, "date": "2026-05-29"}, {"title": "DevOps \u2014 Programming", "url": "/programming/devops.html", "desc": "CI/CD pipelines, containerization, monitoring, and infrastructure as code \u2014 the essential tooling for modern software delivery.", "cat": "programming", "popularity": 70, "date": "2026-05-29"}, {"title": "Frameworks \u2014 Programming", "url": "/programming/frameworks.html", "desc": "A comprehensive overview of frontend, backend, and full-stack frameworks for modern web development.", "cat": "programming", "popularity": 70, "date": "2026-05-29"}, {"title": "Languages \u2014 Programming", "url": "/programming/languages.html", "desc": "A side-by-side comparison of popular programming languages covering typing systems, performance, use cases, and learning curves.", "cat": "programming", "popularity": 70, "date": "2026-05-29"}, {"title": "Programming", "url": "/programming/index.html", "desc": "Languages, frameworks, databases, DevOps, and learning paths \u2014 everything you need to level up as a developer.", "cat": "programming", "popularity": 90, "date": "2026-05-29"}, {"title": "Projects", "url": "/projects/index.html", "desc": "Tools and projects created and maintained by the community \u2014 SMT, OpenCode, Minecraft resources, and more.", "cat": "projects", "popularity": 90, "date": "2026-05-29"}, {"title": "Browser Extensions", "url": "/resources/extensions.html", "desc": "Essential browser extensions for privacy, productivity, development, and fun \u2014 curated for Firefox and Chromium browsers.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Browser Recommendations", "url": "/resources/browsers.html", "desc": "Recommendations for modern, privacy-focused web browsers \u2014 from everyday use to maximum anonymity.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Color & Design Tools", "url": "/resources/color-tools.html", "desc": "Palette generators, gradient tools, contrast checkers, and design inspiration platforms for beautiful interfaces.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Cool GitHub Repos", "url": "/resources/github-repos.html", "desc": "A curated collection of awesome GitHub repos \u2014 tools, learning resources, fun projects, privacy tools, and Linux utilities.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Cool Websites", "url": "/resources/websites.html", "desc": "A curated list of interesting and useful websites, tools, and services.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Design Inspiration", "url": "/resources/design-inspiration.html", "desc": "Find inspiration for your next project \u2014 landing pages, UI designs, color palettes, and component libraries from the best designers.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Developer Cheatsheets", "url": "/resources/cheatsheets.html", "desc": "Quick reference guides for Git, Docker, Linux, SQL, regex, editors, and more \u2014 everything a developer needs at their fingertips.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Font Resources", "url": "/resources/fonts.html", "desc": "A curated collection of font foundries, developer-friendly coding fonts, icon fonts, and web font tools.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Free APIs for Developers", "url": "/resources/free-apis.html", "desc": "Free public APIs to power your projects \u2014 weather, news, music, games, finance, and fun data sources. Many require no authentication at all.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Free Media & Alternatives", "url": "/resources/freemedia.html", "desc": "A curated list of free alternatives to paid services \u2014 inspired by FMHY (Free Media Heck Yeah). Every single thing listed here costs exactly $0. Replace Netflix, Spotify, Photoshop, AutoCAD, and more ", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Free Stock Resources", "url": "/resources/free-stock.html", "desc": "High-quality free stock photos, videos, audio, and icons for your projects \u2014 all completely free to use.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Learning Platforms", "url": "/resources/learning-platforms.html", "desc": "Curated learning platforms for every skill level \u2014 from free courses to interactive coding challenges and technical references.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Resources", "url": "/resources/index.html", "desc": "Curated collections of browser extensions, free media alternatives, learning platforms, design tools, and more.", "cat": "resources", "popularity": 90, "date": "2025-01-01"}, {"title": "Tech Podcasts", "url": "/resources/podcasts.html", "desc": "The best tech podcasts for developers, security enthusiasts, and Linux fans \u2014 from web development to cybersecurity and open source.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Security", "url": "/security/index.html", "desc": "Guides and resources for DNS privacy, secure browsing, VPNs, password security, and Windows hardening.", "cat": "security", "popularity": 90, "date": "2026-05-29"}, {"title": "All 90+ Tools \u2014 SMT", "url": "/smt/features/index.html", "desc": "Every tool from v1.1 through v2.3 &#8212; networking, activation, system utilities, developer tools, and more.", "cat": "smt", "popularity": 90, "date": "2026-05-29"}, {"title": "SMT \u2014 System Multitool", "url": "/smt/index.html", "desc": "Over 90 powerful tools for Windows &#8212; IP Geolocation, Activation, USB Creator, DNS Changer, and more.", "cat": "smt", "popularity": 90, "date": "2026-05-29"}, {"title": "Advanced Backup Strategies \u2014 Survival Kit", "url": "/survival/backup-strategies-deep.html", "desc": "Deep dive into backup strategies: 3-2-1 rule, local and offsite backups, cloud options, rotation schemes, restore testing, and automation.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "BIOS/UEFI Recovery \u2014 Survival Kit", "url": "/survival/bios-recovery.html", "desc": "Recovering a system with corrupted BIOS/UEFI firmware - CMOS reset, Flashback, CH341A programmers, and debricking motherboards.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Building Your Emergency USB Drive \u2014 Survival Kit", "url": "/survival/emergency-usb.html", "desc": "Everything you need to build a doomsday-ready USB drive: multi-boot setup, portable apps, recovery ISOs, and comprehensive testing - all pre-loaded and ready to run on any computer.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Data Recovery Guide \u2014 Survival Kit", "url": "/survival/data-recovery.html", "desc": "Step-by-step guide to recovering lost data from hard drives, SSDs, memory cards, and RAID arrays - from software recovery to professional lab services.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Digital Emergency Prep Checklist \u2014 Survival Kit", "url": "/survival/emergency-prep-checklist.html", "desc": "A comprehensive checklist for digital emergency preparedness - immediate actions, weekly prep, monthly checks, essential downloads, and communication planning.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Digital Estate Planning \u2014 Survival Kit", "url": "/survival/digital-will.html", "desc": "Plan for your digital afterlife - password inheritance via Bitwarden, dead man switches, document storage, and family instructions.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Emergency Local Servers \u2014 Survival Kit", "url": "/survival/servers.html", "desc": "Keep your local network running when the internet goes dark. Local DNS, file sharing, mesh messaging, portable web servers, and off-grid communication for disaster scenarios.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Encrypted Communication Guide \u2014 Survival Kit", "url": "/survival/encrypted-comms.html", "desc": "Set up end-to-end encrypted communication - Signal, Session, Keybase, PGP email, Matrix/Element, and WireGuard VPN.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Hardware Diagnostics \u2014 Survival Kit", "url": "/survival/hardware-diagnostics.html", "desc": "Diagnose failing hardware - RAM testing with MemTest86, storage diagnostics with CrystalDiskInfo, CPU/GPU stress testing, PSU testing, and thermal diagnostics.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Malware Removal Guide \u2014 Survival Kit", "url": "/survival/malware-removal.html", "desc": "A systematic approach to removing malware - from immediate isolation to deep cleaning, rootkit removal, and prevention.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Communication \u2014 Survival Kit", "url": "/survival/offline-communication.html", "desc": "Communicate without internet or cellular - Briar mesh, Meshtastic devices, LoRa radio, goTenna, and ham radio basics.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Knowledge Bases \u2014 Survival Kit", "url": "/survival/knowledge-bases.html", "desc": "Carry a developer's reference library in your pocket. DevDocs, Zeal/Dash docsets, MDN offline, tldr-pages, man pages, cheat sheets, and local wiki systems for when the internet is gone.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Maps & Navigation \u2014 Survival Kit", "url": "/survival/maps.html", "desc": "Never get lost \u2014 even without a data connection. Organic Maps, Maps.me, OsmAnd, Google Maps offline, GPS fundamentals, and downloading whole countries for offline use.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Wikis & Knowledge \u2014 Survival Kit", "url": "/survival/offline-wikis.html", "desc": "Carry the sum of human knowledge in your pocket. Kiwix, ZIM archives, and offline readers for Wikipedia, Wiktionary, WikiHow, Stack Exchange, Project Gutenberg, and more.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Password Reset & Recovery \u2014 Survival Kit", "url": "/survival/password-reset.html", "desc": "Reset or recover passwords on Windows, Linux, and macOS - plus Bitwarden emergency access and 2FA recovery codes.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Portable Toolkit \u2014 Survival Kit", "url": "/survival/tools.html", "desc": "A curated collection of portable apps for Windows, Linux, and cross-platform tools that run entirely from a USB stick. No installation, no traces \u2014 your digital go-bag in software form.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Ransomware Response \u2014 Survival Kit", "url": "/survival/ransomware-response.html", "desc": "What to do when ransomware strikes - isolate, identify the strain, find decryption tools, and recover without paying criminals.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Solar & Off-Grid Power \u2014 Survival Kit", "url": "/survival/solar-charging.html", "desc": "Keep devices running off-grid - solar panel basics, power station sizing, battery types, USB power banks, inverters, and practical tips for extended outages.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Survival Kit", "url": "/survival/index.html", "desc": "Emergency digital resources \u2014 offline tools, data recovery, system rescue, security breach response, and essential bookmarks.", "cat": "survival", "popularity": 90, "date": "2025-01-01"}, {"title": "Surviving Network Outages \u2014 Survival Kit", "url": "/survival/network-outage.html", "desc": "How to survive when the internet goes down - diagnosing outages, local network access, cellular failover, offline entertainment, mesh networks.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "System Rescue with Live CDs \u2014 Survival Kit", "url": "/survival/system-rescue.html", "desc": "How to use Live CDs and USB rescue environments to recover unbootable systems - covering Hiren Boot CD, SystemRescue, Rescatux, and bootloader repair.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Tools", "url": "/tools/index.html", "desc": "A curated collection of batch scripts, online utilities, developer tools, and the legendary SMT.", "cat": "tools", "popularity": 90, "date": "2026-05-29"}, {"title": "AI Models & Tools Directory", "url": "/tutorials/ai-models-directory.html", "desc": "A curated directory of the best AI models, tools, and platforms across every category \u2014 from large language models to local AI runners.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "API Design Best Practices", "url": "/tutorials/api-design-best-practices.html", "desc": "Design robust RESTful and GraphQL APIs with proper status codes and auth.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "API Testing Guide", "url": "/tutorials/api-testing.html", "desc": "Test REST and GraphQL APIs \u2014 curl, Postman/Insomnia, HTTPie, status codes, auth testing, and automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "APK Sideloading Guide", "url": "/tutorials/apk-sideloading.html", "desc": "Everything you need to know about installing Android apps from outside the Play Store \u2014 methods, tools, safety, and best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "ASCII, Unicode &amp; Encoding Explained", "url": "/tutorials/ascii-unicode-encoding.html", "desc": "Understand character encoding \u2014 ASCII, UTF-8, UTF-16, code points, and normalization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Active Recall &amp; Spaced Repetition", "url": "/tutorials/active-recall.html", "desc": "Learn how to study smarter with evidence-based techniques that boost long-term retention.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Ad Blocking Guide", "url": "/tutorials/adblocking.html", "desc": "Block ads and trackers with uBlock Origin, Pi-hole, AdGuard Home, NextDNS, and browser-based filtering.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Advanced Git", "url": "/tutorials/git-advanced.html", "desc": "Beyond the basics \u2014 rebasing, cherry-picking, interactive rebase, bisect, hooks, submodules, reflog, and workflow strategies.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Advanced Python", "url": "/tutorials/python-advanced.html", "desc": "Level up from Python basics \u2014 decorators, generators, context managers, async/await, OOP, type hints, and performance.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Advanced Regex Patterns &amp; Tricks", "url": "/tutorials/regex-advanced.html", "desc": "Go beyond basic regex with lookaheads, backreferences, atomic groups, and performance.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Advanced SQL Queries &amp; Optimization", "url": "/tutorials/sql-advanced.html", "desc": "Master window functions, CTEs, indexing, and query performance tuning.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "All Tutorials", "url": "/tutorials/index.html", "desc": "Browse step-by-step tech tutorials covering Windows, Linux, programming, networking, and more.", "cat": "tutorials", "popularity": 90, "date": "2025-01-01"}, {"title": "Anki Customization &amp; Advanced Features", "url": "/tutorials/anki-customization.html", "desc": "Supercharge Anki with add-ons, card styling, FSRS scheduler, and sync.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Ansible Automation", "url": "/tutorials/ansible.html", "desc": "Automate servers, deploy applications, and manage infrastructure at scale with Ansible.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Ansible Playbooks Deep Dive", "url": "/tutorials/ansible-playbooks-deep-dive.html", "desc": "Advanced playbook patterns, dynamic inventory, collections, and AWX.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Arch Linux Installation Guide", "url": "/tutorials/arch-linux.html", "desc": "From bare metal to a fully functional Arch Linux system \u2014 a complete step-by-step walkthrough.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Audio Editing with Audacity", "url": "/tutorials/audacity-audio-editing.html", "desc": "Record, edit, and produce audio with Audacity \u2014 noise reduction, effects, and multitrack.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "BIOS vs UEFI vs Legacy Boot", "url": "/tutorials/bios-uefi-boot.html", "desc": "Understand the differences between BIOS, UEFI, Secure Boot, and boot process.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Backup Strategies", "url": "/tutorials/backup-strategies.html", "desc": "Reliable backup strategies \u2014 3-2-1 rule, rsync, Borg, restic, Duplicati, cloud backups, and automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Bash Scripting Guide", "url": "/tutorials/bash-scripting.html", "desc": "Learn Bash scripting from the ground up \u2014 variables, conditionals, loops, functions, error handling, and automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Basics of JavaScript", "url": "/tutorials/JS.html", "desc": "JavaScript is a versatile programming language used for interactive web development.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Big Data Tools: Hadoop &amp; Spark", "url": "/tutorials/big-data-tools.html", "desc": "Introduction to big data processing with Hadoop, Spark, Hive, and the data lake ecosystem.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "BitLocker Guide", "url": "/tutorials/bitlocker.html", "desc": "Full-disk encryption on Windows \u2014 enabling, managing, recovery, and alternatives.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Blender 3D Modeling Introduction", "url": "/tutorials/blender-3d-basics.html", "desc": "Start your 3D journey with Blender \u2014 modeling, materials, lighting, and rendering.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Bootable USB Guide", "url": "/tutorials/bootable-usb.html", "desc": "This guide covers creating bootable USB media for Linux distributions, Windows installers, and recovery tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Browser Fingerprinting &amp; Anti-Detection", "url": "/tutorials/browser-fingerprinting.html", "desc": "How browser fingerprinting works and how to protect your privacy online.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Browser Privacy Guide", "url": "/tutorials/browser-privacy.html", "desc": "How to lock down your browser for maximum privacy \u2014 ad blocking, tracker blocking, secure DNS, and essential settings.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "C++ Programming for Beginners", "url": "/tutorials/cpp-basics.html", "desc": "Learn C++ \u2014 pointers, classes, STL, and modern C++ features.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "CI/CD Pipeline Guide", "url": "/tutorials/ci-cd-pipeline.html", "desc": "Build, test, and deploy automatically with continuous integration and continuous delivery pipelines.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "CI/CD with Jenkins Pipeline", "url": "/tutorials/ci-cd-jenkins.html", "desc": "Set up Jenkins for continuous integration and delivery.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "CSS Animations Guide", "url": "/tutorials/css-animations.html", "desc": "Create smooth CSS animations \u2014 transitions, keyframes, transforms, performance tips, and practical examples.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "CachyOS Installation Guide", "url": "/tutorials/cachyos.html", "desc": "CachyOS is a fast, lightweight Linux distribution based on Arch Linux.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Chitralaya", "url": "/tutorials/chitralaya.html", "desc": "Self-hosted lightweight image gallery and media server for organizing and sharing photos.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Chromebook Firmware Guide", "url": "/tutorials/chromebook-firmware.html", "desc": "Everything about flashing, backing up, and replacing Chromebook firmware \u2014 from verified boot to MrChromebox.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cloud Backup Strategies", "url": "/tutorials/cloud-backup-strategies.html", "desc": "Comprehensive guide to backing up your data using cloud providers, encryption, and automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cloud Computing Overview", "url": "/tutorials/cloud-computing-overview.html", "desc": "Compare AWS, GCP, and Azure services for compute, storage, networking, and serverless.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Containerization vs Virtualization", "url": "/tutorials/containerization-vs-virtualization.html", "desc": "Understand the differences between containers and VMs, and when to use each.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cool Apps & Tools Directory", "url": "/tutorials/cool-apps-directory.html", "desc": "Hand-picked collection of the most useful applications across productivity, development, media, utilities, and security.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cracked & Pre-Installed Steam Games Guide", "url": "/tutorials/cracked-steam-games.html", "desc": "A comprehensive guide to understanding game cracking, finding reliable pre-installed releases, using Steam emulators for LAN play, and staying safe \u2014 with strong legal disclaimers.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Creating a Basic Batch File", "url": "/tutorials/Batchfile.html", "desc": "A batch file is a script for Windows command\u2011line interpreter, used to automate tasks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Croc", "url": "/tutorials/croc.html", "desc": "CLI tool for encrypted peer-to-peer file transfers between any two computers.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cross\u2011play Minecraft Server Guide", "url": "/tutorials/hajcacmcs.html", "desc": "This tutorial is preserved from the original repository.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "DNS Privacy & Filtering Guide", "url": "/tutorials/dns-privacy-guide.html", "desc": "Block ads, trackers, and malware at the DNS level with Pi-hole, AdGuard Home, and NextDNS.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "DNS Records Deep Dive", "url": "/tutorials/dns-records-deep-dive.html", "desc": "A comprehensive guide to A, AAAA, CNAME, MX, TXT, NS, SRV, and DNSSEC records.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "DaVinci Resolve Editing Basics", "url": "/tutorials/davinci-resolve-basics.html", "desc": "Learn video editing with DaVinci Resolve \u2014 cut, color, audio, and delivery.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Database Design", "url": "/tutorials/database-design.html", "desc": "Design efficient databases \u2014 normalization, indexing, relationships, ERDs, query optimization, and choosing between SQL/NoSQL.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Digital Zettelkasten with Obsidian", "url": "/tutorials/digital-zettelkasten.html", "desc": "Build a networked knowledge base using Zettelkasten principles in Obsidian.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Docker & Containerization", "url": "/tutorials/docker.html", "desc": "Everything you need to know about Docker \u2014 from containers to Compose, registries to best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Docker Compose", "url": "/tutorials/docker-compose.html", "desc": "Define and run multi-container Docker applications with ease using Docker Compose.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Emergency USB Toolkit", "url": "/tutorials/emergency-usb-toolkit.html", "desc": "A step-by-step guide to building a portable USB drive loaded with essential software for diagnostics, recovery, productivity, and privacy \u2014 ready for any situation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Encryption Guide", "url": "/tutorials/encryption-guide.html", "desc": "GPG for email/files, VeraCrypt for disk encryption, LUKS for full-disk, gocryptfs for per-directory encryption, and TLS basics.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Essential Linux CLI Tools", "url": "/tutorials/linux-cli.html", "desc": "Supercharge your terminal with modern replacements for classic Unix commands \u2014 faster search, better output, and tools you won't want to live without.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Essential Windows Applications", "url": "/tutorials/windows-apps.html", "desc": "A comprehensive guide to the best free Windows software \u2014 from system utilities to development tools, all hand-picked for quality and usefulness. Every app here is free or open-source.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "F-Droid &amp; Aurora Store", "url": "/tutorials/fdroid-guide.html", "desc": "Open-source Android app stores that give you freedom, privacy, and control \u2014 no Google Play Services required.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "FFmpeg Guide", "url": "/tutorials/ffmpeg-guide.html", "desc": "Convert, compress, trim, and manipulate video/audio with FFmpeg \u2014 the ultimate multimedia CLI tool.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Fail2ban", "url": "/tutorials/fail2ban.html", "desc": "Protect your Linux server from brute-force attacks with Fail2ban intrusion prevention.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "File Sharing with Samba & NFS", "url": "/tutorials/file-sharing-samba-nfs.html", "desc": "This guide covers setting up Samba (SMB/CIFS) and NFS file sharing on a Linux server, configuring shares, securing access, and connecting from Windows, macOS, and Linux clients.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "File Systems Compared", "url": "/tutorials/filesystems-compared.html", "desc": "Compare NTFS, ext4, Btrfs, ZFS, and APFS \u2014 features, performance, and use cases.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Firewall Setup Guide", "url": "/tutorials/firewall-setup.html", "desc": "Set up firewalls on Linux and Windows \u2014 UFW, firewalld, nftables basics, Windows Defender Firewall rules, and best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Focus &amp; Productivity Tools Guide", "url": "/tutorials/focus-productivity-tools.html", "desc": "Eliminate distractions and get more done with the best productivity tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Free Services Directory", "url": "/tutorials/free-services-directory.html", "desc": "A comprehensive directory of the best free-tier services across cloud storage, email, hosting, VPN, development tools, design resources, and learning platforms \u2014 with limits and requirements noted.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "GPG &amp; PGP Key Management", "url": "/tutorials/gpg-pgp-guide.html", "desc": "Encrypt, sign, and verify with GPG. Manage keys, smartcards, and secure communication.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Game Repacking Guide", "url": "/tutorials/repacking-guide.html", "desc": "An in-depth explanation of game repacking \u2014 how it works, who the major repackers are, what to expect during installation, and how to stay safe while saving bandwidth and storage space.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Git & GitHub Guide \u2014 SchooiCodes", "url": "/tutorials/git-basics.html", "desc": "A beginner-friendly guide to Git version control and GitHub \u2014 from first commit to pull requests.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "GitHub Actions", "url": "/tutorials/github-actions.html", "desc": "Automate, build, test, and deploy your code with GitHub Actions CI/CD pipelines.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Go Programming Basics", "url": "/tutorials/go-basics.html", "desc": "Learn Go from scratch \u2014 goroutines, channels, interfaces, and CLI tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "HTML & CSS Basics", "url": "/tutorials/html-css-basics.html", "desc": "Build your first website from scratch \u2014 HTML structure, CSS styling, layouts, responsive design, and deployment.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "HTTP/2 &amp; HTTP/3 Protocols", "url": "/tutorials/http2-http3.html", "desc": "Learn the evolution of HTTP \u2014 multiplexing, server push, QUIC, and performance.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Hardware Diagnostics Guide", "url": "/tutorials/hardware-diagnostics.html", "desc": "A comprehensive guide to diagnosing failing hardware \u2014 memory, storage, CPU, GPU, and system monitoring tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Hashing vs Encryption vs Encoding", "url": "/tutorials/hashing-vs-encryption.html", "desc": "Understand the differences between hashing, encryption, and encoding with practical examples.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Hiren's Boot CD PE Guide", "url": "/tutorials/hirens-boot-cd.html", "desc": "A complete guide to Hiren's Boot CD PE \u2014 the modern Windows PE rescue environment for recovery, diagnostics, and system repair.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Home Lab Guide", "url": "/tutorials/homelab-guide.html", "desc": "Build a home lab for learning and self-hosting \u2014 hardware, Proxmox, Docker, networking, services, and security.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "How DNS Works (Full Walkthrough)", "url": "/tutorials/how-dns-works.html", "desc": "Follow a DNS query from browser to resolver to authoritative nameserver, step by step.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "How to BSOD your computer/laptop in 2023", "url": "/tutorials/BSOD.html", "desc": "Warning: This will force\u2011close all programs without saving. Save any work before proceeding.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "How to Create High\u2011Quality Embeds (Not GIFs)", "url": "/tutorials/embeds.html", "desc": "This tutorial shows how to embed a video so that platforms like Discord display a high\u2011quality preview (not a GIF) with optional sound on mobile devices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "How to Use and Type the ESC Character", "url": "/tutorials/ESC.html", "desc": "Tip: Save any unsaved work before experimenting with the ESC key, as some programs may react unexpectedly.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Hydra Launcher Guide", "url": "/tutorials/hydra-launcher.html", "desc": "A complete guide to Hydra Launcher \u2014 an open-source game launcher with a built-in torrent client that integrates with public game repack repositories for easy downloading and management.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Hyprland Tutorial", "url": "/tutorials/hyprland.html", "desc": "Hyprland is a dynamic tiling Wayland compositor. This guide covers installation, basic configuration, and useful tweaks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "IP Obtainer (Legacy)", "url": "/tutorials/IP-Obtainer.html", "desc": "This legacy tool extracts the public IP address from a generated image file.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "ImageMagick Guide", "url": "/tutorials/imagemagick-guide.html", "desc": "Image manipulation from the CLI \u2014 convert, resize, crop, color correct, batch process, and create graphics with ImageMagick's convert and magick commands.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Introduction to Python", "url": "/tutorials/Python.html", "desc": "Python is a high\u2011level, interpreted language prized for readability and versatility across web development, data analysis, automation, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "JDownloader 2 Guide", "url": "/tutorials/jdownloader-guide.html", "desc": "Complete guide to JDownloader 2: install, configure link grabber, captcha solving, premium proxies, and automate downloads.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "JavaScript Basics", "url": "/tutorials/javascript-basics.html", "desc": "JavaScript fundamentals \u2014 variables, functions, DOM manipulation, events, async/await, and modern ES6+ syntax.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Kali Linux Basics", "url": "/tutorials/kali-linux.html", "desc": "A beginner-friendly guide to Kali Linux \u2014 installation, essential tools, and staying on the right side of the law.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Kiwix & ZIM Offline Server", "url": "/tutorials/kiwix-zim-server.html", "desc": "Serve Wikipedia, WikiHow, Stack Exchange, and other knowledge bases entirely offline using Kiwix and ZIM files. Perfect for areas with limited or no internet.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Kubernetes Basics", "url": "/tutorials/kubernetes-basics.html", "desc": "Learn Kubernetes fundamentals \u2014 pods, deployments, services, and cluster management for container orchestration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Kubernetes: Pods, Services &amp; Deployments", "url": "/tutorials/kubernetes-pods-services-deployments.html", "desc": "Deep dive into core Kubernetes objects with practical YAML examples.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Containers (LXC/LXD)", "url": "/tutorials/linux-containers.html", "desc": "Lightweight system containers with LXC and LXD \u2014 create, manage, snapshot, and network containers.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Disk Management: LVM, RAID &amp; Filesystems", "url": "/tutorials/linux-disk-management.html", "desc": "Manage storage with partitioning, LVM, software RAID, and filesystem tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux File Permissions", "url": "/tutorials/linux-permissions.html", "desc": "Master chmod, chown, umask, special permissions (SUID/SGID/sticky), ACLs, and SELinux basics.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Filesystem Hierarchy", "url": "/tutorials/linux-filesystem.html", "desc": "Understand the Linux filesystem \u2014 /, /etc, /var, /proc, /sys, /dev, mounts, and where everything lives.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Networking Guide", "url": "/tutorials/linux-networking.html", "desc": "Configure networking on Linux \u2014 ip, nmcli, netplan, bridges, bonding, routing, and diagnostics.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Overview", "url": "/tutorials/linux.html", "desc": "A curated collection of resources, tips, and best practices for using Linux effectively.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Package Management", "url": "/tutorials/linux-package-management.html", "desc": "Master APT, Pacman, DNF, Flatpak, Snap, and AUR \u2014 install, update, search, and troubleshoot packages.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Process Management with systemd", "url": "/tutorials/linux-process-management.html", "desc": "Master ps, htop, systemd, cgroups, nice values, and troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux SSH Tips & Tricks", "url": "/tutorials/linux-ssh-tips.html", "desc": "Advanced SSH usage \u2014 config files, key management, tunnels, jump hosts, agent forwarding, and security hardening.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Security Hardening", "url": "/tutorials/linux-security-hardening.html", "desc": "Secure Linux with SELinux, AppArmor, auditd, kernel hardening, and monitoring.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Server Administration", "url": "/tutorials/linux-server.html", "desc": "Hardening, user management, systemd, firewalls, web servers, and monitoring \u2014 everything you need to run a Linux server.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Load Balancing & Reverse Proxy Guide", "url": "/tutorials/load-balancing.html", "desc": "Distribute traffic, improve reliability, and secure your services with HAProxy, Nginx, and Caddy.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "LocalSend", "url": "/tutorials/localsend.html", "desc": "Cross-platform LAN file transfer app that works entirely offline \u2014 no internet, no cloud, no server.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Machine Learning Basics with Python", "url": "/tutorials/ml-basics-python.html", "desc": "Get started with ML using scikit-learn, pandas, and Jupyter for classification and regression.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "MariaDB / MySQL Setup & Administration", "url": "/tutorials/mariadb-setup.html", "desc": "Install, configure, secure, and manage MariaDB or MySQL databases for production and development.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Markdown Guide", "url": "/tutorials/markdown-guide.html", "desc": "A complete reference for Markdown \u2014 from basic syntax to extended features, flavors, and editors.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Media Server Automation Stack", "url": "/tutorials/media-server-automation.html", "desc": "Automate your entire media library \u2014 from searching and downloading to organizing and streaming. This guide covers the \"*arr\" stack with qBittorrent, Prowlarr, Bazarr, and Stremio integration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Minecraft Server Hosting (Aternos)", "url": "/tutorials/minecraft-aternos.html", "desc": "Aternos is a free Minecraft server hosting service. This guide covers setup, cross-version support, Bedrock crossplay, cracked mode, and common workarounds.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Morphe", "url": "/tutorials/morphe.html", "desc": "P2P encrypted file transfer tool for secure, high-speed, peer-to-peer sharing with no central server.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "MyInsta &amp; Instagram Mods", "url": "/tutorials/myinsta.html", "desc": "Download Instagram mods like MyInsta and Instander to unlock media downloads, disable ads, copy comments, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Neovim/Vim Editor Guide", "url": "/tutorials/neovim.html", "desc": "From beginner to power user \u2014 navigation, modes, Lua config, plugins, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Network Monitoring with Grafana &amp; Prometheus", "url": "/tutorials/grafana-prometheus.html", "desc": "Monitor servers and networks with Prometheus metrics and Grafana dashboards.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Network Troubleshooting Guide", "url": "/tutorials/network-troubleshooting.html", "desc": "Practical guide to diagnosing and fixing network issues using command-line tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Networking Basics", "url": "/tutorials/networking-basics.html", "desc": "Understand IP addressing, subnets, VLANs, routing, DNS, DHCP, and common network troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "NextDNS Setup Guide", "url": "/tutorials/nextdns.html", "desc": "Comprehensive guide to setting up NextDNS for enhanced privacy and security.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Nginx Reverse Proxy &amp; Load Balancing", "url": "/tutorials/nginx-reverse-proxy.html", "desc": "Configure Nginx as a reverse proxy, load balancer, and TLS terminator.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Nginx Web Server", "url": "/tutorials/nginx.html", "desc": "From installation to production \u2014 configure Nginx as a reverse proxy, static file server, and load balancer.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Node.js Guide", "url": "/tutorials/nodejs-guide.html", "desc": "Server-side JavaScript with Node.js \u2014 setup, npm, file system, Express.js, APIs, and deployment.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Note-Taking Methods for Students", "url": "/tutorials/note-taking-methods.html", "desc": "Compare the best note-taking systems for different learning styles.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "OSINT Basics", "url": "/tutorials/osint-guide.html", "desc": "Open Source Intelligence gathering techniques \u2014 search operators, people search, domain analysis, social media investigation, and tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "OWASP Top 10 Web Vulnerabilities", "url": "/tutorials/owasp-top-10.html", "desc": "Understand and protect against the most critical web application security risks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Off-Grid Messaging (Briar, Meshtastic, Yggdrasil)", "url": "/tutorials/offgrid-messaging.html", "desc": "Communicate when the internet goes down. These tools let you message others over Bluetooth, LoRa radio, or mesh networking without relying on cell towers or ISPs.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Developer Knowledge Bases", "url": "/tutorials/offline-dev-knowledge-bases.html", "desc": "Access API documentation, cheat sheets, and developer references without an internet connection. Essential for remote work, travel, or disaster scenarios.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Maps & Navigation", "url": "/tutorials/offline-maps-navigation.html", "desc": "Navigate anywhere without an internet connection. This guide covers the best tools for downloading maps, importing GPX tracks, and navigating offline.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Online Safety & Digital Hygiene", "url": "/tutorials/online-safety-guide.html", "desc": "A practical guide to staying safe online \u2014 from password hygiene to phishing detection, browser security, and beyond.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Orion Store", "url": "/tutorials/orion-store.html", "desc": "A powerful Android app manager for batch APK installation, app backup and restore, APK export, and app freezing \u2014 all in one tool.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Password Security Guide", "url": "/tutorials/password-security.html", "desc": "Password managers, 2FA/MFA, passkeys, creating strong passwords, and security best practices for accounts.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Paysafe & Online Money Transfer Guide", "url": "/tutorials/paysafe-money-transfer.html", "desc": "A practical guide to using Paysafe (paysafecard) for online payments, along with a comparison of alternatives like PayPal, Wise, Skrill, and Revolut for different use cases.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Plex & Jellyfin Media Server Setup", "url": "/tutorials/plex-jellyfin-setup.html", "desc": "Complete guide to setting up Plex and Jellyfin media servers on Windows and Linux. Compare features, install, configure, and optimize both.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "PostgreSQL", "url": "/tutorials/postgresql.html", "desc": "The world's most advanced open-source relational database \u2014 from setup to performance tuning.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "PowerShell Basics", "url": "/tutorials/powershell.html", "desc": "A comprehensive introduction to PowerShell for beginners \u2014 from cmdlets to scripting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "PowerShell Scripting", "url": "/tutorials/windows-powershell-scripting.html", "desc": "Go beyond basic PowerShell \u2014 functions, modules, error handling, remoting, scheduled jobs, and script security.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Proxmox VE Setup & Management", "url": "/tutorials/proxmox-setup.html", "desc": "Install, configure, and manage Proxmox Virtual Environment for your homelab or production infrastructure.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Proxy Guide", "url": "/tutorials/proxy-guide.html", "desc": "Set up and use proxies \u2014 HTTP/HTTPS/SOCKS5, reverse proxies with Nginx/Caddy, proxy chaining, and privacy considerations.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "RAID Levels Explained", "url": "/tutorials/raid-levels-explained.html", "desc": "Understand RAID 0, 1, 5, 6, 10, 50, and 60 \u2014 performance, redundancy, and trade-offs.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "REST API Basics", "url": "/tutorials/api-basics.html", "desc": "A primer on RESTful APIs \u2014 HTTP methods, status codes, authentication, testing, and best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Raspberry Pi Setup Guide", "url": "/tutorials/raspberry-pi-setup.html", "desc": "Set up a Raspberry Pi from scratch \u2014 headless install, SSH, GPIO, config, useful projects, and troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "ReVanced Guide", "url": "/tutorials/revanced-guide.html", "desc": "Patch Android APKs with ReVanced to remove ads, add features, and customize apps like YouTube, Reddit, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "React Basics", "url": "/tutorials/react-basics.html", "desc": "Build modern UIs with React \u2014 components, props, state, hooks, effects, routing, and project setup.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Redis", "url": "/tutorials/redis.html", "desc": "An in-memory data store used for caching, real-time messaging, session management, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Regular Expressions Guide", "url": "/tutorials/regex.html", "desc": "A practical guide to regex \u2014 patterns, syntax, tools, and real-world examples.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "RethinkDNS Tutorial", "url": "/tutorials/rethinkdns.html", "desc": "RethinkDNS is a privacy\u2011focused DNS resolver that offers easy configuration across devices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Rust Programming Basics", "url": "/tutorials/rust-basics.html", "desc": "Learn Rust from scratch \u2014 ownership, borrowing, structs, enums, and error handling.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SMT System Multitool Guide", "url": "/tutorials/smt-multitool.html", "desc": "SMT (System Multitool) is a batch-powered Windows utility collection with over 90 tools for networking, system configuration, activation, security research, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SQL Database Basics", "url": "/tutorials/sql-basics.html", "desc": "Learn Structured Query Language \u2014 from simple SELECT queries to complex JOINs and subqueries.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SSH Guide", "url": "/tutorials/ssh-guide.html", "desc": "Master the Secure Shell \u2014 keys, config, tunneling, and remote administration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SSL & HTTPS Certificates", "url": "/tutorials/ssl-certificates.html", "desc": "Understand TLS, get free certificates with Let's Encrypt, and secure your web services properly.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SVG Animation with CSS &amp; JS", "url": "/tutorials/svg-animation-css-js.html", "desc": "Create smooth, interactive SVG animations using CSS, JavaScript, and GSAP.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Seal &amp; ulapp", "url": "/tutorials/seal-ulapp.html", "desc": "Android video downloader (Seal) and LAN file sharing app (ulapp) for offline media.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Security Breach Response", "url": "/tutorials/security-breach-response.html", "desc": "A comprehensive step-by-step guide for identifying, containing, and recovering from a security breach \u2014 from immediate triage to full system restoration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Server Monitoring", "url": "/tutorials/monitoring.html", "desc": "Monitor server metrics, visualize data, and set up alerts using Prometheus and Grafana.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Shizuku &amp; Hail", "url": "/tutorials/shizuku-hail.html", "desc": "Manage system apps, debloat your device, and freeze/unfreeze apps without root using Shizuku and Hail.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Social Engineering Awareness Guide", "url": "/tutorials/social-engineering.html", "desc": "Recognize and defend against phishing, pretexting, baiting, and manipulation tactics.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Social Media Privacy Guide", "url": "/tutorials/social-media-privacy.html", "desc": "Platform-by-platform privacy settings, data deletion guides, app permissions, and privacy-focused alternatives to mainstream social media.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Software Testing 101", "url": "/tutorials/testing-101.html", "desc": "Master unit, integration, and E2E testing with pytest, Vitest, and Playwright.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Spicetify", "url": "/tutorials/spicetify.html", "desc": "Customize the Spotify desktop client with themes, extensions, and custom CSS using the Spicetify CLI modding tool.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Subnetting &amp; CIDR Explained", "url": "/tutorials/subnetting-cidr.html", "desc": "Understand IP subnetting, CIDR notation, VLSM, and subnet calculation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Systemd Service Guide", "url": "/tutorials/systemd-guide.html", "desc": "Create and manage systemd services, timers, sockets, and targets \u2014 journalctl, unit files, and troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Tails OS Guide", "url": "/tutorials/tails.html", "desc": "A complete walkthrough of Tails \u2014 the amnesic incognito live system that leaves no trace and routes everything through Tor.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Task Automation Guide", "url": "/tutorials/automation.html", "desc": "Automate everything \u2014 cron, systemd timers, scripts, and CI/CD pipelines.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Telegram Privacy Guide", "url": "/tutorials/telegram-privacy.html", "desc": "A comprehensive walkthrough of every Telegram privacy setting to lock down your account and protect your identity.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Terminal Color Schemes & Themes", "url": "/tutorials/color-schemes.html", "desc": "Make your terminal beautiful \u2014 ANSI codes, popular themes, tools, and configuration for every emulator.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Terraform Infrastructure as Code", "url": "/tutorials/terraform-basics.html", "desc": "Learn Terraform \u2014 HCL, providers, state management, modules, and workspaces.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Time Management Guide for Students", "url": "/tutorials/time-management-guide.html", "desc": "Master your schedule with proven time management techniques.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Tmux Guide", "url": "/tutorials/tmux-guide.html", "desc": "Terminal multiplexing with tmux \u2014 sessions, windows, panes, keybindings, customisation, and pair programming.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Torrent Clients Guide", "url": "/tutorials/torrent-clients-guide.html", "desc": "Complete guide to qBittorrent, Transmission, and Deluge torrent clients. Installation, configuration, VPN binding, port forwarding, and optimization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Two-Factor Authentication Guide", "url": "/tutorials/two-factor-auth.html", "desc": "Everything you need to know about 2FA, TOTP, hardware keys, passkeys, and securing your accounts with a second factor.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "TypeScript", "url": "/tutorials/typescript.html", "desc": "JavaScript with superpowers \u2014 static types, interfaces, generics, and modern tooling.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "VPN Setup Guide", "url": "/tutorials/vpn-setup.html", "desc": "Set up WireGuard and OpenVPN \u2014 server configuration, client setup, key generation, routing, and troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "VS Code Setup & Extensions", "url": "/tutorials/vscode.html", "desc": "A comprehensive guide to setting up VS Code for development.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Vencord &amp; Vesktop", "url": "/tutorials/vencord-vesktop.html", "desc": "Mod your Discord client with plugins, themes, and quality-of-life improvements using Vencord and the standalone Vesktop client.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Ventoy Advanced Guide", "url": "/tutorials/ventoy.html", "desc": "Multi-boot USB mastery \u2014 run dozens of ISOs from a single drive without reformatting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Virtual Machines Guide", "url": "/tutorials/virtual-machines.html", "desc": "A beginner's guide to virtual machines with VirtualBox and VMware.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "VirtualBox vs VMware vs Hyper-V", "url": "/tutorials/virtualbox-vmware-hyperv.html", "desc": "Compare the major hypervisors for desktop and server virtualization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "WSL2 Complete Guide", "url": "/tutorials/wsl2-guide.html", "desc": "Run a full Linux kernel inside Windows \u2014 install, manage, and configure WSL2.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Web Scraping with Python", "url": "/tutorials/web-scraping.html", "desc": "Extract data from websites using Python, BeautifulSoup, Requests, and modern scraping techniques.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "WebSockets &amp; Real-Time Communication", "url": "/tutorials/websockets-guide.html", "desc": "Build real-time apps with WebSockets, Socket.IO, and WebRTC.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Wi-Fi Security Guide", "url": "/tutorials/wifi-security.html", "desc": "Secure your Wi-Fi network \u2014 WPA2/WPA3, 802.1X, guest networks, deauth protection, and auditing.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Debloating & Optimization", "url": "/tutorials/windows-debloat.html", "desc": "A complete guide to removing bloatware, disabling telemetry, and optimizing Windows 10/11 for performance and privacy.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Defender &amp; Security Center Guide", "url": "/tutorials/windows-defender-security.html", "desc": "Configure Microsoft Defender, ASR rules, firewall, and ransomware protection.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Deployment Guide", "url": "/tutorials/windows-deployment.html", "desc": "Everything from clean installs and bootable media to unattended setups, imaging, and Sysprep \u2014 covering Windows 10 and 11.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Environment Variables", "url": "/tutorials/windows-environment-variables.html", "desc": "Understand and manage Windows environment variables \u2014 PATH, system vs user, setx, PowerShell, and common use cases.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Event Viewer &amp; Troubleshooting", "url": "/tutorials/windows-event-viewer.html", "desc": "Master Event Viewer for system diagnostics and troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Hardening Guide", "url": "/tutorials/windows-hardening.html", "desc": "Harden Windows 10/11 \u2014 Attack Surface Reduction, Windows Defender, AppLocker, BitLocker, user account security, and group policy.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Keyboard Shortcuts", "url": "/tutorials/windows-shortcuts.html", "desc": "Essential Windows keyboard shortcuts for power users \u2014 desktop, file explorer, task manager, virtual desktops, and hidden shortcuts.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Recovery & Rescue", "url": "/tutorials/windows-rescue.html", "desc": "Windows Recovery Environment, DISM, SFC, bootrec, system restore, restore points, advanced startup, and repairing Windows without reinstalling.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Registry Guide", "url": "/tutorials/windows-registry.html", "desc": "Understand and edit the Windows Registry \u2014 regedit, reg.exe, .reg files, common tweaks, backup/restore, and safety.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Registry Hacks &amp; Tweaks", "url": "/tutorials/windows-registry-hacks.html", "desc": "Advanced registry tricks for performance, UI, security, and automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Subsystem for Linux (WSL)", "url": "/tutorials/wsl.html", "desc": "Guide to installing and using WSL2 on Windows.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Task Automation", "url": "/tutorials/windows-task-automation.html", "desc": "Automate Windows with Task Scheduler, scheduled tasks via PowerShell, startup scripts, and event-triggered automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Task Scheduler Automation", "url": "/tutorials/windows-task-scheduler.html", "desc": "Automate tasks with Task Scheduler, triggers, conditions, and PowerShell integration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "WireGuard VPN", "url": "/tutorials/wireguard.html", "desc": "Set up a fast, modern, and audited VPN with WireGuard \u2014 the new gold standard for secure tunnels.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "curl & wget Guide", "url": "/tutorials/curl-wget-guide.html", "desc": "Master HTTP requests from the command line \u2014 curl for APIs, wget for downloads, headers, authentication, and scripting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "jq Guide", "url": "/tutorials/jq-guide.html", "desc": "Parse, filter, and transform JSON from the command line using jq \u2014 queries, pipes, arrays, and practical API data extraction.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "rsync", "url": "/tutorials/rsync.html", "desc": "Fast, versatile file synchronization and remote backup tool for Unix-like systems.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "systemd Services", "url": "/tutorials/systemd-services.html", "desc": "Creating and managing systemd service units for background processes, daemons, and scheduled tasks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}];

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

  window.__TL = window.__TL || {};
  window.__TL.searchIndex = searchIndex;

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

/* ===== PWA Manifest Link ===== */
(function(){
  try {
    var manifest = document.createElement('link');
    manifest.rel = 'manifest';
    manifest.href = '/manifest.json';
    document.head.appendChild(manifest);
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

/* ===== Reading Time Estimate ===== */
(function(){
  try {
    var main = document.querySelector('.main-content');
    if (!main || !document.querySelector('.section-badge')) return;
    var text = main.textContent || '';
    var words = text.trim().split(/\s+/).length;
    var minutes = Math.max(1, Math.round(words / 200));
    var badge = document.createElement('span');
    badge.className = 'reading-time';
    badge.textContent = minutes + ' min read';
    var h1 = main.querySelector('h1');
    if (h1 && h1.parentElement) {
      h1.parentElement.insertBefore(badge, h1.nextSibling);
    }
  } catch(e) {}
})();

/* ===== Reading Progress Bar ===== */
(function(){
  try {
    var bar = document.createElement('div');
    bar.className = 'reading-progress-bar';
    document.body.appendChild(bar);
    var winHeight, docHeight;
    function updateProgress() {
      var scrollY = window.scrollY || window.pageYOffset || 0;
      var pct = docHeight > winHeight ? Math.min(scrollY / (docHeight - winHeight) * 100, 100) : 0;
      bar.style.setProperty('--progress', pct + '%');
    }
    function measure() {
      winHeight = window.innerHeight;
      docHeight = document.documentElement.scrollHeight;
      updateProgress();
    }
    measure();
    window.addEventListener('resize', measure, { passive: true });
    window.addEventListener('scroll', updateProgress, { passive: true });
  } catch(e) {}
})();

/* ===== Last Updated Badge ===== */
(function(){
  try {
    var meta = document.querySelector('meta[name="last-updated"]');
    if (!meta) return;
    var date = meta.getAttribute('content');
    if (!date) return;
    var h1 = document.querySelector('.main-content h1');
    if (!h1) return;
    var badge = document.createElement('div');
    badge.className = 'last-updated';
    var d = new Date(date + 'T00:00:00');
    var formatted = d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
    badge.innerHTML = '<i class="far fa-calendar-alt"></i> Last updated ' + formatted;
    h1.parentNode.insertBefore(badge, h1.nextSibling);
  } catch(e) {}
})();

/* ===== Skip to Content focus fix ===== */
(function(){
  try {
    var link = document.querySelector('.skip-to-content');
    var main = document.querySelector('.main-content');
    if (link && main) {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        main.setAttribute('tabindex', '-1');
        main.focus();
        main.addEventListener('blur', function() { main.removeAttribute('tabindex'); }, { once: true });
      });
    }
  } catch(e) {}
})();

/* ===== Service Worker Registration ===== */
(function(){
  try {
    if ('serviceWorker' in navigator) {
      var scripts = document.querySelectorAll('script[src*="scripts.js"]');
      if (scripts.length) {
        var src = scripts[0].src;
        var idx = src.indexOf('/assets/');
        if (idx !== -1) {
          var siteRoot = src.substring(0, idx);
          navigator.serviceWorker.register(siteRoot + '/assets/sw.js', { scope: '/' })
            .then(function() { /* silently registered */ })
            .catch(function() { /* silently failed */ });
        }
      }
    }
  } catch(e) {}
})();

/* ===== Sticky Floating Table of Contents ===== */
(function(){
  try {
    var main = document.querySelector('.main-content');
    if (!main) return;

    var headings = main.querySelectorAll('h2, h3');
    if (headings.length < 3) return;

    var toc = document.createElement('nav');
    toc.className = 'sticky-toc show';
    toc.innerHTML = '<h3><i class="fas fa-list"></i> On this page</h3><ul></ul>';
    var tocUl = toc.querySelector('ul');

    headings.forEach(function(h) {
      if (!h.id) h.id = 'heading-' + Math.random().toString(36).substr(2, 9);
      var isH2 = h.tagName === 'H2';
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = '#' + h.id;
      a.className = isH2 ? 'toc-h2' : 'toc-h3';
      a.textContent = h.textContent.substring(0, 50);
      li.appendChild(a);
      tocUl.appendChild(li);
    });

    document.body.appendChild(toc);

    var activeLink = null;
    function updateActive() {
      var scrollY = window.scrollY || window.pageYOffset || 0;
      var links = toc.querySelectorAll('a');
      var newActive = null;
      links.forEach(function(link) {
        var id = link.getAttribute('href').substring(1);
        var heading = document.getElementById(id);
        if (heading && heading.offsetTop <= scrollY + 150) {
          newActive = link;
        }
      });
      if (newActive !== activeLink) {
        if (activeLink) activeLink.classList.remove('active');
        if (newActive) newActive.classList.add('active');
        activeLink = newActive;
      }
    }

    window.addEventListener('scroll', updateActive, { passive: true });
    updateActive();

    toc.querySelectorAll('a').forEach(function(link) {
      link.addEventListener('click', function(e) {
        e.preventDefault();
        var id = this.getAttribute('href').substring(1);
        var heading = document.getElementById(id);
        if (heading) {
          heading.scrollIntoView({ behavior: 'smooth' });
          updateActive();
        }
      });
    });
  } catch(e) {}
})();

/* ===== Keyboard Shortcuts ===== */
(function(){
  try {
    var modal = document.createElement('div');
    modal.className = 'keyboard-shortcuts-modal';
    modal.innerHTML = 
      '<div class="keyboard-shortcuts-content">' +
      '<button class="keyboard-shortcuts-close" aria-label="Close shortcuts"><i class="fas fa-times"></i></button>' +
      '<h2><i class="fas fa-keyboard"></i> Keyboard Shortcuts</h2>' +
      '<div class="shortcuts-grid">' +
      '<span class="kbd">?</span><span class="kbd-desc">Show this help</span>' +
      '<span class="kbd">s</span><span class="kbd-desc">Focus search</span>' +
      '<span class="kbd">t</span><span class="kbd-desc">Scroll to top</span>' +
      '<span class="kbd">b</span><span class="kbd-desc">Go back</span>' +
      '<span class="kbd">j</span><span class="kbd-desc">Scroll down</span>' +
      '<span class="kbd">k</span><span class="kbd-desc">Scroll up</span>' +
      '</div>' +
      '<div class="shortcuts-footer">Press <span class="kbd">Esc</span> to close</div>' +
      '</div>';
    document.body.appendChild(modal);

    var closeBtn = modal.querySelector('.keyboard-shortcuts-close');
    closeBtn.addEventListener('click', function() { modal.classList.remove('open'); });

    document.addEventListener('keydown', function(e) {
      if (e.key === '?' || e.key === '/') {
        e.preventDefault();
        modal.classList.add('open');
      }
      if (e.key === 'Escape' && modal.classList.contains('open')) {
        modal.classList.remove('open');
      }
      if (!modal.classList.contains('open')) {
        if (e.key === 's' && !e.ctrlKey && !e.metaKey && document.activeElement.tagName !== 'INPUT') {
          e.preventDefault();
          var searchInput = document.getElementById('search-bar-input');
          if (searchInput) searchInput.focus();
        }
        if (e.key === 't') {
          e.preventDefault();
          window.scrollTo({ top: 0, behavior: 'smooth' });
        }
        if (e.key === 'b') {
          e.preventDefault();
          window.history.back();
        }
        if (e.key === 'j') {
          e.preventDefault();
          window.scrollBy({ top: 100, behavior: 'smooth' });
        }
        if (e.key === 'k') {
          e.preventDefault();
          window.scrollBy({ top: -100, behavior: 'smooth' });
        }
      }
    });
  } catch(e) {}
})();
