/* ===== Tech Library AI Assistant v3 — privacy + QoL ===== */
(function(){
try {

/* ---------- Config ---------- */
var ASSISTANT_ENDPOINT = 'https://tech-library-ai.robloxianskp.workers.dev';
var MAX_MESSAGES    = 25;
var MAX_CONTEXT_C   = 4000;
var MAX_PAGES       = 5;
var STORAGE_KEY     = 'tl_assistant_msgs';
var SNIPPET_MAX     = 1200;
var CACHE_KEY       = 'tl_snippet_cache';
var PRELOAD_CACHE_TTL = 120000; /* 2 min */
var SESSION_KEY     = 'tl_assistant_session';

/* ---------- State ---------- */
var messages      = [];
var panelOpen     = false;
var isStreaming   = false;
var wasEverOnline = navigator.onLine;
var currentAbort  = null;
var snippetCache  = new Map();
var preloaded     = false;
var sessionOnly   = false;

/* ---------- Site root ---------- */
var SITE_ROOT = (function(){
  var s = document.querySelector('script[src*="assistant.js"]');
  if (!s) return '';
  var p = s.src;
  return p.substring(0, p.lastIndexOf('/assets/'));
})();

function resolveUrl(url) {
  if (!url) return '';
  if (url.indexOf('://') !== -1) return url;
  return SITE_ROOT + (url.charAt(0) === '/' ? url : '/' + url);
}

/* ---------- HTML escaping ---------- */
function esc(str) {
  if (!str) return '';
  return str.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}

/* ---------- Link validation ---------- */
function isValidPageUrl(url) {
  if (!url) return false;
  var path = url.indexOf(SITE_ROOT) === 0 ? url.slice(SITE_ROOT.length) : url;
  if (path.charAt(0) !== '/') path = '/' + path;
  var idx = window.__TL && window.__TL.searchIndex;
  if (!idx) return false;
  for (var i = 0; i < idx.length; i++) {
    if (idx[i].url === path) return true;
  }
  return false;
}

/* ---------- Abort in-flight request ---------- */
function abortCurrentRequest() {
  if (currentAbort) {
    currentAbort.abort();
    currentAbort = null;
  }
}

/* ---------- RAG — improved relevance scoring ---------- */
function findRelevant(query) {
  var index = window.__TL && window.__TL.searchIndex;
  if (!index || !index.length) return [];

  var ql = query.toLowerCase();
  var words = ql.split(/[^a-z0-9]+/).filter(function(w){ return w.length > 1; });
  if (!words.length) return [];

  /* extract quoted phrases */
  var phrases = [];
  var pm = query.match(/"([^"]+)"/g);
  if (pm) {
    for (var pi = 0; pi < pm.length; pi++) {
      phrases.push(pm[pi].replace(/"/g, '').toLowerCase());
    }
  }

  var scored = [];
  for (var i = 0; i < index.length; i++) {
    var item = index[i];
    var title = (item.title || '').toLowerCase();
    var desc  = (item.desc  || '').toLowerCase();
    var cat   = (item.cat   || '').toLowerCase();
    var score = 0;

    /* exact phrase match (highest boost) */
    for (var pi = 0; pi < phrases.length; pi++) {
      if (title.indexOf(phrases[pi]) !== -1) score += 15;
      if (desc.indexOf(phrases[pi])  !== -1) score += 8;
    }

    /* word overlap with frequency */
    for (var j = 0; j < words.length; j++) {
      var w = words[j];
      if (title.indexOf(w) !== -1) {
        score += 3;
        if (title.indexOf(w) < 5) score += 1;
      }
      if (desc.indexOf(w) !== -1) {
        score += 1;
        var dc = desc.split(w).length - 1;
        if (dc > 1) score += Math.min(dc, 3);
      }
    }

    /* category boost */
    for (var j = 0; j < words.length; j++) {
      if (cat.indexOf(words[j]) !== -1) { score += 2; break; }
    }

    if (score > 0) scored.push({ item: item, score: score });
  }

  scored.sort(function(a,b){ return b.score - a.score; });
  return scored.slice(0, MAX_PAGES).map(function(s){ return s.item; });
}

/* ---------- Snippet cache (memory + sessionStorage) ---------- */
function loadSnippetCache() {
  try {
    var raw = sessionStorage.getItem(CACHE_KEY);
    if (raw) {
      var data = JSON.parse(raw);
      var now = Date.now();
      for (var url in data) { if (!data.hasOwnProperty(url)) continue;
        if (now - data[url].ts < PRELOAD_CACHE_TTL) {
          snippetCache.set(url, data[url].text);
        }
      }
    }
  } catch(e) {}
}

function saveSnippetCache() {
  try {
    var obj = {};
    var now = Date.now();
    snippetCache.forEach(function(text, url){
      obj[url] = { text: text, ts: now };
    });
    sessionStorage.setItem(CACHE_KEY, JSON.stringify(obj));
  } catch(e) {
    try {
      snippetCache.clear();
      sessionStorage.removeItem(CACHE_KEY);
    } catch(e2) {}
  }
}

/* ---------- RAG — fetch page content with caching ---------- */
function fetchSnippet(url) {
  if (snippetCache.has(url)) {
    return Promise.resolve(snippetCache.get(url));
  }

  var full = resolveUrl(url);
  var ctrl = new AbortController();
  var tid = setTimeout(function(){ ctrl.abort(); }, 3000);
  return fetch(full, { signal: ctrl.signal })
    .then(function(r){ return r.text(); })
    .then(function(html){
      clearTimeout(tid);
      var m = html.match(/<main[^>]*>([\s\S]*?)<\/main>/i);
      var text = m ? m[1] : '';
      text = text.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
      text = text.substring(0, SNIPPET_MAX);
      snippetCache.set(url, text);
      saveSnippetCache();
      return text;
    })
    .catch(function(){ clearTimeout(tid); return ''; });
}

/* ---------- Preload popular pages (idle callback) ---------- */
function preloadPopularPages() {
  if (preloaded) return;
  preloaded = true;
  var index = window.__TL && window.__TL.searchIndex;
  if (!index || !index.length) return;

  var sorted = index.slice().sort(function(a,b){ return (b.popularity || 0) - (a.popularity || 0); });
  var top = sorted.slice(0, 10);

  var doFetch = function(i){
    if (i >= top.length) return;
    fetchSnippet(top[i].url).then(function(){ doFetch(i+1); });
  };

  if (typeof requestIdleCallback === 'function') {
    requestIdleCallback(function(){ doFetch(0); }, { timeout: 3000 });
  } else {
    setTimeout(function(){ doFetch(0); }, 2000);
  }
}

/* ---------- RAG — build context (parallelized) ---------- */
function buildContext(query, callback) {
  var pages = findRelevant(query);
  var lexicon = window.__TL && window.__TL.lexicon || {};

  var qwords = query.toLowerCase().split(/[^a-z0-9]+/);
  var lexMatches = [];
  for (var term in lexicon) {
    if (lexicon.hasOwnProperty(term)) {
      var tl = term.toLowerCase();
      for (var k = 0; k < qwords.length; k++) {
        if (tl.indexOf(qwords[k]) !== -1 || qwords[k].indexOf(tl) !== -1) {
          lexMatches.push(term + ': ' + lexicon[term]);
          break;
        }
      }
    }
  }

  var fetches = pages.map(function(p){ return fetchSnippet(p.url); });
  Promise.all(fetches).then(function(snippets){
    var parts = [];
    if (pages.length) {
      parts.push('=== RELEVANT PAGES (only use these for links) ===');
      for (var i = 0; i < pages.length; i++) {
        var p = pages[i];
        parts.push('[' + p.title + '](' + p.url + ') — ' + (snippets[i] || p.desc));
      }
    }
    if (lexMatches.length) {
      parts.push('=== LEXICON MATCHES ===');
      parts.push(lexMatches.join('\n'));
    }
    var ctx = parts.join('\n\n');
    if (ctx.length > MAX_CONTEXT_C) ctx = ctx.substring(0, MAX_CONTEXT_C) + '…';
    callback(ctx);
  });
}

/* ---------- Chat persistence ---------- */
function loadHistory() {
  try {
    var raw = localStorage.getItem(STORAGE_KEY);
    if (raw) { messages = JSON.parse(raw); }
  } catch(e) {}
  if (!Array.isArray(messages)) messages = [];
  if (messages.length > MAX_MESSAGES) messages = messages.slice(-MAX_MESSAGES);
}

function saveHistory() {
  if (sessionOnly) return;
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(messages));
  } catch(e) {
    try {
      messages = messages.slice(-10);
      localStorage.setItem(STORAGE_KEY, JSON.stringify(messages));
    } catch(e2) {}
  }
}

function clearHistory() {
  abortCurrentRequest();
  messages = [];
  snippetCache.clear();
  try { sessionStorage.removeItem(SESSION_KEY); } catch(e) {}
  try { sessionStorage.removeItem(CACHE_KEY); } catch(e) {}
  try { sessionStorage.removeItem('tl_assistant_panel_width'); } catch(e) {}
  sessionOnly = false;
  saveHistory();
  renderMessages();
  renderSuggestions();
}

/* ---------- Online / offline ---------- */
function isOnline() {
  return navigator.onLine;
}

function updateOnlineStatus() {
  var fab = document.getElementById('assistant-fab');
  var dot = document.getElementById('assistant-status-dot');
  if (fab) {
    if (isOnline()) {
      fab.classList.remove('offline');
      fab.setAttribute('title', 'Open AI assistant  (Ctrl+Shift+A)');
      wasEverOnline = true;
    } else {
      fab.classList.add('offline');
      fab.setAttribute('title', 'AI assistant unavailable — no internet');
    }
  }
  if (dot) {
    dot.className = 'assistant-status-dot ' + (isOnline() ? 'online' : 'offline');
  }
  if (!isOnline() && panelOpen) {
    showOfflineNotice();
  }
}

function showOfflineNotice() {
  var container = document.getElementById('assistant-msgs');
  if (!container) return;
  var existing = document.getElementById('assistant-offline-notice');
  if (existing) return;
  var notice = document.createElement('div');
  notice.id = 'assistant-offline-notice';
  notice.className = 'assistant-msg ai-msg';
  notice.innerHTML = '<div class="msg-avatar">AI</div><div class="msg-bubble offline-notice"><i class="fas fa-wifi-slash"></i> No internet connection — AI assistant requires internet. Your local search (⌘K) still works.</div>';
  container.appendChild(notice);
  container.scrollTop = container.scrollHeight;
}

/* ---------- System prompt (improved) ---------- */
function systemPrompt(context) {
  return (
    'You are the Tech Library Assistant — a knowledgeable, concise guide for the Tech Library website.\n\n' +
    'SITE SECTIONS:\n' +
    '- tutorials: 190+ tutorials on Windows, Linux, macOS, programming (Python, JS, Rust, Go, C++, SQL), Docker, Kubernetes, Git, networking, security, cloud, audio/video editing, 3D, and more\n' +
    '- survival: emergency digital resources, offline tools, data recovery, security breach response, emergency USB toolkit\n' +
    '- piracy: streaming, downloading, torrenting, gaming, VPN guides\n' +
    '- smt: 100+ Windows command-line tools (SMT multitool)\n' +
    '- lexicon: 240+ tech terms with definitions\n' +
    '- resources: browser extensions, free media alternatives, learning platforms, design tools\n' +
    '- buying-guide: phones, laptops, desktops, tablets, audio, accessories\n\n' +
    'RESPONSE RULES:\n' +
    '- Answer in 2-4 paragraphs. Be direct and informative.\n' +
    '- When linking, ONLY use pages from CURRENT CONTEXT below.\n' +
    '- Format: 📖 [Page Title](/path/to/page.html)\n' +
    '- NEVER invent URLs or page titles.\n' +
    '- If the topic isn\'t in context, just answer from general knowledge without links.\n' +
    '- Be honest if unsure.\n' +
    '- End with 2 follow-up questions the user might ask.\n\n' +
    'EXAMPLE:\n' +
    'User: What is Docker?\n' +
    'Assistant: Docker is a containerization platform that packages applications with their dependencies into isolated "containers."\n' +
    '📖 [Docker Tutorial](/tutorials/docker.html)\n' +
    'Containers share the host OS kernel (unlike VMs). Define them in a Dockerfile; manage multi-container apps with Docker Compose.\n' +
    'Try asking: "How do I write a Dockerfile?" or "What is Docker Compose?"\n\n' +
    'CURRENT CONTEXT (only pages that exist — ALL 📖 links MUST come from here):\n' + (context || '(none)') +
    '\n\nAnswer based on context and general knowledge.'
  );
}

/* ---------- SSE streaming ---------- */
function readSSE(response, onChunk) {
  if (!response.body) { onChunk('', true); return; }
  var reader = response.body.getReader();
  var decoder = new TextDecoder();
  var buffer = '';

  function pump() {
    return reader.read().then(function(result){
      if (result.done) {
        if (buffer.trim()) onChunk(buffer, false);
        onChunk('', true);
        return;
      }
      buffer += decoder.decode(result.value, { stream: true });
      var lines = buffer.split('\n');
      buffer = lines.pop() || '';
      var tokenBatch = '';
      for (var i = 0; i < lines.length; i++) {
        var line = lines[i].trim();
        if (line.startsWith('data: ')) {
          var data = line.slice(6);
          if (data === '[DONE]') continue;
          try {
            var parsed = JSON.parse(data);
            if (parsed.response) tokenBatch += parsed.response;
          } catch(e) {}
        }
      }
      if (tokenBatch) onChunk(tokenBatch, false);
      return pump();
    });
  }
  return pump();
}

/* ---------- Send message with retry ---------- */
function sendMessage(text) {
  if (!text || !text.trim()) return;
  if (!isOnline()) { showOfflineNotice(); return; }
  if (isStreaming) return;

  abortCurrentRequest();

  text = text.trim();

  addMessage('user', text);
  renderMessages();
  saveHistory();

  var input = document.getElementById('assistant-input');
  if (input) { input.value = ''; input.style.height = 'auto'; }

  addMessage('assistant', '');
  var replyIdx = messages.length - 1;
  renderMessages();

  setInputEnabled(false);

  if (!preloaded) { setTimeout(function(){ preloadPopularPages(); }, 100); }

  buildContext(text, function(context){
    var sys = systemPrompt(context);
    var history = messages.slice(0, replyIdx);
    var accumulated = '';
    var retries = 0;
    var maxRetries = 1;

    var ab = new AbortController();
    currentAbort = ab;

    function doFetch() {
      fetch(ASSISTANT_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ system: sys, messages: history }),
        signal: ab.signal
      })
      .then(function(r){
        if (!r.ok) throw new Error('HTTP ' + r.status);
        var ct = r.headers.get('Content-Type') || '';
        if (ct.indexOf('text/event-stream') !== -1) {
          return readSSE(r, function(token, done) {
            if (ab.signal.aborted) return;
            accumulated += token;
            messages[replyIdx].content = accumulated;
            scheduleBubbleUpdate(replyIdx);
            if (done) finalizeReply(replyIdx);
          });
        }
        return r.json().then(function(data){
          if (ab.signal.aborted) return;
          accumulated = data.reply || '';
          messages[replyIdx].content = accumulated;
          updateBubble(replyIdx);
          finalizeReply(replyIdx);
        });
      })
      .catch(function(err){
        if (err.name === 'AbortError') return;
        if (retries < maxRetries && isOnline()) {
          retries++;
          setTimeout(doFetch, 1000);
          return;
        }
        messages[replyIdx].content = "I couldn't reach the AI service right now. Try again or use the search bar (⌘K) to find what you need.";
        updateBubble(replyIdx);
        finalizeReply(replyIdx);
      });
    }

    doFetch();
  });
}

