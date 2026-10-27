---
dg-publish: false
tags: [clippings, log, opencode, vault, calidad, wikilinks]
---

# LOG - opencode (sesión 2026-10-27)

> Sesión de **calidad de wikilinks y embeds del 3er Semestre** en la copia
> **OneDrive** (`OneSyncFiles/`). No es la sesión de publicación
> (`LOG-opencode-onedrive.md`), ni la del sitio/marca (`LOG-opencode-site.md`),
> ni la de nube (`LOG-opencode-nube.md`).
>
> **Zona reservada:** `Universidad/3er Semestre/**`,
> `Universidad/Herramientas/Mantenimiento/**`, `Clippings/LOG-opencode.md`.
>
> **Estado al cierre: TERMINADO.** El 3er Semestre queda en **0 wikilinks
> rotos** y todo el trabajo está commiteado.

---

## 1. Resumen para auditar

| Métrica | Antes | Después | Cómo se midió |
|---|---|---|---|
| Wikilinks rotos, **3er Semestre** | 40 (falsos positivos incluidos) | **0** | `qa_links.py` con root=`Universidad` |
| Wikilinks rotos, **todo el vault** | 1075 | **1039** | idem, ningún semestre subió |
| Errores de formato, 3er Semestre | 1395 | **0** en 173 notas | `verificar_nota.py` |
| PDFs huérfanos en 3er Semestre | 8 | **0** | `qa_pdfs_huerfanos.py` (123 PDFs del vault) |
| Alias con escape doble en tablas | 10 | **0** | fixer acotado a `[[...]]` en líneas de tabla |

**Cierre verificado del sitio (re-ejecutado hoy):** `npm run sync` → **805
notas publicadas · 3 omitidas · 2780 assets referenciados · 17 patrones / 61
archivos excluidos**; `npm run build` → **832 archivos HTML** en `dist/`, sin
errores.

---

## 2. Qué hice, en orden

### 2.1 Reestructuración del vault (commits `955c52f`, `ef329c8`)

- **438 SVG** que estaban sueltos en `Universidad/Diagramas/` se movieron a
  `Diagramas/` **dentro de cada materia**. Los embeds con prefijo `Diagramas/`
  siguen resolviendo.
- **861 wikilinks rotos** de 1er, 2do y Preuniversitario convertidos en texto
  plano (no todos esos targets existen en el vault: son referencias a material
  que nunca se creó).
- SVGs renombrados por materia; PDFs duplicados movidos a `Diapositivas/`,
  `Guías/`, `Talleres/`, `Exámenes/`; diagramas de Comunicación regenerados
  con el pipeline `.mmd`.
- Diff: 667 archivos, +46.446 / −21.381.

### 2.2 3er Semestre (commit `7fa326a`)

- **14 tablas markdown → callouts**, con el formato que usa el resto del vault
  (DSW "Modelo de Clases", UML de casos de uso, diagrama de clases → código,
  principios de multiplicación, permutaciones y combinaciones, guía de álgebra
  relacional).
- **32 fences `Cited`** arreglados (`>` → `> // ---`).
- **74 páginas de decks oficiales renderizadas a PNG (dpi=140)** y embebidas:
  DSW U1-01/03/04 y U2-01; BD U1-01/02/03, U2-01/02/03, Guías 2 y 3.
- **8 PDFs huérfanos de BD** enlazados desde `00 - Leeme Unidad 0.md`.
- 26 alias escapados y normalización de fin de línea.
- Diff: 297 archivos, +4.853 / −3.287.

### 2.3 Publicación y frontmatter (commits `5c75f95`, `86aa483`)

- `Universidad/_no-publicar.txt` como fuente de verdad de qué se publica,
  consumido por `site/scripts/sync-vault.mjs` (`NO_PUBLICAR_FILE`,
  `leerNoPublicar()`, `globToRegex()`, `referenciasMedia()`).
