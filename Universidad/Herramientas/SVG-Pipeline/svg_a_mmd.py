# -*- coding: utf-8 -*-
"""Reconstruye la fuente mermaid (`.mmd`) de un SVG flowchart generado por mermaid.

El SVG que produce mermaid lleva la informacion necesaria para volver a su fuente:
los ids de nodo (`my-svg-flowchart-<ID>-<n>`), las aristas (`my-svg-L_<ORIGEN>_<DESTINO>_<n>`),
la forma de cada caja (rect / rect redondeado / poligono) y los estilos de fill/stroke/color.

Uso:
    py -X utf8 svg_a_mmd.py -i diagrama.svg -o diagrama.mmd
    py -X utf8 svg_a_mmd.py --lote <carpeta>        # reconstruye todos los flowchart sin .mmd
    py -X utf8 svg_a_mmd.py --lote <carpeta> --sincronizar   # alinea el titulo de los .mmd

Limite conocido: los diagramas con SUBGRAFOS (clusters) no se reconstruyen aqui; su
`.mmd` se edita a mano (ver `Bienvenida_y_Syllabus_Cálculo_de_una_Variable_01.mmd`:
`flowchart LR` + `direction TB` dentro de cada subgraph reproduce el layout original).

Nunca sobrescribe un `.mmd` que ya existe (salvo con `--forzar`).
"""
import argparse
import io
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

SVG = "http://www.w3.org/2000/svg"
XHTML = "http://www.w3.org/1999/xhtml"

RE_NODO = re.compile(r"^my-svg-flowchart-(.+)-(\d+)$")
RE_ARISTA = re.compile(r"^my-svg-L_(.+?)_(.+?)_(\d+)$")


def q(tag, ns=SVG):
    return "{%s}%s" % (ns, tag)


def attr(el, name):
    return el.get(name) or ""


def texto_label(span):
    """Convierte el HTML del nodeLabel en texto mermaid conservando los <br/>."""
    partes = []

    def rec(el):
        tag = el.tag.split("}")[-1]
        if tag == "br":
            partes.append("<br/>")
        else:
            if el.text:
                partes.append(el.text)
            for c in el:
                rec(c)
                if c.tail:
                    partes.append(c.tail)

    rec(span)
    txt = "".join(partes).strip()
    txt = re.sub(r"\s*\n\s*", "<br/>", txt)
    return txt


def esc_mermaid(txt):
    """Escapa lo que rompe el lexer de mermaid dentro de un label entre comillas."""
    return txt.replace('"', "#quot;")


def parse_svg(path):
    root = ET.parse(str(path)).getroot()
    rol = attr(root, "aria-roledescription")
    vb = attr(root, "viewBox")
    nodos = {}
    orden = []
    aristas = []
    labels_arista = {}

    for g in root.iter(q("g")):
        cls = attr(g, "class")
        partes = cls.split()
        if "node" in partes:
            nid = attr(g, "id")
            m = RE_NODO.match(nid)
            if not m:
                continue
            key = m.group(1)
            label = ""
            color = None
            for span in g.iter(q("span", XHTML)):
                sc = attr(span, "class")
                if "nodeLabel" in sc:
                    label = texto_label(span)
                    st = attr(span, "style")
                    mc = re.search(r"color:\s*(#[0-9a-fA-F]{3,8})", st)
                    if mc:
                        color = mc.group(1)
            forma = "rect"
            fill = stroke = None
            pos = None
            tr = attr(g, "transform")
            mt = re.search(r"translate\(\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)", tr)
            if mt:
                pos = (float(mt.group(1)), float(mt.group(2)))
            for sub in g.iter():
                tag = sub.tag.split("}")[-1]
                sc = attr(sub, "class")
                if tag == "rect" and "label-container" in sc:
                    if sub.get("rx"):
                        forma = "rect-xy"
                    st = attr(sub, "style")
                    mf = re.search(r"fill:\s*(#[0-9a-fA-F]{3,8})", st)
                    ms = re.search(r"stroke:\s*(#[0-9a-fA-F]{3,8})", st)
                    if mf:
                        fill = mf.group(1)
                    if ms:
                        stroke = ms.group(1)
                elif tag == "polygon":
                    forma = "rombo"
                elif tag == "circle":
                    forma = "circulo"
            if key not in nodos:
                nodos[key] = {
                    "id": key, "label": label, "forma": forma, "fill": fill,
                    "stroke": stroke, "color": color, "pos": pos,
                }
                orden.append(key)

    for path in root.iter(q("path")):
        if "flowchart-link" not in attr(path, "class"):
            continue
        pid = attr(path, "id")
        m = RE_ARISTA.match(pid)
        if not m:
            continue
        aristas.append({"src": m.group(1), "dst": m.group(2)})

    for g in root.iter(q("g")):
        if attr(g, "class") != "edgeLabel":
            continue
        for sub in g.iter(q("g")):
            did = attr(sub, "data-id")
            if not did:
                continue
            txt = ""
            for span in sub.iter(q("span", XHTML)):
                if "edgeLabel" in attr(span, "class"):
                    txt = texto_label(span)
            labels_arista[did] = txt

    # etiqueta de arista: se empareja por prefijo L_<src>_<dst>_
    for a in aristas:
        pre = "L_%s_%s_" % (a["src"], a["dst"])
        for did, txt in labels_arista.items():
            if did.startswith(pre) and txt:
                a["label"] = txt
                break
        a.setdefault("label", "")

    # titulo del diagrama (mermaid lo pinta como <text class="flowchartTitleText">)
    titulo = ""
    for el in root.iter(q("text")):
        if "flowchartTitleText" in attr(el, "class"):
            titulo = (el.text or "").strip()
            break

    return {"rol": rol, "viewbox": vb, "nodos": nodos, "orden": orden,
            "aristas": aristas, "nodo_count": len(nodos), "titulo": titulo}


