# 📘 Superficies de Nivel

## 🎯 Introducción

> [!info]- 💡 ¿Qué son las Superficies de Nivel?
> 
> Las **superficies de nivel** son la extensión natural de las curvas de nivel a funciones de **tres variables**. Mientras que las curvas de nivel nos ayudan a visualizar funciones $f(x,y)$, las superficies de nivel nos permiten entender funciones $f(x,y,z)$.
> 
> **Analogía con curvas de nivel:**
> 
> - **Curvas de nivel:** Para $f: \mathbb{R}^2 \to \mathbb{R}$, son curvas en el plano
> - **Superficies de nivel:** Para $f: \mathbb{R}^3 \to \mathbb{R}$, son superficies en el espacio
> 
> **Idea intuitiva:** Una superficie de nivel es el conjunto de todos los puntos en el espacio donde la función toma el mismo valor constante $k$.
> 
> **¿Por qué son importantes?**
> 
> - No podemos graficar $w = f(x,y,z)$ (necesitaríamos 4 dimensiones)
> - Las superficies de nivel nos permiten visualizar estas funciones en 3D
> - Son fundamentales en física, química, ingeniería y ciencias de la tierra
> 
> **Ejemplos del mundo real:**
> 
> - **Física:** Superficies equipotenciales en campos eléctricos
> - **Meteorología:** Superficies de presión constante en la atmósfera
> - **Química:** Orbitales atómicos (densidad de probabilidad electrónica)
> - **Geología:** Capas de densidad constante en el interior de la Tierra
> - **Medicina:** Superficies de concentración en tomografías

---

## 📐 Definición Formal

### 🔵 Superficie de Nivel

> [!example]- 🟢 Definición: Superficie de Nivel
> 
> **Definición formal:** Sea $f: D \subseteq \mathbb{R}^3 \to \mathbb{R}$ una función de tres variables. La **superficie de nivel** de $f$ para el valor $k \in \mathbb{R}$ es el conjunto:
> 
> $$S_k = {(x,y,z) \in D : f(x,y,z) = k}$$
> 
> **En palabras:** Es el conjunto de todos los puntos $(x,y,z)$ en el dominio donde la función toma el mismo valor $k$.
> 
> **Notación alternativa:**
> 
> - También llamadas **superficies de contorno** o **superficies equipotenciales**
> - El valor $k$ se llama **nivel** o **valor de la función**
> 
> **Ecuación implícita:** La superficie de nivel se describe mediante la ecuación: $$f(x,y,z) = k$$
> 
> **Observaciones importantes:**
> 
> 1. ✅ Cada superficie corresponde a UN valor específico de $k$
> 2. ✅ Las superficies están en el espacio 3D (no en 4D)
> 3. ✅ Diferentes valores de $k$ producen diferentes superficies
> 4. ✅ Para funciones continuas, superficies de nivel distintas NO se intersectan

### 🎨 Familia de Superficies de Nivel

> [!example]- 🟡 Familia de Superficies
> 
> **Definición:** Una **familia de superficies de nivel** es la colección de todas las superficies $S_k$ para diferentes valores de $k$ en el rango de $f$.
> 
> **Visualización:**
> 
> - Se eligen valores de $k$ igualmente espaciados (e.g., $k = 0, 1, 2, 3, ...$)
> - Se grafican múltiples superficies simultáneamente
> - Permite ver la "estructura" completa de la función
> 
> **Información que proporcionan:**
> 
> - Cómo varía la función en el espacio
> - Direcciones de cambio rápido vs lento
> - Ubicación de extremos
> - Simetría de la función
> 
> **Relación con el gradiente:** El vector gradiente $\nabla f$ es **perpendicular** a las superficies de nivel (similar a las curvas de nivel)

---

## 🔍 Relación con Curvas de Nivel

> [!note]- 🔄 Comparación: Curvas vs Superficies
> 
> |Aspecto|Curvas de Nivel|Superficies de Nivel|
> |---|---|---|
> |**Función**|$f(x,y)$|$f(x,y,z)$|
> |**Dominio**|$\mathbb{R}^2$ (plano)|$\mathbb{R}^3$ (espacio)|
> |**Conjunto de nivel**|Curvas en 2D|Superficies en 3D|
> |**Ecuación**|$f(x,y) = k$|$f(x,y,z) = k$|
> |**Dimensión del conjunto**|1D (curva)|2D (superficie)|
> |**Visualización**|Fácil (en papel)|Requiere 3D|
> |**Gráfica completa**|$z = f(x,y)$ en 3D|$w = f(x,y,z)$ en 4D (imposible)|
> |**Aplicación típica**|Mapas topográficos|Campos físicos 3D|
> 
> **Principio unificador:** Ambos representan conjuntos donde la función es constante, pero en diferentes dimensiones.
> 
> **Extensión natural:**
> 
> - Funciones de 1 variable: puntos de nivel (0D)
> - Funciones de 2 variables: curvas de nivel (1D)
> - Funciones de 3 variables: superficies de nivel (2D)
> - Funciones de $n$ variables: hipersuperficies de nivel ($(n-1)$D)

---

## 📊 Superficies Cuádricas Fundamentales

> [!info]- 🎓 Catálogo de Superficies Básicas
> 
> Las superficies cuádricas son las más comunes como superficies de nivel. Aquí está una guía de referencia:
> 
> ### 1. Esfera
> 
> **Ecuación:** $x^2 + y^2 + z^2 = r^2$
> 
> **Características:**
> 
> - Centro en el origen
> - Radio $r$
> - Simetría esférica completa
> 
> ---
> 
> ### 2. Elipsoide
> 
> **Ecuación:** $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$
> 
> **Características:**
> 
> - Semiejes $a$, $b$, $c$
> - Superficie cerrada
> - Si $a = b = c$: esfera
> 
> ---
> 
> ### 3. Cilindro Circular
> 
> **Ecuación:** $x^2 + y^2 = r^2$
> 
> **Características:**
> 
> - Eje paralelo al eje $z$
> - Radio $r$
> - Se extiende infinitamente en $z$
> 
> ---
> 
> ### 4. Cilindro Elíptico
> 
> **Ecuación:** $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$
> 
> **Características:**
> 
> - Sección transversal elíptica
> - Eje paralelo a $z$
> 
> ---
> 
> ### 5. Cono Circular
> 
> **Ecuación:** $x^2 + y^2 = z^2$ o $z^2 = x^2 + y^2$
> 
> **Características:**
> 
> - Vértice en el origen
> - Dos napas (superior e inferior)
> - Ángulo de apertura constante
> 
> ---
> 
> ### 6. Paraboloide Elíptico
> 
> **Ecuación:** $z = \frac{x^2}{a^2} + \frac{y^2}{b^2}$ o $\frac{x^2}{a^2} + \frac{y^2}{b^2} = z$
> 
> **Características:**
> 
> - Se abre hacia arriba (o abajo si $z$ es negativo)
> - Vértice en el origen
> - Secciones transversales elípticas
> 
> ---
> 
> ### 7. Paraboloide Hiperbólico
> 
> **Ecuación:** $z = \frac{x^2}{a^2} - \frac{y^2}{b^2}$
> 
> **Características:**
> 
> - Forma de "silla de montar"
> - Punto de silla en el origen
> - Curvaturas opuestas en direcciones perpendiculares
> 
> ---
> 
> ### 8. Hiperboloide de Una Hoja
> 
> **Ecuación:** $\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$
> 
> **Características:**
> 
> - Superficie continua
> - Forma de torre de enfriamiento
> - Secciones horizontales: elipses
> - Secciones verticales: hipérbolas
> 
> ---
> 
> ### 9. Hiperboloide de Dos Hojas
> 
> **Ecuación:** $\frac{z^2}{c^2} - \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$
> 
> **Características:**
> 
> - Dos componentes separadas
> - Secciones horizontales: elipses (solo para $|z| > c$)
> - Secciones verticales: hipérbolas
> 
> ---
> 
> ### 10. Plano
> 
> **Ecuación:** $ax + by + cz = d$
> 
> **Características:**
> 
> - Superficie plana
> - Normal: vector $(a, b, c)$
> - Puede tener cualquier orientación

---

## 📚 Ejemplos Fundamentales

> [!example]- 📐 Ejemplo 1: Esferas Concéntricas
> 
> **Función:** $f(x,y,z) = x^2 + y^2 + z^2$
> 
> **Dominio:** $\mathbb{R}^3$ (todo el espacio)
> 
> **Rango:** $[0, +\infty)$
> 
> **Encontrar superficies de nivel:**
> 
> Plantear $f(x,y,z) = k$: $$x^2 + y^2 + z^2 = k$$
> 
> **Análisis por casos:**
> 
> - **Si $k < 0$:** No hay solución (suma de cuadrados no puede ser negativa)
> - **Si $k = 0$:** $x^2 + y^2 + z^2 = 0$ → Solo el punto $(0,0,0)$
> - **Si $k > 0$:** Esfera de radio $r = \sqrt{k}$ centrada en el origen
> 
> **Para diferentes valores de $k$:**
> 
> - $k = 0$: Punto $(0,0,0)$
> - $k = 1$: Esfera de radio 1
> - $k = 4$: Esfera de radio 2
> - $k = 9$: Esfera de radio 3
> - $k = 16$: Esfera de radio 4
> 
> **Descripción:**
> 
> ```
>         z
>         |
>         |   ⚪ k=1
>         | ⚪⚪⚪⚪⚪
>         |⚪⚪⚪⚪⚪⚪⚪ k=4
>     ----+⚪⚪⚪⚪⚪⚪⚪---- y
>        /|⚪⚪⚪⚪⚪⚪⚪
>       / | ⚪⚪⚪⚪⚪
>      x  |   ⚪ k=9
> 
>     Esferas concéntricas
>     (vista esquemática en corte)
> ```
> 
> **Observaciones:**
> 
> - Superficies de nivel son **esferas concéntricas**
> - Radio aumenta con $\sqrt{k}$
> - Todas centradas en el origen
> - Simetría esférica completa
> - Representa la distancia al cuadrado desde el origen
> 
> **Interpretación física:**
> 
> - $f(x,y,z)$ mide la "distancia al cuadrado" del origen
> - En física: potencial gravitacional o eléctrico central
> - Valor mínimo en el origen
> 
> **Cortes con planos:**
> 
> - Corte con plano $z = 0$: Círculos $x^2 + y^2 = k$
> - Corte con plano $x = 0$: Círculos $y^2 + z^2 = k$
> - Todos los cortes son círculos

