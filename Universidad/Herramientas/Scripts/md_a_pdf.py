#!/usr/bin/env python3
"""Convierte una nota .md del vault a PDF (Markdown -> HTML -> Chromium headless).

Soporta la sintaxis de Obsidian:
  ![[imagen.png]]        -> <img> con la imagen resuelta (nota, vault o indice global)
  ![[diagrama.svg]]      -> idem
  [[enlace]]             -> texto plano
  > [!note] Titulo       -> callout con estilos de impresion
  ```mermaid             -> bloque renderizado con mermaid (CDN)
  $...$ y $$...$$        -> KaTeX (CDN); sin internet queda el texto tal cual

El PDF lo imprime Edge o Chrome en headless con CSS de impresion (A4, margenes,
tablas, callouts, figuras que no se parten entre paginas).

Uso:
  py md_a_pdf.py "Universidad/3er Semestre/Sistema de Bases de Datos/Unidad 0 - Guias y Ejercicios/Talleres/Tarea 2.md"
  py md_a_pdf.py "ruta/nota.md" -o "salida.pdf" --html
  py md_a_pdf.py "ruta/nota.md" --landscape --sin-katex
"""
import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

VAULT_POR_DEFECTO = Path(__file__).resolve().parents[3]
Navegadores = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]
EXT_IMAGENES = (".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp", ".bmp")
RE_EMBED = re.compile(r"!\[\[([^\]]+)\]\]")
RE_LINK = re.compile(r"(?<!!)\[\[([^\]]+)\]\]")
RE_CALLOUT = re.compile(r"^>\s*\[!(?P<tipo>[\w-]+)\]\s*(?P<titulo>.*)$")
RE_MERMAID = re.compile(r"^```mermaid\s*$")

CSS = """
@page { size: A4 portrait; margin: 18mm 16mm; }
* { box-sizing: border-box; }
body { font-family: "Segoe UI", Georgia, serif; font-size: 11.2pt; line-height: 1.5; color: #16181d; margin: 0; }
h1 { font-size: 21pt; border-bottom: 2px solid #2b6cb0; padding-bottom: 6px; margin: 0 0 14px; }
h2 { font-size: 16pt; border-bottom: 1px solid #cbd5e0; padding-bottom: 4px; margin: 20px 0 10px; }
h3 { font-size: 13.4pt; margin: 16px 0 8px; }
h4, h5, h6 { font-size: 11.8pt; margin: 12px 0 6px; }
p { margin: 0 0 9px; }
ul, ol { margin: 0 0 10px; padding-left: 22px; }
li { margin: 0 0 4px; }
a { color: #2b6cb0; text-decoration: none; }
code { font-family: "Cascadia Mono", Consolas, monospace; font-size: 9.6pt; background: #f1f5f9; padding: 1px 4px; border-radius: 3px; }
pre { background: #f8fafc; border: 1px solid #e2e8f0; border-left: 3px solid #2b6cb0; border-radius: 4px; padding: 10px 12px; overflow-x: hidden; white-space: pre-wrap; word-wrap: break-word; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: 10px 0 14px; font-size: 10.4pt; page-break-inside: avoid; }
th, td { border: 1px solid #94a3b8; padding: 5px 8px; text-align: left; vertical-align: top; }
th { background: #eef2f7; }
img { max-width: 100%; height: auto; display: block; margin: 8px auto; page-break-inside: avoid; }
figure { margin: 12px 0; page-break-inside: avoid; }
blockquote { border-left: 3px solid #cbd5e0; margin: 10px 0; padding: 4px 12px; color: #475569; }
.callout { border: 1px solid #cbd5e0; border-left: 4px solid #2b6cb0; border-radius: 4px; background: #f8fafc; padding: 8px 12px; margin: 12px 0; page-break-inside: avoid; }
.callout-title { font-weight: 700; margin-bottom: 4px; }
.callout p:last-child { margin-bottom: 0; }
.callout-note { border-left-color: #2b6cb0; }
.callout-info { border-left-color: #0f766e; }
.callout-warning { border-left-color: #b45309; }
.callout-tip { border-left-color: #15803d; }
.callout-example { border-left-color: #7c3aed; }
.callout-question { border-left-color: #be185d; }
.callout-abstract { border-left-color: #475569; }
.mermaid { text-align: center; margin: 12px 0; page-break-inside: avoid; }
hr { border: 0; border-top: 1px solid #cbd5e0; margin: 16px 0; }
.flashcard { font-family: "Cascadia Mono", Consolas, monospace; font-size: 10pt; }
"""


