#!/usr/bin/env python3
"""qa_formato_calculo1.py — auditoria del contrato FORMATO-CALCULO1.

Este validador **hereda** el contrato de SBD: importa `qa_formato_sbd.py` y
ejecuta su mismo nucleo (R1..R14) sin reimplementar una sola regla. Encima
anade las reglas propias de `Universidad/1er Semestre/Cálculo de una
Variable`:

  R3-orden              las 8 secciones del perfil 'clase' en orden canonico
  R3-separador          cada H2 (salvo el primero) va tras una linea '---'
  R8-ejercicio          cada [!example] de 'Ejercicios Propuestos' trae
                        solucion anidada > > [!success]- (plegada)
  R12-prefijo           los assets de U0 se enlazan con tantos '../' como la
                        profundidad de la nota dentro de la materia
  R15                   cada callout de DEFINICION contiene su propia figura
  R16-flashcards        directiva #flashcards/cal1-uN con N de la unidad
  R17-metas             'Metas de Aprendizaje' con checkboxes '- [ ]'

Severidades: H (error duro) y W (desviacion de formato).

Uso:
  py -X utf8 qa_formato_calculo1.py
  py -X utf8 qa_formato_calculo1.py --solo "1er Semestre/Cálculo de una Variable/Unidad 2 - Límites"
  py -X utf8 qa_formato_calculo1.py --calibrar        (nota de referencia C1)
  py -X utf8 qa_formato_calculo1.py -o reporte.txt
"""

import argparse
import io
import os
import re
import sys
from collections import defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

# --- el nucleo heredado de SBD -------------------------------------------
import qa_formato_sbd as SBD  # noqa: E402

SKIP_DIRS = SBD.SKIP_DIRS
RE_H = SBD.RE_H
RE_RULE = SBD.RE_RULE
RE_EMBED = SBD.RE_EMBED
RE_CALL_HDR = SBD.RE_CALL_HDR
RE_CALL_CONT = SBD.RE_CALL_CONT
RE_QA = SBD.RE_QA
RE_LISTITEM = SBD.RE_LISTITEM

CANON_U0 = "Unidad 0 - Guias y Ejercicios"
RE_UNIDAD = re.compile(r"^unidad\s+([1-9]\d*)\s*-", re.I)
RE_DEF = re.compile(r"\bdefinici[oó]n\b", re.I)
RE_SOLUCION = re.compile(r"^\[!success\]\s*-")

SECCIONES = ("Introducción", "Definiciones Formales", "Ejercicios Propuestos",
              "Metas de Aprendizaje", "Referencias", "Repaso SR", "Conexiones",
              "Seguir estudiando")

# nota de referencia de la materia (se usa con --calibrar)
NOTA_REFERENCIA = os.path.join(
    "Unidad 2 - Límites", "I - Fundamentos del Límite",
    "01 - Concepto y Definición Formal del Límite.md")


# --- perfil de nota (C1) -------------------------------------------------
def perfil_nota_c1(nota_path, rel=None):
    """'clase' si la nota cuelga de un ancestro 'Unidad N' con N >= 1.

    En C1 las unidades estan anidadas dos niveles
    ('Unidad 4 - Derivadas/IV - Tecnicas Avanzadas/...'), asi que el perfil
    se decide buscando el ancestro 'Unidad N', NO la carpeta inmediata.
    'Unidad 0 - Guias y Ejercicios' y las notas de la raiz son 'indice'.
    """
    d = os.path.dirname(os.path.abspath(nota_path))
    for p in reversed(d.replace("\\", "/").split("/")):
        if RE_UNIDAD.match(p.strip()):
            return "clase"
    return "indice"


def unidad_de(nota_path):
    """Numero de unidad (>=1) de la nota, o 0 si no esta en una unidad."""
    d = os.path.dirname(os.path.abspath(nota_path))
    for p in reversed(d.replace("\\", "/").split("/")):
        m = RE_UNIDAD.match(p.strip())
        if m:
            return int(m.group(1))
    return 0


# el validador de SBD resuelve el perfil solo: se parchea su funcion
SBD.perfil_nota = perfil_nota_c1


def raiz_por_defecto():
    return SBD.raiz_por_defecto()


def raiz_materia(vault):
    return os.path.join(vault, "1er Semestre", "Cálculo de una Variable")


# --- utilidades ----------------------------------------------------------
def secciones_h2(lineas):
    """[(ini, titulo, fin)] de cada H2 de la nota."""
    hs = []
    for i, ln in enumerate(lineas):
        m = RE_H.match(ln)
        if m and len(m.group(1)) == 2:
            hs.append((i, m.group(2)))
    out = []
    for k, (i, t) in enumerate(hs):
        fin = hs[k + 1][0] if k + 1 < len(hs) else len(lineas)
        out.append({"ini": i, "titulo": t, "fin": fin})
    return out


