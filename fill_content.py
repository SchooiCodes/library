#!/usr/bin/env python3
"""Fill in rich content for all 50 generated tutorial pages."""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
TUTS = os.path.join(BASE, "tutorials")

def replace_section(body, section_id, content_html):
    pattern = rf'(<h2 id="{re.escape(section_id)}">.*?</h2>\n)<p>.*?</p>'
    return re.sub(pattern, lambda m: m.group(1) + content_html, body, count=1, flags=re.DOTALL)

def fill_file(filename, updates):
    path = os.path.join(TUTS, filename)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    for sid, html_body in updates.items():
        old = content
        content = replace_section(content, sid, html_body)
        if content == old:
            print(f"  [WARN] {filename}: section #{sid} not found")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Filled: {filename} ({len(updates)} sections)")

# ======================================================================
# CONTENT FOR ALL 50 TUTORIALS
# ======================================================================

# 1. Active Recall & Spaced Repetition
fill_file("active-recall.html", {
    "what-is-active-recall":
        '<p><strong>Active Recall</strong> is a learning technique where you actively retrieve information from memory rather than passively reviewing it. Instead of re-reading notes or highlighting textbooks, you quiz yourself on the material.</p>'
        '<p>Research by Roediger &amp; Karpicke (2006) demonstrates that active recall produces significantly better long-term retention compared to passive study methods.</p>'
        '<p><strong>Key principles:</strong></p><ul><li>Retrieval strengthens neural pathways</li><li>The struggle to recall builds durable memory</li><li>Testing yourself is more effective than re-reading</li><li>Each recall attempt reinforces the memory trace</li></ul>',
    "what-is-spaced-repetition":
        '<p><strong>Spaced Repetition</strong> schedules reviews at increasing intervals based on your forgetting curve. First described by Hermann Ebbinghaus in 1885, this technique exploits the spacing effect.</p>'
        '<p><strong>How it works:</strong></p><ol><li>Learn new material</li><li>Review after a short interval (1 day)</li><li>If remembered, increase interval (3 days, 1 week, 1 month)</li><li>If forgotten, reset to shorter interval</li></ol>'
        '<p>Software like <strong>Anki</strong> automates this with the SM-2 algorithm, assigning difficulty ratings to adjust intervals.</p>',
    "anki-setup":
        '<p><strong>Anki</strong> is the most popular spaced repetition app. Free on desktop and Android, paid on iOS.</p>'
        '<p><strong>Installation:</strong></p><pre><code># Linux\nsudo apt install anki\n\n# macOS\nbrew install --cask anki\n\n# Windows: https://apps.ankiweb.net</code></pre>'
        '<p><strong>Workflow:</strong></p><ol><li>Create a deck</li><li>Add cards (front: question, back: answer)</li><li>Review daily</li><li>Rate: Again, Hard, Good, Easy</li></ol>',
    "study-workflow":
        '<p>Combine active recall and spaced repetition into a daily workflow:</p>'
        '<ol><li><strong>Preview (5 min)</strong> \u2014 Skim the material</li>'
        '<li><strong>Read actively (25 min)</strong> \u2014 Take notes, create questions</li>'
        '<li><strong>Make cards (10 min)</strong> \u2014 Create Anki cards immediately</li>'
        '<li><strong>Review daily (15-30 min)</strong> \u2014 Do Anki reviews</li>'
        '<li><strong>Practice (20 min)</strong> \u2014 Apply with exercises</li>'
        '<li><strong>Teach (10 min)</strong> \u2014 Feynman technique</li></ol>',
    "pomodoro":
        '<p>The <strong>Pomodoro Technique</strong> uses timed work intervals with breaks:</p>'
        '<ul><li>25 min focused study</li><li>5 min break</li><li>After 4, take 15-30 min break</li></ul>'
        '<p><strong>Tools:</strong> Forest, Focusmate, Be Focused, Pomofocus</p>',
})

# 2. Note-Taking Methods
fill_file("note-taking-methods.html", {
    "cornell-method":
        '<p>The <strong>Cornell Method</strong> divides your page into sections: cue column (left), notes (right), and summary (bottom). Developed at Cornell University, it encourages active engagement during lectures.</p>'
        '<p><strong>How to use:</strong></p><ol><li>Take notes in the right column during class</li><li>Write cues/questions in the left column after class</li><li>Cover the right side and quiz yourself using cues</li><li>Write a 2-3 sentence summary at the bottom</li></ol>',
    "zettelkasten-(slip-box)":
        '<p>The <strong>Zettelkasten</strong> method, developed by Niklas Luhmann, uses atomic notes linked by connections. Each note contains one idea and links to related notes.</p>'
        '<p><strong>Principles:</strong> Atomicity (one idea per note), Autonomy (self-contained), Connection (link notes), Accumulation (build over time).</p>'
        '<p><strong>Digital tools:</strong> Obsidian, Roam Research, Logseq, Notion.</p>',
    "outline-method":
        '<p>The <strong>Outline Method</strong> uses hierarchical bullet points to organize information. Best for well-structured lectures and textbooks with clear headings.</p>'
        '<p><strong>Structure:</strong></p><pre><code>Main Topic\n  \u2514 Subtopic 1\n       \u2514 Key point\n            \u2514 Detail / example</code></pre>'
        '<p>Easy to create and review, but difficult for fast-paced lectures.</p>',
    "mind-mapping":
        '<p><strong>Mind Maps</strong> use a central idea with branching subtopics, creating a radial visual structure. Best for brainstorming and creative thinking.</p>'
        '<p><strong>How to create:</strong></p><ol><li>Write the main topic in the center</li><li>Draw branches for each major subtopic</li><li>Add sub-branches for details</li><li>Use colors and images</li></ol>'
        '<p><strong>Tools:</strong> MindMeister, XMind, FreeMind, draw.io</p>',
    "digital-note-taking-tools":
        '<table><thead><tr><th>Tool</th><th>Best For</th><th>Platform</th></tr></thead><tbody>'
        '<tr><td>Notion</td><td>All-in-one notes, databases</td><td>Web, Win, Mac, iOS, Android</td></tr>'
        '<tr><td>Obsidian</td><td>Zettelkasten, local-first</td><td>Win, Mac, Linux, iOS, Android</td></tr>'
        '<tr><td>OneNote</td><td>Free-form, tablet drawing</td><td>Win, Mac, iOS, Android, Web</td></tr>'
        '<tr><td>Logseq</td><td>Outliner, open-source</td><td>Win, Mac, Linux, iOS, Android</td></tr>'
        '<tr><td>Roam Research</td><td>Bi-directional linking</td><td>Web, iOS, Android</td></tr>'
        '</tbody></table>',
})

# 3. Focus & Productivity Tools
fill_file("focus-productivity-tools.html", {
    "time-management-methods":
        '<p><strong>Eisenhower Matrix</strong> \u2014 Categorize tasks by urgency/importance: Do First (urgent+important), Schedule (not urgent+important), Delegate (urgent+not important), Eliminate (neither).</p>'
        '<p><strong>Time Blocking</strong> \u2014 Schedule every hour of your day. Used by Elon Musk and Bill Gates.</p>'
        '<p><strong>GTD (Getting Things Done)</strong> \u2014 Capture, clarify, organize, reflect, engage.</p>',
    "distraction-blocking-tools":
        '<ul><li><strong>Cold Turkey</strong> \u2014 Blocks websites/apps, cannot be bypassed</li>'
        '<li><strong>Freedom</strong> \u2014 Cross-platform block lists</li>'
        '<li><strong>SelfControl</strong> \u2014 Free macOS, blocks by IP</li>'
        '<li><strong>LeechBlock</strong> \u2014 Free Firefox/Chrome extension</li>'
        '<li><strong>/etc/hosts</strong> \u2014 System-level blocking: <code>echo \'127.0.0.1 reddit.com\' >> /etc/hosts</code></li></ul>',
    "focus-and-deep-work-apps":
        '<ul><li><strong>Forest</strong> \u2014 Gamified Pomodoro timer</li>'
        '<li><strong>Focusmate</strong> \u2014 Virtual co-working accountability</li>'
        '<li><strong>Brain.fm</strong> \u2014 AI-generated focus music</li>'
        '<li><strong>Endel</strong> \u2014 Adaptive soundscapes</li>'
        '<li><strong>Noisli</strong> \u2014 Background sounds for concentration</li></ul>',
    "habit-tracking":
        '<ul><li><strong>Habitica</strong> \u2014 Gamified habit tracker (RPG-style)</li>'
        '<li><strong>Streaks</strong> \u2014 iOS daily streak tracker</li>'
        '<li><strong>Loop Habit Tracker</strong> \u2014 Free Android app</li></ul>'
        '<p><strong>The 2-minute rule:</strong> If a habit takes less than 2 minutes, do it immediately.</p>',
    "distraction-free-writing":
        '<ul><li><strong>iA Writer</strong> \u2014 Minimalist with focus mode</li>'
        '<li><strong>Typora</strong> \u2014 Markdown with live preview</li>'
        '<li><strong>FocusWriter</strong> \u2014 Full-screen with daily goals</li>'
        '<li><strong>WriteMonkey</strong> \u2014 Windows zen writing</li></ul>'
        '<p><strong>Pro tip:</strong> Use vim/nvim with :Goyo for distraction-free terminal writing.</p>',
})

