#!/usr/bin/env python3
"""Kit de recuperacion y saneamiento FESD (stdlib + git).

Historia: el 19/10/2026 un script de tags con un bug (insertaba un segundo
`tags:` y sobrescribia notas con el contenido de otra nota) dano 18 notas de
teoria FESD y 6 practicas. Este kit consolida mi recuperacion completa con
dry-run por defecto: cualquier escritura requiere --aplicar.

Uso:
  py kit_recuperacion.py daniadas <ref_operda> <ref_dano>
      Candidatos danados: numstat entre refs; .md de FESD con
      (borradas - agregadas) > 60. Requiere refs validas de git.

  py kit_recuperacion.py restore <ref_ok> <ref_dano> [--aplicar]
      Restaura cada candidato con su contenido desde <ref_ok> y garantiza
      UNA linea `tags:` correcta por unidad + `dg-publish: true` dentro del
      frontmatter. Si la nota ya tiene `tags:` no inserta (regla
      anti doble-tags).

  py kit_recuperacion.py repath [subcarpeta] [--aplicar]
      Reescribe embeds del arbol FESD: `![[Diagramas/...` → ruta relativa
      correcta segun profundidad de la nota; media bare-name que existe en
      `Anexos` se redirige a `<rel>Anexos/`.

  py kit_recuperacion.py pipes [subcarpeta|nota.md] [--aplicar]
      Escapa pipes de alias en wikilinks dentro de filas de tabla
      ([[dest|alias]] → [[dest\\|alias]]) donde el conteo de pipes excede
      el header de la tabla.

  py kit_recuperacion.py sweep [subcarpeta]
      Corre verificar_nota.py sobre cada .md del arbol (read-only).

  py kit_recuperacion.py compa <ref> <ruta_relativa_al_repo>
      Compara el cuerpo (sin frontmatter) del archivo en <ref> vs disco;
      reporta lineas compartidas, similaridad y headers de cada version.

Tags por carpeta (esquema FESD):
  Unidad 1 -> [EYAG1037, unidad1, electricidad]
  Unidad 2 -> [unidad2, electronica]
  Unidad 3 -> [unidad3, circuitos-integrados]
  Unidad 4 -> [unidad4, sistemas-digitales]
  Ejercicios Recopilados -> [EYAG1037, unidad1, ejercicios]
  Fundamentos del Laboratorio -> [EYAG1037, laboratorio]
"""
import difflib
import os
import re
import subprocess
import sys
from pathlib import Path

GIT_EXE = r"C:\Program Files\Git\bin\git.exe"
MATERIA_PREFIX = "Fundamentos de El"
MEDIA_DIRS = ("Anexos", "Diagramas")
MEDIA_EXTS = (".png", ".jpg", ".jpeg", ".svg", ".pdf", ".mmd", ".gif", ".webp")
EMBED_RE = re.compile(r"!\[\[([^\[\]\r\n]+)\]\]")
PIPE_LINE_RE = re.compile(r"^(?:\s|>\s*)*\|")

TAGS = [
    ("Unidad 1 - Electricidad", "[EYAG1037, unidad1, electricidad]"),
    ("Unidad 2 - ", "[unidad2, electronica]"),
    ("Unidad 3 - ", "[unidad3, circuitos-integrados]"),
    ("Unidad 4 - ", "[unidad4, sistemas-digitales]"),
    ("Ejercicios Recopilados", "[EYAG1037, unidad1, ejercicios]"),
    ("Fundamentos del Laboratorio", "[EYAG1037, laboratorio]"),
]


def out_safe():
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass


def repo_root() -> Path:
    p = Path(__file__).resolve().parent
    while p != p.parent:
        if (p / ".git").exists():
            return p
        p = p.parent
    raise SystemExit("no encontre .git subiendo desde %s" % Path(__file__))


def find_materia(root: Path) -> Path:
    univ = root / "Universidad"
    for d in sorted(univ.rglob("*")):
        if d.is_dir() and d.name.startswith(MATERIA_PREFIX):
            return d
    raise SystemExit("no encontre carpeta FESD bajo " + str(univ))


def git(args, repo: Path, binary=False):
    r = subprocess.run([GIT_EXE, "-C", str(repo), *args], capture_output=True)
    return r.stdout if binary else r.stdout.decode("utf-8", "replace")


def git_unquote(p: str) -> str:
    m = re.match(r'"(.*)"$', p, re.S)
    s = m.group(1) if m else p
    if "\\" not in s:
        return s
    raw = re.sub(r"\\([0-7]{3})", lambda mm: chr(int(mm.group(1), 8)), s)
    return raw.encode("latin-1").decode("utf-8")


