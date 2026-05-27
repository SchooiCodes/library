// Lightweight scroll reveal (replaces 20KB+ AOS library)
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

// Theme picker
(function(){
  // Theme definitions: name, class, desc, swatch colors
  var THEMES = [
    { id: '', name: 'Default', desc: 'Purple & blue', swatch: ['#667eea','#764ba2'] },
    { id: 'ocean', name: 'Ocean', desc: 'Teal & sky', swatch: ['#0ea5e9','#06b6d4'] },
    { id: 'forest', name: 'Forest', desc: 'Earthy green', swatch: ['#22c55e','#16a34a'] },
    { id: 'sunset', name: 'Sunset', desc: 'Orange & red', swatch: ['#f97316','#ef4444'] },
    { id: 'midnight', name: 'Midnight', desc: 'Deep indigo', swatch: ['#6366f1','#4f46e5'] },
    { id: 'mono', name: 'Mono', desc: 'Grayscale', swatch: ['#6b7280','#4b5563'] },
  ];

  // Apply saved color theme on load
  var savedTheme = localStorage.getItem('colorTheme') || '';
  if (savedTheme) document.body.classList.add('theme-' + savedTheme);

  // Inject theme picker button next to theme-toggle
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

  // Dark/Light toggle (upgraded)
  var t = document.getElementById('theme-toggle');
  if (t) {
    var s = localStorage.getItem('theme');
    if (s === 'dark') document.body.classList.add('dark-mode');
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

// Navbar scroll effect (throttled with rAF) + hamburger + mobile UI
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

  // Mobile bottom nav
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

  // Sidebar toggle (mobile)
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
