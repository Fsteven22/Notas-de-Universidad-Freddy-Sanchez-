import argparse, os, re, io, json

import pymupdf

# pdf_a_markdown_lote.py — extrae el texto de PDFs a Markdown, en lote.
#
# Recorre el vault, encuentra los PDFs que viven dentro de una carpeta con
# cierto nombre (por ejemplo "Unidad 0 - Guias y Ejercicios") y escribe un
# .md por PDF, con separadores de pagina. No escribe DENTRO del vault: la
# salida va a una carpeta externa, para no ensuciar el repo.
#
# Uso:
#   py pdf_a_markdown_lote.py --salida "C:\tmp\pdf_md" --carpeta "Unidad 0 - Guias y Ejercicios"
#   py pdf_a_markdown_lote.py --salida "C:\tmp\pdf_md" --scope "Universidad/2do Semestre/Comunicacion"
#
# La raiz del vault se deduce de la ubicacion de este script
# (<vault>/Universidad/Herramientas/Mantenimiento/este_script.py), asi no hay que pasar
# rutas con acentos por linea de comandos. Si se pasa --root, manda ese.

SKIP = (".obsidian", ".trash", ".git", "node_modules")
EXT = ".pdf"


def raiz_por_defecto():
    aqui = os.path.dirname(os.path.abspath(__file__))
    # vault/Universidad/Herramientas/Mantenimiento/este_script.py -> vault
    return os.path.dirname(os.path.dirname(os.path.dirname(aqui)))


def limpiar(nombre):
    nombre = re.sub(r"[\\/]+", "__", nombre)
    nombre = re.sub(r"[^0-9A-Za-z._()\- áéíóúñÁÉÍÓÚÑ]+", "", nombre)
    return nombre.strip()[:140] or "pdf"


def buscar_pdfs(root, scope, carpeta):
    base = os.path.join(root, scope) if scope else root
    encontrados = []
    for dp, ds, fs in os.walk(base):
        ds[:] = [d for d in ds if d not in SKIP]
        if carpeta and os.path.basename(dp) != carpeta:
            continue
        for f in fs:
            if f.lower().endswith(EXT):
                encontrados.append(os.path.join(dp, f))
    encontrados.sort()
    return encontrados


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None, help="raiz del vault (default: deducida)")
    ap.add_argument("--scope", default="", help="subcarpeta del vault a recorrer")
    ap.add_argument("--carpeta", default="", help="solo PDFs dentro de carpetas con este nombre")
    ap.add_argument("--salida", required=True, help="carpeta donde escribir los .md")
    ap.add_argument("--reporte", default=None, help="archivo JSON con el inventario")
    ap.add_argument("--min-chars", type=int, default=100, help="chars minimos para no marcarlo escaneado")
    args = ap.parse_args()

    root = os.path.abspath(args.root) if args.root else raiz_por_defecto()
    if not os.path.isdir(root):
        print("root no existe: %s" % root)
        return 2

    pdfs = buscar_pdfs(root, args.scope, args.carpeta)
    os.makedirs(args.salida, exist_ok=True)

    filas = []
    escaneados = 0
    for pdf in pdfs:
        rel = os.path.relpath(pdf, root)
        partes = rel.split(os.sep)
        prefijo = "__".join(limpiar(p) for p in partes[:-1])
        nombre = prefijo + "__" + limpiar(os.path.splitext(partes[-1])[0]) + ".md"
        destino = os.path.join(args.salida, nombre)
        try:
            doc = pymupdf.open(pdf)
            paginas = []
            chars = 0
            for i, page in enumerate(doc):
                txt = page.get_text("text").strip()
                chars += len(txt)
                paginas.append("## Pagina %d\n\n%s" % (i + 1, txt))
            doc.close()
            cabecera = "# %s\n\n_Origen: %s_\n_Paginas: %d_\n\n" % (
                os.path.basename(pdf), rel, len(paginas))
            io.open(destino, "w", encoding="utf-8", newline="\n").write(
                cabecera + "\n\n---\n\n".join(paginas))
            escaneado = chars < args.min_chars
            escaneados += 1 if escaneado else 0
            filas.append({
                "pdf": rel, "paginas": len(paginas), "chars": chars,
                "escaneado": escaneado, "salida": nombre,
            })
        except Exception as ex:
            filas.append({"pdf": rel, "error": repr(ex)})

    if args.reporte:
        io.open(args.reporte, "w", encoding="utf-8", newline="\n").write(
            json.dumps(filas, ensure_ascii=False, indent=2))

    print("pdfs=%d  escaneados=%d  salida=%s" % (len(pdfs), escaneados, args.salida))
    if args.reporte:
        print("reporte=%s" % args.reporte)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
