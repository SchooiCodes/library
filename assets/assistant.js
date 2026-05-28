/* ===== Tech Library AI Assistant ===== */
(function(){
try {

/* ---------- Config ---------- */
var ASSISTANT_ENDPOINT = 'https://ai-assistant.schooi.workers.dev/chat';
var MAX_MESSAGES    = 30;
var MAX_CONTEXT_C   = 2500;
var MAX_PAGES       = 5;
var STORAGE_KEY     = 'tl_assistant_msgs';

/* ---------- State ---------- */
var messages  = [];
var panelOpen = false;
var isTyping  = false;

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

  /* match lexicon terms */
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

  /* fetch page snippets in parallel */
  var fetches = pages.map(function(p){ return fetchSnippet(p.url); });
  Promise.all(fetches).then(function(snippets){
    var parts = [];

    if (pages.length) {
      parts.push('=== RELEVANT PAGES ===');
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

/* ---------- Build the system prompt ---------- */
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
    'Always respond concisely (2-4 paragraphs). ' +
    'When referencing a resource, ALWAYS include a link using this format: ' +
    '📖 [Page Title](/path/to/page.html)\n' +
    'Keep links as relative paths (starting with /).\n' +
    'If you are unsure about something, say so honestly.\n' +
    'Suggest 1-2 follow-up questions at the end.\n\n' +
    'CURRENT CONTEXT:\n' + (context || '(none)') +
    '\n\nAnswer the user based on the available context and your general knowledge.'
  );
}

/* ---------- API call ---------- */
function callAI(messages, context, callback) {
  var sys = systemPrompt(context);
  var body = JSON.stringify({ system: sys, messages: messages });

  fetch(ASSISTANT_ENDPOINT, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: body
  })
  .then(function(r){
    if (!r.ok) throw new Error('HTTP ' + r.status);
    return r.json();
  })
  .then(function(data){
    callback(null, data.reply || '');
  })
  .catch(function(err){
    callback(err, null);
  });
}

/* ---------- Format AI response (simple markdown-ish) ---------- */
function formatResponse(text) {
  if (!text) return '';
  /* escape HTML first, then convert markdown-like syntax */
  text = esc(text);
  /* bold **text** */
  text = text.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
  /* italic *text* */
  text = text.replace(/\*(.+?)\*/g, '<em>$1</em>');
  /* inline code `text` */
  text = text.replace(/`([^`]+)`/g, '<code>$1</code>');
  /* resource links 📖 [title](/path) */
  text = text.replace(/📖\s*\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" class="assistant-link">📖 $1</a>');
  /* plain links */
  text = text.replace(/(\b(https?|ftp):\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noopener">$1</a>');
  /* newlines to <br> */
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
      html += '<div class="assistant-msg ai-msg"><div class="msg-avatar">AI</div><div class="msg-bubble">' + formatResponse(m.content) + '</div></div>';
    }
  }

  if (isTyping) html += typingHTML();

  container.innerHTML = html;
  container.scrollTop = container.scrollHeight;
}

function typingHTML() {
  return '<div class="assistant-msg ai-msg" id="assistant-typing"><div class="msg-avatar">AI</div><div class="msg-bubble typing-indicator"><span></span><span></span><span></span></div></div>';
}

function showTyping() {
  isTyping = true;
  var container = document.getElementById('assistant-msgs');
  if (container) {
    var existing = document.getElementById('assistant-typing');
    if (!existing) container.insertAdjacentHTML('beforeend', typingHTML());
    container.scrollTop = container.scrollHeight;
  }
}

function hideTyping() {
  isTyping = false;
  var el = document.getElementById('assistant-typing');
  if (el) el.remove();
}

/* ---------- Send message ---------- */
function sendMessage(text) {
  if (!text || !text.trim()) return;
  text = text.trim();

  addMessage('user', text);
  renderMessages();
  saveHistory();
  document.getElementById('assistant-input').value = '';
  setInputHeight();

  showTyping();

  buildContext(text, function(context){
    callAI(messages, context, function(err, reply){
      hideTyping();

      if (err || !reply) {
        var fallback = "I couldn't reach the AI service right now." +
          (window.__TL && window.__TL.searchIndex
            ? ' Try using the search (⌘K) to find what you need.'
            : '');
        addMessage('assistant', fallback);
      } else {
        addMessage('assistant', reply);
      }

      renderMessages();
      saveHistory();
    });
  });
}

function addMessage(role, content) {
  messages.push({ role: role, content: content, ts: Date.now() });
  if (messages.length > MAX_MESSAGES) messages.shift();
}

/* ---------- Suggested questions ---------- */
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
  var html = '<div class="assistant-msg ai-msg"><div class="msg-avatar">AI</div><div class="msg-bubble"><strong>Hi! I can help you find tutorials, explain tech terms, and guide you to the right resources.</strong></div></div>';
  html += '<div class="assistant-chips">';
  for (var i = 0; i < chips.length; i++) {
    html += '<button class="assistant-chip" data-q="' + esc(chips[i]) + '">' + esc(chips[i]) + '</button>';
  }
  html += '</div>';
  container.innerHTML = html;
}

/* ---------- Create UI ---------- */
function createUI() {
  if (document.getElementById('assistant-fab')) return;

  /* FAB */
  var fab = document.createElement('button');
  fab.id = 'assistant-fab';
  fab.className = 'assistant-fab';
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
      '<button id="assistant-close" class="assistant-close" aria-label="Close assistant">&times;</button>' +
    '</div>' +
    '<div class="assistant-msgs" id="assistant-msgs"></div>' +
    '<div class="assistant-input-area">' +
      '<textarea id="assistant-input" class="assistant-input" rows="1" placeholder="Ask about tutorials, terms, resources…" aria-label="Message"></textarea>' +
      '<button id="assistant-send" class="assistant-send" aria-label="Send"><i class="fas fa-paper-plane"></i></button>' +
    '</div>';
  document.body.appendChild(panel);

  /* Events */
  fab.addEventListener('click', togglePanel);
  document.getElementById('assistant-close').addEventListener('click', closePanel);

  var sendBtn = document.getElementById('assistant-send');
  var inputEl = document.getElementById('assistant-input');

  sendBtn.addEventListener('click', function(){ sendMessage(inputEl.value); });

  inputEl.addEventListener('keydown', function(e){
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage(inputEl.value);
    }
  });

  inputEl.addEventListener('input', setInputHeight);

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
}

function setInputHeight() {
  var el = document.getElementById('assistant-input');
  if (!el) return;
  el.style.height = 'auto';
  el.style.height = Math.min(el.scrollHeight, 120) + 'px';
}

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
  setTimeout(function(){
    var inp = document.getElementById('assistant-input');
    if (inp) inp.focus();
  }, 300);
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
  if (messages.length === 0) {
    renderSuggestions();
  } else {
    renderMessages();
  }
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  init();
}

} catch(e) { /* fail silently */ }
})();
