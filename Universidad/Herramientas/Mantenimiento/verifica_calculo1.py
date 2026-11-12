#!/usr/bin/env python3
"""verifica_calculo1.py — comprueba que la transformacion no pierde contenido.

Compara la nota original (backup) contra la nota transformada y exige que
TODO el contenido original siga presente. Solo se admiten diferencias que
sean transformaciones declaradas:

  - el bloque de frontmatter gana `tags:`
  - los tags pasan a `**Tags:**` al pie
  - las lineas de contenido pueden ganar el prefijo `>` (envoltura en callout)
  - los encabezados ganan un emoji al inicio
  - se anaden lineas `>` en blanco (R6/R7)
  - se envuelven bloques top-level (se anade el header del callout)

Todo lo demas (texto, formulas, tablas, embeds, wikilinks) debe seguir
exactamente.

Uso:
  py -3.12 verifica_calculo1.py --backup "C:\\...\\c1_backup" [--solo "1er Semestre/..."]
"""

import argparse
import io
import os
import re
import sys
from pathlib import Path

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

RE_H = re.compile(r"^(#{1,6})\s+(.*)$")
RE_EMOJI = re.compile(r"[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\u2190-\u21FF\u2049\u203C\u2757]")
RE_EMBED = re.compile(r"!\[\[([^\]]+)\]\]")
RE_WIKI = re.compile(r"(?<!!)\[\[([^\]]+)\]\]")
RE_CALL_HDR = re.compile(r"^\s*(?:>\s*)+")
RE_SECCION_TAGS = re.compile(r"^#{2,4}\s+(?:🏷️\s*)?Tags\s*$", re.I)
RE_LINEA_TAGS = re.compile(r"^#[^\s#]+(\s+#[^\s#]+)*\s*$")

MATERIA = os.path.join("1er Semestre", "Cálculo de una Variable")


def tags_de(texto):
    """Conjunto de tags de un texto (frontmatter + pie + lineas sueltas)."""
    out = set()
    for m in re.finditer(r"^tags:\s*\[(.*?)\]", texto, re.M | re.S):
        for t in m.group(1).split(","):
            t = t.strip().strip("'\"")
            if t:
                out.add(t.lower())
    for l in texto.split("\n"):
        s = l.strip()
        if s.startswith("**Tags:**") or re.match(r"^\*\*Tags\*\*\s*:", s, re.I):
            for t in re.findall(r"#([^\s#]+)", s):
                out.add(t.lower())
        elif RE_LINEA_TAGS.match(s) and not RE_H.match(l):
            for t in re.findall(r"#([^\s#]+)", s):
                out.add(t.lower())
    return out


def normaliza(linea):
    """Quita el prefijo de callout, el emoji de encabezado y el espacio.

    Los embeds se reducen a su BASENAME: R12 reescribe la ruta al prefijo
    canonico (mismo archivo, otra forma de escribirlo), y eso NO es perdida
    de contenido.
    """
    s = linea.strip()
    while RE_CALL_HDR.match(s):
        s = RE_CALL_HDR.sub("", s, count=1).strip()
    s = RE_EMOJI.sub("", s).strip()
    s = re.sub(r"^#{1,6}\s*", "", s).strip()

    def _base(m):
        tgt = m.group(1).split("|")[0].split("#")[0].strip()
        return "![[%s]]" % os.path.basename(tgt.replace("\\", "/"))

    s = RE_EMBED.sub(_base, s)
    return re.sub(r"\s+", " ", s)


def lineas_significativas(lineas):
    """lineas de contenido que DEBEN sobrevivir a la transformacion."""
    out = []
    fm = False
    for i, l in enumerate(lineas):
        s = l.strip()
        if i == 0 and s == "---":
            fm = True
            continue
        if fm:
            if s == "---":
                fm = False
            continue
        if not s:
            continue
        if re.match(r"^tags\s*:", s, re.I):
            continue
        if re.match(r"^\*\*Tags", s, re.I):
            continue
        # la seccion de tags y sus lineas se reubican al pie: no es perdida
        if RE_SECCION_TAGS.match(s):
            continue
        if RE_LINEA_TAGS.match(s) and not RE_H.match(l):
            continue
        if s == "---":
            continue
        n = normaliza(l)
        if len(n) < 2:
            continue
        if re.match(r"^\[![\w\-]+\]", n):      # header de callout: puede cambiar de texto
            continue
        out.append(n)
    return out


