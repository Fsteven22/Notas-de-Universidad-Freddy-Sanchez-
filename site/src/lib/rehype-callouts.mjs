/**
 * rehype-callouts.mjs — Callouts de Obsidian `> [!tipo] Título` → bloques.
 * Soporta blockquotes multiparte: un quote largo puede contener varios
 * callouts seguidos (los españa en divs independientes).
 *
 * El icono: si el título del callout empieza por un emoji, ese emoji pasa
 * a ser el icono (y se quita del texto, para no repetirlo). Si no, se usa
 * el icono propio del tipo. Un solo icono, nunca dos.
 *
 * El cuerpo va en su propio elemento (.nx-callout-body) con peso normal:
 * el título es lo único en negrita.
 *
 * Lo que no cabe en un callout (una tabla, un diagrama) sale fuera, detrás
 * del bloque: un callout es una nota breve, no un contenedor.
 *
 * Los colores: solo hay tres (info, aviso, peligro) y van únicamente en la
 * barra de la izquierda. El fondo es transparente.
 */

const TYPES = {
  info: ["info", "ℹ️"],
  note: ["info", "📝"],
  tip: ["info", "💡"],
  success: ["info", "✅"],
  example: ["info", "🧪"],
  warning: ["warn", "⚠️"],
  caution: ["warn", "⚠️"],
  danger: ["danger", "🚫"],
  error: ["danger", "🚫"],
  bug: ["danger", "🐞"],
  quote: ["neutral", "❝"],
  brain: ["info", "🧠"],
  todo: ["info", "📅"],
  question: ["warn", "❓"],
  abstract: ["info", "📄"],
};

/* Tipos que no están en TYPES: se tratan como "note" (info). */
const COLOR_POR_TIPO = {
  info: "info",
  note: "info",
  tip: "info",
  success: "info",
  example: "info",
  abstract: "info",
  brain: "info",
  todo: "info",
  study: "info",
  experiment: "info",
  important: "info",
  summary: "info",
  check: "info",
  notes: "info",
  warning: "warn",
  caution: "warn",
  question: "warn",
  danger: "danger",
  error: "danger",
  bug: "danger",
  quote: "neutral",
};


const DEFAULT_TITLES = {
  info: "Nota",
  note: "Nota",
  tip: "Tip",
  success: "Éxito",
  example: "Ejemplo",
  warning: "Advertencia",
  caution: "Advertencia",
  danger: "Peligro",
  error: "Error",
  bug: "Bug",
  quote: "Cita",
  brain: "Estrategia",
  todo: "Por hacer",
  question: "Pregunta",
  abstract: "Resumen",
};

function flattenText(node) {
  if (!node) return "";
  if (node.type === "text") return node.value ?? "";
  return (node.children ?? []).map(flattenText).join("");
}

function titleFor(type) {
  return DEFAULT_TITLES[type] ?? "Nota";
}

/* Emoji al principio de un texto (con sus variantes y el ZWJ). */
const EMOJI_INICIAL = new RegExp(
  "^(?:\\p{Regional_Indicator}{2}" +
    "|(?:\\p{Extended_Pictographic}" +
    "(?:[\\uFE0E\\uFE0F]|[\\u{1F3FB}-\\u{1F3FF}]|\\u200D\\p{Extended_Pictographic})*))",
  "u"
);

/**
 * Si el título empieza por un emoji, lo devuelve aparte y quita del texto.
 * El texto puede ser una cadena (título simple) o una lista de nodos
 * (título con formato: Neón, enlaces, emphasis…).
 */
function sacarEmojiInicial(title) {
  if (typeof title === "string") {
    const m = title.match(EMOJI_INICIAL);
    if (!m) return { icono: "", titulo: title };
    return { icono: m[0], titulo: title.slice(m[0].length).trim() };
  }
  const nodos = [...title];
  const primero = nodos[0];
  if (!primero || primero.type !== "text") return { icono: "", titulo: nodos };
  const m = (primero.value ?? "").match(EMOJI_INICIAL);
  if (!m) return { icono: "", titulo: nodos };
  const resto = (primero.value ?? "").slice(m[0].length).replace(/^\s+/, "");
  nodos[0] = { ...primero, value: resto };
  if (!resto) nodos.shift();
  return { icono: m[0], titulo: nodos };
}

/** ¿Este nodo es una tabla o un diagrama (cosa que no va en un callout)? */
function esPesado(node) {
  if (!node || node.type !== "element") return false;
  if (node.tagName === "table" || node.tagName === "img" || node.tagName === "figure") return true;
  if (node.tagName === "p") {
    // un párrafo que solo contiene una imagen es una imagen
    const kids = node.children ?? [];
    const utiles = kids.filter((k) => !(k.type === "text" && !(k.value ?? "").trim()));
    if (utiles.length === 1 && utiles[0].type === "element" && utiles[0].tagName === "img") return true;
  }
  return false;
}

function calloutDiv(type, title, isRich, children, iconoPropio) {
  const [color, iconoTipo] = TYPES[type] ?? ["info", "ℹ️"];
  const { icono, titulo } = sacarEmojiInicial(isRich ? title : String(title));
  const ic = iconoPropio ?? icono ?? iconoTipo;
  let contenido;
  if (isRich) {
    contenido = titulo;
  } else {
    const limpio = String(titulo).trim();
    contenido = [{ type: "text", value: limpio || titleFor(type) }];
  }
  return {
    type: "element",
    tagName: "div",
    properties: {
      className: ["nx-callout", `nx-callout-${type}`],
      "data-color": color,
    },
    children: [
      {
        type: "element",
        tagName: "p",
        properties: { className: ["nx-callout-title"] },
        children: [
          {
            type: "element",
            tagName: "span",
            properties: { className: ["nx-callout-ico"], ariaHidden: "true" },
            children: [{ type: "text", value: ic }],
          },
          ...(contenido.length ? [{ type: "text", value: " " }] : []),
          ...contenido,
        ],
      },
      {
        type: "element",
        tagName: "div",
        properties: { className: ["nx-callout-body"] },
        children,
      },
    ],
  };
}

