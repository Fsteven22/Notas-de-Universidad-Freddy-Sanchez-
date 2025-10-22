# 📘 04 – Curvas de Nivel

## 🎯 Introducción

> [!info]- 💡 ¿Qué son las Curvas de Nivel?
> 
> Las **curvas de nivel** son una herramienta fundamental para visualizar funciones de dos variables $f(x,y)$ sin necesitar gráficos tridimensionales.
> 
> **Analogía del mundo real:**
> 
> - **Mapas topográficos:** Las líneas muestran puntos de igual altitud
> - **Mapas meteorológicos:** Isotermas (igual temperatura) e isobaras (igual presión)
> - **Mapas de contorno:** Representan montañas, valles y terrenos
> 
> **Idea intuitiva:** Si cortamos la superficie $z = f(x,y)$ con planos horizontales $z = k$ (constantes), las intersecciones proyectadas en el plano $xy$ forman las **curvas de nivel**.
> 
> **Ventaja principal:** Podemos visualizar una función tridimensional usando solo un gráfico bidimensional.

---

## 📐 Definición Formal

### 🔵 Curva de Nivel

> [!example]- 🟢 Definición: Curva de Nivel
> 
> **Definición formal:** Sea $f: D \subseteq \mathbb{R}^2 \to \mathbb{R}$ una función de dos variables. La **curva de nivel** de $f$ para el valor $k \in \mathbb{R}$ es el conjunto:
> 
> $$C_k = {(x,y) \in D : f(x,y) = k}$$
> 
> **En palabras:** Es el conjunto de todos los puntos $(x,y)$ en el dominio donde la función toma el mismo valor $k$.
> 
> **Notación alternativa:**
> 
> - Curvas de nivel también se llaman **curvas de contorno** o **líneas de contorno**
> - El valor $k$ se llama **nivel** o **altura**
> 
> **Observaciones importantes:**
> 
> 1. ✅ Cada curva de nivel corresponde a UN valor específico de $k$
> 2. ✅ Las curvas de nivel están en el plano $xy$ (no en el espacio)
> 3. ✅ Diferentes valores de $k$ producen diferentes curvas
> 4. ✅ Las curvas de nivel son las proyecciones de las "rebanadas" horizontales de la superficie

### 🎨 Mapa de Contorno

> [!example]- 🟡 Mapa de Contorno
> 
> **Definición:** Un **mapa de contorno** (o **diagrama de curvas de nivel**) es una colección de varias curvas de nivel de una función, graficadas en el mismo plano $xy$.
> 
> **Características:**
> 
> - Cada curva se etiqueta con su valor $k$ correspondiente
> - Las curvas se dibujan para valores de $k$ igualmente espaciados
> - Permite visualizar la "forma" de la superficie completa
> 
> **Convenciones de dibujo:**
> 
> - Líneas más cercanas → pendiente más pronunciada
> - Líneas más separadas → pendiente más suave
> - Curvas cerradas → máximos o mínimos locales
> - Valores crecientes hacia adentro → máximo local (colina)
> - Valores decrecientes hacia adentro → mínimo local (depresión)

---

## 📊 Interpretación Geométrica

> [!note]- 🎭 Relación entre Superficie y Curvas de Nivel
> 
> ### Proceso de Generación
> 
> **Paso 1:** Tenemos una superficie $z = f(x,y)$ en el espacio 3D
> 
> **Paso 2:** Cortamos la superficie con planos horizontales $z = k_1, z = k_2, z = k_3, ...$
> 
> **Paso 3:** Cada intersección forma una curva en el espacio
> 
> **Paso 4:** Proyectamos estas curvas verticalmente hacia abajo al plano $xy$
> 
> **Resultado:** Las proyecciones son las curvas de nivel
> 
> ---
> 
> ### Visualización
> 
> ```
> Vista 3D (lateral):          Vista desde arriba (plano xy):
> 
>         z                           y
>         |                           |
>     k₃  |----[~~~]                  |    ○ ← curva nivel k₃
>         |                           |   ○○○ ← curva nivel k₂
>     k₂  |---[~~~~~]                 |  ○○○○○ ← curva nivel k₁
>         |                           |
>     k₁  |--[~~~~~~~]                +------------- x
>         |                           
>     ----+----------- y              (Mapa de contorno)
>        /
>       /
>      x
> ```
> 
> **Lectura del mapa:**
> 
> - Curvas cerradas pequeñas → cima o valle pronunciado
> - Curvas más espaciadas → terreno plano
> - Curvas muy juntas → acantilado o pendiente empinada

---

## 🔍 Cómo Encontrar Curvas de Nivel

### 📝 Procedimiento General

> [!tip]- 🛠️ Pasos para Encontrar Curvas de Nivel
> 
> **Método sistemático:**
> 
> 1. **Fijar el nivel:** Elegir un valor $k$ específico
> 2. **Plantear la ecuación:** Resolver $f(x,y) = k$
> 3. **Simplificar:** Reducir la ecuación a su forma más simple
> 4. **Identificar la curva:** Reconocer qué tipo de curva es (recta, círculo, parábola, hipérbola, etc.)
> 5. **Repetir:** Hacer lo mismo para varios valores de $k$
> 6. **Graficar:** Dibujar todas las curvas en el mismo plano
> 
> **Consejo práctico:** Elige valores de $k$ igualmente espaciados (e.g., $k = 0, 1, 2, 3, ...$) para obtener una representación uniforme.

---

## 📚 Ejemplos Fundamentales

> [!example]- 📐 Ejemplo 1: Plano Inclinado
> 
> **Función:** $f(x,y) = x + y$
> 
> **Encontrar curvas de nivel:**
> 
> Plantear $f(x,y) = k$: $$x + y = k$$
> 
> Esta es la ecuación de una **recta** con pendiente $-1$ e intercepto $k$ en el eje $y$.
> 
> **Para diferentes valores de $k$:**
> 
> - $k = 0$: $x + y = 0$ → $y = -x$
> - $k = 1$: $x + y = 1$ → $y = 1 - x$
> - $k = 2$: $x + y = 2$ → $y = 2 - x$
> - $k = -1$: $x + y = -1$ → $y = -1 - x$
> 
> **Mapa de contorno:**
> 
> ```
>      y
>    3 |  /k=3
>      | /
>    2 |/k=2
>      /
>    1/k=1
>     /
>    /k=0
>   /|__________ x
>  / |
> k=-1
> ```
> 
> **Observaciones:**
> 
> - Todas las curvas son **rectas paralelas**
> - Espaciamiento uniforme (pendiente constante)
> - Representan un plano inclinado en 3D
> 
> **Superficie 3D:** Un plano que sube uniformemente en dirección noreste

> [!example]- 🎯 Ejemplo 2: Paraboloide Circular
> 
> **Función:** $f(x,y) = x^2 + y^2$
> 
> **Encontrar curvas de nivel:**
> 
> Plantear $f(x,y) = k$: $$x^2 + y^2 = k$$
> 
> **Análisis por casos:**
> 
> - **Si $k < 0$:** No hay solución (suma de cuadrados no puede ser negativa)
> - **Si $k = 0$:** $x^2 + y^2 = 0$ → Solo el punto $(0,0)$
> - **Si $k > 0$:** Círculo de radio $r = \sqrt{k}$ centrado en el origen
> 
> **Para diferentes valores de $k$:**
> 
> - $k = 0$: Punto $(0,0)$
> - $k = 1$: Círculo de radio 1
> - $k = 4$: Círculo de radio 2
> - $k = 9$: Círculo de radio 3
> 
> **Mapa de contorno:**
> 
> ```
>      y
>      |
>    3 |      ⚪ k=9
>      |    ⚪⚪⚪
>    2 |   ⚪   ⚪
>      |  ⚪ ⚪ ⚪  k=4
>    1 | ⚪  ⚪  ⚪
>      | ⚪ · ⚪   k=1
>   ---|⚪  ·  ⚪---|--- x
>   -1 | ⚪ · ⚪
>      |  ⚪ ⚪ ⚪
>   -2 |   ⚪   ⚪
>      |    ⚪⚪⚪
>   -3 |      ⚪
> ```
> 
> **Observaciones:**
> 
> - Curvas son **círculos concéntricos**
> - Radio aumenta con $\sqrt{k}$
> - El espaciamiento entre círculos disminuye a medida que $k$ aumenta
> - El centro $(0,0)$ es un **mínimo** (valores crecen hacia afuera)
> 
> **Superficie 3D:** Un paraboloide (como un tazón) que se abre hacia arriba

