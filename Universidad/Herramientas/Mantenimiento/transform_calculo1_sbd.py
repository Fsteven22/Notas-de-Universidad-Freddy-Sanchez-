"""transform_calculo1_sbd.py — transformador de las notas de Cálculo de una Variable.

Importa la CLASIFICACIÓN del validador (`qa_formato_calculo1`, que a su vez
importa `qa_formato_sbd`): el transformador y el validador no pueden
divergir. No reimplementa `clasifica` ni `bloques_callout`.

Fases (en este orden, el manual lo llama "no negociable"):

  R6/R7  -> `normalizar`   : linea en blanco tras el header del callout y
                                antes de embeds/tablas; sin espacios al final
           `separadores`   : `---` entre secciones H2
           `chequeo`       : informe de lo que falta para cerrar el contrato

El resto (esqueleto de 8 secciones, soluciones R8, figuras R15, metas R17,
flashcards R16) es trabajo de redaccion y lo hace quien reescribe la nota:
esta herramienta no inventa contenido.

Uso:
  py -X utf8 transform_calculo1_sbd.py normalizar  "<nota.md>" [<nota.md> ...]
  py -X utf8 transform_calculo1_sbd.py separadores "<nota.md>" [...]
  py -X utf8 transform_calculo1_sbd.py chequeo     "<nota.md>" [...]
  py -X utf8 transform_calculo1_sbd.py backup      "<carpeta>" "<destino>"
"""

import io
import os
import re
import shutil
import sys
from collections import defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
if AQUI not in sys.path:
    sys.path.insert(0, AQUI)

import qa_formato_calculo1 as QA  # noqa: E402

# --- clasificacion heredada del validador (NO se reimplementa) -----------
clasifica = QA.SBD.clasifica
bloques_callout = QA.SBD.bloques_callout
RE_H = QA.RE_H
RE_RULE = QA.RE_RULE

SECCIONES = QA.SECCIONES


def _es_h2(linea):
    m = RE_H.match(linea)
    return bool(m) and len(m.group(1)) == 2


def normalizar(texto):
    """R6 + R7 + fin de linea sin espacios."""
    lineas = [l.rstrip() for l in texto.split("\n")]
    bloques = bloques_callout(lineas)
    inserts = defaultdict(list)

    # R6: linea '>' en blanco tras el header del callout
    for b in bloques:
        if not b["lineas"]:
            continue
        i0, d0, r0 = b["lineas"][0]
        if d0 == b["depth"] and r0.strip() != "" and "\U0001F4D6" not in b["titulo"]:
            inserts[b["inicio"] + 1].append(">" * b["depth"])

    # R7: linea '>' en blanco antes de un embed o del inicio de una tabla
    for b in bloques:
        if b["depth"] != 1:
            continue
        previa = None
        for idx, depth, rest in b["lineas"]:
            if depth != b["depth"]:
                previa = None
                continue
            tipo = clasifica(rest)
            if tipo == "blank":
                previa = None
                continue
            if tipo == "table" and previa not in (None, "table"):
                inserts[idx].append(">")
            elif tipo == "embed" and previa is not None:
                inserts[idx].append(">")
            previa = tipo

    out = []
    for i, l in enumerate(lineas):
        out.extend(inserts.get(i, []))
        out.append(l)
    return "\n".join(out)


def separadores(texto):
    """`---` entre secciones H2 (la primera H2 no lleva separador)."""
    lineas = texto.split("\n")
    out = []
    primera = True
    for l in lineas:
        if _es_h2(l):
            if not primera:
                while out and out[-1].strip() == "":
                    out.pop()
                if not (out and RE_RULE.match(out[-1])):
                    out.append("---")
                out.append("")
            primera = False
        out.append(l)
    return "\n".join(out)


