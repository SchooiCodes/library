/* ===== Tech Library AI Assistant ===== */
(function(){
try {

/* ---------- Config ---------- */
var ASSISTANT_ENDPOINT = 'https://tech-library-ai.robloxianskp.workers.dev';
var MAX_MESSAGES    = 30;
var MAX_CONTEXT_C   = 2500;
var MAX_PAGES       = 5;
var STORAGE_KEY     = 'tl_assistant_msgs';

/* ---------- State ---------- */
var messages  = [];
var panelOpen = false;
var isStreaming = false;
var wasEverOnline = navigator.onLine;

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

/* ---------- RAG — find relevant pages ---------- */
function findRelevant(query) {
  var index = window.__TL && window.__TL.searchIndex;
  if (!index || !index.length) return [];

  var words = query.toLowerCase().split(/[^a-z0-9]+/).filter(function(w){ return w.length > 2; });
  if (!words.length) return [];

  var scored = [];
  for (var i = 0; i < index.length; i++) {
    var item = index[i];
    var title = (item.title || '').toLowerCase();
    var desc  = (item.desc  || '').toLowerCase();
    var score = 0;
    for (var j = 0; j < words.length; j++) {
      var w = words[j];
      if (title.indexOf(w) !== -1) score += 3;
      if (desc.indexOf(w)  !== -1) score += 1;
    }
    if (score > 0) scored.push({ item: item, score: score });
  }

  scored.sort(function(a,b){ return b.score - a.score; });
  return scored.slice(0, MAX_PAGES).map(function(s){ return s.item; });
}

/* ---------- RAG — fetch page content ---------- */
function fetchSnippet(url) {
  var full = resolveUrl(url);
  return fetch(full, { signal: AbortSignal.timeout ? AbortSignal.timeout(3000) : undefined })
    .then(function(r){ return r.text(); })
    .then(function(html){
      var m = html.match(/<main[^>]*>([\s\S]*?)<\/main>/i);
      var text = m ? m[1] : '';
      text = text.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
      return text.substring(0, 300);
    })
    .catch(function(){ return ''; });
}

/* ---------- RAG — build context ---------- */
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
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(messages));
  } catch(e) {}
}

function clearHistory() {
  messages = [];
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
      fab.setAttribute('title', 'Open AI assistant');
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

/* ---------- System prompt ---------- */
function systemPrompt(context) {
  return (
    'You are the Tech Library Assistant. The Tech Library is a free collection of ' +
    'tutorials, a tech lexicon, resources, and survival guides.\n\n' +
    'SITE SECTIONS:\n' +
    '- tutorials: Windows, Linux, programming, networking, Docker, Git, VS Code, and more\n' +
    '- survival: emergency digital resources, offline tools, data recovery, security breach response\n' +
    '- piracy: streaming, downloading, torrenting, gaming resources\n' +
    '- smt: 100+ Windows command-line tools\n' +
    '- lexicon: 240+ tech terms with definitions\n' +
    '- resources: browser extensions, free media alternatives, learning platforms\n' +
    '- buying-guide: phones, laptops, desktops, tablets, audio, accessories\n\n' +
    'Always respond concisely (2-4 paragraphs).\n' +
    'When linking to a resource, ONLY use pages listed in CURRENT CONTEXT below.\n' +
    'Use this exact format: 📖 [Page Title](/path/to/page.html)\n' +
    'Keep links as relative paths (starting with /).\n' +
    'NEVER invent page titles or URLs. If a topic is not in CURRENT CONTEXT, mention it without the 📖 icon.\n' +
    'If you are unsure about something, say so honestly.\n' +
    'At the end, suggest 2 follow-up questions the user might want to ask.\n\n' +
    'CURRENT CONTEXT (only these pages exist — do not make up others):\n' + (context || '(none)') +
    '\n\nAnswer the user based on the above context and your general knowledge.'
  );
}

/* ---------- Streaming API call ---------- */
function streamReply(msgIdx) {
  var history = messages.slice(0, msgIdx);
  var sys = systemPrompt('');
  var accumulated = '';

  fetch(ASSISTANT_ENDPOINT, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ system: sys, messages: history })
  })
  .then(function(r){
    if (!r.ok) throw new Error('HTTP ' + r.status);
    var ct = r.headers.get('Content-Type') || '';
    if (ct.indexOf('text/event-stream') !== -1) {
      return readSSE(r, function(token, done) {
        accumulated += token;
        messages[msgIdx].content = accumulated;
        updateBubble(msgIdx);
        if (done) finalizeReply(msgIdx);
      });
    }
    /* fallback: non-streaming JSON */
    return r.json().then(function(data){
      accumulated = data.reply || '';
      messages[msgIdx].content = accumulated;
      updateBubble(msgIdx);
      finalizeReply(msgIdx);
    });
  })
  .catch(function(err){
    messages[msgIdx].content = "I couldn't reach the AI service right now. Try again or use search (⌘K) to find what you need.";
    updateBubble(msgIdx);
    finalizeReply(msgIdx);
  });
}