# 4. Anki Customization
fill_file("anki-customization.html", {
    "add-ons-and-plugins":
        '<p>Anki has a rich add-on ecosystem. Access via Tools > Add-ons > Get Add-ons. Paste the code to install.</p>'
        '<p><strong>Essential add-ons:</strong></p><ul><li><strong>AnkiConnect (2055492159)</strong> \u2014 Control Anki from external apps</li>'
        '<li><strong>Image Occlusion Enhanced (1374772155)</strong> \u2014 Hide parts of images</li>'
        '<li><strong>Review Heatmap (1771074083)</strong> \u2014 Visualize review activity</li>'
        '<li><strong>AwesomeTTS (814349176)</strong> \u2014 Text-to-speech for cards</li>'
        '<li><strong>FSRS Helper (759844606)</strong> \u2014 Free Spaced Repetition Scheduler</li></ul>',
    "card-styling-with-css":
        '<p>Customize card appearance with CSS in the card editor:</p>'
        '<pre><code>/* Example card styling */\n.card {\n font-family: "Inter", sans-serif;\n font-size: 20px;\n text-align: center;\n color: #333;\n background-color: #fafafa;\n}\n\nimg {\n max-width: 80%;\n border-radius: 8px;\n}</code></pre>',
    "fsrs-scheduler":
        '<p><strong>FSRS (Free Spaced Repetition Scheduler)</strong> is a modern alternative to the Anki SM-2 algorithm. It uses machine learning to optimize review intervals.</p>'
        '<p>Enable in Deck Options > FSRS. Recommended parameters: desired retention 0.85-0.90.</p>'
        '<p>FSRS learns your memory patterns and adapts intervals for optimal retention with fewer daily reviews.</p>',
    "sync-and-collaboration":
        '<p>Sync your collection across devices using AnkiWeb:</p>'
        '<pre><code># Create account: https://ankiweb.net\n# Sync from Anki: click sync button (cloud icon)\n# AnkiDroid: Settings > AnkiWeb account</code></pre>'
        '<p><strong>Shared decks:</strong> Browse community decks on AnkiWeb shared deck page. Filter by subject, rating, and language.</p>',
    "statistics-and-review":
        '<p>Anki provides detailed statistics: review count, retention rate, time per card, card maturity breakdown.</p>'
        '<p>Key metrics to watch: mature retention (ideally >90%), cards due tomorrow, daily review load. Use the Review Heatmap add-on to maintain streaks.</p>',
})

# 5. Digital Zettelkasten
fill_file("digital-zettelkasten.html", {
    "setting-up-obsidian":
        '<p><strong>Obsidian</strong> is a local-first knowledge base that uses Markdown files. It is free for personal use.</p>'
        '<p><strong>Setup:</strong></p><ol><li>Download from https://obsidian.md</li><li>Create a vault (folder of markdown files)</li><li>Enable "Linking" in Settings > Files & Links</li></ol>',
    "atomic-notes":
        '<p>Each note should contain one idea, written in your own words. Follow the Zettelkainen principle of atomicity.</p>'
        '<p><strong>Structure:</strong></p><pre><code># Note Title (date)\n\n## Source\nBook: Atomic Habits, p.45\n\n## Idea\nHabits are the compound interest of self-improvement.\n\n## Links\n[[Habit Stacking]] [[Identity-Based Habits]]</code></pre>',
    "links-and-graph-view":
        '<p>Obsidian\'s graph view visualizes connections between notes. Use <code>[[double brackets]]</code> to link notes.</p>'
        '<p><strong>Tips:</strong> Use the Local Graph for focused views, filter by tags, and use "Backlinks" panel to see what links to the current note.</p>',
    "templates-and-plugins":
        '<p><strong>Core plugins to enable:</strong> Templates, Daily notes, Graph view, Backlinks, Command palette.</p>'
        '<p><strong>Community plugins:</strong> Dataview (query notes), Calendar, Kanban, Excalidraw (drawing).</p>',
    "daily-notes-workflow":
        '<p>Create a daily note template with: date, tasks, meetings, random thoughts. Link daily notes to projects and topics.</p>'
        '<p><strong>Workflow:</strong> Open daily note each morning. Capture ideas throughout the day. Process into permanent notes weekly.</p>',
})

# 6. Time Management Guide
fill_file("time-management-guide.html", {
    "eisenhower-matrix":
        '<p>The <strong>Eisenhower Matrix</strong> (also called the Urgent-Important Matrix) helps prioritize tasks:</p>'
        '<ul><li><strong>Quadrant 1 (Do First):</strong> Urgent + Important \u2014 Crises, deadlines</li>'
        '<li><strong>Quadrant 2 (Schedule):</strong> Not Urgent + Important \u2014 Planning, learning, exercise</li>'
        '<li><strong>Quadrant 3 (Delegate):</strong> Urgent + Not Important \u2014 Interruptions, meetings</li>'
        '<li><strong>Quadrant 4 (Eliminate):</strong> Not Urgent + Not Important \u2014 Time wasters</li></ul>'
        '<p>Spend most of your time in Quadrant 2 for long-term success.</p>',
    "time-blocking":
        '<p><strong>Time Blocking</strong> means scheduling every hour of your day in advance. This prevents context switching and ensures deep work time.</p>'
        '<p><strong>Example day:</strong></p><ul><li>7-9 AM: Deep work (most important task)</li><li>9-10 AM: Email and messages</li><li>10-12 PM: Meetings</li><li>12-1 PM: Lunch break</li>'
        '<li>1-3 PM: Creative work</li><li>3-4 PM: Admin tasks</li><li>4-5 PM: Planning tomorrow</li></ul>',
    "gtd-method":
        '<p><strong>Getting Things Done (GTD)</strong> by David Allen has 5 steps:</p><ol><li><strong>Capture</strong> \u2014 Collect everything in an inbox</li>'
        '<li><strong>Clarify</strong> \u2014 Process each item: what is it? is it actionable?</li>'
        '<li><strong>Organize</strong> \u2014 Put into lists: Next Actions, Waiting, Someday/Maybe, Calendar</li>'
        '<li><strong>Reflect</strong> \u2014 Weekly review to update lists</li>'
        '<li><strong>Engage</strong> \u2014 Work through Next Actions list by context</li></ol>',
    "weekly-reviews":
        '<p>A <strong>weekly review</strong> is the cornerstone of GTD and time management. Set aside 30-60 minutes each week:</p>'
        '<ol><li>Process all inboxes to zero</li><li>Review next actions lists</li><li>Check calendar for upcoming events</li><li>Review Someday/Maybe list</li><li>Plan the upcoming week</li><li>Clear your desk and digital space</li></ol>',
    "digital-calendars":
        '<p><strong>Recommended calendar tools:</strong></p><ul><li><strong>Google Calendar</strong> \u2014 Free, integrates everywhere</li>'
        '<li><strong>Fantastical</strong> \u2014 Mac/iOS premium calendar</li><li><strong>Notion Calendar</strong> \u2014 Integrated with Notion workspaces</li>'
        '<li><strong>Outlook Calendar</strong> \u2014 Best for corporate environments</li></ul>'
        '<p><strong>Pro tip:</strong> Color-code calendars by category (work, personal, health, learning).</p>',
})

# 7. Rust Basics
fill_file("rust-basics.html", {
    "what-is-rust?":
        '<p><strong>Rust</strong> is a systems programming language focused on safety, speed, and concurrency. Developed by Mozilla (now Rust Foundation), it guarantees memory safety without a garbage collector.</p>'
        '<p>Rust has been the <strong>most loved language</strong> on Stack Overflow surveys for years. It is used by Microsoft, Google, Amazon, and in the Linux kernel.</p>',
    "installation":
        '<pre><code># Install rustup (recommended)\ncurl --proto \'=https\' --tlsv1.2 -sSf https://sh.rustup.rs | sh\n\n# Or via package manager\nsudo apt install rustc cargo\n\n# Verify\nrustc --version\ncargo --version</code></pre>',
    "ownership-and-borrowing":
        '<p><strong>Three rules of ownership:</strong></p><ol><li>Each value has one owner</li><li>Only one owner at a time</li><li>When owner goes out of scope, value is dropped</li></ol>'
        '<pre><code>let s1 = String::from("hello");\nlet s2 = s1;  // s1 is MOVED to s2\n// println!("{s1}");  // ERROR</code></pre>',
    "structs-enums-and-pattern-matching":
        '<pre><code>struct User {\n    username: String,\n    email: String,\n    active: bool,\n}\n\nenum Message {\n    Quit,\n    Move { x: i32, y: i32 },\n    Write(String),\n}\n\nmatch msg {\n    Message::Quit => println!("quit"),\n    Message::Move { x, y } => println!("move ({x}, {y})"),\n    Message::Write(text) => println!("{text}"),\n}</code></pre>',
    "error-handling-with-result":
        '<pre><code>fn read_file(path: &str) -> Result&lt;String, std::io::Error&gt; {\n    let mut file = File::open(path)?;\n    let mut contents = String::new();\n    file.read_to_string(&mut contents)?;\n    Ok(contents)\n}</code></pre>',
})

# 8. Go Basics
fill_file("go-basics.html", {
    "what-is-go?":
        '<p><strong>Go</strong> (Golang) is a compiled, statically-typed language created at Google by Robert Griesemer, Rob Pike, and Ken Thompson. It combines C-like performance with Python-like readability.</p>'
        '<p>Key features: fast compilation, built-in concurrency (goroutines), garbage collection, rich standard library.</p>',
    "installation-and-hello-world":
        '<pre><code># Linux\nsudo apt install golang-go\n\n# macOS\nbrew install go\n\n# hello.go\npackage main\nimport "fmt"\nfunc main() {\n    fmt.Println("Hello, Go!")\n}\n\ngo run hello.go</code></pre>',
    "basic-syntax-and-types":
        '<pre><code>name := "Alice"\nage := 30\nvar height float64 = 5.8\n\nnumbers := []int{1, 2, 3, 4, 5}\nscores := map[string]int{"Alice": 95, "Bob": 87}\n\nfor i, num := range numbers {\n    fmt.Printf("%d: %d\\n", i, num)\n}</code></pre>',
    "goroutines-and-channels":
        '<pre><code>func worker(id int, jobs &lt;-chan int, results chan&lt;- int) {\n    for job := range jobs {\n        time.Sleep(time.Second)\n        results &lt;- job * 2\n    }\n}\n\njobs := make(chan int, 10)\nfor w := 1; w &lt;= 3; w++ {\n    go worker(w, jobs, results)\n}</code></pre>',
    "interfaces":
        '<pre><code>type Shape interface {\n    Area() float64\n}\n\ntype Circle struct { Radius float64 }\nfunc (c Circle) Area() float64 { return 3.14 * c.Radius * c.Radius }</code></pre>',
})

