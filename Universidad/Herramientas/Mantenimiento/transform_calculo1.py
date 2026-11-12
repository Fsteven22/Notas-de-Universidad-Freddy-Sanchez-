#!/usr/bin/env python3
"""transform_calculo1.py — aplica el contrato FORMATO-CALCULO1 a la materia.

Importa la MISMA funcion de clasificacion que el validador
(`qa_formato_calculo1.clasifica` / `.bloques_callout`): si el transformador
reimplementa la clasificacion, divergen y se rompe el render.

Orden de las transformaciones (no negociable, ver el manual de flujo):
  1. R10  tipos de callout invalidos -> validos
  2. R6   linea '>' en blanco tras el encabezado del callout
  3. R7   separador '>' antes de embeds y tablas
  4. R12  rutas de assets canonicas (prefijo segun profundidad)
  5. normalizar las lineas '>' (sin espacios finales)
  6. R4   envolver el contenido top-level en callouts
  7. normalizar las lineas '>' otra vez
  8. R1/R13  tags en el frontmatter y '**Tags:**' al pie
  9. R2/R3  emoji en H1/H2, H1 duplicados -> H2
 10. R3    seccion de cierre en las notas de clase que no la tienen

DRY por defecto (solo reporta). --apply escribe los cambios.

Uso:
  py -3.12 transform_calculo1.py            (reporte)
  py -3.12 transform_calculo1.py --apply    (escribe)
"""

import argparse
import io
import os
import re
import sys
import unicodedata
from pathlib import Path

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

from qa_formato_calculo1 import (          # noqa: E402  (misma clasificacion que el validador)
    RE_CALL_HDR, RE_CALL_CONT, RE_EMBED, RE_H, RE_EMOJI, RE_LISTITEM,
    RE_RULE, RE_TAGS_FOOT, RE_WIKI, TIPOS_OK, CANON_U0,
    bloques_callout, clasifica, fix_rutas, fix_rutas_texto, prefijo_esperado,
)

MATERIA = os.path.join("1er Semestre", "Cálculo de una Variable")
CODIGO = "MATG1045"

# alias de tipos de callout que el sitio no reconoce
ALIAS_TIPO = {
    "summary": "abstract",
    "important": "info",
    "question": "question",
    "todo": "todo",
}


# ---------------------------------------------------------------- utilidades

def limpiar_emoji(texto):
    t = RE_EMOJI.sub("", texto)
    t = re.sub(r"\s+", " ", t)
    return t.strip(" \t:-—–")


def slug(texto):
    t = limpiar_emoji(texto).lower()
    t = unicodedata.normalize("NFKD", t)
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return t


def tipo_valido(tipo):
    t = tipo.rstrip("-").lower()
    if t in TIPOS_OK:
        return t
    return ALIAS_TIPO.get(t, "info")


def quote_linea(depth):
    return "> " * (depth - 1) + ">"


def es_linea_tags(linea):
    """True si la linea es SOLO una lista de tags (no un encabezado)."""
    if RE_TAGS_FOOT.match(linea):
        return True
    if re.match(r"^\s*\*\*Tags\*\*\s*:", linea, re.I):
        return True
    if RE_H.match(linea):
        return False
    if re.match(r"^\s*#[^\s]+(\s+#[^\s]+)*\s*$", linea):
        return True
    return False


def calc_dentro(lineas):
    """indices de linea que pertenecen a un callout (incluido su header)."""
    dentro = set()
    for b in bloques_callout(lineas):
        for i in range(b["inicio"], b["fin"] + 1):
            dentro.add(i)
    return dentro


def norm_quote(lineas):
    out = []
    for l in lineas:
        if re.match(r"^\s*(?:>\s*)+$", l):
            depth = l.count(">")
            out.append(quote_linea(max(depth, 1)))
        else:
            out.append(l)
    return out


# ---------------------------------------------------------------- R10

def t_r10(lineas):
    out = []
    n = 0
    for l in lineas:
        m = RE_CALL_HDR.match(l)
        if m:
            tipo = m.group("tipo")
            nuevo = tipo_valido(tipo)
            if nuevo != tipo:
                l = l.replace("[!%s]" % tipo, "[!%s]" % nuevo, 1)
                n += 1
        out.append(l)
    return out, n


# ---------------------------------------------------------------- R6

