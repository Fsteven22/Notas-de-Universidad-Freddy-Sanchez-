# -*- coding: utf-8 -*-
"""Subconjunta la fuente incrustada de los SVG de Mermaid.

Los SVG que genera Mermaid CLI llevan la tipografia "Recursive Variable" incrustada
como data URI en un <style>, con 4 subconjuntos (cirilico, latin-ext, griego, latin).
Son ~160 KB de base64 por archivo, el 90% del peso, y se repiten en los 2.126 SVG.

Este script deja en cada SVG solo los glifos que ese diagrama usa, conservando:
  - la misma tipografia (misma variable font, mismo eje wght, mismos avances y contornos)
  - la licencia OFL incrustada
  - el SVG como archivo autonomo (sigue siendo valido en <img>, Obsidian o descargado)

Uso:
  py -3.12 subconjuntar_fuente.py <carpeta|archivo> [...] [--dry-run] [--out DIR]

Requerimiento: fontTools + brotli (pip install fonttools brotli)
"""
import base64
import io
import os
import re
import sys
import unicodedata

try:
    from fontTools import subset
    from fontTools.ttLib import TTFont
except ImportError:
    print("FALTA fontTools: py -3.12 -m pip install fonttools brotli")
    raise SystemExit(2)

try:
    import brotli  # noqa: F401  (lo necesita fontTools para leer woff2)
except ImportError:
    print("FALTA brotli: py -3.12 -m pip install brotli")
    raise SystemExit(2)

FACE = re.compile(r"@font-face\s*\{[^{}]*\}", re.S)
B64 = re.compile(r"base64,([A-Za-z0-9+/=]+)")
RANGE = re.compile(r"unicode-range:\s*([^;}]+)")
STYLE = re.compile(r"<style[^>]*>.*?</style>", re.S)
ATTR = re.compile(r'(?:aria-label|title|alt)="([^"]*)"')

RANGO_MIN = 0
RANGO_MAX = 0x10FFFF


def parse_rangos(texto):
    """Convierte 'U+0-FF, U+100-2BA' en una lista de (inicio, fin)."""
    out = []
    if not texto:
        return [(RANGO_MIN, RANGO_MAX)]
    for tok in texto.split(","):
        tok = tok.strip().replace("U+", "").replace("u+", "").replace("?", " ")
        if "-" in tok:
            lo, hi = tok.split("-", 1)
            try:
                out.append((int(lo.strip(), 16), int(hi.strip(), 16)))
            except ValueError:
                return [(RANGO_MIN, RANGO_MAX)]
        else:
            try:
                v = int(tok.strip(), 16)
                out.append((v, v))
            except ValueError:
                return [(RANGO_MIN, RANGO_MAX)]
    return out or [(RANGO_MIN, RANGO_MAX)]


def codepoints_visibles(svg):
    """Caracteres que se ven (texto del diagrama) + los de aria-label/title/alt."""
    sin_estilos = STYLE.sub(" ", svg)
    texto = re.sub(r"<[^>]+>", " ", sin_estilos)
    cps = {ord(c) for c in texto if not c.isspace() and ord(c) > 31}
    for m in ATTR.finditer(svg):
        cps |= {ord(c) for c in m.group(1) if not c.isspace() and ord(c) > 31}
    return cps


def reglas_fuente(svg):
    """Reglas @font-face con payload base64: {css, b64, raw, ranges}."""
    reglas = []
    for fc in FACE.findall(svg):
        m = B64.search(fc)
        if not m:
            continue
        ur = RANGE.search(fc)
        reglas.append({
            "css": fc,
            "b64": m.group(1),
            "raw": base64.b64decode(m.group(1)),
            "ranges": parse_rangos(ur.group(1) if ur else ""),
        })
    return reglas


def subconjuntar_fuente(regla, codepoints):
    """Devuelve el woff2 recortado a codepoints (None si no se puede)."""
    font = TTFont(io.BytesIO(regla["raw"]))
    opts = subset.Options()
    opts.layout_features = ["*"]
    opts.name_IDs = ["*"]          # conserva nombre y licencia
    opts.notdef_outline = True
    opts.recalc_bounds = True
    sub = subset.Subsetter(options=opts)
    sub.populate(unicodes=sorted(codepoints))
    sub.subset(font)
    buf = io.BytesIO()
    font.save(buf)
    return buf.getvalue()


def cmap_de(regla):
    """Codepoints que realmente trae la fuente de una regla (cmap)."""
    try:
        return set(TTFont(io.BytesIO(regla["raw"])).getBestCmap().keys())
    except Exception:
        return set()


MARCA = re.compile(r"/\*fuente-sin-glifo:([^*]*)\*/")


def leer_marca(svg):
    """Glifos que el diagrama usa y que la fuente incrustada NO trae (huecos del original)."""
    huecos = set()
    for m in MARCA.finditer(svg):
        for tok in m.group(1).split(","):
            tok = tok.strip()
            if not tok:
                continue
            try:
                huecos.add(int(tok[2:], 16) if tok.upper().startswith("U+") else int(tok, 16))
            except ValueError:
                pass
    return huecos


def escribir_marca(svg, huecos):
    """Registra en el SVG los glifos que la fuente no trae (CSS comment, no se renderiza)."""
    if not huecos:
        return svg
    marca = "/*fuente-sin-glifo:%s*/" % ",".join("U+%04X" % c for c in sorted(huecos))
    m = re.search(r"@font-face\s*\{", svg)
    if not m:
        return svg
    return svg[:m.start()] + marca + svg[m.start():]


