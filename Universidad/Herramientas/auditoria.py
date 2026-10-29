#!/usr/bin/env python3
"""Reusable vault-audit script for Obsidian-style Markdown vaults (stdlib only).

Scans all *.md under vault root (argv[1] or default) and reports:
 1. Broken wikilinks [[target]] / [[target|alias]] / [[target#sec]]
 2. Broken embeds ![[file.png/jpg/pdf]]
 3. Bracket-less embeds: lines exactly `!name.png` (optional `> ` prefix)
 4. Unbalanced ``` fences + mismatched fence quoting (> ``` vs ```)
 5. Mermaid violations inside ```mermaid blocks: style lines, <br/>/<br>
 6. Table pipe mismatches (rows vs header, ignoring escaped \\|)
 7. Odd `$` counts per line outside fences (excluding $$ pairs and \\$)
 8. Unbalanced [[ vs ]] per line

Output: per-check summary + file:line details (capped at 20 per check).
Handles UTF-8, long Windows paths, missing-file errors gracefully.
"""
import os
import re
import sys
from pathlib import Path

def _raiz_por_defecto():
    """Deduce la raiz del vault desde la ubicacion de este script."""
    aqui = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(aqui))  # Herramientas/ -> Universidad/ -> OneSyncFiles/


DEFAULT_VAULT = os.environ.get("VAULT_ROOT") or _raiz_por_defecto()
DETAIL_CAP = 20
NEARDUP_MIN_RATIO = 0.93
STUB_MAX_BODY = 1200

WIKILINK_RE = re.compile(r"(?<!\!)(\[\[([^\[\]\n]+?)\]\])")
EMBED_RE = re.compile(r"!\[\[([^\[\]\n]+?)\]\]")
# Bracket-less embed: whole line is !name.ext, optional "> " callout prefix, image/pdf ext
BRACKETLESS_RE = re.compile(
    r"^\s*(?:>\s*)*![^\[\]\n\(\)]*?\.(?:png|jpe?g|gif|webp|svg|bmp|ico|tiff?|pdf)\s*$",
    re.IGNORECASE,
)
# Fence: optional leading spaces, optional "> " quoting, then ```
FENCE_RE = re.compile(r"^\s*(?P<quote>>\s*)?```(?P<info>.*)$")
STYLE_RE = re.compile(r"^\s*style\b", re.IGNORECASE)
BR_RE = re.compile(r"<br\s*/?>", re.IGNORECASE)

SKIP_WIKILINK_EXTS = (
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp",
    ".ico", ".tif", ".tiff", ".pdf", ".mp4", ".mov", ".mp3",
    ".wav", ".ogg", ".zip", ".excalidraw",
)


def count_pipes(line: str) -> int:
    """Count unescaped pipes (ignore \\|)."""
    return line.replace("\\|", "").count("|")


def is_separator_row(line: str) -> bool:
    s = line.strip()
    if "|" not in s or "-" not in s:
        return False
    tmp = s.replace("|", "").replace(":", "").replace("-", "").replace(" ", "")
    return tmp == ""


def has_odd_dollar(line: str) -> bool:
    tmp = line.replace("\\$", "")
    tmp = tmp.replace("$$", "")
    return tmp.count("$") % 2 == 1


def open_text_long(path_str: str):
    """Open UTF-8 text, retrying with extended-length prefix on Windows."""
    try:
        return open(path_str, "r", encoding="utf-8", errors="replace")
    except OSError:
        if os.name == "nt" and not path_str.startswith("\\\\?\\"):
            try:
                ext = "\\\\?\\" + os.path.abspath(path_str)
                return open(ext, "r", encoding="utf-8", errors="replace")
            except OSError:
                raise
        raise


def collect_files(vault: Path):
    md_paths = []
    md_stems = set()      # lower stems, e.g. "nota"
    all_names = set()     # lower basenames of ALL files, e.g. "img.png"
    try:
        walker = os.walk(vault, onerror=lambda e: None, followlinks=False)
        for root, dirs, files in walker:
            try:
                for fn in files:
                    try:
                        low = fn.lower()
                        all_names.add(low)
                        if low.endswith(".md"):
                            full = os.path.join(root, fn)
                            md_paths.append(full)
                            md_stems.add(os.path.splitext(fn)[0].lower())
                    except Exception:
                        continue
            except Exception:
                continue
    except Exception:
        pass
    return md_paths, md_stems, all_names


