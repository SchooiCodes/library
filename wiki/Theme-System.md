# Theme System

The site has 10 color themes, each with light and dark variants. Themes are managed by `assets/theme.js`.

## Available Themes

| Theme | Light | Dark | CSS Class |
|---|---|---|---|
| Default | ✅ | ✅ | *(default)* |
| Ocean | ✅ | ✅ | `theme-ocean` |
| Forest | ✅ | ✅ | `theme-forest` |
| Sunset | ✅ | ✅ | `theme-sunset` |
| Midnight | ✅ | ✅ | `theme-midnight` |
| Mono | ✅ | ✅ | `theme-mono` |
| Aurora | ❌ | ✅ | `theme-aurora` |
| Lava | ❌ | ✅ | `theme-lava` |
| Nord | ❌ | ✅ | `theme-nord` |
| Dracula | ❌ | ✅ | `theme-dracula` |

## How It Works

Themes are independent of dark/light mode. Any combination works:
- Dark mode + Ocean theme
- Light mode + Midnight theme
- etc.

Theme and mode preferences are saved to `localStorage`:

```
localStorage.setItem('tl-theme', 'ocean')
localStorage.setItem('tl-dark-mode', 'true')
```

## CSS Implementation

Each theme defines CSS custom properties on `body.theme-*`:

```css
body.theme-ocean {
  --primary: #0ea5e9;
  --primary-dark: #0284c7;
  --primary-light: #7dd3fc;
  /* ... */
}
```

Dark mode is toggled via `body.dark-mode` which swaps background/text colors.
