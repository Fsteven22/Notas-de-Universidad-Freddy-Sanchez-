#!/usr/bin/env node
/**
 * build-search-content.mjs — indice de CONTENIDO de las notas.
 *
 * El indice que ya existia (search-index.json, 186 KB) solo tiene por nota
 * {titulo, materia, semestre, url, mtime}: buscar "gradiente" solo encontraba
 * notas que se llamaran "Gradiente" y buscar "teorema de Rolle" no encontraba
 * nada aunque estuviera escrito en tres notas. Eso es lo que hacia que el
 * buscador pareciera inutil.
 *
 * Este script (corre como postbuild) recorre el HTML ya generado y extrae,
 * por cada apartado (h2/h3) de cada nota: el titulo del apartado, su ancla
 * real (la que puso rehype-slug) y los primeros caracteres de su texto.
 * Con eso el buscador puede decir "encontrado en el apartado X" y llevar al
 * ancla exacta en vez de al principio de la nota.
 *
 * Los anclas se leen del HTML final, no del markdown: asi son correctos de
 * serie, sin tener que replicar el algoritmo de rehype-slug.
 *
 * Salida: dist/search-content.json
 */
import { readdir, readFile, writeFile } from "node:fs/promises";
import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const HERE = path.dirname(fileURLToPath(import.meta.url));
const PROJECT = path.resolve(HERE, "..");
const DIST = path.join(PROJECT, "dist");
const VAULT_JSON = path.join(PROJECT, "src", "data", "vault.json");

/** caracteres de texto que se guardan por apartado */
const SNIPPET = 280;

// entidades por codepoint: no dependen de literales HTML en el fuente
const AMP = String.fromCharCode(38);
const LT = String.fromCharCode(60);
const GT = String.fromCharCode(62);
const QUOT = String.fromCharCode(34);

function decodeEntities(s) {
  return s
    .replace(/&#x([0-9a-f]+);/gi, (_, h) => String.fromCodePoint(parseInt(h, 16)))
    .replace(/&#(\d+);/g, (_, n) => String.fromCodePoint(Number(n)))
    .replace(/&nbsp;/g, " ")
    .replace(/"/g, QUOT)
    .replace(/&apos;/g, "'")
    .replace(/</g, LT)
    .replace(/>/g, GT)
    .replace(/&/g, AMP);
}

/** quita el bloque MathML y el dibujo SVG de KaTeX, luego las etiquetas */
function aTexto(html) {
  return decodeEntities(
    html
      .replace(/<span class="katex-mathml">[\s\S]*?<\/span>/g, " ")
      .replace(/<annotation[^>]*>[\s\S]*?<\/annotation>/g, " ")
      .replace(/<svg[\s\S]*?<\/svg>/g, " ")
      .replace(/<[^>]+>/g, " ")
  )
    .replace(/\s+/g, " ")
    .trim();
}

/** recorta en un limite de palabra */
function recortar(txt, n) {
  if (txt.length <= n) return txt;
  const corte = txt.slice(0, n);
  const esp = corte.lastIndexOf(" ");
  return (esp > n * 0.6 ? corte.slice(0, esp) : corte).trim();
}

/** mapa url -> {titulo, materia, semestre} desde vault.json */
function mapaNotas() {
  const mapa = new Map();
  if (!existsSync(VAULT_JSON)) return mapa;
  const vault = JSON.parse(readFileSync(VAULT_JSON, "utf8"));
  for (const s of vault.semestres || []) {
    for (const m of s.materias || []) {
      for (const n of m.notas || []) {
        const units = n.units?.length ? n.units.join("/") + "/" : "";
        const url = `/${s.id}/${m.id}/${units}${n.slug}/`;
        mapa.set(url, { t: n.title, m: m.title, s: s.title });
      }
    }
  }
  return mapa;
}

const HEAD = /<(h[23])\b([^>]*)>([\s\S]*?)<\/\1>/g;
const ID = /\bid="([^"]+)"/;

/** extrae los apartados de una pagina de nota */
function apartados(html) {
  const ini = html.indexOf("note-prose");
  if (ini < 0) return null;
  const fin = html.indexOf("</article>", ini);
  const cuerpo = html.slice(ini, fin > ini ? fin : html.length);

  const heads = [];
  HEAD.lastIndex = 0;
  let m;
  while ((m = HEAD.exec(cuerpo)) !== null) {
    const idm = ID.exec(m[2]);
    if (!idm) continue;
    heads.push({
      nivel: m[1] === "h2" ? 2 : 3,
      ancla: idm[1],
      titulo: aTexto(m[3]),
      fin: m.index + m[0].length,
      ini: m.index,
    });
  }
  if (!heads.length) return [];

  const out = [];
  for (let i = 0; i < heads.length; i++) {
    const h = heads[i];
    const hasta = i + 1 < heads.length ? heads[i + 1].ini : cuerpo.length;
    const texto = aTexto(cuerpo.slice(h.fin, hasta));
    out.push({
      n: h.nivel,
      a: h.ancla,
      t: h.titulo,
      x: recortar(texto, SNIPPET),
    });
  }
  return out;
}

async function* walk(dir) {
  for (const e of await readdir(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) yield* walk(p);
    else if (e.name === "index.html") yield p;
  }
}

async function main() {
  if (!existsSync(DIST)) {
    console.error("SEARCH-CONTENIDO: no existe dist/ — ¿se corrió el build?");
    process.exit(1);
  }
  const mapa = mapaNotas();
  const salida = [];
  let paginas = 0;

  for await (const file of walk(DIST)) {
    const html = await readFile(file, "utf8");
    if (!html.includes("note-prose")) continue;
    const rel = path.relative(DIST, file).split(path.sep).join("/");
    const url = "/" + rel.replace(/index\.html$/, "");
    const meta = mapa.get(url);
    if (!meta) continue;
    const secs = apartados(html);
    if (!secs || !secs.length) continue;
    paginas++;
    salida.push({ u: url, t: meta.t, m: meta.m, s: meta.s, sec: secs });
  }

  const json = JSON.stringify(salida);
  await writeFile(path.join(DIST, "search-content.json"), json, "utf8");

  const secs = salida.reduce((n, x) => n + x.sec.length, 0);
  console.log(
    `✓ search-content.json: ${salida.length} notas · ${secs} apartados · ${(
      json.length / 1048576
    ).toFixed(2)} MB`
  );
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
