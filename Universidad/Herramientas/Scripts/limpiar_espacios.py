#!/usr/bin/env python3
"""Safe whitespace cleanup for vault notes (stdlib only).

Usage:  py limpiar_espacios.py "ruta/nota.md" [--fix]

Default is DRY-RUN (only reports). With --fix it rewrites the file:
  - collapses 2+ consecutive blank lines into 1 (outside fences),
  - collapses 2+ consecutive bare `>` separators into 1,
  - strips trailing whitespace,
  - preserves the file's line endings (CRLF stays CRLF).

It NEVER deletes:
  - single blank lines between sibling callouts/blocks,
  - blank lines inside ``` fences,
  - anything inside frontmatter except nothing (frontmatter untouched).

Run verificar_nota.py before AND after.
"""
import pathlib
import sys

FENCE_RE = __import__("re").compile(r"^(>*)\s*```")


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    fix = "--fix" in sys.argv
    if not args:
        print('Uso: py limpiar_espacios.py "ruta/nota.md" [--fix]')
        return 2
    p = pathlib.Path(args[0])
    raw = p.read_bytes()
    crlf = raw.count(b"\r\n") > raw.count(b"\n") / 2
    L = raw.decode("utf-8").split("\r\n" if crlf else "\n")

    # fence map (do not touch inside)
    idx = [i for i, l in enumerate(L) if FENCE_RE.match(l)]
    inside = [False] * len(L)
    for k in range(0, len(idx) - 1, 2):
        for i in range(idx[k], idx[k + 1] + 1):
            inside[i] = True

    out: list[str] = []
    stats = {"blanks": 0, "seps": 0, "trail": 0}
    for i, l in enumerate(L):
        if inside[i]:
            out.append(l)
            continue
        s = l.rstrip()
        if s != l:
            stats["trail"] += 1
        if s.strip() == "" and out and out[-1].strip() == "":
            stats["blanks"] += 1
            continue
        if s.strip() == ">" and out and out[-1].strip() == ">":
            stats["seps"] += 1
            continue
        out.append(s)

    print("blanks sobrantes: %d | separadores dobles: %d | trailing: %d | %s" % (
        stats["blanks"], stats["seps"], stats["trail"], "CRLF" if crlf else "LF"))
    if fix:
        txt = "\n".join(out)
        p.write_bytes((txt.replace("\n", "\r\n") if crlf else txt).encode("utf-8"))
        print("escrito:", p.name)
    else:
        print("(dry-run: agrega --fix para aplicar)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