def numstat_candidatos(repo: Path, ref_ok: str, ref_dano: str, materia_rel: str):
    raw = git(["diff", "--numstat", ref_ok, ref_dano, "--", "*.md"], repo)
    found = []
    for line in raw.splitlines():
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        a = int(parts[0]) if parts[0].isdigit() else 0
        d = int(parts[1]) if parts[1].isdigit() else 0
        p = git_unquote(parts[2].strip())
        if materia_rel in p and p.endswith(".md") and d - a > 60:
            found.append(p)
    return found


def detect_tags(nota: str):
    for needle, tagline in TAGS:
        if needle in nota:
            return "tags: " + tagline
    return None


def ending_style(data: bytes) -> str:
    return "\r\n" if data.count(b"\r\n") > data.count(b"\n") / 2 else "\n"


def write_preserving(p: Path, text: str, data: bytes) -> None:
    if ending_style(data) == "\r\n":
        text = text.replace("\n", "\r\n")
    p.write_bytes(text.encode("utf-8"))


def ensure_frontmatter(text: str, nota: str):
    tagline = detect_tags(nota)
    lines = text.split("\n")
    head = lines[:12]
    has_tags = any(l.strip().startswith("tags:") for l in head)
    has_pub = any(l.strip() == "dg-publish: true" for l in head)
    if lines and lines[0].strip() == "---":
        close = next((i for i in range(1, min(len(lines), 15)) if lines[i].strip() == "---"), None)
        if close is None:
            return text, False
        if tagline and not has_tags:
            lines.insert(close, tagline)
        if not has_pub:
            lines.insert(1, "dg-publish: true")
        return "\n".join(lines), (not has_tags or not has_pub)
    if tagline:
        return "\n".join(["---", tagline, "dg-publish: true", "---", ""] + lines), True
    return "\n".join(["---", "dg-publish: true", "---", ""] + lines), True


def cmd_daniadas(repo, materia_rel, args):
    if len(args) < 2:
        print("uso: daniadas <ref_ok> <ref_dano>")
        return 2
    found = numstat_candidatos(repo, args[0], args[1], materia_rel)
    print("candidatos %s..%s: %d" % (args[0], args[1], len(found)))
    for p in found:
        print("  ", p)
    return 0


def cmd_restore(repo, materia_rel, args):
    aplicar = "--aplicar" in args
    ref_ok, ref_dano = args[0], args[1]
    cand = numstat_candidatos(repo, ref_ok, ref_dano, materia_rel)
    print("candidatos: %d | modo: %s" % (len(cand), "APLICAR" if aplicar else "dry-run"))
    for p in cand:
        show = git(["show", ref_ok + ":" + p], repo, binary=True)
        text = (show or b"").decode("utf-8", "replace")
        if not text:
            print("VACIO en", ref_ok, ":", p)
            continue
        fs = repo / p
        if not fs.exists():
            print("FALTA EN DISCO:", p)
            continue
        cur = fs.read_bytes()
        body = text.replace("\r\n", "\n")
        new, _ = ensure_frontmatter(body, p)
        data = new.encode("utf-8")
        same = data == cur or new.replace("\n", ending_style(cur)) == cur.decode("utf-8", "replace")
        print(("=" if same else "!"), fs.name[:55], "|", len(data), "bytes")
        if aplicar and not same:
            write_preserving(fs, new, cur)
            print("   -> escrito")
    return 0


def cmd_repath(repo, materia_rel, args):
    aplicar = "--aplicar" in args
    pos = [a for a in args if not a.startswith("--")]
    materia = find_materia(repo)
    base = materia / pos[0] if pos else materia
    anexos = set()
    adir = materia / "Anexos"
    if adir.exists():
        for f in adir.iterdir():
            if f.suffix.lower() in MEDIA_EXTS:
                anexos.add(f.name)
    changed = 0
    for p in sorted(base.rglob("*.md")):
        if any(part in MEDIA_DIRS for part in p.relative_to(repo).parts):
            continue
        depth = len(p.parent.relative_to(materia).parts)
        if depth == 0:
            continue
        rel = "../" * depth
        data = p.read_bytes()
        text = data.decode("utf-8").replace("\r\n", "\n")
        orig = text
        text = text.replace("![[Diagramas/", "![[%sDiagramas/" % rel)

        def rep(m):
            name = m.group(1)
            if "/" in name:
                return m.group(0)
            if name in anexos:
                return "![[%sAnexos/%s]]" % (rel, name)
            return m.group(0)

        text = EMBED_RE.sub(rep, text)
        if text != orig:
            changed += 1
            print(p.name[:60], "->", rel)
            if aplicar:
                write_preserving(p, text, data)
    print("notas con embeds reescritos:", changed, "| modo:", "APLICAR" if aplicar else "dry-run")
    return 0


def escape_alias_pipes(l: str):
    out = []
    inside = False
    for k in range(len(l)):
        if l.startswith("[[", k):
            inside = True
        elif l.startswith("]]", k):
            inside = False
        out.append("\\|" if (l[k] == "|" and inside) else l[k])
    return "".join(out)