def profundidad_en_materia(dir_nota, raiz_mat):
    """Cuantos niveles tiene la nota dentro de la materia (0 = raiz)."""
    rel = os.path.relpath(dir_nota, raiz_mat).replace("\\", "/")
    if rel.startswith(".."):
        return None
    return len([p for p in rel.split("/") if p not in (".", "")])


def prefijo_profundo(dir_nota, raiz_mat):
    prof = profundidad_en_materia(dir_nota, raiz_mat)
    if prof is None:
        return None
    return "../" * prof


def bloque_de_linea(bloques, idx):
    for b in bloques:
        if b["inicio"] <= idx <= b["fin"]:
            return b
    return None


def indice_archivos_vault(vault):
    """Indice de archivos del vault: ruta relativa en minusculas -> ruta real."""
    idx = {}
    for dp, ds, fs in os.walk(vault):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in fs:
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, vault).replace("\\", "/")
            idx.setdefault(rel.lower(), p)
            idx.setdefault(f.lower(), p)
    return idx


# --- reglas propias de C1 ------------------------------------------------
def auditar_c1(nota_path, raiz, raiz_mat, hallazgos, idx_vault):
    rel = os.path.relpath(nota_path, raiz)
    try:
        texto = io.open(nota_path, encoding="utf-8").read().replace("\ufeff", "")
    except Exception as e:
        hallazgos.append((rel, 0, "FAIL-READ", str(e)))
        return
    lineas = texto.split("\n")
    dir_nota = os.path.dirname(nota_path)
    bloques = SBD.bloques_callout(lineas)
    secs = secciones_h2(lineas)
    perfil = perfil_nota_c1(nota_path, rel)

    # ---------- R3: orden canonico de las 8 secciones
    if perfil == "clase":
        pos = {}
        for k, s in enumerate(secs):
            for nombre in SECCIONES:
                if nombre in s["titulo"] and nombre not in pos:
                    pos[nombre] = k
        faltan = [n for n in SECCIONES if n not in pos]
        if faltan:
            # SBD ya reporta las que faltan; aqui solo el orden de las que hay
            pass
        orden = [pos[n] for n in SECCIONES if n in pos]
        if orden != sorted(orden):
            for a, b in zip(SECCIONES, SECCIONES[1:]):
                if a in pos and b in pos and pos[a] > pos[b]:
                    hallazgos.append((rel, secs[pos[b]]["ini"] + 1, "R3-orden",
                                      "'%s' aparece despues de '%s'" % (b, a)))

    # ---------- R3: separador '---' antes de cada H2 (salvo el primero)
    for k, s in enumerate(secs):
        if k == 0:
            continue
        j = s["ini"] - 1
        while j >= 0 and not lineas[j].strip():
            j -= 1
        if j < 0 or not RE_RULE.match(lineas[j]):
            hallazgos.append((rel, s["ini"] + 1, "R3-separador",
                              "H2 sin '---' antes: %s" % s["titulo"][:40]))

    # ---------- R8: solucion anidada y plegada en los ejercicios
    sec_ej = next((s for s in secs if "Ejercicios Propuestos" in s["titulo"]), None)
    if sec_ej is not None:
        for b in bloques:
            if not (sec_ej["ini"] <= b["inicio"] < sec_ej["fin"]):
                continue
            if b["tipo"].lower() != "example":
                continue
            if b["depth"] != 1:
                continue
            sol = [r for _, d, r in b["lineas"]
                   if d == b["depth"] + 1 and RE_SOLUCION.match(r.strip())]
            if not sol:
                # puede estar plegada sin '-': se acepta [!success] normal?
                sol2 = [r for _, d, r in b["lineas"]
                        if d == b["depth"] + 1 and r.strip().startswith("[!success]")]
                if sol2:
                    hallazgos.append((rel, b["inicio"] + 1, "R8-solucion-no-plegada",
                                      "la solucion no va plegada: %s" % b["titulo"][:40]))
                else:
                    hallazgos.append((rel, b["inicio"] + 1, "R8-ejercicio-sin-solucion",
                                      "ejercicio sin solucion anidada: %s" % b["titulo"][:40]))
            else:
                # la solucion no puede ir vacia
                vacia = True
                for _, d, r in b["lineas"]:
                    if d == b["depth"] + 1 and r.strip() and not RE_SOLUCION.match(r.strip()):
                        if r.strip() != "":
                            vacia = False
                            break
                if vacia:
                    hallazgos.append((rel, b["inicio"] + 1, "R8-solucion-vacia",
                                      "solucion anidada vacia: %s" % b["titulo"][:40]))

    # ---------- R15: cada definicion lleva su figura DENTRO del callout
    for b in bloques:
        if not RE_DEF.search(b["titulo"] or ""):
            continue
        tiene = False
        for _, d, r in b["lineas"]:
            if "![[" in r and re.search(r"\.(svg|png|jpe?g)\b", r, re.I):
                tiene = True
                break
        if not tiene:
            hallazgos.append((rel, b["inicio"] + 1, "R15-definicion-sin-figura",
                              "definicion sin figura dentro: %s" % (b["titulo"] or "")[:44]))

    # ---------- R16: flashcards cal1-uN
    if perfil == "clase":
        u = unidad_de(nota_path)
        directivas = []
        for i, ln in enumerate(lineas):
            m = re.match(r"^\s*#flashcards/([\w\-]+)\s*$", ln)
            if m:
                directivas.append((i, m.group(1)))
        if not directivas:
            hallazgos.append((rel, 0, "R16-flashcards-faltante",
                              "sin directiva #flashcards/cal1-u%d" % u))
        else:
            sec_sr = next((s for s in secs if "Repaso SR" in s["titulo"]), None)
            for i, nombre in directivas:
                if nombre != "cal1-u%d" % u:
                    hallazgos.append((rel, i + 1, "R16-flashcards-unidad",
                                      "'%s' no corresponde a la unidad %d" % (nombre, u)))
                if sec_sr is not None and not (sec_sr["ini"] <= i < sec_sr["fin"]):
                    hallazgos.append((rel, i + 1, "R16-flashcards-seccion",
                                      "la directiva esta fuera de 'Repaso SR'"))
            # al menos 3 tarjetas
            n = 0
            for b in bloques:
                if "\U0001F9E0" not in (b["titulo"] or ""):
                    continue
                for _, d, r in b["lineas"]:
                    if d == b["depth"] and RE_QA.search(r):
                        n += 1
            if n < 3:
                hallazgos.append((rel, 0, "R16-flashcards-pocas",
                                  "solo %d tarjetas 'Q::A' (minimo 3)" % n))

    # ---------- R17: metas de aprendizaje con checkboxes
    sec_meta = next((s for s in secs if "Metas de Aprendizaje" in s["titulo"]), None)
    if perfil == "clase":
        if sec_meta is None:
            pass  # SBD ya lo reporta como seccion faltante
        else:
            n = 0
            for b in bloques:
                if not (sec_meta["ini"] <= b["inicio"] < sec_meta["fin"]):
                    continue
                for _, d, r in b["lineas"]:
                    if d == b["depth"] and re.match(r"^\s*- \[[ x]\]", r):
                        n += 1
            if n < 3:
                hallazgos.append((rel, sec_meta["ini"] + 1, "R17-metas-pocas",
                                  "solo %d metas con checkbox (minimo 3)" % n))

    # ---------- R12: prefijo relativo segun profundidad
    pref = prefijo_profundo(dir_nota, raiz_mat)
    if pref is not None:
        for i, ln in enumerate(lineas):
            for m in RE_EMBED.finditer(ln):
                tgt = m.group(1).split("|")[0].split("#")[0].strip().replace("\\", "/")
                if CANON_U0.lower() not in tgt.lower():
                    continue
                n_up = len(re.match(r"^(?:\.\./)*", tgt).group(0))
                if n_up != len(pref):
                    hallazgos.append((rel, i + 1, "R12-prefijo",
                                      "'%s' deberia usar %s" % (tgt[:50], pref or "")))

    # ---------- R11: wikilinks que no resuelven en el vault
    for i, ln in enumerate(lineas):
        for m in re.finditer(r"(?<!!)\[\[([^\]]+)\]\]", ln):
            tgt = m.group(1).split("|")[0].split("#")[0].strip().replace("\\", "/")
            if not tgt or tgt.lower().startswith(("http://", "https://")):
                continue
            base = os.path.basename(tgt)
            if not base:
                continue
            if base.lower() in idx_vault or tgt.lower() in idx_vault:
                continue
            if (base.lower() + ".md") in idx_vault:
                continue
            cand = os.path.normpath(os.path.join(dir_nota, tgt.replace("/", os.sep)))
            if os.path.isfile(cand):
                continue
            hallazgos.append((rel, i + 1, "R11-wikilink-roto", tgt[:60]))


