import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  // If deploying to https://<username>.github.io/<repo-name>/,
  // set site and base accordingly. Can also be configured via env vars.
  site: process.env.SITE_URL || 'https://miguelrkz.github.io',
  base: process.env.BASE_PATH || undefined,
  integrations: [
    tailwind({
      applyBaseStyles: false,
    }),
  ],
  markdown: {
    shikiConfig: {
      theme: 'github-dark-dimmed',
      wrap: true,
    },
  },
});
