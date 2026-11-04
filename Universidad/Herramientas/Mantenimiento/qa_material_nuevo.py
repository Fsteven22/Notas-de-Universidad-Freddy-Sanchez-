import argparse, os, re, sys, hashlib, csv, io

# Detector de material nuevo en carpetas monitorizadas del vault (carril D1).
#
# Mantiene un "baseline" (snapshot) con la ruta, el sha256 y el tamano de cada
# archivo de las carpetas vigiladas. Luego permite comparar el estado actual
# contra ese baseline para detectar:
#   - NUEVOS      : archivos que el owner ingreso y no estan en el baseline
#   - MODIFICADOS : archivos con contenido distinto (sha256 cambiado)
#   - ELIMINADOS  : archivos que estaban en el baseline y ya no estan
#
# Uso:
#   python qa_material_nuevo.py --baseline baseline.csv --carpetas "<ruta1>" "<ruta2>"
#   python qa_material_nuevo.py --check baseline.csv
#   python qa_material_nuevo.py --check baseline.csv --actualizar
#
# Las rutas son relativas a la raiz del vault (la carpeta que contiene
# "Universidad"). El CSV tiene cabecera:
#   carpeta,ruta,sha256,bytes
# "carpeta" es la carpeta vigilada (relativa al vault), "ruta" es relativa a esa.

AP = argparse.ArgumentParser()
AP.add_argument("--root", default=".", help="raiz del vault (donde vive 'Universidad')")
AP.add_argument("--baseline", required=True, help="ruta del CSV snapshot")
AP.add_argument("--carpetas", nargs="*", default=None,
                help="carpetas a vigilar (relativas al root). Sin este argumento y sin "
                     "--baseline previo, usa las 5 carpetas U0 de 3er Semestre.")
AP.add_argument("--check", action="store_true", help="compara el disco contra el baseline")
AP.add_argument("--actualizar", action="store_true",
                help="reescribe el baseline con el estado actual (usar solo tras revisar)")
AP.add_argument("-o", default=None, help="reporte de texto (los detalles van aqui)")
args = AP.parse_args()

ROOT = os.path.abspath(args.root)

DEFAULT_CARPETAS = [
    r"Universidad\3er Semestre\Diseño de Software\Unidad 0 - Guias y Ejercicios",
    r"Universidad\3er Semestre\Fundamentos de Electricidad y Sistemas Digitales\Unidad 0 - Guias y Ejercicios",
    r"Universidad\3er Semestre\Ingles III\Unidad 0 - Guias y Ejercicios",
    r"Universidad\3er Semestre\Matemáticas Discretas\Unidad 0 - Guias y Ejercicios",
    r"Universidad\3er Semestre\Sistema de Bases de Datos\Unidad 0 - Guias y Ejercicios",
]

SKIP_DIRS = {".obsidian", ".trash", ".git", "node_modules", "_texto"}


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def escanear(carpeta_rel):
    """Devuelve {ruta_rel: (sha256, bytes)} de los archivos de la carpeta vigilada."""
    base = os.path.join(ROOT, carpeta_rel)
    out = {}
    if not os.path.isdir(base):
        return out
    for dp, ds, fs in os.walk(base):
        ds[:] = sorted(d for d in ds if d not in SKIP_DIRS)
        for f in sorted(fs):
            full = os.path.join(dp, f)
            if not os.path.isfile(full):
                continue
            rel = os.path.relpath(full, base).replace(os.sep, "/")
            try:
                out[rel] = (sha256(full), os.path.getsize(full))
            except OSError:
                pass
    return out


def leer_baseline(path):
    """{carpeta: {ruta: (sha256, bytes)}}"""
    data = {}
    if not os.path.exists(path):
        return data
    with io.open(path, encoding="utf-8", newline="") as f:
        for fila in csv.DictReader(f):
            data.setdefault(fila["carpeta"], {})[fila["ruta"]] = (fila["sha256"], int(fila["bytes"]))
    return data


def escribir_baseline(path, estado):
    carpeta = os.path.dirname(os.path.abspath(path))
    if carpeta and not os.path.isdir(carpeta):
        os.makedirs(carpeta)
    with io.open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["carpeta", "ruta", "sha256", "bytes"])
        for carpeta_rel in sorted(estado):
            for ruta in sorted(estado[carpeta_rel]):
                sha, nbytes = estado[carpeta_rel][ruta]
                w.writerow([carpeta_rel.replace(os.sep, "/"), ruta, sha, nbytes])


def main():
    base = leer_baseline(args.baseline)
    carpetas = args.carpetas

    if args.check:
        if not base:
            print("ERROR: no existe el baseline '%s' (usa --baseline para crearlo)" % args.baseline)
            return 2
        # si se pasan carpetas extra, se agregan al universo vigilado
        for c in (carpetas or []):
            base.setdefault(c, {})
        nuevas, modificados, eliminados = [], [], []
        total_actual = 0
        for carpeta_rel, snap in sorted(base.items()):
            actual = escanear(carpeta_rel)
            total_actual += len(actual)
            for ruta, (sha, nbytes) in sorted(actual.items()):
                if ruta not in snap:
                    nuevas.append((carpeta_rel, ruta, nbytes))
                elif snap[ruta][0] != sha:
                    modificados.append((carpeta_rel, ruta, snap[ruta][1], nbytes))
            for ruta in sorted(snap):
                if ruta not in actual:
                    eliminados.append((carpeta_rel, ruta, snap[ruta][1]))
        lineas = []
        lineas.append("carril D1 - material nuevo")
        lineas.append("baseline: %s" % args.baseline)
        lineas.append("carpetas vigiladas: %d | archivos en baseline: %d | archivos en disco: %d"
                      % (len(base), sum(len(v) for v in base.values()), total_actual))
        lineas.append("")
        lineas.append("NUEVOS: %d" % len(nuevas))
        for c, r, n in nuevas:
            lineas.append("  + [%s] %s (%d bytes)" % (c, r, n))
        lineas.append("MODIFICADOS: %d" % len(modificados))
        for c, r, antes, ahora in modificados:
            lineas.append("  ~ [%s] %s (%d -> %d bytes)" % (c, r, antes, ahora))
        lineas.append("ELIMINADOS: %d" % len(eliminados))
        for c, r, n in eliminados:
            lineas.append("  - [%s] %s (%d bytes)" % (c, r, n))
        reporte = "\n".join(lineas)
        if args.o:
            with io.open(args.o, "w", encoding="utf-8", newline="") as f:
                f.write(reporte + "\n")
        sys.stdout.write(reporte + "\n")
        if args.actualizar:
            estado = {c: escanear(c) for c in base}
            escribir_baseline(args.baseline, estado)
            print("\nbaseline actualizado: %s" % args.baseline)
        return 0

    # modo --baseline
    carpetas = carpetas or DEFAULT_CARPETAS
    estado = {}
    for carpeta_rel in carpetas:
        estado[carpeta_rel] = escanear(carpeta_rel)
    escribir_baseline(args.baseline, estado)
    total = sum(len(v) for v in estado.values())
    print("baseline escrito: %s" % args.baseline)
    for c in sorted(estado):
        print("  %-95s %4d archivos" % (c, len(estado[c])))
    print("total: %d archivos en %d carpetas" % (total, len(estado)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
