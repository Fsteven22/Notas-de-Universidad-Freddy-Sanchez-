---
dg-publish: false
tags: [clippings, pista, infraestructura, onedrive, decision, telefono]
---

# PISTA - cambio de cuenta de OneDrive (AutoSync en el teléfono + vault en la institucional)

> [!question] ❓ Decisión que hay que tomar
> La cuenta **personal** de OneDrive está al límite (4,99 GB de 5 GB) y el proyecto sigue creciendo.
> El plan: pasar el vault a la **cuenta institucional (1 TB)** y, en el teléfono, cambiar
> **OneSync (Samsung) → AutoSync** apuntando a esa misma cuenta institucional.
> Nadie debe arrancar a mover carpetas sin leer esto.

> [!info] 📌 Aclaración de alcance (corregida 2026-10-27)
> **AutoSync y OneSync son clientes de sincronización del teléfono, no del escritorio.**
> - **OneSync** = la integración de OneDrive de Samsung (Ajustes → Cuentas → OneDrive /
>   Samsung Gallery): sube fotos/archivos del teléfono a la cuenta de OneDrive que tengas
>   configurada.
> - **AutoSync** = app de Android que hace lo mismo pero te deja **elegir la cuenta y
>   las carpetas** (emparejamiento carpeta local ↔ carpeta de OneDrive, 1 o 2 vías).
> - La PC no usa ninguno de los dos: la PC usa el **cliente de escritorio de OneDrive**
>   sobre `C:\Users\Steven Sànchez\OneDrive\OneSyncFiles`.
>
> **Consecuencia clave:** cambiar el teléfono a la institucional solo sirve si **la PC
> también pasa a la institucional**. Si el teléfono va a la institucional y la PC sigue en
> la personal, el teléfono ve **otra copia** (o nada) del vault: no es "la misma carpeta
> con más espacio", son dos cuentas distintas.

> [!warning] ⚠️ Evidencia reproducida 3 veces: `node_modules` NO puede vivir en OneDrive
> 1. `npm run build` falla con `Cannot find module ...\node_modules\astro\dist\cli\throw-and-exit.js`
>    → OneDrive deshidrató la carpeta (no existía).
> 2. `npm ci` falla con `ENOTEMPTY ... rmdir node_modules\hastscript\lib` → OneDrive y npm
>    peleando por el mismo directorio.
> 3. Build de control **fuera** de OneDrive (copia del código en disco local + junction al
>    vault): `npm ci` OK → `npm run sync` → 806 notas → `npm run build` → **833 `.html`,
>    exit 0**, `speaking-practice-2` publicado, `favicon.ico` presente.
>
> **Regla:** el vault de OneDrive guarda **notas y assets**; el código del sitio y su
> `node_modules` se compilan **en disco local**.

## Contexto medido (2026-10-27)

| Carpeta | Tamaño | ¿Sirve en la nube? |
|---|---|---|
| `Universidad/` | 1,11 GB | Sí — es el contenido real (notas + PDF + 1 `.wmv` de 58 MB) |
| `site/` | 1,83 GB | **No** — `node_modules` 211 MB, `dist` 874 MB, `public/assets` 649 MB, `public/downloads` 74 MB: todo regenerable, todo en `.gitignore` |
| `.git/` | 1,50 GB | **No** — ya espejado en GitHub; un solo pack de 546 MB |
| `.obsidian/` | 167 MB | **No** — ignorado por git, se regenera |
| `OneSyncFiles-backups/` | 0,45 GB | Opcional |
| **Total OneDrive root** | **4,99 GB / 5 GB** | Cuota personal agotada |

## Preguntas para los otros agentes

1. **¿Migrar la carpeta o migrar el repositorio?** El vault **es** un repo git
   (`origin` = `Fsteven22/Notas-de-Universidad-Freddy-Sanchez-`). Al cambiar de cuenta,
   la institucional se monta en otra ruta (Windows: `OneDrive - <Organización>`), no en
   `C:\Users\<user>\OneDrive`. ¿`git clone` en la ruta nueva + se copian encima los
   cambios sin commitear, o se mueve la carpeta tal cual?
2. **¿AutoSync en el teléfono sincroniza el vault entero?** No debería: 1,1 GB de PDFs +
   un `.wmv` de 58 MB + `.git` (pack de 546 MB) es unasync masivo por datos y batería.
   ¿Qué carpetas exactas se emparejan (¿solo `DCIM/Camera` y `Documentos`?) y en qué
   dirección (¿2 vías para fotos, 1 vía de solo descarga para leer notas)?
3. **Rutas absolutas**: ¿se parametrizan todas de una vez (env var `VAULT_ROOT`) o se
   deja `VAULT_DIR` solo para el sync del sitio?
4. **¿Se mueve `site/` fuera del vault antes de migrar?** El RUNBOOK ya lo prohíbe
   dentro del vault, y son 1,83 GB recuperables sin tocar la nube institucional.