/* ---------- Throttled bubble updates (use rAF) ---------- */
var _pendingBubbleUpdate = null;
function scheduleBubbleUpdate(replyIdx) {
  if (_pendingBubbleUpdate) return;
  _pendingBubbleUpdate = requestAnimationFrame(function(){
    _pendingBubbleUpdate = null;
    updateBubble(replyIdx);
  });
}

function showSearchingIndicator(idx) {
  var container = document.getElementById('assistant-msgs');
  if (!container) return;
  var aiMsgs = container.querySelectorAll('.ai-msg');
  if (aiMsgs.length === 0) return;
  var target = aiMsgs[aiMsgs.length - 1];
  if (!target) return;
  var bubble = target.querySelector('.msg-bubble');
  if (bubble) {
    bubble.innerHTML = '<span class="thinking-dots">Searching library<span>.</span><span>.</span><span>.</span></span>';
  }
}

function setInputEnabled(enabled) {
  var input = document.getElementById('assistant-input');
  var send  = document.getElementById('assistant-send');
  if (input) input.disabled = !enabled;
  if (send) send.disabled = !enabled;
  isStreaming = !enabled;
}

function finalizeReply(msgIdx) {
  var ab = currentAbort;
  currentAbort = null;
  setInputEnabled(true);
  saveHistory();
  messages[msgIdx].ts = Date.now();
  var container = document.getElementById('assistant-msgs');
  if (container) scrollIfNearBottom(container);
  renderFollowUpChips(msgIdx);
  addMsgActions(msgIdx);
}