# 9. C++ Basics
fill_file("cpp-basics.html", {
    "what-is-c++?":
        '<p><strong>C++</strong> is a powerful systems programming language created by Bjarne Stroustrup as an extension of C. Used in game engines, operating systems, browsers, and high-frequency trading.</p>',
    "setup-and-first-program":
        '<pre><code>// hello.cpp\n#include &lt;iostream&gt;\nint main() {\n    std::cout &lt;&lt; "Hello, C++!" &lt;&lt; std::endl;\n    return 0;\n}\n\ng++ -std=c++20 -o hello hello.cpp\n./hello</code></pre>',
    "pointers-and-memory":
        '<pre><code>int value = 42;\nint* ptr = &amp;value;\ncout &lt;&lt; *ptr;  // Dereference: 42\n\n// Smart pointers (modern C++)\nauto smart = std::make_unique&lt;int&gt;(100);</code></pre>',
    "classes-and-oop":
        '<pre><code>class Animal {\npublic:\n    virtual void speak() const = 0;\n};\nclass Dog : public Animal {\n    void speak() const override { cout &lt;&lt; "Woof!"; }\n};</code></pre>',
    "stl-and-modern-c++":
        '<pre><code>std::vector&lt;int&gt; nums = {3, 1, 4, 1, 5};\nstd::sort(nums.begin(), nums.end());\n\n// C++11 range-based for\nfor (int n : nums) cout &lt;&lt; n &lt;&lt; " ";</code></pre>',
})

# 10. Advanced SQL
fill_file("sql-advanced.html", {
    "window-functions":
        '<pre><code>SELECT name, department, salary,\n    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) as rank\nFROM employees;\n\n-- Running total\nSELECT date, amount,\n    SUM(amount) OVER (ORDER BY date) as running_total\nFROM transactions;</code></pre>',
    "common-table-expressions":
        '<pre><code>WITH sales_summary AS (\n    SELECT category, SUM(amount) as total_sales\n    FROM orders GROUP BY category\n)\nSELECT * FROM sales_summary ORDER BY total_sales DESC;</code></pre>',
    "indexing-strategies":
        '<pre><code>-- B-tree index\nCREATE INDEX idx_email ON users(email);\n\n-- Composite index (order matters!)\nCREATE INDEX idx_state_city ON addresses(state, city);\n\n-- Partial index\nCREATE INDEX idx_active ON users(email) WHERE active = true;</code></pre>',
    "query-optimization":
        '<pre><code>-- Use EXISTS instead of IN\nSELECT * FROM customers c\nWHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.id);\n\n-- Avoid functions in WHERE\nWHERE created_at >= \'2024-01-01\' AND created_at &lt; \'2024-01-02\'</code></pre>',
    "advanced-joins":
        '<pre><code>-- Lateral join\nSELECT c.name, latest.total as last_order\nFROM customers c\nLEFT JOIN LATERAL (\n    SELECT total FROM orders\n    WHERE customer_id = c.id\n    ORDER BY created_at DESC LIMIT 1\n) latest ON true;</code></pre>',
})

# 11. API Design Best Practices
fill_file("api-design-best-practices.html", {
    "restful-design-principles":
        '<p><strong>REST</strong> principles by Roy Fielding: resources as nouns (/users), HTTP verbs (GET/POST/PUT/DELETE), stateless requests, uniform interface.</p>'
        '<pre><code>GET    /api/v1/users          # List\nPOST   /api/v1/users          # Create\nGET    /api/v1/users/:id      # Read\nPUT    /api/v1/users/:id      # Replace\nDELETE /api/v1/users/:id      # Delete</code></pre>',
    "http-status-codes":
        '<table><tr><th>Code</th><th>Meaning</th></tr><tr><td>200</td><td>OK</td></tr><tr><td>201</td><td>Created</td></tr><tr><td>204</td><td>No Content</td></tr><tr><td>400</td><td>Bad Request</td></tr><tr><td>401</td><td>Unauthorized</td></tr><tr><td>403</td><td>Forbidden</td></tr><tr><td>404</td><td>Not Found</td></tr><tr><td>429</td><td>Too Many Requests</td></tr><tr><td>500</td><td>Internal Server Error</td></tr></table>',
    "api-versioning":
        '<p>Three approaches: URL-based (/v1/), header-based (Accept: version=2), query param (?version=2). URL-based is most common and easiest to route.</p>',
    "authentication-and-authorization":
        '<ul><li><strong>API Keys</strong> \u2014 Simple, passed in header</li><li><strong>JWT</strong> \u2014 Self-contained tokens, stateless</li><li><strong>OAuth 2.0</strong> \u2014 Delegated authorization</li><li><strong>Basic Auth</strong> \u2014 Only over HTTPS</li></ul>',
    "rate-limiting":
        '<p>Common strategies: Token bucket (allow bursts), Leaky bucket (smooth requests), Fixed window, Sliding window.</p><pre><code>X-RateLimit-Limit: 100\nX-RateLimit-Remaining: 87\nX-RateLimit-Reset: 1625123456</code></pre>',
    "api-documentation":
        '<p><strong>OpenAPI/Swagger</strong> is the industry standard. Others: Postman Collections, GraphQL Introspection, Stoplight.</p>',
})

# 12. WebSockets
fill_file("websockets-guide.html", {
    "what-are-websockets?":
        '<p><strong>WebSockets</strong> (RFC 6455) provide full-duplex communication over a single TCP connection. Unlike HTTP request-response, both client and server can send messages anytime.</p>'
        '<p>Uses: chat apps, live notifications, real-time dashboards, multiplayer games, collaborative editing.</p>',
    "websocket-api-(browser)":
        '<pre><code>const ws = new WebSocket("wss://echo.websocket.org");\nws.onopen = () => ws.send("Hello");\nws.onmessage = (e) => console.log("Received:", e.data);\nws.onclose = () => console.log("Disconnected");</code></pre>',
    "websocket-server-(node.js)":
        '<pre><code>const WebSocket = require("ws");\nconst wss = new WebSocket.Server({ port: 8080 });\nwss.on("connection", (ws) => {\n    ws.on("message", (data) => {\n        wss.clients.forEach(c => c.send(data));\n    });\n});</code></pre>',
    "socket.io":
        '<pre><code>const { Server } = require("socket.io");\nconst io = new Server(3000);\nio.on("connection", (socket) => {\n    socket.join("room-1");\n    io.to("room-1").emit("message", {text: "Welcome!"});\n});</code></pre>',
    "webrtc":
        '<p><strong>WebRTC</strong> enables P2P audio, video, and data sharing. Uses: MediaStream (camera/mic), RTCPeerConnection (calling), RTCDataChannel (file transfer).</p>'
        '<p>Libraries: SimplePeer, PeerJS, LiveKit.</p>',
})

# 13. Software Testing
fill_file("testing-101.html", {
    "the-testing-pyramid":
        '<p>The <strong>Testing Pyramid</strong> (Mike Cohn): Unit tests (~70%, fast, isolated), Integration tests (~20%, component interaction), E2E tests (~10%, user flows).</p>',
    "unit-testing":
        '<pre><code>// Python with pytest\ndef test_add():\n    assert add(2, 3) == 5\n\ndef test_divide_by_zero():\n    with pytest.raises(ValueError):\n        divide(1, 0)</code></pre>',
    "mocking-and-stubs":
        '<p><strong>Mock</strong> \u2014 Simulates real objects. <strong>Stub</strong> \u2014 Returns predefined responses. <strong>Fake</strong> \u2014 Simplified implementation. <strong>Spy</strong> \u2014 Wraps real object.</p>',
    "integration-testing":
        '<p>Test database queries, API endpoints, external services with real or sandboxed dependencies. Use fixtures for test data.</p>',
    "e2e-testing":
        '<pre><code>// Playwright\ntest("user can log in", async ({ page }) => {\n    await page.goto("https://example.com/login");\n    await page.fill("#email", "user@example.com");\n    await page.click("button[type=\'submit\']");\n    await expect(page.locator(".dashboard")).toBeVisible();\n});</code></pre>',
    "ci-cd-integration":
        '<p>Run unit tests on every commit, integration on PRs, E2E before deployment. Tools: GitHub Actions, Jenkins, GitLab CI.</p>',
})

# 14. CI/CD with Jenkins
fill_file("ci-cd-jenkins.html", {
    "jenkins-overview":
        '<p>Jenkins is the leading open-source automation server for CI/CD. Supports thousands of plugins for building, deploying, and automating any project.</p>',
    "installation":
        '<pre><code># Docker\nsudo docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts\n\n# Access: http://localhost:8080\n# Initial password:\nsudo cat /var/lib/jenkins/secrets/initialAdminPassword</code></pre>',
    "declarative-pipeline":
        '<pre><code>pipeline {\n    agent any\n    stages {\n        stage("Build") { steps { sh "npm ci && npm run build" } }\n        stage("Test") { steps { sh "npm run test" } }\n        stage("Deploy") { when { branch "main" }; steps { sh "./deploy.sh" } }\n    }\n}</code></pre>',
    "distributed-builds":
        '<p>Scale with agents: permanent agents (VMs), cloud agents (AWS EC2, Kubernetes), Docker agents.</p>',
    "essential-plugins":
        '<p>Git, Pipeline, Blue Ocean, Docker Pipeline, Kubernetes, Credentials Binding, Email Extension, SonarQube.</p>',
})

# 15. Nginx Reverse Proxy
fill_file("nginx-reverse-proxy.html", {
    "what-is-a-reverse-proxy?":
        '<p>A <strong>reverse proxy</strong> sits in front of backend servers, forwarding client requests. Benefits: load balancing, TLS termination, caching, compression, security.</p>',
    "basic-reverse-proxy-setup":
        '<pre><code>server {\n    listen 80;\n    server_name example.com;\n    location / {\n        proxy_pass http://localhost:3000;\n        proxy_set_header Host $host;\n        proxy_set_header X-Real-IP $remote_addr;\n    }\n}</code></pre>',
    "load-balancing-methods":
        '<p>Round Robin (default), Least Connections, IP Hash (sticky sessions), Weighted. Configure with upstream blocks.</p>',
    "tls-termination":
        '<p>Use certbot/Let\'s Encrypt for free TLS certificates. Enable HTTP/2, set strong ciphers, enable HSTS.</p>',
    "caching-static-content":
        '<p>Cache static assets with expires headers. Use proxy_cache for dynamic content caching. Set Cache-Control: public, immutable for versioned assets.</p>',
})

