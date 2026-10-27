---
dg-publish: false
tags: [clippings, log, opencode-onedrive, publicacion, calidad, vault]
---

# LOG - opencode-onedrive (sesión 2026-10-27)

> Sesión de **higiene de publicación del vault**. No es la sesión de links
> rotos (`LOG-opencode.md`), ni la del sitio/marca (`LOG-opencode-site.md`), ni
> la de nube (`LOG-opencode-nube.md`).
> **Zona que reservé:** `Universidad/2do Semestre/Cálculo Vectorial/**`,
> `site/scripts/sync-vault.mjs`, `site/RUNBOOK.md`,
> `site/docs/HISTORIAL-LANZAMIENTO.md`, `Universidad/Herramientas/SVGs por recrear.md`.
> **Commits:** todos en `master` y **pusheados** a `origin/master` (ver tabla abajo).

## 1. Qué hice, en orden

### 1.1 Sistema de publicación (lo que sostiene todo lo demás)

Regla final implementada en `site/scripts/sync-vault.mjs`:

| Regla | Qué hace | Por qué |
|---|---|---|
| Gate `dg-publish` | Solo se publica una nota con `dg-publish: true` | El vault tiene material de clase y libros que no van al sitio |
| `Universidad/_no-publicar.txt` | Lista con comodines `*` y `?`, coincidencia por **nombre o ruta** | Material con copyright que sí vive en el vault pero no se distribuye |
| Solo assets referenciados | Un archivo se copia a `public/` **solo si** alguna nota publicada lo referencia | Evita subir capturas y PDFs huérfanos |
| Fix de embeds | `![[Nota]]` sin extensión de media → `[[Nota]]` | Evita que un enlace a nota se convierta en asset roto |
| Marcador `<!-- nx:asset-omitido -->` | Se deja constancia en la nota de qué se excluyó y por qué | Para que nadie piense que el archivo se perdió |

**Números verificados tras el merge** (`npm run sync`): 805 notas publicadas ·
3 omitidas · 2777 assets referenciados · 17 patrones / 61 archivos excluidos ·
831 páginas en `npm run build`.

### 1.2 Cálculo Vectorial (mi zona)

- 16 diagramas que eran *placeholders* ("Concepto clave / Definición formal")
  sustituidos por las versiones con contenido real, con los embeds actualizados.
- 2 diagramas "Teorema Fundamental de Línea" corregidos: tenían contenido de
  "Distancias en R³" (copia de otro diagrama).
- 37 diagramas maestros huérfanos integrados en sus 32 notas (insertados tras
  el primer callout de intro) → **0 embeds de diagramas rotos** en todo el vault.
- Borrados: `test.svg` del pipeline, 9 SVG superados, 2 duplicados exactos de
  `Figuras/`, `Tarea 2.md` + su PNG, `04_-_Propiedades_de_las_Operaciones_01_temp.svg`.
- 332 previews de `SVG-Pipeline/previews/` borrados (12,7 MB) + regla `previews/`
  en `.gitignore`.
- `Universidad/Herramientas/SVGs por recrear.md` regenerada: 474 entradas
  obsoletas → **0**.

### 1.3 Copyright

- **Fuga real cerrada:** `Escucha Activa Parte 1/2_OCR.pdf` **se estaban
  publicando** (el patrón no cubría el sufijo `_OCR`). Ahora están en
  `_no-publicar.txt`.
- `Universidad/_no-publicar.txt` quedó como **unión** de las listas de dos
  sesiones (17 patrones): libros `z-lib.org`, Cambridge (`Empower*.pdf`,
  `CAMBRIDGE ONE_GUIDE...`), UML Stevens, Refactoring, Pressman, Clean
  Architecture, Johnsonbaugh, Rosen, el `.wmv` de dinámicas y los derivados
  `_OCR` de Escucha Activa.

### 1.4 Documentación

- `site/RUNBOOK.md`: nueva sección "Qué se publica (notas y archivos)" +
  renumerado + "Notas omitidas" con el marcador `nx:asset-omitido`.
- `site/docs/HISTORIAL-LANZAMIENTO.md`: estadísticas reales (805 / 3 / 831 /
  2745 assets) y decisiones 1-9.
- `Clippings/00 - LEEME bandeja de pistas.md`: protocolo multi-agente (claim por
  rename `PISTA - <tema> [EN-PROCESO <agente>].md`, bitácora por agente, stage por
  rutas exactas, nunca `git add -A`) y sección "Progreso de los agentes" con la
  entrada de cada sesión.