function addMessage(role, content) {
  messages.push({ role: role, content: content, ts: Date.now() });
  if (messages.length > MAX_MESSAGES) messages.shift();
}

/* ---------- Time ago helper ---------- */
function timeAgo(ts) {
  if (!ts) return '';
  var diff = Date.now() - ts;
  if (diff < 10000) return 'just now';
  if (diff < 60000) return Math.floor(diff / 1000) + 's ago';
  if (diff < 3600000) return Math.floor(diff / 60000) + 'm ago';
  if (diff < 86400000) return Math.floor(diff / 3600000) + 'h ago';
  return Math.floor(diff / 86400000) + 'd ago';
}

/* ---------- Add / update message actions ---------- */
function addMsgActions(msgIdx) {
  var container = document.getElementById('assistant-msgs');
  if (!container) return;
  var msgEl = container.querySelector('.assistant-msg.ai-msg[data-idx="' + msgIdx + '"]');
  if (!msgEl) return;
  var actions = msgEl.querySelector('.assistant-msg-actions');
  if (!actions || !messages[msgIdx]) return;

  var m = messages[msgIdx];
  var ts = m.ts ? timeAgo(m.ts) : '';
  var isLast = true;
  for (var j = messages.length - 1; j >= 0; j--) {
    if (messages[j].role === 'assistant' && messages[j].content) {
      isLast = (msgIdx === j);
      break;
    }
  }

  actions.innerHTML = ''
    + '<span class="assistant-msg-time">' + ts + '</span>'
    + (m.content ? '<button class="assistant-copy-btn" title="Copy response"><i class="fas fa-copy"></i></button>' : '')
    + (isLast && m.content ? '<button class="assistant-regenerate-btn" title="Regenerate"><i class="fas fa-redo"></i></button>' : '');
}

