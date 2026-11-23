#!/usr/bin/env python3
"""qa_formato_ingles1.py — auditoria del contrato FORMATO-INGLES1.

Verifica que una nota de Ingles I siga el formato que la nota de referencia
ya comparte: frontmatter con IDIG1006, H2 con emoji, todo el contenido dentro
de callouts, vocabulario en tablas dentro de callouts (R15), SVG con lectura
propia (R14), ejercicios con solucion plegada (R8) y tags al pie.

El contrato escrito vive en
`Herramientas/Mantenimiento/FORMATO-INGLES1.md` (reglas R1..R16).

Hereda el nucleo de `qa_formato_algebra.py` (que a su vez hereda de SBD):
no reimplementa R1..R14, las ejecuta. Solo anade R15 (vocabulario en tablas
dentro de callouts) y R16 (enlaces a examenes con alias).

Severidades: H (error duro) y W (desviacion de formato).
  R1  frontmatter con dg-publish + tags                    W
  R2  H1 con emoji                                         W
  R3  seccion 'Introduccion' obligatoria (clase)            W
      + emoji en todo H2                                    W
  R4  TODO el contenido dentro de callouts                 H
  R5  callout con titulo                                   H
  R6  linea en blanco '>' tras el header (excepcion 📖)    W
  R7  separador '>' en blanco ante embeds/tablas/parrafos  W
  R8  el prefijo '> >' solo cuelga de un callout anidado    H
  R9  ejemplos con etiqueta en negrita                     W
  R10 metas de aprendizaje con checkboxes '- [ ]'          W
  R11 flashcards con guion '- ' en la seccion SR           W
  R12 embeds que resuelven: ruta local, ruta a materia     H
      + SVG con fuente .mmd al lado                        W
  R13 '**Tags:**' al final                                 W
  R14 todo lo visual se explica, no se transcribe             W
  R15 vocabulario en tablas dentro de callouts             W
  R16 examenes enlazados con alias (no embebidos)          H

Uso:
  py -3.12 qa_formato_ingles1.py [--solo "1er Semestre/Ingles I (B1-B2)"] [-o reporte.txt]
  py -3.12 qa_formato_ingles1.py --calibrar   (audita la nota de referencia de SBD)
"""

import argparse
import io
import os
import re
import sys
import unicodedata

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# Heredamos el nucleo de Algebra (que hereda de SBD)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qa_formato_algebra import (  # noqa: E402
    SKIP_DIRS, RE_H, RE_EMOJI, RE_CALL_HDR, RE_CALL_CONT, RE_EMBED,
    RE_LISTITEM, RE_TABLE, RE_TABLE_SEP, RE_TAGS_FOOT, AJENO,
    existe, indice_basenames, resolver_asset, perfil_nota,
    clasifica, bloques_callout, auditar as auditar_base,
    raiz_por_defecto,
)

RE_H1 = re.compile(r"^(#{1})\s+(.*)$")


def auditar(nota_path, raiz, hallazgos, basenames_idx=None, vault=None):
    """Audita una nota: nucleo base + R15 (tablas de vocabulario) + R16 (examenes)."""
    # Nucleo heredado (R1..R14)
    auditar_base(nota_path, raiz, hallazgos, basenames_idx=basenames_idx, vault=vault)

    rel = os.path.relpath(nota_path, raiz)
    try:
        texto = io.open(nota_path, encoding="utf-8").read().replace("\ufeff", "")
    except Exception:
        return
    lineas = texto.split("\n")
    bloques = bloques_callout(lineas)

    # ---------- R15: tablas de vocabulario dentro de callouts
    # Cualquier tabla markdown (| ... |) debe estar dentro de un callout
    # (depth >= 1). Las tablas top-level se reportan como W.
    en_callout = set()
    for b in bloques:
        for i in range(b["inicio"], b["fin"] + 1):
            en_callout.add(i)
    for i, ln in enumerate(lineas):
        if not RE_TABLE.match(ln.strip()):
            continue
        if i in en_callout:
            continue
        # tabla fuera de callout
        hallazgos.append((rel, i + 1, "R15-tabla-fuera", ln.strip()[:60]))

    # ---------- R16: examenes enlazados, no embebidos
    for i, ln in enumerate(lineas):
        for m in RE_EMBED.finditer(ln):
            tgt = m.group(1).split("|")[0].split("#")[0].strip()
            low = tgt.lower()
            if low.endswith((".pdf", ".pptx", ".doc", ".docx", ".ppt", ".xlsx")):
                hallazgos.append((rel, i + 1, "R16-examen-embebido", tgt[:60]))


def main():
    ap = argparse.ArgumentParser(description="Audit el contrato FORMATO-INGLES1")
    ap.add_argument("root", nargs="?", default=None)
    ap.add_argument("--solo", default=None)
    ap.add_argument("-o", "--salida", default=None)
    ap.add_argument("--estricto", action="store_true")
    ap.add_argument("--fix-rutas", action="store_true")
    ap.add_argument("--calibrar", action="store_true")
    args = ap.parse_args()

    vault = raiz_por_defecto()
    if args.calibrar:
        # La referencia del contrato es la de SBD (la misma que Algebra y Calculo 1).
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
        raiz = os.path.join(vault, "1er Semestre", "Ingles I (B1-B2)")
        specific = None

    idx = indice_basenames(vault)

    hallazgos = []
    notas = 0
    for dp, ds, fs in os.walk(raiz):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in sorted(fs):
            if not f.endswith(".md"):
                continue
            if f == "FORMATO-INGLES1.md":
                continue
            if specific and f != specific:
                continue
            p = os.path.join(dp, f)
            notas += 1
            auditar(p, raiz, hallazgos, basenames_idx=idx, vault=vault)

    # Codigos duros (H): los del nucleo base + los propios
    CODIGOS_H = {
        "FAIL-READ",
        "R5-sin-titulo", "R6-callout-vacio",
        "R8-doble-gt-sin-callout",
        "R12-embed-rota", "R12-ajeno", "R12-ruta-profundidad",
        "R12-svg-sin-mmd",
        "R16-examen-embebido",
    }

    conteo = {}
    por_nota = {}
    for reln, lin, cod, txt in hallazgos:
        conteo[cod] = conteo.get(cod, 0) + 1
        por_nota.setdefault(reln, []).append((lin, cod, txt))

    orden = sorted(conteo.items(), key=lambda kv: (-kv[1], kv[0]))
    print("raiz=%s  notas=%d" % (os.path.relpath(raiz, vault), notas))
    print("hallazgos=%d" % sum(conteo.values()))
    for cod, n in orden:
        print("  %-26s %4d  %s" % (cod, n, "H" if cod in CODIGOS_H else "W"))

    filas = ["qa_formato_ingles1 - %s - %d notas" % (os.path.relpath(raiz, vault), notas), ""]
    for cod, n in orden:
        filas.append("%s=%d%s" % (cod, n, " (H)" if cod in CODIGOS_H else ""))
    filas.append("")
    for reln in sorted(por_nota):
        filas.append("=== %s (%d)" % (reln, len(por_nota[reln])))
        for lin, cod, txt in por_nota[reln]:
            filas.append("  %5d  %-24s %s" % (lin, cod, txt[:110]))
    if args.salida:
        io.open(args.salida, "w", encoding="utf-8", newline="\n").write("\n".join(filas) + "\n")
        print("reporte: %s" % args.salida)

    duros = [c for _, _, c, _ in hallazgos if c in CODIGOS_H]
    if duros or (args.estricto and hallazgos):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())