> [!example]- 🏔️ Ejemplo 2: Planos Paralelos
> 
> **Función:** $f(x,y,z) = z$
> 
> **Dominio:** $\mathbb{R}^3$
> 
> **Rango:** $\mathbb{R}$
> 
> **Encontrar superficies de nivel:**
> 
> Plantear $f(x,y,z) = k$: $$z = k$$
> 
> **Para diferentes valores de $k$:**
> 
> - $k = -2$: Plano $z = -2$ (debajo del plano $xy$)
> - $k = 0$: Plano $z = 0$ (el plano $xy$)
> - $k = 1$: Plano $z = 1$
> - $k = 2$: Plano $z = 2$
> - $k = 5$: Plano $z = 5$
> 
> **Descripción:**
> 
> ```
>         z
>         |
>     k=2 |========== plano z=2
>         |
>     k=1 |========== plano z=1
>         |
>     k=0 |========== plano xy
>         |
>    k=-1 |========== plano z=-1
>         |
>     ----+----------- y
>        /
>       /
>      x
> ```
> 
> **Observaciones:**
> 
> - Superficies son **planos horizontales** paralelos
> - Espaciamiento uniforme (función lineal)
> - Perpendiculares al eje $z$
> - La función simplemente mide la "altura" $z$
> 
> **Interpretación:**
> 
> - Representa la coordenada $z$ misma
> - Superficies equipotenciales en campo gravitacional uniforme
> - Cada plano tiene altura constante

> [!example]- 🌀 Ejemplo 3: Cilindros Concéntricos
> 
> **Función:** $f(x,y,z) = x^2 + y^2$
> 
> **Dominio:** $\mathbb{R}^3$
> 
> **Rango:** $[0, +\infty)$
> 
> **Encontrar superficies de nivel:**
> 
> Plantear $f(x,y,z) = k$: $$x^2 + y^2 = k$$
> 
> **Análisis:**
> 
> **Observación clave:** La ecuación no involucra $z$, por lo que $z$ puede tomar cualquier valor.
> 
> **Para diferentes valores de $k$:**
> 
> - $k = 0$: $x^2 + y^2 = 0$ → Eje $z$ (línea)
> - $k = 1$: $x^2 + y^2 = 1$ → Cilindro de radio 1
> - $k = 4$: $x^2 + y^2 = 4$ → Cilindro de radio 2
> - $k = 9$: $x^2 + y^2 = 9$ → Cilindro de radio 3
> 
> **Descripción:**
> 
> ```
>         z
>         |
>         ║
>         ║ │ │  ← cilindros
>         ║ │ │
>         ║ │ │
>     ----╬─┼─┼---- y
>        /║ │ │
>       / ║ │ │
>      x  ║
>         eje z
> 
>     k=0  k=1 k=4
> ```
> 
> **Observaciones:**
> 
> - Superficies son **cilindros circulares rectos**
> - Eje de simetría: eje $z$
> - Radio: $r = \sqrt{k}$
> - Se extienden infinitamente en dirección $z$
> - La función no depende de $z$ (independencia de una variable)
> 
> **Interpretación física:**
> 
> - Distancia al cuadrado desde el eje $z$
> - Campo eléctrico de un cable infinito
> - Flujo alrededor de un cable

> [!example]- 🌋 Ejemplo 4: Paraboloide como Superficie de Nivel
> 
> **Función:** $f(x,y,z) = z - x^2 - y^2$
> 
> **Dominio:** $\mathbb{R}^3$
> 
> **Rango:** $\mathbb{R}$
> 
> **Encontrar superficies de nivel:**
> 
> Plantear $f(x,y,z) = k$: $$z - x^2 - y^2 = k$$ $$z = x^2 + y^2 + k$$
> 
> **Para diferentes valores de $k$:**
> 
> - $k = -2$: $z = x^2 + y^2 - 2$ (paraboloide con vértice en $(0,0,-2)$)
> - $k = 0$: $z = x^2 + y^2$ (paraboloide con vértice en el origen)
> - $k = 1$: $z = x^2 + y^2 + 1$ (paraboloide con vértice en $(0,0,1)$)
> - $k = 3$: $z = x^2 + y^2 + 3$ (paraboloide con vértice en $(0,0,3)$)
> 
> **Descripción:**
> 
> ```
>         z
>         |  k=3
>       3 |  /^\
>         | /   \
>       1 |/     \  k=1
>         /       \
>       0/  k=0    \
>      -2\___/^\___/  k=-2
>     ----+----------- y
>        /
>       /
>      x
> ```
> 
> **Observaciones:**
> 
> - Cada superficie es un **paraboloide circular**
> - Todos tienen el mismo eje (eje $z$)
> - Se abren hacia arriba
> - Vértice en altura $z = k$
> - Son **traslaciones verticales** uno del otro
> 
> **Interpretación:**
> 
> - Superficies de igual "altura relativa" al paraboloide
> - En optimización: conjuntos de nivel de funciones objetivo

> [!example]- 🎭 Ejemplo 5: Cono Doble
> 
> **Función:** $f(x,y,z) = z^2 - x^2 - y^2$
> 
> **Dominio:** $\mathbb{R}^3$
> 
> **Rango:** $\mathbb{R}$
> 
> **Encontrar superficies de nivel:**
> 
> Plantear $f(x,y,z) = k$: $$z^2 - x^2 - y^2 = k$$
> 
> **Análisis por casos:**
> 
> **Caso 1: $k = 0$** $$z^2 = x^2 + y^2$$ $$z = \pm\sqrt{x^2 + y^2}$$
> 
> **Cono circular** con vértice en el origen (dos napas)
> 
> **Caso 2: $k > 0$** (e.g., $k = 1$) $$z^2 - x^2 - y^2 = 1$$ $$\frac{z^2}{1} - \frac{x^2}{1} - \frac{y^2}{1} = 1$$
> 
> **Hiperboloide de dos hojas** (dos componentes separadas)
> 
> Secciones horizontales ($z = c$):
> 
> - Si $|c| > 1$: círculos $x^2 + y^2 = c^2 - 1$
> - Si $|c| < 1$: no hay puntos
> - Si $|c| = 1$: solo un punto
> 
> **Caso 3: $k < 0$** (e.g., $k = -1$) $$z^2 - x^2 - y^2 = -1$$ $$x^2 + y^2 - z^2 = 1$$ $$\frac{x^2}{1} + \frac{y^2}{1} - \frac{z^2}{1} = 1$$
> 
> **Hiperboloide de una hoja** (superficie continua)
> 
> Secciones horizontales: círculos $x^2 + y^2 = 1 + z^2$
> 
> **Descripción:**
> 
> ```
>         z
>         |
>       2 | ⚪  k=3 (dos hojas)
>         |
>       1 | · k=1 (dos hojas)
>         |╱╲ k=0 (cono)
>     ----+──── y
>        /╲╱
>       / | k=-1 (una hoja)
>      x  |  ╲│╱
>         |   ⚪
> ```
> 
> **Observaciones:**
> 
> - $k = 0$: Superficie **degenerada** (cono)
> - $k > 0$: **Hiperboloides de dos hojas**
> - $k < 0$: **Hiperboloides de una hoja**
> - Transición continua al variar $k$
> 
> **Interpretación física:**
> 
> - Campos electromagnéticos
> - Superficies de fase constante en ondas

> [!example]- 🎪 Ejemplo 6: Paraboloide Hiperbólico
> 
> **Función:** $f(x,y,z) = x^2 - y^2 - z$
> 
> **Dominio:** $\mathbb{R}^3$
> 
> **Rango:** $\mathbb{R}$
> 
> **Encontrar superficies de nivel:**
> 
> Plantear $f(x,y,z) = k$: $$x^2 - y^2 - z = k$$ $$z = x^2 - y^2 - k$$
> 
> **Para diferentes valores de $k$:**
> 
> - $k = -2$: $z = x^2 - y^2 + 2$ (silla de montar desplazada arriba)
> - $k = 0$: $z = x^2 - y^2$ (silla de montar estándar)
> - $k = 2$: $z = x^2 - y^2 - 2$ (silla de montar desplazada abajo)
> 
> **Descripción:**
> 
> Todas las superficies son **paraboloides hiperbólicos** (sillas de montar) desplazados verticalmente.
> 
> **Secciones transversales:**
> 
> - Plano $y = 0$: Parábolas $z = x^2 - k$ (abren hacia arriba)
> - Plano $x = 0$: Parábolas $z = -y^2 - k$ (abren hacia abajo)
> - Plano $z = c$: Hipérbolas $x^2 - y^2 = c + k$
> 
> **Observaciones:**
> 
> - Todas tienen un **punto de silla**
> - Curvaturas opuestas en direcciones perpendiculares
> - Arquitectura: techos hiperbólicos (Pringles)

> [!example]- 🌍 Ejemplo 7: Elipsoides
> 
> **Función:** $f(x,y,z) = \frac{x^2}{4} + \frac{y^2}{9} + z^2$
> 
> **Dominio:** $\mathbb{R}^3$
> 
> **Rango:** $[0, +\infty)$
> 
> **Encontrar superficies de nivel:**
> 
> Plantear $f(x,y,z) = k$: $$\frac{x^2}{4} + \frac{y^2}{9} + z^2 = k$$
> 
> **Para $k > 0$:** Dividir por $k$: $$\frac{x^2}{4k} + \frac{y^2}{9k} + \frac{z^2}{k} = 1$$
> 
> **Elipsoide** con semiejes:
> 
> - En dirección $x$: $a = 2\sqrt{k}$
> - En dirección $y$: $b = 3\sqrt{k}$
> - En dirección $z$: $c = \sqrt{k}$
> 
> **Para diferentes valores de $k$:**
> 
> - $k = 0$: Punto $(0,0,0)$
> - $k = 1$: Elipsoide $\frac{x^2}{4} + \frac{y^2}{9} + z^2 = 1$
> - $k = 4$: Elipsoide con semiejes $a=4$, $b=6$, $c=2$
> - $k = 9$: Elipsoide con semiejes $a=6$, $b=9$, $c=3$
> 
> **Observaciones:**
> 
> - Todas son **elipsoides concéntricos**
> - Relación de aspecto constante: $a:b:c = 2:3:1$
> - Más alargado en dirección $y$
> - Más comprimido en dirección $z$
> 
> **Interpretación:**
> 
> - Superficies de densidad constante en cuerpos anisótropos
> - Orbitales electrónicos en cristales

---

## 🔬 Análisis Detallado de Superficies Cuádricas

