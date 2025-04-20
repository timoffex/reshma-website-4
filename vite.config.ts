import { sveltekit } from '@sveltejs/kit/vite';
import { enhancedImages } from '@sveltejs/enhanced-img';
import { defineConfig } from 'vite';
import { imagetools } from 'vite-imagetools';

export default defineConfig({
  plugins: [enhancedImages(), imagetools(), sveltekit()],

  css: {
    preprocessorOptions: {
      scss: {
        api: 'modern'
      }
    }
  }
});
