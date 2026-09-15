---
title: "Welcome to the Blog: Setup & Writing Guide"
description: "A comprehensive guide on how this blog operates, managing markdown files, frontmatter specifications, and automated GitHub Pages deployments."
pubDate: 2026-09-16
section: "General"
image: ""
author: "Miguel Robledo"
---

Welcome to your new markdown-driven personal blog. This platform is engineered with a minimalist aesthetic combining cool greys, stark whites, deep obsidian blacks, and vivid red accents.

## Visual Design & Theme

The interface provides a clean, focused reading experience:

- **Light Mode (Clear)**: Cool chalk greys, pure whites, and vivid red accents.
- **Dark Mode**: Obsidian black, carbon slate greys, and glowing neon red highlights.
- **Futuristic Accents**: Monospace telemetry, hairline borders, and subtle grid textures.

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
section: "Engineering" # Creates or assigns to this section
image: "" # Optional URL or local image path. Leave empty for the graphic placeholder!
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

## Key Features

- **Dynamic Section Detection**: Whenever you use a new `section` in frontmatter, the top dropdown automatically detects it and creates a dedicated filtered view.
- **Automatic Fallback Placeholders**: If you don't supply an image or leave `image: ""` blank, a custom graphic placeholder will render automatically.
- **Dark/Light Mode Persistence**: Visitors can toggle modes using the button in the top right, and their preference is saved in their browser.
- **Clean Responsive Cards**: Grid layout scales seamlessly from mobile screens to ultra-wide displays.
