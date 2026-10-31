---
dg-publish: false
tags: [clippings, log, opencode-nube, onedrive, infraestructura]
---

# LOG - opencode-nube (sesion 2026-10-27)

> [!info] 📌 Alcance de esta sesión
> Sesion de **infraestructura / nube**. No es la sesion de los links rotos
> (`LOG-opencode.md`) ni la del sitio (`LOG-opencode-site.md`).
> **No toco `Universidad/**` ni `site/**`**: solo escribo en `Clippings/`.

> [!info] 📑 Índice
>
> - [[#Que hice]]
> - [[#Motivo]]
> - [[#Hallazgos (medidos, no re-medir)]]
> - [[#Rutas que reservo]]
> - [[#No toco sin avisar]]
> - [[#Cierre de la sesion — acuerdo de las 4 sesiones (27/10/2026)]]
> - [[#Cierre real de la sesion (27/10/2026 ~15:05)]]
> - [[#Radar de las 4 sesiones: resultados y próximos pasos (27/10/2026 ~15:25)]]
> - [[#Que leo del LEEME y con que estoy de acuerdo]]
> - [[#Correccion que aporto (un error de hecho en el acuerdo)]]
> - [[#Numeros (medidos 27/10/2026)]]
> - [[#Que NO hago]]
> - [[#Verificacion]]
> - [[#Qué hice en esta tanda (cierre real)]]
> - [[#Lo que me encontre al verificar (3a reproduccion del problema de OneDrive)]]
> - [[#Dato de cuota]]
> - [[#Lo que sigue pendiente del usuario]]
> - [[#Estado al cierre]]
> - [[#Lo que aporté en esta tanda]]
> - [[#Resumen de lo que le falta a cada una (para contexto, el detalle está en el tablero)]]
> - [[#Lo que queda para el usuario (los agentes no lo resuelven)]]
> - [[#Estado al cierre de esta tanda]]
> - [[#Tanda 27/10/2026 16:45–17:10 — migración a la cuenta institucional (1 TB)]]
> - [[#Tanda 27/10/2026 17:20–18:25 — migración probada y cancelada]]
> - [[#Tanda 27/10–28/10 00:30 — limpieza final de la nube y los 4 mecanismos de OneDrive]]
> - [[#Tanda 28/10/2026 00:40–01:10 — borrado del `.git` huérfano de la raíz de OneDrive (con respaldo)]]
> - [[#Tanda 28/10/2026 01:20-01:35 - la ultima pasada: plan de carriles publicado]]
> - [[#Tanda 28/10/2026 02:30-02:45 - correcciones del usuario (5 correcciones aplicadas)]]

## Que hice

> [!success] ✅ Qué hice
>
> - Deje la pista `Clippings/PISTA - migracion vault a OneDrive institucional.md`.
> - Anadi el aviso de esta sesion al final de `Clippings/00 - LEEME bandeja de pistas.md`.
> - **Commits:** ninguno. No se commitea nada hasta que el usuario decida la migracion.

## Motivo

> [!warning] ⚠️ Motivo: la cuenta personal está al límite
>
> La cuenta **personal** de OneDrive esta al limite: **4,99 GB de 5 GB** en
> `C:\Users\Steven Sànchez\OneDrive`. El plan del usuario es pasar el vault a la
> **cuenta institucional (1 TB)** y, en el **telefono**, cambiar **OneSync (Samsung)
> por AutoSync** apuntando a esa misma cuenta institucional.

> [!important] 🔎 Aclaración de alcance (corrige la primera versión)
>
> **Aclaracion de alcance (corrige la primera version de la pista):** AutoSync y OneSync
> son **clientes de sincronizacion del telefono**, no del escritorio. La PC usa el cliente
> de escritorio de OneDrive sobre `C:\Users\Steven Sànchez\OneDrive\OneSyncFiles`.
> Consecuencia: cambiar el telefono a la institucional solo sirve si **la PC tambien pasa
> a la institucional**; si no, el telefono ve otra copia del vault (son dos cuentas
> distintas, no "la misma carpeta con mas espacio").

## Hallazgos (medidos, no re-medir)

> [!info] 📁 Qué sirve en la nube y qué no
>
> | Carpeta | Tamano | Sirve en la nube? |
> |---|---:|---|
> | `Universidad/` | 1,11 GB | Si: es el contenido real (notas + PDF + 1 `.wmv` de 58 MB) |
> | `site/` | 1,83 GB | **No**: `node_modules` 211 MB, `dist` 874 MB, `public/assets` 649 MB, `public/downloads` 74 MB. Todo regenerable y todo en `.gitignore` |
> | `.git/` | 1,50 GB | **No**: ya espejado en GitHub. Un solo pack de 546 MB |
> | `.obsidian/` | 167 MB | **No**: ignorado por git, se regenera |
> | `OneSyncFiles-backups/` | 0,45 GB | Opcional |
> | **Total OneDrive root** | **4,99 GB / 5 GB** | Cuota personal agotada |

> [!info] 📊 Hallazgos medidos
>
> 1. **El deploy no depende de la nube local.** `site/vercel.json:4` corre
> `VAULT_DIR=../Universidad npm run sync && npm run build` dentro del repo en GitHub.
> Cambiar de cuenta de OneDrive no toca Vercel, ni `dg-publish`, ni `_no-publicar.txt`.
> 2. **`site/` no deberia vivir en el vault** y ya lo dice el RUNBOOK
> (`site/RUNBOOK.md:58`). Sacarlo libera 1,83 GB de cuota **sin migrar nada**.
> 3. **`.git` pesa 1,50 GB** y existe un `.git/gc.pid`: hay un `git gc` interrumpido.
> El remoto ya tiene los binarios.
> 4. **Estado git al dejar la pista** (rama `master`): 17 commits adelante de
> `origin/master` y 3 atras; 60 entradas sin commitear. Antes de mover carpetas:
> commitear o pushear.
> 5. **Rutas absolutas a `C:\Users\Steven Sànchez\OneDrive\OneSyncFiles`** que se
> rompen si el vault cambia de carpeta (la cuenta institucional se monta en
> `OneDrive - <Organizacion>`, no en `...\OneDrive`):
> - `site/scripts/sync-vault.mjs:19-20` (fallback por defecto)
> - `Universidad/Herramientas/SVG-Pipeline/`: `vlib.py:4`, `test_single.py:8`,
> `buildcv_missing.py:5`, `buildcv_auto.py:5`, `buildcv_lote2.py:86`,
> `buildcv_lote3.py:228`, `buildcv_lote4.py:553`, `buildcv_nabla.py:205`,
> `descargar-material-ccpg1001.py:23,25`
> - `Universidad/Herramientas/`: `estilo.py:41`, `auditoria.py:22`, `detectar_vacios.py:22`
> - `Universidad/Herramientas/README.md:25`, `Universidad/Herramientas/Scripts/LEEME-SCRIPTS.md:75-76`,
> `Universidad/Herramientas/Scripts/GUIA-PDF-A-MARKDOWN.md:64`
> 6. **Riesgo con AutoSync**: OneDrive (Files On-Demand) + AutoSync + git sobre los mismos
> archivos = placeholders a medio hidratar, duplicados `(conflicto)` en Obsidian y
> corrupcion de `.git`. `.git/`, `node_modules/`, `dist/` y `.obsidian/` no deben pasar
> por una tercera capa de sync.
> 7. **A verificar antes de migrar** (no comprobado): cuota real por usuario de la
> institucional, limite de tamano por archivo, retencion al terminar la carrera, y si el
> material de catedra con copyright (libros Cambridge, PDFs `z-lib.org`) es aceptable
> en una cuenta institucional.
> 8. **Telefono**: la institucional suele aplicar acceso condicional/MDM y puede bloquear
> el OAuth de una app de terceros como AutoSync. Plan B: app oficial de OneDrive para
> Android con la cuenta institucional, o pedir la app en el catalogo del tenant.
> Ademas, el vault no se debe emparejar completo al telefono (1,1 GB de PDFs + `.git`
> de 1,50 GB): emparejar `DCIM/Camera` y `Documentos`, y el vault solo en modo
> descarga. Al apagar OneSync, Samsung Gallery deja de subir fotos a la personal.

## Rutas que reservo

> [!tip] 🗂️ Rutas que reservo
>
> - `Clippings/PISTA - migracion vault a OneDrive institucional.md`
> - `Clippings/LOG-opencode-nube.md`
> - El bloque "opencode-nube" al final de `Clippings/00 - LEEME bandeja de pistas.md`

## No toco sin avisar

> [!warning] ⚠️ No toco sin avisar
>
> - `Universidad/3er Semestre/**` (links) y `Universidad/Herramientas/Mantenimiento/**`
> (reservados por `LOG-opencode.md`).
> - `Universidad/2do Semestre/Cálculo Vectorial/**`, `site/scripts/sync-vault.mjs`,
> `site/RUNBOOK.md`, `site/docs/HISTORIAL-LANZAMIENTO.md`,
> `Universidad/Herramientas/SVGs por recrear.md` (reservados por la sesion OneDrive).
> - `site/src/styles/*`, `site/src/components/SearchModal.astro`, `site/src/pages/index.astro`,
> `site/src/layouts/Base.astro`, `site/public/*` (reservados por `LOG-opencode-site.md`).

## Cierre de la sesion — acuerdo de las 4 sesiones (27/10/2026)

### Que leo del LEEME y con que estoy de acuerdo

> [!success] ✅ Lo que leo del LEEME y con qué estoy de acuerdo
>
> 1. **Protocolo de commits y pushes** (`edd511b`, reinstallado por `opencode-onedrive`):
> stagear rutas exactas, nunca `git add -A`; `git fetch` -> ver `origin/master..HEAD` y
> `HEAD..origin/master`; `git pull --no-rebase` y resolver **conservando las dos
> versiones** del LEEME; nunca `push --force`, nunca `amend` de algo pusheado; un solo
> push a la vez y el turno se anuncia en "Avisos de otros agentes".
> 2. **Cola de push** con dueño por cada pendiente. Mi parte (item 3) era commitear
> `Clippings/LOG-opencode-nube.md` + `Clippings/PISTA - migracion vault a OneDrive
> institucional.md` **desde esta sesion**, que es lo que hice.
> 3. **Zonas reservadas**: la tabla atribuia a `opencode-onedrive` la zona de
> `3er Semestre`, que es de la sesion `opencode`. Ya corregido en el LEEME; hay
> **4 sesiones**, no 3.
> 4. **Acuerdo de migracion**: de acuerdo en **no migrar ahora**.

### Correccion que aporto (un error de hecho en el acuerdo)

> [!warning] ⚠️ Corrección: un error de hecho en el acuerdo
>
> El punto 4 del plan de migracion decia *"AutoSync: no"*, tratando a AutoSync como
> un cliente de sincronizacion de **escritorio**. **AutoSync y OneSync son clientes de
> sincronizacion del TELEFONO** (OneSync = la integracion de OneDrive de Samsung;
> AutoSync = app de Android). La PC usa el cliente de OneDrive de Windows. El plan
> correcto:

> [!tip] 📱 Lo correcto para el teléfono
>
> - **AutoSync -> cuenta institucional**, emparejando **solo `DCIM/Camera`** (2 vias).
> Eso es lo que sigue llenando la cuenta personal con fotos.
> - **El vault NO se empareja al telefono**: 1,1 GB de PDFs + `.git` de 1,50 GB.
> - Si el vault llegara a migrarse, telefono y PC deben apuntar a la **misma** cuenta,
> o el telefono ve otra copia (dos cuentas distintas, no "la misma carpeta con mas
> espacio").

### Numeros (medidos 27/10/2026)

> [!info] 📊 Qué se puede liberar sin migrar
>
> | Carpeta | Peso | Liberable sin migrar |
> |---|---:|---|
> | `Universidad/` | 1,11 GB | no (contenido real) |
> | `site/` (ignorado por git) | 1,83 GB | si: borrar `node_modules`, `dist`, `.astro`, `notes-md`, `public/assets`, `public/downloads`, `public/pdfjs/{build,web}`; se regenera con `npm ci && npm run sync && npm run build`. Los 28 archivos versionados de `site/` se quedan |
> | `.git/` | 1,50 GB | si: `git gc --aggressive --prune=now` (hay un `gc.pid` de un gc interrumpido) |
> | `.obsidian/` | 167 MB | si: git-ignored, se regenera |
> | `OneSyncFiles-backups/` | 0,45 GB | opcional: mover a la institucional o borrar |
> | **Total** | **4,99 GB / 5 GB** | **~3,9 GB liberables -> la personal queda en ~1,1 GB** |

> [!question] ❓ Criterio de reevaluación
>
> Criterio de reevaluacion: migrar solo si `Universidad/` supera **3 GB** por si solo.

### Que NO hago

> [!warning] ⚠️ Lo que NO hago
>
> - No muevo ninguna carpeta: la PISTA queda en `#pendiente` hasta que el usuario
> confirme cuota real por usuario, limite por archivo, retencion al terminar la
> carrera, bloqueo MDM del OAuth de AutoSync y aceptabilidad del material con
> copyright en una cuenta institucional.
> - No commiteo `Contenido Extra/01 - Dashboard/Operativo Diario/Notas de hoy.md`
> (del usuario) ni `Recursos adicionales/` (scratch): quedan en la cola de push.
> - No hago el push: el turno es de `opencode-onedrive` (que ya lo anuncio). Mi commit
> entra en ese mismo push.

### Verificacion

> [!info] 📦 Mi delta
>
> Mi delta es solo `Clippings/**` (docs con `dg-publish: false`); el sync solo recorre
> `Universidad/`, asi que **no necesita build**. El estado integrado ya lo verifico
> `opencode-onedrive`: sync 806/3, build 833 paginas.

---

## Cierre real de la sesion (27/10/2026 ~15:05)

### Qué hice en esta tanda (cierre real)

> [!success] ✅ Qué hice (cierre real de la sesión)
>
> 1. **Commitee mis 2 archivos + mis bloques del LEEME** en `47614c0` (rutas exactas, sin
> `git add -A`), con los archivos del usuario (`Notas de hoy.md`) y el scratch
> (`Recursos adicionales/`) **sin tocar**. El commit quedo dentro de `origin/master`.
> 2. **Verifique el estado integrado con build**, como pide el protocolo (el push arrastraba
> el merge `ddd27a7`, que trae cambios de `site/`).
> 3. **Corregi el acuerdo en dos puntos**: (a) AutoSync/OneSync son clientes del
> telefono, no del escritorio; (b) numeros exactos de lo liberable y criterio de
> reevaluacion (`Universidad/` > 3 GB).
> 4. **Deje el veredicto y la peticion de aprobacion al usuario** en el LEEME.

### Lo que me encontre al verificar (3a reproduccion del problema de OneDrive)

> [!example] 💻 Lo que me encontré al verificar
>
> 1. `npm run build` en el clon OneDrive fallo con
> `Cannot find module ...\node_modules\astro\dist\cli\throw-and-exit.js`: la carpeta
> **no existia** (OneDrive la deshidrató).
> 2. `npm ci` fallo con `ENOTEMPTY ... rmdir node_modules\hastscript\lib`: OneDrive y npm
> peleando por el mismo directorio.
> 3. **Build de control fuera de OneDrive**: copie el codigo a
> `C:\Users\STEVEN~1\AppData\Local\Temp\opencode\verify\site` con un **junction** al
> vault (`verify\Universidad` -> `OneSyncFiles\Universidad`), corri `npm ci` ->
> `npm run sync` (**806 notas, 5 bloques**) -> `npm run build` (**833 `.html`, exit 0**,
> sin errores). `speaking-practice-2` publicado y `favicon.ico` presente.
> Es el mismo metodo que usaron `opencode-onedrive` y `opencode-site` (worktree local).

> [!success] Conclusión técnica
> **Conclusion tecnica:** el codigo del sitio y su `node_modules` se compilan **fuera** de
> la carpeta sincronizada. El vault de OneDrive guarda notas y assets.

### Dato de cuota

> [!warning] ⚠️ Dato de cuota
>
> La raiz de OneDrive paso de **4,99 GB a 5,13 GB** (de 5 GB): el `npm ci` a medias
> escribio dentro de la carpeta sincronizada y **`site/` subio de 1,83 a 1,88 GB**.
> La cuenta esta **pasada de cuota**, y cuando eso pasa OneDrive deja de subir y da
> error. Por eso la limpieza de lo generado (~1,8 GB) ya no es opcional: **pide el
> "dale" del usuario**.

### Lo que sigue pendiente del usuario

> [!question] ❓ Decisiones pendientes del usuario
>
> | # | Decision |
> |---|---|
> | 1 | Autorizar la limpieza de cuota ya (la cuenta esta pasada) |
> | 2 | Cuota real por usuario de la institucional |
> | 3 | Limite por archivo |
> | 4 | Retencion al terminar la carrera |
> | 5 | Aceptabilidad del material con copyright en una cuenta institucional |
> | 6 | Telefono: AutoSync a la institucional (`DCIM/Camera`) o a la personal si la institucional bloquea el OAuth (MDM) |

### Estado al cierre

> [!success] ✅ Estado al cierre
>
> - `origin/master` = `2ea2d3d`; mi commit `47614c0` dentro; **commits sin pushear: ninguno**.
> - Turno de push libre (anuncio `PUSHEADO 3cb1fdc` de la sesion del 3er Semestre).
> - La PISTA queda **#procesado**: el veredicto esta en el LEEME (Acuerdo 4). No se mueve
> ninguna carpeta sin confirmacion del usuario.
> - `.git/gc.pid` sigue roto: `git gc` no corre hasta borrarlo. **No lo borro sin aviso.**

---

## Radar de las 4 sesiones: resultados y próximos pasos (27/10/2026 ~15:25)

> [!note] 📌 Dónde vive el radar
> Otra sesión creó el **tablero canónico**: `Clippings/ESTADO - las 4 sesiones.md`, con un
> bloque por sesión (**Resultados / Qué falta / Próximos pasos**) y la lista de decisiones
> que esperan al usuario. Yo solo mantengo **mi bloque** (sección `3) opencode-nube`) y no
> toco el de los demás. Saqué del LEEME el radar que había escrito ahí para no dejar dos
> versiones del mismo tablero; el LEEME ahora apunta al tablero.

### Lo que aporté en esta tanda

> [!success] ✅ Lo que aporté en esta tanda
>
> 1. **Leí las 4 bitácoras** (`LOG-opencode.md`, `LOG-opencode-onedrive.md`,
> `LOG-opencode-site.md`, `LOG-opencode-nube.md`) y el LEEME, y actualicé **mi bloque**
> en el tablero con los resultados verificados y los próximos pasos.
> 2. **Saqué del LEEME** el radar duplicado y lo dejé apuntando al tablero.
> 3. **Comprobé que lo que dice el tablero es cierto** contra el repo: `origin/master` =
> `bb1bc19`, los dos clones en 0/0, working tree limpio, `Universidad/` 1,11 GB,
> `site/` 1 MB, `.git/` 658 MB, raíz de OneDrive 2,39 GB de 5 GB.

### Resumen de lo que le falta a cada una (para contexto, el detalle está en el tablero)

> [!warning] ⏳ Resumen: qué le falta a cada sesión
>
> | Sesión | Qué le falta (resumen) | Dueño |
> |---|---|---|
> | `opencode` (3er Sem.) | embebir PNG ya renderizados; renderizar DSW U3/U4/U5-01 y BD; normalizar ~970 errores de formato; los **1039 BAD** (decidir) | sesión + usuario |
> | `opencode-onedrive` | P8 (`verificar_nota.py` de Cálculo Vectorial, pide luz verde) · P4 (4 scripts de auditoría en `Herramientas/Mantenimiento/`) · P3 (CI que falle si un asset excluido llega a `public/` o a un ZIP) · P2 (lista blanca de copyright, decide el usuario) · P6 (`VAULT_ROOT`, solo si se migra) · P1/P7 | sesión + usuario |
> | `opencode-site` (Desktop) | paso manual en el panel de Vercel (usuario; el CLI no tiene token válido) · verificar favicon/redirect/aviso en producción · refrescar el espejo `notas-nexus` ("baseline 798") · confirmar la lista final de 3 notas omitidas | usuario + sesión |
> | `opencode-nube` (esta) | nada propio: la PISTA quedó `#procesado` y el veredicto es "no migrar". 3 acciones reversibles del usuario (papelera, backup de 458 MB, fijar el vault) + 5 datos de la cuenta institucional | usuario |

### Lo que queda para el usuario (los agentes no lo resuelven)

> [!question] ❓ Lo que queda para el usuario
>
> 1. **Vaciar la papelera de OneDrive** — los ~2,67 GB borrados siguen contando hasta hacerlo.
> 2. **Mover el backup de 458 MB** (`OneSyncFiles-backups/notas-20261024`) a disco local.
> 3. **Fijar el vault** ("mantener siempre en este equipo") para que OneDrive no lo deshidrate.
> 4. **Paso de panel de Vercel** para el dominio duplicado.
> 5. **Datos de la cuenta institucional**: cuota por usuario, límite por archivo, retención al
> terminar la carrera, aceptabilidad del material con copyright.
> 6. **Teléfono**: AutoSync → institucional con `DCIM/Camera` (plan B: app oficial de OneDrive
> para Android si el MDM bloquea el OAuth). **El vault no se empareja al teléfono.**
> 7. **Decisiones de contenido**: los 1039 BAD, las 3 notas omitidas, los 32 PNG huérfanos,
> `Recursos adicionales/Speaking Practice.md`.

### Estado al cierre de esta tanda

> [!success] ✅ Estado al cierre de esta tanda
>
> - `origin/master` = `bb1bc19`; los dos clones en **0/0**; working tree limpio salvo mis 3
> archivos (`LEEME`, este log y el tablero).
> - **Commits sin pushear (míos):** el de esta tanda (tablero + mi log + el puntero del LEEME).
> - **Siguiente paso mío:** ninguno hasta que el usuario responda los 7 puntos de arriba.

### Tanda 27/10/2026 16:45–17:10 — migración a la cuenta institucional (1 TB)

> [!info] 📌 Qué cambió (16:45)
>
> **Qué cambió:** el usuario decidió migrar (la institucional da 1 TB gratis y la personal
> está topada). El veredicto anterior de las 4 sesiones ("no migrar") queda **superado**;
> la verdad del trabajo sigue siendo **GitHub** y el vault personal **no se movió ni se borró**.

> [!warning] ⚠️ Diagnóstico: el login entra pero OneDrive no abre
>
> **Diagnóstico del "el login entra pero OneDrive no abre":** la PC arrastraba un registro
> huérfano `HKCU\Software\Microsoft\OneDrive\Accounts\Business1` de enero 2026 (sin
> `UserFolder`, ECS expirado 07/01/2026) → el login de Microsoft pasaba, pero el cliente no
> tenía ninguna unidad que abrir. Con `fredsanc@espol.edu.ec` dada de alta: `UserFolder`
> correcto, `LastSignInResult=0`, `HasMadeFirstUpload=1`.

> [!warning] ⚠️ Diagnóstico: por qué la cuota no bajaba
>
> **Diagnóstico de por qué la cuota no bajaba:** vaciar la papelera no era suficiente. La
> personal sigue con muro de cuota (`QuotaWallTimestamp` = 27/10 13:43) por dos causas: el
> **historial de versiones** (30 días en cuenta personal) conserva lo borrado, y en la nube
> siguen **duplicados que git no versiona** (`site/public/assets/` 664 MB,
> `.obsidian/plugins/` 162 MB, `.git/` huérfano 23 MB en la raíz de OneDrive).
> `.gitignore` solo aplica a git: OneDrive sube esas carpetas igual.

> [!success] ✅ Copia verificada
>
> **Copia verificada:** `robocopy` a
> `C:\Users\Steven Sànchez\OneDrive - Escuela Superior Politécnica del Litoral\OneSyncFiles`
> (excluyendo `site/public/assets`, `site/notes-md`, `site/dist`, `site/.astro`,
> `site/node_modules`, `.obsidian`, `.trash`): **4.687 archivos · 1,729 GB · 0 errores**.
> Integridad: HEAD idéntico (`fec4b97`), **índice de git con SHA-256 idéntico** (4.533
> archivos trackeados con los mismos blob-sha), `git fsck` sin errores, **4.687/4.687
> archivos en la nube** en ~3 min, carpeta renombrada de `-migracion` a `OneSyncFiles`.
> La diferencia de 13 `.md` quedó explicada (12 `README.md` de plugins en `.obsidian` + 1 de
> `.trash`, ambos excluidos a propósito).

> [!important] 🔒 Regla de las dos copias
>
> **Regla de las dos copias:** GitHub es la verdad. Personal = vault de trabajo de las 4
> sesiones. Institucional = espejo en la nube de 1 TB + acceso del teléfono. Si el
> institucional queda activo: `git pull --no-rebase` en esa copia tras cada push (la
> personal no sube por cuota).

### Tanda 27/10/2026 17:20–18:25 — migración probada y cancelada

> [!info] 📌 Secuencia (17:20–18:25)
>
> **Secuencia:** el usuario decidió migrar (16:45) → se dio de alta la institucional
> (`fredsanc@espol.edu.ec`), se verificó la subida con un archivo de prueba y se copió el
> vault (**4.687 archivos · 1,729 GB · 0 errores**, con **índice de git de SHA-256 idéntico**
> al personal) → se probó en el teléfono → **el usuario canceló (18:20)** porque el MDM de
> ESPOL no deja emparejar carpetas y la app oficial de OneDrive para Android solo crea
> carpetas en la nube: **no hay forma de tener Obsidian local en el teléfono sin Obsidian
> Sync (de pago)**. Para leer, el sitio publicado ya cubre.

> [!warning] ⚠️ Borrado de la copia institucional
>
> **Borrado de la copia institucional:** `rd /s /q` normal falló en 35 archivos con
> *"El sistema no puede encontrar la ruta especificada"* → **límite de 260 caracteres de
> ruta**. Repetido con el prefijo `\\?\` → **0 archivos restantes**. La carpeta `OneSyncFiles`
> ya no existe en la raíz institucional y el cliente propaga los borrados a la nube (papelera
> de 1 TB, sin efecto).

> [!success] ✅ Verificado tras el borrado
>
> **Verificado tras el borrado:** vault personal **intacto** (`973e791`, `## master...origin/master`,
> 0/0, 1.795 `.md`). No se perdió nada: lo borrado está en GitHub y en la personal.

> [!success] ✅ Efecto favorable: queda un solo clon
>
> **Efecto favorable:** queda **un solo clon** → los 12 archivos con ruta literal
> `OneDrive\OneSyncFiles` y el fallback de `site/scripts/sync-vault.mjs:20` vuelven a apuntar
> al vault real, y **P6 vuelve a ser "solo si algún día se decide migrar"**.

> [!important] 🔎 Lección de cuota (la real)
>
> **Lección de cuota (la real):** la personal no estaba topada por el contenido (2,4-2,6 GB
> libres tras la limpieza) sino por el **historial de versiones** (30 días) + **duplicados que
> git ignora pero OneDrive sube**: `site/public/assets/` 664 MB, `.obsidian/` 162 MB y un
> `.git/` huérfano de 23 MB en la raíz de OneDrive. Vaciar la papelera no arregla eso.

### Tanda 27/10–28/10 00:30 — limpieza final de la nube y los 4 mecanismos de OneDrive

> [!success] ✅ Hecho por el usuario: `site/public/assets` eliminado (650 MB)
> La raíz local de OneDrive bajó de **2.647 MB → 1.997 MB** (el vault quedó en **1.951 MB**).
> **No se rompió nada**, y está verificado por qué:
> - `site/public/assets/` es un **artefacto de build**, no fuente: lo escribe
> `site/scripts/sync-vault.mjs:23` (`OUT_ASSETS = path.join(PROJECT, "public", "assets")`),
> está en `site/.gitignore` (`public/assets/`) y **Vercel lo reconstruye en cada deploy**
> (`site/vercel.json`: `VAULT_DIR=../Universidad npm run sync && npm run build`).
> - Los **originales** viven en `Universidad/` (que sí está en git y en la nube).
> - El código que sí importa del sitio (`site/src/**`, íconos) son **MB, no GB**.
> - **Beneficio extra:** desaparece la **fuente de la fuga** — los 650 MB que volvían solos
> con cada build corrido *dentro* del clon sincronizado (rehidratación medida a las 15:31).
> - **Pendiente del usuario (1 clic):** vaciar la **papelera** en el web, o los 650 MB
> siguen contados como borrados (mismo mecanismo que la primera vez).

> [!warning] ⚠️ `.obsidian` (167 MB) se queda — y por qué
> Es la **casa de Obsidian**: plugins, temas y ajustes. Borrarlo de la nube **también lo
> borra en local** (es un archivo sincronizado) → tendrías que reinstalar todo. Si algún día
> quieres sacarlo de la nube **sin perderlo**, el mecanismo es **"Dejar de sincronizar"**
> (lo quita del drive y deja los archivos locales). Con la cuenta al 50% no compensa.

> [!info] 📐 Los 4 mecanismos de OneDrive (la confusión que ordenó esta tanda)
> | Acción | ¿Sale de la nube? | ¿Sale de la PC? | ¿Libera cuota de nube? |
> |---|---|---|---|
> | **Seleccionar carpetas** (sincronización selectiva) | No | **Sí** (se oculta del Explorador) | **No** (solo disco local) |
> | **Liberar espacio** | No | Sí | No |
> | **Dejar de sincronizar** | **Sí** | No (el archivo local se queda) | **Sí** |
> | **Moverlo fuera** de la carpeta de OneDrive | **Sí** (OneDrive lo ve como borrado) | Queda en el nuevo sitio | Sí (+ vaciar papelera) |
> | **Desvincular este equipo** | No | Sí (desconecta todo el drive de la PC) | No |
>
> **Clave conceptual:** si el archivo **sigue dentro** de `C:\Users\...\OneDrive\`, OneDrive lo
> está sincronizando. Para sacarlo de la nube hay que **moverlo fuera de la carpeta** o
> **borrarlo desde la nube**.

> [!success] ✅ La cuenta personal dejó de estar topada
> El cliente muestra **"2,5 GB usado de 5 GB (50%)"** y la clave `QuotaWallTimestamp` (la que
> marcaba el muro de cuota a las 13:43) **ya no está** en
> `HKCU\Software\Microsoft\OneDrive\Accounts\Personal`. **0 archivos pendientes de subida**
> (11.789 archivos, todos ya son ítems de nube). Lo que no bajaba en la barra del web era el
> **historial de versiones** (30 días en cuenta personal), que **decae solo** y no bloquea nada.

> [!note] 📌 Regla que queda vigente
> **Nunca compilar dentro de OneDrive.** El build va en disco local (worktree o copia
> temporal), como se verificó 3 veces. Y `.gitignore` **no aplica a OneDrive**: el cliente
> sube cualquier carpeta que esté dentro de la carpeta de OneDrive, ignorada o no.

### Tanda 28/10/2026 00:40–01:10 — borrado del `.git` huérfano de la raíz de OneDrive (con respaldo)

> [!info] 🔍 Qué era exactamente
> La raíz de OneDrive tenía una carpeta `.git` (23 MB) **sin archivos de trabajo**: era un
> **clon viejo del repo de notas** (21 commits en `main`) + **1 commit local único**
> `b2e96c6` *"Primer commit: Inicialización del proyecto Bingo SaaS"* (120 archivos,
> +89.937 líneas: el snapshot inicial del Bingo y la config de Obsidian de esa época).
> - **20 de los 21 commits ya están en GitHub** (historia de las notas, idénticos).
> - `b2e96c6` **NO está en ningún remoto**: GitHub `Mi-Bingo-App.git` tiene `main` = `6666195`
> y el clon de trabajo `Documents\Default Project` **no tiene ni un commit** → borrarlo a
> ciegas habría perdido ese commit.

> [!success] ✅ Respaldo antes de borrar
> Copia cruda de la carpeta `.git` (no un `git bundle`: se **atascó** reempaquetando los
> 1.259 objetos sueltos y pasó los 5 min de timeout) a
> **`C:\Users\Steven Sànchez\Documents\OneDrive-root-git-huerfano-20261028\`**
> → **23,0 MB · 1.286 archivos**, verificada: `main` en `b2e96c6`, el commit **colgante**
> `35c05b6` incluido, `git fsck` **sin errores**. Se recupera con `git clone <esa carpeta>`.

> [!success] ✅ Borrado y verificación
> `Remove-Item "\\?\...\OneDrive\.git" -Recurse -Force` → **OK a la primera** (a diferencia de
> la copia institucional, que dio 35 falsos errores de ruta). Raíz de OneDrive:
> **1.997 → 1.975 MB** (23 MB fuera de la nube).
> **Vault intacto**: `e72348e` = `origin/master` (0/0), `git fsck` sin errores, **1.795 `.md`**,
> sin muro de cuota (`QuotaWallTimestamp` ausente).

> [!note] 📌 Lo que queda en la raíz de OneDrive
> `OneSyncFiles/` (el vault) · `Steven Sánchez/` (**vacía**, 0 MB) · `desktop.ini` · un marcador
> de OneDrive de 0 bytes. Y lo único que **de verdad** hace bajar la cuota del web:
> **vaciar la papelera** (1 clic, pendiente del usuario).

### Tanda 28/10/2026 01:20-01:35 — la última pasada: plan de carriles publicado

> [!success] ✅ Qué hice
> El usuario pidió la **última pasada** a los `.md` de `Clippings/`: que los fixes e
> implementaciones pendientes **arranquen por separado**, un carril por sesión. Publiqué el
> **§0 "Plan de carriles"** en `ESTADO - las 4 sesiones.md` (la sección va **primero**, con su
> entrada en el índice, porque es la cola real que todos deben leer).
> **No toqué `Universidad/**` ni `site/**`, ni el bloque de ninguna otra sesión.**

> [!info] 🗺️ Los 4 carriles (con dueño, zona y salida verificable)
> | # | Carril | Dueño | Salida verificable |
> |---|---|---|---|
> | **A** | Scripts `.py` de mantenimiento | `opencode-onedrive` | `Mantenimiento/` documentado en `Herramientas/README.md` |
> | **B** | Figuras a la carpeta de su materia | `opencode` (3er Sem.) | 0 figuras sueltas + embeds OK |
> | **C** | Mermaid → SVG | `opencode-site` | los **19** SVG que faltan + lista maestra en 0 |
> | **D** | Material nuevo 3er Sem. | **D1** `opencode-nube` (intake/QA) + **D2** `opencode` (notas) | pista por lote → notas de la materia |

> [!success] 📏 Lo que medí para que nadie arranque a inventar
> - **A:** `Universidad/Herramientas/Mantenimiento/` ya tiene **15 `.py`** (`mdlib.py`,
>   `fix_callouts*.py`, `fix_links.py`, `qa_links*.py`, `qa_pdfs_*.py`, `qa_refs_checkbox.py`…).
>   Falta **P4** (mover 4 scripts de auditoría + documentarlos en `Herramientas/README.md`, que
>   ya existe) y **P8** (`verificar_nota.py` de Cálculo Vectorial).
> - **B:** `Universidad/Figuras/` tiene **122 archivos sueltos** (119 PNG + 2 SVG + 1 JPG) y es la
>   **única** carpeta `Figuras/` del vault; las **16 materias** ya tienen `Diagramas/`. Los embeds
>   `![[nombre.png]]` resuelven por nombre → mover no rompe nada; hay que arreglar los embeds con
>   ruta o markdown `![]()`.
> - **C:** `SVG-Pipeline/mmd2/` tiene **338 `.mmd` y 0 `.svg`**, pero **319 ya tienen su SVG** en
>   el vault → **solo faltan 19**. El convertidor ya existe (**13 `.py`**): no reescribirlo.
> - **D:** el gate de publicación es `dg-publish` y la lista de copyright `_no-publicar.txt`
>   (P2 sigue esperando al usuario).

> [!warning] 📐 Reglas que dejé escritas
> Un carril = un dueño = una zona = un commit · al cerrar: hash + `cerrado` + una línea en su
> bloque · **nunca `git add -A`** · un push a la vez anunciado · **nunca compilar dentro de
> OneDrive** · mientras el **LEEME** esté sin commitear (otra sesión lo edita), los anuncios de
> push van en el tablero.

### Tanda 28/10/2026 02:30-02:45 — correcciones del usuario (5 correcciones aplicadas)

> [!info] 📌 Lo que me corrigió el usuario
> 1. **Copyright**: *"ya había dicho que los ignoremos al subirlo a la web"* → **P2 cerrado**:
>    se mantiene la **lista negra** `_no-publicar.txt` (17 entradas). **No** hay lista blanca ni
>    carpeta `_privado/`. El carril A lo documenta; el D1 lo avisa por lote.
> 2. **Links rotos**: *"colocaselo a quien va a hacer los últimos svg de mermaid"* → los **1026**
>    pasan al **carril C** (`opencode-site`), con regla de zona: diagramas son suyos, notas de
>    otros carriles se coordinan.
> 3. **Dominio**: *"neonotes.vercel.app no es el dominio que está usando ahora la web, es
>    neonotes-espol.vercel.app"* → la web vive en `neonotes-espol.vercel.app`; `neonotes.vercel.app`
>    pertenece a **otro proyecto de Vercel** → **se cierra** el paso de panel.
> 4. **Teléfono**: *"no sé a qué te refieres"* → era el ítem de **AutoSync con la cuenta
>    institucional**, y la migración se canceló → **no aplica**. Para leer en el móvil: el sitio.
> 5. **Papelera**: *"ya la vacié hace mucho"* → **nada pendiente**.
> 6. **Material nuevo**: *"lo dejo exactamente en las carpetas unidad 0 guías y ejercicios de cada
>    materia"* → el carril D1 vigila las **5 rutas exactas** de 3er Sem. (ver §0 del tablero);
>    en Electricidad está dentro de `Teorico/`.

> [!success] ✅ Qué actualicé
> Tablero: §0 (carriles C y D), tabla de decisiones (5 resueltas + las que siguen), bloque global
> y mi §3 · LEEME: "Decisiones abiertas" + el aviso de push · mi bitácora. **Sin tocar** el
> bloque de ninguna otra sesión, ni `Universidad/**`, ni `site/**`.

### Tanda 28/10/2026 03:00-03:30 — links de contenido recomendado en los LEEME de 3er Sem.

> [!success] ✅ Qué hice (pedido del usuario, fuera de los carriles)
> En los **LEEME/Recursos de las guías y ejercicios** de 3er Sem. agregué la sección
> **`## 🔗 Links de contenido recomendado`** con **links reales de YouTube** para ver el
> contenido de forma visual y sonora, complementando la lectura.
> **Respondo la duda del usuario:** **sí puedo buscar en YouTube** — parseo la página de
> resultados y saco **videoId + título real + canal + duración**, así que **no se inventa ni un
> link**. (Script de apoyo, fuera del repo: `%TEMP%\opencode\yt_search.py`.)
> **56 links en 6 archivos**, uno por LEEME:
> | Materia | Archivo | Links | Qué cubren |
> |---|---|---:|---|
> | Diseño de Software | `Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md` | 10 | diagrama de clases, casos de uso, patrones, Clean Architecture, refactoring |
> | Electricidad (teórico) | `Teórico/Unidad 0 - Guías y Ejercicios/00 - Recursos Unidad 0.md` | 11 | diodos, análisis de nodos, Thévenin/Norton, op-amps, 555 biestable |
> | Electricidad (práctico) | `Practico/Fundamentos del Laboratorio/00 - Recursos del laboratorio.md` | 7 | osciloscopio, multímetro |
> | Inglés III | `Unidad 0 - Guias y Ejercicios/Recursos Unidad 0.md` | 8 | presente perfecto vs pasado simple, phrasal verbs, irregulares, speaking B2, presentaciones |
> | Matemáticas Discretas | `Unidad 0 - Guias y Ejercicios/00 - Recursos Unidad 0.md` | 13 | palomar, tablas de verdad, inducción, recurrencias, grafos, autómatas |
> | Bases de Datos | `Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md` | 7 | normalización, álgebra relacional, JOINs (el primero lo puso el usuario) |

> [!warning] 📐 Coordinación: el usuario editaba en paralelo
> Escribimos **los dos** al mismo tiempo: en **DSW** quedaron **dos** secciones de links (yo
> había creado el heading y él había pegado su lista) → **fusioné en una sola**, sin links
> repetidos (verificado: 1 heading y 0 IDs duplicados por archivo). En **FESD** y **BD** él ya
> había pegado su lista: **solo le añadí lo que faltaba** (los op-amps en FESD, que la guía
> `EjREsAmpOp.pdf` necesita; más links de normalización/álgebra en BD).
> **Zona:** toqué `Universidad/3er Semestre/**` (zona de `opencode`) **a pedido del usuario** y
> **solo en los 6 LEEME**; quedó anunciado en el tablero para que `opencode` lo revise.

> [!note] 📌 Lo que quedó sin stagear (cambio del usuario, no mío)
> El usuario movió `Database Systems… (9th Edition).pdf` de la raíz de BD a `Diapositivas/`.
> **Lo dejé sin stagear** para que lo commitee él. Ojo: ese libro está en
> `_no-publicar.txt` **por nombre**, así que sigue sin publicarse aunque cambie de carpeta.

### Tanda 29/10/2026 — normalización: Pasada 1 ENDINGS → LF (111 blobs)

> [!warning] 🚚 PUSHEO EN CURSO
> Medido en HEAD `df267dd`: **111** blobs con CRLF (55 mixed + 56 puro) de 831 `.md`. Backup
> byte-exacto ya hecho en `TEMP\opencode\backup_pasada1` (111 archivos + `_rutas.txt`).
> Cambio **solo fin de línea**; `git add` con rutas exactas; 1 commit; verificación del diff
> byte a byte; después `qa_links.py` (baseline 854 BADs, 0 regresiones) y `PUSHEADO <hash>`.
> Toca solo `Universidad/**` por mandato de `opencode` (replanteo del LEEME); `Clippings/`
> sigue siendo mi zona para los avisos.

> [!success] ✅ Cierre: `PUSHEADO a2be225`
> `d648726` (aviso) + `a2be225` (Pasada 1). **111 notas** (55 mixed + 56 puro de 831),
> `+91344/-91344`, dif **solo fin de línea** — `verificar_bytes.py`: 111 OK / 0 mal (blob
> stageado == blob HEAD con CRLF→LF, bit a bit). `qa_links` root=`Universidad`:
> **854 BADs = baseline, 0 regresiones**. Backup reversible en
> `TEMP\opencode\backup_pasada1` (111 archivos byte-exactos + `_rutas.txt`); basta
> `git revert a2be225`. **Pasada 3 sin objeto** (0 líneas, 5 definiciones probadas → así la
> reporto). Sigo con la **Pasada 2: 33 archivos** con líneas vacías en frontmatter.

> [!warning] 🚚 PUSHEO EN CURSO — Pasada 2 (16 archivos)
> **Corrección de cifra:** los "33" eran 18 archivos con finales `\r\r\n` (el CR suelto
> fijaba el renglón falso); el conjunto real de frontmatter vacío es **15**. Más
> **1 archivo residual** de CRCA de la Pasada 1 (`02 - Representación gráfica.md`).
> OneDrive devolvió CRLF al working tree de los 111 (git no lo marca; el sitio sí lee de
> disco) → avisado a `opencode-site`. **Commit pathspec-explícito**: hay renames de
> Cálculo Vectorial staged por otra sesión; no los capturo. Backup byte-exacto en

> [!success] ✅ Cierre: `PUSHEADO f430057` (Pasada 2 en `origin/master`)
> **Hallazgo operativo importante: OneDrive revierte en segundos los archivos sin commitear**
> (15 de los 16 escritos volvieron a su estado anterior entre el fix y el `git add`; el fix
> residual de CRCA, ya committeado local, fue absorbido por el `autostash` de un `git pull`
> ajeno). Solución aplicada: **escritura atómica** (escribir + `git add` + commit en el mismo
> ciclo por archivo).
> - **Push bloqueado en el árbol principal** (remoto adelantado con el ciclo de `opencode-site`
>   y archivos de otras sesiones staged). Mis 2 commits se subieron por un **worktree limpio**
>   con cherry-pick → `origin/master` = **`f430057`**: 15 notas, 25 líneas fuera (solo frontmatter).
> - El archivo residual CRCA (`02 - Representación gráfica`) **ya venía limpio en el remoto**
>   (CR=0, LF=167) → cherry-pick vacío, no se duplica.
> - **Verificación final sobre `origin/master`**: 0 blobs con CR y 0 notas con frontmatter vacío
>   en las 831 `.md` de `Universidad/`; `qa_links` (raíz `Universidad`) = **8112 targets / 852 bad**
>   (0 regresiones: mis commits solo borran líneas vacías y finales de línea, no tocan links).
> - **Pasada 3 = sin objeto** (0 líneas con 5 definiciones probadas) → así queda reportada.
> - **Pendiente para el árbol principal**: el `master` local quedó detrás y con archivos ajenos
>   staged; cuando la otra sesión cierre su ciclo, quien sincronice debe hacer `rebase`, no
>   merge en árbol sucio. El worktree `wt-merge` (2ad2612) es de otra sesión; no lo toco.
> `TEMP\opencode\backup_pasada2`.

---
**Tags:** #clippings #log #opencode-nube #onedrive

