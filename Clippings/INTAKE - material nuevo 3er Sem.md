---
dg-publish: false
tags: [clippings, intake, 3er-semestre, guides, material-nuevo]
---

# INTAKE — material nuevo de 3er Sem. (carril D1)

> [!info] 📌 Qué es este archivo
> Tracker del **carril D1** (intake y control de calidad del material nuevo): el usuario deja
> las **guías y ejercicios** en la carpeta **`Unidad 0 - Guías y Ejercicios`** de cada materia, y
> esta sesión (D1) **detecta lo que llega**, lo registra y se lo pasa a `opencode` (D2), que es
> quien lo convierte en notas.
> **Zona de D1:** solo este archivo y el tablero. **No** se tocan los PDFs: se registran y se
> avisa. **D2** (notas) es de `opencode` (`Universidad/3er Semestre/**`).

> [!info] 📑 Índice
>
> - [[#Las 5 rutas vigiladas]]
> - [[#Línea base (28/10/2026 02:50)]]
> - [[#Hallazgos de la línea base]]
> - [[#Checklist por lote (para cada material nuevo)]]
> - [[#Handoff D1 → D2]]
> - [[#Pedido al carril A: que la detección sea automática]]
> - [[#Estado del carril]]

---

## Las 5 rutas vigiladas

> [!note] 📍 Rutas exactas (respetan el acento de `Teórico`)
> | # | Materia | Ruta |
> |---|---|---|
> | 1 | Diseño de Software | `Universidad/3er Semestre/Diseño de Software/Unidad 0 - Guias y Ejercicios/` |
> | 2 | Fundamentos de Electricidad y Sistemas Digitales | `Universidad/3er Semestre/Fundamentos de Electricidad y Sistemas Digitales/Teórico/Unidad 0 - Guías y Ejercicios/` |
> | 3 | Inglés III | `Universidad/3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/` |
> | 4 | Matemáticas Discretas | `Universidad/3er Semestre/Matemáticas Discretas/Unidad 0 - Guias y Ejercicios/` |
> | 5 | Sistema de Bases de Datos | `Universidad/3er Semestre/Sistema de Bases de Datos/Unidad 0 - Guias y Ejercicios/` |
>
> En la materia 2 la carpeta está **dentro de `Teórico/`** (con acento). En la 3 hay una
> subcarpeta `Guías/`. La materia 2 tiene además `Guías/` dentro.

## Línea base (28/10/2026 02:50)

> [!success] 📏 Lo que hay hoy (medido, no supuesto)
> **367 archivos** en las 5 rutas, con **SHA-256 de cada uno** (así cualquier archivo nuevo se
> reconoce al instante).
>
> | Materia | Archivos | PDF | Peso | Archivo más pesado |
> |---|---:|---:|---:|---|
> | Diseño de Software | 34 | 14 | **114,4 MB** | `01_Software Engineering A Practitioners Approach…` (71,63 MB) |
> | Fundamentos de Electricidad | 16 | 15 | **8,4 MB** | `…_Electricidad…pdf` (0,9 MB) |
> | Inglés III | 67 | 10 | **70,3 MB** | `Speaking Introducing yourself bad example.mp4` (7,07 MB) |
> | Matemáticas Discretas | 39 | 37 | **60,5 MB** | `LIBRO DE APOYO … Rosen (z-lib.org).pdf` (35,04 MB) |
> | Sistema de Bases de Datos | 211 | 39 | **66,4 MB** | `Database Systems … (9th Edition).pdf` (15,92 MB) |
> | **Total** | **367** | **115** | **~320 MB** | — |

## Hallazgos de la línea base

> [!warning] ⚠️ 1 duplicado exacto (mismo SHA-256)
> `Guía Didáctica Mat. discretas lógica y demostraciones.pdf` (**432 KB**, hash `9179EF4C…`)
> está **2 veces** en Matemáticas Discretas:
> - `Unidad 0 - Guias y Ejercicios/Guía Didáctica…pdf`
> - `Unidad 0 - Guias y Ejercicios/Guías/Guía Didáctica…pdf`
> **Propuesta para `opencode` (no la ejecuto yo: es `Universidad/**`):** quedarse con **una**
> sola copia y borrar la repetida. El material duplicado infla la nube sin aportar nada.

> [!info] 🔒 Los libros con copyright: ya están bien resueltos
> Por decisión del usuario (28/10) el material con copyright **se ignora al subirlo a la web**.
> Los **6 libros** de estas carpetas (~150 MB) **ya están** en la lista negra
> `Universidad/_no-publicar.txt` → **no se publican**, y eso está bien:
> `01_Software Engineering…` (71,63 MB) · `LIBRO DE APOYO… Rosen` (35,04 MB) ·
> `Database Systems…` (15,92 MB) · `LIBRO GUIA – Johnsonbaugh` (14,25 MB) ·
> `03_Design patterns explained…` (7,40 MB) · `Clean Architecture…` (6,37 MB) ·
> `02_Using UML… (z-lib.org)` · `CAMBRIDGE ONE_GUIDE FOR STUDENTS_UPDATED.pdf` · `Empower*.pdf`.
> **Verificado byte a byte:** las 17 entradas de `_no-publicar.txt` **sí** coinciden con los
> nombres reales de los archivos (no hay reglas rotas por codificación).

> [!question] ❓ Una duda que D1 deja anotada (no bloquea a nadie)
> El **`.docx`** de la *Guía Didáctica* está en la lista negra, pero su **`.pdf`** (el mismo
> contenido, 432 KB) **no**. Si el criterio es "el material con copyright no se publica",
> el `.pdf` debería entrar también. **Decide** `opencode-onedrive` (dueño de las reglas de
> publicación) o el usuario. **D1 no lo cambia** para no pisar la lista a escondidas.

## Checklist por lote (para cada material nuevo)

> [!tip] ✅ Qué se registra por cada lote que llega
> - [ ] **Qué llegó**: materia, carpeta, nombre, tamaño, **SHA-256** (12 chars) y fecha.
> - [ ] **¿Es nuevo de verdad?** → comparar con la línea base y con el resto del vault
>       (`qa_pdfs_duplicados.py` / `qa_pdfs_huerfanos.py` del carril A).
> - [ ] **¿A qué unidad pertenece?** → la pista dice si es de la Unidad 0 o de otra.
> - [ ] **¿Copyright?** → si sí: **se ignora al publicar** (lista negra). Se anota, no se sube.
> - [ ] **¿Publicable?** → gate `dg-publish` + que la nota que lo embeba sea pública.
> - [ ] **¿Huérfano?** → si ningún archivo publicado lo referencia, es material de trabajo:
>       no es error, pero se anota para que nadie lo busque después.
> - [ ] **Handoff a D2** → la pista se publica en el tablero y `opencode` la toma.

## Handoff D1 → D2

> [!info] 🔁 El flujo
> `El usuario deja el material` → **D1** lo detecta y deja la pista (este archivo + aviso en el
> tablero) → **D2** (`opencode`) convierte ese material en **notas de la materia**
> (`Universidad/3er Semestre/<Materia>/`) → el **carril C** (`opencode-site`) se encarga de los
> diagramas que falten y de los links rotos.
> **Nadie edita notas de otro carril:** D1 registra, D2 escribe.

## Pedido al carril A: que la detección sea automática

> [!request] 🧩 `opencode-onedrive` (dueño de `Universidad/Herramientas/Mantenimiento/`)
> Hoy D1 compara **a mano**. Para que sea automático, hace falta **un** script (no dos):
> `qa_material_nuevo.py` con dos modos:
> - `--baseline` → escribe un snapshot (ruta + tamaño + SHA-256) de las 5 rutas de la tabla de
>   arriba → el archivo de snapshot, en `Mantenimiento/`.
> - `--check` → compara el estado actual contra el snapshot y **lista lo nuevo, lo borrado y lo
>   modificado** (exit ≠ 0 si hay algo nuevo).
> Requisitos: `--dry-run`, `--vault <ruta>`, **sin rutas absolutas**, y los patrones de las
> **5 rutas** en una constante al principio del archivo (no en el código hardcodeado).
> **D1 no lo escribe**: `Mantenimiento/` es tu zona (carril A).

## Estado del carril

> [!success] ✅ D1 — en curso
> - [x] Las 5 rutas exactas identificadas y verificadas (incluido el acento de `Teórico`).
> - [x] Línea base de los **367 archivos** con SHA-256, pesos y duplicados.
> - [x] Copyright revisado contra `_no-publicar.txt` (todo cuadra, 1 duda anotada).
> - [x] Checklist por lote y handoff a D2 definidos.
> - [ ] **Script de detección automática** → pedido al carril A.
> - [ ] **Primer lote nuevo** → cuando el usuario deje material, se registra aquí.

---

**Tags:** #clippings #intake #3er-semestre #carril-d1
