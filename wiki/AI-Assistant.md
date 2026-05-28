# AI Assistant

The AI assistant is a client-side chat widget (`assets/assistant.js`) that communicates with a Cloudflare Worker.

## Architecture

```
Browser (assistant.js)  ←→  Cloudflare Worker  ←→  AI API
         |
         +→ Local search index (RAG context)
         +→ Fetches page snippets for context
```

## Features

- **SSE streaming** — responses stream token-by-token as the AI generates
- **RAG (Retrieval-Augmented Generation)** — finds relevant pages from the embedded search index, fetches snippets, and includes them in the system prompt
- **Link validation** — only links to pages that actually exist in the index
- **Chat persistence** — saves last 25 messages to `localStorage`
- **Follow-up chips** — dynamic suggestions extracted from the AI's response
- **Offline detection** — disables the assistant when offline with a clear message
- **Keyboard shortcut** — `Ctrl+Shift+A` to toggle the panel

## Cloudflare Worker

The worker endpoint is:

```
https://tech-library-ai.robloxianskp.workers.dev
```

It expects a POST with JSON body:

```json
{
  "system": "system prompt with RAG context",
  "messages": [{"role": "user", "content": "..."}]
}
```

And returns SSE with `data: {"response":"..."}` lines, terminated by `data: [DONE]`.

## Configuration

Key constants in `assistant.js`:

| Constant | Default | Purpose |
|---|---|---|
| `MAX_MESSAGES` | 25 | Chat history limit |
| `MAX_CONTEXT_C` | 4000 | Max context chars sent to AI |
| `MAX_PAGES` | 5 | Max pages used for RAG |
| `SNIPPET_MAX` | 1200 | Max chars per page snippet |