def indice_imagenes(vault):
    indice = {}
    for extension in EXT_IMAGENES:
        for ruta in vault.rglob(f"*{extension}"):
            indice.setdefault(ruta.name.lower(), []).append(ruta)
    return indice


def resolver_imagen(nombre, nota_dir, vault, indice):
    limpio = nombre.split("|", 1)[0].strip()
    candidatos = [
        nota_dir / limpio,
        vault / limpio,
        vault / "Universidad" / limpio,
    ]
    for candidato in candidatos:
        if candidato.is_file():
            return candidato
    for clave in (Path(limpio).name.lower(), limpio.lower()):
        if clave in indice:
            return sorted(indice[clave])[0]
    return None


def url_archivo(ruta):
    return Path(ruta).resolve().as_uri()


def quitar_frontmatter(texto):
    lineas = texto.split("\n")
    if lineas and lineas[0].strip() == "---":
        for indice in range(1, len(lineas)):
            if lineas[indice].strip() == "---":
                return "\n".join(lineas[indice + 1 :])
    return texto


def convertir_callouts(lineas):
    salida = []
    indice = 0
    while indice < len(lineas):
        linea = lineas[indice]
        coincidencia = RE_CALLOUT.match(linea)
        if not coincidencia:
            salida.append(linea)
            indice += 1
            continue
        tipo = coincidencia.group("tipo").lower()
        titulo = coincidencia.group("titulo").strip() or tipo.capitalize()
        cuerpo = []
        indice += 1
        while indice < len(lineas) and lineas[indice].lstrip().startswith(">"):
            cuerpo.append(re.sub(r"^\s*>\s?", "", lineas[indice]))
            indice += 1
        interno = "\n".join(cuerpo).strip()
        salida.append(
            f'<div class="callout callout-{html.escape(tipo)}" markdown="1">'
            f'<div class="callout-title">{html.escape(titulo)}</div>'
            f"{interno}</div>"
        )
    return salida


def resolver_mermaid(bloque, nota_dir, vault, indice):
    nombre = None
    coincidencia = re.search(r"%%\s*(.+?)\s*%%", bloque)
    if coincidencia:
        nombre = coincidencia.group(1).strip()
    if nombre:
        svg = resolver_imagen(nombre if nombre.lower().endswith(".svg") else nombre + ".svg", nota_dir, vault, indice)
        if svg:
            return f'<div class="mermaid"><img src="{url_archivo(svg)}" alt="{html.escape(nombre)}"></div>'
    return f'<div class="mermaid">{html.escape(bloque)}</div>'


def preprocesar(texto, nota_dir, vault, indice):
    texto = quitar_frontmatter(texto)
    texto = RE_EMBED.sub(
        lambda m: (
            f'<img src="{url_archivo(resolver_imagen(m.group(1), nota_dir, vault, indice))}" '
            f'alt="{html.escape(m.group(1))}">'
            if resolver_imagen(m.group(1), nota_dir, vault, indice)
            else f"<em>[imagen no encontrada: {html.escape(m.group(1))}]</em>"
        ),
        texto,
    )
    texto = RE_LINK.sub(lambda m: m.group(1).split("|", 1)[0].split("#", 1)[0], texto)
    lineas = texto.split("\n")
    salida = []
    indice_linea = 0
    while indice_linea < len(lineas):
        if RE_MERMAID.match(lineas[indice_linea]):
            bloque = []
            indice_linea += 1
            while indice_linea < len(lineas) and not lineas[indice_linea].strip().startswith("```"):
                bloque.append(lineas[indice_linea])
                indice_linea += 1
            indice_linea += 1
            salida.append(resolver_mermaid("\n".join(bloque), nota_dir, vault, indice))
            continue
        salida.append(lineas[indice_linea])
        indice_linea += 1
    return "\n".join(convertir_callouts(salida))


