/* Tech Library Service Worker v1 */
const CACHE_NAME = 'tech-library-v1';
const STATIC_ASSETS = [
  '/assets/style.css',
  '/assets/scripts.js',
  '/assets/assistant.js',
  '/assets/favicon.svg',
  '/manifest.json'
];

const CACHE_URLS = new Set(STATIC_ASSETS);

self.addEventListener('install', function(e) {
  e.waitUntil(
    caches.open(CACHE_NAME).then(function(cache) {
      return cache.addAll(STATIC_ASSETS);
    }).catch(function() {
      /* ignore cache errors */
    })
  );
});

self.addEventListener('fetch', function(e) {
  var url = new URL(e.request.url);
  
  /* Skip non-GET requests */
  if (e.request.method !== 'GET') return;
  
  /* Skip CDN/external requests */
  if (url.origin !== location.origin) return;
  
  var isStatic = CACHE_URLS.has(url.pathname) || 
                 /\.(css|js|svg|woff2?|ttf|eot)$/.test(url.pathname);
  
  if (isStatic) {
    /* Cache-first: use cache if available, fallback to network */
    e.respondWith(
      caches.match(e.request).then(function(response) {
        return response || fetch(e.request).then(function(response) {
          if (response && response.status === 200) {
            var cache_copy = response.clone();
            caches.open(CACHE_NAME).then(function(cache) {
              cache.put(e.request, cache_copy);
            });
          }
          return response;
        });
      }).catch(function() {
        /* offline */
        if (url.pathname.endsWith('.css')) {
          return new Response('/* offline */', { headers: { 'Content-Type': 'text/css' } });
        }
        return new Response('');
      })
    );
  } else {
    /* Network-first for HTML/content: try network, fallback to cache */
    e.respondWith(
      fetch(e.request).then(function(response) {
        if (response && response.status === 200) {
          var cache_copy = response.clone();
          caches.open(CACHE_NAME).then(function(cache) {
            cache.put(e.request, cache_copy);
          });
        }
        return response;
      }).catch(function() {
        return caches.match(e.request).then(function(response) {
          return response || new Response('Offline', { status: 503 });
        });
      })
    );
  }
});

self.addEventListener('activate', function(e) {
  e.waitUntil(
    caches.keys().then(function(names) {
      return Promise.all(names.map(function(name) {
        if (name !== CACHE_NAME) {
          return caches.delete(name);
        }
      }));
    })
  );
});
