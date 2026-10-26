#!/usr/bin/env python3
"""Convierte un PDF en una nota del vault (Obsidian) lista para publicar.

Pipeline:
  1. Extrae el texto del PDF (markitdown si hay capa de texto, OCR con Tesseract
     si es escaneado) reutilizando convertir_pdf.py.
  2. Extrae las imagenes raster de cada pagina con PyMuPDF y las guarda en
     <vault>/Universidad/Figuras.
  3. Arma la nota con frontmatter (dg-publish + una sola linea tags:), callout
     de fuente, el contenido y los embeds ![[...]] de las figuras.

Dry-run por defecto: sin --aplicar solo muestra lo que haria.

Uso:
  py pdf_a_nota_vault.py "material.pdf" --nota "Universidad/3er Semestre/Materia/Unidad 1 - X/material.md" --tags "materia, unidad1" --aplicar
  py pdf_a_nota_vault.py "material.pdf" --nota "Universidad/3er Semestre/Materia/Unidad 1 - X/material.md" --dg-publish true --aplicar

Al terminar valida la nota con verificar_nota.py.
"""
import argparse
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import convertir_pdf

SEP_PAGINA = re.compile(r"^---\s*end of page")
VAULT_POR_DEFECTO = Path(__file__).resolve().parents[3]


def dividir_paginas(markdown):
    paginas = []
    actual = []
    for linea in markdown.splitlines():
        if SEP_PAGINA.match(linea):
            paginas.append("\n".join(actual).strip())
            actual = []
            continue
        actual.append(linea)
    if "\n".join(actual).strip():
        paginas.append("\n".join(actual).strip())
    return paginas


def extraer_imagenes(pdf, carpeta, prefijo):
    import pymupdf

    carpeta.mkdir(parents=True, exist_ok=True)
    por_pagina = []
    vistos = set()
    with pymupdf.open(pdf) as documento:
        for indice, pagina in enumerate(documento, start=1):
            archivos = []
            for imagen in pagina.get_images(full=True):
                xref = imagen[0]
                if xref in vistos:
                    continue
                vistos.add(xref)
                try:
                    datos = documento.extract_image(xref)
                except Exception:
                    continue
                extension = datos.get("ext", "png")
                nombre = f"{prefijo}-p{indice:03d}-img{len(archivos) + 1:02d}.{extension}"
                (carpeta / nombre).write_bytes(datos["image"])
                archivos.append(nombre)
            por_pagina.append(archivos)
    return por_pagina


def ruta_relativa(origen, destino):
    return Path(os.path.relpath(destino, origen.parent)).as_posix()


def ruta_fuente(nota, pdf):
    relativa = ruta_relativa(nota, pdf)
    if relativa.startswith(".."):
        return pdf.as_posix()
    return relativa


def bajar_encabezados(texto):
    """Baja un nivel los encabezados del PDF para que la nota tenga un solo H1."""
    lineas = []
    for linea in texto.splitlines():
        if linea.startswith("#") and not linea.startswith("####"):
            espacio = linea[: len(linea) - len(linea.lstrip("#"))]
            if len(espacio) < 6:
                linea = espacio + "#" + linea[len(espacio) :]
        lineas.append(linea)
    return "\n".join(lineas)


