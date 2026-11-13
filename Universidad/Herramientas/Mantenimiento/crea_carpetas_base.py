"""Crea las carpetas base de material en todas las materias del vault.

Git no trackea carpetas vacias: sin un archivo dentro, desaparecen en el
siguiente clone. Por eso cada carpeta nueva lleva un `.gitkeep` vacio
(estandar de git) y un `_texto.md` no: el unico archivo que se crea es el
`.gitkeep`.

La carpeta base de cada materia es `Unidad 0 - Guias y Ejercicios` (la que ya
usa la casa). No se toca ningun archivo existente: solo se crean directorios
nuevos.
"""

import io
import os
import sys

BASE = [
    "Archivos",
    "Diagramas",
    "Diapositivas",
    "Exámenes",
    "Lecciones",
    "Material de clase",
    "Talleres",
]
# La carpeta base de material. La casa usa "Unidad 0 - Guias y Ejercicios";
# las materias que nombran sus unidades en ingles (MOOC de Ingles) usan
# "Unit 0 - Foundations". Se detectan por nombre, no por numero.
CARPETAS_BASE = ("Unidad 0 - Guias y Ejercicios", "Unit 0 - Foundations")
V = sys.argv[1] if len(sys.argv) > 1 else "."
DRY = "--dry" in sys.argv


def carpeta_base(mp):
    """Ruta de la carpeta base de una materia, o None si no tiene."""
    for c in CARPETAS_BASE:
        d = os.path.join(mp, c)
        if os.path.isdir(d):
            return d
    return None


def materias(root):
    """(semestre, materia, ruta) de las materias reales del vault."""
    out = []
    uni = os.path.join(root, "Universidad")
    for sem in sorted(os.listdir(uni)):
        sp = os.path.join(uni, sem)
        if not os.path.isdir(sp):
            continue
        for mat in sorted(os.listdir(sp)):
            mp = os.path.join(sp, mat)
            if not os.path.isdir(mp):
                continue
            # Herramientas no es materia: es la caja de las herramientas.
            if sem == "Herramientas":
                continue
            out.append((sem, mat, mp))
    return out


def main():
    creadas = 0
    ya_existian = 0
    saltadas = []
    for sem, mat, mp in materias(V):
        u0 = carpeta_base(mp)
        if u0 is None:
            saltadas.append((sem, mat, "sin carpeta base (ni 'Unidad 0 - Guias y Ejercicios' ni 'Unit 0 - Foundations')"))
            continue
        nuevas = []
        for b in BASE:
            d = os.path.join(u0, b)
            if os.path.isdir(d):
                ya_existian += 1
                continue
            nuevas.append(b)
        if not nuevas:
            continue
        if not DRY:
            for b in nuevas:
                d = os.path.join(u0, b)
                os.makedirs(d, exist_ok=True)
                # .gitkeep: git no trackea carpetas vacias.
                with open(os.path.join(d, ".gitkeep"), "w", encoding="utf-8"):
                    pass
        creadas += len(nuevas)
        print(f"  {sem} / {mat}")
        print(f"      + {', '.join(nuevas)}")

    print()
    print(f"carpetas creadas: {creadas}   ya existian: {ya_existian}")
    if saltadas:
        print("materias saltadas:")
        for s, m, r in saltadas:
            print(f"  {s} / {m}  ({r})")


if __name__ == "__main__":
    main()