def chequeo(nota_path):
    """Informe de lo que falta para cerrar el contrato en esa nota."""
    texto = io.open(nota_path, encoding="utf-8").read()
    lineas = texto.split("\n")
    bloques = bloques_callout(lineas)
    secs = QA.secciones_h2(lineas)
    perfil = QA.perfil_nota_c1(nota_path)
    rel = os.path.basename(nota_path)

    faltan = [s for s in SECCIONES
              if not any(s in x["titulo"] for x in secs)]
    print("%s [%s]" % (rel, perfil))
    if faltan:
        print("   faltan secciones: %s" % ", ".join(faltan))
    else:
        print("   secciones: las 8 presentes")

    # orden
    pos = {}
    for k, s in enumerate(secs):
        for nombre in SECCIONES:
            if nombre in s["titulo"] and nombre not in pos:
                pos[nombre] = k
    orden = [pos[n] for n in SECCIONES if n in pos]
    if orden != sorted(orden):
        print("   AVISO: las secciones no estan en orden canonico")

    # definiciones sin figura
    sinfig = [b["titulo"] for b in bloques
              if QA.RE_DEF.search(b["titulo"] or "")
              and not any("![[" in r and re.search(r"\.(svg|png|jpe?g)\b", r, re.I)
                          for _, d, r in b["lineas"])]
    if sinfig:
        print("   definiciones sin figura (R15): %d" % len(sinfig))
        for t in sinfig:
            print("      - %s" % t[:70])

    # ejemplos de ejercicios sin solucion
    sec_ej = next((s for s in secs if "Ejercicios Propuestos" in s["titulo"]), None)
    if sec_ej is None:
        print("   no hay seccion 'Ejercicios Propuestos'")
    else:
        n = 0
        for b in bloques:
            if not (sec_ej["ini"] <= b["inicio"] < sec_ej["fin"]):
                continue
            if b["tipo"].lower() != "example" or b["depth"] != 1:
                continue
            n += 1
            if not any(d == b["depth"] + 1 and QA.RE_SOLUCION.match(r.strip())
                       for _, d, r in b["lineas"]):
                print("      - ejercicio sin solucion: %s" % b["titulo"][:70])
        print("   ejercicios propuestos: %d" % n)

    # flashcards
    u = QA.unidad_de(nota_path)
    if perfil == "clase":
        if not re.search(r"^\s*#flashcards/cal1-u%d\s*$" % u, texto, re.M):
            print("   falta #flashcards/cal1-u%d" % u)
        n = 0
        for b in bloques:
            if "\U0001F9E0" not in (b["titulo"] or ""):
                continue
            n += sum(1 for _, d, r in b["lineas"]
                     if d == b["depth"] and QA.RE_QA.search(r))
        print("   flashcards: %d" % n)

    # metas
    sec_meta = next((s for s in secs if "Metas de Aprendizaje" in s["titulo"]), None)
    if sec_meta is not None:
        n = 0
        for b in bloques:
            if not (sec_meta["ini"] <= b["inicio"] < sec_meta["fin"]):
                continue
            n += sum(1 for _, d, r in b["lineas"]
                     if d == b["depth"] and re.match(r"^\s*- \[[ x]\]", r))
        print("   metas con checkbox: %d" % n)


def backup(origen, destino):
    origen = os.path.abspath(origen)
    destino = os.path.abspath(destino)
    n = 0
    for dp, ds, fs in os.walk(origen):
        ds[:] = [d for d in ds if d not in QA.SKIP_DIRS]
        for f in fs:
            if not f.endswith(".md"):
                continue
            src = os.path.join(dp, f)
            rel = os.path.relpath(src, origen)
            dst = os.path.join(destino, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            n += 1
    print("backup: %d notas -> %s" % (n, destino))


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 1
    fase = sys.argv[1]
    args = sys.argv[2:]

    if fase == "backup":
        backup(args[0], args[1])
        return 0

    if fase == "chequeo":
        for a in args:
            chequeo(a)
        return 0

    fn = {"normalizar": normalizar, "separadores": separadores}.get(fase)
    if fn is None:
        print("fase desconocida: %s" % fase)
        return 1
    for a in args:
        texto = io.open(a, encoding="utf-8").read()
        nuevo = fn(texto)
        if nuevo != texto:
            io.open(a, "w", encoding="utf-8", newline="\n").write(nuevo)
            print("  %s: %s aplicado" % (os.path.basename(a), fase))
        else:
            print("  %s: sin cambios" % os.path.basename(a))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
