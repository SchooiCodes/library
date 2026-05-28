# Content Guidelines

## Page Anatomy

Every content page should have:

```html
<!-- @category tutorial -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Brief description for search and preview">
  <title>Page Title — Tech Library</title>
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
  <main>
    <h1>Page Title</h1>
    <!-- content -->
  </main>
  <script src="../assets/scripts.js" defer></script>
  <script src="../assets/theme.js" defer></script>
</body>
</html>
```

## Category Marker

The `<!-- @category tutorial -->` comment at the top (before `<!DOCTYPE>`) tells the build system which section this page belongs to.

## Headings

- Use `<h1>` for the page title (only one)
- Use `<h2>` for major sections
- Use `<h3>` for subsections
- The build system auto-generates a Table of Contents from `<h2>` and `<h3>` tags

## Navigation Buttons

For multi-part tutorials, use previous/next buttons:

```html
<div class="page-nav">
  <a href="previous-page.html" class="page-nav-btn">← Previous</a>
  <a href="next-page.html" class="page-nav-btn">Next →</a>
</div>
```

## Further Reading

Always include a "Further Reading" section with links:

```html
<div class="further-reading">
  <h2>Further Reading</h2>
  <ul>
    <li><a href="/tutorials/related-topic.html">Related Topic</a></li>
  </ul>
</div>
```

## Lexicon Terms

If you use tech terms that are defined in the lexicon, link them:

```html
<a href="/lexicon/#term" class="lexicon-link" data-term="API">API</a>
```

The site auto-highlights lexicon terms on page load if you include `scripts.js`.