def cmd_pipes(repo, materia_rel, args):
    aplicar = "--aplicar" in args
    pos = [a for a in args if not a.startswith("--")]
    materia = find_materia(repo)
    if pos and Path(pos[0]).suffix == ".md":
        targets = [Path(pos[0])]
    elif pos:
        targets = sorted((materia / pos[0]).rglob("*.md"))
    else:
        targets = sorted(materia.rglob("*.md"))
    total = 0
    for p in targets:
        data = p.read_bytes()
        lines = data.decode("utf-8").replace("\r\n", "\n").split("\n")
        new_lines = list(lines)
        fixed_in_file = 0
        groups, cur = [], []
        for idx, l in enumerate(lines):
            if PIPE_LINE_RE.match(l):
                cur.append((idx, l))
            elif cur:
                groups.append(cur)
                cur = []
        if cur:
            groups.append(cur)
        for group in groups:
            if len(group) < 2:
                continue
            n0 = group[0][1].replace("\\|", "").count("|")
            for idx, l in group[1:]:
                s = l.replace("\\|", "")
                if set(s.strip()) <= set("|:- ") or s.count("|") == n0:
                    continue
                nl = escape_alias_pipes(l)
                if nl != l and nl.replace("\\|", "").count("|") == n0:
                    new_lines[idx] = nl
                    fixed_in_file += 1
                    total += 1
        if fixed_in_file:
            print(p.name[:60], "-> celdas fixadas:", fixed_in_file)
            if aplicar:
                text = "\n".join(new_lines)
                p.write_bytes(text.replace("\n", "\r\n").encode("utf-8")
                              if ending_style(data) == "\r\n"
                              else text.encode("utf-8"))
    print("celdas totales:", total, "| modo:", "APLICAR" if aplicar else "dry-run")
    return 0


def cmd_sweep(repo, materia_rel, args):
    materia = find_materia(repo)
    pos = [a for a in args if not a.startswith("--")]
    base = materia / pos[0] if pos else materia
    verif = repo / "Universidad" / "Herramientas" / "Scripts" / "verificar_nota.py"
    skip = set(MEDIA_DIRS)
    n = tot_err = 0
    for dirpath, dirnames, filenames in os.walk(base):
        dirnames[:] = [d for d in dirnames if d not in skip]
        for f in filenames:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dirpath, f)
            r = subprocess.run([sys.executable, str(verif), p], capture_output=True)
            m = re.search(r"errores: (\d+) \| avisos: (\d+)",
                          (r.stdout + r.stderr).decode("utf-8", "replace"))
            a = int(m.group(1)) if m else 0
            n += 1
            tot_err += a
            if a:
                print(p[-70:], a, m.group(0) if m else "")
    print("notas verificadas:", n, "| errores:", tot_err)
    return 1 if tot_err else 0


def cmd_compa(repo, materia_rel, args):
    if len(args) < 2:
        print("uso: compa <ref> <ruta_relativa_al_repo>")
        return 2
    ref, p_rel = args[0], args[1].replace(os.sep, "/")
    old = git(["show", ref + ":" + p_rel], repo, binary=True).decode("utf-8", "replace")
    cur = (repo / p_rel).read_bytes().decode("utf-8", "replace")
    body_old = "\n".join(old.split("\n")[3:])
    body_cur = "\n".join(cur.split("\n")[3:])
    lo, lc = body_old.split("\n"), body_cur.split("\n")
    sset = set(lc)
    shared = sum(1 for l in lo if l in sset)
    ratio = difflib.SequenceMatcher(None, body_old, body_cur).ratio()
    print(ref, ":", len(old), "chars | disco:", len(cur), "chars")
    print("lineas del ref presentes en disco:", shared, "/", len(lo))
    print("similaridad cuerpo:", round(ratio, 3))
    for name, L in (("ref " + ref, lo), ("disco", lc)):
        heads = [l for l in L if l.startswith("## ")][:20]
        print("headers", name, ":", len(heads))
        for h in heads:
            print("   ", h[:90])
    return 0


def main() -> int:
    out_safe()
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    cmd, args = sys.argv[1], sys.argv[2:]
    repo = repo_root()
    materia_rel = str(find_materia(repo) / "x").replace(os.sep, "/")
    materia_rel = materia_rel.rsplit("/", 1)[0]
    handlers = {
        "daniadas": cmd_daniadas,
        "restore": cmd_restore,
        "repath": cmd_repath,
        "pipes": cmd_pipes,
        "sweep": cmd_sweep,
        "compa": cmd_compa,
    }
    if cmd not in handlers:
        print("comando no reconocido:", cmd)
        print(__doc__)
        return 2
    return handlers[cmd](repo, materia_rel, args)


if __name__ == "__main__":
    raise SystemExit(main())
