---
dg-publish: true
tags: [MATG1046, unidad1, recta-plano, relacion-recta-plano, interseccion-recta-plano, perpendicularidad-recta-plano, paralelismo-recta-plano, angulo-recta-plano]
---

# 🔷 Relación Recta-Plano en ℝ³

## 🎯 Introducción

> [!info] 💡 Introducción a las Interacciones Recta-Plano
>
> La **relación entre rectas y planos** es fundamental en geometría analítica espacial. Estudia cómo una recta puede posicionarse respecto a un plano en el espacio tridimensional.
>
> **Analogías útiles:**
>
> - **Física:** Rayo de luz incidiendo en una superficie
> - **Arquitectura:** Viga atravesando una pared o apoyada en ella
> - **Navegación:** Trayectoria de avión respecto al suelo
>
> **Importancia práctica:**
>
> - **Computación Gráfica:** Ray tracing y detección de colisiones
> - **Ingeniería:** Análisis de intersecciones estructurales
> - **Física:** Trayectorias de partículas y superficies
> - **Robótica:** Planificación de movimientos
>
> **Conceptos clave:**
>
> - Una recta puede estar **contenida** en un plano
> - Una recta puede **intersectar** un plano en un punto
> - Una recta puede ser **paralela** a un plano (sin tocarlo)
> - Una recta puede ser **perpendicular** a un plano
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Relación_recta–plano.svg]]
> **Se lee así:** cuadro raíz «Relación recta-plano» con cuatro ramas: **Contenida**, **Secante**, **Paralela** y **Perpendicular**, cada una con su condición algebraica y geométrica.
> **Por qué importa:** identificar la relación recta-plano es el primer paso para calcular distancias, ángulos y puntos de intersección en el espacio.

---

## 📋 Definiciones Formales

### 📐 Clasificación de Posiciones

> [!note] 🌟 Definición — Tipos de Relaciones Posibles
>
> Una recta L y un plano π pueden relacionarse de cuatro formas según el vector director **v** de la recta y el vector normal **n** del plano:
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Relación_recta–plano.svg]]
> **Se lee así:** tabla con cuatro filas: **Contenida** (**v**⊥**n** y P₀∈π), **Secante** (**v**∦**n**), **Paralela** (**v**⊥**n** y P₀∉π), **Perpendicular** (**v**∥**n**).
> **Por qué importa:** la condición algebraica **v**·**n** permite clasificar la relación sin necesidad de dibujar.
>
> |Relación|Condición algebraica|Puntos en común|Condición geométrica|
> |---|---|---|---|
> |**Contenida**|**v**·**n** = 0 y P₀ ∈ π|Infinitos|Recta dentro del plano|
> |**Secante**|**v**·**n** ≠ 0|Exactamente 1|Se intersectan en un punto|
> |**Paralela**|**v**·**n** = 0 y P₀ ∉ π|Ninguno|No se tocan|
> |**Perpendicular**|**v** = k**n**|Exactamente 1|Intersección a 90°|
>
> Donde:
>
> - **v**: vector director de la recta
> - **n**: vector normal al plano
> - P₀: punto en la recta
> - π: plano
>
> **Nota importante:** La perpendicularidad es un caso especial de secante.

### ⊥ Recta Perpendicular al Plano

> [!note] 🟢 Definición — Recta Perpendicular al Plano
>
> Una recta L es **perpendicular** a un plano π si su vector director es paralelo al vector normal del plano.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Relación_recta–plano.svg]]
> **Se lee así:** cuadro raíz «Recta perpendicular» con rama «v = k·n» mostrando que el vector director es múltiplo del normal.
>
> **Condición matemática:**
>
> $$\mathbf{v} = k\mathbf{n} \quad \text{para algún } k \in \mathbb{R}, k \neq 0$$
>
> O equivalentemente: $$\mathbf{v} \parallel \mathbf{n}$$
>
> **Propiedades:**
>
> - La recta es perpendicular a **toda** recta contenida en el plano
> - Forma el ángulo de 90° con el plano
> - Es la dirección de máximo cambio respecto al plano
> - Única dirección perpendicular desde un punto dado
>
> **Interpretación geométrica:**
>
> - Como una estaca clavada perpendicularmente en el suelo
> - Como la dirección de un rayo de luz perpendicular a un espejo
> - Como la normal a una superficie en un punto

### ∥ Recta Paralela al Plano

