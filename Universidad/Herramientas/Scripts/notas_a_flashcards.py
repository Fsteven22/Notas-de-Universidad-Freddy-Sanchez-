#!/usr/bin/env python3
"""Genera flashcards (Pregunta::Respuesta) desde las definiciones de tus notas.

Detecta bloques de definicion:
  > [!note] Definicion - <termino>     (o "Definicion de <termino>", "Definiciones ...")
  > [!note] Definicion                 (el termino sale del ultimo heading)

Y arma tarjetas con el formato del vault:
  ## 🔁 Repaso SR (flashcards)
  #flashcards/<materia>-<unidad>
  > [!note] 🧠 Repasa con el plugin Spaced Repetition
  - ¿<termino>?::<definicion>

Dry-run por defecto: sin --aplicar solo muestra el plan. Nunca borra tarjetas
existentes, salta los terminos que ya tienen tarjeta y valida al final con
verificar_nota.py.

Uso:
  py notas_a_flashcards.py --todo
  py notas_a_flashcards.py --nota "Universidad/.../01 - Dato, informacion y modelos de datos.md"
  py notas_a_flashcards.py --carpeta "Universidad/3er Semestre/Sistema de Bases de Datos" --aplicar
  py notas_a_flashcards.py --carpeta "Universidad/3er Semestre" --tag flashcards/bd-u3 --aplicar
"""
import argparse
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

VAULT_POR_DEFECTO = Path(__file__).resolve().parents[3]
TITULO_SECCION = "## \U0001F501 Repaso SR (flashcards)"
CALLOUT_REPASO = "> [!note] \U0001F9E0 Repasa con el plugin Spaced Repetition"
RE_CALLOUT = re.compile(r"^>\s*\[!(?P<tipo>\w+)\]\s*(?P<titulo>.+?)\s*$")
RE_DEFINICION = re.compile(r"definici", re.IGNORECASE)
RE_HEADING = re.compile(r"^(#{2,4})\s+(?P<titulo>.+?)\s*$")
RE_EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF\uFE0F\u20E3\u2B00-\u2BFF]"
)
MATERIAS = {
    "sistema de bases de datos": "bd",
    "matematicas discretas": "discretas",
    "diseno de software": "diseno",
    "comunicacion": "comunicacion",
    "ingles iii": "ingles-iii",
    "fundamentos de electricidad y sistemas digitales": "fesd",
    "fisica mecanica": "fisica",
    "fundamentos de programacion": "fundamentos",
}


