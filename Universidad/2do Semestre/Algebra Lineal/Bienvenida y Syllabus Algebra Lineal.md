# 🟦 Álgebra Lineal — Bienvenida y Syllabus

## 🎉 ¡Bienvenido/a a Álgebra Lineal!

> [!info]- 👋 Sobre esta materia
>
> ¡Hola y bienvenido/a! Álgebra Lineal es un curso de formación básica que aborda matrices, sistemas de ecuaciones lineales, espacios vectoriales, transformaciones lineales, espacios con producto interno, y valores y vectores propios. Es una de las materias más fundamentales para la ingeniería y las ciencias computacionales.
>
> | Dato | Detalle |
> |---|---|
> | **Materia** | Álgebra Lineal |
> | **Código** | MATG1049 |
> | **Institución** | ESPOL — Carrera de Computación |
> | **Créditos** | 5.8 ECTS |
> | **Horas** | 3h docencia · 1h prácticas · 5h autónomas |
> | **Tipo** | Obligatorio |
> | **Prerrequisito** | Cálculo de una Variable (MATG1045) |
> | **Coordinadora** | Franca Marisol Laveglia |
> | **Syllabus oficial** | 📎 [Ver PDF completo](SPA-SyllabusEUR_ACE-MATG1049.pdf) |

---

## 🎯 Objetivos del Curso

> [!note]- 📌 ¿Qué vamos a lograr?
>
> Este curso contribuye a la formación integral del futuro profesional, desarrollando el pensamiento abstracto y la capacidad de resolver problemas usando modelos matemáticos lineales.
>
> **Objetivos específicos:**
>
> | # | Objetivo |
> |---|---|
> | 1 | Resolver problemas que requieren modelos matemáticos y sistemas de ecuaciones lineales |
> | 2 | Utilizar conceptos de matrices, espacios vectoriales, transformaciones lineales y vectores propios para resolver problemas de ingeniería |
> | 3 | Identificar hipótesis y conclusión de enunciados lógicos de álgebra lineal para analizar su validez |

---

## 📋 Evaluación

> [!warning]- 📊 ¿Cómo se evalúa?
>
> | Actividad | ¿Aplica? |
> |---|---|
> | Exámenes | ✅ |
> | Lecciones | ✅ |
> | Tareas | ✅ |
> | Proyectos | ✅ |
> | Participación | ✅ |
> | Otras | ✅ |

---

## 🗂️ Contenido del Curso

> [!tip]- 📚 Temas a cubrir
>
> ```mermaid
> graph LR
>     A[📐 Álgebra\nLineal] --> B[Unidad 1\nSistemas Lineales y Matrices]
>     A --> C[Unidad 2\nEspacios Vectoriales]
>     A --> D[Unidad 3\nTransformaciones Lineales]
>     A --> E[Unidad 4\nProducto Interno]
>     A --> F[Unidad 5\nValores y Vectores Propios]
>
>     style B fill:#e1f5ff
>     style C fill:#e1ffe1
>     style D fill:#fff4e1
>     style E fill:#ffe1e1
>     style F fill:#f0e1ff
> ```
>
> | Unidad | Tema | Horas |
> |---|---|---|
> | **1** | Sistemas de ecuaciones lineales y matrices | 4h |
> | **2** | Espacios vectoriales | 14h |
> | **3** | Transformaciones lineales | 9h |
> | **4** | Espacios con producto interno | 6h |
> | **5** | Valores y vectores propios | 9h |
> | — | Actividades de evaluación | 6h |

---

## 📚 Bibliografía (Formato IEEE)

> [!quote]- 📖 Fuentes oficiales de la materia
>
> **Lectura obligatoria:**
>
> [1] S. Grossman, *Álgebra Lineal*, 7ma ed. México: McGraw-Hill, 2012.
>
> **Lectura adicional:**
>
> [2] D. C. Lay, *Álgebra Lineal y sus Aplicaciones*, 4ta ed. México: Pearson, 2012.
>
> [3] D. Poole, *Álgebra Lineal: Una Introducción Moderna*, 3ra ed. México: Cengage Learning, 2011.
>
> [4] J. C. Del Valle Sotelo, *Álgebra Lineal para Estudiantes de Ingeniería y Ciencias*, 1ra ed. México: McGraw-Hill, 2012.
>
> [5] B. Kolman, *Álgebra Lineal*, 8va ed. México: Pearson, 2006.

---

## 🗺️ Índice de Notas

