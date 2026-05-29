(function(){
  try {
    var els = document.querySelectorAll('[data-aos]');
    if (els.length) {
      els.forEach(function(el, i) {
        var d = parseInt(el.getAttribute('data-aos-delay')) || 0;
        setTimeout(function(){ el.classList.add('aos-animate'); }, d + i * 60);
      });
      if (typeof IntersectionObserver !== 'undefined') {
        var obs = new IntersectionObserver(function(entries) {
          entries.forEach(function(e) {
            if (e.isIntersecting) {
              var el = e.target;
              if (!el.classList.contains('aos-animate')) {
                var d = parseInt(el.getAttribute('data-aos-delay')) || 0;
                setTimeout(function(){ el.classList.add('aos-animate'); }, d);
              }
              obs.unobserve(el);
            }
          });
        }, { threshold: 0.05, rootMargin: '0px 0px -20px 0px' });
        els.forEach(function(el) { obs.observe(el); });
      }
    }
  } catch(e) {}
})();

(function(){
  var s = localStorage.getItem('theme');
  if (s === null || s === 'dark') {
    document.body.classList.add('dark-mode');
    if (s === null) localStorage.setItem('theme', 'dark');
  }
  var t = document.getElementById('theme-toggle');
  if (t) {
    t.innerHTML = document.body.classList.contains('dark-mode')
      ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
    t.addEventListener('click', function() {
      document.body.classList.toggle('dark-mode');
      var d = document.body.classList.contains('dark-mode');
      localStorage.setItem('theme', d ? 'dark' : 'light');
      t.innerHTML = d ? '<i class="fas fa-sun"></i>' : '<i class="fas fa-moon"></i>';
      var evt = new CustomEvent('tl-settings-changed', { detail: { darkMode: d } });
      document.dispatchEvent(evt);
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

    var closeBtn = document.createElement('button');
    closeBtn.className = 'nav-menu-close';
    closeBtn.innerHTML = '<i class="fas fa-times"></i>';
    closeBtn.setAttribute('aria-label', 'Close menu');
    m.insertBefore(closeBtn, m.firstChild);

    var closeMenu = function() {
      h.classList.remove('active');
      m.classList.remove('active');
      bd.classList.remove('active');
      document.body.style.overflow = '';
    };

    var openMenu = function() {
      h.classList.add('active');
      m.classList.add('active');
      bd.classList.add('active');
      document.body.style.overflow = 'hidden';
    };

    h.addEventListener('click', function() {
      if (h.classList.contains('active')) closeMenu();
      else openMenu();
    });

    closeBtn.addEventListener('click', closeMenu);
    bd.addEventListener('click', closeMenu);
    Array.from(m.querySelectorAll('a')).forEach(function(l) {
      l.addEventListener('click', closeMenu);
    });

    document.addEventListener('keydown', function(ev) {
      if (ev.key === 'Escape' && m.classList.contains('active')) closeMenu();
    });

    var touchStartY = 0;
    m.addEventListener('touchstart', function(ev) {
      if (m.scrollTop === 0) touchStartY = ev.touches[0].clientY;
    }, { passive: true });
    m.addEventListener('touchmove', function(ev) {
      if (touchStartY && ev.touches[0].clientY - touchStartY > 80) {
        closeMenu();
        touchStartY = 0;
      }
    }, { passive: true });
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
      var cur = (window.location.pathname.replace(/^\//, '') || 'index.html');
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

  var EMBEDDED_INDEX = [{"title": "Accessories Buyer's Guide", "url": "/buying-guide/accessories.html", "desc": "Keyboards, mice, webcams, microphones, docks, and cables \u2014 the gear that completes your setup.", "cat": "buying-guide", "popularity": 70, "date": "2026-05-29"}, {"title": "Audio Buyer's Guide", "url": "/buying-guide/audio.html", "desc": "IEMs, headphones, speakers, DACs, and amps \u2014 navigate the world of personal audio with confidence.", "cat": "buying-guide", "popularity": 70, "date": "2026-05-29"}, {"title": "Desktop Buyer's Guide", "url": "/buying-guide/desktops.html", "desc": "Office, Gaming, Creator, or Server \u2014 choose your next desktop build with confidence.", "cat": "buying-guide", "popularity": 70, "date": "2026-05-29"}, {"title": "Laptop Buyer's Guide", "url": "/buying-guide/laptops.html", "desc": "Chromebook, Ultrabook, Gaming, or Workstation \u2014 find the right portable powerhouse for your workflow.", "cat": "buying-guide", "popularity": 70, "date": "2026-05-29"}, {"title": "Phone Buyer's Guide", "url": "/buying-guide/phones.html", "desc": "From budget workhorses to flagship cameras \u2014 find the right phone for your needs and budget.", "cat": "buying-guide", "popularity": 70, "date": "2026-05-29"}, {"title": "Tablet Buyer's Guide", "url": "/buying-guide/tablets.html", "desc": "iPad, Android, or Windows \u2014 choose the right tablet for creativity, productivity, or entertainment.", "cat": "buying-guide", "popularity": 70, "date": "2026-05-29"}, {"title": "Tech Buyer's Guide", "url": "/buying-guide/index.html", "desc": "Smart recommendations across every budget tier. Whether you are stretching every dollar or building a no-compromise setup, these guides cover phones, laptops, desktops, tablets, audio gear, and access", "cat": "buying-guide", "popularity": 90, "date": "2026-05-29"}, {"title": "Creatives", "url": "/creatives/index.html", "desc": "Music tools, digital art, video editing, AI generators, and fun creative websites.", "cat": "creatives", "popularity": 90, "date": "2026-05-29"}, {"title": "Documentation Archive", "url": "/docs/index.html", "desc": "This section preserves legacy documentation from the websites merged to create this library \u2014 tutorials, Minecraft guides, and more.", "cat": "docs", "popularity": 90, "date": "2026-05-29"}, {"title": "Minecraft Server Guides", "url": "/docs/minecraft.html", "desc": "The complete guide to hosting and joining crossplay, any-version, and cracked Minecraft servers \u2014 all for free using Aternos.", "cat": "docs", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Tutorials", "url": "/docs/tutorials.html", "desc": "This section preserves the legacy tutorials from the original site.", "cat": "docs", "popularity": 70, "date": "2026-05-29"}, {"title": "Gaming", "url": "/gaming/index.html", "desc": "Minecraft servers, Roblox scripts, unblocked games, browser games, and PC gaming optimizations.", "cat": "gaming", "popularity": 90, "date": "2026-05-29"}, {"title": "404 \u2014 Page Not Found", "url": "/404.html", "desc": "Page Not Found", "cat": "home", "popularity": 70, "date": "2026-05-29"}, {"title": "Tech Library \u2014 Tutorials, Tools, Lexicon & Resources", "url": "/index.html", "desc": "Tutorials, tech lexicon, emergency survival resources, free media alternatives, and curated resources \u2014 all free, all organized.", "cat": "home", "popularity": 100, "date": "2026-05-29"}, {"title": "Tech Lexicon", "url": "/lexicon/index.html", "desc": "240+ tech terms defined \u2014 programming, security, networking, Linux, hardware, gaming, and general tech.", "cat": "lexicon", "popularity": 90, "date": "2025-01-01"}, {"title": "All-In-One Book", "url": "/minecraft/commands/all-in-one-book/index.html", "desc": "/give @p written_book{pages:['[\"\",{\"text\":\"Hey! This is a list of some commands\\\\nhaloboyyetheck \\\\nand giorgakis made:\\\\n\\\\nClick on them to do the command.\\\\n\\\\n\"},{\"text\":\"End Portal spawn egg\",\"cl", "cat": "minecraft", "popularity": 90, "date": "2026-05-29"}, {"title": "Minecraft", "url": "/minecraft/index.html", "desc": "Official Minecraft Wiki \u2014 blocks, items, mechanics, and more.", "cat": "minecraft", "popularity": 90, "date": "2026-05-29"}, {"title": "Minecraft Commands", "url": "/minecraft/commands/index.html", "desc": "Skull giver:", "cat": "minecraft", "popularity": 90, "date": "2026-05-29"}, {"title": "Additional Piracy Sources", "url": "/piracy/additional-sources.html", "desc": "Expanded list of sources organized by type \u2014 direct download, torrent, DDL forums, scene trackers, and safety-rated recommendations. Always use a VPN and exercise caution.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Android Piracy Guide &#8212; Piracy", "url": "/piracy/android-piracy-guide.html", "desc": "Comprehensive guide to Android piracy: Aurora Store, modded APKs, Lucky Patcher, ReVanced, Shizuku, and the best APK sites.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Anime Piracy Guide &#8212; Piracy", "url": "/piracy/anime-piracy-guide.html", "desc": "Complete guide to anime piracy: streaming sites, download groups (SubsPlease, Erai), Nyaa torrents, fansub groups, and automation with SeaDex.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Complete Torrenting Guide &#8212; Piracy", "url": "/piracy/torrenting-guide.html", "desc": "The definitive guide to torrenting: clients, trackers, safety, and full automation with Sonarr/Radarr. Everything you need to know to torrent safely and effectively.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Debrid Services Comparison &#8212; Piracy", "url": "/piracy/debrid-services.html", "desc": "Compare the major debrid services: features, pricing, speed tests, and which one to choose for your use case.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Direct Download Sites & Tools &#8212; Piracy", "url": "/piracy/direct-download-guide.html", "desc": "Master direct downloads: top DDL sites, JDownloader2, IDM setup, bypassing limits, and staying safe while downloading.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Ebook & Audiobook Piracy &#8212; Piracy", "url": "/piracy/ebook-piracy-guide.html", "desc": "Everything for book pirates: Z-Library, Anna\u2019s Archive, LibGen, MyAnonamouse (MAM), Readarr automation, and more.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Gaming Piracy Guide &#8212; Piracy", "url": "/piracy/gaming-piracy-guide.html", "desc": "Your complete guide to gaming piracy: FitGirl, DODI repacks, SteamRIP, console emulation, ROMs, and staying safe.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Media Servers for Piracy &#8212; Piracy", "url": "/piracy/media-server-piracy.html", "desc": "Plex, Jellyfin, Sonarr/Radarr, Prowlarr, Overseerr, Usenet/Torrent integration for the ultimate media setup.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Music Piracy Guide &#8212; Piracy", "url": "/piracy/music-piracy-guide.html", "desc": "Complete guide to music piracy: Soulseek, Deemix, Lucida, BlockTheSpot, Freezer, Telegram bots for music, and more.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Office Activation via MAS \u2014 Piracy", "url": "/piracy/office-activation-guide.html", "desc": "A comprehensive technical guide to downloading Microsoft Office and using Microsoft Activation Scripts (MAS) for educational activation research.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Piracy Resources", "url": "/piracy/index.html", "desc": "Sites, tools, and guides for streaming, downloading, torrenting, gaming, and more \u2014 organized and updated.", "cat": "piracy", "popularity": 90, "date": "2025-01-01"}, {"title": "Private Tracker Guide &#8212; Piracy", "url": "/piracy/private-trackers.html", "desc": "Everything about private trackers: ratio systems, getting invited, the top trackers, maintaining ratio, and using seedboxes.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Real-Debrid Guide &#8212; Piracy", "url": "/piracy/real-debrid-guide.html", "desc": "Unlock premium file hosting with Real-Debrid. Learn setup, Stremio integration, JDownloader, and how it compares to alternatives like AllDebrid and Premiumize.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Scene Release Groups & Standards &#8212; Piracy", "url": "/piracy/scene-releases.html", "desc": "The inner workings of the warez scene: release naming conventions, types, groups, P2P vs Scene, and how to find scene releases.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Software Piracy Guide &#8212; Piracy", "url": "/piracy/software-piracy-guide.html", "desc": "Complete guide to pirating software: FileCR, WAREZ, DDoSecrets, portable apps, safe cracking, and Microsoft activation tools.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Staying Safe While Pirating &#8212; Piracy", "url": "/piracy/safe-piracy.html", "desc": "Antivirus setup, sandboxing, fake sites, VirusTotal, adblockers, DNS over HTTPS, separate browser profile.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Streaming Sites Guide &#8212; Piracy", "url": "/piracy/streaming-sites-guide.html", "desc": "Top streaming sites, anime streaming, live TV, sports streaming, ad blocking, and backup sites.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Stremio + Torrentio Setup &#8212; Piracy", "url": "/piracy/stremio-setup.html", "desc": "Transform Stremio into a Netflix-like experience with Torrentio and Real-Debrid. Watch any movie or show instantly with premium cached streams.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Torrent Automation Suite &#8212; Piracy", "url": "/piracy/torrent-automation.html", "desc": "Sonarr, Radarr, Prowlarr, qBittorrent, Overseerr, Usenet automation, and the complete Docker Compose stack.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Usenet Guide &#8212; Piracy", "url": "/piracy/usenet-guide.html", "desc": "Learn about Usenet: providers, indexers, download clients, and how to automate everything with Radarr/Sonarr. The superior alternative to torrenting for many users.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "VPN Guide for Piracy &#8212; Piracy", "url": "/piracy/vpn-for-piracy.html", "desc": "Why you need a VPN, features for piracy, top VPNs (Mullvad, Proton, AirVPN), port forwarding, split tunneling, kill switch.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "iOS Piracy Guide &#8212; Piracy", "url": "/piracy/ios-piracy-guide.html", "desc": "Master iOS piracy: AltStore, SideStore, TrollStore, signing services, AppCake, and emulators on iPhone and iPad.", "cat": "piracy", "popularity": 70, "date": "2026-05-29"}, {"title": "Databases \u2014 Programming", "url": "/programming/databases.html", "desc": "Relational, NoSQL, and NewSQL databases \u2014 understanding their trade-offs and choosing the right one for your project.", "cat": "programming", "popularity": 70, "date": "2026-05-29"}, {"title": "DevOps \u2014 Programming", "url": "/programming/devops.html", "desc": "CI/CD pipelines, containerization, monitoring, and infrastructure as code \u2014 the essential tooling for modern software delivery.", "cat": "programming", "popularity": 70, "date": "2026-05-29"}, {"title": "Frameworks \u2014 Programming", "url": "/programming/frameworks.html", "desc": "A comprehensive overview of frontend, backend, and full-stack frameworks for modern web development.", "cat": "programming", "popularity": 70, "date": "2026-05-29"}, {"title": "Languages \u2014 Programming", "url": "/programming/languages.html", "desc": "A side-by-side comparison of popular programming languages covering typing systems, performance, use cases, and learning curves.", "cat": "programming", "popularity": 70, "date": "2026-05-29"}, {"title": "Programming", "url": "/programming/index.html", "desc": "Languages, frameworks, databases, DevOps, and learning paths \u2014 everything you need to level up as a developer.", "cat": "programming", "popularity": 90, "date": "2026-05-29"}, {"title": "Projects", "url": "/projects/index.html", "desc": "Tools and projects created and maintained by the community \u2014 SMT, OpenCode, Minecraft resources, and more.", "cat": "projects", "popularity": 90, "date": "2026-05-29"}, {"title": "Browser Extensions", "url": "/resources/extensions.html", "desc": "Essential browser extensions for privacy, productivity, development, and fun \u2014 curated for Firefox and Chromium browsers.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Browser Recommendations", "url": "/resources/browsers.html", "desc": "Recommendations for modern, privacy-focused web browsers \u2014 from everyday use to maximum anonymity.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Color & Design Tools", "url": "/resources/color-tools.html", "desc": "Palette generators, gradient tools, contrast checkers, and design inspiration platforms for beautiful interfaces.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Cool GitHub Repos", "url": "/resources/github-repos.html", "desc": "A curated collection of awesome GitHub repos \u2014 tools, learning resources, fun projects, privacy tools, and Linux utilities.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Cool Websites", "url": "/resources/websites.html", "desc": "A curated list of interesting and useful websites, tools, and services.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Design Inspiration", "url": "/resources/design-inspiration.html", "desc": "Find inspiration for your next project \u2014 landing pages, UI designs, color palettes, and component libraries from the best designers.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Developer Cheatsheets", "url": "/resources/cheatsheets.html", "desc": "Quick reference guides for Git, Docker, Linux, SQL, regex, editors, and more \u2014 everything a developer needs at their fingertips.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Font Resources", "url": "/resources/fonts.html", "desc": "A curated collection of font foundries, developer-friendly coding fonts, icon fonts, and web font tools.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Free APIs for Developers", "url": "/resources/free-apis.html", "desc": "Free public APIs to power your projects \u2014 weather, news, music, games, finance, and fun data sources. Many require no authentication at all.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Free Media & Alternatives", "url": "/resources/freemedia.html", "desc": "A curated list of free alternatives to paid services \u2014 inspired by FMHY (Free Media Heck Yeah). Every single thing listed here costs exactly $0. Replace Netflix, Spotify, Photoshop, AutoCAD, and more ", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Free Stock Resources", "url": "/resources/free-stock.html", "desc": "High-quality free stock photos, videos, audio, and icons for your projects \u2014 all completely free to use.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Learning Platforms", "url": "/resources/learning-platforms.html", "desc": "Curated learning platforms for every skill level \u2014 from free courses to interactive coding challenges and technical references.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Resources", "url": "/resources/index.html", "desc": "Curated collections of browser extensions, free media alternatives, learning platforms, design tools, and more.", "cat": "resources", "popularity": 90, "date": "2025-01-01"}, {"title": "Tech Podcasts", "url": "/resources/podcasts.html", "desc": "The best tech podcasts for developers, security enthusiasts, and Linux fans \u2014 from web development to cybersecurity and open source.", "cat": "resources", "popularity": 70, "date": "2026-05-29"}, {"title": "Security", "url": "/security/index.html", "desc": "Guides and resources for DNS privacy, secure browsing, VPNs, password security, and Windows hardening.", "cat": "security", "popularity": 90, "date": "2026-05-29"}, {"title": "All 90+ Tools \u2014 SMT", "url": "/smt/features/index.html", "desc": "Every tool from v1.1 through v2.3 &#8212; networking, activation, system utilities, developer tools, and more.", "cat": "smt", "popularity": 90, "date": "2026-05-29"}, {"title": "SMT \u2014 System Multitool", "url": "/smt/index.html", "desc": "Over 90 powerful tools for Windows &#8212; IP Geolocation, Activation, USB Creator, DNS Changer, and more.", "cat": "smt", "popularity": 90, "date": "2026-05-29"}, {"title": "Advanced Backup Strategies \u2014 Survival Kit", "url": "/survival/backup-strategies-deep.html", "desc": "Deep dive into backup strategies: 3-2-1 rule, local and offsite backups, cloud options, rotation schemes, restore testing, and automation.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "BIOS/UEFI Recovery \u2014 Survival Kit", "url": "/survival/bios-recovery.html", "desc": "Recovering a system with corrupted BIOS/UEFI firmware - CMOS reset, Flashback, CH341A programmers, and debricking motherboards.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Building Your Emergency USB Drive \u2014 Survival Kit", "url": "/survival/emergency-usb.html", "desc": "Everything you need to build a doomsday-ready USB drive: multi-boot setup, portable apps, recovery ISOs, and comprehensive testing - all pre-loaded and ready to run on any computer.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Data Recovery Guide \u2014 Survival Kit", "url": "/survival/data-recovery.html", "desc": "Step-by-step guide to recovering lost data from hard drives, SSDs, memory cards, and RAID arrays - from software recovery to professional lab services.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Digital Emergency Prep Checklist \u2014 Survival Kit", "url": "/survival/emergency-prep-checklist.html", "desc": "A comprehensive checklist for digital emergency preparedness - immediate actions, weekly prep, monthly checks, essential downloads, and communication planning.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Digital Estate Planning \u2014 Survival Kit", "url": "/survival/digital-will.html", "desc": "Plan for your digital afterlife - password inheritance via Bitwarden, dead man switches, document storage, and family instructions.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Emergency Local Servers \u2014 Survival Kit", "url": "/survival/servers.html", "desc": "Keep your local network running when the internet goes dark. Local DNS, file sharing, mesh messaging, portable web servers, and off-grid communication for disaster scenarios.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Encrypted Communication Guide \u2014 Survival Kit", "url": "/survival/encrypted-comms.html", "desc": "Set up end-to-end encrypted communication - Signal, Session, Keybase, PGP email, Matrix/Element, and WireGuard VPN.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Hardware Diagnostics \u2014 Survival Kit", "url": "/survival/hardware-diagnostics.html", "desc": "Diagnose failing hardware - RAM testing with MemTest86, storage diagnostics with CrystalDiskInfo, CPU/GPU stress testing, PSU testing, and thermal diagnostics.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Malware Removal Guide \u2014 Survival Kit", "url": "/survival/malware-removal.html", "desc": "A systematic approach to removing malware - from immediate isolation to deep cleaning, rootkit removal, and prevention.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Communication \u2014 Survival Kit", "url": "/survival/offline-communication.html", "desc": "Communicate without internet or cellular - Briar mesh, Meshtastic devices, LoRa radio, goTenna, and ham radio basics.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Knowledge Bases \u2014 Survival Kit", "url": "/survival/knowledge-bases.html", "desc": "Carry a developer's reference library in your pocket. DevDocs, Zeal/Dash docsets, MDN offline, tldr-pages, man pages, cheat sheets, and local wiki systems for when the internet is gone.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Maps & Navigation \u2014 Survival Kit", "url": "/survival/maps.html", "desc": "Never get lost \u2014 even without a data connection. Organic Maps, Maps.me, OsmAnd, Google Maps offline, GPS fundamentals, and downloading whole countries for offline use.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Wikis & Knowledge \u2014 Survival Kit", "url": "/survival/offline-wikis.html", "desc": "Carry the sum of human knowledge in your pocket. Kiwix, ZIM archives, and offline readers for Wikipedia, Wiktionary, WikiHow, Stack Exchange, Project Gutenberg, and more.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Password Reset & Recovery \u2014 Survival Kit", "url": "/survival/password-reset.html", "desc": "Reset or recover passwords on Windows, Linux, and macOS - plus Bitwarden emergency access and 2FA recovery codes.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Portable Toolkit \u2014 Survival Kit", "url": "/survival/tools.html", "desc": "A curated collection of portable apps for Windows, Linux, and cross-platform tools that run entirely from a USB stick. No installation, no traces \u2014 your digital go-bag in software form.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Ransomware Response \u2014 Survival Kit", "url": "/survival/ransomware-response.html", "desc": "What to do when ransomware strikes - isolate, identify the strain, find decryption tools, and recover without paying criminals.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Solar & Off-Grid Power \u2014 Survival Kit", "url": "/survival/solar-charging.html", "desc": "Keep devices running off-grid - solar panel basics, power station sizing, battery types, USB power banks, inverters, and practical tips for extended outages.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Survival Kit", "url": "/survival/index.html", "desc": "Emergency digital resources \u2014 offline tools, data recovery, system rescue, security breach response, and essential bookmarks.", "cat": "survival", "popularity": 90, "date": "2025-01-01"}, {"title": "Surviving Network Outages \u2014 Survival Kit", "url": "/survival/network-outage.html", "desc": "How to survive when the internet goes down - diagnosing outages, local network access, cellular failover, offline entertainment, mesh networks.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "System Rescue with Live CDs \u2014 Survival Kit", "url": "/survival/system-rescue.html", "desc": "How to use Live CDs and USB rescue environments to recover unbootable systems - covering Hiren Boot CD, SystemRescue, Rescatux, and bootloader repair.", "cat": "survival", "popularity": 70, "date": "2026-05-29"}, {"title": "Tools", "url": "/tools/index.html", "desc": "A curated collection of batch scripts, online utilities, developer tools, and the legendary SMT.", "cat": "tools", "popularity": 90, "date": "2026-05-29"}, {"title": "2D Game Physics &amp; Collision Detection", "url": "/tutorials/2d-game-physics.html", "desc": "Implement 2D physics for games \u2014 rigid bodies, collision shapes, triggers, raycasting, and optimization techniques.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "3D Modeling (Blender)", "url": "/tutorials/blender-3d-modeling.html", "desc": "3D modeling with Blender \u2014 mesh editing, sculpting, materials, and rendering.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "3D Printing &amp; CAD", "url": "/tutorials/3d-printing-cad.html", "desc": "3D printing workflow \u2014 CAD modeling, slicing, printer calibration, and materials guide.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "AI Ethics &amp; Responsible Development", "url": "/tutorials/ai-ethics-guide.html", "desc": "Understand the ethical dimensions of AI \u2014 bias mitigation, fairness metrics, transparency, privacy, regulation, and responsible development practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "AI Models & Tools Directory", "url": "/tutorials/ai-models-directory.html", "desc": "A curated directory of the best AI models, tools, and platforms across every category \u2014 from large language models to local AI runners.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "API Design (REST &amp; GraphQL)", "url": "/tutorials/api-design.html", "desc": "API design \u2014 RESTful principles, GraphQL, versioning, documentation, and rate limiting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "API Design Best Practices", "url": "/tutorials/api-design-best-practices.html", "desc": "Design robust RESTful and GraphQL APIs with proper status codes and auth.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "API Security", "url": "/tutorials/api-security.html", "desc": "Secure REST and GraphQL APIs -- auth, rate limiting, OWASP top 10.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "API Testing Guide", "url": "/tutorials/api-testing.html", "desc": "Test REST and GraphQL APIs \u2014 curl, Postman/Insomnia, HTTPie, status codes, auth testing, and automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "APK Sideloading Guide", "url": "/tutorials/apk-sideloading.html", "desc": "Everything you need to know about installing Android apps from outside the Play Store \u2014 methods, tools, safety, and best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "ASCII, Unicode &amp; Encoding Explained", "url": "/tutorials/ascii-unicode-encoding.html", "desc": "Understand character encoding \u2014 ASCII, UTF-8, UTF-16, code points, and normalization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "ASP.NET Core", "url": "/tutorials/aspnet-core-development.html", "desc": "Cross-platform .NET web apps \u2014 MVC, Razor Pages, Entity Framework, and Web API.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "AWS EC2 &amp; Compute", "url": "/tutorials/aws-ec2-compute.html", "desc": "Deep dive into AWS EC2 -- instance types, storage, networking, and optimization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "AWS ECS &amp; Fargate", "url": "/tutorials/aws-ecs-fargate.html", "desc": "Container orchestration on AWS \u2014 ECS clusters, services, and Fargate serverless.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "AWS Fundamentals", "url": "/tutorials/aws-fundamentals.html", "desc": "Amazon Web Services -- EC2, S3, VPC, IAM, Lambda, and core services.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "AWS Lambda &amp; Serverless", "url": "/tutorials/aws-lambda-serverless.html", "desc": "Serverless compute on AWS \u2014 Lambda functions, triggers, and best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "AWS S3 &amp; Storage", "url": "/tutorials/aws-s3-storage.html", "desc": "Deep dive into S3 -- storage classes, security, lifecycle, and performance.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Academic Writing", "url": "/tutorials/academic-writing.html", "desc": "Academic writing \u2014 structure, research, citations, LaTeX, and publishing.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Accessible Design Patterns", "url": "/tutorials/accessible-design-patterns.html", "desc": "Design accessible interfaces \u2014 forms, navigation, modals, color contrast, focus management, and inclusive design principles.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Active Directory", "url": "/tutorials/active-directory.html", "desc": "Active Directory \u2014 domains, GPOs, LDAP, replication, and security.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Active Recall &amp; Spaced Repetition", "url": "/tutorials/active-recall.html", "desc": "Learn how to study smarter with evidence-based techniques that boost long-term retention.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Ad Blocking Guide", "url": "/tutorials/adblocking.html", "desc": "Block ads and trackers with uBlock Origin, Pi-hole, AdGuard Home, NextDNS, and browser-based filtering.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Advanced Git", "url": "/tutorials/git-advanced.html", "desc": "Beyond the basics \u2014 rebasing, cherry-picking, interactive rebase, bisect, hooks, submodules, reflog, and workflow strategies.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Advanced Linux Networking Tools", "url": "/tutorials/linux-advanced-networking.html", "desc": "ip, ss, nmcli, bridge, tc -- advanced network configuration and troubleshooting on Linux.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Advanced Regex Patterns &amp; Tricks", "url": "/tutorials/regex-advanced.html", "desc": "Go beyond basic regex with lookaheads, backreferences, atomic groups, and performance.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Advanced SQL Queries &amp; Optimization", "url": "/tutorials/sql-advanced.html", "desc": "Master window functions, CTEs, indexing, and query performance tuning.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Algorithms", "url": "/tutorials/algorithms.html", "desc": "Algorithms \u2014 sorting, searching, dynamic programming, and complexity analysis.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "All Tutorials", "url": "/tutorials/index.html", "desc": "Browse step-by-step tech tutorials covering Windows, Linux, programming, networking, and more.", "cat": "tutorials", "popularity": 90, "date": "2025-01-01"}, {"title": "Amazon DynamoDB", "url": "/tutorials/dynamodb-guide.html", "desc": "NoSQL key-value and document database \u2014 single-digit millisecond performance at scale.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Android App Development", "url": "/tutorials/android-app-development.html", "desc": "Build Android apps with Kotlin, Jetpack Compose, and Material Design 3.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Android Development (Kotlin)", "url": "/tutorials/android-kotlin.html", "desc": "Android development with Kotlin \u2014 Jetpack Compose, Activities, and Material Design.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Android Piracy Guide", "url": "/tutorials/android-piracy-guide.html", "desc": "Modded apps, cracked games, and tools for Android \u2014 safety and best sources.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Android Studio Setup &amp; Workflow", "url": "/tutorials/android-studio-guide.html", "desc": "Set up Android Studio for productive Android development \u2014 emulator configuration, Gradle build system, debugging, and profiling.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Angular Development", "url": "/tutorials/angular-development.html", "desc": "Enterprise frontend with Angular \u2014 components, services, routing, and RxJS.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Anime &amp; Cartoon Piracy", "url": "/tutorials/anime-piracy-guide.html", "desc": "Stream and download anime, cartoons, and animated content \u2014 sites, torrents, and subtitles.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Anki Customization &amp; Advanced Features", "url": "/tutorials/anki-customization.html", "desc": "Supercharge Anki with add-ons, card styling, FSRS scheduler, and sync.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Ansible Automation", "url": "/tutorials/ansible-automation.html", "desc": "Configuration management and automation with Ansible \u2014 playbooks, roles, and inventory.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Ansible Automation", "url": "/tutorials/ansible.html", "desc": "Automate servers, deploy applications, and manage infrastructure at scale with Ansible.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Ansible Playbooks Deep Dive", "url": "/tutorials/ansible-playbooks-deep-dive.html", "desc": "Advanced playbook patterns, dynamic inventory, collections, and AWX.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Apache Cassandra Database", "url": "/tutorials/cassandra-guide.html", "desc": "Learn Apache Cassandra \u2014 distributed NoSQL database design, CQL query language, data modeling for high-scale applications.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "App Store Publishing", "url": "/tutorials/app-store-publishing.html", "desc": "Publishing to App Store and Google Play \u2014 signing, review, in-app purchases, and ASO.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Application Performance Monitoring", "url": "/tutorials/application-performance-monitoring.html", "desc": "APM tools \u2014 Datadog, New Relic, OpenTelemetry, and continuous profiling for application observability.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Arch Linux Installation Guide", "url": "/tutorials/arch-linux.html", "desc": "From bare metal to a fully functional Arch Linux system \u2014 a complete step-by-step walkthrough.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Arduino Programming", "url": "/tutorials/arduino-programming.html", "desc": "Program Arduino boards \u2014 digital/analog I/O, sensors, actuators, and project prototyping.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Arduino Programming &amp; Electronics", "url": "/tutorials/arduino-basics.html", "desc": "Program Arduino microcontrollers \u2014 digital/analog I/O, sensor interfacing, communication protocols, and real-world projects.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "ArgoCD &amp; GitOps", "url": "/tutorials/argocd-gitops.html", "desc": "GitOps for Kubernetes \u2014 ArgoCD, application sync, and progressive delivery.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Audacity Audio Editing", "url": "/tutorials/audacity-audio-editing-deep.html", "desc": "Professional audio editing, restoration, mixing, and podcast production with Audacity.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Audio Editing with Audacity", "url": "/tutorials/audacity-audio-editing.html", "desc": "Record, edit, and produce audio with Audacity \u2014 noise reduction, effects, and multitrack.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Audio Production", "url": "/tutorials/audio-production.html", "desc": "Audio production \u2014 DAWs, mixing, mastering, synthesis, and recording.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Azure Cloud Services", "url": "/tutorials/azure-cloud-services.html", "desc": "Microsoft Azure \u2014 VMs, Blob Storage, Azure Functions, and Active Directory.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Azure Functions", "url": "/tutorials/azure-functions.html", "desc": "Serverless compute on Azure \u2014 triggers, bindings, Durable Functions.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Azure Fundamentals", "url": "/tutorials/azure-fundamentals.html", "desc": "Microsoft Azure -- VMs, storage, networking, Entra ID, and core services.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Azure Kubernetes Service", "url": "/tutorials/azure-kubernetes-service.html", "desc": "Managed Kubernetes on Azure \u2014 AKS clusters, node pools, and Azure integration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "BGP Routing Basics", "url": "/tutorials/bgp-basics.html", "desc": "Border Gateway Protocol, AS numbers, peering, route selection, and BGP security with RPKI.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "BIOS vs UEFI vs Legacy Boot", "url": "/tutorials/bios-uefi-boot.html", "desc": "Understand the differences between BIOS, UEFI, Secure Boot, and boot process.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "BIOS/UEFI Recovery &amp; Firmware", "url": "/tutorials/bios-recovery.html", "desc": "Recover from failed BIOS updates, corrupt firmware, and unbrick motherboards.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Backup Strategies", "url": "/tutorials/backup-strategies.html", "desc": "Reliable backup strategies \u2014 3-2-1 rule, rsync, Borg, restic, Duplicati, cloud backups, and automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Bash &amp; Shell Scripting", "url": "/tutorials/bash-shell-scripting.html", "desc": "Advanced shell scripting -- POSIX, Zsh, Fish, and shell automation patterns.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Bash Scripting Guide", "url": "/tutorials/bash-scripting.html", "desc": "Learn Bash scripting from the ground up \u2014 variables, conditionals, loops, functions, error handling, and automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Bash Scripting Mastery", "url": "/tutorials/bash-scripting-mastery.html", "desc": "Bash scripting \u2014 variables, functions, control flow, error handling, and advanced techniques.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Basics of JavaScript", "url": "/tutorials/JS.html", "desc": "JavaScript is a versatile programming language used for interactive web development.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Big Data Tools: Hadoop &amp; Spark", "url": "/tutorials/big-data-tools.html", "desc": "Introduction to big data processing with Hadoop, Spark, Hive, and the data lake ecosystem.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "BitLocker Guide", "url": "/tutorials/bitlocker.html", "desc": "Full-disk encryption on Windows \u2014 enabling, managing, recovery, and alternatives.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Blender 3D Modeling Introduction", "url": "/tutorials/blender-3d-basics.html", "desc": "Start your 3D journey with Blender \u2014 modeling, materials, lighting, and rendering.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Blockchain &amp; Web3", "url": "/tutorials/blockchain-web3.html", "desc": "Blockchain -- smart contracts, DeFi, consensus, Web3 apps.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Bootable USB Guide", "url": "/tutorials/bootable-usb.html", "desc": "This guide covers creating bootable USB media for Linux distributions, Windows installers, and recovery tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Browser Extension Development", "url": "/tutorials/browser-extension-development.html", "desc": "Build Chrome/Firefox extensions \u2014 manifest v3, service workers, content scripts, and stores.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Browser Fingerprinting &amp; Anti-Detection", "url": "/tutorials/browser-fingerprinting.html", "desc": "How browser fingerprinting works and how to protect your privacy online.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Browser Privacy Guide", "url": "/tutorials/browser-privacy.html", "desc": "How to lock down your browser for maximum privacy \u2014 ad blocking, tracker blocking, secure DNS, and essential settings.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Budget Tech Buyer&#x27;s Guide 2026", "url": "/tutorials/budget-tech-buyers-guide.html", "desc": "Best tech under $200 \u2014 monitors, headphones, mice, keyboards, SSDs, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Bug Bounty Hunting Guide", "url": "/tutorials/bug-bounty-guide.html", "desc": "A practical roadmap to bug bounty hunting \u2014 reconnaissance, vulnerability research, weaponization, and responsible disclosure.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Burp Suite Deep Dive", "url": "/tutorials/burp-suite-deep-dive.html", "desc": "Master Burp Suite \u2014 proxy, scanner, intruder, repeater, and extensions for web pentesting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Burp Suite Web Testing", "url": "/tutorials/burp-suite.html", "desc": "Learn how to use Burp Suite for web application security testing \u2014 from intercepting traffic to automated scanning.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "C# Programming Basics", "url": "/tutorials/csharp-basics.html", "desc": "Learn C# -- LINQ, async/await, .NET ecosystem, and modern cross-platform development.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "C++ Programming for Beginners", "url": "/tutorials/cpp-basics.html", "desc": "Learn C++ \u2014 pointers, classes, STL, and modern C++ features.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "CI/CD Concepts", "url": "/tutorials/cicd-concepts.html", "desc": "Continuous Integration and Delivery \u2014 pipelines, artifact management, and deployment strategies.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "CI/CD Pipeline Design", "url": "/tutorials/cicd-pipeline-design.html", "desc": "Design efficient CI/CD pipelines \u2014 GitHub Actions, GitLab CI, testing, caching, and deployment strategies.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "CI/CD Pipeline Guide", "url": "/tutorials/ci-cd-pipeline.html", "desc": "Build, test, and deploy automatically with continuous integration and continuous delivery pipelines.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "CI/CD with Jenkins Pipeline", "url": "/tutorials/ci-cd-jenkins.html", "desc": "Set up Jenkins for continuous integration and delivery.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "CPU Architecture", "url": "/tutorials/cpu-architecture.html", "desc": "CPU architecture \u2014 cores, cache, pipelines, instruction sets, and microarchitecture.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "CSS Animations &amp; Transitions", "url": "/tutorials/css-animations.html", "desc": "CSS animations, transitions, keyframes -- smooth, performant web animations.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "CSS Art &amp; Advanced Styling", "url": "/tutorials/css-art-advanced-styling.html", "desc": "Create CSS art, advanced layouts, container queries, and creative CSS techniques.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "CachyOS Installation Guide", "url": "/tutorials/cachyos.html", "desc": "CachyOS is a fast, lightweight Linux distribution based on Arch Linux.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Calculus Fundamentals", "url": "/tutorials/calculus-fundamentals.html", "desc": "Limits, derivatives, integrals, and optimization \u2014 the mathematical foundation of physics and machine learning.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Canvas 2D API", "url": "/tutorials/canvas-2d-api.html", "desc": "2D graphics programming with HTML Canvas API \u2014 drawing, animation, charts, and games.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Capture The Flag Guide", "url": "/tutorials/ctf-guide.html", "desc": "Everything you need to know about Capture The Flag competitions \u2014 categories, essential tools, strategies, and practice platforms.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Career Planning in Tech", "url": "/tutorials/career-planning-tech.html", "desc": "Plan your tech career \u2014 learning paths, resumes, networking, and interviewing.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Chaos Engineering", "url": "/tutorials/chaos-engineering.html", "desc": "Chaos Engineering \u2014 principles, experiments, tools (Chaos Mesh, Litmus), and GameDay.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Chitralaya", "url": "/tutorials/chitralaya.html", "desc": "Self-hosted lightweight image gallery and media server for organizing and sharing photos.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Chromebook Firmware Guide", "url": "/tutorials/chromebook-firmware.html", "desc": "Everything about flashing, backing up, and replacing Chromebook firmware \u2014 from verified boot to MrChromebox.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Clean Code &amp; SOLID", "url": "/tutorials/clean-code-solid.html", "desc": "Writing clean, maintainable code \u2014 naming, refactoring, and software craftsmanship.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Clean Code Principles", "url": "/tutorials/clean-code.html", "desc": "Naming, functions, comments, error handling, refactoring, and writing maintainable software.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Clojure &amp; Lisp on JVM", "url": "/tutorials/clojure-lisp-jvm.html", "desc": "Modern Lisp dialect on JVM \u2014 immutable data, REPL-driven development, and ClojureScript.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cloud Backup Strategies", "url": "/tutorials/cloud-backup-strategies.html", "desc": "Comprehensive guide to backing up your data using cloud providers, encryption, and automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cloud Computing Overview", "url": "/tutorials/cloud-computing-overview.html", "desc": "Compare AWS, GCP, and Azure services for compute, storage, networking, and serverless.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cloud Cost Optimization", "url": "/tutorials/cloud-cost-optimization.html", "desc": "Reduce cloud costs -- right-sizing, reserved instances, spot instances, and FinOps.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cloud Gaming", "url": "/tutorials/cloud-gaming.html", "desc": "Cloud gaming \u2014 GeForce NOW, Xbox Cloud Gaming, latency, and infrastructure.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cloud Native Security", "url": "/tutorials/cloud-native-security.html", "desc": "Secure containers, Kubernetes, and serverless workloads \u2014 supply chain, runtime, and admission control.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cloud Networking &amp; VPC", "url": "/tutorials/cloud-networking-vpc.html", "desc": "Cloud networking -- VPC design, peering, VPN, Direct Connect, and CDN.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cloud Security &amp; Compliance", "url": "/tutorials/cloud-security-compliance.html", "desc": "Secure cloud infrastructure \u2014 IAM, encryption, compliance frameworks, and audits.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cloud Security Fundamentals", "url": "/tutorials/cloud-security-basics.html", "desc": "Understand the core principles of cloud security \u2014 shared responsibility, IAM, encryption, logging, and cloud security posture management.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Code Review Best Practices", "url": "/tutorials/code-review.html", "desc": "Constructive feedback, security checks, PR etiquette, and building a review culture.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Combinatorics &amp; Discrete Optimization", "url": "/tutorials/combinatorics-optimization.html", "desc": "Counting principles, graph coloring, integer programming, and approximation algorithms.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Computer Vision Deep Dive", "url": "/tutorials/computer-vision-deep.html", "desc": "CNNs, object detection, image segmentation, GANs, and vision transformers.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Computer Vision with OpenCV", "url": "/tutorials/computer-vision-opencv.html", "desc": "Master computer vision with OpenCV \u2014 image processing, object detection, face recognition, video analysis, and deep learning integration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Concurrency &amp; Parallelism", "url": "/tutorials/concurrency-parallelism.html", "desc": "Concurrency \u2014 threads, async/await, locks, channels, and parallel processing.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Container Runtimes", "url": "/tutorials/container-runtimes.html", "desc": "Container runtimes -- containerd, CRI-O, runc, gVisor, Kata.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Container Security Best Practices", "url": "/tutorials/container-security.html", "desc": "Secure your containerized workloads \u2014 image scanning, runtime protection, seccomp profiles, AppArmor, and Kubernetes security contexts.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Containerization vs Virtualization", "url": "/tutorials/containerization-vs-virtualization.html", "desc": "Understand the differences between containers and VMs, and when to use each.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Contract Testing with Pact", "url": "/tutorials/contract-testing-pact.html", "desc": "Consumer-driven contract testing for microservices \u2014 ensure backward compatibility without full integration tests.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cool Apps & Tools Directory", "url": "/tutorials/cool-apps-directory.html", "desc": "Hand-picked collection of the most useful applications across productivity, development, media, utilities, and security.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cooling &amp; Thermal", "url": "/tutorials/cooling-thermal.html", "desc": "PC cooling \u2014 air, AIO, custom loop, thermal paste, and fan optimization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "CouchDB &amp; PouchDB", "url": "/tutorials/couchdb-pouchdb.html", "desc": "Offline-first NoSQL with multi-master replication and conflict resolution.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cracked & Pre-Installed Steam Games Guide", "url": "/tutorials/cracked-steam-games.html", "desc": "A comprehensive guide to understanding game cracking, finding reliable pre-installed releases, using Steam emulators for LAN play, and staying safe \u2014 with strong legal disclaimers.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Creating a Basic Batch File", "url": "/tutorials/Batchfile.html", "desc": "A batch file is a script for Windows command\u2011line interpreter, used to automate tasks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Croc", "url": "/tutorials/croc.html", "desc": "CLI tool for encrypted peer-to-peer file transfers between any two computers.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cross-Platform Mobile Tools", "url": "/tutorials/cross-platform-mobile.html", "desc": "Cross-platform tools \u2014 Kotlin Multiplatform, .NET MAUI, and Progressive Web Apps.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cross\u2011play Minecraft Server Guide", "url": "/tutorials/hajcacmcs.html", "desc": "This tutorial is preserved from the original repository.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cryptography Fundamentals", "url": "/tutorials/cryptography-fundamentals.html", "desc": "Cryptography \u2014 symmetric, asymmetric, hashing, digital signatures, and PKI.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Crystal Language", "url": "/tutorials/crystal-language.html", "desc": "Ruby-like syntax, compiled, type-inferred \u2014 LLVM backend, C bindings.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Cybersecurity Red Team", "url": "/tutorials/cybersecurity-red-team.html", "desc": "Red team -- pentesting, social engineering, adversary emulation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "DNS Deep Dive", "url": "/tutorials/dns-deep-dive.html", "desc": "Domain Name System \u2014 resolution, record types, DNSSEC, and advanced configurations.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "DNS Privacy & Filtering Guide", "url": "/tutorials/dns-privacy-guide.html", "desc": "Block ads, trackers, and malware at the DNS level with Pi-hole, AdGuard Home, and NextDNS.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "DNS Records Deep Dive", "url": "/tutorials/dns-records-deep-dive.html", "desc": "A comprehensive guide to A, AAAA, CNAME, MX, TXT, NS, SRV, and DNSSEC records.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "DaVinci Resolve Editing Basics", "url": "/tutorials/davinci-resolve-basics.html", "desc": "Learn video editing with DaVinci Resolve \u2014 cut, color, audio, and delivery.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Dark Web &amp; Anonymity", "url": "/tutorials/dark-web-anonymity.html", "desc": "Dark web \u2014 Tor, I2P, Onion services, and anonymity best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Dart Programming Language", "url": "/tutorials/dart-programming-language.html", "desc": "Client-optimized language for UI \u2014 sound null safety, isolates, and FFI.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Data Engineering &amp; ETL", "url": "/tutorials/data-engineering-etl.html", "desc": "Data engineering \u2014 ETL/ELT, pipelines, data warehousing, and orchestration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Data Recovery &amp; Forensics", "url": "/tutorials/data-recovery.html", "desc": "Recover deleted files, repair corrupted drives, and salvage data from failing storage.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Data Structures", "url": "/tutorials/data-structures.html", "desc": "Data structures \u2014 arrays, linked lists, trees, hash tables, and advanced structures.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Data Visualization with Matplotlib &amp; Seaborn", "url": "/tutorials/matplotlib-seaborn.html", "desc": "Create publication-quality visualizations \u2014 Matplotlib fundamentals, Seaborn statistical plots, styling, and dashboard integration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Database Design", "url": "/tutorials/database-design.html", "desc": "Database design \u2014 normalization, indexes, ACID, NoSQL, and query optimization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Database Migrations &amp; Schema Management", "url": "/tutorials/database-migrations.html", "desc": "Manage database schema changes safely and consistently using migration tools like Flyway, Alembic, and Liquibase.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Deep Backup Strategies", "url": "/tutorials/backup-strategies-deep.html", "desc": "Comprehensive backup strategies beyond 3-2-1 \u2014 automation, verification, and disaster recovery.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Deep Learning Frameworks", "url": "/tutorials/deep-learning-frameworks.html", "desc": "PyTorch, TensorFlow, JAX \u2014 compare, choose, and master deep learning frameworks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Design Patterns", "url": "/tutorials/design-patterns.html", "desc": "Software design patterns \u2014 creational, structural, behavioral, and architectural patterns.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Design Systems &amp; Component Libraries", "url": "/tutorials/design-systems-component-libraries.html", "desc": "Build and maintain design systems \u2014 tokens, components, Storybook, and cross-team collaboration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Differential Equations", "url": "/tutorials/differential-equations.html", "desc": "ODE and PDE fundamentals, analytical and numerical solutions, and applications in physics and engineering.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Digital Art (Krita &amp; Procreate)", "url": "/tutorials/digital-art-krita-procreate.html", "desc": "Digital art \u2014 Krita, Procreate, painting techniques, and brush engines.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Digital Forensics &amp; Incident Response", "url": "/tutorials/digital-forensics-incident-response.html", "desc": "DFIR methodology \u2014 evidence collection, disk forensics, memory analysis, and containment.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Digital Minimalism Guide", "url": "/tutorials/digital-minimalism.html", "desc": "Reduce digital clutter and improve focus \u2014 declutter apps, manage notifications, optimize social media, and build deep work habits.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Digital Zettelkasten with Obsidian", "url": "/tutorials/digital-zettelkasten.html", "desc": "Build a networked knowledge base using Zettelkasten principles in Obsidian.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Direct Download Guide", "url": "/tutorials/direct-download-guide.html", "desc": "Download files directly (no torrenting) \u2014 DDL sites, JDownloader2, and debrid services.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Discrete Mathematics", "url": "/tutorials/discrete-mathematics.html", "desc": "Logic, set theory, graph theory, combinatorics \u2014 the mathematical foundation of computer science.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Django Web Framework", "url": "/tutorials/django-web-framework.html", "desc": "Build web apps with Django \u2014 models, views, templates, ORM, and REST framework.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Docker & Containerization", "url": "/tutorials/docker.html", "desc": "Everything you need to know about Docker \u2014 from containers to Compose, registries to best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Docker Compose", "url": "/tutorials/docker-compose.html", "desc": "Define and run multi-container Docker applications with ease using Docker Compose.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Docker Compose Deep Dive", "url": "/tutorials/docker-compose-deep-dive.html", "desc": "Master Docker Compose -- multi-service apps, networking, secrets, production.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Docker Deep Dive", "url": "/tutorials/docker-deep-dive.html", "desc": "Master Docker \u2014 images, containers, networks, volumes, multi-stage builds, and Compose.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Docker Swarm", "url": "/tutorials/docker-swarm.html", "desc": "Orchestrate containers with Docker Swarm -- services, stacks, networking, production.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Dockerfile Best Practices", "url": "/tutorials/dockerfile-best-practices.html", "desc": "Build efficient Docker images -- multi-stage, caching, security, and size optimization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Domain-Driven Design", "url": "/tutorials/domain-driven-design.html", "desc": "DDD -- ubiquitous language, bounded context, aggregates, and tactical patterns.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Driver Updates on Linux", "url": "/tutorials/linux-driver-updates.html", "desc": "Manage hardware drivers on Linux \u2014 kernel modules, firmware, NVIDIA/AMD GPUs, and peripheral drivers.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Drone Building &amp; Flight Controllers", "url": "/tutorials/drone-building-flight-controllers.html", "desc": "Build FPV drones \u2014 frame, motors, ESCs, flight controller, Betaflight tuning, and regulations.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Drone CI Pipeline Setup", "url": "/tutorials/drone-ci.html", "desc": "Build continuous integration pipelines with Drone CI \u2014 pipeline configuration, parallel steps, services, secrets management, and plugin ecosystem.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "ELK Stack", "url": "/tutorials/elk-stack.html", "desc": "Elasticsearch, Logstash, Kibana \u2014 log aggregation, parsing, and visualization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "ELK Stack: Elasticsearch, Logstash, Kibana", "url": "/tutorials/elk-stack-guide.html", "desc": "Centralize log aggregation, search, and visualization using the ELK Stack \u2014 Elasticsearch clustering, Logstash pipelines, and Kibana dashboards.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "ESP32 &amp; MicroPython", "url": "/tutorials/esp32-micropython.html", "desc": "Program ESP32 microcontrollers with MicroPython \u2014 Wi-Fi, Bluetooth, sensors, and IoT projects.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Ebook &amp; Audiobook Piracy", "url": "/tutorials/ebook-piracy-guide.html", "desc": "Download books, audiobooks, comics, and academic texts \u2014 sources, tools, and organization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Edge Computing &amp; CDN", "url": "/tutorials/edge-computing-cdn.html", "desc": "Edge computing \u2014 Cloudflare Workers, CDN strategies, edge databases, and IoT edge processing.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Elasticsearch Deep Dive", "url": "/tutorials/elasticsearch-deep-dive.html", "desc": "Search and analytics \u2014 inverted index, mappings, aggregations, and cluster operations.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Eleventy (11ty)", "url": "/tutorials/eleventy-static-site.html", "desc": "Simpler static site generator \u2014 zero-config, multiple template languages, and fast builds.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Elixir &amp; Phoenix", "url": "/tutorials/elixir-phoenix.html", "desc": "Concurrent, fault-tolerant apps with Elixir/Erlang VM \u2014 Phoenix, OTP, and LiveView.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Email Systems &amp; Deliverability", "url": "/tutorials/email-systems-deliverability.html", "desc": "Email infrastructure \u2014 SMTP, DKIM, SPF, DMARC, deliverability, and transactional email.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Emergency Prep Checklist", "url": "/tutorials/emergency-prep-checklist.html", "desc": "A step-by-step checklist to prepare your digital life for emergencies \u2014 before disaster strikes.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Emergency USB Toolkit", "url": "/tutorials/emergency-usb-toolkit.html", "desc": "A step-by-step guide to building a portable USB drive loaded with essential software for diagnostics, recovery, productivity, and privacy \u2014 ready for any situation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Emergency USB Toolkit", "url": "/tutorials/emergency-usb.html", "desc": "Build a multi-boot emergency USB drive for system rescue, diagnostics, and recovery.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Encrypted Communication Tools", "url": "/tutorials/encrypted-comms.html", "desc": "End-to-end encrypted messaging and calling \u2014 Signal, Matrix, Briar, and protocol comparison.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Encryption Guide", "url": "/tutorials/encryption-guide.html", "desc": "GPG for email/files, VeraCrypt for disk encryption, LUKS for full-disk, gocryptfs for per-directory encryption, and TLS basics.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Erlang &amp; BEAM", "url": "/tutorials/erlang-beam.html", "desc": "Concurrent, distributed, fault-tolerant systems on the BEAM VM.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Esports &amp; Competitive Gaming", "url": "/tutorials/esports-competitive.html", "desc": "Competitive gaming \u2014 practice routines, aim training, team strategy, and mental game.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Essential Linux Applications", "url": "/tutorials/essential-linux-apps.html", "desc": "Curated list of essential Linux applications \u2014 productivity, media, development, and utilities.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Essential Linux CLI Tools", "url": "/tutorials/linux-cli.html", "desc": "Supercharge your terminal with modern replacements for classic Unix commands \u2014 faster search, better output, and tools you won't want to live without.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Essential Rescue Tools", "url": "/tutorials/tools.html", "desc": "Curated list of essential offline rescue tools for every scenario.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Essential Windows Applications", "url": "/tutorials/windows-apps.html", "desc": "A comprehensive guide to the best free Windows software \u2014 from system utilities to development tools, all hand-picked for quality and usefulness. Every app here is free or open-source.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Ethical Hacking &amp; Pentesting", "url": "/tutorials/ethical-hacking-pentesting.html", "desc": "Penetration testing methodology, tools, and certifications for ethical hacking.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Event-Driven Architecture", "url": "/tutorials/event-driven-architecture.html", "desc": "Event-driven design -- events, brokers, CQRS, and event sourcing.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Example Tutorial", "url": "/tutorials/example-tutorial.html", "desc": "This is a placeholder tutorial demonstrating that new content integrates with the site\u2011wide settings, navigation, and theme system.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Express.js Deep Dive", "url": "/tutorials/express-js-deep-dive.html", "desc": "Node.js web server with Express \u2014 middleware, routing, error handling, and performance.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "F-Droid &amp; Aurora Store", "url": "/tutorials/fdroid-guide.html", "desc": "Open-source Android app stores that give you freedom, privacy, and control \u2014 no Google Play Services required.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "FFmpeg Guide", "url": "/tutorials/ffmpeg-guide.html", "desc": "Convert, compress, trim, and manipulate video/audio with FFmpeg \u2014 the ultimate multimedia CLI tool.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Fail2ban", "url": "/tutorials/fail2ban.html", "desc": "Protect your Linux server from brute-force attacks with Fail2ban intrusion prevention.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Feature Engineering for ML", "url": "/tutorials/feature-engineering.html", "desc": "Transform raw data into powerful ML features \u2014 encoding, scaling, selection, creation, and automated engineering pipelines.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Feature Flags &amp; A/B Testing", "url": "/tutorials/feature-flags-testing.html", "desc": "Feature flags, canary releases, A/B testing, and experimentation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Figma UI Design Basics", "url": "/tutorials/figma-ui-design.html", "desc": "Design interfaces, prototypes, and design systems with Figma \u2014 the industry-standard collaborative design tool.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "File Sharing with Samba & NFS", "url": "/tutorials/file-sharing-samba-nfs.html", "desc": "This guide covers setting up Samba (SMB/CIFS) and NFS file sharing on a Linux server, configuring shares, securing access, and connecting from Windows, macOS, and Linux clients.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "File Systems Compared", "url": "/tutorials/filesystems-compared.html", "desc": "Compare NTFS, ext4, Btrfs, ZFS, and APFS \u2014 features, performance, and use cases.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Firebase Firestore", "url": "/tutorials/firebase-firestore.html", "desc": "NoSQL document database with real-time sync, offline support, and security rules.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Firewall Setup Guide", "url": "/tutorials/firewall-setup.html", "desc": "Set up firewalls on Linux and Windows \u2014 UFW, firewalld, nftables basics, Windows Defender Firewall rules, and best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Firewalls &amp; Security Groups", "url": "/tutorials/firewalls-security-groups.html", "desc": "Firewalls \u2014 stateful, stateless, WAF, network ACLs, and zero-trust architecture.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Flask Web Development", "url": "/tutorials/flask-web-development.html", "desc": "Lightweight web apps with Flask \u2014 routing, templates, databases, and extensions.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Flutter Advanced Patterns", "url": "/tutorials/flutter-deep-dive.html", "desc": "Deep dive into advanced Flutter development \u2014 state management strategies, custom animations, platform channels, and testing patterns.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Flutter App Development", "url": "/tutorials/flutter-basics.html", "desc": "Cross-platform mobile development with Flutter and Dart -- widgets, state management, and native features.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Flutter Development", "url": "/tutorials/flutter-development.html", "desc": "Cross-platform mobile with Flutter \u2014 widgets, state management, and platform channels.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Focus &amp; Productivity Tools Guide", "url": "/tutorials/focus-productivity-tools.html", "desc": "Eliminate distractions and get more done with the best productivity tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Free Services Directory", "url": "/tutorials/free-services-directory.html", "desc": "A comprehensive directory of the best free-tier services across cloud storage, email, hosting, VPN, development tools, design resources, and learning platforms \u2014 with limits and requirements noted.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Freelancing &amp; Remote Work", "url": "/tutorials/freelancing-remote-work.html", "desc": "Freelance and remote work \u2014 finding clients, pricing, contracts, and productivity.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Functional Programming", "url": "/tutorials/functional-programming.html", "desc": "Functional programming \u2014 pure functions, immutability, monads, and lambda calculus.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Fuzz Testing &amp; Property-Based Testing", "url": "/tutorials/fuzz-testing-property-based.html", "desc": "Automated fuzz testing and property-based testing to discover edge cases and security vulnerabilities.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "GIMP Image Editing", "url": "/tutorials/gimp-image-editing.html", "desc": "Professional photo retouching, compositing, and graphic design with the free open-source GIMP.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "GPG &amp; PGP Key Management", "url": "/tutorials/gpg-pgp-guide.html", "desc": "Encrypt, sign, and verify with GPG. Manage keys, smartcards, and secure communication.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "GPU Architecture", "url": "/tutorials/gpu-architecture.html", "desc": "GPU architecture \u2014 shaders, CUDA cores, ray tracing, VRAM, and tensor cores.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Game Dev (Unity &amp; Unreal)", "url": "/tutorials/game-dev-unity-unreal.html", "desc": "Game development \u2014 Unity, Unreal Engine, game design patterns, and optimization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Game Loop &amp; Architecture Patterns", "url": "/tutorials/game-architecture.html", "desc": "Design robust game architecture \u2014 game loop patterns, ECS, state machines, component patterns, and code organization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Game Modding", "url": "/tutorials/game-modding.html", "desc": "Game modding \u2014 modding tools, asset creation, scripting, and distribution.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Game Optimization &amp; Tweaks", "url": "/tutorials/game-optimization.html", "desc": "Optimize games \u2014 graphics settings, FPS tweaks, launch options, and hardware tuning.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Game Repacking Guide", "url": "/tutorials/repacking-guide.html", "desc": "An in-depth explanation of game repacking \u2014 how it works, who the major repackers are, what to expect during installation, and how to stay safe while saving bandwidth and storage space.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Game Server Hosting", "url": "/tutorials/game-server-hosting.html", "desc": "Host game servers \u2014 dedicated, VPS, containerized, and performance tuning.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Gaming Piracy Guide", "url": "/tutorials/gaming-piracy-guide.html", "desc": "Download games \u2014 repacks, DLC unlockers, emulators, and ROMs.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Gatsby &amp; Static Sites", "url": "/tutorials/gatsby-static-sites.html", "desc": "Blazing-fast static sites with Gatsby \u2014 GraphQL, plugins, and the JAMstack.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Generative AI &amp; Prompt Engineering", "url": "/tutorials/generative-ai-prompt-engineering.html", "desc": "Prompt engineering, RAG, AI agents, and generative AI application development.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Git & GitHub Guide \u2014 SchooiCodes", "url": "/tutorials/git-basics.html", "desc": "A beginner-friendly guide to Git version control and GitHub \u2014 from first commit to pull requests.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "GitHub Actions", "url": "/tutorials/github-actions.html", "desc": "Automate, build, test, and deploy your code with GitHub Actions CI/CD pipelines.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "GitHub Actions CI/CD", "url": "/tutorials/github-actions-cicd.html", "desc": "Automate workflows with GitHub Actions \u2014 CI/CD, matrix builds, artifacts, and deployment.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "GitHub Portfolio &amp; Open Source", "url": "/tutorials/github-portfolio.html", "desc": "Build an impressive GitHub portfolio \u2014 profile README, project repositories, contribution graph, and personal branding.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "GitOps &amp; ArgoCD", "url": "/tutorials/gitops-argocd.html", "desc": "GitOps workflow with ArgoCD \u2014 declarative deployments, sync strategies, and multi-cluster management.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Go Programming", "url": "/tutorials/go-programming.html", "desc": "Go language -- concurrency, interfaces, tooling, and web development.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Go Programming Basics", "url": "/tutorials/go-basics.html", "desc": "Learn Go from scratch \u2014 goroutines, channels, interfaces, and CLI tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Godot Engine Game Development", "url": "/tutorials/godot-basics.html", "desc": "Get started with Godot Engine \u2014 the scene system, GDScript, 2D/3D rendering, signals, and node-based architecture.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Google Cloud Platform", "url": "/tutorials/google-cloud-platform.html", "desc": "Google Cloud -- Compute Engine, GKE, Cloud Storage, BigQuery, and IAM.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Google Cloud Run", "url": "/tutorials/google-cloud-run.html", "desc": "Serverless containers on Google Cloud \u2014 autoscaling, CI/CD, and pricing.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Google Kubernetes Engine", "url": "/tutorials/google-kubernetes-engine.html", "desc": "Managed Kubernetes on Google Cloud \u2014 GKE clusters, Workload Identity, and Autopilot.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Grafana Loki", "url": "/tutorials/grafana-loki.html", "desc": "Log aggregation -- Loki, LogQL, Promtail, and log-based alerting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Graph Databases &amp; Neo4j", "url": "/tutorials/graph-databases.html", "desc": "Cypher query language, Neo4j graph data modeling, and graph database use cases.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Graph Theory &amp; Network Analysis", "url": "/tutorials/graph-theory-network-analysis.html", "desc": "Graph algorithms, network metrics, community detection, and graph neural networks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "GraphQL API Design", "url": "/tutorials/graphql-basics.html", "desc": "Schema design, resolvers, queries, mutations, subscriptions, and Apollo GraphQL ecosystem.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "GraphQL in Practice", "url": "/tutorials/graphql-practice.html", "desc": "GraphQL -- schema design, resolvers, subscriptions, and performance.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Graphic Design", "url": "/tutorials/graphic-design.html", "desc": "Graphic design \u2014 Photoshop, GIMP, vector graphics, and visual hierarchy.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Group Policy", "url": "/tutorials/group-policy.html", "desc": "Group Policy \u2014 administrative templates, security policies, preference, and troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "HTML & CSS Basics", "url": "/tutorials/html-css-basics.html", "desc": "Build your first website from scratch \u2014 HTML structure, CSS styling, layouts, responsive design, and deployment.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "HTTP &amp; HTTPS", "url": "/tutorials/http-https.html", "desc": "HTTP/1.1, HTTP/2, HTTP/3 \u2014 methods, headers, caching, TLS, and security.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "HTTP/2 &amp; HTTP/3 Protocols", "url": "/tutorials/http2-http3.html", "desc": "Learn the evolution of HTTP \u2014 multiplexing, server push, QUIC, and performance.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Hardware Diagnostics Guide", "url": "/tutorials/hardware-diagnostics.html", "desc": "A comprehensive guide to diagnosing failing hardware \u2014 memory, storage, CPU, GPU, and system monitoring tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Hardware Security Module", "url": "/tutorials/hardware-security-module.html", "desc": "HSM for cryptographic key management \u2014 PKCS#11, AWS CloudHSM, and key ceremonies.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "HashiCorp Stack (Vault, Consul, Nomad)", "url": "/tutorials/hashicorp-vault-consul-nomad.html", "desc": "Vault for secrets, Consul for service mesh, Nomad for orchestration \u2014 the HashiCorp ecosystem.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "HashiCorp Vault", "url": "/tutorials/hashicorp-vault.html", "desc": "Secrets management -- Vault, dynamic secrets, encryption-as-a-service, auto-unseal.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "HashiCorp Vault Secrets", "url": "/tutorials/vault-secrets-management.html", "desc": "Manage secrets, encryption keys, and access control with HashiCorp Vault \u2014 secrets engines, dynamic secrets, policies, and integration patterns.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Hashing vs Encryption vs Encoding", "url": "/tutorials/hashing-vs-encryption.html", "desc": "Understand the differences between hashing, encryption, and encoding with practical examples.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Haskell Functional Programming", "url": "/tutorials/haskell-functional-programming.html", "desc": "Pure functional programming with Haskell \u2014 monads, type classes, and lazy evaluation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Headless CMS", "url": "/tutorials/headless-cms.html", "desc": "Content management -- headless CMS, content modeling, preview, workflow.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Helm Charts", "url": "/tutorials/helm-charts.html", "desc": "Kubernetes package manager \u2014 charts, templates, values, and repositories.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Hiren's Boot CD PE Guide", "url": "/tutorials/hirens-boot-cd.html", "desc": "A complete guide to Hiren's Boot CD PE \u2014 the modern Windows PE rescue environment for recovery, diagnostics, and system repair.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Home Assistant Smart Home", "url": "/tutorials/home-assistant-guide.html", "desc": "Set up Home Assistant for smart home automation \u2014 installation, integrations, automations, dashboards, and best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Home Lab", "url": "/tutorials/home-lab.html", "desc": "Build a home lab -- servers, networking, virtualization, self-hosted services.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Home Lab Guide", "url": "/tutorials/homelab-guide.html", "desc": "Build a home lab for learning and self-hosting \u2014 hardware, Proxmox, Docker, networking, services, and security.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Home Lab Hardware Guide", "url": "/tutorials/home-lab-hardware-guide.html", "desc": "Build a home lab \u2014 servers, networking, storage, and virtualization hardware for self-hosting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Homebrew &amp; macOS CLI Tools", "url": "/tutorials/homebrew-guide.html", "desc": "Master Homebrew for package management on macOS \u2014 formulae, casks, taps, and essential CLI tools every developer needs.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Honeypots &amp; Deception", "url": "/tutorials/honeypots-deception-tech.html", "desc": "Deception technology \u2014 honeypots, honeytokens, and threat intelligence gathering.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "How DNS Works (Full Walkthrough)", "url": "/tutorials/how-dns-works.html", "desc": "Follow a DNS query from browser to resolver to authoritative nameserver, step by step.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "How to BSOD your computer/laptop in 2023", "url": "/tutorials/BSOD.html", "desc": "Warning: This will force\u2011close all programs without saving. Save any work before proceeding.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "How to Create High\u2011Quality Embeds (Not GIFs)", "url": "/tutorials/embeds.html", "desc": "This tutorial shows how to embed a video so that platforms like Discord display a high\u2011quality preview (not a GIF) with optional sound on mobile devices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "How to Use and Type the ESC Character", "url": "/tutorials/ESC.html", "desc": "Tip: Save any unsaved work before experimenting with the ESC key, as some programs may react unexpectedly.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Hugo Static Site Generator", "url": "/tutorials/hugo-static-site.html", "desc": "Fastest static site generator \u2014 Go templates, content management, and themes.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Hydra Launcher Guide", "url": "/tutorials/hydra-launcher.html", "desc": "A complete guide to Hydra Launcher \u2014 an open-source game launcher with a built-in torrent client that integrates with public game repack repositories for easy downloading and management.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Hyprland Desktop Customization", "url": "/tutorials/hyprland-customization.html", "desc": "Deep dive into Hyprland \u2014 configuring animations, blur, windows rules, and eye candy.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Hyprland Tutorial", "url": "/tutorials/hyprland.html", "desc": "Hyprland is a dynamic tiling Wayland compositor. This guide covers installation, basic configuration, and useful tweaks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "IAM &amp; Identity Management", "url": "/tutorials/iam-identity-management.html", "desc": "Identity and access management \u2014 SSO, SAML, OAuth 2.0, OIDC, and just-in-time access.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "IP Obtainer (Legacy)", "url": "/tutorials/IP-Obtainer.html", "desc": "This legacy tool extracts the public IP address from a generated image file.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "IPv6 Deployment Guide", "url": "/tutorials/ipv6-deployment.html", "desc": "Address types, stateless autoconfig (SLAAC), DHCPv6, transition mechanisms, and dual-stack setup.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "ImageMagick Guide", "url": "/tutorials/imagemagick-guide.html", "desc": "Image manipulation from the CLI \u2014 convert, resize, crop, color correct, batch process, and create graphics with ImageMagick's convert and magick commands.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Incident Management &amp; On-Call", "url": "/tutorials/incident-management.html", "desc": "Build effective incident management practices \u2014 alerting, runbooks, on-call rotations, postmortems, and escalation procedures.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Information Theory", "url": "/tutorials/information-theory.html", "desc": "Entropy, mutual information, KL divergence, and channel capacity \u2014 the mathematical theory of communication.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Infrastructure as Code", "url": "/tutorials/infrastructure-as-code.html", "desc": "Terraform, Pulumi, CloudFormation \u2014 declarative infrastructure management.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Inkscape Vector Graphics", "url": "/tutorials/inkscape-vector-graphics.html", "desc": "Create logos, illustrations, and scalable vector graphics with Inkscape \u2014 the free SVG editor.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Internationalization (i18n) &amp; Localization", "url": "/tutorials/internationalization-localization.html", "desc": "Internationalize apps \u2014 i18n frameworks, translations, locale-specific formatting, and RTL support.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Internet of Things (IoT)", "url": "/tutorials/internet-of-things.html", "desc": "IoT -- sensors, MQTT, ESP32, edge computing, and security.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Introduction to Python", "url": "/tutorials/Python.html", "desc": "Python is a high\u2011level, interpreted language prized for readability and versatility across web development, data analysis, automation, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "IoT Sensor Projects", "url": "/tutorials/iot-sensor-projects.html", "desc": "Build practical IoT sensor projects \u2014 temperature, humidity, motion, and distance sensors with data logging and visualization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Istio Service Mesh", "url": "/tutorials/istio-service-mesh.html", "desc": "Deploy and manage Istio service mesh \u2014 sidecar injection, traffic management, security policies, and observability for Kubernetes.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "JAMstack Architecture", "url": "/tutorials/jamstack-architecture.html", "desc": "JAMstack -- static sites, headless CMS, serverless functions, edge rendering.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "JDownloader 2 Guide", "url": "/tutorials/jdownloader-guide.html", "desc": "Complete guide to JDownloader 2: install, configure link grabber, captcha solving, premium proxies, and automate downloads.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "JavaScript Basics", "url": "/tutorials/javascript-basics.html", "desc": "JavaScript fundamentals \u2014 variables, functions, DOM manipulation, events, async/await, and modern ES6+ syntax.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Jenkins Pipeline", "url": "/tutorials/jenkins-pipeline.html", "desc": "CI/CD with Jenkins \u2014 declarative pipeline, shared libraries, and master-agent architecture.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Julia for Scientific Computing", "url": "/tutorials/julia-scientific-computing.html", "desc": "High-performance scientific computing with Julia \u2014 multiple dispatch, parallelism, and ML.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Jupyter Notebook Mastery", "url": "/tutorials/jupyter-mastery.html", "desc": "Maximize productivity with Jupyter Notebook \u2014 magic commands, extensions, kernels, version control, and sharing workflows.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Kali Linux Basics", "url": "/tutorials/kali-linux.html", "desc": "A beginner-friendly guide to Kali Linux \u2014 installation, essential tools, and staying on the right side of the law.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Kerberos &amp; Active Directory Security", "url": "/tutorials/kerberos-active-directory.html", "desc": "Understand Kerberos protocol, AD attacks (Kerberoasting, AS-REP Roasting, Golden Ticket), and defenses.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Kiwix & ZIM Offline Server", "url": "/tutorials/kiwix-zim-server.html", "desc": "Serve Wikipedia, WikiHow, Stack Exchange, and other knowledge bases entirely offline using Kiwix and ZIM files. Perfect for areas with limited or no internet.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Kotlin Programming Basics", "url": "/tutorials/kotlin-basics.html", "desc": "Learn Kotlin from scratch -- null safety, coroutines, extension functions, and idiomatic JVM development.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Krita Digital Painting", "url": "/tutorials/krita-digital-painting.html", "desc": "Digital painting, concept art, and illustration with Krita \u2014 the professional free painting software.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Kubernetes Architecture", "url": "/tutorials/kubernetes-architecture.html", "desc": "Kubernetes cluster architecture \u2014 control plane, nodes, scheduling, and resource management.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Kubernetes Basics", "url": "/tutorials/kubernetes-basics.html", "desc": "Learn Kubernetes fundamentals \u2014 pods, deployments, services, and cluster management for container orchestration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Kubernetes Deep Dive", "url": "/tutorials/kubernetes-deep-dive.html", "desc": "Kubernetes architecture, deployments, services, ingress, and cluster management.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Kubernetes: Pods, Services &amp; Deployments", "url": "/tutorials/kubernetes-pods-services-deployments.html", "desc": "Deep dive into core Kubernetes objects with practical YAML examples.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "LLM Prompting &amp; Integration", "url": "/tutorials/llm-prompting-guide.html", "desc": "Learn prompt engineering, RAG architectures, function calling, and API integration for large language models in Python.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "LXC Linux Containers", "url": "/tutorials/lxc-containers.html", "desc": "System containers vs Docker, management with LXD, networking, and use cases.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linear Algebra Fundamentals", "url": "/tutorials/linear-algebra.html", "desc": "Matrices, vectors, eigenvalues, and linear transformations \u2014 essential math for ML and graphics.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Audio (PipeWire)", "url": "/tutorials/linux-audio-pipewire.html", "desc": "Linux audio -- PipeWire, ALSA, PulseAudio, pro-audio setup.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Audio Configuration", "url": "/tutorials/linux-audio-config.html", "desc": "Set up audio on Linux \u2014 PipeWire, PulseAudio, ALSA, and pro audio for music production.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Audio with PipeWire", "url": "/tutorials/pipewire-audio.html", "desc": "Setup, routing, low-latency configuration, Bluetooth audio, and professional audio workflows.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Backups with BorgBackup", "url": "/tutorials/borg-backup.html", "desc": "Deduplicated encrypted backups, automation cron jobs, pruning strategies, and remote repositories.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Boot Process &amp; GRUB", "url": "/tutorials/grub-boot-process.html", "desc": "GRUB configuration, initramfs, UEFI, Secure Boot, and boot troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Container Management", "url": "/tutorials/linux-container-management.html", "desc": "Docker, Podman, LXC, and container orchestration for Linux power users.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Containers (LXC/LXD)", "url": "/tutorials/linux-containers.html", "desc": "Lightweight system containers with LXC and LXD \u2014 create, manage, snapshot, and network containers.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Desktop Customization", "url": "/tutorials/linux-desktop-customization.html", "desc": "Desktop ricing -- tiling WMs, GTK theming, polybar, conky.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Disk Management: LVM, RAID &amp; Filesystems", "url": "/tutorials/linux-disk-management.html", "desc": "Manage storage with partitioning, LVM, software RAID, and filesystem tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux File Permissions", "url": "/tutorials/linux-permissions.html", "desc": "Master chmod, chown, umask, special permissions (SUID/SGID/sticky), ACLs, and SELinux basics.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Filesystem", "url": "/tutorials/linux-filesystem.html", "desc": "Linux filesystem hierarchy \u2014 FHS, inodes, permissions, ACLs, and mount points.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Firewall with nftables", "url": "/tutorials/nftables-firewall.html", "desc": "Tables, chains, rules, sets, NAT, stateful filtering, and migrating from iptables.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux From Scratch", "url": "/tutorials/linux-from-scratch.html", "desc": "Build Linux from source -- LFS, BLFS, toolchain, and customization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Kernel Modules", "url": "/tutorials/linux-kernel-modules.html", "desc": "Linux kernel modules \u2014 loading, parameters, building, and troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Laptop Buyer&#x27;s Guide 2026", "url": "/tutorials/linux-laptop-buyers-guide.html", "desc": "Find the best Linux-compatible laptop \u2014 hardware support, vendor recommendations, and specs.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Network Configuration", "url": "/tutorials/linux-network-config.html", "desc": "Configure networking on Linux \u2014 interfaces, bridges, routing, DNS, and network namespaces.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Networking", "url": "/tutorials/linux-networking.html", "desc": "Linux networking \u2014 iproute2, socket troubleshooting, firewalls, and advanced routing.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Overview", "url": "/tutorials/linux.html", "desc": "A curated collection of resources, tips, and best practices for using Linux effectively.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Package Management", "url": "/tutorials/linux-package-management.html", "desc": "Package managers \u2014 apt, dnf, pacman, emerge, snap, flatpak, and AppImage.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Performance Tuning", "url": "/tutorials/linux-performance-tuning.html", "desc": "Performance analysis \u2014 perf, flamegraphs, sysstat, cgroups, and kernel tuning.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Power User Tools", "url": "/tutorials/linux-power-user-tools.html", "desc": "Essential Linux utilities every power user should know \u2014 fd, ripgrep, fzf, bat, jq, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Printing with CUPS", "url": "/tutorials/cups-printing.html", "desc": "Print queues, driver management, network printing, troubleshooting, and cloud print integration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Process Management with systemd", "url": "/tutorials/linux-process-management.html", "desc": "Master ps, htop, systemd, cgroups, nice values, and troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Ricing Guide", "url": "/tutorials/linux-ricing-guide.html", "desc": "Rice your Linux desktop \u2014 themes, icons, cursors, conky, polybar, and aesthetic system-wide customization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux SSH Tips & Tricks", "url": "/tutorials/linux-ssh-tips.html", "desc": "Advanced SSH usage \u2014 config files, key management, tunnels, jump hosts, agent forwarding, and security hardening.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Security Hardening", "url": "/tutorials/linux-security-hardening.html", "desc": "Harden Linux \u2014 AppArmor, SELinux, auditd, secure boot, and kernel hardening.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Server Administration", "url": "/tutorials/linux-server-admin.html", "desc": "Administer Linux servers \u2014 SSH, firewalls, monitoring, user management, and automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Server Administration", "url": "/tutorials/linux-server.html", "desc": "Hardening, user management, systemd, firewalls, web servers, and monitoring \u2014 everything you need to run a Linux server.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Server Hardening", "url": "/tutorials/linux-server-hardening.html", "desc": "Secure Linux servers -- SSH, firewall, audits, and CIS benchmarks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Storage (LVM/RAID/ZFS)", "url": "/tutorials/linux-storage.html", "desc": "Advanced Linux storage \u2014 LVM, software RAID, ZFS, Btrfs, and filesystem tuning.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux System Rescue Toolkit", "url": "/tutorials/linux-system-rescue.html", "desc": "Rescue, recover, and repair Linux systems \u2014 live USB tools, chroot, fsck, and data recovery.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Linux Virtualization (KVM/LXC)", "url": "/tutorials/linux-virtualization.html", "desc": "Linux virtualization \u2014 KVM, QEMU, libvirt, LXC/LXD, and containers.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Live Streaming (OBS &amp; Twitch)", "url": "/tutorials/live-streaming-obs.html", "desc": "How to stream on Twitch/YouTube \u2014 OBS setup, overlays, alerts, and growth.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Load &amp; Performance Testing", "url": "/tutorials/load-performance-testing.html", "desc": "Performance testing \u2014 load, stress, spike, soak tests, and tooling.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Load Balancing", "url": "/tutorials/load-balancing.html", "desc": "Load balancing \u2014 algorithms, reverse proxies, health checks, and global server load balancing.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "LocalSend", "url": "/tutorials/localsend.html", "desc": "Cross-platform LAN file transfer app that works entirely offline \u2014 no internet, no cloud, no server.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Lua Scripting &amp; Embedding", "url": "/tutorials/lua-scripting-embedding.html", "desc": "Lightweight embeddable scripting language \u2014 Lua syntax, C API, and game scripting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "ML Model Deployment", "url": "/tutorials/ml-model-deployment.html", "desc": "Deploy machine learning models to production \u2014 REST APIs, Docker containers, MLflow tracking, monitoring, and MLOps best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "ML4W Hyprland Configuration", "url": "/tutorials/ml4w-hyprland.html", "desc": "ML4W (My Linux For Work) \u2014 the popular Hyprland dotfiles framework for Arch Linux.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "MLOps &amp; Model Deployment", "url": "/tutorials/mlops-model-deployment.html", "desc": "MLOps pipeline \u2014 experiment tracking, model serving, monitoring, and CI/CD for ML.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "MPLS Networking Basics", "url": "/tutorials/mpls-basics.html", "desc": "Labels, LSPs, LDP, RSVP-TE, MPLS VPNs, and traffic engineering fundamentals.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "MQTT Protocol for IoT", "url": "/tutorials/mqtt-protocol.html", "desc": "Learn the MQTT protocol for IoT communication \u2014 publish/subscribe, brokers, Quality of Service levels, topics, and security.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Machine Learning Basics", "url": "/tutorials/machine-learning-basics.html", "desc": "ML fundamentals -- supervised, unsupervised, neural networks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Machine Learning Basics with Python", "url": "/tutorials/ml-basics-python.html", "desc": "Get started with ML using scikit-learn, pandas, and Jupyter for classification and regression.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Makefile Build Automation", "url": "/tutorials/makefile-guide.html", "desc": "Targets, variables, pattern rules, and best practices for cross-platform build automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Malware Analysis Introduction", "url": "/tutorials/malware-analysis-intro.html", "desc": "Learn the fundamentals of malware analysis \u2014 static and dynamic techniques, sandboxing, and reverse engineering workflows.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Malware Removal Guide", "url": "/tutorials/malware-removal.html", "desc": "Detect and remove malware \u2014 from adware to rootkits, using both automated and manual techniques.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "MariaDB / MySQL Setup & Administration", "url": "/tutorials/mariadb-setup.html", "desc": "Install, configure, secure, and manage MariaDB or MySQL databases for production and development.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "MariaDB Deep Dive", "url": "/tutorials/mariadb-deep-dive.html", "desc": "Advanced MariaDB \u2014 storage engines, replication, Galera cluster, and performance tuning.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Markdown", "url": "/tutorials/markdown.html", "desc": "Markdown syntax -- formatting, extended features, documentation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Markdown Guide", "url": "/tutorials/markdown-guide.html", "desc": "A complete reference for Markdown \u2014 from basic syntax to extended features, flavors, and editors.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Math for Developers", "url": "/tutorials/math-for-developers.html", "desc": "Practical math for coding \u2014 discrete math, linear algebra, probability, and statistics.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Mechanical Keyboard Buyer&#x27;s Guide", "url": "/tutorials/mechanical-keyboard-guide.html", "desc": "Find the perfect mechanical keyboard \u2014 switch types, form factors, keycaps, and vendors for Linux.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Media Server Automation", "url": "/tutorials/media-server-piracy.html", "desc": "Automate your media library \u2014 Sonarr, Radarr, Lidarr, Readarr, and Prowlarr setup.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Media Server Automation Stack", "url": "/tutorials/media-server-automation.html", "desc": "Automate your entire media library \u2014 from searching and downloading to organizing and streaming. This guide covers the \"*arr\" stack with qBittorrent, Prowlarr, Bazarr, and Stremio integration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Metasploit Framework Basics", "url": "/tutorials/metasploit-basics.html", "desc": "Get started with Metasploit \u2014 the most widely used exploitation framework for penetration testing and red team operations.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Microfrontends", "url": "/tutorials/microfrontends.html", "desc": "Microfrontends \u2014 compose frontends from independent teams, frameworks, and deployments.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Microservices Architecture", "url": "/tutorials/microservices-architecture.html", "desc": "Microservices -- design, communication, data management, and deployment.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Minecraft Redstone", "url": "/tutorials/minecraft-redstone.html", "desc": "Master Minecraft redstone \u2014 logic gates, contraptions, and advanced engineering.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Minecraft Server Hosting (Aternos)", "url": "/tutorials/minecraft-aternos.html", "desc": "Aternos is a free Minecraft server hosting service. This guide covers setup, cross-version support, Bedrock crossplay, cracked mode, and common workarounds.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Mobile Accessibility", "url": "/tutorials/mobile-accessibility.html", "desc": "Make mobile apps accessible -- screen readers, contrast, touch targets.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Mobile Analytics &amp; Crash Reporting", "url": "/tutorials/mobile-analytics-crash.html", "desc": "App analytics and crash reporting -- Firebase, Sentry.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Mobile App Store Deployment", "url": "/tutorials/mobile-app-deployment.html", "desc": "End-to-end mobile app deployment \u2014 App Store Connect, Google Play Console, code signing, CI/CD pipelines, and release management.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Mobile App Testing", "url": "/tutorials/mobile-app-testing.html", "desc": "Test mobile apps \u2014 Espresso (Android), XCTests (iOS), Appium (cross-platform), and device farms.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Mobile DevOps (Fastlane)", "url": "/tutorials/mobile-devops-fastlane.html", "desc": "Mobile CI/CD -- Fastlane, automated signing, testing, deployment.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Mobile Game Dev (Unity Mobile)", "url": "/tutorials/mobile-game-dev.html", "desc": "Develop mobile games -- Unity optimization, touch controls, publishing.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Mobile Performance", "url": "/tutorials/mobile-performance.html", "desc": "Mobile app performance \u2014 profiling, memory, startup time, and rendering optimization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Mobile Security", "url": "/tutorials/mobile-security.html", "desc": "Mobile app security \u2014 OWASP Mobile Top 10, code obfuscation, and runtime protection.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Mobile UI/UX Design", "url": "/tutorials/mobile-ui-ux.html", "desc": "Design mobile interfaces \u2014 gesture design, navigation patterns, and accessibility.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Modern Shell Scripting (Zsh &amp; Fish)", "url": "/tutorials/modern-shell-scripting.html", "desc": "Syntax, functions, autocompletion, theming, and practical shell scripting in Zsh and Fish.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "MongoDB NoSQL Database", "url": "/tutorials/mongodb-guide.html", "desc": "Master MongoDB \u2014 document data model, aggregation pipeline, indexing strategies, replication, and sharding for scalable applications.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Morphe", "url": "/tutorials/morphe.html", "desc": "P2P encrypted file transfer tool for secure, high-speed, peer-to-peer sharing with no central server.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Motherboard &amp; Chipset", "url": "/tutorials/motherboard-chipset.html", "desc": "Motherboard \u2014 chipsets, PCIe lanes, VRM, form factors, and BIOS/UEFI.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Music Piracy Guide", "url": "/tutorials/music-piracy-guide.html", "desc": "Download and stream music \u2014 Spotify tools, FLAC downloads, and P2P music clients.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Music Production Basics", "url": "/tutorials/music-production-basics.html", "desc": "DAW fundamentals, MIDI, synthesis, mixing, and mastering \u2014 start making music at home.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "MyInsta &amp; Instagram Mods", "url": "/tutorials/myinsta.html", "desc": "Download Instagram mods like MyInsta and Instander to unlock media downloads, disable ads, copy comments, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Natural Language Processing", "url": "/tutorials/natural-language-processing.html", "desc": "NLP fundamentals \u2014 tokenization, embeddings, transformers, and LLM fine-tuning.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Natural Language Processing with Python", "url": "/tutorials/nlp-python.html", "desc": "Process and analyze text data with Python \u2014 spaCy, NLTK, text classification, word embeddings, transformers, and LLM integration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Neo4j Graph Database", "url": "/tutorials/neo4j-graph-database.html", "desc": "Property graph database \u2014 Cypher queries, graph modeling, and recommendations.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Neovim/Vim Editor Guide", "url": "/tutorials/neovim.html", "desc": "From beginner to power user \u2014 navigation, modes, Lua config, plugins, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Network Automation with Ansible &amp; Python", "url": "/tutorials/network-automation.html", "desc": "Automate network configuration, Netmiko, NAPALM, Ansible network modules, and CI/CD for networks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Network Monitoring with Grafana &amp; Prometheus", "url": "/tutorials/grafana-prometheus.html", "desc": "Monitor servers and networks with Prometheus metrics and Grafana dashboards.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Network Security (TLS, mTLS, PKI)", "url": "/tutorials/network-security.html", "desc": "Network security \u2014 PKI, certificates, mTLS, SSH, and secure protocols.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Network Security Monitoring", "url": "/tutorials/network-security-monitoring.html", "desc": "Monitor network traffic for threats \u2014 Zeek, Suricata, Snort, and security onion.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Network Troubleshooting Guide", "url": "/tutorials/network-troubleshooting.html", "desc": "Practical guide to diagnosing and fixing network issues using command-line tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Networking Basics", "url": "/tutorials/networking-basics.html", "desc": "Understand IP addressing, subnets, VLANs, routing, DNS, DHCP, and common network troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Networking Hardware", "url": "/tutorials/networking-hardware.html", "desc": "Network hardware \u2014 routers, switches, access points, cables, and home networking.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Next.js Full-Stack", "url": "/tutorials/nextjs-full-stack.html", "desc": "Full-stack React with Next.js \u2014 SSR, SSG, API routes, and App Router.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "NextDNS Setup Guide", "url": "/tutorials/nextdns.html", "desc": "Comprehensive guide to setting up NextDNS for enhanced privacy and security.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Nginx Reverse Proxy &amp; Load Balancing", "url": "/tutorials/nginx-reverse-proxy.html", "desc": "Configure Nginx as a reverse proxy, load balancer, and TLS terminator.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Nginx Web Server", "url": "/tutorials/nginx.html", "desc": "From installation to production \u2014 configure Nginx as a reverse proxy, static file server, and load balancer.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Nim Programming Language", "url": "/tutorials/nim-programming-language.html", "desc": "Efficient, expressive, Python-like systems programming \u2014 compile to C/JS.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "NoSQL Databases Overview", "url": "/tutorials/nosql-databases-overview.html", "desc": "NoSQL \u2014 document, key-value, wide-column, graph databases and use cases.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Node.js Guide", "url": "/tutorials/nodejs-guide.html", "desc": "Server-side JavaScript with Node.js \u2014 setup, npm, file system, Express.js, APIs, and deployment.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Note-Taking (Obsidian &amp; Notion)", "url": "/tutorials/note-taking-obsidian-notion.html", "desc": "Knowledge management \u2014 Obsidian, Notion, Zettelkasten, and personal wikis.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Note-Taking Methods for Students", "url": "/tutorials/note-taking-methods.html", "desc": "Compare the best note-taking systems for different learning styles.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "NumPy Deep Dive", "url": "/tutorials/numpy-deep-dive.html", "desc": "Master NumPy \u2014 n-dimensional arrays, vectorization, broadcasting, linear algebra operations for high-performance numerical computing.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Numerical Methods", "url": "/tutorials/numerical-methods.html", "desc": "Root finding, interpolation, numerical integration, ODE solvers \u2014 computational techniques for engineering.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "OBS Studio Streaming", "url": "/tutorials/obs-studio-streaming.html", "desc": "Professional live streaming, recording, and video production with OBS Studio \u2014 the free streaming software.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "OSINT Basics", "url": "/tutorials/osint-guide.html", "desc": "Open Source Intelligence gathering techniques \u2014 search operators, people search, domain analysis, social media investigation, and tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "OSINT Deep Dive", "url": "/tutorials/osint-deep-dive.html", "desc": "Advanced open-source intelligence techniques \u2014 passive reconnaissance, tools, and automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "OWASP Top 10 Web Vulnerabilities", "url": "/tutorials/owasp-top-10.html", "desc": "Understand and protect against the most critical web application security risks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Object-Oriented Programming", "url": "/tutorials/object-oriented-programming.html", "desc": "OOP \u2014 classes, inheritance, polymorphism, encapsulation, and SOLID principles.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Observability &amp; Telemetry", "url": "/tutorials/observability-telemetry.html", "desc": "Observability \u2014 logs, metrics, traces, OpenTelemetry, and alerting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Off-Grid Messaging (Briar, Meshtastic, Yggdrasil)", "url": "/tutorials/offgrid-messaging.html", "desc": "Communicate when the internet goes down. These tools let you message others over Bluetooth, LoRa radio, or mesh networking without relying on cell towers or ISPs.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Communication Mesh", "url": "/tutorials/offline-communication.html", "desc": "Communicate without internet \u2014 mesh networks, LoRa radio, and emergency broadcast tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Developer Knowledge Bases", "url": "/tutorials/offline-dev-knowledge-bases.html", "desc": "Access API documentation, cheat sheets, and developer references without an internet connection. Essential for remote work, travel, or disaster scenarios.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Knowledge Bases", "url": "/tutorials/knowledge-bases.html", "desc": "Download and serve offline knowledge bases \u2014 Wikipedia, Stack Exchange, and technical docs.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Maps & Navigation", "url": "/tutorials/offline-maps-navigation.html", "desc": "Navigate anywhere without an internet connection. This guide covers the best tools for downloading maps, importing GPX tracks, and navigating offline.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Maps &amp; Navigation", "url": "/tutorials/maps.html", "desc": "Download offline maps for navigation when there's no data connection.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Offline Wikivoyage &amp; Travel Guides", "url": "/tutorials/offline-wikis.html", "desc": "Carry travel guides, phrasebooks, and survival knowledge offline \u2014 Kiwix ZIMs for travelers.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Online Safety & Digital Hygiene", "url": "/tutorials/online-safety-guide.html", "desc": "A practical guide to staying safe online \u2014 from password hygiene to phishing detection, browser security, and beyond.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Open Source Contribution", "url": "/tutorials/open-source-contribution.html", "desc": "Contribute to open source \u2014 finding projects, making PRs, community etiquette, and maintainer tips.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Open Source Contribution Guide", "url": "/tutorials/open-source-contributions.html", "desc": "Start contributing to open source \u2014 finding projects, PR workflow, community etiquette, and building your reputation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Open Source Software Alternatives", "url": "/tutorials/open-source-software-alternatives.html", "desc": "Free and open-source alternatives to popular proprietary software across all categories.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Oracle Database Basics", "url": "/tutorials/oracle-database-basics.html", "desc": "Enterprise relational database \u2014 SQL*Plus, PL/SQL, and Oracle architecture.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Orion Store", "url": "/tutorials/orion-store.html", "desc": "A powerful Android app manager for batch APK installation, app backup and restore, APK export, and app freezing \u2014 all in one tool.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "PC Builder&#x27;s Guide 2026", "url": "/tutorials/pc-builders-guide-2026.html", "desc": "Build the perfect PC for Linux \u2014 parts compatibility, vendor picks, and build guide.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "PC Building Guide", "url": "/tutorials/pc-building-guide.html", "desc": "Build your own PC \u2014 component selection, assembly, and benchmarking.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "PHP Web Development", "url": "/tutorials/php-basics.html", "desc": "PHP syntax, PDO, MVC patterns, and modern web development with Laravel and Composer.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "PKI &amp; Certificate Management", "url": "/tutorials/pki-certificate-management.html", "desc": "Public Key Infrastructure \u2014 CA, certificates, ACME, cert-manager, and mTLS.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Packer &amp; Vagrant", "url": "/tutorials/packer-vagrant.html", "desc": "Immutable infrastructure \u2014 Packer images and Vagrant environments for development.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Packer Image Building", "url": "/tutorials/packer-guide.html", "desc": "Automate machine image creation with Packer \u2014 build immutable infrastructure with multi-cloud builders, provisioners, and post-processors.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Pandas Data Analysis", "url": "/tutorials/pandas-deep-dive.html", "desc": "Master Pandas for data manipulation \u2014 DataFrames, groupby operations, merging datasets, time series analysis, and performance optimization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Password Reset &amp; Recovery", "url": "/tutorials/password-reset.html", "desc": "Reset forgotten passwords, bypass lock screens, and recover credentials \u2014 legally and safely.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Password Security Guide", "url": "/tutorials/password-security.html", "desc": "Password managers, 2FA/MFA, passkeys, creating strong passwords, and security best practices for accounts.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Paysafe & Online Money Transfer Guide", "url": "/tutorials/paysafe-money-transfer.html", "desc": "A practical guide to using Paysafe (paysafecard) for online payments, along with a comparison of alternatives like PayPal, Wise, Skrill, and Revolut for different use cases.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Personal Knowledge Management", "url": "/tutorials/knowledge-management.html", "desc": "Build a personal knowledge management system \u2014 note-taking methods, PARA, Zettelkasten, and knowledge base tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Personal Knowledge Management", "url": "/tutorials/personal-knowledge-management.html", "desc": "PKM -- second brain, Zettelkasten, dashboards, and knowledge synthesis.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Platform Engineering", "url": "/tutorials/platform-engineering.html", "desc": "Platform engineering \u2014 internal developer platforms, Backstage, and golden paths.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Plex & Jellyfin Media Server Setup", "url": "/tutorials/plex-jellyfin-setup.html", "desc": "Complete guide to setting up Plex and Jellyfin media servers on Windows and Linux. Compare features, install, configure, and optimize both.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Podcast Production Guide", "url": "/tutorials/podcast-production.html", "desc": "Plan, record, edit, and publish a professional podcast \u2014 from equipment to distribution.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Podman Container Management", "url": "/tutorials/podman-guide.html", "desc": "Daemonless containers, rootless execution, pods, Docker compatibility, and Quadlet systemd integration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "PostgreSQL", "url": "/tutorials/postgresql.html", "desc": "The world's most advanced open-source relational database \u2014 from setup to performance tuning.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "PowerShell Basics", "url": "/tutorials/powershell.html", "desc": "A comprehensive introduction to PowerShell for beginners \u2014 from cmdlets to scripting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "PowerShell Scripting", "url": "/tutorials/powershell-scripting.html", "desc": "PowerShell \u2014 cmdlets, pipelines, remoting, modules, and automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "PowerShell Scripting", "url": "/tutorials/windows-powershell-scripting.html", "desc": "Go beyond basic PowerShell \u2014 functions, modules, error handling, remoting, scheduled jobs, and script security.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Probability &amp; Statistics", "url": "/tutorials/probability-statistics.html", "desc": "Probability distributions, hypothesis testing, Bayesian inference \u2014 the foundation of data science and ML.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Procedural Content Generation", "url": "/tutorials/procedural-generation.html", "desc": "Generate game content procedurally \u2014 noise functions, dungeon generation, terrain algorithms, and PCG design patterns.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Programming for Beginners", "url": "/tutorials/programming-beginners.html", "desc": "Learn programming from scratch \u2014 first language, projects, and learning paths.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Progressive Web Apps (PWAs)", "url": "/tutorials/progressive-web-apps.html", "desc": "Build installable, offline-first web apps \u2014 service workers, cache strategies, and push notifications.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Prometheus &amp; Grafana", "url": "/tutorials/prometheus-grafana.html", "desc": "Monitoring and alerting \u2014 Prometheus metrics, exporters, alertmanager, and Grafana dashboards.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Proxmox VE Setup & Management", "url": "/tutorials/proxmox-setup.html", "desc": "Install, configure, and manage Proxmox Virtual Environment for your homelab or production infrastructure.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Proxy Guide", "url": "/tutorials/proxy-guide.html", "desc": "Set up and use proxies \u2014 HTTP/HTTPS/SOCKS5, reverse proxies with Nginx/Caddy, proxy chaining, and privacy considerations.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Push Notifications", "url": "/tutorials/push-notifications.html", "desc": "Push notifications \u2014 FCM, APNs, notification channels, and best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Python Advanced", "url": "/tutorials/python-advanced.html", "desc": "Advanced Python -- decorators, generators, context managers, async, and metaprogramming.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "QoS &amp; Traffic Shaping", "url": "/tutorials/qos-traffic-shaping.html", "desc": "Prioritization, shaping, policing, DiffServ, CoS, and practical QoS configuration on routers and Linux.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Quantum Computing", "url": "/tutorials/quantum-computing.html", "desc": "Quantum computing -- qubits, gates, algorithms, and quantum programming.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "R Statistical Computing", "url": "/tutorials/r-statistical-computing.html", "desc": "Statistical computing and data visualization with R \u2014 tidyverse, ggplot2, and Shiny.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "RAID Levels Explained", "url": "/tutorials/raid-levels-explained.html", "desc": "Understand RAID 0, 1, 5, 6, 10, 50, and 60 \u2014 performance, redundancy, and trade-offs.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "RAM &amp; Memory", "url": "/tutorials/ram-memory.html", "desc": "Memory \u2014 DDR5, DIMM, latency, dual-channel, ECC, and memory overclocking.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "REST API Basics", "url": "/tutorials/api-basics.html", "desc": "A primer on RESTful APIs \u2014 HTTP methods, status codes, authentication, testing, and best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "REST API Design Patterns", "url": "/tutorials/rest-api-design-patterns.html", "desc": "REST API patterns -- HATEOAS, pagination, filtering, error handling.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "ROS 2 Robotics", "url": "/tutorials/ros2-robotics.html", "desc": "Robot Operating System 2 \u2014 nodes, topics, services, actions, and robot simulation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Ransomware Response", "url": "/tutorials/ransomware-response.html", "desc": "Immediate steps during a ransomware attack \u2014 isolate, assess, and recover without paying.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Raspberry Pi Projects &amp; GPIO", "url": "/tutorials/raspberry-pi-gpio.html", "desc": "Raspberry Pi fundamentals \u2014 GPIO programming, sensors, automation, and project ideas.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Raspberry Pi Setup Guide", "url": "/tutorials/raspberry-pi-setup.html", "desc": "Set up a Raspberry Pi from scratch \u2014 headless install, SSH, GPIO, config, useful projects, and troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "ReVanced Guide", "url": "/tutorials/revanced-guide.html", "desc": "Patch Android APKs with ReVanced to remove ads, add features, and customize apps like YouTube, Reddit, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "React Basics", "url": "/tutorials/react-basics.html", "desc": "Build modern UIs with React \u2014 components, props, state, hooks, effects, routing, and project setup.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "React Native", "url": "/tutorials/react-native.html", "desc": "Cross-platform mobile apps with React Native \u2014 components, navigation, and native modules.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "React Native Cross-Platform", "url": "/tutorials/react-native-development.html", "desc": "Build mobile apps for iOS and Android with React Native and Expo.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "React Native Mobile Development", "url": "/tutorials/react-native-basics.html", "desc": "Build cross-platform mobile apps with React Native \u2014 core components, navigation, native modules, and performance optimization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Redis", "url": "/tutorials/redis.html", "desc": "An in-memory data store used for caching, real-time messaging, session management, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Redis Deep Dive", "url": "/tutorials/redis-deep-dive.html", "desc": "Advanced Redis \u2014 data structures, persistence, clustering, and caching patterns.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Regex", "url": "/tutorials/regex.html", "desc": "Regular expressions -- patterns, groups, lookaheads, applications.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Reinforcement Learning", "url": "/tutorials/reinforcement-learning.html", "desc": "RL fundamentals \u2014 Q-learning, policy gradients, PPO, DQN, and real-world applications.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "RethinkDNS Tutorial", "url": "/tutorials/rethinkdns.html", "desc": "RethinkDNS is a privacy\u2011focused DNS resolver that offers easy configuration across devices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Retro Gaming &amp; Emulation", "url": "/tutorials/retro-gaming-emulation.html", "desc": "Retro gaming \u2014 emulators, ROMs, upscaling, and original hardware preservation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Reverse Engineering Basics", "url": "/tutorials/reverse-engineering-basics.html", "desc": "Understand the core techniques of reverse engineering \u2014 disassembly, debugging, decompilation, and binary patching with industry tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Robotics", "url": "/tutorials/robotics.html", "desc": "Robotics -- ROS 2, kinematics, SLAM, navigation, computer vision.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Routing Protocols (BGP &amp; OSPF)", "url": "/tutorials/routing-protocols.html", "desc": "Dynamic routing \u2014 BGP, OSPF, IS-IS, route redistribution, and network design.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Ruby Programming Basics", "url": "/tutorials/ruby-basics.html", "desc": "Ruby syntax, blocks, metaprogramming, and Rails web development fundamentals.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Rust Programming", "url": "/tutorials/rust-programming.html", "desc": "Systems programming with Rust -- ownership, borrowing, lifetimes, and concurrency.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Rust Programming Basics", "url": "/tutorials/rust-basics.html", "desc": "Learn Rust from scratch \u2014 ownership, borrowing, structs, enums, and error handling.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SDDM Display Manager Customization", "url": "/tutorials/sddm-customization.html", "desc": "Theme, configure, and customize SDDM \u2014 the modern Linux display manager for KDE Plasma.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SDN &amp; Network Automation", "url": "/tutorials/sdn-network-automation.html", "desc": "Software-Defined Networking \u2014 OpenFlow, SDN controllers, NetOps, and automation tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SELinux Policy Writing", "url": "/tutorials/selinux-policy-writing.html", "desc": "Master SELinux policy development \u2014 understand contexts, booleans, type enforcement, and audit log analysis for mandatory access control.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SIEM &amp; SOAR", "url": "/tutorials/siem-soar.html", "desc": "Security information and event management \u2014 SIEM correlation, SOAR automation, and incident response.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SMT System Multitool Guide", "url": "/tutorials/smt-multitool.html", "desc": "SMT (System Multitool) is a batch-powered Windows utility collection with over 90 tools for networking, system configuration, activation, security research, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SNMP Network Monitoring", "url": "/tutorials/snmp-monitoring.html", "desc": "MIBs, OIDs, traps, snmpwalk, SNMPv3 security, and integration with monitoring tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SQL Database Basics", "url": "/tutorials/sql-basics.html", "desc": "Learn Structured Query Language \u2014 from simple SELECT queries to complex JOINs and subqueries.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SQL Server &amp; T-SQL", "url": "/tutorials/sql-server-tsql.html", "desc": "Microsoft SQL Server \u2014 T-SQL, indexes, SSIS, SSRS, and high availability.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SQLite Embedded Database", "url": "/tutorials/sqlite-guide.html", "desc": "Master SQLite \u2014 the world's most widely deployed embedded SQL database engine for mobile, desktop, and server applications.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SRE Fundamentals", "url": "/tutorials/sre-fundamentals.html", "desc": "Learn Site Reliability Engineering principles \u2014 SLIs, SLOs, error budgets, toil reduction, and building reliable distributed systems.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SRE Principles", "url": "/tutorials/sre-principles.html", "desc": "Site Reliability Engineering \u2014 SLIs, SLOs, error budgets, and incident management.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SRE Runbooks &amp; On-Call", "url": "/tutorials/sre-runbooks.html", "desc": "Site Reliability -- runbooks, incident response, on-call, and postmortems.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SSH Guide", "url": "/tutorials/ssh-guide.html", "desc": "Master the Secure Shell \u2014 keys, config, tunneling, and remote administration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SSL & HTTPS Certificates", "url": "/tutorials/ssl-certificates.html", "desc": "Understand TLS, get free certificates with Let's Encrypt, and secure your web services properly.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SVG Animation with CSS &amp; JS", "url": "/tutorials/svg-animation-css-js.html", "desc": "Create smooth, interactive SVG animations using CSS, JavaScript, and GSAP.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Safe Piracy &amp; VPN Guide", "url": "/tutorials/safe-piracy.html", "desc": "Stay safe while pirating \u2014 VPNs, opsec, malware scanning, and legal awareness.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Scala &amp; Functional JVM", "url": "/tutorials/scala-functional-jvm.html", "desc": "Scala combines OOP and functional programming on the JVM \u2014 Akka, Play, and Cats.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Screen Reader Testing &amp; ARIA", "url": "/tutorials/screen-reader-testing.html", "desc": "Test websites with screen readers \u2014 NVDA, VoiceOver, JAWS \u2014 and implement ARIA roles, properties, and best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Seal &amp; ulapp", "url": "/tutorials/seal-ulapp.html", "desc": "Android video downloader (Seal) and LAN file sharing app (ulapp) for offline media.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Security Breach Response", "url": "/tutorials/security-breach-response.html", "desc": "A comprehensive step-by-step guide for identifying, containing, and recovering from a security breach \u2014 from immediate triage to full system restoration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Self-Hosted Software Guide", "url": "/tutorials/self-hosted-software-guide.html", "desc": "Self-host your own services \u2014 media, cloud storage, password manager, monitoring, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Server Monitoring", "url": "/tutorials/monitoring.html", "desc": "Monitor server metrics, visualize data, and set up alerts using Prometheus and Grafana.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Serverless &amp; Event-Driven", "url": "/tutorials/serverless-event-driven.html", "desc": "Serverless architecture -- Lambda, event-driven patterns, and best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Service Mesh (Istio)", "url": "/tutorials/service-mesh-istio.html", "desc": "Service mesh with Istio \u2014 sidecar proxy, traffic management, security, and observability.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Setting Up Offline Servers", "url": "/tutorials/servers.html", "desc": "Run local servers for offline use \u2014 DHCP, DNS, file sharing, and media streaming without internet.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Shell Scripting &amp; Dotfiles", "url": "/tutorials/shell-scripting-dotfiles-mastery.html", "desc": "Master shell scripting (bash/zsh) and manage dotfiles for a reproducible development environment.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Shizuku &amp; Hail", "url": "/tutorials/shizuku-hail.html", "desc": "Manage system apps, debloat your device, and freeze/unfreeze apps without root using Shizuku and Hail.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Smartphone Buyer&#x27;s Guide 2026", "url": "/tutorials/smartphone-buyers-guide.html", "desc": "Choose the best smartphone \u2014 Android vs iOS, camera, performance, battery, and value picks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Social Engineering Awareness Guide", "url": "/tutorials/social-engineering.html", "desc": "Recognize and defend against phishing, pretexting, baiting, and manipulation tactics.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Social Media Privacy Guide", "url": "/tutorials/social-media-privacy.html", "desc": "Platform-by-platform privacy settings, data deletion guides, app permissions, and privacy-focused alternatives to mainstream social media.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Software Piracy Guide", "url": "/tutorials/software-piracy-guide.html", "desc": "Download cracked software \u2014 sources, activation tools, and safety checks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Software Testing", "url": "/tutorials/software-testing.html", "desc": "Testing \u2014 unit, integration, e2e, TDD, mocking, and test automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Software Testing 101", "url": "/tutorials/testing-101.html", "desc": "Master unit, integration, and E2E testing with pytest, Vitest, and Playwright.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Software-Defined Networking", "url": "/tutorials/sdn-overview.html", "desc": "SDN architecture, OpenFlow, network virtualization, controllers, and practical SDN implementations.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Spicetify", "url": "/tutorials/spicetify.html", "desc": "Customize the Spotify desktop client with themes, extensions, and custom CSS using the Spicetify CLI modding tool.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Spring Boot Development", "url": "/tutorials/spring-boot-development.html", "desc": "Enterprise Java with Spring Boot \u2014 auto-configuration, data JPA, security, and microservices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Static Site Generators", "url": "/tutorials/static-site-generators.html", "desc": "Build static sites -- SSG comparison, build process, deployment strategies.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Statistical Modeling", "url": "/tutorials/statistical-modeling.html", "desc": "Linear models, generalized linear models, mixed effects, and model selection for data analysis.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Storage (SSD, NVMe, HDD)", "url": "/tutorials/storage-ssd-nvme.html", "desc": "Storage technology \u2014 SSD, NVMe, HDD, RAID, and data reliability.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Streaming Sites Guide", "url": "/tutorials/streaming-sites-guide.html", "desc": "Find working streaming sites for movies and TV \u2014 safe links, ad blocking, and troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Study Techniques", "url": "/tutorials/study-techniques.html", "desc": "Effective studying \u2014 active recall, spaced repetition, note-taking, and exam prep.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Subnetting &amp; CIDR Explained", "url": "/tutorials/subnetting-cidr.html", "desc": "Understand IP subnetting, CIDR notation, VLSM, and subnet calculation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Svelte &amp; SvelteKit", "url": "/tutorials/svelte-sveltekit.html", "desc": "Compile-time React alternative \u2014 reactive declarations, stores, and SvelteKit.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Swift Programming Basics", "url": "/tutorials/swift-basics.html", "desc": "Learn Apple's Swift -- optionals, structs, protocols, and modern iOS/macOS development fundamentals.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "SwiftUI for iOS Development", "url": "/tutorials/swiftui-basics.html", "desc": "Learn SwiftUI for building declarative iOS interfaces \u2014 state management, data flow, navigation patterns, and best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "System Design", "url": "/tutorials/system-design.html", "desc": "System design \u2014 scalability, caching, load balancing, and distributed systems.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "System Design Interviews", "url": "/tutorials/system-design-interviews.html", "desc": "Ace system design interviews \u2014 scalability, databases, caching, load balancing, and distributed systems.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "System Rescue Deep Dive", "url": "/tutorials/system-rescue.html", "desc": "Boot and repair broken systems \u2014 bootloaders, filesystem repair, and offline malware removal.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Systemd &amp; Services", "url": "/tutorials/systemd-services.html", "desc": "Systemd \u2014 units, targets, timers, journald, and service management.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Systemd Service Guide", "url": "/tutorials/systemd-guide.html", "desc": "Create and manage systemd services, timers, sockets, and targets \u2014 journalctl, unit files, and troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "TCP/IP &amp; OSI Model", "url": "/tutorials/tcpip-osi-model.html", "desc": "Understand the TCP/IP stack and OSI model \u2014 layers, protocols, and packet flow.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Tails OS Guide", "url": "/tutorials/tails.html", "desc": "A complete walkthrough of Tails \u2014 the amnesic incognito live system that leaves no trace and routes everything through Tor.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Task Automation Guide", "url": "/tutorials/automation.html", "desc": "Automate everything \u2014 cron, systemd timers, scripts, and CI/CD pipelines.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Tech Freelancing Guide", "url": "/tutorials/freelancing-guide.html", "desc": "Start and grow a tech freelancing business \u2014 rates, contracts, client acquisition, platforms, and financial management.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Tech Resume Writing Guide", "url": "/tutorials/tech-resume-guide.html", "desc": "Write an effective tech resume \u2014 structure, keywords, achievements, ATS optimization, and industry-specific advice.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Technical Interview Preparation", "url": "/tutorials/technical-interviewing.html", "desc": "Prepare for technical interviews \u2014 coding challenges, system design, behavioral questions, salary negotiation, and strategy.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Technical Writing &amp; Documentation", "url": "/tutorials/technical-writing-documentation.html", "desc": "Write clear technical documentation \u2014 API docs, tutorials, README files, and knowledge bases.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Telegram Privacy Guide", "url": "/tutorials/telegram-privacy.html", "desc": "A comprehensive walkthrough of every Telegram privacy setting to lock down your account and protect your identity.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Terminal Color Schemes & Themes", "url": "/tutorials/color-schemes.html", "desc": "Make your terminal beautiful \u2014 ANSI codes, popular themes, tools, and configuration for every emulator.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Terraform Cloud &amp; Enterprise", "url": "/tutorials/terraform-cloud-enterprise.html", "desc": "Terraform Cloud -- remote state, workspaces, Sentinel, cost estimation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Terraform Infrastructure", "url": "/tutorials/terraform-infrastructure.html", "desc": "Infrastructure as Code with Terraform \u2014 HCL, state management, modules, and providers.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Terraform Infrastructure as Code", "url": "/tutorials/terraform-basics.html", "desc": "Learn Terraform \u2014 HCL, providers, state management, modules, and workspaces.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Time Management", "url": "/tutorials/time-management.html", "desc": "Manage time effectively \u2014 productivity systems, prioritization, and habit building.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Time Management Guide for Students", "url": "/tutorials/time-management-guide.html", "desc": "Master your schedule with proven time management techniques.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Time-Series Databases with InfluxDB", "url": "/tutorials/influxdb-guide.html", "desc": "Learn InfluxDB for time-series data \u2014 data model, Flux queries, downsampling, retention policies, IoT and monitoring use cases.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Tmux Guide", "url": "/tutorials/tmux-guide.html", "desc": "Terminal multiplexing with tmux \u2014 sessions, windows, panes, keybindings, customisation, and pair programming.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Torrent Clients Guide", "url": "/tutorials/torrent-clients-guide.html", "desc": "Complete guide to qBittorrent, Transmission, and Deluge torrent clients. Installation, configuration, VPN binding, port forwarding, and optimization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Torrenting Guide", "url": "/tutorials/torrenting-guide.html", "desc": "Torrent safely \u2014 clients, sites, private trackers, port forwarding, and ratio management.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Two-Factor Authentication Guide", "url": "/tutorials/two-factor-auth.html", "desc": "Everything you need to know about 2FA, TOTP, hardware keys, passkeys, and securing your accounts with a second factor.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "TypeScript", "url": "/tutorials/typescript.html", "desc": "JavaScript with superpowers \u2014 static types, interfaces, generics, and modern tooling.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Typography &amp; Color Theory", "url": "/tutorials/typography-color-theory.html", "desc": "Typography and color theory \u2014 typefaces, color harmony, contrast, and accessibility.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "UI/UX Design (Figma)", "url": "/tutorials/ui-ux-figma.html", "desc": "UI/UX design with Figma \u2014 components, auto layout, prototyping, and design systems.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Unity Game Engine Introduction", "url": "/tutorials/unity-basics.html", "desc": "Introduction to Unity game development \u2014 GameObjects, components, physics, C# scripting, and editor workflow.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "VLANs &amp; Trunking Guide", "url": "/tutorials/vlans-trunking.html", "desc": "802.1Q VLAN tagging, trunk ports, access ports, inter-VLAN routing, and troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "VPN Setup Guide", "url": "/tutorials/vpn-setup.html", "desc": "Set up WireGuard and OpenVPN \u2014 server configuration, client setup, key generation, routing, and troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "VPNs &amp; Tunneling", "url": "/tutorials/vpn-tunneling.html", "desc": "Virtual Private Networks \u2014 WireGuard, OpenVPN, IPsec, and secure site-to-site connections.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "VS Code Setup & Extensions", "url": "/tutorials/vscode.html", "desc": "A comprehensive guide to setting up VS Code for development.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Vagrant Development Environments", "url": "/tutorials/vagrant-guide.html", "desc": "Create reproducible development environments with Vagrant \u2014 multi-machine setups, provisioning, networking, and synced folders.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Vencord &amp; Vesktop", "url": "/tutorials/vencord-vesktop.html", "desc": "Mod your Discord client with plugins, themes, and quality-of-life improvements using Vencord and the standalone Vesktop client.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Ventoy Advanced Guide", "url": "/tutorials/ventoy.html", "desc": "Multi-boot USB mastery \u2014 run dozens of ISOs from a single drive without reformatting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Ventoy Themes &amp; Customization", "url": "/tutorials/ventoy-themes.html", "desc": "Customize Ventoy with themes, boot splash screens, and personalized ISO menus.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "VeraCrypt Full Disk Encryption", "url": "/tutorials/veracrypt-encryption.html", "desc": "Secure your data with VeraCrypt \u2014 full disk, partition, and container encryption for all platforms.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Version Control (Git Deep Dive)", "url": "/tutorials/git-deep-dive.html", "desc": "Git internals \u2014 branching, rebasing, hooks, and advanced workflows.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Video Editing", "url": "/tutorials/video-editing.html", "desc": "Video editing \u2014 DaVinci Resolve, Premiere Pro, color grading, and motion graphics.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Video Editing with Kdenlive", "url": "/tutorials/kdenlive-video-editing.html", "desc": "Professional non-linear video editing with Kdenlive \u2014 the free open-source video editor.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Virtual Machines Guide", "url": "/tutorials/virtual-machines.html", "desc": "A beginner's guide to virtual machines with VirtualBox and VMware.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "VirtualBox vs VMware vs Hyper-V", "url": "/tutorials/virtualbox-vmware-hyperv.html", "desc": "Compare the major hypervisors for desktop and server virtualization.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Vue.js &amp; Nuxt.js", "url": "/tutorials/vuejs-nuxtjs.html", "desc": "Progressive framework Vue.js with Nuxt.js \u2014 composition API, Pinia, SSR.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "WCAG Web Accessibility Standards", "url": "/tutorials/wcag-standards.html", "desc": "Understand WCAG accessibility standards \u2014 POUR principles, conformance levels, success criteria, and compliance testing.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "WSL 2", "url": "/tutorials/wsl-2.html", "desc": "Windows Subsystem for Linux 2 \u2014 full Linux kernel, VS Code integration, and Docker.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "WSL2 Complete Guide", "url": "/tutorials/wsl2-guide.html", "desc": "Run a full Linux kernel inside Windows \u2014 install, manage, and configure WSL2.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Wayland vs X11", "url": "/tutorials/wayland-x11.html", "desc": "Display servers -- Wayland architecture, X11 comparison, migration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Web Application Firewall", "url": "/tutorials/web-application-firewall.html", "desc": "WAF configuration \u2014 ModSecurity, Cloudflare WAF, rate limiting, and rule tuning.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Web Application Security", "url": "/tutorials/web-application-security.html", "desc": "OWASP Top 10, XSS, CSRF, SQL injection, and securing web applications.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Web Auth (OAuth, JWT, SAML)", "url": "/tutorials/web-authentication.html", "desc": "Web authentication -- OAuth 2.0, OpenID Connect, JWT, SAML, WebAuthn.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Web Performance Optimization", "url": "/tutorials/web-performance.html", "desc": "Core Web Vitals, lazy loading, caching, CDN, and performance budgets.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Web Scraping", "url": "/tutorials/web-scraping.html", "desc": "Web scraping -- HTTP requests, HTML parsing, anti-bot bypass.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "WebAssembly", "url": "/tutorials/webassembly.html", "desc": "High-performance browser code -- Wasm, WASI, Emscripten, and tooling.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "WebAssembly (Wasm)", "url": "/tutorials/webassembly-wasm.html", "desc": "Run C/C++/Rust in the browser with WebAssembly \u2014 compilation, memory, and performance.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "WebSockets &amp; Real-Time Communication", "url": "/tutorials/websockets-guide.html", "desc": "Build real-time apps with WebSockets, Socket.IO, and WebRTC.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "WebSockets &amp; SSE", "url": "/tutorials/websockets-sse.html", "desc": "Real-time web -- WebSockets, Server-Sent Events, WebRTC data channels.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "WebXR &amp; Augmented Reality", "url": "/tutorials/webxr-augmented-reality.html", "desc": "Build AR/VR experiences for the web with WebXR API, A-Frame, and React Three Fiber.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Wi-Fi Penetration Testing", "url": "/tutorials/wifi-pentesting.html", "desc": "Assess wireless security \u2014 WPA2/WPA3 cracking, evil twin, and deauthentication attacks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Wi-Fi Security Guide", "url": "/tutorials/wifi-security.html", "desc": "Secure your Wi-Fi network \u2014 WPA2/WPA3, 802.1X, guest networks, deauth protection, and auditing.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows 11 Features Guide", "url": "/tutorials/windows-11-features.html", "desc": "New features, settings, changes from Windows 10, and power user tips.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Automation (PowerShell DSC)", "url": "/tutorials/windows-automation.html", "desc": "Windows automation -- PowerShell remoting, DSC, scheduled tasks.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows BitLocker Deep Dive", "url": "/tutorials/bitlocker-deep-dive.html", "desc": "Full disk encryption, TPM, recovery keys, BitLocker management, and enterprise deployment.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Debloating & Optimization", "url": "/tutorials/windows-debloat.html", "desc": "A complete guide to removing bloatware, disabling telemetry, and optimizing Windows 10/11 for performance and privacy.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Defender &amp; Security Center Guide", "url": "/tutorials/windows-defender-security.html", "desc": "Configure Microsoft Defender, ASR rules, firewall, and ransomware protection.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Deployment (MDT/SCCM)", "url": "/tutorials/windows-deployment.html", "desc": "Deploy Windows at scale -- MDT, SCCM, imaging, PXE boot.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Environment Variables", "url": "/tutorials/windows-environment-variables.html", "desc": "Understand and manage Windows environment variables \u2014 PATH, system vs user, setx, PowerShell, and common use cases.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Event Viewer &amp; Troubleshooting", "url": "/tutorials/windows-event-viewer.html", "desc": "Master Event Viewer for system diagnostics and troubleshooting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Group Policy Editor", "url": "/tutorials/gpedit-guide.html", "desc": "Local Group Policy, administrative templates, security policies, and computer configuration management.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Hardening Guide", "url": "/tutorials/windows-hardening.html", "desc": "Harden Windows 10/11 \u2014 Attack Surface Reduction, Windows Defender, AppLocker, BitLocker, user account security, and group policy.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Intune &amp; Endpoint Manager", "url": "/tutorials/windows-intune.html", "desc": "Cloud device management -- Microsoft Intune, Autopilot, compliance.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Keyboard Shortcuts", "url": "/tutorials/windows-shortcuts.html", "desc": "Essential Windows keyboard shortcuts for power users \u2014 desktop, file explorer, task manager, virtual desktops, and hidden shortcuts.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Networking", "url": "/tutorials/windows-networking.html", "desc": "Windows networking \u2014 DNS, DHCP, RRAS, NLB, and monitoring tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Performance &amp; Troubleshooting", "url": "/tutorials/windows-performance.html", "desc": "Windows performance tuning, diagnostics, and recovery tools.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Performance Monitor", "url": "/tutorials/windows-perfmon.html", "desc": "Data collector sets, performance counters, reports, and troubleshooting with PerfMon.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Recovery & Rescue", "url": "/tutorials/windows-rescue.html", "desc": "Windows Recovery Environment, DISM, SFC, bootrec, system restore, restore points, advanced startup, and repairing Windows without reinstalling.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Registry", "url": "/tutorials/windows-registry.html", "desc": "Windows Registry \u2014 hives, keys, values, editing, backup, and forensic analysis.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Registry Hacks &amp; Tweaks", "url": "/tutorials/windows-registry-hacks.html", "desc": "Advanced registry tricks for performance, UI, security, and automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Remote Desktop Guide", "url": "/tutorials/windows-remote-desktop.html", "desc": "RDP configuration, gateway, security best practices, and third-party alternatives.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Sandbox Guide", "url": "/tutorials/windows-sandbox.html", "desc": "Isolated test environment using Windows Sandbox, configuration files, and practical use cases.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Security", "url": "/tutorials/windows-security.html", "desc": "Windows security \u2014 Defender, BitLocker, Windows Hello, and attack surface reduction.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Server", "url": "/tutorials/windows-server.html", "desc": "Windows Server \u2014 roles, IIS, Hyper-V, Windows Admin Center, and Nano Server.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Software Alternatives on Linux", "url": "/tutorials/windows-software-alternatives-linux.html", "desc": "Find Linux replacements for popular Windows software \u2014 Adobe, Office, gaming, and more.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Subsystem for Android", "url": "/tutorials/wsa-guide.html", "desc": "Run Android apps on Windows 11, install APKs, manage subsystems, and developer tips.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Subsystem for Linux (WSL)", "url": "/tutorials/wsl.html", "desc": "Guide to installing and using WSL2 on Windows.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Task Automation", "url": "/tutorials/windows-task-automation.html", "desc": "Automate Windows with Task Scheduler, scheduled tasks via PowerShell, startup scripts, and event-triggered automation.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Task Scheduler Automation", "url": "/tutorials/windows-task-scheduler.html", "desc": "Automate tasks with Task Scheduler, triggers, conditions, and PowerShell integration.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Windows Terminal Customization", "url": "/tutorials/windows-terminal.html", "desc": "Profiles, themes, oh-my-posh, keybindings, and power user workflows in Windows Terminal.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "WireGuard VPN", "url": "/tutorials/wireguard.html", "desc": "Set up a fast, modern, and audited VPN with WireGuard \u2014 the new gold standard for secure tunnels.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Wireless Networking", "url": "/tutorials/wireless-networking.html", "desc": "Wireless networks \u2014 WiFi 6/7, mesh, security, and spectrum management.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Wireshark Deep Dive", "url": "/tutorials/wireshark-deep-dive.html", "desc": "Master network packet analysis with Wireshark \u2014 capture filters, display filters, protocol dissection, and traffic forensics.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "X11 vs Wayland Display Servers", "url": "/tutorials/x11-vs-wayland.html", "desc": "Architecture comparison, migration guide, compatibility, and practical considerations for Linux users.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Zero Trust Architecture", "url": "/tutorials/zero-trust-architecture.html", "desc": "Security model: never trust, always verify \u2014 micro-segmentation, IAM, and continuous monitoring.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "Zig Systems Programming", "url": "/tutorials/zig-systems-programming.html", "desc": "Modern systems programming \u2014 manual memory management, comptime, and C interop.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "curl & wget Guide", "url": "/tutorials/curl-wget-guide.html", "desc": "Master HTTP requests from the command line \u2014 curl for APIs, wget for downloads, headers, authentication, and scripting.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "gRPC &amp; Protocol Buffers", "url": "/tutorials/grpc-basics.html", "desc": "High-performance RPC with Protobuf -- define services, generate clients/servers, streaming, and best practices.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "iOS App Development", "url": "/tutorials/ios-app-development.html", "desc": "Build iOS apps with Swift, SwiftUI, and Xcode for iPhone and iPad.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "iOS Development (Swift)", "url": "/tutorials/ios-swift.html", "desc": "iOS development with Swift \u2014 SwiftUI, UIKit, and App Store deployment.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "iOS Piracy Guide", "url": "/tutorials/ios-piracy-guide.html", "desc": "Sideload apps, music, and content on iOS \u2014 AltStore, TrollStore, and jailbreaking.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "jq Guide", "url": "/tutorials/jq-guide.html", "desc": "Parse, filter, and transform JSON from the command line using jq \u2014 queries, pipes, arrays, and practical API data extraction.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "macOS Automation (Shortcuts, Automator &amp; AppleScript)", "url": "/tutorials/macos-automation.html", "desc": "Automate repetitive tasks on macOS using Shortcuts, Automator workflows, AppleScript, and shell scripting with launchd scheduling.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "macOS Security &amp; Privacy", "url": "/tutorials/macos-security.html", "desc": "Hardening macOS security with Gatekeeper, SIP, FileVault, firewall settings, and privacy controls to protect your data.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "macOS Troubleshooting &amp; Recovery", "url": "/tutorials/macos-troubleshooting.html", "desc": "Diagnose and fix common macOS problems using Disk Utility, Safe Mode, Recovery Mode, activity monitoring, and log analysis.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "macOS for Linux &amp; Windows Switchers", "url": "/tutorials/macos-basics.html", "desc": "Everything you need to know when switching to macOS from Linux or Windows \u2014 Finder, Terminal, keyboard shortcuts, and key differences.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}, {"title": "rsync", "url": "/tutorials/rsync.html", "desc": "Fast, versatile file synchronization and remote backup tool for Unix-like systems.", "cat": "tutorials", "popularity": 70, "date": "2026-05-29"}];

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
    var tokens = query.trim().split(/\s+/).filter(Boolean);
    if (tokens.length > 1) {
      var escapedTokens = tokens.map(function(t) { return t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); });
      var re = new RegExp('(' + escapedTokens.join('|') + ')', 'gi');
      return text.replace(re, '<mark class="search-hl">$1</mark>');
    }
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

    // Tokenize query for fuzzy matching
    var queryTokens = q.split(/\s+/).filter(Boolean);

    // Filter by query — token-based: match if ANY token appears
    var results = searchIndex.filter(function(item) {
      var searchText = (item.title + ' ' + item.desc).toLowerCase();
      return queryTokens.some(function(t) {
        return searchText.indexOf(t) !== -1;
      });
    });

    // Score & sort by relevance (more token matches first, title match bonus)
    results.forEach(function(item) {
      var text = (item.title + ' ' + item.desc).toLowerCase();
      var matches = 0;
      queryTokens.forEach(function(t) { if (text.indexOf(t) !== -1) matches++; });
      item._score = matches + (queryTokens.some(function(t) { return item.title.toLowerCase().indexOf(t) !== -1; }) ? 0.5 : 0);
    });
    results.sort(function(a,b) { return (b._score || 0) - (a._score || 0); });

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
        fetch(sroot + 'search-index.json').then(function(r) { return r.json(); }).then(function(data) { searchIndex = data; window.__TL.searchIndex = data; }).catch(function() {});
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
    if (!main || !main.querySelector('nav.breadcrumb') || window.location.pathname.endsWith('/lexicon/index.html')) return;
    var path = window.location.pathname;
    if (!path.startsWith('/tutorials/') || path.endsWith('/index.html')) return;
    var text = main.textContent || '';
    var words = text.trim().split(/\s+/).length;
    var minutes = Math.max(1, Math.round(words / 200));
    var badge = document.createElement('span');
    badge.className = 'reading-time';
    badge.textContent = minutes + ' min read';
    var h1 = main.querySelector('h1');
    if (h1 && h1.parentElement) {
      // Create or find toolbar
      var toolbar = h1.parentElement.querySelector('.article-toolbar');
      if (!toolbar) {
        toolbar = document.createElement('div');
        toolbar.className = 'article-toolbar';
        h1.parentElement.insertBefore(toolbar, h1.nextSibling);
      }
      toolbar.appendChild(badge);
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
    var h1 = document.querySelector('.main-content h1');
    if (h1 && h1.parentElement) {
      var toolbar = h1.parentElement.querySelector('.article-toolbar');
      if (!toolbar) {
        toolbar = document.createElement('div');
        toolbar.className = 'article-toolbar';
        h1.parentElement.insertBefore(toolbar, h1.nextSibling);
      }
      toolbar.appendChild(badge);
    }
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

/* ===== Phase 3: Nice-to-Have Features ===== */

/* Image Lightbox */
(function(){
  try {
    var lb = document.createElement('div');
    lb.className = 'image-lightbox-overlay';
    lb.innerHTML = '<div class="image-lightbox-content"><button class="image-lightbox-close" aria-label="Close"><i class="fas fa-times"></i></button><img src="" alt=""><div class="image-lightbox-caption"></div></div>';
    document.body.appendChild(lb);
    var imgEl = lb.querySelector('img');
    var capEl = lb.querySelector('.image-lightbox-caption');
    var closeBtn = lb.querySelector('.image-lightbox-close');
    closeBtn.addEventListener('click', function(){ lb.classList.remove('open'); imgEl.src = ''; capEl.textContent = ''; });
    lb.addEventListener('click', function(e){ if (e.target === lb) { lb.classList.remove('open'); imgEl.src=''; capEl.textContent=''; } });

    document.addEventListener('click', function(e){
      var img = e.target.closest('img');
      if (!img) return;
      // Only open for images inside main content
      if (!img.closest('.main-content')) return;
      // Skip icons and small UI images
      if (img.naturalWidth && img.naturalWidth < 120) return;
      imgEl.src = img.src;
      capEl.textContent = img.getAttribute('alt') || img.getAttribute('title') || '';
      lb.classList.add('open');
    });
  } catch(e) {}
})();

/* Bookmarks & Recently Viewed */
(function(){
  try {
    var BOOKMARK_KEY = 'tl_bookmarks_v1';
    var RECENT_KEY = 'tl_recent_v1';
    function getBookmarks(){ try { return JSON.parse(localStorage.getItem(BOOKMARK_KEY) || '[]'); } catch(e){ return []; } }
    function saveBookmarks(b){ localStorage.setItem(BOOKMARK_KEY, JSON.stringify(b)); }
    function toggleBookmark(url, title){ var b = getBookmarks(); var idx = b.findIndex(function(x){ return x.url === url; }); if (idx === -1) { b.unshift({url:url, title:title}); if (b.length>100) b.pop(); } else { b.splice(idx,1); } saveBookmarks(b); updateBookmarkBtn(); }
    function updateBookmarkBtn(){ var btn = document.querySelector('.bookmark-btn'); if (!btn) return; var url = window.location.pathname; var b = getBookmarks(); var exists = b.some(function(x){ return x.url === url; }); btn.classList.toggle('active', exists); }

    // Insert bookmark button near H1 if present
    var main = document.querySelector('.main-content');
    if (main) {
      var h1 = main.querySelector('h1');
      if (h1) {
        var btn = document.createElement('button'); btn.className = 'bookmark-btn'; btn.setAttribute('aria-label','Save bookmark'); btn.innerHTML = '<i class="fas fa-bookmark"></i>';
        btn.addEventListener('click', function(){ toggleBookmark(window.location.pathname, document.title || h1.textContent || ''); });
        var toolbar = h1.parentElement.querySelector('.article-toolbar');
        if (!toolbar) {
          toolbar = document.createElement('div');
          toolbar.className = 'article-toolbar';
          h1.parentElement.insertBefore(toolbar, h1.nextSibling);
        }
        toolbar.appendChild(btn);
        updateBookmarkBtn();
      }
    }

    // Recently viewed: push to localStorage on page load
    (function trackRecent(){ try { var r = JSON.parse(localStorage.getItem(RECENT_KEY) || '[]'); var u = window.location.pathname; var t = document.title || ''; r = r.filter(function(x){ return x.url !== u; }); r.unshift({url:u, title:t, ts: Date.now()}); if (r.length>30) r.pop(); localStorage.setItem(RECENT_KEY, JSON.stringify(r)); } catch(e) {} })();

    // Render recently viewed in sidebar if present
    var side = document.querySelector('.sidebar');
    if (side) {
      var rv = document.createElement('div'); rv.className = 'recently-viewed'; rv.innerHTML = '<h4>Recently Viewed</h4><ul></ul>';
      side.appendChild(rv);
      var ul = rv.querySelector('ul');
      try {
        var items = JSON.parse(localStorage.getItem(RECENT_KEY) || '[]');
        items.slice(0,10).forEach(function(it){ var li = document.createElement('li'); li.innerHTML = '<a href="'+it.url+'">'+(it.title||it.url)+'</a>'; ul.appendChild(li); });
      } catch(e) {}
    }
  } catch(e) {}
})();

/* Auto-resume scroll position (per-page) */
(function(){
  try {
    var KEY = 'tl_scroll_v1:' + window.location.pathname;
    var last = sessionStorage.getItem(KEY);
    if (last) {
      try { window.scrollTo(0, parseInt(last,10)||0); } catch(e) {}
    }
    var timer = 0;
    window.addEventListener('scroll', function(){ if (timer) clearTimeout(timer); timer = setTimeout(function(){ sessionStorage.setItem(KEY, window.scrollY || window.pageYOffset || 0); }, 250); }, { passive: true });
  } catch(e) {}
})();

/* ===== Font Size Controls ===== */
(function(){
  try {
    var main = document.querySelector('.main-content');
    if (!main) return;

    var saved = localStorage.getItem('tl_fontsize');
    var size = parseInt(saved, 10) || 100;
    document.documentElement.style.fontSize = size + '%';

    var controls = document.createElement('div');
    controls.className = 'font-size-controls';
    controls.innerHTML = '<button class="font-size-btn" data-dir="down" aria-label="Decrease font size">A−</button><span class="font-size-label">' + size + '%</span><button class="font-size-btn" data-dir="up" aria-label="Increase font size">A+</button>';

    var h1 = main.querySelector('h1');
    if (h1 && h1.parentElement) {
      var toolbar = h1.parentElement.querySelector('.article-toolbar');
      if (!toolbar) {
        toolbar = document.createElement('div');
        toolbar.className = 'article-toolbar';
        h1.parentElement.insertBefore(toolbar, h1.nextSibling);
      }
      toolbar.appendChild(controls);
    }

    controls.addEventListener('click', function(e){
      var btn = e.target.closest('.font-size-btn');
      if (!btn) return;
      var dir = btn.getAttribute('data-dir');
      size = Math.max(70, Math.min(150, size + (dir === 'up' ? 10 : -10)));
      document.documentElement.style.fontSize = size + '%';
      localStorage.setItem('tl_fontsize', size.toString());
      controls.querySelector('.font-size-label').textContent = size + '%';
    });
  } catch(e) {}
})();

/* ===== Table Sorting ===== */
(function(){
  try {
    var tables = document.querySelectorAll('.main-content table');
    if (!tables.length) return;
    tables.forEach(function(table){
      var headers = table.querySelectorAll('th');
      headers.forEach(function(th, colIdx){
        if (!th.hasAttribute('data-sortable')) th.style.cursor = 'pointer';
        th.addEventListener('click', function(){
          var tbody = table.querySelector('tbody');
          if (!tbody) return;
          var rows = Array.from(tbody.querySelectorAll('tr'));
          var isAsc = th.classList.contains('sort-asc');
          headers.forEach(function(h){ h.classList.remove('sort-asc','sort-desc'); });
          th.classList.add(isAsc ? 'sort-desc' : 'sort-asc');
          rows.sort(function(a,b){
            var aText = (a.cells[colIdx] ? a.cells[colIdx].textContent.trim() : '');
            var bText = (b.cells[colIdx] ? b.cells[colIdx].textContent.trim() : '');
            var aNum = parseFloat(aText.replace(/[^0-9.\-]/g,''));
            var bNum = parseFloat(bText.replace(/[^0-9.\-]/g,''));
            if (!isNaN(aNum) && !isNaN(bNum)) return isAsc ? bNum - aNum : aNum - bNum;
            return isAsc ? bText.localeCompare(aText) : aText.localeCompare(bText);
          });
          rows.forEach(function(r){ tbody.appendChild(r); });
        });
      });
    });
  } catch(e) {}
})();

/* ===== Read Aloud ===== */

/* ===== Bookmarks Sidebar List ===== */
(function(){
  try {
    var side = document.querySelector('.sidebar');
    if (!side) return;

    var bmDiv = document.createElement('div');
    bmDiv.className = 'bookmarks-list';
    bmDiv.innerHTML = '<h4><i class="fas fa-bookmark"></i> Bookmarks</h4><ul></ul>';
    side.appendChild(bmDiv);

    var ul = bmDiv.querySelector('ul');

    function renderBookmarks() {
      try {
        var items = JSON.parse(localStorage.getItem('tl_bookmarks_v1') || '[]');
        ul.innerHTML = '';
        if (!items.length) {
          ul.innerHTML = '<li style="font-size:0.8rem;color:var(--text-tertiary);">No bookmarks yet</li>';
          return;
        }
        items.forEach(function(it, idx){
          var li = document.createElement('li');
          li.innerHTML = '<a href="' + it.url + '">' + (it.title || it.url) + '</a><button class="bm-remove" data-idx="' + idx + '" aria-label="Remove bookmark"><i class="fas fa-times"></i></button>';
          ul.appendChild(li);
        });
        ul.querySelectorAll('.bm-remove').forEach(function(btn){
          btn.addEventListener('click', function(e){
            e.stopPropagation();
            try {
              var b = JSON.parse(localStorage.getItem('tl_bookmarks_v1') || '[]');
              b.splice(parseInt(this.getAttribute('data-idx'),10), 1);
              localStorage.setItem('tl_bookmarks_v1', JSON.stringify(b));
              renderBookmarks();
              // Update bookmark button on current page if shown
              var pageBtn = document.querySelector('.bookmark-btn');
              if (pageBtn) {
                var url = window.location.pathname;
                var exists = b.some(function(x){ return x.url === url; });
                pageBtn.classList.toggle('active', exists);
              }
            } catch(e) {}
          });
        });
      } catch(e) {}
    }
    renderBookmarks();
  } catch(e) {}
})();

/* ===== Collapsible Sections init (CSS handles most; ensure details polyfill) ===== */
/* All styling is in CSS — details/summary are native HTML elements */
