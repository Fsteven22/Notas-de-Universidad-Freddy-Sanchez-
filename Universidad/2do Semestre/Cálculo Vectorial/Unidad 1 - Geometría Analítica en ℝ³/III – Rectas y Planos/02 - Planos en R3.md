---
dg-publish: true
tags: [MATG1046, unidad1, planos, plano-en-R3, vector-normal, ecuacion-plano, interseccion-planos]
---

# 📐 Planos en ℝ³

## 🎯 Introducción

> [!info] 💡 Introducción a los Planos en el Espacio
>
> Los **planos en ℝ³** son superficies planas bidimensionales que se extienden infinitamente en el espacio tridimensional. Son uno de los objetos geométricos fundamentales en geometría analítica espacial.
>
> **Analogías útiles:**
>
> - **Física:** Como una hoja de papel infinita suspendida en el espacio
> - **Geometría:** Extensión bidimensional de una recta en el espacio
> - **Arquitectura:** Como paredes, pisos o techos idealizados
>
> **Importancia práctica:**
>
> - **Ingeniería:** Diseño de estructuras y superficies
> - **Física:** Análisis de fuerzas y movimientos en planos
> - **Computación Gráfica:** Renderizado de superficies planas
> - **Cristalografía:** Estudio de planos cristalinos
>
> **Por qué importa:** un plano es el siguiente objeto geométrico después de la recta; dominar sus ecuaciones es necesario para casi todo lo que viene después (superficies, integrales múltiples, optimización con restricciones).
>
> **Ejemplo:** una pared del edificio es un plano; el arquitecto necesita saber exactamente dónde la cortan el suelo y el techo (intersecciones con planos coordenados).

---

## 📋 Definiciones Formales

### 📐 Ecuación General del Plano

> [!note] 📋 Definición — Ecuación General del Plano
>
> **Definición:**
>
> Una **ecuación general de un plano** en ℝ³ tiene la forma:
>
> **ax + by + cz + d = 0**
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Ecuacion_General_Plano_01.svg]]
> **Se lee así:** un cuadro raíz «Plano en ℝ³» con dos ramas: **Ecuación general** (ax + by + cz + d = 0) y **Normal** (n = ⟨a, b, c⟩ es perpendicular al plano).
> **Por qué importa:** los coeficientes de x, y, z nos dan directamente el vector normal del plano, que lo define por completo.
> **Ejemplo:** para 2x + 3y - 4z + 6 = 0, el vector normal es (2, 3, -6).
>
> **Características clave:**
>
> - El vector **n** = (a, b, c) es **perpendicular** al plano
> - Si **n** = (a, b, c) ≠ (0, 0, 0), el plano está bien definido
> - El vector normal determina la orientación del plano

### 🔢 Ecuación Vectorial y Paramétrica

> [!note] 📋 Definición — Ecuación Vectorial del Plano
>
> **Definición:**
>
> Usando un punto **P₀** y dos vectores directores **u** y **v** no paralelos:
>
> **r(s,t) = r₀ + su + tv**
>
> O en componentes: $$(x, y, z) = (x_0, y_0, z_0) + s(u_1, u_2, u_3) + t(v_1, v_2, v_3)$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Forma_Vectorial_Plano_01.svg]]
> **Se lee así:** el cuadro raíz «Forma Vectorial» con dos ramas: **Fórmulas** (r(s,t) = r₀ + su + tv y sus componentes) y **Normal** (n = u × v).
> **Por qué importa:** es la parametrización más flexible — dos grados de libertad (s, t) que se mueven sobre el plano.
> **Ejemplo:** plano que pasa por P₀(1, 2, -1) con vectores **u** = (2, 0, 1) y **v** = (1, 1, 0): r(s,t) = (1, 2, -1) + s(2, 0, 1) + t(1, 1, 0).