### 1.5 Integración entre sesiones (lo que más tiempo consumió)

Hubo **tres sesiones** trabajando en el mismo vault y el mismo remoto:

| Sesión | Zona | Bitácora |
|---|---|---|
| `opencode` (3er Semestre) | links rotos, `Herramientas/Mantenimiento/**` | `LOG-opencode.md` |
| `opencode-site` (clon Desktop) | estilos, marca, visor PDF, exclusiones | `LOG-opencode-site.md` |
| `opencode-nube` | decisión de migración de nube | `LOG-opencode-nube.md` |
| `opencode-onedrive` (esta) | reglas de publicación + Cálculo Vectorial | este archivo |

Lo que hubo que resolver:

1. **El remoto (`origin/master`) y el local tenían dos implementaciones
   distintas de `_no-publicar.txt`.** Se integraron en **una sola** en
   `sync-vault.mjs`: la de la otra sesión (`leerNoPublicar`/`coincideNoPublicar`,
   exportadas) + la mía (`globToRegex` con comodines, coincidencia por ruta y
   la pre-pasada de assets referenciados).
2. **Los PDFs de FESD y Matemáticas Discretas**: ganó la layout **local** con
   subcarpetas (`Diapositivas/`, `Guías/`, `Talleres/`, `Lecciones/`,
   `Exámenes/`) y se borraron las copias planas duplicadas del remoto.
3. **Causa raíz del ruido CRLF (la encontré midiendo, no adivinando):** 82 `.md`
   de `Preuniversitario/Matemáticas` tenían **CRLF dentro del blob commiteado**.
   Como `.gitattributes` dice `*.md text eol=lf`, git los marcaba como
   modificados aunque el contenido fuera idéntico → **todos los merges fallaban**
   con `Your local changes would be overwritten by merge`. Se normalizó solo el
   fin de línea (`a05dfa4`) y los merges volvieron a funcionar.
4. **Un merge sobrescribió trabajo sin commitear de otra sesión** (nota de
   Inglés III, nota de BD y `qa_links.py`). Se recuperó desde el commit del
   stash descartado (`ea525f6`) y se confirmó que el merge final traía esa
   misma versión.

## 2. Commits de esta sesión

| Commit | Qué |
|---|---|
| `374e833` | `site/scripts/sync-vault.mjs`: publicar solo assets referenciados + `_no-publicar.txt` + `.gitignore` + borrados |
| `5aded86` | `Clippings/00 - LEEME bandeja de pistas.md`: protocolo multi-agente |
| `67ed5ac` | `Universidad/Herramientas/SVGs por recrear.md` regenerada |
| `462191b` | `2do Semestre/Cálculo Vectorial`: 37 diagramas maestros integrados |
| `6a41cf9` | `site/RUNBOOK.md` + `site/docs/HISTORIAL-LANZAMIENTO.md` |
| `d45c240` | `_no-publicar.txt`: derivados `_OCR` de Escucha Activa |
| `ca4ab56`, `99d8c22`, `17df803`, `ef26d75`, `8fedc9f` | merges con el clon Desktop |
| `a05dfa4` | normalizar fin de línea de 82 `.md` (desbloquea los merges) |
| `544ba11` | responder en el LEEME las preguntas de `opencode-site` |

## 3. Propuestas

### P1 — Un `git worktree` por sesión (arregla la carrera entre agentes)

Hoy las tres sesiones comparten **el mismo directorio de trabajo y el mismo
remoto**. Consecuencia medida: un merge sobrescribió cambios sin commitear de
otro agente. Propuesta: cada sesión trabaja en su propio
`git worktree` (rama propia) y **solo una** integra a `master`.

```bash
git -C "C:/Users/Steven Sànchez/OneDrive/OneSyncFiles" worktree add ../wt-links -b sesion/links master
```

Ventajas: nadie pisa a nadie, los merges se hacen una vez al final, y el
`git status` de cada sesión es limpio.

### P2 — Lista blanca para el material con copyright (decisión del usuario)

`_no-publicar.txt` es una **lista negra**: si se olvida un archivo, se publica.
Propuesta: invertirla — un `Universidad/_publicar.txt` explícito, o mover el
material con copyright a `Universidad/_privado/` (carpeta que el sync ignora por
estructura, no por nombre). Es más difícil que se escape algo.

Mientras tanto, lo que **ya está protegido**: 17 patrones, 61 archivos.

### P3 — Verificación de publications en CI (que no se repita la fuga)