def main():
    parser = argparse.ArgumentParser(description="PDF a nota del vault (dry-run por defecto).")
    parser.add_argument("pdf", type=Path, help="PDF de entrada")
    parser.add_argument("--nota", type=Path, required=True, help="Ruta del .md a crear (relativa al vault)")
    parser.add_argument("--vault", type=Path, default=VAULT_POR_DEFECTO, help="Raiz del vault")
    parser.add_argument("--titulo", default=None, help="Titulo de la nota")
    parser.add_argument("--tags", default="", help="Tags separados por coma")
    parser.add_argument("--dg-publish", choices=["true", "false"], default="false", help="Publicar en el sitio")
    parser.add_argument("--motor", choices=["auto", "pymupdf4llm", "markitdown"], default="auto", help="Motor de texto")
    parser.add_argument("--figuras", type=Path, default=None, help="Carpeta de figuras (por defecto <vault>/Universidad/Figuras)")
    parser.add_argument("--aplicar", action="store_true", help="Escribe la nota y las figuras")
    parser.add_argument("--forzar", action="store_true", help="Sobrescribe una nota existente")
    args = parser.parse_args()

    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    vault = args.vault.resolve()
    pdf = args.pdf if args.pdf.is_absolute() else (Path.cwd() / args.pdf)
    if not pdf.is_file():
        print(f"Error: no existe el PDF '{pdf}'.", file=sys.stderr)
        return 2

    nota = args.nota if args.nota.is_absolute() else (vault / args.nota)
    if nota.exists() and not args.forzar:
        print(f"Error: la nota ya existe ('{nota}'). Usa --forzar para sobrescribir.", file=sys.stderr)
        return 1

    carpeta_figuras = args.figuras or (vault / "Universidad" / "Figuras")
    prefijo = re.sub(r"[^\w\-]+", "-", pdf.stem, flags=re.UNICODE).strip("-")

    convertir_pdf.configurar_tesseract()
    total_paginas, con_texto = convertir_pdf.paginas_con_texto(pdf)
    print(f"PDF: {pdf.name} | {total_paginas} pagina(s) | {con_texto} con capa de texto")

    if args.motor == "markitdown":
        markdown = convertir_pdf.convertir_markitdown(pdf)
        motor = "markitdown"
    else:
        markdown = convertir_pdf.convertir_pymupdf4llm(pdf, "spa+eng")
        motor = "pymupdf4llm" + (" + OCR" if con_texto < total_paginas else "")
    if not markdown or not markdown.strip():
        print("Error: el PDF no devolvio contenido.", file=sys.stderr)
        return 1

    paginas = dividir_paginas(markdown)
    if len(paginas) == 1 and total_paginas > 1:
        print(
            f"Aviso: el motor no marco paginas; las {total_paginas} paginas se tratan como una. "
            "Usa --motor pymupdf4llm para(figuras por pagina).",
            file=sys.stderr,
        )
    imagenes = extraer_imagenes(pdf, carpeta_figuras, prefijo)
    total_imagenes = sum(len(a) for a in imagenes)

    cuerpo = []
    for indice, texto in enumerate(paginas, start=1):
        cuerpo.append(bajar_encabezados(texto))
        archivos = imagenes[indice - 1] if indice - 1 < len(imagenes) else []
        if archivos:
            cuerpo.append("### Figuras (pagina " + str(indice) + ")")
            for nombre in archivos:
                cuerpo.append(f"![[{ruta_relativa(nota, carpeta_figuras / nombre)}]]")

    titulo = args.titulo or pdf.stem
    tags = [t.strip() for t in args.tags.split(",") if t.strip()]
    lineas_tags = f"tags: [{', '.join(tags)}]" if tags else ""

    enlace_fuente = ruta_fuente(nota, pdf)
    contenido = "\n\n".join(part for part in cuerpo if part).strip()

    frontmatter = ["---", f"dg-publish: {args.dg_publish}"]
    if lineas_tags:
        frontmatter.append(lineas_tags)
    frontmatter.append("---")

    encabezado = [
        "\n".join(frontmatter),
        "",
        f"# {titulo}",
        "",
        "> [!info] Fuente",
        f"> [{pdf.name}]({enlace_fuente}) | conversion: PDF a Markdown ({motor}) | "
        f"{datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "",
    ]
    texto_final = "\n".join(encabezado) + contenido + "\n"

    print(f"Nota: {nota}")
    print(f"Figuras: {total_imagenes} en {carpeta_figuras}")
    print(f"dg-publish: {args.dg_publish} | tags: {lineas_tags or '(sin tags)'}")

    if not args.aplicar:
        print("\nDry-run: nada escrito. Agrega --aplicar para crear la nota.")
        return 0

    nota.parent.mkdir(parents=True, exist_ok=True)
    nota.write_text(texto_final, encoding="utf-8")
    print(f"Guardado: {nota}")

    verificador = Path(__file__).resolve().parent / "verificar_nota.py"
    if verificador.is_file():
        resultado = subprocess.run(
            [sys.executable, str(verificador), str(nota)],
            capture_output=True,
            text=True,
        )
        print(f"verificar_nota.py (exit {resultado.returncode}):")
        print((resultado.stdout or resultado.stderr).strip())
    return 0


if __name__ == "__main__":
    sys.exit(main())