> [!note] 📋 Definición — Ecuaciones Paramétricas
>
> **Definición:**
>
> Desarrollando la ecuación vectorial:
>
> $$\begin{cases} x = x_0 + su_1 + tv_1 \\ y = y_0 + su_2 + tv_2 \\ z = z_0 + su_3 + tv_3 \end{cases}$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Forma_Vectorial_Plano_01.svg]]
> **Se lee así:** el cuadro raíz «Forma Vectorial» con las componentes paramétricas del plano: x, y, z en función de s y t.
> **Por qué importa:** la forma paramétrica permite generar cualquier punto del plano variando s y t.
>
> **Ventajas:**
>
> - Fácil generar puntos del plano
> - Útil para parametrizaciones
> - Clara visualización de direcciones
>
> **Ejemplo:** Plano que pasa por P₀(1, 2, -1) con vectores **u** = (2, 0, 1) y **v** = (1, 1, 0):
>
> $$\begin{cases} x = 1 + 2s + t \\ y = 2 + t \\ z = -1 + s \end{cases}$

### 📊 Forma Normal y de Interceptos

> [!note] 📋 Definición — Forma Normal del Plano
>
> **Definición:**
>
> Usando el vector normal unitario **n̂**:
>
> $$\mathbf{\hat{n}} \cdot (\mathbf{r} - \mathbf{r}_0) = 0$$
>
> O equivalentemente: $$\mathbf{\hat{n}} \cdot \mathbf{r} = p$$
>
> Donde:
>
> - **n̂** = **n**/||**n**|| es el vector normal unitario
> - p = **n̂** · **r₀** es la distancia del origen al plano
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Forma_Normal_Plano_01.svg]]
> **Se lee así:** el cuadro raíz «Forma Normal» con tres ramas: **n̂ · (r − r₀) = 0** (ecuación general), **n̂** (vector normal unitario) y **p = n̂ · r₀** (distancia del origen al plano).
> **Por qué importa:** es la forma más eficiente para calcular distancias punto-plano y ángulos entre planos.
> **Ejemplo:** para plano 3x + 4y + 12z = 24, el vector normal unitario es n̂ = (2/13, 3/13, -6/13) y p = 24/13.

> [!note] 📋 Definición — Forma de Interceptos
>
> **Definición:**
>
> Si el plano intercepta los ejes en a, b, c (todos ≠ 0):
>
> $$\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Forma_Interceptos_Plano_01.svg]]
> **Se lee así:** el cuadro raíz «Forma de Interceptos» con dos ramas: **Fórmula** (x/a + y/b + z/c = 1) y **Interpretación** (a: corte eje x, b: corte eje y, c: corte eje z).
> **Por qué importa:** es la forma más rápida para dibujar el plano a mano: marca los tres puntos de corte con los ejes y únelos.
> **Ejemplo:** Plano que pasa por (3, 0, 0), (0, 2, 0), (0, 0, 4):
>
> $$\frac{x}{3} + \frac{y}{2} + \frac{z}{4} = 1$$
>
> Forma general: 4x + 6y + 3z - 12 = 0
>
> **Lección:** es la forma más rápida para dibujar el plano a mano: marca los tres puntos de corte con los ejes y únelos.

---

## 🔧 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> **Nivel 1 - Básico:** 🟢
>
> 1. Encontrar la ecuación del plano que pasa por P(1, 2, -1) con normal **n** = (1, 2, -1).
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Vector normal **n** = (2, -1, 3)
> >
> > **Paso 2:** Usar la ecuación punto-normal:
> >
> > $$\begin{align} 2(x - 1) - 1(y - 2) + 3(z + 1) &= 0 \\ 2x - 2 - y + 2 + 3z + 3 &= 0 \\ 2x - y + 3z + 3 &= 0 \end{align}$$
> >
> > **Ecuación del plano:** 2x - y + 3z + 3 = 0
> >
> > **Lección:** con un punto y un vector normal, la ecuación del plano se obtiene directamente.

