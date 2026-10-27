# HISTORIAL-LANZAMIENTO.md — Neonotes (Fase 7.4)

Historial formal de cierre del proyecto Neonotes. Migración: Obsidian vault → Astro site en Vercel.

## Deploy en producción

- **URL:** https://neonotes-espol.vercel.app
- **Plataforma:** Vercel (import del vault-repo, Root Directory = `site/`)
- **Build command:** `npm ci && VAULT_DIR=../Universidad npm run sync && npm run build`

## Estadísticas finales (build verificado)

- Notas publicadas: 805
- Omitidas (sin `dg-publish: true`): 3
- Semestres/bloques: 5
- Páginas generadas en build: 831
- ZIPs por materia: 13 (en `public/downloads/`)
- Assets publicados: 2745 (742 MB) de 2741 assets del vault tras la limpieza de huérfanos

## Decisiones clave (no reabrir)

1. Gate de publicación = `dg-publish: true` en el frontmatter de cada nota.
2. Segundo gate de archivos = `Universidad/_no-publicar.txt` (patrones con comodines, por nombre y ruta relativa). Material con copyright y material propio ya publicado en PDF quedan siempre fuera.
3. Solo se publica un asset si **alguna nota publicada lo referencia**. Un archivo sin referencia no llega al sitio ni a los ZIPs.
4. La carpeta `_privado/` sigue blacklisteada en `sync-vault.mjs`.
5. Carpeta `Herramientas/` excluida del site (zona interna del vault).
6. Artefactos derivados NUNCA al repo git: `notes-md/`, `public/assets/`, `src/data/vault.json`, `public/search-index.json`, `public/downloads/`.
7. `VAULT_DIR` como env var para unificar código y vault en un solo repo.
8. Unificación: código del site en `site/` dentro del vault-repo; Vercel build desde el builder (sin Action).
9. Los embeds `![[Nota]]` sin extensión de media se normalizan a `[[Nota]]` para que resuelvan como enlace de nota en el sitio.

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
