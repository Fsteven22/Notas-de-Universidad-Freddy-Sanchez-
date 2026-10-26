#!/usr/bin/env python3
"""Atajo: convierte a Markdown un PDF que ya tiene capa de texto (sin OCR).

Usa el motor markitdown (pdfminer). Si el PDF es un escaneo y no hay texto,
el motor devuelve vacio y el script avisa; para eso usa pdf_ocr_a_markdown.py.

Uso:
  py pdf_a_markdown.py entrada.pdf
  py pdf_a_markdown.py entrada.pdf -o salida.md
"""
import subprocess
import sys
from pathlib import Path

CORE = Path(__file__).with_name("convertir_pdf.py")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    return subprocess.call([sys.executable, str(CORE), *sys.argv[1:], "--motor", "markitdown"])


if __name__ == "__main__":
    sys.exit(main())