def t_r6(lineas):
    out = list(lineas)
    ins = []
    for b in bloques_callout(out):
        if not b["lineas"]:
            continue
        idx, dep, rest = b["lineas"][0]
        if dep == b["depth"] and rest.strip() != "":
            ins.append((idx, b["depth"]))
    for pos, depth in sorted(ins, reverse=True):
        out.insert(pos, quote_linea(depth))
    return out, len(ins)


# ---------------------------------------------------------------- R7

def t_r7(lineas):
    out = list(lineas)
    ins = []
    for b in bloques_callout(out):
        if b["depth"] != 1:
            continue
        prev = None
        for idx, depth, rest in b["lineas"]:
            if depth != b["depth"]:
                prev = None
                continue
            t = clasifica(rest)
            if t == "blank":
                prev = None
                continue
            if t == "table" and prev not in (None, "table"):
                ins.append((idx, b["depth"]))
            elif t == "embed" and prev is not None:
                ins.append((idx, b["depth"]))
            prev = t
    for pos, depth in sorted(ins, reverse=True):
        out.insert(pos, quote_linea(depth))
    return out, len(ins)


# ---------------------------------------------------------------- R4

ICONO = {"embed": "🖼️", "tabla": "📊", "lista": "📋", "prosa": "📝", "quote": "❝"}
TIPO_BLOQUE = {"embed": "info", "tabla": "info", "lista": "tip", "prosa": "note", "quote": "quote"}
# la clasificacion del validador usa estos nombres
ALIAS_CLASIF = {"table": "tabla", "listitem": "lista", "prose": "prosa",
                "fence": "prosa", "embed": "embed", "blank": "prosa"}
RE_CONEXION = re.compile(r"referenc|conexion|notas relacionad|notas recomendad|ver tambien", re.I)


def t_r4(lineas):
    """Envuelve el contenido top-level en callouts con titulo."""
    dentro = calc_dentro(lineas)
    out = []
    i, n = 0, len(lineas)
    h1 = h2 = h3 = ""
    envueltos = 0

    # el frontmatter no es prosa: se deja intacto
    fm_fin = -1
    if lineas and lineas[0].strip() == "---":
        for k in range(1, n):
            if lineas[k].strip() == "---":
                fm_fin = k
                break
    if fm_fin >= 0:
        out.extend(lineas[:fm_fin + 1])
        i = fm_fin + 1

    def titulo_para(tipo_bloque, encabezado):
        texto = limpiar_emoji(encabezado)
        if not texto:
            texto = {"embed": "Diagrama", "tabla": "Tabla", "lista": "Lista",
                     "prosa": "Notas", "quote": "Cita"}.get(tipo_bloque, "Notas")
        if tipo_bloque == "lista" and RE_CONEXION.search(encabezado):
            return "info", "🔗"
        return TIPO_BLOQUE[tipo_bloque], ICONO[tipo_bloque]

    while i < n:
        l = lineas[i]
        mh = RE_H.match(l)
        if mh:
            nivel = len(mh.group(1))
            texto = mh.group(2).strip()
            if nivel == 1:
                h1 = texto
            elif nivel == 2:
                h2 = texto
                h3 = ""
            elif nivel == 3:
                h3 = texto
            out.append(l)
            i += 1
            continue
        if i in dentro or not l.strip() or RE_RULE.match(l) or es_linea_tags(l):
            out.append(l)
            i += 1
            continue

        # bloque top-level contiguo
        j = i
        while (j < n and j not in dentro and lineas[j].strip()
               and not RE_RULE.match(lineas[j]) and not RE_H.match(lineas[j])
               and not es_linea_tags(lineas[j])):
            j += 1
        bloque = lineas[i:j]

        # caso especial: el bloque ya es un callout mal formado (header '> [!x-]')
        if RE_CALL_HDR.match(bloque[0]):
            out.extend(bloque)
            i = j
            continue

        # tipo del bloque (clasificacion del validador)
        primera = bloque[0].strip()
        if primera.startswith(">"):
            tipo_bloque = "quote"
        else:
            tipo_bloque = ALIAS_CLASIF.get(clasifica(primera), "prosa")

        encabezado = h3 or h2 or h1
        tipo_call, icono = titulo_para(tipo_bloque, encabezado)
        titulo = "%s %s" % (icono, limpiar_emoji(encabezado) or "Notas")

        cuerpo = []
        for b in bloque:
            if b.startswith(">"):
                cuerpo.append(b)
            elif not b.strip():
                cuerpo.append(">")
            else:
                cuerpo.append("> " + b)

        out.append("> [!%s] %s" % (tipo_call, titulo))
        out.append(">")
        out.extend(cuerpo)
        envueltos += 1
        i = j

    return out, envueltos