> [!info]- 📊 Hiperboloides: Análisis Profundo
> 
> ### Hiperboloide de Una Hoja
> 
> **Ecuación estándar:** $$\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$$
> 
> **Características:**
> 
> - Superficie **continua** (una sola pieza)
> - Se extiende infinitamente en dirección $z$
> - "Cintura" más estrecha en $z = 0$
> 
> **Secciones transversales:**
> 
> **Horizontal ($z = k$):** $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1 + \frac{k^2}{c^2}$$
> 
> Elipses que crecen a medida que $|k|$ aumenta
> 
> **Vertical (e.g., $y = 0$):** $$\frac{x^2}{a^2} - \frac{z^2}{c^2} = 1$$
> 
> Hipérbolas
> 
> **Radio mínimo:** En $z = 0$ $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$
> 
> **Aplicaciones:**
> 
> - Torres de enfriamiento de centrales eléctricas
> - Estructuras arquitectónicas
> - Superficies equipotenciales en física
> 
> ---
> 
> ### Hiperboloide de Dos Hojas
> 
> **Ecuación estándar:** $$\frac{z^2}{c^2} - \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$$
> 
> **Características:**
> 
> - **Dos componentes separadas**
> - Una hoja para $z > c$
> - Otra hoja para $z < -c$
> - No hay puntos cuando $|z| < c$
> 
> **Secciones transversales:**
> 
> **Horizontal ($z = k$ con $|k| > c$):** $$\frac{x^2}{a^2} + \frac{y^2}{b^2} = \frac{k^2}{c^2} - 1$$
> 
> Elipses (solo existen si $|k| > c$)
> 
> **Vertical:** Hipérbolas
> 
> **Puntos más cercanos al origen:** $(0, 0, \pm c)$
> 
> **Aplicaciones:**
> 
> - Trayectorias de partículas en campos
> - Modelos en relatividad

---

## 🎯 Cómo Identificar Superficies Cuádricas

> [!tip]- 🔍 Método de Identificación
> 
> **Paso 1: Forma general**
> 
> La ecuación cuádricas general tiene la forma: $$Ax^2 + By^2 + Cz^2 + Dx + Ey + Fz + G = 0$$
> 
> (ignorando términos cruzados como $xy$, $xz$, $yz$)
> 
> **Paso 2: Completar cuadrados**
> 
> Completar cuadrados en cada variable para llevar la ecuación a forma estándar.
> 
> **Paso 3: Contar signos**
> 
> Después de completar cuadrados, contar:
> - Cuántos términos cuadráticos tienen coeficientes **positivos**
> - Cuántos tienen coeficientes **negativos**
> - Cuántas variables están **ausentes** (orden 1 o constante)
> 
> **Paso 4: Aplicar la tabla de clasificación**
> 
> | Positivos | Negativos | Ausentes | Superficie |
> |-----------|-----------|----------|------------|
> | 3 | 0 | 0 | Elipsoide |
> | 2 | 1 | 0 | Hiperboloide de una hoja |
> | 1 | 2 | 0 | Hiperboloide de dos hojas |
> | 2 | 0 | 1 | Paraboloide elíptico |
> | 1 | 1 | 1 | Paraboloide hiperbólico |
> | 2 | 0 | 0 | Cilindro elíptico |
> | 1 | 1 | 0 | Cilindro hiperbólico |
> | 1 | 0 | 0 | Cilindro parabólico |
> | 1 | 0 | 1 | Cono |
> 
> **Paso 5: Verificar casos especiales**
> 
> - Si todos los coeficientes cuadráticos son iguales → **Esfera** o **Cilindro circular**
> - Si el término constante es cero en una ecuación con 3 cuadráticos → **Cono**
> - Si solo hay términos lineales → **Plano**
> 
> ---
> 
> ### Ejemplo de Aplicación
> 
> **Identificar:** $4x^2 + y^2 - 16z = 0$
> 
> **Paso 1:** Reorganizar
> $$4x^2 + y^2 = 16z$$
> $$z = \frac{x^2}{4} + \frac{y^2}{16}$$
> 
> **Paso 2:** Contar signos
> - 2 términos cuadráticos positivos ($x^2$, $y^2$)
> - 0 términos cuadráticos negativos
> - 1 variable ausente ($z$ es lineal)
> 
> **Paso 3:** Consultar tabla
> → **Paraboloide elíptico**
> 
> **Verificación:** Se abre en dirección $+z$

---

## 🌟 Superficies de Nivel vs Gráficas

> [!note]- 🔄 Dos Perspectivas Diferentes
> 
> ### Confusión Común
> 
> Es importante distinguir entre:
> 
> **1. Gráfica de una función de dos variables**
> - Función: $z = f(x,y)$
> - Resulta en una **superficie en 3D**
> - Ejemplo: $z = x^2 + y^2$ es un paraboloide
> 
> **2. Superficie de nivel de una función de tres variables**
> - Función: $w = f(x,y,z)$
> - Para un nivel $k$: $f(x,y,z) = k$
> - Resulta en una **superficie en 3D**
> - Ejemplo: $x^2 + y^2 + z^2 = 1$ es una esfera
> 
> ---
> 
> ### Ejemplo Comparativo
> 
> **Como gráfica (función de 2 variables):**
> $$z = x^2 + y^2$$
> 
> - Dominio: $\mathbb{R}^2$ (plano $xy$)
> - Rango: $[0, \infty)$
> - Superficie: Paraboloide en 3D
> - **Curvas de nivel** (en el plano $xy$): $x^2 + y^2 = k$ (círculos)
> 
> **Como superficie de nivel (función de 3 variables):**
> $$f(x,y,z) = x^2 + y^2 + z^2$$
> $$x^2 + y^2 + z^2 = k$$
> 
> - Dominio: $\mathbb{R}^3$ (espacio)
> - Rango: $[0, \infty)$
> - **Superficies de nivel**: Esferas de radio $\sqrt{k}$
> 
> ---
> 
> ### Relación entre Curvas y Superficies de Nivel
> 
> **Conexión importante:**
> Si cortamos una superficie de nivel $f(x,y,z) = k$ con un plano (e.g., $z = c$), obtenemos una **curva** en ese plano.
> 
> **Ejemplo:**
> - Superficie de nivel: $x^2 + y^2 + z^2 = 9$ (esfera de radio 3)
> - Corte con plano $z = 0$: $x^2 + y^2 = 9$ (círculo de radio 3)
> - Corte con plano $z = 2$: $x^2 + y^2 = 5$ (círculo de radio $\sqrt{5}$)
> - Corte con plano $z = 3$: $x^2 + y^2 = 0$ (punto)

---

## 🔬 Gradiente y Superficies de Nivel

> [!info]- 📐 Relación Fundamental
> 
> ### Teorema del Gradiente
> 
> **Teorema:**
> El vector gradiente $\nabla f(x_0, y_0, z_0)$ es **perpendicular** (normal) a la superficie de nivel que pasa por el punto $(x_0, y_0, z_0)$.
> 
> $$\nabla f \perp S_k \text{ en cada punto de } S_k$$
> 
> **Demostración intuitiva:**
> 
> Si nos movemos sobre la superficie de nivel, $f$ permanece constante, por lo que $df = 0$.
> 
> Usando la diferencial total:
> $$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \frac{\partial f}{\partial z}dz = \nabla f \cdot d\vec{r} = 0$$
> 
> Esto significa que $\nabla f$ es perpendicular a cualquier desplazamiento tangente $d\vec{r}$ sobre la superficie.
> 
> ---
> 
> ### Vector Normal a una Superficie
> 
> **Definición:**
> Si la superficie está dada por $f(x,y,z) = k$, entonces un vector normal en el punto $(x_0, y_0, z_0)$ es:
> 
> $$\vec{n} = \nabla f(x_0, y_0, z_0) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right)$$
> 
> **Aplicación: Plano tangente**
> 
> El plano tangente a la superficie $f(x,y,z) = k$ en el punto $(x_0, y_0, z_0)$ tiene ecuación:
> 
> $$\frac{\partial f}{\partial x}(x_0, y_0, z_0)(x - x_0) + \frac{\partial f}{\partial y}(x_0, y_0, z_0)(y - y_0) + \frac{\partial f}{\partial z}(x_0, y_0, z_0)(z - z_0) = 0$$
> 
> O más compactamente:
> $$\nabla f(x_0, y_0, z_0) \cdot (x - x_0, y - y_0, z - z_0) = 0$$
> 
> ---
> 
> ### Ejemplo
> 
> **Superficie:** $f(x,y,z) = x^2 + y^2 + z^2 = 9$ (esfera de radio 3)
> 
> **Punto:** $(1, 2, 2)$ (verificar: $1 + 4 + 4 = 9$ ✓)
> 
> **Gradiente:**
> $$\nabla f = (2x, 2y, 2z)$$
> $$\nabla f(1, 2, 2) = (2, 4, 4)$$
> 
> **Interpretación:**
> - El vector $(2, 4, 4)$ es perpendicular a la esfera en el punto $(1, 2, 2)$
> - Apunta radialmente hacia afuera
> - Es paralelo al vector de posición $(1, 2, 2)$ (multiplicado por 2)
> 
> **Plano tangente:**
> $$2(x - 1) + 4(y - 2) + 4(z - 2) = 0$$
> $$2x + 4y + 4z = 18$$
> $$x + 2y + 2z = 9$$

---

## 📊 Aplicaciones Físicas y Científicas

> [!example]- 🌍 Casos del Mundo Real
> 
> ### 1. Física: Superficies Equipotenciales
> 
> **Potencial eléctrico de una carga puntual:**
> $$V(x,y,z) = \frac{kQ}{\sqrt{x^2 + y^2 + z^2}}$$
> 
> **Superficies equipotenciales:** $V = $ constante
> $$\frac{kQ}{\sqrt{x^2 + y^2 + z^2}} = V_0$$
> $$x^2 + y^2 + z^2 = \left(\frac{kQ}{V_0}\right)^2$$
> 
> → **Esferas concéntricas** alrededor de la carga
> 
> **Campo eléctrico:**
> - $\vec{E} = -\nabla V$
> - El campo es perpendicular a las superficies equipotenciales
> - Líneas de campo son perpendiculares a las esferas (radiales)
> 
> ---
> 
> ### 2. Química: Orbitales Atómicos
> 
> **Densidad de probabilidad electrónica:**
> $$\rho(x,y,z) = |\psi(x,y,z)|^2$$
> 
> **Superficies de nivel:**
> - Regiones donde la probabilidad de encontrar el electrón es constante
> - Formas características: esféricas (orbital s), lobulares (orbital p), etc.
> 
> **Ejemplo: Orbital 1s del hidrógeno**
> $$\psi_{1s} = \frac{1}{\sqrt{\pi a_0^3}} e^{-r/a_0}$$
> 
> donde $r = \sqrt{x^2 + y^2 + z^2}$
> 
> Las superficies $|\psi|^2 = $ constante son **esferas concéntricas**
> 
> ---
> 
> ### 3. Meteorología: Superficies Isobáricas
> 
> **Presión atmosférica:** $P(x,y,z)$
> 
> **Superficies isobáricas:** $P(x,y,z) = P_0$ (constante)
> 
> - En la atmósfera estándar, aproximadamente horizontales
> - Ligeramente deformadas por sistemas meteorológicos
> - Importante para análisis de vientos en altura
> 
> **Uso en meteorología:**
> - Mapas de altura geopotencial en superficies de presión constante
> - Corrientes en chorro siguen gradientes de estas superficies
> 
> ---
> 
> ### 4. Geofísica: Geoide
> 
> **Potencial gravitacional terrestre:** $U(x,y,z)$
> 
> **Geoide:** Superficie equipotencial que mejor aproxima el nivel medio del mar
> 
> $$U(x,y,z) = U_0 \text{ (constante)}$$
> 
> **Características:**
> - Aproximadamente elipsoidal
> - Desviaciones debido a variaciones de densidad en la Tierra
> - Importante para geodesia y sistemas GPS
> 
> ---
> 
> ### 5. Ingeniería: Distribución de Temperatura
> 
> **Temperatura en un sólido:** $T(x,y,z)$
> 
> **Superficies isotérmicas:** $T(x,y,z) = T_0$
> 
> **Ley de Fourier:**
> El flujo de calor es perpendicular a las superficies isotérmicas:
> $$\vec{q} = -k\nabla T$$
> 
> **Aplicaciones:**
> - Diseño de sistemas de enfriamiento
> - Análisis térmico de componentes
> - Aislamiento de edificios
> 
> ---
> 
> ### 6. Medicina: Tomografía
> 
> **Densidad de tejido:** $\rho(x,y,z)$
> 
> **Superficies de nivel:**
> - Regiones de igual densidad en imágenes médicas (CT, MRI)
> - Visualización 3D de órganos y tumores
> - Segmentación de estructuras anatómicas
> 
> ---
> 
> ### 7. Economía: Funciones de Producción
> 
> **Función de producción con 3 insumos:**
> $$Q(K, L, M) = \text{producción}$$
> 
> donde $K$ = capital, $L$ = trabajo, $M$ = materiales
> 
> **Superficies isocuánticas:** $Q(K, L, M) = Q_0$
> 
> - Combinaciones de insumos que producen la misma cantidad
> - Decisiones de optimización en producción
> - Análisis de eficiencia

