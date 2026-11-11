/**
 * flashcards.mjs — las tarjetas de repaso que YA viven en las notas.
 *
 * El vault usa el formato del plugin "Spaced Repetition" de Obsidian:
 *
 *     ## 🔁 Repaso SR (flashcards)
 *
 *     #flashcards/bd-u4
 *
 *     > [!note] 🧠 Repasa con el plugin Spaced Repetition
 *     >
 *     > - ¿SQL en 1 frase?::Lenguaje declarativo de acceso a bases de datos.
 *     > - ¿DDL?::Data Definition Language.
 *
 * Es decir: una línea por tarjeta, `pregunta::respuesta`, dentro de un
 * callout. Aquí se leen del markdown crudo (el mismo que renderiza el sitio)
 * para poder armar sesiones de estudio: elegir materia, barajar y repasar.
 *
 * Solo lectura en tiempo de compilación: no toca el vault.
 */
import vault from "../data/vault.json";

/** Todos los .md que el sitio renderiza (los mismos que usa `[...slug].astro`). */
const crudos = import.meta.glob("/notes-md/**/*.md", { query: "?raw", eager: true });

/** Metadatos de cada nota: file -> { sem, semTitulo, mat, matTitulo, titulo } */
const META = new Map();
for (const s of vault.semestres) {
  for (const m of s.materias) {
    for (const n of m.notas) {
      META.set(n.file, {
        sem: s.id,
        semTitulo: s.title,
        mat: m.id,
        matTitulo: m.title,
        titulo: n.title,
      });
    }
  }
}

/** Normaliza una línea de tarjeta: `- pregunta::respuesta` */
function lineaTarjeta(linea) {
  const m = linea.match(/^\s*>\s*[-*]\s+(.+?)\s*::\s*(.*)$/);
  if (!m) return null;
  const q = m[1].trim();
  const a = m[2].trim();
  if (!q || !a) return null;
  return { q, a };
}

/**
 * Extrae las tarjetas de un markdown.
 * @returns {{ deck: string, tarjetas: {q: string, a: string}[] }}
 */
export function parseFlashcards(md) {
  const lineas = md.split(/\r?\n/);
  const tarjetas = [];
  let deck = "";
  let dentro = false;
  let nivel = 0;

  for (const linea of lineas) {
    const heading = linea.match(/^(#{1,6})\s+(.*)$/);
    if (heading) {
      const nivelLinea = heading[1].length;
      if (dentro && nivelLinea <= nivel) break; // se acabó la sección
      if (/repaso\s+sr/i.test(heading[2])) {
        dentro = true;
        nivel = nivelLinea;
        deck = "";
        continue;
      }
    }
    if (!dentro) continue;

    const tag = linea.match(/#flashcards\/([\w-]+)/);
    if (tag) {
      deck = tag[1];
      continue;
    }
    const t = lineaTarjeta(linea);
    if (t) tarjetas.push(t);
  }
  return { deck, tarjetas };
}

/** Todas las tarjetas del sitio, con su nota, materia y semestre. */
let _cache = null;
export function todasLasFlashcards() {
  if (_cache) return _cache;
  const salida = [];
  for (const [ruta, mod] of Object.entries(crudos)) {
    // con `?raw` el glob entrega el módulo; el texto está en `default`
    const md = typeof mod === "string" ? mod : mod?.default;
    if (typeof md !== "string") continue;
    const rel = ruta.replace(/^\/notes-md\//, "").replace(/\.md$/, "");
    const { deck, tarjetas } = parseFlashcards(md);
    if (!tarjetas.length) continue;
    const meta = META.get(rel) || {};
    tarjetas.forEach((t, i) => {
      salida.push({
        id: `${rel}#${i}`,
        q: t.q,
        a: t.a,
        deck,
        file: rel,
        url: `/${rel}/`,
        sem: meta.sem || "",
        semTitulo: meta.semTitulo || "",
        mat: meta.mat || "",
        matTitulo: meta.matTitulo || "",
        nota: meta.titulo || "",
      });
    });
  }
  _cache = salida;
  return salida;
}

/** Tarjetas de una nota concreta (por su `file`). */
export function flashcardsDeNota(file) {
  return todasLasFlashcards().filter((c) => c.file === file);
}

/** Tarjetas de una materia (por su id). */
export function flashcardsDeMateria(matId) {
  return todasLasFlashcards().filter((c) => c.mat === matId);
}

/** Agrupa por materia y por semestre (para los filtros del modo de estudio). */
export function agruparFlashcards(tarjetas) {
  const materias = new Map();
  const semestres = new Map();
  const mazos = new Map();
  for (const t of tarjetas) {
    const mk = (m, k, extra) => {
      if (!m.has(k)) m.set(k, { ...extra, n: 0 });
      m.get(k).n++;
    };
    mk(materias, t.mat || "?", { titulo: t.matTitulo, sem: t.sem, semTitulo: t.semTitulo });
    mk(semestres, t.sem || "?", { titulo: t.semTitulo });
    mk(mazos, t.deck || "sin-mazo", { titulo: t.deck });
  }
  const aLista = (m) =>
    [...m.entries()]
      .map(([id, v]) => ({ id, ...v }))
      .sort((a, b) => b.n - a.n || a.titulo.localeCompare(b.titulo, "es"));
  return { materias: aLista(materias), semestres: aLista(semestres), mazos: aLista(mazos) };
}