# ---------------------------------------------------------------- R1/R13 tags

RE_SECCION_TAGS = re.compile(r"^#{2,4}\s+(?:🏷️\s*)?Tags\s*$", re.I)


def t_tags(lineas, rel, raiz_mat):
    """Normaliza tags: frontmatter + '**Tags:**' al pie. Devuelve (lineas, n)."""
    texto = "\n".join(lineas)

    # 1. recoger tags existentes
    tags = []
    m = re.search(r"^tags:\s*\[(.*?)\]", texto, re.M | re.S)
    if m:
        for t in m.group(1).split(","):
            t = t.strip().strip("'\"")
            if t:
                tags.append(t)
    for l in lineas:
        s = l.strip()
        if s.startswith("**Tags:**") or re.match(r"^\*\*Tags\*\*\s*:", s, re.I):
            for t in re.findall(r"#([^\s#]+)", s):
                tags.append(t)

    # 1b. absorber las lineas de tags sueltas que hay en el cuerpo
    #     (p.ej. '#matematicas/calculo/derivadas #fundamentos/limites ...')
    for l in lineas:
        s = l.strip()
        if RE_H.match(l):
            continue
        if re.match(r"^#[^\s]+(\s+#[^\s]+)*\s*$", s):
            for t in re.findall(r"#([^\s#]+)", s):
                tags.append(t)

    # 2. quitar secciones '## Tags' con su contenido, y absorber esos tags
    out = []
    i, n = 0, len(lineas)
    while i < n:
        l = lineas[i]
        if RE_SECCION_TAGS.match(l):
            i += 1
            while i < n and not RE_H.match(lineas[i]):
                s = lineas[i].strip()
                if s.startswith("#"):
                    for t in re.findall(r"#([^\s#]+)", s):
                        tags.append(t)
                i += 1
            # quitar una linea '---' que quede justo antes
            while out and not out[-1].strip():
                out.pop()
            out.append("")
            out.append("")
            continue
        out.append(l)
        i += 1
    lineas = out

    # 3. quitar lineas de tags sueltas del cuerpo
    out = []
    for l in lineas:
        if es_linea_tags(l) and not l.strip().startswith("**Tags"):
            continue
        out.append(l)
    lineas = out

    # 4. quitar el footer '**Tags:**' viejo (se vuelve a escribir al final)
    out = []
    for l in lineas:
        if l.strip().startswith("**Tags:**") or re.match(r"^\s*\*\*Tags\*\*\s*:", l, re.I):
            continue
        out.append(l)
    lineas = out

    # 5. tags derivados de la ruta (si no hay tags propios)
    partes = Path(rel).parts
    unidad = ""
    for p in partes:
        m2 = re.match(r"^Unidad (\d+)", p)
        if m2:
            unidad = "unidad" + m2.group(1)
            break
    nombre = Path(rel).stem
    nombre = re.sub(r"^\d+\s*-\s*", "", nombre)
    derivados = []
    if unidad:
        derivados.append(unidad)
    s_nombre = slug(nombre)
    if s_nombre:
        derivados.append(s_nombre)

    # 6. frontmatter
    fm_tags = []
    for t in ([CODIGO] + derivados + tags):
        if t and t not in fm_tags:
            fm_tags.append(t)
    fm_tags = fm_tags[:12]

    linea_tags_fm = "tags: [%s]" % ", ".join(fm_tags)
    cierre_fm = None
    for k, l in enumerate(lineas):
        if l.strip() == "---" and k > 0:
            cierre_fm = k
            break
    if lineas and lineas[0].strip() == "---" and cierre_fm is not None:
        cuerpo_fm = lineas[1:cierre_fm]
        # los tags del frontmatter se conservan; se anaden los derivados
        ya = []
        for x in cuerpo_fm:
            mm = re.match(r"^tags:\s*\[(.*?)\]", x, re.S)
            if mm:
                ya = [t.strip().strip("'\"") for t in mm.group(1).split(",") if t.strip()]
        nuevos = [t for t in fm_tags if t not in ya]
        if nuevos:
            cuerpo_fm = [x for x in cuerpo_fm if not re.match(r"^tags:", x)]
            cuerpo_fm.append("tags: [%s]" % ", ".join((ya + nuevos)[:12]))
        lineas = ["---"] + cuerpo_fm + ["---"] + lineas[cierre_fm + 1:]

    # 7. footer '**Tags:**'
    tags_pie = []
    for t in fm_tags:
        if t == CODIGO:
            tags_pie.append("#" + CODIGO)
        else:
            tags_pie.append("#" + t)
    # los tags originales que no esten en el frontmatter tambien van al pie
    for t in tags:
        if t and ("#" + t) not in tags_pie:
            tags_pie.append("#" + t)
    while lineas and not lineas[-1].strip():
        lineas.pop()
    lineas.append("")
    lineas.append("**Tags:** " + " ".join(tags_pie))
    lineas.append("")
    return lineas, 1