> [!note] 🟡 Definición — Recta Paralela al Plano
>
> Una recta L es **paralela** a un plano π si su vector director es perpendicular al vector normal del plano y la recta no está contenida en el plano.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Relación_recta–plano.svg]]
> **Se lee así:** cuadro raíz «Recta paralela» con rama «v·n = 0, P₀∉π» mostrando director perpendicular a normal y punto fuera del plano.
>
> **Condiciones necesarias:**
>
> 1. **v** · **n** = 0 (director perpendicular a normal)
> 2. P₀ ∉ π (punto de la recta no está en el plano)
>
> **Propiedades:**
>
> - La recta y el plano no tienen puntos en común
> - La distancia entre la recta y el plano es constante
> - La recta es paralela a infinitas rectas del plano
> - Existe un único plano paralelo que contiene la recta
>
> **Distinción importante:**
>
> - **Paralela distinta:** No se tocan (recta fuera del plano)
> - **Contenida:** Infinitos puntos comunes (recta en el plano)
> - Ambas cumplen **v** ⊥ **n**, la diferencia está en si P₀ ∈ π

### ∩ Intersección Recta-Plano

> [!note] 🔵 Definición — Punto de Intersección
>
> Cuando una recta es **secante** a un plano, se intersectan en exactamente un punto.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Relación_recta–plano.svg]]
> **Se lee así:** cuadro raíz «Intersección recta-plano» con rama «v·n ≠ 0» y «t = -(n·r₀+D)/(n·v)» mostrando el procedimiento de cálculo.
>
> **Condición:** **v** · **n** ≠ 0
>
> **Método para encontrar el punto de intersección:**
>
> **Dados:**
>
> - Recta L: (x,y,z) = (x₀,y₀,z₀) + t(a,b,c)
> - Plano π: Ax + By + Cz + D = 0
>
> **Procedimiento:**
>
> **Paso 1:** Sustituir las ecuaciones paramétricas de la recta en la ecuación del plano
>
> $$A(x_0 + at) + B(y_0 + bt) + C(z_0 + ct) + D = 0$$
>
> **Paso 2:** Resolver para t
>
> $$\begin{align} t(Aa + Bb + Cc) &= -(Ax_0 + By_0 + Cz_0 + D) \\ t &= -\frac{Ax_0 + By_0 + Cz_0 + D}{Aa + Bb + Cc} \end{align}$$
>
> **Nota:** El denominador es **v** · **n**, que es ≠ 0 para rectas secantes
>
> **Paso 3:** Sustituir t en las ecuaciones de la recta
>
> $$\begin{cases} x = x_0 + at \\ y = y_0 + bt \\ z = z_0 + ct \end{cases}$$
>
> **Fórmula compacta:**
>
> $$t = -\frac{\mathbf{n} \cdot \mathbf{r}_0 + D}{\mathbf{n} \cdot \mathbf{v}}$$
>
> Donde **r₀** = (x₀,y₀,z₀)

### 📐 Ángulo entre Recta y Plano

> [!note] 📊 Definición — Ángulo Recta-Plano
>
> El ángulo θ entre una recta L y un plano π es el **complemento** del ángulo entre el vector director de la recta y el vector normal al plano.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Relación_recta–plano.svg]]
> **Se lee así:** cuadro raíz «Ángulo recta-plano» con rama «sin θ = |v·n|/(||v||·||n||)» y «θ = 90° - α».
>
> **Interpretación geométrica:**
>
> - Es el menor ángulo entre la recta y cualquier recta del plano
> - Es el ángulo entre la recta y su proyección sobre el plano
> - Rango: 0° ≤ θ ≤ 90°
>
> **Relación fundamental:** Si α es el ángulo entre **v** y **n**, entonces:
>
> $$\theta = 90° - \alpha$$
>
> O equivalentemente:
>
> $$\sin \theta = \cos \alpha = \frac{|\mathbf{v} \cdot \mathbf{n}|}{||\mathbf{v}|| \cdot ||\mathbf{n}||}$$
>
> **Casos especiales:**
>
> - θ = 0° → Recta paralela o contenida en el plano
> - θ = 90° → Recta perpendicular al plano
> - 0° < θ < 90° → Recta secante oblicua

---

## 🔧 Ejercicios Propuestos

> [!example] 💪 Clasificación Básica: 🟢
>
> 1. Clasificar la relación entre:
>
>    - L: (x,y,z) = (1,0,2) + t(1,1,0)
>    - π: x + y = 5
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Identificar vectores
> > - **v** = (1, 1, 0)
> > - **n** = (1, 1, 0) (de x + y - 5 = 0)
> > - P₀(1, 0, 2)
> >
> > **Paso 2:** Producto punto
> > $$\mathbf{v} \cdot \mathbf{n} = (1)(1) + (1)(1) + (0)(0) = 2 \neq 0$$
> >
> > **Conclusión:** Como **v**·**n** ≠ 0, la recta es **secante** al plano.
> >
> > **Lección:** si el producto punto director-normal no es cero, la recta corta al plano.

