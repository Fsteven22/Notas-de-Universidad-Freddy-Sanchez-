#!/usr/bin/env python3
"""qa_formato_calculo1.py — auditoria del contrato FORMATO-CALCULO1.

Verifica que una nota de Calculo de una Variable siga el formato de la
materia: frontmatter con tags, H1/H2 con emoji, todo el contenido dentro de
callouts, rutas de assets canonicas y existentes, fuente .mmd al lado de cada
SVG, tags al pie y lectura propia de cada pieza visual.

El contrato escrito vive en
`Universidad/Herramientas/Mantenimiento/FORMATO-CALCULO1.md` (reglas R1..R14).

Severidades: H (error duro) y W (desviacion de formato).
  R1  frontmatter con dg-publish + tags                    W
  R2  H1 con emoji                                         W
  R3  H2 con emoji + seccion de cierre en notas de clase  W
  R4  TODO el contenido dentro de callouts                 H
  R5  callout con titulo                                   H
  R6  linea en blanco '>' tras el header                    W
  R7  separador '>' en blanco ante embeds/tablas/parrafos  W
  R10 tipo de callout valido y en minuscula                 W
  R11 wikilinks que no resuelven a ninguna nota del vault   W
  R12 embeds que resuelven; ruta canonica; .mmd al lado     H
      + material ajeno (_texto, site, etc.)                 H
  R13 '**Tags:**' al final                                 W
  R14 todo lo visual se explica, no se transcribe            W

DRY por defecto (solo reporta). --fix-rutas repara R12 cuando la ruta
canonica existe de verdad.

Uso:
  py -3.12 qa_formato_calculo1.py [--solo "1er Semestre/Cálculo de una Variable"] [-o reporte.txt]
  py -3.12 qa_formato_calculo1.py --calibrar   (audit solo la nota de referencia)
"""

import argparse
import io
import os
import re
import sys
import unicodedata
from collections import defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

SKIP_DIRS = (".obsidian", ".trash", ".git", "node_modules", "__pycache__", "_texto")

RE_H = re.compile(r"^(#{1,6})\s+(.*)$")
RE_RULE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
RE_EMOJI = re.compile(r"[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\u2190-\u21FF\u2049\u203C\u2757]")

RE_CALL_HDR = re.compile(r"^\s*(?P<gg>(?:>\s*)+)+\[!(?P<tipo>[\w\-]+)\](?P<plegado>-?)\s*(?P<titulo>.*)$")
RE_CALL_CONT = re.compile(r"^\s*(?P<gg>(?:>\s*)+)(?P<resto>.*)$")
RE_EMBED = re.compile(r"!\[\[([^\]]+)\]\]")
RE_WIKI = re.compile(r"(?<!!)\[\[([^\]]+)\]\]")
RE_LISTITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
RE_TABLE = re.compile(r"^\s*\|")
RE_TAGS_FOOT = re.compile(r"^\s*\*\*Tags:\*\*")

# material que no debe referenciarse desde el sitio
AJENO = ("_texto/", "contenido extra/", "herramientas/", "site/", "reportes/", "svg-pipeline/")

# tipos de callout que el sitio reconoce (rehype-callouts.mjs)
TIPOS_OK = {
    "info", "note", "tip", "success", "example", "warning", "caution",
    "danger", "error", "bug", "quote", "brain", "todo", "question", "abstract",
}

# carpeta canonica de assets de la materia
CANON_U0 = "Unidad 0 - Guias y Ejercicios"
CANON_SUB = {"svg": "Diagramas", "png": "Figuras", "jpg": "Figuras", "jpeg": "Figuras"}

# secciones que cuentan como cierre de una nota de clase
RE_CIERRE = re.compile(r"referencias|bibliogr|notas recomendadas|conexiones|ver tambien", re.I)

# etiquetas de lectura propias (R14)
ETIQUETAS_EXPL = re.compile(
    r"\*\*(Se lee as[ií]|Por qu[eé] importa|Ejemplos?|Nota|C[uú]mo se lee|"
    r"Verificaci[oó]n|Analog[ií]a|Resumen|Para qu[eé] sirve|Qu[eé] notas|Pista)", re.I)


