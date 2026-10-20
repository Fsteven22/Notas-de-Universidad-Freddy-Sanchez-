---
dg-publish: false
tags: [<% tp.system.prompt("Código materia (ej: IDIG2012)") %>, <% tp.system.prompt("Tag unidad (ej: unidad1)") %>]
---

# <% tp.file.title %>

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Importa?
>
> (Qué problema resuelve + dónde se evalúa/aplica. No adelantar definiciones.)
>
> **Analogía del mundo real:** (compara con algo cotidiano)
>
> | Sin Esto | Con Esto |
> |---|---|
> | (costo) | (beneficio) |
> | (costo) | (beneficio) |
>
> **En esta nota:** (lista de lo que cubre, 1 línea por bloque.)

![[<% tp.system.prompt("Nombre del SVG de intro (en Diagramas de la materia, sin .svg)") %>.svg]]

---

## 📋 Definiciones Formales

> [!note] 📋 Definición 1 — (Nombre)
>
> (Enunciado preciso con notación. Numerar para poder citarla desde otras notas.)
>

> [!note] 📋 Definición 2 — (Nombre)
>
> (Enunciado preciso. Solo numerar en notas teóricas; en aplicadas basta 1-2.)

---

## 🧵 Desarrollo

### 🎭 (Subtema 1)

> [!note] 🎨 (Idea central)
>
> (Explicación + tabla si aplica.)
>
> | Aspecto | Detalle |
> |---|---|
> | (fila) | (valor) |

---

## 🛠️ Método / Procedimiento

> [!note] 📋 Procedimiento General
>
> 1. (Paso verificable)
> 2. (Paso verificable)
> 3. (Criterio de salida: ¿cómo sé que quedó bien?)
>
> **Principio clave:** (1 frase que resume el método.)

---

## 🎨 Ejemplos Trabajados

> [!example] 🟢 Ejemplo 1 — (Caso con datos concretos)
>
> | Paso | Acción |
> |---|---|
> | (paso) | (resultado) |

---

## 📝 Ejercicios Propuestos (Guía N)

> [!example] ✏️ Ejercicio 1 — (Título) (Guía N, ej. X)
>
> (Enunciado. Si tiene literales (a), (b), (c)… o varios casos, CADA uno como ítem de lista `-`, nunca inline con `·`: en el render se pegan lado a lado.)
>
> > [!success]- ✅ Solución guiada
> >
> > - (a) **Resultado** — procedimiento en 1 línea.
> > - (b) **Resultado** — procedimiento en 1 línea.

> [!example] ✏️ Ejercicio 2 — (Título) (Guía N, ej. Y)
>
> (Enunciado como lista si es multi-parte.)
>
> > [!success]- ✅ Solución guiada
> >
> > (Procedimiento completo, no solo el resultado.)

> [!tip] 📏 Regla de callouts: entre dos callouts hermanos deja línea REALMENTE vacía (`>` solo los fusiona y el segundo header se ve como texto literal). El `success` de solución va SIEMPRE anidado DENTRO del `example` del ejercicio (un `> > [!success]` suelto, fuera del example, se renderiza roto).
>
> [!tip] 📏 Regla de ejercicios legibles: el planteamiento con mucha información va como lista `-` (entidades, datos, DF, pedido) para no cansar la vista; la solución se complementa con su diagrama ya compilado (`erDiagram`/`flowchart`) embebido como SVG o función Python cuando el tema lo pida (clausura, normalización).
>
> [!tip] 📏 Regla de enunciado original: todo ejercicio de examen/taller/lección trae su resumen en lista MÁS el enunciado original verbatim en un `> > [!quote]- 📄 Enunciado original` colapsado debajo del pedido (con fuente y nota de figuras si las hay).
>
> [!tip] 📏 Regla de diagramas: los diagramas ya NO van inline en Mermaid. Se escribe el código en un archivo `.mmd`/scratch, se compila con `mmdc` (`npx mmdc -i x.mmd -o x.svg`) y se embebe con `![[Diagramas/<Tema>_NN.svg]]` (los SVG viven en la carpeta `Diagramas` de cada materia, nombrados `<Nota_o_Tema>_NN`).
>
> [!tip] 📏 Regla de código dentro de callouts: un fence (```mermaid/```python) dentro de un callout NO lleva líneas vacías (cortan el callout en Live Preview) ni líneas solo con `>` (se ven literales dentro del código). Separa con comentarios reales (`# …`) o líneas continuas.
>
> [!tip] 📏 Reglas de pasos matemáticos: cada paso en su propia línea de lista `-` (nunca 2 pasos en 1 línea) y cada ecuación importante en bloque `$$` centrado.
>
> [!tip] 📏 Regla de oro en inducción (se evalúa): la HI se escribe **explícita y completa** (nunca "HI para p"), la **meta P(p+1)** se escribe antes de empezar, y el álgebra va **paso a paso sin saltos** (separar → sustituir → desarrollar → simplificar).