---

## 🎨 Visualización de Superficies de Nivel

> [!tip]- 🖼️ Técnicas de Representación
> 
> ### Método 1: Secciones Transversales
> 
> **Idea:** Cortar la superficie con planos paralelos y mostrar las curvas resultantes
> 
> **Ejemplo:** Esfera $x^2 + y^2 + z^2 = 9$
> 
> Cortes con planos $z = $ constante:
> - $z = 0$: Círculo $x^2 + y^2 = 9$ (radio 3)
> - $z = 1$: Círculo $x^2 + y^2 = 8$ (radio $\sqrt{8}$)
> - $z = 2$: Círculo $x^2 + y^2 = 5$ (radio $\sqrt{5}$)
> - $z = 3$: Punto $(0, 0, 3)$
> 
> **Ventaja:** Fácil de dibujar en papel
> 
> ---
> 
> ### Método 2: Proyecciones
> 
> **Mostrar vistas desde diferentes ángulos:**
> - Vista frontal (plano $xz$)
> - Vista lateral (plano $yz$)
> - Vista superior (plano $xy$)
> 
> **Útil para:** Entender la forma general sin visualización 3D completa
> 
> ---
> 
> ### Método 3: Mallas y Wireframe
> 
> **Representación computacional:**
> - Dibujar curvas sobre la superficie en dos direcciones
> - Crear una "malla" que muestra la forma
> 
> **Software:**
> - MATLAB: `isosurface()`
> - Python: `mplot3d`
> - Mathematica: `ContourPlot3D[]`
> - GeoGebra 3D
> 
> ---
> 
> ### Método 4: Superficies Semitransparentes
> 
> **Visualización moderna:**
> - Renderizar la superficie con transparencia
> - Permite ver múltiples superficies de nivel simultáneamente
> - Útil para comparar diferentes niveles
> 
> ---
> 
> ### Método 5: Codificación por Color
> 
> **Técnica avanzada:**
> - Asignar colores según el valor de otra variable
> - Ejemplo: temperatura en una superficie de presión constante
> - Combina información de múltiples funciones

---

## 🧮 Ejemplos Adicionales

> [!example]- 📐 Ejemplo 8: Función Exponencial
> 
> **Función:** $f(x,y,z) = e^{-(x^2+y^2+z^2)}$
> 
> **Dominio:** $\mathbb{R}^3$
> 
> **Rango:** $(0, 1]$
> 
> **Encontrar superficies de nivel:**
> 
> Plantear $f(x,y,z) = k$ con $0 < k \leq 1$:
> $$e^{-(x^2+y^2+z^2)} = k$$
> 
> Aplicar logaritmo natural:
> $$-(x^2 + y^2 + z^2) = \ln(k)$$
> $$x^2 + y^2 + z^2 = -\ln(k)$$
> 
> Como $0 < k \leq 1$, tenemos $\ln(k) \leq 0$, entonces $-\ln(k) \geq 0$ ✓
> 
> **Para diferentes valores de $k$:**
> - $k = 1$: $x^2 + y^2 + z^2 = 0$ → Punto $(0,0,0)$
> - $k = e^{-1} \approx 0.368$: Esfera de radio 1
> - $k = e^{-4} \approx 0.018$: Esfera de radio 2
> - $k = e^{-9} \approx 0.0001$: Esfera de radio 3
> 
> **Radio en función de $k$:**
> $$r = \sqrt{-\ln(k)}$$
> 
> **Observaciones:**
> - Superficies son esferas concéntricas
> - Espaciamiento logarítmico (crecimiento no uniforme)
> - Máximo en el origen
> - Decaimiento exponencial rápido
> 
> **Interpretación:**
> - Distribución gaussiana 3D (campana tridimensional)
> - Modelo de densidad de probabilidad en física estadística
> - Función de onda en mecánica cuántica

> [!example]- 🌀 Ejemplo 9: Función Lineal Combinada
> 
> **Función:** $f(x,y,z) = 2x + 3y - z$
> 
> **Dominio:** $\mathbb{R}^3$
> 
> **Rango:** $\mathbb{R}$
> 
> **Encontrar superficies de nivel:**
> 
> Plantear $f(x,y,z) = k$:
> $$2x + 3y - z = k$$
> $$z = 2x + 3y - k$$
> 
> **Para diferentes valores de $k$:**
> - $k = 0$: Plano $z = 2x + 3y$
> - $k = 1$: Plano $z = 2x + 3y - 1$
> - $k = -2$: Plano $z = 2x + 3y + 2$
> - $k = 5$: Plano $z = 2x + 3y - 5$
> 
> **Observaciones:**
> - Todas las superficies son **planos paralelos**
> - Vector normal común: $\nabla f = (2, 3, -1)$
> - Espaciamiento uniforme (función lineal)
> - Perpendiculares al vector $(2, 3, -1)$
> 
> **Forma vectorial:**
> $$\vec{n} \cdot \vec{r} = k$$
> 
> donde $\vec{n} = (2, 3, -1)$ y $\vec{r} = (x, y, z)$
> 
> **Interpretación:**
> - Cada plano es una traslación de los otros
> - Distancia entre planos consecutivos es constante
> - Modelo de campo uniforme en física

> [!example]- 🎭 Ejemplo 10: Función de Distancia a un Punto
> 
> **Función:** $f(x,y,z) = \sqrt{(x-1)^2 + (y+2)^2 + (z-3)^2}$
> 
> **Interpretación:** Distancia desde el punto $(1, -2, 3)$
> 
> **Dominio:** $\mathbb{R}^3$
> 
> **Rango:** $[0, +\infty)$
> 
> **Encontrar superficies de nivel:**
> 
> Plantear $f(x,y,z) = k$ con $k \geq 0$:
> $$\sqrt{(x-1)^2 + (y+2)^2 + (z-3)^2} = k$$
> $$(x-1)^2 + (y+2)^2 + (z-3)^2 = k^2$$
> 
> **Para diferentes valores de $k$:**
> - $k = 0$: Punto $(1, -2, 3)$
> - $k = 1$: Esfera de radio 1 centrada en $(1, -2, 3)$
> - $k = 2$: Esfera de radio 2 centrada en $(1, -2, 3)$
> - $k = 5$: Esfera de radio 5 centrada en $(1, -2, 3)$
> 
> **Observaciones:**
> - Esferas concéntricas centradas en $(1, -2, 3)$
> - Radio es exactamente $k$ (espaciamiento uniforme)
> - Todas las superficies pasan por puntos equidistantes del centro
> 
> **Aplicación:**
> - Ondas esféricas emanando de una fuente puntual
> - Señales de radio/radar desde una antena

> [!example]- 🏔️ Ejemplo 11: Función Producto
> 
> **Función:** $f(x,y,z) = xyz$
> 
> **Dominio:** $\mathbb{R}^3$
> 
> **Rango:** $\mathbb{R}$
> 
> **Encontrar superficies de nivel:**
> 
> Plantear $f(x,y,z) = k$:
> $$xyz = k$$
> 
> **Análisis:**
> 
> **Para $k = 0$:**
> $$xyz = 0$$
> 
> Se cumple cuando al menos una variable es cero:
> - Plano $x = 0$ (plano $yz$)
> - Plano $y = 0$ (plano $xz$)
> - Plano $z = 0$ (plano $xy$)
> 
> → **Tres planos coordenados**
> 
> **Para $k \neq 0$:**
> $$z = \frac{k}{xy}$$
> 
> Superficies más complejas (hiperbólicas)
> 
> **Secciones transversales:**
> - Si $z = c$ (constante): $xy = k/c$ → Hipérbolas rectangulares
> - Si $x = c$: $yz = k/c$ → Hipérbolas rectangulares
> - Si $y = c$: $xz = k/c$ → Hipérbolas rectangulares
> 
> **Observaciones:**
> - Superficie con múltiples componentes
> - Singularidad en los planos coordenados
> - Simetría respecto a intercambio de variables

> [!example]- 🌊 Ejemplo 12: Combinación de Paraboloides
> 
> **Función:** $f(x,y,z) = x^2 + y^2 - z^2$
> 
> **Dominio:** $\mathbb{R}^3$
> 
> **Rango:** $\mathbb{R}$
> 
> **Encontrar superficies de nivel:**
> 
> Plantear $f(x,y,z) = k$:
> $$x^2 + y^2 - z^2 = k$$
> 
> **Ya analizado en Ejemplo 5, con más detalle:**
> 
> **Para $k = 0$:**
> $$x^2 + y^2 = z^2$$
> 
> **Cono circular** (dos napas)
> 
> **Para $k > 0$:**
> $$\frac{x^2}{k} + \frac{y^2}{k} - \frac{z^2}{k} = 1$$
> 
> **Hiperboloide de una hoja**
> 
> Radio mínimo (en $z = 0$): $r_{min} = \sqrt{k}$
> 
> **Para $k < 0$ (sea $k = -c$ con $c > 0$):**
> $$x^2 + y^2 - z^2 = -c$$
> $$\frac{z^2}{c} - \frac{x^2}{c} - \frac{y^2}{c} = 1$$
> 
> **Hiperboloide de dos hojas**
> 
> Vértices en $z = \pm\sqrt{c}$
> 
> **Transición:**
> - $k < 0$: Dos hojas separadas
> - $k = 0$: Cono (superficie límite)
> - $k > 0$: Una hoja continua
> 
> **Interpretación física:**
> - Superficies de fase constante en ondas
> - Frentes de onda en medios no uniformes