> [!example] 💪 Clasificación Básica: 🟢
>
> 2. Determinar si la recta L: (x,y,z) = (2,1,3) + s(1,2,1) es paralela a π: x + 2y + z = 7
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Identificar elementos
> > - **v** = (1, 2, 1)
> > - **n** = (1, 2, 1)
> > - P₀(2, 1, 3)
> >
> > **Paso 2:** Producto punto
> > $$\mathbf{v} \cdot \mathbf{n} = (1)(1) + (2)(2) + (1)(1) = 1 + 4 + 1 = 6 \neq 0$$
> >
> > **Conclusión:** NO es paralela (es secante), porque **v**·**n** ≠ 0.
> >
> > **Lección:** paralelismo requiere **v**·**n** = 0.

> [!example] 💪 Clasificación Básica: 🟢
>
> 3. Verificar si L: x/2 = y/1 = z/(-3) es perpendicular a π: 4x + 2y - 6z = 10
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Identificar vectores
> > - **v** = (2, 1, -3) (de las ecuaciones simétricas)
> > - **n** = (4, 2, -6) = 2(2, 1, -3)
> >
> > **Paso 2:** Verificar si **v** ∥ **n**
> > $$\mathbf{n} = 2\mathbf{v} \Rightarrow \mathbf{v} \parallel \mathbf{n}$$
> >
> > **Conclusión:** Sí, la recta es **perpendicular** al plano.
> >
> > **Lección:** perpendicularidad requiere **v** = k**n** (vectores proporcionales).

> [!example] 💪 Intersecciones Intermedias: 🟡
>
> 6. Hallar el punto de intersección entre:
>
>    - L: (x,y,z) = (1,2,0) + t(1,-1,2)
>    - π: x + y + z = 6
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Verificar secancia
> > - **v** = (1, -1, 2)
> > - **n** = (1, 1, 1)
> > - **v**·**n** = 1 - 1 + 2 = 2 ≠ 0 ✓
> >
> > **Paso 2:** Sustituir en el plano
> > $$(1+t) + (2-t) + (0+2t) = 6$$
> > $$3 + 2t = 6$$
> > $$2t = 3$$
> > $$t = \frac{3}{2}$$
> >
> > **Paso 3:** Punto de intersección
> > $$\begin{align} x &= 1 + \frac{3}{2} = \frac{5}{2} \\ y &= 2 - \frac{3}{2} = \frac{1}{2} \\ z &= 0 + 2 \cdot \frac{3}{2} = 3 \end{align}$$
> >
> > **Respuesta:** P = $\left(\frac{5}{2}, \frac{1}{2}, 3\right)$
> >
> > **Lección:** sustituir la recta en el plano y despejar t da el punto de corte.

> [!example] 💪 Intersecciones Intermedias: 🟡
>
> 7. Encontrar donde L: (x-1)/2 = (y+1)/1 = z/(-1) corta al plano xy
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Plano xy: z = 0
> >
> > **Paso 2:** De las ecuaciones simétricas: z = -t, entonces z = 0 → t = 0
> >
> > **Paso 3:** Sustituir t = 0
> > $$\begin{align} x &= 1 + 2(0) = 1 \\ y &= -1 + 1(0) = -1 \\ z &= -0 = 0 \end{align}$$
> >
> > **Respuesta:** P = (1, -1, 0)
> >
> > **Lección:** para cortar un plano coordenado, igualar la coordenada correspondiente a cero.

> [!example] 💪 Ángulos Avanzados: 🟠
>
> 11. Calcular el ángulo entre:
>
>     - L: (x,y,z) = (0,0,0) + t(1,2,2)
>     - π: 2x + y + 2z = 9
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Identificar vectores
> > - **v** = (1, 2, 2)
> > - **n** = (2, 1, 2)
> >
> > **Paso 2:** Producto punto y magnitudes
> > $$\mathbf{v} \cdot \mathbf{n} = (1)(2) + (2)(1) + (2)(2) = 2 + 2 + 4 = 8$$
> > $$||\mathbf{v}|| = \sqrt{1+4+4} = 3$$
> > $$||\mathbf{n}|| = \sqrt{4+1+4} = 3$$
> >
> > **Paso 3:** Calcular seno
> > $$\sin \theta = \frac{|8|}{3 \cdot 3} = \frac{8}{9}$$
> >
> > **Paso 4:** Ángulo
> > $$\theta = \arcsin\left(\frac{8}{9}\right) \approx 62.73°$$
> >
> > **Lección:** el ángulo recta-plano usa seno, no coseno.