> [!example]- 🏔️ Ejemplo 3: Cono
> 
> **Función:** $f(x,y) = \sqrt{x^2 + y^2}$
> 
> **Encontrar curvas de nivel:**
> 
> Plantear $f(x,y) = k$: $$\sqrt{x^2 + y^2} = k$$
> 
> Elevar al cuadrado (válido para $k \geq 0$): $$x^2 + y^2 = k^2$$
> 
> **Para diferentes valores de $k$:**
> 
> - $k = 0$: Punto $(0,0)$
> - $k = 1$: Círculo de radio 1
> - $k = 2$: Círculo de radio 2
> - $k = 3$: Círculo de radio 3
> 
> **Diferencia con el Ejemplo 2:** Aquí el radio es directamente $k$ (no $\sqrt{k}$), entonces los círculos están **igualmente espaciados**.
> 
> **Observaciones:**
> 
> - Espaciamiento uniforme → pendiente constante
> - Todos los círculos centrados en origen
> - $k < 0$ no tiene sentido (raíz cuadrada)
> 
> **Superficie 3D:** Un cono circular recto con vértice en el origen

> [!example]- 🎪 Ejemplo 4: Paraboloide Hiperbólico (Silla de Montar)
> 
> **Función:** $f(x,y) = y^2 - x^2$
> 
> **Encontrar curvas de nivel:**
> 
> Plantear $f(x,y) = k$: $$y^2 - x^2 = k$$
> 
> **Análisis por casos:**
> 
> **Caso 1: $k > 0$** $$\frac{y^2}{k} - \frac{x^2}{k} = 1$$
> 
> Hipérbola con eje focal vertical (se abre arriba y abajo)
> 
> **Caso 2: $k < 0$** (sea $k = -c$ con $c > 0$) $$y^2 - x^2 = -c$$ $$\frac{x^2}{c} - \frac{y^2}{c} = 1$$
> 
> Hipérbola con eje focal horizontal (se abre izquierda y derecha)
> 
> **Caso 3: $k = 0$** $$y^2 - x^2 = 0$$ $$y^2 = x^2$$ $$y = \pm x$$
> 
> Dos **rectas que se cruzan** (las asíntotas de las hipérbolas)
> 
> **Para diferentes valores de $k$:**
> 
> - $k = -4$: Hipérbola horizontal $\frac{x^2}{4} - \frac{y^2}{4} = 1$
> - $k = -1$: Hipérbola horizontal $x^2 - y^2 = 1$
> - $k = 0$: Rectas $y = x$ e $y = -x$
> - $k = 1$: Hipérbola vertical $y^2 - x^2 = 1$
> - $k = 4$: Hipérbola vertical $\frac{y^2}{4} - \frac{x^2}{4} = 1$
> 
> **Mapa de contorno:**
> 
> ```
>      y
>      |  k=4
>    4 | ╱│╲
>      |╱ │ ╲
>    2 ╱  │  ╲
>      │╲ │ ╱│ k=1
>      │ ╲│╱ │
>   ───┼──┼──┼─── x (k=0)
>      │ ╱│╲ │
>      │╱ │ ╲│ k=-1
>   -2 ╲  │  ╱
>      |╲ │ ╱
>   -4 | ╲│╱
>      |  k=-4
> ```
> 
> **Observaciones:**
> 
> - En $k = 0$: Punto de silla (saddle point)
> - Para $k > 0$: Hipérbolas verticales
> - Para $k < 0$: Hipérbolas horizontales
> - Las rectas $y = \pm x$ son asíntotas comunes
> 
> **Superficie 3D:** Paraboloide hiperbólico, parece una silla de montar o una papa frita Pringles

> [!example]- 🌊 Ejemplo 5: Función Sinusoidal
> 
> **Función:** $f(x,y) = \sin(x) + \cos(y)$
> 
> **Rango:** $[-2, 2]$ (del documento anterior)
> 
> **Encontrar curvas de nivel:**
> 
> Plantear $f(x,y) = k$ con $-2 \leq k \leq 2$: $$\sin(x) + \cos(y) = k$$ $$\cos(y) = k - \sin(x)$$
> 
> Para que exista solución: $-1 \leq k - \sin(x) \leq 1$
> 
> **Características:**
> 
> - Curvas periódicas en ambas direcciones
> - Patrón ondulado
> - Se repite cada $2\pi$ en $x$ y en $y$
> 
> **Para valores específicos:**
> 
> - $k = 2$: Solo cuando $\sin(x) = 1$ y $\cos(y) = 1$ simultáneamente
>     - $x = \frac{\pi}{2} + 2\pi n$, $y = 2\pi m$
>     - Puntos aislados (máximos)
> - $k = 0$: Curva $\cos(y) = -\sin(x)$
> - $k = -2$: Puntos donde $\sin(x) = -1$ y $\cos(y) = -1$
>     - Puntos aislados (mínimos)
> 
> **Observación:** Las curvas forman un patrón de ondas cruzadas

> [!example]- 🎨 Ejemplo 6: Función Exponencial
> 
> **Función:** $f(x,y) = e^{-(x^2 + y^2)}$
> 
> **Rango:** $(0, 1]$ (del documento anterior)
> 
> **Encontrar curvas de nivel:**
> 
> Plantear $f(x,y) = k$ con $0 < k \leq 1$: $$e^{-(x^2 + y^2)} = k$$
> 
> Aplicar logaritmo natural: $$-(x^2 + y^2) = \ln(k)$$ $$x^2 + y^2 = -\ln(k)$$
> 
> Como $0 < k \leq 1$, tenemos $\ln(k) \leq 0$, entonces $-\ln(k) \geq 0$ ✓
> 
> **Para diferentes valores de $k$:**
> 
> - $k = 1$: $x^2 + y^2 = 0$ → Punto $(0,0)$ (máximo)
> - $k = e^{-1} \approx 0.368$: Círculo de radio $r = 1$
> - $k = e^{-4} \approx 0.018$: Círculo de radio $r = 2$
> - $k = e^{-9} \approx 0.0001$: Círculo de radio $r = 3$
> 
> **Observaciones:**
> 
> - Curvas son círculos concéntricos
> - Radio: $r = \sqrt{-\ln(k)}$
> - Círculos cada vez más espaciados (decrecimiento exponencial)
> - Centro es un máximo absoluto
> - Valores decrecen rápidamente al alejarse del origen
> 
> **Superficie 3D:** "Campana gaussiana" o montaña con cima en el origen

> [!example]- 🏞️ Ejemplo 7: Función Racional
> 
> **Función:** $f(x,y) = \frac{y}{x}$ para $x \neq 0$
> 
> **Encontrar curvas de nivel:**
> 
> Plantear $f(x,y) = k$: $$\frac{y}{x} = k$$ $$y = kx$$
> 
> **Para diferentes valores de $k$:**
> 
> - $k = 0$: $y = 0$ (eje $x$, sin incluir el origen)
> - $k = 1$: $y = x$ (diagonal principal)
> - $k = 2$: $y = 2x$ (recta con pendiente 2)
> - $k = -1$: $y = -x$ (diagonal secundaria)
> - $k = \frac{1}{2}$: $y = \frac{x}{2}$ (recta con pendiente 1/2)
> 
> **Mapa de contorno:**
> 
> ```
>      y
>      |    k=2
>      | ／
>      |／k=1
>   ───┼─────── x
>     ／|
>    ／ | k=-1
>   k=-2
> ```
> 
> **Observaciones:**
> 
> - Todas las curvas son **rectas que pasan por el origen**
> - La pendiente de cada recta es $k$
> - El origen $(0,0)$ NO está en el dominio
> - Cada recta tiene un "agujero" en el origen
> 
> **Superficie 3D:** Superficie tipo "silla" con una singularidad en el eje $x$

> [!example]- 🔷 Ejemplo 8: Elipsoide
> 
> **Función:** $f(x,y) = \frac{x^2}{9} + \frac{y^2}{4}$
> 
> **Encontrar curvas de nivel:**
> 
> Plantear $f(x,y) = k$: $$\frac{x^2}{9} + \frac{y^2}{4} = k$$
> 
> **Para $k > 0$:** Dividir por $k$: $$\frac{x^2}{9k} + \frac{y^2}{4k} = 1$$
> 
> Esta es una **elipse** con:
> 
> - Semieje horizontal: $a = 3\sqrt{k}$
> - Semieje vertical: $b = 2\sqrt{k}$
> 
> **Para diferentes valores de $k$:**
> 
> - $k = 0$: Punto $(0,0)$
> - $k = 1$: Elipse $\frac{x^2}{9} + \frac{y^2}{4} = 1$ (semiejes 3 y 2)
> - $k = 4$: Elipse con semiejes 6 y 4
> - $k = 9$: Elipse con semiejes 9 y 6
> 
> **Observaciones:**
> 
> - Todas las elipses concéntricas en el origen
> - Relación de aspecto constante: $\frac{a}{b} = \frac{3}{2}$
> - Centro es un mínimo
> 
> **Superficie 3D:** Paraboloide elíptico

---

## 🎯 Tipos de Curvas de Nivel Comunes