def normalizar(texto):
    plano = unicodedata.normalize("NFKD", texto)
    plano = "".join(c for c in plano if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", plano.lower()).strip()


def quitar_emoji(texto):
    return RE_EMOJI.sub("", texto).replace("\u00a0", " ").strip()


def slug(texto):
    plano = unicodedata.normalize("NFKD", texto)
    plano = "".join(c for c in plano if not unicodedata.combining(c))
    plano = re.sub(r"[^a-zA-Z0-9]+", "-", plano.lower()).strip("-")
    return plano or "material"


def termino_de_titulo(titulo):
    limpio = quitar_emoji(titulo)
    for separador in ("\u2014", "\u2013"):
        if separador in limpio:
            return limpio.split(separador, 1)[1].strip()
    coincidencia = re.match(r"definici\w*\s+(?:formal\s+)?(?:de|del)\s+(.+)$", limpio, re.IGNORECASE)
    if coincidencia:
        return coincidencia.group(1).strip()
    coincidencia = re.match(r"definici\w*\s+(.+)$", limpio, re.IGNORECASE)
    if coincidencia:
        return coincidencia.group(1).strip()
    return None


def termino_de_heading(titulo):
    limpio = quitar_emoji(titulo)
    limpio = re.sub(r"^\d+[.)]\s*", "", limpio)
    for separador in ("\u2014", "\u2013", " - "):
        if separador in limpio:
            return limpio.split(separador, 1)[0].strip()
    return limpio


def definiciones_de_nota(lineas):
    definiciones = []
    ultimo_heading = None
    indice = 0
    while indice < len(lineas):
        linea = lineas[indice]
        coincidencia_heading = RE_HEADING.match(linea)
        if coincidencia_heading:
            ultimo_heading = coincidencia_heading.group("titulo")
        coincidencia = RE_CALLOUT.match(linea)
        if coincidencia and RE_DEFINICION.search(coincidencia.group("titulo")):
            termino = termino_de_titulo(coincidencia.group("titulo"))
            if not termino and ultimo_heading:
                termino = termino_de_heading(ultimo_heading)
            cuerpo = []
            cursor = indice + 1
            while cursor < len(lineas) and lineas[cursor].lstrip().startswith(">"):
                limpia = re.sub(r"^\s*>\s?", "", lineas[cursor]).strip()
                if limpia:
                    cuerpo.append(limpia)
                elif cuerpo:
                    break
                cursor += 1
            texto = " ".join(cuerpo).strip()
            texto = re.sub(r"\s+", " ", texto)
            if termino and texto:
                definiciones.append((termino.strip(), texto))
            indice = cursor
            continue
        indice += 1
    return definiciones


def tarjetas_existentes(lineas):
    existentes = []
    for linea in lineas:
        if linea.startswith("- ") and "::" in linea:
            pregunta, respuesta = linea[2:].split("::", 1)
            existentes.append((normalizar(pregunta.rstrip("? ")), normalizar(respuesta)))
    return existentes


VACIAS = {
    "de", "la", "el", "los", "las", "un", "una", "que", "en", "con", "por", "para", "se", "su",
    "es", "son", "del", "al", "y", "o", "a", "the", "of", "and", "to", "in", "no", "no", "no",
    "sin", "como", "más", "pero", "este", "esta", "esto", "cuando", "donde", "valor", "dato",
}


def palabras_contenido(texto):
    return {palabra for palabra in normalizar(texto).split() if palabra not in VACIAS and len(palabra) > 3}


def ya_cubierto(termino, definicion, existentes):
    clave = normalizar(termino)
    palabras_def = palabras_contenido(definicion)
    for pregunta, respuesta in existentes:
        if clave and clave in pregunta:
            return True
        if palabras_def:
            palabras_rta = palabras_contenido(respuesta)
            if palabras_rta and len(palabras_def & palabras_rta) / len(palabras_def) >= 0.6:
                return True
    return False


def tag_existente(lineas):
    for linea in lineas:
        coincidencia = re.search(r"#flashcards/[\w\-]+", linea)
        if coincidencia:
            return coincidencia.group(0).replace("#", "")
    return None


def tag_inferido(ruta, vault):
    relativo = ruta.relative_to(vault)
    partes = [quitar_emoji(p).lower() for p in relativo.parts[:-1]]
    materia = "material"
    unidad = "material"
    for parte in partes:
        if parte in MATERIAS:
            materia = MATERIAS[parte]
        coincidencia = re.search(r"^(?:unidad|unit)\s+(\d+)", parte, re.IGNORECASE)
        if coincidencia:
            unidad = "u" + coincidencia.group(1)
    if materia == "material":
        for parte in partes:
            if parte and parte not in ("universidad",) and not parte.startswith(("1er", "2do", "3er", "preuniversitario")):
                materia = slug(parte)
                break
    return f"flashcards/{materia}-{unidad}"


TERMINOS_VAGOS = {
    "conceptos",
    "conceptos fundamentales",
    "definiciones",
    "equivalentes",
    "equivalencias",
    "ejemplo",
    "ejemplos",
    "notas",
    "ideas",
    "caracteristicas generales",
}


def termino_valido(termino):
    if not termino:
        return False
    if len(termino) > 60 or len(termino.split()) > 8:
        return False
    if any(marca in termino for marca in ("**", "$", "?", ":", "!", "|", "`")):
        return False
    if termino.endswith("."):
        return False
    if not termino[0].isupper():
        return False
    if normalizar(termino) in TERMINOS_VAGOS:
        return False
    return True


def limpiar_definicion(texto):
    texto = re.sub(r"!\[\[.*?\]\]", "", texto)
    texto = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", texto)
    texto = texto.replace("::", ":").strip()
    texto = re.sub(r"\s+", " ", texto)
    texto = re.sub(
        r"^\*\*\s*(Definici\w*|Teorema|Propuesta|Lema|Algoritmo|Regla|Criterio|Ejemplo|Nota)\s*:?\s*\*\*\s*:?\s*",
        "",
        texto,
        flags=re.IGNORECASE,
    )
    return texto.strip()


def definicion_valida(texto):
    if not texto:
        return False
    if texto.startswith(("#", "-", "*", ">")):
        return False
    if "###" in texto or "**📏" in texto:
        return False
    sin_matematica = re.sub(r"\$\$.*?\$\$|\$[^$]*\$", " ", texto)
    palabras = [p for p in re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", sin_matematica) if len(p) > 3]
    return len(palabras) >= 4


def construir_tarjetas(nota, definiciones, existentes, limite_def=320):
    tarjetas = []
    vistas = {pregunta for pregunta, _ in existentes}
    for termino, definicion in definiciones:
        clave = normalizar(termino)
        if not termino_valido(termino) or clave in vistas:
            continue
        limpio = limpiar_definicion(definicion)
        if len(limpio) < 15 or len(limpio) > limite_def:
            continue
        if not definicion_valida(limpio):
            continue
        if "?" in termino or limpio.endswith("?"):
            continue
        if ya_cubierto(termino, limpio, existentes):
            continue
        tarjeta = f"- \u00bf{termino}?::{limpio}"
        tarjetas.append(tarjeta)
        vistas.add(clave)
        existentes = existentes + [(clave, normalizar(limpio))]
    return tarjetas


def insertar_tarjetas(lineas, tarjetas, tag):
    nueva = list(lineas)
    indice_titulo = None
    for indice, linea in enumerate(nueva):
        if linea.strip() == TITULO_SECCION:
            indice_titulo = indice
            break
    if indice_titulo is None:
        while nueva and not nueva[-1].strip():
            nueva.pop()
        nueva.extend(["", "---", "", TITULO_SECCION, "", tag, "", CALLOUT_REPASO, ""])
        nueva.extend(tarjetas)
        nueva.append("")
        return nueva

    fin = len(nueva)
    for indice in range(indice_titulo + 1, len(nueva)):
        if nueva[indice].startswith("## ") or nueva[indice].strip() == "---":
            fin = indice
            break
    while fin > indice_titulo + 1 and not nueva[fin - 1].strip():
        fin -= 1
    if tag and not any(re.search(r"#flashcards/[\w\-]+", linea) for linea in nueva[indice_titulo:fin]):
        nueva.insert(indice_titulo + 2, tag)
        nueva.insert(indice_titulo + 3, "")
        fin += 2
    nuevas = nueva[:fin] + tarjetas + nueva[fin:]
    return nuevas


def leer(ruta):
    texto = ruta.read_bytes().decode("utf-8")
    crlf = "\r\n" in texto
    return texto.replace("\r\n", "\n").split("\n"), crlf


def escribir(ruta, lineas, crlf):
    texto = "\n".join(lineas)
    if crlf:
        texto = texto.replace("\n", "\r\n")
    ruta.write_bytes(texto.encode("utf-8"))


def main():
    parser = argparse.ArgumentParser(description="Genera flashcards desde las definiciones de tus notas.")
    parser.add_argument("--nota", type=Path, default=None, help="Una nota .md")
    parser.add_argument("--carpeta", type=Path, default=None, help="Carpeta con notas")
    parser.add_argument("--todo", action="store_true", help="Todas las notas de Universidad/")
    parser.add_argument("--vault", type=Path, default=VAULT_POR_DEFECTO, help="Raiz del vault")
    parser.add_argument("--tag", default=None, help="Tag forzado, ej. flashcards/bd-u3")
    parser.add_argument("--limite", type=int, default=0, help="Maximo de notas a modificar (0 = sin limite)")
    parser.add_argument("--aplicar", action="store_true", help="Escribe los cambios")
    args = parser.parse_args()

    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    vault = args.vault.resolve()
    if args.nota:
        base = args.nota if args.nota.is_absolute() else (vault / args.nota)
        notas = [base] if base.is_file() else []
    elif args.carpeta:
        base = args.carpeta if args.carpeta.is_absolute() else (vault / args.carpeta)
        notas = sorted(base.rglob("*.md")) if base.is_dir() else []
    elif args.todo:
        notas = sorted((vault / "Universidad").rglob("*.md"))
    else:
        print("Indica --nota, --carpeta o --todo.", file=sys.stderr)
        return 2

    if not notas:
        print("No se encontraron notas.", file=sys.stderr)
        return 2

    modificadas = []
    total_tarjetas = 0
    for nota in notas:
        try:
            lineas, crlf = leer(nota)
        except (OSError, UnicodeDecodeError):
            continue
        definiciones = definiciones_de_nota(lineas)
        if not definiciones:
            continue
        existentes = tarjetas_existentes(lineas)
        tarjetas = construir_tarjetas(nota, definiciones, existentes)
        if not tarjetas:
            continue
        tag = args.tag or tag_existente(lineas) or tag_inferido(nota, vault)
        nueva = insertar_tarjetas(lineas, tarjetas, tag)
        total_tarjetas += len(tarjetas)
        modificadas.append((nota, tarjetas, tag, nueva, crlf))

    print(f"Notas revisadas: {len(notas)} | con tarjetas nuevas: {len(modificadas)} | tarjetas: {total_tarjetas}")
    for nota, tarjetas, tag, nueva, crlf in modificadas:
        print(f"\n{nota.relative_to(vault)}  [tag: {tag}]")
        for tarjeta in tarjetas:
            print(f"  {tarjeta[:150]}")

    if not args.aplicar:
        print("\nDry-run: nada escrito. Agrega --aplicar para modificar las notas.")
        return 0

    if args.limite and len(modificadas) > args.limite:
        modificadas = modificadas[: args.limite]
        print(f"\nLimite aplicado: solo se modifican {len(modificadas)} notas.")

    verificador = Path(__file__).resolve().parent / "verificar_nota.py"
    for nota, tarjetas, tag, nueva, crlf in modificadas:
        escribir(nota, nueva, crlf)
        print(f"Guardado: {nota.relative_to(vault)} ({len(tarjetas)} tarjetas)")
        if verificador.is_file():
            resultado = subprocess.run(
                [sys.executable, str(verificador), str(nota)], capture_output=True, text=True
            )
            if resultado.returncode != 0:
                print(f"  verificar_nota.py: {resultado.stdout.strip()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