# ---------------------------------------------------------------- R2/R3 emoji

MAPA_EMOJI = [
    (r"referenc|bibliogr", "📚"),
    (r"notas relacionad|notas recomendad|conexion|ver tambien|ver también|seguir", "🔗"),
    (r"tags", "🏷️"),
    (r"definici|concepto|idea|introducci|fundamento", "📐"),
    (r"ejemplo", "🧪"),
    (r"error|advertencia|precaucion|precaucaci|errores comunes|problema", "⚠️"),
    (r"ejercicio", "📝"),
    (r"tecnica de estudio|metodo de estudio|mnemotecnia|estrategia|memoria", "🧠"),
    (r"algoritmo|procedimiento|proceso|diagrama", "📊"),
    (r"aplicaci|geometr|fisic|econom|ingenier", "🌍"),
    (r"teorema|lema|proposici", "📜"),
    (r"propiedad|caracteriza|característic", "🔄"),
    (r"tabla|comparaci|cuadro", "📋"),
    (r"resumen|sintesis|síntesis", "📚"),
    (r"límite|limite|asíntota|asintota|continuidad", "🎯"),
    (r"derivada|derivacion|pendiente|tangente|normal", "📈"),
    (r"integral|integracion|integración|antiderivada|primitiva", "🧮"),
    (r"sucesion|sucesión|serie|sumatoria", "🔢"),
    (r"volumen|area|área|longitud", "📐"),
    (r"optimiza|extremo|punto critico|punto crítico", "🎯"),
    (r"razon de cambio|razón de cambio|tasa", "📊"),
    (r"unidad \d", "📚"),
    (r"integral", "∫"),
    (r"límite|limite", "∞"),
]
DEFAULT_H1 = "📘"
DEFAULT_H2 = "🎯"


def emoji_para(texto, default):
    for pat, em in MAPA_EMOJI:
        if re.search(pat, texto, re.I):
            return em
    return default


def t_emoji(lineas):
    out = list(lineas)
    vistos_h1 = 0
    cambios = 0
    for i, l in enumerate(out):
        m = RE_H.match(l)
        if not m:
            continue
        nivel = len(m.group(1))
        if nivel not in (1, 2):
            continue
        texto = m.group(2).strip()
        if nivel == 1:
            vistos_h1 += 1
            if vistos_h1 > 1:
                # H1 duplicado (nota concatenada): se degrada a H2
                out[i] = "#" + l.lstrip("#")
                cambios += 1
                continue
        ems = RE_EMOJI.findall(texto)
        if ems:
            # mover el emoji al inicio si esta al final
            limpio = RE_EMOJI.sub("", texto).strip()
            em = ems[0]
            if not RE_EMOJI.match(texto):
                out[i] = "%s %s %s" % (m.group(1), em, limpio)
                cambios += 1
            continue
        em = emoji_para(texto, DEFAULT_H1 if nivel == 1 else DEFAULT_H2)
        out[i] = "%s %s %s" % (m.group(1), em, texto)
        cambios += 1
    return out, cambios


# ---------------------------------------------------------------- R3 cierre

RE_CIERRE = re.compile(r"referencias|bibliogr|notas recomendadas|conexiones|ver tambien", re.I)


