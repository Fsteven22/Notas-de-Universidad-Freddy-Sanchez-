#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""split_callouts_calculo1.py — separa titulo y cuerpo de los callouts de una linea.

En `Cálculo de una Variable` hay 90 callouts cuya PRIMERA LINEA contiene el
titulo Y todo el cuerpo pegados:

    > [!tip] 🎯 Idea Central Un **límite** describe hacia donde se dirige ...

El sitio (`site/src/lib/rehype-callouts.mjs`) toma todo el primer parrafo
como titulo del callout, asi que ese texto se renderiza como un titulo
gigante y el callout queda sin cuerpo. SBD, Diseno de Software y Calculo
Vectorial tienen **0** callouts asi (verificado), de modo que es un defecto
exclusivo de esta materia.

Este script corta esos 90 callouts usando un MAPA REVISADO A MANO: para cada
caso se declara el prefijo del titulo original y el titulo nuevo. El cuerpo
se deriva como el resto exacto de la linea original, asi que no se puede
perder ni una palabra por error de tipeo.

Orden: se ejecuta ANTES de `transform_calculo1.py`, sobre las notas
originales (las lineas del mapa son las del original).

Uso:
  py -3.12 split_callouts_calculo1.py            (dry-run)
  py -3.12 split_callouts_calculo1.py --apply
