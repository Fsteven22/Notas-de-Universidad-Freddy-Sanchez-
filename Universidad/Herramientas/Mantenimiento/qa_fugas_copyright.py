#!/usr/bin/env python3
"""qa_fugas_copyright.py — detecta archivos excluidos que se siguen publicando.

Lee Universidad/_no-publicar.txt (patrones con comodines * y ?, match por nombre
o ruta) y verifica que ninguno de esos archivos aparezca publicado en
site/public/assets/. También detecta variantes _OCR de archivos excluidos cuyo
patron no las cubre directamente.

Sirve como red de seguridad para evitar que material con copyright llegue al
sitio publicado o a los ZIPs.

Convenciones del vault (Mantenimiento/):
  - Corre DRY por defecto (solo reporte). --apply no aplica aqui: es solo lectura.
  - --vault <ruta>  raiz del vault (default: deducida desde la ubicacion del script)
  - -o <reporte>    escribe reporte en archivo (default: solo consola)
  - Exit code != 0 si hay hallazgos (para CI)
  - Excluye: .obsidian, .trash, .git, node_modules

Uso:
  py qa_fugas_copyright.py --vault "C:\\...\\OneSyncFiles" -o reporte.txt
"""

import argparse
import os
import re
import sys
from pathlib import Path

def raiz_por_defecto():
    aqui = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(os.path.dirname(aqui)))

SKIP_DIRS = (".obsidian", ".trash", ".git", "node_modules")


def glob_to_regex(pat: str) -> re.Pattern:
    """Convierte un patron glob (* y ?) a regex. Match por nombre o ruta."""
    out = ""
    for ch in pat:
        if ch == "*":
            out += ".*"
        elif ch == "?":
            out += "."
        else:
            out += re.escape(ch)
    return re.compile("^" + out + "$", re.IGNORECASE)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--vault", default=None, help="raiz del vault (default: deducida)")
    ap.add_argument("--apply", action="store_true", help="(no-op: este script es solo lectura)")
    ap.add_argument("-o", "--salida", default=None, help="ruta del reporte de salida")
    args = ap.parse_args()

    vault = os.path.abspath(args.vault) if args.vault else raiz_por_defecto()
    uni = os.path.join(vault, "Universidad")
    np_file = os.path.join(uni, "_no-publicar.txt")
    assets_dir = os.path.join(vault, "site", "public", "assets")

    if not os.path.isfile(np_file):
        print(f"_no-publicar.txt no existe en: {uni}")
        return 2

    # Leer patrones de exclusion
    patrones = []
    with open(np_file, encoding="utf-8") as fh:
        for linea in fh:
            l = linea.strip()
            if l and not l.startswith("#"):
                patrones.append(l)

    regexs = [glob_to_regex(p) for p in patrones]

    # Escanear assets publicados
    fugas = []
    if os.path.isdir(assets_dir):
        for dp, ds, fs in os.walk(assets_dir):
            ds[:] = [d for d in ds if d not in SKIP_DIRS]
            for f in fs:
                nombre = f.name
                for patron, rx in zip(patrones, regexs):
                    if rx.match(nombre):
                        ruta = os.path.join(dp, f)
                        rel = os.path.relpath(ruta, vault)
                        fugas.append((f"FUGA: {nombre}  (patron: {patron})", rel))
                        break

    # Variantes _OCR de archivos excluidos (patron no cubre directamente)
    variantes_ocr = []
    if os.path.isdir(assets_dir):
        for dp, ds, fs in os.walk(assets_dir):
            ds[:] = [d for d in ds if d not in SKIP_DIRS]
            for f in fs:
                nombre = f.name
                if "_OCR" not in nombre:
                    continue
                base = nombre.replace("_OCR", "")
                for patron, rx in zip(patrones, regexs):
                    if rx.match(base):
                        ruta = os.path.join(dp, f)
                        rel = os.path.relpath(ruta, vault)
                        variantes_ocr.append(
                            f"FUGA_OCR: {nombre}  (patron cubre '{base}' via '{patron}')  [{rel}]"
                        )
                        break

    lineas = [
        f"patrones de exclusion: {len(patrones)}",
        f"fugas directas: {len(fugas)}",
        f"variantes _OCR no cubiertas: {len(variantes_ocr)}",
        "",
    ]
    for txt, _ in fugas:
        lineas.append(f"  {txt}")
    for txt in variantes_ocr:
        lineas.append(f"  {txt}")
    lineas.append("")

    reporte = "\n".join(lineas) + "\n"

    if args.salida:
        with open(args.salida, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(reporte)
        print(f"reporte escrito en: {args.salida}")
    else:
        print(reporte, end="")

    return 1 if (fugas or variantes_ocr) else 0


if __name__ == "__main__":
    raise SystemExit(main())