# 16. Terraform
fill_file("terraform-basics.html", {
    "what-is-terraform?":
        '<p>Terraform by HashiCorp is an infrastructure-as-code tool supporting 2000+ providers (AWS, Azure, GCP, Kubernetes, Cloudflare). Declarative HCL syntax, idempotent, plan/apply workflow.</p>',
    "hcl-syntax-and-resources":
        '<pre><code>resource "aws_instance" "web" {\n    ami           = "ami-0c55b159cbfafe1f0"\n    instance_type = "t2.micro"\n    tags = { Name = "WebServer" }\n}</code></pre>',
    "state-management":
        '<p>State maps config to real resources. Use remote state (S3) for teams. Never edit state files manually. Use terraform state commands.</p>',
    "modules":
        '<p>Modules organize infrastructure into reusable components. Use the Terraform Registry for community modules.</p>',
    "workspaces":
        '<p>Workspaces manage different environments (dev, staging, prod). Use workspace-specific variables and state files.</p>',
})

# 17. Kubernetes Pods, Services, Deployments
fill_file("kubernetes-pods-services-deployments.html", {
    "core-kubernetes-objects":
        '<p><strong>Pod</strong> \u2014 Smallest deployable unit. <strong>Service</strong> \u2014 Stable network endpoint. <strong>Deployment</strong> \u2014 Declarative updates. <strong>ConfigMap</strong> \u2014 Non-sensitive config. <strong>Secret</strong> \u2014 Sensitive data.</p>',
    "pods":
        '<pre><code>apiVersion: v1\nkind: Pod\nmetadata:\n  name: nginx-pod\n  labels:\n    app: nginx\nspec:\n  containers:\n  - name: nginx\n    image: nginx:1.25\n    ports:\n    - containerPort: 80</code></pre>',
    "deployments":
        '<pre><code>apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: nginx-deployment\nspec:\n  replicas: 3\n  selector:\n    matchLabels:\n      app: nginx\n  template:\n    metadata:\n      labels:\n        app: nginx\n    spec:\n      containers:\n      - name: nginx\n        image: nginx:1.25</code></pre>',
    "services":
        '<p><strong>ClusterIP</strong> (internal), <strong>NodePort</strong> (on each node), <strong>LoadBalancer</strong> (cloud LB), <strong>ExternalName</strong> (DNS alias).</p>',
    "ingress-controller":
        '<p>Ingress routes HTTP/S traffic to services. Popular controllers: nginx-ingress, traefik, HAProxy, AWS ALB.</p>',
    "configmaps-and-secrets":
        '<p>ConfigMaps store non-sensitive config (env vars, config files). Secrets store sensitive data (base64 encoded). Both are mounted as volumes or env vars.</p>',
})

# 18. Ansible Playbooks Deep Dive
fill_file("ansible-playbooks-deep-dive.html", {
    "advanced-playbook-patterns":
        '<p>Use handlers for service restarts, tags for selective execution, includes/dynamic imports for modular playbooks.</p>',
    "dynamic-inventory":
        '<p>Dynamic inventories fetch hosts from cloud providers, CMDB, or scripts. Use aws_ec2, gcp_compute, or custom inventory scripts.</p>',
    "ansible-collections":
        '<p>Collections bundle playbooks, roles, modules, and plugins. Install from Ansible Galaxy with ansible-galaxy collection install.</p>',
    "awx---ansible-tower":
        '<p><strong>AWX</strong> is the open-source upstream of Ansible Tower. Provides web UI, RBAC, job scheduling, REST API, and workflow templates.</p>',
    "performance-optimization":
        '<p>Set forks=20, enable pipelining=True, use fact caching, choose strategy=free for faster parallel execution.</p>',
})

# 19. Linux Process Management
fill_file("linux-process-management.html", {
    "process-basics":
        '<p>A process is a running instance of a program, identified by PID. View with ps aux, top, htop, pstree. Process states: Running, Sleeping, Stopped, Zombie.</p>',
    "process-signals":
        '<p>Signals are OS-level notifications to processes: SIGTERM (15), SIGKILL (9), SIGHUP (1), SIGINT (2), SIGSTOP (19), SIGCONT (18).</p>',
    "priority-and-nice-values":
        '<p>Nice values range -20 (highest priority) to +19 (lowest). Default is 0. Use nice/renice to adjust. Real-time priorities use chrt.</p>',
    "managing-services-with-systemd":
        '<p>systemctl start/stop/restart/reload/enable/disable services. View logs with journalctl -u service-name.</p>',
    "cgroups":
        '<p>Control groups limit resource usage (CPU, memory, I/O) for process groups. Use systemd-run to launch with limits: systemd-run --user -p MemoryMax=500M ./app</p>',
    "troubleshooting-high-usage":
        '<p>top -o %CPU (CPU hogs), ps aux --sort=-%mem (memory hogs), iotop (I/O), lsof (open files), vmstat (system stats).</p>',
})

# 20. Linux Security Hardening
fill_file("linux-security-hardening.html", {
    "basic-hardening-steps":
        '<pre><code># Disable root SSH\nPermitRootLogin no\nPasswordAuthentication no\n\n# Firewall\nufw default deny incoming\nufw allow ssh\nufw enable\n\n# Auto updates\napt install unattended-upgrades</code></pre>',
    "selinux":
        '<p>SELinux provides mandatory access control. Modes: Enforcing, Permissive, Disabled. Use getenforce/setenforce to check/change. Audit denials with audit2allow.</p>',
    "apparmor":
        '<p>AppArmor is a simpler alternative to SELinux (path-based). Default on Ubuntu. Profiles enforce or complain. Generate with aa-genprof.</p>',
    "system-auditing-(auditd)":
        '<p>auditd monitors file changes, syscalls, and network config. Rules in /etc/audit/rules.d/. Search logs with ausearch and aureport.</p>',
    "kernel-hardening-(sysctl)":
        '<p>sysctl settings: disable IP forwarding, ignore ICMP redirects, enable SYN cookies, log martian packets. Apply with sysctl -p.</p>',
    "file-integrity-monitoring":
        '<p>AIDE/Tripwire create a database of file hashes and alert on changes. debsums verifies Debian package file integrity.</p>',
})

# 21. Linux Disk Management
fill_file("linux-disk-management.html", {
    "disk-partitioning":
        '<p>Use fdisk (MBR), gdisk (GPT), or parted for partitioning. List disks with lsblk or fdisk -l. Reload table with partprobe.</p>',
    "filesystem-creation":
        '<p>Create filesystems: mkfs.ext4, mkfs.xfs, mkfs.btrfs, mkfs.fat. Mount with mount, persist in /etc/fstab using UUIDs.</p>',
    "lvm":
        '<p>LVM layers: PV (physical volume), VG (volume group), LV (logical volume). Extend online with lvextend + resize2fs. Snapshots with lvcreate -s.</p>',
    "software-raid-(mdadm)":
        '<p>RAID levels: 0 (striping), 1 (mirror), 5 (striped parity), 6 (double parity), 10 (mirrored stripes). Monitor with mdadm --detail /proc/mdstat.</p>',
    "disk-monitoring":
        '<p>Disk usage: df -h, du -sh. I/O: iostat, iotop. SMART: smartctl -a. Find large files: ncdu, find -size +100M.</p>',
})

# 22. Windows Registry Hacks
fill_file("windows-registry-hacks.html", {
    "registry-basics":
        '<p>Five main hives: HKCR (file associations), HKCU (user settings), HKLM (system settings), HKU (all users), HKCC (hardware). Always back up before editing!</p>',
    "performance-tweaks":
        '<pre><code>; Disable Cortana\n[HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search]\n"AllowCortana"=dword:00000000\n\n; Speed up shutdown\n"WaitToKillAppTimeout"="2000"\n"AutoEndTasks"="1"</code></pre>',
    "ui-customization":
        '<pre><code>; Remove shortcut arrows\n[HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Icons]\n"29"="%windir%\\System32\\shell32.dll,50"\n\n; Show hidden files\n[HKCU\\...\\Advanced]\n"Hidden"=dword:00000001</code></pre>',
    "security-and-privacy-hacks":
        '<pre><code>; Disable telemetry\n[HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection]\n"AllowTelemetry"=dword:00000000\n\n; Disable Bing search in Start\n[HKCU\\...\\Search]\n"BingSearchEnabled"=dword:00000000</code></pre>',
    "creating-.reg-files":
        '<pre><code>; tweak.reg\nWindows Registry Editor Version 5.00\n\n; Add value\n[HKCU\\Control Panel\\Desktop]\n"MenuShowDelay"="0"\n\n; Delete key\n[-HKLM\\SOFTWARE\\Policy]</code></pre>',
})

# 23-50: Let me fill the remaining files efficiently

# 23. WSL2
fill_file("wsl2-guide.html", {
    "what-is-wsl2?":
        '<p><strong>WSL2</strong> runs a real Linux kernel inside a lightweight VM on Windows. Full system call compatibility and native ext4 performance.</p>',
    "installation":
        '<pre><code>wsl --install -d Ubuntu-24.04\nwsl --set-default-version 2\nwsl --update</code></pre>',
    "wsl-management":
        '<pre><code>wsl -l -v                    # List distros\nwsl --export Ubuntu backup.tar\nwsl --import Clone Ubuntu-Clone backup.tar\nwsl --shutdown\nwsl --unregister Ubuntu</code></pre>',
    "configuration":
        '<p>.wslconfig in %USERPROFILE%: set memory=8GB, processors=4, localhostForwarding=true.</p>',
    "development-workflow":
        '<p>Store code on Linux filesystem (/home/.../projects). Access via \\\\wsl$\\ from Windows. Use VS Code Remote-WSL. Run Docker with WSL2 backend.</p>',
    "gpu-and-tips":
        '<p>GPU acceleration: CUDA works in WSL2. systemd enabled by default. USB passthrough via usbipd-win.</p>',
})