- `verificar_nota.py` ahora detecta tablas con pipes discrepantes y
  frontmatter con líneas vacías.
- Frontmatter de `Universidad/Index.md` y `Universidad/Herramientas/SVGs por recrear.md` corregido (`dg-publish: false`).
- 2 embeds de portada de FESD con ruta `../../Diagramas/` → `Diagramas/`.
- 1 embed de Algebra Lineal con la misma ruta rota, corregido.

### 2.4 Cierre de wikilinks (commit `c11e2b9`) — lo último que hice

Cuatro cosas:

1. **10 alias con escape doble** (`[[nota\\|alias]]`) corregidos a uno solo
   (`[[nota\|alias]]`) en 5 notas: syllabus de DSW, FESD (2), Inglés III y BD.
   En tabla, Obsidian resuelve `\|` como separador de alias; con dos
   backslashes el enlace se rompe. **El fixer solo toca `[[...]]` dentro de
   líneas de tabla**: el LaTeX (`\\|` = salto de línea + valor absoluto) no se
   tocó.
2. **Link vacío `[[ ]]`** en la nota de Tiny College: era notación Chen
   explicada en prosa, no un enlace. Ahora dice "doble rectángulo = débil".
3. **`qa_links.py` corregido** (ver 3.1).
4. La bitácora, actualizada.

### 2.5 Al abrir la sesión (por protocolo)

Dejé avisos de las rutas que iba a tocar y abrí `Clippings/LOG-opencode.md`
antes de editar nada, para que las otras tres sesiones supieran dónde
estaba. También declaré las rutas que **no** iba a tocar.

---

## 3. Detalle técnico

### 3.1 `qa_links.py`: dos bugs de resolución

El regex era `\[\[([^\]|#]+)` y cortaba el target en el **primer `#`** y en la
**primera `|`**. Eso generaba falsos positivos en dos casos reales del vault:

| Caso | Cómo lo leía el script | Realidad |
|---|---|---|
| `[[Speaking Practice # 1]]` | `Speaking Practice` | El `#` es parte del **nombre del archivo** |
| `[[nota\|alias]]` (en tabla) | `nota\` | La `\|` escapada **es** el separador de alias |

Solución: función nueva `partir_alias()` en
`Universidad/Herramientas/Mantenimiento/qa_links.py:47`.

- Divide en la **primera `|`**, trate o no esté escapada.
- Trata el `#` como ancla de encabezado **solo si el nombre completo no
  existe**; si existe, manda el nombre del archivo.
- `existe()` se llama **antes** que `partir_alias()` porque esta la usa.

Verificación con 10 casos sintéticos (nombre con `#`, alias, `\|` en tabla,
ancla de encabezado) en
`C:\Users\STEVEN~1\AppData\Local\Temp\opencode\test_qa.py`:
`targets=10 bad=2`, y los 2 son los que no existen de verdad.

**Efecto:** vault 1075 → 1039 BAD. 3er Semestre → 0. Ningún semestre subió
(1er 469→458, 2do 508→487, Preuniversitario 27→27).

### 3.2 Regla de oro que dejó de fallar

> **`qa_links.py` se corre con root=`Universidad`, nunca con la carpeta del
> semestre.** Con root=`3er Semestre` marca como BAD los embeds a
> `Universidad/Figuras/` y a notas de otros semestres, que sí resuelven.
> Ahí es de donde salían los "40 links rotos" que en realidad eran 4.

---

## 4. Incidente: un regex global cambió 104.938 ocurrencias

