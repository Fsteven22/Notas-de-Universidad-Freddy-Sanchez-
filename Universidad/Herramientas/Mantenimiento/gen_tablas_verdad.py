# -*- coding: utf-8 -*-
"""
gen_tablas_verdad.py - Genera las figuras PNG de las tablas de verdad de
Matematicas Discretas.

FUENTE UNICA DE VERDAD: las propias notas.
El script escanea los .md del curso, extrae las tablas de verdad (V/F),
las deduplica y dibuja UNA figura PNG por tabla distinta.  Asi la figura
nunca puede quedar desincronizada de la tabla markdown que la acompana:
si editas una tabla, regeneras y la figura sigue a la nota.

Por que un script y no "una imagen hecha a mano":
  - reproducible: la tabla vive en la nota (texto), no en un PNG opaco
  - verificable: si una tabla cambia, se regenera y se vuelve a embeber
  - consistente: misma paleta y tipografia para todas las tablas

Uso:
    py -3.12 gen_tablas_verdad.py              # genera todas las del catalogo
    py -3.12 gen_tablas_verdad.py --dry        # solo lista lo que generaria
    py -3.12 gen_tablas_verdad.py --solo negacion
    py -3.12 gen_tablas_verdad.py --check      # solo audita el catalogo

Salida: <VAULT>/Universidad/3er Semestre/Matematicas Discretas/
        Unidad 0 - Guias y Ejercicios/Figuras/<nombre>.png
"""
import argparse
import io
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import matplotlib
matplotlib.use("Agg")
# Para que el SVG del QA contenga <text> real (y no rutas): sin esto no se
# puede comprobar programaticamente que la figura dice lo que debe.
matplotlib.rcParams["svg.fonttype"] = "none"
import matplotlib.pyplot as plt

# ---------------------------------------------------------------- paleta
# Misma identidad pastel que los callouts del vault (Universidad/Herramientas/estilo.py)
PASTEL = ["#ffe1e1", "#e1e1ff", "#e1ffe1", "#fff4e1", "#f0e1ff", "#e1fff4"]
ACENTO = "#2c5aa0"
PELIGRO = "#e74c3c"
EXITO = "#1e8449"
TINTA = "#1a1a1a"
GRIS = "#666666"
DPI = 200


# ---------------------------------------------------------------- rutas
def _raiz():
    """Raiz del vault: deducida desde la ubicacion de este script."""
    aqui = os.path.dirname(os.path.abspath(__file__))
    # <vault>/Universidad/Herramientas/Mantenimiento/ -> 3 niveles arriba
    return os.path.dirname(os.path.dirname(os.path.dirname(aqui)))


def carpeta_curso():
    raiz = _raiz()
    return os.path.join(raiz, "Universidad", "3er Semestre", "Matemáticas Discretas")


def carpeta_destino():
    return os.path.join(carpeta_curso(), "Unidad 0 - Guias y Ejercicios", "Figuras")


# ---------------------------------------------------------------- escaneo
# El criterio de "que es una tabla de verdad" vive en tablas_verdad_comun.py
# (lo comparten el generador y el validador del contrato).
from tablas_verdad_comun import (  # noqa: E402
    celdas as _celdas, norm as _norm, es_tabla_verdad as _es_tabla_verdad,
    firma as _firma, escanea_lineas,
)


def escanea_tv(raiz=None):
    """Devuelve las tablas de verdad (V/F) de todas las notas del curso."""
    curso = raiz or carpeta_curso()
    salida = []
    for dirpath, dirs, files in os.walk(curso):
        dirs[:] = [d for d in dirs if d not in (".git", ".obsidian")]
        for fn in sorted(files):
            if not fn.endswith(".md"):
                continue
            ruta = os.path.join(dirpath, fn)
            with io.open(ruta, encoding="utf-8") as f:
                lineas = f.read().split("\n")
            for t in escanea_lineas(lineas):
                t["archivo"] = os.path.relpath(ruta, _raiz())
                t["linea"] = t["inicio"] + 1
                salida.append(t)
    return salida