"""

import argparse
import io
import os
import re
import sys
import unicodedata
from pathlib import Path

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

from qa_formato_calculo1 import RE_CALL_HDR, bloques_callout  # noqa: E402

MATERIA = os.path.join("1er Semestre", "Cálculo de una Variable")

# --------------------------------------------------------------------------
# MAPA REVISADO A MANO de los 90 callouts de una linea.
#
# Clave: ruta relativa de la nota dentro de la materia.
# Valor: lista de (linea_original, prefijo_titulo_original, titulo_nuevo)
#
# - `prefijo_titulo_original` DEBE ser prefijo exacto de la linea original.
#   El cuerpo es el resto de la linea, sin tocar.
# - `titulo_nuevo` es lo que queda como titulo del callout.
# - La entrada (linea, None, None) marca "mover el embed siguiente al
#   interior del callout" (caso del Paso 3 de fracciones parciales).
# --------------------------------------------------------------------------

A = "Unidad 2 - Límites/I - Fundamentos del Límite/01 - Concepto y Definición Formal del Límite.md"
B = "Unidad 2 - Límites/II - Técnicas Básicas/01 - Límites Laterales.md"
C = "Unidad 2 - Límites/II - Técnicas Básicas/02 - Límites Especiales.md"
D = "Unidad 2 - Límites/II - Técnicas Básicas/03 - Límites en Gráficas.md"
E = "Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones.md"
F = "Unidad 2 - Límites/III - Avanzados/02 - Formas Indeterminadas.md"
G = "Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal.md"
H = "Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/01 - Análisis Completo de Funciones.md"
I = "Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/03 - Concavidad y Puntos de Inflexión.md"
J = "Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización.md"
K = "Unidad 5 - Aplicaciones de la Derivada/II - Optimización/02 - Optimización con Restricciones.md"
L = "Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas.md"
M = "Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/03 - Aproximaciones Lineales y Diferenciales.md"
N = "Unidad 6 - Integrales/III - Integrales Definidas/03 - Teoremas Especiales para Integrales Definidas.md"
O = "Unidad 6 - Integrales/Técnicas de Integración/01 - Cambio de Variable en Integrales.md"
P = "Unidad 6 - Integrales/Técnicas de Integración/02 - Integración por Partes.md"
Q = "Unidad 6 - Integrales/Técnicas de Integración/03 - Integrales Trigonométricas.md"
Rr = "Unidad 6 - Integrales/Técnicas de Integración/04 - Integrales de Funciones Inversas.md"
S = "Unidad 6 - Integrales/Técnicas de Integración/05 - Integrales por Fracciones Parciales.md"
T = "Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva.md"
U = "Unidad 7 - Aplicaciones de la Integral/I - Áreas/02 - Área entre Curvas.md"
V = "Unidad 7 - Aplicaciones de la Integral/I - Áreas/03 - Área entre Curvas respecto a Y.md"
W = "Unidad 7 - Aplicaciones de la Integral/I - Áreas/04 - Área en Coordenadas Polares y Paramétricas.md"
X = "Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/02 - Volúmenes con Ejes Arbitrarios y Casos Avanzados.md"
Y = "Unidad 7 - Aplicaciones de la Integral/III - Longitud de Arco/01 - Longitud de Curva.md"

MAPA = {
    A: [
        (7,   "🎯 Idea Central", "🎯 Idea Central"),
        (190, "🎯 Concepto Central", "🎯 Concepto Central"),
        (432, "🎓 Para Recordar el Proceso de Demostración", "🎓 Para Recordar el Proceso de Demostración"),
    ],
    B: [
        (7,   "🎯 Concepto Central", "🎯 Concepto Central"),
        (201, "🎓 Para Recordar el Proceso", "🎓 Para Recordar el Proceso"),
    ],
    C: [
        (167, "🚀 Límites Derivados y Extensiones", "🚀 Límites Derivados y Extensiones"),
        (364, "💡 **Concepto Clave**", "💡 **Concepto Clave**"),
    ],
    D: [
        (7,   "🎯 Concepto Central", "🎯 Concepto Central"),
        (97,  '🔍 Método "MIRA"', '🔍 Método "MIRA"'),
        (196, "🎓 Para Leer Límites en Gráficas", "🎓 Para Leer Límites en Gráficas"),
    ],
    E: [
        (7,   "💡 **Concepto Clave**", "💡 **Concepto Clave**"),
        (209, "💡 **Concepto Clave**", "💡 **Concepto Clave**"),
    ],
    F: [
        (647, "⚠️ Importancia Histórica", "⚠️ Importancia Histórica"),
        (796, "📐 Formas que Requieren Transformación L'Hôpital", "📐 Formas que Requieren Transformación L'Hôpital"),
    ],
    G: [
        # el cuerpo es la cita completa; la atribucion pasa al titulo
        (7,   "", "💬 Cita de Gilbert Strang"),
    ],
    H: [
        (47,  "Definición", "📐 Definición"),
        (106, "Puntos Clave", "🔑 Puntos Clave"),
        (157, "Análisis Asintótico", "📊 Análisis Asintótico"),
        (207, "Metodología Sistemática", "🧭 Metodología Sistemática"),
        (346, "", "🔗 Notas relacionadas"),
    ],
    I: [
        (9,   "Concepto Fundamental", "🎯 Concepto Fundamental"),
        (56,  "Definición", "📐 Definición"),
        (84,  "Definición", "📐 Definición"),
        (91,  "Condición Suficiente", "✅ Condición Suficiente"),
        (156, "Análisis Visual Completo", "📊 Análisis Visual Completo"),
        (219, "Aplicaciones de Derivadas", "💡 Aplicaciones de Derivadas"),
    ],
    J: [
        (9,   "Concepto Fundamental", "🎯 Concepto Fundamental"),
        (13,  "Metodología MODELO (Técnica de Memorización)", "🧭 Metodología MODELO (Técnica de Memorización)"),
        (19,  "Lugares Donde Buscar Extremos", "📍 Lugares Donde Buscar Extremos"),
        (40,  "Características", "📋 Características"),
        (76,  "Fórmulas de Volumen Importantes", "📐 Fórmulas de Volumen Importantes"),
        (89,  "Tipos Principales", "🗂️ Tipos Principales"),
        (122, "Contexto", "🌍 Contexto"),
        (171, "Enfoque Sistemático", "🧭 Enfoque Sistemático"),
        (187, "Estrategias de Construcción", "🧠 Estrategias de Construcción"),
        (191, "Clasificación de Restricciones", "🗂️ Clasificación de Restricciones"),
        (197, "Métodos de Reducción", "🛠️ Métodos de Reducción"),
        (201, "Verificaciones Necesarias", "✅ Verificaciones Necesarias"),
        (209, 'Método de Verificación "SPEC"', '✅ Método de Verificación "SPEC"'),
        (272, "Modelado Matemático", "🧠 Modelado Matemático"),
    ],
    K: [
        (9,   "Concepto Fundamental", "🎯 Concepto Fundamental"),
        (64,  "Filosofía del Método", "🧭 Filosofía del Método"),
        (135, "Aplicaciones del Mundo Real", "🌍 Aplicaciones del Mundo Real"),
        (227, "Visualización Conceptual", "👁️ Visualización Conceptual"),
        (383, "", "🔗 Notas relacionadas"),
    ],
    L: [
        (9,   "Concepto Fundamental", "🎯 Concepto Fundamental"),
        (19,  "Proceso Sistemático DERIVA", "🧭 Proceso Sistemático DERIVA"),
        (90,  "Características", "📋 Características"),
        (163, "Naturaleza de los Problemas", "🔍 Naturaleza de los Problemas"),
        (236, "Contexto Profesional", "🌍 Contexto Profesional"),
        (312, 'Estrategia de Resolución "RAPID"', '🧠 Estrategia de Resolución "RAPID"'),
        (354, "Checklist de Verificación", "✅ Checklist de Verificación"),
        (370, "Modelado Matemático", "🧠 Modelado Matemático"),
    ],
    M: [
        (7,   "🎯 Concepto Central", "🎯 Concepto Central"),
    ],
    N: [
        (7,   "💡 **Conceptos Centrales**", "💡 **Conceptos Centrales**"),
        (18,  "🎨 **Interpretación Geométrica**", "🎨 **Interpretación Geométrica**"),
        (28,  "🎨 **Interpretación Geométrica**", "🎨 **Interpretación Geométrica**"),
        (363, "💡 **Concepto Central**", "💡 **Concepto Central**"),
        (452, "⚡ **Propiedad Especial**", "⚡ **Propiedad Especial**"),
    ],
    O: [
        (7,   "💡 Concepto Clave", "💡 Concepto Clave"),
        (113, "💡 Concepto Clave", "💡 Concepto Clave"),
        (181, "📐 Construcción de Triángulos", "📐 Construcción de Triángulos"),
    ],
    P: [
        (7,   "💡 Concepto Clave", "💡 Concepto Clave"),
        (192, "💡 Concepto Clave", "💡 Concepto Clave"),
    ],
    Q: [
        (7,   "💡 Concepto Clave", "💡 Concepto Clave"),
    ],
    Rr: [
        (7,   "💡 Concepto Clave", "💡 Concepto Clave"),
    ],
    S: [
        (57,  None, None),      # el embed siguiente pasa al interior del callout
        (136, "✅ **Verificación**", "✅ **Verificación**"),
    ],
    T: [
        (7,   "💡 **La Interpretación Geométrica Fundamental**", "💡 **La Interpretación Geométrica Fundamental**"),
        (33,  "📈 **Caso Estándar**", "📈 **Caso Estándar**"),
        (225, "🎲 **Funciones de Densidad**", "🎲 **Funciones de Densidad**"),
    ],
    U: [
        (7,   "💡 **Concepto Central**", "💡 **Concepto Central**"),
        (18,  "⚠️ **Condición Importante**", "⚠️ **Condición Importante**"),
        (82,  "➕➖ **Cuando una función es positiva y otra negativa**", "➕➖ **Cuando una función es positiva y otra negativa**"),
        (92,  "🔄 **Cuando las funciones intercambian posiciones**", "🔄 **Cuando las funciones intercambian posiciones**"),
        (98,  "🔄 **Área entre curvas $x = f(y)$ y $x = g(y)$**", "🔄 **Área entre curvas $x = f(y)$ y $x = g(y)$**"),
        (166, "🗛️ **Cálculo de Áreas de Terrenos**", "🗛️ **Cálculo de Áreas de Terrenos**"),
        (170, "💊 **Biodisponibilidad de Medicamentos**", "💊 **Biodisponibilidad de Medicamentos**"),
        (174, "🌊 **Cálculo de Volúmenes de Agua**", "🌊 **Cálculo de Volúmenes de Agua**"),
        (266, "🌀 **Área entre curvas en coordenadas polares**", "🌀 **Área entre curvas en coordenadas polares**"),
        (270, "🔍 **Curvas paramétricas**", "🔍 **Curvas paramétricas**"),
        (274, "🌊 **Cálculo de áreas usando Teorema de Green**", "🌊 **Cálculo de áreas usando Teorema de Green**"),
    ],
    V: [
        (7,   "💡 **Concepto Central**", "💡 **Concepto Central**"),
    ],
    W: [
        (7,   "💡 **Concepto Central**", "💡 **Concepto Central**"),
        (20,  "⚠️ **Condición Importante**", "⚠️ **Condición Importante**"),
        (78,  "🎯 **Intersección de Regiones**", "🎯 **Intersección de Regiones**"),
        (98,  "⚠️ **Orientación Importante**", "⚠️ **Orientación Importante**"),
        (144, "🔄 **Conversión Polar → Paramétrica**", "🔄 **Conversión Polar → Paramétrica**"),
    ],
    X: [
        (10,  "🔗 **Prerrequisito**", "🔗 **Prerrequisito**"),
    ],
    Y: [
        (249, "🎯 **Idea Fundamental**", "🎯 **Idea Fundamental**"),
    ],
}

# texto que se retira del final del cuerpo porque pasa al titulo
SUFIJOS_A_TITULO = {
    (G, 7): " - Gilbert Strang",
}


def split_linea(linea, prefijo, titulo_nuevo, sufijo=""):
    """Devuelve (linea_callout, cuerpo) partiendo la linea del callout.

    La linea queda:  `> [!tipo] <titulo_nuevo>`
    El cuerpo es una lista de lineas `> <texto>` (puede ser vacia).
    """
    m = RE_CALL_HDR.match(linea)
    if not m:
        raise ValueError("no es un encabezado de callout: %r" % linea[:60])
    tipo = m.group("tipo")
    resto = m.group("titulo")
    if not resto.startswith(prefijo):
        raise ValueError("el prefijo %r no coincide con %r" % (prefijo, resto[:60]))
    cuerpo = resto[len(prefijo):].strip()
    if sufijo and cuerpo.endswith(sufijo):
        cuerpo = cuerpo[:-len(sufijo)].rstrip()
    cab = "> [!%s] %s" % (tipo, titulo_nuevo)
    lineas_cuerpo = []
    if cuerpo:
        lineas_cuerpo.append("> " + cuerpo)
    return cab, lineas_cuerpo


def main():
    ap = argparse.ArgumentParser(description="Corta los 90 callouts de una linea de Calculo 1")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()

    vault = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    raiz_mat = os.path.join(vault, MATERIA)

    total = 0
    problemas = []
    tocadas = 0
    for rel, entradas in sorted(MAPA.items()):
        p = os.path.join(raiz_mat, rel.replace("/", os.sep))
        if not os.path.isfile(p):
            problemas.append((rel, "NO EXISTE"))
            continue
        lineas = io.open(p, encoding="utf-8").read().replace("\ufeff", "").split("\n")
        # de mayor linea a menor, para no desfasar los indices
        for ln, prefijo, titulo_nuevo in sorted(entradas, key=lambda x: -x[0]):
            idx = ln - 1
            if idx >= len(lineas):
                problemas.append((rel, "linea %d fuera de rango" % ln))
                continue
            linea = lineas[idx]
            if prefijo is None:
                # caso especial: el embed siguiente entra al callout
                m = RE_CALL_HDR.match(linea)
                if not m:
                    problemas.append((rel, "linea %d no es callout" % ln))
                    continue
                j = idx + 1
                while j < len(lineas) and not lineas[j].strip():
                    j += 1
                if j >= len(lineas) or not lineas[j].lstrip().startswith("![["):
                    problemas.append((rel, "linea %d: no hay embed que mover" % ln))
                    continue
                emb = lineas[j].strip()
                nuevos = [linea, ">", "> " + emb]
                # se borra el embed top-level y su separacion
                for k in range(j, idx, -1):
                    lineas.pop(k)
                lineas[idx:idx + 1] = nuevos
                total += 1
                continue
            sufijo = SUFIJOS_A_TITULO.get((rel, ln), "")
            try:
                cab, cuerpo = split_linea(linea, prefijo, titulo_nuevo, sufijo)
            except ValueError as e:
                problemas.append((rel, "linea %d: %s" % (ln, e)))
                continue
            nuevos = [cab]
            if cuerpo:
                nuevos.append(">")
                nuevos.extend(cuerpo)
            lineas[idx:idx + 1] = nuevos
            total += 1
        salida = "\n".join(lineas)
        if not salida.endswith("\n"):
            salida += "\n"
        if args.apply:
            io.open(p, "w", encoding="utf-8", newline="\n").write(salida)
        tocadas += 1

    print("notas tocadas: %d" % tocadas)
    print("callouts cortados: %d" % total)
    if problemas:
        print("PROBLEMAS: %d" % len(problemas))
        for rel, det in problemas:
            print("   %s :: %s" % (rel[:60], det))
        return 1
    if not args.apply:
        print("(dry-run: no se escribio nada; usa --apply)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