def existe(path_str):
    for c in (path_str, unicodedata.normalize("NFC", path_str), unicodedata.normalize("NFD", path_str)):
        try:
            if os.path.isfile(c):
                return True
        except OSError:
            pass
    return False


def raiz_por_defecto():
    aqui = os.path.dirname(os.path.abspath(__file__))          # ...\Universidad\Herramientas\Mantenimiento
    return os.path.dirname(os.path.dirname(aqui))              # ...\Universidad


def raiz_materia(vault):
    return os.path.join(vault, "1er Semestre", "Cálculo de una Variable")


def perfil_nota(nota_path, rel):
    """Perfil de la nota: 'clase', 'material' o 'indice'."""
    base = os.path.basename(nota_path).lower()
    carpeta = os.path.basename(os.path.dirname(nota_path)).lower()
    ruta = rel.replace("\\", "/").lower()
    if "material de clase" in ruta:
        return "material"
    if re.match(r"^unidad \d+\s*-", carpeta) and re.match(r"^\d+\s*-", base):
        return "clase"
    if re.match(r"^\d+\s*-", base) and "unidad" in ruta:
        return "clase"
    return "indice"


def prefijo_esperado(dir_nota, raiz_mat):
    """Prefijo relativo hacia la raiz de la materia segun la profundidad."""
    rel = os.path.relpath(dir_nota, raiz_mat)
    partes = Path_parts(rel)
    return "../" * len(partes)


def Path_parts(rel):
    return [p for p in rel.replace("\\", "/").split("/") if p not in (".", "")]


def clasifica(rest):
    s = rest.strip()
    if not s:
        return "blank"
    if "![[" in s or s.startswith("[["):
        return "embed"
    if RE_TABLE.match(s):
        return "table"
    if s.startswith("```"):
        return "fence"
    if RE_LISTITEM.match(s):
        return "listitem"
    if s.startswith("[!"):
        return "subheader"
    return "prose"


def bloques_callout(lineas):
    """Bloques de callout: cada entrada = header + lineas internas ('>' continuas)."""
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
            "plegado": m.group("plegado") == "-",
            "titulo": m.group("titulo").strip(),
            "lineas": interior,
        })
        i = j
    return bloques


def indice_notas_vault(vault):
    """basename -> [rutas] de todas las notas .md del vault (para R11)."""
    idx = defaultdict(list)
    for dp, ds, fs in os.walk(vault):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in fs:
            if f.lower().endswith(".md"):
                idx[f[:-3]].append(os.path.join(dp, f))
    return idx


