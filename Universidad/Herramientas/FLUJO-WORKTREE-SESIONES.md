---
dg-publish: false
tags: [herramientas, git, coordinacion, flujo]
---

# Flujo de trabajo por sesión — worktree + reglas anti-mezcla

> [!info] 📌 Por qué existe este documento
> El clon compartido (`OneDrive\OneSyncFiles`) tuvo **3 incidentes de commits mezclados** (`b9de5b7`,
> `394a087`, `68cab8b`) porque las 4 sesiones comparten un único índice de git. El arreglo
> definitivo es **trabajar cada sesión en su propio worktree**. Post-mortem completo y plan de
> arreglo: `Clippings/PROBLEMA - commits mezclados por el indice compartido.md`.
>
> Dueño de este flujo: `opencode-onedrive` (carril A) · Zona: `Universidad/Herramientas/**`.

## 1. Setup (una vez por sesión)

```bash
git -C "C:/Users/Steven Sànchez/OneDrive/OneSyncFiles" fetch origin
git -C "C:/Users/Steven Sànchez/OneDrive/OneSyncFiles" \
    worktree add -b sesion/<nombre-sesion> <RUTA-FUERA-DE-ONEDRIVE> origin/master
```

- **`<RUTA-FUERA-DE-ONEDRIVE>` es obligatoria**: dentro de OneDrive, el cliente rehidrata CRLF y
  revierte archivos sin commitear (dos de las causas del post-mortem). Opciones validadas:
  `%LOCALAPPDATA%\Temp\opencode\wt-<sesion>` (prueba actual de `opencode-onedrive`) o una carpeta
  en el Desktop (`Desktop\wt-<sesion>`) como ruta permanente.
- Cada worktree tiene **su propio índice**: un commit jamás puede capturar trabajo de otra sesión.

## 2. Flujo diario (desde el worktree de tu sesión)

```bash
cd <tu-worktree>
git add -- <ruta-exacta-tuya>          # NUNCA git add -A ni commit -a
git diff --cached --stat               # REGLA C: confirmar que solo hay rutas propias
git commit -m "<mensaje>"              # escritura atomica: add + commit en el mismo ciclo
git show --stat HEAD                   # REGLA C: ultima verificacion antes del push
git push origin HEAD:master            # push directo a master (la rama local master del
                                       # clon compartido se sincroniza con el proximo pull)
```

**Avisos en el LEEME** (protocolo de las 4 sesiones, se mantiene igual):
1. `PUSHEO EN CURSO · master · <qué> · ~N min` — antes de pushear.
2. `PUSHEADO <hash>` — después, con `origin/master = master` y turno libre.

## 3. Reglas operativas (bloque B del post-mortem, vigentes ya)

1. `git add` **solo de rutas exactas propias** (zonas en `Clippings/00 - LEEME bandeja de pistas.md`).
2. `git diff --cached --stat` antes de cada commit: si aparece una ruta ajena,
   `git restore --staged <ruta>` (no toca el archivo en disco, solo el índice).
3. **Escritura atómica**: escribir + `git add` + commit en el mismo ciclo (OneDrive revierte en
   segundos lo que no está commiteado).
4. Si igual se mezcla: **nada de `--force` ni `amend` de lo publicado**; documentar la autoría en
   el LEEME (como en los 3 incidentes).
5. EOL: verificar el fin de línea del disco antes de `sync`/build, o compilar desde el clon
   Desktop; el pipeline ya normaliza al leer (`leerTexto()` en `site/scripts/sync-vault.mjs`).

## 4. Detección automática (regla C)

En el `.git` del clon compartido quedó instalado un hook local `pre-commit` que **avisa** (no
bloquea) listando lo que está staged antes de cada commit. Es local al clon (no se versiona), así
que cada clon/worktree lo hereda; para desactivarlo: borrar `.git/hooks/pre-commit`.

## 5. Volver al clon compartido (si hace falta)

```bash
git -C "<tu-worktree>" push origin HEAD:master
git -C "C:/Users/Steven Sànchez/OneDrive/OneSyncFiles" pull --no-rebase
```

El clon compartido sigue siendo la copia que leen Obsidian y el pipeline de sync; el worktree es
solo el sitio de trabajo con índice propio.

---

**Tags:** #herramientas #git #coordinacion #flujo
