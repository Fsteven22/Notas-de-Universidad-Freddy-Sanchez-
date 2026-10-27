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

## 2. Qué se publica (notas y archivos)

El build tiene **dos gates distintos**:

| Gate | Dónde se declara | Efecto |
|---|---|---|
| `dg-publish: true` | frontmatter de la nota | Si falta, la nota no se publica (queda en "omitidas"). |
| `Universidad/_no-publicar.txt` | un patrón por línea | El archivo nunca se publica, aunque una nota lo referencie. |

Reglas de archivos (`site/scripts/sync-vault.mjs`):

1. **Solo se copia un archivo si alguna nota publicada lo referencia.** Un asset sin
   referencia no llega al sitio ni a los ZIPs por materia.
2. `_no-publicar.txt` se lee antes de copiar: admite comodines (`*`, `?`) y compara
   por nombre de archivo y por ruta relativa a `Universidad/`. Sirve para material
   con copyright (libros de texto, material de Cambridge) y para material propio
   ya publicado en PDF.
3. La carpeta `_privado/` se ignora en todo el recorrido del vault.
4. Cuando una nota referencia un archivo que no se publica, el build deja el
   marcador `<!-- nx:asset-omitido ... -->` en el HTML para que el hueco quede
   explícito y no se pase por alto.

Si querés publicar un archivo que hoy está en `_no-publicar.txt`, quitá su patrón
de la lista y pusheá: el archivo aparece en el siguiente build.

## 3. Cómo verificar que salió

- Entrá a https://neonotes-espol.vercel.app y buscá la nota con Ctrl+K o navegando por semestre → materia.
- O consultá `https://neonotes-espol.vercel.app/search-index.json` y buscá el título de tu nota.
- Si la nota no aparece, revisá que tenga `dg-publish: true` y que el push haya llegado a GitHub.

## 4. Si un build falla

1. Entrá al panel de Vercel → **Deployments**.
2. Buscá el deploy fallido (estado "Error") y abrís el **Build Log**.
3. Identificá el error (suele ser una nota con frontmatter malformado o un asset roto).
4. Fix en Obsidian → pusheá → nuevo deploy automático.
5. Si necesitás volver atrás de inmediato: **Instant Rollback** en el deploy anterior estable desde Vercel.

## 5. Regla de disciplina de copias (NO romper esto)

| Copia | Qué hace | Regla de oro |
|---|---|---|
| **OneDrive** (`OneSyncFiles/Universidad/`) | Solo notas del vault | Editar **siempre** acá. Nunca commitear código (`site/`) acá. |
| **Desktop** (`notas-nexus-unificado/site/`) | Código del site | Clonado del vault-repo. **Nunca** commitear notas (`Universidad/`) acá. |

El único gesto de publicación es un **push del vault** (notas). El site se reconstruye solo en Vercel.

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

Si lo que falta es un **archivo** (imagen, PDF, diagrama), el build lo reporta como
`nx:asset-omitido` en la nota. Causas habituales:

- el archivo no existe en el vault → recrealo con el nombre exacto que usa la nota;
- el archivo está en `_no-publicar.txt` → decidí si corresponde publicarlo;
- el archivo existe pero ninguna nota publicada lo referencia → no se sube por diseño.

La lista de embeds que hoy no resuelven se regenera en
`Universidad/Herramientas/SVGs por recrear.md`.
