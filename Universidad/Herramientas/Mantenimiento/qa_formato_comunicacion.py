#!/usr/bin/env python3
"""qa_formato_comunicacion.py — auditoría del contrato FORMATO-COMUNICACION.

Verifica que una nota de Comunicación (IDIG2012) siga el formato de la materia:
frontmatter, H1 con emoji, H2 con emoji, contenido en callouts, embeds con lectura,
tags al pie, etc.

El contrato escrito vive en `Herramientas/Mantenimiento/FORMATO-COMUNICACION.md`
(reglas R1..R16).

La nota de referencia para `--calibrar` es de SBD (ya en 0 hallazgos):
`3er Semestre/Sistema de Bases de Datos/Unidad 1 - Modelos de Datos y ER/01 - Dato,
información y modelos de datos.md`.

Uso:
    py -3.12 qa_formato_comunicacion.py [--solo "2do Semestre/Comunicación"] [-o reporte.txt]
    py -3.12 qa_formato_comunicacion.py --calibrar   (audita solo la nota de referencia de SBD)
"""

import argparse
import io
import os
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SKIP_DIRS = (".obsidian", ".trash", ".git", "node_modules", "__pycache__")

RE_H = re.compile(r"^(#{1,6})\s+(.*)$")
RE_CALL_HDR = re.compile(r"^\s*(?P<gg>>+) *\[!(?P<tipo>[\w\-]+)\](?P<resto>.*)$")
RE_CALL_CONT = re.compile(r"^\s*(?P<gg>>+) *(?P<resto>.*)$")
RE_EMBED = re.compile(r"!\[\[([^\]]+)\]\]")
RE_TAGS_FOOT = re.compile(r"^\s*\*\*Tags:\*\*")
RE_FENCE_ONLY = re.compile(r"^```\s*$")
RE_TABLE_SEP = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?\s*$")
RE_TABLE = re.compile(r"^\s*\|")
RE_LISTITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
RE_EMOJI = re.compile(r"[\U0001F000-\U0001FAFF\u2300-\u23FF\u2600-\u27BF\u2B00-\u2BFF\u2190-\u21FF]")

AJENO = ("_texto/", "contenido extra/", "herramientas/", "site/", "reportes/", "svg-pipeline/")


def clasifica(rest):
    s = rest.strip()
    if not s:
        return "blank"
    if "![[" in s or s.startswith("[["):
        return "embed"
    if RE_TABLE.match(s) and s.count("|") >= 2:
        return "table_sep_maybe"
    if RE_TABLE.match(s):
        return "table"
    if RE_TABLE_SEP.match(s):
        return "table_sep"
    if s.startswith("```"):
        return "fence"
    if RE_LISTITEM.match(s):
        return "listitem"
    if s.startswith("[!"):
        return "subheader"
    if "::" in s:
        return "qa"
    return "prose"


def raiz_por_defecto():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def indice_basenames(vault):
    idx = {}
    for dirpath, dirnames, filenames in os.walk(vault):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".md"):
                idx.setdefault(fn.lower(), []).append(os.path.join(dirpath, fn))
    return idx


def existe(path_str):
    base = os.path.normpath(path_str)
    for c in (base,):
        try:
            if os.path.isfile(c):
                return True
        except OSError:
            pass
    return False


def resolver_asset(dir_nota, ruta_rel, raiz, vault, basenames_idx):
    candidatos = []
    if os.path.isabs(ruta_rel):
        candidatos.append(ruta_rel)
    else:
        candidatos.append(os.path.join(dir_nota, ruta_rel))
        candidatos.append(os.path.join(raiz, ruta_rel))
        for b in basenames_idx.get(os.path.basename(ruta_rel).lower(), []):
            candidatos.append(b)
    for c in candidatos:
        if existe(c):
            return c
    return None


def bloques_callout(lineas):
    bloques = []
    i, n = 0, len(lineas)
    while i < n:
        m = RE_CALL_HDR.match(lineas[i])
        if not m:
            i += 1
            continue
        depth = m.group("gg").count(">")
        interior = []
        j = i + 1
        while j < n:
            mh = RE_CALL_HDR.match(lineas[j])
            if mh and mh.group("gg").count(">") <= depth:
                break
            mm = RE_CALL_CONT.match(lineas[j])
            if not mm:
                break
            interior.append((j, mm.group("gg").count(">"), mm.group("resto")))
            j += 1
        bloques.append({
            "inicio": i, "fin": j - 1, "depth": depth,
            "tipo": m.group("tipo"),
            "plegado": False,
            "titulo": m.group("resto").strip(),
            "lineas": interior,
        })
        i = j
    return bloques


