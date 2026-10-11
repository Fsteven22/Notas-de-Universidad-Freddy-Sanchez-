---
dg-publish: true
---

# 🗂️ Índice Unidad 4 — Matrices y Sistemas

## 🎯 Introducción

> [!info] 💡 Qué cubre esta unidad
>
> Esta unidad construye el álgebra matricial desde cero: qué es una matriz y sus clases, cómo operar con ellas, determinantes, sistemas lineales (Gauss, Rouché-Frobenius), matriz inversa y rango. La segunda parte extiende a sistemas no lineales y a inecuaciones lineales y no lineales con región factible y optimización.
>
> Ruta sugerida: Parte I en orden (01 → 07) y luego Parte II (01 → 03). Cada nota tiene metas de aprendizaje, resumen ejecutivo y resumen visual.

```mermaid
graph TD
  U4[Unidad 4 - Matrices y Sistemas] --> PI[Parte I - Lineales]
  U4 --> PII[Parte II - Avanzados]
  PI --> N01[01 - Definicion y clases]
  PI --> N02[02 - Operaciones]
  PI --> N03[03 - Relevantes]
  PI --> N04[04 - Determinantes]
  PI --> N05[05 - Sistemas lineales]
  PI --> N06[06 - Inversa]
  PI --> N07[07 - Rango]
  PII --> M01[01 - No lineales]
  PII --> M02[02 - Inecuaciones lineales]
  PII --> M03[03 - Inecuaciones no lineales]
  N01 --> N02
  N02 --> N04
  N04 --> N06
  N05 --> N07
  N06 --> N07
  N05 --> M01
```

---

## 🗺️ Mapa de la unidad

> [!note] 🗺️ Las 10 notas con enlaces cortos intra-Unidad
>
> |Parte|Nota|Contenido clave|
> |---|---|---|
> |I|[[01 - Definición y clases de matrices]]|Orden, notación, clases por dimensión, elementos y simetría|
> |I|[[02 - Operaciones con matrices]]|Suma, escalar, producto no conmutativo, transposición, potencias|
> |I|[[03 - Matrices relevantes]]|Inversa, rotación, reflexión, proyección, Markov, Vandermonde, Toeplitz|
> |I|[[04 - Determinantes]]|Cálculo 2×2/3×3/Gauss, propiedades, geometría, invertibilidad|
> |I|[[05 - Sistemas de ecuaciones lineales]]|Ax igual a b, Rouché-Frobenius, Gauss y Gauss-Jordan|
> |I|[[06 - Matriz Inversa]]|Definición, propiedades, Gauss-Jordan, adjunta, aplicaciones|
> |I|[[07 - Rango de una Matriz]]|Independencia, escalonada, menores, compatibilidad de sistemas|
> |II|[[01 - Sistemas de ecuaciones no lineales]]|Sustitución, eliminación, cambio de variable, verificación|
> |II|[[02 - Sistemas de inecuaciones lineales]]|Semiplanos, región factible, vértices, programación lineal|
> |II|[[03 - Sistemas de inecuaciones no lineales]]|Fronteras curvas, intersección de regiones, optimización|

---

## ✅ Lista de avance

> [!note] 🎯 Checklist por nota
>
> - [ ] [[01 - Definición y clases de matrices]] — Clasifico cualquier matriz por dimensión, elementos y simetría.
> - [ ] [[02 - Operaciones con matrices]] — Opero matrices respetando compatibilidad y no conmutatividad.
> - [ ] [[03 - Matrices relevantes]] — Reconozco inversa, rotación, proyección, Markov y estructuradas.
> - [ ] [[04 - Determinantes]] — Calculo determinantes y decido invertibilidad.
> - [ ] [[05 - Sistemas de ecuaciones lineales]] — Resuelvo y clasifico sistemas por Gauss y Rouché-Frobenius.
> - [ ] [[06 - Matriz Inversa]] — Invierto matrices 2×2 y n×n y resuelvo ecuaciones matriciales.
> - [ ] [[07 - Rango de una Matriz]] — Hallo rangos y determino compatibilidad de sistemas.
> - [ ] [[01 - Sistemas de ecuaciones no lineales]] — Resuelvo sistemas cuadráticos y verifico soluciones.
> - [ ] [[02 - Sistemas de inecuaciones lineales]] — Grafico regiones factibles y optimizo en vértices.
> - [ ] [[03 - Sistemas de inecuaciones no lineales]] — Resuelvo sistemas con fronteras curvas y optimizo.

---

> [!quote] 🔗 Conexiones
>
> - [[Universidad/Preuniversitario/Matemáticas/Unidad 2 - Números Reales/I - Números Reales/01 - Conjuntos Numéricos]] — elementos y campos de las matrices.
> - [[Universidad/Preuniversitario/Matemáticas/Unidad 2 - Números Reales/I - Números Reales/10 - Ecuaciones]] — base para sistemas lineales y cuadráticos.
> - [[Universidad/Preuniversitario/Matemáticas/Unidad 2 - Números Reales/I - Números Reales/11 - Inecuaciones]] — base de una variable para sistemas de inecuaciones.
> - [[Universidad/Preuniversitario/Matemáticas/Unidad 5 - Geometría/III - Geometría Analítica/02 - Circunferencia]] — fronteras circulares en sistemas no lineales.
> - [[Universidad/Preuniversitario/Matemáticas/Unidad 5 - Geometría/III - Geometría Analítica/03 - Parábola]] — regiones parabólicas.
> - [[Universidad/Preuniversitario/Matemáticas/Unidad 5 - Geometría/III - Geometría Analítica/04 - Elipse]] — regiones elípticas.
> - [[Universidad/Preuniversitario/Matemáticas/Unidad 5 - Geometría/III - Geometría Analítica/05 - Hipérbola]] — ramas hiperbólicas en intersecciones.

---

**Tags:** #matematicas #preuniversitario #unidad4
