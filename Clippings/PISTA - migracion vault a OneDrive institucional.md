---
dg-publish: false
tags: [clippings, pista, infraestructura, onedrive, decision, telefono]
---

# PISTA - cambio de cuenta de OneDrive (AutoSync en el teléfono + vault en la institucional)

> [!question] ✅ Decisión tomada (2026-10-27, 16:45)
> La cuenta **personal** de OneDrive está al límite (5 GB, con muro de cuota) y el proyecto sigue creciendo.
> **Decisión del usuario: pasar el vault a la cuenta institucional (1 TB).** La cuenta ya está dada de alta
> (`fredsanc@espol.edu.ec`) y el vault **ya está copiado y verificado** en
> `C:\Users\Steven Sànchez\OneDrive - Escuela Superior Politécnica del Litoral\OneSyncFiles`.
> El vault **personal no se movió ni se borró**: sigue siendo el de trabajo de las 4 sesiones.
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
| `site/` (código versionado) | 1 MB | Sí — es el repo del sitio (30 rutas) |
| `site/public/assets/` | **664 MB** | **No** — artefactos del sync, ya ignorados por `site/.gitignore`; se regeneran en cada build |
| `site/notes-md/` | 13 MB | **No** — copia regenerable del vault en markdown |
| `.git/` | **658 MB** | Opcional — ya espejado en GitHub; un solo pack. En la copia institucional **sí** se copió, para que el repo sea autónomo |
| `.obsidian/` | 162 MB | **No** — ignorado por git, se regenera |
| `.git/` huérfano en la raíz de OneDrive | 23 MB | **No** — rama `main` abandonada, se puede borrar |
| `OneSyncFiles-backups/` | 458 MB | Opcional |
| **Copia institucional** | **1,77 GB / 1 TB** | **Ya subida y verificada** (4.687 archivos, 4.687/4.687 en la nube) |

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

## Lo que se hizo (27/10/2026, 16:45–17:05) — `opencode-nube`

1. **Cuenta institucional dada de alta** en el cliente de escritorio:
   `Business1` → `fredsanc@espol.edu.ec`, `UserFolder` =
   `C:\Users\Steven Sànchez\OneDrive - Escuela Superior Politécnica del Litoral`,
   `LastSignInResult=0`, `HasMadeFirstUpload=1`.
   Antes existía un **registro huérfano de enero 2026** (sin `UserFolder`, ECS expirado
   07/01/2026) → por eso el login de Microsoft pasaba pero el cliente no abría ninguna
   unidad. Esa era la causa real del "entra pero no entra al OneDrive".
2. **Prueba de humo OK**: archivo de prueba subido y confirmado como ítem de nube
   (`ReparsePoint` + `System.StorageProviderId = OneDrive`).
3. **Copia (nunca movimiento) del vault** con `robocopy`, excluyendo lo regenerable
   (`site/public/assets`, `site/notes-md`, `site/dist`, `site/.astro`, `site/node_modules`,
   `.obsidian`, `.trash`): **4.687 archivos · 1,729 GB · 0 errores**.
4. **Verificación de integridad** (no solo "copió bien"):
   - `HEAD` idéntico en las dos copias (`fec4b97`);
   - **índice de git con SHA-256 idéntico** → 4.533 archivos trackeados con los mismos
     blob-sha (contenido versionado bit a bit idéntico);
   - `git fsck` sin errores (solo 2 objetos *dangling* del historial);
   - **4.687/4.687 archivos en la nube** en ~3 min; carpeta renombrada de
     `OneSyncFiles-migracion` a `OneSyncFiles`.
   - La diferencia de 13 `.md` quedó explicada: 12 `README.md` de plugins dentro de
     `.obsidian` y 1 de la papelera interna `.trash` (ambas excluidas a propósito).
5. **Causa real de que la cuota personal no bajara**: el **historial de versiones**
   (30 días en cuenta personal) conserva lo borrado, y en la nube siguen
   **duplicados que git no versiona** (`site/public/assets/` 664 MB, `.obsidian/` 162 MB,
   `.git/` huérfano 23 MB). `.gitignore` solo aplica a git: OneDrive sube esas carpetas igual.

## Estado

- **Estado:** #migracion-en-curso — la copia institucional **ya está hecha y verificada**.
  El vault **personal no se movió ni se borró**: sigue siendo el de trabajo de las 4 sesiones.
- **Veredicto (cambia el de las 4 sesiones):** la migración **sí se hace** — decisión del
  usuario: la institucional da **1 TB gratis** y la personal (5 GB) está topada con muro de
  cuota. Lo que **no** cambia: la verdad del trabajo es **GitHub**, y nada se borra de la
  personal hasta que el usuario diga cuál queda activa.
- **Pendiente de decidir (usuario):**
  1. **Cuál vault queda activo**: el personal o el institucional (esto implica **P6**,
     `VAULT_ROOT` en los 15+ archivos con ruta absoluta, y avisar a las 3 sesiones).
  2. **Teléfono**: app oficial de OneDrive con `fredsanc@espol.edu.ec` (notas + fotos);
     si ESPOL bloquea apps de terceros por MDM, esa oficial es el plan B.
  3. Cuota real por usuario de la institucional.
  4. Límite por archivo (el `.wmv` pesa 58 MB; en cuentas educational suele bajar a 250 MB).
  5. Retención al terminar la carrera: el material ya quedó copiado ahí.
  6. Si el material con copyright (Cambridge, `z-lib.org`) es aceptable en una cuenta
     institucional.
- **Pendiente de sesión (sin riesgo, reversible):** excluir `site/public/assets/` y
  `.obsidian/` de la nube personal (click derecho → OneDrive → Dejar de sincronizar) y
  borrar el `.git/` huérfano de la raíz de OneDrive → libera ~850 MB y corta el
  historial de versiones.

---
**Tags:** #clippings #pista #infraestructura #onedrive #decision #telefono #migracion-en-curso
