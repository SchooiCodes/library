#!/usr/bin/env python3
"""Generate part 3 of tutorials: macOS, Mobile Dev, Game Dev, IoT, Career, Accessibility, Misc."""

from tutorial_helpers import build_page, write_page, TUTS
import os


def generate_part3():

    # =========================================================================
    # macOS (5)
    # =========================================================================
    build_page(
        'macOS for Linux & Windows Switchers',
        'macos-basics.html',
        'Everything you need to know when switching to macOS from Linux or Windows — Finder, Terminal, keyboard shortcuts, and key differences.',
        'macOS',
        'fab fa-apple',
        [
            (
                'The Finder: macOS File Manager',
                '<p>Unlike Windows Explorer or a Linux file manager like Nautilus, the Finder uses a single-window column view by default, though you can switch between icon, list, column, and gallery views with <code>View &gt; Show View Options</code> or the toolbar buttons. The Finder sidebar gives you quick access to Applications, Documents, Downloads, and mounted volumes. You can customize it by dragging folders in and out.</p><p>One major difference is that macOS does not have a “C:” drive concept. Your system files live under <code>/</code> (the root), but everyday users rarely browse there. Your home folder (<code>/Users/you</code>) is the equivalent of <code>C:\\Users\\you</code> on Windows or <code>/home/you</code> on Linux. The Applications folder is where most GUI apps are installed, similar to <code>/Applications</code> on Linux or <code>Program Files</code> on Windows.</p><p>To show hidden files in Finder, press <code>Cmd + Shift + .</code> (period). This toggles visibility of dotfiles like <code>.gitignore</code> or <code>.zshrc</code>. On older macOS versions you needed a Terminal command, but this shortcut has been available since macOS Sierra.</p>',
            ),
            (
                'The Terminal & Shell',
                '<p>macOS ships with Zsh as the default shell since Catalina (10.15). The Terminal app lives in <code>/Applications/Utilities/Terminal.app</code>. Most Linux commands you know work identically — <code>ls</code>, <code>grep</code>, <code>awk</code>, <code>sed</code>, <code>find</code>, and friends are all present because macOS is built on Darwin, a BSD-derived Unix.</p><p>Major differences from Linux include: <code>brew</code> instead of <code>apt</code>/<code>dnf</code> for package management; the filesystem layout differs slightly (<code>/Volumes</code> for mounts instead of <code>/media</code>); and many GNU utilities are BSD versions with slightly different flags. For example, <code>ls -lh</code> works on both, but <code>ls --color=auto</code> is GNU-only — on macOS just alias <code>ls</code> to <code>ls -G</code>.</p><p>To get a Linux-like experience, install Homebrew and then <code>brew install coreutils findutils gnu-sed gawk grep</code>. These install GNU versions prefixed with <code>g</code> (e.g., <code>gls</code>), or you can add them to your <code>PATH</code> without prefix. Your <code>.zshrc</code> lives at <code>~/.zshrc</code>, similar to <code>.bashrc</code> on Linux.</p><pre><code># Install Homebrew\\n/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"\\n\\n# Install GNU coreutils\\nexport PATH="/opt/homebrew/opt/coreutils/libexec/gnubin:$PATH"\\nbrew install coreutils findutils gnu-sed gawk grep</code></pre>',
            ),
            (
                'Essential Keyboard Shortcuts',
                '<p>macOS uses <code>Cmd</code> where Windows/Linux use <code>Ctrl</code> for most shortcuts. This is the single biggest adjustment for switchers. <code>Cmd+C</code> copies, <code>Cmd+V</code> pastes, <code>Cmd+Tab</code> switches apps. The <code>Ctrl</code> key is mainly used for terminal control sequences (<code>Ctrl+C</code> to interrupt, <code>Ctrl+D</code> for EOF).</p><p>Here are key shortcuts to memorize: <code>Cmd+Space</code> opens Spotlight search (like Windows key + type); <code>Cmd+Shift+3</code> takes a full screenshot, <code>Cmd+Shift+4</code> captures a selection; <code>Cmd+Q</code> quits an app entirely (not just closes the window, unlike Windows); <code>Cmd+W</code> closes the current window; <code>Cmd+Option+Esc</code> opens the Force Quit dialog (equivalent to Ctrl+Alt+Del).</p><p>Trackpad gestures are also critical. Three-finger swipe up opens Mission Control (window manager). Four-finger swipe left/right switches between full-screen apps or desktops. Pinch with thumb and three fingers opens Launchpad (app grid). These can be customized in System Settings &gt; Trackpad &gt; More Gestures.</p>',
            ),
            (
                'Installing & Managing Software',
                '<p>macOS has several software installation methods. The most common is the <code>.dmg</code> file — double-click it, drag the app icon to the Applications folder. Some apps use <code>.pkg</code> installers that walk you through a wizard. You can also download apps directly from the Mac App Store, which handles automatic updates like a package manager.</p><p>For command-line tools and developer software, Homebrew is the de facto standard. It works similarly to <code>apt</code> on Debian. You install packages with <code>brew install &lt;formula&gt;</code>, GUI apps with <code>brew install --cask &lt;cask&gt;</code>, and keep everything up to date with <code>brew update &amp;&amp; brew upgrade</code>.</p><p>You can uninstall most apps by dragging them from Applications to Trash, though this may leave preference files behind. For clean removal, tools like AppCleaner (free) scan for associated files. For Homebrew packages, use <code>brew uninstall &lt;formula&gt;</code>. Casks are removed with <code>brew uninstall --cask &lt;cask&gt;</code>.</p><pre><code># Install CLI tools\\nbrew install git wget curl htop neovim tmux\\n\\n# Install GUI applications (casks)\\nbrew install --cask visual-studio-code firefox iterm2 docker\\n\\n# Update everything\\nbrew update &amp;&amp; brew upgrade &amp;&amp; brew cleanup</code></pre>',
            ),
            (
                'Filesystem & Permissions Model',
                "<p>macOS uses a Unix permissions model (owner/group/world with read/write/execute bits) plus a modern security layer called SIP (System Integrity Protection). SIP prevents even root from modifying critical system files in <code>/System</code>, <code>/usr</code>, and <code>/bin</code>. This is different from Linux where root has unrestricted access.</p><p>The <code>/Applications</code> folder is world-readable but only writable by admin users. Each user's home folder (<code>/Users/you</code>) contains subfolders like <code>Desktop</code>, <code>Documents</code>, <code>Downloads</code>, <code>Library</code> (app data and preferences), and <code>Applications</code> (per-user apps). The <code>~/Library</code> folder is hidden in Finder by default but contains critical application support files and caches.</p><p>To manage permissions, you can use the Get Info panel in Finder or the <code>chmod</code> and <code>chown</code> commands in Terminal. macOS also has a feature called “sandboxing” where apps downloaded from the App Store run in restricted environments. For developer tools, you may need to grant permissions in System Settings &gt; Privacy &amp; Security.</p>",
            ),
        ],
        [
            ('Apple macOS User Guide', 'https://support.apple.com/guide/mac-help/welcome/mac', 'Official Apple documentation covering all macOS features.'),
            ('Homebrew Documentation', 'https://docs.brew.sh', 'Complete guide to the macOS package manager.'),
            ('macOS Keyboard Shortcuts', 'https://support.apple.com/en-us/HT201236', "Apple's official list of every keyboard shortcut."),
            ('Switching from Windows to Mac', 'https://www.apple.com/support/switch-from-windows/', "Apple's guide for Windows switchers."),
        ],
    )

    build_page(
        'Homebrew & macOS CLI Tools',
        'homebrew-guide.html',
        'Master Homebrew for package management on macOS — formulae, casks, taps, and essential CLI tools every developer needs.',
        'macOS',
        'fab fa-apple',
        [
            (
                'What Is Homebrew?',
                '<p>Homebrew is the missing package manager for macOS, inspired by Linux tools like <code>apt</code> and <code>yum</code>. It installs software that Apple didn\'t include — compilers, libraries, command-line utilities, and even GUI applications — all from your Terminal. Homebrew uses Ruby under the hood and is hosted on GitHub, making it community-driven and extensible.</p><p>Install Homebrew with a single command: <code>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</code>. On Apple Silicon Macs, it installs into <code>/opt/homebrew</code> instead of <code>/usr/local</code>. After installation, follow the “Next Steps” printed in the terminal to add Homebrew to your <code>PATH</code>.</p><p>Homebrew consists of several components: <strong>brew</strong> (the CLI tool), <strong>formulae</strong> (Ruby scripts defining how to install CLI tools), <strong>casks</strong> (extensions for GUI apps), and <strong>taps</strong> (third-party repositories with additional formulae). This modular design makes it incredibly flexible.</p>',
            ),
            (
                'Formulae: CLI Package Management',
                "<p>A <strong>formula</strong> is a Ruby script that defines how to download, compile, and install a command-line tool. Popular formulae include <code>git</code>, <code>wget</code>, <code>curl</code>, <code>python</code>, <code>node</code>, <code>imagemagick</code>, and hundreds more. You search with <code>brew search &lt;term&gt;</code> and install with <code>brew install &lt;formula&gt;</code>.</p><p>Homebrew compiles from source by default but provides precompiled “bottles” for common configurations, dramatically speeding up installs. You can see what's installed with <code>brew list</code>, check for outdated packages with <code>brew outdated</code>, and upgrade with <code>brew upgrade</code>. Cleaning old versions uses <code>brew cleanup</code>.</p><p>Dependencies are handled automatically. When you install a formula like <code>ffmpeg</code>, Homebrew also installs its dependencies like <code>x264</code>, <code>lame</code>, and <code>libvpx</code>. You can inspect a formula's dependencies with <code>brew deps &lt;formula&gt;</code> and see what depends on it with <code>brew uses &lt;formula&gt;</code>.</p><pre><code># Essential developer formulae\\nbrew install git curl wget htop neofetch tmux tree jq yq ripgrep fd\\n\\n# Languages &amp; runtimes\\nbrew install python node go rust ruby\\n\\n# Database systems\\nbrew install postgresql mysql redis mongodb</code></pre>",
            ),
            (
                'Casks: GUI Application Management',
                '<p>Casks extend Homebrew to manage macOS GUI applications. Instead of downloading DMGs manually and dragging to Applications, you can install everything from the terminal. For example, <code>brew install --cask firefox</code> downloads Firefox, mounts the DMG, copies the app, and unmounts automatically.</p><p>Popular casks include <code>visual-studio-code</code>, <code>iterm2</code>, <code>docker</code>, <code>slack</code>, <code>discord</code>, <code>spotify</code>, and <code>google-chrome</code>. Casks support versioning — install a specific version with <code>brew install --cask &lt;name&gt;@&lt;version&gt;</code> if available.</p><p>Casks have their own search and info commands: <code>brew search --cask &lt;term&gt;</code> and <code>brew info --cask &lt;name&gt;</code>. You can list all installed casks with <code>brew list --cask</code>. Some casks require a one-time password or license agreement — Homebrew handles these interactively.</p><pre><code># Developer tools\\nbrew install --cask visual-studio-code iterm2 docker postman\\n\\n# Browsers &amp; communication\\nbrew install --cask google-chrome firefox slack discord zoom\\n\\n# Creative &amp; productivity\\nbrew install --cask figma notion obs spotify</code></pre>',
            ),
            (
                'Taps: Third-Party Repositories',
                "<p>Taps are third-party Git repositories that provide additional formulae beyond the official Homebrew core. The official taps are <code>homebrew/core</code> (default, always tapped) and <code>homebrew/cask</code>. Popular community taps include <code>homebrew/cask-versions</code> (older versions of casks), <code>homebrew/cask-fonts</code> (fonts), and specialized taps like <code>snyk/tap</code> for security tools.</p><p>You add a tap with <code>brew tap &lt;user/repo&gt;</code>. For example, <code>brew tap homebrew/cask-fonts</code> then <code>brew install --cask font-fira-code</code>. Taps are just GitHub repos following a naming convention.</p><p>To manage taps, use <code>brew tap</code> to list all tapped repositories, <code>brew untap &lt;user/repo&gt;</code> to remove one, and <code>brew tap-info &lt;user/repo&gt;</code> for details. Third-party taps should be audited before use — check the formula's Ruby source with <code>brew edit &lt;formula&gt;</code> to verify it does what you expect.</p><pre><code># Add useful taps\\nbrew tap homebrew/cask-versions\\nbrew tap homebrew/cask-fonts\\nbrew tap hashicorp/tap\\n\\n# Install from a tap\\nbrew install hashicorp/tap/terraform\\nbrew install --cask font-fira-code</code></pre>",
            ),
            (
                'Essential macOS CLI Tools',
                '<p>Beyond Homebrew itself, several CLI tools dramatically improve the macOS terminal experience. <code>htop</code> provides an interactive process viewer; <code>tmux</code> enables terminal multiplexing (multiple shells in one window); <code>ripgrep</code> (<code>rg</code>) is a blazing-fast code search tool; <code>fd</code> is a user-friendly alternative to <code>find</code>; and <code>bat</code> is <code>cat</code> with syntax highlighting.</p><p>System monitoring tools: <code>htop</code> or <code>btop</code> for processes, <code>ncdu</code> for disk usage analysis, <code>lsof</code> for open files and network connections. For network debugging, <code>nmap</code>, <code>netcat</code>, <code>tcpdump</code>, and <code>wireshark</code> are all available via Homebrew.</p><p>File manipulation: <code>tree</code> displays directory structures, <code>jq</code> processes JSON from the command line, <code>yq</code> does the same for YAML, <code>fzf</code> is a fuzzy finder that integrates with your shell, and <code>entr</code> runs commands when files change.</p><pre><code># Install the toolbox\\nbrew install htop btop bat ripgrep fd fzf tree jq yq ncdu entr tmux\\n\\n# Configure fzf (run after install)\\n$(brew --prefix)/opt/fzf/install</code></pre>',
            ),
        ],
        [
            ('Homebrew Official Documentation', 'https://docs.brew.sh', 'Complete reference for Homebrew commands, formulae, and casks.'),
            ('Homebrew Formulae Browser', 'https://formulae.brew.sh', 'Search all available formulae and casks online.'),
            ('Awesome macOS Command Line', 'https://github.com/herrbischoff/awesome-macos-command-line', 'Curated list of macOS terminal commands and tools.'),
            ('Modern Unix Tools', 'https://github.com/ibraheemdev/modern-unix', 'Alternative modern CLI tools that replace classic Unix commands.'),
        ],
    )

    build_page(
        'macOS Security & Privacy',
        'macos-security.html',
        'Hardening macOS security with Gatekeeper, SIP, FileVault, firewall settings, and privacy controls to protect your data.',
        'macOS',
        'fab fa-apple',
        [
            (
                'System Integrity Protection (SIP)',
                "<p>System Integrity Protection is a security feature that restricts what the root user can do on critical system directories. Introduced in OS X El Capitan (10.11), SIP prevents modification of files in <code>/System</code>, <code>/usr</code>, <code>/bin</code>, <code>/sbin</code>, and certain system apps — even if you're running as root. This stops malware from tampering with core system components.</p><p>SIP is enabled by default and controlled by the <code>csrutil</code> tool in Recovery Mode. To check SIP status: run <code>csrutil status</code> in Terminal. You'll see either “enabled” or “disabled.” You should keep SIP enabled unless you have a very specific reason to disable it (like certain kernel extension development).</p><p>To modify SIP, reboot into Recovery Mode (Apple Silicon: hold power button; Intel: Cmd+R at startup), open Terminal from Utilities menu, and use <code>csrutil enable</code> or <code>csrutil disable</code>. You can also selectively disable components like <code>csrutil enable --without debug</code>. Always re-enable SIP after finishing your work.</p><pre><code># Check SIP status\\ncsrutil status\\n\\n# Enable SIP (in Recovery Mode Terminal)\\ncsrutil enable\\n\\n# Disable SIP (NOT recommended for daily use)\\ncsrutil disable</code></pre>",
            ),
            (
                'Gatekeeper & App Notarization',
                "<p>Gatekeeper is macOS's application execution control system. It ensures that only trusted software runs on your Mac. When you download an app from the internet, macOS checks its digital signature and notarization status. If the app is from an unidentified developer or hasn't been notarized by Apple, Gatekeeper blocks it by default.</p><p>To manually override Gatekeeper, right-click (or Ctrl-click) the app and select Open, then confirm the dialog. This adds the app to a per-application exception. You can also adjust Gatekeeper's strictness in System Settings &gt; Privacy &amp; Security. The most restrictive setting is “App Store only”; the default is “App Store and identified developers.”</p><p>Notarization is Apple's automated scanning system. When developers submit apps to Apple for notarization, Apple scans them for malware and security issues. Notarized apps receive a ticket that Gatekeeper verifies before launching. This provides a security baseline even for apps distributed outside the App Store.</p><pre><code># Check an app's code signing status\\ncodesign -dvvv /Applications/Safari.app\\n\\n# Check notarization status\\nspctl --assess --verbose /Applications/SomeApp.app\\n\\n# Remove quarantine attribute from a downloaded app\\nxattr -d com.apple.quarantine /Applications/SomeApp.app</code></pre>",
            ),
            (
                'FileVault: Full Disk Encryption',
                "<p>FileVault encrypts your entire startup disk using XTS-AES-128 encryption with a 256-bit key. When enabled, all data on your drive is encrypted at rest. Without your login password or recovery key, the data is unreadable. This is essential protection against physical theft — if someone steals your Mac, they can't access your files without the password.</p><p>Enable FileVault in System Settings &gt; Privacy &amp; Security &gt; FileVault. Click Turn On and choose how to unlock your disk: your iCloud account (can use Apple ID to reset password) or a recovery key (a long alphanumeric string you must store safely). If you forget both your password and recovery key, your data is permanently lost — there are no backdoors.</p><p>FileVault works transparently. Once you log in, the drive is decrypted and apps work normally. Sleep and screensaver keep the decryption key in memory, but shutdown fully locks the drive. Encryption happens in the background and may take several hours for large drives. You can check progress with <code>sudo fdesetup status</code> in Terminal.</p>",
            ),
            (
                'macOS Firewall & Network Security',
                '<p>macOS includes a built-in application firewall that controls incoming connections on a per-app basis. Enable it in System Settings &gt; Network &gt; Firewall. You can turn on stealth mode (no response to ICMP ping probes), block all incoming connections except essential services, or manually add apps to the allowed list.</p><p>For power users, <code>pfctl</code> (Packet Filter) provides a BSD-level firewall similar to <code>iptables</code> on Linux. You can configure complex rules in <code>/etc/pf.conf</code>. A simpler alternative is third-party tools like Little Snitch or LuLu (free and open-source) which give a GUI for monitoring and blocking both incoming and outgoing connections.</p><p>Additionally, macOS has a built-in VPN client supporting IKEv2, L2TP, and PPTP protocols. You can configure VPNs in System Settings &gt; Network. For privacy, consider using the Private Relay feature in iCloud+ which encrypts your Safari traffic and hides your IP address from websites.</p><pre><code># View firewall status\\n/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate\\n\\n# Enable stealth mode\\n/usr/libexec/ApplicationFirewall/socketfilterfw --setstealthmode on\\n\\n# List pf rules\\nsudo pfctl -s rules\\n\\n# Block all incoming except essential\\nsudo pfctl -a com.apple -s nat</code></pre>',
            ),
            (
                'Privacy Settings & App Permissions',
                '<p>macOS Catalina (10.15) introduced granular privacy controls that require apps to request permission before accessing sensitive data and hardware. These include: Camera, Microphone, Location, Photos, Calendar, Contacts, Reminders, Accessibility (control of other apps), Input Monitoring (keyboard events), Full Disk Access, and Screen Recording.</p><p>Manage all permissions in System Settings &gt; Privacy &amp; Security. Each section lists apps that have requested access, and you can toggle them on or off. macOS also logs when apps access these services — you can view the log with the Console app, filtering for “TCC” (Transparency, Consent, and Control) entries.</p><p>A common pain point for developers: Terminal apps may need Accessibility or Full Disk Access for certain features. For example, <code>tmux</code> clipboard integration might require Accessibility access. Grant these carefully — only give Full Disk Access to tools you explicitly trust, as it bypasses privacy controls entirely.</p><pre><code># View TCC (privacy) database\\nsqlite3 ~/Library/Application\\ Support/com.apple.TCC/TCC.db \\\\\\n  "SELECT * FROM access"\\n\\n# Reset privacy permissions for an app\\ntccutil reset All com.example.someapp\\n\\n# Reset all privacy permissions\\ntccutil reset All</code></pre>',
            ),
        ],
        [
            ('Apple Platform Security Guide', 'https://support.apple.com/guide/security/welcome/web', 'Official Apple security documentation covering all macOS security features.'),
            ('Disabling and Enabling SIP', 'https://developer.apple.com/documentation/security/disabling_and_enabling_system_integrity_protection', 'Apple Developer docs on SIP configuration.'),
            ('FileVault User Guide', 'https://support.apple.com/en-us/HT204837', "Apple's official FileVault setup and troubleshooting guide."),
            ('Objective-See Security Tools', 'https://objective-see.com/products.html', 'Free macOS security tools from security researcher Patrick Wardle.'),
        ],
    )

    build_page(
        'macOS Automation (Shortcuts, Automator & AppleScript)',
        'macos-automation.html',
        'Automate repetitive tasks on macOS using Shortcuts, Automator workflows, AppleScript, and shell scripting with launchd scheduling.',
        'macOS',
        'fab fa-apple',
        [
            (
                'macOS Shortcuts App',
                '<p>Introduced in macOS Monterey, the Shortcuts app brings iOS-style automation to the desktop. Shortcuts are visual workflows built from drag-and-drop actions. You can trigger them from the menu bar, keyboard shortcuts, or even automatically when certain conditions are met (time of day, app launch, network change, etc.).</p><p>Building a shortcut is straightforward: select actions from the sidebar, configure their parameters, and connect them in sequence. Actions include file operations, text manipulation, web requests, script execution, and app-specific commands. Shortcuts can also include input prompts, conditional logic (if/else), loops, and variables.</p><p>Shortcuts integrate with the Finder via Quick Actions — right-click a file and run a shortcut on it. They also appear in the Services menu, Touch Bar (on supported MacBooks), and can be shared via iCloud. More advanced users can run shell scripts within shortcuts, making them almost infinitely extensible.</p>',
            ),
            (
                'Automator: Visual Workflows',
                "<p>Automator has been part of macOS for over a decade and remains powerful for batch file processing. It uses a library of actions that you assemble into workflows. Unlike Shortcuts (which focus on quick automations), Automator excels at bulk operations on files and folders — renaming hundreds of files, converting image formats, or processing PDFs.</p><p>Automator supports five workflow types: Workflow (run within Automator), Application (standalone app), Quick Action (right-click contextual menu), Print Plugin (from print dialog), and Folder Action (triggers when files change in a watched folder). Folder Actions are particularly powerful — for example, automatically resize any image dropped into a specific folder.</p><p>To get started, open Automator from Applications, choose a workflow type, and drag actions from the library on the left. Actions flow from top to bottom, passing results via variables. You can insert AppleScript, shell scripts, and Python code within workflows for custom logic that the built-in actions don't cover.</p>",
            ),
            (
                'AppleScript & JavaScript for Automation',
                '<p>AppleScript is macOS\'s native scripting language, designed to control applications and the operating system. It uses a natural-language-like syntax that reads almost like English: <code>tell application "Finder" to get name of every file of desktop</code>. While the syntax takes getting used to, AppleScript provides deep integration with macOS apps.</p><p>JavaScript for Automation (JXA) is an alternative that lets you use JavaScript instead of AppleScript\'s unique syntax. JXA provides the same application control via the Open Scripting Architecture (OSA) but with a more familiar syntax for web developers. Both can control apps that support Apple Events.</p><p>Practical AppleScript uses include: batch-renaming files in Finder, controlling iTunes/Apple Music, automating email in Mail, processing images in Photoshop, and creating custom dialogs. AppleScripts can be saved as <code>.scpt</code> files, run from Script Editor, or exported as standalone apps that can be triggered via keyboard shortcuts.</p><pre><code>-- AppleScript: Rename all files on desktop\\nset desktopPath to POSIX path of (path to desktop)\\ntell application "System Events"\\n    set fileList to every file of folder desktopPath\\n    repeat with f in fileList\\n        set {oldName, ext} to {name, name extension} of f\\n        if ext is not "" then\\n            set name of f to "prefix_" &amp; oldName\\n        end if\\n    end repeat\\nend tell</code></pre>',
            ),
            (
                'Shell Scripting & launchd Scheduling',
                '<p>For developers, shell scripts remain the most flexible automation tool. macOS is Unix under the hood, so any bash/zsh script runs natively. You can use <code>cron</code>-style scheduling via <code>launchd</code> — macOS\'s service management framework. Launchd replaces both <code>init</code> and <code>cron</code>, using XML <code>.plist</code> files for configuration.</p><p>User-level launchd agents run when you\'re logged in, stored in <code>~/Library/LaunchAgents/</code>. System-level daemons go in <code>/Library/LaunchDaemons/</code> or <code>/System/Library/LaunchDaemons/</code> (avoid modifying system ones). You load/unload agents with <code>launchctl load &lt;plist&gt;</code> and <code>launchctl unload &lt;plist&gt;</code>.</p><p>A typical launchd plist includes: <code>Label</code> (unique identifier), <code>ProgramArguments</code> (command to run), <code>StartCalendarInterval</code> (cron-like schedule), and <code>StandardOutPath</code>/<code>StandardErrorPath</code> (log files). You can also use <code>WatchPaths</code> to trigger scripts when files change, or <code>StartOnMount</code> to run when a volume is mounted.</p><pre><code>&lt;?xml version="1.0" encoding="UTF-8"?&gt;\\n&lt;!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"\\n "http://www.apple.com/DTDs/PropertyList-1.0.dtd"&gt;\\n&lt;plist version="1.0"&gt;\\n&lt;dict&gt;\\n    &lt;key&gt;Label&lt;/key&gt;\\n    &lt;string&gt;com.user.dailybackup&lt;/string&gt;\\n    &lt;key&gt;ProgramArguments&lt;/key&gt;\\n    &lt;array&gt;\\n        &lt;string&gt;/usr/local/bin/backup-script.sh&lt;/string&gt;\\n    &lt;/array&gt;\\n    &lt;key&gt;StartCalendarInterval&lt;/key&gt;\\n    &lt;dict&gt;\\n        &lt;key&gt;Hour&lt;/key&gt;\\n        &lt;integer&gt;3&lt;/integer&gt;\\n        &lt;key&gt;Minute&lt;/key&gt;\\n        &lt;integer&gt;0&lt;/integer&gt;\\n    &lt;/dict&gt;\\n&lt;/dict&gt;\\n&lt;/plist&gt;</code></pre>',
            ),
        ],
        [
            ('macOS Shortcuts User Guide', 'https://support.apple.com/guide/shortcuts-mac/welcome', "Apple's official guide to the Shortcuts app on macOS."),
            ('AppleScript Language Guide', 'https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html', 'Comprehensive AppleScript reference from Apple.'),
            ('launchd Wikipedia', 'https://en.wikipedia.org/wiki/Launchd', "Overview of macOS's launchd service management framework."),
            ('MacScripter', 'https://www.macscripter.net', 'Community forum for AppleScript and macOS automation discussions.'),
        ],
    )

    build_page(
        'macOS Troubleshooting & Recovery',
        'macos-troubleshooting.html',
        'Diagnose and fix common macOS problems using Disk Utility, Safe Mode, Recovery Mode, activity monitoring, and log analysis.',
        'macOS',
        'fab fa-apple',
        [
            (
                'macOS Recovery Mode',
                "<p>Recovery Mode is your lifeline when macOS won't boot or behaves badly. On Apple Silicon Macs, press and hold the power button until “Loading startup options” appears, then click Options &gt; Continue. On Intel Macs, restart and hold <code>Cmd+R</code> (or <code>Option+Cmd+R</code> for internet recovery, which downloads the latest compatible macOS).</p><p>From Recovery Mode, you can: restore from a Time Machine backup, reinstall macOS without losing data, use Disk Utility to repair or erase disks, access Terminal for advanced troubleshooting, and use Startup Security Utility to manage firmware settings (Intel-only).</p><p>Internet Recovery (Option+Cmd+R) is useful when the built-in recovery partition is damaged. It downloads macOS over WiFi and boots into recovery tools. Note that Apple Silicon Macs always use internet recovery when no local recovery is available. If you've never set up your Mac, you'll also see the Setup Assistant in recovery.</p>",
            ),
            (
                'Safe Mode & Diagnostic Boots',
                '<p>Safe Mode (also called Safe Boot) loads only essential system extensions and kernel modules, disabling startup items, login items, and third-party kernel extensions. This helps isolate software problems. On Apple Silicon: shut down, hold power button, select your startup disk, hold Shift, then click “Continue in Safe Mode.” On Intel: hold <code>Shift</code> during boot.</p><p>In Safe Mode, macOS also forces a directory check on the startup volume and clears certain system caches (<code>/Library/Caches</code>). If a problem disappears in Safe Mode, the culprit is likely a startup item, kernel extension, or third-party service. Restart normally and methodically disable login items (System Settings &gt; General &gt; Login Items).</p><p>Apple Diagnostics helps identify hardware issues. On Intel Macs, restart and hold <code>D</code>. Apple Silicon: press and hold power button, press <code>Cmd+D</code> after startup options appear. This runs hardware tests on memory, fans, storage, and connectivity. Different Mac models show different reference codes for failures.</p>',
            ),
            (
                'Disk Utility & File System Repair',
                "<p>Disk Utility is macOS's built-in disk management and repair tool. First Aid checks and repairs the filesystem structure, fixing directory corruption, invalid permissions, and catalog issues. It works on both the main startup volume and external drives. Run First Aid from the Disk Utility app in Applications/Utilities or from Recovery Mode.</p><p>For APFS (Apple File System) volumes — the default since macOS High Sierra — First Aid runs <code>fsck_apfs</code> internally. It checks the container structure, volume superblock, object maps, and snapshots. Run it periodically if you experience kernel panics, weird file behavior, or slow performance that isn't related to hardware.</p><p>Using Disk Utility from Recovery Mode is crucial when the main OS can't boot. Select your startup disk (usually “Macintosh HD” or the actual disk below “Untitled”) and click First Aid. You may need to run it on the container itself — look for “Apple APFS Media” or the physical disk. Severe corruption may require reformatting and restoring from a backup.</p><pre><code># Run fsck from Terminal (force check on next reboot)\\nsudo touch /forcefsck\\nsudo reboot\\n\\n# Check APFS volume status\\ndiskutil apfs list\\n\\n# Run First Aid from Terminal\\ndiskutil verifyVolume /\\ndiskutil repairVolume /</code></pre>",
            ),
            (
                'Activity Monitor & Log Analysis',
                '<p>Activity Monitor (in Applications/Utilities) is the macOS equivalent of Task Manager. The CPU tab shows processes consuming processor time — watch for runaway processes with high %CPU. The Memory tab shows memory pressure (green/yellow/red) and how much is being swapped. Disk and Network tabs show I/O activity per process.</p><p>The Energy tab identifies apps draining battery. Click the Energy Impact column to sort. In the View menu, enable “All Processes” to see system daemons, not just your user apps. The gear icon (toolbar) offers “Run Spindump” — captures a sample of a hung process for developer debugging.</p><p>For deeper log analysis, use the Console app (also in Utilities). It aggregates logs from <code>os_log</code>, system logs, and app crash reports. Create custom searches for terms like “error,” “panic,” or a specific process name. The <code>log</code> command in Terminal is even more powerful: <code>log show --predicate \'eventMessage contains "error"\' --info --last 1h</code> shows all error messages from the last hour.</p><pre><code># Show recent kernel panics\\nlog show --predicate \'eventMessage contains "panic"\' --last 2d | grep -i panic\\n\\n# Stream live logs for a specific process\\nlog stream --predicate \'process == "Finder"\'\\n\\n# Export system diagnostics\\nsudo sysdiagnose\\n\\n# Check disk SMART status\\nsmartctl -a disk0  # requires smartmontools via Homebrew</code></pre>',
            ),
        ],
        [
            ('macOS Recovery Guide', 'https://support.apple.com/en-us/HT204904', 'Official Apple guide to macOS Recovery features.'),
            ('Safe Mode User Guide', 'https://support.apple.com/en-us/HT201262', 'How to start your Mac in Safe Mode.'),
            ('Disk Utility First Aid', 'https://support.apple.com/en-us/HT210898', 'Using Disk Utility to repair disk issues.'),
            ('Activity Monitor User Guide', 'https://support.apple.com/guide/activity-monitor/welcome/mac', "Apple's official Activity Monitor guide."),
        ],
    )


    # =========================================================================
    # Mobile Dev (5)
    # =========================================================================
    build_page(
        'React Native Mobile Development',
        'react-native-basics.html',
        'Build cross-platform mobile apps with React Native — core components, navigation, native modules, and performance optimization.',
        'Mobile Dev',
        'fas fa-mobile-alt',
        [
            (
                'Core Components & JSX',
                "<p>React Native uses React's component model to render native UI elements. Instead of <code>&lt;div&gt;</code> and <code>&lt;span&gt;</code>, you use <code>&lt;View&gt;</code> (equivalent to <code>&lt;div&gt;</code>), <code>&lt;Text&gt;</code> (text display), <code>&lt;Image&gt;</code>, <code>&lt;ScrollView&gt;</code>, and <code>&lt;FlatList&gt;</code> (performant scrollable lists). Components are written in JSX and styled with JavaScript objects using a subset of CSS properties.</p><p>Styling uses Flexbox exclusively for layout. The default <code>flexDirection</code> is <code>column</code> (unlike web CSS which defaults to <code>row</code>). All dimensions are unitless — <code>fontSize: 16</code> instead of <code>16px</code>. Positions use <code>absolute</code> or <code>relative</code> as in CSS. There is no cascade or inheritance; you style each element explicitly with <code>StyleSheet.create()</code>.</p><p>Platform-specific components can be handled with <code>.ios.js</code> and <code>.android.js</code> extensions. When you import <code>MyComponent</code>, React Native automatically picks the platform-appropriate file. The <code>Platform</code> module (<code>Platform.OS === 'ios'</code>) lets you write conditional code in shared files.</p><pre><code>import { View, Text, StyleSheet } from 'react-native';\\n\\nconst Greeting = ({ name }) =&gt; (\\n  &lt;View style={styles.container}&gt;\\n    &lt;Text style={styles.text}&gt;Hello, {name}!&lt;/Text&gt;\\n  &lt;/View&gt;\\n);\\n\\nconst styles = StyleSheet.create({\\n  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },\\n  text: { fontSize: 20, fontWeight: '600', color: '#333' },\\n});</code></pre>",
            ),
            (
                'Navigation with React Navigation',
                '<p>React Navigation is the de facto standard for navigation in React Native apps. It provides stack navigators (push/pop screens), tab navigators (bottom or top tabs), and drawer navigators (slide-out menu). Install it with <code>npm install @react-navigation/native @react-navigation/stack</code> and its dependencies including <code>react-native-screens</code> and <code>react-native-safe-area-context</code>.</p><p>A stack navigator manages a stack of screens. Calling <code>navigation.navigate(\'Profile\')</code> pushes the Profile screen onto the stack; the header back button pops it. Parameters are passed as the second argument: <code>navigation.navigate(\'Profile\', { userId: 42 })</code>. The receiving screen accesses them via <code>route.params</code>.</p><p>Tab navigators work well for top-level navigation between different sections of your app (Home, Search, Profile). Combine them with stack navigators inside each tab — a common pattern called “nested navigation.” Deep linking is supported out of the box, making it possible to open specific screens from push notifications or URLs.</p><pre><code>import { NavigationContainer } from \'@react-navigation/native\';\\nimport { createStackNavigator } from \'@react-navigation/stack\';\\n\\nconst Stack = createStackNavigator();\\n\\nfunction App() {\\n  return (\\n    &lt;NavigationContainer&gt;\\n      &lt;Stack.Navigator&gt;\\n        &lt;Stack.Screen name="Home" component={HomeScreen} /&gt;\\n        &lt;Stack.Screen name="Profile" component={ProfileScreen} /&gt;\\n      &lt;/Stack.Navigator&gt;\\n    &lt;/NavigationContainer&gt;\\n  );\\n}</code></pre>',
            ),
            (
                'Native Modules & Bridging',
                "<p>When you need platform-specific functionality not covered by React Native's core APIs, you write native modules. For iOS, this means Objective-C or Swift files; for Android, Java or Kotlin files. These modules expose functionality to JavaScript through React Native's bridge, which serializes messages between JS and native threads.</p><p>Creating a native module involves: (1) writing the native code that implements the feature, (2) registering the module with the React Native runtime, and (3) importing and calling the module from JavaScript. The bridge communicates asynchronously via a batched JSON queue, so native calls should be treated as asynchronous operations.</p><p>New Architecture (Fabric renderer + TurboModules) is gradually replacing the legacy bridge. TurboModules allow synchronous JavaScript-to-native calls for simple getters, lazy loading (modules are initialized on demand), and type-safe interfaces defined in JavaScript. This is the future of React Native native modules and improves startup performance.</p>",
            ),
            (
                'State Management',
                '<p>React Native supports all React state management approaches. Local component state uses <code>useState</code> and <code>useReducer</code>. For global state across the app, Context API with <code>useContext</code> works well for medium-sized apps. For larger apps, consider Redux Toolkit or Zustand, which provide predictable state containers with devtools and middleware support.</p><p>Async data from APIs is typically managed with custom hooks. The <code>useEffect</code> hook triggers data fetching on mount, while <code>useState</code> holds the loading/error/data state. Libraries like React Query (TanStack Query) or SWR add caching, background refetching, and optimistic updates, reducing boilerplate significantly.</p><p>Persistent state (user preferences, auth tokens) should use <code>AsyncStorage</code> or, for more complex needs, <code>react-native-mmkv</code> (fast key-value storage) or <code>WatermelonDB</code> (SQLite-based reactive database). For real-time data, consider Firebase Realtime Database, Supabase with subscriptions, or a WebSocket connection wrapped in a custom hook.</p>',
            ),
            (
                'Performance Optimization',
                '<p>React Native performance issues typically stem from unnecessary re-renders, slow list scrolling, or bridge congestion. For lists, always use <code>FlatList</code> or <code>SectionList</code> instead of <code>ScrollView</code> with <code>map()</code> — virtualized lists only render visible items. Provide a stable <code>key</code> prop and consider <code>getItemLayout</code> for fixed-size items.</p><p>Memoize components with <code>React.memo</code> and expensive calculations with <code>useMemo</code>. Use <code>useCallback</code> for callback props to prevent child re-renders. The React DevTools profiler helps identify wasted renders. For images, use <code>react-native-fast-image</code> which caches images to disk and loads them faster than the built-in <code>Image</code> component.</p><p>JavaScript thread performance: move heavy computation to native modules or use <code>InteractionManager.runAfterInteractions()</code> to defer non-urgent work until after animations complete. For Hermes (the JS engine recommended for production), enable it in <code>android/app/build.gradle</code> and <code>ios/Podfile</code> for faster startup and lower memory usage.</p>',
            ),
        ],
        [
            ('React Native Official Docs', 'https://reactnative.dev/docs/getting-started', 'Comprehensive documentation maintained by Meta.'),
            ('React Navigation Docs', 'https://reactnavigation.org/docs/getting-started', 'Official guide for React Navigation.'),
            ('React Native Performance', 'https://reactnative.dev/docs/performance', 'Official performance optimization guide.'),
            ('Awesome React Native', 'https://github.com/jondot/awesome-react-native', 'Curated list of libraries and resources.'),
        ],
    )

    build_page(
        'Flutter Advanced Patterns',
        'flutter-deep-dive.html',
        'Deep dive into advanced Flutter development — state management strategies, custom animations, platform channels, and testing patterns.',
        'Mobile Dev',
        'fas fa-mobile-alt',
        [
            (
                'State Management Approaches',
                "<p>Flutter offers multiple state management solutions, each suited to different app complexities. The simplest approach is <code>setState</code> within <code>StatefulWidget</code> — fine for isolated local state but doesn't scale. For medium apps, <code>InheritedWidget</code> + <code>ChangeNotifier</code> with <code>Provider</code> or <code>Riverpod</code> provides clean dependency injection and reactive updates without boilerplate.</p><p>For large applications, the BLoC (Business Logic Component) pattern separates business logic from UI using Streams and Sinks. Events flow into the BLoC, which processes them and emits new states. Alternatively, <code>flutter_bloc</code> provides a Cubit variant (simpler, method-based instead of event classes). Redux-style stores are available via <code>flutter_redux</code>.</p><p>Riverpod has gained popularity as an improvement over Provider — it's compile-safe (no runtime errors from missing providers), supports autodispose, and doesn't depend on Flutter's widget tree. Choose based on your team's familiarity and app complexity. For most new projects, Riverpod or BLoC are the recommended starting points.</p>",
            ),
            (
                'Custom Animations & Transforms',
                "<p>Flutter's animation system is built around <code>AnimationController</code>, a class that generates values from 0.0 to 1.0 over a specified duration. You drive animations with <code>Ticker</code> (Flutter's frame callback) and apply values via <code>Animation</code> objects. <code>CurvedAnimation</code> wraps another animation with easing curves like <code>Curves.easeInOut</code> or <code>Curves.bounceOut</code>.</p><p>For complex animations, use <code>AnimatedBuilder</code> or <code>AnimatedWidget</code> to rebuild specific parts of the widget tree when the animation ticks. Staggered animations chain multiple controllers. The <code>Hero</code> widget creates shared element transitions between routes. For explicit particle effects or complex 2D transforms, consider the <code>flutter_animate</code> package or <code>Rive</code> for runtime-interactive vector animations.</p><p>Performance tip: animations run on Flutter's raster thread (separate from the UI thread). Avoid heavy build methods during animation frames. Use <code>RepaintBoundary</code> to isolate repainting. For 60fps animations, ensure your build methods complete within 16ms. Profile with the Flutter DevTools timeline view to identify jank.</p><pre><code>class FadeInWidget extends StatefulWidget {\\n  final Widget child;\\n  const FadeInWidget({required this.child});\\n\\n  @override\\n  State createState() =&gt; _FadeInWidgetState();\\n}\\n\\nclass _FadeInWidgetState extends State\\n    with SingleTickerProviderStateMixin {\\n  late AnimationController _controller;\\n  late Animation _animation;\\n\\n  @override\\n  void initState() {\\n    super.initState();\\n    _controller = AnimationController(\\n      vsync: this, duration: Duration(milliseconds: 500),\\n    );\\n    _animation = CurvedAnimation(parent: _controller, curve: Curves.easeIn);\\n    _controller.forward();\\n  }\\n\\n  @override\\n  Widget build(BuildContext context) =&gt; FadeTransition(\\n    opacity: _animation, child: widget.child,\\n  );\\n\\n  @override\\n  void dispose() { _controller.dispose(); super.dispose(); }\\n}</code></pre>",
            ),
            (
                'Platform Channels',
                "<p>Platform channels enable communication between Dart and native (Java/Kotlin on Android, Swift/Objective-C on iOS) code. The <code>MethodChannel</code> class sends method calls and receives results asynchronously. Basic types are automatically serialized/deserialized — <code>String</code>, <code>int</code>, <code>bool</code>, <code>List</code>, <code>Map</code> — in a format called the StandardMessageCodec.</p><p>To create a platform channel: (1) in Dart, instantiate <code>MethodChannel('com.example/channel')</code> and call <code>invokeMethod('methodName', args)</code>. (2) On the native side, register a handler for the same channel name. On Android, implement <code>MethodChannel.MethodCallHandler</code> in your MainActivity. On iOS, use <code>FlutterMethodChannel</code> in AppDelegate or your FlutterViewController.</p><p>For event streams from native code (sensor data, location updates), use <code>EventChannel</code> instead of <code>MethodChannel</code>. This allows the native side to push multiple values over time. Consider <code>Pigeon</code>, a code-generation tool that creates type-safe channel interfaces from a shared definition file — reducing runtime errors from mismatched channel names or serialization.</p><pre><code>// Dart side\\nstatic const platform = MethodChannel('com.example/battery');\\n\\nFuture getBatteryLevel() async {\\n  try {\\n    final result = await platform.invokeMethod('getBatteryLevel');\\n    return 'Battery: $result%';\\n  } on PlatformException catch (e) {\\n    return 'Failed: ${e.message}';\\n  }\\n}</code></pre>",
            ),
            (
                'Testing: Unit, Widget & Integration',
                "<p>Flutter's testing framework is three-tiered. Unit tests (<code>flutter test</code>) run synchronously in the Dart VM without a device. Test pure Dart classes, repositories, BLoCs/Cubits, and utility functions. Use the <code>test</code> and <code>mockito</code> packages. Mock dependencies like HTTP clients or database adapters.</p><p>Widget tests (<code>flutter test</code> same command) render individual widgets in a test environment. Use <code>WidgetTester</code> to pump widgets, tap buttons, enter text, and verify state. <code>find.text('Submit')</code> locates widgets; <code>expect(find.byType(FloatingActionButton), findsOneWidget)</code> asserts widget presence. Wrap widgets with needed providers and <code>MaterialApp</code> for proper context.</p><p>Integration tests (<code>flutter test integration_test/</code>) run on a real device or emulator, testing full user flows. The <code>integration_test</code> package provides <code>IntegrationTestWidgetsFlutterBinding</code>. Use the same finder API as widget tests. CI/CD pipelines typically run unit + widget tests on each commit and integration tests on key flows before release.</p><pre><code>// Widget test example\\nvoid main() {\\n  testWidgets('Counter increments when tapped', (tester) async {\\n    await tester.pumpWidget(const MyApp());\\n    expect(find.text('0'), findsOneWidget);\\n\\n    await tester.tap(find.byIcon(Icons.add));\\n    await tester.pump();\\n\\n    expect(find.text('1'), findsOneWidget);\\n  });\\n}</code></pre>",
            ),
        ],
        [
            ('Flutter Official Documentation', 'https://docs.flutter.dev', 'Comprehensive Flutter guides and API reference.'),
            ('Riverpod Package', 'https://pub.dev/packages/riverpod', 'Compile-safe state management for Flutter.'),
            ('Flutter Animation Tutorial', 'https://docs.flutter.dev/ui/animations', 'Official animations guide with examples.'),
            ('Pigeon Platform Channels', 'https://pub.dev/packages/pigeon', 'Type-safe platform channel code generation.'),
        ],
    )

    build_page(
        'Android Studio Setup & Workflow',
        'android-studio-guide.html',
        'Set up Android Studio for productive Android development — emulator configuration, Gradle build system, debugging, and profiling.',
        'Mobile Dev',
        'fas fa-mobile-alt',
        [
            (
                'Installing & Configuring Android Studio',
                '<p>Android Studio is the official IDE for Android development, built on IntelliJ IDEA. Download it from developer.android.com/studio. The installer includes the Android SDK, emulator system images, and build tools. On macOS, install via Homebrew cask: <code>brew install --cask android-studio</code>. On Windows and Linux, use the installer from the website.</p><p>During first launch, the Setup Wizard guides you through SDK component installation. Essential components: Android SDK Platform (for your target API level), Android SDK Build-Tools, Android Emulator, and Intel HAXM (hardware acceleration for the emulator on Intel Macs). On Apple Silicon, Android Studio uses the ARM emulator natively.</p><p>Configure the IDE to your preferences: set the theme (Darcula or Light), keymap (macOS preset for Mac users, Eclipse/VS Code presets available), and enable auto-import for Kotlin/Java. Disable unnecessary plugins to speed up startup. Install the Kotlin plugin if not bundled. Set your JDK path to the embedded JetBrains Runtime or a manually installed JDK 17+.</p>',
            ),
            (
                'Emulator Configuration & AVD Manager',
                '<p>The Android Virtual Device (AVD) Manager creates emulator instances for testing. Click the device icon in the toolbar or go to Tools &gt; AVD Manager. Create a virtual device selecting a hardware profile (Pixel 6, Pixel Tablet, etc.) and a system image. Choose API 34 or the latest stable for new development, but also create an older API level device for backward compatibility testing.</p><p>Performance tuning is crucial. Enable hardware acceleration: on Intel, use HAXM; on Apple Silicon, the ARM emulator runs natively with excellent performance. Allocate at least 2GB RAM (4GB preferred). Enable “Store a snapshot for faster startup” — this saves the device state, reducing cold boot time to seconds. Use the “Resizable” device definition to test multiple screen sizes with one AVD.</p><p>Extended controls (the “...” button in the emulator toolbar) provide powerful testing features: simulate phone calls and SMS, battery levels, GPS locations (useful for location-based app testing), network speed/latency profiles, fingerprint enrollment for biometric testing, and camera virtual scene environments.</p>',
            ),
            (
                'Gradle Build System',
                '<p>Gradle is Android\'s build system, configured with Kotlin DSL (preferred) or Groovy. The <code>build.gradle.kts</code> files come in two levels: project-level (top-level <code>build.gradle.kts</code>) and module-level (<code>app/build.gradle.kts</code>). The project file configures repositories and plugin versions; the module file defines the SDK versions, dependencies, build types, and product flavors.</p><p>Key configurations in <code>app/build.gradle.kts</code>: <code>compileSdk</code> (latest API features available), <code>minSdk</code> (minimum Android version you support), <code>targetSdk</code> (optimization target). <code>buildTypes</code> define debug and release builds — release builds need ProGuard/R8 for code shrinking. <code>productFlavors</code> create different variants (free vs paid, demo vs full) with separate app IDs and resources.</p><p>Dependencies are declared in the <code>dependencies</code> block. Use version catalogs (<code>libs.versions.toml</code>) for centralized version management. Gradle syncs automatically when you change build files. For slow syncs, enable Gradle\'s build cache, use the <code>--parallel</code> flag, and keep Gradle and AGP (Android Gradle Plugin) up to date to leverage incremental builds.</p><pre><code>// app/build.gradle.kts\\nplugins {\\n    id(\'com.android.application\')\\n    id(\'org.jetbrains.kotlin.android\')\\n}\\n\\nandroid {\\n    namespace = "com.example.myapp"\\n    compileSdk = 34\\n    defaultConfig {\\n        applicationId = "com.example.myapp"\\n        minSdk = 26\\n        targetSdk = 34\\n        versionCode = 1\\n        versionName = "1.0.0"\\n    }\\n    buildTypes {\\n        release {\\n            isMinifyEnabled = true\\n            proguardFiles(getDefaultProguardFile(\'proguard-android-optimize.txt\'))\\n        }\\n    }\\n}</code></pre>',
            ),
            (
                'Debugging & Profiling Tools',
                '<p>Android Studio\'s debugger supports standard breakpoints, conditional breakpoints, expression evaluation, and method breakpoints. The <code>Logcat</code> tool window shows system logs filtered by app PID, log level (Verbose through Error), and custom search strings. Mark important log sections with <code>Log.d("TAG", "message")</code> in Kotlin or Java.</p><p>The Android Profiler (View &gt; Tool Windows &gt; Profiler) shows real-time CPU, memory, network, and energy usage. The Memory Profiler captures heap dumps, detects memory leaks, and shows allocation tracking. The Network Profiler captures HTTP traffic timing and payload sizes. The Energy Profiler shows system wake locks and location requests draining battery.</p><p>For UI debugging, the Layout Inspector (View &gt; Tool Windows &gt; Layout Inspector) shows the full view hierarchy, property values, and 3D rendering of your activity\'s layout. The Database Inspector lets you query and modify SQLite/Room databases in real-time. The Background Task Inspector traces WorkManager tasks. Use these tools during development, not just when bugs appear.</p>',
            ),
        ],
        [
            ('Android Studio User Guide', 'https://developer.android.com/studio/intro', 'Official Android Studio documentation from Google.'),
            ('Gradle Plugin User Guide', 'https://developer.android.com/build', 'Android Gradle plugin configuration reference.'),
            ('Android Emulator Guide', 'https://developer.android.com/studio/run/emulator', 'Complete emulator setup and usage guide.'),
            ('Debugging with Android Studio', 'https://developer.android.com/studio/debug', 'Official debugging and profiling documentation.'),
        ],
    )

    build_page(
        'SwiftUI for iOS Development',
        'swiftui-basics.html',
        'Learn SwiftUI for building declarative iOS interfaces — state management, data flow, navigation patterns, and best practices.',
        'Mobile Dev',
        'fas fa-mobile-alt',
        [
            (
                'Declarative UI with SwiftUI',
                '<p>SwiftUI uses a declarative syntax where you describe what the UI should do, not how to achieve it. A view is a struct conforming to the <code>View</code> protocol with a computed <code>body</code> property. Combine views using <code>VStack</code>, <code>HStack</code>, and <code>ZStack</code> for vertical, horizontal, and overlapping layouts. Spacers, dividers, and padding adjust spacing.</p><p>Built-in controls include <code>Text</code>, <code>Image</code>, <code>Button</code>, <code>TextField</code>, <code>Toggle</code>, <code>Slider</code>, <code>Picker</code>, <code>List</code>, and <code>Form</code>. Each control has modifier methods that return modified views — <code>.font(.title)</code>, <code>.foregroundColor(.blue)</code>, <code>.padding()</code>, <code>.cornerRadius(8)</code>. The order of modifiers matters; each one wraps the previous view.</p><p>SwiftUI automatically handles dark mode, accessibility (Dynamic Type, VoiceOver), and right-to-left languages. PreviewProvider structs in your code display live previews in Xcode\'s canvas.</p><pre><code>import SwiftUI\\n\\nstruct ContentView: View {\\n    @State private var count = 0\\n\\n    var body: some View {\\n        VStack(spacing: 20) {\\n            Text("Count: \\\\\\(count)")\\n                .font(.largeTitle)\\n            Button("Increment") {\\n                count += 1\\n            }\\n            .buttonStyle(.borderedProminent)\\n        }\\n        .padding()\\n    }\\n}</code></pre>',
            ),
            (
                'State & Data Flow',
                '<p>SwiftUI provides property wrappers to manage data flow. <code>@State</code> manages local mutable state within a single view — the view re-renders when the value changes. <code>@Binding</code> creates a two-way connection to state owned by a parent view, allowing child views to mutate parent state. <code>@StateObject</code> initializes and owns a reference-type observable object.</p><p><code>@ObservedObject</code> references an observable object owned elsewhere but still subscribes to changes. <code>@EnvironmentObject</code> reads an observable object from the environment (injected higher in the view hierarchy), avoiding manual passing through initializers. <code>@AppStorage</code> reads/writes UserDefaults, ideal for user preferences.</p><p>For value types, use <code>@State</code> (simple local) or <code>@Bindable</code> (iOS 17+) for two-way bindings to observable classes. For reference types, create a class conforming to <code>ObservableObject</code> with <code>@Published</code> properties. The <code>Observable</code> macro (iOS 17+) simplifies this — just mark the class <code>@Observable</code> and use <code>@Environment</code> or <code>@State</code> directly.</p>',
            ),
            (
                'Navigation & Routing',
                '<p><code>NavigationStack</code> (iOS 16+) manages a stack of views. Push new views with <code>NavigationLink(value:label:)</code> where the value is a hashable type. Use <code>.navigationDestination(for:destination:)</code> to map value types to destination views. This type-safe approach replaces the older <code>NavigationLink</code> with string-based destinations.</p><p>Tab bars use <code>TabView</code> with <code>.tabItem</code> modifier on each child. For split-view layouts on iPad, use <code>NavigationSplitView</code> with two or three columns — sidebar, content, and detail columns. Sheets (modal presentations) use the <code>.sheet(isPresented:dismiss:content:)</code> modifier; full-screen covers use <code>.fullScreenCover</code>.</p><p>Programmatic navigation works with <code>NavigationPath</code> — a type-erased path you can push, pop, and manipulate. Pass it to <code>NavigationStack(path:)</code>. Deep linking from push notifications or URLs can append to the path. For complex routing, consider a coordinator pattern using <code>NavigationPath</code> with an enum of route destinations.</p><pre><code>struct ContentView: View {\\n    @State private var path = NavigationPath()\\n\\n    var body: some View {\\n        NavigationStack(path: $path) {\\n            List(1..&lt;10) { i in\\n                NavigationLink(value: i) {\\n                    Text("Item \\\\\\(i)")\\n                }\\n            }\\n            .navigationDestination(for: Int.self) { i in\\n                DetailView(id: i)\\n            }\\n        }\\n    }\\n}</code></pre>',
            ),
            (
                'Layout & Composition Best Practices',
                '<p>Break your UI into small, reusable views. Each view should do one thing. Extract repeated modifiers into a custom <code>ViewModifier</code> or a computed property on <code>View</code> extension. Use <code>@ViewBuilder</code> for functions that return multiple child views. The <code>Group</code> view groups children without layout impact, useful for conditional content.</p><p>Performance: use <code>LazyVStack</code> and <code>LazyHStack</code> inside <code>ScrollView</code> for large lists. For even better performance with thousands of rows, use <code>List</code> which reuses cells like <code>UITableView</code>. Mark views with <code>.equatable()</code> or conform to <code>EquatableView</code> to diff and skip redundant redraws. Avoid putting heavy computation in <code>body</code> — offload to view models.</p><p>Adaptive layouts: use <code>GeometryReader</code> sparingly (it expands to fill and disables some optimizations). Prefer <code>Layout</code> protocols (iOS 16+) for custom layout containers with spacing and sizing logic. Use <code>@ScaledMetric</code> for sizes that respect Dynamic Type. Test on multiple device sizes in the Xcode preview canvas with different preview layouts.</p>',
            ),
        ],
        [
            ('SwiftUI Official Documentation', 'https://developer.apple.com/documentation/swiftui', "Apple's complete SwiftUI API reference."),
            ('SwiftUI Tutorials by Apple', 'https://developer.apple.com/tutorials/swiftui', 'Official getting-started tutorials from Apple.'),
            ('Hacking with SwiftUI', 'https://www.hackingwithswift.com/quick-start/swiftui', 'Excellent free SwiftUI tutorials by Paul Hudson.'),
            ('SwiftUI Lab', 'https://swiftui-lab.com', 'Advanced SwiftUI patterns and deep dives by Javier.'),
        ],
    )

    build_page(
        'Mobile App Store Deployment',
        'mobile-app-deployment.html',
        'End-to-end mobile app deployment — App Store Connect, Google Play Console, code signing, CI/CD pipelines, and release management.',
        'Mobile Dev',
        'fas fa-mobile-alt',
        [
            (
                'Apple App Store Connect',
                "<p>App Store Connect is Apple's portal for managing iOS, iPadOS, macOS, watchOS, and tvOS apps. After enrolling in the Apple Developer Program ($99/year), you access App Store Connect at appstoreconnect.apple.com. Here you create app listings, manage certificates and provisioning profiles, configure in-app purchases, and submit builds for TestFlight beta testing and App Store review.</p><p>To distribute an iOS app: (1) archive your app in Xcode (Product &gt; Archive), (2) upload via the Organizer window or Transporter app, (3) in App Store Connect, select the build, fill out metadata (description, keywords, screenshots, privacy URLs), and set pricing. Submit for review. Common rejections include incomplete privacy descriptions, placeholder UI, and crashes on the reviewer's device.</p><p>TestFlight allows up to 10,000 external testers without requiring their UDIDs. Internal testing supports up to 100 team members. TestFlight builds expire after 90 days. Adopt phased release (1%, 10%, 50%, 100%) and monitor crash reports and feedback before full rollout.</p>",
            ),
            (
                'Google Play Console',
                '<p>Google Play Console manages Android app publishing. Register for a Google Play Developer account ($25 one-time fee). The console provides publishing, testing, and monitoring tools. Build your Android App Bundle (<code>.aab</code>) in Android Studio using Build &gt; Generate Signed Bundle/APK. Sign with an upload key (different from your app signing key that Google manages).</p><p>Google Play offers four testing tracks: Internal (100 users, no review), Closed (up to 100,000 testers, no review), Open (public, no review), and Production (requires review). Use Closed testing for pre-release QA — Google now requires 12 testers with 14 days of testing for new developer accounts to access production.</p><p>After release, the Play Console provides Android Vitals — crash rate, ANR rate, startup time, and battery usage broken down by device model and Android version. Set up custom alerts for crash thresholds. Use in-app reviews API and in-app updates API to prompt users for ratings and force critical updates.</p>',
            ),
            (
                'Code Signing & Provisioning',
                "<p>iOS code signing ensures app integrity and identity. You need three things: (1) a <strong>Distribution Certificate</strong> (valid for 1 year, identifies your organization), (2) a <strong>Provisioning Profile</strong> (links certificate to app ID and devices), and (3) a <strong>Bundle ID</strong> (unique identifier like <code>com.example.app</code>). Xcode manages most of this automatically with automatic signing.</p><p>For manual signing, use the Apple Developer portal or Xcode's Accounts preferences to create certificates and profiles. App Store distribution uses an App Store provisioning profile; ad-hoc distribution includes specific device UDIDs; enterprise distribution uses in-house profiles (requires Apple Enterprise Program). For continuous integration, store certificates and profiles in a secure vault like Fastlane's match.</p><p>Android code signing uses a <strong>keystore</strong> (a binary file containing private keys). <code>keytool</code> generates keystores. Google Play App Signing lets you use an upload key for submission while Google manages the app signing key. This allows key replacement if your upload key is compromised. Keep your keystore in secure, backed-up storage — losing it means losing the ability to update your app.</p><pre><code># Android: generate a keystore\\nkeytool -genkey -v -keystore release.keystore \\\\\\n  -alias my-app -keyalg RSA -keysize 2048 \\\\\\n  -validity 10000\\n\\n# iOS: use Fastlane match for team signing\\nfastlane match appstore --git_url https://github.com/team/certs</code></pre>",
            ),
            (
                'CI/CD for Mobile Apps',
                '<p>Continuous integration and deployment for mobile apps automates building, testing, and distributing builds. Popular services include GitHub Actions, GitLab CI, Bitrise (mobile-focused), and Fastlane (the most popular mobile CI tool, integrates with all major CI providers). Fastlane automates screenshots, code signing, beta deployment, and app store submission.</p><p>A typical Fastlane setup uses a <code>Fastfile</code> defining lanes: <code>test</code> runs unit/integration tests, <code>beta</code> builds and deploys to TestFlight or Firebase App Distribution, <code>release</code> submits to App Store/Play Store. Fastlane\'s <code>snapshot</code> tool automates localized screenshot capture. <code>match</code> manages signing identities across the team via a Git repository.</p><p>CI pipeline best practices: run linting and tests on every pull request. Execute UI tests on real devices via cloud services (Firebase Test Lab for Android, Mac Stadium or AWS Device Farm for iOS). Store signing keys as encrypted CI secrets. Publish beta builds automatically after merges to main. Tag releases with semantic versioning triggered by git tags.</p><pre><code># Fastfile: iOS lanes example\\nplatform :ios do\\n  lane :beta do\\n    capture_screenshots\\n    match(type: "appstore")\\n    build_app(scheme: "MyApp")\\n    upload_to_testflight(\\n      skip_waiting_for_build_processing: true\\n    )\\n  end\\n\\n  lane :release do\\n    match(type: "appstore")\\n    build_app(scheme: "MyApp")\\n    upload_to_app_store(skip_metadata: false)\\n  end\\nend</code></pre>',
            ),
        ],
        [
            ('App Store Connect Help', 'https://developer.apple.com/help/app-store-connect/', 'Official Apple App Store submission guide.'),
            ('Google Play Console Help', 'https://support.google.com/googleplay/android-developer', 'Official Android publishing documentation.'),
            ('Fastlane Documentation', 'https://docs.fastlane.tools', 'The most popular mobile DevOps tool.'),
            ('Code Signing Guide', 'https://developer.apple.com/support/code-signing/', "Apple's guide to iOS code signing."),
        ],
    )


    # =========================================================================
    # Game Dev (0)
    # =========================================================================

    # =========================================================================
    # IoT (0)
    # =========================================================================

    # =========================================================================
    # Career (0)
    # =========================================================================

    # =========================================================================
    # Accessibility (0)
    # =========================================================================

    # =========================================================================
    # General (0)


    # =========================================================================
    # Game Dev (5)
    # =========================================================================
    build_page(
        'Godot Engine Game Development',
        'godot-basics.html',
        'Get started with Godot Engine — the scene system, GDScript, 2D/3D rendering, signals, and node-based architecture.',
        'Game Dev',
        'fas fa-gamepad',
        [
            (
                "Godot's Scene System",
                '<p>In Godot, everything is a <strong>node</strong>. A node is a single element with a specific function — a <code>Sprite2D</code> displays an image, an <code>AudioStreamPlayer2D</code> plays sound, a <code>CollisionShape2D</code> defines physics boundaries. Nodes are organized in a tree called a <strong>scene</strong>. A scene can be a player character, a level, a UI menu — anything you build from nodes.</p><p>Scenes are reusable and nestable. A Player scene containing Sprite2D, AnimationPlayer, and CollisionShape2D can be instanced into a Level scene. Changes to the Player scene update all instances automatically. This composition-over-inheritance approach keeps projects modular.</p><p>Each node has lifecycle callbacks: <code>_ready()</code> (called when node enters the tree), <code>_process(delta)</code> (called every frame), and <code>_physics_process(delta)</code> (called at fixed rate for physics).</p>',
            ),
            (
                'GDScript Fundamentals',
                "<p>GDScript is Godot's native scripting language, similar to Python. It's dynamically typed with optional static typing. Variables use <code>var</code>, constants use <code>const</code>. Indentation defines blocks. GDScript uses <code>func</code> for functions, <code>if/elif/else</code> for conditionals, and <code>match</code> for pattern matching.</p><p>Key features: <code>@export</code> exposes variables in the inspector. <code>@onready</code> defers initialization. Signals are built-in event notification. Godot 4 added typed arrays, lambda functions, and the <code>@tool</code> annotation for editor scripts.</p><pre><code>extends Node2D\\n@export var speed: int = 200\\nfunc _process(delta: float):\\n    var input = Input.get_vector(&quot;left&quot;, &quot;right&quot;, &quot;up&quot;, &quot;down&quot;)\\n    position += input * speed * delta</code></pre>",
            ),
            (
                '2D & 3D Rendering',
                "<p>Godot treats 2D and 3D as separate engines. For 2D, use <code>CanvasItem</code> nodes: <code>Node2D</code>, <code>Sprite2D</code>, <code>AnimatedSprite2D</code>, <code>TileMap</code>. The Y-axis points down. For 3D, use <code>Node3D</code> nodes: <code>MeshInstance3D</code>, <code>DirectionalLight3D</code>, <code>Camera3D</code>.</p><p>Godot 4's renderer supports Forward+ (high-end), Mobile (optimized), and Compatibility (GLES3 fallback). Import 3D models in glTF, FBX, or OBJ format. Custom shaders use GLSL via <code>ShaderMaterial</code>.</p>",
            ),
            (
                'Signals & Event Communication',
                '<p>Signals are Godot\'s observer pattern. A node emits a signal and connected nodes receive callbacks, decoupling game systems. Custom signals: <code>signal health_changed(amount)</code> and <code>health_changed.emit(10)</code>.</p><p>Connect signals via editor, <code>signal.connect(callable)</code>, or automatically. Use groups with <code>add_to_group("enemies")</code> and <code>get_tree().call_group("enemies", "take_damage", 10)</code> for broadcasting.</p>',
            ),
        ],
        [
            ('Godot Engine Documentation', 'https://docs.godotengine.org', 'Official Godot documentation.'),
            ('GDQuest Godot Tutorials', 'https://gdquest.com', 'High-quality Godot learning resources.'),
        ],
    )

    build_page(
        'Unity Game Engine Introduction',
        'unity-basics.html',
        'Introduction to Unity game development — GameObjects, components, physics, C# scripting, and editor workflow.',
        'Game Dev',
        'fas fa-gamepad',
        [
            (
                'GameObjects & Components',
                '<p>Unity uses an Entity-Component architecture. Every object is a <strong>GameObject</strong> (empty container) with attached <strong>Components</strong> that give behavior: <code>MeshRenderer</code> (visibility), <code>Rigidbody</code> (physics), <code>BoxCollider</code> (collision), custom C# scripts (game logic).</p><p>The Transform component (position, rotation, scale) is mandatory. Access components via <code>GetComponent&lt;Type&gt;()</code>. GameObjects nest in parent-child hierarchies. Prefabs are reusable templates with saved configurations.</p>',
            ),
            (
                'C# Scripting in Unity',
                '<p>Unity scripts inherit from <code>MonoBehaviour</code>. Lifecycle: <code>Awake()</code>, <code>Start()</code>, <code>Update()</code>, <code>FixedUpdate()</code> (physics), <code>LateUpdate()</code> (camera follow). Public fields appear in the Inspector.</p><pre><code>using UnityEngine;\\npublic class PlayerController : MonoBehaviour {\\n    public float speed = 5f;\\n    void Update() {\\n        float h = Input.GetAxis(&quot;Horizontal&quot;);\\n        transform.Translate(Vector3.right * h * speed * Time.deltaTime);\\n    }\\n}</code></pre>',
            ),
            (
                'Physics & Collision',
                "<p>Unity's physics engine (PhysX) handles rigid bodies, collisions, and joints. <code>Rigidbody</code> enables physics. Colliders define shapes: <code>BoxCollider</code>, <code>SphereCollider</code>, <code>CapsuleCollider</code>. Triggers (<code>isTrigger = true</code>) detect overlaps without physical response.</p><p>Collision callbacks: <code>OnCollisionEnter()</code>, <code>OnCollisionStay()</code>, <code>OnCollisionExit()</code>. Use <code>Physics.Raycast()</code> for line-of-sight and shooting. Physics layers prevent unnecessary checks.</p>",
            ),
            (
                'Editor Workflow & Asset Pipeline',
                '<p>Key editor panels: Scene, Game, Project (assets), Hierarchy, Inspector, Console. Play mode tests within the editor. Assets (PNG, FBX, WAV) are imported with configurable settings via the Inspector.</p><p>The Asset Store provides free and paid assets. Version control: use Unity Smart Merge with Git. External script editor: VS Code or Rider with Unity IntelliSense.</p>',
            ),
        ],
        [
            ('Unity Manual', 'https://docs.unity3d.com/Manual/index.html', 'Official Unity documentation.'),
            ('Unity Learn', 'https://learn.unity.com', 'Free official tutorials and courses.'),
        ],
    )

    build_page(
        'Game Loop & Architecture Patterns',
        'game-architecture.html',
        'Design robust game architecture — game loop patterns, ECS, state machines, component patterns, and code organization.',
        'Game Dev',
        'fas fa-gamepad',
        [
            (
                'The Game Loop Pattern',
                "<p>Every game runs a loop: process input, update state, render. Modern engines abstract this with per-frame callbacks. The key variable is <strong>delta time</strong> — time since last frame — used for frame-rate-independent movement.</p><p>Fixed timestep vs variable: physics needs fixed timestep (e.g., 60Hz) for determinism, rendering runs variable. Unity separates with <code>FixedUpdate()</code> and <code>Update()</code>. Godot has <code>_physics_process()</code> and <code>_process()</code>.</p><p>Update order: player input, AI, physics, late-update systems (camera). Unity's execution order settings prioritize scripts.</p><pre><code>// Fixed timestep accumulator\\nfloat accumulator = 0f;\\nconst float FIXED_DT = 1f / 60f;\\nvoid Update() {\\n    accumulator += Time.deltaTime;\\n    while (accumulator &gt;= FIXED_DT) {\\n        FixedUpdatePhysics(FIXED_DT);\\n        accumulator -= FIXED_DT;\\n    }\\n}</code></pre>",
            ),
            (
                'Entity-Component-System (ECS)',
                "<p>ECS separates data (components) from behavior (systems), organizing entities as IDs with component collections. Unlike OOP inheritance, ECS composes from components: <code>Position</code>, <code>Velocity</code>, <code>Health</code>.</p><p>Benefits: cache-friendly data (contiguous arrays), better multithreading, flexibility. Unity's DOTS uses ECS with Burst compiler for C++-near performance. Hybrid approaches use ECS for performance-critical systems and OOP for high-level logic.</p>",
            ),
            (
                'Finite State Machines (FSM)',
                "<p>FSMs model behavior as states with transitions. Player states: Idle, Running, Jumping, Attacking, Dead. Each state has <code>Enter()</code>, <code>Update()</code>, <code>Exit()</code>. Transitions are triggered by conditions.</p><p>Hierarchical FSMs allow nested states (Alive super-state containing Idle/Move/Attack). Behavior trees (selectors, sequences, decorators) are often preferred for AI as they're easier to extend and visualize.</p>",
            ),
            (
                'Service Locator & Dependency Injection',
                '<p>The Service Locator pattern provides a central registry: <code>AudioService</code>, <code>SaveLoadService</code>. <code>AudioManager.Instance.PlaySound("shoot")</code> is cleaner than finding references everywhere.</p><p>Dependency Injection inverts control — services are injected into constructors. Unity\'s Zenject/Extenject auto-wires dependencies. ScriptableObject event channels decouple UI from game logic via a <code>GameEvent</code> ScriptableObject with listener lists.</p>',
            ),
        ],
        [
            ('Game Programming Patterns', 'https://gameprogrammingpatterns.com', 'Free online book by Robert Nystrom.'),
            ('Unity DOTS Overview', 'https://unity.com/dots', "Unity's Data-Oriented Tech Stack."),
        ],
    )

    build_page(
        '2D Game Physics & Collision Detection',
        '2d-game-physics.html',
        'Implement 2D physics for games — rigid bodies, collision shapes, triggers, raycasting, and optimization techniques.',
        'Game Dev',
        'fas fa-gamepad',
        [
            (
                'Rigid Bodies & Forces',
                "<p>A <strong>rigid body</strong> moves under physical forces. Unity's <code>Rigidbody2D</code> has body types: Dynamic (forces/gravity), Kinematic (script-driven, pushes dynamics), Static (immovable walls).</p><p>Apply forces with <code>AddForce()</code> (gradual), <code>AddImpulse()</code> (instant), or direct <code>velocity</code> setting. Physics material controls bounciness and friction. For responsive platformers, kinematic bodies with manual velocity are preferred.</p>",
            ),
            (
                'Collision Shapes & Layers',
                '<p>Common 2D colliders: <code>BoxCollider2D</code>, <code>CircleCollider2D</code>, <code>CapsuleCollider2D</code>, <code>PolygonCollider2D</code>. Godot equivalents: <code>CollisionShape2D</code> with shape resources.</p><p>Collision layers prevent unwanted interactions. Define layers (Player, Enemy, Projectile) and set the collision matrix. A player\'s attack hitbox on "PlayerHitbox" layer only collides with "EnemyHurtbox".</p>',
            ),
            (
                'Triggers & Overlap Detection',
                '<p>Triggers detect overlaps without physical response. Mark collider as trigger (<code>isTrigger</code> in Unity). Use for: pickups, zone detection, melee range. Overlap checks: <code>Physics2D.OverlapCircle()</code>, <code>OverlapBox()</code>, <code>OverlapArea()</code>.</p><p>Avoid <code>OnTriggerStay2D()</code> every frame — use Enter/Exit to register objects. For many triggers, prefer overlap queries over individual colliders.</p>',
            ),
            (
                'Raycasting & Line of Sight',
                '<p>Raycasting fires a line and reports hits. Use for: shooting, ground detection, wall detection, object interaction. <code>Physics2D.Raycast(origin, direction, distance, layerMask)</code>.</p><p>Layer masks filter raycasts. Debug with <code>Debug.DrawLine()</code>. Advanced: <code>CircleCast</code>, <code>BoxCast</code>, <code>OverlapCircleNonAlloc</code>. Enable CCD on fast-moving objects to prevent tunneling.</p><pre><code>RaycastHit2D hit = Physics2D.Raycast(origin, dir, dist);\\nif (hit.collider &amp;&amp; hit.collider.CompareTag(&quot;Enemy&quot;))\\n    hit.collider.GetComponent&lt;Enemy&gt;().TakeDamage(10);</code></pre>',
            ),
        ],
        [
            ('Unity 2D Physics Overview', 'https://docs.unity3d.com/Manual/Physics2DOverview.html', 'Official Unity 2D physics documentation.'),
            ('Godot 2D Physics Tutorial', 'https://docs.godotengine.org/en/stable/tutorials/physics/physics_introduction.html', 'Godot physics introduction.'),
        ],
    )

    build_page(
        'Procedural Content Generation',
        'procedural-generation.html',
        'Generate game content procedurally — noise functions, dungeon generation, terrain algorithms, and PCG design patterns.',
        'Game Dev',
        'fas fa-gamepad',
        [
            (
                'Noise Functions: Perlin & Simplex',
                '<p>Noise functions generate pseudo-random continuous values. <strong>Perlin noise</strong> (1983) produces smooth gradients. <strong>Simplex noise</strong> (2001) is cheaper with fewer artifacts. Octaves layer frequencies: lower octaves define shape, higher add detail.</p><p>Fractional Brownian Motion (fBm) combines octaves with persistence scaling. Domain warping creates organic shapes. Seeded noise allows reproducible worlds.</p><pre><code>float GetHeight(float x, float z, int seed) {\\n    float amplitude = 1f, frequency = 1f, height = 0f;\\n    for (int i = 0; i &lt; octaves; i++) {\\n        float sampleX = (x + seed) * frequency * scale;\\n        height += Mathf.PerlinNoise(sampleX, sampleZ) * amplitude;\\n        amplitude *= persistence;\\n        frequency *= lacunarity;\\n    }\\n    return height;\\n}</code></pre>',
            ),
            (
                'Dungeon Generation Algorithms',
                "<p><strong>Binary Space Partition (BSP)</strong> recursively splits rectangles into rooms, connecting with corridors. <strong>Drunkard's Walk</strong> carves organic tunnels. <strong>Random Room Placement</strong> places non-overlapping rectangles, connects nearest neighbors.</p><p><strong>Cellular Automata</strong> generates caves from random noise with iteration rules. <strong>Delaunay triangulation</strong> + minimum spanning tree ensures connected rooms with loops. Use A* to verify reachability.</p>",
            ),
            (
                'Terrain Generation & Erosion',
                '<p>Start with fBm Perlin noise, then apply <strong>hydraulic erosion</strong> — water erodes high areas and deposits sediment, creating realistic valleys. Thermal erosion smooths steep slopes.</p><p>Biome mapping: elevation thresholds (coast, grassland, forest, mountain) combined with moisture noise. Voxel terrain uses 3D Perlin noise for solid/air distinction with cave subtraction.</p>',
            ),
            (
                'PCG Design Patterns',
                '<p><strong>Grammar-based generation</strong> (L-systems) creates fractal plants and cities. <strong>WFC (Wave Function Collapse)</strong> generates locally-similar patterns from example inputs — used for tile-based levels.</p><p><strong>Seeded generation</strong> ensures reproducibility with a single integer seed. Allow sharing seeds for same-world experiences. Version your generation algorithm for backward compatibility.</p>',
            ),
        ],
        [
            ('Procedural Content Generation in Games', 'https://www.pcgbook.com', 'Academic book on PCG.'),
            ('Red Blob Games PCG Tutorials', 'https://www.redblobgames.com', 'Interactive tutorials on noise and algorithms.'),
        ],
    )


    # =========================================================================
    # IoT (5)
    # =========================================================================
    build_page(
        'Arduino Programming & Electronics',
        'arduino-basics.html',
        'Program Arduino microcontrollers — digital/analog I/O, sensor interfacing, communication protocols, and real-world projects.',
        'IoT',
        'fas fa-microchip',
        [
            (
                'Arduino Platform Overview',
                '<p>Arduino is an open-source electronics platform. The Uno uses an ATmega328P at 16MHz with 32KB flash, 14 digital I/O pins (6 PWM), 6 analog inputs. Other boards: Nano (compact), Mega (more pins), ESP32 (WiFi/Bluetooth).</p><p>The Arduino IDE provides a simplified C++. Every sketch has <code>setup()</code> (runs once) and <code>loop()</code> (runs repeatedly). Alternatives: PlatformIO (VS Code) and Arduino CLI.</p><pre><code>void setup() { pinMode(LED_BUILTIN, OUTPUT); }\\nvoid loop() {\\n  digitalWrite(LED_BUILTIN, HIGH); delay(1000);\\n  digitalWrite(LED_BUILTIN, LOW); delay(1000);\\n}</code></pre>',
            ),
            (
                'Digital & Analog I/O',
                '<p><strong>Digital I/O</strong>: <code>pinMode(pin, OUTPUT)</code> for LEDs/motors/relays. <code>INPUT_PULLUP</code> enables internal pull-up for buttons. <code>digitalRead()</code> detects presses (debounce with delay).</p><p><strong>Analog Input</strong>: 10-bit ADC (0-1023). <code>analogRead(A0)</code> returns proportional voltage. Use for potentiometers, LDRs, temperature sensors. <strong>PWM</strong>: <code>analogWrite(pin, 0-255)</code> controls LED brightness, servo position, motor speed.</p>',
            ),
            (
                'Sensor Interfacing',
                '<p>Digital sensors (DHT11/DHT22) use single-wire protocol. I2C sensors (MPU6050 gyro, VL53L0X distance) connect via SDA/SCL with the <code>Wire</code> library. Analog sensors output variable voltage: TMP36 outputs 10mV per degree C.</p><p>Best practices: long reading intervals (300ms+) save power. Moving average filters smooth noise. For outdoor sensors, use weatherproof enclosures.</p><pre><code>#include &lt;DHT.h&gt;\\nDHT dht(2, DHT22);\\nvoid loop() {\\n  float t = dht.readTemperature();\\n  float h = dht.readHumidity();\\n  delay(2000);\\n}</code></pre>',
            ),
            (
                'Communication Protocols',
                '<p><strong>Serial (UART)</strong>: TX/RX pins, <code>Serial.begin(9600)</code>. Common baud: 9600 (reliable), 115200 (fast). <strong>I2C</strong>: two wires (SDA/SCL), multiple devices per bus, unique addresses. <strong>SPI</strong>: four wires (MOSI, MISO, SCK, SS), faster than I2C, good for displays and SD cards.</p><p>For wireless: NRF24L01 modules (2.4GHz, SPI interface, up to 1km range).</p>',
            ),
        ],
        [
            ('Arduino Official Documentation', 'https://docs.arduino.cc', 'Complete Arduino reference.'),
            ('Adafruit Learning System', 'https://learn.adafruit.com', 'Excellent tutorials for sensors and IoT hardware.'),
        ],
    )

    build_page(
        'ESP32 with MicroPython',
        'esp32-micropython.html',
        'Program ESP32 microcontrollers with MicroPython — WiFi, Bluetooth, sensor integration, deep sleep, and OTA updates.',
        'IoT',
        'fas fa-microchip',
        [
            (
                'Setting Up MicroPython on ESP32',
                "<p>MicroPython brings Python to microcontrollers. Flash firmware: <code>esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash &amp;&amp; esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-*.bin</code>.</p><p>After flashing, connect via serial at 115200 baud. You'll see the REPL prompt. <code>boot.py</code> runs first, <code>main.py</code> runs your application. Upload scripts via Thonny, ampy, or WebREPL.</p><pre><code>from machine import Pin\\nfrom time import sleep\\nled = Pin(2, Pin.OUT)\\nwhile True:\\n    led.value(not led.value())\\n    sleep(0.5)</code></pre>",
            ),
            (
                'WiFi & Networking',
                "<p>ESP32's WiFi is ideal for IoT. Use <code>network</code> module: station mode connects to AP, AP mode creates access point. Simple HTTP server with <code>socket</code> module. MQTT with <code>umqtt.simple</code> is more efficient. mDNS gives hostnames like <code>esp32.local</code>.</p><pre><code>import network\\nwlan = network.WLAN(network.STA_IF)\\nwlan.active(True)\\nwlan.connect('SSID', 'PASSWORD')\\nwhile not wlan.isconnected(): time.sleep(1)\\nprint('Connected:', wlan.ifconfig())</code></pre>",
            ),
            (
                'Sensors & Actuators',
                "<p>Read sensors: <code>machine.ADC(Pin(34))</code> (12-bit, 0-4095). DHT22 with <code>dht</code> module. I2C sensors with <code>machine.I2C</code>. Actuators: servos with <code>machine.PWM</code> (50Hz, duty 40-115). NeoPixel RGB LEDs with <code>neopixel</code> module.</p><p>Data logging: write to filesystem (<code>with open('data.csv', 'a') as f</code>), send to MQTT, or upload via HTTP.</p>",
            ),
            (
                'Deep Sleep & Power Management',
                '<p>Deep sleep cuts current from ~80mA to ~10uA. <code>machine.deepsleep(time_ms)</code>. Wake on timer or GPIO. RTC memory retains data: <code>machine.RTC().memory()</code> (8KB).</p><p>Strategies: deep sleep instead of delays. WiFi on only when needed. Lower CPU frequency: <code>machine.freq(80000000)</code>. Use low-quiescent regulators (MCP1700: 1.6uA).</p><pre><code>import machine\\nmachine.deepsleep(10000)  # Sleep 10 seconds</code></pre>',
            ),
            (
                'OTA Updates & Remote Management',
                '<p>OTA updates let you update firmware wirelessly. Options: WebREPL file upload, custom HTTP download of <code>main.py</code>, or dual-boot partition scheme.</p><p>For remote management: subscribe to MQTT command topic (<code>devices/esp32-livingroom/cmd</code>). Commands: <code>{"cmd": "restart"}</code>, <code>{"cmd": "update", "url": "..."}</code>. Build a watchdog timer for auto-recovery.</p>',
            ),
        ],
        [
            ('MicroPython ESP32 Docs', 'https://docs.micropython.org/en/latest/esp32/quickref.html', 'Official MicroPython quick reference.'),
            ('Random Nerd Tutorials ESP32', 'https://randomnerdtutorials.com/esp32-micropython/', 'Comprehensive ESP32 MicroPython tutorials.'),
        ],
    )

    build_page(
        'Home Assistant Smart Home',
        'home-assistant-guide.html',
        'Set up Home Assistant for smart home automation — installation, integrations, automations, dashboards, and best practices.',
        'IoT',
        'fas fa-microchip',
        [
            (
                'Installing Home Assistant',
                '<p>Home Assistant OS is the recommended installation. Write to SD/SSD with Balena Etcher, boot Raspberry Pi 4/5 or x86, access at <code>http://homeassistant.local:8123</code>. Alternatives: Docker container, Core (venv), or supervised install.</p><p>After boot, create an owner account. Home Assistant auto-discovers devices via mDNS/UPnP — Philips Hue, Sonoff, Google Home appear automatically.</p>',
            ),
            (
                'Integrations & Device Setup',
                '<p>Integrations connect devices and services. Over 2,000 built-in integrations: Philips Hue, TP-Link Kasa, Zigbee2MQTT, Z-Wave JS, ESPHome. Add via Settings &gt; Devices &amp; Services &gt; Add Integration.</p><p>After adding, entities are created with unique IDs like <code>sensor.living_room_temperature</code>. Entities have state and attributes. Use Developer Tools &gt; States to inspect.</p>',
            ),
            (
                'Automations & Scripts',
                '<p>Automations use triggers, conditions, and actions. Visual editor creates rules without YAML. Triggers: time, device state, events. Conditions: time of day, home/away. Actions: turn lights, send notifications.</p><p>Blueprints are pre-built automations shared by the community. Scripts are reusable action sequences. Scenes snapshot device states for recall.</p><pre><code># Motion-activated light\\nalias: &quot;Hallway Light&quot;\\ntrigger:\\n  - platform: state\\n    entity_id: binary_sensor.hallway_motion\\n    to: &quot;on&quot;\\naction:\\n  - service: light.turn_on\\n    target:\\n      entity_id: light.hallway\\n  - delay: 5 min\\n  - service: light.turn_off\\n    target:\\n      entity_id: light.hallway</code></pre>',
            ),
            (
                'Dashboards & Lovelace UI',
                '<p>The dashboard (Lovelace) is fully customizable. Add cards: entity buttons, sensor graphs, gauges, camera feeds, weather forecasts. Conditional cards show/hide based on state. Tab-based dashboards organize by room.</p><p>For wall-mounted tablets, use kiosk-mode add-on. Use <code>browser_mod</code> for battery monitoring and screen wake-lock. Design high-contrast interfaces with large touch buttons.</p>',
            ),
        ],
        [
            ('Home Assistant Documentation', 'https://www.home-assistant.io/docs/', 'Official HA setup and configuration guide.'),
            ('ESPHome Documentation', 'https://esphome.io', 'Build custom sensors for Home Assistant.'),
        ],
    )

    build_page(
        'IoT Sensor Projects',
        'iot-sensor-projects.html',
        'Build practical IoT sensor projects — temperature, humidity, motion, and distance sensors with data logging and visualization.',
        'IoT',
        'fas fa-microchip',
        [
            (
                'Temperature & Humidity Sensors',
                '<p>The DHT22 is the most popular temperature/humidity sensor. Range: -40C to 80C, +/-0.5C accuracy. Read every 2 seconds. Wire with 4.7k pull-up resistor. DHT11 is cheaper but less accurate (+/-2C).</p><p>The BME280 measures temperature, humidity, and barometric pressure via I2C/SPI. More accurate than DHT22 and reads at 100Hz. Good for weather stations. The DS18B20 provides +/-0.1C accuracy via OneWire protocol, multiple sensors on one pin.</p><pre><code>#include &lt;Adafruit_BME280.h&gt;\\nAdafruit_BME280 bme;\\nvoid setup() { bme.begin(0x76); }\\nvoid loop() {\\n  Serial.print(bme.readTemperature());\\n  Serial.print(bme.readPressure() / 100.0);\\n  Serial.println(bme.readHumidity());\\n  delay(5000);\\n}</code></pre>',
            ),
            (
                'Motion & Presence Detection',
                '<p>PIR sensors (HC-SR501) detect motion via infrared changes. Sensitivity up to 7m, hold time 0.5s to 5min. For advanced presence, use mmWave radar (LD2410) that detects micro-movements through walls.</p><p>Ultrasonic sensors (HC-SR04) measure distance: trigger sends 10us pulse, echo returns pulse at 58us per cm. Range 2cm to 4m, accuracy 3mm. Use for liquid levels, parking sensors.</p>',
            ),
            (
                'Data Logging & Visualization',
                '<p>Local logging: microSD card module with SD library writes CSV with timestamps. Batch writes to minimize SD wear — store in RAM, flush every 10-60 minutes.</p><p>Cloud logging: Adafruit IO (simple MQTT), InfluxDB + Grafana (powerful visualization), or custom web dashboard. Use timestamps (NTP sync) and format data as JSON for cloud APIs.</p>',
            ),
        ],
        [
            ('Adafruit Learning System', 'https://learn.adafruit.com', 'Tutorials for sensors and displays.'),
            ('InfluxDB + Grafana Guide', 'https://docs.influxdata.com', 'Time-series database and visualization.'),
        ],
    )

    build_page(
        'MQTT Protocol for IoT',
        'mqtt-protocol.html',
        'Learn the MQTT protocol for IoT communication — publish/subscribe, brokers, Quality of Service levels, topics, and security.',
        'IoT',
        'fas fa-microchip',
        [
            (
                'Publish/Subscribe Model',
                "<p>MQTT uses a publish/subscribe model where clients connect to a <strong>broker</strong> and communicate via <strong>topics</strong>. Publishers send messages to topics; subscribers receive messages from topics they've subscribed to. This decouples senders from receivers.</p><p>Topics are hierarchical: <code>sensor/livingroom/temperature</code>. Clients subscribe with wildcards: <code>sensor/+/temperature</code> (single-level) or <code>sensor/#</code> (multi-level). This allows flexible grouping.</p>",
            ),
            (
                'Brokers & Clients',
                '<p>Popular brokers: Mosquitto (lightweight, open-source), EMQX (enterprise, scalable), HiveMQ Cloud (free tier), and AWS IoT Core (cloud-managed). Client libraries exist for every language.</p><p>Setting up Mosquitto: <code>apt install mosquitto mosquitto-clients</code>. Publish: <code>mosquitto_pub -h broker -t "test/topic" -m "Hello"</code>. Subscribe: <code>mosquitto_sub -h broker -t "test/topic"</code>.</p>',
            ),
            (
                'Quality of Service (QoS)',
                '<p>MQTT offers three QoS levels. <strong>QoS 0</strong>: At most once (fire and forget) — fastest but may lose messages. <strong>QoS 1</strong>: At least once — guaranteed delivery but possible duplicates. <strong>QoS 2</strong>: Exactly once — guaranteed and no duplicates, but slowest due to four-step handshake.</p><p>Choose QoS wisely: use 0 for frequent sensor readings where occasional loss is acceptable, 1 for commands that must arrive, 2 for financial or critical control systems. Higher QoS increases bandwidth and latency.</p>',
            ),
            (
                'Security & Best Practices',
                '<p>MQTT security: enable TLS/SSL encryption, use username/password authentication, and restrict topic access via ACL (Access Control Lists). Never use default credentials on production brokers.</p><p>Best practices: set <strong>Last Will and Testament (LWT)</strong> to notify when a client disconnects unexpectedly. Use <strong>Retained Messages</strong> for device state that new subscribers receive immediately. Keep payloads small — use binary or compact JSON formats.</p><pre><code># Mosquitto ACL example\\nuser sensor_node\\ntopic write sensor/+/temperature\\ntopic read sensor/+/status\\n\\nuser admin\\ntopic readwrite #</code></pre>',
            ),
        ],
        [
            ('MQTT Official Specification', 'https://mqtt.org', 'Official MQTT protocol specification.'),
            ('Mosquitto Documentation', 'https://mosquitto.org/documentation/', 'Open-source MQTT broker guide.'),
        ],
    )


    # =========================================================================
    # Career (5)
    # =========================================================================
    build_page(
        'Tech Resume Writing Guide',
        'tech-resume-guide.html',
        'Write an effective tech resume — structure, keywords, achievements, ATS optimization, and industry-specific advice.',
        'Career',
        'fas fa-briefcase',
        [
            (
                'Resume Structure & Format',
                '<p>A tech resume should follow a reverse-chronological format. Essential sections: Contact Info, Professional Summary, Technical Skills (grouped by category), Professional Experience (with bullet points), Education, and optional sections (Projects, Certifications, Publications).</p><p>Keep it to one page for under 10 years experience, two pages max for senior roles. Use a clean, ATS-friendly format — avoid tables, columns, and graphics that confuse parsers. Save as PDF unless instructed otherwise.</p>',
            ),
            (
                'Keywords & ATS Optimization',
                '<p>Applicant Tracking Systems (ATS) scan resumes for keywords from the job description. Include specific technologies (Python, AWS, Docker, Kubernetes), methodologies (Agile, CI/CD), and domain terms. Use both acronyms and full names: "AWS (Amazon Web Services)".</p><p>Weave keywords naturally into experience bullets and skills sections. Don\'t just list them — demonstrate context: "Reduced deployment time by 60% using Docker and Kubernetes." Check your resume with ATS simulators like Jobscan.</p>',
            ),
            (
                'Writing Achievement Bullets',
                '<p>Use the STAR method (Situation, Task, Action, Result) for each bullet. Start with a strong action verb: "Designed," "Implemented," "Optimized," "Led." Quantify results: "Reduced API latency by 40%," "Managed a team of 5 engineers," "Served 1M+ daily users."</p><p>Avoid vague statements like "Responsible for..." or "Worked on..." Instead: "Architected a microservices migration that improved deployment frequency from monthly to weekly." Include metrics, technologies, and business impact.</p>',
            ),
            (
                'Tailoring for Different Roles',
                '<p>Customize your resume for each application. For startups, emphasize full-stack skills, versatility, and speed. For FAANG/big tech, focus on system design, scalability, and algorithms. For agencies, highlight client management and project delivery.</p><p>Create a "master resume" with all your experience, then trim and reorder bullets for each application. Keep a "Technical Skills" section that you reorder based on the job requirements — put relevant skills first.</p>',
            ),
        ],
        [
            ('Resume Worded', 'https://resumeworded.com', 'Free ATS resume checker and optimization tool.'),
            ("Google's Resume Guide", 'https://careers.google.com/how-we-hire/resume/', 'Official Google resume advice.'),
        ],
    )

    build_page(
        'GitHub Portfolio & Open Source',
        'github-portfolio.html',
        'Build an impressive GitHub portfolio — profile README, project repositories, contribution graph, and personal branding.',
        'Career',
        'fas fa-briefcase',
        [
            (
                'Profile README & Branding',
                '<p>Your GitHub profile README is the first thing recruiters see. Create a repository with your username and add a README.md. Include: a brief bio, key skills with badges, pinned repositories, GitHub stats, and links to LinkedIn, personal site, or blog.</p><p>Use Shields.io badges for technologies: <code>![Python](https://img.shields.io/badge/Python-3.11-blue)</code>. Keep it professional — avoid excessive GIFs or meme content. Update it periodically with new accomplishments.</p>',
            ),
            (
                'Pinned Repositories & Projects',
                '<p>Pin 6 repositories that showcase your best work. At least 3 should be substantial personal projects, not forks. Each pinned repo needs: a clear name, one-line description, detailed README (what, why, how, tech stack), and live demo link if possible.</p><p>Use GitHub Topics to tag technologies ("python," "machine-learning," "react"). Maintain a clean commit history — use conventional commits. Add a LICENSE file (MIT recommended for portfolio projects) and CONTRIBUTING.md if open to collaboration.</p>',
            ),
            (
                'Contributions & Activity',
                '<p>A consistent contribution graph signals active development. Aim for small daily contributions: documentation fixes, issue comments, dependency updates. Use GitHub Actions to automate tasks (auto-merge Dependabot, scheduled tests).</p><p>Quality over quantity: meaningful PRs to established projects carry more weight than hundreds of trivial commits. Contribute to projects you actually use — fix bugs you encounter, improve documentation you found confusing.</p>',
            ),
            (
                'Open Source Collaboration Etiquette',
                '<p>Before contributing: read CONTRIBUTING.md, check open issues labeled "good first issue" or "help wanted." Comment on the issue to express interest before starting work. Fork the repo, create a descriptive branch name, and make focused changes.</p><p>Write clear commit messages and PR descriptions explaining what and why. Be responsive to reviewer feedback. If your PR isn\'t merged, don\'t take it personally — maintainers have their own priorities. Stay professional in all interactions.</p>',
            ),
        ],
        [
            ('GitHub Profile README Guide', 'https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile/customizing-your-profile/managing-your-profile-readme', 'Official GitHub guide.'),
            ('Awesome GitHub Profile README', 'https://github.com/abhisheknaiidu/awesome-github-profile-readme', 'Curated list of profile README examples.'),
        ],
    )

    build_page(
        'Open Source Contribution Guide',
        'open-source-contributions.html',
        'Start contributing to open source — finding projects, PR workflow, community etiquette, and building your reputation.',
        'Career',
        'fas fa-briefcase',
        [
            (
                'Finding the Right Project',
                '<p>Start with projects you already use. Check the "good first issue" and "help wanted" labels. Use tools like Up For Grabs, CodeTriage, and First Timers Only to find beginner-friendly issues.</p><p>Evaluate project health: recent commits, responsive maintainers, clear documentation, active community (Discord, Discourse). Avoid projects with stale issues, unwelcoming code of conduct, or no response for months.</p>',
            ),
            (
                'PR Workflow & Best Practices',
                "<p>Fork the repository, create a feature branch, make focused commits. Follow the project's coding style — match existing patterns, use their linter config. Write tests if the project has a test suite.</p><p>PR description: explain what the change does, why it's needed, and how to test it. Reference related issues. Keep PRs small and focused — one feature or fix per PR. Large changes should be discussed in an issue first.</p>",
            ),
            (
                'Community Etiquette',
                '<p>Be respectful and patient. Maintainers are often volunteers with limited time. Read existing discussions before asking questions. When disagreeing, focus on technical merits, not personalities.</p><p>Give constructive code reviews. Thank reviewers for their time. If your contribution is rejected, ask for specific feedback and try again. Build relationships by consistently contributing quality work.</p>',
            ),
            (
                'Building Your Reputation',
                '<p>Consistent quality contributions build reputation. Start with documentation and bug fixes, then progress to features. Maintain your own popular projects. Become a reviewer for projects you know well.</p><p>A strong GitHub profile with meaningful contributions is a powerful career asset. Many companies recruit directly from open source communities. Speaking at conferences about your contributions adds visibility.</p>',
            ),
        ],
        [
            ('First Timers Only', 'https://www.firsttimersonly.com', 'Beginner-friendly open source contributions.'),
            ('Open Source Guide', 'https://opensource.guide', 'Comprehensive guide to open source contribution.'),
        ],
    )

    build_page(
        'Technical Interview Preparation',
        'technical-interviewing.html',
        'Prepare for technical interviews — coding challenges, system design, behavioral questions, salary negotiation, and strategy.',
        'Career',
        'fas fa-briefcase',
        [
            (
                'Coding Interview Preparation',
                '<p>Master data structures and algorithms: arrays, strings, hash tables, trees, graphs, dynamic programming. Practice on LeetCode (250+ problems), HackerRank, or CodeSignal. Focus on patterns: two pointers, sliding window, BFS/DFS, binary search.</p><p>During the interview: clarify requirements, discuss trade-offs verbally, start with a brute force solution, then optimize. Think out loud — interviewers want to see your thought process. Write clean, correct code with proper variable names.</p>',
            ),
            (
                'System Design Interviews',
                '<p>System design questions test architecture skills (for senior roles). Key topics: load balancers, caching (Redis, CDN), databases (SQL vs NoSQL), messaging queues, microservices, and CAP theorem.</p><p>Framework: gather requirements, estimate scale (QPS, storage), design data model, outline high-level architecture, deep dive into components, identify bottlenecks. Use diagrams (excalidraw.com). Common questions: design URL shortener, chat system, Netflix, Twitter.</p>',
            ),
            (
                'Behavioral Interviews',
                '<p>Behavioral questions assess cultural fit and soft skills. Use the STAR method (Situation, Task, Action, Result). Prepare 5-7 stories covering: conflict resolution, failure, leadership, technical challenge, cross-team collaboration.</p><p>Common questions: "Tell me about a time you disagreed with a teammate," "Describe your biggest failure," "Why do you want to work here?" Research the company\'s values and mission beforehand. Prepare thoughtful questions to ask the interviewer.</p>',
            ),
            (
                'Salary Negotiation',
                '<p>Never share your current salary. When asked for expectations, say "I\'m focusing on finding the right fit, but I\'m happy to discuss once we determine if this is a match." Research market rates on Levels.fyi, Glassdoor, and Blind.</p><p>Negotiate after receiving the offer, not before. Negotiate multiple offers against each other. Consider total compensation: base salary, equity, signing bonus, annual bonus, benefits. Get everything in writing. Be professional and gracious throughout.</p>',
            ),
        ],
        [
            ('LeetCode', 'https://leetcode.com', 'Platform for coding interview practice.'),
            ('System Design Interview', 'https://github.com/donnemartin/system-design-primer', 'Comprehensive system design preparation guide.'),
        ],
    )

    build_page(
        'Tech Freelancing Guide',
        'freelancing-guide.html',
        'Start and grow a tech freelancing business — rates, contracts, client acquisition, platforms, and financial management.',
        'Career',
        'fas fa-briefcase',
        [
            (
                'Setting Your Rates',
                "<p>Calculate your rate based on desired annual income, business expenses, taxes, and non-billable time. Formula: (target salary + expenses + profit) / billable hours. Typical tech freelancers charge $75-200/hour depending on expertise and location.</p><p>Start with project-based pricing (easier for clients), then move to hourly or retainer. Increase rates 10-20% annually. Don't compete on price — compete on value and expertise. Have a minimum engagement size to filter tire-kickers.</p>",
            ),
            (
                'Contracts & Legal Essentials',
                '<p>Always use a written contract. Essential clauses: scope of work, deliverables, timeline, payment terms (50% upfront recommended), revision limits, intellectual property transfer, termination clause, and dispute resolution. Use templates from sites like Hello Bonsai or Lawdepot.</p><p>Invoicing: send invoices promptly (weekly or bi-weekly) with clear payment terms (Net 15). Use accounting software: FreshBooks, Wave (free), or Xero. Set aside 25-30% of income for taxes.</p>',
            ),
            (
                'Finding Clients',
                '<p>Build a portfolio website showcasing case studies with measurable results. Use LinkedIn: share expertise via posts, join relevant groups, connect with decision makers. Platforms: Upwork (entry level), Toptal (premium), Gun.io (tech focus), and local networking.</p><p>Referrals are the best source of high-quality clients. Deliver exceptional work, ask for testimonials, and maintain relationships. Offer existing clients a referral fee (10-15% of first project).</p>',
            ),
            (
                'Managing Finances & Growth',
                '<p>Separate personal and business finances — get a business bank account and credit card. Track all expenses for tax deductions: home office, equipment, software, internet, travel, education. Consider forming an LLC or S-corp for liability protection.</p><p>Diversify income: combine project work with retainers, digital products (templates, courses), or consulting. Build an emergency fund of 3-6 months of expenses to handle dry spells. Reinvest in skills development and marketing.</p>',
            ),
        ],
        [
            ('Nomad List Freelance', 'https://nomadlist.com', 'Community and resources for remote freelancers.'),
            ('Freelancers Union', 'https://www.freelancersunion.org', 'Advocacy and resources for freelancers.'),
        ],
    )


    # =========================================================================
    # Accessibility (3)
    # =========================================================================
    build_page(
        'WCAG Web Accessibility Standards',
        'wcag-standards.html',
        'Understand WCAG accessibility standards — POUR principles, conformance levels, success criteria, and compliance testing.',
        'Accessibility',
        'fas fa-universal-access',
        [
            (
                'POUR Principles',
                '<p>WCAG 2.1/2.2 is organized around four principles: <strong>Perceivable</strong> (content must be presentable to senses), <strong>Operable</strong> (UI must be navigable), <strong>Understandable</strong> (content must be clear), and <strong>Robust</strong> (content must work with assistive technologies).</p><p>All success criteria fall under one of these POUR principles. When auditing, check each principle systematically. A resource that fails even one principle is not accessible.</p>',
            ),
            (
                'Conformance Levels: A, AA, AAA',
                '<p><strong>Level A</strong> is the minimum: 30 criteria covering basic accessibility (alt text, keyboard access, captions). <strong>Level AA</strong> is the legal standard (Section 508, ADA, EU Directive): 20 additional criteria (color contrast 4.5:1, headings, labels). <strong>Level AAA</strong> is the gold standard: 23 additional criteria (sign language, extended descriptions, contrast 7:1).</p><p>Most organizations target AA compliance. Some AAA criteria cannot be met for all content types — use reasonable judgment. Document known issues in an accessibility statement.</p>',
            ),
            (
                'Key Success Criteria',
                '<p>Critical success criteria to address first: 1.1.1 Non-text Content (alt text for images), 1.4.3 Contrast (minimum 4.5:1 for text), 2.1.1 Keyboard (all functionality via keyboard), 2.4.1 Bypass Blocks (skip navigation links), 2.4.4 Link Purpose (descriptive link text), 3.3.2 Labels (form input labels), 4.1.2 Name/Role/Value (proper ARIA attributes).</p><p>Use automated tools (axe, WAVE, Lighthouse) for initial audits, but manual testing is essential for many criteria. Screen reader testing catches issues automation misses.</p>',
            ),
            (
                'Compliance Testing & Auditing',
                '<p>Accessibility auditing is a multi-step process: (1) automated scanning with axe DevTools or WAVE, (2) manual keyboard-only navigation, (3) screen reader testing (NVDA + Firefox for most comprehensive), (4) magnification testing at 200%, (5) review against WCAG checklist.</p><p>Document findings with specific element references, WCAG criteria violated, and fix recommendations. Use a severity scale: critical (blocks task), major (significant barrier), minor (inconvenience). Re-test after fixes.</p>',
            ),
        ],
        [
            ('WCAG 2.2 Quick Reference', 'https://www.w3.org/WAI/WCAG22/quickref/', 'Interactive WCAG reference from W3C.'),
            ('WebAIM Contrast Checker', 'https://webaim.org/resources/contrastchecker/', 'Color contrast checking tool.'),
        ],
    )

    build_page(
        'Screen Reader Testing & ARIA',
        'screen-reader-testing.html',
        'Test websites with screen readers — NVDA, VoiceOver, JAWS — and implement ARIA roles, properties, and best practices.',
        'Accessibility',
        'fas fa-universal-access',
        [
            (
                'Major Screen Readers',
                '<p><strong>NVDA</strong> (Windows, free): most popular for testing. Install the open-source version from nvaccess.org. Key shortcuts: <code>NVDA+Down</code> reads current object, <code>NVDA+F7</code> shows element list. <strong>VoiceOver</strong> (macOS/iOS, built-in): enable in System Settings &gt; Accessibility &gt; VoiceOver. <code>VO+A</code> reads web page. <strong>JAWS</strong> (Windows, paid): popular in enterprise and government.</p><p>Test with at least two screen readers across different browsers. NVDA with Firefox is the recommended combination for comprehensive testing. VoiceOver with Safari tests Apple ecosystem compatibility.</p>',
            ),
            (
                'ARIA Roles & Properties',
                '<p>ARIA (Accessible Rich Internet Applications) supplements HTML semantics. Use <code>role</code> attributes to define element purpose: <code>role="navigation"</code>, <code>role="banner"</code>, <code>role="main"</code>. Properties provide extra context: <code>aria-label</code>, <code>aria-describedby</code>, <code>aria-expanded</code>, <code>aria-current="page"</code>.</p><p>First rule of ARIA: don\'t use it if native HTML works. Use <code>&lt;nav&gt;</code> instead of <code>&lt;div role="navigation"&gt;</code>. ARIA is only needed when HTML semantics are insufficient. Test ARIA implementations with actual screen readers.</p>',
            ),
            (
                'Testing Methodologies',
                '<p>Create a test protocol covering: navigation (tab order, skip links), forms (labels, error messages, autocomplete), dynamic content (live regions, announcements), images (alt text, decorative images), and media (captions, transcripts).</p><p>Record issues with: element path, screen reader used, observed behavior, expected behavior, WCAG criteria violated. Use automated + manual + user testing for full coverage. Include people with disabilities in your testing process.</p>',
            ),
        ],
        [
            ('NVDA Screen Reader', 'https://www.nvaccess.org', 'Free open-source screen reader for Windows.'),
            ('ARIA Authoring Practices Guide', 'https://www.w3.org/WAI/ARIA/apg/', 'W3C guide for ARIA design patterns.'),
        ],
    )

    build_page(
        'Accessible Design Patterns',
        'accessible-design-patterns.html',
        'Design accessible interfaces — forms, navigation, modals, color contrast, focus management, and inclusive design principles.',
        'Accessibility',
        'fas fa-universal-access',
        [
            (
                'Accessible Forms',
                '<p>Always associate labels with inputs using <code>&lt;label for="id"&gt;</code> or wrapping input in label. Group related fields with <code>&lt;fieldset&gt;</code> and <code>&lt;legend&gt;</code>. Error messages should be programmatically associated: <code>aria-describedby="error-id"</code>.</p><p>Provide clear instructions, autocomplete attributes (<code>autocomplete="email"</code>), and visible focus indicators. Use <code>aria-required="true"</code> for required fields — don\'t rely solely on asterisks. Test form submission with screen readers.</p>',
            ),
            (
                'Navigation & Menus',
                '<p>Use semantic HTML: <code>&lt;nav&gt;</code> for navigation, <code>&lt;ul&gt;</code> for menu lists, <code>&lt;a&gt;</code> for links. Skip navigation link should be the first focusable element. For dropdown menus, use <code>aria-expanded</code> and <code>aria-controls</code>.</p><p>Ensure keyboard navigation: Tab moves between items, Enter/Space activates, Escape closes dropdowns. Provide visible focus indicators (2-3px outline). Breadcrumbs help orientation: use <code>aria-label="Breadcrumb"</code> and <code>aria-current="page"</code> on current page link.</p>',
            ),
            (
                'Modals & Overlays',
                '<p>Accessible modals: trap focus within the modal while open, close on Escape key, restore focus to trigger element on close, use <code>role="dialog"</code> and <code>aria-modal="true"</code>. Include a descriptive <code>aria-label</code> on the dialog container.</p><p>Consider: show/hide content inline (disclosure widget) instead of a modal when possible. If using a modal, ensure background content is inert (<code>aria-hidden="true"</code>). Test with screen readers to verify announcements.</p>',
            ),
            (
                'Color Contrast & Visual Design',
                "<p>Minimum contrast ratios: 4.5:1 for normal text, 3:1 for large text (18px+ bold or 24px+ regular). Use tools like WebAIM Contrast Checker or Stark for Figma. Don't rely solely on color to convey information — add icons, patterns, or text labels.</p><p>Support dark mode and system preferences via <code>prefers-color-scheme</code> media query. Allow users to zoom to 200% without content loss. Use relative units (rem, em) instead of pixels for text sizing.</p>",
            ),
        ],
        [
            ('Inclusive Design Principles', 'https://inclusivedesignprinciples.org', 'Principles for designing inclusive interfaces.'),
            ('A11y Project Checklist', 'https://www.a11yproject.com/checklist/', 'Accessibility checklist for web developers.'),
        ],
    )


    # =========================================================================
    # General (2)
    # =========================================================================
    build_page(
        'Digital Minimalism Guide',
        'digital-minimalism.html',
        'Reduce digital clutter and improve focus — declutter apps, manage notifications, optimize social media, and build deep work habits.',
        'General',
        'fas fa-book',
        [
            (
                'Decluttering Your Digital Life',
                "<p>Digital minimalism is about aligning your technology use with your values. Start with a 30-day digital declutter: suspend optional technologies, identify what adds real value, then selectively reintroduce what serves you. Delete apps you haven't used in 30 days.</p><p>Organize files with a structured system. Use a single notes app (Obsidian, Notion) for all information. Unsubscribe from marketing emails. Keep desktop clean — zero icons. Maintain a single to-do list system.</p>",
            ),
            (
                'Notification Management',
                '<p>Notifications are the primary source of digital distraction. Disable all non-essential notifications. Allow only time-sensitive notifications from people (calls, messages from family). Batch process emails 2-3 times daily, not push notifications.</p><p>Use Do Not Disturb mode during focus blocks. Turn off badge icons on social media apps. Review notification settings weekly — every app wants your attention; be selective about what gets through.</p>',
            ),
            (
                'Social Media Optimization',
                '<p>Use social media deliberately, not habitually. Unfollow accounts that don\'t add value. Use tools like News Feed Eradicator (shows quotes instead of feed). Set time limits: 15-30 minutes per day for personal use. Delete apps and use browser versions instead.</p><p>Schedule social media time rather than checking impulsively. Post with intention — contribute quality content rather than consuming mindlessly. Consider a "social media sabbath" one day per week.</p>',
            ),
            (
                'Deep Work & Focus Systems',
                '<p>Deep work is the ability to focus without distraction on cognitively demanding tasks. Schedule 2-4 hour deep work blocks in your calendar. Use the Pomodoro Technique (25 min work, 5 min break) as a starting point. Gradually extend focus periods.</p><p>Environment matters: turn off phone, close unnecessary tabs, use noise-canceling headphones. Tools like Freedom or Cold Turkey block distracting sites. Track your focus hours weekly — aim for 4+ hours of deep work daily.</p>',
            ),
        ],
        [
            ('Digital Minimalism by Cal Newport', 'https://www.calnewport.com/books/digital-minimalism/', 'Book on choosing a focused life in a noisy world.'),
            ('Deep Work by Cal Newport', 'https://www.calnewport.com/books/deep-work/', 'Rules for focused success in a distracted world.'),
        ],
    )

    build_page(
        'Personal Knowledge Management',
        'knowledge-management.html',
        'Build a personal knowledge management system — note-taking methods, PARA, Zettelkasten, and knowledge base tools.',
        'General',
        'fas fa-book',
        [
            (
                'Note-Taking Systems',
                '<p>A PKM system captures, organizes, and retrieves knowledge. The <strong>Zettelkasten</strong> method (slip box) creates atomic notes linked by connections. Each note is a single idea with a unique ID, content, and links to related notes. Over time, this builds a web of interconnected knowledge.</p><p>The <strong>Cornell Method</strong> divides notes into cues (left column), notes (right column), and summary (bottom). Best for lectures and meetings. The <strong>Outline Method</strong> uses hierarchical headings — good for structured content. Experiment to find what sticks.</p>',
            ),
            (
                'PARA Method',
                '<p>PARA (Projects, Areas, Resources, Archives) by Tiago Forte organizes all digital information into four categories. <strong>Projects</strong>: short-term outcomes with deadlines. <strong>Areas</strong>: long-term responsibilities without deadlines. <strong>Resources</strong>: topics of interest. <strong>Archives</strong>: inactive items from other categories.</p><p>PARA works across any tool — folders, tags, or databases. The key insight: most organizing effort is wasted. PARA gives you a single system that captures everything with minimal friction. Review and archive quarterly.</p>',
            ),
            (
                'Progressive Summarization',
                '<p>Progressive summarization is a five-layer note refinement technique. Layer 1: original notes (capture). Layer 2: bold passages (what\'s important). Layer 3: highlighted passages (what\'s most important). Layer 4: executive summary (one-line overview). Layer 5: remix (original content created from the note).</p><p>Not every note needs all five layers. Only summarize notes you reference. This "just-in-time" approach prevents over-organizing while making important information discoverable. Use highlighting and formatting consistently.</p>',
            ),
            (
                'Tools & Workflows',
                '<p>Popular PKM tools: Obsidian (local, markdown, graph view, plugins), Notion (database-driven, collaborative, flexible), Roam Research (outliner, block references, daily notes), Logseq (open-source outliner, markdown). Choose based on your thinking style — linear vs networked.</p><p>Build a daily note routine: morning (plan the day), capture throughout (fleeting notes), evening (review and organize). Weekly review: process inbox, update projects, refine notes. Monthly: archive completed projects, update areas.</p>',
            ),
        ],
        [
            ('Building a Second Brain by Tiago Forte', 'https://www.buildingasecondbrain.com', 'Book on the PARA method and progressive summarization.'),
            ('Zettelkasten Method', 'https://zettelkasten.de', 'Comprehensive guide to the Zettelkasten note-taking system.'),
        ],
    )

if __name__ == "__main__":
    os.makedirs(TUTS, exist_ok=True)
    generate_part3()
