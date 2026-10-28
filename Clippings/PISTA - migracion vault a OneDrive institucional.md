---
dg-publish: false
tags: [clippings, pista, infraestructura, onedrive, decision, telefono]
---

# PISTA - cambio de cuenta de OneDrive (AutoSync en el teléfono + vault en la institucional)

> [!question] ✅ Decisión final (2026-10-27, 18:20): **NO se migra**
> El usuario probó la cuenta institucional (1 TB) de punta a punta y decidió **no migrar**:
> - La **personal** (5 GB) queda como vault de lo de la U: tras la limpieza quedan **2,4-2,6 GB
>   libres**, y lo que realmente topaba la cuenta era el **historial de versiones + duplicados**
>   (no la papelera).
> - La **institucional** (`fredsanc@espol.edu.ec`) **queda dada de alta y vacía**, disponible
>   para lo que se quiera hacer después (p. ej. fotos del teléfono).
> - El motivo técnico de que no haya Obsidian local en el teléfono: **el MDM de ESPOL no
>   permite a AutoSync emparejar carpetas**, y la app oficial de OneDrive para Android solo
>   crea carpetas en la nube. Editar en el móvil exigiría **Obsidian Sync (de pago)**.
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

> [!info] 📑 Índice
>
> - [[#Contexto medido (2026-10-27)]]
> - [[#Preguntas para los otros agentes]]
> - [[#Datos ya verificados (no volver a medir)]]
> - [[#Lo que se hizo (27/10/2026, 16:45–17:05) — `opencode-nube`]]
> - [[#Cancelación (27/10/2026, 18:20) — `opencode-nube`]]
> - [[#Estado]]

## Contexto medido (2026-10-27)

> [!info] 📁 Contexto medido: qué sirve en la nube
>
> | Carpeta | Tamaño | ¿Sirve en la nube? |
> |---|---|---|
> | `Universidad/` | 1,11 GB | Sí — es el contenido real (notas + PDF + 1 `.wmv` de 58 MB) |
> | `site/` (código versionado) | 1 MB | Sí — es el repo del sitio (30 rutas) |
> | `site/public/assets/` | **664 MB** | **No** — artefactos del sync, ya ignorados por `site/.gitignore`; se regeneran en cada build |
> | `site/notes-md/` | 13 MB | **No** — copia regenerable del vault en markdown |
> | `.git/` | **658 MB** | Opcional — ya espejado en GitHub; un solo pack. En la copia institucional **sí** se copió, para que el repo sea autónomo |
> | `.obsidian/` | 162 MB | **No** — ignorado por git, se regenera |
> | `.git/` huérfano en la raíz de OneDrive | 23 MB | **No** — rama `main` abandonada, se puede borrar |
> | `OneSyncFiles-backups/` | 458 MB | Opcional |
> | **Copia institucional** | 1,77 GB / 1 TB | **Se hizo, se verificó y se eliminó (18:20)** — queda en `#procesado` |

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

## Cancelación (27/10/2026, 18:20) — `opencode-nube`

6. **El usuario cancela la migración** y pide eliminar la copia institucional.
   Motivo: con la personal (2,4-2,6 GB libres tras la limpieza) el vault de lo de la U cabe
   igual, y **el MDM de ESPOL no deja emparejar carpetas** en AutoSync; la app oficial de
   OneDrive para Android **solo crea carpetas en la nube** ("Agregar carpeta" = le pones un
   nombre), así que **no hay forma de tener Obsidian con archivos locales en el teléfono**
   sin pagar **Obsidian Sync**. Para **leer** en el móvil, el sitio ya está publicado
   (806 notas + buscador) y no requiere ninguna sincronización.
7. **Copia institucional eliminada**: `rd /s /q` con prefijo `\\?\` (las rutas >260 chars
   fallaban en el `rd` normal: 35 archivos con error *"no se puede encontrar la ruta"*) →
   **0 archivos restantes**. La carpeta `OneSyncFiles` ya no existe en la raíz
   institucional; el cliente propaga los borrados a la nube (papelera de 1 TB, sin efecto).
8. **No se perdió nada**: lo borrado está en **GitHub** (`origin/master`) y en el vault
   personal, que nunca se movió ni se borró (verificado: `973e791`, árbol limpio, 0/0).
9. **Efecto colateral favorable** (riesgo que `opencode` había medido a las 17:40): al quedar
   **un solo clon**, los **12 archivos con ruta literal** `OneDrive\OneSyncFiles` y el
   **fallback de `sync-vault.mjs:20`** vuelven a apuntar al vault real. **P6 vuelve a ser
   "solo si algún día se decide migrar"**.

## Estado

- **Estado:** #procesado — **migración cancelada** (18:20). La copia institucional se hizo,
  se verificó y **se eliminó**. El vault **personal sigue siendo el de trabajo de las 4
  sesiones**, sin cambios.
- **Veredicto final:** **no se migra.** La cuenta personal (5 GB) queda para lo de la U:
  tras la limpieza quedan **2,4-2,6 GB libres**, y lo que realmente topaba la cuenta era
  el **historial de versiones + duplicados**, no el contenido. La institucional (1 TB)
  **queda dada de alta y vacía** para lo que se quiera hacer después.
- **Lo que se aprendió (no volver a medir):**
  - El **registro huérfano `Business1`** (enero 2026) era la causa del "el login entra pero
    OneDrive no abre".
  - La **nube cuenta el historial de versiones** (30 días en cuenta personal): vaciar la
    papelera no libera eso.
  - **`.gitignore` no aplica a OneDrive**: el cliente sube `site/public/assets/` (664 MB),
    `.obsidian/` (162 MB) y el `.git/` huérfano (23 MB) igual que si fueran contenido.
  - **Copiar y verificar es barato y seguro**: `robocopy` con exclusiones + comprobación de
    que el **índice de git dé el mismo SHA-256** en ambas copias. Si algún día se repite,
    ese es el método.
  - **Dos clones con el mismo `origin` son un riesgo real** (pueden divergir sin avisar) y
    las rutas hardcodeadas siguen apuntando al vault personal.
- **Pendiente de decidir (usuario):**
  1. Si se **desvincula** la cuenta institucional del cliente de la PC (hoy está dada de
     alta y vacía) o se deja lista para fotos/1 TB.
  2. **Teléfono**: si en algún momento quiere **editar** en Obsidian desde el móvil → hace
     falta **Obsidian Sync** (de pago). Para **leer**, el sitio publicado ya basta.
  3. Si el material con copyright (Cambridge, `z-lib.org`) se llegaría a subir a la
     institucional en el futuro (hoy **no** está copiado ahí: la copia se eliminó).
  4. Retención de la institucional al terminar la carrera, si se vuelve a usar.
- **Pendiente de sesión (sin riesgo, reversible):** `site/public/assets/` **ya se borró**
  (28/10 00:30, por el usuario: 650 MB de artefacto de build → raíz local 2.647 → **1.997 MB**)
  y el **`.git/` huérfano de la raíz también** (28/10 01:00, con respaldo verificado en
  `C:\Users\Steven Sànchez\Documents\OneDrive-root-git-huerfano-20261028\` → raíz local
  **1.975 MB**). Falta **vaciar la papelera** en el web (1 clic). Queda decidir si
  `.obsidian/` (162 MB) sale de la nube con **"Dejar de sincronizar"** (lo deja local,
  Obsidian sigue funcionando).

---
**Tags:** #clippings #pista #infraestructura #onedrive #decision #telefono #procesado #cancelada
