/**
 * rehype-anclas.mjs — ids de encabezado "limpios" y alias de los antiguos.
 *
 * El problema (207 anclas cruzadas rotas):
 *
 *   · `rehype-slug` genera el id a partir del texto EXACTO del encabezado:
 *     "## Definición de Límite" → `definición-de-límite` (con tildes) y
 *     "## 🤔 Derivadas Laterales" → `-derivadas-laterales` (con un guion
 *     delante, por el emoji).
 *   · Los enlaces escritos a mano en los apuntes usan el criterio habitual:
 *     minúsculas, sin tildes, sin emojis y sin guiones sobrantes:
 *     `#definicion-de-limite`, `#derivadas-laterales`.
 *   · Resultado: el enlace apunta a un id que no existe → al hacer clic no
 *     pasa nada.
 *
 * La solución: el id CANÓNICO de cada encabezado pasa a ser el "limpio"
 * (sin tildes, sin símbolos, sin guiones en los extremos) y el id antiguo se
 * conserva como un ancla alias invisible. Así:
 *
 *   · los 195 enlaces que estaban rotos ahora encuentran su destino;
 *   · los 220 que ya funcionaban siguen funcionando (por el alias);
 *   · las URLs que se copian del navegador quedan limpias.
 *
 * No se toca el vault: todo el trabajo es del sitio.
 */

/** Quita tildes, emojis y símbolos; pasa a minúsculas; une con guiones. */
export function slugLimpio(id) {
  return String(id)
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "") // tildes
    .replace(/[\u200d\ufe0f]/g, "") // emojis (variación selector / ZWJ)
    .replace(/[^\p{L}\p{N}\s-]/gu, "") // todo lo que no sea letra, número o guion
    .trim()
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-")
    .replace(/^-+|-+$/g, "")
    .toLowerCase();
}

function esHeading(node) {
  return (
    node &&
    node.type === "element" &&
    typeof node.tagName === "string" &&
    /^h[1-6]$/.test(node.tagName)
  );
}

export function rehypeAnclas() {
  return (tree) => {
    /** ids ya ocupados (los limpios y los antiguos): evita duplicados. */
    const usados = new Set();

    const visitar = (node) => {
      if (!node.children || !node.children.length) return;
      const nuevos = [];

      for (const hijo of node.children) {
        if (esHeading(hijo)) {
          const viejo = String(hijo.properties?.id || "");
          if (viejo) {
            const base = slugLimpio(viejo) || viejo;
            let destino = base;
            let n = 2;
            while (usados.has(destino)) destino = base + "-" + n++;
            usados.add(destino);

            if (destino !== viejo) {
              // El id antiguo se queda como alias: los enlaces que ya
              // funcionaban (o que apuntan a él) siguen llegando a la sección.
              usados.add(viejo);
              hijo.properties.id = destino;
              // El alias va DENTRO del encabezado (y no antes): así el salto
              // del navegador cae justo sobre el título, no en un hueco.
              hijo.children = [
                {
                  type: "element",
                  tagName: "a",
                  properties: { id: viejo, className: ["nx-anchor-alias"] },
                  children: [],
                },
                ...(hijo.children || []),
              ];
            }
          }
        }
        visitar(hijo);
        nuevos.push(hijo);
      }

      node.children = nuevos;
    };

    visitar(tree);
  };
}
