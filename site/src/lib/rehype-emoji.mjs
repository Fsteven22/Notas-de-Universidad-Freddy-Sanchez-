/**
 * rehype-emoji.mjs — envuelve los emojis de los encabezados en su propia
 * etiqueta para poder tratarlos aparte del texto.
 *
 * En el vault los encabezados empiezan casi siempre por un emoji
 * ("🧩 Diseño de Software", "⚖️ Propiedades de los Límites"). Con el texto
 * plano ese emoji se mezcla con el título y se lee como ruido; el CSS lo
 * puede en cambio tratar por separado (mismo tamaño, en gris y discreto).
 *
 * Solo se toca lo que se LEE (encabezados): los emojis de las tablas, las
 * fórmulas o el cuerpo de la nota se quedan como estaban.
 *
 * Los callouts no pasan por aquí: su icono lo pone rehype-callouts, que
 * además lo saca del texto del título.
 */

// Emoji: banderas (RI RI), pictogramas y secuencias con ZWJ y variantes.
const EMOJI = new RegExp(
  "(?:\\p{Regional_Indicator}{2}" +
    "|(?:\\p{Extended_Pictographic}" +
    "(?:[\\uFE0E\\uFE0F]|[\\u{1F3FB}-\\u{1F3FF}]|\\u200D\\p{Extended_Pictographic})*))",
  "gu"
);

/** Parte un texto en trozos: emoji (marcados) y texto normal. */
function partir(texto) {
  const out = [];
  let ultimo = 0;
  for (const m of texto.matchAll(EMOJI)) {
    const i = m.index ?? 0;
    if (i > ultimo) out.push({ tipo: "texto", valor: texto.slice(ultimo, i) });
    out.push({ tipo: "emoji", valor: m[0] });
    ultimo = i + m[0].length;
  }
  if (ultimo < texto.length) out.push({ tipo: "texto", valor: texto.slice(ultimo) });
  return out;
}

function esEmoji(value) {
  return new RegExp(`^(?:${EMOJI.source})$`, "u").test(value);
}

/** Reemplaza los nodos de texto de un hijo por trozos con emoji marcado. */
function marcarEmoji(node) {
  const hijos = node.children ?? [];
  const nuevos = [];
  let cambio = false;
  for (const hijo of hijos) {
    if (hijo.type === "text" && esEmoji(hijo.value ?? "")) {
      // el nodo es solo un emoji: se marca entero
      nuevos.push({
        type: "element",
        tagName: "span",
        properties: { className: ["nx-emoji"] },
        children: [hijo],
      });
      cambio = true;
      continue;
    }
    if (hijo.type === "text") {
      const trozos = partir(hijo.value ?? "");
      if (trozos.some((t) => t.tipo === "emoji")) {
        cambio = true;
        for (const t of trozos) {
          if (t.tipo === "emoji") {
            nuevos.push({
              type: "element",
              tagName: "span",
              properties: { className: ["nx-emoji"] },
              children: [{ type: "text", value: t.valor }],
            });
          } else {
            nuevos.push({ type: "text", value: t.valor });
          }
        }
        continue;
      }
    }
    nuevos.push(hijo);
  }
  if (cambio) node.children = nuevos;
}

const NIVELES = new Set(["h1", "h2", "h3", "h4"]);

export function rehypeEmoji() {
  return (tree) => {
    const visitar = (node) => {
      if (!node || typeof node !== "object") return;
      if (node.type === "element" && NIVELES.has(node.tagName)) {
        marcarEmoji(node);
      }
      for (const hijo of node.children ?? []) visitar(hijo);
    };
    visitar(tree);
  };
}

export default rehypeEmoji;
