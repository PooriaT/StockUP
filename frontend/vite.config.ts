import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [sveltekit()],
  preview: {
    port: 10000,
    host: true,
    allowedHosts: ['stockupforall.onrender.com']
  }
});