> [!note]- 📊 Catálogo de Formas
> 
> |Función|Ecuación de nivel|Tipo de curva|Ejemplo|
> |---|---|---|---|
> |$ax + by$|$ax + by = k$|Rectas paralelas|Plano inclinado|
> |$x^2 + y^2$|$x^2 + y^2 = k$|Círculos concéntricos|Paraboloide|
> |$\sqrt{x^2 + y^2}$|$x^2 + y^2 = k^2$|Círculos (espaciados uniformemente)|Cono|
> |$\frac{x^2}{a^2} + \frac{y^2}{b^2}$|$\frac{x^2}{a^2k} + \frac{y^2}{b^2k} = 1$|Elipses concéntricas|Paraboloide elíptico|
> |$y^2 - x^2$|$y^2 - x^2 = k$|Hipérbolas|Silla de montar|
> |$xy$|$xy = k$|Hipérbolas rectangulares|Superficie hiperbólica|
> |$\frac{y}{x}$|$y = kx$|Rectas por el origen|Superficie cónica|
> |$e^{-(x^2+y^2)}$|$x^2 + y^2 = -\ln(k)$|Círculos (espaciados exponencialmente)|Campana gaussiana|
> |$\sin(x) + \cos(y)$|Transcendental|Curvas onduladas|Superficie ondulada|

---

## 🔍 Información que Revelan las Curvas de Nivel

> [!tip]- 📖 Lectura e Interpretación
> 
> ### 1. Máximos y Mínimos
> 
> **Curvas cerradas concéntricas:**
> 
> - Valores **crecientes hacia adentro** → **Máximo local** (cima de montaña)
> - Valores **decrecientes hacia adentro** → **Mínimo local** (fondo de valle)
> 
> **Ejemplo:**
> 
> - $f(x,y) = -x^2 - y^2$: Círculos con valores decreciendo hacia afuera → máximo en origen
> - $f(x,y) = x^2 + y^2$: Círculos con valores creciendo hacia afuera → mínimo en origen
> 
> ---
> 
> ### 2. Pendiente de la Superficie
> 
> **Espaciamiento de curvas:**
> 
> - Curvas **muy juntas** → Pendiente **pronunciada** (acantilado)
> - Curvas **separadas** → Pendiente **suave** (terreno plano)
> - Espaciamiento **uniforme** → Pendiente **constante**
> 
> **Regla práctica:** La pendiente es inversamente proporcional a la distancia entre curvas de nivel consecutivas.
> 
> ---
> 
> ### 3. Puntos de Silla
> 
> **Características:**
> 
> - Curvas que se **cruzan** o forman **patrones en X**
> - Valores crecen en algunas direcciones y decrecen en otras
> - No es máximo ni mínimo
> 
> **Ejemplo:** $f(x,y) = y^2 - x^2$ tiene un punto de silla en $(0,0)$
> 
> ---
> 
> ### 4. Dirección de Mayor Cambio
> 
> **Gradiente:** La dirección perpendicular a las curvas de nivel indica la dirección de **máximo crecimiento**.
> 
> - **Perpendicular a las curvas** → dirección de cambio más rápido
> - **Tangente a las curvas** → dirección sin cambio (la función permanece constante)
> 
> ---
> 
> ### 5. Simetría
> 
> **Patrones de simetría en curvas:**
> 
> - **Simetría radial** (círculos) → función depende solo de la distancia al origen
> - **Simetría axial** → función tiene un eje de simetría
> - **Simetría periódica** → función se repite regularmente
> 
> ---
> 
> ### 6. Comportamiento en la Frontera
> 
> **Curvas abiertas vs cerradas:**
> 
> - **Curvas cerradas** → la función está acotada en esa dirección
> - **Curvas abiertas** (que salen del dominio) → función no acotada
> - **Curvas que terminan en el borde del dominio** → frontera del dominio

---

## 🗺️ Aplicaciones Prácticas

> [!example]- 🌍 Casos del Mundo Real
> 
> ### 1. Topografía y Mapas
> 
> **Función:** $h(x,y)$ = altura del terreno
> 
> **Curvas de nivel:** Líneas de igual elevación
> 
> **Información útil:**
> 
> - Líneas juntas → pendiente empinada (difícil de escalar)
> - Líneas separadas → terreno plano
> - Círculos concéntricos → cima o depresión
> - Curvas en forma de V apuntando hacia arriba → valle
> - Curvas en forma de V apuntando hacia abajo → cresta
> 
> ---
> 
> ### 2. Meteorología
> 
> **Isotermas:** $T(x,y)$ = temperatura
> 
> - Curvas de nivel muestran regiones de igual temperatura
> - Gradiente perpendicular → dirección del cambio de temperatura más rápido
> 
> **Isobaras:** $P(x,y)$ = presión atmosférica
> 
> - Líneas de igual presión
> - Curvas muy juntas → vientos fuertes
> - Centros de alta y baja presión claramente visibles
> 
> ---
> 
> ### 3. Economía
> 
> **Curvas de indiferencia:** $U(x,y)$ = utilidad
> 
> - Combinaciones de dos bienes que dan la misma satisfacción
> - El consumidor es indiferente entre puntos en la misma curva
> 
> **Curvas de isocosto:** $C(x,y) = px + qy$ = costo
> 
> - Combinaciones de recursos con el mismo costo
> - Rectas paralelas
> 
> ---
> 
> ### 4. Física
> 
> **Potencial eléctrico:** $V(x,y)$ = voltaje
> 
> - Curvas equipotenciales
> - El campo eléctrico es perpendicular a estas curvas
> 
> **Temperatura en una placa:** $T(x,y)$
> 
> - Curvas isotérmicas
> - Flujo de calor perpendicular a las isotermas
> 
> ---
> 
> ### 5. Optimización
> 
> **Función objetivo:** $f(x,y)$ = ganancia, costo, rendimiento
> 
> - Las curvas de nivel ayudan a identificar óptimos
> - Máximos y mínimos visibles como centros de curvas cerradas
> - Restricciones se pueden graficar y buscar puntos de tangencia

---

## 🎨 Cómo Dibujar Curvas de Nivel a Mano

