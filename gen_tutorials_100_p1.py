#!/usr/bin/env python3
"""Generate 41 tutorial HTML files — Part 1 (Programming 15, Linux 10, Windows 8, Networking 8)."""
import os
from tutorial_helpers import build_page, write_page, TUTS


def generate_part1():
    # ========== PROGRAMMING (15) ==========

    # 1. Kotlin
    build_page(
        "Kotlin Programming Basics",
        "kotlin-basics.html",
        "Learn Kotlin from scratch -- null safety, coroutines, extension functions, and idiomatic JVM development.",
        "Programming",
        "fas fa-code",
        [
            ("Getting Started with Kotlin",
             "<p>Kotlin is a modern, statically-typed programming language that runs on the JVM and compiles to JavaScript and native binaries. Developed by JetBrains, it became the official language for Android development in 2019.</p>"
             "<p>Install Kotlin via SDKMAN or your IDE:</p>"
             "<pre><code># Install SDKMAN\ncurl -s https://get.sdkman.io | bash\nsdk install kotlin\n\n# Verify\nkotlin -version\n\n# Or use IntelliJ IDEA -- Kotlin is bundled</code></pre>"
             "<p>Kotlin is fully interoperable with Java, meaning you can call Java code from Kotlin and vice versa. This makes adoption gradual and safe for existing projects.</p>"),
            ("Null Safety & Type System",
             "<p>Kotlin's type system eliminates null pointer exceptions at compile time. Types are non-nullable by default:</p>"
             "<pre><code>var name: String = \"Alice\"     // Cannot be null\nvar nullable: String? = null  // Nullable with ?\n\n// Safe call operator\nval length = nullable?.length  // Returns null if nullable is null\n\n// Elvis operator\nval len = nullable?.length ?: 0\n\n// Not-null assertion\nval len2 = nullable!!.length   // Throws if null</code></pre>"
             "<p>Use <code>lateinit</code> for properties initialized after construction, and <code>lazy</code> for deferred initialization.</p>"),
            ("Extension Functions & Properties",
             "<p>Extension functions let you add new behavior to existing classes without inheritance:</p>"
             "<pre><code>fun String.isEmail(): Boolean =\n    this.contains(\"@\") && this.contains(\".\")\n\n\"user@example.com\".isEmail()  // true\n\n// Extension properties\nval String.isNumeric: Boolean\n    get() = this.all { it.isDigit() }</code></pre>"
             "<p>Extensions are resolved statically -- they do not modify the underlying class. This is a powerful tool for creating fluent APIs and utility functions.</p>"
             "<ul><li><strong>Top-level functions</strong> -- no need for utility classes</li><li><strong>Infix notation</strong> -- create DSL-like syntax</li><li><strong>Operator overloading</strong> -- define custom behavior for standard operators</li></ul>"),
            ("Coroutines for Async",
             "<p>Coroutines provide structured concurrency in Kotlin, replacing callbacks and raw threads with suspending functions:</p>"
             "<pre><code>import kotlinx.coroutines.*\n\nsuspend fun fetchData(): String {\n    delay(1000)  // Non-blocking\n    return \"Data loaded\"\n}\n\nfun main() = runBlocking {\n    launch {\n        val result = fetchData()\n        println(result)\n    }\n    println(\"Running...\")\n}</code></pre>"
             "<p>Key concepts: <code>launch</code> for fire-and-forget, <code>async/await</code> for deferred results, <code>Dispatchers</code> for thread pools, and <code>CoroutineScope</code> for lifecycle management.</p>"),
            ("Idiomatic Kotlin: Data Classes & Sealed Classes",
             "<p>Data classes automatically generate <code>equals()</code>, <code>hashCode()</code>, <code>toString()</code>, and <code>copy()</code>:</p>"
             "<pre><code>data class User(val id: Int, val name: String)\n\nval user = User(1, \"Alice\")\nval copy = user.copy(name = \"Bob\")\n\n// Destructuring\nval (id, name) = user</code></pre>"
             "<p>Sealed classes define restricted class hierarchies, ideal for representing states:</p>"
             "<pre><code>sealed class Result {\n    data class Success(val data: String) : Result()\n    data class Error(val msg: String) : Result()\n    object Loading : Result()\n}\n\nfun handle(result: Result) = when (result) {\n    is Result.Success -> println(result.data)\n    is Result.Error -> println(result.msg)\n    Result.Loading -> println(\"Loading...\")\n}</code></pre>"),
        ],
        [
            ("Kotlin Documentation", "https://kotlinlang.org/docs/home.html", "Official Kotlin language reference and guides"),
            ("Kotlin Coroutines Guide", "https://kotlinlang.org/docs/coroutines-guide.html", "In-depth coroutines documentation"),
            ("Kotlin for Android Developers", "https://developer.android.com/kotlin", "Android-specific Kotlin resources"),
        ]
    )

    # 2. Swift
    build_page(
        "Swift Programming Basics",
        "swift-basics.html",
        "Learn Apple's Swift -- optionals, structs, protocols, and modern iOS/macOS development fundamentals.",
        "Programming",
        "fas fa-code",
        [
            ("Swift Overview & Setup",
             "<p>Swift is a powerful, intuitive programming language created by Apple for iOS, macOS, watchOS, and tvOS development. It combines the performance of compiled languages with the expressiveness of scripting languages.</p>"
             "<p>To get started, install Xcode from the Mac App Store, which includes the Swift compiler and LLDB debugger. For Linux or Windows, you can download the Swift toolchain from swift.org.</p>"
             "<p>Create your first Swift file and run it:</p>"
             "<pre><code>// hello.swift\nimport Foundation\nprint(\"Hello, Swift!\")\n\n// Compile & run\nswiftc hello.swift -o hello\n./hello</code></pre>"),
            ("Optionals & Safety",
             "<p>Optionals are Swift's solution to nil safety. A type followed by <code>?</code> indicates it may hold a value or be <code>nil</code>:</p>"
             "<pre><code>var name: String? = \"Alice\"\nname = nil  // Valid\n\n// Optional binding\nif let unwrapped = name {\n    print(\"Hello, \\(unwrapped)\")\n} else {\n    print(\"No name\")\n}\n\n// Guard statement\nfunc greet(_ name: String?) {\n    guard let n = name else { return }\n    print(\"Hello, \\(n)\")\n}\n\n// Nil-coalescing\nlet display = name ?? \"Guest\"</code></pre>"
             "<p>Swift also provides <code>try?</code> and <code>try!</code> for error handling with optionals, ensuring safe error propagation.</p>"),
            ("Structs & Value Semantics",
             "<p>Structs in Swift are value types -- they are copied when assigned. They support methods, properties, and initializers:</p>"
             "<pre><code>struct Point {\n    var x: Double\n    var y: Double\n    \n    func distance(to other: Point) -> Double {\n        let dx = x - other.x\n        let dy = y - other.y\n        return sqrt(dx*dx + dy*dy)\n    }\n    \n    mutating func moveBy(dx: Double, dy: Double) {\n        x += dx\n        y += dy\n    }\n}\n\nlet p1 = Point(x: 0, y: 0)\nvar p2 = p1  // Copy\np2.x = 10</code></pre>"
             "<p>Swift automatically provides memberwise initializers for structs. Use <code>mutating</code> keyword for methods that modify properties.</p>"),
            ("Protocols & Protocol-Oriented Programming",
             "<p>Protocols define a blueprint of methods and properties. They are central to Swift's protocol-oriented programming paradigm:</p>"
             "<pre><code>protocol Drawable {\n    func draw()\n    var area: Double { get }\n}\n\nstruct Circle: Drawable {\n    let radius: Double\n    \n    var area: Double {\n        .pi * radius * radius\n    }\n    \n    func draw() {\n        print(\"Drawing circle with area \\(area)\")\n    }\n}\n\n// Protocol extensions provide default implementations\nextension Drawable {\n    func describe() {\n        print(\"Area: \\(area)\")\n    }\n}</code></pre>"
             "<p>Protocols can also require initializers and subscript implementations. Use protocol composition with <code>&</code> to require multiple protocols.</p>"),
            ("Error Handling & Result Types",
             "<p>Swift uses <code>throws</code>, <code>try</code>, <code>catch</code> for explicit error handling:</p>"
             "<pre><code>enum FileError: Error {\n    case notFound\n    case permissionDenied\n}\n\nfunc readFile(_ path: String) throws -> String {\n    guard path.contains(\"/\") else {\n        throw FileError.notFound\n    }\n    return \"file contents\"\n}\n\ndo {\n    let content = try readFile(\"/data/file.txt\")\n    print(content)\n} catch FileError.notFound {\n    print(\"File not found\")\n} catch {\n    print(\"Other error: \\(error)\")\n}</code></pre>"
             "<p>Swift 5.0 introduced <code>Result&lt;Success, Failure&gt;</code> for asynchronous error handling, making APIs more composable.</p>"),
        ],
        [
            ("Swift.org Documentation", "https://docs.swift.org/swift-book/", "Official Swift programming language guide"),
            ("Apple Developer -- Swift", "https://developer.apple.com/swift/", "Apple's Swift resources and tutorials"),
            ("Swift by Sundell", "https://www.swiftbysundell.com/", "Articles and tips for Swift development"),
        ]
    )

    # 3. C#
    build_page(
        "C# Programming Basics",
        "csharp-basics.html",
        "Learn C# -- LINQ, async/await, .NET ecosystem, and modern cross-platform development.",
        "Programming",
        "fas fa-code",
        [
            ("C# & .NET Overview",
             "<p>C# is a modern, object-oriented language from Microsoft that runs on the .NET runtime. It is used for desktop, web, mobile, game development (Unity), and cloud services. .NET 6+ unified the platform into a single cross-platform runtime.</p>"
             "<p>Install the .NET SDK and create your first project:</p>"
             "<pre><code># Install .NET SDK (Linux/macOS/Windows)\nwget https://dot.net/v1/dotnet-install.sh\nchmod +x dotnet-install.sh\n./dotnet-install.sh\n\n# Create a console app\ndotnet new console -n HelloWorld\ncd HelloWorld\ndotnet run</code></pre>"
             "<p>C# is strongly-typed, supports both managed and unmanaged code, and has first-class tooling in Visual Studio and VS Code.</p>"),
            ("LINQ -- Language Integrated Query",
             "<p>LINQ lets you query collections, databases, and XML using a SQL-like syntax directly in C#:</p>"
             "<pre><code>using System;\nusing System.Linq;\n\nvar numbers = new[] { 1, 2, 3, 4, 5, 6 };\n\n// Query syntax\nvar even = from n in numbers\n           where n % 2 == 0\n           select n;\n\n// Method syntax\nvar squared = numbers.Where(n => n % 2 == 0)\n                     .Select(n => n * n);\n\nforeach (var n in squared)\n    Console.WriteLine(n);\n\n// Deferred execution -- query runs when enumerated\nvar query = numbers.Where(n => n > 3);\nnumbers[0] = 10;  // Query reflects changes</code></pre>"
             "<p>LINQ works with any <code>IEnumerable&lt;T&gt;</code> and has providers for SQL (EF Core), XML (LINQ to XML), and parallel processing (PLINQ).</p>"),
            ("Async/Await & Task Parallel Library",
             "<p>C# has first-class async support through the Task-based Async Pattern (TAP):</p>"
             "<pre><code>using System.Net.Http;\nusing System.Threading.Tasks;\n\npublic async Task&lt;string&gt; FetchDataAsync(string url)\n{\n    using var client = new HttpClient();\n    string result = await client.GetStringAsync(url);\n    return result;\n}\n\n// Caller\npublic async Task ProcessAsync()\n{\n    string data = await FetchDataAsync(\"https://api.example.com\");\n    Console.WriteLine(data);\n}\n\n// Parallel execution\nvar task1 = FetchDataAsync(\"https://api1.com\");\nvar task2 = FetchDataAsync(\"https://api2.com\");\nawait Task.WhenAll(task1, task2);</code></pre>"
             "<p>Use <code>CancellationToken</code> for cooperative cancellation, and <code>ConfigureAwait(false)</code> to avoid capturing the synchronization context in libraries.</p>"),
            ("Object-Oriented Features: Records & Pattern Matching",
             "<p>C# 9 introduced records -- immutable value types with value equality:</p>"
             "<pre><code>public record Person(string FirstName, string LastName, int Age);\n\nvar person1 = new Person(\"Alice\", \"Smith\", 30);\nvar person2 = person1 with { Age = 31 };  // Non-destructive mutation\n\n// Deconstruction\nvar (first, last, age) = person1;</code></pre>"
             "<p>Pattern matching has evolved across versions:</p>"
             "<pre><code>string Describe(object obj) => obj switch\n{\n    int i when i &gt; 0 => \"Positive integer\",\n    int i => \"Non-positive integer\",\n    string s => $\"String: {s}\",\n    null => \"Null\",\n    _ => \"Unknown\"\n};</code></pre>"),
            ("The .NET Ecosystem & ASP.NET Core",
             "<p>The .NET ecosystem includes:</p>"
             "<ul><li><strong>ASP.NET Core</strong> -- Web APIs, MVC, Razor Pages, Blazor</li>"
             "<li><strong>EF Core</strong> -- ORM for SQL databases</li>"
             "<li><strong>MAUI</strong> -- Cross-platform desktop and mobile UI</li>"
             "<li><strong>Xamarin</strong> -- Mobile apps (legacy, replaced by MAUI)</li>"
             "<li><strong>Unity</strong> -- Game engine using C# for scripting</li></ul>"
             "<p>Create an ASP.NET Core API:</p>"
             "<pre><code>dotnet new webapi -n MyApi\ncd MyApi\ndotnet run\n# Navigate to https://localhost:5001/swagger</code></pre>"),
        ],
        [
            ("Microsoft C# Documentation", "https://learn.microsoft.com/en-us/dotnet/csharp/", "Official C# language reference"),
            (".NET Documentation", "https://learn.microsoft.com/en-us/dotnet/", "Complete .NET platform documentation"),
            ("ASP.NET Core Tutorials", "https://learn.microsoft.com/en-us/aspnet/core/", "Web development with .NET"),
        ]
    )

    # 4. PHP
    build_page(
        "PHP Web Development",
        "php-basics.html",
        "PHP syntax, PDO, MVC patterns, and modern web development with Laravel and Composer.",
        "Programming",
        "fas fa-code",
        [
            ("PHP 8 Features & Setup",
             "<p>PHP 8.x introduced major improvements: JIT compilation, named arguments, attributes, union types, and the match expression. Setup a modern PHP environment:</p>"
             "<pre><code># Linux (apt)\nsudo apt install php-cli php-mbstring php-xml composer\n\n# macOS (Homebrew)\nbrew install php composer\n\n# Verify\nphp -v\ncomposer --version</code></pre>"
             "<p>PHP powers over 75% of websites. Modern PHP with frameworks like Laravel bears little resemblance to the old PHP spaghetti code reputation.</p>"),
            ("Modern PHP Syntax & Features",
             "<p>PHP 8 brings expressive type system and concise syntax:</p>"
             "<pre><code>&lt;?php\n\n// Named arguments\nfunction createUser(string $name, string $email, bool $admin = false) {}\ncreateUser(name: \"Alice\", email: \"alice@example.com\", admin: true);\n\n// Union types\nfunction process(int|string $input): int|string {\n    return $input;\n}\n\n// Match expression (strict comparison)\n$result = match ($status) {\n    200, 201 => 'Success',\n    404 => 'Not Found',\n    500 => 'Server Error',\n    default => 'Unknown'\n};\n\n// Attributes (annotations)\n#[Route('/api/users', methods: ['GET'])]\nfunction listUsers() {}</code></pre>"),
            ("PDO Database Access",
             "<p>PDO (PHP Data Objects) provides a safe, consistent interface for multiple databases:</p>"
             "<pre><code>&lt;?php\n$dsn = 'mysql:host=localhost;dbname=app;charset=utf8mb4';\n$pdo = new PDO($dsn, 'user', 'password', [\n    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,\n    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,\n    PDO::ATTR_EMULATE_PREPARES => false,\n]);\n\n// Prepared statements prevent SQL injection\n$stmt = $pdo->prepare('SELECT * FROM users WHERE email = ?');\n$stmt->execute([$email]);\n$user = $stmt->fetch();\n\n// Named parameters\n$stmt = $pdo->prepare('UPDATE users SET name = :name WHERE id = :id');\n$stmt->execute(['name' => $name, 'id' => $id]);</code></pre>"
             "<p>Always use prepared statements. Never concatenate user input into SQL queries.</p>"),
            ("MVC Architecture in Laravel",
             "<p>Laravel is the most popular PHP framework, following the MVC pattern:</p>"
             "<pre><code># Install Laravel\ncomposer create-project laravel/laravel my-app\ncd my-app\nphp artisan serve\n\n# Create a controller\nphp artisan make:controller UserController</code></pre>"
             "<pre><code>&lt;?php\n// routes/web.php\nuse App\\Http\\Controllers\\UserController;\n\nRoute::get('/users', [UserController::class, 'index']);\nRoute::post('/users', [UserController::class, 'store']);\n\n// app/Http/Controllers/UserController.php\nclass UserController extends Controller\n{\n    public function index()\n    {\n        $users = User::all();\n        return view('users.index', compact('users'));\n    }\n    \n    public function store(Request $request)\n    {\n        $validated = $request->validate([\n            'name' => 'required|max:255',\n            'email' => 'required|email|unique:users',\n        ]);\n        \n        return User::create($validated);\n    }\n}</code></pre>"),
            ("Testing & Deployment",
             "<p>PHPUnit is the standard testing framework:</p>"
             "<pre><code>&lt;?php\nuse PHPUnit\\Framework\\TestCase;\n\nclass UserTest extends TestCase\n{\n    public function test_user_has_name(): void\n    {\n        $user = new User(['name' => 'Alice']);\n        $this->assertEquals('Alice', $user->name);\n    }\n}</code></pre>"
             "<ul><li>Use <strong>Laravel Sail</strong> for Docker-based local development</li>"
             "<li>Deploy with <strong>Forge</strong> or <strong>Envoyer</strong> for zero-downtime deployments</li>"
             "<li>Monitor with <strong>Laravel Telescope</strong> (debugging) and <strong>Horizon</strong> (queues)</li></ul>"),
        ],
        [
            ("PHP Manual", "https://www.php.net/manual/en/", "Official PHP documentation"),
            ("Laravel Documentation", "https://laravel.com/docs", "Complete Laravel framework reference"),
            ("PHP The Right Way", "https://phptherightway.com/", "Community best practices guide"),
        ]
    )

    # 5. Ruby
    build_page(
        "Ruby Programming Basics",
        "ruby-basics.html",
        "Ruby syntax, blocks, metaprogramming, and Rails web development fundamentals.",
        "Programming",
        "fas fa-code",
        [
            ("Ruby Philosophy & Setup",
             "<p>Ruby is a dynamic, object-oriented language designed by Yukihiro Matsumoto with a focus on developer happiness and readability. Everything in Ruby is an object, including numbers and classes.</p>"
             "<p>Install Ruby via a version manager:</p>"
             "<pre><code># Install rbenv\ngit clone https://github.com/rbenv/rbenv.git ~/.rbenv\n~/.rbenv/bin/rbenv init\n\n# Install Ruby\nrbenv install 3.3.0\nrbenv global 3.3.0\n\n# Or use RVM\ncurl -sSL https://get.rvm.io | bash\nrvm install 3.3.0\n\nruby --version</code></pre>"),
            ("Elegant Syntax & Blocks",
             "<p>Ruby's syntax prioritizes natural language readability. Blocks are first-class code chunks:</p>"
             "<pre><code># Everything is an object\n5.times { print \"Hi! \" }\n\n# Blocks with do/end\n[1, 2, 3].map do |n|\n  n * 2\nend\n# => [2, 4, 6]\n\n# Symbol shorthand\nusers.map(&amp;:name)  # Same as users.map { |u| u.name }\n\n# Implicit returns -- last expression is returned\ndef square(x)\n  x * x  # No return keyword needed\nend</code></pre>"
             "<p>Blocks can capture local variables (closures) and are used extensively for iteration, callbacks, and DSLs.</p>"),
            ("Metaprogramming & Dynamic Features",
             "<p>Ruby allows modifying classes and objects at runtime -- this is called metaprogramming:</p>"
             "<pre><code># Open classes -- add methods to existing classes\nclass String\n  def shout\n    upcase + \"!\"\n  end\nend\n\n\"hello\".shout  # \"HELLO!\"\n\n# method_missing -- catch undefined method calls\nclass DynamicProxy\n  def method_missing(name, *args, &amp;block)\n    puts \"Called #{name} with #{args}\"\n  end\nend\n\n# define_method -- create methods dynamically\n%w[get post put delete].each do |verb|\n  define_method(verb) do |path, &amp;block|\n    puts \"#{verb.upcase} #{path}\"\n  end\nend</code></pre>"),
            ("Ruby on Rails -- MVC Framework",
             "<p>Ruby on Rails is the flagship Ruby web framework, embracing Convention over Configuration:</p>"
             "<pre><code># Install Rails\ngem install rails\nrails new my_app\ncd my_app\nbin/rails server\n\n# Generate scaffold (full CRUD)\nbin/rails generate scaffold Post title:string body:text\nbin/rails db:migrate\n\n# Routes\n# config/routes.rb\nRails.application.routes.draw do\n  resources :posts\n  root 'posts#index'\nend\n\n# Model with validations\nclass Post &lt; ApplicationRecord\n  validates :title, presence: true, length: { minimum: 5 }\n  has_many :comments, dependent: :destroy\nend</code></pre>"),
            ("Testing with RSpec & Best Practices",
             "<p>RSpec is the dominant testing framework in Ruby:</p>"
             "<pre><code># Gemfile\ngroup :test do\n  gem 'rspec-rails'\n  gem 'factory_bot_rails'\nend\n\n# spec/models/post_spec.rb\nRSpec.describe Post, type: :model do\n  it 'is valid with valid attributes' do\n    post = build(:post, title: 'My Post')\n    expect(post).to be_valid\n  end\n  \n  it 'is invalid without a title' do\n    post = build(:post, title: nil)\n    expect(post).not_to be_valid\n    expect(post.errors[:title]).to include(\"can't be blank\")\n  end\nend</code></pre>"
             "<p>Other testing tools: <strong>Minitest</strong> (built-in), <strong>Capybara</strong> (integration tests), <strong>FactoryBot</strong> (test data).</p>"),
        ],
        [
            ("Ruby Documentation", "https://ruby-doc.org/", "Official Ruby language documentation"),
            ("Ruby on Rails Guides", "https://guides.rubyonrails.org/", "Comprehensive Rails framework guides"),
            ("Ruby Style Guide", "https://rubystyle.guide/", "Community Ruby coding conventions"),
        ]
    )

    # 6. Flutter
    build_page(
        "Flutter App Development",
        "flutter-basics.html",
        "Cross-platform mobile development with Flutter and Dart -- widgets, state management, and native features.",
        "Programming",
        "fas fa-code",
        [
            ("Flutter & Dart Setup",
             "<p>Flutter is Google's UI toolkit for building natively compiled applications for mobile, web, and desktop from a single codebase. It uses the Dart language and renders its own widgets via Skia.</p>"
             "<p>Install Flutter and set up your environment:</p>"
             "<pre><code># Download Flutter SDK\nwget https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.22.0-stable.tar.xz\ntar xf flutter_linux_3.22.0-stable.tar.xz\nexport PATH=\"$PATH:`pwd`/flutter/bin\"\n\n# Check setup\nflutter doctor\n\n# Create your first project\nflutter create my_app\ncd my_app\nflutter run</code></pre>"
             "<p>Flutter's hot reload feature provides sub-second iteration cycles, making UI development highly productive.</p>"),
            ("Widget Tree & Composition",
             "<p>Everything in Flutter is a widget. The UI is built by composing widgets in a tree hierarchy:</p>"
             "<pre><code>import 'package:flutter/material.dart';\n\nvoid main() {\n  runApp(const MyApp());\n}\n\nclass MyApp extends StatelessWidget {\n  const MyApp({super.key});\n  \n  @override\n  Widget build(BuildContext context) {\n    return MaterialApp(\n      home: Scaffold(\n        appBar: AppBar(title: const Text('Hello Flutter')),\n        body: const Center(\n          child: Text('Hello, World!',\n            style: TextStyle(fontSize: 24)),\n        ),\n      ),\n    );\n  }\n}</code></pre>"
             "<p>Widgets fall into two categories: <strong>StatelessWidget</strong> (immutable configuration) and <strong>StatefulWidget</strong> (mutable state that triggers rebuilds). Build methods should be pure -- side effects belong in lifecycle methods.</p>"),
            ("State Management Approaches",
             "<p>Flutter offers multiple state management solutions. Provider is the recommended starting point:</p>"
             "<pre><code>// 1. Provider (simple DI)\nclass Counter extends ChangeNotifier {\n  int _count = 0;\n  int get count => _count;\n  void increment() {\n    _count++;\n    notifyListeners();\n  }\n}\n\n// 2. Riverpod (compile-safe, testable)\nfinal counterProvider = StateNotifierProvider&lt;CounterNotifier, int&gt;((ref) {\n  return CounterNotifier();\n});\n\n// 3. BLoC (event-driven, enterprise)\nclass CounterCubit extends Cubit&lt;int&gt; {\n  CounterCubit() : super(0);\n  void increment() => emit(state + 1);\n}</code></pre>"
             "<p>Choose Provider for simple apps, Riverpod for medium complexity, and BLoC for large enterprise applications.</p>"),
            ("Navigation & Routing",
             "<p>Flutter provides declarative routing with GoRouter, replacing the older Navigator 1.0 approach:</p>"
             "<pre><code>// pubspec.yaml\ndependencies:\n  go_router: ^14.0.0\n\n// Router configuration\nfinal router = GoRouter(\n  initialLocation: '/',\n  routes: [\n    GoRoute(\n      path: '/',\n      builder: (context, state) => const HomeScreen(),\n    ),\n    GoRoute(\n      path: '/details/:id',\n      builder: (context, state) => DetailsScreen(\n        id: state.pathParameters['id']!,\n      ),\n    ),\n  ],\n);\n\n// Navigate\ncontext.go('/details/42');\ncontext.pop();</code></pre>"),
            ("Platform Integration & Packages",
             "<p>Access native platform features through packages from pub.dev:</p>"
             "<pre><code># pubspec.yaml\ndependencies:\n  http: ^1.2.0           # HTTP requests\n  shared_preferences: ^2.3.0  # Key-value storage\n  camera: ^0.11.0        # Camera access\n  firebase_core: ^3.1.0  # Firebase integration\n  google_maps_flutter: ^2.9.0  # Maps</code></pre>"
             "<p>Use <strong>MethodChannels</strong> to write custom platform-specific code in Kotlin/Swift when a package doesn't exist. Flutter's platform channels are bi-directional and support asynchronous calls.</p>"),
        ],
        [
            ("Flutter Documentation", "https://docs.flutter.dev/", "Official Flutter development guides"),
            ("Dart Language Tour", "https://dart.dev/language", "Learn Dart, the language behind Flutter"),
            ("pub.dev Packages", "https://pub.dev/", "Flutter and Dart package repository"),
        ]
    )

    # 7. GraphQL
    build_page(
        "GraphQL API Design",
        "graphql-basics.html",
        "Schema design, resolvers, queries, mutations, subscriptions, and Apollo GraphQL ecosystem.",
        "Programming",
        "fas fa-code",
        [
            ("What is GraphQL?",
             "<p>GraphQL is a query language and runtime for APIs developed by Facebook. Unlike REST, GraphQL lets clients request exactly the data they need, nothing more and nothing less. This eliminates over-fetching and under-fetching problems.</p>"
             "<p>Key concepts:</p>"
             "<ul><li><strong>Schema</strong> -- defines types and operations available</li>"
             "<li><strong>Query</strong> -- read data (like GET)</li>"
             "<li><strong>Mutation</strong> -- write data (like POST/PUT/DELETE)</li>"
             "<li><strong>Subscription</strong> -- real-time data (WebSocket)</li></ul>"
             "<p>GraphQL can be used with any backend language. Apollo Server (Node.js) and graphql-ruby are popular implementations.</p>"),
            ("Schema Design & Type System",
             "<p>The schema is the contract between client and server. It uses a human-readable SDL (Schema Definition Language):</p>"
             "<pre><code>type Query {\n  user(id: ID!): User\n  users(limit: Int, offset: Int): [User!]!\n  search(query: String!): [SearchResult!]!\n}\n\ntype Mutation {\n  createUser(input: CreateUserInput!): User!\n  updateUser(id: ID!, input: UpdateUserInput!): User!\n  deleteUser(id: ID!): Boolean!\n}\n\ntype User {\n  id: ID!\n  name: String!\n  email: String!\n  posts: [Post!]!\n  createdAt: DateTime!\n}\n\ntype Post {\n  id: ID!\n  title: String!\n  content: String!\n  author: User!\n  comments: [Comment!]!\n}\n\ninput CreateUserInput {\n  name: String!\n  email: String!\n  password: String!\n}</code></pre>"),
            ("Resolvers & Data Fetching",
             "<p>Resolvers are functions that fetch data for each field. They can call databases, REST APIs, or other services:</p>"
             "<pre><code>const resolvers = {\n  Query: {\n    user: async (_, { id }, { db }) => {\n      return db.users.findUnique({ where: { id } });\n    },\n    users: async (_, { limit, offset }, { db }) => {\n      return db.users.findMany({ take: limit, skip: offset });\n    },\n  },\n  User: {\n    posts: async (parent, _, { db }) => {\n      return db.posts.findMany({ where: { authorId: parent.id } });\n    },\n  },\n  Mutation: {\n    createUser: async (_, { input }, { db }) => {\n      return db.users.create({ data: input });\n    },\n  },\n};</code></pre>"
             "<p>The <strong>DataLoader</strong> pattern batches and caches database calls to solve the N+1 query problem. Dataloader coalesces individual requests within a single event-loop tick.</p>"),
            ("Subscriptions for Real-Time Data",
             "<p>Subscriptions use WebSocket connections to push real-time data to clients:</p>"
             "<pre><code># Schema\ntype Subscription {\n  postAdded: Post!\n  commentAdded(postId: ID!): Comment!\n}\n\n# Server (Apollo)\nconst pubsub = new PubSub();\n\nconst resolvers = {\n  Subscription: {\n    postAdded: {\n      subscribe: () => pubsub.asyncIterator(['POST_ADDED']),\n    },\n  },\n  Mutation: {\n    createPost: async (_, { input }, { db }) => {\n      const post = await db.posts.create({ data: input });\n      pubsub.publish('POST_ADDED', { postAdded: post });\n      return post;\n    },\n  },\n};</code></pre>"
             "<p>For production, use a persistent message broker like Redis for PubSub to support horizontal scaling.</p>"),
            ("Security & Best Practices",
             "<p>Securing a GraphQL API requires specific considerations:</p>"
             "<ul><li><strong>Depth limiting</strong> -- prevent deeply nested queries</li>"
             "<li><strong>Query cost analysis</strong> -- reject expensive queries</li>"
             "<li><strong>Rate limiting</strong> -- per-IP or per-token limits</li>"
             "<li><strong>Authentication</strong> -- validate JWT tokens in context</li>"
             "<li><strong>Authorization</strong> -- field-level permission checks</li>"
             "<li><strong>Persisted queries</strong> -- allow only pre-registered queries in production</li></ul>"
             "<pre><code>// Apollo Server with depth limiting\nimport depthLimit from 'graphql-depth-limit';\n\nconst server = new ApolloServer({\n  typeDefs,\n  resolvers,\n  validationRules: [depthLimit(10)],\n});</code></pre>"),
        ],
        [
            ("GraphQL Foundation", "https://graphql.org/learn/", "Official GraphQL specification and learning resources"),
            ("Apollo GraphQL Documentation", "https://www.apollographql.com/docs/", "Apollo client and server documentation"),
            ("HowToGraphQL", "https://www.howtographql.com/", "Full-stack GraphQL tutorial series"),
        ]
    )

    # 8. gRPC
    build_page(
        "gRPC & Protocol Buffers",
        "grpc-basics.html",
        "High-performance RPC with Protobuf -- define services, generate clients/servers, streaming, and best practices.",
        "Programming",
        "fas fa-code",
        [
            ("What is gRPC?",
             "<p>gRPC is a high-performance, open-source RPC framework developed by Google. It uses Protocol Buffers (Protobuf) as the interface definition language and binary serialization format. gRPC is built on HTTP/2, enabling multiplexed streams, flow control, and bidirectional streaming.</p>"
             "<p>Key advantages over REST:</p>"
             "<ul><li>Strongly-typed service contracts via <code>.proto</code> files</li>"
             "<li>Binary serialization (smaller, faster than JSON)</li>"
             "<li>HTTP/2 multiplexing -- single connection handles multiple streams</li>"
             "<li>Four communication patterns: unary, server-streaming, client-streaming, bidirectional</li>"
             "<li>Built-in authentication, load balancing, and tracing</li></ul>"),
            ("Protocol Buffers (Protobuf) Definition",
             "<p>Protobuf is the interface definition language for gRPC. Define your services and messages in <code>.proto</code> files:</p>"
             "<pre><code>syntax = \"proto3\";\n\npackage users;\n\nservice UserService {\n  rpc GetUser (GetUserRequest) returns (User);\n  rpc ListUsers (ListUsersRequest) returns (stream User);\n  rpc CreateUser (stream CreateUserRequest) returns (User);\n  rpc Chat (stream ChatMessage) returns (stream ChatMessage);\n}\n\nmessage User {\n  string id = 1;\n  string name = 2;\n  string email = 3;\n  int32 age = 4;\n  repeated string tags = 5;\n}\n\nmessage GetUserRequest {\n  string id = 1;\n}\n\nmessage ListUsersRequest {\n  int32 page_size = 1;\n  string page_token = 2;\n}</code></pre>"
             "<p>Field numbers (1, 2, 3...) are used for binary encoding. Numbers 1-15 use 1 byte, 16-2047 use 2 bytes. Reserve field numbers for backward compatibility.</p>"),
            ("Generating Code & Building Services",
             "<p>Generate client and server code from proto files using <code>protoc</code>:</p>"
             "<pre><code># Install protoc and Go plugins\nsudo apt install protobuf-compiler\ngo install google.golang.org/protobuf/cmd/protoc-gen-go@latest\ngo install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest\n\n# Generate code\nprotoc --go_out=. --go-grpc_out=. users.proto\n\n# Python\ngrpc_tools_protoc -I. --python_out=. --grpc_python_out=. users.proto</code></pre>"
             "<p>Implement the generated server interface:</p>"
             "<pre><code>// Go server\npackage main\n\ntype userServer struct {\n    pb.UnimplementedUserServiceServer\n}\n\nfunc (s *userServer) GetUser(ctx context.Context, req *pb.GetUserRequest) (*pb.User, error) {\n    user, err := db.FindUser(req.Id)\n    if err != nil {\n        return nil, status.Errorf(codes.NotFound, \"user not found\")\n    }\n    return user, nil\n}\n\nfunc main() {\n    lis, _ := net.Listen(\"tcp\", \":50051\")\n    s := grpc.NewServer()\n    pb.RegisterUserServiceServer(s, &amp;userServer{})\n    s.Serve(lis)\n}</code></pre>"),
            ("Streaming Patterns",
             "<p>gRPC supports four streaming patterns beyond simple request-response:</p>"
             "<pre><code>// Server-side streaming -- send multiple responses\nrpc ListUsers(ListUsersRequest) returns (stream User);\n\nfunc (s *userServer) ListUsers(req *pb.ListUsersRequest, stream pb.UserService_ListUsersServer) error {\n    users, _ := db.GetAllUsers()\n    for _, u := range users {\n        if err := stream.Send(u); err != nil {\n            return err\n        }\n    }\n    return nil\n}\n\n// Client-side streaming -- receive multiple requests\nrpc CreateUser(stream CreateUserRequest) returns (User);\n\n// Bidirectional streaming -- both sides send independently\nrpc Chat(stream ChatMessage) returns (stream ChatMessage);</code></pre>"
             "<p>Streaming is ideal for large datasets, file uploads, real-time messaging, and event processing.</p>"),
            ("Interceptors, Deadlines & Best Practices",
             "<p>gRPC provides powerful middleware and control mechanisms:</p>"
             "<pre><code>// Unary interceptor (middleware)\nfunc loggingInterceptor(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, handler grpc.UnaryHandler) (interface{}, error) {\n    log.Printf(\"method: %s, request: %v\", info.FullMethod, req)\n    resp, err := handler(ctx, req)\n    log.Printf(\"response: %v, error: %v\", resp, err)\n    return resp, err\n}\n\n// Set deadline on client\nctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)\ndefer cancel()\nuser, err := client.GetUser(ctx, &amp;pb.GetUserRequest{Id: \"123\"})</code></pre>"
             "<ul><li>Always set deadlines/timeouts on client calls</li>"
             "<li>Use TLS for production communication</li>"
             "<li>Enable gRPC reflection for debugging tools like grpcurl</li>"
             "<li>Use <strong>gRPC-Web</strong> for browser clients (requires Envoy proxy)</li></ul>"),
        ],
        [
            ("gRPC Documentation", "https://grpc.io/docs/", "Official gRPC documentation and tutorials"),
            ("Protobuf Language Guide", "https://protobuf.dev/programming-guides/proto3/", "Protocol Buffers version 3 language guide"),
            ("gRPC Best Practices", "https://grpc.io/docs/guides/", "Official gRPC best practices and patterns"),
        ]
    )

    # 9. Design Patterns
    build_page(
        "Software Design Patterns",
        "design-patterns.html",
        "GoF patterns: creational, structural, and behavioral -- with practical examples and modern language idioms.",
        "Programming",
        "fas fa-code",
        [
            ("Creational Patterns",
             "<p>Creational patterns abstract object instantiation, making systems independent of how objects are created:</p>"
             "<p><strong>Singleton</strong> -- ensures a class has only one instance:</p>"
             "<pre><code>class Database {\n  static final Database _instance = Database._internal();\n  Database._internal();\n  factory Database() => _instance;\n}\n\n// Usage\ndb1 = Database()\ndb2 = Database()\ndb1 === db2  // true</code></pre>"
             "<p><strong>Factory Method</strong> -- lets subclasses decide which class to instantiate. <strong>Builder</strong> separates construction from representation, useful for objects with many optional parameters. <strong>Prototype</strong> clones objects instead of creating from scratch.</p>"),
            ("Structural Patterns",
             "<p>Structural patterns compose classes and objects into larger structures:</p>"
             "<p><strong>Adapter</strong> -- allows incompatible interfaces to work together:</p>"
             "<pre><code>// Legacy XML service\nclass XmlService {\n  String getXml() => \"&lt;user&gt;Alice&lt;/user&gt;\";\n}\n\n// Target interface\nabstract class JsonService {\n  Map&lt;String, dynamic&gt; getJson();\n}\n\nclass XmlToJsonAdapter implements JsonService {\n  final XmlService _xmlService;\n  \n  XmlToJsonAdapter(this._xmlService);\n  \n  @override\n  Map&lt;String, dynamic&gt; getJson() {\n    final xml = _xmlService.getXml();\n    // Parse XML and convert to JSON map\n    return {'user': 'Alice'};\n  }\n}</code></pre>"
             "<p><strong>Decorator</strong> adds behavior dynamically (Python decorators are a language-level example). <strong>Facade</strong> provides a simplified interface to a complex subsystem.</p>"),
            ("Behavioral Patterns",
             "<p>Behavioral patterns manage algorithms, relationships, and responsibilities between objects:</p>"
             "<p><strong>Observer</strong> -- notifies multiple objects of state changes (pub/sub):</p>"
             "<pre><code>class EventEmitter {\n  final _listeners = &lt;String, List&lt;Function&gt;&gt;{};\n  \n  void on(String event, Function handler) {\n    _listeners.putIfAbsent(event, () =&gt; []).add(handler);\n  }\n  \n  void emit(String event, [dynamic data]) {\n    _listeners[event]?.forEach((fn) =&gt; fn(data));\n  }\n}</code></pre>"
             "<p><strong>Strategy</strong> -- selects an algorithm at runtime (think sorting strategies). <strong>State</strong> -- changes object behavior when its state changes (e.g., TCP connection states). <strong>Command</strong> -- encapsulates requests as objects for undo/redo queues.</p>"),
            ("Modern Pattern Usage & Anti-Patterns",
             "<p>Modern languages and frameworks have absorbed many classic patterns:</p>"
             "<ul><li><strong>Dependency Injection</strong> replaces the Service Locator pattern -- use DI containers like Spring, .NET DI, or GetIt</li>"
             "<li><strong>Functional patterns</strong> (map, filter, reduce) replace Iterator and Command in many cases</li>"
             "<li><strong>Composition over inheritance</strong> -- mixins, traits, and extension methods reduce need for Template Method</li></ul>"
             "<p>Common anti-patterns to avoid:</p>"
             "<ul><li><strong>God Object</strong> -- a class that knows too much or does too much</li>"
             "<li><strong>Spaghetti Code</strong> -- unclear control flow, usually from excessive gotos or deeply nested conditionals</li>"
             "<li><strong>Premature Optimization</strong> -- optimizing before profiling, leading to complex, unreadable code</li>"
             "<li><strong>Copy-Paste Programming</strong> -- duplicating code instead of abstracting it</li></ul>"),
        ],
        [
            ("Refactoring.Guru -- Design Patterns", "https://refactoring.guru/design-patterns", "Comprehensive catalog with code examples"),
            ("GoF Design Patterns Book", "https://en.wikipedia.org/wiki/Design_Patterns", "Original Gang of Four patterns reference"),
            ("SourceMaking -- Design Patterns", "https://sourcemaking.com/design_patterns", "Pattern catalog with anti-patterns"),
        ]
    )

    # 10. Clean Code
    build_page(
        "Clean Code Principles",
        "clean-code.html",
        "Naming, functions, comments, error handling, refactoring, and writing maintainable software.",
        "Programming",
        "fas fa-code",
        [
            ("Meaningful Names & Code as Documentation",
             "<p>Good names reduce the need for comments. Names should reveal intent, avoid disinformation, and be pronounceable:</p>"
             "<pre><code>// Bad\nint d; // elapsed days\nList&lt;int&gt; lst;\nbool flg;\n\n// Good\nint elapsedDays;\nList&lt;int&gt; userIds;\nbool isComplete;\n\n// Classes and objects should have noun or noun phrase names\nclass Customer {}\nclass AccountProcessor {}\n\n// Methods should have verb or verb phrase names\nvoid save() {}\nvoid deleteAccount() {}\nbool hasValidAddress() {}</code></pre>"
             "<p>Use consistent naming conventions across your codebase. Choose one style and stick to it -- do not mix <code>snake_case</code>, <code>camelCase</code>, and <code>PascalCase</code> arbitrarily.</p>"),
            ("Functions: Small, Focused, Pure",
             "<p>Functions should do one thing and do it well. The ideal function is small (4-20 lines), with no side effects:</p>"
             "<pre><code>// Bad -- too many responsibilities\nvoid processOrder(Order order) {\n  validateOrder(order);\n  calculateTotals(order);\n  applyDiscount(order);\n  chargeCustomer(order);\n  sendConfirmation(order);\n  updateInventory(order);\n}\n\n// Good -- each function has one clear purpose\nvoid processOrder(Order order) {\n  order.validate();\n  order.calculateTotal();\n  paymentProcessor.charge(order);\n  notificationService.sendConfirmation(order);\n  inventoryService.update(order);\n}</code></pre>"
             "<p>Avoid output arguments (modifying parameters). Prefer returning values. Keep the number of parameters to 0-2; if you need more, group them into an object.</p>"),
            ("Comments: Why, Not What",
             "<p>Comments should explain <em>why</em> something is done, not <em>what</em> the code does. The code itself should be self-explanatory:</p>"
             "<pre><code>// Bad -- states the obvious\ni += 1;  // Increment i by 1\n\n// Good -- explains rationale\n// Retry up to 3 times because the upstream service\n// occasionally returns 503 during deployments\nfor (int attempt = 0; attempt &lt; 3; attempt++) {\n  try {\n    return api.call();\n  } catch (ServiceUnavailableException e) {\n    if (attempt == 2) throw;\n  }\n}\n\n// TODO comments should include a date or ticket number\n// TODO(2026-06): SC-452 -- Replace with new auth service</code></pre>"
             "<p>A comment that contradicts the code is worse than no comment. When you change code, always update the accompanying comments. Better yet, refactor the code so the comment becomes unnecessary.</p>"),
            ("Error Handling & Boundary Conditions",
             "<p>Use exceptions, not return codes. Separate error handling from business logic:</p>"
             "<pre><code>// Bad -- mixing error handling with logic\nif (deleteFile(path) == ERROR) {\n  logError(\"Failed to delete\");\n  return ERROR;\n}\n\n// Good -- use exceptions\npublic void deletePath(String path) {\n  try {\n    fileSystem.delete(path);\n  } catch (IOException e) {\n    throw new StorageException(\"Unable to delete: \" + path, e);\n  }\n}</code></pre>"
             "<p>Don't return null -- return empty collections or Optional. Don't pass null. Provide context with exceptions: include the operation that failed and the state of relevant variables.</p>"),
            ("Refactoring: The Boy Scout Rule",
             "<p>The Boy Scout Rule: Leave the campground cleaner than you found it. When you touch a file, improve it:</p>"
             "<ul><li><strong>Extract method</strong> -- break large methods into smaller ones</li>"
             "<li><strong>Rename</strong> -- improve variable, function, and class names</li>"
             "<li><strong>Move</strong> -- relocate methods to more appropriate classes</li>"
             "<li><strong>Extract class</strong> -- split large classes into focused ones</li>"
             "<li><strong>Remove duplication</strong> -- DRY (Don't Repeat Yourself)</li></ul>"
             "<p>Use automated refactoring tools in your IDE. Run tests after each small refactoring step. Commit frequently so you can revert if something breaks.</p>"),
        ],
        [
            ("Clean Code by Robert C. Martin", "https://www.oreilly.com/library/view/clean-code/9780136083238/", "The seminal book on clean code principles"),
            ("Google Style Guides", "https://google.github.io/styleguide/", "Google's coding style guides by language"),
            ("Refactoring by Martin Fowler", "https://martinfowler.com/books/refactoring.html", "Catalog of refactoring techniques"),
        ]
    )

    # 11. Code Review
    build_page(
        "Code Review Best Practices",
        "code-review.html",
        "Constructive feedback, security checks, PR etiquette, and building a review culture.",
        "Programming",
        "fas fa-code",
        [
            ("The Purpose of Code Review",
             "<p>Code review is a systematic examination of code changes by developers other than the author. It serves multiple purposes beyond finding bugs:</p>"
             "<ul><li><strong>Knowledge sharing</strong> -- team members learn from each other's code and domain knowledge</li>"
             "<li><strong>Consistency</strong> -- ensures code follows team conventions and standards</li>"
             "<li><strong>Design improvement</strong> -- catches architectural issues early</li>"
             "<li><strong>Security</strong> -- identifies vulnerabilities before they reach production</li>"
             "<li><strong>Ownership</strong> -- spreads codebase knowledge across the team</li></ul>"
             "<p>Studies show that code review catches 60-90% of defects when done properly, making it one of the most cost-effective quality practices.</p>"),
            ("What to Look For",
             "<p>Review code at multiple levels of abstraction:</p>"
             "<p><strong>Architecture & Design</strong>:</p>"
             "<ul><li>Does this change fit the existing architecture?</li>"
             "<li>Are there unnecessary dependencies or coupling?</li>"
             "<li>Is there over-engineering (patterns where simple code would do)?</li></ul>"
             "<p><strong>Correctness & Logic</strong>:</p>"
             "<ul><li>Are edge cases handled? (empty inputs, boundaries, nulls)</li>"
             "<li>Are there off-by-one errors or race conditions?</li>"
             "<li>Do error paths release resources properly?</li></ul>"
             "<p><strong>Security & Performance</strong>:</p>"
             "<ul><li>Are inputs validated and sanitized?</li>"
             "<li>Are there SQL injection or XSS vulnerabilities?</li>"
             "<li>Are there obvious performance issues (N+1 queries, unnecessary allocations)?</li></ul>"),
            ("Giving Effective Feedback",
             "<p>Feedback should be constructive, specific, and respectful:</p>"
             "<pre><code>// Instead of: \"This is wrong\"\n// Say:\n\"This SQL query inside the loop will cause N+1 database calls.\nConsider using eager loading or a batch query instead.\"\n\n// Instead of: \"Bad variable name\"\n// Say:\n\"`data` is too vague. Since this contains user profile fields,\nhow about `userProfile` or `profileData`?\"</code></pre>"
             "<p>Use tags to categorize feedback:</p>"
             "<ul><li><strong>Nitpick</strong> -- minor style issues, non-blocking</li>"
             "<li><strong>Question</strong> -- seeking clarification, not a request for change</li>"
             "<li><strong>Suggestion</strong> -- improvement idea, author can decide</li>"
             "<li><strong>Blocking</strong> -- must be resolved before merge</li></ul>"
             "<p>Always explain <em>why</em> a change is needed, not just what to change.</p>"),
            ("PR Etiquette & Review Workflow",
             "<p>Best practices for pull requests:</p>"
             "<ul><li><strong>Keep PRs small</strong> -- ideally under 400 lines changed. Large PRs get shallow reviews</li>"
             "<li><strong>Write good descriptions</strong> -- explain what, why, and how to test</li>"
             "<li><strong>Self-review first</strong> -- review your own diff before requesting reviewers</li>"
             "<li><strong>Respond to feedback</strong> -- reply to each comment (agree, explain, or propose alternative)</li>"
             "<li><strong>Review within 24 hours</strong> -- fast reviews keep momentum</li>"
             "<li><strong>Use draft PRs</strong> for work-in-progress that isn't ready for review</li></ul>"
             "<p>A good review culture prioritizes psychological safety. The goal is to improve the code, not to judge the author.</p>"),
        ],
        [
            ("Google Code Review Guide", "https://google.github.io/eng-practices/review/", "Google's engineering practices for code review"),
            ("The Art of Code Review", "https://mtlynch.io/human-code-reviews-1/", "Human aspects of effective code review"),
            ("Conventional Comments", "https://conventionalcomments.org/", "Standardized format for review feedback"),
        ]
    )

    # 12. Functional Programming
    build_page(
        "Functional Programming Concepts",
        "functional-programming.html",
        "Pure functions, immutability, monads, currying, and applying FP in mainstream languages.",
        "Programming",
        "fas fa-code",
        [
            ("Core Principles of FP",
             "<p>Functional programming is a paradigm that treats computation as the evaluation of mathematical functions, avoiding mutable state and side effects. Key principles:</p>"
             "<ul><li><strong>Pure functions</strong> -- same input always produces same output, no side effects</li>"
             "<li><strong>Immutability</strong> -- data cannot be modified after creation, only transformed into new data</li>"
             "<li><strong>Referential transparency</strong> -- an expression can be replaced with its value without changing the program's behavior</li>"
             "<li><strong>Functions as first-class citizens</strong> -- functions can be passed as arguments, returned, and assigned to variables</li></ul>"
             "<p>These principles make programs easier to reason about, test, and parallelize.</p>"),
            ("Pure Functions & Side Effects",
             "<p>A pure function depends only on its inputs and produces no observable side effects:</p>"
             "<pre><code>// Impure -- depends on external state and mutates it\nlet counter = 0;\nfunction increment() {\n    counter++;\n    return counter;\n}\n\n// Pure -- no side effects, deterministic\nfunction increment(n) {\n    return n + 1;\n}\n\n// Impure -- modifies input array\nfunction addItem(items, item) {\n    items.push(item);\n    return items;\n}\n\n// Pure -- returns new array\nfunction addItem(items, item) {\n    return [...items, item];\n}</code></pre>"
             "<p>Pure functions are easy to test (no mocks needed), cacheable (memoization), and can be run in parallel safely.</p>"),
            ("Higher-Order Functions & Currying",
             "<p>Higher-order functions take functions as arguments or return functions. Currying transforms a multi-argument function into a chain of single-argument functions:</p>"
             "<pre><code>// Higher-order function\nfunction filter(predicate) {\n    return function(array) {\n        return array.filter(predicate);\n    };\n}\n\nconst isEven = n => n % 2 === 0;\nconst getEvens = filter(isEven);\ngetEvens([1, 2, 3, 4]);  // [2, 4]\n\n// Currying\ndef add(a: Int)(b: Int): Int = a + b\nval addFive = add(5)_\naddFive(3)  // 8\n\n// JavaScript curried version\nconst add = a => b => a + b;\nconst addFive = add(5);\naddFive(3);  // 8</code></pre>"
             "<p>Partial application (pre-filling some arguments) is closely related to currying and enables function reuse.</p>"),
            ("Immutability & Persistent Data Structures",
             "<p>Immutability means data never changes. Instead of modifying, create new data with the changes applied:</p>"
             "<pre><code>// Mutable approach\nconst user = { name: 'Alice', age: 30 };\nuser.age = 31;  // mutation\n\n// Immutable approach\nconst user = { name: 'Alice', age: 30 };\nconst updatedUser = { ...user, age: 31 };\n\n// Persistent data structures share structure between versions\n// Implementations: Immutable.js, Immer, Clojure's vectors/maps\n\n// List operations produce new lists\nconst numbers = [1, 2, 3];\nconst added = [0, ...numbers];  // [0, 1, 2, 3] -- original unchanged\nconst mapped = numbers.map(n => n * 2);  // [2, 4, 6]</code></pre>"
             "<p>Persistent data structures use structural sharing to make immutability efficient -- only the path to the changed element is copied, not the entire data structure.</p>"),
            ("Monads & Functors",
             "<p>Functors and monads are abstractions for applying functions in a context (like Optional, List, or Promise):</p>"
             "<pre><code>// Functor -- has a `map` method\nOptional.of(5).map(x => x * 2);  // Optional.of(10)\n[1, 2, 3].map(x => x * 2);      // [2, 4, 6]\n\n// Monad -- has `flatMap` (or `bind`, `chain`)\n// Handles nested contexts\nOptional.of(5)\n    .flatMap(x => Optional.of(x * 2))\n    .flatMap(x => Optional.of(x + 1));  // Optional.of(11)\n\n// Maybe monad (null-safe chaining)\nconst result = Maybe.fromNullable(user)\n    .map(u => u.address)\n    .map(a => a.city)\n    .getOrElse('Unknown');</code></pre>"
             "<p>In practice, you use monads whenever you chain operations that return Optional, Result, Promise, or Stream -- these are all monadic types.</p>"),
        ],
        [
            ("Learn You a Haskell for Great Good", "http://learnyouahaskell.com/", "Gentle introduction to functional programming"),
            ("Functional Programming Jargon", "https://github.com/hemanth/functional-programming-jargon", "Glossary of FP terms with examples"),
            ("Mostly Adequate Guide to FP", "https://mostly-adequate.gitbook.io/mostly-adequate-guide/", "Practical FP in JavaScript"),
        ]
    )

    # 13. Makefile
    build_page(
        "Makefile Build Automation",
        "makefile-guide.html",
        "Targets, variables, pattern rules, and best practices for cross-platform build automation.",
        "Programming",
        "fas fa-code",
        [
            ("Makefile Fundamentals",
             "<p>Make is a build automation tool that reads <code>Makefile</code> instructions to build targets. A Makefile consists of rules, variables, and functions:</p>"
             "<pre><code># Basic Makefile structure\ntarget: dependencies\n\tcommands\n\n# Example: compile a C program\nmyapp: main.o utils.o\n\tgcc -o myapp main.o utils.o\n\nmain.o: main.c main.h\n\tgcc -c main.c\n\nutils.o: utils.c utils.h\n\tgcc -c utils.c\n\nclean:\n\trm -f *.o myapp\n\n.PHONY: clean  # Prevents conflicts with file named 'clean'</code></pre>"
             "<p>Make checks file timestamps -- it only rebuilds targets whose dependencies have changed since the last build.</p>"),
            ("Variables & Automatic Variables",
             "<p>Variables make Makefiles maintainable. Automatic variables simplify rule definitions:</p>"
             "<pre><code># User-defined variables\nCC = gcc\nCFLAGS = -Wall -O2 -std=c11\nLDFLAGS = -lm\nTARGET = myapp\nSRCDIR = src\nOBJDIR = obj\n\nSRCS = $(wildcard $(SRCDIR)/*.c)\nOBJS = $(patsubst $(SRCDIR)/%.c, $(OBJDIR)/%.o, $(SRCS))\n\n# Automatic variables\n# $@  -- target name\n# $&lt;  -- first prerequisite\n# $^  -- all prerequisites\n$(OBJDIR)/%.o: $(SRCDIR)/%.c | $(OBJDIR)\n\t$(CC) $(CFLAGS) -c $&lt; -o $@\n\n$(OBJDIR):\n\tmkdir -p $@\n\n$(TARGET): $(OBJS)\n\t$(CC) $^ -o $@ $(LDFLAGS)</code></pre>"),
            ("Pattern Rules & Functions",
             "<p>Pattern rules use <code>%</code> wildcard to apply rules generically. Make functions manipulate strings and files:</p>"
             "<pre><code># Pattern rule -- compile all .c files\n%.o: %.c\n\t$(CC) $(CFLAGS) -c $&lt; -o $@\n\n# String substitution\nNAME = project_v2\nUPPER = $(shell echo $(NAME) | tr a-z A-Z)  # PROJECT_V2\n\n# Conditional\nifeq ($(OS),Windows_NT)\n    RM = del /Q\n    EXT = .exe\nelse\n    RM = rm -f\n    EXT =\nendif\n\n# File functions\nSRC_FILES = $(wildcard src/*.c)\nHEADER_FILES = $(wildcard include/*.h)\n\n# Multi-line shell commands\nbuild:\n\t@echo \"Building $(TARGET)...\"\n\t$(CC) $(CFLAGS) -o $(TARGET) $(SRCS)\n\t@echo \"Done.\"</code></pre>"),
            ("Advanced Topics: Include, Make Flags & Debugging",
             "<p>Advanced Makefile features for real projects:</p>"
             "<pre><code># Include other Makefiles\n-include config.mk\ninclude $(wildcard makefiles/*.mk)\n\n# Parallel builds\n# make -j$(nproc)  -- run jobs in parallel\n\n# Dry run\n# make -n  -- print commands without executing\n\n# Debugging\n# make --debug=v  -- print detailed info\n\n# Output one value\ndebug:\n\t@echo \"CC=$(CC)\"\n\t@echo \"CFLAGS=$(CFLAGS)\"\n\t@echo \"OBJS=$(OBJS)\"</code></pre>"),
            ("Best Practices & Cross-Platform Tips",
             "<p>Write robust Makefiles that work across platforms:</p>"
             "<ul><li>Always use <code>.PHONY</code> for non-file targets (clean, install, test)</li>"
             "<li>Use <code>:=</code> (simply expanded) instead of <code>=</code> (recursively expanded) for better performance</li>"
             "<li>Prefix commands with <code>@</code> to suppress echoing</li>"
             "<li>Use <code>$(MAKE)</code> instead of <code>make</code> in recursive calls</li>"
             "<li>Support <code>DESTDIR</code> and <code>PREFIX</code> variables for install targets</li>"
             "<li>Check for required tools at the top of the Makefile</li>"
             "<li>Use <code>.DELETE_ON_ERROR</code> to clean up partially-built targets on failure</li></ul>"
             "<pre><code>.DELETE_ON_ERROR:\n\n# Check for required tools\nREQUIRED_TOOLS = python3 node cargo\n$(foreach tool,$(REQUIRED_TOOLS),\\(\n    $(if $(shell which $(tool)),,$(error \"Missing tool: $(tool)\")))</code></pre>"),
        ],
        [
            ("GNU Make Manual", "https://www.gnu.org/software/make/manual/", "Official GNU Make documentation"),
            ("Makefile Tutorial", "https://makefiletutorial.com/", "Interactive Makefile tutorial for beginners"),
            ("Managing Projects with GNU Make", "https://www.oreilly.com/library/view/managing-projects-with/0596006101/", "O'Reilly book on advanced Make usage"),
        ]
    )

    # 14. Modern Shell Scripting
    build_page(
        "Modern Shell Scripting (Zsh & Fish)",
        "modern-shell-scripting.html",
        "Syntax, functions, autocompletion, theming, and practical shell scripting in Zsh and Fish.",
        "Programming",
        "fas fa-code",
        [
            ("Zsh vs Fish vs Bash",
             "<p>Modern shells offer significant improvements over traditional Bash:</p>"
             "<ul><li><strong>Zsh</strong> -- backwards-compatible with Bash, with enhanced completion, globbing, and theming (Oh My Zsh)</li>"
             "<li><strong>Fish</strong> -- 'friendly interactive shell' with syntax highlighting, autosuggestions, and a web-based configuration</li>"
             "<li><strong>Bash</strong> -- the POSIX standard, available everywhere but lacking modern ergonomics</li></ul>"
             "<p>Check your current shell and change default:</p>"
             "<pre><code>echo $SHELL\nwhich zsh\nchsh -s $(which zsh)  # Change default shell\n\n# Install fish\nsudo apt install fish\nchsh -s $(which fish)</code></pre>"),
            ("Zsh Scripting & Configuration",
             "<p>Zsh scripts resemble Bash but with powerful enhancements:</p>"
             "<pre><code>#!/usr/bin/env zsh\n\n# Arrays are 1-indexed\nfruits=(\"apple\" \"banana\" \"cherry\")\necho $fruits[2]  # banana\n\n# Glob qualifiers -- filter by type, age, etc.\necho *.txt(.Om)  # Regular files, sorted by modification time\n\n# Extended globbing\nsetopt extended_glob\nls ^*.txt     # Everything except .txt files\nls **/*.py    # Recursive glob (already works)\n\n# Named directory expansion\nhash -d docs=~/Documents/projects\necho ~docs  # Expands to ~/Documents/projects</code></pre>"
             "<p>Customize Zsh with <code>~/.zshrc</code>. Use <strong>Oh My Zsh</strong> for plugin management and <strong>Powerlevel10k</strong> for theming.</p>"),
            ("Fish Scripting & Configuration",
             "<p>Fish has its own syntax -- not compatible with POSIX sh, but cleaner:</p>"
             "<pre><code>#!/usr/bin/env fish\n\n# Variables -- no $ for assignment\nset name \"Alice\"\necho $name\n\n# Lists (1-indexed)\nset fruits apple banana cherry\necho $fruits[2]  # banana\n\n# Functions\nfunction hello\n    set name $argv[1]\n    echo \"Hello, $name!\"\nend\n\nhello \"World\"\n\n# Command substitution uses () not $()\necho (date)\n\n# Conditional\ngrep -q \"error\" /var/log/syslog; and echo \"Found errors\"\n\n# Autoload functions from ~/.config/fish/functions/</code></pre>"
             "<p>Fish configuration is in <code>~/.config/fish/config.fish</code>. Use <strong>Fisher</strong> or <strong>Oh My Fish</strong> for plugin management.</p>"),
            ("Autocompletion & Prompt Customization",
             "<p>Modern shells excel at providing rich completions:</p>"
             "<pre><code># Zsh -- write completions\n# ~/.zsh/completion/_mycommand\n#compdef mycommand\n\n_mycommand() {\n  local -a subcommands\n  subcommands=(\n    'start:Start the service'\n    'stop:Stop the service'\n    'status:Show status'\n  )\n  _describe 'command' subcommands\n}\n\n# Prompt customization (Powerlevel10k)\n# In ~/.zshrc:\nsource ~/powerlevel10k/powerlevel10k.zsh-theme\n\n# Fish prompt customization\nfunction fish_prompt\n    set_color green\n    echo -n (prompt_pwd)\n    set_color normal\n    echo -n ' $ '\nend</code></pre>"
             "<p>Install popular prompt themes: <strong>Starship</strong> (cross-shell), <strong>Powerlevel10k</strong> (Zsh), <strong>Pure</strong> (Zsh/Fish).</p>"),
            ("Error Handling & Debugging",
             "<p>Modern shell scripts should include robust error handling:</p>"
             "<pre><code>#!/usr/bin/env zsh\n\nset -e          # Exit on error\nset -o pipefail # Fail pipeline if any command fails\nset -u          # Error on undefined variables\n\n# Trap errors for cleanup\ntrap 'echo \"Error on line $LINENO\"; cleanup' ERR\n\ncleanup() {\n    rm -f /tmp/build_*\n    echo \"Cleaned up\"\n}\n\n# Validate arguments\nif [[ $# -lt 1 ]]; then\n    echo \"Usage: $0 &lt;directory&gt;\" >&amp;2\n    exit 1\nfi\n\n# Debugging\nset -x  # Print commands before executing\n# ... debug code ...\nset +x  # Disable debug</code></pre>"),
        ],
        [
            ("Zsh Documentation", "https://zsh.sourceforge.io/Doc/", "Official Zsh reference manual"),
            ("Fish Shell Documentation", "https://fishshell.com/docs/current/", "Official Fish shell documentation"),
            ("Oh My Zsh", "https://ohmyz.sh/", "Community Zsh configuration framework"),
        ]
    )

    # 15. Graph Databases
    build_page(
        "Graph Databases & Neo4j",
        "graph-databases.html",
        "Cypher query language, Neo4j graph data modeling, and graph database use cases.",
        "Programming",
        "fas fa-code",
        [
            ("What are Graph Databases?",
             "<p>Graph databases store data as nodes (entities) and relationships (connections), with properties on both. This model excels at handling highly interconnected data -- social networks, recommendation engines, fraud detection, and knowledge graphs.</p>"
             "<p>Unlike relational databases, graph databases don't require expensive JOIN operations. Traversing relationships is a constant-time operation regardless of dataset size, making graph databases ideal for deep-path queries.</p>"
             "<p>Key terms:</p>"
             "<ul><li><strong>Node</strong> -- represents an entity (person, product, location)</li>"
             "<li><strong>Relationship</strong> -- connects nodes with direction, type, and properties</li>"
             "<li><strong>Property</strong> -- key-value pairs on nodes and relationships</li>"
             "<li><strong>Label</strong> -- categorizes nodes (e.g., :User, :Movie)</li></ul>"),
            ("Installing Neo4j & Cypher Basics",
             "<p>Install Neo4j locally or use Neo4j AuraDB (cloud):</p>"
             "<pre><code># Docker\ndocker run --publish=7474:7474 --publish=7687:7687 neo4j:5\n\n# Linux (deb)\nwget -O - https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -\necho \"deb https://debian.neo4j.com stable latest\" | sudo tee /etc/apt/sources.list.d/neo4j.list\nsudo apt update && sudo apt install neo4j\n\n# Access Neo4j Browser at http://localhost:7474</code></pre>"
             "<p>Cypher is Neo4j's declarative query language. It uses ASCII art for patterns:</p>"
             "<pre><code>// Create nodes and relationships\nCREATE (a:Person {name: 'Alice', age: 30})\nCREATE (b:Person {name: 'Bob', age: 32})\nCREATE (a)-[:FRIENDS_WITH {since: 2015}]->(b)\n\n// Query with pattern matching\nMATCH (a:Person {name: 'Alice'})-[:FRIENDS_WITH]->(friends)\nRETURN friends.name, friends.age\n\n// Find friends of friends\nMATCH (a:Person {name: 'Alice'})-[:FRIENDS_WITH]->()-[:FRIENDS_WITH]->(fof)\nRETURN DISTINCT fof.name</code></pre>"),
            ("Graph Data Modeling",
             "<p>Graph data modeling focuses on use cases (queries you need to run) rather than normalization:</p>"
             "<pre><code>// Relational-style model (less ideal for graphs)\nCREATE (u:User {id: 1, name: 'Alice'})\nCREATE (p:Product {id: 100, name: 'Laptop'})\nCREATE (o:Order {id: 5000, date: '2026-01-15'})\nCREATE (u)-[:PLACED]->(o)\nCREATE (o)-[:CONTAINS]->(p)\n\n// Query: products purchased by friends\nMATCH (me:User {name: 'Alice'})\nMATCH (me)-[:PLACED]->(:Order)-[:CONTAINS]->(p:Product)\nWITH COLLECT(DISTINCT p) AS myProducts\nMATCH (me)-[:FRIENDS_WITH]->(:User)-[:PLACED]->(:Order)-[:CONTAINS]->(friendProduct:Product)\nWHERE NOT friendProduct IN myProducts\nRETURN DISTINCT friendProduct.name</code></pre>"
             "<p>Modeling tips:</p>"
             "<ul><li>Prefer relationships over intermediate 'join' nodes</li>"
             "<li>Use relationship direction naturally -- Cypher can traverse both ways</li>"
             "<li>Store data as properties on relationships when context-dependent (e.g., <code>since: 2015</code> on FRIENDS_WITH)</li>"
             "<li>Use composite indexes for frequently queried property combinations</li></ul>"),
            ("Advanced Cypher: Aggregation, Paths & Procedures",
             "<p>Cypher is powerful for complex graph traversals:</p>"
             "<pre><code>// Shortest path\nMATCH p = SHORTEST 1 (\n  (a:Person {name: 'Alice'})-[:FRIENDS_WITH*]-(b:Person {name: 'Dave'})\n)\nRETURN [node IN nodes(p) | node.name] AS path\n\n// Variable-length paths\nMATCH (a:Person {name: 'Alice'})-[:ACTED_IN*1..3]->(movie:Movie)\nRETURN DISTINCT movie.title\n\n// Aggregation\nMATCH (d:Director)-[:DIRECTED]->(m:Movie)\nRETURN d.name, COUNT(m) AS movieCount\nORDER BY movieCount DESC\n\n// Built-in procedures\nCALL db.schema.visualization()\nCALL db.index.fulltext.queryNodes('movies', 'matrix') YIELD node\nRETURN node.title\n\n// APOC library -- utility procedures\nCALL apoc.load.json(\"https://api.example.com/movies\") YIELD value\nMERGE (m:Movie {id: value.id})\nSET m.title = value.title</code></pre>"),
            ("Use Cases & Scaling",
             "<p>Graph databases excel in specific domains:</p>"
             "<ul><li><strong>Recommendation engines</strong> -- collaborative filtering through user-item relationships</li>"
             "<li><strong>Fraud detection</strong> -- find rings of fraudulent accounts through shared devices, IPs, or addresses</li>"
             "<li><strong>Knowledge graphs</strong> -- Wikipedia, Wikidata, enterprise knowledge bases</li>"
             "<li><strong>Social networks</strong> -- friend suggestions, feed ranking, influence propagation</li>"
             "<li><strong>Network & IT operations</strong> -- dependency graphs, root cause analysis</li></ul>"
             "<p>Neo4j scales through clustering (causal clustering with read replicas), sharding (Neo4j 5+), and optimized page cache configuration for in-memory traversal performance.</p>"),
        ],
        [
            ("Neo4j Documentation", "https://neo4j.com/docs/", "Official Neo4j product documentation"),
            ("Cypher Query Language Reference", "https://neo4j.com/docs/cypher-manual/", "Complete Cypher language reference"),
            ("Graph Databases Book (O'Reilly)", "https://www.oreilly.com/library/view/graph-databases/9781491930885/", "Comprehensive guide to graph databases"),
        ]
    )

    # ========== LINUX (10) ==========

    # 16. PipeWire
    build_page(
        "Linux Audio with PipeWire",
        "pipewire-audio.html",
        "Setup, routing, low-latency configuration, Bluetooth audio, and professional audio workflows.",
        "Linux",
        "fab fa-linux",
        [
            ("PipeWire Overview",
             "<p>PipeWire is a modern multimedia server for Linux that handles audio and video streams. It was designed to replace both PulseAudio (consumer audio) and JACK (professional audio) with a single unified system. PipeWire provides low-latency performance, per-application volume control, and secure screen sharing.</p>"
             "<p>Most major distributions now ship PipeWire by default. If your system still uses PulseAudio, switching is straightforward:</p>"
             "<pre><code># Debian/Ubuntu\nsudo apt install pipewire pipewire-pulse wireplumber\nsystemctl --user disable --now pulseaudio\nsystemctl --user enable --now pipewire pipewire-pulse\n\n# Fedora\nsudo dnf install pipewire pipewire-pulsewire wireplumber</code></pre>"),
            ("Configuration & Low-Latency Tuning",
             "<p>PipeWire's configuration files live in <code>/etc/pipewire/</code> and <code>~/.config/pipewire/</code>. For real-time audio production, tune these settings:</p>"
             "<pre><code># ~/.config/pipewire/pipewire.conf.d/low-latency.conf\ncontext.properties = {\n    # Default sample rate\n    default.clock.rate = 48000\n    \n    # Buffer size (lower = less latency, more CPU)\n    # 256 = ~5ms, 128 = ~3ms, 64 = ~1.3ms\n    default.clock.quantum = 256\n    \n    # Min/max quantum for dynamic adjustment\n    default.clock.min-quantum = 64\n    default.clock.max-quantum = 2048\n}</code></pre>"
             "<p>For USB audio interfaces, check supported sample rates and buffer sizes. Use <code>pw-top</code> to monitor DSP load and <code>pw-cli info</code> to inspect devices.</p>"),
            ("Routing Audio with WirePlumber & qpwgraph",
             "<p>WirePlumber is the session manager for PipeWire. It handles device enumeration and routing policies. For manual routing, use patchbay tools:</p>"
             "<pre><code># Install qpwgraph (GUI patchbay)\nsudo apt install qpwgraph\n\n# Command-line routing\n# List nodes\npw-cli list-objects Node\n\n# Disconnect default audio sink\npw-cli disconnect \"alsa_output.pci-0000_00_1f.3.analog-stereo\"\n\n# Connect application to specific output\npw-link \"Firefox\" \"alsa_output.usb-Scarlett_Solo-00.analog-stereo\"</code></pre>"
             "<p>Use <strong>qpwgraph</strong> for visual routing -- drag connections between application outputs and hardware inputs/outputs. This is essential for podcasting, streaming, or music production setups.</p>"),
            ("Bluetooth Audio & Codecs",
             "<p>PipeWire supports Bluetooth audio codecs including SBC, AAC, LDAC, aptX, and LC3 (LE Audio):</p>"
             "<pre><code># Install Bluetooth audio support\nsudo apt install libspa-0.2-bluetooth\n\n# Check Bluetooth device codec\npw-cli list-objects Node | grep -A 20 \"bluez\"\n\n# Configure codec priority\n# ~/.config/wireplumber/bluetooth.lua.d/51-codec.lua\nbluetooth.codecs = [\n    \"ldac\",\n    \"aptx_hd\",\n    \"aac\",\n    \"sbc_xq\",\n    \"sbc\"\n]</code></pre>"
             "<p>Enable LE Audio with LC3 codec for lower latency and improved battery life: <code>sudo apt install libspa-0.2-bluetooth-lc3</code>.</p>"),
            ("Troubleshooting PipeWire",
             "<p>Common issues and solutions:</p>"
             "<ul><li><strong>No sound after switch</strong> -- check <code>pactl info</code> shows 'PipeWire' as server name, restart with <code>systemctl --user restart pipewire</code></li>"
             "<li><strong>Crackling audio</strong> -- increase quantum buffer size or check for CPU throttling (install <code>rtkit</code> for real-time priority)</li>"
             "<li><strong>Bluetooth skipping</strong> -- switch to a lower-latency codec or disable WiFi (2.4 GHz interference)</li>"
             "<li><strong>High memory usage</strong> -- limit allowed streams: <code>default.clock.allowed-rates = [44100, 48000]</code></li></ul>"
             "<pre><code># Test audio playback\nspeaker-test -c 2 -l 1\n\n# Full reset\nsystemctl --user stop pipewire pipewire-pulse wireplumber\nrm -rf ~/.local/share/pipewire/\nsystemctl --user start pipewire pipewire-pulse wireplumber</code></pre>"),
        ],
        [
            ("PipeWire Documentation", "https://pipewire.org/docs/", "Official PipeWire documentation"),
            ("WirePlumber Project", "https://gitlab.freedesktop.org/pipewire/wireplumber", "WirePlumber session manager sources"),
            ("Arch Wiki: PipeWire", "https://wiki.archlinux.org/title/PipeWire", "Community-maintained PipeWire guide"),
        ]
    )

    # 17. CUPS Printing
    build_page(
        "Linux Printing with CUPS",
        "cups-printing.html",
        "Print queues, driver management, network printing, troubleshooting, and cloud print integration.",
        "Linux",
        "fab fa-linux",
        [
            ("CUPS Overview & Setup",
             "<p>CUPS (Common Unix Printing System) is the standard printing system for Linux and macOS. It uses the IPP (Internet Printing Protocol) and provides a web-based administration interface on port 631.</p>"
             "<p>Install CUPS on your system:</p>"
             "<pre><code># Debian/Ubuntu\nsudo apt install cups cups-client cups-filters\n\n# Fedora\nsudo dnf install cups\n\n# Start and enable\nsudo systemctl enable --now cups\n\n# Add user to lpadmin group\nsudo usermod -a -G lpadmin $USER\n\n# Access web interface\n# http://localhost:631</code></pre>"
             "<p>Broadcast your printers on the network with <code>cups-browsed</code> for automatic discovery.</p>"),
            ("Adding & Managing Print Queues",
             "<p>Printers can be added via USB, network, or Samba shares. Use the web interface or command line:</p>"
             "<pre><code># List connected printers\nlpinfo -v\n\n# Find available drivers\nlpinfo -m | grep -i \"brother\"\n\n# Add printer (with PPD driver)\nlpadmin -p Brother_HL-L2360D -E -v usb://... -m brother:...\n\n# Add raw queue (no driver, for network printers)\nlpadmin -p Office_Printer -E -v ipp://192.168.1.100/ipp/print -m everywhere\n\n# Set default printer\nlpadmin -d Brother_HL-L2360D\n\n# List queues\nlpstat -p -d</code></pre>"
             "<p>Use the <code>-m everywhere</code> driver for IPP Everywhere printers (most modern network printers). This requires no proprietary drivers.</p>"),
            ("Driverless Printing with IPP Everywhere",
             "<p>IPP Everywhere and AirPrint enable driverless printing. CUPS auto-discovers these printers with Avahi (mDNS):</p>"
             "<pre><code># Install Avahi discovery\nsudo apt install avahi-daemon\nsudo systemctl enable --now avahi-daemon\n\n# Check for AirPrint/IPP Everywhere printers\navahi-browse -rt _ipp._tcp\navahi-browse -rt _uscan._tcp  # Scanner discovery\n\n# Add a driverless printer\nlpadmin -p NetworkPrinter -E -v ipp://printer.local:631/ipp/print -m everywhere\n\n# Test\nlp -d NetworkPrinter /path/to/test.pdf</code></pre>"
             "<p>Driverless printing works with most HP, Brother, Epson, and Canon printers manufactured after 2010.</p>"),
            ("Network Printing & Samba Sharing",
             "<p>Share Linux printers with Windows clients via Samba:</p>"
             "<pre><code># /etc/samba/smb.conf\n[printers]\n   comment = All Printers\n   path = /var/spool/samba\n   browseable = yes\n   guest ok = yes\n   printable = yes\n\n# Start Samba\nsudo systemctl enable --now smbd nmbd</code></pre>"
             "<p>For printing to Windows shares from Linux:</p>"
             "<pre><code># Install Samba client\nsudo apt install smbclient\n\n# Add printer via Samba\nlpadmin -p WindowsPrinter -E -v smb://user@server/printer_name -m everywhere</code></pre>"),
            ("Troubleshooting Common Issues",
             "<p>Diagnose printing problems systematically:</p>"
             "<pre><code># Check CUPS status\nlpstat -t\nsystemctl status cups\n\n# View error log\ntail -f /var/log/cups/error_log\n\n# Common issues:\n\n# 1. Job stuck 'Filter Failed' -- missing printer driver\nlpinfo -m | grep -i \"your-model\"\nlpadmin -p Printer -m cups-driver-...\n\n# 2. 'Permission denied' -- user not in lpadmin\nsudo usermod -a -G lpadmin $USER\n\n# 3. Paper size mismatch\nlpoptions -p Printer -o media=A4\n\n# 4. Restart CUPS\nsudo systemctl restart cups</code></pre>"
             "<p>Enable debug logging: <code>cupsctl --debug-logging</code> then check <code>/var/log/cups/error_log</code>.</p>"),
        ],
        [
            ("CUPS Documentation", "https://www.cups.org/documentation.html", "Official CUPS documentation and man pages"),
            ("Arch Wiki: CUPS", "https://wiki.archlinux.org/title/CUPS", "Comprehensive community CUPS guide"),
            ("OpenPrinting", "https://openprinting.org/", "Printer driver database and resources"),
        ]
    )

    # 18. nftables
    build_page(
        "Linux Firewall with nftables",
        "nftables-firewall.html",
        "Tables, chains, rules, sets, NAT, stateful filtering, and migrating from iptables.",
        "Linux",
        "fab fa-linux",
        [
            ("nftables vs iptables",
             "<p>nftables is the modern Linux firewall framework that replaces iptables, ip6tables, arptables, and ebtables with a single unified interface. It uses a simple, structured syntax -- no more complex raw table rules.</p>"
             "<p>Key advantages over iptables:</p>"
             "<ul><li>Simpler, more readable syntax</li>"
             "<li>Native support for sets, maps, and dictionaries</li>"
             "<li>Atomic rule replacement (entire chains replaced atomically)</li>"
             "<li>Better performance with nft (generic netlink) vs nfnetlink</li>"
             "<li>Single tool for IPv4, IPv6, ARP, and bridge</li></ul>"
             "<p>Install nftables:</p>"
             "<pre><code>sudo apt install nftables\nsudo systemctl enable --now nftables</code></pre>"),
            ("Tables, Chains & Rules",
             "<p>nftables organizes rules into tables and chains. Tables contain chains; chains contain rules:</p>"
             "<pre><code>#!/usr/sbin/nft -f\n\n# Flush existing rules\nflush ruleset\n\n# Create table (with ip, ip6, inet, arp, or bridge family)\ntable inet filter {\n\n    # Base chains (hook into kernel netfilter)\n    chain input {\n        type filter hook input priority 0; policy drop;\n\n        # Allow established connections\n        ct state established,related accept\n\n        # Allow loopback\n        iif lo accept\n\n        # SSH (rate-limited)\n        tcp dport 22 accept\n        \n        # ICMP (ping)\n        icmp type echo-request accept\n    }\n\n    chain forward {\n        type filter hook forward priority 0; policy drop;\n    }\n\n    chain output {\n        type filter hook output priority 0; policy accept;\n    }\n}\n\n# Apply\nsudo nft -f /etc/nftables.conf</code></pre>"),
            ("Sets & Dictionaries",
             "<p>Sets and dictionaries reduce rule duplication and improve performance:</p>"
             "<pre><code># Anonymous set (inline)\ntcp dport { 80, 443, 8080 } accept\n\n# Named set\nset allowed_ports {\n    type inet_service\n    flags interval\n    elements = { 22, 80, 443, 3000-3999, 8080, 8443 }\n}\n\ntcp dport @allowed_ports accept\n\n# Dictionary (map) -- different actions per value\nchain input {\n    tcp dport vmap {\n        22: accept,\n        80: accept,\n        443: accept,\n        3306: drop,\n    }\n}\n\n# Update sets at runtime\nnft add element inet filter allowed_ports { 9090 }</code></pre>"
             "<p>Sets support intervals (<code>3000-3999</code>), concatenations (<code>ip saddr . tcp dport</code>), and timeouts for dynamic banning.</p>"),
            ("NAT with nftables",
             "<p>Configure NAT (masquerading, port forwarding) in nftables:</p>"
             "<pre><code># NAT table\ntable inet nat {\n\n    chain prerouting {\n        type nat hook prerouting priority -100;\n        \n        # Port forwarding: WAN:8080 -> 192.168.1.10:80\n        tcp dport 8080 dnat to 192.168.1.10:80\n    }\n\n    chain postrouting {\n        type nat hook postrouting priority 100;\n        \n        # Masquerade (WAN interface)\n        oif eth0 masquerade\n    }\n}\n\n# IP masquerading (share internet connection)\nsudo nft add table inet nat\nsudo nft add chain inet nat postrouting '{ type nat hook postrouting priority 100; }'\nsudo nft add rule inet nat postrouting oif eth0 masquerade</code></pre>"),
            ("Logging, Monitoring & Atomic Updates",
             "<p>Debug and monitor nftables traffic:</p>"
             "<pre><code># Monitor all nftables events (real-time)\nsudo nft monitor\n\n# List all rules with packet/byte counters\nsudo nft list ruleset\n\n# Add logging\ntable inet filter {\n    chain input {\n        # Log dropped packets\n        log prefix \"nft-drop: \" flags all counter drop\n    }\n}\n\n# Atomic reload\nnft -f /etc/nftables.conf  # Whole ruleset replaced atomically\n\n# Zero counters\nnft reset counters\n\n# Save current ruleset\nsudo nft list ruleset > /etc/nftables.conf</code></pre>"),
        ],
        [
            ("nftables Wiki", "https://wiki.nftables.org/", "Official nftables project documentation"),
            ("Arch Wiki: nftables", "https://wiki.archlinux.org/title/Nftables", "Community nftables configuration guide"),
            ("Netfilter Project", "https://netfilter.org/", "nftables and netfilter framework homepage"),
        ]
    )

    # 19. GRUB Boot Process
    build_page(
        "Linux Boot Process & GRUB",
        "grub-boot-process.html",
        "GRUB configuration, initramfs, UEFI, Secure Boot, and boot troubleshooting.",
        "Linux",
        "fab fa-linux",
        [
            ("The Linux Boot Sequence",
             "<p>When you press the power button, this sequence runs:</p>"
             "<ol><li><strong>BIOS/UEFI</strong> -- initializes hardware, runs POST, reads boot device</li>"
             "<li><strong>Bootloader (GRUB)</strong> -- loads from EFI System Partition or MBR, presents menu</li>"
             "<li><strong>Kernel</strong> -- decompresses itself, initializes subsystems, mounts initramfs</li>"
             "<li><strong>initramfs</strong> -- loads storage drivers, mounts root filesystem</li>"
             "<li><strong>init/systemd</strong> -- PID 1, starts services, reaches target</li></ol>"
             "<p>GRUB 2 is the default bootloader for most Linux distributions. It supports both BIOS (legacy) and UEFI boot modes.</p>"),
            ("GRUB Configuration Files",
             "<p>GRUB's main configuration files:</p>"
             "<pre><code># Main config -- auto-generated, DO NOT EDIT directly\n/boot/grub/grub.cfg\n\n# User-editable settings\n/etc/default/grub\n\n# Custom scripts (executed during grub-mkconfig)\n/etc/grub.d/\n  00_header        # Sets defaults\n  10_linux         # Finds Linux kernels\n  30_os-prober     # Detects other OSes\n  40_custom        # User entries\n  41_custom        # More user entries</code></pre>"
             "<pre><code># /etc/default/grub example\nGRUB_DEFAULT=0               # Default menu entry\nGRUB_TIMEOUT=5               # Seconds before boot\nGRUB_TIMEOUT_STYLE=menu      # menu, countdown, hidden\nGRUB_CMDLINE_LINUX_DEFAULT=\"quiet splash\"  # Kernel params\nGRUB_GFXMODE=1920x1080       # Graphics resolution\nGRUB_DISABLE_OS_PROBER=false # Detect other OSes\n\n# Apply changes\nsudo update-grub  # or: sudo grub-mkconfig -o /boot/grub/grub.cfg</code></pre>"),
            ("Initramfs & Kernel Parameters",
             "<p>The initramfs (initial RAM filesystem) contains kernel modules needed to mount the root filesystem:</p>"
             "<pre><code># Rebuild initramfs\nsudo mkinitcpio -P                     # Arch\nsudo update-initramfs -u -k all        # Debian/Ubuntu\ndracut --force                         # Fedora\n\n# View initramfs contents\nlsinitramfs /boot/initrd.img-$(uname -r)\n\n# Kernel parameters (in GRUB_CMDLINE_LINUX)\n# Add these to solve specific issues:\n\n# Disable nouveau (NVIDIA) for safe boot\nGRUB_CMDLINE_LINUX=\"modprobe.blacklist=nouveau\"\n\n# Memory limits\nGRUB_CMDLINE_LINUX=\"mem=4G\"\n\n# Single-user mode (rescue)\nGRUB_CMDLINE_LINUX=\"single\"\n\n# Disable ACPI (hardware debug)\nGRUB_CMDLINE_LINUX=\"acpi=off\"</code></pre>"),
            ("UEFI, Secure Boot & Dual Boot",
             "<p>Modern systems use UEFI with GPT partitioning. Key points:</p>"
             "<pre><code># Check boot mode\n[ -d /sys/firmware/efi ] && echo \"UEFI\" || echo \"BIOS/Legacy\"\n\n# EFI System Partition (ESP)\n# Usually mounted at /boot/efi or /boot\nls /boot/efi/EFI/\n\n# Install GRUB for UEFI\nsudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB\n\n# Secure Boot enrollment (using shim)\nsudo apt install shim-signed\nsudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=GRUB\n\n# Dual boot: enable os-prober\nGRUB_DISABLE_OS_PROBER=false\nsudo update-grub</code></pre>"),
            ("Troubleshooting Boot Issues",
             "<p>When your system won't boot, use these recovery techniques:</p>"
             "<pre><code># At GRUB menu, press 'e' to edit boot entry\n# Add these kernel parameters for rescue:\n\n# Boot to emergency shell\nsystemd.unit=emergency.target\n\n# Boot to single-user mode (root shell)\ninit=/bin/bash\n\n# Skip systemd\ninit=/bin/sh\n\n# After boot, view logs\njournalctl -b -1        # Previous boot log\njournalctl -xb          # Current boot with explanations\n\n# Regenerate GRUB\nsudo mount /dev/sda1 /mnt\nsudo mount --bind /dev /mnt/dev\nsudo chroot /mnt\ngrub-install /dev/sda\nupdate-grub</code></pre>"
             "<p>Keep a live USB handy for recovery. Most distros offer a 'Try' mode that lets you chroot into your installed system.</p>"),
        ],
        [
            ("GNU GRUB Manual", "https://www.gnu.org/software/grub/manual/", "Official GRUB 2 documentation"),
            ("Arch Wiki: GRUB", "https://wiki.archlinux.org/title/GRUB", "Comprehensive community GRUB guide"),
            ("UEFI Forum Specifications", "https://uefi.org/specifications", "UEFI specifications and guidelines"),
        ]
    )

    # 20. BorgBackup
    build_page(
        "Linux Backups with BorgBackup",
        "borg-backup.html",
        "Deduplicated encrypted backups, automation cron jobs, pruning strategies, and remote repositories.",
        "Linux",
        "fab fa-linux",
        [
            ("What is BorgBackup?",
             "<p>BorgBackup (Borg) is a deduplicating backup tool for Linux. It efficiently stores backup data by splitting files into chunks and deduplicating across all backups -- only new chunks consume additional space. Features include compression, authenticated encryption, and remote backup via SSH.</p>"
             "<p>Key benefits:</p>"
             "<ul><li><strong>Deduplication</strong> -- identical files are stored once, across all backups</li>"
             "<li><strong>Compression</strong> -- lz4 (fast), zstd (balanced), lzma (maximum)</li>"
             "<li><strong>Encryption</strong> -- AEAD encryption with repokey or keyfile modes</li>"
             "<li><strong>Mountable backups</strong> -- browse backups as FUSE filesystems</li></ul>"
             "<p>Install Borg:</p><pre><code>sudo apt install borgbackup</code></pre>"),
            ("Initializing a Repository & Creating Backups",
             "<p>Set up a Borg repository and create your first backup:</p>"
             "<pre><code># Initialize a local repo with encryption\nexport BORG_REPO=/mnt/backup/borg\nborg init --encryption=repokey-blake2 $BORG_REPO\n\n# Back up ~/Documents\nborg create --stats --progress \\\n    $BORG_REPO::documents-{now:%Y-%m-%d} \\\n    ~/Documents\n\n# With compression\nborg create --compression zstd,3 --stats \\\n    $BORG_REPO::home-{now:%Y-%m-%d} \\\n    ~ --exclude '*.cache' --exclude '*.tmp'\n\n# Remote repository via SSH\nborg init --encryption=repokey-blake2 \\\n    user@backupserver:/mnt/backup/borg</code></pre>"),
            ("Restoring & Mounting Backups",
             "<p>Restore entire archives or individual files:</p>"
             "<pre><code># List archives\nborg list $BORG_REPO\n\n# List files in an archive\nborg list $BORG_REPO::documents-2026-05-28\n\n# Extract entire archive\ncd /tmp/restore\nborg extract $BORG_REPO::documents-2026-05-28\n\n# Extract specific files\nborg extract $BORG_REPO::documents-2026-05-28 \\\n    --path home/user/Documents/important.pdf\n\n# Mount archive as FUSE filesystem (browse interactively)\nmkdir /mnt/borg-mount\nborg mount $BORG_REPO::documents-2026-05-28 /mnt/borg-mount\nls /mnt/borg-mount\nborg umount /mnt/borg-mount</code></pre>"),
            ("Pruning & Automation",
             "<p>Borg does not auto-delete old archives. Use <code>borg prune</code> to maintain retention policies:</p>"
             "<pre><code># Prune archives -- keep\nborg prune --list --stats $BORG_REPO \\\n    --keep-daily 7 \\\n    --keep-weekly 4 \\\n    --keep-monthly 6\n\n# Full backup script\n#!/bin/bash\n# /usr/local/bin/backup.sh\n\nexport BORG_REPO=/mnt/backup/borg\nexport BORG_PASSPHRASE='your-passphrase'\n\nborg create --compression zstd,6 --stats \\\n    $BORG_REPO::system-{now:%Y-%m-%d} \\\n    /etc /var/lib /home \\\n    --exclude '*.cache' --exclude '*.tmp'\n\nborg prune --list $BORG_REPO \\\n    --keep-daily 7 --keep-weekly 4 --keep-monthly 6</code></pre>"
             "<pre><code># Cron: run daily at 2 AM\n0 2 * * * /usr/local/bin/backup.sh</code></pre>"),
            ("Security & Best Practices",
             "<p>Protect your backups with these practices:</p>"
             "<ul><li><strong>Store passphrase securely</strong> -- use a password manager and consider <code>BORG_PASSCOMMAND</code> for scripts</li>"
             "<li><strong>Test restores regularly</strong> -- an untested backup is no backup at all</li>"
             "<li><strong>Use append-only mode</strong> for remote repos to prevent ransomware from deleting backups: <code>borg init --append-only</code></li>"
             "<li><strong>Enable compaction</strong> -- <code>borg compact</code> reclaims space after prune</li>"
             "<li><strong>Monitor with borgmatic</strong> -- a wrapper that adds YAML config, healthchecks, and notification integration</li></ul>"
             "<pre><code># Compact repository (reclaim space after prune)\nborg compact $BORG_REPO\n\n# Verify archive integrity\nborg check $BORG_REPO</code></pre>"),
        ],
        [
            ("BorgBackup Documentation", "https://borgbackup.readthedocs.io/", "Official BorgBackup documentation and examples"),
            ("Borgmatic Documentation", "https://torsion.org/borgmatic/", "Borg wrapper with YAML config and monitoring"),
            ("Offsite Backup Guide", "https://www.borgbackup.org/support/", "Community resources and support forums"),
        ]
    )

    # 21. Linux Desktop Customization
    build_page(
        "Linux Desktop Customization (KDE & GNOME)",
        "linux-desktop-customization.html",
        "Themes, extensions, widgets, and deep customization of KDE Plasma and GNOME Shell.",
        "Linux",
        "fab fa-linux",
        [
            ("KDE Plasma vs GNOME Shell",
             "<p>KDE Plasma and GNOME Shell are the two most popular Linux desktop environments, each with a distinct philosophy:</p>"
             "<ul><li><strong>KDE Plasma</strong> -- highly customizable out of the box; resembles Windows with a taskbar, desktop widgets, and system tray. Built with Qt.</li>"
             "<li><strong>GNOME Shell</strong> -- minimalist, focused on workflow and keyboard navigation. Uses extensions for customization. Built with GTK.</li></ul>"
             "<p>Both support Wayland by default in their latest versions and offer rich theming ecosystems.</p>"),
            ("Customizing KDE Plasma",
             "<p>KDE Plasma offers extensive customization through System Settings and community resources:</p>"
             "<pre><code># Install Plasma themes\n# https://store.kde.org/ or via Discover\n\n# Global themes (System Settings > Appearance > Global Theme)\nget-new-stuff --install plasma-themes\n\n# Latte Dock (macOS-like dock)\nsudo apt install latte-dock\n\n# Kvantum theme engine\nsudo apt install qt5-style-kvantum kvantum\n</code></pre>"
             "<p>Key customization areas:</p>"
             "<ul><li><strong>Desktop effects</strong> -- wobbly windows, transparency, window tiling (System Settings > Desktop Effects)</li>"
             "<li><strong>Widgets</strong> -- right-click desktop > Add Widgets (weather, system monitor, notes)</li>"
             "<li><strong>Activity manager</strong> -- separate virtual desktops with different wallpapers and widgets per activity</li>"
             "<li><strong>Plasma themes</strong> -- KDE Store > Plasma Themes, or manually in <code>~/.local/share/plasma/desktoptheme/</code></li></ul>"),
            ("Customizing GNOME Shell with Extensions",
             "<p>GNOME's functionality is extended through shell extensions managed by GNOME Software or <code>gnome-extensions-cli</code>:</p>"
             "<pre><code># Install Extension Manager (flatpak)\nflatpak install flathub com.mattjakeman.ExtensionManager\n\n# CLI tool\nsudo apt install gnome-shell-extensions\npip install --user gnome-extensions-cli\n\n# Essential extensions:\ngnome-extensions install dash-to-dock\ngnome-extensions install blur-my-shell\ngnome-extensions install user-themes\ngnome-extensions install appindicatorsupport\n\n# List installed extensions\ngnome-extensions list\ngnome-extensions info dash-to-dock</code></pre>"
             "<p>GNOME Tweaks (<code>gnome-tweaks</code>) provides a GUI for fonts, title bar buttons, and extension configuration. <strong>GNOME 45+</strong> uses a new extension system with quick-settings toggles.</p>"),
            ("Icon & Cursor Themes",
             "<p>Change the entire look and feel of your desktop with icon and cursor themes:</p>"
             "<pre><code># Install popular icon themes\nsudo apt install papirus-icon-theme\nsudo apt install tela-icon-theme\nsudo apt install breeze-icon-theme\n\n# Manual installation\nmkdir -p ~/.local/share/icons\ncd ~/.local/share/icons\ngit clone https://github.com/PapirusDevelopmentTeam/papirus-icon-theme.git\n\n# Cursor themes\nsudo apt install bibata-cursor-theme\nsudo apt install capitaine-cursors\n\n# Apply via System Settings or GNOME Tweaks</code></pre>"),
            ("Conky & Desktop Widgets",
             "<p>Conky is a lightweight system monitor that displays on your desktop:</p>"
             "<pre><code># Install Conky\nsudo apt install conky-all\n\n# Example .conkyrc\nconky.config = {\n    alignment = 'top_right',\n    gap_x = 20,\n    gap_y = 60,\n    minimum_width = 250,\n    update_interval = 2,\n    own_window = true,\n    own_window_type = 'desktop',\n    own_window_transparent = true,\n};\n\nconky.text = [[\n${color #5294e2}${font Ubuntu:bold:size=12}System${font}\n${color}Uptime: $uptime\nCPU: ${cpu}% ${cpubar}\nRAM: $mem / $memmax ${membar}\nDisk: ${fs_used /} / ${fs_size /} ${fs_bar /}\nProcesses: $processes\n]];</code></pre>"
             "<p>Browse Conky themes at Pling (https://pling.com/) or r/ConkyPorn on Reddit. Use Conky Manager (<code>conky-manager</code>) for GUI management.</p>"),
        ],
        [
            ("KDE Plasma Store", "https://store.kde.org/", "KDE themes, widgets, and Plasma add-ons"),
            ("GNOME Shell Extensions", "https://extensions.gnome.org/", "Official GNOME extension repository"),
            ("Pling -- Linux Desktop Art", "https://pling.com/", "Cross-desktop themes and customization resources"),
        ]
    )

    # 22. X11 vs Wayland
    build_page(
        "X11 vs Wayland Display Servers",
        "x11-vs-wayland.html",
        "Architecture comparison, migration guide, compatibility, and practical considerations for Linux users.",
        "Linux",
        "fab fa-linux",
        [
            ("Display Server Architecture",
             "<p>The display server is the layer between applications (clients) and the hardware (GPU, input devices). X11 (X.Org) has been the standard for decades but was designed in 1984 for a very different computing landscape. Wayland is its modern replacement.</p>"
             "<p><strong>X11 Architecture:</strong></p>"
             "<ul><li>Client-server model -- applications connect to the X server, which composites the display</li>"
             "<li>Network-transparent -- apps can display on remote machines via SSH</li>"
             "<li>Server handles all input and output coordination</li>"
             "<li>Complex: decades of accumulated protocol extensions (XKB, XRandR, DRI2, etc.)</li></ul>"
             "<p><strong>Wayland Architecture:</strong></p>"
             "<ul><li>Each compositor is a display server (smaller, simpler)</li>"
             "<li>Clients render directly to buffers, compositor just composites</li>"
             "<li>No network transparency built-in (Wayland proxy solutions exist)</li>"
             "<li>Inherently more secure -- clients cannot snoop on each other's input</li></ul>"),
            ("Security & Isolation",
             "<p>Wayland addresses fundamental security weaknesses in X11:</p>"
             "<pre><code># X11 vulnerability: any app can read all input\n# Try this on X11:\nxinput list\nxinput test &lt;id&gt;  # See all keyboard events from any window\n\n# X11: keyloggers are trivial\nxev -event keyboard  # Captures all keystrokes\n\n# Wayland: input events are only delivered to the focused window\n# Screen capture requires compositor permission (xdg-desktop-portal)\n# Wayland apps cannot read other windows' content</code></pre>"
             "<p>Wayland's security model means screen recording tools (OBS, Zoom) need xdg-desktop-portal-wlr or pipewire integration. No app can take screenshots or record the screen without explicit user permission.</p>"),
            ("Performance & Rendering",
             "<p>Wayland offers tangible performance improvements over X11:</p>"
             "<ul><li><strong>No tearing</strong> -- Wayland protocols require explicit vsync, eliminating screen tearing without NVIDIA-specific workarounds</li>"
             "<li><strong>Smoother animation</strong> -- compositor directly schedules buffer swaps; no round-trip to X server</li>"
             "<li><strong>Lower input latency</strong> -- input events go directly to the focused application without passing through the X server</li>"
             "<li><strong>Per-monitor refresh rates</strong> -- Wayland supports mixed refresh rates (e.g., 60 Hz + 144 Hz) correctly</li></ul>"
             "<p>NVIDIA proprietary driver support has improved significantly. Wayland works with NVIDIA driver 545+ using EGLStreams or GBM (via nvidia-dkms with nvidia-modeset).</p>"),
            ("Compatibility & Migration",
             "<p>Check if Wayland works with your setup:</p>"
             "<pre><code># Check current session\necho $XDG_SESSION_TYPE  # 'wayland' or 'x11'\n\n# Force Wayland in GDM\nsudoedit /etc/gdm3/custom.conf\n# Uncomment: WaylandEnable=true\n\n# Switch session from login screen\n# Click gear icon to choose 'GNOME on Wayland' or 'Plasma (Wayland)'\n\n# Check Wayland support per app\n# Most modern apps work natively (GTK4, Qt6, Firefox, Chrome)\n# Electron apps: --enable-features=UseOzonePlatform --ozone-platform=wayland\n\n# XWayland -- compatibility layer for X11-only apps\n# Runs X11 apps in a Wayland window, auto-started by compositor</code></pre>"
             "<p>Common migration gotchas:</p>"
             "<ul><li>Screen sharing in video calls -- requires xdg-desktop-portal backend</li>"
             "<li>Color management -- still evolving in Wayland (KDE 6 has better support)</li>"
             "<li>Remote desktop -- x11vnc doesn't work; use wayvnc or KRDC (RDP)</li></ul>"),
            ("Choosing Your Compositor",
             "<p>Several Wayland compositors are available for different needs:</p>"
             "<ul><li><strong>GNOME (mutter)</strong> -- default Wayland compositor for GNOME; stable, feature-rich</li>"
             "<li><strong>KDE (kwin)</strong> -- full-featured with extensive settings; Wayland support in Plasma 6 is production-ready</li>"
             "<li><strong>Sway</strong> -- i3-compatible tiling Wayland compositor; for tiling WM users</li>"
             "<li><strong>Hyprland</strong> -- dynamic tiling compositor with animations, blur, and eye candy</li>"
             "<li><strong>River</strong> -- dynamic tiling, minimal, Wayland-native</li></ul>"
             "<p>For most users, GNOME or KDE on Wayland is the best choice in 2026. Try <code>export KWIN_DRM_NO_AMS=1</code> to troubleshoot KDE Wayland issues.</p>"),
        ],
        [
            ("Wayland Project", "https://wayland.freedesktop.org/", "Official Wayland protocol documentation"),
            ("Arch Wiki: Wayland", "https://wiki.archlinux.org/title/Wayland", "Comprehensive community Wayland guide"),
            ("Are We Wayland Yet?", "https://arewewaylandyet.com/", "Track Wayland application compatibility"),
        ]
    )

    # 23. Podman
    build_page(
        "Podman Container Management",
        "podman-guide.html",
        "Daemonless containers, rootless execution, pods, Docker compatibility, and Quadlet systemd integration.",
        "Linux",
        "fab fa-linux",
        [
            ("Podman vs Docker",
             "<p>Podman is a daemonless container engine that can run containers without a central daemon. Unlike Docker, Podman does not require root access to run containers (rootless mode is default). It is fully compatible with Docker images and registries.</p>"
             "<p>Key differences:</p>"
             "<ul><li><strong>Daemonless</strong> -- no long-running daemon; containers are child processes</li>"
             "<li><strong>Rootless by default</strong> -- containers run with user namespaces for security</li>"
             "<li><strong>Pod support</strong> -- run multiple containers sharing the same network namespace (like Kubernetes pods)</li>"
             "<li><strong>Docker-compatible CLI</strong> -- <code>alias docker=podman</code> works for most commands</li></ul>"
             "<pre><code># Install Podman\nsudo apt install podman podman-docker podman-compose\n\n# Test with alias\nalias docker=podman\ndocker run hello-world</code></pre>"),
            ("Rootless Containers & Security",
             "<p>Rootless containers provide isolation without requiring root privileges:</p>"
             "<pre><code># Podman runs rootless by default -- no sudo needed\npodman run -d -p 8080:80 nginx\n\n# Check: user namespaces\npodman unshare cat /proc/self/uid_map\n# Shows UID mapping: 0 1000 1  (root in container = user 1000 on host)\n\n# Rootless networking: slirp4netns or pasta\n# --network bridge requires root; rootless uses slirp4netns\n\n# Privileged operations\n# --privileged flag works but reduces isolation\n\n# Resource limits\npodman run --cpus 2 --memory 512m nginx</code></pre>"
             "<p>For rootless containers to bind to privileged ports (&lt;1024), enable <code>sysctl net.ipv4.ip_unprivileged_port_start=80</code> or use port mapping.</p>"),
            ("Pods -- Kubernetes-Style Groups",
             "<p>Pods let you run multiple containers that share network, IPC, and PID namespaces:</p>"
             "<pre><code># Create an empty pod\npodman pod create --name myapp -p 3000:3000\n\n# Add containers to the pod\npodman run -d --pod myapp --name frontend nginx\npodman run -d --pod myapp --name backend node:18 app.js\npodman run -d --pod myapp --name database postgres:16\n\n# Pod management\npodman pod list\npodman pod stats myapp\npodman pod ps --pod\n\n# Generate Kubernetes YAML from a pod\npodman generate kube myapp > myapp.yaml\nkubectl apply -f myapp.yaml</code></pre>"),
            ("Systemd Integration with Quadlet",
             "<p>Quadlet lets you run Podman containers as systemd services using simple YAML-like files:</p>"
             "<pre><code># /etc/containers/systemd/nginx.container\n[Unit]\nDescription=Nginx web server\nAfter=network-online.target\n\n[Container]\nImage=docker.io/library/nginx:latest\nPort=8080:80\nVolume=/srv/www:/usr/share/nginx/html:Z\nNetwork=host\n\n[Install]\nWantedBy=default.target\n\n# Enable and start\nsystemctl --user daemon-reload\nsystemctl --user enable --now nginx\nsystemctl --user status nginx\n\n# View generated service\nsystemctl --user cat nginx</code></pre>"
             "<p>Quadlet files go in <code>/etc/containers/systemd/</code> (system) or <code>~/.config/containers/systemd/</code> (user). They are automatically converted to systemd unit files at daemon-reload.</p>"),
            ("Podman Compose & Registries",
             "<p>Podman Compose works as a Docker Compose drop-in replacement:</p>"
             "<pre><code># docker-compose.yml works unmodified\nversion: '3'\nservices:\n  web:\n    image: nginx\n    ports:\n      - \"8080:80\"\n  db:\n    image: postgres:16\n    environment:\n      POSTGRES_PASSWORD: example\n\n# Run with podman-compose\npodman-compose up -d\npodman-compose logs -f</code></pre>"
             "<p>Configure registries in <code>/etc/containers/registries.conf</code>:</p>"
             "<pre><code>[registries.search]\nregistries = ['docker.io', 'quay.io', 'registry.fedoraproject.org']\n\n[registries.insecure]\nregistries = ['localhost:5000']</code></pre>"),
        ],
        [
            ("Podman Documentation", "https://podman.io/docs", "Official Podman documentation and tutorials"),
            ("Red Hat Podman Guide", "https://www.redhat.com/en/topics/containers/what-is-podman", "Enterprise Podman overview from Red Hat"),
            ("Quadlet Documentation", "https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html", "Systemd integration with Quadlet"),
        ]
    )

    # 24. Advanced Linux Networking
    build_page(
        "Advanced Linux Networking Tools",
        "linux-advanced-networking.html",
        "ip, ss, nmcli, bridge, tc -- advanced network configuration and troubleshooting on Linux.",
        "Linux",
        "fab fa-linux",
        [
            ("iproute2: The Modern Network Stack",
             "<p>The <code>iproute2</code> suite replaces legacy tools (ifconfig, route, arp, netstat) with a unified interface. The <code>ip</code> command manages addresses, routes, links, and neighbors:</p>"
             "<pre><code># Address management\nip addr show                     # List all interfaces\nip addr add 192.168.1.10/24 dev eth0  # Assign IP\nip addr del 192.168.1.10/24 dev eth0  # Remove IP\n\n# Link management\nip link set eth0 up/down         # Enable/disable interface\nip link set eth0 mtu 9000        # Jumbo frames\n\n# Route management\nip route show                    # View routing table\nip route add default via 192.168.1.1\nip route add 10.0.0.0/8 via 192.168.1.254\n\n# Neighbor (ARP) table\nip neigh show\nip neigh del 192.168.1.5 dev eth0</code></pre>"),
            ("Socket Statistics with ss",
             "<p><code>ss</code> is the modern replacement for <code>netstat</code>. It reads socket information directly from the kernel for faster, more detailed output:</p>"
             "<pre><code># List all listening TCP sockets\nss -tlnp\n\n# List all established connections\nss -tunap\n\n# Filter by port\nss -tlnp 'sport = :22'\nss -tunap 'dport = :443'\n\n# Show process using socket\nss -tlnp | grep nginx\n\n# Unix domain sockets\nss -xlp\n\n# Socket statistics by state\nss -s\n# Total: 1234 (kernel 5678)\n# TCP:   456 (estab 234, closed 123, orphaned 5, synrecv 0, ...)</code></pre>"),
            ("Network Management with nmcli",
             "<p><code>nmcli</code> is the command-line interface to NetworkManager. It controls network connections and devices:</p>"
             "<pre><code># Device status\nnmcli device status\nnmcli device show wlan0\n\n# Connection management\nnmcli connection show\nnmcli connection up \"My WiFi\"\nnmcli connection down \"My WiFi\"\n\n# Create new connection\nnmcli connection add type wifi con-name \"Office\" \\\n    ifname wlan0 ssid \"Office-5G\" \\\n    wifi-sec.key-mgmt wpa-psk wifi-sec.psk \"password\"\n\n# Modify connection\nnmcli connection modify \"Office\" ipv4.method manual \\\n    ipv4.addresses 192.168.1.100/24 \\\n    ipv4.gateway 192.168.1.1 \\\n    ipv4.dns 8.8.8.8\n\n# Hotspot\nnmcli device wifi hotspot ifname wlan0 ssid \"MyHotspot\" password \"guest1234\"</code></pre>"),
            ("Linux Bridge & Bonding",
             "<p>Create virtual bridges for VMs/containers and bond interfaces for redundancy:</p>"
             "<pre><code># Create a bridge\nip link add name br0 type bridge\nip link set br0 up\nip addr add 10.0.100.1/24 dev br0\nip link set eth0 master br0\nip link set tap0 master br0\n\n# Bridge management\nbridge link show\nbridge fdb show  # Forwarding database\n\n# Bonding (NIC teaming)\nip link add bond0 type bond mode 802.3ad\nip link set eth0 master bond0\nip link set eth1 master bond0\nip addr add 192.168.1.10/24 dev bond0\n\n# View bond status\ncat /proc/net/bonding/bond0</code></pre>"),
            ("Traffic Control (tc) -- Shaping & Queuing",
             "<p>Traffic control manages packet queuing, shaping, and scheduling:</p>"
             "<pre><code># Add root qdisc (HTB -- Hierarchical Token Bucket)\ntc qdisc add dev eth0 root handle 1: htb default 30\n\n# Create classes\ntc class add dev eth0 parent 1: classid 1:1 htb rate 100mbit\ntc class add dev eth0 parent 1:1 classid 1:10 htb rate 10mbit ceil 20mbit\ntc class add dev eth0 parent 1:1 classid 1:20 htb rate 30mbit ceil 40mbit\n\n# Add filters to classify traffic\ntc filter add dev eth0 protocol ip parent 1:0 prio 1 \\\n    u32 match ip dport 80 0xffff flowid 1:10\ntc filter add dev eth0 protocol ip parent 1:0 prio 2 \\\n    u32 match ip dst 192.168.1.0/24 flowid 1:20\n\n# Show tc stats\ntc -s qdisc show dev eth0\ntc -s class show dev eth0</code></pre>"),
        ],
        [
            ("iproute2 Documentation", "https://wiki.linuxfoundation.org/networking/iproute2", "Linux foundation iproute2 reference"),
            ("Arch Wiki: Network Configuration", "https://wiki.archlinux.org/title/Network_configuration", "Community Linux networking guide"),
            ("Traffic Control Manual", "https://tldp.org/HOWTO/Traffic-Control-HOWTO/", "Linux traffic control how-to"),
        ]
    )

    # 25. LXC Containers
    build_page(
        "LXC Linux Containers",
        "lxc-containers.html",
        "System containers vs Docker, management with LXD, networking, and use cases.",
        "Linux",
        "fab fa-linux",
        [
            ("LXC vs Docker: System Containers vs Application Containers",
             "<p>LXC (Linux Containers) provides system containers -- lightweight virtual machines that run a full operating system with init, systemd, and multiple processes. Docker focuses on application containers -- single-process, ephemeral environments.</p>"
             "<p>Key differences:</p>"
             "<ul><li><strong>LXC/LXD</strong> -- boots a full OS (like a VM but using kernel namespaces); persistent, long-running</li>"
             "<li><strong>Docker</strong> -- runs a single application process; stateless, designed for orchestration</li>"
             "<li><strong>Use LXC when</strong> -- you need a full Linux environment (development VM, CI runners, legacy apps)</li>"
             "<li><strong>Use Docker when</strong> -- microservices, stateless apps, Kubernetes orchestration</li></ul>"),
            ("Installing LXD & Creating Containers",
             "<p>LXD is the container hypervisor that manages LXC containers:</p>"
             "<pre><code># Install LXD\nsudo snap install lxd\n# OR from apt\nsudo apt install lxd lxd-client\n\n# Initialize LXD (interactive)\nsudo lxd init\n\n# Launch a container\nlxc launch ubuntu:24.04 my-container\nlxc launch images:centos/9/amd64 centos-dev\n\n# List containers\nlxc list\n\n# Execute commands inside\nlxc exec my-container -- bash\nlxc exec my-container -- apt update\n\n# Stop and delete\nlxc stop my-container\nlxc delete my-container</code></pre>"),
            ("Container Profiles & Configuration",
             "<p>Profiles define container resource limits, network, and storage:</p>"
             "<pre><code># Create a profile\nlxc profile create dev-env\n\n# Configure resource limits\nlxc profile set dev-env limits.cpu 2\nlxc profile set dev-env limits.memory 4GB\nlxc profile set dev-env limits.disk.priority 10\n\n# Configure networking\nlxc profile device add dev-env eth0 nic nictype=bridged parent=lxdbr0\n\n# Configure storage\nlxc profile device add dev-env root disk path=/ pool=default size=20GB\n\n# Apply profile\nlxc launch ubuntu:24.04 dev-container --profile dev-env\n\n# Edit profile YAML directly\nlxc profile edit dev-env</code></pre>"),
            ("Networking & Storage in LXD",
             "<p>LXD provides flexible networking options:</p>"
             "<pre><code># Default bridge (NAT)\nlxc network show lxdbr0\n\n# Create a new bridge\nlxc network create mybr0 --type=bridge \\\n    ipv4.address=10.10.100.1/24 ipv4.nat=true\n\n# Attach container to network\nlxc network attach mybr0 my-container eth0\n\n# Create storage pool\nlxc storage create ssd zfs source=/dev/sdb\nlxc storage create data dir source=/mnt/storage\n\n# Attach storage to container\nlxc storage volume create ssd my-volume --size=10GB\nlxc storage volume attach ssd my-volume my-container /mnt/data</code></pre>"),
            ("Snapshots, Backup & Migration",
             "<p>LXD's snapshot and migration features make it great for development environments:</p>"
             "<pre><code># Create snapshot\nlxc snapshot my-container clean-install\nlxc snapshot my-container before-upgrade\n\n# List and restore\nlxc list my-container/snapshots\nlxc restore my-container clean-install\n\n# Export/import container (full backup)\nlxc export my-container /backup/my-container.tar.gz\nlxc import /backup/my-container.tar.gz\n\n# Live migration (between hosts)\nlxc move my-container remote-host:\n\n# Copy container\nlxc copy my-container my-container-clone\n\n# Publish as image\nlxc publish my-container --alias my-custom-image --public</code></pre>"),
        ],
        [
            ("LXD Documentation", "https://documentation.ubuntu.com/lxd/", "Official LXD container management documentation"),
            ("Linux Containers Project", "https://linuxcontainers.org/", "LXC/LXD project homepage and resources"),
            ("Stgraber's LXD Blog", "https://stgraber.org/category/lxd/", "Detailed LXD tutorials and news from maintainer"),
        ]
    )

    # ========== WINDOWS (8) ==========

    # 26. Windows Terminal
    build_page(
        "Windows Terminal Customization",
        "windows-terminal.html",
        "Profiles, themes, oh-my-posh, keybindings, and power user workflows in Windows Terminal.",
        "Windows",
        "fab fa-windows",
        [
            ("Windows Terminal Overview",
             "<p>Windows Terminal is a modern, open-source terminal application for Windows 10 and 11. It supports multiple tabs, panes, GPU-accelerated rendering, and tabs for PowerShell, CMD, WSL, and SSH connections. It replaced the legacy console host as the default terminal in Windows 11.</p>"
             "<p>Install from Microsoft Store, winget, or GitHub:</p>"
             "<pre><code># winget\nwinget install Microsoft.WindowsTerminal\n\n# Chocolatey\nchoco install microsoft-windows-terminal\n\n# Scoop\nscoop bucket add extras\nscoop install windows-terminal</code></pre>"),
            ("Profiles & Settings",
             "<p>Windows Terminal settings are stored in <code>settings.json</code> (JSONC format). Access via Settings UI or directly:</p>"
             "<pre><code>// ~/AppData/Local/Packages/Microsoft.WindowsTerminal_8wekyb3d8bbwe/LocalState/settings.json\n{\n    \"$schema\": \"https://aka.ms/terminal-profiles-schema\",\n    \"profiles\": {\n        \"defaults\": {\n            \"fontFace\": \"Cascadia Code NF\",\n            \"fontSize\": 12,\n            \"opacity\": 90,\n            \"useAcrylic\": true,\n            \"cursorShape\": \"filledBox\"\n        },\n        \"list\": [\n            {\n                \"name\": \"PowerShell\",\n                \"commandline\": \"pwsh.exe -NoLogo\",\n                \"icon\": \"ms-appx:///ProfileIcons/{61c54bbd-c2c6-5271-96e7-009a87ff44bf}.png\"\n            },\n            {\n                \"name\": \"Ubuntu WSL\",\n                \"source\": \"Windows.Terminal.Wsl\",\n                \"distribution\": \"Ubuntu\"\n            }\n        ]\n    }\n}</code></pre>"),
            ("Oh My Posh Prompt Customization",
             "<p>Oh My Posh provides beautiful prompt themes for PowerShell, CMD, and WSL:</p>"
             "<pre><code># Install Oh My Posh (winget)\nwinget install JanDeDobbeleer.OhMyPosh\n\n# Install a Nerd Font (Cascadia Code)\noh-my-posh font install\n\n# Edit PowerShell profile\nnotepad $PROFILE\n# Add:\noh-my-posh init pwsh --config ~/jandedobbeleer.omp.json | Invoke-Expression\n\n# Install themes\noh-my-posh init pwsh --config \"$(oh-my-posh config path)/themes/cloud-native.omp.json\"\n\n# Browse themes\nGet-PoshThemes</code></pre>"),
            ("Keybindings & Productivity",
             "<p>Boost productivity with custom keybindings and actions:</p>"
             "<pre><code>// In settings.json \"actions\" array:\n{\n    \"command\": { \"action\": \"splitPane\", \"split\": \"vertical\" },\n    \"keys\": \"alt+shift+d\"\n},\n{\n    \"command\": { \"action\": \"splitPane\", \"split\": \"horizontal\" },\n    \"keys\": \"alt+shift+- \"\n},\n{\n    \"command\": \"closePane\",\n    \"keys\": \"ctrl+shift+w\"\n},\n{\n    \"command\": { \"action\": \"newTab\", \"index\": 0 },\n    \"keys\": \"ctrl+1\"\n},\n{\n    \"command\": { \"action\": \"sendInput\", \"input\": \"clear\\u000d\" },\n    \"keys\": \"ctrl+l\"\n}</code></pre>"
             "<p>Use <strong>quake mode</strong> (<code>win+`</code>) for a drop-down terminal that appears on any keypress.</p>"),
            ("Color Schemes & Theming",
             "<p>Windows Terminal supports custom color schemes. Popular ones include Catppuccin, Dracula, and Nord:</p>"
             "<pre><code>// In settings.json\n\"schemes\": [\n    {\n        \"name\": \"Catppuccin Mocha\",\n        \"background\": \"#1e1e2e\",\n        \"foreground\": \"#cdd6f4\",\n        \"black\": \"#45475a\",\n        \"red\": \"#f38ba8\",\n        \"green\": \"#a6e3a1\",\n        \"yellow\": \"#f9e2af\",\n        \"blue\": \"#89b4fa\",\n        \"purple\": \"#cba6f7\",\n        \"cyan\": \"#94e2d5\",\n        \"white\": \"#bac2de\"\n    }\n],\n\n// Apply to profile\n\"profiles\": {\n    \"defaults\": { \"colorScheme\": \"Catppuccin Mocha\" }\n}</code></pre>"),
        ],
        [
            ("Windows Terminal Documentation", "https://learn.microsoft.com/en-us/windows/terminal/", "Official Microsoft documentation"),
            ("Oh My Posh Documentation", "https://ohmyposh.dev/docs/", "Prompt customization reference and themes"),
            ("Windows Terminal GitHub", "https://github.com/microsoft/terminal", "Source code and issue tracker"),
        ]
    )

    # 27. WSA Guide
    build_page(
        "Windows Subsystem for Android",
        "wsa-guide.html",
        "Run Android apps on Windows 11, install APKs, manage subsystems, and developer tips.",
        "Windows",
        "fab fa-windows",
        [
            ("What is WSA?",
             "<p>Windows Subsystem for Android (WSA) enables Windows 11 to run Android applications natively on x86 and ARM devices. It provides a full Android 13 environment that integrates with the Windows Start Menu, taskbar, and notification center.</p>"
             "<p>WSA uses Hyper-V virtualization to run a custom Android OS image. Android apps appear alongside native Windows apps and support windowed mode, drag-and-drop, and clipboard sharing.</p>"
             "<p>System requirements:</p>"
             "<ul><li>Windows 11 (Build 22000+)</li>"
             "<li>8 GB RAM minimum (16 GB recommended)</li>"
             "<li>Solid-state drive (SSD)</li>"
             "<li>Virtualization enabled in BIOS (VT-x/AMD-V)</li></ul>"),
            ("Installation & Setup",
             "<p>Install WSA via Microsoft Store or command line:</p>"
             "<pre><code># Option 1: Microsoft Store\n# Search \"Amazon Appstore\" and install (includes WSA)\n\n# Option 2: winget\nwinget install 9P3395VX91NR\n\n# Option 3: Manual install (for sideloading)\n# Download WSA .msixbundle from https://store.rg-adguard.net/\n# Search for \"MicrosoftCorporationII.WindowsSubsystemForAndroid\"\n\n# Enable Developer Mode\n# Settings > Privacy & Security > For developers > Developer Mode</code></pre>"
             "<p>After installation, launch WSA from Start Menu. You can enable developer settings and ADB debugging from the WSA Settings app.</p>"),
            ("Installing APKs & Sideloading",
             "<p>Sideload Android apps not available on the Amazon Appstore:</p>"
             "<pre><code># Enable developer mode in WSA Settings\n# Enable \"Developer mode\" toggle\n\n# Install ADB (Android Debug Bridge)\nwinget install Google.PlatformTools\n\n# Connect to WSA\nadb connect 127.0.0.1:58526\n\n# Install APK\nadb install my-app.apk\n\n# List installed packages\nadb shell pm list packages\n\n# Uninstall app\nadb uninstall com.example.app</code></pre>"
             "<p>You can also use <strong>WSATools</strong> (from Microsoft Store) for a GUI-based APK installer. For bulk installations, use <code>adb install-multiple</code> for split APKs.</p>"),
            ("Configuration & Performance",
             "<p>Optimize WSA performance in its Settings app:</p>"
             "<pre><code># WSA Settings options:\n# - Subsystem resources: Continuous (always running) or As needed\n# - Graphics: Compatible or Advanced (GPU passthrough)\n# - Memory: Auto or manual allocation\n\n# Advanced GPU settings for gamers\n# Install GPU drivers from your OEM (Intel, NVIDIA, AMD)\n# Enable \"Advanced graphics\" in WSA Settings\n\n# Keyboard shortcuts\n# F11 -- toggle fullscreen\n# Win+Shift+W -- switch between WSA and Windows input\n# Ctrl+Alt+Delete -- send Ctrl+Alt+Delete to Android</code></pre>"
             "<p>For better performance: allocate at least 4 GB RAM to WSA, use SSD storage, and close unused Android apps via the subsystem task manager.</p>"),
            ("Troubleshooting & Tips",
             "<p>Common issues and solutions:</p>"
             "<ul><li><strong>WSA won't start</strong> -- enable virtualization in BIOS, ensure Hyper-V is enabled (<code>Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V</code>)</li>"
             "<li><strong>App crashes on launch</strong> -- check graphics compatibility mode in WSA Settings, update GPU drivers</li>"
             "<li><strong>ADB connection refused</strong> -- restart WSA, verify developer mode is on, check port 58526</li>"
             "<li><strong>No internet in apps</strong> -- WSA shares Windows network stack; try <code>ipconfig /flushdns</code> or restart WSA</li></ul>"
             "<pre><code># Reset WSA\n# Settings > Apps > Windows Subsystem for Android > Advanced options > Reset\n\n# Check WSA logs\n# Run WSA Settings > Diagnostics > Save logs</code></pre>"),
        ],
        [
            ("WSA Documentation (Microsoft)", "https://learn.microsoft.com/en-us/windows/android/wsa/", "Official Windows Subsystem for Android docs"),
            ("WSA GitHub Community", "https://github.com/microsoft/WSA", "Community discussions and issues"),
            ("ADB Documentation", "https://developer.android.com/studio/command-line/adb", "Android Debug Bridge reference"),
        ]
    )

    # 28. Windows Sandbox
    build_page(
        "Windows Sandbox Guide",
        "windows-sandbox.html",
        "Isolated test environment using Windows Sandbox, configuration files, and practical use cases.",
        "Windows",
        "fab fa-windows",
        [
            ("What is Windows Sandbox?",
             "<p>Windows Sandbox is a lightweight desktop environment that provides isolated, temporary desktops for running untrusted applications safely. It is essentially a minimal Windows running inside Hyper-V -- any changes made inside the sandbox are discarded when you close it.</p>"
             "<p>Key features:</p>"
             "<ul><li>Isolated kernel -- sandbox runs a separate instance of Windows kernel</li>"
             "<li>No persistent state -- everything resets on close</li>"
             "<li>Host integration -- clipboard sharing, file copy/paste, network access</li>"
             "<li>Hardware-accelerated -- uses GPU virtualization for graphics</li></ul>"
             "<p>Requirements: Windows 10 Pro/Enterprise (Build 18305+) or Windows 11 Pro/Enterprise, AMD64 architecture, virtualization enabled in BIOS.</p>"),
            ("Enabling Windows Sandbox",
             "<p>Enable the feature through Windows Features or PowerShell:</p>"
             "<pre><code># Method 1: Windows Features\n# Control Panel > Programs > Turn Windows features on or off\n# Check \"Windows Sandbox\" > OK > Restart\n\n# Method 2: PowerShell (Admin)\nEnable-WindowsOptionalFeature -Online -FeatureName \"Containers-DisposableClientVM\" -All\n\n# Method 3: DISM\nDISM /Online /Enable-Feature /FeatureName:\"Containers-DisposableClientVM\" /All\n\n# Verify installation\nGet-WindowsOptionalFeature -Online -FeatureName \"Containers-DisposableClientVM\"</code></pre>"
             "<p>After restart, find <strong>Windows Sandbox</strong> in the Start Menu. Launch it to get a fresh, clean Windows desktop.</p>"),
            ("Configuration Files (.wsb)",
             "<p>Windows Sandbox supports XML configuration files for customizing the environment:</p>"
             "<pre><code>&lt;?xml version=\"1.0\" encoding=\"utf-8\" ?&gt;\n&lt;Configuration&gt;\n  &lt;MappedFolders&gt;\n    &lt;MappedFolder&gt;\n      &lt;HostFolder&gt;C:\\Projects\\test-files&lt;/HostFolder&gt;\n      &lt;ReadOnly&gt;true&lt;/ReadOnly&gt;\n    &lt;/MappedFolder&gt;\n  &lt;/MappedFolders&gt;\n  &lt;LogonCommand&gt;\n    &lt;Command&gt;explorer.exe C:\\Users\\WDAGUtilityAccount\\Desktop\\test-files&lt;/Command&gt;\n  &lt;/LogonCommand&gt;\n  &lt;AudioInput&gt;disable&lt;/AudioInput&gt;\n  &lt;VideoInput&gt;disable&lt;/VideoInput&gt;\n  &lt;ProtectedClient&gt;enable&lt;/ProtectedClient&gt;\n  &lt;Networking&gt;disable&lt;/Networking&gt;\n&lt;/Configuration&gt;</code></pre>"
             "<p>Save as <code>sandbox-config.wsb</code> and double-click to launch. The configuration supports mapped folders, startup commands, GPU passthrough, and clipboard sharing toggles.</p>"),
            ("Practical Use Cases",
             "<p>Windows Sandbox is valuable for many scenarios:</p>"
             "<ul><li><strong>Testing suspicious software</strong> -- run unknown EXEs, installers, or browser extensions safely</li>"
             "<li><strong>Previewing documents</strong> -- open PDFs, Office files, or email attachments in isolation</li>"
             "<li><strong>Developer testing</strong> -- test application installation, registry changes, system modifications</li>"
             "<li><strong>Short-term computing</strong> -- run a clean browser for a specific task without risking your main profile</li>"
             "<li><strong>Training & demos</strong> -- provide a consistent, clean environment for tutorials</li></ul>"
             "<p>Note: The sandbox does not persist data. Copy files out before closing if you need to save results.</p>"),
        ],
        [
            ("Windows Sandbox Documentation", "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/", "Official Microsoft Windows Sandbox documentation"),
            ("WSB Configuration Reference", "https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-sandbox/windows-sandbox-configure-using-wsb-file", "XML configuration file reference"),
            ("Windows Sandbox on GitHub", "https://github.com/microsoft/Windows-Sandbox", "Sample configuration files and scripts"),
        ]
    )

    # 29. Group Policy Editor
    build_page(
        "Windows Group Policy Editor",
        "gpedit-guide.html",
        "Local Group Policy, administrative templates, security policies, and computer configuration management.",
        "Windows",
        "fab fa-windows",
        [
            ("What is Group Policy?",
             "<p>Group Policy is a Microsoft Windows infrastructure that allows administrators to implement specific configurations for users and computers. It controls the operating system, applications, and user settings in an Active Directory environment. Local Group Policy Editor (<code>gpedit.msc</code>) provides the same functionality on standalone Windows machines.</p>"
             "<p>Group Policy settings are organized into two main categories:</p>"
             "<ul><li><strong>Computer Configuration</strong> -- applied at system startup, affects all users</li>"
             "<li><strong>User Configuration</strong> -- applied at user logon, affects specific users</li></ul>"
             "<p>Each category contains Administrative Templates (registry-based policies), Windows Settings (security, scripts, folder redirection), and software installation settings.</p>"),
            ("Opening & Navigating Local Group Policy Editor",
             "<p>Launch and navigate the Group Policy Editor:</p>"
             "<pre><code># Open Local Group Policy Editor (Windows Pro/Enterprise only)\ngpedit.msc\n\n# Open Group Policy Management (for domain environments)\ngpmc.msc\n\n# Resultant Set of Policy (what policies are applied)\nrsop.msc\n\n# Command-line policy update\ngpupdate /force\ngpresult /r  # View effective policy\ngpresult /h policy-report.html  # HTML report</code></pre>"
             "<p>Navigate the tree: <strong>Computer Configuration > Windows Settings > Security Settings > Local Policies > Security Options</strong> is the most common path for security hardening.</p>"),
            ("Key Security Policies",
             "<p>Essential security policies to configure:</p>"
             "<pre><code># Password Policy (Computer > Windows Settings > Security > Account Policies)\n# - Enforce password history: 24 passwords remembered\n# - Maximum password age: 60 days\n# - Minimum password length: 14 characters\n# - Password must meet complexity requirements: Enabled\n\n# Account Lockout Policy\n# - Account lockout threshold: 5 invalid attempts\n# - Account lockout duration: 30 minutes\n# - Reset account lockout counter after: 30 minutes\n\n# User Rights Assignment (Security Settings > Local Policies)\n# - Deny log on through Remote Desktop Services: add Guests, Local Accounts\n\n# Security Options\n# - Network access: Do not allow anonymous enumeration of SAM accounts\n# - Microsoft network server: Digitally sign communications (always)</code></pre>"),
            ("Administrative Templates & Registry-Based Policies",
             "<p>Administrative Templates control hundreds of Windows features via registry. Common examples:</p>"
             "<pre><code># Computer > Admin Templates > Windows Components > Windows Update\n# - Configure Automatic Updates: Enabled (4 - Auto download and install)\n# - Specify intranet Microsoft update service location (for WSUS)\n\n# User > Admin Templates > Start Menu and Taskbar\n# - Remove Run menu from Start Menu: Disabled (keep Run)\n# - Remove notification and action center: Disabled\n\n# Computer > Admin Templates > System > Device Installation\n# - Prevent installation of removable devices: Enabled (block USB drives)\n\n# Custom ADMX templates can be added:\n# Copy .admx files to C:\\Windows\\PolicyDefinitions\\\n# Copy .adml files to C:\\Windows\\PolicyDefinitions\\en-US\\</code></pre>"),
            ("Managing Policies via PowerShell",
             "<p>PowerShell provides programmatic access to Group Policy:</p>"
             "<pre><code># Get installed Administrative Templates\nGet-ADMXTemplate -Name | Format-Table\n\n# Backup all Local Group Policy settings\n$backupPath = \"C:\\Backups\\GPO_$(Get-Date -Format yyyyMMdd)\"\nBackup-GPO -Name \"Local Policy\" -Path $backupPath\n\n# Reset Local Group Policy to defaults\nRemove-Item -Recurse -Force $env:windir\\System32\\GroupPolicy\\*\ngpupdate /force\n\n# Check specific policy setting\n# Use LGPO.exe tool from Microsoft for advanced management\n# Download: https://www.microsoft.com/en-us/download/details.aspx?id=55319</code></pre>"),
        ],
        [
            ("Group Policy Overview (Microsoft)", "https://learn.microsoft.com/en-us/windows/client-management/group-policy/", "Official Microsoft Group Policy documentation"),
            ("Group Policy Settings Reference", "https://www.microsoft.com/en-us/download/details.aspx?id=25250", "Spreadsheet of all Group Policy settings"),
            ("LGPO Utility", "https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/", "Local Group Policy Object utility"),
        ]
    )

    # 30. BitLocker Deep Dive
    build_page(
        "Windows BitLocker Deep Dive",
        "bitlocker-deep-dive.html",
        "Full disk encryption, TPM, recovery keys, BitLocker management, and enterprise deployment.",
        "Windows",
        "fab fa-windows",
        [
            ("BitLocker Overview & Architecture",
             "<p>BitLocker Drive Encryption is a full volume encryption feature in Windows Professional and Enterprise editions. It encrypts the entire operating system volume, protecting data at rest. BitLocker uses AES encryption (128-bit or 256-bit) in XTS or CBC mode with an Elephant diffuser for disk sector encryption.</p>"
             "<p>Key components:</p>"
             "<ul><li><strong>TPM (Trusted Platform Module)</strong> -- stores encryption keys securely; validates boot integrity</li>"
             "<li><strong>BitLocker System Boot</strong> -- requires a separate, unencrypted system partition for boot files</li>"
             "<li><strong>Recovery Key</strong> -- 48-digit numeric password used when TPM fails or boot chain changes</li>"
             "<li><strong>Secure Boot</strong> -- ensures only trusted firmware and OS components load</li></ul>"),
            ("Enabling BitLocker",
             "<p>Enable BitLocker via Control Panel or PowerShell:</p>"
             "<pre><code># Check TPM status\ntpm.msc\nGet-Tpm\n\n# Enable BitLocker (Control Panel)\n# Control Panel > System and Security > BitLocker Drive Encryption > Turn on BitLocker\n\n# Enable via PowerShell (Admin)\nEnable-BitLocker -MountPoint \"C:\" -EncryptionMethod XtsAes256 -UsedSpaceOnly \\\n    -RecoveryPasswordProtector -SkipHardwareTest\n\n# Add recovery key protector\nAdd-BitLockerKeyProtector -MountPoint \"C:\" -RecoveryPasswordProtector\n\n# Backup recovery key to Microsoft Account\nBackup-BitLockerKeyProtector -MountPoint \"C:\" -KeyProtectorId \"{GUID}\"\n\n# Check encryption status\nGet-BitLockerVolume -MountPoint \"C:\"</code></pre>"),
            ("TPM & Key Protectors",
             "<p>BitLocker uses multiple key protectors to secure the Volume Master Key (VMK):</p>"
             "<pre><code># TPM protector (default) -- key released only if boot integrity check passes\n# TPM+PIN -- requires user PIN at boot\n# TPM+Startup Key -- requires USB key at boot\n# Recovery Password -- 48-digit key for rescue scenarios\n# Password (Data Drives) -- password-based protection for fixed/removable drives\n\n# Configure TPM+PIN for enhanced security\n# Group Policy: Computer > Admin Templates > Windows Components > BitLocker\n# \"Configure TPM startup PIN\" > Enabled\n# Set PIN: 4-20 digits\n\n# Add TPM with PIN protector\nAdd-BitLockerKeyProtector -MountPoint \"C:\" -TpmAndPinProtector\n\n# View protectors\nGet-BitLockerVolume -MountPoint \"C:\" | Select-Object KeyProtector</code></pre>"),
            ("Recovery & Data Recovery",
             "<p>When BitLocker prompts for recovery, use these methods:</p>"
             "<pre><code># Common triggers for recovery mode:\n# - BIOS/UEFI update\n# - Boot configuration changes\n# - TPM firmware update\n# - Disk controller changes (AHCI vs RAID)\n\n# Suspend BitLocker (before hardware changes)\nSuspend-BitLocker -MountPoint \"C:\" -RebootCount 2\n\n# Resume protection\nResume-BitLocker -MountPoint \"C:\"\n\n# Find recovery key:\n# 1. Microsoft Account (https://account.microsoft.com/devices/recoverykey)\n# 2. Active Directory (if domain-joined)\n# 3. Print or USB backup\n\n# Recovery key file\n# C:\\Users\\%USERNAME%\\AppData\\Roaming\\Microsoft\\RecoveryKey\\*.txt\n\n# Manual unlock (if recovery key known)\nUnlock-BitLocker -MountPoint \"D:\" -RecoveryPassword \"48-digit-key\"</code></pre>"),
            ("BitLocker Management & Enterprise Deployment",
             "<p>Manage BitLocker at scale with MBAM or PowerShell:</p>"
             "<pre><code># MBAM (Microsoft BitLocker Administration and Monitoring)\n# - Part of Microsoft Desktop Optimization Pack (MDOP)\n# - Centralized key escrow, compliance reporting, self-service recovery\n\n# Manage-BDE command-line tool\nmanage-bde -status C:\nmanage-bde -protectors -get C:\nmanage-bde -off C:   # Decrypt\nmanage-bde -on C:     # Encrypt with defaults\n\n# Enterprise deployment via GPO\n# Computer > Admin Templates > Windows Components > BitLocker Drive Encryption\n# - Choose drive encryption method and cipher strength: XTS-AES 256-bit\n# - Require additional authentication at startup: Enabled (TPM+PIN)\n# - Deny write access to removable drives not protected by BitLocker: Enabled</code></pre>"),
        ],
        [
            ("BitLocker Documentation (Microsoft)", "https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/", "Official BitLocker documentation"),
            ("BitLocker Recovery Guide", "https://learn.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-recovery-guide", "Recovery key management and procedures"),
            ("TPM Basics", "https://trustedcomputinggroup.org/resource/tpm-library-specification/", "Trusted Platform Module specifications"),
        ]
    )

    # 31. Windows Performance Monitor
    build_page(
        "Windows Performance Monitor",
        "windows-perfmon.html",
        "Data collector sets, performance counters, reports, and troubleshooting with PerfMon.",
        "Windows",
        "fab fa-windows",
        [
            ("Performance Monitor Overview",
             "<p>Performance Monitor (PerfMon) is a Windows tool that collects and displays real-time performance data. It helps identify bottlenecks in CPU, memory, disk, network, and application performance. PerfMon can log data over time, alert on thresholds, and generate HTML reports.</p>"
             "<p>Launch PerfMon via:</p>"
             "<pre><code>perfmon.msc\nperfmon /rel   # Reliability Monitor\nperfmon /sys   # System Summary</code></pre>"
             "<p>Performance Monitor works with <strong>Performance Counters</strong> -- numeric metrics published by the OS, drivers, and applications. Thousands of counters exist for processors, memory, disks, network adapters, processes, and .NET runtime.</p>"),
            ("Working with Performance Counters",
             "<p>Add and analyze performance counters in real-time:</p>"
             "<pre><code># In PerfMon GUI:\n# 1. Expand Monitoring Tools > Performance Monitor\n# 2. Click the green + button\n# 3. Select counters (use Ctrl+click for multiple)\n\n# Essential counters to monitor:\n# \\Memory\\Pages/sec          -- Memory pressure\n# \\Processor(_Total)\\% Processor Time  -- CPU usage\n# \\PhysicalDisk(_Total)\\% Disk Time     -- Disk activity\n# \\Network Interface(*)\\Bytes Total/sec -- Network throughput\n\n# Logman command-line (create data collector)\nlogman create counter system_monitor \\\n    -c \"\\Processor(_Total)\\% Processor Time\" \\\n       \"\\Memory\\Available MBytes\" \\\n       \"\\PhysicalDisk(_Total)\\% Disk Time\" \\\n    -o \"C:\\PerfLogs\\system_monitor.blg\" \\\n    -f bincirc -max 500 -si 00:00:15</code></pre>"),
            ("Data Collector Sets & Logging",
             "<p>Data Collector Sets (DCS) are groups of counters, configuration, and alerts that run on a schedule:</p>"
             "<pre><code># Create a DCS via GUI:\n# 1. Expand Data Collector Sets > User Defined\n# 2. Right-click > New > Data Collector Set\n# 3. Choose \"Create from a template\" or \"Create manually\"\n\n# Create via PowerShell\n$dcs = New-Object -COM Pla.DataCollectorSet\n$dcs.DisplayName = \"My Custom Monitor\"\n$dcs.Duration = 86400  # 24 hours\n$dcs.SubdirectoryFormat = 1  # Day-monotonic\n$dcs.SubdirectoryFormatPattern = \"yyyy-MM-dd\"\n$dcs.Commit(\"My Custom Monitor\", $null, 3)  # 3 = add/modify\n\n# System Collector Sets (built-in):\n# - System Diagnostics: 60-second high-resolution snapshot\n# - System Performance: Performance analysis with report\n# - Active Directory Diagnostics: Domain controller health</code></pre>"),
            ("Analyzing Performance Reports",
             "<p>PerfMon generates detailed HTML reports for data collector sets:</p>"
             "<pre><code># Generate report from a .blg file\nrelog.exe C:\\PerfLogs\\system_monitor.blg -f CSV -o report.csv\n\n# Use PowerShell to analyze counter data\n$counters = Get-Counter -Counter @(\n    \"\\Processor(_Total)\\% Processor Time\",\n    \"\\Memory\\Available MBytes\"\n) -SampleInterval 5 -MaxSamples 60\n\n$counters.CounterSamples | ForEach-Object {\n    [PSCustomObject]@{\n        TimeStamp = $_.TimeStamp\n        CPU = ($_.CookedValue | Where Path -like \"*Processor*\").CookedValue\n        Memory = ($_.CookedValue | Where Path -like \"*Memory*\").CookedValue\n    }\n}\n\n# View built-in report\n# PerfMon > Reports > User Defined > select your DCS > right-click > View Report</code></pre>"),
            ("Alerts & Troubleshooting Scenarios",
             "<p>Set up alerts for proactive monitoring:</p>"
             "<pre><code># Create alert via GUI:\n# Data Collector Sets > User Defined > New > Data Collector Set\n# Choose \"Performance Counter Alert\"\n\n# Configure alert conditions:\n# - \\Processor(_Total)\\% Processor Time > 90% for 10 seconds\n# - \\LogicalDisk(C:)\\% Free Space < 10%\n# - \\Memory\\Available MBytes < 512\n\n# Action: Log an entry in the application event log\n# Or run a script:\n# powershell.exe -Command \"Send-MailMessage -To admin@example.com ...\"\n\n# Common troubleshooting with PerfMon:\n# High CPU: Identify which process in Process\\% Processor Time\n# Memory leak: Monitor Process\\Private Bytes over time\n# Disk bottleneck: Check PhysicalDisk\\Avg. Disk Queue Length > 2</code></pre>"),
        ],
        [
            ("Performance Monitor Guide", "https://learn.microsoft.com/en-us/windows-server/administration/performance-monitor/", "Official Microsoft PerfMon documentation"),
            ("Windows Performance Toolkit", "https://learn.microsoft.com/en-us/windows-hardware/test/wpt/", "Advanced ETW-based performance tools from Microsoft"),
            ("PerfMon Best Practices", "https://techcommunity.microsoft.com/blog/windows-it-pro-blog/", "Community tips and performance analysis guides"),
        ]
    )

    # 32. Windows Remote Desktop
    build_page(
        "Windows Remote Desktop Guide",
        "windows-remote-desktop.html",
        "RDP configuration, gateway, security best practices, and third-party alternatives.",
        "Windows",
        "fab fa-windows",
        [
            ("Remote Desktop Protocol (RDP) Overview",
             "<p>Remote Desktop Protocol (RDP) allows users to connect to a remote Windows computer over a network. Developed by Microsoft, RDP provides full desktop access, file sharing, printer redirection, clipboard sharing, and audio/video streaming.</p>"
             "<p>RDP operates on port 3389 over TCP (and UDP for RemoteFX). Modern RDP 10.x includes support for H.264/H.265 codecs, multi-monitor setups, and touch input. Windows 11 Pro, Enterprise, and Windows Server include RDP host support; Windows Home only provides the client.</p>"),
            ("Enabling & Configuring RDP",
             "<p>Enable Remote Desktop on your Windows machine:</p>"
             "<pre><code># GUI: Settings > System > Remote Desktop > Enable Remote Desktop\n\n# PowerShell (Admin)\nSet-ItemProperty -Path \"HKLM:\\System\\CurrentControlSet\\Control\\Terminal Server\" -Name \"fDenyTSConnections\" -Value 0\nEnable-NetFirewallRule -DisplayGroup \"Remote Desktop\"\n\n# Configure RDP port (optional, for security)\n# Registry: HKLM\\System\\CurrentControlSet\\Control\\Terminal Server\\WinStations\\RDP-Tcp\\PortNumber\n# Change from 3389 to a custom port (e.g., 3390)\n\n# Network Level Authentication (NLA) -- recommended\n# Group Policy: Computer > Admin Templates > Windows Components > Remote Desktop Services > Remote Desktop Session Host > Security\n# \"Require user authentication for remote connections using NLA\" > Enabled</code></pre>"),
            ("Remote Desktop Gateway & RD Web Access",
             "<p>RD Gateway provides secure HTTPS-based RDP access from the internet:</p>"
             "<pre><code># RD Gateway components:\n# - RD Gateway Server: acts as HTTPS proxy for RDP connections\n# - RD Web Access: provides web portal for launching remote apps\n# - RD Connection Broker: load balances across session hosts\n\n# Install RD Gateway role (Windows Server)\nInstall-WindowsFeature -Name RDS-Gateway -IncludeManagementTools\n\n# Configure RD Gateway with SSL certificate\n# Certificates must be trusted by clients (public CA or enterprise CA)\n\n# Client-side connection: mstsc.exe /v:gateway.example.com /g:internal-pc.company.local\n\n# Alternative: RD Client for macOS, iOS, Android\n# Download from respective app stores</code></pre>"),
            ("Security Best Practices",
             "<p>Secure your RDP deployment against attacks:</p>"
             "<ul><li><strong>Use Network Level Authentication (NLA)</strong> -- prevents brute force at the protocol level</li>"
             "<li><strong>Change default port (3389)</strong> -- reduces automated scanning attacks</li>"
             "<li><strong>Enable account lockout policies</strong> -- 5 failed attempts = 30-minute lockout</li>"
             "<li><strong>Restrict users</strong> -- add only required users to Remote Desktop Users group</li>"
             "<li><strong>Use RD Gateway or VPN</strong> -- never expose RDP directly to the internet</li>"
             "<li><strong>Enable Conditional Access</strong> -- require MFA for remote access (Azure AD)</li></ul>"
             "<pre><code># Restrict access to specific users\nnet localgroup \"Remote Desktop Users\" DOMAIN\\alice /add\n\n# View active RDP sessions\nqwinsta /server:localhost\n\n# Disconnect session (force)\nrwinsta /server:localhost 2  # Session ID 2</code></pre>"),
            ("Alternatives & Third-Party Tools",
             "<p>When RDP is not suitable, consider these alternatives:</p>"
             "<ul><li><strong>RustDesk</strong> -- open-source remote desktop, self-hosted or relay server</li>"
             "<li><strong>Chrome Remote Desktop</strong> -- browser-based, good for cross-platform help desk</li>"
             "<li><strong>TeamViewer</strong> -- commercial, works through firewalls, supports unattended access</li>"
             "<li><strong>AnyDesk</strong> -- lightweight, fast, supports file transfer and VPN</li>"
             "<li><strong>Apache Guacamole</strong> -- web-based gateway supporting RDP, VNC, SSH in browser</li></ul>"
             "<p>For pure RDP management across many machines, use <strong>Remote Desktop Manager</strong> (Devolutions) or <strong>mRemoteNG</strong>.</p>"),
        ],
        [
            ("RDP Documentation", "https://learn.microsoft.com/en-us/windows/win32/termserv/remote-desktop-protocol", "Official Microsoft Remote Desktop Protocol documentation"),
            ("RD Gateway Configuration", "https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/", "Remote Desktop Services deployment guides"),
            ("RDP Security Hardening", "https://www.cisa.gov/news-events/news/securing-remote-desktop-protocol-rdp", "CISA guidance on securing RDP"),
        ]
    )

    # 33. Windows 11 Features
    build_page(
        "Windows 11 Features Guide",
        "windows-11-features.html",
        "New features, settings, changes from Windows 10, and power user tips.",
        "Windows",
        "fab fa-windows",
        [
            ("What's New in Windows 11",
             "<p>Windows 11 introduced a redesigned user interface, improved performance, and new features focused on productivity and security. The most visible change is the centered Start Menu and taskbar, but significant changes run deeper:</p>"
             "<ul><li><strong>Redesigned UI</strong> -- rounded corners, Mica material, Fluent Design icons, centered taskbar</li>"
             "<li><strong>Snap Layouts</strong> -- hover over maximize button to snap windows in preset layouts</li>"
             "<li><strong>Snap Groups</strong> -- taskbar groups of snapped apps persist between app switches</li>"
             "<li><strong>Widgets</strong> -- AI-powered customizable news, weather, calendar panel from left swipe</li>"
             "<li><strong>Microsoft Teams Chat</strong> -- integrated video calling and chat (now replaced by Teams 2.0)</li>"
             "<li><strong>Virtual Desktops</strong> -- separate wallpapers per desktop, improved management</li></ul>"),
            ("System Requirements & Settings Changes",
             "<p>Windows 11 raised the hardware bar significantly:</p>"
             "<pre><code># Minimum requirements:\n# - 1 GHz dual-core 64-bit processor\n# - 4 GB RAM\n# - 64 GB storage\n# - TPM 2.0 (Trusted Platform Module)\n# - Secure Boot capable\n# - DirectX 12 compatible graphics\n\n# Check compatibility\nGet-WmiObject -Namespace root\\cimv2\\Security\\MicrosoftTpm -Class Win32_Tpm\n\n# Bypass TPM check (not recommended for production)\n# Registry: HKLM\\SYSTEM\\Setup\\LabConfig\n# DWORD: BypassTPMCheck = 1\n# DWORD: BypassSecureBootCheck = 1\n\n# Settings reorganization:\n# - Settings app redesigned with categories, breadcrumbs\n# - Windows Update settings more granular\n# - New > Personalization > Colors > \"Show accent color on Start and taskbar\"</code></pre>"),
            ("Power User Features & Hidden Gems",
             "<p>Lesser-known but powerful Windows 11 features:</p>"
             "<pre><code># Enhanced taskbar shortcuts\n# Win + T -- cycle through taskbar apps\n# Win + B -- focus notification area\n# Win + A -- Quick Settings panel\n# Win + N -- Notification center / Calendar\n# Win + W -- Widgets panel\n\n# File Explorer tabs (Windows 11 22H2+)\n# Open multiple folder tabs in File Explorer (Ctrl+T, Ctrl+W, Ctrl+Tab)\n\n# Voice Access (Accessibility)\n# Settings > Accessibility > Speech > Voice Access\n# Control PC entirely by voice\n\n# Focus Sessions (Clock app)\n# Integrated Pomodoro timer with Spotify integration\n\n# Sudo for Windows (Windows 11 24H2+)\n# Elevated commands without opening new terminal</code></pre>"),
            ("Performance & Power Improvements",
             "<p>Windows 11 includes under-the-hood improvements for performance:</p>"
             "<ul><li><strong>Memory management</strong> -- improved memory compression, fewer background processes</li>"
             "<li><strong>Power efficiency</strong> -- longer battery life on laptops (Intel 12th+ Gen optimized)</li>"
             "<li><strong>DirectStorage</strong> -- faster game loading from NVMe SSDs (requires compatible game)</li>"
             "<li><strong>Auto HDR</strong> -- enhances SDR games with HDR coloring</li>"
             "<li><strong>Smart App Control</strong> -- AI-based app reputation security (replaces S Mode)</li></ul>"
             "<pre><code># Performance settings\n# System > About > Advanced system settings > Performance > Adjust for best performance\n\n# Game Mode\n# Settings > Gaming > Game Mode > Enabled\n# Win + G -- Game Bar overlay</code></pre>"),
            ("Privacy, Security & Enterprise Features",
             "<p>Windows 11 strengthens security and privacy:</p>"
             "<ul><li><strong>Windows Hello Enhanced Sign-in</strong> -- biometric authentication with improved anti-spoofing</li>"
             "<li><strong>Microsoft Pluton</strong> -- TPM integrated directly in CPU (supported on select devices)</li>"
             "<li><strong>Credential Guard</strong> -- isolates credentials in virtualized environment (Enterprise)</li>"
             "<li><strong>Microsoft Defender for Business</strong> -- enterprise-grade endpoint protection</li>"
             "<li><strong>Personal Data Encryption</strong> -- protects user files even when OS is running (Enterprise)</li></ul>"
             "<pre><code># Privacy dashboard\n# Settings > Privacy & Security > Windows permissions\n# - Review app permissions (camera, microphone, location, etc.)\n# - Diagnostic data viewer: see what data Microsoft collects\n\n# Windows Security\n# Check health: Get-MpComputerStatus\n# Quick scan: Start-MpScan -ScanType QuickScan</code></pre>"),
        ],
        [
            ("Windows 11 Documentation", "https://learn.microsoft.com/en-us/windows/whats-new/windows-11-overview", "Official Windows 11 overview and documentation"),
            ("Windows IT Pro Blog", "https://techcommunity.microsoft.com/t5/windows-it-pro-blog/bg-p/Windows10Blog", "Enterprise-focused Windows news and guides"),
            ("Windows 11 Known Issues", "https://learn.microsoft.com/en-us/windows/release-health/", "Windows release health dashboard and known issues"),
        ]
    )

    # ========== NETWORKING (8) ==========

    # 34. BGP Routing
    build_page(
        "BGP Routing Basics",
        "bgp-basics.html",
        "Border Gateway Protocol, AS numbers, peering, route selection, and BGP security with RPKI.",
        "Networking",
        "fas fa-network-wired",
        [
            ("What is BGP?",
             "<p>Border Gateway Protocol (BGP) is the routing protocol that makes the internet work. It is a path-vector protocol that exchanges routing and reachability information between autonomous systems (ASes). BGP replaces earlier EGP and has been the internet's core routing protocol since 1993.</p>"
             "<p>Key concepts:</p>"
             "<ul><li><strong>Autonomous System (AS)</strong> -- a network under a single administrative domain, identified by a unique AS number (ASN)</li>"
             "<li><strong>eBGP</strong> -- external BGP; routes exchanged between different ASes</li>"
             "<li><strong>iBGP</strong> -- internal BGP; routes exchanged within the same AS</li>"
             "<li><strong>CIDR notation</strong> -- BGP advertises IP prefixes with subnet masks (e.g., 203.0.113.0/24)</li></ul>"),
            ("BGP Path Attributes & Route Selection",
             "<p>BGP uses path attributes to make routing decisions. When multiple paths exist, the router selects the best path using this order:</p>"
             "<pre><code>1. Highest Weight (Cisco proprietary, local to router)\n2. Highest Local Preference (local to AS)\n3. Prefer locally originated routes\n4. Shortest AS_PATH\n5. Lowest ORIGIN type (IGP &lt; EGP &lt; INCOMPLETE)\n6. Lowest MED (Multi-Exit Discriminator)\n7. eBGP preferred over iBGP\n8. Shortest IGP metric to next-hop\n9. Oldest route (eBGP) or lowest Router ID (iBGP)\n\n# Common AS_PATH prepending example:\n# route-map SET_PATH permit 10\n#   set as-path prepend 64510 64510 64510\n\n# BGP community string example:\n# 64510:80  -- prepend to upstream peers\n# 64510:90  -- announce to all peers</code></pre>"),
            ("BGP Peering & Configuration",
             "<p>Configure a basic BGP peering on a Cisco router or Linux with FRR/BIRD:</p>"
             "<pre><code># Cisco IOS XE\nrouter bgp 64500\n bgp router-id 192.0.2.1\n neighbor 203.0.113.1 remote-as 64501\n neighbor 203.0.113.1 description TRANSIT_PROVIDER\n neighbor 203.0.113.1 password my-secret\n !\n address-family ipv4 unicast\n  network 192.0.2.0 mask 255.255.255.0\n  neighbor 203.0.113.1 activate\n  neighbor 203.0.113.1 route-map INBOUND in\n  neighbor 203.0.113.1 route-map OUTBOUND out\n exit-address-family\n\n# BIRD (Linux)\nprotocol bgp upstream {\n    local as 64500;\n    neighbor 203.0.113.1 as 64501;\n    source address 192.0.2.1;\n    password \"my-secret\";\n    ipv4 {\n        export filter {\n            if net ~ [192.0.2.0/24+] then accept;\n            reject;\n        };\n        import all;\n    };\n}</code></pre>"),
            ("BGP Security: RPKI, BGPsec & Prefix Filtering",
             "<p>BGP was designed without built-in security. Modern mitigation techniques include:</p>"
             "<pre><code># RPKI (Resource Public Key Infrastructure)\n# Validates that an AS is authorized to announce a prefix\n# Three states: VALID, INVALID, NOT_FOUND\n\n# Configure ROV (Route Origin Validation) on Cisco:\nrouter bgp 64500\n bgp rpki server tcp 192.0.2.10 port 323 refresh 600\n route-map RPKI-FILTER permit 10\n  match rpki valid\n route-map RPKI-FILTER deny 10\n  match rpki invalid\n\n# IRR (Internet Routing Registry) prefix filtering\n# Create prefix-list based on registered routes\nip prefix-list ALLOWED seq 5 permit 192.0.2.0/24\nneighbor 203.0.113.1 prefix-list ALLOWED in\n\n# BGPsec (draft standard, limited adoption)\n# Cryptographicly signs BGP updates using router keys\n\n# TTL Security (GTSM)\nneighbor 203.0.113.1 ttl-security hops 1</code></pre>"),
            ("Troubleshooting BGP",
             "<p>Common BGP troubleshooting commands:</p>"
             "<pre><code># Cisco\nshow ip bgp summary\nshow ip bgp neighbors 203.0.113.1 advertised-routes\nshow ip bgp neighbors 203.0.113.1 received-routes\nshow ip bgp 192.0.2.0/24\nshow ip route bgp\nping 203.0.113.1 source 192.0.2.1\n\n# Linux (FRR)\nvtysh\nrouter# show ip bgp summary\nrouter# show ip bgp 192.0.2.0/24\nrouter# show ip bgp neighbors 203.0.113.1\n\n# Linux (BIRD)\nsudo birdc show status\nsudo birdc show protocols\nsudo birdc show route for 192.0.2.0/24\nsudo birdc show route all</code></pre>"),
        ],
        [
            ("BGP Documentation (Cisco)", "https://www.cisco.com/c/en/us/support/docs/ip/border-gateway-protocol-bgp/26634-bgp-toc.html", "Cisco BGP configuration guides and best practices"),
            ("BGP on Wikipedia", "https://en.wikipedia.org/wiki/Border_Gateway_Protocol", "Comprehensive BGP overview and history"),
            ("Cloudflare RPKI Tool", "https://rpki.cloudflare.com/", "BGP RPKI validator and route origin validation tool"),
        ]
    )

    # 35. VLANs & Trunking
    build_page(
        "VLANs & Trunking Guide",
        "vlans-trunking.html",
        "802.1Q VLAN tagging, trunk ports, access ports, inter-VLAN routing, and troubleshooting.",
        "Networking",
        "fas fa-network-wired",
        [
            ("What are VLANs?",
             "<p>A Virtual Local Area Network (VLAN) is a logical grouping of devices on the same broadcast domain, even if they are physically connected to different switches. VLANs segment networks without requiring separate physical infrastructure, improving security, performance, and manageability.</p>"
             "<p>Key benefits:</p>"
             "<ul><li><strong>Traffic isolation</strong> -- broadcast traffic stays within the VLAN</li>"
             "<li><strong>Security</strong> -- sensitive devices isolated from general traffic</li>"
             "<li><strong>Simplified moves and changes</strong> -- re-VLANing a port is a configuration change, not a physical re-cable</li>"
             "<li><strong>Cost savings</strong> -- fewer switches and routers needed</li></ul>"),
            ("802.1Q Tagging & Trunking",
             "<p>802.1Q is the IEEE standard for VLAN tagging. Frames traversing a trunk port carry a 4-byte tag identifying the VLAN:</p>"
             "<pre><code># Access port -- untagged, assigned to single VLAN\ninterface GigabitEthernet0/1\n switchport mode access\n switchport access vlan 10\n spanning-tree portfast\n\n# Trunk port -- carries multiple VLANs with tags\ninterface GigabitEthernet0/24\n switchport trunk encapsulation dot1q\n switchport mode trunk\n switchport trunk native vlan 99  # Untagged traffic (management)\n switchport trunk allowed vlan 10,20,30,100-200\n switchport nonegotiate  # Disable DTP\n\n# Native VLAN -- frames without tags belong to this VLAN\n# Important: Native VLAN must match on both ends of trunk\n\n# Check trunk status\nshow interfaces trunk\nshow interfaces GigabitEthernet0/24 switchport</code></pre>"),
            ("Inter-VLAN Routing (Router-on-a-Stick & Layer 3 Switch)",
             "<p>Devices in different VLANs must route through a Layer 3 device:</p>"
             "<pre><code># Router-on-a-Stick (subinterfaces on router)\ninterface GigabitEthernet0/0.10\n encapsulation dot1Q 10\n ip address 192.168.10.1 255.255.255.0\n!\ninterface GigabitEthernet0/0.20\n encapsulation dot1Q 20\n ip address 192.168.20.1 255.255.255.0\n\n# Layer 3 Switch (SVI -- Switched Virtual Interface)\ninterface Vlan10\n ip address 192.168.10.1 255.255.255.0\n no shutdown\n!\ninterface Vlan20\n ip address 192.168.20.1 255.255.255.0\n no shutdown\n!\nip routing  # Enable IP routing on the switch</code></pre>"),
            ("VLAN Design Best Practices",
             "<p>Design a scalable VLAN architecture:</p>"
             "<pre><code># Recommended VLAN numbering scheme:\n# 1      -- Default VLAN (untagged, avoid using)\n# 10-19  -- User VLANs (data)\n# 20-29  -- Voice VLANs (VoIP)\n# 30-39  -- Management (switches, APs, IPMI)\n# 40-49  -- Guest/Public WiFi\n# 50-59  -- Server/DMZ\n# 60-69  -- IoT/OT devices\n# 99     -- Native/Blackhole VLAN\n# 100-199 -- Customer VLANs (MSP)\n# 999    -- Unused ports (shut down)\n\n# VTP (VLAN Trunking Protocol)\nvtp mode transparent  # Best practice: transparent mode\n\n# Private VLANs (PVLAN) -- micro-segmentation within a VLAN\n# Primary VLAN: carries all traffic\n# Community VLAN: ports can communicate within the community\n# Isolated VLAN: ports can only communicate with promiscuous port</code></pre>"),
            ("VLAN Troubleshooting",
             "<p>Common VLAN issues and diagnostic commands:</p>"
             "<pre><code># Check VLAN database\nshow vlan brief\nshow vlan id 10\n\n# Verify trunk status\nshow interfaces trunk\nshow interfaces GigabitEthernet0/24 trunk\n\n# Check MAC address table\nshow mac address-table vlan 10\n\n# Common issues:\n# 1. Trunk not forming -- check native VLAN mismatch\n# 2. Port stuck in blocking -- RSTP: verify port roles\n# 3. VLAN not in database -- create VLAN: vlan 10\n# 4. Allowed VLAN list missing -- check \"switchport trunk allowed vlan\"\n# 5. ACL blocking traffic -- verify inter-VLAN ACLs\n\n# Debug spanning tree\nshow spanning-tree vlan 10\ndebug spanning-tree events</code></pre>"),
        ],
        [
            ("802.1Q Standard", "https://standards.ieee.org/ieee/802.1Q/", "IEEE 802.1Q VLAN tagging standard"),
            ("Cisco VLAN Configuration Guide", "https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst9300/software/release/16-12/configuration_guide/vlan/b_1612_vlan_9300_cg.html", "Official Cisco VLAN configuration guide"),
            ("VLAN Security Best Practices", "https://www.cisco.com/c/en/us/support/docs/lan-switching/vlan/69230-vlan-security.html", "Hardening VLANs against attacks"),
        ]
    )

    # 36. SNMP Monitoring
    build_page(
        "SNMP Network Monitoring",
        "snmp-monitoring.html",
        "MIBs, OIDs, traps, snmpwalk, SNMPv3 security, and integration with monitoring tools.",
        "Networking",
        "fas fa-network-wired",
        [
            ("SNMP Overview & Versions",
             "<p>Simple Network Management Protocol (SNMP) is the standard protocol for monitoring and managing network devices. It collects data from routers, switches, servers, printers, and other IP-enabled devices. SNMP uses a manager-agent model where agents expose data through MIBs (Management Information Bases).</p>"
             "<p>Three major versions exist:</p>"
             "<ul><li><strong>SNMPv1</strong> -- basic read/write, plaintext community strings (obsolete)</li>"
             "<li><strong>SNMPv2c</strong> -- improved protocol, bulk requests, still plaintext community</li>"
             "<li><strong>SNMPv3</strong> -- authenticated and encrypted communication (recommended)</li></ul>"
             "<p>Install SNMP tools on Linux:</p><pre><code>sudo apt install snmp snmpd snmp-mibs-downloader</code></pre>"),
            ("MIBs, OIDs & SNMP Walk",
             "<p>MIBs define the structure of SNMP data. OIDs (Object Identifiers) uniquely identify managed objects:</p>"
             "<pre><code># Common OIDs (from 1.3.6.1.2.1 - SNMP MIB-2 internet)\n# .1.3.6.1.2.1.1      -- System group\n# .1.3.6.1.2.1.2      -- Interfaces group\n# .1.3.6.1.2.1.4      -- IP group\n# .1.3.6.1.2.1.6      -- TCP group\n# .1.3.6.1.2.1.25     -- Host Resources\n\n# snmpwalk -- retrieve entire OID tree\nsnmpwalk -v2c -c public 192.168.1.1 .1.3.6.1.2.1\n\n# Query specific OID\nsnmpget -v2c -c public 192.168.1.1 .1.3.6.1.2.1.1.5.0  # sysName\nsnmpget -v2c -c public 192.168.1.1 .1.3.6.1.2.1.2.1.0  # Number of interfaces\n\n# snmpbulkwalk -- faster for large MIBs\nsnmpbulkwalk -v2c -c public 192.168.1.1 .1.3.6.1.2.1.25.2.3.1.3  # Storage types</code></pre>"),
            ("Configuring SNMPv3 (Authenticated & Encrypted)",
             "<p>SNMPv3 provides robust security with authentication (SHA) and encryption (AES):</p>"
             "<pre><code># Linux snmpd.conf (/etc/snmp/snmpd.conf)\n# Create SNMPv3 user\ncreateUser monitor SHA \"authPassword123\" AES \"encryptPassword456\"\nrouser monitor authpriv\n\n# Restrict to specific subnet\nagentAddress udp:161,udp6:[::1]:161\n\n# Cisco SNMPv3 configuration\nsnmp-server group MONITORS v3 priv\nsnmp-server user monitor MONITORS v3 auth sha authPassword123 priv aes 128 encryptPassword456\nsnmp-server host 192.168.1.100 version 3 priv monitor\n\n# Query SNMPv3 device\nsnmpwalk -v3 -u monitor -l authPriv \\\n    -a SHA -A \"authPassword123\" \\\n    -x AES -X \"encryptPassword456\" \\\n    192.168.1.1 .1.3.6.1.2.1.1</code></pre>"),
            ("SNMP Traps & Notifications",
             "<p>SNMP traps are unsolicited messages from agents to managers:</p>"
             "<pre><code># snmptrapd configuration (/etc/snmp/snmptrapd.conf)\nauthCommunity log,execute,net public\ntraphandle default /usr/bin/traptoemail --admin@example.com\n\n# Cisco trap configuration\nsnmp-server enable traps\nsnmp-server enable traps snmp authentication linkdown linkup\nsnmp-server enable traps config\nsnmp-server host 192.168.1.100 version 2c public udp-port 162\nsnmp-server host 192.168.1.100 version 3 priv monitor\n\n# Test trap generation\nsnmptrap -v2c -c public 192.168.1.100:162 '' \\\n    .1.3.6.1.4.1.99999.1 .1.3.6.1.4.1.99999.1.1 s \"Test Trap\"\n\n# Automation with trap receivers: Nagios, Zabbix, Prometheus (snmp_exporter)</code></pre>"),
            ("Monitoring Tools & Best Practices",
             "<p>Integrate SNMP with popular monitoring platforms:</p>"
             "<pre><code># Prometheus snmp_exporter\n# snmp.yml generator:\ngenerate: {\\n  - module: if_mib\\n    walk: [1.3.6.1.2.1.2, 1.3.6.1.2.1.31.1.1]\\n    max_repetitions: 25\\n\\n# librenms -- full SNMP discovery and monitoring\n# docker run -d --name librenms -p 80:80 librenms/librenms:latest\n\n# Zabbix SNMP template\nzabbix_get -s 192.168.1.1 -k \"snmpwalk[.1.3.6.1.2.1.1.5.0]\"\n\n# Best practices:\n# - Use SNMPv3 with authPriv security level\n# - Limit SNMP access to monitoring servers only\n# - Set appropriate community strings (not 'public' in production)\n# - Tune polling intervals (30s for critical, 5m for standard)\n# - Monitor both interface utilization and errors</code></pre>"),
        ],
        [
            ("SNMP RFC Collection", "https://datatracker.ietf.org/doc/html/rfc1157", "SNMPv1 (RFC 1157) and related specifications"),
            ("MIB Repository", "https://www.oidview.com/mibs/", "Searchable MIB database and OID reference"),
            ("LibreNMS SNMP Configuration", "https://docs.librenms.org/Support/SNMP-Configuration/", "SNMP setup guide for LibreNMS monitoring"),
        ]
    )

    # 37. QoS & Traffic Shaping
    build_page(
        "QoS & Traffic Shaping",
        "qos-traffic-shaping.html",
        "Prioritization, shaping, policing, DiffServ, CoS, and practical QoS configuration on routers and Linux.",
        "Networking",
        "fas fa-network-wired",
        [
            ("What is QoS?",
             "<p>Quality of Service (QoS) is a set of techniques to manage network resources by prioritizing certain types of traffic over others. QoS is essential for real-time applications like VoIP, video conferencing, and online gaming, where latency and jitter must be minimized.</p>"
             "<p>Three fundamental QoS actions:</p>"
             "<ul><li><strong>Classification</strong> -- identifying traffic by type (DSCP, CoS, ACLs)</li>"
             "<li><strong>Marking</strong> -- setting priority bits in packet headers</li>"
             "<li><strong>Policing/Shaping</strong> -- enforcing bandwidth limits</li></ul>"),
            ("DiffServ: DSCP & Trust Boundaries",
             "<p>DiffServ (Differentiated Services) is the primary QoS architecture for modern networks. DSCP (Differentiated Services Code Point) marks packets with 6-bit priority values:</p>"
             "<pre><code># Common DSCP values:\n# EF (46)   -- Expedited Forwarding: VoIP RTP (lowest latency)\n# AF41 (34) -- Assured Forwarding 4.1: Video conferencing\n# AF31 (26) -- Assured Forwarding 3.1: Streaming video\n# AF21 (18) -- Assured Forwarding 2.1: Business-critical data\n# AF11 (10) -- Assured Forwarding 1.1: Standard data\n# CS0 (0)   -- Best effort\n# CS6 (48)  -- Network control (routing protocols)\n# CS7 (56)  -- Network control (reserved)\n\n# Cisco trust boundary configuration\ninterface GigabitEthernet0/1\n description Access port\n ml qos trust device cisco-phone\n ml qos trust cos\n\n# Rewrite DSCP on untrusted ports\npolicy-map MARK-ACCESS\n class VOIP\n  set dscp ef\n class VIDEO\n  set dscp af41\n class BUSINESS\n  set dscp af21\n class DEFAULT\n  set dscp 0</code></pre>"),
            ("Shaping vs Policing",
             "<p>Traffic shaping buffers excess packets; policing drops them:</p>"
             "<pre><code># Policing (dropping excess packets)\npolicer LIMIT-10M {\n    if-exceeding {\n        bandwidth-percent 10\n        burst-packet-count 1500\n    }\n    then discard;\n}\n\n# Shaping (buffering excess packets)\ninterface GigabitEthernet0/0\n traffic-shape rate 10000000 1000000 1000000\n\n# Cisco MQC (Modular QoS CLI) shaping\npolicy-map SHAPE-50M\n class class-default\n  shape average 50000000\n\n# Linux tc shaping (HTB)\ntc qdisc add dev eth0 root handle 1: htb default 30\ntc class add dev eth0 parent 1: classid 1:1 htb rate 100mbit\ntc class add dev eth0 parent 1:1 classid 1:10 htb rate 10mbit ceil 20mbit</code></pre>"),
            ("QoS Configuration Examples",
             "<p>Real-world QoS configurations for different network roles:</p>"
             "<pre><code># ISP/Edge Router -- limited bandwidth WAN link\nclass-map match-any VOIP\n match ip dscp ef\nclass-map match-any VIDEO\n match ip dscp af41 af42 af43\n\npolicy-map WAN-EDGE\n class VOIP\n  priority percent 10    # Strict priority queue\n class VIDEO\n  bandwidth percent 30   # Guaranteed bandwidth\n class BUSINESS\n  bandwidth percent 30\n class class-default\n  fair-queue\n  random-detect          # WRED for TCP\n\ninterface Serial0/0/0\n bandwidth 50000        # 50 Mbps\n service-policy output WAN-EDGE\n\n# Linux tc with fq_codel (modern, no manual config needed)\ntc qdisc replace dev eth0 root fq_codel\n# Fair Queuing with Controlled Delay -- adaptive AQM</code></pre>"),
            ("Monitoring QoS & Troubleshooting",
             "<p>Verify QoS is working correctly:</p>"
             "<pre><code># Cisco\nshow policy-map interface Serial0/0/0\nshow policy-map interface Serial0/0/0 class VOIP\n# Look for: \"Queue depth 0\", \"Packets matched 0\" (if no traffic)\n\n# Linux tc\n# -s = statistics\ntc -s qdisc show dev eth0\ntc -s class show dev eth0\n\n# Check for drops (overlimit) in shaping classes\n# If drops > 0, consider increasing shapred rate or reducing offered load\n\n# End-to-end QoS verification\niperf3 -u -b 10M -l 1400 -t 30 -c 192.168.1.100\n# Check jitter and packet loss at receiver</code></pre>"),
        ],
        [
            ("Cisco QoS Configuration Guide", "https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/qos/configuration/15-sy/qos-15-sy-book.html", "Cisco IOS QoS configuration and best practices"),
            ("DiffServ RFC 2474", "https://datatracker.ietf.org/doc/html/rfc2474", "Definition of the Differentiated Services Field in IPv4/IPv6"),
            ("Linux tc (traffic control)", "https://lartc.org/", "Linux Advanced Routing & Traffic Control HOWTO"),
        ]
    )

    # 38. IPv6 Deployment
    build_page(
        "IPv6 Deployment Guide",
        "ipv6-deployment.html",
        "Address types, stateless autoconfig (SLAAC), DHCPv6, transition mechanisms, and dual-stack setup.",
        "Networking",
        "fas fa-network-wired",
        [
            ("IPv6 Addressing & Header",
             "<p>IPv6 uses 128-bit addresses (vs IPv4's 32-bit), providing 340 undecillion addresses. It was designed to replace IPv4 completely, but the transition has been gradual through dual-stack deployment.</p>"
             "<p>IPv6 address types:</p>"
             "<ul><li><strong>Global Unicast (2000::/3)</strong> -- globally routable, similar to IPv4 public addresses</li>"
             "<li><strong>Link-Local (fe80::/10)</strong> -- automatically assigned, used for local subnet communication</li>"
             "<li><strong>Unique Local (fc00::/7)</strong> -- private addresses, similar to RFC 1918</li>"
             "<li><strong>Multicast (ff00::/8)</strong> -- replaces IPv4 broadcast</li>"
             "<li><strong>Anycast</strong> -- multiple interfaces share one address, traffic goes to nearest</li></ul>"
             "<p>An IPv6 address example: <code>2001:db8:1234:abcd:5678:90ab:cdef:1234</code></p>"),
            ("Address Autoconfiguration: SLAAC vs DHCPv6",
             "<p>IPv6 supports both stateless and stateful address configuration:</p>"
             "<pre><code># SLAAC (Stateless Address Autoconfiguration)\n# Router Advertisement (RA) contains prefix + prefix length\n# Host generates its own interface ID (EUI-64 or privacy extension)\n# Flags in RA: A=auto, M=managed, O=other\n\n# Router configuration (Cisco)\ninterface GigabitEthernet0/0\n ipv6 address 2001:db8:1:10::1/64\n ipv6 enable\n ipv6 nd prefix 2001:db8:1:10::/64  # SLAAC advertisement\n ipv6 nd ra-interval 30\n\n# DHCPv6 (stateful) -- provides addresses and options\nipv6 dhcp pool MYPOOL\n prefix-delegation pool MYPOOL-PD\n dns-server 2001:4860:4860::8888\n domain-name example.com\n\ninterface GigabitEthernet0/0\n ipv6 dhcp server MYPOOL\n ipv6 nd other-config-flag  # M=0, O=1 (DHCP for options only)</code></pre>"),
            ("Dual-Stack & Transition Mechanisms",
             "<p>Dual-stack runs IPv4 and IPv6 simultaneously; various other transition techniques exist:</p>"
             "<pre><code># Dual-stack -- best practice: run both protocols\ninterface GigabitEthernet0/0\n ip address 192.168.1.1 255.255.255.0\n ipv6 address 2001:db8:1::1/64\n ipv6 enable\n\n# DNS64 + NAT64 -- connect IPv6-only clients to IPv4 servers\n# Uses DNS rewriting: AAAA queries synthesized from A records\n\n# Tunneling mechanisms (legacy):\n# 6to4 -- automatic tunnel using 2002::/16\n# Teredo -- UDP tunnel through NAT devices\n# ISATAP -- tunnel over IPv4 intranet\n\n# DS-Lite (Carrier-Grade NAT)\n# CPE builds IPv4-in-IPv6 tunnel to ISP's AFTR\n\n# Check dual-stack operation\nping google.com            # IPv4 test\nping -6 google.com         # IPv6 test\nnslookup -type=AAAA google.com\ncurl -6 https://ipv6.google.com</code></pre>"),
            ("IPv6 Security Considerations",
             "<p>IPv6 introduces new security challenges beyond IPv4:</p>"
             "<pre><code># ICMPv6 is essential (unlike ICMPv4 which can be blocked)\n# Neighbor Discovery Protocol (NDP) replaces ARP\n# Must allow: Neighbor Solicitation (135), Neighbor Advertisement (136)\n# Router Solicitation (133), Router Advertisement (134)\n\n# RA Guard -- prevent rogue router advertisements\nipv6 nd raguard\n\n# DHCPv6 Guard -- prevent rogue DHCPv6 servers\nipv6 dhcp guard\n\n# Source address validation (First Hop Security)\nipv6 source-guard\n\n# Privacy Extensions (temporary addresses)\n# Windows: Enabled by default\n# Linux: /proc/sys/net/ipv6/conf/all/use_tempaddr = 2\n# macOS: Enabled by default\n\n# Firewall example (nftables)\ntable ip6 filter {\n    chain input {\n        type filter hook input priority 0\n        icmpv6 type { nd-neighbor-solicit, nd-neighbor-advert, nd-router-solicit, nd-router-advert } accept\n        ct state established,related accept\n    }\n}</code></pre>"),
            ("Deployment Planning & Testing",
             "<p>Plan and test your IPv6 deployment:</p>"
             "<pre><code># IPv6 readiness checklist:\n# [ ] ISP provides IPv6 prefix (check with your provider)\n# [ ] Customer Premise Equipment (CPE) supports IPv6\n# [ ] Core routers/switches have IPv6 enabled\n# [ ] DNS infrastructure serves AAAA records\n# [ ] Firewall rules include IPv6 (ip6tables or nftables ip6 family)\n# [ ] Applications tested on IPv6\n# [ ] Monitoring systems track IPv6 metrics\n\n# Test tools:\nip -6 addr show\nip -6 route show\nip -6 neigh show\n\n# Online IPv6 tests:\n# https://test-ipv6.com/\n# https://ipv6-test.com/\n\n# Google IPv6 statistics\n# https://www.google.com/intl/en/ipv6/statistics.html</code></pre>"),
        ],
        [
            ("IPv6 Fundamentals (RFC 8200)", "https://datatracker.ietf.org/doc/html/rfc8200", "Internet Protocol Version 6 specification"),
            ("Google IPv6 Statistics", "https://www.google.com/intl/en/ipv6/statistics.html", "Global IPv6 adoption statistics"),
            ("NIST IPv6 Security Guide", "https://csrc.nist.gov/publications/detail/sp/800-119/final", "US government IPv6 security recommendations"),
        ]
    )

    # 39. Software-Defined Networking
    build_page(
        "Software-Defined Networking",
        "sdn-overview.html",
        "SDN architecture, OpenFlow, network virtualization, controllers, and practical SDN implementations.",
        "Networking",
        "fas fa-network-wired",
        [
            ("What is SDN?",
             "<p>Software-Defined Networking (SDN) decouples the network control plane from the data plane, enabling centralized network management and programmatic control. In traditional networking, each device makes independent forwarding decisions. In SDN, a central controller computes paths and installs flow entries into switches.</p>"
             "<p>Key architecture layers:</p>"
             "<ul><li><strong>Infrastructure Layer</strong> -- physical/virtual switches and routers (data plane)</li>"
             "<li><strong>Control Layer</strong> -- SDN controller that manages forwarding state</li>"
             "<li><strong>Application Layer</strong> -- network services (firewalling, load balancing, visibility)</li></ul>"
             "<p>The controller communicates with switches via Southbound APIs (primarily OpenFlow) and with applications via Northbound APIs (REST, gRPC).</p>"),
            ("OpenFlow Protocol",
             "<p>OpenFlow is the first standard SDN protocol. It allows the controller to install flow entries in switches:</p>"
             "<pre><code># OpenFlow flow entry components:\n# - Match fields: ingress port, MAC src/dst, IP src/dst, TCP/UDP ports, VLAN, MPLS\n# - Priority: higher priority matches first\n# - Instructions: actions or goto-table\n# - Actions: output, drop, set-field, push-vlan, group\n# - Counters: packets, bytes, duration\n\n# Example flow entry (OVS commands):\n# Match all HTTP traffic from 10.0.0.0/8, send to controller\novs-ofctl add-flow br0 \\\n    \"priority=100,tcp,nw_src=10.0.0.0/8,tp_dst=80,actions=controller\"\n\n# Match all ARP, flood via all ports\novs-ofctl add-flow br0 \\\n    \"priority=10,arp,actions=FLOOD\"\n\n# Match IPv4, apply normal L2/L3 switching\novs-ofctl add-flow br0 \\\n    \"priority=1,ip,actions=NORMAL\"</code></pre>"),
            ("SDN Controllers & Platforms",
             "<p>Popular SDN controllers and platforms:</p>"
             "<pre><code># OpenDaylight -- Linux Foundation, Java, modular\n# Features: OpenFlow, NETCONF, OVSDB, RESTCONF\n\n# ONOS (Open Network Operating System) -- Java, carrier-grade\n# Features: Intent-based networking, distributed core\n\n# Floodlight (OpenFlow 1.3) -- Java, OpenFlow-only\n\n# Ryu -- Python-based, lightweight\npip install ryu\nryu-manager ~/simple_switch.py\n\n# POX -- Python, educational/research\n\n# OVS (Open vSwitch) -- production virtual switch\nsudo apt install openvswitch-switch\nsudo ovs-vsctl add-br br0\nsudo ovs-vsctl add-port br0 eth0\nsudo ovs-vsctl set-controller br0 tcp:192.168.1.100:6633</code></pre>"),
            ("Network Virtualization & Overlays",
             "<p>SDN enables network virtualization through overlay tunnels:</p>"
             "<pre><code># VXLAN (Virtual Extensible LAN)\n# Encapsulates L2 frames in UDP (port 4789)\n# 24-bit VNI (VXLAN Network Identifier) -- 16 million segments\n\n# OVS VXLAN configuration\nsudo ovs-vsctl add-br vxlan-br\nsudo ovs-vsctl add-port vxlan-br vxlan1 -- set interface vxlan1 \\\n    type=vxlan options:remote_ip=192.168.2.100 options:key=5000\n\n# VTEP (VXLAN Tunnel Endpoint) -- switches or hosts\n\n# Geneve -- modern overlay protocol (Linux kernel 3.18+)\n# Similar to VXLAN but with variable-length options\n\n# Network Service Mesh (NSM) -- cloud-native SDN for Kubernetes\n\n# EVPN (Ethernet VPN) -- BGP-based control plane for VXLAN\n# Standardized in RFC 7432</code></pre>"),
            ("Practical SDN: Use Cases & Getting Started",
             "<p>Real-world SDN applications and lab setup:</p>"
             "<pre><code># Mininet -- network emulator for SDN testing\nsudo apt install mininet\nsudo mn --topo tree,3 --controller=remote,ip=127.0.0.1\n\n# Hands-on SDN scenario:\n# 1. Start Mininet with remote controller\n# 2. Run Ryu controller with simple_switch\n# 3. Verify connectivity between hosts\n\n# SDN use cases:\n# - Traffic engineering: dynamic path computation based on utilization\n# - Service chaining: steer traffic through firewall > LB > WAN optimizer\n# - Network slicing: dedicated virtual networks for tenants\n# - Intent-based networking: declare what you want, controller figures out how\n# - Cloud networking: OpenStack Neutron, OpenShift SDN, Kubernetes CNI</code></pre>"),
        ],
        [
            ("Open Networking Foundation", "https://opennetworking.org/sdn-resources/", "Industry SDN standards and resources"),
            ("OpenFlow Specification", "https://opennetworking.org/openflow/", "OpenFlow switch specification documents"),
            ("Mininet Project", "http://mininet.org/", "Network emulator for SDN prototyping and education"),
        ]
    )

    # 40. MPLS Networking
    build_page(
        "MPLS Networking Basics",
        "mpls-basics.html",
        "Labels, LSPs, LDP, RSVP-TE, MPLS VPNs, and traffic engineering fundamentals.",
        "Networking",
        "fas fa-network-wired",
        [
            ("What is MPLS?",
             "<p>Multiprotocol Label Switching (MPLS) is a data-carrying technique that directs data from one network node to the next based on short path labels rather than long network addresses. It sits between Layer 2 (data link) and Layer 3 (network) — often called Layer 2.5. MPLS is widely used by ISPs and large enterprises for VPNs, traffic engineering, and QoS.</p>"
             "<p>Key concepts:</p>"
             "<ul><li><strong>Label</strong> -- 20-bit identifier (1,048,576 possible values), local significance per hop</li>"
             "<li><strong>LSP (Label Switched Path)</strong> -- the path packets traverse through the MPLS network</li>"
             "<li><strong>LER (Label Edge Router)</strong> -- ingress/egress router that pushes/removes labels</li>"
             "<li><strong>LSR (Label Switch Router)</strong> -- core router that swaps labels</li></ul>"),
            ("Label Distribution: LDP vs RSVP-TE",
             "<p>MPLS labels can be distributed using different protocols:</p>"
             "<pre><code># LDP (Label Distribution Protocol) -- basic, hop-by-hop\n# Automatically distributes labels for IGP routes\n# Each LSR assigns label for each prefix in routing table\n\n# Cisco LDP configuration\nmpls label protocol ldp\ninterface GigabitEthernet0/0\n mpls ip\n!\nrouter ospf 1\n mpls ldp autoconfig\n\n# RSVP-TE (Resource Reservation Protocol - Traffic Engineering)\n# Explicit path setup, bandwidth reservation\n# Used for traffic engineering MPLS-TE\n\n# Cisco RSVP-TE configuration\nip explicit-path name PATH-TO-CORE\n next-address 10.0.1.1\n next-address 10.0.2.1\n!\ninterface Tunnel100\n ip unnumbered Loopback0\n tunnel mode mpls traffic-eng\n tunnel destination 192.168.255.1\n tunnel mpls traffic-eng path-option 1 explicit name PATH-TO-CORE\n!</code></pre>"),
            ("MPLS VPNs: Layer 3 VPN & Layer 2 VPN",
             "<p>MPLS is widely used to provide VPN services:</p>"
             "<pre><code># Layer 3 MPLS VPN (RFC 4364)\n# Provider Edge (PE) routers contain separate VRF per customer\n# Customer Edge (CE) router peers with PE\n\n# VRF configuration (Cisco)\nip vrf CUSTOMER-A\n rd 64500:100\n route-target export 64500:100\n route-target import 64500:100\n!\ninterface GigabitEthernet0/1\n ip vrf forwarding CUSTOMER-A\n ip address 192.168.10.1 255.255.255.252\n!\nrouter bgp 64500\n address-family ipv4 vrf CUSTOMER-A\n  neighbor 192.168.10.2 remote-as 65001\n  neighbor 192.168.10.2 activate\n\n# Layer 2 VPN (VPWS -- Virtual Private Wire Service, VPLS)\n# Point-to-point (VPWS) or multipoint (VPLS) L2 connectivity\n# Pseudowire: emulates a wire between two sites\n\n# Pseudowire configuration\ninterface Pseudowire1\n encapsulation mpls\n neighbor 192.168.255.1 100</code></pre>"),
            ("MPLS Traffic Engineering (MPLS-TE)",
             "<p>MPLS-TE provides explicit path control and bandwidth management:</p>"
             "<pre><code># Traffic engineering database (TED) via OSPF-TE or IS-IS TE\n# Links advertise available bandwidth, TE metric, admin groups\n\n# Constraint-based path computation (CSPF)\n# Finds path meeting constraints (bandwidth, latency, affinity)\n\n# Fast Reroute (FRR) -- sub-50ms protection switching\n# Protects link or node failures via pre-computed backup paths\n\n# DiffServ-Aware TE (DS-TE)\n# Different bandwidth pools for different traffic classes\n\n# View MPLS-TE tunnels\nshow mpls traffic-eng tunnels brief\nshow mpls traffic-eng topology\n\n# LSP ping and traceroute\nping mpls ipv4 192.168.255.1/32\ntraceroute mpls ipv4 192.168.255.1/32</code></pre>"),
            ("Segment Routing (SR-MPLS)",
             "<p>Segment Routing simplifies MPLS by using IGP-based labels without LDP:</p>"
             "<pre><code># SR-MPLS benefits:\n# - No LDP or RSVP-TE needed (uses IGP extensions)\n# - Source routing: ingress node encodes path as label stack\n# - TI-LFA (Topology-Independent LFA) for sub-50ms FRR\n\n# Cisco SR-MPLS (IS-IS) configuration\nrouter isis 1\n net 49.0001.1921.6800.1001.00\n is-type level-2-only\n metric-style wide\n segment-routing mpls\n!\ninterface Loopback0\n ip address 192.168.255.1 255.255.255.255\n ip router isis 1\n isis passive\n isis prefix-sid index 101\n!\ninterface GigabitEthernet0/0\n ip address 10.0.1.1 255.255.255.252\n ip router isis 1\n isis circuit-type level-2-only\n isis adjacency-sid label 16001</code></pre>"),
        ],
        [
            ("MPLS Fundamentals (Cisco)", "https://www.cisco.com/c/en/us/support/docs/multiprotocol-label-switching-mpls/mpls/4649-mpls-fa-4649.html", "Cisco MPLS technology overview"),
            ("MPLS RFCs", "https://datatracker.ietf.org/doc/html/rfc3031", "MPLS Architecture (RFC 3031) specification"),
            ("Segment Routing Documentation", "https://www.segment-routing.net/", "Segment Routing tutorials, tools, and case studies"),
        ]
    )

    # 41. Network Automation
    build_page(
        "Network Automation with Ansible & Python",
        "network-automation.html",
        "Automate network configuration, Netmiko, NAPALM, Ansible network modules, and CI/CD for networks.",
        "Networking",
        "fas fa-network-wired",
        [
            ("Why Network Automation?",
             "<p>Manual network configuration is slow, error-prone, and difficult to audit at scale. Network automation replaces CLI-based, human-intensive workflows with programmatic, version-controlled, and repeatable processes. Benefits include reduced configuration drift, faster deployments, consistent multi-vendor management, and self-documenting infrastructure.</p>"
             "<p>Key tools in the network automation ecosystem:</p>"
             "<ul><li><strong>Netmiko</strong> -- Python library for SSH-based network device interaction</li>"
             "<li><strong>NAPALM</strong> -- multi-vendor abstraction layer with consistent API</li>"
             "<li><strong>Ansible</strong> -- agentless automation with declarative YAML playbooks</li>"
             "<li><strong>Nornir</strong> -- Python-based task automation framework</li>"
             "<li><strong>pyATS</strong> -- Cisco test automation system</li></ul>"),
            ("Netmiko: SSH Automation in Python",
             "<p>Netmiko simplifies SSH connections to network devices:</p>"
             "<pre><code>from netmiko import ConnectHandler\n\n# Define device\ncisco_device = {\n    'device_type': 'cisco_ios',\n    'host': '192.168.1.1',\n    'username': 'admin',\n    'password': 'password',\n    'secret': 'enable_password',\n}\n\n# Connect and run commands\nconnection = ConnectHandler(**cisco_device)\nconnection.enable()\n\n# Send one command\noutput = connection.send_command('show ip interface brief')\nprint(output)\n\n# Send configuration\nconfig_commands = [\n    'interface GigabitEthernet0/1',\n    'description LAN Access Port',\n    'switchport mode access',\n    'switchport access vlan 10',\n    'no shutdown',\n]\noutput = connection.send_config_set(config_commands)\n\n# Save config\nconnection.save_config()\nconnection.disconnect()</code></pre>"),
            ("NAPALM: Multi-Vendor Abstraction",
             "<p>NAPALM provides a consistent API across different network vendors:</p>"
             "<pre><code>from napalm import get_network_driver\n\n# Connect to device\ndriver = get_network_driver('ios')\ndevice = driver(\n    hostname='192.168.1.1',\n    username='admin',\n    password='password',\n    optional_args={'secret': 'enable'},\n)\ndevice.open()\n\n# Consistent methods across vendors\nfacts = device.get_facts()\ninterfaces = device.get_interfaces()\narp_table = device.get_arp_table()\nntp_peers = device.get_ntp_peers()\n\n# Deploy configuration\nconfig = \"\"\"\ninterface GigabitEthernet0/1\n description Automated port\n switchport mode access\n switchport access vlan 20\n\"\"\"\ndevice.load_merge_candidate(config=config)\n\n# Compare and commit\nprint(device.compare_config())\ndevice.commit_config()\ndevice.close()</code></pre>"),
            ("Ansible Network Automation",
             "<p>Ansible manages network devices using agentless YAML playbooks:</p>"
             "<pre><code># inventory/hosts.yml\nall:\n  hosts:\n    core-01:\n      ansible_host: 192.168.1.1\n      ansible_network_os: cisco.ios.ios\n    core-02:\n      ansible_host: 192.168.1.2\n      ansible_network_os: cisco.ios.ios\n\n# playbooks/configure-vlans.yml\n---\n- name: Configure VLANs on Core Switches\n  hosts: core\n  gather_facts: false\n  tasks:\n    - name: Ensure VLAN 10 exists\n      cisco.ios.ios_vlan:\n        vlan_id: 10\n        name: USERS\n        state: present\n\n    - name: Apply interface config\n      cisco.ios.ios_interfaces:\n        config:\n          - name: GigabitEthernet0/1\n            description: \"User Access Port\"\n            mode: access\n            enabled: true</code></pre>"),
            ("CI/CD for Network & Validation Tools",
             "<p>Integrate network automation with GitOps pipelines:</p>"
             "<pre><code># GitHub Actions example\n# .github/workflows/network-deploy.yml\nname: Deploy Network Config\non:\n  push:\n    branches: [main]\n    paths:\n      - 'network-configs/**'\n\njobs:\n  deploy:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v4\n      - name: Validate and deploy\n        run: |\n          ansible-playbook playbooks/validate.yml\n          ansible-playbook playbooks/deploy.yml --check\n          ansible-playbook playbooks/deploy.yml\n\n# Network validation tools:\n# Batfish -- static config analysis (find ACL errors, routing issues)\n# pytest + pyATS -- automated test suites for network states\n# Ansible --assert -- ensure post-deployment state\n\n# Backup automation (run daily):\n# ansible-playbook playbooks/backup-configs.yml\n# Stores configs in version control</code></pre>"),
        ],
        [
            ("Netmiko Documentation", "https://ktbyers.github.io/netmiko/", "SSH automation library for network devices"),
            ("NAPALM Documentation", "https://napalm.readthedocs.io/", "Multi-vendor network automation library"),
            ("Ansible Network Automation", "https://docs.ansible.com/ansible/latest/network/getting_started/index.html", "Official Ansible network automation guide"),
        ]
    )


    print("\n=== Generated 41 tutorial files (Part 1) ===")


if __name__ == "__main__":
    os.makedirs(TUTS, exist_ok=True)
    generate_part1()
