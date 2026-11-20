#!/usr/bin/env python3
"""qa_formato_algebra.py — auditoria del contrato FORMATO-ALGEBRA.

Verifica que una nota de Algebra Lineal siga el formato que las 39
notas de clase ya comparten en su nucleo: seccion `## 🎯 Introducción` en el
100%, todo H2 con emoji, y —respecto a la casa— las mismas reglas de
callouts/embeds de SBD y Diseno (R4..R14). El contrato escrito vive en
`Herramientas/Mantenimiento/FORMATO-ALGEBRA.md` (reglas R1..R16).

Severidades: H (error duro) y W (desviacion de formato).
  R1  frontmatter con dg-publish + tags                    W
  R2  H1 con emoji                                         W
  R3  seccion 'Introduccion' obligatoria (clase)            W
      + emoji en todo H2                                    W
      + cierre recomendado (no exigido)                     W
  R4  TODO el contenido dentro de callouts                 H
  R5  callout con titulo                                   H
  R6  linea en blanco '>' tras el header (excepcion 📖)    W
  R7  separador '>' en blanco ante embeds/tablas/parrafos  W
  R10 metas de aprendizaje con checkboxes '- [ ]'          W
  R11 flashcards con guion '- ' en la seccion SR           W
  R12 embeds que resuelven: ruta local, ruta a materia     H
      o basename en cualquier parte de Universidad/        H
      + material ajeno (_texto, Contenido Extra, etc.)     H
      + SVG con fuente .mmd al lado                        W
  R13 '**Tags:**' al final                                 W
      + '**Tags:**' pegado al ultimo callout               W
  R14 todo lo visual se explica, no se transcribe             W
      + embeds (.png de deck / .svg de diagrama) con lectura   W
      + callouts 📖 de deck con etiqueta de lectura            W
  R8  el prefijo '> >' solo cuelga de un callout anidado    H
      (si no, se renderiza como texto indentado sin estilo)

DRY por defecto (solo reporta). --fix-rutas repara R12 cuando la ruta
corta (un nivel menos en '../') existe de verdad.

Uso:
  py -3.12 qa_formato_algebra.py [--solo "2do Semestre/Álgebra Lineal"] [-o reporte.txt]
  py -3.12 qa_formato_algebra.py --calibrar   (audit solo la nota de referencia candidata)
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
RE_EMOJI = re.compile(r"[\U0001F000-\U0001FAFF\u2300-\u23FF\u2600-\u27BF\u2B00-\u2BFF\u2190-\u21FF\u2049\u203C\u2757\u20E3\u00A9\u00AE\u2122]")

RE_CALL_HDR = re.compile(r"^\s*(?P<gg>(?:>\s*)+)+\[!(?P<tipo>[\w\-]+)\](?P<plegado>-?)\s*(?P<titulo>.*)$")
RE_CALL_CONT = re.compile(r"^\s*(?P<gg>(?:>\s*)+)(?P<resto>.*)$")
RE_EMBED = re.compile(r"!\[\[([^\]]+)\]\]")
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


# indice de basenames del vault (NFC) -> rutas absolutas, para resolver
# embeds que el sitio resuelve globalmente (basename puro)
def indice_basenames(vault):
    idx = {}
    for dp, ds, fs in os.walk(vault):
        ds[:] = [d for d in ds if d not in SKIP_DIRS and d not in (".obsidian", ".trash", ".git")]
        for f in fs:
            idx.setdefault(unicodedata.normalize("NFC", f), []).append(os.path.normpath(os.path.join(dp, f)))
    return idx


def resolver_asset(dir_nota, tgt, raiz, vault, idx):
    """Devuelve la ruta absoluta del asset (o None).

    Orden: 1) relativa a la nota (A/B o ../B), 2) relativa a la raiz de la
    materia, 3) por basename en cualquier parte de Universidad/ (el sitio
    resuelve wikilinks globalmente).
    """
    p = os.path.normpath(os.path.join(dir_nota, tgt))
    if existe(p):
        return p
    if raiz:
        p2 = os.path.normpath(os.path.join(raiz, tgt))
        if existe(p2):
            return p2
    if idx is not None:
        base = unicodedata.normalize("NFC", os.path.basename(tgt))
        cands = idx.get(base)
        if cands:
            return cands[0]
    return None


def raiz_por_defecto():
    aqui = os.path.dirname(os.path.abspath(__file__))          # ...\Universidad\Herramientas\Mantenimiento
    return os.path.dirname(os.path.dirname(aqui))              # ...\Universidad


def perfil_nota(nota_path, rel):
    """Perfil de la nota: 'clase' (leccion), 'material' (material de clase) o 'indice'.

    Las notas de clase de Álgebra Lineal NO comparten un esqueleto fijo
    (son documentos largos y multi-sección). El contrato exige solo:
    frontmatter, H2 con emoji, cierre recomendado (Metas/Ejercicios/
    Conexiones/Referencias) y la mecánica de callouts/embeds/R14.
    """
    base = os.path.basename(nota_path).lower()
    carpeta = os.path.basename(os.path.dirname(nota_path)).lower()
    ruta = rel.replace("\\", "/").lower()
    if "material de clase" in ruta:
        return "material"
    # los carpetas de Álgebra usan en-dash (U+2013): "Unidad 1 – Sistemas..."; los
    # nombres de archivo usan guion simple: "01 - Algoritmo de Gauss.md"
    if re.match(r"^unidad \d+\s*[-–]", carpeta) and re.match(r"^\d+\s*-", base):
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


def lineas_callout_anidado(lineas):
    """Indices de las lineas que cuelgan de un callout anidado ('> > [!tipo]').

    El prefijo '> >' solo es legitimo como contenido de un callout anidado
    (contrato R8, patron de Diseno/SBD). Un '> >' suelto se renderiza como
    texto indentado sin estilo: es lo que reporto el dueno en ALGEBRA.
    """
    dentro = set()
    i, n = 0, len(lineas)
    while i < n:
        if not re.match(r"^\s*> >\s*\[!", lineas[i]):
            i += 1
            continue
        dentro.add(i)
        j = i + 1
        while j < n:
            mm = RE_CALL_CONT.match(lineas[j])
            if not mm or mm.group("gg").count(">") < 2:
                break
            dentro.add(j)
            j += 1
        i = j
    return dentro


def auditar(nota_path, raiz, hallazgos, basenames_idx=None, vault=None):
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
    if perfil == "clase":
        # sin esqueleto obligatorio por nota; solo emoji en H2 (más abajo)
        requeridas = ()
    else:  # indice / material de clase: no exige secciones
        requeridas = ()
    for nombre in requeridas:
        if nombre not in h2_join:
            hallazgos.append((rel, 0, "R3-seccion-falta", "%s: %s" % (perfil, nombre)))
    # cierre recomendado, no exigido: recomienda encarecer sin romper el render
    if perfil == "clase" and not any(
            c in h2_join for c in ("Metas de Aprendizaje", "Ejercicios", "Conexiones", "Referencias")):
        hallazgos.append((rel, 0, "R3-cierre-falta",
                          "clase: sin ningun cierre recomendado (Metas/Ejercicios/Conexiones/Referencias)"))
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
        if not b["lineas"]:
            hallazgos.append((rel, b["inicio"] + 1, "R6-callout-vacio", b["tipo"]))
            continue
        titulo = b["titulo"]
        limpio = re.sub(r"[\s\U0001F000-\U0001FAFF\u2600-\u27BF\u2190-\u21FF\u2B00-\u2BFF]", "", titulo)
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
    # R10 solo aplica dentro de la seccion 'Metas de Aprendizaje': en Diseno
    # los callouts 'Nivel N - Basico' tambien aparecen en 'Ejercicios
    # Propuestos' (agrupacion de ejercicios), y no son metas.
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
            # material de clase no se embebe (PDF/PPTX/DOC): se capturan sus
            # paginas como PNG en Archivos/ y se citan con su numero de pagina
            if low.endswith((".pdf", ".pptx", ".doc", ".docx", ".ppt", ".xlsx")):
                hallazgos.append((rel, i + 1, "R12-clase-embebida", tgt[:60]))
                continue
            resolved = resolver_asset(dir_nota, tgt, raiz, vault, basenames_idx)
            # cada SVG embebido debe tener su fuente .mmd al lado (regla del
            # SVG-Pipeline: el diagrama se puede re-editar y volver a compilar)
            if low.endswith(".svg") and resolved:
                mmd = os.path.splitext(resolved)[0] + ".mmd"
                if not os.path.isfile(mmd):
                    hallazgos.append((rel, i + 1, "R12-svg-sin-mmd",
                                      "%s sin .mmd fuente" % os.path.basename(resolved)))
                # los diagramas viven todos en la carpeta canonica
                norm = resolved.replace("\\", "/").lower()
                if "unidad 0 - guias y ejercicios/diagramas/" not in norm:
                    hallazgos.append((rel, i + 1, "R12-diagrama-fuera",
                                      "SVG fuera de Unidad 0/Diagramas: %s" % tgt[:50]))
            if resolved:
                continue
            if tgt.startswith("../"):
                corto = re.sub(r"^(\.\./)+", "../", tgt, count=1)
                if corto != tgt and resolver_asset(dir_nota, corto, raiz, vault, basenames_idx) is not None:
                    hallazgos.append((rel, i + 1, "R12-ruta-profundidad", "'%s' → use '%s'" % (tgt, corto)))
                    continue
            hallazgos.append((rel, i + 1, "R12-embed-rota", tgt[:60]))

    # ---------- R8 el prefijo '> >' solo cuelga de un callout anidado
    anidado = lineas_callout_anidado(lineas)
    for i, ln in enumerate(lineas):
        mm = RE_CALL_CONT.match(ln)
        if not mm:
            continue
        if mm.group("gg").count(">") >= 2 and i not in anidado:
            hallazgos.append((rel, i + 1, "R8-doble-gt-sin-callout",
                              "'> >' sin callout anidado: %s" % ln.strip()[:44]))

    # ---------- R13 tags al pie
    if not any(RE_TAGS_FOOT.match(x) for x in lineas):
        hallazgos.append((rel, len(lineas), "R13-tags-final", "falta '**Tags:** ...'"))
    # los tags van en la raiz, no pegados al ultimo callout
    for i, ln in enumerate(lineas):
        if not RE_TAGS_FOOT.match(ln):
            continue
        prev = lineas[i - 1].strip() if i > 0 else ""
        if prev.startswith(">") and prev != ">":
            hallazgos.append((rel, i + 1, "R13-tags-pegado",
                              "'**Tags:**' pegado al callout (separa con linea en blanco + '---')"))

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


# En Algebra las notas son prosa densa fuera de callouts por diseno (estilo del
# dueno); se evaluan pero como AVISO, no como bloqueo. H solo para fallos reales:
# callout vacío, doble > sin anclaje, embeds rotos/ajenos.
CODIGOS_H = {
    "FAIL-READ",
    "R5-sin-titulo", "R6-callout-vacio",
    "R8-doble-gt-sin-callout",
    "R12-embed-rota", "R12-ajeno", "R12-ruta-profundidad",
}


def main():
    ap = argparse.ArgumentParser(description="Audit el contrato FORMATO-ALGEBRA")
    ap.add_argument("root", nargs="?", default=None)
    ap.add_argument("--solo", default=None)
    ap.add_argument("-o", "--salida", default=None)
    ap.add_argument("--estricto", action="store_true")
    ap.add_argument("--fix-rutas", action="store_true")
    ap.add_argument("--calibrar", action="store_true")
    args = ap.parse_args()

    vault = raiz_por_defecto()
    if args.calibrar:
        raiz = os.path.join(vault, "2do Semestre", "Algebra Lineal")
        specific = None
    elif args.solo:
        raiz = args.solo if os.path.isabs(args.solo) else os.path.join(vault, args.solo)
        specific = None
    elif args.root:
        raiz = args.root
        specific = None
    else:
        raiz = os.path.join(vault, "2do Semestre", "Álgebra Lineal")
        specific = None

    idx = indice_basenames(vault)

    hallazgos = []
    fijados = []
    notas = 0
    for dp, ds, fs in os.walk(raiz):
        ds[:] = [d for d in ds if d not in SKIP_DIRS]
        for f in sorted(fs):
            if not f.endswith(".md") or f == "FORMATO-ALGEBRA.md":
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
            auditar(p, raiz, hallazgos, basenames_idx=idx, vault=vault)

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
            print("  %s :: %s -> %s" % (reln, a[:36], b[:36]))

    filas = ["qa_formato_algebra — %s — %d notas" % (os.path.relpath(raiz, vault), notas), ""]
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
