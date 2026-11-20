---
dg-publish: true
tags: [MATG1046, unidad1, distancias, distancia-punto-punto, distancia-punto-recta, distancia-punto-plano, distancia-recta-recta, distancia-plano-plano, metrica-euclidiana, producto-vectorial, producto-mixto]
---

# 📏 Distancias en ℝ³

## 🎯 Introducción

> [!info] 💡 Introducción a las Métricas en el Espacio Tridimensional
>
> Las **distancias en ℝ³** son medidas que cuantifican la separación entre diferentes objetos geométricos (puntos, rectas, planos) en el espacio tridimensional. Estas métricas son fundamentales para la geometría analítica y tienen aplicaciones directas en física, ingeniería, computación gráfica y análisis espacial.
>
> **Analogías útiles:**
>
> - **Geografía:** Distancia entre ciudades en un mapa 3D
> - **Física:** Medición de desplazamientos en el espacio
> - **Videojuegos:** Cálculo de colisiones y proximidad entre objetos
> - **Arquitectura:** Medición de separaciones entre estructuras
>
> **Importancia histórica:**
>
> - **Euclides (300 a.C.):** Fundamentos geométricos básicos
> - **Descartes (1637):** Geometría analítica
> - **Gauss (1827):** Geometría diferencial
> - **Minkowski (1908):** Espacios métricos generales
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Distancias_en_R3.svg]]
> **Se lee así:** cuadro raíz «Distancias en ℝ³» con ramas para cada tipo: punto-punto, punto-recta, punto-plano, recta-recta, recta-plano, plano-plano.
> **Por qué importa:** dominar las fórmulas de distancia es esencial para optimización, proximidad, colisiones y análisis espacial en cualquier aplicación de ℝ³.

---

## 📋 Definiciones Formales

### 📊 Tipos de Distancias Fundamentales

> [!note] 🌟 Definición — Clasificación de Distancias en ℝ³
>
> Las distancias en ℝ³ se clasifican según los objetos involucrados:
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Distancias_en_R3.svg]]
> **Se lee así:** tabla con seis tipos de distancia: punto-punto, punto-recta, punto-plano, recta-recta, recta-plano, plano-plano, cada una con su complejidad y aplicación principal.
> **Por qué importa:** identificar el tipo de distancia permite elegir la fórmula correcta inmediatamente.
>
> |Tipo de Distancia|Objetos Involucrados|Complejidad|Aplicación Principal|
> |---|---|---|---|
> |**Punto-Punto**|P₁, P₂|Básica|Navegación, física|
> |**Punto-Recta**|P, L|Media|CAD, robótica|
> |**Punto-Plano**|P, π|Media|Computación gráfica|
> |**Recta-Recta**|L₁, L₂|Alta|Diseño mecánico|
> |**Recta-Plano**|L, π|Media|Arquitectura|
> |**Plano-Plano**|π₁, π₂|Básica|Construcción|
>
> **Características generales de toda métrica:**
>
> - Son **no negativas:** d(A, B) ≥ 0
> - Son **simétricas:** d(A, B) = d(B, A)
> - Cumplen **desigualdad triangular:** d(A, C) ≤ d(A, B) + d(B, C)
> - Son **invariantes** bajo traslaciones y rotaciones

### 📍 Distancia entre Dos Puntos

> [!note] 🔵 Definición — Métrica Euclidiana Punto-Punto
>
> La distancia entre dos puntos P₁(x₁, y₁, z₁) y P₂(x₂, y₂, z₂) en ℝ³ es la longitud del segmento que los une.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Distancias_en_R3.svg]]
> **Se lee así:** diagrama mostrando dos puntos P₁ y P₂ conectados por un segmento, con la fórmula de Pitágoras en 3D extendida.
> **Por qué importa:** es la fórmula base de la que se derivan todas las demás distancias.
>
> **Fórmula:**
>
> $$d(P_1, P_2) = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}$$
>
> **Forma vectorial:**
>
> $$d(P_1, P_2) = |\vec{P_1P_2}| = |\vec{v}|$$
>
> donde $\vec{v} = (x_2-x_1, y_2-y_1, z_2-z_1)$
>
> **Interpretación geométrica:**
>
> - Es la **hipotenusa** de un paralelepípedo rectangular
> - Extiende el **teorema de Pitágoras** a tres dimensiones
> - Es el **camino más corto** entre dos puntos

