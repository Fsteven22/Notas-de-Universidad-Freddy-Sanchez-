#!/usr/bin/env node
/**
 * sync-vault.mjs — Ingesta del vault Obsidian → notas-nexus
 * Lee OneSyncFiles/Universidad, copia notas y assets al repo,
 * reescribe wikilinks/embeds, convierte flashcards, genera vault.json.
 *
 * Uso: npm run sync   (desde la raíz del proyecto)
 */
import { mkdir, rm, writeFile, copyFile, readdir, readFile, stat } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PROJECT = path.resolve(HERE, "..");
// VAULT_DIR: ruta al vault. Local = OneDrive; en CI (Vercel/build) = "../Universidad"
// relativo a la raíz del site, o absoluto — siempre se resuelve desde process.cwd().
const VAULT = process.env.VAULT_DIR
  ? path.resolve(process.cwd(), process.env.VAULT_DIR)
  : path.join(process.env.USERPROFILE, "OneDrive", "OneSyncFiles", "Universidad");

const OUT_CONTENT = path.join(PROJECT, "notes-md");
const OUT_ASSETS = path.join(PROJECT, "public", "assets");
const OUT_DATA = path.join(PROJECT, "src", "data");

/* ── helpers ─────────────────────────────────────────────── */

function slugify(s) {
  return s
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/[''`]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 64) || "n";
}

function prettyTitle(filename) {
  let t = filename.replace(/\.md$/i, "");
  t = t.replace(/^\d+[\s.\-_]+/, "");          // "04 - Precisión" → "Precisión"
  t = t.replace(/^[IVX]+[\s.\-]+(?=\w)/i, ""); // "III - Derivadas" → "Derivadas"
  t = t.replace(/^\d+(?:\.\d+)*\s*[-–—]\s*/, ""); // "1.2 - X" → "X"
  return t.trim() || filename;
}

const SEMESTER_IDS = {
  "Preuniversitario": { id: "preuniversitario", title: "Preuniversitario", order: 0 },
  "1er Semestre": { id: "1er-semestre", title: "1er Semestre", order: 1 },
  "2do Semestre": { id: "2do-semestre", title: "2do Semestre", order: 2 },
  "3er Semestre": { id: "3er-semestre", title: "3er Semestre", order: 3 },
};
const RAIZ = { id: "raiz", title: "Universidad", order: 4 };

const MD_EXT = /\.(md|markdown)$/i;
const IMG_EXT = /\.(png|jpe?g|gif|svg|webp|avif|bmp)$/i;
const MEDIA_EXT = /\.(png|jpe?g|gif|svg|webp|avif|bmp|pdf|docx?|pptx?|mp4|mp3|wav|ogg|xlsx?|zip)$/i;
const PDF_VIEWER = "/pdfjs/viewer.html?file=";
const PDF_MAX_INLINE_BYTES = 25 * 1024 * 1024; // PDFs mayores: solo descarga, no visor embebido

/** Carpetas de la RAÍZ del vault con assets globales referenciables desde
 *  cualquier materia (imágenes, diagramas). Copiadas a /assets/raiz/… */
const ROOT_ASSET_DIRS = ["Figuras", "Diagramas"];

/** Gate de publicación (Fase 1): una nota va al site solo si su frontmatter
 *  inicial declara `dg-publish: true`. Sin frontmatter = omitida. */
function isPublished(raw) {
  const m = raw.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  return !!m && /(^|\n)\s*dg-publish:\s*true\b/i.test(m[1]);
}

const ASSET_SKIP = [
  MD_EXT,
  /^__pycache__$/,
  /^\.(git|obsidian|stfolder|stignore)/,
  /node_modules/,
  /\.(tmp|bak)$/i,
];

/* ── _no-publicar.txt ─────────────────────────────────────────
 * Lista de archivos que nunca se suben al sitio (patrones de nombre,
 * comodín * y ?). Se lee desde la raíz de Universidad.            */
const NO_PUBLICAR_FILE = path.join(VAULT, "_no-publicar.txt");

async function leerNoPublicar() {
  try {
    const txt = await readFile(NO_PUBLICAR_FILE, "utf8");
    return txt
      .split(/\r?\n/)
      .map((l) => l.trim())
      .filter((l) => l && !l.startsWith("#"));
  } catch {
    return [];
  }
}

function globToRegex(pat) {
  const esc = pat.replace(/[.+^${}()|[\]\\]/g, "\\$&").replace(/\*/g, ".*").replace(/\?/g, ".");
  return new RegExp(`^${esc}$`, "i");
}

/** Assets (imágenes/PDF/etc.) que menciona una nota: embeds ![[x]], wikilinks
 *  [[x]] y enlaces markdown ![](x) / [](x). Se comparan por nombre de archivo. */
function referenciasMedia(raw) {
  const out = new Set();
  const add = (ref) => {
    const clean = ref.trim().split("|")[0].split("#")[0].trim();
    if (!clean || /^(https?:|data:|mailto:|#)/i.test(clean)) return;
    const base = path.basename(clean);
    if (MEDIA_EXT.test(base)) out.add(base.toLowerCase());
  };
  for (const m of raw.matchAll(/!\[\[([^\]|#]+)/g)) add(m[1]);
  for (const m of raw.matchAll(/\[\[([^\]|#]+)/g)) add(m[1]);
  for (const m of raw.matchAll(/!?\[[^\]]*\]\(([^)\s]+)/g)) add(m[1]);
  return out;
}

async function walk(dir, acc = { files: [], dirs: [] }, base = dir) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.name.startsWith(".") || entry.name === "__pycache__" || entry.name === "_privado" || /node_modules/.test(entry.name)) continue;
    if (entry.isDirectory()) {
      acc.dirs.push({ name: entry.name, full, rel: path.relative(base, full).split(path.sep).join("/") });
      await walk(full, acc, base);
    } else {
      const st = await stat(full);
      acc.files.push({ name: entry.name, full, rel: path.relative(base, full).split(path.sep).join("/"), size: st.size });
    }
  }
  return acc;
}

/* ── fases ───────────────────────────────────────────────── */

/** Fase A: armamos el esqueleto semestre → materia y volcamos su contenido */
function buildSkeleton(dirs) {
  const semestres = new Map(); // semId → {…, materias: Map(matId → {…})}
  const ensureSem = (info) => {
    if (!semestres.has(info.id))
      semestres.set(info.id, { ...info, materias: new Map() });
    return semestres.get(info.id);
  };
  const seenSemDirs = new Set();
  for (const d of dirs) {
    const top = d.rel.split("/")[0];
    const sem = SEMESTER_IDS[top];
    if (sem && !seenSemDirs.has(top)) {
      seenSemDirs.add(top);
      ensureSem(sem);
    }
  }
  return { semestres, ensureSem };
}

async function main() {
  console.log("→ Leyendo vault:", VAULT);
  if (!existsSync(VAULT)) throw new Error("No existe el vault");

  const rootWalk = await walk(VAULT);

  // sincronía incremental: NO borramos nada de entrada;
  // los archivos que no cambien se dejan intactos (evita tempestad de reload
  // en el dev-server). Huérfanos se limpian al final.
  await mkdir(OUT_CONTENT, { recursive: true });
  await mkdir(OUT_ASSETS, { recursive: true });
  await mkdir(OUT_DATA, { recursive: true });
  const writtenNotes = new Set();
  const copiedAssets = new Set();

  async function writeFileIfChanged(abs, content, relKey) {
    try {
      const old = await readFile(abs, "utf8");
      if (old === content) {
        writtenNotes.add(relKey);
        return;
      }
    } catch {}
    await writeFile(abs, content, "utf8");
    writtenNotes.add(relKey);
  }

  async function copyIfChanged(src, dest, relKey) {
    try {
      const a = await stat(src);
      const b = await stat(dest);
      if (a.size === b.size && Math.abs(a.mtimeMs - b.mtimeMs) < 2000) {
        copiedAssets.add(relKey);
        return;
      }
    } catch {}
    await copyFile(src, dest);
    copiedAssets.add(relKey);
  }

  // ── 1. descubrir (semestre, materia) y asociar notas.
  // Solo carpetas "Semestre conocido / materia": los dirs sueltos de la raíz
  // (Herramientas, Diagramas, Figuras, …) son zona interna del vault y jamás
  // generan materias fantasma bajo `raiz` (Hallazgo 1 de la Fase 2).
  const subjDirs = rootWalk.dirs
    .filter((d) => d.rel.split("/").length === 2) // "sem/materia"
    .filter((d) => !!SEMESTER_IDS[d.rel.split("/")[0]]);
  const raizDir = { name: "General", full: VAULT, rel: "." };

  const semMap = new Map();
  const candidates = [...subjDirs, { ...raizDir, sem: RAIZ }];
  for (const d of subjDirs) {
    const top = d.rel.split("/")[0];
    const semInfo = SEMESTER_IDS[top] || RAIZ;
    if (!semMap.has(semInfo.id)) semMap.set(semInfo.id, { ...semInfo, materias: [] });
  }
  semMap.set(RAIZ.id, { ...RAIZ, materias: [] });

  const linkMap = new Map(); // título de nota → url
  const assetMaps = new Map(); // "sem/mat" y "sem/*" y "raiz" → Map(base→assetUrl)

  // ── 1a. reglas de publicación de assets:
  //   · _no-publicar.txt  → nunca se suben (copyright, material propio ya en PDF)
  //   · solo se sube lo que menciona alguna nota PUBLICADA
  const patronesNP = await leerNoPublicar();
  const reNP = patronesNP.map(globToRegex);
  const esPrivado = (nombre, rel = "") =>
    reNP.some((re) => re.test(nombre) || re.test(rel));
  const privadosVistos = new Set();

  // pre-pasada: assets mencionados por notas publicadas (gate dg-publish)
  const referidos = new Set();
  for (const f of rootWalk.files) {
    if (!MD_EXT.test(f.name) || f.name.startsWith(".")) continue;
    const partes = f.rel.split("/");
    // el sitio solo publica notas de semestre/materia y las de la raíz
    if (partes.length > 1 && !SEMESTER_IDS[partes[0]]) continue;
    let raw;
    try {
      raw = await readFile(f.full, "utf8");
    } catch {
      continue;
    }
    if (!isPublished(raw)) continue;
    for (const r of referenciasMedia(raw)) referidos.add(r);
  }
  console.log(`✓ assets referenciados por notas publicadas: ${referidos.size}`);

  // ── 1b. assets globales de la raíz del vault (Figuras/, Diagramas/ y
  // sueltos en la primera capa): alimentan el mapa "raiz" que consultará
  // resolveAsset desde cualquier materia. No generan materias fantasma
  // (el Hallazgo 1 sigue válido: son assets, no notas).
  const raizAssets = new Map();
  const rootAssetFiles = rootWalk.files.filter((f) => {
    const top = f.rel.split("/")[0];
    const isRootDir = ROOT_ASSET_DIRS.includes(top);
    const isTopLevel = !f.rel.includes("/");
    return (
      (isRootDir || isTopLevel) &&
      !MD_EXT.test(f.name) &&
      !f.name.startsWith(".") &&
      MEDIA_EXT.test(f.name) &&
      f.name !== "_no-publicar.txt"
    );
  });
  for (const f of rootAssetFiles) {
    if (esPrivado(f.name, f.rel)) {
      privadosVistos.add(f.rel);
      continue;
    }
    if (!referidos.has(f.name.toLowerCase())) continue; // nadie lo usa → no se sube
    const rel = f.rel.split("/");
    const fileName = rel[rel.length - 1];
    const dirs = rel.slice(0, -1).map(slugify);
    const url = `/assets/raiz/${[...dirs, fileName].join("/")}`;
    const dest = path.join(OUT_ASSETS, "raiz", ...dirs, fileName);
    await mkdir(path.dirname(dest), { recursive: true });
    await copyIfChanged(f.full, dest, url.slice("/assets/".length));
    if (!raizAssets.has(fileName)) raizAssets.set(fileName, { url, size: f.size ?? 0 });
  }
  assetMaps.set("raiz", raizAssets);
  const notas = [];
  const omitidas = []; // Fase 1: notas sin `dg-publish: true` → fuera del site
  const pdfsPorMat = new Map();

  for (const subj of candidates) {
    const semInfo = subj.sem || SEMESTER_IDS[subj.rel.split("/")[0]] || RAIZ;
    const sem = semMap.get(semInfo.id) || { ...semInfo, materias: [] };
    const isRaiz = subj.rel === ".";
    const subjectName = isRaiz ? "General" : subj.name;
    const matId = slugify(subjectName);
    const contentDir = path.join(OUT_CONTENT, sem.id, matId);
    const assetDir = path.join(OUT_ASSETS, sem.id, matId);

    // ── 2. copiar assets de esta materia (recursivo, conserva nombre de archivo)
    const w = isRaiz ? { files: [], dirs: [] } : await walk(subj.full);
    const assets = new Map(); // base → assetUrl (relativo público)
    for (const f of w.files) {
      if (MD_EXT.test(f.name) || f.name.startsWith(".")) continue;
      if (esPrivado(f.name, f.rel)) {
        privadosVistos.add(f.rel);
        continue;
      }
      if (!referidos.has(f.name.toLowerCase())) continue; // nadie lo usa → no se sube
      const rel = f.rel.split("/");
      const fileName = rel[rel.length - 1];
      const dirs = rel.slice(0, -1).map(slugify);
      const url = `/assets/${sem.id}/${matId}/${[...dirs, fileName].join("/")}`;
      const dest = path.join(assetDir, ...dirs, fileName);
      await mkdir(path.dirname(dest), { recursive: true });
      await copyIfChanged(f.full, dest, url.slice("/assets/".length));
      if (!assets.has(fileName)) assets.set(fileName, { url, size: f.size ?? 0 });
    }
    assetMaps.set(`${sem.id}/${matId}`, assets);

    // ── 3. procesar notas (*.md)
    const mdFiles = w.files.filter((f) => MD_EXT.test(f.name) && !f.name.startsWith("."));
    if (isRaiz) {
      // raíz de Universidad: solo notas sueltas (primera capa, sin recursión)
      for (const f of await readdir(VAULT)) {
        if (MD_EXT.test(f)) {
          const st = await stat(path.join(VAULT, f));
          mdFiles.push({ name: f, full: path.join(VAULT, f), rel: f, mtimeMs: st.mtimeMs });
        }
      }
    }

    const materia = { id: matId, title: subjectName, notas: [], pdfs: [] };
    sem.materias.push(materia);

    for (const f of mdFiles) {
      const mtime = f.mtimeMs ?? (await stat(f.full)).mtimeMs;
      const rel = f.rel.split("/");
      const fileName = rel[rel.length - 1];

      // ── gate de publicación: primero se lee la nota, luego se decide
      const raw = await readFile(f.full, "utf8");
      if (!isPublished(raw)) {
        omitidas.push({ sem: sem.id, mat: subjectName, rel: f.rel });
        continue;
      }

      const title = prettyTitle(fileName);
      const unitPath = rel.slice(0, -1).map(slugify); // slugs de unidades anidadas
      const noteDir = path.join(contentDir, ...unitPath);
      await mkdir(noteDir, { recursive: true });

      const out = await transformNote(raw, {
        sem: sem.id,
        mat: matId,
        assetMaps,
      });
      const slug = slugify(fileName.replace(/\.md$/i, ""));
      const outRel = `${sem.id}/${matId}${unitPath.length ? "/" + unitPath.join("/") : ""}/${slug}.md`;
      await writeFileIfChanged(path.join(OUT_CONTENT, outRel), out.content, outRel);

      const noteEntry = {
        slug,
        title,
        units: unitPath,
        file: outRel.replace(/\.md$/, ""),
        mtime,
      };
      materia.notas.push(noteEntry);
      notas.push({ ...noteEntry, sem: sem.id, semTitle: sem.title, mat: matId, matTitle: subjectName });
      linkMap.set(fileName.replace(/\.md$/i, ""), noteEntry.file);
      linkMap.set(title.toLowerCase(), noteEntry.file);
    }

    // PDFs de esta materia
    materia.pdfs = [...assets.entries()]
      .filter(([n]) => /\.pdf$/i.test(n))
      .map(([name, url]) => ({ title: prettyTitle(name), url }));
  }

  // ── 4. segunda pasada: resolver wikilinks con el mapa global
  for (const nota of notas) {
    const file = path.join(OUT_CONTENT, nota.file + ".md");
    const relKey = nota.file + ".md";
    const old = await (await import("node:fs/promises")).readFile(file, "utf8");
    const txt = resolveWikilinks(old, linkMap, (base) => resolveAsset(base, nota.sem, nota.mat, assetMaps));
    if (txt !== old) await writeFile(file, txt, "utf8");
    writtenNotes.add(relKey);
  }

  // ── limpieza de huérfanos
  for (const [baseDir, keep] of [
    [OUT_CONTENT, writtenNotes],
    [OUT_ASSETS, copiedAssets],
  ]) {
    const stack = [baseDir];
    while (stack.length) {
      const dir = stack.pop();
      for (const e of await readdir(dir, { withFileTypes: true })) {
        const full = path.join(dir, e.name);
        const rel = path.relative(baseDir, full).split(path.sep).join("/");
        if (e.isDirectory()) {
          stack.push(full);
        } else if (!keep.has(rel)) {
          await rm(full, { force: true });
        }
      }
    }
  }

  // ── 5. vault.json
  const semList = [...semMap.values()]
    .filter((s) => s.materias.length > 0)
    .sort((a, b) => a.order - b.order)
    .map((s) => ({
      id: s.id,
      title: s.title,
      materias: s.materias
        .sort((a, b) => a.title.localeCompare(b.title, "es"))
        .map((m) => ({ ...m, total: m.notas.length })),
    }));

  const recent = [...notas]
    .sort((a, b) => b.mtime - a.mtime)
    .slice(0, 6)
    .map((n) => ({
      title: n.title,
      sem: n.sem,
      semTitle: n.semTitle,
      mat: n.mat,
      matTitle: n.matTitle,
      url: `/${n.sem}/${n.mat}${n.units.length ? "/" + n.units.join("/") : ""}/${n.slug}/`,
      mtime: n.mtime,
    }));

  const data = {
    stats: { notas: notas.length, semestres: semList.length, actualizado: recent[0]?.mtime ?? Date.now() },
    semestres: semList,
    recent,
  };
  const dataStr = JSON.stringify(data, null, 1);
  const vaultPath = path.join(OUT_DATA, "vault.json");
  let vaultOld = "";
  try {
    vaultOld = await readFile(vaultPath, "utf8");
  } catch {}
  if (vaultOld !== dataStr) {
    await writeFile(vaultPath, dataStr, "utf8");
    console.log("✓ vault.json actualizado");
  }

  // ── 6. índice de búsqueda (público, para el modal)
  const searchIndex = notas
    .map((n) => ({
      t: n.title,
      m: n.matTitle,
      s: n.semTitle,
      u: `/${n.sem}/${n.mat}${n.units.length ? "/" + n.units.join("/") : ""}/${n.slug}/`,
      mt: n.mtime,
    }))
    .sort((a, b) => a.t.localeCompare(b.t, "es"));
  const searchStr = JSON.stringify(searchIndex);
  const searchPath = path.join(process.cwd(), "public", "search-index.json");
  let searchOld = "";
  try {
    searchOld = await readFile(searchPath, "utf8");
  } catch {}
  if (searchOld !== searchStr) {
    await writeFile(searchPath, searchStr, "utf8");
    console.log("✓ search-index.json actualizado");
  }

  // Visor PDF: recursos estaticos de pdf.js servidos desde el mismo origen
  const pdfjsSrc = path.join(PROJECT, "node_modules", "pdfjs-dist");
  const pdfjsDst = path.join(PROJECT, "public", "pdfjs");
  if (existsSync(pdfjsSrc)) {
    await mkdir(pdfjsDst, { recursive: true });
    const srcBuild = path.join(pdfjsSrc, "build");
    const dstBuild = path.join(pdfjsDst, "build");
    if (existsSync(srcBuild)) {
      await rm(dstBuild, { recursive: true, force: true });
      await mkdir(dstBuild, { recursive: true });
      let copied = 0;
      for (const f of await readdir(srcBuild)) {
        // sin sourcemaps ni sandbox: el visor propio no los usa y multiplican el peso del deploy
        if (f.endsWith(".map") || f.startsWith("pdf.sandbox")) continue;
        await copyFile(path.join(srcBuild, f), path.join(dstBuild, f));
        copied++;
      }
      console.log(`V pdf.js copiado a public/pdfjs/build (${copied} archivos)`);
    }
    // public/pdfjs/web no se usa: nuestro visor vive en public/pdfjs/viewer.html
    await rm(path.join(pdfjsDst, "web"), { recursive: true, force: true });
  }

  // ── 7. sitemap.xml y robots.txt (SEO básico, Fase 7.3)
  const SITE_URL = "https://neonotes-espol.vercel.app";
  const sitemapUrls = [];
  sitemapUrls.push(`<url><loc>${SITE_URL}/</loc><lastmod>${new Date(Math.max(0, data.stats.actualizado)).toISOString()}</lastmod></url>`);
  for (const s of [...semMap.values()].sort((a, b) => a.order - b.order)) {
    sitemapUrls.push(`<url><loc>${SITE_URL}/${s.id}/</loc><lastmod>${new Date(Math.max(0, data.stats.actualizado)).toISOString()}</lastmod></url>`);
    for (const m of s.materias.sort((a, b) => a.title.localeCompare(b.title, "es"))) {
      sitemapUrls.push(`<url><loc>${SITE_URL}/${s.id}/${m.id}/</loc><lastmod>${new Date(Math.max(0, data.stats.actualizado)).toISOString()}</lastmod></url>`);
      for (const n of m.notas) {
        const units = n.units?.length ? "/" + n.units.join("/") : "";
        sitemapUrls.push(`<url><loc>${SITE_URL}/${s.id}/${m.id}${units}/${n.slug}/</loc><lastmod>${new Date(n.mtime).toISOString()}</lastmod></url>`);
      }
    }
  }
  const sitemapXml = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${sitemapUrls.join("\n")}
</urlset>`;
  await writeFile(path.join(PROJECT, "public", "sitemap.xml"), sitemapXml, "utf8");

  const robotsTxt = `User-agent: *
Allow: /

Sitemap: ${SITE_URL}/sitemap.xml`;
  await writeFile(path.join(PROJECT, "public", "robots.txt"), robotsTxt, "utf8");

  console.log(`✓ ${notas.length} notas publicadas · ${omitidas.length} omitidas (sin dg-publish)`);
  if (omitidas.length) {
    for (const o of omitidas) console.log(`  · omitida: ${o.sem}/${o.mat}/${o.rel}`);
  }
  if (patronesNP.length) {
    console.log(`✓ _no-publicar.txt: ${patronesNP.length} patrones · ${privadosVistos.size} archivos excluidos`);
    for (const p of privadosVistos) console.log(`  · no publicado: ${p}`);
  }
  console.log(`✓ ${notas.length} notas · ${semList.length} bloques · sync incremental listo`);
}

/* ── transformaciones por nota ───────────────────────────── */

async function transformNote(raw, { sem, mat, assetMaps }) {
  let t = raw;

  // frontmatter out (para no tocarlo): preservar bloque yaml inicial
  // pero saneado: primera ocurrencia gana si hay claves duplicadas
  let fm = "";
  const fmMatch = t.match(/^---\n[\s\S]*?\n---\n/);
  if (fmMatch) {
    const blocks = fmMatch[0].split("\n");
    const seen = new Set();
    const clean = [];
    for (const line of blocks) {
      const km = line.match(/^([A-Za-z][\w-]*):/);
      if (km) {
        if (seen.has(km[1])) continue;
        seen.add(km[1]);
      }
      clean.push(line);
    }
    fm = clean.join("\n") + "\n";
    t = t.slice(fmMatch[0].length);
  }

  // quitar comentarios SR (ruido para la web)
  t = t.replace(/<!--SR:.*?-->/g, "");
  // "Tags: #a #b …" → chips visuales en vez de texto crudo
  t = t.replace(/^[ \t_]*(\*\*)?[ \t]*(Tags?|Etiquetas)[ \t]*(\*\*)?[ \t]*:(.*)$/gim, (m, b1, k, b2, rest) => {
    rest = (rest || "").trim();
    if (!rest || !rest.includes("#")) return m;
    const chips = rest
      .split(/\s+/)
      .filter((w) => w.startsWith("#"))
      .map((w) => `<span class="nx-tag">${escapeHtml(w)}</span>`)
      .join(" ");
    return chips ? `<p class="nx-tags">${chips}</p>` : m;
  });

  // flashcards Q::A → <details>
  t = transformFlashcards(t);

  // tarjeta de documento para embeds no-imagen (pdf, docx, mp4, …)
  const docCard = (label, url) =>
    `<div class="nx-doc"><a href="${encodeURI(url)}" target="_blank" rel="noopener">📄 ${escapeHtml(label)}</a></div>`;


  // visor PDF embebido con carga diferida: el HTML solo guarda la URL y el
  // navegador inserta el iframe cuando la tarjeta entra en pantalla. Dentro,
  // pdf.js renderiza las páginas de forma progresiva. PDFs > 25 MB: solo descarga.
  const pdfViewer = (label, url, size) => {
    const bytes = Number(size) || 0;
    const mb = (bytes / 1048576).toFixed(1);
    const heavy = bytes > PDF_MAX_INLINE_BYTES;
    const safeUrl = encodeURI(url);
    const meta = heavy ? `${mb} MB · archivo pesado, conviene descargarlo` : `${mb} MB`;
    const action = heavy
      ? `<a href="${safeUrl}" target="_blank" rel="noopener">Abrir en pestaña nueva</a>`
      : `<button type="button" class="nx-pdf-open" data-nx-pdf-open>Ver PDF</button>`;
    const src = heavy ? "" : ` data-nx-pdf-src="${PDF_VIEWER}${encodeURIComponent(url)}"`;
    return `<div class="nx-pdf"${src} data-nx-pdf-bytes="${bytes}"><div class="nx-pdf-bar"><span class="nx-pdf-name">${escapeHtml(label)}</span><span class="nx-pdf-meta">${meta}</span><span class="nx-pdf-acts">${action}<a href="${safeUrl}" target="_blank" rel="noopener" download>Descargar</a></span></div><div class="nx-pdf-slot"></div></div>`;
  };

  // embeds ![[file]] → imagen codificada, tarjeta de doc, o comentario si no existe
  t = t.replace(/!\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]/g, (_, name) => {
    const label = name.trim();
    const info = resolveAssetInfo(label, sem, mat, assetMaps);
    if (!info) {
      // embebido de una NOTA (sin extensión de media): se deja como wikilink
      // para que la 2ª pasada lo convierta en enlace a la nota.
      if (!MEDIA_EXT.test(path.basename(label))) return `[[${label}]]`;
      return `<!-- nx:asset-omitido ${escapeHtml(label)} -->`;
    }
    if (IMG_EXT.test(info.url)) return `![${label}](${encodeURI(info.url)})`;
    return info.url.toLowerCase().endsWith(".pdf") ? pdfViewer(label, info.url, info.size) : docCard(label, info.url);
  });
  // links markdown relatives a media → absolutos (fout ! ya fue manejado):
  t = t.replace(/(?<!!)\[([^\]]*)\]\(([^)]+)\)/g, (m, alt, src) => {
    if (/^(https?:|\/|data:|mailto:|#)/.test(src)) return m;
    const url = resolveAsset(src.replace(/[<>"']/g, "").trim(), sem, mat, assetMaps);
    if (!url) return m;
    return `[${alt}]( ${encodeURI(url)} )`.replace(/\(\s+/g, "(").replace(/\s+\)/g, ")");
  });

  // embeds markdown con ruta relativa → absoluta pública (mismo criterio)
  t = t.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, (m, alt, src) => {
    if (/^(https?:|\/|data:)/.test(src)) return m;
    const info = resolveAssetInfo(src.replace(/[<>"']/g, "").trim(), sem, mat, assetMaps);
    if (!info) return `<!-- nx:asset-omitido ${escapeHtml((alt || src).trim())} -->`;
    if (IMG_EXT.test(info.url)) return `![${alt}](${encodeURI(info.url)})`;
    const mLabel = alt.trim() || src.trim();
    return info.url.toLowerCase().endsWith(".pdf") ? pdfViewer(mLabel, info.url, info.size) : docCard(mLabel, info.url);
  });

  // lenguas de fence no soportadas por shiki → sin anotación
  // (cubre "```mathematica" al inicio y "```mathematica" dentro de blockquotes, con o sin \r)
  t = t.replace(/(^[\t ]*>?[\t ]*```)[\t ]*mathematica.*$/gim, "$1");

  return { content: fm + t };
}

function resolveAssetInfo(name, sem, mat, assetMaps) {
  const base = path.basename(name);
  const tries = [`${sem}/${mat}`, `${sem}/*`, `raiz`];
  for (const key of tries) {
    const map = assetMaps.get(key);
    if (map && map.has(base)) return map.get(base);
  }
  // fallback: buscar en todas las materias del mismo semestre
  for (const [key, map] of assetMaps.entries()) {
    if (key.startsWith(sem + "/") && map.has(base)) return map.get(base);
    if (key === `raiz` && map.has(base)) return map.get(base);
  }
  return null;
}

function resolveAsset(name, sem, mat, assetMaps) {
  const info = resolveAssetInfo(name, sem, mat, assetMaps);
  return info ? info.url : null;
}

function transformFlashcards(t) {
  const lines = t.split("\n");
  let inFence = false, inFm = false, fmCount = 0;
  const out = [];
  for (let line of lines) {
    if (line.startsWith("```")) inFence = !inFence;
    if (line.trim() === "---") { fmCount++; if (fmCount === 2) inFm = false; else if (fmCount === 1) inFm = true; }

    if (!inFence && !inFm && /^(?!\s*[-*>#\[\[])(?![\d]+[.)] )\s*([^:\n]+?)\s*::(\s*[^:\n].*)?$/.test(line)) {
      const m = line.match(/^(?!\s*[-*>#\[\[])(?![\d]+[.)] )\s*([^:\n]+?)\s*::(\s*[^:\n].*)?$/);
      if (m) {
        const q = escapeHtml(m[1].trim());
        const a = m[2] ? escapeHtml(m[2].trim()) : "";
        out.push(`<details class="nx-fc"><summary>${q}</summary><p>${a}</p></details>`);
        out.push("");
        continue;
      }
    }
    out.push(line);
  }
  return out.join("\n");
}

function escapeHtml(s) {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function resolveWikilinks(t, linkMap, resolveMediaLink) {
  // 1) wikilinks a MEDIA (sin !): [[file.pdf|alias]] / [[file.png]] →
  //    en Obsidian se ven como links clickeables; en la web emiten
  //    link a /assets/... o se descartan si el asset no existe.
  t = t.replace(/\[\[([^\]|#]+)\.([a-z0-9]+)(#[^\]|]*)?(?:\|([^\]]+))?\]\]/gi, (m, stem, ext, anchor, alias) => {
    const base = path.basename((stem + "." + ext).trim());
    if (!MEDIA_EXT.test("." + ext)) return m;
    const url = resolveMediaLink(base);
    if (!url) return `<!-- nx:link-omitido ${escapeHtml(base)} -->`;
    if (anchor) return m; // anclas sobre media no tienen sentido: sin embed
    return `[${alias || `📄 ${base}`}](${encodeURI(url)})`;
  });
  // 2) [[Target#Sección|alias]] / [[Target|alias]] / [[Target]] → notas
  // [[Target#Sección|alias]] / [[Target|alias]] / [[Target]]
  t = t.replace(/\[\[([^\]|#]+)(#[^\]|]+)?(?:\|([^\]]+))?\]\]/g, (m, target, anchor, alias) => {
    if (!target.trim()) return m;
    // admite [[Carpeta/subcarpeta/Nota.md]] → usa solo el basename
    const baseName = target.trim().split("/").pop().replace(/\.md$/i, "");
    let key = baseName.toLowerCase();
    let entry =
      linkMap.get(baseName) ||
      linkMap.get(key) ||
      linkMap.get(prettyTitle(baseName).toLowerCase());
    if (!entry) return `**${alias || baseName}**`;
    let url = `/${entry}/`;
    if (anchor) {
      const a = anchor.slice(1);
      url += "#" + slugify(a.replace(/\s+/g, "-"));
    }
    return `[${alias || prettyTitle(baseName)}](${url})`;
  });
  return t;
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
