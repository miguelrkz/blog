---
title: "Welcome to 808s: Minimalist Transmission Guide"
description: "A comprehensive guide on how this blog operates, managing markdown files, frontmatter specifications, and automated GitHub Pages deployments."
pubDate: 2026-09-16
section: "General"
image: ""
author: "Miguel Robledo"
---

Welcome to your new markdown-driven blog. This system was engineered specifically to blend the emotional minimalism of the **808s & Heartbreak** aesthetic with a razor-sharp, modern futuristic HUD feel.

## Visual Design & The 808s Philosophy

The design centers on three key pillars:

- **Light Mode (Clear)**: Cool chalk greys, pure whites, and vivid 808s Heartbreak red accents.
- **Dark Mode**: Obsidian black, carbon slate greys, and glowing infrared neon highlights.
- **Futuristic Telemetry**: Monospace coordinates, audio waveform pulse lines, and hairline borders.

> "Keep it simple. Everything synthetic, yet emotionally resonant."

---

## How to Publish a New Post

Writing a new post takes only seconds:

1. Create a `.md` file inside the `src/content/posts/` folder (for example: `my-new-post.md`).
2. Add the frontmatter block at the top of the file:

```yaml
---
title: "Your Post Title"
description: "A brief summary that will appear on the card preview."
pubDate: 2026-09-16
section: "Music & Sound" # Creates or assigns to this section
image: "" # Optional URL or local image path. Leave empty for 808s placeholder!
author: "Miguel Robledo"
---
```

3. Write your article in standard Markdown below the frontmatter.
4. Save the file, commit, and push:

```bash
git add .
git commit -m "feat: add new post"
git push
```

Within 60 to 90 seconds, GitHub Actions automatically builds the static site and deploys it live to GitHub Pages.

---

## Automatic Features

- **Dynamic Section Detection**: Whenever you use a new `section` in frontmatter, the top dropdown automatically detects it and creates a dedicated channel page.
- **Automatic Fallback Placeholders**: If you don't supply an image or leave `image: ""` blank, our custom 808s cracked heart and audio waveform SVG will render automatically.
- **Dark/Light Mode Persistence**: Your visitors can toggle modes using the pill button in the top right, and their preference is saved in their browser.
- **Clean Responsive Cards**: Grid layout scales seamlessly from mobile screens to ultra-wide displays.