def basename_of(target: str) -> str:
    t = target.replace("\\", "/")
    return t.rsplit("/", 1)[-1].strip()


def main() -> int:
    try:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
    vault_str = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_VAULT
    vault = Path(vault_str)
    print(f"Vault: {vault}")
    if not vault.exists():
        print(f"ERROR: vault root does not exist: {vault}")
        return 2

    md_paths, md_stems, all_names = collect_files(vault)
    print(f"Files scanned (*.md): {len(md_paths)}")

    # totals + capped details
    c1_total = c2_total = c3_total = c4_total = c5_total = c6_total = c7_total = c8_total = 0
    c9_total = c10_total = c11_total = c12_total = 0
    c1_det, c2_det, c3_det, c4_det, c5_det, c6_det, c7_det, c8_det = ([] for _ in range(8))
    c9_det, c10_det, c11_det, c12_det = ([] for _ in range(4))

    bodies: dict[str, list] = {}   # md5 -> [(rel, h1, body_text, size)]
    h1_groups: dict[tuple, list] = {}  # (h1, size_bucket) -> [(rel, body_text)]

    def add(det, total_box, s):
        # helper inlined manually below for speed; kept for clarity
        return total_box

    for full in md_paths:
        try:
            rel = os.path.relpath(full, str(vault))
        except Exception:
            rel = os.path.basename(full)
        # read lines
        try:
            with open_text_long(full) as f:
                text_full = f.read()
            lines = text_full.splitlines()
        except Exception:
            continue

        # 12. doble CR en bytes crudos (\r\r\n, firma de reescrituras corruptas)
        try:
            with open(full, "rb") as bf:
                raw = bf.read()
            n_crcr = raw.count(b"\r\r")
            if n_crcr:
                c12_total += n_crcr
                if len(c12_det) < DETAIL_CAP:
                    c12_det.append(f"{rel}: {n_crcr} secuencia(s) \\r\\r")
        except Exception:
            pass

        # cuerpo sin frontmatter + H1 (para 10/11, duplicados y cruzado)
        body_lines = lines
        h1 = ""
        if lines and lines[0].strip() == "---":
            try:
                close = next(i for i in range(1, min(len(lines), 20)) if lines[i].strip() == "---")
                body_lines = lines[close + 1:]
            except StopIteration:
                pass
        for bl in body_lines:
            if bl.startswith("# "):
                h1 = bl.strip()
                break
        body_text = "\n".join(body_lines)
        try:
            import hashlib
            digest = hashlib.md5(body_text.encode("utf-8", "replace")).hexdigest()
        except Exception:
            digest = ""
        if digest:
            bodies.setdefault(digest, []).append((rel, h1, body_text, len(body_text)))
            key = (h1[:80], len(body_text) // 700)
            if h1:
                h1_groups.setdefault(key, []).append((rel, body_text))

        # 9. doble `tags:` en la cabecera (firma del incidente 19/10)
        tag_positions = [i for i, l in enumerate(lines[:16], 1) if l.strip().startswith("tags:")]
        if len(tag_positions) > 1:
            c9_total += len(tag_positions) - 1
            if len(c9_det) < DETAIL_CAP:
                c9_det.append(f"{rel}: {len(tag_positions)} lineas tags: en L{tag_positions}")

        fence_entries = []  # (lineno, quoted, info)
        in_fence = False
        in_mermaid = False
        table_group = []  # list of (lineno, line)

        def flush_table():
            nonlocal c6_total
            if len(table_group) < 2:
                table_group.clear()
                return
            first_stripped = re.sub(r"^(?:>\s*)*", "", table_group[0][1]).lstrip()
            if not first_stripped.startswith("|"):
                # list items with | (e.g. `- a || b`) are not tables
                table_group.clear()
                return
            # find separator to confirm it's a table
            has_sep = any(is_separator_row(ln) for _, ln in table_group)
            if not has_sep:
                # still check vs first row? Only report if clearly table-like:
                # require first row to start/end with | or >=2 pipes. Otherwise skip.
                first = table_group[0][1]
                if count_pipes(first) < 2:
                    table_group.clear()
                    return
            header_count = count_pipes(table_group[0][1])
            header_ln = table_group[0][0]
            for ln_no, ln in table_group[1:]:
                if is_separator_row(ln):
                    continue
                n = count_pipes(ln)
                if n != header_count:
                    c6_total += 1
                    if len(c6_det) < DETAIL_CAP:
                        c6_det.append(
                            f"{rel}:{ln_no}: pipes {n} != header({header_ln}) {header_count}: {ln.strip()[:160]}"
                        )
            table_group.clear()

        for idx, line in enumerate(lines, start=1):
            m_fence = FENCE_RE.match(line)
            if m_fence:
                quoted = m_fence.group("quote") is not None
                info = (m_fence.group("info") or "").strip()
                fence_entries.append((idx, quoted, info))
                # entering or leaving fence?
                if not in_fence:
                    # opening
                    in_fence = True
                    in_mermaid = info.lower().startswith("mermaid")
                    flush_table()
                else:
                    # closing
                    in_fence = False
                    in_mermaid = False
                continue

            if in_fence:
                if in_mermaid:
                    if STYLE_RE.match(line):
                        c5_total += 1
                        if len(c5_det) < DETAIL_CAP:
                            c5_det.append(f"{rel}:{idx}: `style` directive: {line.strip()[:160]}")
                    # NOTE: <br/> is valid mermaid line-break syntax (mmdc renders
                    # it); it is intentionally NOT flagged.
                continue

            # ---- outside fences ----
            # 1. wikilinks (skip embeds via lookbehind)
            try:
                for m in WIKILINK_RE.finditer(line):
                    inner = m.group(2)
                    tgt = inner.split("|", 1)[0].split("#", 1)[0].strip()
                    if not tgt:
                        continue
                    if "://" in tgt:
                        continue
                    low = tgt.lower()
                    if low.endswith(SKIP_WIKILINK_EXTS):
                        continue
                    base = basename_of(tgt)
                    if "." in base:
                        # file with extension: check against ALL vault files
                        if base.lower() not in all_names:
                            c1_total += 1
                            if len(c1_det) < DETAIL_CAP:
                                c1_det.append(f"{rel}:{idx}: [[{inner}]] -> ?{base}?")
                        continue
                    if low.endswith(".md"):
                        tgt = tgt[: -len(".md")]
                    base = basename_of(tgt)
                    if not base:
                        continue
                    if base.lower() not in md_stems:
                        c1_total += 1
                        if len(c1_det) < DETAIL_CAP:
                            c1_det.append(f"{rel}:{idx}: [[{inner}]] -> ?{base}?")
            except Exception:
                pass

            # 2. broken embeds ![[...]]
            try:
                for m in EMBED_RE.finditer(line):
                    inner = m.group(1)
                    tgt = inner.split("|", 1)[0].split("#", 1)[0].strip()
                    if not tgt or "://" in tgt:
                        continue
                    base = basename_of(tgt)
                    if not base:
                        continue
                    if "." in base:
                        if base.lower() not in all_names:
                            c2_total += 1
                            if len(c2_det) < DETAIL_CAP:
                                c2_det.append(f"{rel}:{idx}: ![[{inner}]] missing file `{base}`")
                    else:
                        if base.lower() not in md_stems:
                            c2_total += 1
                            if len(c2_det) < DETAIL_CAP:
                                c2_det.append(f"{rel}:{idx}: ![[{inner}]] missing note `{base}`")
            except Exception:
                pass

            # 3. bracket-less embeds
            try:
                if line.lstrip().startswith("!") or line.lstrip().startswith(">"):
                    if BRACKETLESS_RE.match(line):
                        # exclude markdown image ![..](..) and wikilink embeds (start with ![)
                        s = line.strip()
                        s2 = re.sub(r"^(?:>\s*)*", "", s)
                        if not s2.startswith("!["):
                            c3_total += 1
                            if len(c3_det) < DETAIL_CAP:
                                c3_det.append(f"{rel}:{idx}: {s[:160]}")
            except Exception:
                pass

            # 7. odd $
            try:
                if "$" in line and has_odd_dollar(line):
                    c7_total += 1
                    if len(c7_det) < DETAIL_CAP:
                        c7_det.append(f"{rel}:{idx}: {line.strip()[:160]}")
            except Exception:
                pass

            # 8. unbalanced [[ vs ]]
            try:
                if "[[" in line or "]]" in line:
                    o, c = line.count("[["), line.count("]]")
                    if o != c:
                        c8_total += 1
                        if len(c8_det) < DETAIL_CAP:
                            c8_det.append(f"{rel}:{idx}: [[x{o} ]]x{c}: {line.strip()[:160]}")
            except Exception:
                pass

            # 6. accumulate table rows
            try:
                if "|" in line:
                    table_group.append((idx, line))
                else:
                    if table_group:
                        flush_table()
            except Exception:
                pass

        # end of file
        try:
            if table_group:
                flush_table()
        except Exception:
            pass
        # 4. fences
        try:
            if len(fence_entries) % 2 == 1:
                c4_total += 1
                if len(c4_det) < DETAIL_CAP:
                    c4_det.append(f"{rel}: unbalanced ``` count={len(fence_entries)} (lines {[e[0] for e in fence_entries][:10]})")
            for i in range(0, len(fence_entries) - 1, 2):
                a, b = fence_entries[i], fence_entries[i + 1]
                if a[1] != b[1]:
                    c4_total += 1
                    if len(c4_det) < DETAIL_CAP:
                        qa = "> ```" if a[1] else "```"
                        qb = "> ```" if b[1] else "```"
                        c4_det.append(
                            f"{rel}:{a[0]}-{b[1]}: fence quoting mismatch open({qa} `{a[2][:30]}`) vs close({qb} `{b[2][:30]}`)"
                        )
        except Exception:
            pass

    # 10. cuerpos idénticos (notas clonadas: el stub de otro archivo)
    for digest, grupo in bodies.items():
        if len(grupo) > 1:
            c10_total += len(grupo) - 1
            rels = [g[0] for g in grupo[:4]]
            if len(c10_det) < DETAIL_CAP * 4:
                c10_det.append(f"cuerpo {digest[:8]} compartido por: {', '.join(rels)}")

    # 11. cuerpos casi idénticos (contenido cruzado tipo incidente 19/10)
    try:
        import difflib
    except Exception:
        difflib = None
    for key, grupo in h1_groups.items():
        if len(grupo) < 2 or difflib is None:
            continue
        for i in range(len(grupo) - 1):
            for j in range(i + 1, len(grupo)):
                r = difflib.SequenceMatcher(None, grupo[i][1], grupo[j][1]).quick_ratio()
                if r < NEARDUP_MIN_RATIO:
                    continue
                r = difflib.SequenceMatcher(None, grupo[i][1], grupo[j][1]).ratio()
                if r >= NEARDUP_MIN_RATIO:
                    c11_total += 1
                    if len(c11_det) < DETAIL_CAP:
                        c11_det.append(f"{grupo[i][0]} ~ {grupo[j][0]} (sim {r:.3f})")

    checks = [
        ("1. Broken wikilinks [[target]] (by .md basename, images skipped)", c1_total, c1_det),
        ("2. Broken embeds ![[file]] (by filename vault-wide)", c2_total, c2_det),
        ("3. Bracket-less embeds `!name.png` lines (won't render)", c3_total, c3_det),
        ("4. Unbalanced/mismatched ``` fences", c4_total, c4_det),
        ("5. Mermaid violations (`style` lines, <br>)", c5_total, c5_det),
        ("6. Table pipe mismatches vs header (ignoring \\|)", c6_total, c6_det),
        ("7. Odd `$` per line outside fences ($$ and \\$ excluded)", c7_total, c7_det),
        ("8. Unbalanced [[ vs ]] per line", c8_total, c8_det),
        ("9. Multiple/frontmatter-extra tags: lines per file", c9_total, c9_det),
        ("10. Note bodies duplicated exactly (clones/stubs)", c10_total, c10_det),
        ("11. Near-duplicate bodies >=0.93 (contenido cruzado)", c11_total, c11_det),
        ("12. Double-CR byte sequences \\r\\r (endings corruptos)", c12_total, c12_det),
    ]
    print("=" * 72)
    for title, total, det in checks:
        print(f"{title}: {total} (showing up to {DETAIL_CAP})")
        for d in det:
            print(f"  {d}")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
