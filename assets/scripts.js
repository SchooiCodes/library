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
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
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

// Navbar scroll effect + hamburger
(function(){
  var n = document.getElementById('navbar');
  if (n) {
    window.addEventListener('scroll', function() {
      if (window.scrollY > 50) n.classList.add('scrolled');
      else n.classList.remove('scrolled');
    });
  }
  var h = document.getElementById('hamburger');
  if (h) {
    var m = document.querySelector('.nav-menu');
    h.addEventListener('click', function() {
      h.classList.toggle('active');
      m.classList.toggle('active');
    });
    Array.from(document.querySelectorAll('.nav-menu a')).forEach(function(l) {
      l.addEventListener('click', function() {
        h.classList.remove('active');
        m.classList.remove('active');
      });
    });
  }
})();