> [!tip]- ✏️ Guía Práctica
> 
> ### Pasos para Dibujar
> 
> **1. Identificar el tipo de función**
> 
> - ¿Polinómica? ¿Exponencial? ¿Trigonométrica?
> 
> **2. Determinar el rango de valores de $k$**
> 
> - ¿Qué valores de $k$ tienen sentido?
> - ¿Cuál es el rango de la función?
> 
> **3. Elegir valores de $k$ apropiados**
> 
> - Espaciados uniformemente (e.g., $k = 0, 1, 2, 3, ...$)
> - Incluir valores especiales (máximos, mínimos, cero)
> 
> **4. Para cada $k$, resolver $f(x,y) = k$**
> 
> - Simplificar la ecuación
> - Identificar el tipo de curva (recta, círculo, elipse, hipérbola)
> 
> **5. Graficar cada curva**
> 
> - Usar regla para rectas
> - Compás para círculos
> - Técnicas de parábolas/hipérbolas para cónicas
> 
> **6. Etiquetar ```
> **6. Etiquetar cada curva**
> - Escribir el valor de $k$ sobre o cerca de cada curva
> - Usar flechas si es necesario para indicar dirección de crecimiento
> 
> **7. Verificar coherencia**
> - ¿Las curvas tienen sentido geométricamente?
> - ¿Se mantienen dentro del dominio?
> - ¿El espaciamiento refleja la pendiente de la superficie?
> 
> ---
> 
> ### Herramientas Útiles
> 
> - **Compás:** Para círculos exactos
> - **Regla:** Para rectas y mediciones
> - **Plantillas de elipses:** Si están disponibles
> - **Papel milimetrado:** Facilita la precisión
> - **Colores:** Para distinguir diferentes niveles
> 
> ---
> 
> ### Convenciones de Dibujo
> 
> ✅ **Líneas sólidas** para curvas calculadas
> ✅ **Etiquetas claras** con valores de $k$
> ✅ **Espaciamiento proporcional** cuando sea posible
> ✅ **Ejes coordenados** claramente marcados
> ✅ **Indicar dominio** si está restringido
> ✅ **Flechas opcionales** mostrando dirección de crecimiento

---

## 🧮 Ejemplos Avanzados

> [!example]- 🎓 Ejemplo 9: Función con Dominio Restringido
> 
> **Función:** $f(x,y) = \sqrt{16 - x^2 - y^2}$
> 
> **Dominio:** $x^2 + y^2 \leq 16$ (disco de radio 4)
> 
> **Rango:** $[0, 4]$
> 
> **Encontrar curvas de nivel:**
> 
> Plantear $f(x,y) = k$ con $0 \leq k \leq 4$:
> $$\sqrt{16 - x^2 - y^2} = k$$
> $$16 - x^2 - y^2 = k^2$$
> $$x^2 + y^2 = 16 - k^2$$
> 
> **Para diferentes valores de $k$:**
> - $k = 0$: $x^2 + y^2 = 16$ → Círculo de radio 4 (borde del dominio)
> - $k = 1$: $x^2 + y^2 = 15$ → Círculo de radio $\sqrt{15} \approx 3.87$
> - $k = 2$: $x^2 + y^2 = 12$ → Círculo de radio $\sqrt{12} \approx 3.46$
> - $k = 3$: $x^2 + y^2 = 7$ → Círculo de radio $\sqrt{7} \approx 2.65$
> - $k = 4$: $x^2 + y^2 = 0$ → Punto $(0,0)$ (centro, máximo)
> 
> **Observaciones:**
> - Los círculos se hacen más pequeños a medida que $k$ aumenta
> - El espaciamiento entre círculos disminuye cerca del borde
> - Todas las curvas están dentro del disco de radio 4
> - El centro tiene el valor máximo
> 
> **Superficie 3D:** Hemisferio superior de radio 4
> 
> **Interpretación física:** Altura de una cúpula semiesférica

> [!example]- 🌀 Ejemplo 10: Hipérbolas Rectangulares
> 
> **Función:** $f(x,y) = xy$
> 
> **Encontrar curvas de nivel:**
> 
> Plantear $f(x,y) = k$:
> $$xy = k$$
> 
> **Análisis por casos:**
> 
> **Caso 1: $k > 0$**
> $$y = \frac{k}{x}$$
> 
> Hipérbola en los **cuadrantes I y III**
> - Para $x > 0$: rama en cuadrante I
> - Para $x < 0$: rama en cuadrante III
> 
> **Caso 2: $k < 0$** (sea $k = -c$ con $c > 0$)
> $$y = -\frac{c}{x}$$
> 
> Hipérbola en los **cuadrantes II y IV**
> - Para $x > 0$: rama en cuadrante IV
> - Para $x < 0$: rama en cuadrante II
> 
> **Caso 3: $k = 0$**
> $$xy = 0$$
> 
> Los **ejes coordenados** (sin el origen):
> - Eje $x$ ($y = 0$) y eje $y$ ($x = 0$)
> 
> **Para diferentes valores de $k$:**
> - $k = 4$: Hipérbola $y = \frac{4}{x}$ en cuadrantes I y III
> - $k = 1$: Hipérbola $y = \frac{1}{x}$ en cuadrantes I y III
> - $k = 0$: Ejes coordenados
> - $k = -1$: Hipérbola $y = -\frac{1}{x}$ en cuadrantes II y IV
> - $k = -4$: Hipérbola $y = -\frac{4}{x}$ en cuadrantes II y IV
> 
> **Mapa de contorno:**
> ```
>      y
>      |
>    4 | \    k=-4    /
>      |  \          /
>    2 |   \  k=-1 /
>      |    \      /
>   ---|─────\────/───── x (k=0)
>      |      /  \
>   -2 |     / k=1\
>      |    /      \
>   -4 |   /  k=4   \
>      |
> ```
> 
> **Observaciones:**
> - Todas las hipérbolas tienen asíntotas en los ejes
> - Simetría respecto al origen
> - El origen no está en ninguna curva de nivel
> - Punto de silla en el origen
> 
> **Superficie 3D:** Superficie hiperbólica con forma de "silla de caballo"

> [!example]- 🏔️ Ejemplo 11: Función con Múltiples Extremos
> 
> **Función:** $f(x,y) = (x^2 - 1)(y^2 - 1)$
> 
> **Encontrar curvas de nivel:**
> 
> Plantear $f(x,y) = k$:
> $$(x^2 - 1)(y^2 - 1) = k$$
> 
> **Análisis de puntos especiales:**
> 
> **En $x = \pm 1$ o $y = \pm 1$:**
> - $f(\pm 1, y) = 0$ para todo $y$
> - $f(x, \pm 1) = 0$ para todo $x$
> - Las rectas $x = \pm 1$ y $y = \pm 1$ están todas en el nivel $k = 0$
> 
> **Para $k = 0$:**
> $$(x^2 - 1)(y^2 - 1) = 0$$
> 
> Esto se cumple cuando:
> - $x^2 = 1$ → $x = \pm 1$ (dos rectas verticales)
> - $y^2 = 1$ → $y = \pm 1$ (dos rectas horizontales)
> 
> **Curva de nivel $k=0$:** Cuatro rectas que forman una cruz: $x = \pm 1$, $y = \pm 1$
> 
> **Para otros valores de $k$:**
> 
> Despejando:
> $$y^2 = 1 + \frac{k}{x^2 - 1}$$
> 
> Esta ecuación define curvas complejas que cambian de forma según el signo de $k$ y la región del plano.
> 
> **Regiones del plano:**
> 1. $|x| < 1, |y| < 1$ (rectángulo central)
> 2. $|x| > 1, |y| < 1$ (franjas horizontales)
> 3. $|x| < 1, |y| > 1$ (franjas verticales)
> 4. $|x| > 1, |y| > 1$ (cuatro esquinas)
> 
> **Valores de $f$ en cada región:**
> - Región 1: $f > 0$ (ambos factores negativos)
> - Regiones 2 y 3: $f < 0$ (un factor positivo, uno negativo)
> - Región 4: $f > 0$ (ambos factores positivos)
> 
> **Observaciones:**
> - Función tiene **cuatro puntos críticos**: $(\pm 1, \pm 1)$
> - Patrones simétricos
> - Curvas complejas excepto en $k = 0$

> [!example]- 🎪 Ejemplo 12: Combinación Lineal-Cuadrática
> 
> **Función:** $f(x,y) = x^2 + y^2 - 2x - 4y$
> 
> **Completando cuadrados:**
> $$f(x,y) = (x^2 - 2x) + (y^2 - 4y)$$
> $$= (x^2 - 2x + 1 - 1) + (y^2 - 4y + 4 - 4)$$
> $$= (x - 1)^2 + (y - 2)^2 - 5$$
> 
> **Forma estándar:**
> $$f(x,y) = (x - 1)^2 + (y - 2)^2 - 5$$
> 
> **Encontrar curvas de nivel:**
> 
> Plantear $f(x,y) = k$:
> $$(x - 1)^2 + (y - 2)^2 - 5 = k$$
> $$(x - 1)^2 + (y - 2)^2 = k + 5$$
> 
> **Para diferentes valores de $k$:**
> - $k = -5$: $(x-1)^2 + (y-2)^2 = 0$ → Punto $(1, 2)$ (mínimo)
> - $k = -4$: Círculo de radio 1 centrado en $(1, 2)$
> - $k = 0$: Círculo de radio $\sqrt{5} \approx 2.24$ centrado en $(1, 2)$
> - $k = 4$: Círculo de radio 3 centrado en $(1, 2)$
> - $k = 11$: Círculo de radio 4 centrado en $(1, 2)$
> 
> **Observaciones:**
> - Todas las curvas son círculos concéntricos
> - Centro desplazado al punto $(1, 2)$
> - Mínimo absoluto en $(1, 2)$ con valor $f(1,2) = -5$
> - Radio aumenta con $\sqrt{k+5}$
> 
> **Técnica clave:** Completar cuadrados revela la estructura geométrica

> [!example]- 🌊 Ejemplo 13: Función Gaussiana Bidimensional
> 
> **Función:** $f(x,y) = e^{-\frac{x^2 + y^2}{2}}$
> 
> **Rango:** $(0, 1]$
> 
> **Encontrar curvas de nivel:**
> 
> Plantear $f(x,y) = k$ con $0 < k \leq 1$:
> $$e^{-\frac{x^2 + y^2}{2}} = k$$
> 
> Aplicar logaritmo natural:
> $$-\frac{x^2 + y^2}{2} = \ln(k)$$
> $$x^2 + y^2 = -2\ln(k)$$
> 
> Como $0 < k \leq 1$, tenemos $\ln(k) \leq 0$, entonces $-2\ln(k) \geq 0$ ✓
> 
> **Para diferentes valores de $k$:**
> - $k = 1$: $x^2 + y^2 = 0$ → Punto $(0,0)$ (máximo)
> - $k = e^{-\frac{1}{2}} \approx 0.606$: Círculo de radio 1
> - $k = e^{-2} \approx 0.135$: Círculo de radio 2
> - $k = e^{-\frac{9}{2}} \approx 0.011$: Círculo de radio 3
> 
> **Radio en función de $k$:**
> $$r = \sqrt{-2\ln(k)}$$
> 
> **Observaciones:**
> - Círculos concéntricos en el origen
> - Espaciamiento aumenta logarítmicamente
> - Decaimiento rápido desde el centro
> - Modelo común en estadística (distribución normal bivariada)
> 
> **Aplicación:** Distribución de probabilidad en dos dimensiones

---

## 🔬 Curvas de Nivel y Derivadas

> [!info]- 📐 Relación con el Gradiente
> 
> ### El Gradiente es Perpendicular a las Curvas de Nivel
> 
> **Teorema importante:**
> El vector gradiente $\nabla f$ en un punto es **perpendicular** a la curva de nivel que pasa por ese punto.
> 
> $$\nabla f(x_0, y_0) \perp \text{curva de nivel en } (x_0, y_0)$$
> 
> **Consecuencias:**
> 
> 1. **Dirección de máximo crecimiento:** El gradiente apunta en la dirección donde $f$ crece más rápidamente
> 
> 2. **Dirección de máximo decrecimiento:** $-\nabla f$ apunta donde $f$ decrece más rápidamente
> 
> 3. **Dirección sin cambio:** Moverse tangente a una curva de nivel mantiene $f$ constante
> 
> ---
> 
> ### Ejemplo Visual
> 
> **Función:** $f(x,y) = x^2 + y^2$
> 
> **Gradiente:** $\nabla f = (2x, 2y)$
> 
> **En el punto $(1, 1)$:**
> - Curva de nivel: círculo $x^2 + y^2 = 2$
> - Gradiente: $\nabla f(1,1) = (2, 2)$
> - El vector $(2, 2)$ es perpendicular al círculo en $(1, 1)$
> - El vector $(2, 2)$ apunta radialmente hacia afuera
> 
> ```
>      y
>      |
>    2 |    ⚪
>      |  ⚪   ⚪
>    1 | ⚪ ·→ ⚪  ← vector (2,2) perpendicular al círculo
>      | ⚪   ⚪
>   ---|⚪--·--⚪---|--- x
>      |   ⚪
> ```
> 
> ---
> 
> ### Interpretación Física
> 
> **Si $f(x,y)$ representa temperatura:**
> - Curvas de nivel = isotermas (líneas de temperatura constante)
> - Gradiente = dirección del flujo de calor (perpendicular a isotermas)
> - Magnitud del gradiente = tasa de cambio de temperatura
> 
> **Si $f(x,y)$ representa altura:**
> - Curvas de nivel = líneas de contorno topográfico
> - Gradiente = dirección de máxima pendiente
> - Magnitud del gradiente = inclinación del terreno

---

## 🎯 Casos Especiales y Consideraciones

> [!warning]- ⚠️ Situaciones Especiales
> 
> ### 1. Curvas de Nivel Degeneradas
> 
> **Puntos aislados:**
> 
> **Ejemplo:** $f(x,y) = x^2 + y^2$, nivel $k = 0$
> - Curva de nivel: solo el punto $(0,0)$
> - No es una "curva" en el sentido usual
> 
> **Curvas vacías:**
> 
> **Ejemplo:** $f(x,y) = x^2 + y^2 + 1$, nivel $k = 0$
> - No hay puntos que satisfagan $x^2 + y^2 + 1 = 0$
> - La curva de nivel es el conjunto vacío
> 
> ---
> 
> ### 2. Curvas de Nivel No Conexas
> 
> **Ejemplo:** $f(x,y) = \sin(x)\sin(y)$
> 
> Para $k = 0.5$:
> - La ecuación $\sin(x)\sin(y) = 0.5$ tiene múltiples soluciones
> - Forman un patrón periódico de curvas separadas
> - Cada "componente" es una curva distinta
> 
> ---
> 
> ### 3. Curvas de Nivel que se Auto-Intersectan
> 
> **Ejemplo:** Curvas de nivel de funciones no diferenciables
> 
> **Observación:**
> Para funciones diferenciables (suaves), las curvas de nivel **no se cruzan** entre sí.
> 
> **Razón:** Si dos curvas de nivel se cruzaran, habría un punto donde $f(x,y) = k_1$ y $f(x,y) = k_2$ simultáneamente, lo cual es imposible si $k_1 \neq k_2$.
> 
> ---
> 
> ### 4. Discontinuidades
> 
> **Ejemplo:** $f(x,y) = \lfloor x \rfloor + \lfloor y \rfloor$ (función escalón)
> 
> - Curvas de nivel son uniones de cuadrados
> - Función discontinua en las líneas de la cuadrícula
> - Las curvas de nivel son regiones, no curvas suaves
> 
> ---
> 
> ### 5. Dominio Restringido
> 
> **Importante:** Las curvas de nivel deben estar **dentro del dominio**
> 
> **Ejemplo:** $f(x,y) = \sqrt{4 - x^2 - y^2}$
> - Dominio: $x^2 + y^2 \leq 4$
> - Todas las curvas de nivel son arcos de círculos dentro del disco
> - Curvas terminan en el borde del dominio

---

## 📊 Comparación: Superficie vs Curvas de Nivel

> [!note]- 🎭 Dos Maneras de Visualizar
> 
> | Aspecto | Gráfica 3D ($z = f(x,y)$) | Curvas de Nivel |
> |---------|---------------------------|-----------------|
> | **Dimensionalidad** | 3D (necesita perspectiva) | 2D (plano) |
> | **Facilidad de dibujo** | Difícil a mano | Más fácil |
> | **Información exacta** | Altura visible directamente | Requiere leer etiquetas |
> | **Visualización de pendiente** | Visible en la inclinación | Espaciamiento entre curvas |
> | **Identificación de extremos** | Cimas y valles visibles | Centros de curvas cerradas |
> | **Utilidad práctica** | Impresionante visualmente | Más práctica para cálculos |
> | **Aplicaciones reales** | Modelos 3D, visualización | Mapas, ingeniería |
> 
> **Conclusión:**
> - Gráfica 3D: mejor para **intuición visual**
> - Curvas de nivel: mejor para **análisis cuantitativo**
> 
> **Lo ideal:** Usar ambas representaciones complementariamente

---

## 💡 Consejos Prácticos

> [!tip]- ⭐ Estrategias para Trabajar con Curvas de Nivel
> 
> ### Para Dibujar
> 
> 1. ✅ **Empieza con valores simples** de $k$ (enteros, múltiplos de 5, etc.)
> 2. ✅ **Incluye siempre $k = 0$** si está en el rango
> 3. ✅ **Usa simetría** para reducir trabajo (si la función la tiene)
> 4. ✅ **Verifica puntos especiales** (intersecciones con ejes, origen)
> 5. ✅ **Marca la dirección de crecimiento** con flechas
> 6. ✅ **Indica el dominio** claramente
> 
> ### Para Interpretar
> 
> 1. ✅ **Identifica patrones** (círculos, rectas, hipérbolas)
> 2. ✅ **Observa el espaciamiento** (pendiente)
> 3. ✅ **Busca centros** (extremos)
> 4. ✅ **Nota la simetría** (ayuda a entender la función)
> 5. ✅ **Compara con funciones conocidas**
> 
> ### Errores Comunes a Evitar
> 
> - ❌ Dibujar curvas que se cruzan (imposible para funciones continuas)
> - ❌ Olvidar que curvas de nivel diferentes tienen valores diferentes
> - ❌ No respetar el dominio de la función
> - ❌ Espaciar curvas arbitrariamente sin considerar la función
> - ❌ Omitir etiquetas de valores de $k$
> - ❌ Confundir curvas cerradas creciendo hacia adentro vs hacia afuera

---

## 📝 Ejercicios Propuestos

> [!example]- 💪 Práctica Guiada
> 
> ### Nivel Básico
> 
> **1. Encontrar y dibujar las curvas de nivel:**
> 
> a) $f(x,y) = 2x + 3y$ para $k = 0, 3, 6, -3$
> 
> b) $f(x,y) = x^2 + y^2$ para $k = 0, 1, 4, 9$
> 
> c) $f(x,y) = y - x^2$ para $k = 0, 1, -1, 2$
> 
> d) $f(x,y) = |x| + |y|$ para $k = 0, 1, 2, 3$
> 
> e) $f(x,y) = \max(x, y)$ para $k = 0, 1, 2$
> 
> ---
> 
> **2. Identificar la función a partir de las curvas de nivel:**
> 
> a) Círculos concéntricos de radio $r = k$ centrados en el origen
> 
> b) Rectas paralelas con pendiente $-2$
> 
> c) Hipérbolas en los cuadrantes I y III
> 
> d) Elipses concéntricas con relación de aspecto 2:1
> 
> ---
> 
> ### Nivel Intermedio
> 
> **3. Curvas de nivel y análisis:**
> 
> a) $f(x,y) = e^{x+y}$ para $k = 1, e, e^2$
> 
> b) $f(x,y) = \ln(x^2 + y^2)$ para $k = 0, 1, 2$
> 
> c) $f(x,y) = \frac{x}{x^2 + y^2}$ para $k = 0, \pm 1, \pm 2$
> 
> d) $f(x,y) = x^2 - y^2$ para $k = -4, -1, 0, 1, 4$
> 
> ---
> 
> **4. Identificar extremos y puntos de silla:**
> 
> A partir de las curvas de nivel, determinar si hay máximos, mínimos o puntos de silla:
> 
> a) $f(x,y) = -x^2 - y^2 + 4$
> 
> b) $f(x,y) = x^2 - y^2$
> 
> c) $f(x,y) = x^2 + 2y^2 - 4x + 8y$
> 
> ---
> 
> ### Nivel Avanzado
> 
> **5. Funciones complejas:**
> 
> a) $f(x,y) = \sin(x) \cos(y)$ para $k = -1, -0.5, 0, 0.5, 1$
> 
> b) $f(x,y) = \frac{xy}{x^2 + y^2 + 1}$ para varios valores de $k$
> 
> c) $f(x,y) = e^{-x^2} + e^{-y^2}$ para $k = 0.5, 1, 1.5, 2$
> 
> d) $f(x,y) = \arctan\left(\frac{y}{x}\right)$ para $k = 0, \frac{\pi}{4}, \frac{\pi}{2}, \frac{3\pi}{4}$
> 
> ---
> 
> **6. Análisis geométrico:**
> 
> a) Demostrar que las curvas de nivel de $f(x,y) = ax + by$ son rectas perpendiculares al vector $(a, b)$
> 
> b) Si $f(x,y) = g(r)$ donde $r = \sqrt{x^2 + y^2}$, demostrar que todas las curvas de nivel son círculos concéntricos
> 
> c) Encontrar una función cuyas curvas de nivel sean parábolas $y = x^2 + k$
> 
> ---
> 
> **7. Aplicaciones:**
> 
> a) La temperatura en una placa está dada por $T(x,y) = 100 - x^2 - 2y^2$. Dibujar las isotermas para $T = 100, 75, 50, 25, 0$.
> 
> b) El costo de transporte desde un punto $(x,y)$ a dos ciudades en $(0,0)$ y $(4,0)$ es $C(x,y) = \sqrt{x^2+y^2} + \sqrt{(x-4)^2+y^2}$. Dibujar las curvas de isocosto para $C = 4, 5, 6$.
> 
> c) Una función de utilidad es $U(x,y) = x^{0.5}y^{0.5}$. Dibujar las curvas de indiferencia para $U = 1, 2, 4$.

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas de Ejercicios Básicos
> 
> **1a)** $f(x,y) = 2x + 3y$
> 
> Curvas de nivel $2x + 3y = k$:
> - $k = 0$: $y = -\frac{2x}{3}$ (recta por el origen)
> - $k = 3$: $y = 1 - \frac{2x}{3}$
> - $k = 6$: $y = 2 - \frac{2x}{3}$
> - $k = -3$: $y = -1 - \frac{2x}{3}$
> 
> **Resultado:** Rectas paralelas con pendiente $-\frac{2}{3}$
> 
> ---
> 
> **1b)** $f(x,y) = x^2 + y^2$
> 
> Curvas de nivel $x^2 + y^2 = k$:
> - $k = 0$: Punto $(0,0)$
> - $k = 1$: Círculo de radio 1
> - $k = 4$: Círculo de radio 2
> - $k = 9$: Círculo de radio 3
> 
> **Resultado:** Círculos concéntricos, mínimo en el origen
> 
> ---
> 
> **1c)** $f(x,y) = y - x^2$
> 
> Curvas de nivel $y - x^2 = k$:
> - $k = 0$: $y = x^2$ (parábola)
> - $k = 1$: $y = x^2 + 1$ (parábola desplazada)
> - $k = -1$: $y = x^2 - 1$ (parábola desplazada)
> - $k = 2$: $y = x^2 + 2$ (parábola desplazada)
> 
> **Resultado:** Parábolas verticales, todas con vértice en eje $y$
> 
> ---
> 
> **2a)** Círculos $x^2 + y^2 = k^2$
> 
> **Función:** $f(x,y) = \sqrt{x^2 + y^2}$ (distancia al origen)
> 
> ---
> 
> **2b)** Rectas $y = -2x + c$
> 
> **Función:** $f(x,y) = 2x + y$ (o cualquier múltiplo)
> 
> ---
> 
> **2c)** Hipérbolas $xy = k$
> 
> **Función:** $f(x,y) = xy$
> 
> ---
> 
> **2d)** Elipses $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ con $b = 2a$
> 
> **Función:** $f(x,y) = x^2 + \frac{y^2}{4}$ (o similar)

> [!success]- 🔑 Respuestas de Ejercicios Intermedios
> 
> **3a)** $f(x,y) = e^{x+y}$
> Curvas de nivel $e^{x+y} = k$:
> 
> Aplicar logaritmo natural: $$x + y = \ln(k)$$
> 
> Para $k > 0$:
> 
> - $k = 1$: $x + y = 0$ → $y = -x$
> - $k = e$: $x + y = 1$ → $y = 1 - x$
> - $k = e^2$: $x + y = 2$ → $y = 2 - x$
> 
> **Resultado:** Rectas paralelas con pendiente $-1$, espaciadas logarítmicamente
> 
> ---
> 
> **3b)** $f(x,y) = \ln(x^2 + y^2)$
> 
> Curvas de nivel $\ln(x^2 + y^2) = k$:
> 
> $$x^2 + y^2 = e^k$$
> 
> - $k = 0$: $x^2 + y^2 = 1$ → Círculo de radio 1
> - $k = 1$: $x^2 + y^2 = e$ → Círculo de radio $\sqrt{e} \approx 1.65$
> - $k = 2$: $x^2 + y^2 = e^2$ → Círculo de radio $e \approx 2.72$
> 
> **Resultado:** Círculos concéntricos, espaciados exponencialmente
> 
> **Dominio:** $x^2 + y^2 > 0$ (todo excepto el origen)
> 
> ---
> 
> **3d)** $f(x,y) = x^2 - y^2$
> 
> Ya analizado en Ejemplo 4 (Paraboloide Hiperbólico)
> 
> - $k = -4, -1$: Hipérbolas horizontales
> - $k = 0$: Rectas $y = \pm x$
> - $k = 1, 4$: Hipérbolas verticales
> 
> **Punto de silla en el origen**
> 
> ---
> 
> **4a)** $f(x,y) = -x^2 - y^2 + 4$
> 
> Completando: $f(x,y) = 4 - (x^2 + y^2)$
> 
> Curvas de nivel: $x^2 + y^2 = 4 - k$
> 
> - Círculos concéntricos
> - Valores **decrecen** hacia afuera (radio aumenta cuando $k$ disminuye)
> - En el origen: $f(0,0) = 4$ (máximo)
> 
> **Conclusión:** Máximo absoluto en $(0,0)$
> 
> ---
> 
> **4b)** $f(x,y) = x^2 - y^2$
> 
> - Curvas de nivel son hipérbolas
> - En $k = 0$: rectas que se cruzan
> - Valores crecen en dirección $x$, decrecen en dirección $y$
> 
> **Conclusión:** Punto de silla en $(0,0)$
> 
> ---
> 
> **4c)** $f(x,y) = x^2 + 2y^2 - 4x + 8y$
> 
> Completando cuadrados: $$f(x,y) = (x^2 - 4x + 4) + 2(y^2 + 4y + 4) - 4 - 8$$ $$= (x-2)^2 + 2(y+2)^2 - 12$$
> 
> Curvas de nivel: $(x-2)^2 + 2(y+2)^2 = k + 12$
> 
> O bien: $\frac{(x-2)^2}{k+12} + \frac{(y+2)^2}{\frac{k+12}{2}} = 1$
> 
> - Elipses concéntricas centradas en $(2, -2)$
> - Valores crecen hacia afuera
> - En $(2, -2)$: $f(2,-2) = -12$ (mínimo)
> 
> **Conclusión:** Mínimo absoluto en $(2, -2)$

> [!success]- 🔑 Respuestas de Ejercicios Avanzados
> 
> **6a)** Demostración: Las curvas de nivel de $f(x,y) = ax + by$ son perpendiculares a $(a,b)$
> 
> **Curvas de nivel:** $ax + by = k$
> 
> **Vector tangente a la curva:** Para encontrar un vector tangente, despejamos $y$: $$y = \frac{k - ax}{b}$$
> 
> Vector tangente: $(1, -\frac{a}{b})$ o equivalentemente $(b, -a)$
> 
> **Producto punto con $(a,b)$:** $$(b, -a) \cdot (a, b) = ab + (-a)b = ab - ab = 0$$
> 
> Como el producto punto es cero, los vectores son perpendiculares. ✓
> 
> **Interpretación:** El gradiente $\nabla f = (a, b)$ es perpendicular a las curvas de nivel
> 
> ---
> 
> **6b)** Demostración: Si $f(x,y) = g(r)$ con $r = \sqrt{x^2+y^2}$, las curvas son círculos
> 
> **Curvas de nivel:** $g(r) = k$
> 
> Si $g$ es invertible: $r = g^{-1}(k) = R$ (constante)
> 
> Por tanto: $$\sqrt{x^2 + y^2} = R$$ $$x^2 + y^2 = R^2$$
> 
> Esto es un círculo de radio $R$ centrado en el origen. ✓
> 
> **Conclusión:** Funciones que dependen solo de la distancia al origen tienen curvas de nivel circulares (simetría radial)
> 
> ---
> 
> **6c)** Encontrar función con curvas de nivel $y = x^2 + k$
> 
> Despejando $k$: $$k = y - x^2$$
> 
> Por tanto, la función es: $$f(x,y) = y - x^2$$
> 
> **Verificación:** Curvas de nivel: $y - x^2 = k$ → $y = x^2 + k$ ✓
> 
> ---
> 
> **7a)** Temperatura: $T(x,y) = 100 - x^2 - 2y^2$
> 
> Isotermas $100 - x^2 - 2y^2 = T$: $$x^2 + 2y^2 = 100 - T$$
> 
> Forma estándar: $$\frac{x^2}{100-T} + \frac{y^2}{\frac{100-T}{2}} = 1$$
> 
> Para diferentes temperaturas:
> 
> - $T = 100$: Punto $(0,0)$ (temperatura máxima)
> - $T = 75$: Elipse $\frac{x^2}{25} + \frac{y^2}{12.5} = 1$
> - $T = 50$: Elipse $\frac{x^2}{50} + \frac{y^2}{25} = 1$
> - $T = 25$: Elipse $\frac{x^2}{75} + \frac{y^2}{37.5} = 1$
> - $T = 0$: Elipse $\frac{x^2}{100} + \frac{y^2}{50} = 1$
> 
> **Observación:**
> 
> - Elipses concéntricas
> - Temperatura máxima en el centro
> - La placa se enfría más rápido en dirección $y$ (coeficiente $2y^2$)
> 
> ---
> 
> **7c)** Utilidad: $U(x,y) = x^{0.5}y^{0.5} = \sqrt{xy}$
> 
> Curvas de indiferencia $\sqrt{xy} = U$: $$xy = U^2$$
> 
> Para diferentes utilidades:
> 
> - $U = 1$: $xy = 1$ → Hipérbola rectangular
> - $U = 2$: $xy = 4$ → Hipérbola rectangular
> - $U = 4$: $xy = 16$ → Hipérbola rectangular
> 
> **Interpretación económica:**
> 
> - Cada curva representa combinaciones de bienes $x$ e $y$ que dan la misma satisfacción
> - Hipérbolas convexas hacia el origen (utilidad tipo Cobb-Douglas)
> - Mayor utilidad = curvas más alejadas del origen
> - El consumidor prefiere combinaciones balanceadas (producto máximo)

---

## 🌐 Curvas de Nivel en Tres Variables

> [!info]- 📐 Superficies de Nivel
> 
> Para funciones de **tres variables** $f(x,y,z)$, el análogo a las curvas de nivel son las **superficies de nivel**.
> 
> ### Definición
> 
> **Superficie de nivel** de $f(x,y,z)$ para el valor $k$: $$S_k = {(x,y,z) \in \mathbb{R}^3 : f(x,y,z) = k}$$
> 
> ### Ejemplos
> 
> **Ejemplo 1:** $f(x,y,z) = x^2 + y^2 + z^2$
> 
> Superficies de nivel $x^2 + y^2 + z^2 = k$:
> 
> - $k > 0$: Esferas de radio $\sqrt{k}$ centradas en el origen
> - $k = 0$: Punto $(0,0,0)$
> - $k < 0$: Conjunto vacío
> 
> **Ejemplo 2:** $f(x,y,z) = z - x^2 - y^2$
> 
> Superficies de nivel $z = x^2 + y^2 + k$:
> 
> - Paraboloides circulares
> - Cada valor de $k$ da un paraboloide desplazado verticalmente
> 
> **Ejemplo 3:** $f(x,y,z) = x + y + z$
> 
> Superficies de nivel $x + y + z = k$:
> 
> - Planos paralelos
> - Normal al vector $(1,1,1)$
> 
> **Ejemplo 4:** $f(x,y,z) = x^2 + y^2 - z^2$
> 
> Superficies de nivel $x^2 + y^2 - z^2 = k$:
> 
> - $k = 0$: Cono circular $x^2 + y^2 = z^2$
> - $k > 0$: Hiperboloides de una hoja
> - $k < 0$: Hiperboloides de dos hojas
> 
> ### Visualización
> 
> A diferencia de las curvas de nivel (que se pueden dibujar fácilmente en 2D), las superficies de nivel requieren visualización 3D o cortes transversales.
> 
> ### Aplicaciones
> 
> - **Física:** Superficies equipotenciales en campos eléctricos
> - **Química:** Densidad de probabilidad electrónica en orbitales
> - **Meteorología:** Superficies de presión constante en la atmósfera
> - **Ingeniería:** Distribución de temperatura en sólidos 3D

---

## 🔄 Relación con Otros Conceptos

> [!quote]- 🌉 Conexiones
> 
> **Este tema se relaciona con:**
> 
> ### Ya estudiados:
> 
> - [[02 - Dominio y Rango]] - Las curvas de nivel existen solo en el dominio
> - [[03 - Gráfico de Funciones]] - Las curvas son proyecciones de la superficie
> 
> ### Por estudiar:
> 
> - **Derivadas parciales** - El gradiente es perpendicular a curvas de nivel
> - **Derivadas direccionales** - Máxima en dirección perpendicular a curvas
> - **Optimización** - Extremos corresponden a centros de curvas cerradas
> - **Multiplicadores de Lagrange** - Encontrar extremos sobre curvas de nivel de restricciones
> - **Integrales dobles** - Integrar sobre regiones definidas por curvas de nivel
> - **Campos vectoriales** - Líneas de flujo vs curvas de nivel
> 
> **Conceptos avanzados relacionados:**
> 
> - **Conjuntos de nivel** - Generalización a dimensiones superiores
> - **Teoría de Morse** - Clasificación de funciones por topología de curvas de nivel
> - **Gradiente descendente** - Optimización siguiendo dirección perpendicular a curvas

---

## 📊 Tabla Resumen: Funciones Comunes y sus Curvas de Nivel

> [!note]- 📋 Referencia Rápida
> 
> |Función|Curvas de Nivel|Forma Geométrica|Características|
> |---|---|---|---|
> |$ax + by$|$ax + by = k$|Rectas paralelas|Espaciamiento uniforme|
> |$x^2 + y^2$|$x^2 + y^2 = k$|Círculos|Mínimo en origen|
> |$-x^2 - y^2$|$x^2 + y^2 = -k$|Círculos|Máximo en origen|
> |$\sqrt{x^2+y^2}$|$x^2 + y^2 = k^2$|Círculos|Espaciamiento uniforme|
> |$x^2 - y^2$|$x^2 - y^2 = k$|Hipérbolas/rectas|Punto de silla en origen|
> |$xy$|$xy = k$|Hipérbolas rectangulares|Asíntotas en ejes|
> |$\frac{x^2}{a^2} + \frac{y^2}{b^2}$|Elipses|Elipses concéntricas|Mínimo en origen|
> |$e^{-(x^2+y^2)}$|$x^2 + y^2 = -\ln k$|Círculos|Espaciamiento logarítmico|
> |$\ln(x^2+y^2)$|$x^2 + y^2 = e^k$|Círculos|Espaciamiento exponencial|
> |$\sin x + \cos y$|Transcendental|Ondulaciones|Patrón periódico|
> |$y/x$|$y = kx$|Rectas por origen|Singularidad en origen|

---

## 🎓 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Importantes
> 
> **Sobre Curvas de Nivel:**
> 
> 1. ✅ Son proyecciones en el plano $xy$ de "rebanadas" horizontales de la superficie
> 2. ✅ Cada curva corresponde a un **único valor** de $k$
> 3. ✅ Curvas de nivel de funciones continuas **nunca se cruzan**
> 4. ✅ El espaciamiento indica la **pendiente** de la superficie
> 5. ✅ Curvas cerradas concéntricas indican **extremos** (máximos o mínimos)
> 6. ✅ Patrones en "X" o "silla" indican **puntos de silla**
> 7. ✅ El **gradiente es perpendicular** a las curvas de nivel
> 
> **Interpretación:**
> 
> - 🔍 **Curvas juntas** → pendiente pronunciada
> - 🔍 **Curvas separadas** → terreno plano
> - 🔍 **Valores creciendo hacia adentro** → máximo local
> - 🔍 **Valores decreciendo hacia adentro** → mínimo local
> - 🔍 **Círculos concéntricos** → simetría radial
> - 🔍 **Rectas paralelas** → función lineal o plano
> 
> **Aplicaciones:**
> 
> - 🗺️ Mapas topográficos (altitud)
> - 🌡️ Mapas meteorológicos (temperatura, presión)
> - 💰 Economía (curvas de indiferencia, isocostos)
> - ⚡ Física (equipotenciales, isotermas)
> - 📊 Optimización (identificar extremos)
> 
> **Habilidades esenciales:**
> 
> - ✍️ **Dibujar** curvas de nivel dada una función
> - 📖 **Leer** información de un mapa de contorno
> - 🔍 **Identificar** extremos y puntos de silla
> - 🧮 **Relacionar** curvas con la forma de la superficie 3D
> - 📐 **Usar** curvas de nivel para análisis cuantitativo

---

## 🔧 Herramientas Computacionales

> [!info]- 💻 Software y Tecnología
> 
> ### Herramientas para Visualizar Curvas de Nivel
> 
> **Software matemático:**
> 
> - **MATLAB/Octave:** `contour(X, Y, Z, levels)`
> - **Python (Matplotlib):** `plt.contour(X, Y, Z, levels)`
> - **Mathematica:** `ContourPlot[f[x,y], {x, -5, 5}, {y, -5, 5}]`
> - **GeoGebra:** Herramienta de curvas de nivel interactiva
> - **Desmos 3D:** Para visualización online
> 
> **Ejemplo en Python:**
> 
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> 
> # Crear malla de puntos
> x = np.linspace(-5, 5, 100)
> y = np.linspace(-5, 5, 100)
> X, Y = np.meshgrid(x, y)
> 
> # Definir función
> Z = X**2 + Y**2
> 
> # Dibujar curvas de nivel
> plt.contour(X, Y, Z, levels=[1, 4, 9, 16, 25])
> plt.colorbar()
> plt.axis('equal')
> plt.xlabel('x')
> plt.ylabel('y')
> plt.title('Curvas de nivel de f(x,y) = x² + y²')
> plt.show()
> ```
> 
> ### Funciones Útiles
> 
> - `contour()` - Líneas de contorno
> - `contourf()` - Contornos rellenos con colores
> - `clabel()` - Etiquetas en las curvas
> - `colorbar()` - Barra de colores para referencia
> 
> ### Ventajas de Herramientas Computacionales
> 
> - ✅ Visualización rápida y precisa
> - ✅ Funciones complejas fáciles de graficar
> - ✅ Interactividad (zoom, rotación)
> - ✅ Múltiples representaciones simultáneas
> - ✅ Exportación de imágenes de alta calidad