def procesar(svg, dry_run=False):
    """Devuelve (svg_nuevo_o_None, informe)."""
    reglas = reglas_fuente(svg)
    if not reglas:
        return None, {"estado": "sin fuente incrustada", "antes": len(svg), "despues": len(svg)}

    usados = codepoints_visibles(svg)
    # glifos que la fuente ORIGINAL trae de verdad
    original_cmap = set()
    for r in reglas:
        original_cmap |= cmap_de(r)
    # glifos que el diagrama usa y que la fuente original NO trae (se dibujan con la
    # tipografia del sistema: emoji, flechas, prima triple, ZWJ...). Preexistentes.
    huecos = {c for c in usados
              if c not in original_cmap
              and any(any(a <= c <= b for a, b in r["ranges"]) for r in reglas)}

    # cobertura original: que codepoint cubre cada regla
    cubierta_orig = set()
    for r in reglas:
        for c in usados:
            if any(a <= c <= b for a, b in r["ranges"]):
                cubierta_orig.add(c)

    nuevo = svg
    reglas_nuevas = 0
    bytes_antes = sum(len(r["b64"]) for r in reglas)
    bytes_despues = 0
    for r in reglas:
        propios = {c for c in usados if any(a <= c <= b for a, b in r["ranges"])}
        if not propios:
            nuevo = nuevo.replace(r["css"], "")
            continue
        try:
            woff2 = subconjuntar_fuente(r, propios)
        except Exception as exc:                      # pragma: no cover
            return None, {"estado": "error al subconjuntar (%s)" % exc,
                          "antes": len(svg), "despues": len(svg)}
        b64 = base64.b64encode(woff2).decode("ascii")
        nuevo = nuevo.replace(r["b64"], b64)
        bytes_despues += len(b64)
        reglas_nuevas += 1

    # ── verificacion 1: la cobertura por rangos no puede cambiar ──
    reglas_out = reglas_fuente(nuevo)
    cubierta_out = set()
    for r in reglas_out:
        for c in usados:
            if any(a <= c <= b for a, b in r["ranges"]):
                cubierta_out.add(c)
    if cubierta_orig != cubierta_out:
        return None, {"estado": "RECHAZADO: cambia la cobertura de glifos",
                      "antes": len(svg), "despues": len(svg)}

    # ── verificacion 2: ningun glifo que la fuente ORIGINAL traia puede perderse ──
    salida_cmap = set()
    for r in reglas_out:
        salida_cmap |= cmap_de(r)
    perdidos = sorted(c for c in usados if c in original_cmap and c not in salida_cmap)
    if perdidos:
        return None, {"estado": "RECHAZADO: la fuente recortada pierde %s" %
                      " ".join(chr(c) for c in perdidos),
                      "antes": len(svg), "despues": len(svg)}

    if reglas_nuevas == 0:
        return None, {"estado": "sin reglas con glifos usados", "antes": len(svg), "despues": len(svg)}
    if "SIL OPEN FONT LICENSE" in svg and "SIL OPEN FONT LICENSE" not in nuevo:
        return None, {"estado": "RECHAZADO: se perderia la licencia", "antes": len(svg), "despues": len(svg)}

    # ── se registra el hueco de la fuente original (para que el QA lo sepa) ──
    nuevo = escribir_marca(nuevo, huecos)

    return nuevo, {"estado": "ok", "antes": len(svg), "despues": len(nuevo),
                   "reglas_antes": len(reglas), "reglas_despues": reglas_nuevas,
                   "fuente_antes": bytes_antes, "fuente_despues": bytes_despues,
                   "glifos": len(usados), "huecos": len(huecos)}


def aplicar(path, dry_run=False):
    """Subconjunta la fuente de un SVG en el sitio. Devuelve el informe."""
    svg = io.open(path, encoding="utf-8", errors="replace").read()
    nuevo, info = procesar(svg, dry_run)
    if nuevo is not None and nuevo != svg and not dry_run:
        io.open(path, "w", encoding="utf-8", newline="\n").write(nuevo)
        info["cambiado"] = True
    else:
        info["cambiado"] = False
    return info


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    out_dir = None
    if "--out" in sys.argv:
        out_dir = sys.argv[sys.argv.index("--out") + 1]

    if not args:
        print(__doc__)
        raise SystemExit(1)

    archivos = []
    for a in args:
        if os.path.isdir(a):
            for dp, _ds, fs in os.walk(a):
                for f in fs:
                    if f.endswith(".svg"):
                        archivos.append(os.path.join(dp, f))
        else:
            archivos.append(a)
    archivos.sort()

    tot_antes = tot_despues = 0
    n_ok = n_sin = n_err = 0
    for p in archivos:
        svg = io.open(p, encoding="utf-8", errors="replace").read()
        nuevo, info = procesar(svg, dry)
        tot_antes += info["antes"]
        if nuevo is None:
            if info["estado"].startswith("RECHAZADO") or info["estado"].startswith("error"):
                n_err += 1
                print("  [%s] %s" % (info["estado"], os.path.basename(p)))
            else:
                n_sin += 1
            tot_despues += info["despues"]
            continue
        n_ok += 1
        tot_despues += len(nuevo)
        if out_dir:
            destino = os.path.join(out_dir, os.path.basename(p))
            io.open(destino, "w", encoding="utf-8", newline="\n").write(nuevo)
        elif not dry:
            io.open(p, "w", encoding="utf-8", newline="\n").write(nuevo)

    print()
    print("archivos: %d   transformados: %d   sin fuente: %d   rechazados/errores: %d" % (
        len(archivos), n_ok, n_sin, n_err))
    print("peso: %.1f MB -> %.1f MB  (%.0f%% menos)" % (
        tot_antes / 1048576, tot_despues / 1048576,
        100 * (1 - tot_despues / max(tot_antes, 1))))


if __name__ == "__main__":
    main()
