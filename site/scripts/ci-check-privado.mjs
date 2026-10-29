#!/usr/bin/env node
/**
 * ci-check-privado.mjs — red de seguridad P3 para CI.
 *
 * Verifica que ningún archivo listado en Universidad/_no-publicar.txt
 * (patrones con comodines * y ?, match por nombre o ruta relativa) haya
 * llegado publicado en:
 *   - public/assets/            (directo, tras npm run sync)
 *   - public/downloads/*.zip    (ZIPs por materia, tras npm run zips)
 *
 * Sale con codigo != 0 si encuentra alguna fuga (para que el CI falle).
 *
 * Uso:
 *   node scripts/ci-check-privado.mjs          (desde la raiz de site/)
 *   node scripts/ci-check-privado.mjs --vault ../Universidad
 */

import { readdir } from "node:fs/promises";
import { existsSync, readdirSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { execSync } from "node:child_process";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PROJECT = path.resolve(HERE, "..");
const DEFAULT_VAULT = path.join(PROJECT, "..", "Universidad");

function globToRegex(pat) {
  let out = "";
  for (const ch of pat) {
    if (ch === "*") out += ".*";
    else if (ch === "?") out += ".";
    else out += ch.replace(/[.+^${}()|[\]\\]/g, "\\$&");
  }
  return new RegExp("^" + out + "$", "i");
}

async function leerNoPublicar(vault) {
  const file = path.join(vault, "_no-publicar.txt");
  if (!existsSync(file)) return [];
  const fs = await import("node:fs/promises");
  const text = await fs.readFile(file, "utf8");
  return text
    .split("\n")
    .map((l) => l.trim())
    .filter((l) => l && !l.startsWith("#"));
}

async function walkAssets(dir, reNP, relBase) {
  const encontrados = [];
  if (!existsSync(dir)) return encontrados;
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    const rel = relBase ? relBase + "/" + entry.name : entry.name;
    if (entry.isDirectory()) {
      encontrados.push(...(await walkAssets(full, reNP, rel)));
    } else {
      const nombre = entry.name;
      if (reNP.some((re) => re.test(nombre) || re.test(rel))) {
        encontrados.push(rel);
      }
    }
  }
  return encontrados;
}

function listarZip(zipPath) {
  try {
    const out = execSync("unzip -l \"" + zipPath + "\"", {
      encoding: "utf8",
      maxBuffer: 50 * 1024 * 1024,
    });
    const lineas = out.split("\n");
    const archivos = [];
    let enCuerpo = false;
    for (const l of lineas) {
      const t = l.trim();
      if (t.startsWith("----")) {
        enCuerpo = !enCuerpo;
        continue;
      }
      if (!enCuerpo) continue;
      const partes = t.split(/\s+/);
      if (partes.length >= 4) {
        archivos.push(partes.slice(3).join(" "));
      }
    }
    return archivos;
  } catch (e) {
    console.warn("  (no se pudo listar " + path.basename(zipPath) + ": " + e.message + ")");
    return [];
  }
}

async function main() {
  const args = process.argv.slice(2);
  let vault = DEFAULT_VAULT;
  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--vault" && i + 1 < args.length) {
      vault = args[i + 1];
      i++;
    }
  }

  const patrones = await leerNoPublicar(vault);
  const reNP = patrones.map(globToRegex);

  console.log("CI-PRIVADO: " + patrones.length + " patrones de _no-publicar.txt");
  console.log("Vault: " + vault);
  console.log("Proyecto: " + PROJECT);

  let fugas = 0;

  // 1. public/assets/
  const assetsDir = path.join(PROJECT, "public", "assets");
  const fugasAssets = await walkAssets(assetsDir, reNP, "");
  for (const f of fugasAssets) {
    console.error("  FUGA assets: " + f);
    fugas++;
  }
  console.log("✓ public/assets/ escaneado: " + fugasAssets.length + " coincidencias");

  // 2. public/downloads/*.zip
  const downloadsDir = path.join(PROJECT, "public", "downloads");
  if (existsSync(downloadsDir)) {
    for (const zip of readdirSync(downloadsDir)) {
      if (!zip.toLowerCase().endsWith(".zip")) continue;
      const zipPath = path.join(downloadsDir, zip);
      const internos = listarZip(zipPath);
      const fugasZip = internos.filter((nombre) => reNP.some((re) => re.test(nombre)));
      for (const f of fugasZip) {
        console.error("  FUGA zip " + zip + ": " + f);
        fugas++;
      }
      console.log("✓ " + zip + ": " + internos.length + " archivos listados, " + fugasZip.length + " coincidencias");
    }
  } else {
    console.log("ℹ public/downloads/ no existe (todavía no se generaron ZIPs)");
  }

  console.log("");
  if (fugas > 0) {
    console.error("CI-PRIVADO: FALLO — " + fugas + " archivo(s) excluido(s) publicado(s)");
    process.exit(1);
  } else {
    console.log("CI-PRIVADO: OK — ningún archivo excluido publicado");
    process.exit(0);
  }
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