DELIMS = {
    # todos los labels van entre comillas dobles: es lo unico que sobrevive a
    # llaves, pipes, punto y coma y signos de comparacion sin romper el lexer
    "rect": ('["', '"]'),
    "rect-xy": ('("', '")'),
    "rombo": ('{"', '"}'),
    "circulo": ('(("', '"))'),
}


def direccion_por_geometria(data):
    """Deduce LR/TD mirando hacia donde avanza el grafo.

    En mermaid TD el flujo avanza en Y (cada hijo queda debajo del padre); en LR
    avanza en X (cada hijo queda a la derecha). Se cuenta, para cada eje, cuantas
    aristas avanzan en ese eje; el eje que mas avanza es el de la direccion.
    """
    # nivel de cada nodo (profundidad desde la raiz)
    nivel = {}

    def prof(id_, parent=None):
        if id_ in nivel:
            return nivel[id_]
        nivel[id_] = 0
        for a in data["aristas"]:
            if a["src"] == id_:
                nivel[id_] = max(nivel[id_], prof(a["dst"], id_) + 1)
            elif a["dst"] == id_ and parent is None:
                nivel[id_] = max(nivel[id_], 0)
        return nivel[id_]

    for a in data["aristas"]:
        prof(a["src"])
        prof(a["dst"])

    fwd_x = fwd_y = 0
    tot = 0
    for a in data["aristas"]:
        s = data["nodos"].get(a["src"])
        d = data["nodos"].get(a["dst"])
        if not s or not d or not s["pos"] or not d["pos"]:
            continue
        tot += 1
        if d["pos"][0] > s["pos"][0]:
            fwd_x += 1
        if d["pos"][1] > s["pos"][1]:
            fwd_y += 1
    if not tot:
        return "LR"
    if fwd_x == fwd_y:
        # empate: el eje que mas correlaciona con el nivel del nodo
        corr_x = corr_y = 0
        for key, n in data["nodos"].items():
            if not n["pos"]:
                continue
            lvl = nivel.get(key, 0)
            corr_x += lvl * n["pos"][0]
            corr_y += lvl * n["pos"][1]
        return "LR" if corr_x >= corr_y else "TD"
    return "LR" if fwd_x > fwd_y else "TD"


def frontmatter(titulo):
    """Bloque YAML que mermaid lee como titulo del diagrama."""
    if not titulo:
        return ""
    return '---\ntitle: "%s"\n---\n' % titulo.replace('"', '\\"')


