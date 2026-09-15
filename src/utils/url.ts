/**
 * Helper to resolve paths respecting Astro's configured BASE_URL for GitHub Pages
 */
export function url(path: string): string {
  const base = (import.meta.env.BASE_URL || '/').replace(/\/$/, '');
  const cleanPath = path.startsWith('/') ? path : `/${path}`;
  return `${base}${cleanPath}`;
}
