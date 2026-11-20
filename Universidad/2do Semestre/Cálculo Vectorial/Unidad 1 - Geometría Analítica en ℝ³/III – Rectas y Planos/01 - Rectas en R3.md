---
dg-publish: true
tags: [MATG1046, unidad1, rectas, rectas-en-R3, vector-director, ecuaciones-parametricas, ecuaciones-simetricas, ecuaciones-vectoriales]
---

# 📐 Rectas en ℝ³

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Importa la Recta en el Espacio?
>
> En ℝ² dos rectas solo pueden ser paralelas o cortarse. En ℝ³ aparece una tercera posibilidad que no existe en el plano: **rectas alabeadas** (no se cortan y tampoco son paralelas). Una recta del espacio queda definida por un punto y una dirección, y de esa idea salen todas sus ecuaciones.
>
> **¿Dónde se usa?**
>
> - **Trayectorias:** la luz viaja en línea recta; un rayo es una recta con dirección.
> - **Ingeniería:** el eje de una viga, una vía de tren, un cable tenso.
> - **Computación gráfica:** rayos de cámara, intersecciones y colisiones.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Rectas_en_R3.svg]]
>
> **Se lee así:** el cuadro raíz «Recta en ℝ³» abre cuatro ramas: **punto P₀**, **vector director v**, la definición conjuntista `L = {P₀ + tv : t ∈ ℝ}` y la condición **v ≠ 0**. Basta un punto P₀ y una dirección v no nula para determinar la recta entera.
>
> **Por qué importa:** sin esos dos ingredientes, cualquier ecuación de recta pierde sentido geométrico; el vector nulo no define dirección, y sin punto la recta flota sin ubicación.

---

## 📋 Definiciones Formales

### 1️⃣ Recta en ℝ³ — puntos colineales

> [!note] 📋 Definición — Recta en ℝ³
>
> Una **recta L** en ℝ³ es el conjunto infinito de puntos que se obtienen al desplazar un punto fijo P₀ a lo largo de una dirección **v** ≠ **0**:
>
> $$L = \{ P_0 + t\mathbf{v} : t \in \mathbb{R} \}$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Rectas_en_R3_01.svg]]
>
> **Se lee así:** el diagrama muestra P₀ como ancla y **v** como flecha de dirección; variando t ∈ ℝ se recorre la recta en ambos sentidos.
>
> **Ejemplo:** con P₀(1, 2, 3) y **v**(2, 1, 0), la recta es L = {(1+2t, 2+t, 3) : t ∈ ℝ}.

### 2️⃣ Ecuación vectorial — la forma compacta

> [!note] 📋 Definición — Ecuación Vectorial
>
> Dado un punto P₀(x₀, y₀, z₀) y un vector director **v** = (a, b, c), la recta se escribe:
>
> $$\mathbf{r}(t) = P_0 + t\mathbf{v} = (x_0, y_0, z_0) + t(a, b, c)$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Ecuacion_de_recta_en_R3_01.svg]]
>
> **Se lee así:** el diagrama conecta la forma vectorial con las paramétricas y simétricas: un mismo objeto con tres escrituras.
>
> **Ejemplo:** r(t) = (1, 0, 2) + t(3, 1, 4).

### 3️⃣ Ecuaciones paramétricas — una por coordenada

> [!note] 📋 Definición — Ecuaciones Paramétricas
>
> Desarrollando la ecuación vectorial componente a componente:
>
> $$\begin{cases} x = x_0 + at \\ y = y_0 + bt \\ z = z_0 + ct \end{cases}, \quad t \in \mathbb{R}$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Ecuacion_parametrica_01.svg]]
>
> **Se lee así:** el cuadro raíz «Ecuaciones paramétricas» muestra la fórmula (tres ecuaciones lineales en t) y un ejemplo con P₀ = (1,2,3), v = (2,1,0).
>
> **Ejemplo:** la recta por (1, 2, 3) con dirección (2, 1, 0): x = 1+2t, y = 2+t, z = 3.

### 4️⃣ Ecuaciones simétricas — sin parámetro

