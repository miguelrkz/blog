import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    section: z.string(),
    image: z.string().optional().default(''),
    author: z.string().optional().default('Miguel Robledo'),
    featured: z.boolean().optional().default(false),
  }),
});

export const collections = { posts };