# 24. Windows Defender
fill_file("windows-defender-security.html", {
    "defender-overview":
        '<p>Microsoft Defender provides real-time protection, cloud-delivered protection, tamper protection, and consistently ranks top in AV-Test.</p>',
    "powershell-configuration":
        '<pre><code># Check status\nGet-MpComputerStatus\n\n# Scan\nStart-MpScan -ScanType FullScan\n\n# Exclusions\nAdd-MpPreference -ExclusionPath "C:\\MyApps"</code></pre>',
    "asr-rules":
        '<p>Attack Surface Reduction rules block common malware entry points. Enable via Group Policy or PowerShell. Test in Audit mode first.</p>',
    "controlled-folder-access":
        '<p>Ransomware protection: prevents untrusted apps from modifying protected folders. Enable with Set-MpPreference -EnableControlledFolderAccess Enabled.</p>',
    "defender-firewall":
        '<pre><code># Allow port\nNew-NetFirewallRule -DisplayName "Port 8080" -Direction Inbound -Protocol TCP -LocalPort 8080 -Action Allow\n\n# Block outbound app\nNew-NetFirewallRule -DisplayName "Block App" -Direction Outbound -Program "C:\\Bad\\app.exe" -Action Block</code></pre>',
})

# 25. Windows Event Viewer
fill_file("windows-event-viewer.html", {
    "event-viewer-basics":
        '<p>Event Viewer (eventvwr.msc) logs system events in categories: Application, Security, System, Setup, Forwarded Events. Event levels: Info, Warning, Error, Critical.</p>',
    "custom-views-and-filtering":
        '<p>Filter by Event ID, Level, Source. Key IDs: 4624 (logon), 4625 (failed logon), 4688 (process creation), 41 (unclean shutdown), 1001 (crash).</p>',
    "powershell-queries":
        '<pre><code># Recent errors\nGet-WinEvent -LogName System -MaxEvents 50 | Where-Object { $_.LevelDisplayName -match "Error|Critical" }\n\n# Failed logins\nGet-WinEvent -LogName Security -FilterXPath "*[System[EventID=4625]]"</code></pre>',
    "common-event-ids":
        '<p><strong>41</strong> \u2014 Unexpected shutdown | <strong>1074</strong> \u2014 Shutdown/restart | <strong>4624</strong> \u2014 Successful logon | <strong>4625</strong> \u2014 Failed logon | <strong>4688</strong> \u2014 Process creation | <strong>6008</strong> \u2014 Unexpected shutdown</p>',
    "diagnostic-scenarios":
        '<p>Use Event Viewer to diagnose BSODs (critical level), app crashes (1001), driver failures, service hangs, and login failures.</p>',
})

# 26. Windows Task Scheduler
fill_file("windows-task-scheduler.html", {
    "task-scheduler-overview":
        '<p>Task Scheduler (taskschd.msc) automates task execution based on time, events, or system state. Tasks consist of triggers, actions, and conditions.</p>',
    "creating-basic-tasks":
        '<ol><li>Open Task Scheduler</li><li>Action > Create Basic Task</li><li>Name and description</li><li>Set trigger (daily, weekly, etc.)</li><li>Set action (start program, send email, show message)</li><li>Finish</li></ol>',
    "advanced-triggers":
        '<p>Triggers: on schedule, at system startup, at logon, on idle, on event, on connection to VPN, on workstation lock/unlock, on session connect.</p>',
    "actions-and-conditions":
        '<p>Actions: start program, send email, display message. Conditions: only if AC power, only on network, only if computer is idle.</p>',
    "powershell-and-cli":
        '<pre><code># PowerShell cmdlets\nGet-ScheduledTask\nNew-ScheduledTask\nRegister-ScheduledTask\nStart-ScheduledTask\n\n# schtasks.exe\nschtasks /create /tn "MyTask" /tr "notepad.exe" /sc daily /st 09:00</code></pre>',
    "troubleshooting-scheduled-tasks":
        '<p>Check task status in History tab. Run the task manually. Verify user has "Log on as batch job" rights. Check Last Run Result code.</p>',
})

# 27. Subnetting
fill_file("subnetting-cidr.html", {
    "ip-addressing-review":
        '<p>IPv4: 32-bit address, divided into 4 octets. Network portion + Host portion. Class A (1-126), Class B (128-191), Class C (192-223). Private ranges: 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16.</p>',
    "what-is-subnetting?":
        '<p>Subnetting divides a network into smaller subnetworks, improving efficiency, security, and reducing broadcast domains.</p>',
    "cidr-notation":
        '<p>CIDR (Classless Inter-Domain Routing) uses /prefix notation, e.g., 192.168.1.0/24 = 255.255.255.0 = 256 addresses - 2 = 254 usable.</p>',
    "subnet-calculation":
        '<p><strong>Formula:</strong> Usable hosts = 2^(32-prefix) - 2. Example: /24 = 254 hosts, /25 = 126 hosts, /26 = 62 hosts, /27 = 30 hosts.</p>',
    "vlsm":
        '<p><strong>VLSM</strong> (Variable Length Subnet Mask) allows subnets of different sizes within the same network, optimizing address usage.</p>',
    "practice-problems":
        '<p><strong>Problem:</strong> Network 192.168.1.0/24 needs 3 subnets with 50, 30, and 10 hosts.</p><p>/26 (62 hosts): 192.168.1.0/26, /27 (30 hosts): 192.168.1.64/27, /28 (14 hosts): 192.168.1.96/28</p>',
})

# 28. DNS Records
fill_file("dns-records-deep-dive.html", {
    "dns-fundamentals":
        '<p>DNS translates domain names to IP addresses. Hierarchy: Root (.) > TLD (.com) > Authoritative (example.com). Record types define the kind of data.</p>',
    "a-and-aaaa-records":
        '<p><strong>A record</strong> maps hostname to IPv4 (example.com -> 93.184.216.34). <strong>AAAA record</strong> maps hostname to IPv6 (example.com -> 2606:2800:220:1:248:1893:25c8:1946).</p>',
    "cname-and-aliases":
        '<p><strong>CNAME</strong> (Canonical Name) creates an alias: www.example.com -> example.com. Cannot coexist with other records at the same name.</p>',
    "mx-and-mail-records":
        '<p><strong>MX</strong> (Mail Exchange): specifies mail servers with priority values (lower = higher priority). Example: priority 10 mail.example.com.</p>',
    "txt-and-spf-records":
        '<p><strong>TXT</strong> stores arbitrary text for domain verification, SPF (email sending authorization), DKIM (email signing), and DMARC policies.</p>',
    "dnssec":
        '<p><strong>DNSSEC</strong> adds cryptographic signatures to DNS records, protecting against spoofing and cache poisoning. Uses RRSIG, DNSKEY, DS records.</p>',
})

# 29. HTTP/2 & HTTP/3
fill_file("http2-http3.html", {
    "http-1.1-limitations":
        '<p>HTTP/1.1 issues: head-of-line blocking (one request blocks others), multiple connections needed, verbose headers, no server push.</p>',
    "http-2-features":
        '<p>HTTP/2 improvements: multiplexed streams (multiple requests over one connection), header compression (HPACK), server push, binary protocol, stream prioritization.</p>',
    "multiplexing-and-prioritization":
        '<p>Multiple streams send data in interleaved frames over a single TCP connection. Stream prioritization ensures critical resources load first.</p>',
    "server-push":
        '<p>Server can push resources (CSS, JS, images) before client requests them. Reduces round trips but must be used carefully to avoid sending unwanted data.</p>',
    "http-3-and-quic":
        '<p><strong>HTTP/3</strong> uses QUIC (Quick UDP Internet Connections) instead of TCP. Benefits: faster connection establishment (0-RTT), built-in encryption, connection migration, no head-of-line blocking at transport layer.</p>',
    "migration-guide":
        '<p>To support HTTP/2: enable TLS (required), update web server (Nginx 1.9+, Apache 2.4.17+). For HTTP/3: use Nginx with quiche or Caddy with built-in HTTP/3 support.</p>',
})

# 30. Grafana & Prometheus
fill_file("grafana-prometheus.html", {
    "monitoring-overview":
        '<p>Modern monitoring stack: Prometheus collects metrics (pull model), Grafana visualizes them. Alertmanager handles alerts. Exporters expose metrics from various systems.</p>',
    "prometheus-setup":
        '<pre><code># docker-compose.yml\nservices:\n  prometheus:\n    image: prom/prometheus\n    volumes:\n      - ./prometheus.yml:/etc/prometheus/prometheus.yml\n    ports:\n      - "9090:9090"</code></pre>',
    "exporters-and-metrics":
        '<p>Exporters: node_exporter (system), blackbox_exporter (HTTP/DNS), mysqld_exporter, nginx_exporter, cadvisor (Docker), kube-state-metrics (K8s).</p>',
    "grafana-dashboards":
        '<p>Grafana connects to Prometheus as a data source. Import community dashboards from grafana.com. Create panels with PromQL queries.</p>',
    "alerting-rules":
        '<pre><code># prometheus.yml\nalerting:\n  alertmanagers:\n    - static_configs:\n        - targets: ["alertmanager:9093"]\n\n# rules.yml\ngroups:\n  - name: node\n    rules:\n      - alert: HighCPU\n        expr: 100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 80</code></pre>',
    "best-practices":
        '<p>Use recording rules for expensive queries. Apply histogram buckets for latency. Set up team notification channels (Slack, PagerDuty, email).</p>',
})

