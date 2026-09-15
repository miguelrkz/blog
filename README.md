# 808s // LOGS — Minimalist Futuristic Markdown Blog

A fast, minimalist blog engineered with the iconic **808s & Heartbreak** color palette (Grey, White, Red in Light Mode; Grey, Black, Red in Dark Mode) fused with a modern futuristic HUD aesthetic.

Powered by **Astro 5**, **Tailwind CSS**, and **GitHub Pages**.

---

## Features

- 🎧 **808s & Heartbreak Color Palette**:
  - **Light Mode**: Chalk cool greys, pure whites, and vivid heart red accents.
  - **Dark Mode**: Deep carbon/obsidian black, graphite slate, and glowing infrared neon red.
- ⚡ **Instant Theme Switcher**: Toggle between light and dark modes with persistent state in `localStorage` and zero flash on page load.
- 📑 **Dynamic Section Channels**: Top dropdown automatically scans all posts in your content folder, groups them into sections, and displays live post counts.
- 🗂 **Card Grid View & Pagination**: Clean responsive cards displaying titles, publication dates, section tags, brief descriptions, and read triggers. Multi-page pagination (`[PREV]`, `1`, `2`, `[NEXT]`) operates across all posts and individual sections.
- 💔 **Automatic 808s SVG Fallback**: If a post omits an image, our bespoke 808s cracked-heart and audio pulse waveform SVG renders automatically.
- 🚀 **Zero-Config Git Workflow**: Just drop a Markdown file into `src/content/posts/` and run `git push`. GitHub Actions builds and publishes it live to GitHub Pages in ~60 seconds.

---

## How to Add a New Post

1. Create a `.md` file inside `src/content/posts/` (e.g. `src/content/posts/my-new-story.md`).
2. Add the frontmatter block at the very top:

```markdown
---
title: "Your Post Title"
description: "A brief summary that will appear on the card preview."
pubDate: 2026-09-16
section: "Music & Sound"
image: "" # (Optional) Image URL or local image in /public/images/. Leave empty for the 808s placeholder!
author: "Miguel Robledo"
---

Your markdown content goes here!

## Section Title

You can write standard markdown with **bold text**, *italics*, [links](https://example.com), code blocks, and blockquotes.

> "In the coldest winter..."
```

3. Save the file.
4. Commit and push:
```bash
git add .
git commit -m "feat: add my new story"
git push
```

---

## Local Development

To run and preview the blog on your machine:

```bash
# Start local development server
npm run dev

# Build the static site (output generated in dist/)
npm run build

# Preview the production build locally
npm run preview
```

---

## Deployment to GitHub Pages

The blog comes preconfigured with a GitHub Actions workflow (`.github/workflows/deploy.yml`).

### First-Time GitHub Setup:
1. Create a repository on GitHub (e.g. `https://github.com/<your-username>/blog`).
2. Connect your local repository to GitHub:
   ```bash
   git remote add origin https://github.com/<your-username>/blog.git
   git branch -M main
   git push -u origin main
   ```
3. On GitHub, go to your repository:
   - Click **Settings** > **Pages** (in the left sidebar).
   - Under **Build and deployment** > **Source**, select **GitHub Actions**.
4. That's it! Every time you `git push` to `main`, GitHub Actions will build and deploy the blog automatically.