function extractTitle(pNode) {
  const text = flattenText(pNode).trim();
  const m = text.match(/^\[!(\w+)\]?([-+]?)/);
  if (!m) return null;
  const raw = m[1].toLowerCase();
  const type = TYPES[raw] ? raw : "note";
  // titulo RICO: recorre los niños hasta el primer salto de línea preservando
  // los elementos (math inline de remark-math, énfasis, links) para que
  // rehype-katex siga procesándolos; el tipo se detecta por texto plano.
  const kids = [];
  let stripped = false;
  for (const child of pNode.children ?? []) {
    if (child.type === "break") break;
    if (child.type === "text") {
      let v = child.value ?? "";
      if (!stripped) {
        v = v.replace(/^\s*\[!(\w+)\]?[-+]?[ \t]?/, "");
        stripped = true;
      }
      // el indice del salto se calcula DESPUES de quitar el prefijo [!tipo]:
      // si se calcula antes, slice() se pasa de largo y el titulo se traga
      // un fragmento de la primera linea del cuerpo.
      const nl = v.indexOf("\n");
      if (nl !== -1) {
        if (v.slice(0, nl)) kids.push({ type: "text", value: v.slice(0, nl) });
        break;
      }
      if (v) kids.push({ type: "text", value: v });
    } else {
      kids.push(child);
    }
  }
  const titleChildren = kids.filter((k) => k.type !== "text" || (k.value ?? "").length > 0);
  const isPlain = titleChildren.every((k) => k.type === "text");
  const title = isPlain ? titleChildren.map((k) => k.value ?? "").join("").trim() || titleFor(type) : titleChildren;
  return { type, title, isRich: !isPlain };
}

/** separa el resto de la línea del título (contenido tras el salto de línea) */
function keepBodyRemainder(pNode) {
  const fc = pNode.children ?? [];
  // breakpoint = primer hijo con "\n" en texto, o un "break"
  const iBreak = fc.findIndex((c) => c.type === "break" || (c.type === "text" && (c.value ?? "").includes("\n")));
  if (iBreak === -1) return [];
  const tail = fc.slice(iBreak + 1).filter((c) => !(c.type === "text" && !(c.value ?? "").trim()));
  const headNode = fc[iBreak];
  if (headNode.type === "text") {
    const rest = (headNode.value ?? "").replace(/^[^\n]*\n/, "");
    if (rest.trim()) tail.unshift({ type: "text", value: rest });
    else if (rest) tail.unshift({ type: "text", value: rest }); // preserva posibles sangrías
  }
  return [{ type: "element", tagName: "p", properties: {}, children: tail }];
}

export function rehypeCallouts() {
  const visit = (node) => {
    if (node.type === "element" || node.type === "root") {
      const out = [];
      for (const child of node.children ?? []) {
        const v = visit(child) ?? child;
        // un hijo puede convertirse en varios (callout + lo que sale fuera)
        if (Array.isArray(v)) out.push(...v);
        else out.push(v);
      }
      node.children = out;
    }

    if (node.type !== "element" || node.tagName !== "blockquote") return null;
    const kids = node.children ?? [];
    const firstEl = kids.find((c) => c.type === "element");
    if (!firstEl) return null;

    // segmentar hijos: registrar callouts donde arranque un <p> [!...]
    const segments = []; // {kind:'plain'|'callout', type, title, children}
    let current = null;
    let hasCallout = false;
    for (const c of kids) {
      if (c.type === "text" && !(c.value ?? "").trim()) {
        if (current) current.children.push(c);
        continue; // whitespace
      }
      if (c.type === "element") {
        const info = c.tagName === "p" ? extractTitle(c) : null;
        if (info) {
          segments.push(current);
          current = { kind: "callout", type: info.type, title: info.title, isRich: !!info.isRich, header: c, body: keepBodyRemainder(c), children: [] };
          hasCallout = true;
          continue;
        }
      }
      if (!current) {
        current = { kind: "plain", children: [] };
        segments.push(current);
      }
      current.children.push(c);
    }
    segments.push(current);
    if (!hasCallout) return null;

    const result = [];
    for (const seg of segments.filter(Boolean)) {
      if (seg.kind === "plain") {
        if (!seg.children.length) continue;
        result.push({
          type: "element",
          tagName: "blockquote",
          properties: { className: ["nx-quote-plain"] },
          children: seg.children,
        });
      } else {
        const header = seg.header;
        void header;
        // Una tabla o un diagrama dentro de un callout no cabe: sale
        // detrás del bloque, en su sitio, sin romper el texto.
        const todos = [...seg.body, ...seg.children];
        const pesados = todos.filter(esPesado);
        const cuerpo = todos.filter((n) => !esPesado(n));
        result.push(calloutDiv(seg.type, seg.title, seg.isRich, cuerpo));
        for (const p of pesados) result.push(p);
      }
    }
    return result.length === 1 ? result[0] : result;
  };

  return (tree) => {
    visit(tree);
  };
}