---

## 📚 Problemas Tipo Examen

> [!example]- 🎯 Práctica para Evaluación
> 
> ### Problema 1: Análisis Completo
> 
> Dada la función $f(x,y) = 4 - x^2 - 4y^2$:
> 
> a) Encuentra el dominio y rango b) Determina las curvas de nivel para $k = 4, 3, 0, -5$ c) Identifica y clasifica los puntos críticos d) Dibuja el mapa de contorno e) Describe la forma de la superficie 3D
> 
> ---
> 
> ### Problema 2: Identificación
> 
> Un mapa de contorno muestra círculos concéntricos centrados en $(2, -1)$ con valores $k = 0, 1, 4, 9$ (de adentro hacia afuera). Los radios son 0, 1, 2, 3 respectivamente.
> 
> a) Determina la función $f(x,y)$ b) ¿Es un máximo o mínimo en $(2, -1)$? c) Calcula $f(3, -1)$ y $f(2, 1)$
> 
> ---
> 
> ### Problema 3: Aplicación
> 
> La temperatura en una placa metálica está dada por: $$T(x,y) = \frac{100}{1 + x^2 + y^2}$$
> 
> a) Encuentra las isotermas para $T = 100, 50, 25$ b) ¿Dónde está la temperatura máxima? c) ¿Qué sucede con la temperatura cuando nos alejamos del origen? d) Dibuja las isotermas
> 
> ---
> 
> ### Problema 4: Análisis Avanzado
> 
> Considera $f(x,y) = e^y\sin x$:
> 
> a) Encuentra las curvas de nivel para $k = 0, 1, -1$ b) Describe el patrón de las curvas c) ¿Dónde la función es cero? d) ¿Cómo afecta el factor $e^y$ al comportamiento?
> 
> ---
> 
> ### Problema 5: Comparación
> 
> Compara las curvas de nivel de:
> 
> - $f_1(x,y) = x^2 + y^2$
> - $f_2(x,y) = |x| + |y|$
> - $f_3(x,y) = \max(|x|, |y|)$
> 
> Para cada función: a) Dibuja las curvas de nivel para $k = 1, 2, 3$ b) Describe las diferencias geométricas c) ¿Cuál tiene curvas suaves y cuál tiene esquinas?

