/**
 * rehype-callouts.mjs — Callouts de Obsidian `> [!tipo] Título` → cards neón.
 * Soporta blockquotes multiparte: un quote largo puede contener varios
 * callouts seguidos (los españa en divs independientes).
 */

const TYPES = {
  info: ["blue", "ℹ️"],
  note: ["purple", "📝"],
  tip: ["green", "💡"],
  success: ["green", "✅"],
  example: ["cyan", "🧪"],
  warning: ["gold", "⚠️"],
  caution: ["gold", "⚠️"],
  danger: ["red", "🚫"],
  error: ["red", "🚫"],
  bug: ["red", "🐞"],
  quote: ["muted", "❝"],
  brain: ["purple", "🧠"],
  todo: ["blue", "📅"],
  question: ["gold", "❓"],
  abstract: ["cyan", "📄"],
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

function calloutDiv(type, title, children) {
  const [color, icon] = TYPES[type] ?? ["blue", "ℹ️"];
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
        children: [{ type: "text", value: `${icon} ${title}` }],
      },
      ...children,
    ],
  };
}

function extractTitle(pNode) {
  const text = flattenText(pNode).trim();
  const m = text.match(/^\[!(\w+)\]?([-+]?)[\s\S]*$/);
  if (!m) return null;
  const raw = m[1].toLowerCase();
  const type = TYPES[raw] ? raw : "note";
  const titleLine = text.split("\n")[0].replace(/^\[!(\w+)\]?[-+]?[ \t]*/, "").trim();
  return { type, title: titleLine || titleFor(type), header: m[0].length > 0 };
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
        out.push(visit(child) ?? child);
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
          current = { kind: "callout", type: info.type, title: info.title, header: c, body: keepBodyRemainder(c), children: [] };
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
        const siblings = seg.children;
        result.push(calloutDiv(seg.type, seg.title, [...seg.body, ...siblings]));
      }
    }
    return result.length === 1 ? result[0] : result;
  };

  return (tree) => {
    visit(tree);
  };
}