# ---------------------------------------------------------------- registro
# Una entrada por tabla de verdad DISTINTA del curso.
# La clave es la cabecera de la tabla tal cual aparece en la nota (se
# normaliza al comparar: sin espacios y sin **).
#   nombre -> archivo .png de la figura
#   titulo -> encabezado de la figura
#   nota   -> texto pequeno al pie de la figura (opcional)
#   clave  -> indices de las filas que la figura resalta (la fila que
#             hace teaching); si no se indica, se resaltan las filas que
#             la nota marca en negrita.
#
# Si aparece una tabla de verdad nueva en las notas y no esta aqui, el
# script avisa y no genera nada: hay que registrarla a proposito.
REGISTRO = {
    r"$p$ | $\neg p$": {
        "nombre": "tabla-verdad-negacion",
        "titulo": "Negación",
        "nota": "el valor lógico se invierte siempre",
        "clave": [],
    },
    r"$p$ | $q$ | $p \vee q$": {
        "nombre": "tabla-verdad-disjuncion",
        "titulo": "Disyunción",
        "nota": "solo hay una fila falsa: ambos operandos falsos",
        "clave": [3],
    },
    r"$p$ | $q$ | $p \wedge q$": {
        "nombre": "tabla-verdad-conjuncion",
        "titulo": "Conjunción",
        "nota": "solo hay una fila verdadera: ambos operandos verdaderos",
        "clave": [0],
    },
    r"$p$ | $q$ | $p \veebar q$": {
        "nombre": "tabla-verdad-disjuncion-exclusiva",
        "titulo": "Disyunción exclusiva (XOR)",
        "nota": "verdadera cuando los dos operandos tienen valores distintos",
        "clave": [0],
    },
    r"$p$ | $q$ | $p \rightarrow q$": {
        "nombre": "tabla-verdad-condicional",
        "titulo": "Condicional",
        "nota": "la única fila falsa: antecedente verdadero y consecuente falso",
        "clave": [1],
    },
    r"$p$ | $q$ | $p \leftrightarrow q$": {
        "nombre": "tabla-verdad-bicondicional",
        "titulo": "Bicondicional",
        "nota": "verdadera cuando ambos operandos coinciden",
        "clave": [0, 3],
    },
    r"$p$ | $q$ | $\neg q$ | $p \rightarrow q$ | $\neg(p \rightarrow q)$ | $p \wedge \neg q$": {
        "nombre": "tabla-verdad-negacion-condicional",
        "titulo": "Negación del condicional",
        "nota": "es la columna contraria del condicional, fila por fila",
        "clave": [1],
    },
    r"$p$ | $q$ | $\neg p$ | $\neg q$ | $p \rightarrow q$ | $\neg q \rightarrow \neg p$": {
        "nombre": "tabla-verdad-condicional-contrapositiva",
        "titulo": "Condicional y contrapositiva",
        "nota": "las dos últimas columnas son idénticas: son equivalentes",
        "clave": [],
    },
    r"$p$ | $q$ | $p \rightarrow q$ | $q \rightarrow p$": {
        "nombre": "tabla-verdad-condicional-reciproco",
        "titulo": "Condicional y recíproco",
        "nota": "las columnas difieren: el recíproco NO es equivalente",
        "clave": [1, 2],
    },
    r"$p$ | $q$ | $\neg p$ | $p \rightarrow q$ | $\neg p \vee q$": {
        "nombre": "tabla-verdad-condicional-disjuncion",
        "titulo": "Condicional y disyunción",
        "nota": "columnas idénticas: p → q ≡ ¬p ∨ q",
        "clave": [1],
    },
    r"$p$ | $q$ | $p \leftrightarrow q$ | $p \rightarrow q$ | $q \rightarrow p$ | $(p \rightarrow q) \wedge (q \rightarrow p)$": {
        "nombre": "tabla-verdad-bicondicional-equivalencia",
        "titulo": "Bicondicional y su equivalencia",
        "nota": "la conjunción de los dos condicionales coincide con el bicondicional",
        "clave": [0, 3],
    },
    r"$p$ | $q$ | $\neg p$ | $\neg q$ | $p \veebar q$ | $p \wedge \neg q$ | $q \wedge \neg p$ | $(p \wedge \neg q) \vee (q \wedge \neg p)$": {
        "nombre": "tabla-verdad-disjuncion-exclusiva-equivalencia",
        "titulo": "Disyunción exclusiva: ⊻ y ⊕",
        "nota": "⊻ y ⊕ son el mismo operador",
        "clave": [0],
    },
    r"$p$ | $q$ | $r$ | $p \rightarrow q$ | $(p \rightarrow q) \rightarrow r$ | $q \rightarrow r$ | $p \rightarrow (q \rightarrow r)$": {
        "nombre": "tabla-verdad-tres-proposiciones",
        "titulo": "Tres proposiciones: 2³ = 8 filas",
        "nota": "con n variables la tabla tiene 2ⁿ filas",
        "clave": [5, 7],
    },
    r"$p$ | $\neg p$ | $p \vee \neg p$": {
        "nombre": "tabla-verdad-tautologia",
        "titulo": "Tautología",
        "nota": "siempre verdadera: es una tautología",
        "clave": [],
    },
    r"$p$ | $q$ | $p \rightarrow q$ | $p \wedge (p \rightarrow q)$ | $(p \wedge (p \rightarrow q)) \rightarrow q$": {
        "nombre": "tabla-verdad-modus-ponens",
        "titulo": "Modus ponens",
        "nota": "con premisa verdadera y condicional verdadero, la conclusión es verdadera",
        "clave": [0],
    },
    r"$p$ | $q$ | $r$ | $p \to q$ | $\neg r \lor p$ | $(p\to q)\land(\neg r\lor p)$ | $q \lor r$ | $s$": {
        "nombre": "tabla-verdad-ejercicio-guia1",
        "titulo": "Ejercicio 4 — tabla de verdad",
        "nota": "la fila (F,F,F) da Falso: es una contingencia",
        "clave": [7],
    },
}


