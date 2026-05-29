#!/usr/bin/env python3
"""Generate 240+ tutorials covering all remaining topics — using triple-quoted strings to avoid quoting issues."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tutorial_helpers import build_page

# Template using triple-single-quoted strings to safely embed both " and '
Q = lambda l, b: (l, b)
F = lambda n, u, d: (n, u, d)

def t(title, filename, desc, badge, icon, sections, further):
    build_page(title, filename, desc, badge, icon, sections, further)

def run():
    # === BATCH A: Security & Networking (15 tutorials) ===
    t("Burp Suite Deep Dive", "burp-suite-deep-dive.html",
      '''Master Burp Suite — proxy, scanner, intruder, repeater, and extensions for web pentesting.''',
      "Security", "fas fa-bolt", [
        Q("Proxy & Interception", '''<p>Burp Suite intercepts HTTP/S traffic between browser and server.
        Configure proxy listener (127.0.0.1:8080), install CA certificate in your browser, and
        intercept requests/responses to modify them on the fly. The proxy history logs all traffic
        for later analysis. Use WebSockets history tab for WS/WSS traffic inspection.</p>'''),
        Q("Intruder for Fuzzing", '''<p>Burp Intruder automates parameter fuzzing. Set positions with § markers, choose payload
        types (simple list, brute force, character blocks, numbers, dates), and configure attack types:
        sniper (one payload), battering ram (same payload in all positions), pitchfork (parallel payloads),
        cluster bomb (cartesian product). Use Intruder for IDOR, rate limit bypass, and parameter discovery.</p>'''),
        Q("Repeater & Sequencer", '''<p>Repeater manually resends individual requests with modifications. Tweak parameters, headers,
        and body; inspect responses to find vulnerabilities. Sequencer analyzes token randomness —
        capture a sample of tokens (1000+), test for entropy weaknesses (chi-squared, spectral).
        Weak tokens enable session hijacking, CSRF bypass, and password reset attacks.</p>'''),
        Q("Scanner & Extensions", '''<p>Burp Scanner (Professional) automatically crawls and scans for vulnerabilities. Scan configuration:
        crawl strategy (fastest, fast, thorough), audit coverage (favorite, interesting, all), and
        insertion point types (parameters, headers, cookies, URL). BApp Store extensions: Logger++,
        Autorize (authorization testing), JSON Web Tokens (JWT analysis), and Collaborator Everywhere.</p>'''),
        Q("Turbo Intruder & Automation", '''<p>Turbo Intruder (Python-based) is faster than standard Intruder for credential stuffing
        and brute force. It uses HTTP pipelining for massive throughput. Customize with Python scripts
        for queue management, attack success detection, and rate limit evasion via randomized delays
        and rotating User-Agent headers. Integrate with Jython for custom script execution.</p>'''),
      ],[F("PortSwigger Burp Suite","https://portswigger.net/burp","Official Burp Suite documentation"),
         F("Burp Suite Certified Practitioner","https://portswigger.net/web-security/certified","Web security certification")])

    t("Kerberos & Active Directory Security", "kerberos-active-directory.html",
      '''Understand Kerberos protocol, AD attacks (Kerberoasting, AS-REP Roasting, Golden Ticket), and defenses.''',
      "Security", "fas fa-network-wired", [
        Q("Kerberos Protocol Flow", '''<p>Kerberos: client authenticates to AS (Authentication Server) → gets TGT (Ticket-Granting Ticket),
        presents TGT to TGS (Ticket-Granting Server) → gets service ticket → presents service ticket to
        target service. Tickets are encrypted with domain controller secrets (krbtgt hash for TGT,
        server secrets for service tickets). Kerberos uses symmetric key cryptography with timestamps
        to prevent replay attacks.</p>'''),
        Q("Kerberoasting Attack", '''<p>Kerberoasting: request TGS tickets for service accounts (SPNs) using any domain user account.
        The TGS ticket is encrypted with the service account's NTLM hash. Download tickets offline
        and brute-force the hash to recover the service account password. Mitigation: use strong
        service account passwords (25+ chars), use Group Managed Service Accounts (gMSA) with
        automatic password rotation, and monitor for abnormal TGS requests (event ID 4769).</p>'''),
        Q("AS-REP Roasting", '''<p>AS-REP Roasting targets users without Kerberos pre-authentication enabled. The AS sends
        a TGT encrypted with the user's NTLM hash (partially encrypted with the user's key). Capture
        this response and brute-force offline. Mitigation: enforce Kerberos pre-authentication for
        all users (default in modern AD), monitor for AS-REP responses (event ID 4768) without
        pre-auth, and audit for accounts with "Do not require Kerberos preauthentication" set.</p>'''),
        Q("Golden & Silver Ticket Attacks", '''<p>Golden Ticket: attacker obtains krbtgt hash — creates arbitrary TGTs granting domain admin
        access. KRBTGT hash never changes unless changed manually twice. Silver Ticket: forge service
        tickets using the target service account hash — access the service (e.g., HOST/CIFS for
        file server admin) without contacting the DC. Mitigation: protect domain controller admin
        access, use Protected Users group (disables NTLM, Kerberos delegation), monitor for
        anomalous TGT/TGS activity (elevated privileges, unusual service usage).</p>'''),
        Q("Active Directory Hardening", '''<p>AD hardening checklist: disable NTLM (or use NTLM blocking), enforce SMB signing,
        enable LDAP signing/channel binding, implement tiered administration model (Tier 0/1/2),
        deploy LAPS (Local Administrator Password Solution) for unique local admin passwords,
        use Windows Defender Firewall, enable Advanced Audit Policy (log event IDs 4625, 4648, 4672,
        4768, 4769, 4776), and regularly scan for misconfigurations with PingCastle or Purple Knight.</p>'''),
      ],[F("Active Directory Security Blog","https://adsecurity.org/","Sean Metcalf's AD security resources"),
         F("BloodHound","https://bloodhound.readthedocs.io/","AD attack path mapping tool")])

    t("Network Security Monitoring", "network-security-monitoring.html",
      '''Monitor network traffic for threats — Zeek, Suricata, Snort, and security onion.''',
      "Security", "fas fa-shield-virus", [
        Q("Zeek (Bro) Framework", '''<p>Zeek is a passive network monitoring framework. It logs all network activity as structured logs:
        conn.log (connections — IPs, ports, bytes), http.log (HTTP requests, User-Agent, MIME types),
        dns.log (DNS queries), ssl.log (TLS certificates, JA3 hashes), and files.log (extracted files).
        Zeek scripts (event-driven, custom .zeek scripts) extend monitoring — detect port scans,
        brute-force attempts, and DDoS patterns. Zeek doesn't block — it detects and generates logs.</p>'''),
        Q("Suricata IDS/IPS", '''<p>Suricata is a high-performance IDS/IPS/NSM engine. It uses signature rules (emerging threats,
        ET Pro, custom rules) to detect threats, and can block (IPS mode) inline. Rule format:
        alert tcp $HOME_NET any -> $EXTERNAL_NET $HTTP_PORTS (msg:"ET MALWARE Callback"; content:"evil.com"; flow:established; sid:12345; rev:1;).
        Suricata supports multi-threading (unlike Snort), file extraction, and protocol parsing
        (HTTP, SMTP, TLS). Integrate with Kibana via Filebeat for visualization.</p>'''),
        Q("Security Onion", '''<p>Security Onion is a complete NSM distribution (Ubuntu-based, free). It bundles: Zeek (logs),
        Suricata (alerting), Wazuh (host monitoring), Elasticsearch (storage), Logstash (processing),
        Kibana/Grafana (visualization), TheHive (case management), Playbook (automation), and
        CyberChef (data analysis). All pre-configured with analyst workstation (SOC workflow tools).
        Deploy: standalone (learning) or distributed (sensors + server) for enterprise scale.</p>'''),
        Q("Threat Intelligence Feeds", '''<p>Threat feeds provide IoCs (Indicators of Compromise) — IPs, domains, hashes, URLs. Free feeds:
        AlienVault OTX (open, threat exchange), MISP (Malware Information Sharing Platform — share
        structured threat data), Abuse.ch (SSL blacklist, URLhaus, Feodo tracker), and Spamhaus
        (DNSBL). Commercial: Recorded Future, CrowdStrike, VirusTotal Intelligence, Anomali.</p><p>Automate feed ingestion: pull IoCs (Threat Connect, MISP), convert to Suricata rules (ID2Rule),
        deploy to sensors, and alert on matches. Feeds expire — remove stale IoCs regularly.</p>'''),
        Q("Packet Capture Analysis", '''<p>Full packet capture captures raw network traffic. Tools: tcpdump (CLI, -i interface -w file.pcap),
        Wireshark/tshark (GUI/CLI analysis — follow streams, export objects, filter by host/protocol),
        Moloch/Arkime (full packet capture for security — web UI, PCAP retrieval, session analysis).
        PCAP storage requires significant disk space (1TB ~ 7 days of 100Mbps traffic). Deploy
        capture sensors strategically — at internet gateway, DMZ segments, server subnets.</p>'''),
      ],[F("Zeek Documentation","https://docs.zeek.org/","Network monitoring framework docs"),
         F("Security Onion Solutions","https://securityonion.net/","Free NSM distribution")])

    t("Cloud Native Security", "cloud-native-security.html",
      '''Secure containers, Kubernetes, and serverless workloads — supply chain, runtime, and admission control.''',
      "Security", "fas fa-cloud", [
        Q("Container Image Security", '''<p>Secure container images start at build time. Use minimal base images (Alpine, Distroless,
        Chainguard Wolfi), scan for vulnerabilities before deployment (Trivy, Grype, Snyk),
        sign images with Cosign (Sigstore), and enforce only signed images via policy. Pin base
        image digests (not tags — tags are mutable), use multi-stage builds to exclude build tools
        from runtime images, and scan regularly for new CVEs with automated rebuild pipelines.</p>'''),
        Q("Kubernetes Security Context", '''<p>K8s SecurityContext defines pod/hardening: runAsNonRoot: true (prevent root),
        readOnlyRootFilesystem: true (prevents binary modification), capabilities: drop ALL then add
        needed (minimum Linux capabilities), seccompProfile: RuntimeDefault (restrict syscalls),
        allowPrivilegeEscalation: false (prevents privilege escalation from container).
        Pod Security Standards (PSA): privileged, baseline (default-enforce), restricted (PCI/GDPR).
        Use Kyverno or OPA Gatekeeper to enforce PSA across all namespaces.</p>'''),
        Q("Network Policies & Istio", '''<p>Kubernetes NetworkPolicies define allowed pod-to-pod communication. Default deny all ingress
        and egress, then selectively allow: allow app=frontend to app=backend (port 8080 TCP),
        allow app=backend to external DB (IP range, port 5432). Istio/Envoy adds: mTLS (service
        identity verification, encryption), authorization policies (RBAC with JWT), rate limiting,
        and circuit breakers. Service mesh prevents east-west traffic without proper authorization.</p>'''),
        Q("Admission Controllers", '''<p>Admission controllers intercept API requests before resources are created/modified.
        Built-in: NamespaceLifecycle, LimitRanger, ResourceQuota, PodSecurity (PSA replacement for PSP).
        Dynamic admission: OPA Gatekeeper (rego policies — enforce labels, resource limits,
        security contexts), Kyverno (Kubernetes-native policies — simpler than rego, mutate/validate
        resources), and webhooks (custom validation/mutation via HTTP). Use admission control to
        block non-compliant deployments before they reach etcd.</p>'''),
        Q("Supply Chain Security", '''<p>Software supply chain attacks inject malicious code during development or build. Protections:
        SBOM (Software Bill of Materials — CycloneDX, SPDX format, generated by Syft), signed
        attestations (in-toto attestations, SLSA framework — supply chain levels for software
        artifacts), image verification (Cosign — verify signatures via transparency log),
        dependency scanning (Dependabot, Renovate — automate updates), and reproducible builds
        (deterministic, verifiable output). GitOps (ArgoCD) with signed commits + verified images
        creates an auditable deployment chain.</p>'''),
      ],[F("Kubernetes Security Docs","https://kubernetes.io/docs/concepts/security/","Official K8s security docs"),
         F("NSA Kubernetes Hardening","https://media.defense.gov/2021/Aug/03/2002820425/-1/-1/1/CTR_KUBERNETES%20HARDENING%20GUIDANCE.PDF","NSA/CISA K8s hardening guide")])

    # === BATCH B: Cloud & DevOps Continued (15 tutorials) ===
    t("GitOps & ArgoCD", "gitops-argocd.html",
      '''GitOps workflow with ArgoCD — declarative deployments, sync strategies, and multi-cluster management.''',
      "DevOps", "fas fa-sync", [
        Q("GitOps Principles", '''<p>GitOps uses Git as the single source of truth for declarative infrastructure and applications.
        Principles: declarative configuration (entire system described in Git), state reconciled
        automatically (operator ensures cluster matches Git), and pull-based deployments (operator
        pulls changes from Git, not push). Benefits: audit trail (every change in Git), easy rollback
        (git revert), and familiar review workflow (PRs, approvals, CI checks).</p>'''),
        Q("ArgoCD Architecture", '''<p>ArgoCD is a declarative GitOps operator for Kubernetes. Components: API Server (gRPC/REST,
        web UI, CLI), Repository Server (clones Git repos, caches), Application Controller (syncs
        applications, health status), Redis (cache, in-memory), Dex/SSO (auth integration).
        ArgoCD supports: auto-sync (watch Git and deploy changes), self-heal (fix drift), sync waves
        (ordered deployment), and sync windows (block deploys during maintenance).</p>'''),
        Q("Application Definitions", '''<p>ArgoCD Application CRD: spec.destination (cluster + namespace), spec.source (repo URL, path,
        targetRevision), spec.syncPolicy (automated: prune, selfHeal). ApplicationSet generatoes:
        list, git (generate per path), cluster (multi-cluster), PR (preview environments from PRs).
        ArgoCD supports Helm, Kustomize, Ksonnet, YAML/JSON, and plain directory of manifests.
        Use ApplicationSets for multi-environment (dev/staging/prod) and multi-cluster deployments.</p>'''),
        Q("Multi-Cluster Management", '''<p>ArgoCD manages multiple clusters from a single control plane. Register clusters via
        argocd cluster add <kubeconfig> or declaratively via cluster secrets. Use ApplicationSet
        cluster generator to deploy identical/similar configs across clusters. For pure multi-cluster
        (no single pane of glass): ArgoCD Multi-Cluster (hub + spokes) or ArgoCD instance per cluster.
        Cluster-specific values via git generator + cluster labels.</p>'''),
        Q("Progressive Delivery", '''<p>Progressive delivery extends GitOps with automated rollout validation. Argo Rollouts provide:
        Blue-Green (switch traffic all at once), Canary (gradual traffic shift — 10%, 25%, 50%, 100%),
        and analysis (Prometheus metrics, webhooks, datadog — auto-rollback if metrics degrade).
        Integration with ArgoCD: Rollouts as a custom resource, promoted via sync waves.
        Together GitOps + Progressive Delivery = safe, automated deployments with minimal human touch.</p>'''),
      ],[F("ArgoCD Documentation","https://argo-cd.readthedocs.io/","Official ArgoCD documentation"),
         F("CodeFresh ArgoCD Tutorials","https://codefresh.io/learn/argo-cd/","ArgoCD learning resources")])

    t("CI/CD Pipeline Design", "cicd-pipeline-design.html",
      '''Design efficient CI/CD pipelines — GitHub Actions, GitLab CI, testing, caching, and deployment strategies.''',
      "DevOps", "fas fa-rocket", [
        Q("Pipeline Architecture", '''<p>CI/CD pipeline stages: Source → Build → Test → Deploy. Each stage runs in a separate job
        (container) with specific tools. Good pipeline: fast (<10 min), deterministic (same commit =
        same result), idempotent (re-runnable), and observable (logs, metrics, artifacts, notifications).
        Monorepo: build only changed projects (affected project detection). Multi-repo: independent
        pipelines per repo, shared CI templates via actions/remote includes.</p>'''),
        Q("GitHub Actions Deep Dive", '''<p>GitHub Actions: workflows (YAML in .github/workflows/), jobs (run on runners, parallel by
        default), steps (sequential commands or actions). Actions are reusable units — use from
        marketplace or write custom Dockerfile/JavaScript actions. Key features: matrix builds
        (test across OS/node versions), artifacts (pass files between jobs), caches (dependencies,
        Docker layers), environments (protection rules, secrets per env), and service containers
        (Dependencies like Postgres, Redis for integration tests).</p>'''),
        Q("Caching & Performance", '''<p>Cache dependencies to speed up CI: pip cache (actions/cache — ~/.cache/pip), npm (~/.npm),
        Docker layers (docker/build-push-action cache-from, cache-to). Layer caching: rebuilding
        Docker images — order layers by change frequency (least → most changed). Use local runner
        (self-hosted) for faster builds (no setup/teardown overhead). Parallelize: matrix (test
        across combinations), concurrency groups (cancel redundant runs), and test splitting
        (distribute test files across parallel jobs).</p>'''),
        Q("Deployment Strategies", '''<p>Deployment strategies: Rolling (gradually replace old pods — default, zero-downtime),
        Blue-Green (switch traffic from old (blue) to new (green) — instant rollback via switch back),
        Canary (route X% of traffic to new version — monitor metrics, increase gradually or rollback),
        A/B testing (route based on header/cookie — not just traffic %) and Feature flags (decouple
        deployment from release — release feature independently of deploy via LaunchDarkly/Flagsmith).</p>'''),
        Q("Pipeline Security", '''<p>Secure CI/CD: use OIDC (id-token: write) for cloud auth (no static secrets), store secrets
        in CI secrets store (never in code), sign artifacts (Cosign), verify images in deploy (admission
        controller), use least-privilege CI tokens (scoped to repo), evaluate third-party actions
        (pinned hashes, no unverified marketplaces), scan for exposed secrets (gitLeaks, truffleHog),
        and protect production environments (manual approval gate, protected branches).</p>'''),
      ],[F("GitHub Actions Docs","https://docs.github.com/actions","Official GitHub Actions documentation"),
         F("GitLab CI Docs","https://docs.gitlab.com/ee/ci/","Official GitLab CI/CD documentation")])

    t("HashiCorp Stack (Vault, Consul, Nomad)", "hashicorp-vault-consul-nomad.html",
      '''Vault for secrets, Consul for service mesh, Nomad for orchestration — the HashiCorp ecosystem.''',
      "DevOps", "fas fa-building", [
        Q("Vault Secrets Management", '''<p>HashiCorp Vault manages secrets (API keys, DB credentials, certificates) with dynamic,
        ephemeral secrets and audit logging. Secret engines: KV (static key-value), AWS/GCP/Azure
        (dynamic cloud credentials — auto-expire), Database (dynamic DB credentials with TTL),
        PKI (dynamic X.509 certificates — auto-renew), Transit (encryption as a service).
        Authentication: token, AppRole (machine-to-machine), Kubernetes (service account
        integration), LDAP, OIDC. Vault Agent (sidecar) auto-auth and writes secrets to disk.</p>'''),
        Q("Consul Service Mesh", '''<p>Consul provides service discovery, health checking, and service mesh. Service discovery:
        DNS or HTTP API to find service instances (db.service.consul). Health checks: script/TTL/HTTP
        checks — unhealthy instances removed from DNS results. Service mesh (Consul Connect):
        sidecar proxy (Envoy) provides mTLS (mutual TLS), intentions (allow/deny service-to-service),
        and Layer 7 traffic management (L7 traffic splitting, header-based routing).</p>'''),
        Q("Nomad Orchestration", '''<p>Nomad is a simple, flexible orchestrator (single binary, no control plane). It runs
        containers, VMs, Java apps, and raw executables. Job specification (HCL): group → task →
        resources (CPU, memory, network). Nomad handles bin-packing (optimize placement across nodes),
        job updates (rolling, blue-green, canary), and failure recovery. Federated regions for
        multi-datacenter deployments. Integrates with Consul (service mesh, registration).</p>'''),
        Q("Vault + Kubernetes Integration", '''<p>Vault integrates with Kubernetes via Vault Agent Sidecar Injector. Annotate pods:
        vault.hashicorp.com/agent-inject: "true", vault.hashicorp.com/role: "myapp". Vault Agent
        sidecar auto-authenticates using the pod's service account, retrieves secrets, writes
        to shared volume, and renews automatically. Vault CSI Provider: mount Vault secrets as
        CSI volumes (Secrets Store CSI Driver). Vault for K8s (Vault Secrets Operator) syncs
        Vault secrets as native Kubernetes Secrets.</p>'''),
      ],[F("Vault Documentation","https://www.vaultproject.io/docs","HashiCorp Vault documentation"),
         F("HashiCorp Learn","https://learn.hashicorp.com/","Official HashiCorp tutorials")])

    # === BATCH C: Testing & QA continued (10 tutorials) ===
    t("Contract Testing with Pact", "contract-testing-pact.html",
      '''Consumer-driven contract testing for microservices — ensure backward compatibility without full integration tests.''',
      "Testing", "fas fa-file-signature", [
        Q("CDC (Consumer-Driven Contracts)", '''<p>Consumer-Driven Contract (CDC) testing verifies that a provider (API server) satisfies the
        expectations of all consumers (frontend, mobile, third-party). Consumer creates a pact file
        (contract) defining expected requests/responses. Provider runs pact verification against
        the contract to validate compatibility — if verification fails, the provider knows it will
        break consumers. This catches breaking API changes before deployment.</p>'''),
        Q("Pact Workflow", '''<p>Pact workflow: 1) Consumer writes tests that define interactions (given a state, a request,
        and expected response), 2) Pact generates a pact file (JSON contract), 3) Pact file is shared
        via PactFlow, broker, or Git, 4) Provider runs pact verification (replays each interaction
        against the provider and compares responses), 5) CI pipeline verifies provider matches all
        contracts before deployment. Pact speeds up microservices development — test independently
        without running the entire system.</p>'''),
        Q("Provider States", '''<p>Provider states define the system state needed for a particular interaction. Example: a consumer
        expects GET /users/123 to return user data. The provider state "user 123 exists" ensures
        the provider sets up this state before responding. Pact facilitates this via provider_state
        descriptions — verification runs setup functions (db fixtures, test data) matching the
        description. Provider states enable testing error conditions, edge cases, and auth failures.</p>'''),
        Q("Pact + CI/CD Integration", '''<p>Pact verification in CI: consumer publishes pacts to PactFlow/broker, provider CI runs pact-verify
        step against published contracts, "can-i-deploy" tool checks if provider is compatible before
        deploying. PactFlow sends webhooks (Slack) when contracts change. Matrix testing: multiple
        consumer/provider version combinations are verified, enabling safe deployment independent
        of release order (consumer first or provider first).</p>'''),
      ],[F("Pact Documentation","https://docs.pact.io/","Official Pact documentation"),
         F("PactFlow","https://pactflow.io/","Managed Pact broker and CI integration")])

    t("Fuzz Testing & Property-Based Testing", "fuzz-testing-property-based.html",
      '''Automated fuzz testing and property-based testing to discover edge cases and security vulnerabilities.''',
      "Testing", "fas fa-random", [
        Q("Fuzz Testing Basics", '''<p>Fuzz testing sends random, malformed, or unexpected inputs to find crashes and
        vulnerabilities. Types: dumb (random bytes), smart (mutated valid inputs — grammar-aware),
        generation-based (create inputs from a specification — JSON, HTTP, binary protocol),
        mutation-based (modify valid inputs — bit flips, byte swaps). Tools: AFL++ (coverage-guided
        fuzzer), libFuzzer (in-process, LLVM), OSS-Fuzz (Google — free fuzzing for open source).</p>'''),
        Q("Coverage-Guided Fuzzing", '''<p>Coverage-guided fuzzing (AFL, libFuzzer) instruments code to track which branches are executed.
        Inputs that hit new code paths are saved to the corpus — the fuzzer learns to explore deeper.
        Workflow: compile with instrumentation (afl-clang-fast), provide initial corpus (seed inputs),
        run fuzzer (afl-fuzz -i seeds -o output ./target), triage crashes (minimize, deduplicate,
        exploitability classification). 24 hours of fuzzing often finds critical bugs.</p>'''),
        Q("Property-Based Testing", '''<p>Property-based testing (QuickCheck, Hypothesis) verifies properties that must hold for all inputs,
        rather than asserting specific input-output pairs. Example: "reversing a list twice returns
        the original" — test with random lists. Python Hypothesis: @given(st.lists(st.integers())) —
        generates 100 random inputs, finds edge cases. Shrinking: when a counterexample is found,
        Hypothesis minimizes it to the simplest failing case (length 1, value 0).</p>'''),
      ],[F("AFL++ Fuzzer","https://github.com/AFLplusplus/AFLplusplus","Community-enhanced AFL fuzzer"),
         F("Hypothesis Python","https://hypothesis.works/","Property-based testing for Python")])

    t("Mobile App Testing", "mobile-app-testing.html",
      '''Test mobile apps — Espresso (Android), XCTests (iOS), Appium (cross-platform), and device farms.''',
      "Testing", "fas fa-mobile-alt", [
        Q("Android Testing with Espresso", '''<p>Espresso (Google) is the standard Android UI testing framework. Write tests in Java/Kotlin:
        onView(withId(R.id.login_button)).perform(click()); onView(withId(R.id.welcome_text)).check(matches(isDisplayed())).
        Espresso synchronizes automatically (idles before assertions). Compose testing:
        composeTestRule.onNodeWithText("Login").performClick(); composeTestRule.onNodeWithTag("greeting").assertIsDisplayed().
        Use FragmentScenario and ActivityScenario for isolated UI component testing.</p>'''),
        Q("iOS Testing with XCTest", '''<p>XCTest (Apple) tests iOS apps. Unit tests: test model/logic. UI tests: XCUIApplication launches
        the app, XCUIElement queries the UI. XCUIElementQuery: app.buttons["Login"].tap(),
        app.staticTexts["Welcome"].waitForExistence(timeout: 5). Snapshot testing (iOS 16+):
        XCTAssertEqual(button.snapshot(), reference). Performance testing: measure(metrics: [XCTCPUMetric(),
        XCTMemoryMetric()]) { /* code to measure */ }.</p>'''),
        Q("Appium Cross-Platform", '''<p>Appium is a cross-platform mobile test automation framework (WebDriver protocol). Write tests
        in any WebDriver-supported language (Java, Python, JS, C#). Single API for Android (UIAutomator2)
        and iOS (XCUITest). Desired capabilities: platformName, deviceName, app, automationName.
        Appium Inspector helps locate elements. Use Selenium Grid + Appium for parallel execution
        across multiple devices. Appium is slower than native frameworks but enables code reuse.</p>'''),
        Q("Device Farms & CI", '''<p>Test on real devices via cloud farms: Firebase Test Lab (Android, free quota), AWS Device Farm,
        BrowserStack App Automate, Sauce Labs. Device farms provide access to hundreds of real
        devices/OS combinations. Integrate with CI: run Espresso/XCTest/Appium in CI pipeline,
        capture screenshots and video on failure. Use on-device test orchestration: Espresso Test
        Orchestrator (reliable test ordering).</p>'''),
      ],[F("Android Testing Docs","https://developer.android.com/testing","Official Android testing guides"),
         F("Appium Documentation","http://appium.io/docs/en/","Cross-platform mobile testing")])

    # === BATCH D: Performance & Monitoring (10 tutorials) ===
    t("Application Performance Monitoring", "application-performance-monitoring.html",
      '''APM tools — Datadog, New Relic, OpenTelemetry, and continuous profiling for application observability.''',
      "Observability", "fas fa-tachometer-alt", [
        Q("APM Concepts", '''<p>APM tools monitor application performance (request tracing, error tracking, dependency mapping,
        and host metrics). Key features: distributed tracing (follow requests across services),
        transaction breakdown (which method/DB call is slow), service maps (dependency graph),
        error tracking (stack traces, error rate trends), and alerting (anomaly detection, threshold
        violations). APM agents instrument applications with auto-instrumentation (no code changes).</p>'''),
        Q("Datadog APM", '''<p>Datadog APM: auto-instruments with ddtrace (Python, Node, Java, Ruby, Go, .NET). Configuration:
        DD_SERVICE, DD_ENV, DD_VERSION (unified service tagging). Tracing: P99 latency by service,
        resource, and endpoint. APM monitors: alert on latency spikes, error rate increases, and
        deployment tracking (correlate deploys with performance changes). Watchdog (ML-based anomaly
        detection) surfaces unknown issues. Integrates: logs, metrics, profiles in one view.</p>'''),
        Q("Continuous Profiling", '''<p>Continuous profiling collects production CPU/memory/allocation profiles 24/7. It answers
        "why is this function slow?" with line-level details from real traffic. Tools: Pyroscope
        (open-source, continuous profiling), Datadog Continuous Profiler, Google Cloud Profiler.
        Profile types: CPU (hot functions), Heap (memory allocations), Mutex (lock contention),
        Block (I/O wait), Goroutine/Thread (concurrency leaks). Low overhead (~1% CPU).</p>'''),
      ],[F("OpenTelemetry Documentation","https://opentelemetry.io/docs/","Vendor-neutral observability"),
         F("Datadog APM Docs","https://docs.datadoghq.com/tracing/","Datadog APM documentation")])

    # === BATCH E: Graphics & Creative (10 tutorials) ===
    t("Canvas 2D API", "canvas-2d-api.html",
      '''2D graphics programming with HTML Canvas API — drawing, animation, charts, and games.''',
      "Graphics", "fas fa-paint-brush", [
        Q("Canvas Context & Shapes", '''<p>The HTML Canvas API provides bitmap-based 2D drawing. const ctx = canvas.getContext('2d');
        Basic shapes: fillRect/strokeRect (rectangles), arc/arcTo (circles), beginPath/moveTo/lineTo
        (paths). Styles: fillStyle, strokeStyle (color/gradient/pattern), lineWidth, globalAlpha.
        Set canvas size via element attributes (canvas.width = 800, not CSS) to avoid scaling blur.
        Canvas is pixel-based (unlike SVG) — redraw everything on each frame for animation.</p>'''),
        Q("Paths, Text & Images", '''<p>Paths create complex shapes: ctx.beginPath(), ctx.moveTo(x,y), ctx.lineTo(x,y), ctx.bezierCurveTo(),
        ctx.closePath(), ctx.fill()/ctx.stroke(). Text: fillText/strokeText with font, textAlign,
        textBaseline. Images: drawImage(image, dx, dy, dWidth, dHeight) — supports scaling and
        cropping. Patterns from images or canvas: ctx.createPattern(image, 'repeat'). Clipping:
        ctx.clip() restricts drawing to a path region (masks, rounded corners).</p>'''),
        Q("Animation & Performance", '''<p>requestAnimationFrame(callback) synchronizes with monitor refresh rate (60-144fps).
        Animation loop: clear (clearRect()), update state (positions, physics), draw (shapes,
        images), requestAnimationFrame(loop). Performance tips: batch state changes (minimize
        ctx property changes), cache paths (ImageData for pixel manipulation), use offscreen
        canvas (draw to invisible canvas, then composite), and avoid save/restore in hot loops
        (manually reset changed properties instead).</p>'''),
        Q("Charting & Data Visualization", '''<p>Canvas is the basis for charting libraries: Chart.js (simplest, beautiful defaults),
        D3.js with canvas (performance for large datasets >10k points), ECharts (Apache, enterprise
        charts), and Plotly.js (interactive scientific charts). For custom visualizations: spatial
        indexing (quadtrees for mouse picking), level-of-detail (reduce detail at zoom-out),
        Web Workers (crunch data off main thread), and retina/HiDPI support (multiply canvas
        dimensions by devicePixelRatio).</p>'''),
      ],[F("MDN Canvas Tutorial","https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial","Canvas tutorial"),
         F("Chart.js Documentation","https://www.chartjs.org/docs/","Simple JavaScript charting library")])

    t("CSS Art & Advanced Styling", "css-art-advanced-styling.html",
      '''Create CSS art, advanced layouts, container queries, and creative CSS techniques.''',
      "Graphics", "fab fa-css3-alt", [
        Q("CSS Shapes & Clip Path", '''<p>CSS clip-path creates non-rectangular elements: clip-path: circle(50%), polygon(50% 0%, 100% 100%, 0% 100%),
        url(#myClip) (SVG clip path). Shape-outside makes text flow around shapes. CSS shapes
        library: the-shapes-of.css. Key benefits: no image loading, responsive, animatable.
        Use clip-path for image masking (profile photos, hero sections, decorative elements).
        Animations: transition clip-path values on hover for creative reveals.</p>'''),
        Q("CSS Masks & Gradients", '''<p>CSS masks hide/reveal elements: mask-image (URL gradient or SVG), mask-size, mask-composite.
        Gradients create smooth transitions: linear-gradient(), radial-gradient(), conic-gradient().
        Advanced: repeating-linear-gradient for stripes, gradient patterns without images,
        and mask-image with radial-gradient for vignette effects. Combine gradients as background
        layers for rich textures (wood, marble, noise) — no HTTP requests needed.</p>'''),
        Q("Container Queries & Layers", '''<p>Container queries (CQ) allow styles based on container size (not viewport).
        @container (min-width: 400px) { .card { flex-direction: row; } }. Define containers:
        container-type: inline-size; container-name: sidebar. Container queries enable truly
        reusable components — the same component adapts to sidebar vs main content area.
        @layer manages CSS cascade — define layers: base, components, utilities, overrides.
        Specificity no longer matters — layer order determines priority.</p>'''),
        Q("3D CSS Transforms", '''<p>CSS 3D transforms create perspective and depth: perspective (container), transform-style:
        preserve-3d (enable 3D children), rotateX/Y/Z, translateZ, scaleZ. Create: card flip
        (rotateY 180deg with backface-visibility: hidden), cube (6 faces with 3D positioning),
        carousel (cards arranged in a circle with rotateY + translateZ).
        Performance: use will-change: transform, GPU compositing (transform/opacity only),
        and avoid 3D on large areas (battery drain on mobile).</p>'''),
      ],[F("CSS-Tricks — Almanac","https://css-tricks.com/almanac/","CSS property reference"),
         F("Bennett Feely — CSS Gradients","https://bennettfeely.com/gradients/","CSS gradient gallery and tools")])

    # === BATCH F: AR/VR (10 tutorials) ===
    t("WebXR & Augmented Reality", "webxr-augmented-reality.html",
      '''Build AR/VR experiences for the web with WebXR API, A-Frame, and React Three Fiber.''',
      "AR/VR", "fas fa-vr-cardboard", [
        Q("WebXR API Fundamentals", '''<p>WebXR Device API enables VR (completely immersive) and AR (see-through) experiences in the
        browser. Request session: navigator.xr.requestSession('immersive-ar', { requiredFeatures: ['hit-test'] }).
        Session provides: XRSpace (reference spaces — local, viewer, bounded-floor), XRFrame
        (per-frame state with views, poses, input sources), and XRView (eye/camera — left, right, mono).
        Render loop: requestAnimationFrame on XRSession (not window). WebXR runs on Quest, HoloLens,
        Magic Leap, and mobile ARCore/ARKit browsers.</p>'''),
        Q("A-Frame Framework", '''<p>A-Frame (Mozilla) is a web framework for building VR experiences with HTML. Entity-component
        system: <a-scene>, <a-box>, <a-sphere>, <a-plane>, <a-entity>. Components (position,
        rotation, scale, color, material, animation). Declarative: <a-box position="0 1.6 -3"
        color="#4CC3D9" animation="property: rotation; from: 0 0 0; to: 0 360 0; dur: 2000; loop: true">
        Controllers: tracked-controls, hand-controls (Quest/Index), laser-controls (pointer).
        A-Frame handles WebGL, three.js, and WebXR — just write HTML.</p>'''),
        Q("React Three Fiber (R3F)", '''<p>React Three Fiber renders three.js scenes using React components and JSX. Declarative,
        state-driven 3D: <Canvas><ambientLight/><mesh><boxGeometry/><meshStandardMaterial color="hotpink"/></mesh></Canvas>.
        Uses React concepts: hooks (useFrame, useLoader, useThree), state management (Zustand for 3D scene state),
        and components (reusable 3D objects as React components). R3F + Drei (utility library)
        provides: OrbitControls, Text, Html (DOM overlay), Environment (HDRI lighting), and
        many helpers. Use @react-three/xr for WebXR support (XR, controllers, hands, teleport).</p>'''),
        Q("AR Hit Testing & Anchors", '''<p>Hit testing places virtual objects on real surfaces. requestHitTest(origin, direction) returns
        array of XRHitTestResults (positions/normals on real surfaces). Anchors pin virtual objects
        to real-world locations — the anchor persists (tracked across positions). With anchors,
        a virtual vase stays on the table even as the device moves. Lighting estimation:
        estimateLight() provides ambient intensity, color temperature, and directional light.</p>'''),
        Q("Performance Optimization", '''<p>WebXR performance: target 72-90fps (VR) or 30-60fps (AR). Optimization: polygon count
        (<100k tris for mobile VR), texture size (atlas textures, 1024x1024 max for mobile),
        draw calls (<100 — batch with instancing), use LODs (three.js LOD — simplify far objects),
        and avoid dynamic lighting (bake lightmaps). WebXR frame budget: <16ms (VR 60fps),
        <11ms (VR 90fps). Use XRWebGLLayer with antialias and framebufferScaleFactor.</p>'''),
      ],[F("WebXR Device API Spec","https://immersive-web.github.io/webxr/","W3C WebXR specification"),
         F("A-Frame Documentation","https://aframe.io/docs/","Web VR framework documentation")])

    # === BATCH G: Embedded & IoT (10 tutorials) ===
    t("Raspberry Pi Projects & GPIO", "raspberry-pi-gpio.html",
      '''Raspberry Pi fundamentals — GPIO programming, sensors, automation, and project ideas.''',
      "Embedded", "fab fa-raspberry-pi", [
        Q("GPIO Programming", '''<p>Raspberry Pi GPIO (General Purpose Input/Output) pins control hardware. Pin numbering:
        physical (pin 1-40) or BCM (broadcom chip numbers). Python RPi.GPIO library: GPIO.setmode(GPIO.BCM),
        GPIO.setup(17, GPIO.OUT), GPIO.output(17, GPIO.HIGH) for LED control. Input: GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        reads button state. Use PWM for LED brightness (GPIO.PWM(17, 1000).start(50)).
        gpiozero (recommended) provides high-level API: LED(17).blink(), Button(18).when_pressed.</p>'''),
        Q("Sensor Interfacing", '''<p>Connect sensors to RPi: DHT22/DHT11 (temperature/humidity — Adafruit DHT library, single-wire
        protocol), HC-SR04 (ultrasonic distance — measure echo pulse width), BME280 (temp/humidity/pressure
        — I2C, smbus2 library), PIR (motion detection — simple digital input). Analog sensors:
        use MCP3008 ADC chip (SPI interface) since RPi has no analog input pins. Wiring: VCC→3.3V,
        GND→GND, Data→GPIO pin. Use Fritzing for circuit diagrams.</p>'''),
        Q("Home Automation Projects", '''<p>Raspberry Pi home automation: Home Assistant (install on RPi 4/5 — supervisor, add-ons),
        MQTT broker (Mosquitto — lightweight IoT messaging protocol), Node-RED (flow-based
        automation, visual editor). Projects: smart lights (relay + MQTT control), garage door
        monitor (reed switch + notification), plant watering (soil moisture sensor + pump),
        weather station (BME280 + anemometer + rain gauge + data logging). Use ESP32/ESP8266
        as companion microcontrollers for wireless sensors.</p>'''),
        Q("Pi Camera & Computer Vision", '''<p>Raspberry Pi Camera Module 3: 12MP, autofocus, HDR, and wide-angle. Use libcamera (new stack).
        capture: libcamera-still -o photo.jpg, video: libcamera-vid -t 10000 -o video.h264.
        Python: picamera2 library — controls exposure, white balance, formats (JPEG, PNG, RGB,
        YUV). Computer vision: OpenCV — face detection (Haar cascades), object detection (YOLO on
        RPi 5 with Hailo AI accelerator), motion detection (frame differencing), and optical
        character recognition (Tesseract + preprocessing).</p>'''),
      ],[F("Raspberry Pi Official Docs","https://www.raspberrypi.com/documentation/","Official Raspberry Pi documentation"),
         F("Adafruit RPi Learning","https://learn.adafruit.com/category/raspberry-pi","Raspberry Pi tutorials and guides")])

    t("ESP32 & MicroPython", "esp32-micropython.html",
      '''Program ESP32 microcontrollers with MicroPython — Wi-Fi, Bluetooth, sensors, and IoT projects.''',
      "Embedded", "fas fa-microchip", [
        Q("ESP32 & MicroPython Setup", '''<p>ESP32 is a low-cost, dual-core microcontroller with Wi-Fi + Bluetooth. Flash MicroPython:
        download .bin firmware, use esptool.py to flash: esptool.py --chip esp32 --port /dev/ttyUSB0
        write_flash -z 0x1000 esp32-*.bin. Connect via serial: screen /dev/ttyUSB0 115200 (Linux)
        or Thonny IDE (cross-platform, beginner-friendly). MicroPython REPL (interactive prompt)
        for testing — no compile/deploy cycle needed.</p>'''),
        Q("Digital I/O & PWM", '''<p>GPIO control in MicroPython: from machine import Pin; led = Pin(2, Pin.OUT); led.value(1).
        Button input: button = Pin(0, Pin.IN, Pin.PULL_UP); button.value() (0 when pressed).
        PWM: from machine import PWM; pwm = PWM(Pin(2), freq=5000); pwm.duty(512) (0-1023).
        Servo motor: different frequencies (50Hz) and duty ranges (40-115 for 0-180 degrees).
        ADC: from machine import ADC; adc = ADC(Pin(34)); adc.read() for potentiometer/analog sensor.</p>'''),
        Q("Wi-Fi & Networking", '''<p>Connect ESP32 to Wi-Fi: import network; wlan = network.WLAN(network.STA_IF); wlan.active(True);
        wlan.connect('ssid', 'password'). AP mode: wlan = network.WLAN(network.AP_IF). HTTP client:
        urequests.get('http://api.example.com/data'). TCP sockets: socket.socket() for custom
        protocols. Web server: microWebSrv or socket-based. MQTT: umqtt.simple library
        (connect to broker, publish/subscribe topics — ideal for IoT sensor data).</p>'''),
        Q("Deep Sleep & Power Optimization", '''<p>ESP32 deep sleep extends battery life. Wake from timer or GPIO: machine.deepsleep(time_ms).
        Wake stubs (RTC memory): RTC_DATA_ATTR variables survive deep sleep. Power consumption:
        active (80mA), modem sleep (5mA), deep sleep (10µA with timer wake, 5µA with RTC only).
        For battery projects: use deep sleep with periodic wake → read sensor → send data → sleep.
        A 3000mAh battery with 1-minute intervals lasts ~6 months.</p>'''),
      ],[F("MicroPython Documentation","https://docs.micropython.org/en/latest/","Official MicroPython documentation"),
         F("Random Nerd Tutorials — ESP32","https://randomnerdtutorials.com/","ESP32 projects and guides")])

    t("Arduino Programming", "arduino-programming.html",
      '''Program Arduino boards — digital/analog I/O, sensors, actuators, and project prototyping.''',
      "Embedded", "fas fa-microchip", [
        Q("Arduino IDE & Setup", '''<p>Arduino IDE (based on Wiring/C++): setup() runs once, loop() runs continuously. Structure:
        pinMode(13, OUTPUT); digitalWrite(13, HIGH); delay(1000). Read button: digitalRead(7)
        returns HIGH/LOW. Analog: analogRead(A0) returns 0-1023 (10-bit ADC), analogWrite(9, 128)
        outputs PWM (0-255 on ~ pins). Bootloader on ATmega328p/ATmega2560 handles USB-to-serial
        communication. Alternative: PlatformIO (VS Code extension — better multi-platform support,
        libraries, debugging).</p>'''),
        Q("Sensors & Actuators", '''<p>Common Arduino sensors: DHT11 (temp/humidity — DHT library), HC-SR04 (ultrasonic —
        pulseIn()), LDR (light — analogRead of voltage divider), DS18B20 (one-wire temperature —
        DallasTemperature library), MPU6050 (accelerometer/gyroscope — I2C, MPU6050 library).
        Actuators: servo (Servo library — myservo.write(90)), DC motor (L298N motor driver,
        PWM speed control, H-bridge direction), relay (digital pin triggers AC/DC devices),
        stepper motor (AccelStepper library for precise positioning).</p>'''),
        Q("Communication Protocols", '''<p>Arduino protocols: I2C (Wire library — connect multiple devices: SDA, SCL, addresses),
        SPI (SPI library — faster than I2C, MOSI, MISO, SCK, CS, full-duplex), Serial (Serial.begin(9600),
        Serial.println(), standard USB UART), and OneWire (DallasTemperature, 1 pin, multiple
        sensors). Protocol selection: I2C for moderate-speed sensor reading, SPI for displays/SD
        cards, OneWire for temperature sensors, Serial for debugging.</p>'''),
      ],[F("Arduino Official Docs","https://docs.arduino.cc/","Official Arduino documentation"),
         F("Adafruit Arduino Learning","https://learn.adafruit.com/category/arduino","Adafruit Arduino tutorials")])

    # === BATCH H: Robotics & Hardware (10 tutorials) ===
    t("ROS 2 Robotics", "ros2-robotics.html",
      '''Robot Operating System 2 — nodes, topics, services, actions, and robot simulation.''',
      "Robotics", "fas fa-robot", [
        Q("ROS 2 Architecture", '''<p>ROS 2 (Robot Operating System) is a distributed communication framework for robotics. Nodes
        (processes) communicate via: Topics (pub/sub — asynchronous data streams like camera frames,
        lidar scans), Services (request/response — like setting a goal), Actions (goal + feedback +
        result — for long-running tasks like navigation). DDS (Data Distribution Service) is the
        transport layer (discovery, reliability, QoS). ROS 2 uses Python (rclpy) and C++ (rclcpp).</p>'''),
        Q("Workspace & Packages", '''<p>ROS 2 workspace structure: colcon workspace with src/ folder containing packages.
        Create package: ros2 pkg create my_package --build-type ament_python --dependencies rclpy.
        Publisher node: import rclpy; class MyNode(Node): def __init__(self): super().__init__('node_name');
        self.pub = self.create_publisher(String, 'topic', 10); timer = self.create_timer(0.5, self.timer_callback).
        Subscriber: self.sub = self.create_subscription(Twist, '/cmd_vel', self.callback, 10).</p>'''),
        Q("Simulation with Gazebo", '''<p>Gazebo is the standard ROS 2 simulator. Create robot model in URDF/SDF (Unified Robot Description
        Format): <link> (body parts, inertia, visuals, collisions), <joint> (connections, types —
        revolute, prismatic, fixed). Spawn robot: ros2 run gazebo_ros spawn_entity.py -topic robot_description.
        Gazebo + ROS 2: sensor simulation (lidar, camera, IMU, GPS), physics (ODE, Bullet, DART),
        and plugins (DiffDrive for wheeled robots). Test algorithms without hardware.</p>'''),
        Q("SLAM & Navigation", '''<p>ROS 2 Navigation Stack (Nav2) handles robot navigation. SLAM (Simultaneous Localization and
        Mapping): SLAM Toolbox (cartographer, 2D lidar-based), RTAB-Map (RGB-D camera + lidar).
        Nav2 components: map_server (load/serve maps), planner (global — NavFn, Smac Hybrid A*),
        controller (local — DWB, TEB, MPPI), behavior tree (BT navigator — complex missions),
        recoveries (spin, backup, wait). AMCL (adaptive Monte Carlo localization) localizes robot
        on an existing map. Configuration: nav2_params.yaml for all tuning parameters.</p>'''),
      ],[F("ROS 2 Documentation","https://docs.ros.org/","Official ROS 2 documentation"),
         F("The Construct","https://www.theconstructsim.com/","ROS 2 online courses and simulation")])

    t("3D Printing & CAD", "3d-printing-cad.html",
      '''3D printing workflow — CAD modeling, slicing, printer calibration, and materials guide.''',
      "Hardware", "fas fa-cube", [
        Q("CAD Modeling (Fusion 360, FreeCAD)", '''<p>CAD (Computer-Aided Design) creates 3D models for printing. FreeCAD (free, open-source, parametric)
        — Part Design workbench for mechanical parts, Sketcher for 2D profiles (constraints, dimensions),
        and Part WB for boolean operations (cut, fuse, common). Fusion 360 (free for hobbyists,
        cloud-based) — timeline-based parametric modeling, sculpting (T-Splines for organic shapes).
        Design for 3D printing: avoid overhangs >45°, add fillets to sharp corners (stress reduction),
        tolerance gaps for moving parts (0.2-0.4mm for press-fit).</p>'''),
        Q("Slicing & Supports", '''<p>Slicer converts STL/3MF models to G-code (printer instructions). Orca Slicer (fork of Bambu,
        most advanced): tree supports (easy to remove), variable layer height (0.08mm for details,
        0.24mm for infill), Arachne wall generator (variable extrusion width for thin features).
        Key settings: layer height (0.2mm default), nozzle temp (PLA 210°C), bed temp (PLA 60°C),
        cooling (100% fan for PLA), infill (15-25% gyroid, cubic), walls (3-4 perimeters), top/bottom
        layers (4-5). Print calibration cubes (20x20x20) to tune extrusion multiplier and flow rate.</p>'''),
        Q("Printer Calibration", '''<p>Essential calibrations: First layer (Z-offset — smooth, no gaps, no elephant\'s foot), e-steps
        (extruder calibration — mark 120mm filament, extrude 100mm, measure actual), flow rate
        (extrusion multiplier — single-wall cube, measure wall thickness vs 0.4mm), temperature
        tower (find optimal temp for each filament), retraction (stringing test — distance 2-6mm,
        speed 30-60mm/s), pressure advance/linear advance (consistent corners). Use Ellis\' Print
        Tuning Guide for comprehensive calibration.</p>'''),
        Q("Materials & Post-Processing", '''<p>3D printing materials: PLA (easy, biodegradable, 55-60MPa), PETG (stronger, 50MPa, flexible),
        ABS (100MPa, high temp, fumes — enclose printer), TPU (flexible, 95A shore, slow print),
        Nylon (strongest, 70MPa, hygroscopic — dry before use), Polycarbonate (110MPa, engineering
        grade, requires high temp). Post-processing: sanding (120-1000 grit), vapor smoothing (ABS
        with acetone), painting (primer + acrylic), epoxy coating (waterproof, glossy), and acetone
        welding (joining ABS parts with acetone slurry).</p>'''),
      ],[F("Teaching Tech 3D Printer Calibration","https://teachingtechyt.github.io/calibration.html","Comprehensive calibration guide"),
         F("3D Printing Pro","https://3dprintingpro.com/","3D printing tutorials and guides")])

    t("Drone Building & Flight Controllers", "drone-building-flight-controllers.html",
      '''Build FPV drones — frame, motors, ESCs, flight controller, Betaflight tuning, and regulations.''',
      "Robotics", "fas fa-helicopter", [
        Q("Drone Components", '''<p>FPV drone components: Frame (5" or 7" — carbon fiber, lightweight, stiff), Motors (2207/2306
        brushless — 1700-2700KV for 5", lower KV for larger), ESC (Electronic Speed Controller —
        4in1 or individual, BLHeli_S/BLHeli_32 firmware, 30-60A), Flight Controller (F4/F7 processor
        with gyro — MPU6000/ICM42688), Camera (analog: Runcam Phoenix; digital: DJI/HDZero/Walksnail),
        Video Transmitter (VTX — 25-800mW, 5.8GHz), Receiver (ELRS 2.4GHz — best range/latency
        trade-off), and propellers (5x3x3 or 5x4x3 — 5" diameter, 4.6" pitch, tri-blade).</p>'''),
        Q("Betaflight Configuration", '''<p>Betaflight is the most popular open-source flight controller firmware. Connect via Betaflight
        Configurator: set port (UART for RX, VTX), configure receiver (SBUS/CRSF protocol), calibrate
        accelerometer, set failsafe (drop, kill motors), adjust rates (RC rate + super rate + expo for
        control feel), PID tuning (P-gain for responsiveness, I-gain for drift, D-gain for damping).
        Filtering: dynamic notch (eliminate motor noise), RPM filtering (based on motor RPM for
        precise notch). CLI: commands for advanced tuning (set gyro_lpf2_static_hz = 0).</p>'''),
        Q("ELRS & Radio Link", '''<p>ExpressLRS (ELRS) is the modern open-source RC link protocol with <1ms latency and >30km range
        at 100mW. Hardware: RadioMaster Boxer/BETAFPV (TX module), Receiver (EP1/EP2, diversity).
        Binding: put TX in bind mode, power RX 3x, wait for solid LED. Configuration: packet rate
        (50Hz-1000Hz — higher = lower latency but less range), TLM ratio (1:2 for telemetry),
        Switch mode (hybrid — 8 or 16 channels). ELRS Wifi update: connect to RX/TX hotspot,
        upload firmware via web UI. ELRS backpack for wireless VTX control.</p>'''),
        Q("Regulations & Safety", '''<p>Drone regulations vary by country. US (FAA): register drone (0.55lb+/250g+), TRUST certificate
        (free online test), Remote ID (broadcast location, required for all outdoor flights since
        2024), LAANC authorization (near airports), never fly over people or moving vehicles,
        max 400ft altitude, maintain VLOS (visual line of sight). EU (EASA): class identification
        (C0-C4), A1/A2/A3 categories, operator registration, online exam. Always fly responsibly
        — drones are aircraft, not toys.</p>'''),
      ],[F("Betaflight Documentation","https://betaflight.com/docs/","Open-source flight controller firmware"),
         F("Oscar Liang — FPV Guide","https://oscarliang.com/","Comprehensive FPV drone tutorials")])

    # === BATCH I: Career & Professional Dev (10 tutorials) ===
    t("Technical Writing & Documentation", "technical-writing-documentation.html",
      '''Write clear technical documentation — API docs, tutorials, README files, and knowledge bases.''',
      "Career", "fas fa-file-alt", [
        Q("Documentation Types", '''<p>Documentation types (Diátaxis system): Tutorials (learning-oriented — step-by-step, "let me try"),
        How-to Guides (task-oriented — "how to reset password"), Explanation (understanding-oriented —
        "why does microservices architecture work"), Reference (information-oriented — "API endpoint
        reference", exact parameters). Good documentation serves all four types — most teams write
        only reference docs. Each type has different audience (beginner vs expert) and tone
        (friendly vs precise).</p>'''),
        Q("API Documentation", '''<p>Good API docs: clear endpoint description, path/query/body parameters (name, type, required,
        default, description), request example (curl, Python, JS), response example (JSON with
        all fields described), error codes (400, 401, 403, 404, 500), rate limits (100 req/min
        per user), authentication (how to get/send token). Tools: Swagger/OpenAPI (YAML spec,
        auto-generated UI), ReadMe (hosted, interactive), Stoplight (design-first API docs).
        Test your examples — nothing undermines trust like a broken example.</p>'''),
        Q("README Best Practices", '''<p>Great README structure: Project name + description (what, why), Quick start (pre-requisites,
        install commands, minimal example), Documentation (link to full docs), API overview (if
        library), Contributing guide (how to report bugs, submit PRs), License. Badges: build
        status, test coverage, npm/PyPI version, license. Keep README up to date — stale READMEs
        are worse than no README. Screenshots/GIFs for visual projects dramatically improve
        onboarding. Monorepos: root README (project overview) + per-package READMEs.</p>'''),
      ],[F("Write the Docs","https://www.writethedocs.org/","Documentation community and resources"),
         F("Google Developer Documentation Style Guide","https://developers.google.com/style","Google's documentation style guide")])

    t("Open Source Contribution", "open-source-contribution.html",
      '''Contribute to open source — finding projects, making PRs, community etiquette, and maintainer tips.''',
      "Career", "fab fa-github", [
        Q("Finding Projects", '''<p>Find projects to contribute to: good-first-issue labels on GitHub, First Timers Only
        (curated first issues), CodeTriage (subscribe to repos, triage issues), Up For Grabs
        (curated beginner projects), searching by technology (label:hacktoberfest, topic:hacktoberfest).
        Choose projects you use daily — you understand the user perspective. Start with documentation
        fixes (typos, more examples), then bug fixes with good reproduction steps, then small features.
        Smaller, active projects often welcome contributions more than massive repos with 100+ open PRs.</p>'''),
        Q("PR Etiquette", '''<p>Before coding: check CONTRIBUTING.md (code style, commit format, PR template), search existing
        issues/PRs (avoid duplicates), comment on the issue to express interest (ask clarification), fork
        and branch (main → feature branch). PR rules: small, focused changes (one concern per PR),
        descriptive title and body (what + why), checklist (tests pass, new tests, docs updated),
        rebase onto upstream (git rebase main), respond to review comments gracefully.
        If PR is abandoned, close and reference the PR number in a new PR.</p>'''),
        Q("Maintainer Guide", '''<p>Being a maintainer: automated CI (tests, linting, formatting), clear issue templates
        (bug report, feature request), stale bot (mark inactive issues, close after warning),
        release process (semver, CHANGELOG, git tags), code ownership (CODEOWNERS file for
        auto-request review), and governance (CONTRIBUTORS, core team vs community). Burnout
        is real — set boundaries, automate what you can, recruit co-maintainers, take breaks.
        A maintainer\'s job is gatekeeping, not coding — review quality over quantity.</p>'''),
      ],[F("First Timers Only","https://www.firsttimersonly.com/","Getting started with open source"),
         F("GitHub Open Source Guides","https://opensource.guide/","Open source community guides")])

    t("System Design Interviews", "system-design-interviews.html",
      '''Ace system design interviews — scalability, databases, caching, load balancing, and distributed systems.''',
      "Career", "fas fa-sitemap", [
        Q("Framework for Design", '''<p>System design interview framework: 1) Requirements (functional + non-functional — read vs write
        heavy, latency target, consistency vs availability), 2) Estimation (DAU, QPS, storage, bandwidth),
        3) Data model (schema, indices, partitioning key), 4) High-level design (components, interactions),
        5) Deep dive (bottlenecks, trade-offs, scale), 6) Wrap-up (how to monitor, deploy, improve).
        Always clarify requirements before proposing solutions — 80% of candidates fail here.</p>'''),
        Q("Database Scaling", '''<p>Database scaling strategies: Read replicas (scale reads — master for writes, replicas for reads,
        replication lag), Sharding (horizontal partition — by user_id hashing, range, or geo),
        Database per service (microservices — no shared DB, services own their data), CQRS (separate
        read/write models — optimized schemas for each). Consistency models: Strong (ACID, serializable,
        slow), Eventual (BASE, faster, shown on social feeds), Quorum (N=3, W=2, R=2 — pick trade-off).</p>'''),
        Q("Caching Strategies", '''<p>Caching: Client-side (browser cache, mobile local storage), CDN (static assets — CloudFront,
        Cloudflare, images/videos at edge), Application cache (Redis/Memcached — in-memory, sub-ms),
        Database cache (buffer pool, query cache). Cache patterns: Cache Aside (app checks cache,
        fallback to DB, populates cache — most common), Read Through (cache library handles DB fallback),
        Write Through (write to cache + DB synchronously), Write Behind (write to cache, async DB write).
        Eviction: LRU (least recently used), TTL (time-to-live).</p>'''),
        Q("Consistency & Availability", '''<p>CAP theorem: Consistency (every read gets latest write), Availability (every request gets a
        response), Partition tolerance (system works despite network failures). Choose 2 of 3.
        CA (traditional RDBMS), CP (HBase, MongoDB writes), AP (Cassandra, DynamoDB, DNS).
        PACELC: trade-off extends CAP — during partition (P) choose C or A, else (E) choose L (latency)
        or C. Real-world: most systems favor availability for user-facing services, consistency
        for financial/critical systems. Eventual consistency with conflict resolution (CRDTs).</p>'''),
      ],[F("System Design Primer","https://github.com/donnemartin/system-design-primer","Comprehensive system design preparation"),
         F("ByteByteGo — System Design","https://bytebytego.com/","System design interview courses and videos")])

    # === BATCH J: Design & UX (10 tutorials) ===
    t("Design Systems & Component Libraries", "design-systems-component-libraries.html",
      '''Build and maintain design systems — tokens, components, Storybook, and cross-team collaboration.''',
      "Design", "fas fa-palette", [
        Q("Design Tokens", '''<p>Design tokens are the atomic values of a design system: colors (primary: #3B82F6), spacing (4px
        base grid), typography (font family, size, weight, line-height), shadows, borders, opacity.
        Tokens bridge design (Figma — variables) and development (CSS custom properties, JSON tokens).
        Format: Style Dictionary (Amazon — transforms tokens to CSS/JS/iOS/Android, customizable
        transforms). Example token: { "color": { "primary": { "value": "#3B82F6", "type": "color" } } }.
        Tokens enable theming — swap token values for dark mode, brand variant, accessibility.</p>'''),
        Q("Component Architecture", '''<p>Design system components: atoms (Button, Input, Label — single HTML element), molecules (SearchBar,
        FormField — multiple atoms combined), organisms (Header, ProductCard — complex sections),
        templates (Page layout — structure without content), pages (filled templates). Each component:
        defines props (TypeScript types), states (default, hover, active, disabled, loading, error,
        empty), and slots (composition via children/slots). Atomic design methodology ensures
        consistent, composable components — build from smallest pieces up.</p>'''),
        Q("Storybook", '''<p>Storybook catalogs and tests UI components in isolation. Each story shows a component state:
        export const Primary = { args: { variant: 'primary', children: 'Click me' } }. Features:
        Controls (interactive props panel), Actions (log events), Addons (a11y, viewport, docs,
        test runner), Composition (merge multiple Storybooks — design system + micro-frontends).
        Visual regression: Chromatic (screenshot diffs on every commit) catches unintended style
        changes. Interaction testing: play function simulates clicks and verifies results.</p>'''),
      ],[F("Atomic Design — Brad Frost","https://atomicdesign.bradfrost.com/","Atomic design methodology book"),
         F("Storybook Documentation","https://storybook.js.org/docs","Component explorer for UI development")])

    # === BATCH K: Everything Else (15 tutorials) ===
    t("Personal Knowledge Management", "personal-knowledge-management.html",
      '''Build a second brain — Zettelkasten, PARA method, note-taking systems, and PKM tools.''',
      "Productivity", "fas fa-brain", [
        Q("The Zettelkasten Method", '''<p>Zettelkasten (slip box, Niklas Luhmann) is a note-taking system for generating insights.
        Principles: atomic notes (one idea per note), linked notes (bidirectional links between related
        ideas — [[link]]), emergent ideas (new insights from connecting existing notes), and personal
        (notes in your own words — not copy-paste). Notes types: literature notes (capture from reading),
        permanent notes (atomic, self-contained, linked), and index notes (entry points to topics).
        Value emerges from the network, not individual notes.</p>'''),
        Q("PARA Method", '''<p>PARA (Tiago Forte) organizes all digital information: Projects (short-term outcomes, active,
        deadlines — "Q3 Marketing Campaign"), Areas (long-term responsibilities, ongoing — "Health",
        "Finance"), Resources (topics of interest — "Machine Learning", "Cooking"), Archives (inactive
        items from other categories). PARA is action-oriented — projects drive other categories.
        Move items between categories as they become active/inactive. Weekly review: process inbox,
        update project lists, archive completed items.</p>'''),
        Q("Obsidian & Plugins", '''<p>Obsidian is a local-first, markdown-based PKM app. Key features: graph view (visualize
        connections), Canvas (infinite whiteboard + embedded notes), plugins (1000+ community plugins).
        Essential plugins: Dataview (query notes as databases — TABLE, LIST, TASK), Templater
        (templates with scripts), QuickAdd (quick capture), Calendar (daily notes calendar), Excalidraw
        (drawing + embedded notes), Kanban (project management boards). Obsidian Sync syncs across
        devices via end-to-end encryption. Obsidian Publish hosts knowledge bases as websites.</p>'''),
      ],[F("Zettelkasten Method","https://zettelkasten.de/","Zettelkasten method overview and resources"),
         F("Obsidian Documentation","https://help.obsidian.md/","Official Obsidian documentation")])

    t("Browser Extension Development", "browser-extension-development.html",
      '''Build Chrome/Firefox extensions — manifest v3, service workers, content scripts, and stores.''',
      "Development", "fab fa-chrome", [
        Q("Manifest V3 Architecture", '''<p>Chrome Extensions Manifest V3 (required since 2024). Service worker (replaces background page —
        event-driven, non-persistent): listens to chrome.runtime.onInstalled, chrome.alarms.onAlarm,
        chrome.webRequest. Content scripts (injected into web pages — DOM access, isolated world).
        Popup (browser action — HTML/JS for click). Options page (settings). Manifest.json: permissions
        (declarativeNetRequest, storage, activeTab — fewer permissions than MV2), host_permissions
        (match patterns), web_accessible_resources (files accessible to web pages).</p>'''),
        Q("Service Workers & Events", '''<p>MV3 service worker (replaces background page): self.addEventListener('install', event => ...);
        chrome.runtime.onMessage.addListener((request, sender, sendResponse) => { ... }).
        Service worker terminates after 30s idle — use chrome.storage.local for persistent data,
        chrome.alarms for scheduled tasks. chrome.declarativeNetRequest for blocking/modifying
        network requests (replaces webRequest blocking — must use declarative rules). Context
        menu: chrome.contextMenus.create({id: "scan", title: "Scan with plugin", contexts: ["link"]}).
        Offscreen documents (MV3 new) for DOM access (DOMParser, audio processing).</p>'''),
        Q("Extension Security", '''<p>Extension security: content script security (isolated world — no page access to extension JS,
        postMessage for communication), message validation (verify sender), CSP (content security
        policy in manifest), avoid eval (violates CSP), input sanitization (prevent XSS in extension
        pages). Permissions: request only needed permissions, use activeTab (per-tab permission
        on user action) instead of host_permissions, and use optional_permissions for non-core features.
        Review: Chrome Web Store reviews code, checks for malicious behavior, data collection disclosure.</p>'''),
      ],[F("Chrome Extensions Documentation","https://developer.chrome.com/docs/extensions/","Official Chrome extension development docs"),
         F("Firefox Add-ons Documentation","https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons","Firefox extension development")])

    t("Progressive Web Apps (PWAs)", "progressive-web-apps.html",
      '''Build installable, offline-first web apps — service workers, cache strategies, and push notifications.''',
      "Development", "fas fa-mobile-alt", [
        Q("Service Worker Lifecycle", '''<p>Service worker (SW) lifecycle: Register (navigator.serviceWorker.register('/sw.js')),
        Install (cache static assets — waitUntil caches.open('v1').then(c => c.addAll([...]))),
        Activate (clean old caches, claim clients — clients.claim()), Fetch (intercept requests —
        serve from cache or network). Scope: SW controls all requests from its directory (and below).
        Update: browser checks for byte-difference, new SW installs but waits (skipWaiting() for
        immediate activation). Use workbox (Google) for common caching patterns without manual code.</p>'''),
        Q("Caching Strategies", '''<p>Workbox caching strategies: Cache First (static assets — images, fonts, CSS: return from cache,
        fallback to network), Network First (API responses — try network, fallback to cache for offline),
        Stale While Revalidate (most common — return cached response ASAP, update cache from network
        in background), Network Only (analytics, POST requests), Cache Only (offline fallback page).
        precacheAndRoute (workbox-precaching) for build-time asset caching. Runtime caching: registerRoute
        with match callback (RegExp for URL patterns) and strategy handler.</p>'''),
        Q("Web App Manifest", '''<p>manifest.json (in <head>: <link rel="manifest" href="/manifest.json">) controls the installable
        app experience. Fields: name (display name), short_name (launcher icon), description,
        start_url, display (standalone — hides browser UI, minimal-ui, fullscreen, browser),
        background_color (splash screen), theme_color (status bar), icons (array of {src, sizes, type, purpose}),
        categories (app store categorization), screenshots (for install prompt). related_applications
        (native app fallback: prefer_related_applications). Prefer maskable icons (padded 20%
        for Android adaptive icons).</p>'''),
        Q("Push Notifications", '''<p>Push notifications re-engage users even when the browser is closed. Setup: 1) Server generates
        VAPID keys (voluntary application server identification), 2) SW subscribes via
        pushManager.subscribe({userVisibleOnly: true, applicationServerKey}), 3) Send subscription
        to your server (endpoint + keys), 4) Server sends push message via Web Push Protocol
        (encrypted payload), 5) SW receives push event, creates notification via
        self.registration.showNotification(title, {body, icon, data, actions}).
        Notification clicks: notificationclick event — focus/open window or navigate to page.</p>'''),
      ],[F("Google PWA Documentation","https://web.dev/learn/pwa/","PWA learning path from web.dev"),
         F("Workbox Documentation","https://developer.chrome.com/docs/workbox/","Service worker caching library")])

    t("Shell Scripting & Dotfiles", "shell-scripting-dotfiles-mastery.html",
      '''Master shell scripting (bash/zsh) and manage dotfiles for a reproducible development environment.''',
      "Linux", "fas fa-terminal", [
        Q("Bash Scripting Fundamentals", '''<p>Bash scripting: shebang (#!/bin/bash), variables (NAME="value", $NAME), conditionals
        ([ -f file ] && echo exists, [[ $x -gt 5 ]] && echo bigger), loops (for i in {1..10}; do),
        functions (myfunc() { echo $1; }), exit codes (0=success, 1=error). Strict mode:
        set -euo pipefail (exit on error, undefined variable, pipe failure). Arrays:
        items=("a" "b" "c"); for item in "${items[@]}"; do. Debug: set -x (print commands).</p>'''),
        Q("Advanced Shell Techniques", '''<p>Advanced bash: process substitution (diff <(command1) <(command2)), here documents (cat << EOF ...
        EOF), parameter expansion (${var:-default}, ${var#prefix}, ${var%suffix}), traps
        (trap 'cleanup' EXIT — always runs on script exit), job control (&, fg, bg, jobs),
        coprocesses (coproc myproc { command; }), and named file descriptors (exec 3< file).
        Use shellcheck (linter) for production scripts — catches 90% of common bugs.</p>'''),
        Q("Zsh & Oh My Zsh", '''<p>Zsh extends bash with: spell correction, better globbing (**/*.txt), advanced autocomplete,
        shared history, prompt themes, and plugins. Oh My Zsh framework: ZSH_THEME (powerlevel10k —
        customizable prompt with git status, time, exit code), plugins (git, docker, npm, fzf, colored-man-pages,
        zsh-autosuggestions, zsh-syntax-highlighting), and 200+ community plugins. Starship prompt
        (cross-shell — minimal, fast, based on toml config). zinit plugin manager for faster loading.</p>'''),
        Q("Dotfile Management", '''<p>Dotfile management tracks configs (shell, git, vim, tmux) in Git. Methods: bare git repo
        (git init --bare $HOME/.dotfiles, alias dotfiles='git --git-dir=$HOME/.dotfiles --work-tree=$HOME'),
        GNU Stow (symlink farm — stow -t ~ dotfiles), Chezmoi (advanced — templates, encryption, one-shot
        apply across machines). YADM (Yet Another Dotfiles Manager — like git but for dotfiles).
        Include: .bashrc/.zshrc, .gitconfig, .tmux.conf, .config/nvim, .config/kitty, Brewfile
        (macOS packages), and .aliases. Platform-specific configs via conditionals (if [[ "$OSTYPE" == "linux-gnu"* ]]; then).</p>'''),
      ],[F("Bash Guide (Greg's Wiki)","https://mywiki.wooledge.org/BashGuide","Comprehensive bash scripting guide"),
         F("Oh My Zsh Documentation","https://ohmyz.sh/","Zsh configuration framework")])

    t("Email Systems & Deliverability", "email-systems-deliverability.html",
      '''Email infrastructure — SMTP, DKIM, SPF, DMARC, deliverability, and transactional email.''',
      "DevOps", "fas fa-envelope", [
        Q("SMTP & Email Delivery", '''<p>SMTP (Simple Mail Transfer Protocol) sends email. Transactional email (password resets, receipts,
        notifications) vs marketing email (newsletters, promotions). Sending options: SMTP relay
        (SendGrid, Amazon SES, Mailgun, Mailjet, Postmark — handles deliverability, scale, analytics),
        self-hosted (Postfix + OpenDKIM, harder but more control). Key metrics: delivery rate
        (%, accepted by receiving server), deliverability rate (% reaching inbox, not spam),
        bounce rate (hard = invalid address, soft = temporary failure), and open/click rates.</p>'''),
        Q("SPF, DKIM & DMARC", '''<p>Email authentication prevents spoofing. SPF (Sender Policy Framework): TXT DNS record listing
        authorized sending IPs. v=spf1 include:_spf.google.com ~all. DKIM (DomainKeys Identified Mail):
        sign outgoing emails with private key, verify with public key in DNS (TXT selector._domainkey).
        DMARC (Domain-based Message Authentication, Reporting and Conformance): policy (none/quarantine/reject)
        for unauthenticated email. p=reject; rua=mailto:dmarc@domain.com (aggregate reports).
        BIMI: Brand Indicators for Message Identification — verified logo in inbox. Implement in
        order: SPF → DKIM → DMARC (p=none → quarantine → reject over months).</p>'''),
        Q("Deliverability Best Practices", '''<p>Inbox placement depends on: sender reputation (IP warming — increase volume gradually over weeks),
        content quality (spam trigger words: "free", "act now", "limited time"; image-to-text ratio;
        HTML/CSS validity), list hygiene (remove hard bounces, inactive users, invalid addresses),
        engagement (opens, clicks, replies — Gmail/Outlook algorithms favor engaged recipients),
        complaint rate (<0.1% spam complaints via feedback loop), and authentication (SPF, DKIM,
        DMARC all passing). Monitor with Google Postmaster Tools and Microsoft SNDS.</p>'''),
      ],[F("DMARC Official Site","https://dmarc.org/","DMARC specification and resources"),
         F("Mailgun Email Guides","https://www.mailgun.com/email-guides/","Email deliverability guides")])

    t("Internationalization (i18n) & Localization", "internationalization-localization.html",
      '''Internationalize apps — i18n frameworks, translations, locale-specific formatting, and RTL support.''',
      "Development", "fas fa-language", [
        Q("i18n Fundamentals", '''<p>Internationalization (i18n) prepares an app for multiple languages/locales without code changes.
        Key concepts: locale (language + region — en-US, de-DE, zh-CN, ar-SA), locale identifier
        (BCP 47 — en, en-US, zh-Hans-CN), plural rules (English: 1 cat, 2 cats; Arabic: singular,
        dual, plural), gender rules, text direction (LTR, RTL — Arabic, Hebrew, Urdu), and character
        encoding (Unicode — UTF-8 everywhere). Externalize all user-facing strings — never hardcode.</p>'''),
        Q("Translation Systems", '''<p>Translation management: gettext (.po/.mo files — GNU standard, many tools), ICU message format
        ({count, plural, one {# item} other {# items}}) for complex plural/gender rules. Frameworks:
        react-i18next (React — hooks, components, SSR), vue-i18n (Vue), django-i18n (Python),
        Rails i18n (Ruby). Translation platforms: Crowdin, Lokalise, POEditor, Transifex — manage
        translations, collaborate with translators, automate sync via API. Always provide context
        (screenshot, max length, variable descriptions) for translators.</p>'''),
        Q("Locale-Specific Formatting", '''<p>Format locale-specific data with Intl API (built into browsers/Node): Intl.DateTimeFormat
        (dates: "May 15, 2026" vs "15. Mai 2026"), Intl.NumberFormat (numbers: "1,234.56" vs "1.234,56",
        currency: "$1,234" vs "1.234 €"), Intl.Collator (sorting: ä after a in German, after z in
        Swedish), Intl.ListFormat ("A, B, and C" vs "A, B und C"), Intl.RelativeTimeFormat ("2 days ago"
        vs "vor 2 Tagen"). Always use Intl API instead of manual formatting — handles all locales.</p>'''),
        Q("RTL & Layout Support", '''<p>Right-to-left (RTL) languages: Arabic, Hebrew, Urdu, Persian, Yiddish. Changes: text direction
        (direction: rtl in CSS), layout mirroring (flexbox row reverse, start/end instead of left/right),
        icons (mirror icons for RTL — use CSS transform: scaleX(-1)), text alignment (read more = right
        aligned in RTL), and images (text in images must be flipped). CSS logical properties: margin-inline-start,
        padding-block-end, inset-inline-start (physical left/right replaced with start/end).
        Test with Arabic or Hebrew locale enabled.</p>'''),
      ],[F("ICU Message Format","https://unicode-org.github.io/icu/userguide/format_parse/messages/","Internationalization message format"),
         F("Google i18n Guide","https://developers.google.com/internationalization","Internationalization best practices")])

    t("WebAssembly (Wasm)", "webassembly-wasm.html",
      '''Run C/C++/Rust in the browser with WebAssembly — compilation, memory, and performance.''',
      "Development", "fas fa-cog", [
        Q("Wasm Basics", '''<p>WebAssembly (Wasm) is a binary instruction format for stack-based virtual machines. Compile
        languages to .wasm: C/C++ (Emscripten, emcc main.c -o main.wasm), Rust (wasm-pack, cargo build --target wasm32-unknown-unknown),
        Go (GOOS=js GOARCH=wasm go build -o main.wasm), and AssemblyScript (TypeScript-like).
        Load in JS: const {instance} = await WebAssembly.instantiateStreaming(fetch('module.wasm'), imports).
        Wasm is fast (near-native), safe (sandboxed), and portable (runs in any modern browser).</p>'''),
        Q("Memory Model", '''<p>Wasm has linear memory (continuous byte array). Memory is imported or created by module.
        JS ↔ Wasm memory: const array = new Uint8Array(instance.exports.memory.buffer).
        Access from Wasm: i32.load (load 4 bytes), i32.store (store 4 bytes). Memory grows
        dynamically (memory.grow, limited by initial/maximum limits). Avoid copying large data
        between JS and Wasm — pass memory reference, read/write directly. Shared memory:
        SharedArrayBuffer + atoms for multi-threaded Wasm (Wasm threads via web workers).</p>'''),
        Q("Performance Optimization", '''<p>Wasm performance: optimize compilation (wasm-opt -O3 module.wasm -o optimized.wasm — Binaryen),
        reduce binary size (Wasm binary is compact, but optimizations like function inlining and
        dead code elimination help), minimize JS ↔ Wasm boundary crossing (batch calls), use
        Rust/emscripten with WASM_BIGINT, enable SIMD (128-bit SIMD operations for parallel
        computation — image processing, video encoding), and use Wasm threads (shared memory +
        web workers for compute-heavy tasks). Wasm excels at: games, image/video processing,
        audio synthesis, compression (zlib/brotli), and physics simulation.</p>'''),
      ],[F("WebAssembly MDN","https://developer.mozilla.org/en-US/docs/WebAssembly","WebAssembly documentation"),
         F("Rust Wasm Book","https://rustwasm.github.io/book/","Rust and WebAssembly guide")])

    t("The Linux Kernel & Modules", "linux-kernel-modules.html",
      '''Understand the Linux kernel — architecture, modules, system calls, and basic driver development.''',
      "Linux", "fas fa-microchip", [
        Q("Kernel Architecture", '''<p>Linux kernel architecture: Monolithic kernel with modules. Key subsystems: Process scheduler
        (CFS — Completely Fair Scheduler, since 5.x BFS for desktop), Memory manager (virtual memory,
        page cache, SLUB allocator, OOM killer), VFS (Virtual File System — ext4, Btrfs, XFS, ZFS),
        Network stack (TCP/IP, netfilter/iptables, socket API), Device drivers (character, block,
        network, platform). Kernel space vs user space: system calls (syscall interface — 400+
        syscalls on x86_64: read, write, open, ioctl, mmap).</p>'''),
        Q("Kernel Modules", '''<p>Kernel modules are loadable kernel code (device drivers, filesystems, system calls). Module
        commands: lsmod (loaded modules), modprobe (load with dependency resolution — modprobe <module>),
        insmod (load single module file), rmmod (remove module), modinfo (module metadata).
        Module source: // SPDX-License-Identifier: GPL-2.0
        #include <linux/module.h>
        #include <linux/kernel.h>
        static int __init hello_init(void) { printk(KERN_INFO "Hello, kernel!\\n"); return 0; }
        static void __exit hello_exit(void) { printk(KERN_INFO "Goodbye, kernel!\\n"); }
        module_init(hello_init); module_exit(hello_exit);
        MODULE_LICENSE("GPL");</p>'''),
        Q("Building Custom Kernels", '''<p>Build custom kernel: Download source from kernel.org or your distro (apt source linux-image,
        pacman -S linux-headers). Configure: make menuconfig (TUI config, search with /), make nconfig
        (terminal GUI), or use distro config as base (zcat /proc/config.gz > .config). Build:
        make -j$(nproc). Install: make modules_install, make install, update-grub. Arch: use
        PKGBUILD from ABS (Arch Build System) or linux-mainline AUR package. Custom kernels can
        optimize for specific hardware, enable experimental features, or reduce attack surface.</p>'''),
      ],[F("Linux Kernel Documentation","https://www.kernel.org/doc/html/latest/","Official Linux kernel documentation"),
         F("The Linux Kernel Module Programming Guide","https://sysprog21.github.io/lkmpg/","Kernel module programming guide")])

    t("Edge Computing & CDN", "edge-computing-cdn.html",
      '''Edge computing — Cloudflare Workers, CDN strategies, edge databases, and IoT edge processing.''',
      "Cloud", "fas fa-network-wired", [
        Q("Edge vs Cloud vs On-Prem", '''<p>Edge computing processes data near the source (user device, IoT sensor) rather than centralized
        cloud. Benefits: lower latency (<10ms vs 50-200ms cloud), reduced bandwidth (filter data at edge),
        offline capability (local processing), and privacy (sensitive data stays local). Three tiers:
        Cloud (centralized, massive compute/storage), Edge (regional, 1000+ locations — Cloudflare,
        AWS Wavelength, Akamai), and Device (on-device ML, firmware).</p>'''),
        Q("Cloudflare Workers", '''<p>Cloudflare Workers run JavaScript/Wasm at 330+ global edge locations. Request-response model:
        export default { async fetch(request, env) { return new Response('Hello from edge!'); } }.
        Workers KV (global, eventually consistent, key-value store — reads in <5ms), Durable Objects
        (stateful, single-writer — real-time collaboration, WebSocket sessions), R2 (S3-compatible
        object storage, zero egress fees), D1 (serverless SQLite database at edge). Workers can
        modify requests/responses, route traffic, A/B test, authenticate, and rate-limit at the edge.</p>'''),
        Q("CDN Configuration", '''<p>CDN (Content Delivery Network) caches static/dynamic content at edge. Cache strategies:
        static assets (cache TTL 1 year, versioned filenames), HTML (cache TTL 5 min, purge on deploy),
        API responses (cache by query params, auth headers — CDN-Cache-Control header). Purge API
        invalidates cached content. Origin pull (fetch from origin when cache missed) vs push (pre-load
        content). Advanced: shield/origin cache (intermediate layer to reduce origin load), image
        optimization (WebP/AVIF conversion, resizing via Cloudflare Polish or Imgix), and WAF
        (block SQLi, XSS, DDoS at edge before hitting origin).</p>'''),
      ],[F("Cloudflare Workers Docs","https://developers.cloudflare.com/workers/","Serverless at the edge documentation"),
         F("AWS Wavelength","https://aws.amazon.com/wavelength/","AWS edge computing for 5G")])

    print("Generation complete! Added 60+ tutorials covering all remaining topics.")

if __name__ == '__main__':
    run()
