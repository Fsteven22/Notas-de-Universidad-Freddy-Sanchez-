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
`opencode-onedrive`: sync 806/3, build 833 paginas.

---

## Cierre real de la sesion (27/10/2026 ~15:05)

### Que hice

1. **Commitee mis 2 archivos + mis bloques del LEEME** en `47614c0` (rutas exactas, sin
   `git add -A`), con los archivos del usuario (`Notas de hoy.md`) y el scratch
   (`Recursos adicionales/`) **sin tocar**. El commit quedo dentro de `origin/master`.
2. **Verifique el estado integrado con build**, como pide el protocolo (el push arrastraba
   el merge `ddd27a7`, que trae cambios de `site/`).
3. **Corregi el acuerdo en dos puntos**: (a) AutoSync/OneSync son clientes del
   telefono, no del escritorio; (b) numeros exactos de lo liberable y criterio de
   reevaluacion (`Universidad/` > 3 GB).
4. **Deje el veredicto y la peticion de aprobacion al usuario** en el LEEME.

### Lo que me encontre al verificar (3a reproduccion del problema de OneDrive)

1. `npm run build` en el clon OneDrive fallo con
   `Cannot find module ...\node_modules\astro\dist\cli\throw-and-exit.js`: la carpeta
   **no existia** (OneDrive la deshidrató).
2. `npm ci` fallo con `ENOTEMPTY ... rmdir node_modules\hastscript\lib`: OneDrive y npm
   peleando por el mismo directorio.
3. **Build de control fuera de OneDrive**: copie el codigo a
   `C:\Users\STEVEN~1\AppData\Local\Temp\opencode\verify\site` con un **junction** al
   vault (`verify\Universidad` -> `OneSyncFiles\Universidad`), corri `npm ci` ->
   `npm run sync` (**806 notas, 5 bloques**) -> `npm run build` (**833 `.html`, exit 0**,
   sin errores). `speaking-practice-2` publicado y `favicon.ico` presente.
   Es el mismo metodo que usaron `opencode-onedrive` y `opencode-site` (worktree local).

> **Conclusion tecnica:** el codigo del sitio y su `node_modules` se compilan **fuera** de
> la carpeta sincronizada. El vault de OneDrive guarda notas y assets.

### Dato de cuota

La raiz de OneDrive paso de **4,99 GB a 5,13 GB** (de 5 GB): el `npm ci` a medias
escribio dentro de la carpeta sincronizada y **`site/` subio de 1,83 a 1,88 GB**.
La cuenta esta **pasada de cuota**, y cuando eso pasa OneDrive deja de subir y da
error. Por eso la limpieza de lo generado (~1,8 GB) ya no es opcional: **pide el
"dale" del usuario**.

### Lo que sigue pendiente del usuario

| # | Decision |
|---|---|
| 1 | Autorizar la limpieza de cuota ya (la cuenta esta pasada) |
| 2 | Cuota real por usuario de la institucional |
| 3 | Limite por archivo |
| 4 | Retencion al terminar la carrera |
| 5 | Aceptabilidad del material con copyright en una cuenta institucional |
| 6 | Telefono: AutoSync a la institucional (`DCIM/Camera`) o a la personal si la institucional bloquea el OAuth (MDM) |

### Estado al cierre

- `origin/master` = `2ea2d3d`; mi commit `47614c0` dentro; **commits sin pushear: ninguno**.
- Turno de push libre (anuncio `PUSHEADO 3cb1fdc` de la sesion del 3er Semestre).
- La PISTA queda **#procesado**: el veredicto esta en el LEEME (Acuerdo 4). No se mueve
  ninguna carpeta sin confirmacion del usuario.
- `.git/gc.pid` sigue roto: `git gc` no corre hasta borrarlo. **No lo borro sin aviso.**

---

## Radar de las 4 sesiones: resultados y próximos pasos (27/10/2026 ~15:25)

