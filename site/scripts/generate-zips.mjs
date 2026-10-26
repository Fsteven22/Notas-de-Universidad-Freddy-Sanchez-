#!/usr/bin/env node
/**
 * generate-zips.mjs — Crea un .zip por materia con todos sus PDFs.
 * Se ejecuta después del sync para dejar los zip listos en public/downloads/.
 */
import { mkdir, readdir, readFile, writeFile, stat } from "node:fs/promises";
import { join } from "node:path";
import JSZip from "jszip";

const PROJECT = process.cwd();
const ASSETS_ROOT = join(PROJECT, "public", "assets");
const DOWNLOADS_DIR = join(PROJECT, "public", "downloads");

async function walk(dir, acc = []) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const full = join(dir, entry.name);
    if (entry.isDirectory()) {
      await walk(full, acc);
    } else if (/\.pdf$/i.test(entry.name)) {
      acc.push(full);
    }
  }
  return acc;
}

async function main() {
  await mkdir(DOWNLOADS_DIR, { recursive: true });
  const semestres = await readdir(ASSETS_ROOT, { withFileTypes: true });
  let totalZips = 0;

  for (const sem of semestres) {
    if (!sem.isDirectory()) continue;
    const semDir = join(ASSETS_ROOT, sem.name);
    const materias = await readdir(semDir, { withFileTypes: true });

    for (const mat of materias) {
      if (!mat.isDirectory()) continue;
      const matDir = join(semDir, mat.name);
      const pdfs = await walk(matDir, []);
      if (pdfs.length === 0) continue;

      const zip = new JSZip();
      for (const pdfPath of pdfs) {
        const rel = pdfPath.slice(matDir.length + 1);
        const content = await readFile(pdfPath);
        zip.file(rel, content);
      }

      const zipName = `${sem.name}-${mat.name}.zip`;
      const zipPath = join(DOWNLOADS_DIR, zipName);
      const buffer = await zip.generateAsync({ type: "nodebuffer" });
      await writeFile(zipPath, buffer);
      totalZips++;
      console.log(`✓ ${zipName} (${pdfs.length} PDFs)`);
    }
  }

  console.log(`✓ ${totalZips} ZIPs generados en public/downloads/`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
