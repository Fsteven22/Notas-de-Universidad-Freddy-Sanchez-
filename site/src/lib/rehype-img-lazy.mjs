/**
 * rehype-img-lazy.mjs — loading="lazy", decoding="async" y width/height en las
 * <img> del markdown.
 *
 * Medido sobre el dist: 2.735 imagenes y NI UNA sola tenia loading, decoding
 * ni width/height. Consecuencias:
 *   · el navegador descarga todas las imagenes de la pagina de golpe. La
 *     pagina de SBD "diseno por componentes" baja 5,5 MB en 36 imagenes.
 *   · sin width/height el navegador no reserva el hueco -> la pagina salta
 *     (CLS) cada vez que entra una imagen.
 *
 * Las dimensiones se leen de la cabecera del propio archivo (PNG: bytes
 * 16-24, JPEG: marcador SOFn, SVG: viewBox). No hace falta ninguna libreria
 * ni decodificar la imagen: solo leer los primeros bytes.
 */

import { readFileSync, existsSync } from "node:fs";
import path from "node:path";

const PUBLIC_DIR = path.resolve(process.cwd(), "public");
const cache = new Map();

function dimsPng(buf) {
  if (buf.length < 24) return null;
  if (buf.readUInt32BE(0) !== 0x89504e47) return null;
  const w = buf.readUInt32BE(16);
  const h = buf.readUInt32BE(20);
  return w > 0 && h > 0 ? { w, h } : null;
}

function dimsJpeg(buf) {
  let i = 2;
  while (i < buf.length - 9) {
    if (buf[i] !== 0xff) {
      i++;
      continue;
    }
    const marker = buf[i + 1];
    // marcadores sin payload
    if (marker === 0x01 || (marker >= 0xd0 && marker <= 0xd9)) {
      i += 2;
      continue;
    }
    if (marker === 0xd8) {
      i += 2;
      continue;
    }
    const len = buf.readUInt16BE(i + 2);
    // SOF0..SOF15 (salvo DHT/JPG/DAC) traen las dimensiones
    if (marker >= 0xc0 && marker <= 0xcf && marker !== 0xc4 && marker !== 0xc8 && marker !== 0xcc) {
      const h = buf.readUInt16BE(i + 5);
      const w = buf.readUInt16BE(i + 7);
      return w > 0 && h > 0 ? { w, h } : null;
    }
    i += 2 + len;
  }
  return null;
}

function dimsSvg(buf) {
  const head = buf.toString("utf8", 0, Math.min(2048, buf.length));
  const vb = head.match(/viewBox\s*=\s*["']\s*(-?[\d.]+)[,\s]+(-?[\d.]+)[,\s]+(-?[\d.]+)[,\s]+(-?[\d.]+)/i);
  if (vb) {
    const w = Math.round(Number(vb[3]));
    const h = Math.round(Number(vb[4]));
    if (w > 0 && h > 0) return { w, h };
  }
  const mw = head.match(/\bwidth\s*=\s*["']([\d.]+)/i);
  const mh = head.match(/\bheight\s*=\s*["']([\d.]+)/i);
  if (mw && mh) {
    const w = Math.round(Number(mw[1]));
    const h = Math.round(Number(mh[1]));
    if (w > 0 && h > 0) return { w, h };
  }
  return null;
}

/** dimensiones intrinsecas de un asset servido en /assets/... */
function dimensiones(src) {
  if (cache.has(src)) return cache.get(src);
  let out = null;
  const rel = src.split("?")[0].replace(/^\/+/, "");
  // el src llega con los acentos codificados (%C3%A1) pero en disco el
  // archivo se llama con el caracter; se prueban las dos formas
  const candidatas = [rel];
  try {
    const dec = decodeURIComponent(rel);
    if (dec !== rel) candidatas.push(dec);
  } catch {
    // src mal formado: se usa tal cual
  }
  for (const c of candidatas) {
    const abs = path.join(PUBLIC_DIR, c);
    try {
      if (!existsSync(abs)) continue;
      const buf = readFileSync(abs);
      const lower = c.toLowerCase();
      if (lower.endsWith(".png")) out = dimsPng(buf);
      else if (lower.endsWith(".jpg") || lower.endsWith(".jpeg")) out = dimsJpeg(buf);
      else if (lower.endsWith(".svg")) out = dimsSvg(buf);
      if (out) break;
    } catch {
      out = null;
    }
  }
  cache.set(src, out);
  return out;
}

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

export function rehypeImgLazy() {
  return (tree) => {
    walk(tree, (node) => {
      if (node.type !== "element" || node.tagName !== "img") return;
      const props = node.properties || (node.properties = {});
      props.loading = "lazy";
      props.decoding = "async";
      const src = props.src;
      if (typeof src !== "string" || !src.startsWith("/")) return;
      const d = dimensiones(src);
      if (d) {
        props.width = d.w;
        props.height = d.h;
      }
    });
  };
}

export default rehypeImgLazy;
