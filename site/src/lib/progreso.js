/**
 * progreso.js — favoritos y notas leídas, guardados en el navegador del lector.
 *
 * Sin cuentas ni servidor: todo vive en `localStorage`, así que es privado
 * por construcción y funciona sin conexión. El sitio es estático, así que no
 * hay a dónde mandar nada.
 *
 * · `nx-favoritos`: { [url]: { t, m, mt, s, at } }  → url, título, materia,
 *   título de la materia, semestre y fecha.
 * · `nx-leidas`:   { [url]: { t, m, mt, s, at } }  → lo mismo, para el avance.
 *
 * Los botones se detectan por atributo de datos, así que el mismo código
 * sirve en la nota, en la ficha de materia y en las páginas de resumen:
 *   · [data-nx-fav]    → alterna favorito
 *   · [data-nx-hecha]  → marca / desmarca como leída
 *
 * La delegación de eventos se registra una sola vez en `document`, así que
 * sigue funcionando al navegar con el ClientRouter de Astro.
 */
const KEY_FAV = "nx-favoritos";
const KEY_LEIDAS = "nx-leidas";

function leer(key) {
  try {
    const v = JSON.parse(localStorage.getItem(key) || "{}");
    return v && typeof v === "object" && !Array.isArray(v) ? v : {};
  } catch (e) {
    return {};
  }
}

function escribir(key, obj) {
  try {
    localStorage.setItem(key, JSON.stringify(obj));
  } catch (e) {
    /* modo privado o cuota llena: se sigue funcionando, solo no se guarda */
  }
}

export function favoritos() {
  return leer(KEY_FAV);
}

export function leidas() {
  return leer(KEY_LEIDAS);
}

export function esFavorito(url) {
  return !!leer(KEY_FAV)[url];
}

export function esLeida(url) {
  return !!leer(KEY_LEIDAS)[url];
}

/** Metadatos de un botón (vienen en los atributos data-*). */
export function metaDeEl(el) {
  return {
    url: el.getAttribute("data-url") || "",
    t: el.getAttribute("data-t") || "",
    m: el.getAttribute("data-m") || "",
    mt: el.getAttribute("data-mt") || "",
    s: el.getAttribute("data-s") || "",
  };
}

export function alternarFavorito(meta) {
  if (!meta.url) return false;
  const f = leer(KEY_FAV);
  if (f[meta.url]) {
    delete f[meta.url];
  } else {
    f[meta.url] = { t: meta.t, m: meta.m, mt: meta.mt, s: meta.s, at: Date.now() };
  }
  escribir(KEY_FAV, f);
  pintarEstado();
  return !!f[meta.url];
}

export function marcarLeida(meta, valor) {
  if (!meta.url) return false;
  const l = leer(KEY_LEIDAS);
  if (valor) {
    l[meta.url] = { t: meta.t, m: meta.m, mt: meta.mt, s: meta.s, at: Date.now() };
  } else {
    delete l[meta.url];
  }
  escribir(KEY_LEIDAS, l);
  pintarEstado();
  return !!l[meta.url];
}

/** Refleja el estado guardado en los botones y en los contadores. */
export function pintarEstado() {
  const f = leer(KEY_FAV);
  const l = leer(KEY_LEIDAS);
  const nFav = Object.keys(f).length;

  document.querySelectorAll("[data-nx-fav]").forEach((el) => {
    const on = !!f[el.getAttribute("data-url") || ""];
    el.classList.toggle("es-fav", on);
    el.setAttribute("aria-pressed", on ? "true" : "false");
    const ico = el.querySelector("[data-nx-fav-ico]");
    if (ico) ico.textContent = on ? "★" : "☆";
    const txt = el.querySelector("[data-nx-fav-txt]");
    if (txt) txt.textContent = on ? "Guardado" : "Guardar";
  });

  document.querySelectorAll("[data-nx-hecha]").forEach((el) => {
    const on = !!l[el.getAttribute("data-url") || ""];
    el.classList.toggle("es-hecha", on);
    el.setAttribute("aria-pressed", on ? "true" : "false");
    const ico = el.querySelector("[data-nx-hecha-ico]");
    if (ico) ico.textContent = on ? "✓" : "○";
    const txt = el.querySelector("[data-nx-hecha-txt]");
    if (txt) txt.textContent = on ? "Leída" : "Marcar leída";
  });

  document.querySelectorAll("[data-nx-fav-count]").forEach((el) => {
    el.textContent = String(nFav);
    el.classList.toggle("es-vacio", nFav === 0);
  });

  document.querySelectorAll("[data-nx-leidas-count]").forEach((el) => {
    el.textContent = String(Object.keys(l).length);
    el.classList.toggle("es-vacio", Object.keys(l).length === 0);
  });
}

let iniciado = false;

export function iniciar() {
  if (iniciado) return;
  iniciado = true;

  document.addEventListener("click", (ev) => {
    const t = ev.target;
    if (!(t instanceof Element)) return;
    const fav = t.closest("[data-nx-fav]");
    if (fav) {
      ev.preventDefault();
      alternarFavorito(metaDeEl(fav));
      return;
    }
    const hecha = t.closest("[data-nx-hecha]");
    if (hecha) {
      ev.preventDefault();
      const url = hecha.getAttribute("data-url") || "";
      marcarLeida(metaDeEl(hecha), !esLeida(url));
    }
  });

  document.addEventListener("astro:page-load", pintarEstado);
  pintarEstado();
}
