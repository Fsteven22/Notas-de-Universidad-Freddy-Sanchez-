#!/usr/bin/env python3
"""pdf_a_png.py — captura las páginas de un PDF como PNG (para embeberlas).

La casa no embebe PDFs de clase: se captura la página y se cita por número
(`slides04, pp. 2-4`). Este script hace esa captura de forma reproducible.

  py pdf_a_png.py --pdf "Examen.pdf" --salida "Archivos/Examenes" --prefijo cal1-2023-0s-1par --dpi 140

Reglas:
  · DPI 140 (el de la casa): láminas 16:9 -> 1862x1027 px; carta -> 1190x1540 px.
  · Nombre: <prefijo>-p<NN>.png (NN con 2 digitos, la 1 es p01).
  · No pisa un PNG existente salvo que se pase --sobrescribir.
  · Informe JSON opcional con el tamano y el hash de cada pagina.

Uso:
  py -X utf8 pdf_a_png.py --pdf <pdf> --salida <carpeta> --prefijo <slug> [--dpi 140]
                         [--paginas 1,2,5-7] [--informe <json>] [--sobrescribir]
"""

import argparse
import hashlib
import io
import json
import os
import re

import pymupdf


def seleccionar(npag, spec):
    """'1,2,5-7' -> [1,2,5,6,7] (1-based)."""
    if not spec:
        return list(range(1, npag + 1))
    out = []
    for parte in spec.split(","):
        parte = parte.strip()
        if "-" in parte:
            a, b = parte.split("-", 1)
            out.extend(range(int(a), int(b) + 1))
        elif parte:
            out.append(int(parte))
    return [p for p in out if 1 <= p <= npag]


def slug(texto):
    s = texto.lower()
    s = s.replace("á", "a").replace("é", "e").replace("í", "i")
    s = s.replace("ó", "o").replace("ú", "u").replace("ñ", "n")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def main():
    ap = argparse.ArgumentParser(description="Captura paginas de PDF como PNG")
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--salida", required=True)
    ap.add_argument("--prefijo", default=None, help="slug base (por defecto, del nombre del PDF)")
    ap.add_argument("--dpi", type=int, default=140)
    ap.add_argument("--paginas", default="", help="'1,2,5-7' (1-based); vacio = todas")
    ap.add_argument("--informe", default=None)
    ap.add_argument("--sobrescribir", action="store_true")
    args = ap.parse_args()

    pdf = args.pdf
    prefijo = args.prefijo or slug(os.path.splitext(os.path.basename(pdf))[0])
    os.makedirs(args.salida, exist_ok=True)

    doc = pymupdf.open(pdf)
    paginas = seleccionar(doc.page_count, args.paginas)
    filas = []
    for n in paginas:
        page = doc[n - 1]
        pix = page.get_pixmap(dpi=args.dpi)
        destino = os.path.join(args.salida, "%s-p%02d.png" % (prefijo, n))
        if os.path.exists(destino) and not args.sobrescribir:
            print("  ya existe: %s" % os.path.basename(destino))
            continue
        pix.save(destino)
        filas.append({
            "pagina": n,
            "archivo": os.path.basename(destino),
            "px": "%dx%d" % (pix.width, pix.height),
            "bytes": os.path.getsize(destino),
            "sha256": hashlib.sha256(io.open(destino, "rb").read()).hexdigest()[:12],
        })
        print("  p%02d -> %s  (%dx%d, %d KB)" % (n, os.path.basename(destino),
                                                pix.width, pix.height, os.path.getsize(destino) // 1024))
    doc.close()

    if args.informe:
        io.open(args.informe, "w", encoding="utf-8").write(json.dumps({
            "pdf": os.path.basename(pdf),
            "prefijo": prefijo,
            "dpi": args.dpi,
            "paginas": filas,
        }, ensure_ascii=False, indent=1))
    print("capturas: %d  ->  %s" % (len(filas), args.salida))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
