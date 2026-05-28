/* ===== Tech Library AI Assistant — Cloudflare Worker =====
   Deploy: paste into Cloudflare Dashboard → Workers & Pages → Create Worker
   Free tier: 100k req/day Worker + 10k req/day Workers AI
   ========================================================= */

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
    'Access-Control-Allow-Headers': 'Content-Type'
  };
}

export default {
  async fetch(request, env) {
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders() });
    }

    if (request.method !== 'POST') {
      return new Response(JSON.stringify({ error: 'POST only' }), {
        status: 405, headers: { ...corsHeaders(), 'Content-Type': 'application/json' }
      });
    }

    var ip = request.headers.get('cf-connecting-ip') || 'unknown';
    if (!checkRate(ip)) {
      return new Response(JSON.stringify({ error: 'Rate limited. Please wait a moment.' }), {
        status: 429, headers: { ...corsHeaders(), 'Content-Type': 'application/json' }
      });
    }

    var body;
    try { body = await request.json(); } catch(e) {
      return new Response(JSON.stringify({ error: 'Invalid JSON' }), {
        status: 400, headers: { ...corsHeaders(), 'Content-Type': 'application/json' }
      });
    }

    var systemMsg = body.system || '';
    var chatMsgs  = body.messages || [];

    var msgs = [{ role: 'system', content: systemMsg }];
    var start = Math.max(0, chatMsgs.length - 8);
    for (var i = start; i < chatMsgs.length; i++) {
      var m = chatMsgs[i];
      if (m.role === 'user' || m.role === 'assistant') {
        msgs.push({ role: m.role, content: m.content || '' });
      }
    }

    var model = '@cf/meta/llama-3.1-8b-instruct';

    try {
      var aiResp = await env.AI.run(model, {
        messages: msgs,
        stream: true,
        max_tokens: 600
      });

      return new Response(aiResp, {
        headers: {
          ...corsHeaders(),
          'Content-Type': 'text/event-stream',
          'Cache-Control': 'no-cache',
          'Connection': 'keep-alive'
        }
      });
    } catch(err) {
      return new Response(JSON.stringify({ error: 'AI error: ' + err.message }), {
        status: 500, headers: { ...corsHeaders(), 'Content-Type': 'application/json' }
      });
    }
  }
};
