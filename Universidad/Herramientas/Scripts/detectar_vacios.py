#!/usr/bin/env python3
"""Detecta ejercicios/callouts vacios: headers `> [!example]` (o ##) sin
contenido debajo (solo blancos hasta el siguiente header/callout/separador).
Uso:  py detectar_vacios.py [carpeta]  (default: vault Universidad)
Registro de patrones (ver LEEME-SCRIPTS.md).
"""
import pathlib
import re
import sys

HEADER_RE = re.compile(r"^(?:>\s*)?#{1,4} ")
CALL_RE = re.compile(r"^>\s*\[!(example|note|tip|question)\]")


def main() -> int:
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    base = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path(
        "C:/Users/Steven Sànchez/OneDrive/OneSyncFiles/Universidad")
    hits = 0
    for f in sorted(base.rglob("*.md")):
        try:
            L = f.read_text(encoding="utf-8").splitlines()
        except Exception:
            continue
        for i, l in enumerate(L):
            # solo ejercicios: callouts example y headers ###/####.
            # (## seguido de ### es estructura normal, no vacio)
            m_h = re.match(r"^(#{3,4}) ", l)
            m_c = CALL_RE.match(l) and "example" in l
            if not (m_h or m_c):
                continue
            if m_c and re.sub(r"^>\s*\[![\w-]+\]\s*", "", l).strip():
                continue  # contenido en la misma linea del header: no vacio
            j = i + 1
            while j < len(L) and L[j].strip() == "":
                j += 1
            if j >= len(L):
                continue
            nxt = L[j]
            if nxt.strip() in ("---", ""):
                empty = True
            else:
                m_nh = re.match(r"^(#{1,4}) ", nxt)
                if m_c:
                    empty = bool(m_nh or CALL_RE.match(nxt))
                else:
                    # header: vacio solo si lo que sigue no es mas profundo
                    empty = bool(m_nh and len(m_nh.group(1)) <= len(m_h.group(1)))
            if empty:
                print("%s:%d VACIO: %s" % (f.name[:55], i + 1, l[:75]))
                hits += 1
    print("vacios:", hits)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
