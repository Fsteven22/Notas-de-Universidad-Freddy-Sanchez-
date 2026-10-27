---
dg-publish: false
tags: [clippings, log, opencode]
---

# LOG - opencode (sesion 2026-10-27)

> Bitacora de la sesion abierta el 2026-10-27. Escribe aqui que estas
> tocando y que comitteaste, para que los otros agentes no dupliquen
> trabajo ni pisen cambios.

## Estado: EN CURSO

### Archivos que estoy tocando (no editar sin avisar)

| Ruta | Que hago |
|---|---|
| `Universidad/3er Semestre/**` | Links rotos: 4 BAD reales (3 de Ingles III + 1 vacio en BD) |
| `Universidad/Herramientas/Mantenimiento/**` | Posible fix al resolutor de `qa_links.py` |
| `Clippings/LOG-opencode.md` | Esta bitacora |

### Temas que NO voy a tocar

- `Universidad/2do Semestre/Calculo Vectorial/**`: hay otro agente rehaciendo esas notas (commits paralelos visibles).
- `Universidad/1er Semestre/**`: 469 BAD de wikilinks, preexistentes, fuera del alcance de esta sesion.
- `Universidad/Preuniversitario/**`: 27 BAD, preexistentes.
- `Universidad/Herramientas/SVG-Pipeline/**`: previews ya ignorados por git.

## Commits de esta sesion

| Commit | Alcance |
|---|---|
| `955c52f` | `refactor(vault)`: vaciar `Universidad/Diagramas/` (438 SVG sueltos) |
| `ef329c8` | `fix(1er, 2do y preuniversitario)`: wikilinks rotos, orden de embeds, PDFs |
| `7fa326a` | `feat(3er semestre)`: 14 tablas a callouts, 74 paginas de decks a PNG, 8 PDFs huerfanos enlazados |
| `5c75f95` | `feat(site)`: `_no-publicar.txt` (13 archivos con copyright fuera del build) |
| `86aa483` | `fix(FESD)`: 2 embeds de portada con ruta `../../Diagramas/` |
| `99d8c22` | `docs(Clippings)`: abrir esta bitacora |
| `8fedc9f` | (otro agente) merge de `origin/master`; integró mis commits |

## Hallazgos que le sirven a otros agentes

1. **`qa_links.py` hay que correrlo con root=`Universidad`, no con la carpeta del semestre.** Con root=`3er Semestre` marca como BAD los embeds a `Universidad/Figuras/` y a notas de otros semestres, que si resuelven. Con root=`Universidad`: 3er semestre = 0 BAD, no 40.
2. Las imagenes de `Universidad/Figuras/` (`Pasted image *.png`, `ChatGPT Image *.png`, `venn-*.png`, `g5-ej*.png`, `U2-*.png`) existen y resuelven por basename. No borrarlas.
3. Los SVG de `Universidad/Diagramas/` se movieron a `Diagramas/` dentro de cada materia (commit `955c52f`). Los embeds con prefijo `Diagramas/` siguen funcionando.
4. `verificar_nota.py` sobre las 174 notas del 3er semestre da **0 errores**. En 1er/2do/Preuniversitario quedan ~600 (casi todos `ENDINGS mixed` y lineas vacias dentro de fences en callout).
5. Hay un `image.png` adjunto con la lista de errores que el usuario menciono, pero **no existe en disco**. El catalogo real de los 7 tipos de error esta en `Universidad/Herramientas/README.md` y en `detect_fuera_callouts.py`.
6. **El separador de alias dentro de una tabla lleva UN solo backslash**: `[[nota\|alias]]`. Con doble escape el wikilink no resuelve. Corregidos 10 casos en los syllabus de DSW, FESD, Ingles III y BD.

## Tarea en curso

**4 BAD reales del 3er semestre: resueltos (queda 0).**

1. `Speaking Practice` x3 (Ingles III) -> no habia nada roto en las notas: los links ya apuntaban a `Speaking Practice # 1`, y el BAD era un bug del regex de `qa_links.py`, que cortaba el target en el primer `#`.
2. Link vacio `[[ ]]` en `Sistema de Bases de Datos/Unidad 1 - Modelos de Datos y ER/03 - Modelo relacional, ERM y casos Tiny College.md`: era notacion Chen explicada en prosa. Ahora dice "rectangulo = entidad (doble rectangulo = debil)".

### Fix al resolutor de `qa_links.py`

El regex `\[\[([^\]|#]+)` cortaba el target en el primer `#` y en la primera `|`, asi que:
- `[[Speaking Practice # 1]]` se leia como `Speaking Practice` -> falso BAD.
- `[[nota\|alias]]` (tabla) se leia como `nota\` -> falso BAD.

Ahora separa destino y alias correctamente (la `|` escapada en tabla tambien es separador de alias en Obsidian) y solo trata el `#` como ancla cuando el nombre completo no existe. Se agrego `partir_alias()`.

Resultado en el vault: **1075 -> 1039 BAD**, y el 3er semestre queda en **0**. Ningun semestre subio de conteo. Test sintetico con 10 casos edge en `C:\Users\STEVEN~1\AppData\Local\Temp\opencode\test_qa.py`.

### Incidente: script de escapes multiples mal acotado

> [!warning] Para los otros agentes
> Corri un regex `(\\\\|)+\|` sobre TODO el vault y cambio 104,938 ocurrencias, incluyendo LaTeX donde `\\|` es salto de linea + barra de valor absoluto. El merge `ca4ab56` lo revirtio antes de que llegara a un commit, asi que no hay nada que revertir en el historial.
>
> **Regla**: los cambios masivos de formato se hacen con un fixer que Dry-run por defecto (los de `Universidad/Herramientas/Mantenimiento/` ya lo hacen) y acotados a un patron inequivoco, nunca con un regex global aplicado a disco. Si hay duda del alcance, primero en un subcarpeta y se revisa el diff.
>
> El fix final si fue quirurgico: 5 archivos, 10 lineas, solo dentro de `[[...]]` en lineas de tabla.

---
**Tags:** #clippings #log #opencode
