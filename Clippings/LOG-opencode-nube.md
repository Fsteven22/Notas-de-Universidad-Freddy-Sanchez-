---
dg-publish: false
tags: [clippings, log, opencode-nube, onedrive, infraestructura]
---

# LOG - opencode-nube (sesion 2026-10-27)

> Sesion de **infraestructura / nube**. No es la sesion de los links rotos
> (`LOG-opencode.md`) ni la del sitio (`LOG-opencode-site.md`).
> **No toco `Universidad/**` ni `site/**`**: solo escribo en `Clippings/`.

## Que hice

- Deje la pista `Clippings/PISTA - migracion vault a OneDrive institucional.md`.
- Anadi el aviso de esta sesion al final de `Clippings/00 - LEEME bandeja de pistas.md`.
- **Commits:** ninguno. No se commitea nada hasta que el usuario decida la migracion.

## Motivo

La cuenta **personal** de OneDrive esta al limite: **4,99 GB de 5 GB** en
`C:\Users\Steven Sànchez\OneDrive`. El plan del usuario es pasar el vault a la
**cuenta institucional (1 TB)** y, en el **telefono**, cambiar **OneSync (Samsung)
por AutoSync** apuntando a esa misma cuenta institucional.

**Aclaracion de alcance (corrige la primera version de la pista):** AutoSync y OneSync
son **clientes de sincronizacion del telefono**, no del escritorio. La PC usa el cliente
de escritorio de OneDrive sobre `C:\Users\Steven Sànchez\OneDrive\OneSyncFiles`.
Consecuencia: cambiar el telefono a la institucional solo sirve si **la PC tambien pasa
a la institucional**; si no, el telefono ve otra copia del vault (son dos cuentas
distintas, no "la misma carpeta con mas espacio").

## Hallazgos (medidos, no re-medir)

| Carpeta | Tamano | Sirve en la nube? |
|---|---:|---|
| `Universidad/` | 1,11 GB | Si: es el contenido real (notas + PDF + 1 `.wmv` de 58 MB) |
| `site/` | 1,83 GB | **No**: `node_modules` 211 MB, `dist` 874 MB, `public/assets` 649 MB, `public/downloads` 74 MB. Todo regenerable y todo en `.gitignore` |
| `.git/` | 1,50 GB | **No**: ya espejado en GitHub. Un solo pack de 546 MB |
| `.obsidian/` | 167 MB | **No**: ignorado por git, se regenera |
| `OneSyncFiles-backups/` | 0,45 GB | Opcional |
| **Total OneDrive root** | **4,99 GB / 5 GB** | Cuota personal agotada |

1. **El deploy no depende de la nube local.** `site/vercel.json:4` corre
   `VAULT_DIR=../Universidad npm run sync && npm run build` dentro del repo en GitHub.
   Cambiar de cuenta de OneDrive no toca Vercel, ni `dg-publish`, ni `_no-publicar.txt`.
2. **`site/` no deberia vivir en el vault** y ya lo dice el RUNBOOK
   (`site/RUNBOOK.md:58`). Sacarlo libera 1,83 GB de cuota **sin migrar nada**.
3. **`.git` pesa 1,50 GB** y existe un `.git/gc.pid`: hay un `git gc` interrumpido.
   El remoto ya tiene los binarios.
4. **Estado git al dejar la pista** (rama `master`): 17 commits adelante de
   `origin/master` y 3 atras; 60 entradas sin commitear. Antes de mover carpetas:
   commitear o pushear.
5. **Rutas absolutas a `C:\Users\Steven Sànchez\OneDrive\OneSyncFiles`** que se
   rompen si el vault cambia de carpeta (la cuenta institucional se monta en
   `OneDrive - <Organizacion>`, no en `...\OneDrive`):
   - `site/scripts/sync-vault.mjs:19-20` (fallback por defecto)
   - `Universidad/Herramientas/SVG-Pipeline/`: `vlib.py:4`, `test_single.py:8`,
     `buildcv_missing.py:5`, `buildcv_auto.py:5`, `buildcv_lote2.py:86`,
     `buildcv_lote3.py:228`, `buildcv_lote4.py:553`, `buildcv_nabla.py:205`,
     `descargar-material-ccpg1001.py:23,25`
   - `Universidad/Herramientas/`: `estilo.py:41`, `auditoria.py:22`, `detectar_vacios.py:22`
   - `Universidad/Herramientas/README.md:25`, `Universidad/Herramientas/Scripts/LEEME-SCRIPTS.md:75-76`,
     `Universidad/Herramientas/Scripts/GUIA-PDF-A-MARKDOWN.md:64`
6. **Riesgo con AutoSync**: OneDrive (Files On-Demand) + AutoSync + git sobre los mismos
   archivos = placeholders a medio hidratar, duplicados `(conflicto)` en Obsidian y
   corrupcion de `.git`. `.git/`, `node_modules/`, `dist/` y `.obsidian/` no deben pasar
   por una tercera capa de sync.
7. **A verificar antes de migrar** (no comprobado): cuota real por usuario de la
   institucional, limite de tamano por archivo, retencion al terminar la carrera, y si el
   material de catedra con copyright (libros Cambridge, PDFs `z-lib.org`) es aceptable
   en una cuenta institucional.
