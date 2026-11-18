/**
 * estados-sem.mjs — el estado de cada semestre, en TEXTO.
 *
 * Es la fuente de verdad compartida: la portada lo muestra como rótulo y el
 * mapa lo usa para decidir el tono de sus esferas. Si cambia uno, cambian
 * los dos.
 *
 * El estado es TEXTO, no color: cada estado tiene su propio token (ver
 * `tokenEstado`) y el color se resuelve aparte. Así el rótulo de la portada
 * y la esfera del mapa siempre hablan el mismo idioma.
 */
export const estadosSem = {
  preuniversitario: "Completado",
  "1er-semestre": "Reconstrucción",
  "2do-semestre": "En curso",
  "3er-semestre": "En curso",
};

/** Estado de un semestre por su id (vacío si no está en la lista). */
export const estadoSem = (id) => estadosSem[id] ?? "";

/**
 * El color de cada estado. Tres señales, tres tokens:
 *   · "En curso"       → el coral (el punto de calidez del arrecife)
 *   · "Completado"     → el verde de mar
 *   · "Reconstrucción" → el ámbar (está a medias)
 * Los tres pasan el contraste mínimo contra el fondo y la superficie.
 */
export const tokenEstado = {
  "En curso": "--nx-coral",
  Completado: "--nx-done",
  Reconstrucción: "--nx-warn",
};

/** Clase CSS de un estado, para pintar el rótulo de la portada. */
export const claseEstado = (estado) =>
  "nx-sem-state--" +
  estado
    .toLowerCase()
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "") // quita las tildes: "reconstrucción" → "reconstruccion"
    .replace(/\s+/g, "-");