def construir_html(cuerpo, titulo, con_katex=True, con_mermaid=True):
    scripts = ""
    estilos_extra = ""
    if con_katex:
        estilos_extra += (
            '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16/dist/katex.min.css">'
        )
        scripts += (
            '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16/dist/katex.min.js"></script>'
            '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16/dist/contrib/auto-render.min.js"></script>'
            '<script>document.addEventListener("DOMContentLoaded",function(){'
            'try{renderMathInElement(document.body,{delimiters:['
            '{left:"$$",right:"$$",display:true},{left:"$",right:"$",display:false}]});}catch(e){}});</script>'
        )
    if con_mermaid:
        scripts += (
            '<script type="module">import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";'
            "mermaid.initialize({startOnLoad:true});</script>"
        )
    return (
        "<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'>"
        f"<title>{html.escape(titulo)}</title>"
        f"<style>{CSS}</style>{estilos_extra}</head>"
        f"<body>{cuerpo}{scripts}</body></html>"
    )


def navegador_disponible():
    for ruta in Navegadores:
        if Path(ruta).is_file():
            return ruta
    return shutil.which("msedge") or shutil.which("chrome")


def imprimir_pdf(html_ruta, pdf_ruta, navegador, landscape=False):
    perfil = tempfile.mkdtemp(prefix="md_a_pdf_")
    comando = [
        navegador,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=15000",
        f"--user-data-dir={perfil}",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_ruta}",
    ]
    if landscape:
        comando.append("--landscape")
    comando.append(html_ruta.as_uri())
    resultado = subprocess.run(comando, capture_output=True, text=True, timeout=180)
    shutil.rmtree(perfil, ignore_errors=True)
    return resultado


def main():
    parser = argparse.ArgumentParser(description="Convierte una nota .md del vault a PDF.")
    parser.add_argument("nota", type=Path, help="Nota .md de entrada")
    parser.add_argument("-o", "--salida", type=Path, default=None, help="PDF de salida")
    parser.add_argument("--vault", type=Path, default=VAULT_POR_DEFECTO, help="Raiz del vault")
    parser.add_argument("--titulo", default=None, help="Titulo del PDF")
    parser.add_argument("--landscape", action="store_true", help="Pagina horizontal")
    parser.add_argument("--sin-katex", action="store_true", help="No cargar KaTeX (sin matematicas)")
    parser.add_argument("--sin-mermaid", action="store_true", help="No cargar mermaid")
    parser.add_argument("--html", action="store_true", help="Guarda el HTML intermedio")
    args = parser.parse_args()

    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    vault = args.vault.resolve()
    nota = args.nota if args.nota.is_absolute() else (vault / args.nota)
    if not nota.is_file():
        print(f"Error: no existe la nota '{nota}'.", file=sys.stderr)
        return 2

    navegador = navegador_disponible()
    if not navegador:
        print("Error: no se encontro Edge ni Chrome para imprimir el PDF.", file=sys.stderr)
        return 1

    salida = args.salida or nota.with_suffix(".pdf")
    titulo = args.titulo or nota.stem

    indice = indice_imagenes(vault)
    cuerpo_md = preprocesar(nota.read_text(encoding="utf-8"), nota.parent, vault, indice)

    import markdown

    cuerpo_html = markdown.markdown(
        cuerpo_md,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "md_in_html"],
    )
    documento = construir_html(
        cuerpo_html, titulo, con_katex=not args.sin_katex, con_mermaid=not args.sin_mermaid
    )

    with tempfile.TemporaryDirectory(prefix="md_a_pdf_") as temporal:
        html_ruta = Path(temporal) / "nota.html"
        html_ruta.write_text(documento, encoding="utf-8")
        if args.html:
            guardado = nota.with_suffix(".html")
            guardado.write_text(documento, encoding="utf-8")
            print(f"HTML: {guardado}")
        pdf_temporal = Path(temporal) / "salida.pdf"
        resultado = imprimir_pdf(html_ruta, pdf_temporal, navegador, args.landscape)
        if not pdf_temporal.is_file():
            print(f"Error: el navegador no genero el PDF. {resultado.stderr[:400]}", file=sys.stderr)
            return 1
        salida.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(pdf_temporal, salida)

    print(f"PDF: {salida} ({salida.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