def auditar(nota_path, raiz, raiz_mat, hallazgos, idx_vault):
    rel = os.path.relpath(nota_path, raiz)
    try:
        texto = io.open(nota_path, encoding="utf-8").read().replace("\ufeff", "")
    except Exception as e:
        hallazgos.append((rel, 0, "FAIL-READ", str(e)))
        return
    lineas = texto.split("\n")
    dir_nota = os.path.dirname(nota_path)
    bloques = bloques_callout(lineas)

    # ---------- R1 frontmatter
    fm_fin = None
    if lineas and lineas[0].strip() == "---":
        cierre = None
        for k in range(1, len(lineas)):
            if lineas[k].strip() == "---":
                cierre = k
                break
        if cierre is not None:
            fm_fin = cierre
        fm_texto = "\n".join(lineas[1:cierre]) if cierre else ""
        if "dg-publish" not in fm_texto:
            hallazgos.append((rel, 1, "R1-dg-publish", "frontmatter sin dg-publish"))
        if not re.search(r"^tags:", fm_texto, re.M):
            hallazgos.append((rel, 1, "R1-tags", "frontmatter sin 'tags:'"))
    else:
        hallazgos.append((rel, 1, "R1-frontmatter", "no arranca con '---'"))

    # ---------- R2 H1 con emoji
    h1 = [i for i, ln in enumerate(lineas) if RE_H.match(ln) and len(RE_H.match(ln).group(1)) == 1]
    if not h1:
        hallazgos.append((rel, 0, "R2-h1", "sin H1"))
    else:
        ln1 = lineas[h1[0]]
        if not RE_EMOJI.search(ln1):
            hallazgos.append((rel, h1[0] + 1, "R2-h1-emoji", ln1[:60]))

    # ---------- R3 H2 con emoji + cierre en notas de clase
    h2_textos = []
    h2_lineas = []
    for i, ln in enumerate(lineas):
        m = RE_H.match(ln)
        if m and len(m.group(1)) == 2:
            h2_textos.append(m.group(2))
            h2_lineas.append((i, m.group(2)))
    perfil = perfil_nota(nota_path, rel)
    if perfil == "clase":
        if not any(RE_CIERRE.search(t) for t in h2_textos):
            hallazgos.append((rel, 0, "R3-seccion-cierre",
                              "clase: falta seccion de cierre (Referencias|Notas Recomendadas|Conexiones)"))
    for i, tit in h2_lineas:
        if not RE_EMOJI.search(tit):
            hallazgos.append((rel, i + 1, "R3-h2-emoji", tit[:50]))

    # ---------- R4 todo dentro de callouts
    dentro = {}
    for b in bloques:
        for i in range(b["inicio"], b["fin"] + 1):
            dentro[i] = True
    fences = {}
    f = False
    for i, ln in enumerate(lineas):
        if ln.lstrip().startswith(">"):
            continue
        s = ln.strip()
        if s.startswith("```"):
            fences[i] = not f
            f = not f
    en_fence = False
    solo_link = re.compile(r"^\s*(?:!\[\[|\[\[).*$")
    tags_linea = re.compile(r"^\s*(?:[*_]+\s*)*(?:#[\w\-/#.]+|tags\s*:)", re.I)
    for i, ln in enumerate(lineas):
        if fm_fin is not None and i <= fm_fin:
            continue
        if i in fences:
            if fences[i] and not dentro.get(i):
                hallazgos.append((rel, i + 1, "R4-fence-top", ln.strip()[:60]))
            en_fence = fences[i]
            continue
        if en_fence or dentro.get(i):
            continue
        s = ln.strip()
        if not s or RE_RULE.match(ln) or RE_H.match(ln):
            continue
        if solo_link.match(ln):
            if s.startswith("!["):
                hallazgos.append((rel, i + 1, "R4-embed-top", s[:60]))
            continue
        if RE_TAGS_FOOT.match(ln) or tags_linea.match(ln):
            continue
        if s.startswith("|"):
            hallazgos.append((rel, i + 1, "R4-tabla-top", s[:60]))
        elif RE_LISTITEM.match(ln):
            hallazgos.append((rel, i + 1, "R4-lista-top", s[:60]))
        else:
            hallazgos.append((rel, i + 1, "R4-prosa-top", s[:60]))

    # ---------- R5 / R6 / R7 / R10 por callout
    for b in bloques:
        # R10 tipo valido
        if b["tipo"].lower() not in TIPOS_OK:
            hallazgos.append((rel, b["inicio"] + 1, "R10-tipo-invalido",
                              "tipo de callout no reconocido: %r" % b["tipo"][:20]))
        if not b["lineas"]:
            hallazgos.append((rel, b["inicio"] + 1, "R6-callout-vacio", b["tipo"]))
            continue
        titulo = b["titulo"]
        limpio = re.sub(r"[\s\U0001F000-\U0001FAFF\u2600-\u27BF\u2190-\u21FF\u2B00-\u2BFF]", "", titulo)
        if len(limpio) < 3:
            hallazgos.append((rel, b["inicio"] + 1, "R5-sin-titulo",
                              "[%s] %r" % (b["tipo"], titulo[:40])))
        # R6: linea en blanco tras el header
        d0, dep0, r0 = b["lineas"][0]
        if dep0 == b["depth"] and r0.strip() != "":
            hallazgos.append((rel, d0 + 1, "R6-sin-blanco-header", r0[:44]))
        # R7 separadores: linea '>' en blanco antes de tabla/embed
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
                hallazgos.append((rel, idx + 1, "R7-separador-antes", tipo + " " + rest[:44]))
            elif tipo == "embed" and previa is not None:
                hallazgos.append((rel, idx + 1, "R7-separador-antes", tipo + " " + rest[:44]))
            previa = tipo

    # ---------- R11 wikilinks que no resuelven en el vault
    for i, ln in enumerate(lineas):
        for m in RE_WIKI.finditer(ln):
            tgt = m.group(1).split("|")[0].split("#")[0].strip()
            if not tgt:
                continue
            if tgt.lower().startswith(("http://", "https://")):
                continue
            base = os.path.basename(tgt)
            if base.lower().endswith(".md"):
                base = base[:-3]
            if not base:
                continue
            if base in idx_vault:
                continue
            hallazgos.append((rel, i + 1, "R11-wikilink-roto", tgt[:60]))

    # ---------- R12 embeds resuelven + rutas canonicas + material ajeno
    pref = prefijo_esperado(dir_nota, raiz_mat)
    for i, ln in enumerate(lineas):
        for m in RE_EMBED.finditer(ln):
            tgt = m.group(1).split("|")[0].split("#")[0].strip()
            if not tgt:
                continue
            low = tgt.lower().replace("\\", "/")
            for bad in AJENO:
                if bad in low:
                    hallazgos.append((rel, i + 1, "R12-ajeno", tgt[:60]))
                    break
            if low.endswith((".pdf", ".pptx", ".doc", ".docx", ".ppt", ".xlsx")):
                hallazgos.append((rel, i + 1, "R12-clase-embebida", tgt[:60]))
                continue
            ext = os.path.splitext(low)[1].lstrip(".")
            sub = CANON_SUB.get(ext)
            canon_txt = ("%s/%s/" % (CANON_U0, sub)).lower() if sub else None
            # resolucion real
            abs_tgt = os.path.normpath(os.path.join(dir_nota, tgt.replace("/", os.sep)))
            resuelve = existe(abs_tgt)
            # ruta canonica esperada (prefijo según profundidad de la nota)
            esperado = None
            if sub:
                if canon_txt in low:
                    # ya nombra la carpeta canonica: puede ser solo el prefijo
                    idx = low.index(canon_txt) + len(canon_txt)
                    esperado = "%s%s/%s/%s" % (pref, CANON_U0, sub, low[idx:])
                else:
                    esperado = "%s%s/%s/%s" % (pref, CANON_U0, sub, os.path.basename(low))
            if not resuelve:
                if esperado and existe(os.path.normpath(os.path.join(dir_nota, esperado.replace("/", os.sep)))):
                    hallazgos.append((rel, i + 1, "R12-ruta-no-canonica",
                                      "'%s' -> use '%s'" % (tgt[:40], esperado[:56])))
                    continue
                hallazgos.append((rel, i + 1, "R12-embed-rota", tgt[:60]))
                continue
            # el archivo existe: tiene que estar en la carpeta canonica
            if sub and canon_txt not in low:
                hallazgos.append((rel, i + 1, "R12-diagrama-fuera",
                                  "%s fuera de %s/%s/: %s" % (ext.upper(), CANON_U0, sub, tgt[:46])))
                continue
            if ext == "svg":
                mmd = os.path.splitext(abs_tgt)[0] + ".mmd"
                if not os.path.isfile(mmd):
                    hallazgos.append((rel, i + 1, "R12-svg-sin-mmd",
                                      "%s sin .mmd fuente" % os.path.basename(abs_tgt)))

    # ---------- R13 tags al pie
    if not any(RE_TAGS_FOOT.match(x) for x in lineas):
        hallazgos.append((rel, len(lineas), "R13-tags-final", "falta '**Tags:** ...'"))

    # ---------- R14 todo lo visual se explica (no se transcribe)
    def ventana_expl(i, n):
        out = []
        for k in range(i + 1, min(n, i + 8)):
            s = lineas[k].strip()
            if not s:
                continue
            if not s.startswith(">"):
                break
            out.append(s)
        return out

    for i, ln in enumerate(lineas):
        bajo = ln.lower()
        if not any(e in bajo for e in (".png", ".jpg", ".jpeg", ".svg")):
            continue
        if "![" not in ln:
            continue
        ventana = ventana_expl(i, len(lineas))
        if not ventana:
            hallazgos.append((rel, i + 1, "R14-embed-sin-explicacion",
                              "embed visual sin lectura: %s" % ln.strip()[:50]))
            continue
        tiene_etiqueta = any(ETIQUETAS_EXPL.search(x) for x in ventana)
        tiene_prosa = any(
            "![[" not in x and len(re.sub(r"^>\s*", "", x)) >= 60 for x in ventana)
        if not (tiene_etiqueta or tiene_prosa):
            hallazgos.append((rel, i + 1, "R14-embed-sin-explicacion",
                              "embed visual sin lectura propia: %s" % ln.strip()[:50]))


