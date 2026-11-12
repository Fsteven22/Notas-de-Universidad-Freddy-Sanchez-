/**
 * rehype-flashcards.mjs — el bloque "🔁 Repaso SR (flashcards)" de cada nota
 * pasa de ser una lista con "pregunta::respuesta" a ser tarjetas que se
 * destapan al hacer clic.
 *
 * Corre DESPUÉS de `rehype-callouts` (que es quien convierte el blockquote
 * de Obsidian en `div.nx-callout`), así que aquí ya se puede buscar el
 * callout por su clase y por su título.
 *
 * Se usa `<details>/<summary>` a propósito: voltear la tarjeta funciona sin
 * JavaScript, es accesible con teclado y con lector de pantalla, y no añade
 * ningún script al sitio.
 */

// El callout de las tarjetas se titula "🧠 Repasa con el plugin Spaced
// Repetition" (y en algunos apuntes "Repaso SR (flashcards)").
const TITULO_REPASO = /repasa con el plugin|repaso\s+sr|spaced repetition|flashcards/i;

/** Texto plano de un nodo hast. */
function texto(node) {
  if (!node) return "";
  if (node.type === "text") return node.value ?? "";
  return (node.children ?? []).map(texto).join("");
}

/**
 * Parte los hijos de un <li> en la parte anterior al separador "::" (la
 * pregunta) y la posterior (la respuesta), preservando los elementos
 * enriched (fórmulas, énfasis, enlaces) de cada lado.
 */
function partirEnDos(li) {
  const hijos = li.children ?? [];
  let largo = 0;
  let corte = -1;
  for (const h of hijos) {
    const t = texto(h);
    const i = t.indexOf("::");
    if (i !== -1) { corte = largo + i; break; }
    largo += t.length;
  }
  if (corte === -1) return null;

  const pregunta = [];
  const respuesta = [];
  let acumulado = 0;
  for (const h of hijos) {
    const t = texto(h);
    const inicio = acumulado;
    const fin = acumulado + t.length;
    if (fin <= corte) {
      pregunta.push(h);
    } else if (inicio >= corte + 2) {
      respuesta.push(h);
    } else {
      const dentro = corte - inicio;
      if (h.type === "text") {
        const antes = h.value.slice(0, dentro);
        const despues = h.value.slice(dentro + 2);
        if (antes) pregunta.push({ type: "text", value: antes });
        if (despues) respuesta.push({ type: "text", value: despues });
      } else {
        // nodo compuesto: no se puede partir con seguridad -> va a la pregunta
        pregunta.push(h);
      }
    }
    acumulado = fin;
  }
  return { pregunta, respuesta };
}

function esCalloutDeFlashcards(node) {
  if (node.type !== "element" || node.tagName !== "div") return false;
  const clases = node.properties?.className;
  const lista = Array.isArray(clases) ? clases : clases ? String(clases).split(/\s+/) : [];
  if (!lista.includes("nx-callout")) return false;
  const titulo = node.children?.[0];
  return TITULO_REPASO.test(texto(titulo));
}

/** Construye el bloque de tarjetas. */
function bloqueTarjetas(tarjetas, url, deck) {
  const items = tarjetas.map(({ pregunta, respuesta }) => ({
    type: "element",
    tagName: "details",
    properties: { className: ["nx-flashcard"] },
    children: [
      {
        type: "element",
        tagName: "summary",
        properties: { className: ["nx-flashcard__q"] },
        children: pregunta,
      },
      {
        type: "element",
        tagName: "div",
        properties: { className: ["nx-flashcard__a"] },
        children: respuesta.length ? respuesta : [{ type: "text", value: "—" }],
      },
    ],
  }));

  return {
    type: "element",
    tagName: "div",
    properties: { className: ["nx-flashcards"] },
    children: [
      {
        type: "element",
        tagName: "div",
        properties: { className: ["nx-flashcards__head"] },
        children: [
          {
            type: "element",
            tagName: "span",
            properties: { className: ["nx-flashcards__count"] },
            children: [
              { type: "text", value: `${tarjetas.length} tarjeta${tarjetas.length === 1 ? "" : "s"}` },
            ],
          },
          {
            type: "element",
            tagName: "a",
            properties: {
              className: ["nx-flashcards__cta"],
              href: `/estudio/?nota=${encodeURIComponent(url.replace(/^\/|\/$/g, ""))}`,
            },
            children: [{ type: "text", value: "Practicar estas tarjetas →" }],
          },
        ],
      },
      ...items,
    ],
  };
}

export function rehypeFlashcards() {
  return (tree, file) => {
    // URL de la nota (para el enlace "Practicar estas tarjetas")
    const ruta = String(file?.path || "").replace(/\\/g, "/");
    const m = ruta.match(/\/notes-md\/(.+)\.md$/);
    const url = m ? `/${m[1]}/` : "";

    // 1) quitar la línea "#flashcards/mazo": es metadato del plugin de
    //    Obsidian y fuera de él solo se ve como un hashtag suelto.
    const quitar = (node) => {
      if (!node.children) return;
      node.children = node.children.filter((c) => {
        if (c.type === "element" && c.tagName === "p") {
          const t = texto(c).trim();
          if (/^#flashcards\/[\w-]+$/.test(t)) return false;
        }
        return true;
      });
    };

    // 2) sustituir el callout por el bloque de tarjetas
    const visitar = (node) => {
      if (node.type === "element" || node.type === "root") {
        const salida = [];
        for (const hijo of node.children ?? []) {
          if (esCalloutDeFlashcards(hijo)) {
            const lis = [];
            const juntar = (n) => {
              if (n.type === "element" && n.tagName === "li") lis.push(n);
              for (const c of n.children ?? []) juntar(c);
            };
            for (const c of hijo.children ?? []) juntar(c);
            const tarjetas = [];
            for (const li of lis) {
              const partes = partirEnDos(li);
              if (partes && texto({ children: partes.pregunta }).trim()) {
                tarjetas.push(partes);
              }
            }
            if (tarjetas.length) {
              salida.push(bloqueTarjetas(tarjetas, url, ""));
              continue;
            }
          }
          visitar(hijo);
          salida.push(hijo);
        }
        node.children = salida;
        quitar(node);
      }
    };

    visitar(tree);
  };
}