# 31. OWASP Top 10
fill_file("owasp-top-10.html", {
    "broken-access-control":
        '<p>#1 risk. Occurs when users can act outside their permissions. Prevention: enforce role-based access, deny by default, validate permissions server-side.</p>',
    "cryptographic-failures":
        '<p>Formerly "Sensitive Data Exposure". Use TLS everywhere, encrypt sensitive data at rest, use strong hashing (argon2, bcrypt), never roll your own crypto.</p>',
    "injection":
        '<p>SQL, NoSQL, OS, LDAP injection. Prevention: parameterized queries, input validation, least privilege, ORM frameworks.</p>',
    "insecure-design":
        '<p>Insufficient threat modeling, missing security controls. Prevention: secure design patterns, threat modeling (STRIDE), security review in design phase.</p>',
    "security-misconfiguration":
        '<p>Default credentials, unnecessary features enabled, improper headers. Prevention: hardening guides, automated scanners, minimal configurations.</p>',
    "vulnerable-components":
        '<p>Using outdated libraries with known CVEs. Prevention: SBOM (software bill of materials), dependabot/renovate, regular updates.</p>',
    "auth-failures":
        '<p>Weak passwords, credential stuffing, missing MFA. Prevention: multi-factor auth, rate limiting, password policies, OAuth/OIDC.</p>',
    "data-integrity":
        '<p>Software supply chain attacks. Prevention: code signing, integrity checks, subresource integrity (SRI), secure CI/CD pipelines.</p>',
    "logging-monitoring":
        '<p>Insufficient incident detection. Prevention: centralized logging, alerting on suspicious events, regular log review.</p>',
    "ssrf":
        '<p>Server-Side Request Forgery. Prevention: allowlist destinations, disable unnecessary URL schemes, validate and sanitize URLs.</p>',
})

# 32. GPG & PGP
fill_file("gpg-pgp-guide.html", {
    "what-is-gpg?":
        '<p>GNU Privacy Guard (GPG) implements OpenPGP standard for encryption and signing. Used for secure email (with Thunderbird/Enigmail), file encryption, and code signing (git tag -s).</p>',
    "key-generation":
        '<pre><code>gpg --full-generate-key\n# Select: RSA and RSA, 4096 bits\n# No expiry recommended for primary key\n# Set UID: Name, email address</code></pre>',
    "key-management":
        '<pre><code>gpg --list-keys               # Public keys\ngpg --list-secret-keys        # Private keys\ngpg --export -a "Alice" > alice.pub\ngpg --import alice.pub\ngpg --keyserver keyserver.ubuntu.com --search-keys alice@example.com</code></pre>',
    "encryption-and-decryption":
        '<pre><code># Encrypt file (to multiple recipients)\ngpg -e -r alice@example.com -r bob@example.com secret.txt\n\n# Decrypt\ngpg -d secret.txt.gpg > secret.txt</code></pre>',
    "signing-and-verification":
        '<pre><code># Sign a file (detached signature)\ngpg --detach-sign -a file.txt\n\n# Verify\ngpg --verify file.txt.asc file.txt\n\n# Sign git commit\ngit commit -S -m "Signed commit"</code></pre>',
    "smartcards-and-yubikey":
        '<p>Store GPG private keys on YubiKey for hardware security: gpg --edit-key KEYID then "keytocard". Keys cannot be extracted from the device.</p>',
})

# 33. Hashing vs Encryption
fill_file("hashing-vs-encryption.html", {
    "core-concepts":
        '<p><strong>Hashing</strong> \u2014 One-way function, cannot be reversed, deterministic. <strong>Encryption</strong> \u2014 Two-way with key, reversible. <strong>Encoding</strong> \u2014 Not security, just format transformation (base64, URL encoding).</p>',
    "hashing-algorithms":
        '<p>MD5 (broken, do not use), SHA-1 (deprecated), SHA-256/512 (current), bcrypt/argon2 (password hashing, deliberately slow).</p>',
    "symmetric-encryption":
        '<p>Same key for encrypt and decrypt. Algorithms: AES-256 (standard), ChaCha20 (modern), 3DES (deprecated). Use cases: file encryption, full-disk encryption.</p>',
    "asymmetric-encryption":
        '<p>Different keys: public key encrypts, private key decrypts. Algorithms: RSA (widely supported), ECC/Elliptic Curve (smaller keys, faster). Use cases: TLS/SSL, GPG, SSH.</p>',
    "encoding-schemes":
        '<p>Base64 (binary to text, used in data URIs), URL encoding (%20 for spaces), Base58 (Bitcoin addresses), Hex (hexadecimal representation).</p>',
    "when-to-use-each":
        '<p><strong>Hash</strong> passwords, verify file integrity, digital signatures. <strong>Encrypt</strong> confidential data, secure communication. <strong>Encode</strong> data transmission, URL formatting.</p>',
})

# 34. Browser Fingerprinting
fill_file("browser-fingerprinting.html", {
    "what-is-fingerprinting?":
        '<p>Browser fingerprinting identifies users by collecting unique browser/device characteristics. Unlike cookies, it is passive and harder to block. Fingerprints can be near-unique across millions of users.</p>',
    "fingerprinting-techniques":
        '<p>Common techniques: user agent, screen resolution, timezone, language, installed fonts, browser plugins, HTTP headers (Accept, DNT). Combine these into a hash.</p>',
    "canvas-and-webgl":
        '<p>Canvas fingerprinting renders invisible text/images and reads the pixel hash (differs per GPU/driver). WebGL fingerprinting queries GPU model and driver details.</p>',
    "audio-and-font-fingerprinting":
        '<p>Audio fingerprinting measures how the browser handles audio processing (differences in DAC, drivers). Font fingerprinting uses CSS @font-face to detect installed fonts by measuring rendered widths.</p>',
    "anti-detection-tools":
        '<ul><li><strong>Firefox</strong> \u2014 Enable resistive fingerprinting (privacy.resistFingerprinting)</li><li><strong>Brave</strong> \u2014 Built-in fingerprinting protection (farbling)</li><li><strong>Tor Browser</strong> \u2014 All users have identical fingerprints</li><li><strong>CanvasBlocker</strong> \u2014 Firefox extension</li></ul>',
})

# 35. Social Engineering
fill_file("social-engineering.html", {
    "what-is-social-engineering?":
        '<p>Social engineering manipulates people into revealing sensitive information or taking actions. It exploits human psychology: authority, urgency, fear, trust, reciprocity.</p>',
    "phishing-attacks":
        '<p><strong>Phishing</strong>: fake emails pretending to be legitimate. <strong>Spear phishing</strong>: targeted at specific individuals. <strong>Whaling</strong>: targeting executives. <strong>Smishing</strong>: SMS phishing. <strong>Vishing</strong>: voice phishing.</p>',
    "pretexting-and-tailgating":
        '<p><strong>Pretexting</strong>: attacker creates a fabricated scenario to extract information. <strong>Tailgating</strong>: following authorized person into secure area without credentials. <strong>Piggybacking</strong>: with consent.</p>',
    "baiting-and-quid-pro-quo":
        '<p><strong>Baiting</strong>: leaving infected USB drives in parking lots. <strong>Quid Pro Quo</strong>: offering a service in exchange for information (tech support scams).</p>',
    "defense-strategies":
        '<p>Security awareness training, verify identities before sharing info, don\'t trust caller ID, use multi-factor auth, report suspicious contacts.</p>',
    "incident-response":
        '<p>If you suspect social engineering: document everything, report to security team, change passwords, monitor accounts, enable additional verification.</p>',
})

# 36. DaVinci Resolve
fill_file("davinci-resolve-basics.html", {
    "interface-overview":
        '<p>DaVinci Resolve has 7 pages (tabs at bottom): Media (import), Cut (quick edit), Edit (timeline), Fusion (VFX), Color (grading), Fairlight (audio), Deliver (export). Free version is remarkably capable.</p>',
    "project-setup":
        '<p>Create project: Master Settings > Timeline resolution (1080p/4K), frame rate (24/30/60), color management (DaVinci YRGB), proxy generation for smooth editing.</p>',
    "cut-and-edit-pages":
        '<p><strong>Cut page</strong>: Fast editing with source tape, trim, and sync bin. <strong>Edit page</strong>: Full timeline editing, multi-cam, transitions, keyframes, titles.</p>',
    "color-correction":
        '<p><strong>Primary correction</strong>: Lift/Gamma/Gain, color wheels, curves. <strong>Secondary correction</strong>: qualifiers (selective color), power windows (shapes), tracking.</p>',
    "fairlight-audio":
        '<p>Fairlight page: multi-track audio editing, noise reduction (with Fairlight FX), compression, EQ, level automation, ADR (automated dialogue replacement).</p>',
    "delivery-and-export":
        '<p>Deliver page: export presets for YouTube/Vimeo, custom settings (codec: H.264/H.265, format: MP4/MOV), render queue, subtitle export.</p>',
})

# 37. Blender 3D
fill_file("blender-3d-basics.html", {
    "blender-interface":
        '<p>Blender interface: 3D Viewport (center), Outliner (right), Properties (right), Timeline (bottom). Key shortcuts: G (grab), R (rotate), S (scale), Tab (edit mode).</p>',
    "basic-modeling":
        '<p>Primitives: cube, sphere, cylinder. Edit mode: vertices, edges, faces. Tools: extrude (E), loop cut (Ctrl+R), bevel (Ctrl+B), subdivision surface modifier.</p>',
    "materials-and-textures":
        '<p>Shader Editor: Principled BSDF (main shader), add image textures, normal maps. UV Unwrap (U) for applying 2D images to 3D surfaces.</p>',
    "lighting-and-cameras":
        '<p>Light types: Point, Sun, Spot, Area. 3-point lighting is standard. Camera settings: focal length, depth of field, composition guides.</p>',
    "rendering":
        '<p>Render engines: Eevee (fast, real-time), Cycles (accurate, path-traced). Output: PNG sequences, video (FFmpeg). GPU rendering in Cycles is much faster.</p>',
    "animation-basics":
        '<p>Keyframes (I key), Auto Keying, Graph Editor (curves), Dope Sheet (timing). Constraints, armatures (rigging), shape keys (blendshapes).</p>',
})