> [!example] 📋 Planteamiento
>
> **Nivel 2 - Intermedio:** 🟡
>
> Encontrar el plano que pasa por los puntos P₁(1, 0, 0), P₂(0, 2, 0), P₃(0, 0, 3).
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Formar dos vectores en el plano:
> >
> > $$\mathbf{v}_1 = P_1P_2 = (2-1, 0-2, 1-3) = (1, -2, -2)$$
> > $$\mathbf{v}_2 = P_1P_3 = (0-1, 1-2, 2-3) = (-1, -1, -1)$$
> >
> > **Paso 2:** Calcular el vector normal mediante producto cruz:
> >
> > $$\mathbf{n} = \mathbf{v}_1 \times \mathbf{v}_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & -2 & -2 \\ -1 & -1 & -1 \end{vmatrix}$$
> >
> > $$n = i[(-2)(-1) - (-2)(-1)] - j[(1)(-1) - (-2)(-1)] + k[(1)(-1) - (-2)(-1)]$$
> > $$n = i(2 - 2) - j(-1 - 2) + k(-1 - 2) = (0, 3, -3)$$
> >
> > Simplificando: **n** = (0, 1, -1)
> >
> > **Paso 3:** Usar un punto (P₁) para obtener la ecuación:
> >
> > $$\begin{align} 0(x - 1) + 1(y - 2) + (-1)(z - 3) &= 0 \\ y - 2 - z + 3 &= 0 \\ y - z + 1 &= 0 \end{align}$$
> >
> > **Ecuación del plano:** y - z + 1 = 0
> >
> > **Verificación:** Los tres puntos deben satisfacer la ecuación:
> >
> > - P₁(1, 2, 3): 2 - 3 + 1 = 0 ✓
> > - P₂(2, 0, 1): 0 - 1 + 1 = 0 ✓
> > - P₃(0, 1, 2): 1 - 2 + 1 = 0 ✓

> [!example] 📋 Planteamiento
>
> **Nivel 2 - Intermedio:** 🟡
>
> Encontrar el plano que pasa por P₀(1, -1, 2) con vectores directores **u** = (2, 1, 0) y **v** = (1, 0, 3)
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Calcular vector normal **n** = u × v
> >
> > $$n = u \times v = \begin{vmatrix} i & j & k \\ 2 & 1 & 0 \\ 1 & 0 & 3 \end{vmatrix} = i(3 - 0) - j(6 - 0) + k(0 - 1) = (3, -6, -1)$$
> >
> > **Paso 2:** Aplicar ecuación del plano usando P₀(1, -1, 2)
> >
> > $$\begin{align} 3(x - 1) - 6(y + 2) - 1(z - 2) &= 0 \\ 3x - 3 - 6y - 6 - z + 2 &= 0 \\ 3x - 6y - z - 7 &= 0 \end{align}$$
> >
> > **Ecuación del plano:** 3x - 6y - z - 7 = 0
> >
> > **Lección:** si ya tienes dos vectores directores, el normal es directamente su producto cruz.

> [!example] 📋 Planteamiento
>
> **Nivel 2 - Intermedio:** 🟡
>
> Encontrar el plano que contiene la recta L: (x, y, z) = (1, 0, 2) + t(2, 1, -1) y el punto P(3, 2, 1)
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Identificar elementos
> >
> > - Punto en la recta: P₀(1, 0, 2)
> > - Vector director de la recta: **u** = (2, 1, -1)
> > - Punto externo: P(3, 2, 1)
> >
> > **Paso 2:** Formar segundo vector director **v** = P₀P = (3-1, 2-0, 1-2) = (2, 2, -1)
> >
> > **Paso 3:** Calcular normal n = u × v
> >
> > $$n = u \times v = \begin{vmatrix} i & j & k \\ 2 & 1 & -1 \\ 2 & 2 & -1 \end{vmatrix} = i(-1 + 2) - j(-2 + 2) + k(4 - 2) = (1, 0, 2)$$
> >
> > **Paso 4:** Ecuación del plano usando P₀(1, 0, 2)
> >
> > $$\begin{align} 1(x - 1) + 0(y - 0) + 2(z - 2) &= 0 \\ x - 1 + 2z - 4 &= 0 \\ x + 2z - 5 &= 0 \end{align}$$
> >
> > **Ecuación del plano:** x + 2z - 5 = 0
> >
> > **Lección:** si una recta y un punto externo están dados, el vector director de la recta y el vector entre un punto de la recta y el punto externo definen el plano.

