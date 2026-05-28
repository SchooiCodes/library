# Deployment

## GitHub Pages

The site is hosted on GitHub Pages at `https://schooicodes.github.io/library/`.

### To deploy:

1. Run the build system to update search index and stats:
   ```bash
   python3 build.py
   ```

2. Commit and push:
   ```bash
   git add -A
   git commit -m "Update"
   git push origin main
   ```

3. GitHub Pages auto-deploys from the `main` branch (configured in repo Settings > Pages).

## Local Development

No server required — just open `index.html` in any browser:

```bash
open index.html      # macOS
xdg-open index.html  # Linux
start index.html     # Windows
```

For the AI assistant to work locally, you need an internet connection (it calls a Cloudflare Worker). The search and lexicon work fully offline.