# ---------------------------------------------------------------- latex
def _para_mathtext(celda):
    """Traduce el latex de la nota al dialecto que acepta mathtext.

    mathtext no conoce \\lor ni \\land (si \\vee y \\wedge).  El resto
    (\\neg, \\veebar, \\rightarrow, \\leftrightarrow...) se deja igual.
    """
    s = str(celda).strip()
    s = re.sub(r"\\lor(?![a-zA-Z])", r"\\vee", s)
    s = re.sub(r"\\land(?![a-zA-Z])", r"\\wedge", s)
    s = re.sub(r"\\to(?![a-zA-Z])", r"\\rightarrow", s)
    return s


def _peso(texto):
    """Peso relativo de una columna: proporcional a lo que ocupa su texto."""
    limpio = re.sub(r"[$\\{}^_]", "", str(texto))
    return max(1.0, len(limpio) / 4.0)


def _filas_clave(filas):
    """Filas que la nota marca en negrita: son las que la figura resalta."""
    clave = []
    for i, fila in enumerate(filas):
        if any("**" in str(c) for c in fila):
            clave.append(i)
    return clave


def construye_catalogo():
    """Escanea las notas y arma el catalogo de figuras.

    Devuelve (catalogo, huerfanos):
      catalogo  -> {nombre: spec}
      huerfanos -> tablas de verdad de las notas sin figura registrada
    """
    tablas = escanea_tv()
    vistas = {}
    for t in tablas:
        vistas.setdefault(_firma(t["cab"], t["filas"]), t)

    catalogo = {}
    huerfanos = []
    usados = set()
    for cab_norm, meta in REGISTRO.items():
        clave = "|".join(_norm(x) for x in _celdas_cabecera(cab_norm))
        for firma, t in vistas.items():
            if firma.split("#")[0] != clave:
                continue
            spec = {
                "titulo": meta["titulo"],
                "cols": [(_para_mathtext(c), _peso(c)) for c in t["cab"]],
                "filas": [[_norm(c) for c in fila] for fila in t["filas"]],
                "clave": meta.get("clave", _filas_clave(t["filas"])),
                "nota": meta.get("nota", ""),
                "origen": "%s:%d" % (t["archivo"], t["linea"]),
                "firma": _firma(t["cab"], t["filas"]),
            }
            catalogo[meta["nombre"]] = spec
            usados.add(firma)
            break
        else:
            huerfanos.append(("REGISTRO sin tabla en las notas", cab_norm))

    for firma, t in vistas.items():
        if firma not in usados:
            cab = " | ".join(t["cab"])
            huerfanos.append(("TABLA sin figura registrada",
                              "%s (%s:%d)" % (cab, t["archivo"], t["linea"])))
    return catalogo, huerfanos


def _celdas_cabecera(cab):
    """Convierte 'a | b | c' en la lista de celdas (reutiliza el parser)."""
    return _celdas("| " + cab.replace(" | ", " | ") + " |") or \
        [c.strip() for c in cab.split("|")]


CATALOGO, HUERFANOS = construye_catalogo()