---

## 📝 Ejercicios Propuestos

> [!example]- 💪 Práctica Guiada
> 
> ### Nivel Básico
> 
> **1. Identificar y describir las superficies de nivel:**
> 
> a) $f(x,y,z) = x + 2y + 3z$ para $k = 0, 6, -3$
> 
> b) $f(x,y,z) = x^2 + y^2 + z^2$ para $k = 1, 4, 9, 16$
> 
> c) $f(x,y,z) = z$ para $k = -2, 0, 3, 5$
> 
> d) $f(x,y,z) = x^2 + y^2$ para $k = 0, 1, 4$
> 
> e) $f(x,y,z) = |z|$ para $k = 0, 1, 2$
> 
> ---
> 
> **2. Verificar si los puntos están en la superficie de nivel indicada:**
> 
> Para $f(x,y,z) = x^2 + y^2 + z^2$, nivel $k = 25$:
> 
> a) $(3, 4, 0)$
> b) $(0, 0, 5)$
> c) $(2, 3, 4)$
> d) $(1, 2, 2\sqrt{5})$
> 
> ---
> 
> ### Nivel Intermedio
> 
> **3. Encontrar y clasificar las superficies de nivel:**
> 
> a) $f(x,y,z) = \frac{x^2}{4} + \frac{y^2}{9} + z^2$ para $k = 1, 4$
> 
> b) $f(x,y,z) = z - x^2 - y^2$ para $k = 0, 2, -1$
> 
> c) $f(x,y,z) = x^2 + y^2 - z^2$ para $k = -1, 0, 1$
> 
> d) $f(x,y,z) = xyz$ para $k = 0, 1, -1, 8$
> 
> e) $f(x,y,z) = e^{-z} \sin(\sqrt{x^2+y^2})$ para $k = 0$
> 
> ---
> 
> **4. Calcular el gradiente y vector normal:**
> 
> Para cada función y punto, calcular $\nabla f$ y dar la ecuación del plano tangente:
> 
> a) $f(x,y,z) = x^2 + y^2 + z^2 = 9$ en $(2, 2, 1)$
> 
> b) $f(x,y,z) = x^2 + 2y^2 - z = 0$ en $(1, 1, 3)$
> 
> c) $f(x,y,z) = xyz = 6$ en $(1, 2, 3)$
> 
> ---
> 
> **5. Análisis de secciones transversales:**
> 
> Para $f(x,y,z) = x^2 - y^2 + z^2 = 1$:
> 
> a) Encontrar la curva de intersección con el plano $z = 0$
> b) Encontrar la curva de intersección con el plano $y = 0$
> c) Encontrar la curva de intersección con el plano $x = 0$
> d) Clasificar la superficie
> 
> ---
> 
> ### Nivel Avanzado
> 
> **6. Superficies complejas:**
> 
> a) $f(x,y,z) = x^2 + y^2 + z^2 - 2x - 4y + 6z$ para $k = 0$
> (Sugerencia: completar cuadrados)
> 
> b) $f(x,y,z) = \frac{1}{\sqrt{x^2+y^2+z^2}}$ para diferentes valores de $k > 0$
> 
> c) $f(x,y,z) = \sin(x)\cos(y)e^z$ para $k = 0$
>
> d) $f(x,y,z) = \ln(x^2 + y^2 + z^2)$ para $k = 0, 1, 2$
> 
> ---
> 
> **7. Aplicaciones físicas:**
> 
> a) El potencial eléctrico de dos cargas puntuales iguales en $(-1,0,0)$ y $(1,0,0)$ es: $$V(x,y,z) = \frac{k}{\sqrt{(x+1)^2+y^2+z^2}} + \frac{k}{\sqrt{(x-1)^2+y^2+z^2}}$$ Describe cualitativamente las superficies equipotenciales.
> 
> b) La temperatura en un sólido es $T(x,y,z) = 100 - x^2 - y^2 - z^2$. Encuentra las superficies isotérmicas para $T = 100, 75, 50, 0$.
> 
> c) La densidad de un gas es $\rho(x,y,z) = e^{-z/(x^2+y^2+1)}$. Describe las superficies de densidad constante.
> 
> ---
> 
> **8. Problemas de optimización con restricciones:**
> 
> a) Encuentra los puntos sobre la esfera $x^2 + y^2 + z^2 = 9$ más cercanos y lejanos al punto $(1, 2, 2)$.
> 
> b) Encuentra el volumen del sólido acotado por la superficie de nivel $f(x,y,z) = x^2 + y^2 + z^2 = 4$.
> 
> c) Una superficie de nivel es $x^2 + y^2 - z = 0$. Encuentra el punto sobre esta superficie más cercano al origen.
> 
> ---
> 
> **9. Análisis topológico:**
> 
> a) ¿Para qué valores de $k$ la superficie $x^2 + y^2 - z^2 = k$ es conexa (una sola pieza)?
> 
> b) Describe cómo cambia la topología de las superficies de nivel de $f(x,y,z) = z^3 - 3z + x^2 + y^2$ al variar $k$.
> 
> c) Para $f(x,y,z) = (x^2+y^2-1)(z^2-4)$, describe las superficies para $k = -4, 0, 4$.
> 
> ---
> 
> **10. Relación entre funciones:**
> 
> a) Si $g(x,y,z) = [f(x,y,z)]^2$ donde $f(x,y,z) = x^2 + y^2 + z^2$, ¿cómo se relacionan las superficies de nivel de $f$ y $g$?
> 
> b) Si $h(x,y,z) = f(x,y,z) + c$ (constante), ¿cómo se relacionan las superficies de nivel de $h$ y $f$?

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas de Ejercicios Básicos
> 
> **1a)** $f(x,y,z) = x + 2y + 3z$
> 
> Superficies de nivel $x + 2y + 3z = k$:
> 
> - $k = 0$: Plano $x + 2y + 3z = 0$ (pasa por el origen)
> - $k = 6$: Plano $x + 2y + 3z = 6$
> - $k = -3$: Plano $x + 2y + 3z = -3$
> 
> **Resultado:** Planos paralelos con vector normal $\vec{n} = (1, 2, 3)$
> 
> ---
> 
> **1b)** $f(x,y,z) = x^2 + y^2 + z^2$
> 
> Superficies de nivel $x^2 + y^2 + z^2 = k$:
> 
> - $k = 1$: Esfera de radio 1
> - $k = 4$: Esfera de radio 2
> - $k = 9$: Esfera de radio 3
> - $k = 16$: Esfera de radio 4
> 
> **Resultado:** Esferas concéntricas centradas en el origen
> 
> ---
> 
> **1c)** $f(x,y,z) = z$
> 
> Superficies de nivel $z = k$:
> 
> - $k = -2$: Plano horizontal $z = -2$
> - $k = 0$: Plano $xy$ ($z = 0$)
> - $k = 3$: Plano horizontal $z = 3$
> - $k = 5$: Plano horizontal $z = 5$
> 
> **Resultado:** Planos horizontales paralelos
> 
> ---
> 
> **1d)** $f(x,y,z) = x^2 + y^2$
> 
> Superficies de nivel $x^2 + y^2 = k$:
> 
> - $k = 0$: Eje $z$ (línea)
> - $k = 1$: Cilindro circular de radio 1, eje en $z$
> - $k = 4$: Cilindro circular de radio 2, eje en $z$
> 
> **Resultado:** Cilindros circulares concéntricos
> 
> ---
> 
> **1e)** $f(x,y,z) = |z|$
> 
> Superficies de nivel $|z| = k$:
> 
> - $k = 0$: $|z| = 0$ → Plano $xy$ ($z = 0$)
> - $k = 1$: $|z| = 1$ → Dos planos: $z = 1$ y $z = -1$
> - $k = 2$: $|z| = 2$ → Dos planos: $z = 2$ y $z = -2$
> 
> **Resultado:** Pares de planos horizontales simétricos respecto al plano $xy$
> 
> ---
> 
> **2)** Para $f(x,y,z) = x^2 + y^2 + z^2 = 25$:
> 
> a) $(3, 4, 0)$: $9 + 16 + 0 = 25$ ✅ **Sí está**
> 
> b) $(0, 0, 5)$: $0 + 0 + 25 = 25$ ✅ **Sí está**
> 
> c) $(2, 3, 4)$: $4 + 9 + 16 = 29 \neq 25$ ❌ **No está**
> 
> d) $(1, 2, 2\sqrt{5})$: $1 + 4 + 20 = 25$ ✅ **Sí está**

> [!success]- 🔑 Respuestas de Ejercicios Intermedios
> 
> **3a)** $f(x,y,z) = \frac{x^2}{4} + \frac{y^2}{9} + z^2$
> 
> Para $k = 1$: $$\frac{x^2}{4} + \frac{y^2}{9} + z^2 = 1$$
> 
> **Elipsoide** con semiejes $a = 2$, $b = 3$, $c = 1$
> 
> Para $k = 4$: $$\frac{x^2}{16} + \frac{y^2}{36} + \frac{z^2}{4} = 1$$
> 
> **Elipsoide** con semiejes $a = 4$, $b = 6$, $c = 2$
> 
> ---
> 
> **3b)** $f(x,y,z) = z - x^2 - y^2$
> 
> Para $k = 0$: $z = x^2 + y^2$ → **Paraboloide circular** (vértice en origen)
> 
> Para $k = 2$: $z = x^2 + y^2 + 2$ → **Paraboloide circular** (vértice en $(0,0,2)$)
> 
> Para $k = -1$: $z = x^2 + y^2 - 1$ → **Paraboloide circular** (vértice en $(0,0,-1)$)
> 
> ---
> 
> **3c)** $f(x,y,z) = x^2 + y^2 - z^2$
> 
> Ya analizado extensamente:
> 
> - $k = -1$: Hiperboloide de dos hojas
> - $k = 0$: Cono circular
> - $k = 1$: Hiperboloide de una hoja
> 
> ---
> 
> **4a)** $f(x,y,z) = x^2 + y^2 + z^2$, punto $(2, 2, 1)$
> 
> **Gradiente:** $$\nabla f = (2x, 2y, 2z)$$ $$\nabla f(2,2,1) = (4, 4, 2)$$
> 
> **Plano tangente:** $$4(x - 2) + 4(y - 2) + 2(z - 1) = 0$$ $$4x + 4y + 2z = 18$$ $$2x + 2y + z = 9$$
> 
> **Simplificado:** $2x + 2y + z = 9$
> 
> ---
> 
> **4b)** $f(x,y,z) = x^2 + 2y^2 - z$, punto $(1, 1, 3)$
> 
> Verificar que está en la superficie: $1 + 2 - 3 = 0$ ✓
> 
> **Gradiente:** $$\nabla f = (2x, 4y, -1)$$ $$\nabla f(1,1,3) = (2, 4, -1)$$
> 
> **Plano tangente:** $$2(x - 1) + 4(y - 1) - 1(z - 3) = 0$$ $$2x + 4y - z = 3$$
> 
> ---
> 
> **4c)** $f(x,y,z) = xyz$, punto $(1, 2, 3)$
> 
> Verificar: $1 \cdot 2 \cdot 3 = 6$ ✓
> 
> **Gradiente:** $$\nabla f = (yz, xz, xy)$$ $$\nabla f(1,2,3) = (6, 3, 2)$$
> 
> **Plano tangente:** $$6(x - 1) + 3(y - 2) + 2(z - 3) = 0$$ $$6x + 3y + 2z = 18$$
> 
> ---
> 
> **5)** Para $f(x,y,z) = x^2 - y^2 + z^2 = 1$:
> 
> a) Intersección con $z = 0$: $$x^2 - y^2 = 1$$ **Hipérbola** (eje focal en $x$)
> 
> b) Intersección con $y = 0$: $$x^2 + z^2 = 1$$ **Círculo** de radio 1
> 
> c) Intersección con $x = 0$: $$-y^2 + z^2 = 1$$ $$z^2 - y^2 = 1$$ **Hipérbola** (eje focal en $z$)
> 
> d) **Clasificación:** Hiperboloide de una hoja
> 
> - 2 términos positivos ($x^2$, $z^2$)
> - 1 término negativo ($-y^2$)
> - Constante positiva

