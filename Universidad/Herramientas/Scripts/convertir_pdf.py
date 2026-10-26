#!/usr/bin/env python3
"""Convierte PDF a Markdown con OCR opcional (Windows, sin Poppler).

Motores:
  markitdown   -> capa de texto real (rapido, sin OCR).
  pymupdf4llm  -> texto con layout + OCR automatico en paginas escaneadas.
  manual       -> OCR por pagina con PyMuPDF + pytesseract (ultimo recurso).

Uso:
  py convertir_pdf.py entrada.pdf
  py convertir_pdf.py entrada.pdf -o salida.md
  py convertir_pdf.py entrada.pdf --split
  py convertir_pdf.py entrada.pdf --motor manual --lang spa+eng

Requisito de OCR: Tesseract en PATH o en C:\\Program Files\\Tesseract-OCR con
el paquete spa (spa.traineddata). Poppler NO es necesario.
"""
import argparse
import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

TESSERACT_CANDIDATES = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
]
SEP = re.compile(r"^---\s*end of page")


def configurar_tesseract():
    exe = shutil.which("tesseract")
    if exe is None:
        for candidato in TESSERACT_CANDIDATES:
            if Path(candidato).is_file():
                exe = candidato
                break
    if exe is None:
        return None
    exe_dir = str(Path(exe).parent)
    os.environ["PATH"] = exe_dir + os.pathsep + os.environ.get("PATH", "")
    tessdata = Path(exe_dir) / "tessdata"
    if tessdata.is_dir() and not os.environ.get("TESSDATA_PREFIX"):
        os.environ["TESSDATA_PREFIX"] = str(tessdata)
    try:
        import pytesseract

        pytesseract.pytesseract.tesseract_cmd = exe
    except ImportError:
        pass
    return exe


def paginas_con_texto(pdf):
    import pymupdf

    total = 0
    con_texto = 0
    with pymupdf.open(pdf) as doc:
        total = doc.page_count
        for page in doc:
            if page.get_text().strip():
                con_texto += 1
    return total, con_texto


def convertir_pymupdf4llm(pdf, lang):
    import pymupdf4llm

    return pymupdf4llm.to_markdown(
        str(pdf),
        use_ocr=True,
        ocr_language=lang,
        page_separators=True,
        show_progress=True,
    )


def convertir_markitdown(pdf):
    from markitdown import MarkItDown

    return MarkItDown().convert(str(pdf)).text_content


def ocr_manual(pdf, lang):
    from PIL import Image
    import pymupdf
    import pytesseract

    partes = []
    with pymupdf.open(pdf) as doc:
        for indice, page in enumerate(doc, start=1):
            pix = page.get_pixmap(dpi=300)
            imagen = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            texto = pytesseract.image_to_string(imagen, lang=lang).strip()
            partes.append(f"## Página {indice}\n\n{texto}")
    return "\n\n---\n\n".join(partes)


def escribir_split(markdown, destino):
    carpeta = destino.with_suffix("")
    carpeta.mkdir(exist_ok=True)
    secciones = []
    actual = []
    numero = 0
    for linea in markdown.splitlines():
        if SEP.match(linea):
            numero += 1
            secciones.append((numero, "\n".join(actual).strip()))
            actual = []
            continue
        actual.append(linea)
    if actual and "\n".join(actual).strip():
        numero += 1
        secciones.append((numero, "\n".join(actual).strip()))
    for indice, texto in secciones:
        archivo = carpeta / f"pagina-{indice:04d}.md"
        archivo.write_text(texto, encoding="utf-8")
    return carpeta, len(secciones)


def main():
    parser = argparse.ArgumentParser(
        description="Convierte PDF a Markdown. Usa PyMuPDF4LLM (texto y OCR con Tesseract), sin depender de Poppler."
    )
    parser.add_argument("pdf", type=Path, help="PDF de entrada")
    parser.add_argument("-o", "--salida", type=Path, default=None, help="Archivo .md de salida")
    parser.add_argument("--lang", default="spa+eng", help="Idiomas de Tesseract (por defecto spa+eng)")
    parser.add_argument("--split", action="store_true", help="Guarda además una carpeta con un .md por página")
    parser.add_argument(
        "--motor",
        choices=["auto", "markitdown", "pymupdf4llm", "manual"],
        default="auto",
        help="Motor de conversión. auto usa markitdown si hay capa de texto y pymupdf4llm (OCR) si es escaneado",
    )
    args = parser.parse_args()

    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    pdf = args.pdf
    if not pdf.is_file():
        print(f"Error: no existe el archivo '{pdf}'.", file=sys.stderr)
        return 2

    salida = args.salida or pdf.with_suffix(".md")
    exe = configurar_tesseract()
    total, con_texto = paginas_con_texto(pdf)

    print(f"PDF: {pdf.name} | {total} pagina(s) | {con_texto} con capa de texto")
    print(f"Tesseract: {exe or 'NO ENCONTRADO'}")

    if con_texto == 0 and exe is None:
        print(
            "Error: el PDF es un escaneo y Tesseract no esta disponible.\n"
            "Instala Tesseract (winget install UB-Mannheim.TesseractOCR) o usa un PDF con capa de texto.",
            file=sys.stderr,
        )
        return 1

    markdown = None
    errores = []
    motores = {
        "markitdown": lambda: convertir_markitdown(pdf),
        "pymupdf4llm": lambda: convertir_pymupdf4llm(pdf, args.lang),
        "manual": lambda: ocr_manual(pdf, args.lang),
    }
    if args.motor == "auto":
        orden = ["markitdown", "pymupdf4llm", "manual"] if con_texto else ["pymupdf4llm", "manual"]
    else:
        orden = [args.motor]
    for nombre in orden:
        funcion = motores[nombre]
        try:
            markdown = funcion()
            if markdown and markdown.strip():
                print(f"Convertido con: {nombre}")
                break
            markdown = None
            errores.append(f"{nombre}: resultado vacio")
        except Exception as exc:
            errores.append(f"{nombre}: {type(exc).__name__}: {exc}")

    if markdown is None:
        print("Error: no se pudo convertir el PDF.", file=sys.stderr)
        for detalle in errores:
            print(f"  - {detalle}", file=sys.stderr)
        return 1

    sospechosos = sum(1 for ch in markdown if ch == "\ufffd" or "\u0100" <= ch <= "\u017f")
    if sospechosos >= 3:
        print(
            "Aviso: la capa de texto del PDF esta mal codificada (caracteres rotos). "
            "El problema esta en el PDF original, no en la conversion."
        )

    cabecera = (
        f"# {pdf.stem}\n\n"
        f"Fuente: `{pdf.name}` | Paginas: {total} | "
        f"OCR: {'si' if con_texto < total else 'no'} | "
        f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    )
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(cabecera + markdown.strip() + "\n", encoding="utf-8")
    print(f"Guardado: {salida}")

    if args.split:
        carpeta, n = escribir_split(markdown, salida)
        print(f"Paginas separadas: {n} archivos en {carpeta}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