# 38. SVG Animation
fill_file("svg-animation-css-js.html", {
    "svg-basics":
        '<p>SVG (Scalable Vector Graphics) is XML-based vector graphics. Elements: rect, circle, path, text, g (group). ViewBox defines coordinate system. Responsive by default.</p>',
    "css-svg-animations":
        '<pre><code>@keyframes dash {\n  to { stroke-dashoffset: 0; }\n}\npath {\n  stroke-dasharray: 1000;\n  stroke-dashoffset: 1000;\n  animation: dash 2s ease forwards;\n}</code></pre>',
    "javascript-svg-manipulation":
        '<pre><code>const circle = document.querySelector("circle");\ncircle.setAttribute("r", "50");\ncircle.style.transition = "r 0.5s";\ncircle.addEventListener("click", () => {\n  circle.setAttribute("r", "100");\n});</code></pre>',
    "gsap-library":
        '<pre><code>gsap.to("#myPath", {\n  duration: 2,\n  strokeDashoffset: 0,\n  ease: "power2.out"\n});\ngsap.from("#logo", { opacity: 0, y: -50, duration: 1 });</code></pre>',
    "interactive-animations":
        '<p>Combine mouse events, scroll position, and CSS transitions for interactive SVG animations. Use IntersectionObserver for scroll-triggered animations.</p>',
    "performance-tips":
        '<p>Use will-change for hardware acceleration, avoid animating stroke-dasharray on many elements, use requestAnimationFrame for JS animations. Prefer CSS animations over JS for simple effects.</p>',
})

# 39. Audacity Audio Editing
fill_file("audacity-audio-editing.html", {
    "audacity-setup":
        '<p>Download from audacityteam.org. Install FFmpeg library for extended format support. Configure audio host (ALSA on Linux, WASAPI on Windows, CoreAudio on macOS).</p>',
    "recording-audio":
        '<p>Select input device (microphone), set project rate (44100 Hz standard), use Transport > Record. Monitor levels: aim for -12dB to -6dB peaks. Use USB mics for best quality.</p>',
    "basic-editing":
        '<p>Selection tool (I-beam), Envelope tool (volume), Draw tool (sample-level). Cut (Ctrl+X), Copy (Ctrl+C), Paste (Ctrl+V). Time Shift tool to move clips.</p>',
    "noise-reduction":
        '<p>Select a noise-only sample (1-2 seconds). Effect > Noise Reduction > Get Noise Profile. Select entire track > Noise Reduction > OK. For removing background hum: use Notch Filter.</p>',
    "effects-and-filters":
        '<p>Compression (even out volume), Equalization (boost/cut frequencies), Reverb, Delay, Pitch Shift, Speed Change. Use Effect > Amplify to normalize to -1dB.</p>',
    "multitrack-mixing":
        '<p>Create multiple tracks for voice, music, effects. Use Solo/Mute buttons. Track > Mix > Mix Stereo to Master. Adjust gain envelopes for smooth transitions.</p>',
    "exporting":
        '<p>File > Export Audio. Formats: WAV (lossless, archival), MP3 (compressed, compatible), FLAC (lossless, compressed), OGG (open format). Set metadata (Title, Artist, Album).</p>',
})

# 40-50: General Tech tutorials
fill_file("cloud-computing-overview.html", {
    "what-is-cloud-computing?":
        '<p>Cloud computing delivers computing services over the internet: compute, storage, databases, networking, software. Three models: IaaS, PaaS, SaaS. Five characteristics: on-demand, broad access, resource pooling, rapid elasticity, measured service.</p>',
    "iaas-vs-paas-vs-saas":
        '<p><strong>IaaS</strong> \u2014 Virtual machines, storage, networking (AWS EC2, GCP Compute). <strong>PaaS</strong> \u2014 Managed runtime (Heroku, App Engine). <strong>SaaS</strong> \u2014 Complete applications (Gmail, Office 365).</p>',
    "aws-services":
        '<p>Compute: EC2, Lambda. Storage: S3, EBS. Database: RDS, DynamoDB. Networking: VPC, CloudFront. Container: ECS, EKS, Fargate. AI: SageMaker, Bedrock.</p>',
    "google-cloud-services":
        '<p>Compute: Compute Engine, Cloud Functions. Storage: Cloud Storage, Filestore. Database: Cloud SQL, Firestore. Networking: VPC, Cloud CDN. Container: GKE. AI: Vertex AI.</p>',
    "azure-services":
        '<p>Compute: Azure VMs, Functions. Storage: Blob Storage, Files. Database: SQL Database, Cosmos DB. Networking: VNet, Front Door. Container: AKS. AI: Azure AI.</p>',
    "multi-cloud-strategies":
        '<p>Reasons for multi-cloud: avoid lock-in, best-of-breed services, compliance, disaster recovery. Challenges: complexity, data transfer costs, security across providers.</p>',
})

# 41. VirtualBox vs VMware vs Hyper-V
fill_file("virtualbox-vmware-hyperv.html", {
    "virtualization-overview":
        '<p>Hypervisors create and run virtual machines. Type 1 (bare metal): Hyper-V, ESXi, KVM. Type 2 (hosted): VirtualBox, VMware Workstation. Performance: Type 1 is faster for production.</p>',
    "virtualbox-features":
        '<p>Free and open-source (Oracle). Features: snapshots, seamless mode, shared folders, 3D acceleration (experimental), USB passthrough. Supports many guest OS types.</p>',
    "vmware-workstation-player":
        '<p>VMware Workstation Player (free for personal use), Pro (paid). Features: better 3D support than VirtualBox, consistent snapshots, Unity mode, vSphere integration.</p>',
    "hyper-v-features":
        '<p>Built into Windows Pro/Enterprise. Type 1 hypervisor. Features: nested virtualization, live migration, shared VHDX, PowerShell management, Linux integration services.</p>',
    "performance-comparison":
        '<p>Hyper-V has best CPU/memory performance (Type 1). VMware has best GPU passthrough. VirtualBox is most convenient for quick testing on any host OS.</p>',
    "choosing-the-right-tool":
        '<p>Use VirtualBox for cross-platform testing. VMware for development and lab with better graphics. Hyper-V for Windows-centric production and server virtualization.</p>',
})

# 42. Containerization vs Virtualization
fill_file("containerization-vs-virtualization.html", {
    "traditional-virtualization":
        '<p>Each VM includes a full OS kernel, virtual hardware (CPU, memory, disk, NIC). Heavyweight (GBs per VM). Strong isolation boundary. Boot time: minutes.</p>',
    "containerization-with-docker":
        '<p>Containers share the host kernel, package only the application and dependencies. Lightweight (MBs per container). Weak isolation (same kernel). Boot time: seconds.</p>',
    "key-differences":
        '<table><tr><th>Feature</th><th>VM</th><th>Container</th></tr><tr><td>Size</td><td>GBs</td><td>MBs</td></tr><tr><td>Boot</td><td>Minutes</td><td>Seconds</td></tr><tr><td>Isolation</td><td>Strong (hypervisor)</td><td>Weak (kernel namespace)</td></tr><tr><td>OS</td><td>Any (full OS)</td><td>Same kernel as host</td></tr></table>',
    "use-cases":
        '<p>VMs: running different operating systems, legacy apps, strong isolation required, production servers. Containers: microservices, CI/CD pipelines, development environments, portable apps.</p>',
    "kubernetes-orchestration":
        '<p>Kubernetes orchestrates containers across a cluster: scheduling, scaling, rolling updates, service discovery, load balancing, self-healing.</p>',
})

# 43. Big Data Tools
fill_file("big-data-tools.html", {
    "what-is-big-data?":
        '<p>Big Data characterized by 3 Vs: Volume (terabytes/petabytes), Velocity (real-time streaming), Variety (structured, semi-structured, unstructured). Also: Veracity and Value.</p>',
    "hadoop-ecosystem":
        '<p>Hadoop includes: HDFS (distributed storage), MapReduce (processing), YARN (resource management), Hive (SQL-like queries), HBase (NoSQL), Pig (scripts), Oozie (workflow).</p>',
    "hdfs-and-mapreduce":
        '<p>HDFS: files split into blocks (128MB default), replicated across nodes (3x default), rack-aware placement. MapReduce: maps process data in parallel, reduces aggregate results.</p>',
    "apache-spark":
        '<p>Spark is 100x faster than MapReduce (in-memory processing). Components: Spark Core, Spark SQL, Spark Streaming, MLlib (ML), GraphX (graph processing). Uses DataFrames and RDDs.</p>',
    "spark-sql-and-streaming":
        '<pre><code># Spark SQL\nfrom pyspark.sql import SparkSession\nspark = SparkSession.builder.appName("example").getOrCreate()\ndf = spark.read.json("data.json")\ndf.createOrReplaceTempView("users")\nresult = spark.sql("SELECT count(*) FROM users")</code></pre>',
    "data-lakes":
        '<p>Data lakes store raw, unprocessed data in native formats (Parquet, Avro, ORC). Unlike data warehouses (schemas enforced on write), lakes enforce schema on read. Tools: Delta Lake, Apache Iceberg, Apache Hudi.</p>',
})

# 44. Machine Learning Basics
fill_file("ml-basics-python.html", {
    "what-is-machine-learning?":
        '<p>ML builds models that learn from data. Types: Supervised (labeled data), Unsupervised (unlabeled), Reinforcement (reward-based). Key concepts: features, labels, training, inference, overfitting, underfitting.</p>',
    "setting-up-python-ml-stack":
        '<pre><code>pip install numpy pandas scikit-learn matplotlib jupyter\n\n# Or conda\nconda install numpy pandas scikit-learn matplotlib jupyter</code></pre>',
    "data-preparation":
        '<pre><code>import pandas as pd\ndf = pd.read_csv("data.csv")\ndf.isnull().sum()  # Missing values\ndf.describe()      # Summary stats\n# Train/test split\nfrom sklearn.model_selection import train_test_split\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)</code></pre>',
    "supervised-learning":
        '<pre><code># Classification: Random Forest\nfrom sklearn.ensemble import RandomForestClassifier\nmodel = RandomForestClassifier(n_estimators=100)\nmodel.fit(X_train, y_train)\naccuracy = model.score(X_test, y_test)\n\n# Regression: Linear Regression\nfrom sklearn.linear_model import LinearRegression\nreg = LinearRegression()\nreg.fit(X_train, y_train)</code></pre>',
    "unsupervised-learning":
        '<pre><code># K-Means Clustering\nfrom sklearn.cluster import KMeans\nkmeans = KMeans(n_clusters=3)\ndf["cluster"] = kmeans.fit_predict(X)\n\n# Dimensionality Reduction: PCA\nfrom sklearn.decomposition import PCA\npca = PCA(n_components=2)\nX_reduced = pca.fit_transform(X)</code></pre>',
    "model-evaluation":
        '<p>Metrics: accuracy, precision, recall, F1-score (classification); MSE, MAE, R-squared (regression). Cross-validation for more reliable evaluation. Confusion matrix, ROC curve.</p>',
})