> [!tip]- 📂 Estructura del repositorio
>
> ```
> 📁 Álgebra Lineal/
> ├── 📄 00 - Bienvenida y Syllabus.md
> ├── 📎 SPA-SyllabusEUR_ACE-MATG1049.pdf
> │
> ├── 📁 Unidad 1 - Sistemas Lineales y Matrices/
> │   ├── 📁 I - Sistemas de ecuaciones y representación/
> │   │   └── 📄 01 - Sistema de ecuaciones lineales en R2 y R3.md
> │   ├── 📁 II - Métodos de resolución/
> │   │   ├── 📄 01 - Algoritmo de Gauss.md
> │   │   └── 📄 02 - Formas Escalonadas y Matriz Escalonada.md
> │   ├── 📁 III - Rango y teoremas fundamentales/
> │   │   ├── 📄 01 - Rango de una Matriz.md
> │   │   ├── 📄 02 - Teorema de Rouché-Frobenius.md
> │   │   └── 📄 03 - Matriz asociada a un S.E.L. y sistema aumentado.md
> │   └── 📁 IV - Estructura de soluciones/
> │       └── 📄 01 - Dimensión y descripción del conjunto solución.md
> │
> ├── 📁 Unidad 2 - Espacios Vectoriales y Transformaciones Lineales/
> │   ├── 📁 I - Fundamentos de Espacios Vectoriales/
> │   │   ├── 📄 01 - Vectores en espacios vectoriales (definición y ejemplos).md
> │   │   ├── 📄 02 - Espacio Vectorial.md
> │   │   ├── 📄 03 - Operaciones en un espacio vectorial (conmutatividad, etc.).md
> │   │   ├── 📄 04 - Lema de Cancelación.md
> │   │   ├── 📄 05 - Teoremas fundamentales del espacio vectorial.md
> │   │   └── 📄 06 - Operaciones No Convencionales.md
> │   ├── 📁 II - Subespacios y Generación/
> │   │   ├── 📄 01 - Subespacios Vectoriales.md
> │   │   ├── 📄 02 - Combinación lineal.md
> │   │   ├── 📄 03 - Espacio generado por un conjunto de vectores.md
> │   │   ├── 📄 04 - Suma de subespacios.md
> │   │   ├── 📄 05 - Espacio columna.md
> │   │   └── 📄 06 - Espacio fila.md
> │   ├── 📁 III - Dependencia, Base y Coordenadas/
> │   │   ├── 📄 01 - Dependencia e independencia lineal.md
> │   │   ├── 📄 02 - Base y dimensión.md
> │   │   ├── 📄 03 - Coordenadas en un espacio vectorial.md
> │   │   └── 📄 04 - Matriz de cambio de base.md
> │   └── 📁 IV - Transformaciones Lineales/
> │       ├── 📄 01 - Transformaciones lineales.md
> │       ├── 📄 02 - Núcleo e imagen de una transformación lineal.md
> │       ├── 📄 03 - Inyectividad y Sobreyectividad.md
> │       ├── 📄 04 - Biyectividad e isomorfismo.md
> │       ├── 📄 05 - Espacios isomorfos.md
> │       ├── 📄 06 - Inversa de una transformación lineal.md
> │       ├── 📄 07 - Matriz de una Transformación Lineal.md
> │       └── 📄 08 - Teorema de la dimensión (Rango-Nulidad).md
> │
> ├── 📁 Unidad 3 - Espacios con Producto Interno/
> │   └── 📁 V - Espacios con Producto Interno/
> │       ├── 📄 01 - Producto interno.md
> │       ├── 📄 02 - Norma inducida y distancia.md
> │       ├── 📄 03 - Ortogonalidad y conjuntos ortonormales.md
> │       ├── 📄 04 - Proyección ortogonal.md
> │       ├── 📄 05 - Proceso de Gram-Schmidt.md
> │       ├── 📄 06 - Complemento ortogonal.md
> │       ├── 📄 07 - Teorema de la Descomposición Ortogonal.md
> │       ├── 📄 08 - Desigualdad de Cauchy-Schwarz.md
> │       └── 📄 09 - Proyección ortogonal sobre un subespacio.md
> │
> └── 📁 Unidad 4 - Valores y Vectores Propios/
>     └── 📁 VI - Valores y Vectores Propios/
>         ├── 📄 01 - Valores y Vectores propios.md
>         ├── 📄 02 - Polinomio Característico.md
>         ├── 📄 03 - Espacio propio y multiplicidades (MA y MG).md
>         ├── 📄 05 - Matriz semejante.md
>         ├── 📄 06 - Matriz diagonalizable.md
>         ├── 📄 07 - Matriz ortogonal.md
>         └── 📄 08 - Teorema espectral.md
> ```

---

**Tags:** #algebra #lineal #ESPOL #MATG1049 #matematicas #matrices #vectores #semester2