def fix_rutas(nota_path, raiz_mat):
    """Normaliza el prefijo relativo de los embeds de U0."""
    texto = io.open(nota_path, encoding="utf-8").read()
    dir_nota = os.path.dirname(nota_path)
    pref = prefijo_profundo(dir_nota, raiz_mat)
    if pref is None:
        return texto, []
    cambios = []

    def repl(m):
        tgt = m.group(1).split("|")[0].split("#")[0].strip().replace("\\", "/")
        if CANON_U0.lower() not in tgt.lower():
            return m.group(0)
        i = tgt.lower().index(CANON_U0.lower())
        resto = tgt[i:]
        nuevo = pref + resto
        if nuevo != tgt and existe(os.path.join(dir_nota, nuevo.replace("/", os.sep))) \
                and not existe(os.path.join(dir_nota, tgt.replace("/", os.sep))):
            cambios.append((tgt, nuevo))
            return m.group(0).replace(tgt, nuevo, 1)
        return m.group(0)

    return RE_EMBED.sub(repl, texto), cambios


def existe(path_str):
    return SBD.existe(path_str)


CODIGOS_H = set(SBD.CODIGOS_H) | {
    "R8-ejercicio-sin-solucion",
    "R11-wikilink-roto",
    "R15-definicion-sin-figura",
    "R16-flashcards-unidad",
    "R17-metas-pocas",
}