> [!success]- 🔑 Respuestas de Ejercicios Avanzados
> 
> **6a)** $f(x,y,z) = x^2 + y^2 + z^2 - 2x - 4y + 6z = 0$
> 
> **Completar cuadrados:** $$(x^2 - 2x + 1) + (y^2 - 4y + 4) + (z^2 + 6z + 9) = 1 + 4 + 9$$ $$(x - 1)^2 + (y - 2)^2 + (z + 3)^2 = 14$$
> 
> **Resultado:** Esfera de radio $\sqrt{14}$ centrada en $(1, 2, -3)$
> 
> ---
> 
> **6b)** $f(x,y,z) = \frac{1}{\sqrt{x^2+y^2+z^2}}$
> 
> Superficies de nivel: $$\frac{1}{\sqrt{x^2+y^2+z^2}} = k$$ $$\sqrt{x^2+y^2+z^2} = \frac{1}{k}$$ $$x^2 + y^2 + z^2 = \frac{1}{k^2}$$
> 
> **Esferas** de radio $r = \frac{1}{k}$
> 
> A medida que $k$ aumenta, el radio disminuye (relación inversa)
> 
> ---
> 
> **6d)** $f(x,y,z) = \ln(x^2 + y^2 + z^2)$
> 
> Superficies de nivel: $$\ln(x^2 + y^2 + z^2) = k$$ $$x^2 + y^2 + z^2 = e^k$$
> 
> Para diferentes valores de $k$:
> 
> - $k = 0$: $x^2 + y^2 + z^2 = 1$ → Esfera de radio 1
> - $k = 1$: $x^2 + y^2 + z^2 = e$ → Esfera de radio $\sqrt{e}$
> - $k = 2$: $x^2 + y^2 + z^2 = e^2$ → Esfera de radio $e$
> 
> **Esferas** con espaciamiento exponencial
> 
> ---
> 
> **7b)** $T(x,y,z) = 100 - x^2 - y^2 - z^2$
> 
> Isotermas $100 - x^2 - y^2 - z^2 = T$: $$x^2 + y^2 + z^2 = 100 - T$$
> 
> - $T = 100$: Punto $(0,0,0)$ (temperatura máxima)
> - $T = 75$: Esfera de radio 5
> - $T = 50$: Esfera de radio $\sqrt{50} = 5\sqrt{2}$
> - $T = 0$: Esfera de radio 10
> 
> **Interpretación:**
> 
> - Temperatura máxima en el centro
> - Decrece radialmente hacia afuera
> - Isotermas son esferas concéntricas
> 
> ---
> 
> **9a)** $x^2 + y^2 - z^2 = k$
> 
> - **$k < 0$:** Hiperboloide de dos hojas (dos componentes) → **No conexa**
> - **$k = 0$:** Cono (vértice conecta las napas) → **Conexa** (técnicamente)
> - **$k > 0$:** Hiperboloide de una hoja → **Conexa**
> 
> **Respuesta:** Conexa para $k \geq 0$
> 
> ---
> 
> **10a)** Si $g(x,y,z) = [f(x,y,z)]^2$ donde $f(x,y,z) = x^2 + y^2 + z^2$:
> 
> Superficies de $f$: $x^2 + y^2 + z^2 = k$ (esferas de radio $\sqrt{k}$)
> 
> Superficies de $g$: $(x^2 + y^2 + z^2)^2 = k'$ $$x^2 + y^2 + z^2 = \sqrt{k'}$$
> 
> **Relación:** Las superficies de $g$ para nivel $k'$ coinciden con las de $f$ para nivel $\sqrt{k'}$
> 
> **Diferencia:** El espaciamiento cambia (no lineal)
> 
> ---
> 
> **10b)** Si $h(x,y,z) = f(x,y,z) + c$:
> 
> Superficies de $h$: $f(x,y,z) + c = k_h$ $$f(x,y,z) = k_h - c$$
> 
> **Relación:** Las superficies de $h$ para nivel $k_h$ son idénticas a las de $f$ para nivel $k_f = k_h - c$
> 
> **Conclusión:** Las superficies son las mismas, solo los valores de nivel están desplazados por $c$

---

## 🎓 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Importantes
> 
> **Sobre Superficies de Nivel:**
> 
> 1. ✅ Son conjuntos donde $f(x,y,z) = k$ (constante) en el espacio 3D
> 2. ✅ Permiten visualizar funciones de 3 variables sin necesitar 4D
> 3. ✅ Para funciones continuas, superficies de niveles diferentes **no se intersectan**
> 4. ✅ El **gradiente es perpendicular** a las superficies de nivel
> 5. ✅ Son el análogo 3D de las curvas de nivel 2D
> 6. ✅ Superficies de nivel distintas pueden tener topologías diferentes
> 
> **Superficies Cuádricas Básicas:**
> 
> - 🔵 **Esfera:** $x^2 + y^2 + z^2 = r^2$
> - 🟢 **Elipsoide:** $\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$
> - 🔴 **Cilindro:** $x^2 + y^2 = r^2$ (independiente de $z$)
> - 🟡 **Cono:** $z^2 = x^2 + y^2$
> - 🟣 **Paraboloide:** $z = x^2 + y^2$
> - 🟠 **Hiperboloide (1 hoja):** $\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$
> - 🟤 **Hiperboloide (2 hojas):** $\frac{z^2}{c^2} - \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$
> - ⚪ **Plano:** $ax + by + cz = d$
> 
> **Gradiente y Geometría:**
> 
> - 📐 $\nabla f$ es **normal** a la superficie de nivel
> - 📐 $|\nabla f|$ mide la **tasa de cambio** máxima
> - 📐 Dirección de $\nabla f$ apunta hacia valores **crecientes** de $f$
> - 📐 El plano tangente usa $\nabla f$ como vector normal
> 
> **Aplicaciones:**
> 
> - ⚡ **Física:** Superficies equipotenciales, isotermas
> - 🧪 **Química:** Orbitales atómicos, densidad electrónica
> - 🌍 **Geofísica:** Geoide, capas de densidad
> - 🏥 **Medicina:** Segmentación en imágenes 3D
> - 📊 **Optimización:** Conjuntos de nivel en problemas con restricciones

---

## 🔧 Herramientas Computacionales

