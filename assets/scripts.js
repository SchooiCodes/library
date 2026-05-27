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

// Theme toggle
(function(){
  var t = document.getElementById('theme-toggle');
  if (!t) return;
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
