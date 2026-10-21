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

Colapsa blancos múltiples y separadores `>` dobles, quita trailing whitespace, **preserva CRLF/LF** y nunca toca blanks entre callouts hermanos ni dentro de fences. Guard nuevo: si los fences están desbalanceados o con quoting disparejo, fuerza dry-run y no aplica (arregla con `verificar_nota.py` primero).

## `kit_recuperacion.py` — kit de recuperación FESD (dry-run por defecto)

Creado tras el incidente del 19/10/2026 (un script de tags con doble `tags:` sobrescribió 24 notas de FESD con stubs y con el contenido de otra nota). Todos los comandos que modifican archivos (`restore`, `repath`, `pipes`) son dry-run por defecto y solo escriben con `--aplicar`; `daniadas`, `sweep` y `compa` son siempre de solo lectura.

```bash
py kit_recuperacion.py daniadas 8a89bcf 6424ecf          # lista .md dañados entre refs
py kit_recuperacion.py restore 8a89bcf 6424ecf           # dry-run; --aplicar escribe
py kit_recuperacion.py repath --aplicar                  # arregla embeds '../Diagramas'/'../Anexos'
py kit_recuperacion.py pipes "Unidad 3 - Circuitos integrados" --aplicar
py kit_recuperacion.py sweep                             # verificar_nota.py en todas las notas FESD
py kit_recuperacion.py compa 5ba8f1b "Universidad/.../nota.md"   # dif cuerpo vs ref
```

La restauración reemplaza el cuerpo del archivo por el contenido en `git show <ref_ok>:<ruta>` (con guardado que preserva CRLF/LF) y garantiza UNA línea `tags:` correcta por unidad + `dg-publish: true` dentro del frontmatter.

### Regla anti doble-`tags:` (la del incidente)

Ningún script inserta una línea `tags:` si la nota ya tiene una en sus primeras 12 líneas. Invariantes: la nota tiene CERO o UNA línea `tags:`, dentro del frontmatter, nunca dos ni fuera del `---` limítrofe. Los stubs de ~500/750/980 bytes en FESD eran la firma del script roto del 19/10 — si reaparecen, `kit_recuperacion.py restore <ref_ok> <ref_dano> --aplicar`.

### Capa de prevención (añadida tras el incidente)

`verificar_nota.py` ahora falla cuando ve: más de una línea `tags:` en el frontmatter, un segundo bloque `---` en la cabecera (frontmatter duplicado), `tags:` sueltas después del frontmatter, o secuencias `\r\r` (endings corruptos por reescrituras dobles).

`auditoria.py` (barrido del vault) añadió checks: **9** múltiples `tags:` por archivo, **10** cuerpos clónicos exactos (md5), **11** cuerpos casi-iguales ≥ 0.93 de similaridad (contenido cruzado: nota A rellenada con nota B), **12** `\r\r` en bytes crudos.

`kit_recuperacion.py` añadió:
- `fix-tags [subcarpeta|nota] [--aplicar]` — repara notas con doble `tags:`/segundo `---`/`tags:` suelta: conserva UNA línea tags (la primera) y limpia el cuerpo.
- `dupez [subcarpeta]` — clones exactos + contenido cruzado (similaridad ≥ 0.93, prefiltrada por H1 y tamaño).
- `guardian [subcarpeta]` — chequeo completo (verify + clones + cruzado); sugiere el comando de reparación. Correrlo tras cualquier sesión de scripts que toquen notas.

## `referencias.py` — auditoría de referencias entre notas FESD

```bash
py referencias.py                       # dry-run completo de la materia
py referencias.py --aplicar             # agrega la sección a las sin referencias
py referencias.py --min 3               # exigir más links inline para dar OK
```

Audita cada nota: OK si tiene sección `## 📚 Referencias` (fuentes, estilo Unidad 1) o si enlaza a ≥ 2 notas de la materia; `SIN REF` si no tiene ninguna. Con `--aplicar`, a las `SIN REF` les agrega `## 🔗 Relacionadas` al final con links a las notas hermanas de su carpeta (o a la MOC de la materia si es nota única no tiene hermanas). Nunca inventa citas bibliográficas.

## Diagramas mermaid → SVG (receta)

Los bloques mermaid dentro de callouts no renderizan en Live Preview ni confiable en Garden: se convierten a SVG y se incrustan con `![[carpeta/archivo.svg]]`. La fuente `.mmd` se guarda junto al `.svg` para reeditar.

```bash
mmdc -i diagrama.mmd -o diagrama.svg
```

Convención de nombres BD: `uX-NN-tipo.svg` (unidad-nota-posición-tipo: `er`, `flow`, `graph`) y `ejNN-tema.svg` para guías. Tras reemplazar, correr `verificar_nota.py` (chequea que cada embed resuelva).

## Figuras de dependencias (matplotlib)

`Temp/opencode/bdstrips.py` genera tiras de dependencias estilo examen (cajas + flechas arriba/abajo + corchete PK) en SVG. Es desechable por figura; si se vuelve rutina, traer la función aquí.

## Registro de patrones (error → fix → script)

- Ejercicio/example vacío (header sin cuerpo, ej. Inglés U1-01 Ej.4): completar con el drill real; detecta con `detectar_vacios.py`. Falsos positivos conocidos: `###`→`####` con contenido, callout usado como título de sección, contenido inline en la línea del header.
- `> [!example]` usado como título (`Machine Learning.md`): convertir a `###`.

- Dentro de fences en callouts: ni líneas vacías (cortan el quote) ni líneas solo con `>` (salen literales) — separar con comentarios reales.
- El `success` de solución va anidado DENTRO del `example`, nunca suelto.
- Flashcards (`Pregunta::Respuesta`): para notas nuevas, siempre a nivel superior, fuera de callouts (formato documentado). Las que ya viven en callouts con datos `<!--SR:...-->` SÍ las lee el plugin (probado) — no migrar mazos que funcionan; solo unificar secciones mezcladas moviendo tarjeta + comentario juntos.
- Rutas de embeds: relativas a la carpeta de la nota; tras mover archivos, re-verificar.