> [!note] 📋 Definición — Ecuaciones Simétricas
>
> Si a, b, c ≠ 0, despejando t de cada ecuación paramétrica e igualando:
>
> $$\frac{x - x_0}{a} = \frac{y - y_0}{b} = \frac{z - z_0}{c}$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Ecuacion_simetrica_01.svg]]
>
> **Se lee así:** el cuadro raíz «Ecuación simétrica» muestra la fórmula igualada y la nota de que no aparece el parámetro t.
>
> **Ejemplo:** r(t) = (1, 0, 2) + t(3, 1, 4) → (x−1)/3 = y = (z−2)/4.

### 5️⃣ Paralelismo y perpendicularidad — dos atajos

> [!note] 📋 Definición — Paralelismo y Perpendicularidad
>
> Dos rectas L₁, L₂ con directores **v₁**, **v₂** cumplen:
>
> - **Paralelas:** v₁ = k·v₂ (directores proporcionales).
> - **Perpendiculares:** v₁ · v₂ = 0 (producto punto nulo).
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Paralelismo_01.svg]]
>
> **Se lee así:** el cuadro raíz «Paralelismo en el espacio» da la regla L₁ ∥ L₂ ⟺ v₁ = k·v₂, separando el signo de k (mismo sentido / opuesto).
>
> **Ejemplo:** v₁ = (2,3,1) y v₂ = (4,6,2) = 2v₁ → paralelas.

### 6️⃣ Clasificación de rectas — el caso nuevo de ℝ³

> [!note] 📋 Definición — Rectas Secantes y Alabeadas
>
> - **Secantes:** se cortan en un único punto (resolver el sistema P₁+t·v₁ = P₂+s·v₂).
> - **Alabeadas:** no son paralelas y no se cortan (solo ocurre en ℝ³ o más dimensiones).
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Alabeadas_01.svg]]
>
> **Se lee así:** el cuadro raíz «Rectas alabeadas» da las dos condiciones (NO paralelas Y NO se intersectan) y la nota de que solo existen en ℝ³.
>
> **Ejemplo:** L₁: (1,0,1)+t(1,0,1) y L₂: (0,1,0)+t(0,1,1): no paralelas y su sistema es contradictorio → alabeadas.

### 7️⃣ Ángulo entre rectas — siempre agudo

> [!note] 📋 Definición — Ángulo entre Rectas
>
> El ángulo θ entre L₁ y L₂ es el ángulo entre sus directores, tomado en [0°, 90°]:
>
> $$\cos\theta = \frac{|\mathbf{v}_1 \cdot \mathbf{v}_2|}{||\mathbf{v}_1||\,||\mathbf{v}_2||}$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Angulo_rectas_01.svg]]
>
> **Se lee así:** el cuadro raíz «Ángulo entre rectas» da la fórmula con valor absoluto y los casos (0° paralelas, 90° perpendiculares).
>
> **Ejemplo:** v₁ = (1,0,0), v₂ = (1,1,0) → cos θ = 1/√2 → θ = 45°.

---

## 🛠️ Tabla Resumen de Formas

> [!note] 📋 Las Tres Escrituras de una Recta
>
> | Forma | Ecuación | Ventaja | Cuidado |
> |---|---|---|---|
> | **Vectorial** | **r**(t) = **P₀** + t**v** | Compacta y geométrica | — |
> | **Paramétrica** | x = x₀+at, y = y₀+bt, z = z₀+ct | Fácil de programar | Tres ecuaciones |
> | **Simétrica** | (x−x₀)/a = (y−y₀)/b = (z−z₀)/c | Sin parámetro | Falla si a, b o c = 0 |
>
> **Conversión:** Vectorial ↔ Paramétrica es directa; Paramétrica → Simétrica despejando t; Simétrica → Paramétrica igualando a t.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Tres formas de la misma recta

> [!example] 📋 Planteamiento
>
> Escribe la recta por A(1, 0, 2) con director **v** = (2, −1, 3) en forma vectorial, paramétrica y simétrica.
>
> > [!success]- ✅ Solución
> >
> > Vectorial: r(t) = (1, 0, 2) + t(2, −1, 3).
> >
> > Paramétrica: x = 1 + 2t, y = −t, z = 2 + 3t.
> >
> > Simétrica: (x − 1)/2 = y/(−1) = (z − 2)/3.

### ✏️ Ejercicio 2 — Paralelas o no

