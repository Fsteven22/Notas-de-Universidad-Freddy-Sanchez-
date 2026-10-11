"""Estilo global para figuras del vault (Obsidian + Digital Garden).

Uso:
    from estilo import setup, guardar
    setup()
    ... dibujar ...
    guardar("nombre.png")
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Paleta pastel (misma identidad que los callouts del vault)
PASTEL = ["#ffe1e1", "#e1e1ff", "#e1ffe1", "#fff4e1", "#f0e1ff", "#e1fff4"]
ACENTO = "#2c5aa0"
PELIGRO = "#e74c3c"
EXITO = "#1e8449"
TINTA = "#1a1a1a"
GRIS = "#888888"

DPI = 150


def setup():
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.size": 11,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.edgecolor": "#444444",
        "text.color": TINTA,
        "axes.labelcolor": TINTA,
        "xtick.color": TINTA,
        "ytick.color": TINTA,
    })


def guardar(nombre, fig=None, carpeta=None):
    import os
    if carpeta is None:
        carpeta = r"C:\Users\Steven Sànchez\OneDrive\OneSyncFiles\Universidad\Figuras"
    os.makedirs(carpeta, exist_ok=True)
    (fig or plt).savefig(f"{carpeta}\\{nombre}", dpi=DPI, bbox_inches="tight")
    if fig is None:
        plt.close()
