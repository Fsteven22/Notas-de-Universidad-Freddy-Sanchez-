# HISTORIAL-LANZAMIENTO.md — Neonotes (Fase 7.4)

Historial formal de cierre del proyecto Neonotes. Migración: Obsidian vault → Astro site en Vercel.

## Deploy en producción

- **URL:** https://neonotes-espol.vercel.app
- **Plataforma:** Vercel (import del vault-repo, Root Directory = `site/`)
- **Build command:** `npm ci && VAULT_DIR=../Universidad npm run sync && npm run build`

## Estadísticas finales (build verificado)

- Notas publicadas: 802
- Omitidas (sin `dg-publish: true`): 5
- Semestres/bloques: 5
- Páginas generadas en build: 828
- ZIPs por materia: 13 (en `public/downloads/`)

## Decisiones clave (no reabrir)

1. Gate de publicación = `dg-publish: true` en el frontmatter de cada nota.
2. Assets sin gate; carpeta `_privado/` blacklisteada en `sync-vault.mjs`.
3. Carpeta `Herramientas/` excluida del site (zona interna del vault).
4. Artefactos derivados NUNCA al repo git: `notes-md/`, `public/assets/`, `src/data/vault.json`, `public/search-index.json`, `public/downloads/`.
5. `VAULT_DIR` como env var para unificar código y vault en un solo repo.
6. Unificación: código del site en `site/` dentro del vault-repo; Vercel build desde el builder (sin Action).

## Backlog 7.3 completado

- [x] sitemap.xml y robots.txt generados en build (alta)
- [x] Canonical + Open Graph tags en `Base.astro` (alta)
- [x] ZIP por materia con botón de descarga (media)
- [x] Carpeta `_privado/` blacklisteada en sync (media)
- [x] CSS `.nx-tag`, `.nx-doc`, KaTeX móvil (media)
- [x] `.gitignore` con artefactos derivados (media)
- [x] Runbook para el usuario (media) → `RUNBOOK.md`
- [ ] Cierre formal y migración a `site/docs/HISTORIAL-LANZAMIENTO.md` (baja) → este archivo

## Visor PDF (pendiente de decisión)

El visor embebido con pdf.js (`/pdfjs/viewer.html`) renderizaba pantalla negra sin errores en consola. Se revertió a tarjetas de descarga directa (commit `339078f`). Queda pendiente decidir si se revisa el visor o se mantiene la descarga directa.
