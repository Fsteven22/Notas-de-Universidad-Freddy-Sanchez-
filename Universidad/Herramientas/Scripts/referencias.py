#!/usr/bin/env python3
"""Audita y completa referencias en notas FESD (stdlib).

Dos modos:
  1. AUDIT (default, read-only): reporta por nota si tiene
     - seccion `## 📚 Referencias` (fuentes consultadas, estilo IEEE), o
     - links [[...]] a notas hermanas de la materia (>= --min, default 2).
     Marca SIN REFERENCIAS a las notas que no cumplen ninguna.

  2. --aplicar: a las notas SIN REFERENCIAS agrega al final una seccion
     `## 🔗 Relacionadas` con bullets [[...]] a sus notas hermanas
     (misma carpeta; si la carpeta no tiene otras notas, con la MOC de la
     materia). Nunca inventa citas bibliograficas.

Uso:
  py referencias.py                     # barrido completo de FESD, dry-run
  py referencias.py "Unidad 2 - Introducción a la Electrónica"
  py referencias.py "ruta/nota.md" --aplicar
  py referencias.py --min 3             # exigir mas links inline

Despues de --aplicar correr verificar_nota.py (regla del vault).
"""
import re
import sys
from pathlib import Path

from kit_recuperacion import MEDIA_DIRS, ending_style, find_materia, repo_root

REF_SECTION_RE = re.compile(r"^#{1,4}.*\bReferencias\b", re.IGNORECASE)
REL_SECTION_RE = re.compile(r"^#{1,4}.*\b(?:Relacionadas|Relacionada|Vease tambien|Ver tambien)\b", re.IGNORECASE)
WIKILINK_RE = re.compile(r"\[\[([^\[\]#|\n]+)(?:#[^\]|\n]*)?(?:\|[^\]\n]*)?\]\]")

DEFAULT_MIN = 2
RANGO_HEADER = "## \U0001F517 Relacionadas"


def collect(repo: Path, base: Path):
    for p in sorted(base.rglob("*.md")):
        rel = p.relative_to(repo)
        if any(part in MEDIA_DIRS for part in rel.parts):
            continue
        yield p, rel


def body_of(raw: bytes):
    lines = raw.decode("utf-8", "replace").replace("\r\n", "\n").split("\n")
    if lines and lines[0].strip() == "---":
        try:
            close = next(i for i in range(1, min(len(lines), 20)) if lines[i].strip() == "---")
            return lines[close + 1:], lines
        except StopIteration:
            return lines, lines
    return lines, lines


def configurar_salida():
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def main() -> int:
    configurar_salida()
    repo = repo_root()
    materia = find_materia(repo)
    args = sys.argv[1:]
    aplicar = "--aplicar" in args
    exigir = DEFAULT_MIN
    if "--min" in args:
        try:
            exigir = int(args[args.index("--min") + 1])
        except (IndexError, ValueError):
            pass
    pos = [a for a in args if not a.startswith("--")]
    if pos:
        q = Path(pos[0])
        base = q if q.suffix == ".md" and q.exists() else (materia / pos[0])
    else:
        base = materia
    if not base.exists():
        print("ruta no existe:", base)
        return 2

    stems = {}
    for p, _ in collect(repo, materia):
        stems[p.stem.lower()] = p

    sin = 0
    for p, rel in collect(repo, base):
        raw = p.read_bytes()
        eol = ending_style(raw)
        body, _ = body_of(raw)
        tiene_refs = any(REF_SECTION_RE.match(l) for l in body)
        tiene_rel = any(REL_SECTION_RE.match(l) for l in body)
        linked = set()
        for l in body:
            for m in WIKILINK_RE.finditer(l):
                base_name = m.group(1).strip()
                if base_name.lower() in stems and base_name.lower() != p.stem.lower():
                    linked.add(stems[base_name.lower()])
        ok = tiene_refs or tiene_rel or len(linked) >= exigir
        diccpref = "refs" if tiene_refs else ("rel" if tiene_rel else "-")
        print("%-14s links:%-3d %s %s" % ("OK" if ok else "SIN REF", len(linked), diccpref, str(rel)[:80]))
        if ok:
            continue
        sin += 1
        if not aplicar:
            continue
        hermanos = sorted(x for x in p.parent.glob("*.md")
                          if x != p and x.stem.lower() in stems)
        if not hermanos:
            fallback = materia / "Fundamentos de Electricidad y Sistemas Digitales.md"
            if fallback.exists() and fallback != p:
                hermanos = [fallback]
        seccion = ["", RANGO_HEADER, ""]
        seccion += ["- [[%s]]" % h.stem for h in hermanos]
        texto = "\n".join(body + seccion)
        p.write_bytes(texto.replace("\n", "\r\n").encode("utf-8") if eol == "\r\n"
                      else texto.encode("utf-8"))
        print("   -> seccion agregada con %d links" % len(hermanos))
    print("sin referencias:", sin, "| modo:",
          "APLICAR" if aplicar else "dry-run (--aplicar escribe)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