# ---------------------------------------------------------------- medicion
# Las cajas de texto se miden en pixeles del lienzo (dpi del canvas = 100),
# no en el dpi de guardado. Las proporciones se conservan al guardar.
DPI_CANVAS = 100.0
PAD = 10          # margen minimo alrededor de cada texto
PAD_FIG = 16      # margen minimo del lienzo


def _ancho_px(texto, fontsize, weight="normal"):
    """Ancho real en px del texto (mathtext incluido).

    El peso importa: el texto en bold es mas ancho que en normal, asi que
    hay que medir EXACTAMENTE como se va a dibujar (o el lienzo queda
    pequeno y el texto se sale)."""
    fig = plt.figure(figsize=(1, 1))
    t = fig.text(0, 0, texto, fontsize=fontsize, fontweight=weight)
    fig.canvas.draw()
    bb = t.get_window_extent(renderer=fig.canvas.get_renderer())
    w = bb.width
    plt.close(fig)
    return w


def _envolver(texto, max_chars):
    """Parte la nota en varias lineas para que no se salga del lienzo."""
    import textwrap
    if not texto:
        return ""
    return "\n".join(textwrap.wrap(texto, max_chars))


def _planificar(spec):
    """Calcula (figsize, anchos_normalizados, fontsize_cab, nota_envuelta)
    midiendo el texto real: nada se sale del lienzo ni se solapa."""
    cols = spec["cols"]
    ncols = len(cols)
    rel = [c[1] for c in cols]
    total_rel = sum(rel)

    # --- ancho de cada cabecera, reduciendo fontsize si hace falta
    #     (se miden en bold: es como se dibujan)
    fs_cab = 13
    anchos_px = [_ancho_px(c[0], fs_cab, "bold") for c in cols]
    ancho_fig = 1.05 + 0.42 * ncols          # pulgadas -> px abajo
    ancho_fig_px = ancho_fig * DPI_CANVAS
    while True:
        necesario = sum(a + 2 * PAD for a in anchos_px) + 2 * PAD_FIG
        if necesario <= ancho_fig_px or fs_cab <= 9:
            break
        fs_cab -= 1
        anchos_px = [_ancho_px(c[0], fs_cab, "bold") for c in cols]
    ancho_fig_px = max(ancho_fig_px, necesario)

    # --- titulo (bold)
    ancho_tit = _ancho_px(spec["titulo"], 15, "bold")
    ancho_fig_px = max(ancho_fig_px, ancho_tit + 2 * PAD_FIG)

    # --- nota al pie: se envuelve hasta que quepa
    nota = spec.get("nota") or ""
    nota_env = nota
    if nota:
        for max_chars in (78, 62, 48, 38):
            nota_env = _envolver(nota, max_chars)
            ancho_nota = max((_ancho_px(l, 9.5) for l in nota_env.split("\n")),
                             default=0)
            if ancho_nota + 2 * PAD_FIG <= ancho_fig_px:
                break
            ancho_fig_px = max(ancho_fig_px, ancho_nota + 2 * PAD_FIG)

    # --- anchos normalizados: cada columna toma lo que necesita su texto,
    #     y el sobrante se reparte segun los pesos relativos
    minimos = [(a + 2 * PAD) / ancho_fig_px for a in anchos_px]
    sobrante = 1.0 - sum(minimos)
    if sobrante > 0:
        for i in range(ncols):
            minimos[i] += sobrante * (rel[i] / total_rel)
    else:
        # no cabe: se reparte a partes iguales entre lo que ya excede
        exceso = sum(minimos) - 1.0
        for i in range(ncols):
            minimos[i] -= exceso * (minimos[i] / sum(minimos))
    anchos = minimos

    # --- alto: la nota envuelta puede ocupar varias lineas
    #     (esto es el alto del CONTENIDO; el lienzo lleva padding alrededor)
    n_lineas_nota = len(nota_env.split("\n")) if nota_env else 0
    h_fila = 0.42
    h_cab = 0.52
    h_tit = 0.62
    h_nota = (0.24 + 0.20 * n_lineas_nota) if nota else 0.0
    alto = h_tit + h_cab + h_fila * len(spec["filas"]) + h_nota

    # El lienzo es mas grande que el contenido: PAD_FIG de aire a cada lado,
    # para que el marco de la tabla NO toque el borde de la imagen (si lo
    # toca, al renderizar la figura parece pegada al texto de al lado).
    figsize = ((ancho_fig_px + 2 * PAD_FIG) / DPI_CANVAS,
               alto + 2 * PAD_FIG / DPI_CANVAS)
    return figsize, anchos, fs_cab, nota_env