> [!note] 📌 Dónde vive el radar
> Otra sesión creó el **tablero canónico**: `Clippings/ESTADO - las 4 sesiones.md`, con un
> bloque por sesión (**Resultados / Qué falta / Próximos pasos**) y la lista de decisiones
> que esperan al usuario. Yo solo mantengo **mi bloque** (sección `3) opencode-nube`) y no
> toco el de los demás. Saqué del LEEME el radar que había escrito ahí para no dejar dos
> versiones del mismo tablero; el LEEME ahora apunta al tablero.

### Lo que aporté en esta tanda

1. **Leí las 4 bitácoras** (`LOG-opencode.md`, `LOG-opencode-onedrive.md`,
   `LOG-opencode-site.md`, `LOG-opencode-nube.md`) y el LEEME, y actualicé **mi bloque**
   en el tablero con los resultados verificados y los próximos pasos.
2. **Saqué del LEEME** el radar duplicado y lo dejé apuntando al tablero.
3. **Comprobé que lo que dice el tablero es cierto** contra el repo: `origin/master` =
   `bb1bc19`, los dos clones en 0/0, working tree limpio, `Universidad/` 1,11 GB,
   `site/` 1 MB, `.git/` 658 MB, raíz de OneDrive 2,39 GB de 5 GB.

### Resumen de lo que le falta a cada una (para contexto, el detalle está en el tablero)

| Sesión | Qué le falta (resumen) | Dueño |
|---|---|---|
| `opencode` (3er Sem.) | embebir PNG ya renderizados; renderizar DSW U3/U4/U5-01 y BD; normalizar ~970 errores de formato; los **1039 BAD** (decidir) | sesión + usuario |
| `opencode-onedrive` | P8 (`verificar_nota.py` de Cálculo Vectorial, pide luz verde) · P4 (4 scripts de auditoría en `Herramientas/Mantenimiento/`) · P3 (CI que falle si un asset excluido llega a `public/` o a un ZIP) · P2 (lista blanca de copyright, decide el usuario) · P6 (`VAULT_ROOT`, solo si se migra) · P1/P7 | sesión + usuario |
| `opencode-site` (Desktop) | paso manual en el panel de Vercel (usuario; el CLI no tiene token válido) · verificar favicon/redirect/aviso en producción · refrescar el espejo `notas-nexus` ("baseline 798") · confirmar la lista final de 3 notas omitidas | usuario + sesión |
| `opencode-nube` (esta) | nada propio: la PISTA quedó `#procesado` y el veredicto es "no migrar". 3 acciones reversibles del usuario (papelera, backup de 458 MB, fijar el vault) + 5 datos de la cuenta institucional | usuario |

### Lo que queda para el usuario (los agentes no lo resuelven)

1. **Vaciar la papelera de OneDrive** — los ~2,67 GB borrados siguen contando hasta hacerlo.
2. **Mover el backup de 458 MB** (`OneSyncFiles-backups/notas-20261024`) a disco local.
3. **Fijar el vault** ("mantener siempre en este equipo") para que OneDrive no lo deshidrate.
4. **Paso de panel de Vercel** para el dominio duplicado.
5. **Datos de la cuenta institucional**: cuota por usuario, límite por archivo, retención al
   terminar la carrera, aceptabilidad del material con copyright.
6. **Teléfono**: AutoSync → institucional con `DCIM/Camera` (plan B: app oficial de OneDrive
   para Android si el MDM bloquea el OAuth). **El vault no se empareja al teléfono.**
7. **Decisiones de contenido**: los 1039 BAD, las 3 notas omitidas, los 32 PNG huérfanos,
   `Recursos adicionales/Speaking Practice.md`.

### Estado al cierre de esta tanda

- `origin/master` = `bb1bc19`; los dos clones en **0/0**; working tree limpio salvo mis 3
  archivos (`LEEME`, este log y el tablero).
- **Commits sin pushear (míos):** el de esta tanda (tablero + mi log + el puntero del LEEME).
- **Siguiente paso mío:** ninguno hasta que el usuario responda los 7 puntos de arriba.

---
**Tags:** #clippings #log #opencode-nube #onedrive

