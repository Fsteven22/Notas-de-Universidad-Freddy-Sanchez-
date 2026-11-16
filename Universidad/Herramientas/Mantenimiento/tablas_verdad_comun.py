# -*- coding: utf-8 -*-
"""
tablas_verdad_comun.py - Logica compartida de las tablas de verdad.

Lo usan DOS herramientas y por eso vive aparte:
  - gen_tablas_verdad.py   (dibuja la figura PNG de cada tabla)
  - qa_formato_matdisc.py  (comprueba que cada tabla tiene su figura encima)

Que compartan el mismo criterio es lo que garantiza que el generador y el
validador hablen de la misma tabla: si cada uno tuviera el suyo, una tabla
podria existir para uno y no para el otro.

Criterio de "tabla de verdad":
  - bloque markdown tabular (cabecera + separador + filas)
  - todas las cabeceras son matematicas ($...$ o una sola letra)
  - el cuerpo es mayoritariamente V/F (se ignoran las ** de enfasis)
"""
import re

RE_SEP = re.compile(r"^\s*>?\s*\|?\s*:?-{1,}:?\s*(\|\s*:?-{1,}:?\s*)*\|?\s*$")
RE_CELL = re.compile(r"^\s*>?\s*\|(.*)\|\s*$")


def celdas(linea):
    """Celdas de una linea de tabla markdown (con o sin prefijo '> ')."""
    m = RE_CELL.match(linea)
    if not m:
        return None
    return [c.strip() for c in m.group(1).split("|")]


def norm(celda):
    """Normaliza una celda para comparar: sin **, sin espacios."""
    return str(celda).replace("**", "").replace("*", "").replace(" ", "").strip()


def es_formal(cabecera):
    """Una cabecera de tabla de verdad es solo matematica: $...$ o una letra.

    Si hay prosa ('Condicional', 'Tipo', 'Motivo') la tabla NO es de verdad
    sino de clasificacion: no se convierte en figura.
    """
    c = str(cabecera).strip()
    if c.startswith("$") and c.endswith("$"):
        return True
    return len(c) == 1 and c.isalpha()


def es_tabla_verdad(cab, filas):
    if len(cab) < 2 or not filas:
        return False
    if not all(es_formal(c) for c in cab):
        return False
    celdas_ = [c for f in filas for c in f]
    vf = [c for c in celdas_ if norm(c).upper() in ("V", "F")]
    return len(vf) / max(1, len(celdas_)) >= 0.45


def firma(cab, filas):
    """Identidad de una tabla (cabecera + cuerpo), para deduplicar."""
    c = "|".join(norm(x) for x in cab)
    f = "|".join(",".join(norm(x) for x in fila) for fila in filas)
    return c + "#" + f


def escanea_lineas(lineas, offset=0):
    """Tablas de verdad dentro de una lista de lineas.

    Devuelve [{'inicio': i, 'fin': j, 'cab': [...], 'filas': [[...]]}]
    con indices 0-based dentro de `lineas` (mas `offset` para el numero
    de linea real de la nota).
    """
    salida = []
    i = 0
    n = len(lineas)
    while i < n:
        cab = celdas(lineas[i])
        if cab and i + 1 < n and RE_SEP.match(lineas[i + 1]):
            j = i + 2
            filas = []
            while j < n:
                c = celdas(lineas[j])
                if c is None:
                    break
                filas.append(c)
                j += 1
            if es_tabla_verdad(cab, filas):
                salida.append({"inicio": i, "fin": j - 1,
                               "cab": cab, "filas": filas})
                i = j
                continue
        i += 1
    return salida
