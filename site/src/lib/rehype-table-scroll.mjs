/**
 * rehype-table-scroll.mjs — envuelve cada tabla en un contenedor con scroll.
 *
 * Las tablas del vault tienen hasta 8 columnas y no caben en el ancho de
 * un teléfono. Sin este envoltorio la tabla empuja la página y aparece un
 * scroll horizontal en TODO el sitio (no solo dentro de la tabla), que es
 * justo lo que hay que evitar.
 *
 * Con el envoltorio, la tabla se desplaza dentro de su caja y el resto de
 * la nota se queda quieto.
 */

const CLASE = "nx-table-scroll";

export function rehypeTableScroll() {
  return (tree) => {
    /* `dentro` evita envolver dos veces la misma tabla: al meterla en el
       envoltorio ya no se vuelve a visitar. */
    const visitar = (node, dentro) => {
      if (!node || typeof node !== "object") return;
      const hijos = node.children;
      if (!Array.isArray(hijos)) return;
      for (let i = 0; i < hijos.length; i++) {
        const hijo = hijos[i];
        if (hijo?.type === "element" && hijo.tagName === "table" && !dentro) {
          hijos[i] = {
            type: "element",
            tagName: "div",
            properties: { className: [CLASE] },
            children: [hijo],
          };
          continue;
        }
        visitar(hijo, dentro);
      }
    };
    visitar(tree, false);
  };
}

export default rehypeTableScroll;