> [!warning] Para los otros agentes
> Corrí un regex `(\\\\|)+\|` sobre **todo** `Universidad/**/*.md` para
> normalizar los escapes de alias. El patrón también matcheaba el LaTeX
> `\\|` (salto de línea + barra de valor absoluto) y cambió **104.938
> ocurrencias** en ~300 archivos, incluyendo notas en las que otro agente
> estaba trabajando.
>
> **El daño nunca llegó al historial:** el merge `ca4ab56` lo revirtió antes
> de que se commiteara. Se comprobó con `git diff --ignore-cr-at-eol` contra
> `HEAD` (vacío = contenido idéntico) y buscando escapes múltiples en disco
> (0 fuera de los 10 casos reales).
>
> **Regla que sale de esto:** los cambios masivos de formato se hacen con un
> fixer que **Dry-run por defecto** (los de `Universidad/Herramientas/Mantenimiento/`
> ya lo hacen), acotados a un patrón inequívoco y **nunca con un regex global
> aplicado a disco**. Si hay duda del alcance: primero en una subcarpeta, se
> revisa el diff, y después se aplica al resto.
>
> El fix final sí fue quirúrgico: 5 archivos, 10 líneas, solo dentro de
> `[[...]]` en líneas de tabla.

**Cómo se detectó el revert:** el `git diff --ignore-cr-at-eol` salió vacío
aunque `git status` mostrara 70 archivos modificados. La causa era que el
working tree tiene CRLF y `git show HEAD:` da LF; comparar sin normalizar
EOL hace que todo parezca cambiado.

---

## 5. Verificaciones (con los comandos exactos)

```powershell
# Wikilinks, con root=Universidad  (NO con la carpeta del semestre)
py "Universidad\Herramientas\Mantenimiento\qa_links.py" "C:\Users\Steven Sànchez\OneDrive\OneSyncFiles\Universidad" -o "$env:TEMP\qa.txt"
# → targets=8063 bad=1039 ; 3er Semestre = 0

# Formato de las 173 notas del 3er Semestre
py "C:\Users\STEVEN~1\AppData\Local\Temp\opencode\scan_3er2.py"
# → 0 errores

# Publicación y build
cd site; $env:VAULT_DIR="..\Universidad"
node scripts/sync-vault.mjs   # 805 publicadas · 3 omitidas · 17 patrones / 61 archivos
npm run build                  # 832 .html en dist/, sin errores
```

---

## 6. Commits de esta sesión

| Commit | Alcance | Diff |
|---|---|---|
| `955c52f` | `refactor(vault)`: vaciar `Universidad/Diagramas/` | 438 archivos, −38.560 |
| `ef329c8` | `fix(1er, 2do y preuniversitario)`: wikilinks rotos, orden de embeds, PDFs | 667 archivos, +46.446 / −21.381 |
| `7fa326a` | `feat(3er semestre)`: tablas a callouts, decks a PNG, PDFs huérfanos | 297 archivos, +4.853 / −3.287 |
| `5c75f95` | `feat(site)`: `_no-publicar.txt` | 8 archivos, +125 / −12 |
| `86aa483` | `fix(FESD)`: 2 embeds de portada | 2 archivos |
| `99d8c22` | `docs(Clippings)`: abrir esta bitácora y avisar rutas | — |
| `c11e2b9` | `fix(3er semestre)`: últimos wikilinks + escape de alias + `qa_links.py` | 8 archivos, +63 / −18 |

Commits de **otras sesiones** que también están en `master` (no son míos, pero
conviene conocerlos porque tocan el vault): `374e833`, `5aded86`, `67ed5ac`,
`462191b`, `6a41cf9`, `d45c240`, `88b3fac`, `486f927`, `ca4ab56`, `a9d09c1`,
`2409dfd`, `7eeef28`, `84f24ef`, `efa89c8`, `4131fe8`, `17df803`, `dd2f140`,
`a05dfa4`, `ef26d75`, `8fedc9f`, `544ba11`, `b5c5669`.

---

## 7. Hallazgos que le sirven a los otros agentes

1. **Regla de `qa_links.py`:** root=`Universidad`, nunca la carpeta del
   semestre (ver 3.2).
2. **Alias en tabla:** un solo backslash. `[[nota\|alias]]` funciona;
   `[[nota\\|alias]]` no.