def main():
    ap = argparse.ArgumentParser(description="Audit el contrato FORMATO-CALCULO1")
    ap.add_argument("root", nargs="?", default=None)
    ap.add_argument("--solo", default=None)
    ap.add_argument("--nota", default=None,
                    help="audita una sola nota (ruta relativa al vault o absoluta)")
    ap.add_argument("-o", "--salida", default=None)
    ap.add_argument("--estricto", action="store_true")
    ap.add_argument("--fix-rutas", action="store_true")
    ap.add_argument("--calibrar", action="store_true")
    args = ap.parse_args()

    vault = raiz_por_defecto()
    raiz_mat = raiz_materia(vault)
    specific = None
    solo_notas = None
    if args.nota:
        p = args.nota if os.path.isabs(args.nota) else os.path.join(vault, args.nota)
        if not os.path.isfile(p):
            print("no existe la nota: %s" % p)
            return 2
        raiz = os.path.dirname(p)
        solo_notas = [os.path.basename(p)]
    elif args.calibrar:
        raiz = raiz_mat
        specific = NOTA_REFERENCIA
    elif args.solo:
        raiz = args.solo if os.path.isabs(args.solo) else os.path.join(vault, args.solo)
    elif args.root:
        raiz = args.root
    else:
        raiz = raiz_mat

    idx_vault = indice_archivos_vault(vault)
    hallazgos = []
    fijados = []
    notas = 0
    for dp, ds, fs in os.walk(raiz):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in sorted(fs):
            if not f.endswith(".md") or f == "FORMATO-CALCULO1.md":
                continue
            if specific and f != specific:
                continue
            if solo_notas and f not in solo_notas:
                continue
            p = os.path.join(dp, f)
            notas += 1
            if args.fix_rutas:
                nuevo, cambios = fix_rutas(p, raiz_mat)
                if cambios:
                    io.open(p, "w", encoding="utf-8", newline="\n").write(nuevo)
                    for a, b in cambios:
                        fijados.append((os.path.relpath(p, raiz), a, b))
            SBD.auditar(p, raiz, hallazgos)
            auditar_c1(p, raiz, raiz_mat, hallazgos, idx_vault)

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
    if fijados:
        print("--fix-rutas aplico %d:" % len(fijados))
        for reln, a, b in fijados:
            print("  %s :: %s -> %s" % (reln, a[:40], b[:56]))

    filas = ["qa_formato_calculo1 — %s — %d notas" % (os.path.relpath(raiz, vault), notas), ""]
    for cod, n in orden:
        filas.append("%s=%d%s" % (cod, n, " (H)" if cod in CODIGOS_H else ""))
    filas.append("")
    for reln in sorted(por_nota):
        filas.append("=== %s (%d)" % (reln, len(por_nota[reln])))
        for lin, cod, txt in por_nota[reln]:
            filas.append("  %5d  %-26s %s" % (lin, cod, txt[:110]))
    if args.salida:
        io.open(args.salida, "w", encoding="utf-8", newline="\n").write("\n".join(filas) + "\n")
        print("reporte: %s" % args.salida)

    duros = [c for _, _, c, _ in hallazgos if c in CODIGOS_H]
    if duros or (args.estricto and hallazgos):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
