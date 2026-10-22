import { defineConfig } from "astro/config";
import path from "node:path";
import react from "@astrojs/react";
import tailwindcss from "@tailwindcss/vite";
import rehypeSlug from "rehype-slug";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import { rehypeCallouts } from "./src/lib/rehype-callouts.mjs";

export default defineConfig({
  site: "https://neonotes.vercel.app",
  integrations: [react()],
  prefetch: {
    prefetchAll: true,
  },
  vite: {
    plugins: [tailwindcss()],
    server: {
      strictPort: true,
      host: "localhost",
      fs: {
        strict: false,
        allow: [process.cwd(), path.dirname(process.cwd())],
        deny: [],
      },
      warmup: {
        ssrFiles: ["src/pages/index.astro", "src/layouts/**/*", "src/styles/**/*"],
        clientFiles: ["src/styles/**/*"],
      },
    },
  },
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeSlug, rehypeCallouts, [rehypeKatex, { throwOnError: false }]],
  },
  build: {
    assets: "assets",
  },
});
