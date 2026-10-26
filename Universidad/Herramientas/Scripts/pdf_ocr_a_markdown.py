#!/usr/bin/env python3
"""Atajo: convierte a Markdown un PDF escaneado forzando OCR (Tesseract).

Usa el motor pymupdf4llm, que hace OCR solo en las paginas sin capa de texto
y respeta el layout. Si Tesseract no esta disponible, cae al motor manual.

Uso:
  py pdf_ocr_a_markdown.py entrada.pdf
  py pdf_ocr_a_markdown.py entrada.pdf --split --lang spa+eng
"""
import subprocess
import sys
from pathlib import Path

CORE = Path(__file__).with_name("convertir_pdf.py")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    return subprocess.call([sys.executable, str(CORE), *sys.argv[1:], "--motor", "pymupdf4llm"])


if __name__ == "__main__":
    sys.exit(main())
