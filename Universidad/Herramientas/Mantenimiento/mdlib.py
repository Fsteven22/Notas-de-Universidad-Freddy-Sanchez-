import os, io, re

# Utilidades compartidas para los scripts de mantenimiento del vault.

SKIP = (".obsidian", ".trash", ".git", "node_modules")
EXCLUDE = ("Catalogo de errores del vault.md",)  # nota espejo del usuario: sus ejemplos son intencionales

RE_CALL = re.compile(r"^\s*(>+)\s*\[!([a-zA-Z]+)\](-?)")

def legible(p):
    return os.path.relpath(p, "") if False else p

def walk_notes(root):
    for dp, ds, fs in os.walk(root):
        ds[:] = [d for d in ds if d not in SKIP]
        for f in fs:
            if f.endswith(".md"):
                p = os.path.join(dp, f)
                rel = os.path.relpath(p, root)
                if rel.split(os.sep)[-1] in EXCLUDE:
                    continue
                yield p, rel

def load(p):
    return io.open(p, encoding="utf-8").read()

def save(p, t):
    io.open(p, "w", encoding="utf-8", newline="\n").write(t)

def report(path, rows):
    io.open(path, "w", encoding="utf-8", newline="\n").write("\n".join(rows) if rows else "")

def callout(line):
    """(profundidad, tipo, plegado) si la linea inicia callout; None si no."""
    m = RE_CALL.match(line)
    if m:
        return len(m.group(1)), m.group(2).lower(), m.group(3) == "-"
    return None

def es_fences(lines):
    """indices donde cambia el estado de un code fence (con o sin prefijo >)"""
    estados = {}
    f = False
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s.startswith("```"):
            estados[i] = not f
            f = not f
    return estados
