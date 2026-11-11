import { defineConfig } from "astro/config";
import path from "node:path";
import react from "@astrojs/react";
import tailwindcss from "@tailwindcss/vite";
import rehypeSlug from "rehype-slug";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import { rehypeCallouts } from "./src/lib/rehype-callouts.mjs";
import { rehypeFlashcards } from "./src/lib/rehype-flashcards.mjs";
import { rehypeAssetOmitido } from "./src/lib/rehype-asset-omitido.mjs";
import { rehypeH1Demote } from "./src/lib/rehype-h1-demote.mjs";
import { rehypeImgLazy } from "./src/lib/rehype-img-lazy.mjs";

export default defineConfig({
  site: "https://neonotes-espol.vercel.app",
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
      rehypePlugins: [rehypeSlug, rehypeCallouts, rehypeFlashcards, rehypeAssetOmitido, [rehypeKatex, { throwOnError: false }], rehypeH1Demote, rehypeImgLazy],
  },
  build: {
    assets: "assets",
  },
});