> [!example] 💪 Construcción Avanzada: 🔴
>
> 16. Encontrar la recta perpendicular a π: 2x - y + 3z = 5 que pasa por P(1,2,-1)
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Vector normal del plano = vector director de la recta
> > $$\mathbf{n} = (2, -1, 3) = \mathbf{v}$$
> >
> > **Paso 2:** Ecuación de la recta
> > $$(x, y, z) = (1, 2, -1) + t(2, -1, 3)$$
> >
> > **Ecuaciones paramétricas:**
> > $$\begin{cases} x = 1 + 2t \\ y = 2 - t \\ z = -1 + 3t \end{cases}$$
> >
> > **Lección:** la recta perpendicular a un plano usa el vector normal como director.

---

## 🎓 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Clasifico la relación entre una recta y un plano usando **v**·**n**.
> - [ ] Distingo si una recta es contenida, paralela, secante o perpendicular a un plano.
> - [ ] Encuentro el punto de intersección de una recta secante con un plano.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo el ángulo entre una recta y un plano usando $\sin\theta = \frac{|\mathbf{v}\cdot\mathbf{n}|}{||\mathbf{v}||\cdot||\mathbf{n}||}$.
> - [ ] Construyo una recta perpendicular a un plano por un punto dado.
> - [ ] Construyo una recta paralela a un plano por un punto dado.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo problemas de proyección ortogonal de puntos sobre planos.
> - [ ] Aplico relaciones recta-plano en contextos de computación gráfica y física.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Calculus*, cap. 12 «Vectors and the Geometry of Space»: relaciones recta-plano.
> - Syllabus oficial MATG1046 «Cálculo Vectorial», ESPOL — Unidad 1 (Geometría Analítica en ℝ³).
> - Apuntes del curso MATG1046 y las figuras de la propia materia (`Unidad 0 - Guias y Ejercicios/Diagramas/`).

---

## 🔁 Repaso SR

#flashcards/calcvec-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cómo se clasifica la relación recta-plano?::Calcular **v**·**n**: si =0 y P₀∈π es contenida; si =0 y P₀∉π es paralela; si ≠0 es secante.
> - ¿Cuándo una recta es perpendicular a un plano?::Cuando su vector director es paralelo al vector normal del plano (**v** = k**n**).
> - ¿Qué fórmula usa el ángulo entre recta y plano?::$\sin\theta = \frac{|\mathbf{v}\cdot\mathbf{n}|}{||\mathbf{v}||\cdot||\mathbf{n}||}$ (seno, no coseno).
> - ¿Cómo se encuentra el punto de intersección recta-plano?::Sustituir las ecuaciones paramétricas de la recta en la ecuación del plano y despejar t.

---

## 🔗 Conexiones con el Sistema de Notas

> [!quote] 🌐 Enlaces Conceptuales
>
> **Prerrequisitos (Prerequisites):**
>
> - [[01 - Rectas en R3]] - Ecuaciones y propiedades de rectas
> - [[02 - Planos en R3]] - Ecuaciones y propiedades de planos
> - [[02 - Vectores en R3]] - Operaciones vectoriales
> - [[01 – Producto punto y ángulos]] - Para ángulos y perpendicularidad
> - [[02 – Producto cruz y áreas]] - Para vectores normales
>
> **Temas siguientes:**
>
> - [[01 - Distancias en ℝ³]] - Distancia punto-plano, recta-plano
> - 07.1 Distancia Punto-Plano - Usando perpendiculares
> - 07.2 Distancia Punto-Recta - Geometría relacionada
>
> **Conceptos relacionados:**
>
> - Vector Director - Dirección de la recta
> - Paralelismo en R3 - Condiciones de paralelismo
> - Perpendicularidad en R3 - Condiciones de ortogonalidad
> - Proyecciones en R3 - Proyección ortogonal
>
> **Aplicaciones directas:**
>
> - Ray Tracing - Computación gráfica
> - Óptica Geométrica - Reflexión y refracción
> - Mecánica Clásica - Planos inclinados

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Dominar la clasificación usando **v**·**n** antes de pasar a distancias.
> - Siguiente nota: [[01 - Distancias en ℝ³]] — distancia punto-plano y recta-plano usando perpendiculares.
> - Repaso: siempre verificar si **v**·**n** = 0 antes de buscar intersección.

**Tags:** #MATG1046 #unidad1 #recta-plano #relacion-recta-plano #interseccion-recta-plano #perpendicularidad-recta-plano #paralelismo-recta-plano #angulo-recta-plano #proyecciones #ray-tracing #computacion-grafica #fisica #navegacion #universidad #matematicas #geometria-espacial #vectores #calculo-vectorial
