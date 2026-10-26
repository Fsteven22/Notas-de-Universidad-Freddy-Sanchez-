# RUNBOOK — Neonotes (Fase 7.2)

Flujo diario para publicar notas en https://neonotes-espol.vercel.app

## 1. Flujo de publicación (cada día)

1. **Escribís la nota en Obsidian** (vault en OneDrive: `OneSyncFiles/Universidad/`).
2. **Agregá `dg-publish: true`** en el frontmatter inicial de la nota (`--- ... ---`).
   - Sin este flag, la nota NO se publica (queda en "omitidas").
3. **Guardá y pusheá** el vault-repo a GitHub (`Fsteven22/Notas-de-Universidad-Freddy-Sanchez-`).
4. **Vercel detecta el push** y despliega automáticamente:
   - `npm ci && VAULT_DIR=../Universidad npm run sync && npm run build`
   - Los cambios aparecen en producción en pocos minutos.

## 2. Cómo verificar que salió

- Entrá a https://neonotes-espol.vercel.app y buscá la nota con Ctrl+K o navegando por semestre → materia.
- O consultá `https://neonotes-espol.vercel.app/search-index.json` y buscá el título de tu nota.
- Si la nota no aparece, revisá que tenga `dg-publish: true` y que el push haya llegado a GitHub.

## 3. Si un build falla

1. Entrá al panel de Vercel → **Deployments**.
2. Buscá el deploy fallido (estado "Error") y abrís el **Build Log**.
3. Identificá el error (suele ser una nota con frontmatter malformado o un asset roto).
4. Fix en Obsidian → pusheá → nuevo deploy automático.
5. Si necesitás volver atrás de inmediato: **Instant Rollback** en el deploy anterior estable desde Vercel.

## 4. Regla de disciplina de copias (NO romper esto)

| Copia | Qué hace | Regla de oro |
|---|---|---|
| **OneDrive** (`OneSyncFiles/Universidad/`) | Vault de trabajo (el que ves en Obsidian) | Editar **siempre** acá. Nunca commitear código (`site/`) acá. |
| **Desktop** (`notas-nexus-unificado/site/`) | Código del site | Clonado del vault-repo. **Nunca** commitear notas (`Universidad/`) acá. |
| **Repo** (`notas-nexus-unificado/Universidad/`) | Copia del vault que Vercel construye | Se replica desde OneDrive; es lo único que el deploy ve. |

El único gesto de publicación es un **push del vault** (notas). El site se reconstruye solo en Vercel.

> Ojo: el vault del repo **sí** lleva las notas commiteadas (Vercel las necesita para
> construir). La regla "no commitear notas" aplica al trabajo diario: se edita en
> OneDrive y se replica al repo. `_no-publicar.txt` y los assets que publica el
> sitio tienen que existir en **las dos** copias.

## 5. Archivos que NO se publican (`_no-publicar.txt`)

Para material que no debe salir a internet (libros de texto con copyright, material de cátedra) hay una lista en la raíz del vault:

`Universidad/_no-publicar.txt`

Un nombre de archivo por línea, `#` para comentarios, comodín `*` admitido.

Qué hace, automáticamente y en cada build:

- el archivo **no** se copia a `/assets/` → no existe URL pública
- **no** entra en los ZIP por materia
- si una nota lo embebe, queda como `asset omitido` (no como link roto)

Los archivos **no se borran**: siguen en tu vault local, solo se ocultan del sitio. Sacar algo de la lista y pushear lo vuelve a publicar en el siguiente deploy.

> La lista existe en las dos copias del vault (OneDrive y el repo del sitio). Si la editás en una, replicá el cambio en la otra: el deploy lee la del repo.

## 6. Comandos útiles (solo en el clone de desarrollo)

```bash
# Ver notas nuevas del vault antes de hacer sync
git pull

# Sincronizar vault → site (genera notes-md/, public/assets/, vault.json, zips)
VAULT_DIR=../notas-nexus-unificado/Universidad npm run sync

# Build local para probar antes de pushear
npm run build

# Servidor de desarrollo
npm run dev
```

## 7. Qué NO hacer

- No edites notas directamente en el clone de Desktop (`notas-nexus-unificado/Universidad/`). Esa zona es de solo lectura para el site; las notas viven en OneDrive.
- No commitees artefactos derivados (`notes-md/`, `public/assets/`, `vault.json`, `search-index.json`, `public/downloads/`). Están en `.gitignore` y se regeneran en cada build.
- No borres `public/pdfjs/build/` ni `public/pdfjs/web/` manualmente; se regeneran con `sync`.

---

## Notas omitidas (sin `dg-publish`)

Si una nota no aparece, probablemente le falta el flag. Las omitidas se listan en la consola al correr `npm run sync`. Para publicarlas, agregá `dg-publish: true` en el frontmatter de la nota en Obsidian y pusheá.