8. **Telefono**: la institucional suele aplicar acceso condicional/MDM y puede bloquear
   el OAuth de una app de terceros como AutoSync. Plan B: app oficial de OneDrive para
   Android con la cuenta institucional, o pedir la app en el catalogo del tenant.
   Ademas, el vault no se debe emparejar completo al telefono (1,1 GB de PDFs + `.git`
   de 1,50 GB): emparejar `DCIM/Camera` y `Documentos`, y el vault solo en modo
   descarga. Al apagar OneSync, Samsung Gallery deja de subir fotos a la personal.

## Rutas que reservo

- `Clippings/PISTA - migracion vault a OneDrive institucional.md`
- `Clippings/LOG-opencode-nube.md`
- El bloque "opencode-nube" al final de `Clippings/00 - LEEME bandeja de pistas.md`

## No toco sin avisar

- `Universidad/3er Semestre/**` (links) y `Universidad/Herramientas/Mantenimiento/**`
  (reservados por `LOG-opencode.md`).
- `Universidad/2do Semestre/Cálculo Vectorial/**`, `site/scripts/sync-vault.mjs`,
  `site/RUNBOOK.md`, `site/docs/HISTORIAL-LANZAMIENTO.md`,
  `Universidad/Herramientas/SVGs por recrear.md` (reservados por la sesion OneDrive).
- `site/src/styles/*`, `site/src/components/SearchModal.astro`, `site/src/pages/index.astro`,
  `site/src/layouts/Base.astro`, `site/public/*` (reservados por `LOG-opencode-site.md`).

## Cierre de la sesion — acuerdo de las 4 sesiones (27/10/2026)

### Que leo del LEEME y con que estoy de acuerdo

1. **Protocolo de commits y pushes** (`edd511b`, reinstallado por `opencode-onedrive`):
   stagear rutas exactas, nunca `git add -A`; `git fetch` -> ver `origin/master..HEAD` y
   `HEAD..origin/master`; `git pull --no-rebase` y resolver **conservando las dos
   versiones** del LEEME; nunca `push --force`, nunca `amend` de algo pusheado; un solo
   push a la vez y el turno se anuncia en "Avisos de otros agentes".
2. **Cola de push** con dueño por cada pendiente. Mi parte (item 3) era commitear
   `Clippings/LOG-opencode-nube.md` + `Clippings/PISTA - migracion vault a OneDrive
   institucional.md` **desde esta sesion**, que es lo que hice.
3. **Zonas reservadas**: la tabla atribuia a `opencode-onedrive` la zona de
   `3er Semestre`, que es de la sesion `opencode`. Ya corregido en el LEEME; hay
   **4 sesiones**, no 3.
4. **Acuerdo de migracion**: de acuerdo en **no migrar ahora**.

### Correccion que aporto (un error de hecho en el acuerdo)

El punto 4 del plan de migracion decia *"AutoSync: no"*, tratando a AutoSync como
un cliente de sincronizacion de **escritorio**. **AutoSync y OneSync son clientes de
sincronizacion del TELEFONO** (OneSync = la integracion de OneDrive de Samsung;
AutoSync = app de Android). La PC usa el cliente de OneDrive de Windows. El plan
correcto:

- **AutoSync -> cuenta institucional**, emparejando **solo `DCIM/Camera`** (2 vias).
  Eso es lo que sigue llenando la cuenta personal con fotos.
- **El vault NO se empareja al telefono**: 1,1 GB de PDFs + `.git` de 1,50 GB.
- Si el vault llegara a migrarse, telefono y PC deben apuntar a la **misma** cuenta,
  o el telefono ve otra copia (dos cuentas distintas, no "la misma carpeta con mas
  espacio").

### Numeros (medidos 27/10/2026)

| Carpeta | Peso | Liberable sin migrar |
|---|---:|---|
| `Universidad/` | 1,11 GB | no (contenido real) |
| `site/` (ignorado por git) | 1,83 GB | si: borrar `node_modules`, `dist`, `.astro`, `notes-md`, `public/assets`, `public/downloads`, `public/pdfjs/{build,web}`; se regenera con `npm ci && npm run sync && npm run build`. Los 28 archivos versionados de `site/` se quedan |
| `.git/` | 1,50 GB | si: `git gc --aggressive --prune=now` (hay un `gc.pid` de un gc interrumpido) |
| `.obsidian/` | 167 MB | si: git-ignored, se regenera |
| `OneSyncFiles-backups/` | 0,45 GB | opcional: mover a la institucional o borrar |
| **Total** | **4,99 GB / 5 GB** | **~3,9 GB liberables -> la personal queda en ~1,1 GB** |

Criterio de reevaluacion: migrar solo si `Universidad/` supera **3 GB** por si solo.

### Que NO hago

- No muevo ninguna carpeta: la PISTA queda en `#pendiente` hasta que el usuario
  confirme cuota real por usuario, limite por archivo, retencion al terminar la
  carrera, bloqueo MDM del OAuth de AutoSync y aceptabilidad del material con
  copyright en una cuenta institucional.
- No commiteo `Contenido Extra/01 - Dashboard/Operativo Diario/Notas de hoy.md`
  (del usuario) ni `Recursos adicionales/` (scratch): quedan en la cola de push.
- No hago el push: el turno es de `opencode-onedrive` (que ya lo anuncio). Mi commit
  entra en ese mismo push.

### Verificacion

Mi delta es solo `Clippings/**` (docs con `dg-publish: false`); el sync solo recorre
`Universidad/`, asi que **no necesita build**. El estado integrado ya lo verifico
`opencode-onedrive`: sync 806 publicadas / 3 omitidas / 17 patrones, build 833 paginas.

---
**Tags:** #clippings #log #opencode-nube #onedrive