def main():
    ap = argparse.ArgumentParser(description="Verifica que no se pierda contenido")
    ap.add_argument("--backup", required=True)
    ap.add_argument("--solo", default=None)
    args = ap.parse_args()

    vault = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    raiz_mat = os.path.join(vault, MATERIA)
    raiz = args.solo if args.solo and os.path.isabs(args.solo) else (
        os.path.join(vault, args.solo) if args.solo else raiz_mat)
    # el backup puede ser: la raiz de la materia, la carpeta que la contiene,
    # o un nivel por encima. Se resuelve probando candidatos.
    backup = args.backup
    candidatos = [
        backup,
        os.path.join(backup, "Cálculo de una Variable"),
        os.path.join(backup, "1er Semestre", "Cálculo de una Variable"),
    ]
    # prueba: ¿existe alguna nota de la materia dentro del candidato?
    muestra = os.path.join(raiz_mat, "Cálculo de una Variable.md")
    backup = None
    for c in candidatos:
        if not os.path.isdir(c):
            continue
        rel_prueba = os.path.relpath(muestra, raiz_mat)
        if os.path.isfile(os.path.join(c, rel_prueba.replace("/", os.sep))):
            backup = c
            break
    if backup is None:
        print("no se encuentra el backup en: %s" % args.backup)
        return 2
    print("backup: %s" % backup)

    problemas = []
    notas = 0
    for dp, ds, fs in os.walk(raiz):
        ds[:] = [d for d in ds if d not in (".obsidian", ".trash", ".git", "__pycache__", "_texto")]
        for f in sorted(fs):
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, raiz_mat).replace("\\", "/")
            bp = os.path.join(backup, rel.replace("/", os.sep))
            if not os.path.isfile(bp):
                problemas.append((rel, "sin backup"))
                continue
            notas += 1
            antes = lineas_significativas(io.open(bp, encoding="utf-8").read().split("\n"))
            antes_txt = io.open(bp, encoding="utf-8").read()
            despues_txt = io.open(p, encoding="utf-8").read()
            despues = lineas_significativas(despues_txt.split("\n"))
            # indice de lineas del despues (para multiset)
            from collections import Counter
            cnt = Counter(despues)
            for linea in antes:
                if cnt[linea] > 0:
                    cnt[linea] -= 1
                else:
                    problemas.append((rel, "contenido perdido: %s" % linea[:90]))
            # tags: cada tag original debe seguir existiendo en la nota
            tags_perdidos = tags_de(antes_txt) - tags_de(despues_txt)
            if tags_perdidos:
                problemas.append((rel, "tags perdidos: %s" % ", ".join(sorted(tags_perdidos)[:5])))
            # embeds y wikilinks: recuento (por basename: R12 reescribe la ruta)
            for nombre, rx in (("embed", RE_EMBED), ("wikilink", RE_WIKI)):
                a = Counter(os.path.basename(x.split("|")[0].split("#")[0].strip()
                            .replace("\\", "/")) for x in rx.findall(io.open(bp, encoding="utf-8").read()))
                b = Counter(os.path.basename(x.split("|")[0].split("#")[0].strip()
                            .replace("\\", "/")) for x in rx.findall(despues_txt))
                faltan = a - b
                if faltan:
                    problemas.append((rel, "%s perdidos: %s" % (nombre, dict(list(faltan.items())[:3]))))

    print("notas comparadas: %d" % notas)
    print("problemas: %d" % len(problemas))
    for rel, det in problemas[:60]:
        print("  %-70s %s" % (rel[:70], det))
    return 1 if problemas else 0


if __name__ == "__main__":
    raise SystemExit(main())
