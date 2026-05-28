# Tech Library Wiki

Welcome to the Tech Library wiki. This documentation covers the architecture, workflow, and conventions used across the project.

## Quick Links

- [[Home]] — Project overview
- [[Architecture]] — How the site is structured
- [[Build System]] — How `build.py` works
- [[Content Guidelines]] — How to write and format pages
- [[AI Assistant]] — How the AI assistant works
- [[Theme System]] — How themes and dark mode work
- [[Admin Panel]] — How to use the Flask admin panel
- [[Deployment]] — How to deploy to GitHub Pages
- [[Contributing]] — How to contribute

## Overview

This is a zero-dependency static documentation site. It consists of plain HTML files, a single CSS stylesheet, and a few JavaScript files. There is no build step for development — just open `index.html` in a browser.

For production (search index, stats, breadcrumbs), run `python3 build.py` to regenerate the search index and propagate changes across all pages.
