#!/usr/bin/env python3
"""Pre-flight check for one vault note (read-only, stdlib only).

Usage:  py verificar_nota.py "ruta/nota.md"

Checks (exit 0 = clean, 1 = findings):
 1. Frontmatter: exists, dg-publish true/false, no blank lines inside, tags present.
 2. Orphan callouts: `> [!x]` / `> > [!x]` headers not connected to a parent quote.
 3. Blank-line disease: empty lines strictly inside a quote run
    (both neighbors start with `>`). If a neighbor is a bare `>`, it is
    corruption (breaks Live Preview); otherwise it is a sibling separator (ok).
 4. Fences: unbalanced ``` count; open/close quote mismatch; empty or
    quote-only lines INSIDE fences (render literally / break the callout).
 5. Mermaid-in-callout warning: ```mermaid inside quotes shows as code in
    Live Preview (convert to SVG with mmdc, see LEEME-SCRIPTS.md).
 6. Embeds: every ![[*.svg|png|pdf|mmd]] resolves from the note's folder.
 7. Tables: pipe-count mismatch vs header row (ignoring \\|), inside quotes too.
 8. Headers: indented (`   ###`) or glued (content line directly before ###).
 9. Line endings: CRLF / LF / mixed report (mixed = fail).
"""
import pathlib
import re
import sys

FENCE_RE = re.compile(r"^(?P<q>>*)\s*```(?P<info>.*)$")
CALLOUT_RE = re.compile(r"^((?:>\s*)+)\[!([\w-]+)\]")