> [!example] 📋 Planteamiento
>
> **Nivel 2 - Intermedio:** 🟡
>
> Encontrar el plano que contiene las rectas paralelas:
>
> - L₁: (x, y, z) = (1, 0, 1) + s(2, 1, 0)
> - L₂: (x, y, z) = (0, 1, 2) + t(2, 1, 0)
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Vector director común u = (2, 1, 0)
> >
> > **Paso 2:** Vector entre las rectas. Puntos: P₁(1, 0, 1) en L₁ y P₂(0, 1, 2) en L₂
> >
> > $$v = P_1P_2 = (-1, 1, 1)$$
> >
> > **Paso 3:** Calcular normal n = u × v
> >
> > $$n = u \times v = \begin{vmatrix} i & j & k \\ 2 & 1 & 0 \\ -1 & 1 & 1 \end{vmatrix} = (1, -2, 3)$$
> >
> > **Paso 4:** Ecuación del plano usando P₁(1, 0, 1)
> >
> > $$\begin{align} 1(x - 1) - 2(y - 0) + 3(z - 1) &= 0 \\ x - 1 - 2y + 3z - 3 &= 0 \\ x - 2y + 3z - 4 &= 0 \end{align}$$
> >
> > **Ecuación del plano:** x - 2y + 3z - 4 = 0
> >
> > **Lección:** dos rectas paralelas determinan un plano único; el vector normal es el producto cruz del vector director común y el vector entre un punto de cada recta.

> [!example] 📋 Planteamiento
>
> **Nivel 2 - Intermedio:** 🟡
>
> Encontrar el plano que contiene las rectas secantes:
>
> - L₁: (x, y, z) = (1, 1, 0) + s(1, 0, 1)
> - L₂: (x, y, z) = (1, 1, 0) + t(0, 1, 1)
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Los vectores directores son u = (1, 0, 1) y v = (0, 1, 1)
> >
> > **Paso 2:** Calcular normal n = u × v
> >
> > $$n = u \times v = \begin{vmatrix} i & j & k \\ 1 & 0 & 1 \\ 0 & 1 & 1 \end{vmatrix} = (-1, -1, 1)$$
> >
> > O simplificado: **n** = (1, 1, -1)
> >
> > **Paso 3:** Usar el punto común P₀(1, 1, 0)
> >
> > $$\begin{align} 1(x - 1) + 1(y - 1) - 1(z - 0) &= 0 \\ x + y - z - 2 &= 0 \end{align}$$
> >
> > **Ecuación del plano:** x + y - z - 2 = 0
> >
> > **Lección:** dos rectas secantes determinan un plano único; su punto común está en el plano y su normal es el producto cruz de sus directores.

---

## 🎓 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Calculo la ecuación general de un plano ax + by + cz + d = 0.
> - [ ] Identifico el vector normal de un plano a partir de su ecuación.
> - [ ] Encuentro la ecuación de un plano dado un punto y un vector normal.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Encuentro la ecuación de un plano dado por tres puntos no colineales.
> - [ ] Distingo si dos planos son paralelos, perpendiculares o secantes.
> - [ ] Calculo el ángulo entre dos planos.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo problemas que mezclan el factorial con conteo restringido (inclusión-exclusión).
> - [ ] Verifico resultados complejos mediante el factorial como conteo de órdenes.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - Johnsonbaugh, *Discrete Mathematics*, 8.ª ed., cap. 5: permutaciones y combinaciones.
> - [[Unidad 3 - Números y Conteo/06 - Permutaciones y Combinaciones|06 - Permutaciones y Combinaciones]] — el factorial como conteo de órdenes.
> - [[Unidad 3 - Números y Conteo/07 - Teorema del Binomio y Principio del Palomar|07 - Teorema del Binomio y Principio del Palomar]] — $\\binom{n}{k}$ y $\\binom{n}{k} = \\binom{n}{n-k}$.
> - [[Unidad 3 - Números y Conteo/04 - Principios de Multiplicación y Suma|04 - Principios de Multiplicación y Suma]] — el principio multiplicativo detrás de $n!$.
> - [[Unidad 2 - Funciones y Relaciones/04 - Sucesiones y Cadenas|04 - Sucesiones y Cadenas]] — el factorial como producto de sucesión telescópica.
> - [[Unidad 1 - Logica y Conjuntos/III - Razonamiento Inductivo/03 - Inducción Matemática|03 - Inducción Matemática]] — la inducción que prueba $n! = n \\cdot (n-1)!$ y $n! \\geq 2^{n-1}$.
> - Unidad 0 - Guias y Ejercicios/Lecciones/SOLUCIÓN_LEC_2.pdf — Lección 2 (04/11/2026): el producto telescópico $\\prod_{i=2}^n(1-\\frac{1}{i^2}) = \\frac{n+1}{2n}$ resuelto con inducción, y la relación $f \\,R\\, g \\iff f(0)=g(0)$ sobre funciones con su clase $[f] = \\{g : g(0) = 0\\}$.
> - Unidad 0 - Guias y Ejercicios/Lecciones/SOLUCIÓN_LEC_1.pdf — Lección 1 (04/11/2026): fundamentos de lógica y demostraciones.