function readSSE(response, onChunk) {
  var reader = response.body.getReader();
  var decoder = new TextDecoder();
  var buffer = '';

  function pump() {
    return reader.read().then(function(result){
      if (result.done) {
        onChunk('', true);
        return;
      }

      buffer += decoder.decode(result.value, { stream: true });
      var lines = buffer.split('\n');
      buffer = lines.pop() || '';

      for (var i = 0; i < lines.length; i++) {
        var line = lines[i].trim();
        if (line.startsWith('data: ')) {
          var data = line.slice(6);
          if (data === '[DONE]') continue;
          try {
            var parsed = JSON.parse(data);
            if (parsed.response) {
              onChunk(parsed.response, false);
            }
          } catch(e) {}
        }
      }

      return pump();
    });
  }

  return pump();
}

/* ---------- Send message (with RAG context) ---------- */
function sendMessage(text) {
  if (!text || !text.trim()) return;
  if (!isOnline()) { showOfflineNotice(); return; }
  if (isStreaming) return;

  text = text.trim();

  addMessage('user', text);
  renderMessages();
  saveHistory();

  var input = document.getElementById('assistant-input');
  if (input) { input.value = ''; input.style.height = 'auto'; }
  setInputEnabled(false);

  /* Reserve slot for AI reply (empty, will be streamed in) */
  var replyIdx = messages.length;
  addMessage('assistant', '');

  buildContext(text, function(context){
    /* Rebuild system prompt with the real context */
    var sys = systemPrompt(context);
    var history = messages.slice(0, replyIdx);
    var accumulated = '';

    fetch(ASSISTANT_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ system: sys, messages: history })
    })
    .then(function(r){
      if (!r.ok) throw new Error('HTTP ' + r.status);
      var ct = r.headers.get('Content-Type') || '';
      if (ct.indexOf('text/event-stream') !== -1) {
        return readSSE(r, function(token, done) {
          accumulated += token;
          messages[replyIdx].content = accumulated;
          updateBubble(replyIdx);
          if (done) finalizeReply(replyIdx);
        });
      }
      return r.json().then(function(data){
        accumulated = data.reply || '';
        messages[replyIdx].content = accumulated;
        updateBubble(replyIdx);
        finalizeReply(replyIdx);
      });
    })
    .catch(function(err){
      messages[replyIdx].content = "I couldn't reach the AI service right now. Try again or use search (⌘K) to find what you need.";
      updateBubble(replyIdx);
      finalizeReply(replyIdx);
    });
  });
}

function setInputEnabled(enabled) {
  var input = document.getElementById('assistant-input');
  var send  = document.getElementById('assistant-send');
  if (input) input.disabled = !enabled;
  if (send) send.disabled = !enabled;
  isStreaming = !enabled;
}

function finalizeReply(msgIdx) {
  setInputEnabled(true);
  saveHistory();
  messages[msgIdx].ts = Date.now();
  var container = document.getElementById('assistant-msgs');
  if (container) container.scrollTop = container.scrollHeight;
  renderFollowUpChips(msgIdx);
}

function addMessage(role, content) {
  messages.push({ role: role, content: content, ts: Date.now() });
  if (messages.length > MAX_MESSAGES + 1) messages.shift();
}

