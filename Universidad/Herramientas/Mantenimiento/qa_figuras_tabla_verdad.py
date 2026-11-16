# -*- coding: utf-8 -*-
"""
qa_figuras_tabla_verdad.py - Verifica las figuras de tablas de verdad de
Matematicas Discretas SIN abrirlas a ojo.

Seis comprobaciones por figura:
  1. CATALOGO: cada tabla de verdad de las notas tiene figura registrada
     y cada figura registrada tiene su tabla (bidireccional).
  2. PNG: existe, dimensiones razonables y no esta en blanco.
  3. COLOR: pixeles verdes (V) y rojos (F) presentes si la tabla tiene V/F.
  4. TEXTO: se re-dibuja la spec en SVG (vectorial, con texto real) y se
     extraen los <text> recorriendo el arbol. Se comprueba que el
     multiset de V/F es EXACTAMENTE el de la tabla de la nota y que
     estan los simbolos de la cabecera.
  5. GEOMETRIA: se mide la caja real de cada texto (renderer de
     matplotlib): nada fuera del lienzo, nada solapado.
  6. FRESCOR: el PNG del disco es pixel a pixel el que produce el
     generador hoy -> si editaste la tabla y no regeneraste, falla.

Uso:
    py -3.12 qa_figuras_tabla_verdad.py
    py -3.12 qa_figuras_tabla_verdad.py --solo X
"""
import argparse
import importlib.util
import os
import re
import sys
import tempfile
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams["svg.fonttype"] = "none"
import matplotlib.pyplot as plt
from PIL import Image, ImageChops

RUTA_GEN = os.path.join(
    os.path.expanduser("~"), "OneDrive", "OneSyncFiles", "Universidad",
    "Herramientas", "Mantenimiento", "gen_tablas_verdad.py",
)

spec_mod = importlib.util.spec_from_file_location("gen", RUTA_GEN)
gen = importlib.util.module_from_spec(spec_mod)
spec_mod.loader.exec_module(gen)

VERDE = (30, 132, 73)     # EXITO
ROJO = (231, 76, 60)      # PELIGRO
TOL = 60

# latex -> simbolo que mathtext dibuja (y que aparece en el SVG)
OPS = {
    r"\neg": "¬", r"\vee": "∨", r"\lor": "∨", r"\wedge": "∧", r"\land": "∧",
    r"\veebar": "⊻", r"\oplus": "⊕", r"\rightarrow": "→", r"\to": "→",
    r"\leftrightarrow": "↔", r"\Leftrightarrow": "⇔", r"\equiv": "≡",
    r"\not": "¬", r"\neq": "≠", r"\leq": "≤", r"\geq": "≥", r"\times": "×",
}


# ---------------------------------------------------------------- texto
def texto_figura(spec_t, ruta_svg):
    """Re-dibuja en SVG y extrae todos los textos (recorriendo el arbol)."""
    gen.dibujar(spec_t, ruta_svg)
    arbol = ET.parse(ruta_svg).getroot()
    textos = []
    for nodo in arbol.iter():
        if nodo.tag.endswith("text") or nodo.tag.endswith("tspan"):
            t = (nodo.text or "").strip()
            if t:
                textos.append(t)
    return textos


def tokens_esperados(cabecera):
    """Simbolos que debe contener el texto dibujado de una cabecera."""
    s = str(cabecera)
    for cmd, sym in sorted(OPS.items(), key=lambda kv: -len(kv[0])):
        s = s.replace(cmd, sym)
    s = s.replace("$", "").replace("{", "").replace("}", "")
    s = re.sub(r"\\[a-zA-Z]+", "", s)          # comandos sueltos
    toks = set()
    for ch in s:
        if ch.isalpha() or ch in "∨∧¬⊻⊕→↔⇔≡≠≤≥×":
            toks.add(ch)
    return toks


# ---------------------------------------------------------------- png
def _cerca(c, ref, tol=TOL):
    return all(abs(int(a) - int(b)) <= tol for a, b in zip(c[:3], ref[:3]))


def revisar_png(ruta):
    """Devuelve (ok, [problemas], stats)."""
    problemas = []
    if not os.path.isfile(ruta):
        return False, ["no existe"], {}
    im = Image.open(ruta).convert("RGB")
    w, h = im.size
    pix = im.load()
    verde = rojo = oscuros = 0
    total = w * h
    for y in range(0, h, 2):
        for x in range(0, w, 2):
            c = pix[x, y]
            if _cerca(c, VERDE):
                verde += 1
            elif _cerca(c, ROJO):
                rojo += 1
            if sum(c[:3]) < 330:
                oscuros += 1
    stats = {"px": total, "ancho": w, "alto": h,
             "verde": verde, "rojo": rojo, "oscuros": oscuros}
    if w < 200 or h < 80:
        problemas.append("dimensiones anomalas %dx%d" % (w, h))
    if oscuros < 50:
        problemas.append("figura casi vacia (%d pixeles oscuros)" % oscuros)
    return (not problemas), problemas, stats


def comparar_png(ruta, ruta_nueva):
    """El PNG del disco debe ser IDENTICO al que genera el script hoy."""
    if not os.path.isfile(ruta):
        return "no existe"
    a = Image.open(ruta).convert("RGB")
    b = Image.open(ruta_nueva).convert("RGB")
    if a.size != b.size:
        return "desfasado (%dx%d vs %dx%d)" % (a.size[0], a.size[1],
                                              b.size[0], b.size[1])
    diff = ImageChops.difference(a, b)
    if diff.getbbox() is not None:
        return "desfasado (la tabla de la nota cambio: regenera)"
    return None


