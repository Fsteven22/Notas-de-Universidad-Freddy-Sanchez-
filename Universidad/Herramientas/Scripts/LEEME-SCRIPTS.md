---
dg-publish: false
---

# 🛠️ Scripts del vault (no se publican)

> [!info] ℹ️ Qué hay aquí
> Utilidades propias en Python (solo librería estándar). Los `.py` nunca se publican al Garden (solo viajan `.md` con `dg-publish: true`). Flujo antes de dar por terminada una nota: **verificar → limpiar → volver a verificar**.

## `verificar_nota.py` — auditoría pre-entrega (solo lee)

```bash
py verificar_nota.py "ruta/nota.md"
```

Revisa: frontmatter (`dg-publish`, sin blancos, tags), callouts huérfanos, líneas vacías intrusas, fences desbalanceados o con líneas vacías adentro, mermaid dentro de callouts (aviso: en Live Preview se ve como código), embeds que no resuelven, tablas con pipes disparejos, headers indentados/pegados y finales de línea (CRLF/LF/mixto). Sale `0` si está limpia.

## `limpiar_espacios.py` — limpiador seguro

```bash
py limpiar_espacios.py "ruta/nota.md"        # dry-run (solo reporta)
py limpiar_espacios.py "ruta/nota.md" --fix # aplica
```

Colapsa blancos múltiples y separadores `>` dobles, quita trailing whitespace, **preserva CRLF/LF** y nunca toca blanks entre callouts hermanos ni dentro de fences.

## Diagramas mermaid → SVG (receta)

Los bloques mermaid dentro de callouts no renderizan en Live Preview ni confiable en Garden: se convierten a SVG y se incrustan con `![[carpeta/archivo.svg]]`. La fuente `.mmd` se guarda junto al `.svg` para reeditar.

```bash
mmdc -i diagrama.mmd -o diagrama.svg
```

Convención de nombres BD: `uX-NN-tipo.svg` (unidad-nota-posición-tipo: `er`, `flow`, `graph`) y `ejNN-tema.svg` para guías. Tras reemplazar, correr `verificar_nota.py` (chequea que cada embed resuelva).

## Figuras de dependencias (matplotlib)

`Temp/opencode/bdstrips.py` genera tiras de dependencias estilo examen (cajas + flechas arriba/abajo + corchete PK) en SVG. Es desechable por figura; si se vuelve rutina, traer la función aquí.

## Reglas aprendidas (no repetir)

- Dentro de fences en callouts: ni líneas vacías (cortan el quote) ni líneas solo con `>` (salen literales) — separar con comentarios reales.
- El `success` de solución va anidado DENTRO del `example`, nunca suelto.
- Flashcards (`Pregunta::Respuesta`) siempre a nivel superior, fuera de callouts.
- Rutas de embeds: relativas a la carpeta de la nota; tras mover archivos, re-verificar.
