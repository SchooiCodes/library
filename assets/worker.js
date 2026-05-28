/* ===== Tech Library AI Assistant — Cloudflare Worker =====
   Deploy: paste into Cloudflare Dashboard → Workers & Pages → Create Worker
   Free tier: 100k req/day Worker + 10k req/day Workers AI
   ========================================================= */

/* Simple in-memory rate limiter (resets per cold start, fine for free tier) */
var rateMap = {};

function checkRate(ip) {
  var now = Date.now();
  var windowMs = 60000;
  var maxReqs = 10;
  if (!rateMap[ip]) rateMap[ip] = [];
  rateMap[ip] = rateMap[ip].filter(function(t){ return now - t < windowMs; });
  if (rateMap[ip].length >= maxReqs) return false;
  rateMap[ip].push(now);
  return true;
}

function corsHeaders() {
  return {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Content-Type': 'application/json'
  };
}

export default {
  async fetch(request, env) {
    /* CORS preflight */
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders() });
    }

    if (request.method !== 'POST') {
      return new Response(JSON.stringify({ error: 'POST only' }), {
        status: 405, headers: corsHeaders()
      });
    }

    /* Rate limit */
    var ip = request.headers.get('cf-connecting-ip') || 'unknown';
    if (!checkRate(ip)) {
      return new Response(JSON.stringify({ error: 'Rate limited. Please wait a moment.' }), {
        status: 429, headers: corsHeaders()
      });
    }

    /* Parse body */
    var body;
    try { body = await request.json(); } catch(e) {
      return new Response(JSON.stringify({ error: 'Invalid JSON' }), {
        status: 400, headers: corsHeaders()
      });
    }

    var systemMsg = body.system || '';
    var chatMsgs  = body.messages || [];

    /* Build message array for the model — preserve conversation history */
    var msgs = [{ role: 'system', content: systemMsg }];
    var start = Math.max(0, chatMsgs.length - 8);
    for (var i = start; i < chatMsgs.length; i++) {
      var m = chatMsgs[i];
      if (m.role === 'user' || m.role === 'assistant') {
        msgs.push({ role: m.role, content: m.content || '' });
      }
    }

    /* Available model: @cf/meta/llama-2-7b-chat-int8 (free tier)
       Change to any Workers AI model as needed. */
    var model = '@cf/meta/llama-2-7b-chat-int8';

    try {
      var aiResp = await env.AI.run(model, { messages: msgs });
      var reply = aiResp.response || '';

      return new Response(JSON.stringify({ reply: reply }), {
        headers: corsHeaders()
      });
    } catch(err) {
      return new Response(JSON.stringify({ error: 'AI error: ' + err.message }), {
        status: 500, headers: corsHeaders()
      });
    }
  }
};
