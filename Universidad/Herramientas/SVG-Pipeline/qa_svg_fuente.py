# -*- coding: utf-8 -*-
"""QA de la fuente incrustada de los SVG.

Comprueba dos cosas en cada SVG con tipografia incrustada:

  1. COBERTURA: que todo caracter que el diagrama muestra Y que la fuente incrustada
     declara en su `unicode-range` este de verdad en la fuente (cmap). Si alguien edita
     un SVG a mano y anade una etiqueta con un caracter que la fuente ya no trae, ese
     glifo se dibujaria con la tipografia del sistema y el diagrama se veria "raro".
     Ojo: los emoji y simbolos que NUNCA estuvo en la fuente (✅ ❌ →) se dibujan con la
     tipografia del sistema a proposito: no cuentan como fallo.
  2. PESO: si el SVG todavia lleva la tipografia completa (4 subconjuntos, ~160 KB de
     base64) en vez de la recortada (~14 KB). Senal de que hay que pasarlo por
     `subconjuntar_fuente.py`.

Uso:
  py -3.12 qa_svg_fuente.py <raiz> [-o SALIDA] [--solo-pesados]

Devuelve 1 si hay problemas de cobertura, 0 si no.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subconjuntar_fuente import (codepoints_visibles, leer_marca,  # noqa: E402
                                  reglas_fuente)

try:
    from fontTools.ttLib import TTFont
except ImportError:
    print("FALTA fontTools: py -3.12 -m pip install fonttools brotli")
    raise SystemExit(2)

RAIZ_POR_DEFECTO = os.environ.get("VAULT_ROOT") or os.path.join(
    os.path.expanduser("~"), "OneDrive", "OneSyncFiles")

PESADO = 40 * 1024  # bytes de base64: por encima, la fuente viene completa


def revisar(svg):
    """Devuelve el informe del SVG o None si no lleva fuente incrustada."""
    reglas = reglas_fuente(svg)
    if not reglas:
        return None
    usados = codepoints_visibles(svg)

    # caracteres que la fuente DECLARA (por su unicode-range) y que el diagrama usa
    declarados = set()
    for r in reglas:
        for c in usados:
            if any(a <= c <= b for a, b in r["ranges"]):
                declarados.add(c)

    # caracteres que la fuente REALMENTE trae (cmap)
    disponibles = set()
    for r in reglas:
        try:
            font = TTFont(io.BytesIO(r["raw"]))
            disponibles |= set(font.getBestCmap().keys())
        except Exception:
            disponibles |= {c for a, b in r["ranges"] for c in usados if a <= c <= b}

    # huecos preexistentes: glifos que la fuente original NO traia (emoji, flechas, ZWJ...)
    # y que el diagrama dibuja con la tipografia del sistema a proposito. El recorte los
    # registra en el SVG (`/*fuente-sin-glifo:U+XXXX*/`), asi que no son un fallo.
    huecos = leer_marca(svg)

    faltantes = sorted(c for c in declarados if c not in disponibles and c not in huecos)
    bytes_fuente = sum(len(r["b64"]) for r in reglas)
    return {
        "reglas": len(reglas),
        "bytes_fuente": bytes_fuente,
        "glifos_usados": len(usados),
        "declarados": len(declarados),
        "faltantes": [chr(c) for c in faltantes],
        "huecos": [chr(c) for c in sorted(huecos)],
        "pesado": bytes_fuente > PESADO,
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    raiz = args[0] if args else RAIZ_POR_DEFECTO
    salida = None
    if "-o" in sys.argv:
        salida = sys.argv[sys.argv.index("-o") + 1]
    solo_pesados = "--solo-pesados" in sys.argv

    svgs = []
    if os.path.isfile(raiz):
        svgs.append(raiz)
    else:
        for dp, ds, fs in os.walk(raiz):
            ds[:] = [d for d in ds if d not in (".git", "node_modules", "dist", "site")]
            for f in fs:
                if f.lower().endswith(".svg"):
                    svgs.append(os.path.join(dp, f))
    svgs.sort()

    problemas, pesados, ok = [], [], 0
    n_huecos = 0
    for p in svgs:
        try:
            svg = io.open(p, encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        r = revisar(svg)
        if r is None:
            continue
        rel = os.path.relpath(p, raiz)
        if r["huecos"]:
            n_huecos += 1
        if r["faltantes"]:
            problemas.append({"archivo": rel, "faltantes": r["faltantes"],
                              "glifos": r["glifos_usados"], "bytes_fuente": r["bytes_fuente"]})
        elif r["pesado"]:
            pesados.append({"archivo": rel, "bytes_fuente": r["bytes_fuente"],
                            "reglas": r["reglas"], "glifos": r["glifos_usados"]})
        else:
            ok += 1

    print("SVG revisados: %d" % len(svgs))
    print("  con fuente recortada (ok)      : %d" % ok)
    print("  con la fuente completa (pesados): %d" % len(pesados))
    print("  con glifos declarados y ausentes: %d" % len(problemas))
    print("  con huecos preexistentes de la fuente (ok, documentados): %d" % n_huecos)
    if pesados and not solo_pesados:
        print("\n-- pesados (pasarlos por subconjuntar_fuente.py) --")
        for x in pesados[:10]:
            print("   %8d B  %s" % (x["bytes_fuente"], x["archivo"][-84:]))
        if len(pesados) > 10:
            print("   ... y %d mas" % (len(pesados) - 10))
    if problemas:
        print("\n-- FALLO: caracteres que la fuente declara pero no trae --")
        for x in problemas[:20]:
            print("   %s  ->  %s" % (x["archivo"][-84:], " ".join(x["faltantes"])))

    if salida:
        io.open(salida, "w", encoding="utf-8", newline="\n").write(json.dumps(
            {"raiz": raiz, "svg_revisados": len(svgs), "ok": ok,
             "pesados": pesados, "problemas": problemas}, ensure_ascii=False, indent=2))
        print("\nreporte: %s" % salida)

    return 1 if problemas else 0


if __name__ == "__main__":
    raise SystemExit(main())