5. **¿Qué pasa con `.git`?** ¿Se deja sincronizado por OneDrive, se mueve con
   `git init --separate-git-dir`, o se compacta y se acepta el churn?
6. **¿OneSync (Samsung) se apaga?** Al dejar de usarlo, Samsung Gallery deja de subir
   fotos nuevas a la personal. ¿Se reemplaza por un emparejamiento en AutoSync
   (`DCIM/Camera` → `OneDrive/Imágenes`) o por Galaxy Cloud?

## Datos ya verificados (no volver a medir)

- **El deploy no depende de la nube local.** `site/vercel.json:4` corre
  `VAULT_DIR=../Universidad npm run sync && npm run build` dentro del repo en GitHub.
  Cambiar de cuenta de OneDrive no toca Vercel, ni `dg-publish`, ni `_no-publicar.txt`.
- **Rutas hardcodeadas a `C:\Users\Steven Sànchez\OneDrive\OneSyncFiles`** (a cambiar si
  la ruta del vault cambia):
  - `site/scripts/sync-vault.mjs:19-20` (fallback por defecto)
  - `Universidad/Herramientas/SVG-Pipeline/`: `vlib.py:4`, `test_single.py:8`,
    `buildcv_missing.py:5`, `buildcv_auto.py:5`, `buildcv_lote2.py:86`,
    `buildcv_lote3.py:228`, `buildcv_lote4.py:553`, `buildcv_nabla.py:205`,
    `descargar-material-ccpg1001.py:23,25`
  - `Universidad/Herramientas/`: `estilo.py:41`, `auditoria.py:22`, `detectar_vacios.py:22`
  - `Universidad/Herramientas/README.md:25`, `Universidad/Herramientas/Scripts/LEEME-SCRIPTS.md:75-76`,
    `Universidad/Herramientas/Scripts/GUIA-PDF-A-MARKDOWN.md:64`
- **Estado git en el momento de dejar la pista** (rama `master`): 17 commits por delante
  de `origin/master` y 3 por detrás; 60 entradas sin commitear; existe `.git/gc.pid`
  (un `git gc` interrumpido). Antes de mover nada hay que commitear o pushear.
- **Disciplina de copias vigente** (`site/RUNBOOK.md:54-61`): las notas se editan en el
  vault de OneDrive, el código del sitio vive en el clon de Desktop
  (`notas-nexus-unificado/`). La migración no puede romper esa separación.
- **Ventaja de la cuenta institucional**: 1 TB en vez de 5 GB, y es la que sobrevive
  cuando el proyecto crezca (lo que no cabe hoy en `Universidad/` + PDFs nuevos).
- **A verificar antes de migrar** (no está comprobado todavía):
  1. Cuota real por usuario de la institucional (¿1 TB o "unlimited" compartido?).
  2. Límite de tamaño por archivo (en OneDrive para empresas/educación suele bajar a
     250 MB; el vault tiene un PDF de 71,6 MB y un `.wmv` de 58 MB, pero puede crecer).
  3. **Si la institucional bloquea apps de terceros**: las cuentas institucionales suelen
     aplicar acceso condicional/MDM y pueden impedir que una app como AutoSync (OAuth
     propio) autentique. Si pasa, el plan B es la **app oficial de OneDrive para Android**
     con la cuenta institucional, o pedir la app en el catálogo del tenant.
  4. Retención/borrado de la cuenta al terminar la carrera (y qué pasa con el vault).
  5. Si el material de cátedra con copyright (libros Cambridge, PDFs `z-lib.org`) es
     aceptable en una cuenta institucional.

## Estado

- **Estado:** #procesado — el veredicto de las 4 sesiones está en
  `Clippings/00 - LEEME bandeja de pistas.md` → **"ACUERDO entre sesiones", Acuerdo 4**
  (y la "Respuesta final de `opencode-nube`"). **No hace falta tomar esta pista.**
- **Veredicto:** **la migración del vault NO es necesaria.** La cuota personal se
  resuelve limpiando lo generado (~1,8 GB) + compactando `.git`; el contenido real
  (`Universidad/`) son 1,11 GB y la personal tiene 5 GB.
- **Lo único que sí necesita la institucional es el teléfono** (fotos): AutoSync →
  institucional, emparejando solo `DCIM/Camera`.
- **Sigue pendiente del usuario** (bloquea cualquier movimiento de carpetas):
  1. **Autorizar la limpieza ya** — la cuenta pasó de cuota (5,13 GB / 5 GB).
  2. Cuota real por usuario de la institucional.
  3. Límite por archivo (el `.wmv` pesa 58 MB).
  4. Retención al terminar la carrera.
  5. Si el material con copyright (Cambridge, `z-lib.org`) es aceptable en una
     cuenta institucional.
  6. Teléfono: institucional o personal (si la institucional bloquea el OAuth por MDM).

---
**Tags:** #clippings #pista #infraestructura #onedrive #decision #telefono #procesado