### 📏 Distancia de un Punto a una Recta

> [!note] 🟢 Definición — Distancia Punto-Recta
>
> La distancia de un punto P a una recta L es la longitud del segmento perpendicular desde P hasta L.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Distancias_en_R3.svg]]
> **Se lee así:** diagrama mostrando un punto P, una recta L, y el segmento perpendicular desde P hasta L con su fórmula.
> **Por qué importa:** la distancia punto-recta se calcula como la altura del paralelogramo formado por dos vectores.
>
> **Ecuación paramétrica de la recta:**
>
> $$L: \vec{r}(t) = \vec{r_0} + t\vec{d}$$
>
> donde:
>
> - $\vec{r_0}$ = punto conocido en la recta
> - $\vec{d}$ = vector director de la recta
> - t = parámetro
>
> **Fórmula de la distancia:**
>
> $$d(P, L) = \frac{|\vec{P_0P} \times \vec{d}|}{|\vec{d}|}$$
>
> donde:
>
> - P₀ es un punto cualquiera de la recta L
> - × denota el producto vectorial
>
> **Método alternativo (proyección):**
>
> $$d(P, L) = |\vec{P_0P}| \sin\theta$$
>
> donde θ es el ángulo entre $\vec{P_0P}$ y $\vec{d}$

### 🛫 Distancia de un Punto a un Plano

> [!note] 🟡 Definición — Distancia Punto-Plano
>
> La distancia de un punto P a un plano π es la longitud del segmento perpendicular desde P hasta π.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Distancias_en_R3.svg]]
> **Se lee así:** diagrama mostrando un punto P, un plano π, y el segmento perpendicular desde P hasta π con la fórmula de sustitución y normalización.
> **Por qué importa:** la distancia punto-plano es la base para cálculo de distancias entre rectas y planos, y para optimización con restricciones.
>
> **Ecuación del plano:**
>
> $$\pi: Ax + By + Cz + D = 0$$
>
> **Fórmula de la distancia:**
>
> $$d(P, \pi) = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}$$
>
> donde P(x₀, y₀, z₀) es el punto.
>
> **Forma vectorial:**
>
> $$d(P, \pi) = \frac{|\vec{n} \cdot \vec{P_0P}|}{|\vec{n}|}$$
>
> donde:
>
> - $\vec{n} = (A, B, C)$ = vector normal al plano
> - P₀ = punto cualquiera del plano
> - $\vec{P_0P}$ = vector desde P₀ hasta P

### ↔️ Distancia entre Dos Rectas

> [!note] 🔵 Definición — Distancia Recta-Recta
>
> La distancia entre dos rectas depende de su posición relativa: secantes (d = 0), paralelas (d > 0 constante) o alabeadas (d > 0, mínimo entre ellas).
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Distancias_en_R3.svg]]
> **Se lee así:** diagrama mostrando los tres casos: rectas secantes (se cortan), paralelas (distancia constante), alabeadas (no coplanares).
> **Por qué importa:** para rectas alabeadas, la distancia se calcula con producto mixto (volumen sobre área base).
>
> **Fórmula general para rectas alabeadas:**
>
> $$d(L_1, L_2) = \frac{|(\vec{P_2} - \vec{P_1}) \cdot (\vec{d_1} \times \vec{d_2})|}{|\vec{d_1} \times \vec{d_2}|}$$
>
> **Interpretación:**
>
> - El numerador es el producto mixto (volumen del paralelepípedo)
> - El denominador es el área del paralelogramo base
> - El resultado es la "altura" del paralelepípedo
>
> **Casos especiales:**
>
> - **Rectas paralelas:** $d(L_1, L_2) = \frac{|\vec{P_1P_2} \times \vec{d_1}|}{|\vec{d_1}|}$
> - **Rectas secantes:** d(L₁, L₂) = 0

### ✈️ Distancia de una Recta a un Plano