def _geometria_figura(figsize):
    """Reparte el lienzo entre el aire exterior y el area de contenido.

    Devuelve (alto_contenido, ancho_contenido_px, alto_total_px,
    ancho_total_px, frac_x, frac_y, frac_w, frac_h), donde frac_* es la
    posicion/tamano del eje dentro del lienzo (para fig.add_axes)."""
    ancho_total_px = figsize[0] * DPI_CANVAS
    alto_total_px = figsize[1] * DPI_CANVAS
    ancho_contenido_px = ancho_total_px - 2 * PAD_FIG
    alto_contenido_px = alto_total_px - 2 * PAD_FIG
    alto_contenido = alto_total_px / DPI_CANVAS - 2 * PAD_FIG / DPI_CANVAS
    return (alto_contenido, ancho_contenido_px, alto_total_px, ancho_total_px,
            PAD_FIG / ancho_total_px, PAD_FIG / alto_total_px,
            ancho_contenido_px / ancho_total_px,
            alto_contenido_px / alto_total_px)


def _color_celda(v):
    """V -> verde, F -> rojo. El resto (numeros, formulas) -> tinta."""
    s = str(v).strip()
    if s in ("V", "v"):
        return EXITO
    if s in ("F", "f"):
        return PELIGRO
    return TINTA


def _es_formula(v):
    return "$" in str(v)


def dibujar(spec, salida=None):
    """Dibuja la tabla. Con `salida` la guarda; sin `salida` solo la
    construye y la devuelve (la usa el QA para medir la geometria)."""
    cols = spec["cols"]
    filas = spec["filas"]
    clave = set(spec.get("clave", []))

    ncols = len(cols)
    figsize, anchos, fs_cab, nota_env = _planificar(spec)

    (alto_cont, _ancho_cont_px, _alto_tot_px, _ancho_tot_px,
     fx, fy, fw, fh) = _geometria_figura(figsize)

    fig = plt.figure(figsize=figsize)
    # El eje ocupa SOLO el area de contenido: el padding queda fuera, en
    # blanco. Asi el marco de la tabla no toca nunca el borde de la imagen.
    ax = fig.add_axes([fx, fy, fw, fh])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # ---- alto por fila (fraccion del lienzo)
    h_fila = 0.42 / alto_cont
    h_cab = 0.52 / alto_cont
    h_tit = 0.62 / alto_cont
    n_lineas_nota = len(nota_env.split("\n")) if nota_env else 0
    h_nota = ((0.24 + 0.20 * n_lineas_nota) / alto_cont) if nota_env else 0.0

    # ---- titulo
    y = 1 - h_tit * 0.25
    ax.text(0.5, y, spec["titulo"],
            ha="center", va="center", fontsize=15, fontweight="bold",
            color=TINTA)

    # ---- Nota al pie
    # Vive DEBAJO del marco de la tabla (es una nota, no una fila) y las
    # lineas de las columnas NO la cruzan: antes bajaban hasta y=0 y le
    # partian el texto en trozos.
    if nota_env:
        ax.text(0.5, h_nota * 0.5, nota_env,
                ha="center", va="center", fontsize=9.5, color=GRIS,
                style="italic", linespacing=1.35)

    # ---- cabecera
    y_cab_sup = 1 - h_tit
    y_cab_inf = y_cab_sup - h_cab
    x = 0.0
    for (etiqueta, _), w in zip(cols, anchos):
        ax.add_patch(plt.Rectangle((x, y_cab_inf), w, h_cab,
                                   facecolor=PASTEL[1], edgecolor="none"))
        ax.text(x + w / 2, (y_cab_sup + y_cab_inf) / 2, etiqueta,
                ha="center", va="center", fontsize=fs_cab, color=ACENTO,
                fontweight="bold")
        x += w

    # ---- filas
    y_sup = y_cab_inf
    for i, fila in enumerate(filas):
        h = h_fila
        y_inf = y_sup - h
        fondo = PASTEL[5] if i in clave else ("#ffffff" if i % 2 == 0 else "#fafafa")
        ax.add_patch(plt.Rectangle((0, y_inf), 1.0, h,
                                   facecolor=fondo, edgecolor="none"))
        x = 0.0
        for j, celda in enumerate(fila):
            if _es_formula(celda):
                ax.text(x + anchos[j] / 2, (y_sup + y_inf) / 2, celda,
                        ha="center", va="center", fontsize=12, color=TINTA)
            else:
                ax.text(x + anchos[j] / 2, (y_sup + y_inf) / 2, celda,
                        ha="center", va="center", fontsize=13,
                        color=_color_celda(celda),
                        fontweight="bold" if i in clave else "normal")
            x += anchos[j]
        y_sup = y_inf

    # ---- bordes
    # El marco abriga solo la tabla (cabecera + filas): el pie queda fuera, con
    # su propio aire, como una nota al pie de verdad.
    ax.add_patch(plt.Rectangle((0, h_nota), 1.0, y_cab_sup - h_nota,
                               fill=False, edgecolor="#9aa4b2", linewidth=1.2))
    ax.plot([0, 1], [y_cab_inf, y_cab_inf], color="#9aa4b2", linewidth=1.0)
    ax.plot([0, 1], [y_sup, y_sup], color="#9aa4b2", linewidth=1.0)
    for j in range(1, ncols):
        x = sum(anchos[:j])
        # de la ultima fila hasta la cabecera: nunca bajan al pie
        ax.plot([x, x], [y_sup, y_cab_sup], color="#d3d9e0", linewidth=0.8)
    for i in range(len(filas) - 1):
        y = y_cab_inf - h_fila * (i + 1)
        ax.plot([0, 1], [y, y], color="#e6e9ed", linewidth=0.7)

    if salida:
        fig.savefig(salida, dpi=DPI, facecolor="white")
        plt.close(fig)
        return None
    return fig


