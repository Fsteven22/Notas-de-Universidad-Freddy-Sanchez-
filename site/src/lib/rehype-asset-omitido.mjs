/**
 * rehype-asset-omitido.mjs — convierte los marcadores que deja el sync
 *   <!-- nx:asset-omitido NOMBRE -->   (asset en _no-publicar.txt)
 *   <!-- nx:link-omitido  NOMBRE -->   (nota que no se publica)
 * en un aviso visible para el lector. Antes el embed desaparecia en silencio
 * y el usuario creia que la nota estaba incompleta.
 *
 * El marcador llega de dos formas segun el contexto del markdown:
 *   - nodo `comment` (HTML a nivel de bloque)
 *   - nodo `raw` (HTML inline dentro de listas o citas)
 */

const RE_INLINE = /<!--\s*nx:(asset|link)-omitido\s*([\s\S]*?)\s*-->/g;

function decodeEntities(s) {
  return s
    .replace(/&#(\d+);/g, (_, n) => String.fromCharCode(Number(n)))
    .replace(/&#x([0-9a-f]+);/gi, (_, h) => String.fromCharCode(parseInt(h, 16)))
    .replace(/"/g, '"')
    .replace(/&apos;/g, "'")
    .replace(/</g, "<")
    .replace(/>/g, ">")
    .replace(/&/g, "&");
}

function aviso(tipo, nombre) {
  const esAsset = tipo === "asset";
  const titulo = esAsset ? "Material no publicado" : "Contenido no publicado";
  const texto = esAsset
    ? `«${nombre}» no está disponible en el sitio. Puede ser material con copyright o licencia de lectura (se consulta en la copia local del vault) o un archivo que no está en la copia pública.`
    : `«${nombre}» es una nota que no se publica en el sitio.`;
  return {
    type: "element",
    tagName: "div",
    properties: { className: ["nx-omitido", `nx-omitido-${tipo}`] },
    children: [
      {
        type: "element",
        tagName: "strong",
        properties: {},
        children: [{ type: "text", value: titulo }],
      },
      { type: "text", value: ` ${texto}` },
    ],
  };
}

/** Devuelve los nodos que reemplazan a un nodo `raw`, o null si no hay marcador. */
function fromRaw(value) {
  const out = [];
  let last = 0;
  let m;
  RE_INLINE.lastIndex = 0;
  while ((m = RE_INLINE.exec(value)) !== null) {
    if (m.index > last) out.push({ type: "text", value: value.slice(last, m.index) });
    out.push(aviso(m[1], decodeEntities((m[2] || "").trim()) || "material"));
    last = m.index + m[0].length;
  }
  if (!out.length) return null;
  if (last < value.length) out.push({ type: "text", value: value.slice(last) });
  return out;
}

function walk(node, replace) {
  if (!node || !Array.isArray(node.children)) return;
  for (let i = 0; i < node.children.length; i++) {
    const child = node.children[i];
    if (child.type === "comment" && typeof child.value === "string" && child.value.startsWith("nx:")) {
      const m = /^nx:(asset|link)-omitido\s*([\s\S]*)$/.exec(child.value);
      if (m) {
        node.children.splice(i, 1, aviso(m[1], decodeEntities((m[2] || "").trim()) || "material"));
        continue;
      }
    }
    if (child.type === "raw" && typeof child.value === "string" && child.value.includes("<!-- nx:")) {
      const parsed = fromRaw(child.value);
      if (parsed) {
        node.children.splice(i, 1, ...parsed);
        i += parsed.length - 1;
        continue;
      }
    }
    walk(child, replace);
  }
}

export function rehypeAssetOmitido() {
  return (tree) => {
    walk(tree, null);
  };
}