/* ---------- Format AI response ---------- */
function formatResponse(text) {
  if (!text) return '';

  text = esc(text);

  text = text.replace(/```(\w*)\n([\s\S]*?)```/g, function(m, lang, code) {
    return '<div class="ai-code-block"><span class="ai-code-lang">' + esc(lang || 'code') + '</span><pre><code>' + code + '</code></pre></div>';
  });

  text = text.replace(/`([^`]+)`/g, '<code>$1</code>');

  text = text.replace(/^### (.+)$/gm, '<h4 class="ai-h4">$1</h4>');
  text = text.replace(/^#### (.+)$/gm, '<h5 class="ai-h5">$1</h5>');

  text = text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  text = text.replace(/\*(.+?)\*/g, '<em>$1</em>');

  text = text.replace(/📖\s*\[([^\]]+)\]\(([^)]+)\)/g, function(m, title, url) {
    if (isValidPageUrl(url)) {
      return '<a href="' + esc(url) + '" class="assistant-link">📖 ' + title + '</a>';
    }
    return title;
  });

  text = text.replace(/(\b(https?|ftp):\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noopener">$1</a>');

  text = text.replace(/^\d+\.\s(.+)$/gm, '<li class="ai-li">$1</li>');
  text = text.replace(/(<li class="ai-li">.*<\/li>\n?)+/g, '<ol class="ai-ol">$&</ol>');

  text = text.replace(/(?:^[-*]\s(.+)$\n?)+/gm, function(m) {
    var items = m.split('\n').filter(function(l){ return l.trim(); }).map(function(l){
      return '<li class="ai-li">' + l.replace(/^[-*]\s+/, '') + '</li>';
    }).join('');
    return '<ul class="ai-ul">' + items + '</ul>';
  });

  text = text.replace(/^>\s(.+)$/gm, '<blockquote class="ai-blockquote">$1</blockquote>');

  text = text.replace(/^(\|.+\|)\n\|[-| :]+\|\n((?:\|.+\|\n?)*)/gm, function(m, headerRow, bodyRows) {
    var cells = headerRow.split('|').filter(function(c){ return c.trim(); });
    var thead = '<thead><tr>' + cells.map(function(c){ return '<th>' + c.trim() + '</th>'; }).join('') + '</tr></thead>';
    var rows = bodyRows.trim().split('\n');
    var tbody = '<tbody>' + rows.map(function(row){
      return '<tr>' + row.split('|').filter(function(c){ return c.trim(); }).map(function(c){ return '<td>' + c.trim() + '</td>'; }).join('') + '</tr>';
    }).join('') + '</tbody>';
    return '<table class="ai-table">' + thead + tbody + '</table>';
  });

  text = text.replace(/\n/g, '<br>');
  text = text.replace(/📖/g, '');

  return text;
}

/* ---------- Render messages ---------- */
function renderMessages() {
  var container = document.getElementById('assistant-msgs');
  if (!container) return;

  var lastAiMsgIdx = -1;
  for (var j = messages.length - 1; j >= 0; j--) {
    if (messages[j].role === 'assistant' && messages[j].content) {
      lastAiMsgIdx = j;
      break;
    }
  }

  var html = '';
  for (var i = 0; i < messages.length; i++) {
    var m = messages[i];
    if (m.role === 'system') continue;
    if (m.role === 'user') {
      html += '<div class="assistant-msg user-msg"><div class="msg-bubble">' + esc(m.content) + '</div></div>';
    } else {
      var ts = m.ts ? timeAgo(m.ts) : '';
      var isLastAi = !isStreaming && m.role === 'assistant' && m.content && i === lastAiMsgIdx;
      html += '<div class="assistant-msg ai-msg msg-animate" data-idx="' + i + '">'
        + '<div class="msg-avatar">AI</div>'
        + '<div><div class="msg-bubble">' + formatResponse(m.content) + '</div>'
        + '<div class="assistant-msg-actions">'
        + '<span class="assistant-msg-time">' + ts + '</span>'
        + (m.content ? '<button class="assistant-copy-btn" title="Copy response"><i class="fas fa-copy"></i></button>' : '')
        + (isLastAi ? '<button class="assistant-regenerate-btn" title="Regenerate"><i class="fas fa-redo"></i></button>' : '')
        + '</div></div></div>';
    }
  }

  container.innerHTML = html;
  if (container) scrollIfNearBottom(container);
}

function scrollIfNearBottom(el) {
  if (!el) return;
  var atBottom = el.scrollHeight - el.scrollTop - el.clientHeight < 60;
  if (atBottom) el.scrollTop = el.scrollHeight;
}

function updateBubble(msgIdx) {
  if (!messages[msgIdx]) return;
  var container = document.getElementById('assistant-msgs');
  if (!container) return;
  var msgEl = container.querySelector('.assistant-msg.ai-msg[data-idx="' + msgIdx + '"]');
  if (!msgEl) return;
  var bubble = msgEl.querySelector('.msg-bubble');
  if (bubble) {
    bubble.innerHTML = formatResponse(messages[msgIdx].content) || '<span class="stream-cursor">|</span>';
  }
  scrollIfNearBottom(container);
}

/* ---------- Dynamic follow-up chips ---------- */
function renderFollowUpChips(msgIdx) {
  var container = document.getElementById('assistant-msgs');
  if (!container) return;

  var existing = container.querySelector('.follow-up-row');
  if (existing) existing.remove();

  var chips = generateFollowUps(messages[msgIdx] && messages[msgIdx].content || '');
  if (!chips.length) return;

  var div = document.createElement('div');
  div.className = 'follow-up-row';
  div.innerHTML = '<span class="follow-up-label">Ask a follow-up:</span> ' +
    chips.map(function(q){ return '<button class="assistant-chip follow-up-chip" data-q="' + esc(q) + '">' + esc(q) + '</button>'; }).join('');
  container.appendChild(div);
  scrollIfNearBottom(container);
}

function generateFollowUps(reply) {
  var lower = reply.toLowerCase();

  var extracted = [];
  var qm = reply.match(/(?:Ask|Try|Consider|Here are|Questions?|Try asking)[:.]?\s*(?:"([^"]+)"|'([^']+)'|([^.!?]+[?]))/gi);
  if (qm) {
    for (var i = 0; i < qm.length && extracted.length < 3; i++) {
      var q = qm[i].replace(/^(?:Ask|Try|Consider|Here are|Questions?|Try asking)[:.']?\s*/i, '').replace(/^["']|["']$/g, '').trim();
      if (q && q.length > 5 && q.length < 100 && extracted.indexOf(q) === -1) {
        extracted.push(q);
      }
    }
  }

  if (extracted.length >= 2) return extracted.slice(0, 3);

  var sets = {
    'linux': ['How do I install software on Linux?', 'What is the Linux filesystem structure?'],
    'docker': ['How do I write a Dockerfile?', 'What is Docker Compose?'],
    'kubernetes': ['How do I deploy a pod?', 'What is a Kubernetes service?'],
    'k8s': ['How do I deploy a pod?', 'What is a Kubernetes service?'],
    'git': ['How do I undo a commit?', 'What is a merge conflict?'],
    'python': ['How do I install Python packages?', 'What are Python virtual environments?'],
    'windows': ['How do I debloat Windows?', 'What are essential Windows tools?'],
    'network': ['How do I troubleshoot network issues?', 'What is the OSI model?'],
    'security': ['How do I secure my home network?', 'What is two-factor authentication?'],
    'vpn': ['What is the difference between VPN and proxy?', 'How do I set up WireGuard?'],
    'javascript': ['What are JavaScript promises?', 'How do I use async/await?'],
    'js': ['What are JavaScript promises?', 'How do I use async/await?'],
    'ssh': ['How do I set up SSH keys?', 'What is SSH tunneling?'],
    'encrypt': ['What is encryption?', 'How do I use GPG?'],
    'terminal': ['What are essential terminal commands?', 'How do I use grep?'],
    'wsl': ['How do I set up WSL2?', 'What is the difference between WSL1 and WSL2?'],
    'nginx': ['How do I configure a reverse proxy?', 'How do I enable HTTPS on Nginx?'],
    'terraform': ['What is infrastructure as code?', 'How do I write Terraform configs?'],
    'ansible': ['What is Ansible?', 'How do I write an Ansible playbook?'],
    'rust': ['How do I start with Rust?', 'What is ownership in Rust?'],
    'go': ['How do I start with Go?', 'What are goroutines?'],
    'sql': ['How do I write SQL queries?', 'What are JOINs in SQL?'],
    'aws': ['What are core AWS services?', 'How do I set up an EC2 instance?'],
    'gcp': ['What are core GCP services?', 'How does GCP compare to AWS?'],
    'azure': ['What are core Azure services?', 'How does Azure compare to AWS?'],
    'blender': ['How do I model in Blender?', 'How do I render in Blender?'],
    'resolve': ['How do I edit video in DaVinci Resolve?', 'How do I color grade?'],
    'obsidian': ['How do I set up Obsidian?', 'What is a Zettelkasten?'],
    'anki': ['How do I use Anki effectively?', 'What are Anki card types?']
  };

  var matched = [];
  var lwords = lower.split(/[^a-z0-9]+/).filter(function(w){ return w.length > 1; });
  for (var key in sets) {
    if (lwords.indexOf(key) !== -1) {
      matched = sets[key];
      break;
    }
  }
  if (matched.length) return matched;

  if (extracted.length === 1) {
    return [extracted[0], 'What else can I learn here?'];
  }

  return ['What else can I learn here?', 'Show me popular tutorials'];
}

/* ---------- Suggested questions (initial, page-aware) ---------- */
function pageSuggestions() {
  var path = window.location.pathname.split('?')[0];

  if (path.indexOf('/tutorials/') !== -1) {
    return ['How do I start with Linux?', 'What is the best Docker tutorial?', 'Show me VS Code tips', 'How do I set up Git?'];
  }
  if (path.indexOf('/lexicon/') !== -1) {
    return ['What does API mean?', 'Explain common networking terms', 'What is the difference between HTTP and HTTPS?', 'Search programming terms'];
  }
  if (path.indexOf('/survival/') !== -1) {
    return ['What should I put on an emergency USB?', 'How do I recover lost data?', 'How do I respond to a security breach?', 'What are essential offline tools?'];
  }
  if (path.indexOf('/piracy/') !== -1) {
    return ['How do I stay safe torrenting?', 'What are the best streaming sites?', 'How do I use a VPN?', 'What is Usenet?'];
  }
  if (path.indexOf('/buying-guide/') !== -1) {
    return ['What budget laptop should I get?', 'Best headphones under $100?', 'What phone has the best camera?', 'How do I choose a monitor?'];
  }
  if (path.indexOf('/resources/') !== -1) {
    return ['What are the best browser extensions?', 'Show me free media alternatives', 'What learning platforms are recommended?', 'Best design tools?'];
  }
  if (path.indexOf('/smt/') !== -1) {
    return ['What is SMT?', 'Show me the best Windows CLI tools', 'How do I use IP geolocation tools?'];
  }

  return [
    'What tutorials are available?',
    'How do I use the search?',
    'Show me survival resources',
    'What is the Tech Library?'
  ];
}

function renderSuggestions() {
  var container = document.getElementById('assistant-msgs');
  if (!container) return;

  var chips = pageSuggestions();
  var html = '<div class="assistant-msg ai-msg"><div class="msg-avatar">AI</div><div class="msg-bubble welcome-text">' +
    '<strong>Hi! I can help you find tutorials, explain tech terms, and guide you to the right resources.</strong>' +
    '<br><span class="welcome-hint">Pick a question below or type your own.  (Ctrl+Shift+A)</span></div></div>';
  if (!isOnline()) {
    html += '<div class="assistant-msg ai-msg"><div class="msg-bubble offline-notice"><i class="fas fa-wifi-slash"></i> No internet — AI is unavailable. Your local search (⌘K) still works.</div></div>';
  }
  html += '<div class="assistant-chips">';
  for (var i = 0; i < chips.length; i++) {
    html += '<button class="assistant-chip" data-q="' + esc(chips[i]) + '">' + esc(chips[i]) + '</button>';
  }
  html += '</div>';
  container.innerHTML = html;
}

/* ---------- Scroll-to-bottom button ---------- */
function createScrollBottomBtn() {
  var btn = document.createElement('button');
  btn.id = 'assistant-scroll-bottom';
  btn.className = 'assistant-scroll-bottom';
  btn.innerHTML = '<i class="fas fa-chevron-down"></i>';
  btn.setAttribute('aria-label', 'Scroll to bottom');
  btn.style.display = 'none';
  document.getElementById('assistant-panel').appendChild(btn);

  var msgs = document.getElementById('assistant-msgs');
  msgs.addEventListener('scroll', function(){
    var atBottom = msgs.scrollHeight - msgs.scrollTop - msgs.clientHeight < 60;
    btn.style.display = atBottom ? 'none' : 'flex';
  });

  btn.addEventListener('click', function(){
    msgs.scrollTop = msgs.scrollHeight;
    btn.style.display = 'none';
  });
}

/* ---------- Copy handler ---------- */
function handleCopyClick(btn) {
  var msgEl = btn.closest('.assistant-msg');
  if (!msgEl) return;
  var bubble = msgEl.querySelector('.msg-bubble');
  if (!bubble) return;
  var text = bubble.textContent || bubble.innerText || '';
  if (!text) return;
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(function(){
      showCopiedToast(btn);
    }).catch(function(){
      fallbackCopy(text, btn);
    });
  } else {
    fallbackCopy(text, btn);
  }
}

function fallbackCopy(text, btn) {
  var ta = document.createElement('textarea');
  ta.value = text;
  ta.style.position = 'fixed'; ta.style.left = '-9999px';
  document.body.appendChild(ta);
  ta.select();
  try { document.execCommand('copy'); showCopiedToast(btn); } catch(e) {}
  document.body.removeChild(ta);
}

function showCopiedToast(btn) {
  var orig = btn.innerHTML;
  btn.innerHTML = '<span style="font-size:0.7rem;">Copied!</span>';
  btn.disabled = true;
  setTimeout(function(){
    btn.innerHTML = orig;
    btn.disabled = false;
  }, 1500);
}

/* ---------- Regenerate handler ---------- */
function handleRegenerateClick() {
  if (isStreaming) return;
  var lastUser = '';
  for (var i = messages.length - 1; i >= 0; i--) {
    if (messages[i].role === 'user') {
      lastUser = messages[i].content;
      break;
    }
  }
  if (!lastUser) return;
  /* trim back to before the last assistant reply */
  for (var i = messages.length - 1; i >= 1; i -= 2) {
    if (i > 0 && messages[i].role === 'assistant' && messages[i-1].role === 'user' && messages[i-1].content === lastUser) {
      messages.pop();
      messages.pop();
      break;
    }
  }
  renderMessages();
  sendMessage(lastUser);
}

/* ---------- Resize handle ---------- */
function initResizeHandle() {
  var handle = document.getElementById('assistant-resize-handle');
  var panel = document.getElementById('assistant-panel');
  if (!handle || !panel) return;

  var startX, startW;
  handle.addEventListener('mousedown', function(e) {
    e.preventDefault();
    startX = e.clientX;
    startW = panel.offsetWidth;
    document.addEventListener('mousemove', onMove);
    document.addEventListener('mouseup', onUp);
  });

  function onMove(e) {
    var w = startW - (e.clientX - startX);
    if (w < 300) w = 300;
    if (w > 800) w = 800;
    panel.style.width = w + 'px';
  }

  function onUp() {
    document.removeEventListener('mousemove', onMove);
    document.removeEventListener('mouseup', onUp);
    try { localStorage.setItem('tl_assistant_panel_width', panel.style.width); } catch(e) {}
  }
}

/* ---------- Session mode toggle ---------- */
function toggleSessionMode() {
  sessionOnly = !sessionOnly;
  try {
    if (sessionOnly) {
      sessionStorage.setItem(SESSION_KEY, '1');
    } else {
      sessionStorage.removeItem(SESSION_KEY);
    }
  } catch(e) {}
  updateSessionBadge();
}

function updateSessionBadge() {
  var badge = document.getElementById('assistant-session-badge');
  if (!badge) return;
  if (sessionOnly) {
    badge.style.display = 'inline-flex';
  } else {
    badge.style.display = 'none';
  }
}

/* ---------- Privacy popup ---------- */
function showPrivacyPopup() {
  var existing = document.getElementById('assistant-privacy-popup');
  if (existing) { existing.remove(); return; }

  var overlay = document.createElement('div');
  overlay.id = 'assistant-privacy-popup';
  overlay.className = 'assistant-privacy-popup';
  overlay.innerHTML =
    '<div class="assistant-privacy-content">' +
      '<button class="assistant-privacy-close" id="assistant-privacy-close">&times;</button>' +
      '<h3><i class="fas fa-shield-alt"></i> Privacy & Data</h3>' +
      '<div class="assistant-privacy-section">' +
        '<h4>What we store</h4>' +
        '<p>Your conversations are saved in <code>localStorage</code> on this device. No data is sent to third parties — only to the AI worker endpoint to generate responses.</p>' +
      '</div>' +
      '<div class="assistant-privacy-section">' +
        '<h4>Session-Only Mode</h4>' +
        '<p>Enable <strong>session-only mode</strong> to skip all local storage. Messages persist only while the panel is open and disappear when you close it.</p>' +
      '</div>' +
      '<div class="assistant-privacy-section">' +
        '<h4>Clear All Data</h4>' +
        '<p>Use the <i class="fas fa-trash-alt"></i> button in the header to delete all stored messages, cached snippets, and preferences.</p>' +
      '</div>' +
      '<p class="assistant-privacy-footer">No tracking, no analytics, no cookies. Your data stays on your device.</p>' +
    '</div>';
  document.getElementById('assistant-panel').appendChild(overlay);

  document.getElementById('assistant-privacy-close').addEventListener('click', function(){ overlay.remove(); });
  overlay.addEventListener('click', function(e){ if (e.target === overlay) overlay.remove(); });
}

/* ---------- Keyboard shortcuts modal ---------- */
function showShortcutsModal() {
  var existing = document.getElementById('assistant-shortcuts-overlay');
  if (existing) { existing.remove(); return; }

  var overlay = document.createElement('div');
  overlay.id = 'assistant-shortcuts-overlay';
  overlay.className = 'assistant-shortcuts-overlay';
  overlay.innerHTML =
    '<div class="assistant-shortcuts-content">' +
      '<button class="assistant-shortcuts-close" id="assistant-shortcuts-close">&times;</button>' +
      '<h3><i class="fas fa-keyboard"></i> Keyboard Shortcuts</h3>' +
      '<div class="assistant-shortcuts-grid">' +
        '<div><span class="kbd">Enter</span></div><div>Send message</div>' +
        '<div><span class="kbd">Shift</span> + <span class="kbd">Enter</span></div><div>New line</div>' +
        '<div><span class="kbd">Ctrl</span> + <span class="kbd">Shift</span> + <span class="kbd">A</span></div><div>Toggle assistant panel</div>' +
        '<div><span class="kbd">Esc</span></div><div>Close panel</div>' +
        '<div><span class="kbd">?</span></div><div>Show this help</div>' +
      '</div>' +
      '<p class="assistant-shortcuts-footer">Press <span class="kbd">?</span> at any time to reopen this help.</p>' +
    '</div>';
  document.getElementById('assistant-panel').appendChild(overlay);

  document.getElementById('assistant-shortcuts-close').addEventListener('click', function(){ overlay.remove(); });
  overlay.addEventListener('click', function(e){ if (e.target === overlay) overlay.remove(); });
}

/* ---------- Create UI ---------- */
function createUI() {
  if (document.getElementById('assistant-fab')) return;

  var fab = document.createElement('button');
  fab.id = 'assistant-fab';
  fab.className = 'assistant-fab' + (isOnline() ? '' : ' offline');
  fab.innerHTML = '<i class="fas fa-robot"></i>';
  fab.setAttribute('aria-label', 'Open AI assistant');
  fab.setAttribute('title', isOnline() ? 'Open AI assistant  (Ctrl+Shift+A)' : 'AI assistant unavailable — no internet');
  document.body.appendChild(fab);

  var panel = document.createElement('div');
  panel.id = 'assistant-panel';
  panel.className = 'assistant-panel';
  panel.innerHTML =
    '<div class="assistant-resize-handle" id="assistant-resize-handle"></div>' +
    '<div class="assistant-header">' +
      '<span><i class="fas fa-robot"></i> Tech Library Assistant<span id="assistant-session-badge" class="session-badge" title="Session-only mode active" style="display:none;"><i class="fas fa-lock"></i></span></span>' +
      '<span class="assistant-header-right">' +
        '<span id="assistant-status-dot" class="assistant-status-dot ' + (isOnline() ? 'online' : 'offline') + '" title="' + (isOnline() ? 'Connected' : 'Offline') + '"></span>' +
        '<button id="assistant-shortcuts-btn" class="assistant-header-btn" title="Keyboard shortcuts"><i class="fas fa-question-circle"></i></button>' +
        '<button id="assistant-privacy-btn" class="assistant-header-btn" title="Privacy info"><i class="fas fa-shield-alt"></i></button>' +
        '<button id="assistant-settings-btn" class="assistant-header-btn" title="Settings"><i class="fas fa-cog"></i></button>' +
        '<button id="assistant-clear" class="assistant-clear-btn" title="Clear conversation"><i class="fas fa-trash-alt"></i></button>' +
        '<button id="assistant-close" class="assistant-close" aria-label="Close assistant">&times;</button>' +
      '</span>' +
    '</div>' +
    '<div class="assistant-settings-dropdown" id="assistant-settings-dropdown" style="display:none;">' +
      '<label class="assistant-settings-item"><input type="checkbox" id="assistant-session-toggle"> Session-only mode (no localStorage)</label>' +
    '</div>' +
    '<div class="assistant-msgs" id="assistant-msgs"></div>' +
    '<div class="assistant-input-area">' +
      '<textarea id="assistant-input" class="assistant-input" rows="1" placeholder="Ask about tutorials, terms, resources…" aria-label="Message"></textarea>' +
      '<button id="assistant-send" class="assistant-send" aria-label="Send"><i class="fas fa-paper-plane"></i></button>' +
    '</div>';
  document.body.appendChild(panel);

  fab.addEventListener('click', function(){
    if (!isOnline()) { showOfflineNotice(); }
    togglePanel();
  });

  document.getElementById('assistant-close').addEventListener('click', closePanel);

  var clearBtn = document.getElementById('assistant-clear');
  if (clearBtn) {
    clearBtn.addEventListener('click', function(){
      if (messages.length > 0 && confirm('Clear conversation?')) {
        clearHistory();
        renderSuggestions();
      }
    });
  }

  /* Settings dropdown */
  var settingsBtn = document.getElementById('assistant-settings-btn');
  var settingsDropdown = document.getElementById('assistant-settings-dropdown');
  if (settingsBtn && settingsDropdown) {
    settingsBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      var d = settingsDropdown.style.display;
      settingsDropdown.style.display = d === 'block' ? 'none' : 'block';
    });
    document.addEventListener('click', function() {
      settingsDropdown.style.display = 'none';
    });
    settingsDropdown.addEventListener('click', function(e) { e.stopPropagation(); });
    var sessionToggle = document.getElementById('assistant-session-toggle');
    if (sessionToggle) {
      sessionToggle.checked = sessionOnly;
      sessionToggle.addEventListener('change', function() {
        toggleSessionMode();
      });
    }
  }

  /* Privacy button */
  var privacyBtn = document.getElementById('assistant-privacy-btn');
  if (privacyBtn) {
    privacyBtn.addEventListener('click', showPrivacyPopup);
  }

  /* Shortcuts button */
  var shortcutsBtn = document.getElementById('assistant-shortcuts-btn');
  if (shortcutsBtn) {
    shortcutsBtn.addEventListener('click', showShortcutsModal);
  }

  var sendBtn = document.getElementById('assistant-send');
  var inputEl = document.getElementById('assistant-input');

  sendBtn.addEventListener('click', function(){ sendMessage(inputEl.value); });

  inputEl.addEventListener('keydown', function(e){
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage(inputEl.value);
    }
  });

  inputEl.addEventListener('input', function(){
    var el = this;
    el.style.height = 'auto';
    el.style.height = Math.min(el.scrollHeight, 120) + 'px';
  });

  panel.addEventListener('click', function(e){
    var chip = e.target.closest('.assistant-chip');
    if (chip && chip.getAttribute('data-q')) {
      sendMessage(chip.getAttribute('data-q'));
      return;
    }
    var copyBtn = e.target.closest('.assistant-copy-btn');
    if (copyBtn) {
      handleCopyClick(copyBtn);
      return;
    }
    var regenBtn = e.target.closest('.assistant-regenerate-btn');
    if (regenBtn) {
      handleRegenerateClick();
      return;
    }
  });

  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && panelOpen) closePanel();
  });

  document.addEventListener('keydown', function(e){
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === 'a' || e.key === 'A')) {
      e.preventDefault();
      togglePanel();
    }
  });

  document.addEventListener('keydown', function(e){
    if (e.key === '?' && !e.ctrlKey && !e.metaKey && !e.altKey) {
      var active = document.activeElement;
      if (active && active.tagName === 'INPUT') return;
      if (active && active.tagName === 'TEXTAREA') return;
      if (panelOpen) showShortcutsModal();
    }
  });

  window.addEventListener('online', updateOnlineStatus);
  window.addEventListener('offline', updateOnlineStatus);

  createScrollBottomBtn();
  initResizeHandle();
}

/* ---------- Panel controls ---------- */
function togglePanel() {
  if (panelOpen) closePanel();
  else openPanel();
}

function openPanel() {
  panelOpen = true;
  var panel = document.getElementById('assistant-panel');
  var fab  = document.getElementById('assistant-fab');
  if (panel) {
    panel.classList.add('open');
    var savedW = localStorage.getItem('tl_assistant_panel_width');
    if (savedW) panel.style.width = savedW;
  }
  if (fab) fab.classList.add('hidden');
  if (!isOnline()) showOfflineNotice();
  if (sessionOnly && messages.length === 0) {
    renderSuggestions();
  }
  setTimeout(function(){
    var inp = document.getElementById('assistant-input');
    if (inp) inp.focus();
  }, 350);
}

function closePanel() {
  abortCurrentRequest();
  panelOpen = false;
  var panel = document.getElementById('assistant-panel');
  var fab  = document.getElementById('assistant-fab');
  if (panel) panel.classList.remove('open');
  if (fab) fab.classList.remove('hidden');
  if (sessionOnly && messages.length > 0) {
    clearHistory();
  }
}

/* ---------- Init ---------- */
function init() {
  /* load session-only preference */
  try {
    if (sessionStorage.getItem(SESSION_KEY)) sessionOnly = true;
  } catch(e) {}
  createUI();
  if (!sessionOnly) loadHistory();
  loadSnippetCache();
  updateOnlineStatus();
  updateSessionBadge();
  if (messages.length === 0) {
    renderSuggestions();
  } else {
    renderMessages();
    if (!isOnline()) showOfflineNotice();
  }
  preloadPopularPages();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}

} catch(e) { /* fail silently */ }
})();