def genera_mmd(data, direccion="LR"):
    L = []
    fm = frontmatter(data.get("titulo", ""))
    if fm:
        L.append(fm.rstrip("\n"))
    L.append("flowchart %s" % direccion)
    for key in data["orden"]:
        n = data["nodos"][key]
        abre, cierra = DELIMS.get(n["forma"], DELIMS["rect"])
        L.append('    %s%s%s%s' % (key, abre, esc_mermaid(n["label"]), cierra))
    for a in data["aristas"]:
        if a.get("label"):
            L.append('    %s -->|"%s"| %s' % (a["src"], esc_mermaid(a["label"]), a["dst"]))
        else:
            L.append("    %s --> %s" % (a["src"], a["dst"]))
    estilos = []
    for key in data["orden"]:
        n = data["nodos"][key]
        props = []
        if n["fill"]:
            props.append("fill:%s" % n["fill"])
        if n["stroke"]:
            props.append("stroke:%s" % n["stroke"])
        if n["color"]:
            props.append("color:%s" % n["color"])
        if props:
            estilos.append("    style %s %s" % (key, ",".join(props)))
    if estilos:
        L.append("")
        L.extend(estilos)
    return "\n".join(L) + "\n"


def sincroniza_titulo(mmd_path, titulo):
    """Alinea el frontmatter de un .mmd existente con el titulo que muestra su SVG.

    Devuelve True si el archivo cambio. No toca el cuerpo del diagrama.
    """
    txt = io.open(str(mmd_path), encoding="utf-8").read()
    if not titulo:
        return False
    want = frontmatter(titulo)
    if txt.startswith("---"):
        fin = txt.find("\n---", 3)
        if fin > 0:
            cuerpo = txt[fin + 4:].lstrip("\n")
            actual = txt[:fin + 4]
            if re.search(r'^title:\s*"?%s"?\s*$' % re.escape(titulo), actual, re.M):
                return False
            nuevo = want.rstrip("\n") + cuerpo
            if nuevo != txt:
                io.open(str(mmd_path), "w", encoding="utf-8", newline="\n").write(nuevo)
                return True
            return False
        return False
    if txt.startswith("---") is False and want:
        nuevo = want + txt
        io.open(str(mmd_path), "w", encoding="utf-8", newline="\n").write(nuevo)
        return True
    return False


def main(argv=None):
    ap = argparse.ArgumentParser(description="Reconstruye .mmd desde un SVG flowchart de mermaid")
    ap.add_argument("-i", "--input", help="SVG de entrada")
    ap.add_argument("-o", "--output", help="mmd de salida")
    ap.add_argument("--lote", help="carpeta con SVG (reconstruye los que no tienen .mmd)")
    ap.add_argument("--direccion", choices=["LR", "TD"], help="fuerza la direccion del diagrama")
    ap.add_argument("--forzar", action="store_true", help="sobrescribe un .mmd existente")
    ap.add_argument("--sincronizar", action="store_true",
                    help="solo alinea el titulo (frontmatter) de los .mmd ya existentes")
    args = ap.parse_args(argv)

    if args.lote:
        d = Path(args.lote)
        hechos = 0
        for svg in sorted(d.glob("*.svg")):
            mmd = svg.with_suffix(".mmd")
            if args.sincronizar:
                if not mmd.exists():
                    print("[FALTA] %s: no hay .mmd" % svg.name)
                    continue
                data = parse_svg(svg)
                if sincroniza_titulo(mmd, data.get("titulo", "")):
                    print("[TITULO] %s: frontmatter actualizado -> %r" % (svg.name, data.get("titulo", "")))
                    hechos += 1
                continue
            if mmd.exists() and not args.forzar:
                continue
            data = parse_svg(svg)
            if data["rol"] != "flowchart-v2":
                print("[SKIP] %s: no es flowchart-v2 (%s)" % (svg.name, data["rol"]))
                continue
            dir_ = args.direccion or direccion_por_geometria(data)
            io.open(str(mmd), "w", encoding="utf-8", newline="\n").write(genera_mmd(data, dir_))
            hechos += 1
            print("[OK] %s -> %s (%s, %d nodos, %d aristas)" % (
                svg.name, mmd.name, dir_, len(data["nodos"]), len(data["aristas"])))
        print("procesados:", hechos)
        return 0

    if not args.input or not args.output:
        ap.print_help()
        return 1
    data = parse_svg(Path(args.input))
    dir_ = args.direccion or direccion_por_geometria(data)
    io.open(args.output, "w", encoding="utf-8", newline="\n").write(genera_mmd(data, dir_))
    print("[OK] %s -> %s (%s)" % (args.input, args.output, dir_))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