# 45. Advanced Regex
fill_file("regex-advanced.html", {
    "regex-engine-types":
        '<p>Two main engine types: <strong>DFA</strong> (Deterministic Finite Automaton) \u2014 fast, no backreferences/capture groups. <strong>NFA</strong> (Nondeterministic Finite Automaton) \u2014 supports full regex features, can be slow on backtracking. Most modern languages use NFA.</p>',
    "lookahead-and-lookbehind":
        '<pre><code># Positive lookahead: match x only if followed by y\nx(?=y)\n\n# Negative lookahead: match x only if NOT followed by y\nx(?!y)\n\n# Positive lookbehind: match x only if preceded by y\n(?<=y)x\n\n# Negative lookbehind: match x only if NOT preceded by y\n(?<!y)x\n\n# Example: password with uppercase, digit, 8+ chars\n^(?=.*[A-Z])(?=.*\\d).{8,}$</code></pre>',
    "backreferences":
        '<pre><code># Match repeated words\n(\\w+) \\1\n# Matches "is is", "hello hello"\n\n# Use in replacement (Python)\nre.sub(r"(\\w+) (\\w+)", r"\\2 \\1", "first last")\n# "last first"</code></pre>',
    "atomic-groups":
        '<pre><code># Atomic group: once matched, no backtracking\n(?>a|ab)c\n# Will match "ac" but NOT "abc" because the group consumes "a"\n# and never tries "ab"</code></pre>',
    "performance-optimization":
        '<p><strong>Catastrophic backtracking</strong>: avoid nested quantifiers like (a+)+b. Use possessive quantifiers: a++ instead of a+. Use atomic groups: (?>...). Unroll loops: a+b instead of a+.*?b.</p>',
    "real-world-patterns":
        '<pre><code># Email (simplified)\n^[\\w.-]+@[\\w.-]+\\.\\w{2,}$\n\n# URL\nhttps?:\\/\\/[\\w.-]+(?:\\/[\\w./%-]*)?\n\n# IPv4\n^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$\n\n# ISO date\n^\\d{4}-\\d{2}-\\d{2}$</code></pre>',
})

# 46. ASCII, Unicode & Encoding
fill_file("ascii-unicode-encoding.html", {
    "what-is-character-encoding?":
        '<p>Character encoding maps characters to numbers (code points) for digital storage. Early systems used ASCII (7-bit, 128 chars), but it could not handle non-English text.</p>',
    "ascii-standard":
        '<p>ASCII encodes 128 characters (0-127): control characters (0-31, 127), printable characters (32-126): letters, digits, punctuation. Extended ASCII added 128-255, but varied by locale.</p>',
    "unicode-and-code-points":
        '<p>Unicode assigns every character a unique code point (U+0000 to U+10FFFF). Planes: BMP (U+0000-U+FFFF), Supplementary Multilingual (U+10000-U+1FFFF), Supplementary Ideographic (U+20000-U+2FFFF).</p>',
    "utf-8-encoding":
        '<p>UTF-8 is the dominant encoding (98% of web pages). It is backward-compatible with ASCII (0-127 use 1 byte), uses 2-4 bytes for other characters. Variable length: 1-4 bytes per character.</p>',
    "utf-16-and-utf-32":
        '<p>UTF-16 uses 2 or 4 bytes per character. Windows and Java use UTF-16 internally. UTF-32 uses exactly 4 bytes per character (wasteful, but fixed-width).</p>',
    "normalization-forms":
        '<p>Unicode normalization ensures equivalent strings: NFC (composed, default for web), NFD (decomposed, used by macOS), NFKC/NFKD (compatible forms). ê = U+00EA (NFC) = e + combining ^ (NFD).</p>',
})

# 47. Filesystems Compared
fill_file("filesystems-compared.html", {
    "file-system-basics":
        '<p>File systems manage how data is stored and retrieved. Key features: journaling (crash recovery), snapshots, compression, encryption, quotas, access control, maximum file/volume sizes.</p>',
    "ntfs-(windows)":
        '<p>Default for Windows since NT 3.1 (1993). Features: journaling, file permissions, encryption (EFS), compression, quotas, hard links, reparse points, max volume 256TB, max file 256TB.</p>',
    "ext4-(linux)":
        '<p>Default for most Linux distros (since 2008). Features: journaling, extents, delayed allocation, online defragmentation, max volume 1EB, max file 16TB. No built-in compression/snapshots.</p>',
    "btrfs-(linux)":
        '<p>Modern COW filesystem for Linux. Features: snapshots (instant, writable), subvolumes, checksums (data+metadata), compression (zlib, zstd), RAID (0/1/5/6/10), send/receive for incremental backups.</p>',
    "zfs-(solaris-linux)":
        '<p>Advanced filesystem from Sun/Oracle. Features: pooled storage (no more volumes), snapshots, clones, checksums, compression, deduplication, RAID-Z, send/receive, max volume 256ZB.</p>',
    "apfs-(macos)":
        '<p>Apple File System (2017). Features: snapshots, cloning, encryption (per-file), space sharing, TRIM for SSDs. Designed for SSDs and flash storage.</p>',
})

# 48. RAID Levels
fill_file("raid-levels-explained.html", {
    "what-is-raid?":
        '<p>RAID (Redundant Array of Independent Disks) combines multiple disks for performance, redundancy, or both. Implementations: hardware RAID (dedicated controller), software RAID (mdadm, ZFS), motherboard RAID (fakeRAID).</p>',
    "raid-0-(striping)":
        '<p>Data is striped across disks. Performance: Nx (N=disk count). Redundancy: none \u2014 any disk failure loses ALL data. Use case: scratch storage, render cache, temporary files.</p>',
    "raid-1-(mirroring)":
        '<p>Data is identical on each disk. Performance: read = Nx, write = 1x. Redundancy: N-1 disk failures tolerated. Use case: OS disks, critical databases.</p>',
    "raid-5-(striped-parity)":
        '<p>Striped with distributed parity. Requires minimum 3 disks. Performance: read ~N-1x, write = slower (parity calculation). Redundancy: 1 disk failure. Use case: general purpose storage.</p>',
    "raid-6-and-raid-10":
        '<p><strong>RAID 6</strong>: double parity (2 disk failures), needs 4+ disks. <strong>RAID 10</strong>: mirrored stripes (fast + redundant), minimum 4 disks, tolerates 1 per mirror pair.</p>',
    "software-vs-hardware-raid":
        '<p>Hardware RAID: dedicated controller, battery-backed cache, OS independent, expensive. Software RAID: mdadm (free), uses CPU, no cache, flexible. ZFS combines software RAID with filesystem.</p>',
})

# 49. BIOS vs UEFI
fill_file("bios-uefi-boot.html", {
    "what-is-bios?":
        '<p>BIOS (Basic Input/Output System) is the legacy firmware interface. Features: POST (Power-On Self Test), MBR partition table, 16-bit real mode, limited to 2.2TB boot disks, slow boot.</p>',
    "uefi-overview":
        '<p>UEFI (Unified Extensible Firmware Interface) is the modern replacement for BIOS. Features: 64-bit mode, GPT partition table, faster boot, network boot, Secure Boot, graphical interface, supports >2TB disks.</p>',
    "secure-boot":
        '<p>Secure Boot verifies that each boot component (firmware, bootloader, kernel) is signed by a trusted authority. Prevents bootkits and rootkits. Configure in UEFI settings (enable/disable, enroll keys).</p>',
    "gpt-vs-mbr":
        '<p><strong>MBR</strong> (Master Boot Record): supports 4 primary partitions, max 2.2TB disk, legacy. <strong>GPT</strong> (GUID Partition Table): supports 128+ partitions, max 9.4ZB, CRC32 integrity checks, backup header at end of disk.</p>',
    "boot-process-comparison":
        '<p><strong>BIOS Boot:</strong> Power on > BIOS init > POST > Load MBR > Load boot sector > Load bootloader > Load OS kernel.</p><p><strong>UEFI Boot:</strong> Power on > UEFI init > Secure Boot check > Load bootloader from EFI System Partition > Load kernel.</p>',
    "troubleshooting-boot-issues":
        '<p>Common issues: boot mode mismatch (UEFI vs Legacy), missing bootloader, Secure Boot blocking unsigned drivers, corrupted NVRAM entries, incorrect boot order.</p>',
})

# 50. How DNS Works
fill_file("how-dns-works.html", {
    "dns-hierarchy":
        '<p>DNS is a hierarchical system: Root servers (13 sets, letters A-M) > TLD servers (.com, .org, .net) > Authoritative servers (example.com). Each level delegates authority to the next.</p>',
    "recursive-resolution":
        '<p>When you visit example.com: browser checks cache > local resolver queries root server > root redirects to .com TLD > .com TLD redirects to example.com authoritative > returns IP address. Takes milliseconds.</p>',
    "caching-and-ttl":
        '<p>DNS responses are cached to improve performance. TTL (Time To Live) specifies cache duration. Browser cache (seconds/minutes), OS cache, resolver cache (ISP/Cloudflare/Google), application cache.</p>',
    "record-types":
        '<p>Common DNS record types: A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), TXT (text), NS (nameserver), SOA (Start of Authority), SRV (service location), PTR (reverse DNS).</p>',
    "dns-propagation":
        '<p>When you update a DNS record, propagation time depends on TTL (old value) before update, then TTL (new value) for full propagation. Typically minutes to 48 hours. Use tools like whatsmydns.net.</p>',
    "troubleshooting-dns":
        '<pre><code># nslookup\nnslookup example.com\nnslookup -type=MX example.com\n\n# dig\ndig example.com\ndig +trace example.com  # Full resolution path\n\n# Check propagation\n# Use Google DNS (8.8.8.8) for global view\nnslookup example.com 8.8.8.8</code></pre>',
})

print("\n=== All 50 tutorials filled with rich content ===")
