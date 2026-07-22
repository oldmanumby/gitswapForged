import { defineConfig } from 'blume';

export default defineConfig({
  title: 'GitWarp',
  description: 'Documentation for the GitWarp URL manipulation toolkit.',
  theme: {
    accent: { light: '#478BE6', dark: '#478BE6' },
    background: { light: '#151B23', dark: '#151B23' },
    mode: 'dark',
  },
  analytics: {
    scripts: [
      {
        content: `
          const style = document.createElement('style');
          style.innerHTML = 'button[aria-label="Toggle color theme"] { display: none !important; }';
          document.head.appendChild(style);
          localStorage.setItem('blume-theme', 'dark');
          document.documentElement.dataset.theme = 'dark';
        `
      }
    ]
  },
  navigation: {
    featured: [{ href: '../', label: 'Back to GitWarp' }],
  },
});