/* ---------- Format AI response (richer markdown) ---------- */
function formatResponse(text) {
  if (!text) return '';

  text = esc(text);

  /* Strip orphaned 📖 references without URLs */
  text = text.replace(/📖\s+([^\n<\].[]+?)(?:\s|$|<br>)/g, function(m, t) {
    return t.trim() + ' ';
  });

  /* Code blocks (must come before inline code) */
  text = text.replace(/```(\w*)\n([\s\S]*?)```/g, function(m, lang, code) {
    return '<div class="ai-code-block"><span class="ai-code-lang">' + esc(lang || 'code') + '</span><pre><code>' + code + '</code></pre></div>';
  });

  /* Inline code */
  text = text.replace(/`([^`]+)`/g, '<code>$1</code>');

  /* Headings (h3-h6) */
  text = text.replace(/^### (.+)$/gm, '<h4 class="ai-h4">$1</h4>');
  text = text.replace(/^#### (.+)$/gm, '<h5 class="ai-h5">$1</h5>');

  /* Bold & italic */
  text = text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  text = text.replace(/\*(.+?)\*/g, '<em>$1</em>');

  /* 📖 links */
  text = text.replace(/📖\s*\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" class="assistant-link">📖 $1</a>');

  /* Bare URLs */
  text = text.replace(/(\b(https?|ftp):\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noopener">$1</a>');

  /* Ordered lists */
  text = text.replace(/^\d+\.\s(.+)$/gm, '<li class="ai-li">$1</li>');
  text = text.replace(/(<li class="ai-li">.*<\/li>\n?)+/g, '<ol class="ai-ol">$&</ol>');

  /* Unordered lists */
  text = text.replace(/^[-*]\s(.+)$/gm, '<li class="ai-li">$1</li>');

  /* Blockquotes */
  text = text.replace(/^>\s(.+)$/gm, '<blockquote class="ai-blockquote">$1</blockquote>');

  /* Tables: simple pipe table to HTML */
  text = text.replace(/^(\|.+\|)\n\|[-| :]+\|\n((?:\|.+\|\n?)*)/gm, function(m, headerRow, bodyRows) {
    var cells = headerRow.split('|').filter(function(c){ return c.trim(); });
    var thead = '<thead><tr>' + cells.map(function(c){ return '<th>' + c.trim() + '</th>'; }).join('') + '</tr></thead>';
    var rows = bodyRows.trim().split('\n');
    var tbody = '<tbody>' + rows.map(function(row){
      return '<tr>' + row.split('|').filter(function(c){ return c.trim(); }).map(function(c){ return '<td>' + c.trim() + '</td>'; }).join('') + '</tr>';
    }).join('') + '</tbody>';
    return '<table class="ai-table">' + thead + tbody + '</table>';
  });

  /* Newlines → <br> */
  text = text.replace(/\n/g, '<br>');

  return text;
}

/* ---------- Render messages ---------- */
function renderMessages() {
  var container = document.getElementById('assistant-msgs');
  if (!container) return;

  var html = '';
  for (var i = 0; i < messages.length; i++) {
    var m = messages[i];
    if (m.role === 'system') continue;
    if (m.role === 'user') {
      html += '<div class="assistant-msg user-msg"><div class="msg-bubble">' + esc(m.content) + '</div></div>';
    } else {
      html += '<div class="assistant-msg ai-msg msg-animate"><div class="msg-avatar">AI</div><div class="msg-bubble">' + formatResponse(m.content) + '</div></div>';
    }
  }

  container.innerHTML = html;
  container.scrollTop = container.scrollHeight;
}

function updateBubble(msgIdx) {
  var container = document.getElementById('assistant-msgs');
  if (!container) return;
  var bubbles = container.querySelectorAll('.ai-msg .msg-bubble');
  var aiMsgs = container.querySelectorAll('.ai-msg');
  if (aiMsgs.length === 0) return;
  var targetAi = aiMsgs[msgIdx - countUserMsgsBefore(msgIdx)];
  if (!targetAi) return;
  var bubble = targetAi.querySelector('.msg-bubble');
  if (bubble) {
    bubble.innerHTML = formatResponse(messages[msgIdx].content) || '<span class="stream-cursor">|</span>';
  }
  container.scrollTop = container.scrollHeight;
}

function countUserMsgsBefore(idx) {
  var count = 0;
  for (var i = 0; i < idx; i++) {
    if (messages[i] && messages[i].role === 'user') count++;
  }
  return idx - count;
}

/* ---------- Follow-up chips ---------- */
function renderFollowUpChips(msgIdx) {
  var container = document.getElementById('assistant-msgs');
  if (!container) return;

  var existing = container.querySelector('.follow-up-row');
  if (existing) existing.remove();

  var chips = generateFollowUps(messages[msgIdx].content);
  if (!chips.length) return;

  var div = document.createElement('div');
  div.className = 'follow-up-row';
  div.innerHTML = '<span class="follow-up-label">Ask a follow-up:</span> ' +
    chips.map(function(q){ return '<button class="assistant-chip follow-up-chip" data-q="' + esc(q) + '">' + esc(q) + '</button>'; }).join('');
  container.appendChild(div);
  container.scrollTop = container.scrollHeight;
}

function generateFollowUps(reply) {
  var sets = {
    'linux': ['How do I install software on Linux?', 'What is the Linux filesystem structure?'],
    'docker': ['How do I write a Dockerfile?', 'What is Docker Compose?'],
    'git': ['How do I undo a commit?', 'What is a merge conflict?'],
    'python': ['How do I install Python packages?', 'What are Python virtual environments?'],
    'windows': ['How do I debloat Windows?', 'What are essential Windows tools?'],
    'network': ['How do I troubleshoot network issues?', 'What is the OSI model?'],
    'security': ['How do I secure my home network?', 'What is two-factor authentication?'],
    'vpn': ['What is the difference between VPN and proxy?', 'How do I set up WireGuard?'],
    'search': ['What tutorials are available?', 'How do I search the library?']
  };

  var lower = reply.toLowerCase();
  for (var key in sets) {
    if (lower.indexOf(key) !== -1) return sets[key];
  }
  return ['What else can I learn here?', 'Show me popular tutorials'];
}

/* ---------- Suggested questions (initial) ---------- */
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
    '<br><span class="welcome-hint">Pick a question below or type your own.</span></div></div>';
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

/* ---------- Create UI ---------- */
function createUI() {
  if (document.getElementById('assistant-fab')) return;

  /* FAB */
  var fab = document.createElement('button');
  fab.id = 'assistant-fab';
  fab.className = 'assistant-fab' + (isOnline() ? '' : ' offline');
  fab.innerHTML = '<i class="fas fa-robot"></i>';
  fab.setAttribute('aria-label', 'Open AI assistant');
  document.body.appendChild(fab);

  /* Panel */
  var panel = document.createElement('div');
  panel.id = 'assistant-panel';
  panel.className = 'assistant-panel';
  panel.innerHTML =
    '<div class="assistant-header">' +
      '<span><i class="fas fa-robot"></i> Tech Library Assistant</span>' +
      '<span class="assistant-header-right">' +
        '<span id="assistant-status-dot" class="assistant-status-dot ' + (isOnline() ? 'online' : 'offline') + '" title="' + (isOnline() ? 'Connected' : 'Offline') + '"></span>' +
        '<button id="assistant-clear" class="assistant-clear-btn" title="Clear conversation"><i class="fas fa-trash-alt"></i></button>' +
        '<button id="assistant-close" class="assistant-close" aria-label="Close assistant">&times;</button>' +
      '</span>' +
    '</div>' +
    '<div class="assistant-msgs" id="assistant-msgs"></div>' +
    '<div class="assistant-input-area">' +
      '<textarea id="assistant-input" class="assistant-input" rows="1" placeholder="Ask about tutorials, terms, resources…" aria-label="Message"></textarea>' +
      '<button id="assistant-send" class="assistant-send" aria-label="Send"><i class="fas fa-paper-plane"></i></button>' +
    '</div>';
  document.body.appendChild(panel);

  /* Events */
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

  /* Chip delegation */
  panel.addEventListener('click', function(e){
    var chip = e.target.closest('.assistant-chip');
    if (chip && chip.getAttribute('data-q')) {
      sendMessage(chip.getAttribute('data-q'));
    }
  });

  /* Close on Escape */
  document.addEventListener('keydown', function(e){
    if (e.key === 'Escape' && panelOpen) closePanel();
  });

  /* Keyboard shortcut: Ctrl+Shift+A */
  document.addEventListener('keydown', function(e){
    if ((e.ctrlKey || e.metaKey) && e.shiftKey && (e.key === 'a' || e.key === 'A')) {
      e.preventDefault();
      togglePanel();
    }
  });

  /* Online/offline listeners */
  window.addEventListener('online', updateOnlineStatus);
  window.addEventListener('offline', updateOnlineStatus);

  createScrollBottomBtn();
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
  if (panel) panel.classList.add('open');
  if (fab) fab.classList.add('hidden');
  if (!isOnline()) showOfflineNotice();
  setTimeout(function(){
    var inp = document.getElementById('assistant-input');
    if (inp) inp.focus();
  }, 350);
}

function closePanel() {
  panelOpen = false;
  var panel = document.getElementById('assistant-panel');
  var fab  = document.getElementById('assistant-fab');
  if (panel) panel.classList.remove('open');
  if (fab) fab.classList.remove('hidden');
}

/* ---------- Init ---------- */
function init() {
  createUI();
  loadHistory();
  updateOnlineStatus();
  if (messages.length === 0) {
    renderSuggestions();
  } else {
    renderMessages();
    if (!isOnline()) showOfflineNotice();
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}

} catch(e) { /* fail silently */ }
})();
