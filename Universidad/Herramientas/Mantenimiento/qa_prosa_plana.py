import argparse, re, os, sys

# Error 7 (complemento): PROSA EXPLICATIVA suelta fuera de callouts.
#
# El vault tiene una convencion del dueno: "nada de texto plano fuera de
# callouts". `detect_fuera_callouts.py` mide los bloques de contenido pesado
# (tablas, formulas, listas de datos). Este script mide lo que ese detector
# NO ve: las lineas de prosa (parrafos) que quedaron sueltas entre
# encabezados y callouts.
#
# No toca nada: reporta. Aplicar un callout exige elegir tipo + titulo, que
# es decision humana.
#
# Exclusiones (deliberadas, con motivo):
#   - `Herramientas/` y `Reportes/` : documentacion de las propias herramientas.
#   - frontmatter YAML             : metadatos, no prosa.
#   - code fences                  : codigo, no prosa.
#   - lineas citadas (`>`)         : ya estan dentro de un callout.
#   - encabezados / reglas / HR    : estructura, no prosa.
#   - wikilink / embed solo        : navegacion, no prosa.
#   - `-> [[...]]`                 : navegacion entre notas, no prosa.
#   - lineas de tags (`#hashtag`)  : indice de tags, no prosa.
#   - `Q::A` + `<!--SR:...-->`     : flashcards del plugin SR (formato plano
#                                    obligatorio: no se pueden citar).
#   - bloques `$$...$$`            : matematica, no prosa.
#   - continuaciones de lista      : son parte del item anterior, no prosa
#                                    suelta (la lista entera la mide
#                                    detect_fuera_callouts.py).
#
# Uso:
#   py qa_prosa_plana.py "<carpeta>" [-o reporte.txt]
#
# Salida: "prosa-real=N  (sr=K latex-codigo=L navegacion=M)".

ap = argparse.ArgumentParser()
ap.add_argument("root")
ap.add_argument("-o", default=None)
args = ap.parse_args()

RE_SR = re.compile(r"<!--\s*SR:")
RE_SR_QA = re.compile(r"^\s*[^:#\n]{1,200}::[^:\n]*")
RE_TAGLINE = re.compile(r"^\s*(?:[*_]+\s*)*tags?\s*:?\s*(?:[*_]+\s*)*$", re.I)
RE_TAG_START = re.compile(r"^\s*(?:[*_]+\s*)*tags?\s*:", re.I)
RE_META = re.compile(r"^\s*(?:[*_]+\s*)*(?:[uú]ltima actualizaci[oó]n|actualizado|updated)\b", re.I)
RE_TAG_HASH = re.compile(r"^\s*(?:_+\s*)?#[\w\-/#.]+")
# linea que es solo una lista de hashtags, con o sin backticks/cursiva
RE_SOLO_TAGS = re.compile(r"^\s*(?:_+\s*)?(?:`#[\w\-/#.]+`\s*)+$")
RE_NAV = re.compile(r"^\s*(?:[-*+]\s*)?(?:→|->|=>)\s*\[\[")
RE_LINK_SOLO = re.compile(r"^\s*(?:!\[\[|\[\[)")
RE_HEAD = re.compile(r"^\s*#{1,6}\s")
RE_RULE = re.compile(r"^\s*(?:---+|\*\*\*+|___+)\s*$")
RE_FENCE = re.compile(r"^\s*(?:>\s*)?```")
RE_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
RE_DOLLAR = re.compile(r"\$\$")
RE_LATEX_CMD = re.compile(r"\\(?:begin|end|frac|sum|int|lim|sqrt|vec|bar|hat|left|right|text|mathbb|mathcal|boxed|partial|nabla|cdot|times|quad|qquad|infty|sigma|delta|mu|omega|alpha|beta|gamma|theta|phi|psi|lambda|pi)\b")
RE_PALABRA = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{3,}")

SKIP_DIRS = (".obsidian", ".trash", ".git", "node_modules", "__pycache__")
EXCLUDE_DIRS = ("Herramientas", "Reportes")
EXCLUDE_FILES = ("Catalogo de errores del vault.md",)

filas = []
conteo = {"prosa": 0, "sr": 0, "latex-codigo": 0, "navegacion": 0}
notas = {}


