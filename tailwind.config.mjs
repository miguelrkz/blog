import typography from '@tailwindcss/typography';

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        brand: {
          red: {
            DEFAULT: '#e11d48',
            light: '#f43f5e',
            neon: '#ff2a5f',
            dark: '#be123c',
            glow: 'rgba(255, 42, 95, 0.35)',
          },
          grey: {
            50: '#f8f9fa',
            100: '#f1f3f5',
            200: '#e5e7eb',
            300: '#d1d5db',
            400: '#9ca3af',
            500: '#6b7280',
            600: '#4b5563',
            700: '#374151',
            800: '#1f2937',
            900: '#111827',
          },
          dark: {
            bg: '#090a0f',
            surface: '#12131a',
            surfaceHover: '#181a24',
            border: '#222533',
            borderHighlight: '#ff2a5f40',
          },
          light: {
            bg: '#f4f5f8',
            surface: '#ffffff',
            surfaceHover: '#fafafc',
            border: '#e2e5eb',
            borderHighlight: '#e11d4830',
          },
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        mono: ['JetBrains Mono', 'Fira Code', 'SFMono-Regular', 'Menlo', 'monospace'],
        display: ['Space Grotesk', 'Inter', 'sans-serif'],
      },
      boxShadow: {
        'glow-red': '0 0 25px -5px rgba(255, 42, 95, 0.4)',
        'glow-red-sm': '0 0 12px -2px rgba(255, 42, 95, 0.3)',
        'hud-light': '0 4px 20px -2px rgba(0, 0, 0, 0.05), 0 0 0 1px rgba(226, 229, 235, 0.8)',
        'hud-dark': '0 4px 25px -2px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(34, 37, 51, 0.8)',
      },
      animation: {
        'pulse-subtle': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'heartbeat': 'heartbeat 2s ease-in-out infinite',
      },
      keyframes: {
        heartbeat: {
          '0%, 100%': { transform: 'scale(1)' },
          '14%': { transform: 'scale(1.06)' },
          '28%': { transform: 'scale(1)' },
          '42%': { transform: 'scale(1.04)' },
          '70%': { transform: 'scale(1)' },
        },
      },
    },
  },
  plugins: [typography],
};