def dibujar_para_auditar(spec):
    """Devuelve la figura viva (sin guardar) para medir su geometria."""
    return dibujar(spec, None)


def escribe_manifiesto():
    """Mapa tabla -> figura, en JSON.

    Lo lee qa_formato_matdisc.py (R17) para comprobar que la figura que
    esta embebida encima de cada tabla es LA de esa tabla, no otra.
    """
    import json
    datos = {
        "figuras": {
            spec["firma"]: {
                "nombre": nombre,
                "titulo": spec["titulo"],
                "origen": spec["origen"],
            }
            for nombre, spec in CATALOGO.items()
        },
    }
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "tablas_verdad.json")
    with io.open(ruta, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(datos, ensure_ascii=False, indent=2,
                           sort_keys=True))
        f.write("\n")
    return ruta


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true", help="solo lista, no escribe")
    ap.add_argument("--solo", help="genera una sola tabla por nombre")
    ap.add_argument("--check", action="store_true",
                    help="solo audita el catalogo contra las notas")
    args = ap.parse_args()

    destino = carpeta_destino()

    if HUERFANOS:
        print("!! DESAJUSTE CATALOGO <-> NOTAS")
        for que, detalle in HUERFANOS:
            print("   %s: %s" % (que, detalle))
        if not args.check:
            return 1

    nombres = [args.solo] if args.solo else sorted(CATALOGO)
    if args.solo and args.solo not in CATALOGO:
        print("NO existe en el catalogo:", args.solo)
        print("disponibles:", ", ".join(sorted(CATALOGO)))
        return 1

    if args.check:
        for nombre in nombres:
            spec = CATALOGO[nombre]
            print("OK   %-44s %s  %d filas x %d col"
                  % (nombre, spec["origen"], len(spec["filas"]), len(spec["cols"])))
            for i in spec["clave"]:
                print("       fila clave %d: %s" % (i, " | ".join(spec["filas"][i])))
        print("---- figuras: %d, desajustes: %d" % (len(nombres), len(HUERFANOS)))
        return 1 if HUERFANOS else 0

    os.makedirs(destino, exist_ok=True)
    for nombre in nombres:
        spec = CATALOGO[nombre]
        salida = os.path.join(destino, nombre + ".png")
        if args.dry:
            print("DRY  %-44s -> %s   (%s)" % (nombre, salida, spec["origen"]))
            continue
        dibujar(spec, salida)
        kb = os.path.getsize(salida) / 1024.0
        print("OK   %-44s %7.1f KB  %s" % (nombre, kb, spec["origen"]))
    man = escribe_manifiesto()
    print("manifiesto: %s" % man)
    return 0


if __name__ == "__main__":
    sys.exit(main())
