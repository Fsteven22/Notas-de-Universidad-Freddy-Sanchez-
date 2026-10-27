---
dg-publish: false
tags: [clippings, log, opencode-site]
---

# LOG - opencode-site (sesion 2026-10-27)

> Bitácora de la sesión **opencode-site** (la que trabaja el sitio y las exclusiones
> de publicación). No confundir con `LOG-opencode.md`, que es de otra sesión en paralelo
> (links rotos en `Universidad/3er Semestre/**` y `Universidad/Herramientas/Mantenimiento/**`).

## Ámbito

- Repo: `notas-nexus-unificado` (rama `master`, push a `origin/master`).
- Deploy: `https://neonotes-espol.vercel.app` (Astro + Vercel, 828 páginas).
- Vault con dos copias que se deben mantener iguales: `notas-nexus-unificado/Universidad/` (despliega) y `OneSyncFiles/Universidad/` (trabajo).
- Flujo: `npm run sync` (`$env:VAULT_DIR="..\Universidad"`) → `npm run build` → `git add <rutas exactas>` → commit → push → esperar deploy → verificar en producción.

## Archivos que reservo (no editar sin avisar)

| Ruta | Qué hago |
|---|---|
| `site/src/styles/nexus.css`, `site/src/styles/content.css` | Paleta de marca |
| `site/src/components/SearchModal.astro` | Buscador (estilos y resaltado) |
| `site/src/pages/index.astro`, `site/src/layouts/Base.astro` | Portada y metadatos |
| `site/public/logo.svg`, `favicon.svg`, `og-neonotes.png`, `icon-*.png`, `apple-touch-icon.png` | Marca |
| `Universidad/_no-publicar.txt` (repo y OneDrive) | Qué se publica |
| `2do Semestre/Comunicación/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md` | Exclusiones |
| `3er Semestre/Diseño de Software/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md` | Exclusiones (tú dentro de 3er Semestre) |
| `3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/Recursos Unidad 0.md` | Exclusiones (tú dentro de 3er Semestre) |

## Commits de esta sesión

| Commit | Alcance |
|---|---|
| `4a3e443` | Site: logo propio, portada OG y favicon |
| `ba9ad13` | Site: paleta violeta→azul + fix de estilos del buscador |
| `88b3fac` | Vault: excluye Escucha Activa, UML Stevens y material Cambridge |
| `486f927` | Vault: excluye video de dinámicas y capturas Cambridge |
| `7eeef28` | Site: redirect 308 del dominio duplicado al canonical + sección de dominios en RUNBOOK |

**Efecto:** ZIP Comunicación 32,4→18,8 MB, Inglés III 10,3→1,4 MB, Diseño 10,6→7,3 MB; assets publicados 791→691 MB.

## Pendientes (requieren decisión)

1. **6 notas sin `dg-publish`** (no se publican):
   - `1er Semestre/Física Mecánica/Unidad 0 - Guias y Ejercicios/Guías y Ejercicios (Prof. Zambrano).md`
   - `3er Semestre/Fundamentos de Electricidad y Sistemas Digitales/Practico/Practicas del Laboratorio/Práctica 3 FESD/Práctica 3 — Diodos y Transistores.md`
   - `3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md`
   - `3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/Capturas Empower U10-U12/Libro de ingles ultimas unidades.md`
   - `3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/Capturas Empower U7-U10/Libro de ingles las primeras unidades.md`
   - `3er Semestre/Sistema de Bases de Datos/Unidad 0 - Guias y Ejercicios/Talleres/Tarea 2.md`
2. **Dominio duplicado — falta un paso en el panel (no se puede hacer desde el repo).** `neonotes.vercel.app` lo responde un proyecto de Vercel aparte (la página "About" por defecto), no este sitio. Ya agregué el redirect 308 por host en `site/vercel.json` (se activa solo si el dominio pasa a apuntar a este proyecto) y los pasos en `site/RUNBOOK.md` sección 8:
   - Panel → proyecto `neonotes` (el que muestra "About") → Settings → Domains: redirigir a `https://neonotes-espol.vercel.app` o borrarlo.
   - O borrarlo y en `neonotes-espol` → Settings → Domains → Add Domain → `neonotes.vercel.app`.
   - Verificar: `curl -I https://neonotes.vercel.app/3er-semestre/` → 308 con `Location` al canonical.
   - Nota: el CLI de Vercel de esta máquina no tiene token válido (`vercel whoami` → "The specified token is not valid"), por eso no se puede hacer por terminal.
3. `favicon.ico` da 404 (solo hay `.svg`).
4. **Sandbox desactualizado:** `notas-nexus` (`C:\Users\STEVEN~1\Desktop\Proyectos`) sirve la versión verde del sitio y su `PLAN-PUBLICACION.md` dice "baseline 798".
5. **Divergencia de vault:** la copia de OneDrive de `3er Semestre/Diseño de Software/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md` es una versión anterior (la del repo es la vigente).
6. **Colisión con la otra sesión `opencode`:** las dos creamos `Universidad/_no-publicar.txt` (la mía en `master` con 15 entradas; la de la otra en `backup-pre-fix-links` con 13). Al integrar, **unir las listas** y re-sincronizar.

## No toco sin avisar

- Cambios de color/estilos del sitio (`nexus.css`, `content.css`, `SearchModal.astro`, `index.astro`, `Base.astro`).
- Archivos de marca en `site/public/` (logo, favicon, OG, iconos).
- `_no-publicar.txt` y las 3 notas reservadas de la tabla de arriba.
- Los ~17 `.md` con CRLF del vault: aparecen modificados en `git status` pero no son cambios míos.
- El trabajo de la otra sesión en `Universidad/3er Semestre/**` (links) y `Universidad/Herramientas/Mantenimiento/**`.

## Notas técnicas para quien siga

- `git diff --name-only` escapa los paths: usar `-c core.quotePath=false`.
- `git add -A` está prohibido: stagear rutas exactas (los `.md` con CRLF se cuelan).
- `node -e` con el signo dollar + llave se rompe en PowerShell: escribir scripts `.mjs`.
- Servidor estático para probar `dist`: `node static-server.mjs <raiz> <puerto>` (ojo: el 8099 lo tenía un servidor viejo apuntando al sandbox).
- Los nombres de archivo con á/é en la ruta rompen `Start-Process -ArgumentList`; usar `C:\Users\STEVEN~1\...`.
- El `<style>` de un componente Astro es *scoped*: lo que el JS inyecta en el DOM no lo toma, hay que moverlo a `is:global`.

---
**Tags:** #clippings #log #opencode-site