# ---------------------------------------------------------------- geometria
def revisar_geometria(spec_t):
    """Mide las cajas de texto reales: salida del lienzo y solapamientos."""
    fig = gen.dibujar_para_auditar(spec_t)
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    W, H = fig.canvas.get_width_height()

    cajas = []
    for ax in fig.axes:
        for txt in ax.texts:
            t = txt.get_text()
            if not t.strip():
                continue
            bb = txt.get_window_extent(renderer=rend)
            cajas.append((t, bb))

    problemas = []
    for t, bb in cajas:
        if bb.x0 < -1 or bb.y0 < -1 or bb.x1 > W + 1 or bb.y1 > H + 1:
            problemas.append("texto fuera del lienzo: %r" % t[:32])

    # solapamiento entre cajas de texto (mismo eje, con margen)
    for i in range(len(cajas)):
        for j in range(i + 1, len(cajas)):
            t1, b1 = cajas[i]
            t2, b2 = cajas[j]
            ox = min(b1.x1, b2.x1) - max(b1.x0, b2.x0)
            oy = min(b1.y1, b2.y1) - max(b1.y0, b2.y0)
            if ox > 2 and oy > 2:
                problemas.append("textos solapados: %r / %r"
                                 % (t1[:22], t2[:22]))
    plt.close(fig)
    return problemas, len(cajas)


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--solo", help="revisar una sola figura")
    args = ap.parse_args()

    destino = gen.carpeta_destino()
    nombres = [args.solo] if args.solo else sorted(gen.CATALOGO)
    if args.solo and args.solo not in gen.CATALOGO:
        print("NO existe en el catalogo:", args.solo)
        return 1

    fallos = 0
    tmpdir = tempfile.mkdtemp(prefix="qa_tabla_")

    # --- 1. CATALOGO <-> NOTAS
    if gen.HUERFANOS:
        fallos += len(gen.HUERFANOS)
        print("FAIL catalogo <-> notas")
        for que, detalle in gen.HUERFANOS:
            print("     %s: %s" % (que, detalle))

    for nombre in nombres:
        spec_t = gen.CATALOGO[nombre]
        problemas = []

        # --- 4. TEXTO (re-dibujo a SVG con texto real)
        svg_tmp = os.path.join(tmpdir, nombre + ".svg")
        try:
            textos = texto_figura(spec_t, svg_tmp)
        except Exception as e:
            problemas.append("no se pudo dibujar: %s" % str(e)[:60])
            textos = []
        if not textos:
            problemas.append("el SVG no contiene texto (svg.fonttype != none)")
        else:
            # 4a. multiset V/F exacto
            vf_figura = [t for t in textos if t in ("V", "F")]
            vf_tabla = [c for fila in spec_t["filas"] for c in fila
                        if c in ("V", "F")]
            if sorted(vf_figura) != sorted(vf_tabla):
                problemas.append("V/F de la figura != V/F de la tabla "
                                 "(figura %d, tabla %d)"
                                 % (len(vf_figura), len(vf_tabla)))
            # 4b. simbolos de la cabecera presentes
            plano = " ".join(textos)
            for cab, _ in spec_t["cols"]:
                for tok in tokens_esperados(cab):
                    if tok not in plano:
                        problemas.append("falta el simbolo %r de la cabecera" % tok)
            # 4c. titulo presente
            tit = spec_t["titulo"]
            if tit not in plano:
                problemas.append("falta el titulo: %r" % tit[:40])

        # --- 2 y 3. PNG
        ruta_png = os.path.join(destino, nombre + ".png")
        ok_png, probs_png, stats = revisar_png(ruta_png)
        problemas += probs_png

        hay_v = any(c in ("V", "F") for f in spec_t["filas"] for c in f)
        if hay_v and stats.get("verde", 0) == 0:
            problemas.append("sin pixeles verdes (ningun V dibujado)")
        if hay_v and stats.get("rojo", 0) == 0:
            problemas.append("sin pixeles rojos (ningun F dibujado)")

        # --- 5. GEOMETRIA
        try:
            probs_geo, n_textos = revisar_geometria(spec_t)
            problemas += probs_geo
        except Exception as e:
            problemas.append("no se pudo medir geometria: %s" % str(e)[:50])
            n_textos = 0

        # --- 6. FRESCOR (el PNG del disco vs el que genera el script hoy)
        png_tmp = os.path.join(tmpdir, nombre + ".nuevo.png")
        try:
            gen.dibujar(spec_t, png_tmp)
            desfasado = comparar_png(ruta_png, png_tmp)
            if desfasado:
                problemas.append("PNG %s" % desfasado)
        except Exception as e:
            problemas.append("no se pudo regenerar: %s" % str(e)[:50])

        if problemas:
            fallos += 1
            print("FAIL %-44s %s" % (nombre, problemas))
        else:
            print("OK   %-44s %4dx%-4d  %2d textos  V:%-4d F:%-4d  %6.1f KB  %s"
                  % (nombre, stats["ancho"], stats["alto"], n_textos,
                     stats["verde"], stats["rojo"],
                     os.path.getsize(ruta_png) / 1024.0, spec_t["origen"]))

    print("---- figuras: %d, fallos: %d" % (len(nombres), fallos))
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