> [!note] 🟡 Definición — Distancia Recta-Plano
>
> La distancia de una recta L a un plano π es 0 si se intersectan o están contenidas, y es constante si son paralelas.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Distancias_en_R3.svg]]
> **Se lee así:** diagrama mostrando recta paralela a plano con distancia constante entre ambos.
> **Por qué importa:** si la recta es paralela al plano, la distancia es la misma para cualquier punto de la recta.
>
> **Cuando L ∥ π:**
>
> $$d(L, \pi) = d(P, \pi) = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}$$
>
> donde P(x₀, y₀, z₀) es cualquier punto de L.

### 🏢 Distancia entre Dos Planos

> [!note] 🔵 Definición — Distancia Plano-Plano
>
> La distancia entre dos planos es 0 si se intersectan o coinciden, y es constante si son paralelos.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Distancias_en_R3.svg]]
> **Se lee así:** diagrama mostrando dos planos paralelos con distancia constante entre ellos.
> **Por qué importa:** para planos paralelos, la distancia se calcula con la diferencia de términos independientes normalizada.
>
> **Cuando π₁ ∥ π₂ con normales proporcionales:**
>
> $$d(\pi_1, \pi_2) = \frac{|D_2 - D_1|}{\sqrt{A^2 + B^2 + C^2}}$$
>
> Si π₂: Ax + By + Cz + D₂ = 0 es paralelo a π₁: Ax + By + Cz + D₁ = 0.

---

## 🔧 Ejercicios Propuestos

> [!example] 💪 Clasificación Básica: 🟢
>
> 1. **Distancia básica:**
>
>    Calcular d entre P₁(2, -1, 3) y P₂(5, 3, -1).
>
> > [!success]- ✅ Solución
> >
> > $$d = \sqrt{(5-2)^2 + (3-(-1))^2 + (-1-3)^2} = \sqrt{3^2 + 4^2 + (-4)^2} = \sqrt{9 + 16 + 16} = \sqrt{41} \approx 6.40$$
> >
> > **Lección:** aplicar directamente la fórmula de Pitágoras en 3D.

> [!example] 💪 Clasificación Básica: 🟢
>
> 2. **Punto en eje:**
>
>    Distancia de P(3, 4, 0) al origen.
>
> > [!success]- ✅ Solución
> >
> > $$d = \sqrt{3^2 + 4^2 + 0^2} = \sqrt{9 + 16} = 5$$
> >
> > **Lección:** la distancia al origen es la norma euclidiana del vector posición.

> [!example] 💪 Clasificación Básica: 🟢
>
> 3. **Plano coordenado:**
>
>    Distancia de P(2, -3, 7) al plano XY.
>
> > [!success]- ✅ Solución
> >
> > Plano XY: z = 0, por lo tanto d = |7| = 7 unidades.
> >
> > **Lección:** para planos coordenados, la distancia es el valor absoluto de la coordenada correspondiente.

> [!example] 💪 Intersecciones Intermedias: 🟡
>
> 5. **Punto-Recta:**
>
>    P(1, 2, 3), L: r = (0, 1, 1) + t(1, 0, 1). Calcular d(P, L).
>
> > [!success]- ✅ Solución
> >
> > - P₀(0, 1, 1), $\vec{d} = (1, 0, 1)$
> > - $\vec{P_0P} = (1-0, 2-1, 3-1) = (1, 1, 2)$
> > - $\vec{P_0P} \times \vec{d} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & 2 \\ 1 & 0 & 1 \end{vmatrix} = (1, 1, -1)$
> > - $|\vec{P_0P} \times \vec{d}| = \sqrt{3}$
> > - $|\vec{d}| = \sqrt{2}$
> > - $d = \frac{\sqrt{3}}{\sqrt{2}} = \sqrt{\frac{3}{2}} \approx 1.22$
> >
> > **Lección:** usar producto vectorial para distancia punto-recta.

> [!example] 💪 Intersecciones Intermedias: 🟡
>
> 6. **Punto-Plano:**
>
>    P(2, -1, 4), π: 3x - 2y + z - 5 = 0. Calcular d(P, π).
>
> > [!success]- ✅ Solución
> >
> > $$d = \frac{|3(2) - 2(-1) + 4 - 5|}{\sqrt{3^2 + (-2)^2 + 1^2}} = \frac{|6 + 2 + 4 - 5|}{\sqrt{14}} = \frac{7}{\sqrt{14}} \approx 1.87$$
> >
> > **Lección:** sustituir las coordenadas del punto en la ecuación del plano y normalizar.