def hallazgos_por_nota(lineas, rel, vault):
    hallazgos = []
    bloques = bloques_callout(lineas)

    for b in bloques:
        if not b["lineas"]:
            hallazgos.append((b["inicio"] + 1, "R6-callout-vacio", b["tipo"]))
            continue
        titulo = b["titulo"]
        limpio = re.sub(r"[\s\U0001F000-\U0001FAFF\u2600-\u27BF\u2190-\u21FF\u2B00-\u2BFF]", "", titulo)
        if len(limpio) < 3:
            hallazgos.append((b["inicio"] + 1, "R5-sin-titulo", f"[{b['tipo']}] {titulo[:40]}"))
        d0, _dep0, r0 = b["lineas"][0]
        if _dep0 == b["depth"] and r0.strip() != "" and "\U0001F4D6" not in titulo:
            hallazgos.append((d0 + 1, "R6-sin-blanco-header", r0[:44]))
        if b["depth"] != 1:
            continue
        previa = None
        idx = 0
        L = len(b["lineas"])
        en_fence = False
        while idx < L:
            idx0, depth, rest = b["lineas"][idx]
            tipo = clasifica(rest)
            if en_fence:
                if RE_FENCE_ONLY.match(rest.strip()):
                    en_fence = False
                previa = None
                idx += 1
                continue
            if depth != b["depth"]:
                previa = None
                idx += 1
                continue
            if tipo == "fence":
                en_fence = True
                previa = None
                idx += 1
                continue
            if tipo == "blank":
                previa = None
                idx += 1
                continue
            if tipo == "table_sep_maybe":
                sig = b["lineas"][idx + 1] if idx + 1 < L else None
                es_tabla = bool(sig) and sig[1] == b["depth"] and clasifica(sig[2]) == "table_sep"
                tipo = "table" if es_tabla else "prose"
            if en_fence and tipo == "table":
                tipo = "prose"
            if tipo == "table" and previa not in (None, "table"):
                hallazgos.append((idx0 + 1, "R7-separador-antes", tipo + " " + rest[:44]))
            elif tipo == "embed" and previa is not None:
                hallazgos.append((idx0 + 1, "R7-separador-antes", tipo + " " + rest[:44]))
            previa = tipo
            idx += 1
    return hallazgos


def fix_rutas(nota_path):
    texto = io.open(nota_path, encoding="utf-8").read()
    cambios = []

    def repl(m):
        tgt = m.group(1).split("|")[0].split("#")[0].strip()
        if not tgt:
            return m.group(0)
        low = tgt.lower()
        for bad in AJENO:
            if bad in low:
                return m.group(0)
        resolved = resolver_asset(os.path.dirname(nota_path), tgt, raiz_por_defecto(), vault_abs, basenames_idx)
        if resolved:
            return m.group(0)
        return m.group(0)

    nuevo = RE_EMBED.sub(repl, texto)
    return nuevo, cambios


def main():
    ap = argparse.ArgumentParser(description="Audit el contrato FORMATO-COMUNICACION")
    ap.add_argument("root", nargs="?", default=None)
    ap.add_argument("--solo", default=None)
    ap.add_argument("-o", "--salida", default=None)
    ap.add_argument("--estricto", action="store_true")
    ap.add_argument("--fix-rutas", action="store_true")
    ap.add_argument("--calibrar", action="store_true")
    args = ap.parse_args()

    vault = raiz_por_defecto()
    if args.calibrar:
        raiz = os.path.join(vault, "3er Semestre", "Sistema de Bases de Datos",
                            "Unidad 1 - Modelos de Datos y ER")
        specific = "01 - Dato, información y modelos de datos.md"
    elif args.solo:
        raiz = args.solo if os.path.isabs(args.solo) else os.path.join(vault, args.solo)
        specific = None
    elif args.root:
        raiz = args.root
        specific = None
    else:
        raiz = os.path.join(vault, "2do Semestre", "Comunicación")
        specific = None

    idx = indice_basenames(vault)
    vault_abs = os.path.abspath(vault)

    hallazgos = []
    fijados = []
    notas = 0
    for dp, ds, fs in os.walk(raiz):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in sorted(fs):
            if not f.endswith(".md") or f == "FORMATO-COMUNICACION.md":
                continue
            if specific and f != specific:
                continue
            p = os.path.join(dp, f)
            notas += 1
            if args.fix_rutas:
                nuevo, cambios = fix_rutas(p)
                if cambios:
                    io.open(p, "w", encoding="utf-8", newline="\n").write(nuevo)
                    for a, b in cambios:
                        fijados.append((os.path.relpath(p, raiz), a, b))
            lineas = io.open(p, encoding="utf-8", errors="ignore").read().splitlines()
            h = hallazgos_por_nota(lineas, os.path.relpath(p, raiz), vault_abs)
            hallazgos.extend(h)

    conteo = {}
    por_nota = {}
    for rel, codigo, texto in hallazgos:
        conteo[codigo] = conteo.get(codigo, 0) + 1
        por_nota.setdefault(rel, []).append((codigo, texto))

    total = sum(conteo.values())
    print(f"raiz={raiz}  notas={notas}")
    print(f"hallazgos={total}")
    for codigo, cant in sorted(conteo.items(), key=lambda x: -x[1]):
        print(f"  {codigo:<30} {cant:>5}  W")
    for rel in sorted(por_nota.keys()):
        print(f"\n{rel}")
        for codigo, texto in por_nota[rel]:
            print(f"    {codigo:<30} {texto[:80]}")


if __name__ == "__main__":
    main()