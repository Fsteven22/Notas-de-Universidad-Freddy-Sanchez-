# PISTA - Mensaje para opencode: pendientes y taxonomía Unidad 0

> [!info] 📌 De: `opencode-nube` → Para: `opencode` (3er Semestre)
> Fecha: 29/10/2026 · Zona: `Clippings/` (mía) · No toca `Universidad/**` ni `site/**`.

---

## 1. Respuesta a tus 3 pendientes (decisiones del usuario)

### Pendiente 1 — 7 PNG huérfanos (cierre carril B)

- **DSW U5:** `01b-p35.png`, `01b-p39.png`, `01b-p42.png`, `01b-p43.png`, `01b-p44.png`
- **BD U2:** `bd-023-p15.png`, `bd-s04-p12.png`

**Decisión del usuario:** si la información se puede embebir y enlazar, hazlo (embebé en las notas indicadas: `02 - Control de versiones con Git.md` para DSW, `04 - Normalización paso a paso.md` para BD). Si ya hay algo ocupando su lugar o ya no es necesario, descártalos.

### Pendiente 2 — Carril D2 (material nuevo 3er Semestre)

**Decisión del usuario:** aún no hay material nuevo de 3er Semestre. Déjalo **pendiente** para cuando llegue un nuevo `.pdf`. No actúes todavía.

### Pendiente 3 — Normalización de formato (14.106 errores en 306 notas)

**Decisión del usuario:** **sí**, hazlo, pero con cuidado:
- **Sin scripts que tengan riesgo de romper el vault.**
- Si vas a usar un script, **haz una copia de seguridad antes** (commit previo o copia del vault) para poder regresar si algo sale mal.
- Las 3 pasadas mecánicas: `ENDINGS mixed` (126 archivos, solo fin de línea) → frontmatter con líneas vacías (15 archivos) → líneas vacías dentro de fence/callout (3.935 líneas en 185 notas).

---

## 2. Advertencia: PDF de BD movido por el usuario (sin stagear)

`Database Systems - Design, Implementation, and Management (9th Edition).pdf` fue movido por el usuario de la raíz de BD a `Diapositivas/` y lo dejó **sin stagear**. Sigue en `_no-publicar.txt` por nombre, así que no se publica igual.

**No lo stagees ni lo toques sin su visto bueno.** `Universidad/3er Semestre/Sistema de Bases de Datos/` tiene cambios ajenos; ten cuidado al commitear esa materia.

---

## 3. Propuesta de taxonomía unificada para carpetas de Unidad 0 (3er Semestre)

> [!tip] Objetivo: evitar que `Diapositivas/`, `Guías/` y `Material de clase/` sigan solapándose.

Cada materia de 3er Semestre tendría en `Unidad 0 - Guías y Ejercicios/`:

```
00 - Leeme Unidad 0.md          (índice, mismo esqueleto en las 5 materias)
Diapositivas/                   (presentaciones del docente exportadas a PDF)
Guías/                          (guías de estudio, guías de problemas, ejercicios guiados)
Material de clase/              (capturas del libro, plantillas, audios, videos locales, material suelto de clase)
Talleres/                       (talleres y soluciones)
Lecciones/                      (lecciones y soluciones)
Exámenes/                       (exámenes y resoluciones)
Diagramas/                      (drawio + svg generados)
Figuras/                        (imágenes PNG/JPG sueltas)
```

**Regla de colocación:**
- Es una presentación de clase → `Diapositivas/`
- Es una guía de estudio o problemas → `Guías/`
- Es material suelto de clase (capturas, plantillas, multimedia local) → `Material de clase/`
- Tiene copyright (libros `z-lib.org`, Cambridge, etc.) y no se publica → no va en ninguna de las tres; queda en `_local/` o en la raíz de `Unidad 0` (a decidir)

**Método de migración (por materia):**
1. `git mv` de cada archivo a su carpeta destino.
2. Actualizar todas las referencias `![[ruta/archivo]]` y `[[ruta/archivo]]` que usen rutas.
3. Verificar con `qa_links.py` que queden 0 links rotos en esa materia.
4. Verificar build del sitio en **worktree local** (nunca dentro de OneDrive).
5. Commit por materia (hash + `cerrado` + línea en tu bloque del tablero).

---

## 4. Qué necesito de vos

Revisá esta pista y, cuando tengas turno, ejecutá lo que te corresponda en tu zona (`Universidad/3er Semestre/**`). Si tenés dudas sobre algún archivo en particular, avisá en el tablero antes de commitear.

> [!success] Estado: propuesta lista para revisión de `opencode`.

> [!info] ✅ Autorización del usuario (29/10/2026)
> El usuario autorizó que `opencode` commitee el PDF `Database Systems - Design, Implementation, and Management (9th Edition).pdf` (movido de la raíz de BD a `Diapositivas/`). **No se sube a la web**: sigue en `_no-publicar.txt` por nombre.

**Tags:** #clippings #pista #opencode #taxonomia #unidad0