---

## 🎨 Galería Visual

> [!note]- 🖼️ Ejemplos Visualizados
> 
> ### Paraboloide Circular
> 
> ```
> f(x,y) = x² + y²
> 
> Superficie 3D:          Curvas de nivel:
>       z                      y
>       |                      |
>     9 |    /^\              3|    ⚪₉
>       |   /   \              |  ⚪⚪⚪
>     4 |  /     \            2| ⚪⚪⚪⚪⚪
>       | /       \            | ⚪ ⚪ ⚪  ₄
>     1 |/         \          1|⚪  ⚪  ⚪
>       +___________           |⚪ · ⚪   ₁
>      / \         /           +─⚪─·─⚪──── x
>     /   \       /              ⚪ · ⚪
>    y     \     /               ⚪⚪⚪⚪⚪
>           \   /                 ⚪⚪⚪
>            \ /                   ⚪
>             x                    
> ```
> 
> ---
> 
> ### Silla de Montar
> 
> ```
> f(x,y) = y² - x²
> 
> Superficie 3D:          Curvas de nivel:
>       z                      y
>       |                      |
>     4 | \  |  /             2|  ╱₄│╲
>       |  \ | /               | ╱  │ ╲
>     1 |   \|/                |╱ ₁ │  ╲
>   ----+----+----            ─┼────┼────┼── x
>    -1 |   /|\                |╲   │  ╱
>       |  / | \               | ╲₋₁│ ╱
>    -4 | /  |  \             -2|  ╲₋₄╱
>       |                      |
> ```
> 
> ---
> 
> ### Plano Inclinado
> 
> ```
> f(x,y) = x + y
> 
> Superficie 3D:          Curvas de nivel:
>       z                      y
>       |                      |
>     3 |    ⟋               3 | ⟋ ₃
>       |   ⟋                 | ⟋
>     2 |  ⟋                 2|⟋ ₂
>       | ⟋                   ⟋
>     1 |⟋                  1⟋ ₁
>       +________            ⟋₀
>      /⟋        \          ⟋|________ x
>     / ⟋        \        ⟋
>    y  ⟋        x       ₋₁
> ```