Hoy la exclusión depende de que alguien recuerde agregar el patrón. Propuesta:
un workflow de GitHub Actions que corra `npm run sync` + `npm run build` en cada
PR y **falle** si:

- algún archivo de `public/assets` está en `_no-publicar.txt`, o
- algún archivo excluido aparece en `public/downloads/*.zip`.

Es la red de seguridad que faltó para `Escucha Activa Parte 1_OCR.pdf`.

### P4 — Que el embed roto se detecte antes de publicar

Existen ya `qa_links.py` y `verificar_nota.py` en `Universidad/Herramientas/`.
Propuesta: mover ahí mis scripts de auditoría (están en
`C:\Users\STEVEN~1\AppData\Local\Temp\opencode\`) y dejar **una sola** entrada
que corra todo:

| Script | Qué detecta |
|---|---|
| `qa_resolucion_diagramas.py` | embeds de diagramas cuyo archivo no existe |
| `qa_assets_huerfanos.py` | assets en el vault que ninguna nota referencia |
| `qa_fugas_copyright.py` | archivos con copyright que sí se publicarían |
| `qa_svg_titulo.py` | SVG placeholder ("Concepto clave") que quedó sin sustituir |

### P5 — Sacar `site/` del vault (resuelve la cuota sin migrar nada)

`site/` pesa **1,83 GB** dentro del vault y es **todo regenerable**
(`node_modules` 211 MB, `dist` 874 MB, `public/assets` 649 MB,
`public/downloads` 74 MB). El RUNBOOK ya dice que no debería vivir ahí.
Sacarlo **libera 1,83 GB de la cuota personal sin tocar la nube institucional**
y elimina de raíz la ambigüedad de "dos clones".

Relacionado: `.git/` pesa 1,50 GB con un pack de 546 MB y hay un
`.git/gc.pid` de un `git gc` interrumpido → un `git gc --aggressive` local
compactaría bastante.

### P6 — Parametrizar las rutas absolutas antes de migrar

Hay **15+ archivos** con rutas hardcodeadas a
`C:\Users\Steven Sànchez\OneDrive\OneSyncFiles` (lista completa en
`PISTA - migracion vault a OneDrive institucional.md`). Si el vault se mueve a
`OneDrive - <Organización>`, todos se rompen. Propuesta: una sola variable de
entorno (`VAULT_ROOT`) con fallback a la ruta actual, leída por los ~12
scripts Python de `Universidad/Herramientas/` y por `sync-vault.mjs`.

### P7 — Limpiar los 32 PNG huérfanos de `Universidad/Figuras/`

Son material en curso de **Matemáticas Discretas** (`01-cardinalidad.png`,
`05-de-morgan.png`, `09-hasse.png`, `U3-*`, `U5-cubo.png`…). Con la regla "solo assets referenciados" **no llegan
al sitio**, pero siguen ocupando sitio en el vault. Propuesta: moverlos a la
carpeta de la unidad que los usa cuando se integren en las notas, o borrarlos
si ya no sirven.

### P8 — Arreglar los `verificar_nota.py` que fallan en Cálculo Vectorial

Quedaron vacías dentro de fences en callouts de las notas de CV (las reporta
`Universidad/Herramientas/Reportes/qa_refs_checkbox_2026-10-26.md`). Son de mi
zona; los arreglo en una pasada propia si me das luz verde.

## 4. Lo que necesito

- **Del usuario:** decidir P2 (lista negra vs lista blanca), P5 (sacar `site/`
  del vault) y responder si el material con copyright puede vivir en la cuenta
  institucional.
- **De `opencode-site`:** ya está resuelto (no tocar `sync-vault.mjs` sin
  avisar; `_no-publicar.txt` no se vuelve a tocar sin avisar).
- **De `opencode` (3er Semestre):** nada pendiente de mi parte; su trabajo
  (nota de BD + `qa_links.py`) quedó commiteado.
- **De `opencode-nube`:** P5 y P6 tocan su pista; lo dejo decidir a esa sesión
  y al usuario, y por eso no muevo nada.

## 5. Estado al cierre

- `master` = `origin/master` (0/0), sin conflictos pendientes.
- `npm run sync` → 805 publicadas · 3 omitidas · 2777 assets · 17 patrones.
- `npm run build` → 831 páginas, sin errores.
- Working tree limpio, salvo lo que pertenece a otras sesiones.

---
**Tags:** #clippings #log #opencode-onedrive #publicacion #calidad #vault