def fix_rutas_texto(texto, dir_nota, raiz_mat):
    """Reescribe embeds a la ruta canonica (prefijo segun profundidad).

    Opera sobre TEXTO (no sobre el archivo) para que el transformador pueda
    encadenar fases sin que una reescriba el archivo desde disco y pise lo
    anterior.
    """
    pref = prefijo_esperado(dir_nota, raiz_mat)
    cambios = []

    def repl(m):
        tgt = m.group(1).split("|")[0].split("#")[0].strip()
        ext = os.path.splitext(tgt.lower())[1].lstrip(".")
        sub = CANON_SUB.get(ext)
        if not sub:
            return m.group(0)
        norm = tgt.replace("\\", "/")
        if ("%s/%s/" % (CANON_U0, sub)) in norm:
            # ya esta en la carpeta canonica: solo ajustar el prefijo
            idx = norm.lower().index(("%s/%s/" % (CANON_U0, sub)).lower())
            nombre = norm[idx + len("%s/%s/" % (CANON_U0, sub)):]
            nuevo = "%s%s/%s/%s" % (pref, CANON_U0, sub, nombre)
        else:
            nombre = os.path.basename(norm)
            nuevo = "%s%s/%s/%s" % (pref, CANON_U0, sub, nombre)
        if existe(os.path.join(dir_nota, nuevo.replace("/", os.sep))) and \
           not existe(os.path.join(dir_nota, tgt.replace("/", os.sep))):
            cambios.append((tgt, nuevo))
            return m.group(0).replace(tgt, nuevo, 1)
        return m.group(0)

    nuevo_texto = RE_EMBED.sub(repl, texto)
    return nuevo_texto, cambios