> [!example] 💪 Intersecciones Intermedias: 🟡
>
> 7. **Planos paralelos:**
>
>    π₁: 2x + y - 2z + 3 = 0, π₂: 2x + y - 2z - 6 = 0.
>
> > [!success]- ✅ Solución
> >
> > $$d = \frac{|(-6) - 3|}{\sqrt{2^2 + 1^2 + (-2)^2}} = \frac{9}{\sqrt{9}} = 3$$
> >
> > **Lección:** para planos paralelos con la misma normal, usar la diferencia de términos independientes.

> [!example] 💪 Intersecciones Intermedias: 🟡
>
> 8. **Verificación:**
>
>    ¿El punto P(1, 2, -1) está en el plano x + y + z - 2 = 0?
>
> > [!success]- ✅ Solución
> >
> > $$d = \frac{|1 + 2 + (-1) - 2|}{\sqrt{3}} = \frac{0}{\sqrt{3}} = 0$$
> >
> > Sí, el punto está en el plano (d = 0).
> >
> > **Lección:** si d(P, π) = 0, el punto pertenece al plano.

> [!example] 💪 Ángulos Avanzados: 🔴
>
> 9. **Rectas alabeadas:**
>
>    L₁: r = (1, 0, 1) + s(1, 1, 0), L₂: r = (0, 1, 0) + t(0, 1, 1). Calcular d(L₁, L₂).
>
> > [!success]- ✅ Solución
> >
> > - $\vec{P_1} = (1, 0, 1)$, $\vec{d_1} = (1, 1, 0)$
> > - $\vec{P_2} = (0, 1, 0)$, $\vec{d_2} = (0, 1, 1)$
> > - $\vec{P_1P_2} = (-1, 1, -1)$
> > - $\vec{d_1} \times \vec{d_2} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{vmatrix} = (1, -1, 1)$
> > - Producto mixto: $(-1)(1) + (1)(-1) + (-1)(1) = -1 - 1 - 1 = -3$
> > - $|\vec{d_1} \times \vec{d_2}| = \sqrt{3}$
> > - $d = \frac{|-3|}{\sqrt{3}} = \sqrt{3} \approx 1.73$
> >
> > **Lección:** producto mixto sobre área base para rectas alabeadas.

> [!example] 💪 Construcción Avanzada: 🔴
>
> 10. **Problema aplicado:**
>
>     Un dron vuela en trayectoria L: (0,0,50) + t(10,0,0) m. Torre de comunicaciones: eje z (recta x=5, y=0). ¿Distancia mínima?
>
> > [!success]- ✅ Solución
> >
> > - L₁ (dron): P₁(0, 0, 50), $\vec{d_1} = (10, 0, 0)$
> > - L₂ (torre): P₂(5, 0, 0), $\vec{d_2} = (0, 0, 1)$
> > - $\vec{P_1P_2} = (5, 0, -50)$
> > - $\vec{d_1} \times \vec{d_2} = (0, -10, 0)$
> > - Producto mixto: $(5)(0) + (0)(-10) + (-50)(0) = 0$
> > - $d = \frac{0}{10} = 0$
> >
> > **Resultado:** Las rectas se intersectan (el dron pasa sobre la torre en algún momento).
> >
> > **Lección:** producto mixto = 0 indica que las rectas son coplanares (secantes o paralelas).