---

## 🔁 Repaso SR

#flashcards/calcvec-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es la ecuación general de un plano?::ax + by + cz + d = 0 donde (a,b,c) es el vector normal.
> - ¿Cómo se obtiene el vector normal de un plano dado por 3 puntos?::Producto cruz de dos vectores en el plano.
> - ¿Cuándo dos planos son paralelos?::Cuando sus vectores normales son proporcionales.
> - ¿Cómo se calcula el ángulo entre dos planos?::Cos θ = |n₁·n₂|/(||n₁|| · ||n₂||) usando sus normales.

---

## 🔗 Conexiones con el Sistema de Notas

> [!quote] 🌐 Enlaces Conceptuales
>
> **Prerrequisitos (Prerequisites):**
>
> - [[01 - Sistema de referencia espacial en R3]] - Coordenadas en ℝ³
> - [[02 - Vectores en R3]] - Operaciones vectoriales fundamentales
> - [[02 – Producto cruz y áreas]] - Cálculo de vectores normales
> - [[01 – Producto punto y ángulos]] - Perpendicularidad y ángulos
> - 03. Distancia en el Espacio - Fundamentos métricos
>
> **Temas siguientes:**
>
> - [[02 - Relación recta–plano]] - Intersecciones y paralelismo
> - [[01 - Distancias en ℝ³]] - Distancia punto-plano, plano-plano
> - 07.1 Distancia Punto-Plano - Fórmula y aplicaciones
> - 07.4 Distancia entre Planos Paralelos - Caso especial
>
> **Temas relacionados:**
>
> - [[01 – Transformaciones lineales]] - Planos como núcleo/imagen
> - [[05 - Sistemas de ecuaciones lineales]] - Intersección de planos
> - [[01 - Subespacios Vectoriales]] - Planos como subespacios
> - Álgebra de Matrices - Representación matricial
>
> **Aplicaciones avanzadas:**
>
> - [[01 - Longitud de Curva]] - Planos tangentes
> - [[03 - Teoremas Especiales para Integrales Definidas]] - Gradiente y planos tangentes
> - Ecuaciones Diferenciales - Familias de planos solución
> - [[01 - Polinomios de Taylor]] - Restricciones planares
>
> **Aplicaciones prácticas:**
>
> - Computación Gráfica 3D - Renderizado y clipping
> - Diseño Asistido por Computadora - Modelado CAD
> - Robótica - Planificación de trayectorias
> - Análisis Estructural - Elementos finitos

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Regla rápida: antes de cada fórmula con factorial, pregúntate si puedes simplificar cancelando prefijos comunes.
> - Después pasa a [[Unidad 3 - Números y Conteo/06 - Permutaciones y Combinaciones|06 - Permutaciones y Combinaciones]] (usos del factorial en conteo).
> - Cierra con [[Unidad 3 - Números y Conteo/07 - Teorema del Binomio y Principio del Palomar|07 - Teorema del Binomio y Principio del Palomar]] ($\\binom{n}{k}$ con factoriales).
>

**Tags:** #MATG1046 #unidad1 #planos #plano-en-R3 #vector-normal #ecuacion-plano #interseccion-planos #cálculo-vectorial