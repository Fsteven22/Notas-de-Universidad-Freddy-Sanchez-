import argparse, os, re, sys, collections

# Detecta y repara mojibake (doble codificacion UTF-8) en las notas .md del vault.
#
# Metodo: cada "run" de caracteres altos suspicious (latin-1 / cp1252) se intenta
# decodificar de vuelta a UTF-8. Solo se reescribe el run si el roundtrip produce
# texto valido Y el run originalizia con el patron tipico de mojibake
# (primer byte UTF-8 mal decodificado: 'a', 'A', U+00C2, U+00C3, U+00E2, U+00F0).
# Nunca toca acentos legitimos ni texto ya correcto.
#
# Uso:
#   python qa_mojibake.py "<carpeta-vault>" --check
#       (solo reporta: cantidad de runs por nota; NO escribe)
#   python qa_mojibake.py "<carpeta-vault>" --fix
#       (repara en el sitio, con verificacion byte a byte del esqueleto ASCII)
#   python qa_mojibake.py "<carpeta-vault>" --fix -o reporte.txt
#       (ademas deja el detalle en el reporte)

AP = argparse.ArgumentParser()
AP.add_argument("root")
AP.add_argument("--check", action="store_true", help="solo reporta, no escribe")
AP.add_argument("--fix", action="store_true", help="repara los runs detectados")
AP.add_argument("-o", default=None, help="archivo de reporte con el detalle")
args = AP.parse_args()

if not (args.check or args.fix):
    print("ERROR: indica --check (solo reporta) o --fix (repara)")
    sys.exit(2)

# codec hibrido: cp1252 para los chars mapeados, latin-1 para el resto (<256)
CP1252 = {}
for _b in range(256):
    try:
        CP1252[bytes([_b]).decode("cp1252")] = _b
    except UnicodeDecodeError:
        pass


def a_bytes(s):
    """Codifica un string a bytes con cp1252/latin-1; None si hay chars > 255."""
    out = bytearray()
    for c in s:
        if c in CP1252:
            out.append(CP1252[c])
        elif ord(c) < 256:
            out.append(ord(c))
        else:
            return None
    return bytes(out)


# run de chars altos (los que aparecen al decodificar mal UTF-8)
ALTOS = re.compile(
    r"[\u0080-\u00ff\u0152\u0153\u0160\u0161\u0178\u017d\u017e\u0192\u02c6\u02dc"
    r"\u2013\u2014\u2018\u2019\u201a\u201c\u201d\u201e\u2026\u2030\u2039\u203a\u20ac\u2122]+"
)
# primer byte de una secuencia UTF-8 mal decodificada
INICIO = re.compile(r"^[\u00c2\u00c3\u00e2\u00f0A]")


def reparar_texto(texto):
    """Devuelve (texto_reparado, n_runs)."""
    n = 0

    def fix(m):
        nonlocal n
        run = m.group(0)
        if not INICIO.match(run) or len(run) < 2:
            return run
        cur = run
        for _ in range(4):
            b = a_bytes(cur)
            if b is None:
                break
            try:
                # solo si el roundtrip es reversible y produce texto valido
                f = b.decode("utf-8")
            except UnicodeDecodeError:
                break
            if f == cur:
                break
            cur = f
        if cur != run:
            n += 1
        return cur

    return ALTOS.sub(fix, texto), n


def ascii_only(t):
    """Texto ASCII puro (sin los chars no-ASCII). Debe ser IDENTICO antes y
    despues de reparar: la reparacion solo cambia chars no-ASCII por otros
    no-ASCII, nunca agrega ni borra texto legible."""
    return "".join(ch for ch in t if ord(ch) < 128)


def solo_sospechosos(viejo):
    """True si el tramo modificado tenia chars altos (marca de mojibake)."""
    return bool(re.search(r"[\u0080-\u00ff\u2013-\u201f\u2026\u20ac\u2122]", viejo))


def main():
    notas = []
    for dp, ds, fs in os.walk(args.root):
        ds[:] = [d for d in ds if d not in (".obsidian", ".trash", ".git", "node_modules", "_texto")]
        for f in fs:
            if f.lower().endswith(".md"):
                notas.append(os.path.join(dp, f))
    notas.sort()

    detalle = []
    totales = collections.Counter()
    reparados = 0

    for p in notas:
        raw = open(p, "rb").read()
        try:
            t = raw.decode("utf-8")
        except UnicodeDecodeError as e:
            detalle.append("SKIP (no es UTF-8 valido): %s -> %s" % (p, e))
            totales["no_utf8"] += 1
            continue
        nuevo, n = reparar_texto(t)
        if not n:
            continue
        totales["notas_con_runs"] += 1
        totales["runs"] += n
        detalle.append("%s: %d run(s)" % (os.path.relpath(p, args.root), n))
        if args.fix:
            # 1) el texto ASCII no puede cambiar (no se agrega ni se borra letra)
            if ascii_only(t) != ascii_only(nuevo):
                detalle[-1] += "  [SALTADO: el texto ASCII cambio]"
                totales["saltados"] += 1
                continue
            # 2) cada tramo modificado debe tener chars altos sospechosos
            import difflib
            malo = None
            for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, t, nuevo, autojunk=False).get_opcodes():
                if tag != "equal" and not solo_sospechosos(t[i1:i2]):
                    malo = t[i1:i2]
                    break
            if malo is not None:
                detalle[-1] += "  [SALTADO: tramo no sospechoso %r]" % (malo[:40],)
                totales["saltados"] += 1
                continue
            with open(p, "wb") as f:
                f.write(nuevo.encode("utf-8"))
            reparados += n

    modo = "FIX" if args.fix else "CHECK"
    lineas = []
    lineas.append("qa_mojibake (%s) - root=%s" % (modo, os.path.abspath(args.root)))
    lineas.append("notas revisadas: %d" % len(notas))
    lineas.append("notas con mojibake: %d | runs detectados: %d" % (totales["notas_con_runs"], totales["runs"]))
    if args.fix:
        lineas.append("runs reparados: %d | saltados por esqueleto ASCII: %d" % (reparados, totales["saltados"]))
    if totales["no_utf8"]:
        lineas.append("notas no-UTF8 (saltadas): %d" % totales["no_utf8"])
    lineas.append("")
    lineas.extend(detalle)
    reporte = "\n".join(lineas)
    if args.o:
        with open(args.o, "w", encoding="utf-8", newline="") as f:
            f.write(reporte + "\n")
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    print(reporte)
    return 0


if __name__ == "__main__":
    sys.exit(main())