> [!example] 💪 Optimización: 🔴
>
> 11. **Punto más cercano en un plano:**
>
>     Encontrar el punto en el plano 2x + y + 2z = 9 más cercano a P(1, 1, 1).
>
> > [!success]- ✅ Solución
> >
> > El punto más cercano está en la perpendicular al plano que pasa por P.
> > - Vector normal: $\vec{n} = (2, 1, 2)$
> > - Recta perpendicular por P: $(x, y, z) = (1, 1, 1) + t(2, 1, 2)$
> > - Sustituir en el plano: $2(1+2t) + (1+t) + 2(1+2t) = 9$
> > - $2 + 4t + 1 + t + 2 + 4t = 9$
> > - $5 + 9t = 9$
> > - $t = \frac{4}{9}$
> > - Punto: $(1 + \frac{8}{9}, 1 + \frac{4}{9}, 1 + \frac{8}{9}) = (\frac{17}{9}, \frac{13}{9}, \frac{17}{9})$
> >
> > **Lección:** el punto más cercano a un plano está en su perpendicular.

---

## 🎓 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Calculo la distancia entre dos puntos en ℝ³ usando Pitágoras en 3D.
> - [ ] Identifico el tipo de distancia (punto-punto, punto-recta, punto-plano, etc.) según los objetos.
> - [ ] Aplico la fórmula de distancia punto-plano directamente.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo la distancia de un punto a una recta usando producto vectorial.
> - [ ] Calculo la distancia entre dos rectas alabeadas usando producto mixto.
> - [ ] Distingo si dos rectas son paralelas, secantes o alabeadas.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo problemas de optimización: punto más cercano en un plano o recta.
> - [ ] Aplico fórmulas de distancia en contextos de computación gráfica y física.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Calculus*, cap. 12 «Vectors and the Geometry of Space»: fórmulas de distancia en ℝ³.
> - Syllabus oficial MATG1046 «Cálculo Vectorial», ESPOL — Unidad 1 (Geometría Analítica en ℝ³).
> - Apuntes del curso MATG1046 y las figuras de la propia materia (`Unidad 0 - Guias y Ejercicios/Diagramas/`).

---

## 🔁 Repaso SR

#flashcards/calcvec-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Fórmula distancia punto-punto?::$\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}$ (Pitágoras en 3D).
> - ¿Fórmula distancia punto-recta?::$\frac{|\vec{P_0P} \times \vec{d}|}{|\vec{d}|}$ (altura del paralelogramo).
> - ¿Fórmula distancia punto-plano?::$\frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}}$ (sustituir y normalizar).
> - ¿Fórmula distancia entre rectas alabeadas?::$\frac{|(\vec{P_2}-\vec{P_1})\cdot(\vec{d_1}\times\vec{d_2})|}{|\vec{d_1}\times\vec{d_2}|}$ (producto mixto sobre área).
> - ¿Cuándo dos rectas tienen distancia 0?::Cuando son secantes o coincidentes (se intersectan).
> - ¿Cómo se calcula distancia punto-plano si d = 0?::El punto pertenece al plano.

---

## 🔗 Conexiones con el Sistema de Notas

> [!quote] 🌐 Enlaces Conceptuales
>
> **Prerrequisitos (Prerequisites):**
>
> - [[02 - Vectores en R3]] - Operaciones vectoriales fundamentales
> - [[01 - Rectas en R3]] - Formas paramétricas y simétricas
> - [[02 - Planos en R3]] - Forma general y normal
> - Producto Escalar - Proyecciones y ángulos
> - Producto Vectorial - Distancia punto-recta y recta-recta
>
> **Temas siguientes:**
>
> - Optimización en ℝ³ - Minimización de distancias
> - 07.1 Distancia Punto-Plano - Aplicaciones avanzadas
> - Proyecciones en R3 - Relacionado con distancias perpendiculares
>
> **Conceptos relacionados:**
>
> - Métricas en ℝ³ - Euclidiana, Manhattan, Chebyshev
> - Inecuación triangular - Propiedad fundamental de toda distancia
> - Invariancia bajo traslaciones y rotaciones

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Dominar las 6 fórmulas de distancia antes de pasar a optimización con restricciones.
> - Siguiente: aplicar distancias en problemas de computación gráfica y física.
> - Repaso: siempre verificar si d = 0 (pertenencia o intersección) antes de calcular.

**Tags:** #MATG1046 #unidad1 #distancias #distancia-punto-punto #distancia-punto-recta #distancia-punto-plano #distancia-recta-recta #distancia-plano-plano #metrica-euclidiana #producto-vectorial #producto-mixto #calculo-vectorial #geometria-3d