> [!example] 📋 Planteamiento
>
> Determina si L₁: (x−1)/3 = (y+2)/2 = (z−4)/1 y L₂: x = 2+6t, y = 1+4t, z = −1+2t son paralelas o perpendiculares.
>
> > [!success]- ✅ Solución
> >
> > v₁ = (3, 2, 1); v₂ = (6, 4, 2) = 2v₁ → **paralelas**.
> >
> > Producto punto v₁·v₂ = 18 + 8 + 2 = 28 ≠ 0 → no perpendiculares.

### ✏️ Ejercicio 3 — Ángulo entre rectas

> [!example] 📋 Planteamiento
>
> Calcula el ángulo entre L₁: **v₁** = (1, 1, 0) y L₂: **v₂** = (0, 1, 1).
>
> > [!success]- ✅ Solución
> >
> > v₁·v₂ = 1; ||v₁|| = ||v₂|| = √2.
> >
> > cos θ = 1/(√2·√2) = 1/2 → θ = **60°**.

### ✏️ Ejercicio 4 — Clasificación completa

> [!example] 📋 Planteamiento
>
> Clasifica L₁: x = 1+2t, y = 3−t, z = 2+t y L₂: x = 2+s, y = 1+2s, z = 4−s.
>
> > [!success]- ✅ Solución
> >
> > v₁ = (2, −1, 1), v₂ = (1, 2, −1): no proporcionales → no paralelas.
> >
> > Sistema: de (3) s = 2−t; en (1) 2t − (2−t) = 1 → t = 1, s = 1; en (2) −1 − 2 = −3 ≠ −2 → contradicción.
> >
> > **Alabeadas.** El ángulo: cos θ = |−1|/6 → θ ≈ 80.4°.

---

## 🎓 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo las tres formas de una recta (vectorial, paramétrica, simétrica).
> - [ ] Ubico puntos de la recta sustituyendo t.
> - [ ] Identifico punto base y vector director en cualquier ecuacón.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Decido si dos rectas son paralelas, perpendiculares, secantes o alabeadas.
> - [ ] Calculo el ángulo entre rectas con el valor absoluto del producto punto.
> - [ ] Construyo la recta por dos puntos.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo sistemas 3×3 para hallar intersecciones y clasificar rectas.
> - [ ] Manejo los casos de componentes nulas en la forma simétrica.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - J. Stewart, *Calculus*, cap. 12 «Vectors and the Geometry of Space»: ecuaciones de rectas.
> - Syllabus oficial MATG1046 «Cálculo Vectorial», ESPOL — Unidad 1 (Geometría Analítica en ℝ³).
> - Apuntes del curso MATG1046 y las figuras de la materia (`Unidad 0 - Guias y Ejercicios/Diagramas/`).

---

## 🔁 Repaso SR

#flashcards/calcvec-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Ecuación vectorial de una recta?::r(t) = P₀ + t·v, con P₀ punto y v director ≠ 0.
> - ¿Ecuaciones simétricas?::(x−x₀)/a = (y−y₀)/b = (z−z₀)/c, sin el parámetro t.
> - ¿Cuándo dos rectas son paralelas?::Cuando v₁ = k·v₂ (directores proporcionales).
> - ¿Cuándo son perpendiculares?::Cuando v₁·v₂ = 0.
> - ¿Qué son rectas alabeadas?::No paralelas y sin intersección; solo en ℝ³.
> - ¿Fórmula del ángulo entre rectas?::cos θ = |v₁·v₂|/(||v₁||·||v₂||), θ en [0°,90°].

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[01 - Sistema de referencia espacial en R3]] — puntos y coordenadas en ℝ³.
> - [[02 - Vectores en R3]] — vector director y operaciones.
> - [[01 – Producto punto y ángulos]] — perpendicularidad y ángulos.
> - [[02 – Producto cruz y áreas]] — vectores normales para planos.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Cálculo Vectorial]]
> - Siguiente: [[02 - Planos en R3]] — la recta gana una dimensión.
> - Relacionado: [[02 - Relación recta–plano]] — posiciones relativas recta-plano.

---

**Tags:** #MATG1046 #unidad1 #rectas #rectas-en-R3 #vector-director #ecuaciones-parametricas #ecuaciones-simetricas #cálculo-vectorial
