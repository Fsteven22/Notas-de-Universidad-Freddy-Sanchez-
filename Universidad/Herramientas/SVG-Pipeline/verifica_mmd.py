# -*- coding: utf-8 -*-
"""Verifica que cada SVG tenga su fuente .mmd y que esa fuente lo reproduzca.

Para cada SVG de la carpeta:
  1. exige el .mmd homonimo al lado (R12-svg-sin-mmd);
  2. re-renderiza el .mmd con el pipeline (mmdc_ligero) a un temporal;
  3. compara el TEXTO VISIBLE (nodos, etiquetas de arista y titulo) y el viewBox
     del SVG original con los del SVG re-renderizado.

Salida: 0 si todo cuadra, 1 si hay hallazgos.

Uso:
    py -X utf8 verifica_mmd.py <carpeta> [-o reporte.txt] [--trabajadores 4] [--solo id]
"""
import argparse
import io
import os
import re
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

SVG = "http://www.w3.org/2000/svg"
XHTML = "http://www.w3.org/1999/xhtml"
HERE = Path(__file__).resolve().parent

q = lambda t, ns=SVG: "{%s}%s" % (ns, t)


def texto_visible(path):
    """Texto que el lector ve: etiquetas de nodo, de arista y titulo."""
    root = ET.parse(str(path)).getroot()
    out = []
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag == "span":
            c = el.get("class") or ""
            if "nodeLabel" in c or "edgeLabel" in c:
                t = " ".join("".join(el.itertext()).split())
                if t:
                    out.append(t)
        elif tag == "text":
            c = el.get("class") or ""
            if "TitleText" in c:
                t = " ".join((el.text or "").split())
                if t:
                    out.append(t)
    return out


def viewbox(path):
    root = ET.parse(str(path)).getroot()
    vb = root.get("viewBox") or ""
    try:
        return [float(x) for x in vb.split()]
    except ValueError:
        return None


def render(mmd, destino, timeout=180):
    env = dict(os.environ)
    env.setdefault("PUPPETEER_EXECUTABLE_PATH",
                   r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    cmd = [sys.executable, "-X", "utf8", str(HERE / "mmdc_ligero.py"),
           "-i", str(mmd), "-o", str(destino), "-b", "white"]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                       errors="replace", env=env, timeout=timeout)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def verifica(svg, tmpdir, workers=1):
    mmd = svg.with_suffix(".mmd")
    if not mmd.exists():
        return {"svg": svg.name, "estado": "SIN-MMD"}
    out = Path(tmpdir) / svg.name
    try:
        rc, log = render(mmd, out)
    except Exception as exc:
        return {"svg": svg.name, "estado": "ERROR-RENDER", "detalle": str(exc)}
    if rc != 0 or not out.exists():
        return {"svg": svg.name, "estado": "ERROR-RENDER", "detalle": log.strip()[-300:]}

    ta, tb = texto_visible(svg), texto_visible(out)
    va, vb = viewbox(svg), viewbox(out)
    problemas = []
    if sorted(ta) != sorted(tb):
        faltan = sorted(set(ta) - set(tb))
        sobran = sorted(set(tb) - set(ta))
        problemas.append("texto: faltan %s sobran %s" % (faltan[:3], sobran[:3]))
    if va != vb:
        if va is None or vb is None or len(va) != len(vb) or \
                any(abs(x - y) > 0.01 for x, y in zip(va, vb)):
            problemas.append("viewBox %s != %s" % (va, vb))
    try:
        out.unlink()
    except OSError:
        pass
    return {"svg": svg.name, "estado": "OK" if not problemas else "DIFIERE",
            "detalle": "; ".join(problemas)}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("carpeta")
    ap.add_argument("-o", "--reporte")
    ap.add_argument("--trabajadores", type=int, default=4)
    ap.add_argument("--solo", help="verifica solo este nombre de SVG")
    args = ap.parse_args(argv)

    d = Path(args.carpeta)
    svgs = sorted(d.glob("*.svg"))
    if args.solo:
        svgs = [s for s in svgs if args.solo in s.name]
    print("svg a verificar: %d" % len(svgs))

    resultados = []
    with tempfile.TemporaryDirectory() as tmp:
        with ThreadPoolExecutor(max_workers=args.trabajadores) as ex:
            futs = {ex.submit(verifica, s, tmp, args.trabajadores): s for s in svgs}
            for i, f in enumerate(futs, 1):
                r = f.result()
                resultados.append(r)
                if r["estado"] != "OK":
                    print("  [%3d/%3d] %-11s %s %s" % (
                        i, len(svgs), r["estado"], r["svg"], r.get("detalle", "")))
                elif i % 25 == 0:
                    print("  [%3d/%3d] ok" % (i, len(svgs)))

    bad = [r for r in resultados if r["estado"] != "OK"]
    print()
    print("verificados: %d | OK: %d | con problemas: %d" % (
        len(resultados), len(resultados) - len(bad), len(bad)))
    for r in bad:
        print("  %-11s %s  %s" % (r["estado"], r["svg"], r.get("detalle", "")))
    if args.reporte:
        io.open(args.reporte, "w", encoding="utf-8", newline="\n").write(
            "\n".join("%-11s %s %s" % (r["estado"], r["svg"], r.get("detalle", "")) for r in resultados))
        print("reporte:", args.reporte)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
