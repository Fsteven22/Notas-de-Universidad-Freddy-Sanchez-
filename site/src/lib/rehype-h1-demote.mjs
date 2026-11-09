/**
 * rehype-h1-demote.mjs — degrada los h1 del markdown a h2 con clase propia.
 *
 * El layout ya pone un h1 (el título de la nota) y el markdown del vault
 * suele traer otro. Medido sobre el dist: 775 de 848 páginas tienen 2 h1, y
 * en 565 de 823 el h1 del markdown dice ALGO DISTINTO al título
 * ("Concepto Intuitivo de Limite" vs "Concepto y Definicion Formal del
 * Limite"), asi que no se puede borrar ninguno de los dos sin perder texto.
 *
 * La solucion es bajar el del markdown un nivel: queda un solo h1 por pagina
 * (el del hero) y el texto del markdown se conserva como apartado. Se le
 * pone la clase `nx-h1-md` para que el CSS le devuelva el aspecto que tenia
 * como h1 (1.9rem / 800, sin la linea de borde que tienen los h2).
 *
 * El PRIMER h1 de cada nota es el titulo de la nota repetido: se marca con
 * `data-nx-toc-skip` para que el indice de la nota no lo liste (seria ruido:
 * el lector ya ve ese titulo en el header).
 */

function walk(node, fn) {
  if (!node || typeof node !== "object") return;
  if (Array.isArray(node)) {
    for (const child of node) walk(child, fn);
    return;
  }
  fn(node);
  if (Array.isArray(node.children)) {
    for (const child of node.children) walk(child, fn);
  }
}

export function rehypeH1Demote() {
  return (tree) => {
    let first = true;
    walk(tree, (node) => {
      if (node.type !== "element" || node.tagName !== "h1") return;
      node.tagName = "h2";
      node.properties = node.properties || {};
      const cls = node.properties.className;
      const list = Array.isArray(cls) ? [...cls] : cls ? [cls] : [];
      if (!list.includes("nx-h1-md")) list.push("nx-h1-md");
      node.properties.className = list;
      if (first) {
        // hast: dataNxTocSkip -> data-nx-toc-skip
        node.properties.dataNxTocSkip = "";
        first = false;
      }
    });
  };
}

export default rehypeH1Demote;