def es_estructura(linea):
    s = linea.strip()
    if not s:
        return True
    if RE_HEAD.match(linea) or RE_RULE.match(linea):
        return True
    if (RE_TAGLINE.match(linea) or RE_TAG_START.match(linea)
            or RE_TAG_HASH.match(linea) or RE_SOLO_TAGS.match(linea)
            or RE_META.match(linea)):
        return True
    if s.startswith(("|", ">", "-", "*", "+")):
        return True
    if RE_ITEM.match(linea):
        return True
    return False


def clasificar(linea, en_continuacion):
    """Devuelve (categoria|None). `en_continuacion`: la linea anterior era
    un item de lista y esta es su renglon de continuacion."""
    s = linea.strip()
    if RE_SR.search(linea) or RE_SR_QA.match(linea):
        return "sr"
    if RE_NAV.match(linea):
        return "navegacion"
    if RE_LINK_SOLO.match(linea):
        return "navegacion"
    if es_estructura(linea):
        return None
    if en_continuacion:
        # continuacion de un item de lista: no es prosa suelta
        return None
    # matematica pura (pocas palabras y comandos LaTeX)
    palabras = RE_PALABRA.findall(s)
    if RE_LATEX_CMD.search(s) and len(palabras) <= 3:
        return "latex-codigo"
    if s.startswith("\\") and len(palabras) <= 3:
        return "latex-codigo"
    # fragmento matematico partido: sin ninguna palabra (p.ej. ") ", "<", "`")
    if not palabras:
        return "latex-codigo"
    return "prosa"


for dp, ds, fs in os.walk(args.root):
    ds[:] = [d for d in ds if d not in SKIP_DIRS]
    partes = os.path.relpath(dp, args.root).split(os.sep)
    if any(p in EXCLUDE_DIRS for p in partes):
        continue
    for f in sorted(fs):
        if not f.endswith(".md") or f in EXCLUDE_FILES:
            continue
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, args.root)
        lines = open(p, encoding="utf-8").read().split("\n")
        in_fm = False
        fence = False
        en_math = False
        ultimo_item = False
        for i, ln in enumerate(lines):
            s = ln.strip()
            if i == 0 and s == "---":
                in_fm = True
                continue
            if in_fm:
                if s == "---":
                    in_fm = False
                continue
            if RE_FENCE.match(ln):
                fence = not fence
                continue
            if fence:
                continue
            # bloque de matematica $$ ... $$ (puede ocupar varias lineas)
            if RE_DOLLAR.search(s):
                # el item de lista sigue vigente si la parte ANTES del
                # primer `$$` era un item (p.ej. `* Texto: $$ formula $$`)
                antes = s.split("$$")[0]
                if antes.strip():
                    ultimo_item = bool(RE_ITEM.match(antes))
                else:
                    ultimo_item = bool(RE_ITEM.match(ln))
                if s.count("$$") >= 2:
                    en_math = False
                else:
                    en_math = not en_math
                continue
            if en_math:
                ultimo_item = False
                continue
            cat = clasificar(ln, ultimo_item)
            if cat:
                conteo[cat] += 1
                notas.setdefault(rel, []).append((i + 1, cat, s[:110]))
            ultimo_item = bool(RE_ITEM.match(ln))

total = sum(conteo.values())
for cat, n in conteo.items():
    filas.append("%s=%d" % (cat, n))
filas.insert(0, "lineas-clasificadas=%d  notas=%d" % (total, len(notas)))
filas.append("")
for rel in sorted(notas):
    filas.append("=== %s (%d)" % (rel, len(notas[rel])))
    for n, cat, txt in notas[rel]:
        filas.append("  %4d  %-12s %s" % (n, cat, txt))

print("prosa-real=%d  (sr=%d latex-codigo=%d navegacion=%d)  lineas-clasificadas=%d  notas=%d"
      % (conteo["prosa"], conteo["sr"], conteo["latex-codigo"],
         conteo["navegacion"], total, len(notas)))
if args.o:
    import io as _io
    _io.open(args.o, "w", encoding="utf-8", newline="\n").write("\n".join(filas))
    print("reporte: %s" % args.o)