def main() -> int:
    p = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None
    if not p or not p.exists():
        print("Uso: py verificar_nota.py \"ruta/nota.md\"")
        return 2
    raw = p.read_bytes()
    n_crlf, n_lf = raw.count(b"\r\n"), raw.count(b"\n")
    L = raw.decode("utf-8").splitlines()
    bad: list[str] = []
    warn: list[str] = []

    def rep(msg: str) -> None:
        bad.append(msg)

    # 9. endings
    if n_crlf and n_crlf != n_lf:
        rep(f"ENDINGS mixed: {n_crlf} CRLF + {n_lf - n_crlf} LF (normalize!)")
    else:
        print(f"endings: {'CRLF' if n_crlf else 'LF'} ({len(L)} lineas)")

    # 1. frontmatter
    if not L or L[0] != "---":
        rep("FRONTMATTER ausente (primera linea no es ---)")
    else:
        j = next((i for i in range(1, min(len(L), 15)) if L[i] == "---"), -1)
        if j < 0:
            rep("FRONTMATTER sin cierre ---")
        else:
            fm = L[1:j]
            if any(l.strip() == "" for l in fm):
                rep("FRONTMATTER con lineas vacias adentro (rompe YAML)")
            if not any("dg-publish" in l for l in fm):
                rep("FRONTMATTER sin dg-publish")
            if not any(l.strip().startswith("tags") for l in fm):
                warn.append("frontmatter sin tags")

    # fence map (for 4/5)
    opens: list[tuple[int, str]] = []
    for i, l in enumerate(L):
        m = FENCE_RE.match(l)
        if m:
            opens.append((i + 1, m.group("q")))
    if len(opens) % 2:
        rep(f"FENCES desbalanceados: {len(opens)} marcas ```")
    inside = [False] * len(L)
    quoted_fence = [False] * len(L)
    for k in range(0, len(opens) - 1, 2):
        a, b = opens[k], opens[k + 1]
        if a[1] != b[1]:
            rep(f"FENCE quoting mismatch L{a[0]} vs L{b[0]}")
        for i in range(a[0] - 1, b[0]):
            inside[i] = True
            quoted_fence[i] = bool(a[1])
        info = L[a[0] - 1].strip().lstrip(">").strip()
        if info.startswith("```mermaid") and a[1]:
            warn.append(f"mermaid-en-callout L{a[0]} (en Live Preview se ve como codigo; mejor SVG)")

    for i, l in enumerate(L):
        n = i + 1
        if inside[i]:
            # vacios solo rompen dentro de callouts; a nivel superior son legibles
            if quoted_fence[i] and (l == "" or l.strip() in (">", "> >")):
                rep(f"L{n}: linea vacia/suelta DENTRO de fence en callout (corta el quote o sale literal)")
            continue
        # 3. blank-line disease: empty strictly inside a quote run, EXCEPT
        # sibling separation (one side is a `> [!...]` callout header).
        if l.strip() == "" and 0 < i < len(L) - 1 \
                and L[i - 1].startswith(">") and L[i + 1].startswith(">"):
            hdr = (re.match(r"^> \[!", L[i - 1]) or re.match(r"^> > \[!", L[i - 1])
                   or re.match(r"^> \[!", L[i + 1]) or re.match(r"^> > \[!", L[i + 1]))
            if not hdr:
                rep(f"L{n}: vacio dentro del flujo del quote (rompe el callout en Live Preview)")
        # 2. orphan callouts
        if CALLOUT_RE.match(l):
            depth = l.split("[")[0].count(">")
            if depth > 1:
                k = i - 1
                while k >= 0 and L[k].strip() == ">":
                    k -= 1
                if k < 0 or not L[k].startswith(">"):
                    rep(f"L{n}: success/callout huerfano (sin quote padre)")
        # 8. headers
        if re.match(r"^ +#", l):
            rep(f"L{n}: header indentado")
        if re.match(r"^#{1,4} ", l) and i > 0 and L[i - 1].strip() != "" \
                and not L[i - 1].startswith(">"):
            warn.append(f"L{n}: header pegado a contenido (falta blanco antes)")

    # 6. embeds
    for i, l in enumerate(L):
        if inside[i]:
            continue
        # 6b. HTML-eaters: <<stereotipo>> en prosa se lo traga el renderer
        # (en fences o `codigo` esta bien). Regla: backticks o nada.
        t = re.sub(r"`[^`]*`", "", l)
        for m in re.finditer(r"<<[A-Za-z]+>>", t):
            rep(f"L{i + 1}: <<..>> en prosa rompe el render (usa `codigo`): {m.group(0)}")
        for m in re.finditer(r"!\[\[([^\]]+)\]\]", l):
            tgt = m.group(1).split("|")[0].split("#")[0]
            if tgt.endswith((".svg", ".png", ".jpg", ".jpeg", ".pdf", ".mmd")) \
                    or "/" in tgt:
                if not (p.parent / tgt).exists():
                    rep(f"L{i + 1}: embed no resuelve: {tgt[:70]}")

    # 7. tables: consecutive |-lines STARTING with | (quote-tolerant).
    # (List items like `- a || b` are not tables and are skipped.)
    grp: list[tuple[int, str]] = []
    def flush() -> None:
        first = re.sub(r"^(?:>\s*)*", "", grp[0][1]).lstrip() if grp else ""
        if len(grp) >= 2 and first.startswith("|"):
            head = grp[0][1].replace("\\|", "")
            n0 = head.count("|")
            for ln, ll in grp[1:]:
                s = ll.replace("\\|", "")
                if set(s.strip()) <= set("|: -"):
                    continue
                if s.count("|") != n0:
                    rep(f"L{ln}: tabla con {s.count('|')} pipes (header {n0})")
        grp.clear()
    for i, l in enumerate(L):
        if inside[i]:
            continue
        s = re.sub(r"^(?:>\s*)*", "", l)
        if "|" in s:
            grp.append((i + 1, s))
        elif grp:
            flush()
    flush()

    print(f"errores: {len(bad)} | avisos: {len(warn)}")
    for b in bad[:30]:
        print("  ERR ", b)
    for w in warn[:15]:
        print("  AVISO", w)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
