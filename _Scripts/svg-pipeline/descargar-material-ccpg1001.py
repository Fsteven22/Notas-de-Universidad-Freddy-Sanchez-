import os, urllib.request, urllib.parse, json, io
here = os.path.dirname(os.path.abspath(__file__))
items = [
("Módulo 1  - Introducción y Ambientes de Programación", "1.1 Programación y su relevancia.pdf", "CCPG1001-Slides-1.1 Programación y su relevancia.pdf"),
("Módulo 1  - Introducción y Ambientes de Programación", "1.2 Introducción a Python.pdf", "CCPG1001-Slides-1.2 Introducción a Python.pdf"),
("Módulo 1  - Introducción y Ambientes de Programación", "Políticas del curso.pdf", "CCPG1001-Políticas del curso.pdf"),
("Módulo 1  - Introducción y Ambientes de Programación", "ponderacion.png", "fp-ponderacion.png"),
("Módulo 2 - Tipos de datos, operadores, cadenas, listas y aleatoriedad", "2.1 Variables y tipos de datos.pdf", "CCPG1001-Slides-2.1 Variables y tipos de datos.pdf"),
("Módulo 2 - Tipos de datos, operadores, cadenas, listas y aleatoriedad", "2.2 Operaciones con datos y variables.pdf", "CCPG1001-Slides-2.2 Operaciones con datos y variables.pdf"),
("Módulo 2 - Tipos de datos, operadores, cadenas, listas y aleatoriedad", "2.3 Listas.pdf", "CCPG1001-Slides-2.3 Listas.pdf"),
("Módulo 2 - Tipos de datos, operadores, cadenas, listas y aleatoriedad", "2.4 Aleatoriedad.pdf", "CCPG1001-Slides-2.4 Aleatoriedad.pdf"),
("Módulo 3 - Funciones", "3.1 Funciones.pdf", "CCPG1001-Slides-3.1 Funciones.pdf"),
("Módulo 4 - Estructuras de control", "4.1 Condicional.pdf", "CCPG1001-Slides-4.1 Condicional.pdf"),
("Módulo 4 - Estructuras de control", "4.2 Iteradores for.pdf", "CCPG1001-Slides-4.2 Iteradores for.pdf"),
("Módulo 4 - Estructuras de control", "4.3 Bucle While.pdf", "CCPG1001-Slides-4.3 Bucle While.pdf"),
("Módulo 5 - Diccionarios", "5.1 Diccionarios.pdf", "CCPG1001-Slides-5.1 Diccionarios.pdf"),
("Módulo 5 - Diccionarios", "5.2 Iterar diccionarios.pdf", "CCPG1001-Slides-5.2 Iterar diccionarios.pdf"),
("Módulo 6 - Pandas", "6.1 Introducción a Numpy.pdf", "CCPG1001-Slides-6.1 Introducción a Numpy.pdf"),
("Módulo 6 - Pandas", "6.2 Intro a Pandas.pdf", "CCPG1001-Slides-6.2 Intro a Pandas.pdf"),
("Módulo 6 - Pandas", "6.3 Manipulación de datos.pdf", "CCPG1001-Slides-6.3 Manipulación de datos.pdf"),
("Módulo 6 - Pandas", "6.4 Limpieza de datos.pdf", "CCPG1001-Slides-6.4 Limpieza de datos.pdf"),
]
base_fp = os.path.join(os.environ["USERPROFILE"], "OneDrive", "OneSyncFiles", "Universidad", "1er Semestre", "Fundamentos de Programación")
dest_dir = os.path.join(base_fp, "Unidad 0 - Guias y Ejercicios")
fig_dir = os.path.join(os.environ["USERPROFILE"], "OneDrive", "OneSyncFiles", "Universidad", "Figuras")
log = []
for folder, fname, dname in items:
    segs = ["CarlosCedeniio", "FP-CCPG1043", "main"] + folder.split("/") + fname.split("/")
    url = "https://raw.githubusercontent.com/" + "/".join(urllib.parse.quote(s) for s in segs)
    dest = os.path.join(dest_dir if dname != "fp-ponderacion.png" else fig_dir, dname)
    try:
        urllib.request.urlretrieve(url, dest)
        log.append("OK   %8d  %s" % (os.path.getsize(dest), dname))
    except Exception as ex:
        log.append("FAIL %s :: %r" % (dname, ex))
io.open(os.path.join(here, "dl.txt"), "w", encoding="utf-8").write("\n".join(log))
print("done", len([l for l in log if l.startswith("OK")]))
