# -*- coding: utf-8 -*-
"""qa_formato_fisica.py - auditoria del contrato FORMATO-FISICA.

Verifica que una nota de Fisica Mecanica siga el formato propio de la
materia (notas de clase con conceptos, definiciones, ecuaciones y
ejemplos en callouts; notas de laboratorio con contexto, procedimiento y
resultados; notas raiz sin secciones exigidas). El contrato escrito
vive en `Herramientas/Mantenimiento/FORMATO-FISICA.md` (reglas R1..R16).

Severidades: H (error duro), W (desviacion de formato) y P (pendiente de
la ronda de lecturas: R14, los embeds que aun no tienen lectura).
  R1  frontmatter con dg-publish + tags                    W
  R2  H1 con emoji                                         W
  R3  secciones H2 requeridas                              W
  R4  TODO el contenido dentro de callouts                 H
  R5  callout con titulo                                   H
  R6  linea en blanco '>' tras el header                   W
  R7  separador '>' en blanco ante embeds/tablas           W
  R10 metas (cuando existen) con checkboxes '- [ ]'         W
  R12 embeds que resuelven; material ajeno (_texto, etc.)   H
      + material de clase (PDF/PPTX) embebido: se enlaza   H
      + cada SVG tiene su .mmd al lado                     W
  R13 '**Tags:**' al final                                 W
  R14 todo lo visual se explica, no se transcribe           P
  R15 el enlace a material de clase lleva alias legible     W

DRY por defecto (solo reporta). --fix-rutas repara R12 cuando la ruta
corte (un nivel menos en '../') existe de verdad.

Uso:
  py -3.12 qa_formato_fisica.py [--solo "1er Semestre/Física Mecánica"] [-o reporte.txt]
  py -3.12 qa_formato_fisica.py --calibrar   (audit solo la nota de referencia)
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

SKIP_DIRS = (".obsidian", ".trash", ".git", "node_modules", "__pycache__")

RE_H = re.compile(r"^(#{1,6})\s+(.*)$")
RE_RULE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
# Rango de emoji: bloques Miscellaneous Symbols (2600-27BF), Dingbats (2B00-2BFF),
# Supplemental Symbols (1F000-1FAFF), flechas, y TECHNICAL (2300-23FF): este
# ultimo cubre los emoji de reloj y cronometro (⏱️ U+23F1, ⌛ U+231B, ⏳ U+23F3).
RE_EMOJI = re.compile(r"[\U0001F000-\U0001FAFF\u2300-\u23FF\u2600-\u27BF\u2B00-\u2BFF\u2190-\u21FF\u2049\u203C\u2757]")

RE_CALL_HDR = re.compile(r"^\s*(?P<gg>(?:>\s*)+)+\[!(?P<tipo>[\w\-]+)\](?P<plegado>-?)\s*(?P<titulo>.*)$")
RE_CALL_CONT = re.compile(r"^\s*(?P<gg>(?:>\s*)+)(?P<resto>.*)$")
RE_EMBED = re.compile(r"!\[\[([^\]]+)\]\]")
# enlace (no embed) a un archivo: [[ruta|alias]] o [[ruta]]
RE_LINK = re.compile(r"(?<!!)\[\[([^\]]+)\]\]")
RE_LISTITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
RE_TABLE = re.compile(r"^\s*\|")
RE_QA = re.compile(r"::")
RE_TAGS_FOOT = re.compile(r"^\s*\*\*Tags:\*\*")

# material que no debe referenciarse desde el sitio
AJENO = ("_texto/", "contenido extra/", "herramientas/", "site/", "reportes/", "svg-pipeline/")


def existe(path_str):
    # Normalizar antes de comprobar: Windows recorta las rutas de mas de
    # MAX_PATH (260) si no se colapsan los "..", de modo que un embed con
    # ruta relativa larga se marcaria como roto aunque el archivo exista.
    # Obsidian si resuelve esas rutas, asi que el QA debe hacerlo igual.
    base = os.path.normpath(path_str)
    for c in (base, unicodedata.normalize("NFC", base), unicodedata.normalize("NFD", base)):
        try:
            if os.path.isfile(c):
                return True
        except OSError:
            pass
    return False


def raiz_por_defecto():
    aqui = os.path.dirname(os.path.abspath(__file__))          # ...\Universidad\Herramientas\Mantenimiento
    return os.path.dirname(os.path.dirname(aqui))              # ...\Universidad


def perfil_nota(nota_path, rel):
    """Perfil de la nota de POO: 'clase' o 'indice'.

    · clase  — teoria: 01 - Cinematica/, 02 - Dinamica/, 03 - Trabajo y Energia/,
               04 - Impulso y Colisiones (Lineal)/, 05 - Equilibrio y Elasticidad/,
               06 - Hidrostatica e Hidrodinamica/, Fundamentos de Fisica Mecanica/
    · practica — practicas de laboratorio (Practicas De Laboratorio/).
    · indice — notas raiz: mapa, syllabus, indice de contenido, recursos.
    """
    base = os.path.basename(nota_path).lower()
    carpeta = os.path.basename(os.path.dirname(nota_path)).lower()
    if carpeta == "practicas de laboratorio":
        return "practica"
    if re.match(r"^\d+\s*-\s", carpeta) or "fundamentos de fisica" in carpeta:
        return "clase"
    return "indice"


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
    if RE_QA.search(s):
        return "qa"
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
            # un nuevo header de callout al mismo depth (o menor) cierra el
            # bloque actual: no es contenido suyo
            mh = RE_CALL_HDR.match(lineas[j])
            if mh and mh.group("gg").count(">") <= depth:
                break
            mm = RE_CALL_CONT.match(lineas[j])
            if not mm:
                break
            interior.append((j, mm.group("gg").count(">"), mm.group("resto")))
            j += 1
        bloques.append({
            "inicio": i, "fin": j - 1, "depth": m.group("gg").count(">"),
            "tipo": m.group("tipo"),
            "plegado": m.group("plegado") == "-",
            "titulo": m.group("titulo").strip(),
            "lineas": interior,
        })
        i = j
    return bloques


def auditar(nota_path, raiz, hallazgos, es_referencia=False):
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
    fm_fin = None  # indice 0-based del cierre '---' del frontmatter
    if lineas and lineas[0].strip() == "---":
        # encontrar cierre
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

    # ---------- R3 secciones requeridas (segun perfil de nota)
    h2_textos = []
    h2_lineas = []
    for i, ln in enumerate(lineas):
        m = RE_H.match(ln)
        if m and len(m.group(1)) == 2:
            h2_textos.append(m.group(2))
            h2_lineas.append((i, m.group(2)))
    h2_join = "\n".join(h2_textos)
    perfil = perfil_nota(nota_path, rel)
    # Fisica no exige nombres de seccion fijos: el esqueleto varia por unidad.
    # R3-h2-emigo (linea 222+) ya exige que TODAS las H2 lleven emoji, que es
    # lo importante para esta materia.
    requeridas = ()
    for nombre in requeridas:
        if nombre not in h2_join:
            hallazgos.append((rel, 0, "R3-seccion-falta", "%s: %s" % (perfil, nombre)))
    # cada H2 debe abrir con emoji (como la referencia)
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
            continue  # un fence de callout no toca el estado top-level
        s = ln.strip()
        if s.startswith("```"):
            fences[i] = not f
            f = not f
    en_fence = False
    solo_link = re.compile(r"^\s*(?:!\[\[|\[\[).*$")
    tags_linea = re.compile(r"^\s*(?:[*_]+\s*)*(?:#[\w\-/#.]+|tags\s*:)", re.I)
    for i, ln in enumerate(lineas):
        if fm_fin is not None and i <= fm_fin:
            continue  # frontmatter: no es prosa top-level
        if i in fences:
            # marcador de fence top-level: el de apertura fuera de callout es R4
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
        if RE_QA.search(s):  # flashcards SR del plugin
            continue
        if s.startswith("|"):
            hallazgos.append((rel, i + 1, "R4-tabla-top", s[:60]))
        elif RE_LISTITEM.match(s):
            hallazgos.append((rel, i + 1, "R4-lista-top", s[:60]))
        else:
            hallazgos.append((rel, i + 1, "R4-prosa-top", s[:60]))

    # ---------- R5 / R6 / R7 por callout
    for b in bloques:
        titulo = b["titulo"]
        limpio = re.sub(r"[\s\U0001F000-\U0001FAFF\u2600-\u27BF\u2190-\u21FF\u2B00-\u2BFF\u2300-\u23FF\U0001F4CC]", "", titulo)
        if not b["lineas"]:
            # En Física el texto de introduccion vive en el propio header del
            # callout (patron del contrato R5: '> [!tip] Definicion ...').
            # Solo es un callout VACIO si tampoco hay texto en el titulo.
            if len(limpio.strip()) < 20:
                hallazgos.append((rel, b["inicio"] + 1, "R6-callout-vacio", b["tipo"]))
            continue
        if len(limpio) < 3:
            hallazgos.append((rel, b["inicio"] + 1, "R5-sin-titulo", "[%s] %r" % (b["tipo"], titulo[:40])))
        # R6: blanca tras header, salvo los 📖
        d0, _dep0, r0 = b["lineas"][0]
        if _dep0 == b["depth"] and r0.strip() != "" and "\U0001F4D6" not in titulo:
            hallazgos.append((rel, d0 + 1, "R6-sin-blanco-header", r0[:44]))
        # R7 separadores: linea '>' en blanco antes de tabla/embed, a depth
        # del callout. Las filas consecutivas de la MISMA tabla son continuacion
        # (no inicio nuevo). Los bloques anidados (soluciones [!success]- a
        # depth>=2) van pegados en la referencia: solo se audita el depth principal.
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

    # ---------- R10/R11 metas y flashcards
    # R10 solo aplica dentro de la seccion 'Metas de Aprendizaje' cuando
    # la nota la trae; POO no la exige, pero si existe se audita.
    # las metas son una seccion H2 con sus callouts, y los callouts de
    # 'Nivel' que aparecen en otras secciones son agrupacion de ejemplos.
    rango_metas = None
    for k, (i, tit) in enumerate(h2_lineas):
        if "Metas de Aprendizaje" in tit:
            fin = h2_lineas[k + 1][0] if k + 1 < len(h2_lineas) else len(lineas)
            rango_metas = (i, fin)
            break
    for b in bloques:
        t = b["titulo"]
        en_metas = rango_metas is not None and rango_metas[0] <= b["inicio"] < rango_metas[1]
        if en_metas and re.search(r"\bNivel\b", t):
            for idx, depth, rest in b["lineas"]:
                if depth != b["depth"] or not rest.strip():
                    continue
                if not re.match(r"^\s*- \[[ x]\]", rest):
                    hallazgos.append((rel, idx + 1, "R10-metas-checkbox", rest.strip()[:44]))
                    break
        if "\U0001F9E0" in t:  # 🧠
            items_guion = False
            for idx, depth, rest in b["lineas"]:
                s = rest.strip()
                if not s:
                    continue
                if RE_QA.search(s):
                    if not re.match(r"^\s*- ", s):
                        hallazgos.append((rel, idx + 1, "R11-flashcards-guion", s[:44]))
                    else:
                        items_guion = True
            if isinstance(b["titulo"], str) and not items_guion:
                pass  # si no hay flashcards en este callout, no chilla

    # ---------- R12 embeds resuelven + material ajeno
    for i, ln in enumerate(lineas):
        for m in RE_EMBED.finditer(ln):
            tgt = m.group(1).split("|")[0].split("#")[0].strip()
            if not tgt:
                continue
            low = tgt.lower()
            for bad in AJENO:
                if bad in low:
                    hallazgos.append((rel, i + 1, "R12-ajeno", tgt[:60]))
                    break
            # material de clase no se embebe (PDF/PPTX/DOC): se ENLAZA con
            # alias y, si la nota transcribe una pagina concreta, esa pagina
            # se captura como PNG en Archivos/ y se cita por su numero
            if low.endswith((".pdf", ".pptx", ".doc", ".docx", ".ppt", ".xlsx")):
                hallazgos.append((rel, i + 1, "R12-clase-embebida", tgt[:60]))
                continue
            # cada SVG embebido debe tener su fuente .mmd al lado (regla del
            # SVG-Pipeline: el diagrama se puede re-editar y volver a compilar)
            if low.endswith(".svg"):
                abs_svg = os.path.join(dir_nota, tgt)
                if not os.path.isabs(abs_svg):
                    abs_svg = os.path.normpath(abs_svg)
                if os.path.isfile(abs_svg):
                    mmd = os.path.splitext(abs_svg)[0] + ".mmd"
                    if not os.path.isfile(mmd):
                        hallazgos.append((rel, i + 1, "R12-svg-sin-mmd",
                                          "%s sin .mmd fuente" % os.path.basename(abs_svg)))
            try:
                if existe(os.path.join(dir_nota, tgt)) or existe(os.path.join(raiz, tgt)):
                    continue
            except Exception:
                pass
            if tgt.startswith("../"):
                corto = re.sub(r"^(\.\./)+", "../", tgt, count=1)
                if corto != tgt and existe(os.path.join(dir_nota, corto)):
                    hallazgos.append((rel, i + 1, "R12-ruta-profundidad", "'%s' → use '%s'" % (tgt, corto)))
                    continue
            hallazgos.append((rel, i + 1, "R12-embed-rota", tgt[:60]))

    # ---------- R13 tags al pie
    if not any(RE_TAGS_FOOT.match(x) for x in lineas):
        hallazgos.append((rel, len(lineas), "R13-tags-final", "falta '**Tags:** ...'"))

    # ---------- R15 el enlace a material de clase lleva alias legible
    # En POO el material de clase (syllabus, guias)
    # se ENLAZA, no se embebe: '[[ruta.pdf|alias.pdf]]'. El alias es lo que
    # se ve en el sitio, asi que tiene que decir que es el archivo.
    for i, ln in enumerate(lineas):
        for m in RE_LINK.finditer(ln):
            cuerpo = m.group(1)
            if "|" not in cuerpo:
                continue
            tgt = cuerpo.split("|")[0].split("#")[0].strip()
            if not tgt.lower().endswith((".pdf", ".pptx", ".doc", ".docx",
                                         ".ppt", ".xlsx")):
                continue
            alias = cuerpo.split("|", 1)[1].strip()
            if not alias or len(alias) < 3:
                hallazgos.append((rel, i + 1, "R15-enlace-clase-sin-alias",
                                  tgt[:60]))
                continue
            # el alias debe nombrar el archivo, no repetir la ruta
            if "/" in alias or "\\" in alias:
                hallazgos.append((rel, i + 1, "R15-enlace-clase-sin-alias",
                                  "alias con ruta: %s" % alias[:40]))

    # ---------- R14 todo lo visual se explica (no se transcribe)
    # Una captura del deck o un diagrama no se documenta solo: al lado debe
    # haber una lectura (lo que significa), no solo la transcripcion.
    # Se acepta 'Se lee asi:', 'Por que importa:', 'Ejemplo(s):', 'Nota:',
    # 'Verificacion', 'Analogia', 'Resumen', 'Para que sirve', ...
    ETIQUETAS_EXPL = re.compile(
        r"\*\*(Se lee as[ií]|Por qu[eé] importa|Ejemplos?|Nota|C[uú]mo se lee|"
        r"Verificaci[oó]n|Analog[ií]a|Resumen|Para qu[eé] sirve|Qu[eé] notas|Pista)", re.I)

    def ventana_expl(i, n):
        """Lineas siguientes al embed, dentro del mismo callout."""
        out = []
        for k in range(i + 1, min(n, i + 7)):
            s = lineas[k].strip()
            if not s:
                continue
            if not s.startswith(">"):
                break            # salio del callout: no hay explicacion
            out.append(s)
        return out

    # (a) cada embed visual (.png de deck o .svg de diagrama) lleva lectura
    for i, ln in enumerate(lineas):
        bajo = ln.lower()
        if ".png" not in bajo and ".svg" not in bajo:
            continue
        if "![" not in ln:
            continue
        ventana = ventana_expl(i, len(lineas))
        if not ventana:
            hallazgos.append((rel, i + 1, "R14-embed-sin-explicacion",
                              "embed visual sin lectura: %s" % ln.strip()[:50]))
            continue
        tiene_etiqueta = any(ETIQUETAS_EXPL.search(x) for x in ventana)
        # la prosa debe ser texto real: la ruta del propio embed no cuenta
        tiene_prosa = any(
            "![[" not in x and len(re.sub(r"^>\s*", "", x)) >= 60 for x in ventana)
        if not (tiene_etiqueta or tiene_prosa):
            hallazgos.append((rel, i + 1, "R14-embed-sin-explicacion",
                              "embed visual sin lectura propia: %s" % ln.strip()[:50]))

    # (b) cada callout 📖 de deck lleva al menos una etiqueta de lectura.
    #     Excepcion: los callouts 📖 de 'Fuentes' son bibliografia.
    i = 0
    n = len(lineas)
    while i < n:
        m = RE_CALL_HDR.match(lineas[i])
        if not m:
            i += 1
            continue
        depth = m.group("gg").count(">")
        titulo = m.group("titulo")
        interior = []
        j = i + 1
        while j < n:
            mh = RE_CALL_HDR.match(lineas[j])
            if mh and mh.group("gg").count(">") <= depth:
                break
            mm = RE_CALL_CONT.match(lineas[j])
            if not mm:
                break
            interior.append(mm.group("resto"))
            j += 1
        if "\U0001F4D6" in titulo and depth == 1 and "Fuente" not in titulo:
            if not any(ETIQUETAS_EXPL.search(x) for x in interior):
                hallazgos.append((rel, i + 1, "R14-deck-sin-explicacion",
                                  "callout de deck sin lectura: %s" % titulo[:50]))
        i = j


def fix_rutas(nota_path):
    texto = io.open(nota_path, encoding="utf-8").read()
    dir_nota = os.path.dirname(nota_path)
    cambios = []

    def repl(m):
        tgt = m.group(1).split("|")[0].split("#")[0].strip()
        if not tgt.startswith("../"):
            return m.group(0)
        corto = re.sub(r"^(\.\./)+", "../", tgt, count=1)
        if corto == tgt:
            return m.group(0)
        if existe(os.path.join(dir_nota, corto)) and not existe(os.path.join(dir_nota, tgt)):
            cambios.append((tgt, corto))
            return m.group(0).replace(tgt, corto, 1)
        return m.group(0)

    nuevo = RE_EMBED.sub(repl, texto)
    return nuevo, cambios


CODIGOS_H = {
    "FAIL-READ", "R4-prosa-top", "R4-tabla-top", "R4-lista-top",
    "R4-fence-top", "R5-sin-titulo", "R6-callout-vacio",
    "R12-embed-rota", "R12-ajeno", "R12-ruta-profundidad",
    "R12-clase-embebida",
}

# Pendientes de la ronda de lecturas (R14): no son errores de formato, son
# el trabajo de escribir la lectura de cada figura. Se reportan aparte para
# que la ronda mecanica pueda cerrar en 0 H + 0 W sin perder de vista el
# backlog. Con --estricto-pendientes tambien hacen fallar la auditoria.
CODIGOS_P = {
    "R14-embed-sin-explicacion", "R14-deck-sin-explicacion",
}


def main():
    ap = argparse.ArgumentParser(description="Audit el contrato FORMATO-FISICA")
    ap.add_argument("root", nargs="?", default=None)
    ap.add_argument("--solo", default=None)
    ap.add_argument("-o", "--salida", default=None)
    ap.add_argument("--estricto", action="store_true")
    ap.add_argument("--estricto-pendientes", action="store_true")
    ap.add_argument("--fix-rutas", action="store_true")
    ap.add_argument("--calibrar", action="store_true")
    args = ap.parse_args()

    vault = raiz_por_defecto()
    CURSO_FISICA = ("1er Semestre", "Física Mecánica")
    if args.calibrar:
        raiz = os.path.join(vault, *CURSO_FISICA)
        specific = "01 - Cinemática/Cinemática Traslacional.md"
    elif args.solo:
        raiz = args.solo if os.path.isabs(args.solo) else os.path.join(vault, args.solo)
        specific = None
    elif args.root:
        raiz = args.root
        specific = None
    else:
        raiz = os.path.join(vault, *CURSO_FISICA)
        specific = None

    hallazgos = []
    fijados = []
    notas = 0
    for dp, ds, fs in os.walk(raiz):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in sorted(fs):
            if not f.endswith(".md") or f == "FORMATO-FISICA.md":
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
            auditar(p, raiz, hallazgos)

    conteo = {}
    por_nota = {}
    for reln, lin, cod, txt in hallazgos:
        conteo[cod] = conteo.get(cod, 0) + 1
        por_nota.setdefault(reln, []).append((lin, cod, txt))

    orden = sorted(conteo.items(), key=lambda kv: (-kv[1], kv[0]))
    n_h = sum(n for c, n in conteo.items() if c in CODIGOS_H)
    n_p = sum(n for c, n in conteo.items() if c in CODIGOS_P)
    n_w = sum(conteo.values()) - n_h - n_p
    print("raiz=%s  notas=%d" % (os.path.relpath(raiz, vault), notas))
    print("hallazgos=%d  (errores=%d  avisos=%d  pendientes-de-lectura=%d)"
          % (sum(conteo.values()), n_h, n_w, n_p))
    for cod, n in orden:
        sev = "H" if cod in CODIGOS_H else ("P" if cod in CODIGOS_P else "W")
        print("  %-26s %4d  %s" % (cod, n, sev))
    if fijados:
        print("--fix-rutas aplico %d:" % len(fijados))
        for reln, a, b in fijados:
            print("  %s :: %s -> %s" % (reln, a[:36], b[:36]))

    filas = ["qa_formato_fisica — %s — %d notas" % (os.path.relpath(raiz, vault), notas), ""]
    for cod, n in orden:
        sev = " (H)" if cod in CODIGOS_H else (" (P)" if cod in CODIGOS_P else "")
        filas.append("%s=%d%s" % (cod, n, sev))
    filas.append("")
    for reln in sorted(por_nota):
        filas.append("=== %s (%d)" % (reln, len(por_nota[reln])))
        for lin, cod, txt in por_nota[reln]:
            filas.append("  %5d  %-24s %s" % (lin, cod, txt[:110]))
    if args.salida:
        io.open(args.salida, "w", encoding="utf-8", newline="\n").write("\n".join(filas) + "\n")
        print("reporte: %s" % args.salida)

    duros = [c for _, _, c, _ in hallazgos if c in CODIGOS_H]
    pendientes = [c for _, _, c, _ in hallazgos if c in CODIGOS_P]
    otros = [c for _, _, c, _ in hallazgos
             if c not in CODIGOS_H and c not in CODIGOS_P]
    if duros or (args.estricto and otros) or (args.estricto_pendientes and pendientes):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