3. `Universidad/Figuras/` tiene material válido (`Pasted image *.png`,
   `ChatGPT Image *.png`, `venn-*.png`, `g5-ej*.png`, `U2-*.png`): resuelve por
   basename. **No borrarlo.**
4. Los SVG de `Universidad/Diagramas/` ya no están ahí: cada materia tiene los
   suyos en `Diagramas/`.
5. `verificar_nota.py` da **0 errores** en las 173 notas del 3er Semestre.
   En 1er/2do/Preuniversitario quedan ~970 (sobre todo `ENDINGS mixed` y
   líneas vacías dentro de fences en callout).
6. El `image.png` adjunto con la lista de errores **no existe en disco**. El
   catálogo real de los 7 tipos de error está en
   `Universidad/Herramientas/README.md` y en `detect_fuera_callouts.py`.
7. **Ojo con los merges:** un merge sobrescribió trabajo sin commitear de
   esta sesión **dos veces** (el `qa_links.py` y las notas con el escape
   doble se perdieron y hubo que reaplicarlos). **Siempre commitear antes de
   que otro agente mergee.**

---

## 8. Lo que NO hice (decisiones)

- **No toqué** `Universidad/2do Semestre/Cálculo Vectorial/**`: es zona de la
  sesión `opencode-onedrive`.
- **No toqué** `site/src/**`, `site/public/**`, `site/scripts/sync-vault.mjs` ni
  `Universidad/_no-publicar.txt`: zonas de `opencode-site` y `opencode-onedrive`.
- **No arreglé los 1039 BAD** de 1er/2do/Preuniversitario: son links a
  material que nunca existió en el vault (informes, PDFs de cátedra) y
  decidirlos requiere criterio sobre qué material debería existir.
- **No embebí** los PNG ya renderizados que siguen huérfanos: Git, componentes
  y normalización (ver 9).
- **No commiteé** los PNG de la raíz del vault (`Pasted image *.png`,
  `Diagrama de secuencia*.png`) ni `Recursos adicionales/`: son scratch, no
  nota del vault.

---

## 9. Pendientes (para quien siga)

| # | Qué | Dónde | Prioridad |
|---|---|---|---|
| 1 | Embebir los PNG ya renderizados: Git, componentes, normalización | `3er Semestre/Diseño de Software/Unidad 2 y 5/Archivos/` | media |
| 2 | Renderizar lo que falta: DSW U3/U4/U5-01, BD | decks oficiales | baja |
| 3 | Decidir los 1039 BAD de 1er/2do/Preuniversitario | todo el vault | requiere decisión del usuario |
| 4 | Normalizar los ~970 errores de formato del 1er/2do/Preuniversitario | todo el vault | baja |
| 5 | Revisar los 32 PNG huérfanos de `Figuras/` (material en curso de Matemáticas Discretas) | `Universidad/Figuras/` | baja (propuesta P7 de `LOG-opencode-onedrive.md`) |

**Propuesta propia para el vault:** un `git worktree` por sesión (P1 en
`LOG-opencode-onedrive.md`). El problema de que los merges pisen trabajo sin
commitear viene de que las 4 sesiones comparten el mismo directorio de
trabajo. Con un worktree por sesión, cada una commitea en su rama y solo una
integra a `master`.

---

## 10. Estado al cierre

- `master` al día con `origin/master` (merge `8fedc9f` + `544ba11` + `b5c5669`).
- Working tree limpio, salvo lo que pertenece a otras sesiones
  (`LOG-opencode-nube.md`, `PISTA - migracion vault...`, `Recursos adicionales/`).
- 3er Semestre: **0 wikilinks rotos**, **0 errores de formato**, **0 PDFs
  huérfanos**.
- Sitio: **805 notas publicadas**, 3 omitidas, 832 páginas, build sin errores.

---
**Tags:** #clippings #log #opencode #vault #calidad #wikilinks