def t_cierre(lineas, rel, raiz_mat):
    h2_textos = []
    for l in lineas:
        m = RE_H.match(l)
        if m and len(m.group(1)) == 2:
            h2_textos.append(m.group(2))
    if any(RE_CIERRE.search(t) for t in h2_textos):
        return lineas, 0

    # enlaces citados en la nota
    texto = "\n".join(lineas)
    vistos, enlaces = set(), []
    for m in RE_WIKI.finditer(texto):
        tgt = m.group(1).split("|")[0].strip()
        if not tgt or tgt in vistos:
            continue
        vistos.add(tgt)
        enlaces.append(tgt)
    # si no hay enlaces, se listan las notas hermanas de la misma subcarpeta
    if not enlaces:
        carpeta = Path(raiz_mat) / Path(rel).parent
        try:
            for p in sorted(carpeta.glob("*.md")):
                if p.name != Path(rel).name:
                    # ruta completa desde la raiz de la materia, como la casa
                    href = (Path(rel).parent / p.name).as_posix()
                    enlaces.append("%s|%s" % (href, p.name))
        except OSError:
            pass
    if not enlaces:
        return lineas, 0

    # la seccion de cierre va ANTES del pie de '**Tags:**' (R13: tags al final)
    out = list(lineas)
    idx_tags = None
    for i, l in enumerate(out):
        if RE_TAGS_FOOT.match(l):
            idx_tags = i
            break
    if idx_tags is None:
        while out and not out[-1].strip():
            out.pop()
        bloque = ["", "## 📚 Referencias", "", "> [!quote] 🔗 Notas relacionadas", ">"]
        for e in enlaces[:12]:
            bloque.append("> - [[%s]]" % e)
        bloque.append("")
        return out + bloque, 1

    # recorta el pie de tags y lo vuelve a pegar al final
    cola = out[idx_tags:]
    cuerpo = out[:idx_tags]
    while cuerpo and not cuerpo[-1].strip():
        cuerpo.pop()
    bloque = ["", "## 📚 Referencias", "", "> [!quote] 🔗 Notas relacionadas", ">"]
    for e in enlaces[:12]:
        bloque.append("> - [[%s]]" % e)
    bloque.append("")
    return cuerpo + bloque + cola, 1


# ---------------------------------------------------------------- pipeline

def transformar(path, rel, raiz_mat, aplicar):
    original = io.open(path, encoding="utf-8").read()
    lineas = original.replace("\ufeff", "").split("\n")
    stats = {}

    lineas, n = t_r10(lineas); stats["R10"] = n
    lineas, n = t_r6(lineas); stats["R6"] = n
    lineas, n = t_r7(lineas); stats["R7"] = n

    # R12 sobre el TEXTO en memoria (no releer el archivo: pisaria lo anterior)
    nuevo, cambios = fix_rutas_texto("\n".join(lineas), os.path.dirname(path), raiz_mat)
    if cambios:
        lineas = nuevo.replace("\ufeff", "").split("\n")
    stats["R12"] = len(cambios)

    lineas = norm_quote(lineas)
    lineas, n = t_r4(lineas); stats["R4"] = n
    lineas = norm_quote(lineas)

    lineas, n = t_tags(lineas, rel, raiz_mat); stats["R1/R13"] = n
    lineas, n = t_emoji(lineas); stats["R2/R3"] = n
    lineas, n = t_cierre(lineas, rel, raiz_mat); stats["R3-cierre"] = n

    salida = "\n".join(lineas)
    if not salida.endswith("\n"):
        salida += "\n"
    cambiada = salida != original
    if aplicar and cambiada:
        io.open(path, "w", encoding="utf-8", newline="\n").write(salida)
    return cambiada, stats


def main():
    ap = argparse.ArgumentParser(description="Aplica FORMATO-CALCULO1")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--solo", default=None)
    args = ap.parse_args()

    vault = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    raiz_mat = os.path.join(vault, MATERIA)
    if args.solo:
        raiz = args.solo if os.path.isabs(args.solo) else os.path.join(vault, args.solo)
    else:
        raiz = raiz_mat

    total = {}
    tocadas = 0
    for dp, ds, fs in os.walk(raiz):
        ds[:] = [d for d in ds if d not in (".obsidian", ".trash", ".git", "__pycache__", "_texto")]
        for f in sorted(fs):
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, raiz_mat).replace("\\", "/")
            cambiada, stats = transformar(p, rel, raiz_mat, args.apply)
            if cambiada:
                tocadas += 1
                for k, v in stats.items():
                    if v:
                        total[k] = total.get(k, 0) + v
            if args.solo is None and not args.apply:
                print("%s  %s" % ("CAMBIA" if cambiada else "igual ", rel))
    print()
    print("notas modificables: %d" % tocadas)
    for k in sorted(total):
        print("  %-12s %d" % (k, total[k]))
    if not args.apply:
        print("(dry-run: no se escribio nada; usa --apply)")


if __name__ == "__main__":
    raise SystemExit(main())
