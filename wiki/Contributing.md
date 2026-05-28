# Contributing

## How to Contribute

1. **Report bugs** — open an issue with `bug` label
2. **Suggest features** — open an issue with `enhancement` label
3. **Submit content** — send a PR with new tutorial pages or improvements
4. **Fix issues** — check the issues tab for open tasks

## Adding a New Tutorial Page

1. Create a new `.html` file in the appropriate category directory
2. Include the `<!-- @category tutorial -->` marker at the top
3. Add proper `<meta>` tags (description, title)
4. Run the build system:
   ```bash
   python3 build.py
   ```
5. Verify the page appears in search results

## Code Style

- **HTML** — semantic tags, proper heading hierarchy, accessible labels
- **CSS** — custom properties for theming, no `!important` unless necessary
- **JS** — `var` for wide compatibility (no transpiler), no modern API that breaks on older browsers
- **Python** — PEP 8, f-strings, pathlib

## PR Checklist

Before submitting a PR:

- [ ] Tested on desktop browser (Chrome / Firefox)
- [ ] Tested on mobile viewport
- [ ] Verified all links work
- [ ] Ran `python3 build.py` if search index or stats changed
- [ ] No hardcoded URLs (use relative paths)
