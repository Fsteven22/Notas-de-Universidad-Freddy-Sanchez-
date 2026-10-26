import argparse, os, io
import pymupdf

# Extrae el texto de todos los PDFs de una carpeta a *.txt y genera un
# inventario (paginas, chars, encabezado) para leer contenido sin abrir PDFs.
# Uso:  python pdf_a_texto.py "<carpeta-de-pdfs>"
# Salida: <carpeta>/_texto/*.pdf.txt y _texto/_inventario.txt

ap = argparse.ArgumentParser()
ap.add_argument("carpeta")
args = ap.parse_args()

src = args.carpeta
out = os.path.join(src, "_texto")
os.makedirs(out, exist_ok=True)

inv = []
for f in sorted(os.listdir(src)):
    if not f.lower().endswith(".pdf"):
        continue
    p = os.path.join(src, f)
    try:
        doc = pymupdf.open(p)
        npag = doc.page_count
        txt = "\n".join(pg.get_text() for pg in doc)
        doc.close()
        io.open(os.path.join(out, f + ".txt"), "w", encoding="utf-8").write(txt)
        lines = [l.strip() for l in txt.splitlines() if l.strip()]
        inv.append("%-56s p%-3d %7d ch  %s" % (f, npag, len(txt), " // ".join(lines[:3])[:150]))
    except Exception as ex:
        inv.append("%-56s FAIL %r" % (f, ex))

io.open(os.path.join(out, "_inventario.txt"), "w", encoding="utf-8").write("\n".join(inv))
print("pdfs=%d -> %s" % (len(inv), out))