> [!info]- 💻 Software para Visualización
> 
> ### MATLAB/Octave
> 
> ```matlab
> % Crear malla 3D
> [X, Y, Z] = meshgrid(-5:0.2:5, -5:0.2:5, -5:0.2:5);
> 
> % Definir función
> F = X.^2 + Y.^2 + Z.^2;
> 
> % Graficar superficie de nivel
> isosurface(X, Y, Z, F, 9);  % nivel k=9
> axis equal
> xlabel('x'); ylabel('y'); zlabel('z');
> title('Superficie de nivel: x² + y² + z² = 9');
> ```
> 
> ### Python (Matplotlib)
> 
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> from mpl_toolkits.mplot3d import Axes3D
> from skimage import measure
> 
> # Crear malla
> x = np.linspace(-5, 5, 100)
> y = np.linspace(-5, 5, 100)
> z = np.linspace(-5, 5, 100)
> X, Y, Z = np.meshgrid(x, y, z)
> 
> # Definir función
> F = X**2 + Y**2 + Z**2
> 
> # Extraer superficie de nivel
> verts, faces, _, _ = measure.marching_cubes(F, level=9)
> 
> # Graficar
> fig = plt.figure()
> ax = fig.add_subplot(111, projection='3d')
> ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2],
>                 cmap='viridis', alpha=0.7)
> plt.show()
> ```
> 
> ### Mathematica
> 
> ```mathematica
> (* Graficar superficie de nivel *)
> ContourPlot3D[x^2 + y^2 + z^2 == 9, 
>   {x, -4, 4}, {y, -4, 4}, {z, -4, 4},
>   Mesh -> None,
>   ContourStyle -> Opacity[0.7]]
> 
> (* Múltiples superficies *)
> ContourPlot3D[x^2 + y^2 + z^2, 
>   {x, -5, 5}, {y, -5, 5}, {z, -5, 5},
>   Contours -> {1, 4, 9, 16},
>   ContourStyle -> Opacity[0.5]]
> ```
> 
> ### GeoGebra 3D
> 
> - Interfaz gráfica interactiva
> - Entrada de ecuaciones implícitas
> - Rotación y zoom en tiempo real
> - Ideal para exploración educativa
> 
> ### Ventajas de Visualización Computacional
> 
> - ✅ Visualización de geometrías complejas
> - ✅ Múltiples superficies simultáneas
> - ✅ Transparencia y colores para claridad
> - ✅ Rotación interactiva (comprensión 3D)
> - ✅ Animaciones del cambio de nivel
> - ✅ Exportación de imágenes de alta calidad

---

## 🌐 Extensión a Dimensiones Superiores

> [!info]- 🚀 Hipersuperficies de Nivel
> 
> ### Concepto General
> 
> Para una función de $n$ variables $f: \mathbb{R}^n \to \mathbb{R}$, el conjunto de nivel es una **hipersuperficie** de dimensión $(n-1)$ en $\mathbb{R}^n$.
> 
> |Función|Dimensión del dominio|Dimensión del conjunto de nivel|Nombre|
> |---|---|---|---|
> |$f(x)$|1D|0D|Punto|
> |$f(x,y)$|2D|1D|Curva|
> |$f(x,y,z)$|3D|2D|Superficie|
> |$f(x,y,z,w)$|4D|3D|Hipersuperficie|
> |$f(x_1,...,x_n)$|$n$D|$(n-1)$D|Hipersuperficie|
> 
> ### Ejemplo en 4D
> 
> **Función:** $f(x,y,z,w) = x^2 + y^2 + z^2 + w^2$
> 
> **Conjunto de nivel:** $x^2 + y^2 + z^2 + w^2 = k$
> 
> → **Hiperesfera** de dimensión 3 en el espacio 4D
> 
> (No podemos visualizarla directamente, pero podemos estudiar sus propiedades matemáticas)
> 
> ### Aplicaciones
> 
> - **Aprendizaje automático:** Superficies de decisión en espacios de alta dimensión
> - **Física teórica:** Variedades en teoría de cuerdas
> - **Optimización:** Conjuntos de nivel en problemas de muchas variables
> - **Estadística:** Regiones de confianza multivariadas

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌉 Relaciones
> 
> **Este tema se relaciona con:**
> 
> ### Ya estudiados:
> 
> - [[02 - Dominio y Rango]] - Las superficies existen solo en el dominio
> - [[04 - Curvas de Nivel]] - Las superficies de nivel son la extensión 3D
> 
> ### Por estudiar:
> 
> - **Derivadas parciales** - Necesarias para calcular el gradiente
> - **Gradiente** - Vector perpendicular a superficies de nivel
> - **Derivadas direccionales** - Tasa de cambio en cualquier dirección
> - **Plano tangente** - Usa el gradiente como vector normal
> - **Multiplicadores de Lagrange** - Optimización sobre superficies de nivel
> - **Integrales de superficie** - Integrar sobre superficies de nivel
> - **Teoremas integrales** - Divergencia, Stokes en superficies
> 
> **Conceptos avanzados:**
> 
> - **Geometría diferencial** - Curvatura de superficies de nivel
> - **Topología** - Clasificación de superficies
> - **Teoría de Morse** - Análisis de funciones vía conjuntos de nivel
> 
> **Próximo tema recomendado:** [[06 - Límites en Varias Variables]]

---

## 📖 Resumen Visual

> [!note]- 🎨 Guía Rápida de Superficies
> 
> ```
> FUNCIÓN              SUPERFICIE DE NIVEL          FORMA
> 
> x²+y²+z²=k²          ⚪                           Esfera
>                      ⚪⚪⚪
>                     ⚪⚪⚪⚪⚪
> 
> x²+y²=k²             ║║║                          Cilindro
>                      ║║║
>                      ║║║
> 
> z=k                  ========                    Plano
>                      ========                    horizontal
> 
> x²+y²-z²=k          
>   k>0:               ╲│╱                         Hiperboloide
>                      ─┼─                         (1 hoja)
>                      ╱│╲
> 
>   k<0:               ⚪                           Hiperboloide
>                      │                           (2 hojas)
>                      ⚪
> 
>   k=0:               ╲│╱                         Cono
>                      ─┼─
>                      ╱│╲
> 
> z=x²+y²+k            ╱^╲                         Paraboloide
>                     ╱   ╲
>                    ╱     ╲
> ```

---

## ✔️ Autoevaluación

> [!tip]- 📝 Verificación de Comprensión
> 
> **¿Puedes responder estas preguntas?**
> 
> 1. ✅ ¿Qué es una superficie de nivel y cómo se define matemáticamente?
> 2. ✅ ¿Cuál es la diferencia entre una superficie de nivel y la gráfica de una función?
> 3. ✅ ¿Por qué las superficies de nivel son útiles para funciones de 3 variables?
> 4. ✅ ¿Qué forma tienen las superficies de nivel de $f(x,y,z) = x^2 + y^2 + z^2$?
> 5. ✅ ¿Cómo identificar un hiperboloide de una hoja vs dos hojas?
> 6. ✅ ¿Qué relación tiene el gradiente con las superficies de nivel?
> 7. ✅ ¿Cómo encontrar el plano tangente a una superficie de nivel?
> 8. ✅ ¿Qué tipo de superficie es $x^2 + y^2 - z^2 = 0$?
> 9. ✅ ¿Pueden dos superficies de nivel diferentes intersectarse?
> 10. ✅ ¿Cómo se usan las superficies de nivel en aplicaciones físicas?
>
> **Si puedes responder todas con confianza, ¡estás listo para avanzar!**
> 
> ---
> 
> ### Checklist de Competencias
> 
> **Habilidades que deberías dominar:**
> 
> - [ ] Identificar el tipo de superficie cuádrica dada su ecuación
> - [ ] Encontrar superficies de nivel para diferentes valores de $k$
> - [ ] Clasificar superficies usando el método de contar signos
> - [ ] Completar cuadrados para llevar ecuaciones a forma estándar
> - [ ] Calcular el gradiente de una función de 3 variables
> - [ ] Encontrar el vector normal a una superficie en un punto
> - [ ] Escribir la ecuación del plano tangente
> - [ ] Determinar secciones transversales de superficies
> - [ ] Interpretar superficies de nivel en contextos físicos
> - [ ] Visualizar mentalmente superficies cuádricas básicas
> 
> **Si tienes dificultades con alguna, revisa la sección correspondiente.**

---

## 📚 Tabla de Referencia Rápida

> [!note]- 📋 Guía de Superficies Cuádricas Estándar
> 
> |Nombre|Ecuación Estándar|Características|Secciones Horizontales|Secciones Verticales|
> |---|---|---|---|---|
> |**Esfera**|$x^2 + y^2 + z^2 = r^2$|Centro en origen, radio $r$|Círculos|Círculos|
> |**Elipsoide**|$\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$|Cerrado, semiejes $a,b,c$|Elipses|Elipses|
> |**Cilindro Circular**|$x^2 + y^2 = r^2$|Eje paralelo a $z$|Círculos|Rectas paralelas|
> |**Cilindro Elíptico**|$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$|Eje paralelo a $z$|Elipses|Rectas paralelas|
> |**Cono**|$z^2 = x^2 + y^2$|Vértice en origen, dos napas|Círculos|Rectas que se cruzan|
> |**Paraboloide Elíptico**|$z = \frac{x^2}{a^2} + \frac{y^2}{b^2}$|Se abre en $+z$ o $-z$|Elipses|Parábolas|
> |**Paraboloide Hiperbólico**|$z = \frac{x^2}{a^2} - \frac{y^2}{b^2}$|Silla de montar|Hipérbolas|Parábolas|
> |**Hiperboloide 1 hoja**|$\frac{x^2}{a^2} + \frac{y^2}{b^2} - \frac{z^2}{c^2} = 1$|Una pieza continua|Elipses|Hipérbolas|
> |**Hiperboloide 2 hojas**|$\frac{z^2}{c^2} - \frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$|Dos componentes|Elipses (si $\|z\|>c$)|Hipérbolas|
> |**Plano**|$ax + by + cz = d$|Plano, normal $(a,b,c)$|Rectas|Rectas|

---

## 🎯 Estrategias de Resolución de Problemas

> [!tip]- 🧩 Metodología Paso a Paso
> 
> ### Problema Tipo 1: Identificar Superficie de Nivel
> 
> **Dado:** Ecuación $f(x,y,z) = k$
> 
> **Pasos:**
> 
> 1. **Contar términos cuadráticos:** ¿Cuántos hay? ¿Con qué signos?
> 2. **Identificar términos lineales:** ¿Alguna variable falta o es lineal?
> 3. **Completar cuadrados:** Si es necesario, llevar a forma estándar
> 4. **Consultar tabla de clasificación:** Usar conteo de signos
> 5. **Verificar casos especiales:** Esferas, cilindros, planos
> 6. **Determinar parámetros:** Radio, semiejes, vértice, etc.
> 7. **Describir geométricamente:** Ubicación, orientación, tamaño
> 
> ---
> 
> ### Problema Tipo 2: Encontrar Plano Tangente
> 
> **Dado:** Superficie $f(x,y,z) = k$ y punto $(x_0, y_0, z_0)$
> 
> **Pasos:**
> 
> 8. **Verificar que el punto está en la superficie:** $f(x_0, y_0, z_0) = k$
> 9. **Calcular derivadas parciales:** $\frac{\partial f}{\partial x}$, $\frac{\partial f}{\partial y}$, $\frac{\partial f}{\partial z}$
> 10. **Evaluar en el punto:** $\nabla f(x_0, y_0, z_0)$
> 11. **Escribir ecuación del plano:** $$\frac{\partial f}{\partial x}(x_0, y_0, z_0)(x - x_0) + \frac{\partial f}{\partial y}(x_0, y_0, z_0)(y - y_0) + \frac{\partial f}{\partial z}(x_0, y_0, z_0)(z - z_0) = 0$$
> 12. **Simplificar:** Expandir y reducir a forma estándar
> 
> ---
> 
> ### Problema Tipo 3: Analizar Secciones Transversales
> 
> **Dado:** Superficie y plano de corte
> 
> **Pasos:**
> 
> 13. **Sustituir la restricción del plano:** e.g., si $z = c$, sustituir en ecuación
> 14. **Simplificar la ecuación resultante:** Obtener ecuación en 2 variables
> 15. **Identificar la curva:** Círculo, elipse, hipérbola, parábola, recta, punto
> 16. **Determinar parámetros:** Radio, semiejes, vértice, etc.
> 17. **Repetir para varios valores:** Ver cómo cambia la sección
> 18. **Sintetizar:** Describir el patrón general
> 
> ---
> 
> ### Problema Tipo 4: Análisis Topológico
> 
> **Dado:** Familia de superficies para diferentes $k$
> 
> **Pasos:**
> 
> 19. **Identificar valores críticos de $k$:** Donde cambia la topología
> 20. **Analizar cada región:**
>     - $k < k_{crítico}$: ¿Qué tipo de superficie?
>     - $k = k_{crítico}$: ¿Superficie degenerada?
>     - $k > k_{crítico}$: ¿Qué tipo de superficie?
> 21. **Determinar conexidad:** ¿Una pieza o varias?
> 22. **Verificar continuidad:** ¿Transición suave entre niveles?
> 23. **Describir la transición:** Cómo evoluciona al variar $k$

---

## 🌟 Problemas Desafiantes

> [!example]- 🎓 Problemas de Nivel Superior
> 
> ### Problema Avanzado 1: Intersección de Superficies
> 
> Encuentra la curva de intersección entre:
> 
> - Esfera: $x^2 + y^2 + z^2 = 9$
> - Cilindro: $x^2 + y^2 = 4$
> 
> **Solución:**
> 
> De la segunda ecuación: $x^2 + y^2 = 4$
> 
> Sustituir en la primera: $$4 + z^2 = 9$$ $$z^2 = 5$$ $$z = \pm\sqrt{5}$$
> 
> **Resultado:** Dos círculos de radio 2 en los planos $z = \sqrt{5}$ y $z = -\sqrt{5}$
> 
> Paramétricamente: $$x = 2\cos\theta, \quad y = 2\sin\theta, \quad z = \pm\sqrt{5}$$
> 
> ---
> 
> ### Problema Avanzado 2: Superficie de Nivel de Función Compuesta
> 
> Sea $f(x,y,z) = g(x^2 + y^2 + z^2)$ donde $g$ es diferenciable. Demuestra que todas las superficies de nivel son esferas concéntricas.
> 
> **Demostración:**
> 
> Superficie de nivel: $g(x^2 + y^2 + z^2) = k$
> 
> Si $g$ es invertible: $x^2 + y^2 + z^2 = g^{-1}(k) = R$ (constante)
> 
> Esto define una esfera de radio $\sqrt{R}$ centrada en el origen. ✓
> 
> ---
> 
> ### Problema Avanzado 3: Volumen Encerrado
> 
> Calcula el volumen del sólido encerrado por la superficie de nivel: $$\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1$$
> 
> **Solución:**
> 
> Esta es un elipsoide. El volumen es: $$V = \frac{4}{3}\pi abc$$
> 
> (Fórmula del volumen del elipsoide)
> 
> Para una esfera ($a = b = c = r$): $V = \frac{4}{3}\pi r^3$ ✓
> 
> ---
> 
> ### Problema Avanzado 4: Distancia Mínima
> 
> Encuentra la distancia mínima desde el origen hasta la superficie: $$x^2 + 2y^2 + 3z^2 = 6$$
> 
> **Solución:**
> 
> Reescribir: $$\frac{x^2}{6} + \frac{y^2}{3} + \frac{z^2}{2} = 1$$
> 
> Elipsoide con semiejes $a = \sqrt{6}$, $b = \sqrt{3}$, $c = \sqrt{2}$
> 
> La distancia mínima es el semieje menor: $\sqrt{2}$
> 
> Ocurre en los puntos $(0, 0, \pm\sqrt{2})$
> 
> ---
> 
> ### Problema Avanzado 5: Superficie Implícita
> 
> Analiza la superficie definida por: $$x^4 + y^4 + z^4 = 1$$
> 
> **Análisis:**
> 
> - No es cuádrica (términos de orden 4)
> - Simetría esférica (invariante bajo rotaciones)
> - Cerrada y acotada
> - Se parece a una esfera pero con "esquinas redondeadas"
> - Cuando $p \to \infty$ en $x^p + y^p + z^p = 1$, se acerca a un cubo
> - Para $p = 2$: esfera; $p = 4$: forma intermedia; $p \to \infty$: cubo

---

## 🔬 Aplicaciones Avanzadas

> [!info]- 🚀 Temas Avanzados
> 
> ### 1. Teoría de Morse
> 
> **Concepto:** Estudia cómo cambia la topología de las superficies de nivel al pasar por **puntos críticos** (donde $\nabla f = 0$).
> 
> **Ejemplo:** Para $f(x,y,z) = z^2 - x^2 - y^2$:
> 
> - $k < 0$: Hiperboloide de 2 hojas (2 componentes)
> - $k = 0$: Cono (las componentes se tocan en el origen - punto crítico)
> - $k > 0$: Hiperboloide de 1 hoja (1 componente)
> 
> El origen es un **punto de silla** donde la topología cambia.
> 
> ---
> 
> ### 2. Conjuntos Subnivel
> 
> **Definición:** El **conjunto subnivel** es: $$S_k = {(x,y,z) : f(x,y,z) \leq k}$$
> 
> (Incluye todo el interior, no solo la superficie)
> 
> **Aplicación:**
> 
> - Optimización: región factible
> - Probabilidad: regiones de alta probabilidad
> - Física: regiones con energía menor que $k$
> 
> ---
> 
> ### 3. Flujos de Gradiente
> 
> **Idea:** Seguir la dirección del gradiente $\nabla f$ para moverse entre superficies de nivel.
> 
> **Ecuación diferencial:** $$\frac{d\vec{r}}{dt} = \nabla f(\vec{r})$$
> 
> Las trayectorias son **perpendiculares** a las superficies de nivel.
> 
> **Aplicación:**
> 
> - Algoritmos de ascenso/descenso de gradiente
> - Líneas de campo en física
> 
> ---
> 
> ### 4. Superficie de Nivel como Variedad
> 
> **Geometría diferencial:** Una superficie de nivel regular (donde $\nabla f \neq 0$) es una **variedad diferenciable** de dimensión 2.
> 
> **Propiedades:**
> 
> - Se puede parametrizar localmente
> - Tiene plano tangente en cada punto
> - Se puede calcular curvatura
> 
> ---
> 
> ### 5. Método de Multiplicadores de Lagrange
> 
> **Problema:** Optimizar $g(x,y,z)$ sujeto a restricción $f(x,y,z) = k$
> 
> **Método:** En el óptimo: $\nabla g = \lambda \nabla f$ (gradientes paralelos)
> 
> **Interpretación geométrica:**
> 
> - El óptimo ocurre donde una superficie de nivel de $g$ es **tangente** a la superficie de nivel de $f$
> - Los gradientes son paralelos en el punto de tangencia

---

## 📖 Problemas Integrados

> [!example]- 🌐 Problemas que Combinan Conceptos
> 
> ### Problema Integral 1: Temperatura en un Sólido
> 
> La temperatura en un sólido esférico está dada por: $$T(x,y,z) = 100e^{-(x^2+y^2+z^2)}$$
> 
> a) Describe las superficies isotérmicas b) ¿Dónde está la temperatura máxima? c) Calcula $\nabla T$ en el punto $(1,0,0)$ d) ¿En qué dirección aumenta la temperatura más rápidamente desde $(1,0,0)$? e) Encuentra la ecuación del plano tangente a la isoterma $T = 100e^{-1}$ en $(1,0,0)$
> 
> **Soluciones:**
> 
> a) Isotermas: $100e^{-(x^2+y^2+z^2)} = T_0$ $$x^2 + y^2 + z^2 = -\ln(T_0/100)$$ Esferas concéntricas en el origen
> 
> b) Máximo en $(0,0,0)$ donde $T = 100$
> 
> c) $\nabla T = -200(x,y,z)e^{-(x^2+y^2+z^2)}$ $\nabla T(1,0,0) = -200(1,0,0)e^{-1} = (-200e^{-1}, 0, 0)$
> 
> d) Dirección de $\nabla T$: hacia $(-1,0,0)$ (hacia el origen) La temperatura aumenta hacia el centro
> 
> e) Plano tangente en $(1,0,0)$ para $T = 100e^{-1}$: $$-200e^{-1}(x-1) + 0(y-0) + 0(z-0) = 0$$ $$x = 1$$ (plano vertical)
> 
> ---
> 
> ### Problema Integral 2: Potencial Gravitacional
> 
> Dos masas iguales $M$ están ubicadas en $(0,0,1)$ y $(0,0,-1)$. El potencial gravitacional es: $$\Phi(x,y,z) = -\frac{GM}{\sqrt{x^2+y^2+(z-1)^2}} - \frac{GM}{\sqrt{x^2+y^2+(z+1)^2}}$$
> 
> a) Describe cualitativamente las superficies equipotenciales b) ¿Hay simetría? ¿De qué tipo? c) ¿Qué forma tienen cerca del plano $z = 0$?
> 
> **Respuestas:**
> 
> a) Superficies cerradas alrededor de ambas masas; forma de "cacahuate" o "mancuerna"
> 
> b) Simetría de revolución alrededor del eje $z$; simetría de reflexión respecto al plano $z = 0$
> 
> c) Cerca de $z = 0$, aproximadamente elipsoidales, aplastadas en dirección $z$

---

## 🎬 Conclusión y Próximos Pasos

> [!quote]- 🎓 Síntesis Final
> 
> ### Lo que has aprendido
> 
> En este capítulo has dominado:
> 
> ✅ **Concepto fundamental:** Superficies de nivel como visualización de funciones 3D
> 
> ✅ **Superficies cuádricas:** Identificación y clasificación completa
> 
> ✅ **Relación con geometría:** Gradiente perpendicular a superficies
> 
> ✅ **Aplicaciones:** Física, química, ingeniería, optimización
> 
> ✅ **Técnicas computacionales:** Visualización con software moderno
> 
> ### Habilidades desarrolladas
> 
> - 🎯 Identificar tipos de superficies a partir de ecuaciones
> - 🎯 Completar cuadrados y llevar a forma estándar
> - 🎯 Calcular gradientes y planos tangentes
> - 🎯 Analizar secciones transversales
> - 🎯 Interpretar aplicaciones físicas
> - 🎯 Resolver problemas integrados
> 
> ### Preparación para temas futuros
> 
> Las superficies de nivel son fundamentales para:
> 
> - **Límites y continuidad** en 3D
> - **Derivadas parciales** y el gradiente
> - **Optimización** con restricciones
> - **Integrales múltiples** sobre superficies
> - **Cálculo vectorial** avanzado
> 
> ### Próximo paso
> 
> **[[06 - Límites en Varias Variables]]**
> 
> Aprenderás sobre:
> 
> - Límites de funciones de 2 y 3 variables
> - Continuidad en espacios multidimensionales
> - Límites en trayectorias
> - Teoremas fundamentales

---

## 📚 Referencias y Recursos Adicionales

> [!quote]- 📖 Para Profundizar
> 
> ### Libros de Texto Recomendados
> 
> 1. **Stewart, Calculus** - Capítulo sobre funciones de varias variables
> 2. **Thomas' Calculus** - Sección de superficies cuádricas
> 3. **Marsden & Tromba, Vector Calculus** - Tratamiento geométrico profundo
> 4. **Apostol, Calculus Vol. II** - Enfoque riguroso
> 5. **Edwards & Penney, Multivariable Calculus** - Muchos ejemplos
> 
> ### Videos y Tutoriales
> 
> - **Khan Academy:** "Level surfaces and quadric surfaces"
> - **MIT OpenCourseWare:** Calculus III - Lecture on level surfaces
> - **3Blue1Brown:** Visualizing multivariable functions
> - **Paul's Online Math Notes:** Quadric surfaces guide
> 
> ### Software y Herramientas
> 
> - **GeoGebra 3D:** Exploración interactiva gratuita
> - **Wolfram Alpha:** "plot3d [ecuación]" para visualización rápida
> - **MATLAB/Octave:** Para análisis numérico serio
> - **Python + Matplotlib:** Visualización programática flexible
> 
> ### Sitios Web Útiles
> 
> - Math Insight (mathinsight.org): Visualizaciones interactivas
> - Paul's Online Math Notes: Guías detalladas
> - Wolfram MathWorld: Referencia enciclopédica
> - Wikipedia: Artículos sobre superficies cuádricas

---

**Tags:** #calculo-multivariable #superficies-de-nivel #funciones-tres-variables #cuadricas #gradiente #visualizacion-3D #geometria-analitica #aplicaciones-fisicas #elipsoide #hiperboloide #paraboloide #esfera #cilindro #cono



