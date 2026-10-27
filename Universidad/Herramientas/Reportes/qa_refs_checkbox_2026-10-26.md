---
dg-publish: false
tags: [auditoria, mantenimiento, markdown]
---

# 🔍 Auditoría: referencias que Obsidian vuelve checkbox (26/10/2026)

> [!warning] El bug
> Obsidian convierte cualquier item de lista que empiece por `[algo]` en **task list**. Una referencia APA escrita como `- [1] Autor...` se renderiza como un checkbox marcado, igual que la notación matemática `- [E] = ML²T⁻²`.

> [!success] Corrección aplicada
> Las referencias numéricas pasaron a `- **[1]** Autor...` y los símbolos a `- \[E\] = ...`. Los checkboxes legítimos (`- [ ]`, `- [x]`) no se tocaron.

**Resultado:** 13 notas con referencias numéricas (35 casos), 3 notas con símbolos (6 casos) y 5 notas con callouts dentro de lista (5 casos, solo aviso).

## Referencias numéricas (corregidas)

| Nota | Líneas | Tokens |
|---|---|---|
| `Universidad/2do Semestre/Comunicación/Bienvenida y Syllabus Comunicación.md` | 91 | [1] |
| `Universidad/2do Semestre/Comunicación/Unidad 1 - Comunicación efectiva/02 - Comunicación grupal y toma de decisiones.md` | 264 | [1] |
| `Universidad/2do Semestre/Comunicación/Unidad 1 - Comunicación efectiva/03 - Comunicación estratégica, IIR y pitch personal.md` | 278, 279, 280 | [1], [2], [3] |
| `Universidad/2do Semestre/Comunicación/Unidad 2 - Pensamiento complejo y crítico/01 - Pensamiento complejo vs pensamiento lineal.md` | 196, 197, 198 | [1], [2], [3] |
| `Universidad/2do Semestre/Comunicación/Unidad 2 - Pensamiento complejo y crítico/02 - Pensamiento crítico y perfil prosumidor.md` | 192, 193 | [1], [2] |
| `Universidad/2do Semestre/Comunicación/Unidad 3 - Redacción/01 - Texto expositivo, claridad y APA.md` | 196, 197 | [1], [2] |
| `Universidad/2do Semestre/Comunicación/Unidad 3 - Redacción/02 - Informes técnicos y ejecutivos, síntesis y paráfrasis.md` | 269, 270, 271, 272, 273 | [1], [2], [3], [4], [5] |
| `Universidad/2do Semestre/Comunicación/Unidad 3 - Redacción/03 - IA ética y prompts para redacción.md` | 329, 330, 331, 332 | [1], [2], [3], [4] |
| `Universidad/2do Semestre/Comunicación/Unidad 4 - Comportamiento comunicacional/01 - Argumentación efectiva, convencer vs persuadir.md` | 170 | [1] |
| `Universidad/2do Semestre/Comunicación/Unidad 4 - Comportamiento comunicacional/02 - Storytelling para comunicar ciencia.md` | 152 | [1] |
| `Universidad/2do Semestre/Comunicación/Unidad 4 - Comportamiento comunicacional/03 - Voz, cuerpo, formatos y práctica TED.md` | 195, 196 | [1], [2] |
| `Universidad/3er Semestre/Diseño de Software/Bienvenida y Syllabus Diseño de Software.md` | 92, 95, 96, 97, 98, 99 | [1], [2], [3], [4], [5], [6] |
| `Universidad/3er Semestre/Ingles III/Bienvenida y Syllabus Ingles III.md` | 74, 77, 78, 79 | [1], [2], [3], [4] |

## Símbolos en lista (corregidos)

| Nota | Líneas | Tokens |
|---|---|---|
| `Universidad/1er Semestre/Física Mecánica/Practicas De Laboratorio/Prerrequisitos de Talleres y Reportes/Mediciones e Instrumentos/Mediciones Fundamentales.md` | 258, 262, 263, 264 | [E], [m], [v²], [½mv²] |
| `Universidad/2do Semestre/Algebra Lineal/Unidad 1 – Sistemas Lineales y Matrices/III – Rango y teoremas fundamentales/01 - Rango de una Matriz.md` | 316 | [A\|B] |
| `Universidad/2do Semestre/Cálculo Vectorial/Unidad 1 - Geometría Analítica en ℝ³/II – Producto Punto, Producto Cruz y Aplicaciones Geométricas/02 – Producto cruz y áreas.md` | 66 | [u, v] |

## Callouts dentro de lista (pendiente manual)

| Nota | Línea | Texto |
|---|---|---|
| `Universidad/Preuniversitario/MOOC de Comunicación/Unidad 4 - Resumen y síntesis/01 - El resumen académico.md` | 245 | > - [!info] Conexión cruzada con la Unidad 5: la fase 3 (localizar ideas secundarias esenciales) reutiliza la ... |
| `Universidad/Preuniversitario/MOOC de Comunicación/Unidad 4 - Resumen y síntesis/04 - Usos correctos e incorrectos del gerundio.md` | 209 | > - [!info] Aunque temáticamente es un tema gramatical distinto al resumen/síntesis, esta nota se agrupa en la... |
| `Universidad/Preuniversitario/MOOC de Comunicación/Unidad 5 - Textos expositivos/01 - El texto expositivo (concepto, tipos y estructura).md` | 284 | > - [!info] Conexión cruzada con la Unidad 6: el texto expositivo se distingue del texto argumentativo por la ... |
| `Universidad/Preuniversitario/MOOC de Comunicación/Unidad 5 - Textos expositivos/02 - Análisis del texto expositivo.md` | 215 | > - [!info] Conexión cruzada con la Unidad 6: esta técnica de disección es análoga a la metodología de análisi... |
| `Universidad/Preuniversitario/MOOC de Comunicación/Unidad 5 - Textos expositivos/03 - Conectores textuales y coherencia lógica.md` | 404 | > - [!info] Conexión cruzada con la Unidad 6: la contraargumentación en el texto argumentativo (ver [ [Universi... |

## Cómo re-ejecutar la auditoría

```bash
py "Universidad\Herramientas\Mantenimiento\qa_refs_checkbox.py" "<vault>" -o "reporte.txt"
py "Universidad\Herramientas\Mantenimiento\qa_refs_checkbox.py" "<vault>" --fix
```

> [!tip] Criterio
> Script documentado en [[LEEME-SCRIPTS]]. Al escribir preserva el fin de línea original de cada archivo y no toca los checkboxes legítimos.

---

**Tags:** #auditoria #mantenimiento #markdown