---

## 📋 Tablas Comparativas

> [!note] 📋 (Nombre de la comparación)
>
> | Aspecto | Opción A | Opción B |
> |---|---|---|
> | (criterio) | (valor) | (valor) |

---

## ⚠️ Errores Comunes y Principios Lógicos

> [!danger] ❌ Error 1 — (Nombre) (viola **(principio o definición)**)
>
> - ❌ **EL ERROR ESTÁ AQUÍ:** (qué se hace mal, concreto).
> - ✅ Así sí: (cómo hacerlo bien en 1 línea).

> [!danger] ❌ Error 2 — (Nombre) (viola **(principio)**)
>
> - ❌ **EL ERROR ESTÁ AQUÍ:** (qué se hace mal, concreto).
> - ✅ Así sí: (cómo hacerlo bien en 1 línea).

---

## 🎯 Metas de Aprendizaje

> [!note] 🎯 Nivel Básico
>
> - [ ] (Puedo definir / identificar sin mirar.)
> - [ ] (Reconozco el concepto en un ejemplo.)

> [!note] 🎯 Nivel Intermedio
>
> - [ ] (Aplico el método a un caso nuevo.)
> - [ ] (Comparo variantes y elijo bien.)

> [!note] 🎯 Nivel Avanzado
>
> - [ ] (Justifico decisiones / detecto errores en casos ajenos.)

---

## 🔁 Repaso SR (flashcards)

#flashcards/<% tp.system.prompt("Mazo SR (ej: bd-u1, discretas-u1)") %>

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿(Pregunta)?::(Respuesta corta, 1 línea.)
> - ¿(Pregunta)?::(Respuesta corta, 1 línea.)
> - ¿(Pregunta)?::(Respuesta corta, 1 línea.)

---

## 📊 Resumen Visual

![[<% tp.system.prompt("Nombre del SVG de resumen (en Diagramas de la materia, sin .svg)") %>.svg]]

> [!success] 🔍 Comparación Final
>
> | Aspecto | Sin Esto | Con Esto |
> |---|---|---|
> | (criterio) | ❌ | ✅ |

---

## 🚀 Próximos Pasos

> [!quote] 🌟 Continuando
>
> **Has aprendido:**
>
> ✅ (punto 1)
> ✅ (punto 2)
>
> **Próximo tema:**
>
> | Tema | Qué verás | Por qué importa |
> |---|---|---|
> | (siguiente) | (contenido) | (motivo) |

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[<% tp.system.prompt("Nota mapa de contenido") %>]]
> - Índice: [[<% tp.system.prompt("Nota índice de unidad") %>]]
> - Anterior: [[<% tp.system.prompt("Nota anterior (vacío si es la 1)") %>]]
> - Siguiente: [[<% tp.system.prompt("Nota siguiente (vacío si es la última)") %>]]
> - Syllabus: [[<% tp.system.prompt("Nota bienvenida/syllabus") %>]]
> - Base MOOC (si aplica): [[<% tp.system.prompt("Nota MOOC base (vacío si no aplica)") %>]]

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - (Libro, cap. X §Y / diapositiva docente / URL verificada — citar exacto, no de memoria)

---

**Tags:** #<% tp.system.prompt("Tag materia") %>
