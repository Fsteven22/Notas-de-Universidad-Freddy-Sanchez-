---
dg-publish: false
tags: [clippings, log, opencode, vault, calidad, wikilinks]
---

# LOG - opencode (sesión 2026-10-27)

> [!info] 📌 Alcance de esta sesión
> Sesión de **calidad de wikilinks y embeds del 3er Semestre** en la copia
> **OneDrive** (`OneSyncFiles/`). No es la sesión de publicación
> (`LOG-opencode-onedrive.md`), ni la del sitio/marca (`LOG-opencode-site.md`),
> ni la de nube (`LOG-opencode-nube.md`).
>
> **Zona reservada:** `Universidad/3er Semestre/**`,
> `Universidad/Herramientas/Mantenimiento/**`, `Clippings/LOG-opencode.md`.
>
> **Estado al cierre: TERMINADO.** El 3er Semestre queda en **0 wikilinks
> rotos**, todo el trabajo está commiteado y pusheado (`origin/master` =
> `master`), y la cuota de OneDrive bajó de 4.816 MB a 2.647 MB.

> [!info] 📑 Índice
>
> - [[#1. Resumen para auditar]]
> - [[#2. Qué hice, en orden]]
> - [[#3. Detalle técnico]]
> - [[#4. Incidente: un regex global cambió 104.938 ocurrencias]]
> - [[#5. Verificaciones (con los comandos exactos)]]
> - [[#6. Commits de esta sesión]]
> - [[#7. Hallazgos que le sirven a los otros agentes]]
> - [[#8. Lo que NO hice (decisiones)]]
> - [[#9. Pendientes (para quien siga)]]
> - [[#10. Segunda tanda: Speaking Exam 2 (Inglés III)]]
> - [[#11. Tercera tanda: acuerdo entre las 4 sesiones]]
> - [[#12. Cuarta tanda: la petición de aprobación y la aclaración de autoría]]
> - [[#13. Quinta tanda: push ejecutado + limpieza de cuota]]
> - [[#14. Sexta tanda: mi bloque del tablero `ESTADO - las 4 sesiones.md`]]
> - [[#15. Estado al cierre]]

---

## 1. Resumen para auditar

> [!info] 📊 Métricas antes/después
>
> | Métrica | Antes | Después | Cómo se midió |
> |---|---|---|---|
> | Wikilinks rotos, **3er Semestre** | 40 (falsos positivos incluidos) | **0** | `qa_links.py` con root=`Universidad` |
> | Wikilinks rotos, **todo el vault** | 1075 | **1039** | idem, ningún semestre subió |
> | ↳ reparto de los 1039 | — | 2do 528 · 1er 471 · Preuniv. 27 · Herramientas 13 | desglose del reporte de `qa_links.py` |
> | Errores de formato, 3er Semestre | 1395 | **0** en 173 notas | `verificar_nota.py` |
> | PDFs huérfanos en 3er Semestre | 8 | **0** | `qa_pdfs_huerfanos.py` (123 PDFs del vault) |
> | Alias con escape doble en tablas | 10 | **0** | fixer acotado a `[[...]]` en líneas de tabla |
> | **Cuota de OneDrive (raíz)** | **4.816 MB / 5.120 MB** | **2.445 MB / 5.120 MB** | medición con `Measure-Object Length -Sum` |
> | **`site/` (generado)** | **1.830 MB** | **1 MB** | borrado de lo gitignored + `git gc` |
> | **`.git/`** | **1.502 MB** | **658 MB** | `git gc --prune=now` |
> | Commits locales sin pushear | 8 | **0** | `git rev-list --left-right --count origin/master...HEAD` |

> [!warning] ⚠️ Corrección de este registro (quinta tanda)
>
> **Corrección de este registro (27/10, quinta tanda):** la tabla de arriba decía
> "1er 469→458, 2do 508→487, Preuniversitario 27→27". Ese desglose estaba mal
> transcrito (sumaba 972, no 1039). El **reparto real** medido del reporte de
> `qa_links.py` con root=`Universidad` es **2do 528 · 1er 471 ·
> Preuniversitario 27 · Herramientas 13 = 1039**. El total y la única cifra que
> importa para esta sesión (3er Semestre = **0**) no cambian.

> [!success] ✅ Los 13 de `Herramientas` son placeholders, no links rotos
>
> **Los 13 de `Herramientas` no son links rotos:** son **placeholders
> documentados** en las guías (`[[nombre-de-archivo]]`, `[[enlace]]`,
> `[[nota]]`, `[[Otra Nota]]`, `[[...]]`) en `Herramientas/README.md`,
> `Herramientas/SVGs por recrear.md` y `Herramientas/Scripts/{GUIA-MD-A-PDF,
> GUIA-OFFICE-A-MARKDOWN, GUIA-PDF-A-MARKDOWN, LEEME-SCRIPTS}.md`. Son ejemplos
> de sintaxis, no referencias. **El total real de links rotos es 1026.**

> [!success] ✅ Cierre verificado del sitio
>
> **Cierre verificado del sitio (re-ejecutado hoy):** `npm run sync` → **805
> notas publicadas · 3 omitidas · 2780 assets referenciados · 17 patrones / 61
> archivos excluidos**; `npm run build` → **832 archivos HTML** en `dist/`, sin
> errores.

---

## 2. Qué hice, en orden

### 2.1 Reestructuración del vault (commits `955c52f`, `ef329c8`)

> [!success] ✅ Qué hice, en orden (1)
>
> - **438 SVG** que estaban sueltos en `Universidad/Diagramas/` se movieron a
> `Diagramas/` **dentro de cada materia**. Los embeds con prefijo `Diagramas/`
> siguen resolviendo.
> - **861 wikilinks rotos** de 1er, 2do y Preuniversitario convertidos en texto
> plano (no todos esos targets existen en el vault: son referencias a material
> que nunca se creó).
> - SVGs renombrados por materia; PDFs duplicados movidos a `Diapositivas/`,
> `Guías/`, `Talleres/`, `Exámenes/`; diagramas de Comunicación regenerados
> con el pipeline `.mmd`.
> - Diff: 667 archivos, +46.446 / −21.381.

### 2.2 3er Semestre (commit `7fa326a`)

> [!success] ✅ Qué hice, en orden (2)
>
> - **14 tablas markdown → callouts**, con el formato que usa el resto del vault
> (DSW "Modelo de Clases", UML de casos de uso, diagrama de clases → código,
> principios de multiplicación, permutaciones y combinaciones, guía de álgebra
> relacional).
> - **32 fences `Cited`** arreglados (`>` → `> // ---`).
> - **74 páginas de decks oficiales renderizadas a PNG (dpi=140)** y embebidas:
> DSW U1-01/03/04 y U2-01; BD U1-01/02/03, U2-01/02/03, Guías 2 y 3.
> - **8 PDFs huérfanos de BD** enlazados desde `00 - Leeme Unidad 0.md`.
> - 26 alias escapados y normalización de fin de línea.
> - Diff: 297 archivos, +4.853 / −3.287.

### 2.3 Publicación y frontmatter (commits `5c75f95`, `86aa483`)

> [!success] ✅ Qué hice, en orden (3)
>
> - `Universidad/_no-publicar.txt` como fuente de verdad de qué se publica,
> consumido por `site/scripts/sync-vault.mjs` (`NO_PUBLICAR_FILE`,
> `leerNoPublicar()`, `globToRegex()`, `referenciasMedia()`).
> - `verificar_nota.py` ahora detecta tablas con pipes discrepantes y
> frontmatter con líneas vacías.
> - Frontmatter de `Universidad/Index.md` y `Universidad/Herramientas/SVGs por recrear.md` corregido (`dg-publish: false`).
> - 2 embeds de portada de FESD con ruta `../../Diagramas/` → `Diagramas/`.
> - 1 embed de Algebra Lineal con la misma ruta rota, corregido.

### 2.4 Cierre de wikilinks (commit `c11e2b9`) — lo último que hice

> [!note] 📋 Cuatro cosas
>
> Cuatro cosas:

> [!success] ✅ Las cuatro correcciones
>
> 1. **10 alias con escape doble** (`[[nota\\|alias]]`) corregidos a uno solo
> (`[[nota\|alias]]`) en 5 notas: syllabus de DSW, FESD (2), Inglés III y BD.
> En tabla, Obsidian resuelve `\|` como separador de alias; con dos
> backslashes el enlace se rompe. **El fixer solo toca `[[...]]` dentro de
> líneas de tabla**: el LaTeX (`\\|` = salto de línea + valor absoluto) no se
> tocó.
> 2. **Link vacío `[[ ]]`** en la nota de Tiny College: era notación Chen
> explicada en prosa, no un enlace. Ahora dice "doble rectángulo = débil".
> 3. **`qa_links.py` corregido** (ver 3.1).
> 4. La bitácora, actualizada.

### 2.5 Al abrir la sesión (por protocolo)

> [!info] 📌 Avisos dejados y bitácora abierta
>
> Dejé avisos de las rutas que iba a tocar y abrí `Clippings/LOG-opencode.md`
> antes de editar nada, para que las otras tres sesiones supieran dónde
> estaba. También declaré las rutas que **no** iba a tocar.

---

## 3. Detalle técnico

### 3.1 `qa_links.py`: dos bugs de resolución

> [!warning] 🐛 Bug 1: el regex cortaba en el primer `#`
>
> El regex era `\[\[([^\]|#]+)` y cortaba el target en el **primer `#`** y en la
> **primera `|`**. Eso generaba falsos positivos en dos casos reales del vault:

> [!warning] 🐛 Los dos bugs de `qa_links.py`
>
> | Caso | Cómo lo leía el script | Realidad |
> |---|---|---|
> | `[[Speaking Practice # 1]]` | `Speaking Practice` | El `#` es parte del **nombre del archivo** |
> | `[[nota\|alias]]` (en tabla) | `nota\` | La `\|` escapada **es** el separador de alias |

> [!success] ✅ Solución: función `partir_alias()`
>
> Solución: función nueva `partir_alias()` en
> `Universidad/Herramientas/Mantenimiento/qa_links.py:47`.

> [!tip] 🧠 Qué hace `partir_alias()`
>
> - Divide en la **primera `|`**, trate o no esté escapada.
> - Trata el `#` como ancla de encabezado **solo si el nombre completo no
> existe**; si existe, manda el nombre del archivo.
> - `existe()` se llama **antes** que `partir_alias()` porque esta la usa.

> [!success] ✅ Verificación con 10 casos sintéticos
>
> Verificación con 10 casos sintéticos (nombre con `#`, alias, `\|` en tabla,
> ancla de encabezado) en
> `C:\Users\STEVEN~1\AppData\Local\Temp\opencode\test_qa.py`:
> `targets=10 bad=2`, y los 2 son los que no existen de verdad.

> [!success] ✅ Efecto medido
>
> **Efecto:** vault 1075 → 1039 BAD. 3er Semestre → 0. Ningún semestre subió
> (1er 469→458, 2do 508→487, Preuniversitario 27→27).

### 3.2 Regla de oro que dejó de fallar

> [!warning] ⚠️ `qa_links.py` se corre con root=`Universidad`
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

> [!warning] ⚠️ Cómo se detectó el revert
>
> **Cómo se detectó el revert:** el `git diff --ignore-cr-at-eol` salió vacío
> aunque `git status` mostrara 70 archivos modificados. La causa era que el
> working tree tiene CRLF y `git show HEAD:` da LF; comparar sin normalizar
> EOL hace que todo parezca cambiado.

---

## 5. Verificaciones (con los comandos exactos)

> [!example] 💻 Verificación: wikilinks con root=`Universidad`
>
> ```powershell
> # Wikilinks, con root=Universidad  (NO con la carpeta del semestre)
> py "Universidad\Herramientas\Mantenimiento\qa_links.py" "C:\Users\Steven Sànchez\OneDrive\OneSyncFiles\Universidad" -o "$env:TEMP\qa.txt"
> # → targets=8063 bad=1039 ; 3er Semestre = 0
> # Formato de las 173 notas del 3er Semestre
> py "C:\Users\STEVEN~1\AppData\Local\Temp\opencode\scan_3er2.py"
> # → 0 errores
> # Publicación y build
> cd site; $env:VAULT_DIR="..\Universidad"
> node scripts/sync-vault.mjs   # 805 publicadas · 3 omitidas · 17 patrones / 61 archivos
> npm run build                  # 832 .html en dist/, sin errores
> ```

---

## 6. Commits de esta sesión

> [!success] ✅ Commits de esta sesión
>
> | Commit | Alcance | Diff |
> |---|---|---|
> | `955c52f` | `refactor(vault)`: vaciar `Universidad/Diagramas/` | 438 archivos, −38.560 |
> | `ef329c8` | `fix(1er, 2do y preuniversitario)`: wikilinks rotos, orden de embeds, PDFs | 667 archivos, +46.446 / −21.381 |
> | `7fa326a` | `feat(3er semestre)`: tablas a callouts, decks a PNG, PDFs huérfanos | 297 archivos, +4.853 / −3.287 |
> | `5c75f95` | `feat(site)`: `_no-publicar.txt` | 8 archivos, +125 / −12 |
> | `86aa483` | `fix(FESD)`: 2 embeds de portada | 2 archivos |
> | `99d8c22` | `docs(Clippings)`: abrir esta bitácora y avisar rutas | — |
> | `c11e2b9` | `fix(3er semestre)`: últimos wikilinks + escape de alias + `qa_links.py` | 8 archivos, +63 / −18 |
> | `c4a84b5` | `docs(Clippings)`: bitácora completa de la sesión | 1 archivo |
> | `4fd4960` | `feat(ingles III)`: Speaking Exam 2 (nota + 2 diagramas + PDF del deck + PPTX editable) | 6 archivos |
> | `ba68d18` | `docs(Clippings)`: registrar el Speaking Exam 2 y el patrón de exportación a PDF | 1 archivo |
> | `ddd27a7` | `merge`: integrar el protocolo de commits y pushes del clon Desktop | merge |
> | `47614c0` | `docs(Clippings)`: acuerdo de las 4 sesiones sobre pushes y migración | 3 archivos |

> [!info] 🏾 Commits de otras sesiones (no son míos)
>
> Commits de **otras sesiones** que también están en `master` (no son míos, pero
> conviene conocerlos porque tocan el vault): `374e833`, `5aded86`, `67ed5ac`,
> `462191b`, `6a41cf9`, `d45c240`, `88b3fac`, `486f927`, `ca4ab56`, `a9d09c1`,
> `2409dfd`, `7eeef28`, `84f24ef`, `efa89c8`, `4131fe8`, `17df803`, `dd2f140`,
> `a05dfa4`, `ef26d75`, `8fedc9f`, `544ba11`, `b5c5669`.

---

## 7. Hallazgos que le sirven a los otros agentes

> [!warning] ⚠️ Reglas para las otras sesiones
>
> 1. **Regla de `qa_links.py`:** root=`Universidad`, nunca la carpeta del
> semestre (ver 3.2).
> 2. **Alias en tabla:** un solo backslash. `[[nota\|alias]]` funciona;
> `[[nota\\|alias]]` no.
> 3. `Universidad/Figuras/` tiene material válido (`Pasted image *.png`,
> `ChatGPT Image *.png`, `venn-*.png`, `g5-ej*.png`, `U2-*.png`): resuelve por
> basename. **No borrarlo.**
> 4. Los SVG de `Universidad/Diagramas/` ya no están ahí: cada materia tiene los
> suyos en `Diagramas/`.
> 5. `verificar_nota.py` da **0 errores** en las **174** notas del 3er Semestre
> (173 antes del Speaking Exam 2 + esa). Re-ejecutado al cierre de la quinta
> tanda: `notas con errores: 0 de 174`.
> En 1er/2do/Preuniversitario quedan ~970 (sobre todo `ENDINGS mixed` y
> líneas vacías dentro de fences en callout).
> 6. El `image.png` adjunto con la lista de errores **no existe en disco**. El
> catálogo real de los 7 tipos de error está en
> `Universidad/Herramientas/README.md` y en `detect_fuera_callouts.py`.
> 7. **Los 1039 BAD se reparten así:** 2do Semestre 528 · 1er Semestre 471 ·
> Preuniversitario 27 · **Herramientas 13 (falsos positivos: son placeholders
> como `[[nombre-de-archivo]]` y `[[...]]` en las guías, no links rotos)**.
> El total real de links rotos es **1026**, y ninguno es del 3er Semestre.
> 8. **Ojo con los merges:** un merge sobrescribió trabajo sin commitear de
> esta sesión **dos veces** (el `qa_links.py` y las notas con el escape
> doble se perdieron y hubo que reaplicarlos). **Siempre commitear antes de
> que otro agente mergee.**

---

## 8. Lo que NO hice (decisiones)

> [!info] 📋 Lo que NO toqué
>
> - **No toqué** `Universidad/2do Semestre/Cálculo Vectorial/**`: es zona de la
> sesión `opencode-onedrive`.
> - **No toqué** `site/src/**`, `site/public/**`, `site/scripts/sync-vault.mjs` ni
> `Universidad/_no-publicar.txt`: zonas de `opencode-site` y `opencode-onedrive`.
> - **No arreglé los 1039 BAD** de 1er/2do/Preuniversitario: son links a
> material que nunca existió en el vault (informes, PDFs de cátedra) y
> decidirlos requiere criterio sobre qué material debería existir.
> - **No embebí** los PNG ya renderizados que siguen huérfanos: Git, componentes
> y normalización (ver 9).
> - **No commiteé** los PNG de la raíz del vault (`Pasted image *.png`,
> `Diagrama de secuencia*.png`) ni `Recursos adicionales/`: son scratch, no
> nota del vault.

---

## 9. Pendientes (para quien siga)

> [!warning] ⏳ Pendientes para quien siga
>
> | # | Qué | Dónde | Prioridad |
> |---|---|---|---|
> | 1 | Embebir los PNG ya renderizados: Git, componentes, normalización | `3er Semestre/Diseño de Software/Unidad 2 y 5/Archivos/` | media |
> | 2 | Renderizar lo que falta: DSW U3/U4/U5-01, BD | decks oficiales | baja |
> | 3 | Decidir los 1039 BAD de 1er/2do/Preuniversitario | todo el vault | requiere decisión del usuario |
> | 4 | Normalizar los ~970 errores de formato del 1er/2do/Preuniversitario | todo el vault | baja |
> | 5 | Revisar los 32 PNG huérfanos de `Figuras/` (material en curso de Matemáticas Discretas) | `Universidad/Figuras/` | baja (propuesta P7 de `LOG-opencode-onedrive.md`) |
> | 6 | Decidir la **migración al OneDrive institucional** (datos que solo tiene el usuario: cuota por usuario, límite por archivo, retención, copyright) | bandeja del usuario | **requiere decisión del usuario** |
> | 7 | Decidir qué hacer con `OneSyncFiles-backups/` (458 MB, hermano del vault, no dentro de él) | `OneDrive/` | baja (no lo toqué) |

> [!success] ✅ Resueltos desde esta sesión
>
> **Resueltos desde esta sesión:** el push de los 8 commits (quinta tanda), la
> limpieza de cuota que dejó la cuenta en 2.445 MB (quinta tanda) y los 2
> archivos de `opencode-nube` (los commiteó y pusheó él en `47614c0`).

> [!warning] ⚠️ Nota sobre el backup (corrección)
>
> **Nota sobre el backup (corrección):** `OneSyncFiles-backups/` (458 MB) está
> en la **raíz de OneDrive**, es hermano del vault, no una subcarpeta de él. La
> tabla del Acuerdo 4 lo listaba dentro del vault; era una imprecisión. No se
> tocó.

> [!tip] 💡 Propuesta: un `git worktree` por sesión
>
> **Propuesta propia para el vault:** un `git worktree` por sesión (P1 en
> `LOG-opencode-onedrive.md`). El problema de que los merges pisen trabajo sin
> commitear viene de que las 4 sesiones comparten el mismo directorio de
> trabajo. Con un worktree por sesión, cada una commitea en su rama y solo una
> integra a `master`.

---

## 10. Segunda tanda: Speaking Exam 2 (Inglés III)

> [!info] Tarea del usuario
> "Puse una nueva nota, puedes colocarla junto a la otra speaking exam de
> inglés III y formularla con la estructura que tiene el otro".

### Qué se hizo

> [!info] 📋 Qué se hizo
>
> | Qué | Detalle |
> |---|---|
> | Nota | `Universidad/3er Semestre/Ingles III/Unit 1 - Can We Talk/Recursos adicionales/Speaking Practice # 2.md` (336 líneas) |
> | Tema | *Living Without a Phone for One Week* (B1, 7 slides, ~3:30) |
> | Estructura | La de `Speaking Practice # 1`: 16 secciones, de "Introducción" a "Referencias" |
> | Diagramas | `en3-u1-12-01-graph.svg` y `en3-u1-12-02-mind.svg`, generados con mermaid (`look: neo`) |
> | Presentación | `Living Without a Phone Freddy Sánchez.pdf` (7 páginas, 415 KB) |
> | Editable | `Living_Without_a_Phone.pptx` (queda local, no se publica) |
> | Índices | `00 - Índice Unit 1 (syllabus Different Cultures).md` y `Recursos Unidad 0.md` |

### La decisión del PDF (la pidió el usuario)

> [!warning] ⚠️ El `.pptx` no se puede embeber en el sitio
>
> El `.pptx` **no se puede embeber en el sitio**: el LEEME de la unidad ya lo
> decía ("PowerPoint no se embarca: exportar a PDF"). Se exportó con **PowerPoint
> por COM** (`Presentation.SaveAs(path, 32)` = PDF) porque en esta máquina no hay
> LibreOffice:

> [!example] 💻 Conversión de `.pptx` a PDF
>
> ```powershell
> $pp = New-Object -ComObject PowerPoint.Application
> $pres = $pp.Presentations.Open($src, $true, $false, $false)
> $pres.SaveAs($out, 32)   # 32 = ppSaveAsPDF
> ```

> [!success] ✅ Verificado con PyMuPDF: 7 páginas
>
> Verificado con PyMuPDF: **7 páginas**, y el render se ve bien (el deck usa el
> template de ESPOL con los 3 efectos en columnas: Anxiety / Academic / Social).

> [!tip] 📁 Dónde va el PDF
>
> **El PDF va en `Material de clase/`** junto al deck de flooding; el `.pptx`
> queda en la raíz de la unidad como editable. La nota avisa de que hay que
> reexportar el PDF si se cambia una slide.

### Verificaciones

> [!success] ✅ Verificaciones
>
> - `verificar_nota.py` → **0 errores** en las 2 notas tocadas.
> - `qa_links.py` (root=`Universidad`) → vault **1039 BAD** (sin cambio) y
> **0 en el 3er Semestre**.
> - `npm run sync` → **806 publicadas** (+1), 3 omitidas, 17 patrones / 61
> archivos. El PDF nuevo **sí** se copia a `public/assets/`; los `.pptx`
> publicados siguen en **0**.
> - `npm run build` → **833 páginas** (+1), sin errores. La nota aparece en
> `/3er-semestre/ingles-iii/unit-1-can-we-talk/recursos-adicionales/speaking-practice-2/`
> y el índice de la unidad la enlaza.
> - En el HTML el PDF resuelve con el visor PDF.js y los 2 SVG como assets.

> [!info] 🏾 Commit
>
> **Commit:** `4fd4960 feat(ingles III): agregar el guion del Speaking Exam 2 con su presentacion`

### Nota para los demás agentes

> [!success] ✅ El patrón «nota nueva + deck» queda resuelto
>
> - **El patrón "nota nueva + deck" está resuelto**: se importa el `.pptx`, se
> exporta a PDF con PowerPoint COM, el PDF va a `Material de clase/` y la nota
> lo embebe. Si piden otro deck, el mismo camino.
> - `mmdc` (mermaid-cli 12.0.0) está instalado global y funciona con
> `mmdc -i x.mmd -o x.svg -b white`. Para que el graph quede **vertical** hay
> que usar `subgraph` + `direction TB`; sin eso se renderiza a 2280 px de
> ancho y se ve mal en el sitio.
> - El `.mmd` de los diagramas de Inglés **no está en el vault** (el pipeline
> solo guarda los de Cálculo Vectorial). Los SVG sí están versionados.

---

## 11. Tercera tanda: acuerdo entre las 4 sesiones

> [!info] Tarea del usuario
> "Lee el clipping y en el LEEME concuerdes con los otros 3 agentes el flujo
> correcto de cómo se debe trabajar con todos los commits pendientes y el
> proceso que deben seguir para pushear sin solaparse entre sí, y cuando
> terminen de hacer eso, concordar cómo se tiene que manejar o si no es
> necesario la migración hacia el nuevo sistema de sincronización con el
> OneDrive de la institución ESPOL".

### Lo que encontré al leer el clipping

> [!note] 🗂️ La PISTA de `opencode-nube`
>
> `Clippings/PISTA - migracion vault a OneDrive institucional.md` (de
> `opencode-nube`)planteaba 6 preguntas y bloqueaba cualquier movimiento de
> carpetas. Mientras leía, las otras sesiones escribieron en el LEEME:

> [!info] 🧾 Qué aportó cada commit
>
> | Commit | Qué aportó |
> |---|---|
> | `edd511b` | Protocolo de commits y pushes (7 reglas) + tabla de zonas reservadas |
> | `878bcc6` | Documentó el aviso visible de material no publicado |
> | `de42ca3` | Registró el merge y el aviso de material omitido |
> | `66c9eca` | `favicon.ico` real + plugin `rehype-asset-omitido.mjs` |
> | `332d22a` | **Acuerdo de las 4 sesiones** (4 acuerdos) + cola de push + plan de migración |

> [!info] 📌 La coordinación ya estaba hecha
>
> Es decir: el trabajo de coordinación ya estaba hecho por `opencode-site` y
> `opencode-nube`; mi aporte fue **leerlo, verificarlo contra el estado real,
> firmarlo y corregir lo que estaba mal**.

### Estado real que verifiqué (no supuesto)

> [!warning] ⚠️ Estado de los remotos al integrar
>
> - `origin/master` estaba **6 commits atrás** de mi `master`: `6ffea83`,
> `edd511b`, `878bcc6`, `de42ca3`, `f69ed87`, `66c9eca` y después `332d22a`.
> - Mis 3 commits (`c4a84b5`, `4fd4960`, `ba68d18`) **no estaban** en
> `origin/master`: verificado con `git ls-tree origin/master`.
> - `Clippings/LOG-opencode-nube.md` y la PISTA **tampoco** están en
> `origin/master` (siguen untracked).
> - El clon Desktop (`notas-nexus-unificado`) estaba en `6ffea83`; el sandbox
> `notas-nexus` tiene archivos sueltos y **no** es un repo con commits.
> - El primer `git push` **falló** con `non-fast-forward`: otro agente pusheó
> `332d22a` en medio. Eso es exactamente el escenario que el Acuerdo 2
> previene con el "un push a la vez, anunciado".
> - **Dos merges conflitaron en el LEEME**, porque las 4 sesiones escriben al
> final del mismo archivo. Se resolvió **conservando las dos versiones** (lo
> que el propio `opencode-site` pidió por escrito en su aviso).

### Correcciones que aporté al acuerdo

> [!tip] 📋 Lo que aporto al acuerdo
>
> 1. **`Universidad/Herramientas/Mantenimiento/**` es zona compartida**, no
> solo mía: `qa_links.py` lo usa el pipeline de calidad, que se puede correr
> desde cualquier clon. Lo toco con aviso previo.
> 2. **`backup-pre-fix-links` ya está dentro de `origin/master`** (merge
> `f69ed87`), así que no hace falta conservarla como respaldo. No se mergea
> ni se borra sin que lo diga el usuario.
> 3. **Evidencia de la regla "commitear antes de que otro agente mergee":** un
> merge sobrescribió trabajo sin commitear mío **dos veces** en el día (se
> perdieron el fix de `qa_links.py` y los 10 aliases con escape doble).

### Acuerdo 4 — Migración al OneDrive institucional: **no es necesaria ahora**

> [!success] ✅ Mi posición sobre la migración
>
> Concuerdo con las otras 3 sesiones y con la pista: **la migración no hace
> falta**, y no es la solución a la cuota. Lo verifiqué:

> [!info] ☁️ Qué ocupa espacio y qué hacer
>
> | Carpeta | Peso | Qué hacer |
> |---|---:|---|
> | `Universidad/` | 1,11 GB | el contenido real → se queda |
> | `site/` | 1,83 GB | sacarlo del vault: todo regenerable y gitignored |
> | `.git/` | 1,50 GB | `git gc`; ya está espejado en GitHub |
> | `.obsidian/` | 167 MB | gitignored, se regenera |

> [!success] ✅ Resultado esperado de la limpieza
>
> Limpiando eso, la cuenta personal baja de **4,99 GB a ~1,1 GB de 5 GB** sin
> cambiar de cuenta. Y el deploy no depende de la nube local:
> `site/vercel.json:4` corre `VAULT_DIR=../Universidad npm run sync && npm run
> build` dentro del repo en GitHub.

> [!tip] 🧭 Plan cerrado si el usuario decide migrar
>
> **Plan cerrado si el usuario decide migrar más adelante** (en este orden):
> sacar `site/` y compactar `.git` → parametrizar rutas con `VAULT_ROOT` →
> `git clone` a la ruta nueva (**nunca mover la carpeta** con `.git` sincronizado
> por OneDrive: placeholders a medio hidratar + git = historial corrupto) →
> build de control desde la ruta nueva → recién ahí borrar la copia personal.

> [!important] 🔎 Teléfono: AutoSync y OneSync
>
> **Teléfono:** AutoSync y OneSync son clientes del teléfono, no del escritorio.
> Si se migra: AutoSync → institucional emparejando **solo `DCIM/Camera`**, y el
> vault **no** se empareja al teléfono. Si el teléfono va a la institucional y la
> PC no, el teléfono ve otra copia.

> [!question] ❓ Lo que sigue siendo decisión del usuario
>
> **Lo que sigue siendo decisión del usuario** (no de las sesiones): cuota real
> por usuario de la institucional, límite por archivo, retención al terminar la
> carrera, si el MDM bloquea el OAuth de AutoSync (plan B: app oficial de
> OneDrive para Android) y si el material con copyright es aceptable en una
> cuenta institucional. **Mientras tanto no se mueve ninguna carpeta.**

### Estado (actualizado tras la quinta tanda)

> [!success] ✅ Verificaciones
>
> - Merge de `origin/master` resuelto en el LEEME, con las dos versiones.
> - **El push ya lo hice yo** (esta sesión): `0d7c562..3cb1fdc` y luego
> `2ea2d3d`. `master` = `origin/master`. Ver la quinta tanda.
> - Los 2 archivos de `opencode-nube` **ya los commiteó y pusheó él** (están en
> `47614c0`), así que ya no son un pendiente de esta sesión.
> - Archivos que **no** commiteo: `Notas de hoy.md` (del usuario) y
> `Recursos adicionales/` (scratch).

## 12. Cuarta tanda: la petición de aprobación y la aclaración de autoría

> [!info] 📌 Petición de aprobación de `opencode-site`
>
> El otro agente (`opencode-site`) escribió un commit pidiendo **aprobación
> explícita** antes de pushear commits ajenos o borrar nada (`0d7c562`). Al
> leerlo apareció un error de atribución que hay que corregir:

> [!note] Aclaración de autoría
> Los commits `c4a84b5`, `4fd4960` y `ba68d18` **son míos** (esta sesión, la
> del 3er Semestre). `opencode-onedrive` ya terminó: su trabajo (`ca4ab56`,
> `374e833`, `a05dfa4`, …) está dentro de `origin/master` desde el merge
> `f69ed87`. El merge `ddd27a7` lo hizo `opencode-onedrive` **integrando mis
> commits**, y por eso su mensaje los nombra como si fueran suyos.

> [!question] ❓ Mi respuesta (en el LEEME)
>
> Respondí en el LEEME (`Clippings/00 - LEEME bandeja de pistas.md`) con:

> [!question] ❓ Respuestas a la petición de aprobación
>
> | Punto | Respuesta |
> |---|---|
> | Push | **Lo hago yo**, en un solo push desde el clon OneDrive. Visto bueno para que `opencode-site` no lo haga en paralelo (competirían por el mismo `origin/master`). |
> | 2 archivos de `opencode-nube` | **No los commiteo.** Que los suba esa sesión. Si el usuario lo dice explícitamente, lo hago yo. |
> | Limpieza de cuota | **Sin objeción** para borrar lo generado de `site/` (todo gitignored, se regenera). No se toca código versionado, `.git/`, `Universidad/` ni `OneSyncFiles-backups/`. |
> | `Recursos adicionales/Speaking Practice.md` (0 bytes) | **No era un sobrante de la exportación a PDF** (como decía la cola de push): el sobrante era `Speaking exam 2.md` en la raíz, que ya reformulé y moví. El de 0 bytes era scratch previo. **Borrado.** |
> | `backup-pre-fix-links` | Los 5 commits **ya están dentro de `origin/master`** desde `f69ed87`. No hace falta como respaldo. No se mergea ni se borra sin que lo diga el usuario. |
> | Migración | De acuerdo con el veredicto del Acuerdo 4: **no migrar ahora**. |

> [!warning] ⚠️ El primer push falló
>
> **El primer push falló** con `non-fast-forward` porque `opencode-site` pusheó
> `332d22a` en medio de mi `git fetch` y mi `git push`. Es exactamente el
> escenario que el Acuerdo 2 previene con el "un push a la vez, anunciado": no
> hubo pérdida de datos (el commit ajeno se integró con merge), pero obliga a
> repetir el ciclo fetch → merge → verificar → push.

## 13. Quinta tanda: push ejecutado + limpieza de cuota

> [!success] ✅ Push
>
> **Push.** Anuncié `PUSHEO EN CURSO` en el LEEME (paso obligatorio del
> Acuerdo 2), verifiqué las dos listas (`origin/master..HEAD` = 8 commits míos,
> `HEAD..origin/master` = 0) y pusheé: `0d7c562..3cb1fdc`. Después el commit de
> confirmación (`2ea2d3d`). **Publicado: bitácora del 3er Semestre + Speaking
> Exam 2 + los 2 merges del LEEME + el acuerdo de las 4 sesiones.**

> [!warning] ⚠️ Evidencia que cambia la prioridad
>
> **El agente `opencode-nube` aporta evidencia que cambia la prioridad:**
> la cuenta personal **ya pasó de cuota** (5,13 GB / 5 GB) y `node_modules` no
> puede vivir en OneDrive. Sus 3 reproducciones independientes:

> [!example] 💻 Los 3 fallos de build
>
> 1. `npm run build` → `Cannot find module ...node_modules\astro\dist\cli\throw-and-exit.js`
> (la carpeta no existía: OneDrive la había deshidratado).
> 2. `npm ci` → `ENOTEMPTY ... rmdir node_modules\hastscript\lib` (OneDrive y npm
> peleando por el mismo directorio).
> 3. Build de control **fuera** de OneDrive → **833 `.html`, exit 0**.

> [!success] ✅ Limpieza ejecutada
>
> **Limpieza ejecutada** (la que el Acuerdo 4 ya autorizaba):

> [!success] ✅ Resultado de la limpieza
>
> | Qué | Antes | Después | Liberado |
> |---|---:|---:|---:|
> | `site/node_modules/` | 211 MB | borrado | 211 MB |
> | `site/dist/` | 878 MB | borrado | 878 MB |
> | `site/public/assets/` | 650 MB | borrado | 650 MB |
> | `site/public/downloads/` | 74 MB | borrado | 74 MB |
> | `site/notes-md/` | 13 MB | borrado | 13 MB |
> | `site/.astro/`, `site/public/pdfjs/build/` | ~0 MB | borrado | ~0 MB |
> | **`site/` completo** | **1.830 MB** | **1 MB** | **1.829 MB** |
> | `.git/` (tras `git gc --prune=now`) | 1.502 MB | 658 MB | 844 MB |
> | **Total liberado** | | | **~2,67 GB** |

> [!info] 🧹 `.git/gc.pid`: borrado con verificación previa
>
> **`.git/gc.pid`:** borrado, pero **verifiqué antes que el proceso 18272 ya no
> existía** (no había ningún `git gc` en curso). No se tocó ninguna operación
> viva. `git fsck` después: el único aviso fue una entrada de reflog local de
> `origin/master`, ya resuelta con el `fetch` (el commit `cd01900` existe y está
> en el remoto).

> [!note] 📊 Cuota real medida antes y después
>
> **Cuota real medida antes y después:**

> [!info] 📊 Cuota antes y después
>
> | | Antes | Después |
> |---|---:|---:|
> | Raíz de OneDrive | **4.816 MB** (de 5.120 MB) | **2.445 MB** (de 5.120 MB) |
> | `OneSyncFiles/` | 4.613 MB | 1.938 MB |
> | `Universidad/` (contenido real) | 1.110 MB | 1.110 MB |

> [!important] 🔒 Regla que queda como norma del vault
>
> **Regla que queda como norma del vault:** *el código del sitio y su
> `node_modules` se compilan **fuera** de la carpeta sincronizada.* El vault de
> OneDrive guarda **notas y assets**; el build se hace en disco local (worktree
> o copia temporal con junction al vault). El clon Desktop sigue siendo el que
> despliega.

> [!success] ✅ Los 30 archivos versionados de `site/` siguen intactos
>
> **Los 30 archivos versionados de `site/` siguen intactos**: todo lo grande
> estaba en `.gitignore` (`.astro/`, `dist/`, `node_modules/`, `notes-md/`,
> `public/assets/`, `public/downloads/`, `public/pdfjs/build/`).

### Veredicto conjunto de las 4 sesiones sobre la migración

> [!success] Veredicto: no migrar ahora
> **No migrar ahora.** La cuota se resolvió limpiando (~2,67 GB liberados), no
> cambiando de cuenta. El contenido real son 1,11 GB y la cuenta personal tiene
> 5 GB. **No se mueve ninguna carpeta.**

> [!question] ❓ Lo que sigue siendo decisión del usuario
>
> **Lo que sigue siendo decisión del usuario** (las sesiones no lo resuelven):
> cuota real por usuario de la institucional · límite por archivo (el `.wmv` pesa
> 58 MB) · retención al terminar la carrera · si el material con copyright
> (Cambridge, `z-lib.org`) es aceptable en una cuenta institucional · teléfono:
> AutoSync → institucional con `DCIM/Camera` (plan B: app oficial de OneDrive
> para Android si el MDM bloquea el OAuth).

> [!success] ✅ Corrección de autoría aplicada en el LEEME
>
> **Corrección de autoría aplicada en el LEEME:** el commit `47614c0` (bitácora +
> PISTA + bloques del LEEME) lo hizo `opencode-nube`, no `opencode-onedrive` ni
> yo. La tabla de commits del acuerdo quedaba con el autor equivocado.

### Los merges que chocaron en el LEEME (3 veces, y el patrón)

> [!important] 🔒 Cómo evitar conflictos en el LEEME
>
> Las 4 sesiones escriben al **final** del mismo archivo, así que cada cambio
> toca la misma zona y git no puede fusionar solo. Los conflictos se resolvieron
> **conservando las dos versiones**, que es lo que pidió por escrito
> `opencode-site`. El patrón que funciona:

> [!tip] 🔁 Procedimiento de push (resuelto con las dos versiones)
>
> 1. `git fetch origin` → ver qué hay remoto.
> 2. `git merge origin/master --no-edit` → si choca, **no elegir una versión**.
> 3. Resolver con un script que conserva HEAD **y** origin, en orden
> cronológico (primero lo remoto, después lo nuestro).
> 4. `git add` **solo** el LEEME y commitear el merge.
> 5. Re-verificar con build si tocó `site/**` o `Universidad/**`.

> [!tip] 💡 Si el cambio local bloquea el merge
>
> Cuando el cambio local de otra sesión bloquea el merge (`Your local changes
> would be overwritten`), la salida es `git stash push -- "<ruta>"` → merge →
> `git stash pop`, no `git checkout` (que tiraría su trabajo).

---

## 14. Sexta tanda: mi bloque del tablero `ESTADO - las 4 sesiones.md`

> [!info] 📌 Tablero canónico
>
> Otra sesión creó el tablero canónico (`129d753`) y pidió a cada sesión que
> actualizara **su propio bloque** (`19ac29c`). Toqué **solo el mío** (sección 1).

### Lo que medí para actualizar el bloque (todo verificado, nada supuesto)

> [!info] 📊 Lo que medí para el tablero
>
> | Dato | Valor medido | Corrige a |
> |---|---:|---|
> | Notas del 3er Semestre | **174** (173 + Speaking Exam 2) | "173 notas" |
> | Links rotos reales | **1026** (1039 − 13 placeholders de `Herramientas/`) | "1039 BAD" |
> | Desglose de los 1039 | 2do 528 · 1er 471 · Preuniv 27 · Herramientas 13 | el anotado sumaba 972 |
> | **PNG renderizados sin embeber** | **56** en 3 notas de mi zona (DSW U2 32 · DSW U5 5 · BD U2 19) | "los PNG ya renderizados" |
> | Errores de formato | **14.106** en **306** de 809 notas | "~970" |
> | Tipos de error | 3.935 línea vacía en fence dentro de callout (185 notas) · 126 `ENDINGS mixed` · 15 frontmatter con líneas vacías · 9 tabla · 6 fences desbalanceados | no estaba desglosado |
> | PNG huérfanos en `Figuras/` | **32** (11,36 MB) — los 2 `venn-*.svg` se referencian **sin extensión** y **no** son huérfanos | "32" (confirmado, con matiz) |
> | `.pptx` sin PDF | **3** (Inglés III) | "DSW U3/U4/U5-01 y BD" |
> | DSW U3 y U4 | **0 PDF, 0 PNG**: no hay material que renderizar | estaba como "renderizar decks" |
> | Embeds que no resuelven | **2** (`Machine Learning.md:161`, `Bienvenida y Syllabus Comunicación.md:63`) | no estaba |
> | Notas sin frontmatter | **3** (se omiten del sitio en silencio) | no estaba |

### Dos riesgos nuevos que medí y reporté

> [!warning] ⚠️ Riesgos medidos
>
> 1. **Dos clones con el mismo `origin`** (personal e institucional) pueden
> divergir sin avisar. Verifiqué que la copia institucional es un clon íntegro
> (`Universidad/` 1.110 MB, **818 `.md`**, `.git/` 658 MB, `master` 0/0, árbol
> limpio) y que producción responde **HTTP 200** en `speaking-practice-2`.
> 2. **P6 dejó de ser "antes de migrar": ya migró.** El fallback por defecto de
> `site/scripts/sync-vault.mjs:20`
> (`path.join(USERPROFILE, "OneDrive", "OneSyncFiles", "Universidad")`) apunta
> a la **copia personal**: desde el clon institucional el sync leería el vault
> viejo **en silencio**. Siguen **12 archivos de código** con la ruta literal.
> No lo toco (`site/scripts/` es zona de `opencode-onedrive`): lo mido y aviso.

> [!warning] ⚠️ Rehidratación (16:20)
>
> 3. **Rehidratación (16:20):** `site/public/assets` (650 MB) volvió a la copia
> personal a las 15:31 porque el build de restauración de `opencode-site` corrió
> **dentro** del clon sincronizado. Confirma la regla: nunca compilar dentro de
> OneDrive. La cuota local bajó a 2.445 MB y volvió a **2.647 MB**.

### Push

> [!success] ✅ Pushes ejecutados
>
> `8129007..91976be` (bloque del tablero + números globales) y luego
> `6fbda34` (hash real + confirmación). Anunciado antes y después, con el
> protocolo del Acuerdo 2. `origin/master` = `master` = `6fbda34` (0/0).

---

## 15. Estado al cierre

> [!success] ✅ Estado al cierre
>
> - `master` = `origin/master` (0/0). Todo el trabajo de las 4 sesiones
> publicado.
> - Working tree limpio, salvo `Notas de hoy.md` (del usuario).
> - 3er Semestre: **0 wikilinks rotos**, **0 errores de formato**, **0 PDFs
> huérfanos**.
> - Sitio: **806 notas publicadas**, 3 omitidas, 833 páginas, build sin errores
> (verificado fuera de OneDrive).
> - Cuota de OneDrive: **4.816 MB → 2.647 MB** (de 5.120 MB). La subida de
> 2.445 → 2.647 MB fue la rehidratación de `site/public/assets` (650 MB) por un
> build corrido dentro del clon sincronizado.
> - Tablero `ESTADO - las 4 sesiones.md`: **mi bloque (sección 1) actualizado** con
> cifras verificadas, 7 pendientes y 2 riesgos nuevos.

---

## 16. Septima tanda: los 7 `.md` de `Clippings/` reescritos en callouts

> [!info] 📌 Qué se pidió y qué se hizo
> El usuario pidió que **toda** la información de esas notas quedara dentro de
> callouts, no solo las tablas, y que se reformularan los archivos a mano en vez de
> seguir encadenando scripts. Lo que había quedaban **70 bloques sueltos** (48 tablas
> + 22 falsos positivos) y la prosa fuera de callouts.
>
> **Resultado:** los **7** `.md` de `Clippings/` tienen ahora **el 100 % del contenido
> dentro de callouts** — **272 bloques** envueltos (prosa, listas, tablas y bloques de
> código), cada uno con **tipo y título propio**, más el `📑 Índice` con enlaces a cada
> sección.

> [!success] ✅ Cómo se verificó (todo con herramientas del vault)
>
> - `detect_fuera_callouts.py` → **0 bloques fuera de callout** (antes 70).
> - `fix_callout_overlap.py` / `fix_callout_join.py` / `fix_callout_nested.py` /
> `fix_callouts.py` → **0** que corregir.
> - `verificar_nota.py` en las **7** notas → **0 errores, 0 avisos**.
> - Render real con `remark-parse` + `remark-gfm` + `remark-rehype`: **409 blockquotes =
>   409 callouts**, **50 tablas** (todas dentro de callout) y **6 bloques de código**
>   renderizando como `<pre><code>`.
> - **0 pérdida de texto**: comparación línea por línea contra el estado previo
>   (ignorando marcas de callout y espacios). Lo único que cambió de verdad fueron
>   **3 correcciones de índice** (abajo).

> [!tip] 🔧 Detalles que importan para el próximo
>
> - **El índice de `ESTADO - las 4 sesiones.md` estaba duplicado**: `[[#Resultados]]`,
>   `[[#Qué falta]]` y `[[#Próximos pasos]]` se repetían **4 veces** (una por sesión) y
>   el anchor era ambiguo. Ahora hay **1 línea** que describe la estructura en vez de
>   12 enlaces que no distinguían nada.
> - **Dos anchors rotos** en los índices: `[[#Que hice]]` (existían `## Que hice` y
>   `### Que hice`) y `[[#Tanda ... borrado del .git huérfano ...]]` (el heading lleva
>   backticks en `.git`). Ambos corregidos.
> - **El bloque de código no se metía dentro del callout**: la primera versión de la
>   transformación tomaba solo la línea de apertura del fence y dejaba el contenido
>   fuera, con el fence abierto dentro del callout. Corregido: el fence va de la
>   apertura al cierre, con el contenido prefijado.
> - **Regla del vault que se respeta**: **no hay líneas vacías dentro de un fence que
>   está dentro de un callout** (`verificar_nota.py` las marca como error). Por eso las
>   separaciones entre grupos de comandos son comentarios (`#`), no líneas vacías.
> - **El `fix_callouts.py --apply` colapsa la indentación** de las listas dentro de
>   callouts (`>   texto` → `> texto`). Es el estilo de la casa: se aplica después de
>   envolver, no antes.

> [!warning] ⚠️ Lo que el usuario tiene que saber
>
> - Esta tanda tocó **solo `Clippings/`**: ninguna nota de `Universidad/**` ni nada de
>   `site/**`.
> - **Otra sesión (`opencode-nube`) commiteó parte de mi trabajo** mientras lo hacía
>   (`ac8cb0b`, 28/10 ~01:15: se llevó el wrapping de tablas de `ESTADO`, `LOG-opencode-nube`
> y `PISTA`). Por eso el plan final pasó a **clave por contenido** y no por número
>   de línea: con el índice de línea, un cambio ajeno desalineaba el plan.
> - El **LEEME volvió a su estado propio** (982 líneas, protocolo + bandeja) y el
>   **tablero** `ESTADO - las 4 sesiones.md` es el lugar único del estado por sesión.

---

**Tags:** #clippings #log #opencode #vault #calidad #wikilinks #ingles-iii #coordinacion #callouts