---

## 🔗 Recursos Adicionales

> [!quote]- 📖 Para Profundizar
> 
> ### Videos Recomendados
> 
> - Khan Academy: "Level curves and contour plots"
> - 3Blue1Brown: "Multivariable calculus visualization"
> - MIT OpenCourseWare: "Calculus III - Level curves"
> 
> ### Lecturas
> 
> - Stewart, Calculus: Capítulo sobre funciones de varias variables
> - Thomas' Calculus: Sección de curvas de nivel
> - Marsden & Tromba: Vector Calculus
> 
> ### Simuladores Interactivos
> 
> - GeoGebra 3D Calculator
> - Wolfram Alpha: "contour plot [función]"
> - CalcPlot3D: Herramienta educativa online
> 
> ### Próximo Tema
> 
> **[[05 - Límites en Varias Variables]]**
> 
> - Límites de funciones de dos variables
> - Continuidad
> - Límites en trayectorias

---

## 🎯 Autoevaluación

> [!tip]- ✔️ Verificación de Comprensión
> 
> **¿Puedes responder estas preguntas?**
> 
> 1. ✅ ¿Qué representa geométricamente una curva de nivel?
> 2. ✅ ¿Por qué las curvas de nivel de funciones continuas no se cruzan?
> 3. ✅ ¿Cómo identificar un máximo local en un mapa de contorno?
> 4. ✅ ¿Qué indica el espaciamiento entre curvas de nivel?
> 5. ✅ ¿Cuál es la relación entre el gradiente y las curvas de nivel?
> 6. ✅ ¿Cómo se ven las curvas de nivel de una función lineal?
> 7. ✅ ¿Qué forma tienen las curvas de nivel de $f(x,y) = x^2 + y^2$?
> 8. ✅ ¿Qué es un punto de silla y cómo se ve en curvas de nivel?
> 9. ✅ ¿Para qué valores de $k$ existe la curva de nivel de $f(x,y) = \sqrt{4-x^2-y^2}$?
> 10. ✅ ¿Cómo usarías curvas de nivel en un problema de optimización?
> 
> **Si puedes responder todas con confianza, ¡estás listo para avanzar!**

---

**Tags:** #calculo-multivariable #curvas-de-nivel #contorno #visualizacion #funciones-dos-variables #mapas-topograficos #gradiente #optimizacion
`