def fix_rutas(nota_path, raiz_mat):
    texto = io.open(nota_path, encoding="utf-8").read()
    dir_nota = os.path.dirname(nota_path)
    return fix_rutas_texto(texto, dir_nota, raiz_mat)


CODIGOS_H = {
    "FAIL-READ", "R4-prosa-top", "R4-tabla-top", "R4-lista-top",
    "R4-fence-top", "R4-embed-top", "R5-sin-titulo", "R6-callout-vacio",
    "R12-embed-rota", "R12-ajeno", "R12-clase-embebida",
}


def main():
    ap = argparse.ArgumentParser(description="Audit el contrato FORMATO-CALCULO1")
    ap.add_argument("root", nargs="?", default=None)
    ap.add_argument("--solo", default=None)
    ap.add_argument("-o", "--salida", default=None)
    ap.add_argument("--estricto", action="store_true")
    ap.add_argument("--fix-rutas", action="store_true")
    ap.add_argument("--calibrar", action="store_true")
    args = ap.parse_args()

    vault = raiz_por_defecto()
    raiz_mat = raiz_materia(vault)
    if args.calibrar:
        raiz = os.path.join(raiz_mat, "Unidad 3 - Aplicaciones de Límites")
        specific = "01 - Continuidad y Límites.md"
    elif args.solo:
        raiz = args.solo if os.path.isabs(args.solo) else os.path.join(vault, args.solo)
        specific = None
    elif args.root:
        raiz = args.root
        specific = None
    else:
        raiz = raiz_mat
        specific = None

    idx_vault = indice_notas_vault(vault)
    hallazgos = []
    fijados = []
    notas = 0
    for dp, ds, fs in os.walk(raiz):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in sorted(fs):
            if not f.endswith(".md") or f in ("FORMATO-CALCULO1.md",):
                continue
            if specific and f != specific:
                continue
            p = os.path.join(dp, f)
            notas += 1
            if args.fix_rutas:
                nuevo, cambios = fix_rutas(p, raiz_mat)
                if cambios:
                    io.open(p, "w", encoding="utf-8", newline="\n").write(nuevo)
                    for a, b in cambios:
                        fijados.append((os.path.relpath(p, raiz), a, b))
            auditar(p, raiz, raiz_mat, hallazgos, idx_vault)

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
