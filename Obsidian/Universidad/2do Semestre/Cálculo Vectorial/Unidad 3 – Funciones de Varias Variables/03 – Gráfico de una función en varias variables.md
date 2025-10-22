# 📘 03 – Gráfico de una función z=f(x,y)

## 🎯 Introducción

> [!info]- 💡 ¿Cómo Visualizar Funciones de Dos Variables? En funciones de **una variable** $y = f(x)$, la gráfica es una **curva** en el plano $\mathbb{R}^2$.
> 
> En funciones de **dos variables** $z = f(x,y)$, la gráfica es una **superficie** en el espacio $\mathbb{R}^3$.
> 
> **Definición formal:** La **gráfica** de $f: D \subseteq \mathbb{R}^2 \to \mathbb{R}$ es el conjunto: $$\text{Graf}(f) = {(x, y, z) \in \mathbb{R}^3 : (x,y) \in D \text{ y } z = f(x,y)}$$
> 
> **Interpretación:**
> 
> - Cada punto $(x,y)$ del dominio genera un punto $(x, y, f(x,y))$ en el espacio
> - El conjunto de todos estos puntos forma una **superficie tridimensional**
> 
> **¿Por qué es importante?**
> 
> - 🏔️ Modelar terrenos (topografía)
> - 📊 Visualizar relaciones entre tres variables
> - 🔬 Análisis de fenómenos físicos (temperatura, presión)
> - 💰 Optimización (maximizar ganancias, minimizar costos)

---

## 📐 Sistema de Coordenadas 3D

### 🎯 Ejes Cartesianos en el Espacio

> [!example]- 🟢 El Espacio Tridimensional $\mathbb{R}^3$
> 
> **Sistema de coordenadas:**
> 
> ```
>         z
>         |
>         |
>         |______ y
>        /
>       /
>      x
> ```
> 
> **Tres ejes perpendiculares:**
> 
> - **Eje $x$:** Usualmente hacia la derecha
> - **Eje $y$:** Usualmente hacia atrás (o izquierda en 2D)
> - **Eje $z$:** Usualmente hacia arriba (altura)
> 
> **Convención de mano derecha:**
> 
> - Pulgar → $x$
> - Índice → $y$
> - Medio → $z$
> 
> **Punto genérico:** $(x, y, z)$
> 
> - $x$ = coordenada en eje $x$
> - $y$ = coordenada en eje $y$
> - $z$ = altura (valor de la función)

### 📊 Planos Coordenados

> [!note]- 🔷 Los Tres Planos Principales
> 
> **1. Plano $xy$ (piso):**
> 
> - Ecuación: $z = 0$
> - Contiene todos los puntos $(x, y, 0)$
> - Es donde "vive" el **dominio** de la función
> 
> **2. Plano $xz$ (pared frontal):**
> 
> - Ecuación: $y = 0$
> - Contiene todos los puntos $(x, 0, z)$
> - Vista lateral derecha
> 
> **3. Plano $yz$ (pared lateral):**
> 
> - Ecuación: $x = 0$
> - Contiene todos los puntos $(0, y, z)$
> - Vista frontal
> 
> **Octantes:** Los tres planos dividen el espacio en **8 octantes** (análogo a los 4 cuadrantes del plano).
> 
> **Primer octante:**
> 
> - $x > 0$, $y > 0$, $z > 0$
> - Todos los valores son positivos

---

## 🏔️ Superficies Comunes

### 1️⃣ Paraboloide Circular

> [!example]- 📝 Ejemplo 1: Paraboloide hacia arriba
> 
> **Función:** $z = x^2 + y^2$
> 
> **Análisis:**
> 
> - **Dominio:** $\mathbb{R}^2$ (todo el plano)
> - **Rango:** $[0, +\infty)$
> - **Punto más bajo:** $(0, 0, 0)$ (vértice)
> 
> **Características:**
> 
> - Forma de "cuenco" o "tazón"
> - Se abre **hacia arriba**
> - Simétrica respecto al eje $z$
> - Distancia al cuadrado desde el eje $z$
> 
> **Trazas (secciones):**
> 
> **En planos horizontales $z = k$ (donde $k > 0$):** $$k = x^2 + y^2$$
> 
> - Circunferencias de radio $\sqrt{k}$
> - A mayor altura, mayor radio
> 
> **En el plano $y = 0$ (vista lateral):** $$z = x^2$$
> 
> - Parábola en el plano $xz$
> 
> **En el plano $x = 0$ (vista frontal):** $$z = y^2$$
> 
> - Parábola en el plano $yz$
> 
> **Visualización ASCII:**
> 
> ```
>         z
>         |
>       8 |      /\
>         |     /  \
>       4 |    /    \
>         |   /      \
>       1 |  /________\
>       0 |______________ y
>        / -2  0   2
>       /
>      x
> ```
> 
> **Interpretación física:**
> 
> - Energía potencial de un oscilador armónico
> - Superficie de un líquido girando
> - Reflector parabólico

> [!example]- 📝 Ejemplo 2: Paraboloide hacia abajo
> 
> **Función:** $z = 4 - x^2 - y^2$
> 
> **Análisis:**
> 
> - **Dominio:** $\mathbb{R}^2$
> - **Rango:** $(-\infty, 4]$
> - **Punto más alto:** $(0, 0, 4)$ (vértice)
> 
> **Características:**
> 
> - Forma de "montaña" o "cúpula"
> - Se abre **hacia abajo**
> - Máximo en el origen
> 
> **Trazas horizontales $z = k$ (donde $k < 4$):** $$k = 4 - x^2 - y^2$$ $$x^2 + y^2 = 4 - k$$
> 
> - Circunferencias de radio $\sqrt{4-k}$
> - A menor altura, mayor radio
> 
> **Ejemplos de trazas:**
> 
> - $z = 4$: punto $(0,0,4)$
> - $z = 3$: círculo $x^2 + y^2 = 1$
> - $z = 0$: círculo $x^2 + y^2 = 4$
> - $z = -5$: círculo $x^2 + y^2 = 9$

> [!example]- 📝 Ejemplo 3: Paraboloide Elíptico
> 
> **Función:** $z = x^2 + 4y^2$
> 
> **Características:**
> 
> - Similar al paraboloide circular
> - **Estirado** más rápido en dirección $y$
> - Las trazas horizontales son **elipses** (no círculos)
> 
> **Traza en $z = 4$:** $$4 = x^2 + 4y^2$$ $$\frac{x^2}{4} + y^2 = 1$$
> 
> - Elipse con semiejes $a = 2$ (en $x$) y $b = 1$ (en $y$)
> 
> **Comparación:**
> 
> - $z = x^2 + y^2$: crece igual en todas direcciones → círculos
> - $z = x^2 + 4y^2$: crece más rápido en $y$ → elipses

### 2️⃣ Plano

> [!example]- 📝 Ejemplo 4: Plano Horizontal
> 
> **Función:** $z = 5$
> 
> **Características:**
> 
> - **Plano paralelo** al plano $xy$
> - **Altura constante** $z = 5$
> - No depende de $x$ ni de $y$
> 
> **Interpretación:** Superficie plana a 5 unidades del suelo.

> [!example]- 📝 Ejemplo 5: Plano Inclinado
> 
> **Función:** $z = 2x + 3y + 1$
> 
> **Características:**
> 
> - **Superficie plana** inclinada
> - Pendiente en $x$: 2 (sube 2 unidades por cada unidad en $x$)
> - Pendiente en $y$: 3 (sube 3 unidades por cada unidad en $y$)
> - Intercepto en $z$: 1 (cuando $x=0, y=0$)
> 
> **Puntos específicos:**
> 
> - $(0, 0, 1)$
> - $(1, 0, 3)$
> - $(0, 1, 4)$
> - $(1, 1, 6)$
> 
> **Forma general de un plano:** $$z = ax + by + c$$ donde:
> 
> - $a$ = tasa de cambio respecto a $x$
> - $b$ = tasa de cambio respecto a $y$
> - $c$ = valor cuando $x = y = 0$

### 3️⃣ Superficies Cilíndricas

> [!example]- 📝 Ejemplo 6: Cilindro Parabólico
> 
> **Función:** $z = x^2$
> 
> **Características:**
> 
> - **No depende de $y$** → se extiende igual en toda dirección $y$
> - Forma de "canal" o "valle"
> - Sección transversal es parábola
> 
> **Trazas:**
> 
> - En $y = k$ (cualquier valor): $z = x^2$ (parábola)
> - En $z = k$ (donde $k > 0$): $k = x^2$ → $x = \pm\sqrt{k}$ (dos rectas paralelas al eje $y$)
> 
> **Visualización:** La parábola $z = x^2$ se "barre" a lo largo del eje $y$.

> [!example]- 📝 Ejemplo 7: Cilindro Circular
> 
> **Función:** $x^2 + y^2 = 4$ (técnicamente no es función de la forma $z=f(x,y)$)
> 
> **Características:**
> 
> - Cilindro vertical de radio 2
> - Eje paralelo al eje $z$
> - No depende de $z$
> 
> **Como función multi-valuada:**
> 
> - Parte superior: $z$ puede ser cualquier valor
> - Se puede expresar como $z = f(x,y)$ + restricción $x^2 + y^2 \leq 4$

### 4️⃣ Esfera y Hemisferio

> [!example]- 📝 Ejemplo 8: Hemisferio Superior
> 
> **Función:** $z = \sqrt{9 - x^2 - y^2}$
> 
> **Análisis:**
> 
> - **Dominio:** ${(x,y) : x^2 + y^2 \leq 9}$ (disco de radio 3)
> - **Rango:** $[0, 3]$
> - **Punto más alto:** $(0, 0, 3)$
> 
> **Características:**
> 
> - **Media esfera** superior de radio 3
> - Centro en el origen
> - Solo la parte con $z \geq 0$
> 
> **Ecuación de la esfera completa:** $$x^2 + y^2 + z^2 = 9$$
> 
> Despejando $z$: $$z = \pm\sqrt{9 - x^2 - y^2}$$
> 
> - Signo positivo: hemisferio superior
> - Signo negativo: hemisferio inferior
> 
> **Trazas horizontales $z = k$ (donde $0 \leq k \leq 3$):** $$k = \sqrt{9 - x^2 - y^2}$$ $$k^2 = 9 - x^2 - y^2$$ $$x^2 + y^2 = 9 - k^2$$
> 
> - Circunferencias de radio $\sqrt{9-k^2}$
> - En $z = 0$: círculo de radio 3 (ecuador)
> - En $z = 3$: punto (polo norte)

### 5️⃣ Silla de Montar (Paraboloide Hiperbólico)

> [!example]- 📝 Ejemplo 9: Silla de Montar
> 
> **Función:** $z = x^2 - y^2$
> 
> **Características:**
> 
> - Forma de **silla** o **chip Pringles**
> - Se curva hacia **arriba** en dirección $x$
> - Se curva hacia **abajo** en dirección $y$
> - **Punto silla** en $(0, 0, 0)$
> 
> **Trazas:**
> 
> **En el plano $y = 0$:** $$z = x^2$$
> 
> - Parábola que abre hacia arriba
> 
> **En el plano $x = 0$:** $$z = -y^2$$
> 
> - Parábola que abre hacia abajo
> 
> **En planos horizontales $z = k$:** $$k = x^2 - y^2$$ $$\frac{x^2}{k} - \frac{y^2}{k} = 1$$ (si $k > 0$)
> 
> - **Hipérbolas**
> 
> **Casos específicos:**
> 
> - $z = 0$: $x^2 = y^2$ → rectas $y = \pm x$
> - $z = 1$: hipérbola $x^2 - y^2 = 1$
> - $z = -1$: hipérbola $y^2 - x^2 = 1$
> 
> **Punto silla:** El origen $(0,0,0)$ es un **punto crítico** pero **no es ni máximo ni mínimo** (es un punto silla).

### 6️⃣ Cono

> [!example]- 📝 Ejemplo 10: Cono Circular
> 
> **Función:** $z = \sqrt{x^2 + y^2}$
> 
> **Características:**
> 
> - **Dominio:** $\mathbb{R}^2$
> - **Rango:** $[0, +\infty)$
> - Vértice en el origen
> - Se abre hacia arriba
> 
> **Trazas horizontales $z = k$ (donde $k > 0$):** $$k = \sqrt{x^2 + y^2}$$ $$x^2 + y^2 = k^2$$
> 
> - Circunferencias de radio $k$
> - El radio crece linealmente con la altura
> 
> **Trazas verticales:**
> 
> - En $y = 0$: $z = |x|$ (V absoluta)
> - En $x = 0$: $z = |y|$
> 
> **Ecuación alternativa:** $$z^2 = x^2 + y^2$$
> 
> - Cono completo (superior e inferior)
> 
> **Aplicaciones:**
> 
> - Modelos de volcanes
> - Embudos
> - Radiación de antenas

### 7️⃣ Funciones Trigonométricas

> [!example]- 📝 Ejemplo 11: Onda Sinusoidal 2D
> 
> **Función:** $z = \sin(x)$
> 
> **Características:**
> 
> - No depende de $y$
> - Ondula en dirección $x$
> - Constante en dirección $y$
> - **Rango:** $[-1, 1]$
> 
> **Forma:** Superficie ondulatoria como una "chapa ondulada".

> [!example]- 📝 Ejemplo 12: Superficie Ondulada en Dos Direcciones
> 
> **Función:** $z = \sin(x) + \cos(y)$
> 
> **Características:**
> 
> - Ondula en **ambas direcciones**
> - **Rango:** $[-2, 2]$
> - Máximo cuando $\sin(x) = 1$ y $\cos(y) = 1$
> - Mínimo cuando $\sin(x) = -1$ y $\cos(y) = -1$
> 
> **Aplicaciones:**
> 
> - Patrones de interferencia
> - Ondas en agua
> - Membranas vibrantes

> [!example]- 📝 Ejemplo 13: Onda Radial
> 
> **Función:** $z = \sin(\sqrt{x^2 + y^2})$
> 
> **Características:**
> 
> - **Ondas circulares** que se expanden desde el origen
> - Similar a ondas en agua al tirar una piedra
> - Simetría radial
> 
> **Comportamiento:**
> 
> - En el centro: $z = \sin(0) = 0$
> - A distancia $r$ del origen: $z = \sin(r)$
> - Ondas concéntricas

### 8️⃣ Funciones Exponenciales

> [!example]- 📝 Ejemplo 14: Campana Gaussiana 2D
> 
> **Función:** $z = e^{-(x^2 + y^2)}$
> 
> **Características:**
> 
> - **Forma de campana**
> - Máximo en el origen: $z = 1$
> - Decae exponencialmente al alejarse del origen
> - **Rango:** $(0, 1]$
> 
> **Propiedades:**
> 
> - Simetría radial
> - Siempre positiva
> - Tiende a 0 en el infinito (pero nunca lo alcanza)
> 
> **Aplicaciones:**
> 
> - Distribución normal bidimensional (estadística)
> - Densidad de probabilidad
> - Función de difusión

> [!example]- 📝 Ejemplo 15: Crecimiento Exponencial
> 
> **Función:** $z = e^{x+y}$
> 
> **Características:**
> 
> - Crece exponencialmente en ambas direcciones
> - **Rango:** $(0, +\infty)$
> - Siempre positiva
> 
> **Comportamiento:**
> 
> - Crece muy rápido cuando $x$ y $y$ aumentan
> - Tiende a 0 cuando $x, y \to -\infty$

---

## 🔍 Técnicas para Analizar Superficies

### 📊 Método de Trazas (Secciones Transversales)

> [!tip]- 🎯 Cortar la Superficie con Planos
> 
> **Concepto:** Para entender una superficie compleja, la **cortamos** con planos y analizamos las **curvas resultantes**.
> 
> **Tipos de trazas:**
> 
> ### 1. Trazas Horizontales ($z = k$)
> 
> Cortar con planos paralelos al plano $xy$ a diferentes alturas.
> 
> **Procedimiento:**
> 
> 1. Fijar $z = k$ (constante)
> 2. Sustituir en la ecuación $z = f(x,y)$
> 3. Obtener ecuación en $x$ y $y$: $k = f(x,y)$
> 4. Graficar esta curva en el plano $xy$
> 
> **Ejemplo:** $z = x^2 + y^2$
> 
> - $z = 0$: $x^2 + y^2 = 0$ → punto $(0,0)$
> - $z = 1$: $x^2 + y^2 = 1$ → círculo radio 1
> - $z = 4$: $x^2 + y^2 = 4$ → círculo radio 2
> - $z = 9$: $x^2 + y^2 = 9$ → círculo radio 3
> 
> ---
> 
> ### 2. Trazas Verticales en Plano $y = k$
> 
> Cortar con planos perpendiculares al eje $y$.
> 
> **Procedimiento:**
> 
> 1. Fijar $y = k$
> 2. Sustituir: $z = f(x, k)$
> 3. Graficar en el plano $xz$
> 
> **Ejemplo:** $z = x^2 + y^2$
> 
> - $y = 0$: $z = x^2$ (parábola en plano $xz$)
> - $y = 1$: $z = x^2 + 1$ (parábola desplazada)
> - $y = 2$: $z = x^2 + 4$ (parábola más alta)
> 
> ---
> 
> ### 3. Trazas Verticales en Plano $x = k$
> 
> Cortar con planos perpendiculares al eje $x$.
> 
> **Procedimiento:**
> 
> 1. Fijar $x = k$
> 2. Sustituir: $z = f(k, y)$
> 3. Graficar en el plano $yz$
> 
> **Ejemplo:** $z = x^2 + y^2$
> 
> - $x = 0$: $z = y^2$ (parábola en plano $yz$)
> - $x = 1$: $z = 1 + y^2$
> - $x = 2$: $z = 4 + y^2$

### 🎨 Procedimiento General para Graficar

> [!success]- ✅ Pasos Sistemáticos
> 
> **Para graficar $z = f(x,y)$:**
> 
> **Paso 1: Determinar el dominio**
> 
> - ¿En qué región del plano $xy$ está definida?
> 
> **Paso 2: Encontrar puntos especiales**
> 
> - Interceptos con los ejes
> - Puntos donde $z = 0$
> - Máximos, mínimos (si se conocen)
> 
> **Paso 3: Analizar trazas horizontales**
> 
> - Fijar varios valores de $z = k$
> - Identificar el tipo de curva (círculo, elipse, hipérbola, etc.)
> 
> **Paso 4: Analizar trazas verticales**
> 
> - Cortar con $x = 0$ y $y = 0$ (ejes coordenados)
> - Identificar tipo de curva (parábola, recta, etc.)
> 
> **Paso 5: Determinar el rango**
> 
> - ¿Qué valores puede tomar $z$?
> 
> **Paso 6: Identificar simetrías**
> 
> - ¿Es simétrica respecto a algún eje o plano?
> 
> **Paso 7: Analizar comportamiento en el infinito**
> 
> - ¿Qué pasa cuando $x, y \to \pm\infty$?
> 
> **Paso 8: Bosquejar la superficie**
> 
> - Combinar toda la información
> - Dibujar las trazas principales
> - Conectar con una superficie suave

---

## 📊 Ejemplo Completo Paso a Paso

> [!example]- 🎓 Análisis Detallado: $z = 9 - x^2 - y^2$
> 
> **Paso 1: Dominio**
> 
> - No hay restricciones algebraicas
> - **Dominio:** $\mathbb{R}^2$ (todo el plano)
> 
> ---
> 
> **Paso 2: Puntos especiales**
> 
> - En el origen: $z = 9 - 0 - 0 = 9$ → punto $(0, 0, 9)$
> - ¿Dónde $z = 0$? $0 = 9 - x^2 - y^2$ → $x^2 + y^2 = 9$ (círculo radio 3 en el plano $xy$)
> 
> ---
> 
> **Paso 3: Trazas horizontales ($z = k$)** $$k = 9 - x^2 - y^2$$ $$x^2 + y^2 = 9 - k$$
> 
> - **$z = 9$:** $x^2 + y^2 = 0$ → punto $(0,0)$ (vértice)
> - **$z = 8$:** $x^2 + y^2 = 1$ → círculo radio 1
> - **$z = 5$:** $x^2 + y^2 = 4$ → círculo radio 2
> - **$z = 0$:** $x^2 + y^2 = 9$ → círculo radio 3
> - **$z = -7$:** $x^2 + y^2 = 16$ → círculo radio 4
> 
> **Observación:** Las trazas son círculos concéntricos que crecen al disminuir $z$.
> 
> ---
> 
> **Paso 4: Trazas verticales**
> 
> **En $y = 0$ (plano $xz$):** $$z = 9 - x^2$$
> 
> - Parábola que abre hacia abajo
> - Vértice en $(0, 9)$
> - Interceptos en $x = \pm 3$
> 
> **En $x = 0$ (plano $yz$):** $$z = 9 - y^2$$
> 
> - Parábola que abre hacia abajo
> - Vértice en $(0, 9)$
> - Interceptos en $y = \pm 3$
> 
> ---
> 
> **Paso 5: Rango**
> 
> - Valor máximo: $z = 9$ (en el origen)
> - Sin cota inferior: $z \to -\infty$ cuando $x^2 + y^2 \to \infty$
> - **Rango:** $(-\infty, 9]$
> 
> ---
> 
> **Paso 6: Simetrías**
> 
> - Simétrica respecto al eje $z$ (función solo depende de $x^2 + y^2$)
> - Simétrica respecto al plano $xz$ (cambiar $y$ por $-y$ no afecta)
> - Simétrica respecto al plano $yz$ (cambiar $x$ por $-x$ no afecta)
> 
> ---
> 
> **Paso 7: Comportamiento en infinito**
> 
> - Cuando $x^2 + y^2 \to \infty$: $z \to -\infty$
> - La superficie baja indefinidamente
> 
> ---
> 
> **Paso 8: Conclusión**
> 
> - **Tipo de superficie:** Paraboloide circular que abre hacia abajo
> - **Forma:** Montaña o cúpula
> - **Vértice:** $(0, 0, 9)$ (punto máximo)
> - **Base visible:** Círculo de radio 3 en $z = 0$

---

## 🖼️ Galería de Superficies

> [!note]- 🎨 Catálogo de Superficies Estándar
> 
> |Función|Nombre|Forma|Características|
> |---|---|---|---|
> |$z = x^2 + y^2$|Paraboloide circular ↑|Cuenco|Mínimo en origen|
> |$z = -(x^2 + y^2)$|Paraboloide circular ↓|Montaña|Máximo en origen|
> |$z = x^2 - y^2$|Silla de montar|Chip Pringles|Punto silla|
> |$z = \sqrt{R^2 - x^2 - y^2}$|Hemisferio|Media esfera|Acotada|
> |$z = \sqrt{x^2 + y^2}$|Cono|Cono helado|Vértice en origen|
> |$z = c$|Plano horizontal|Piso/techo|Altura constante|
> |$z = ax + by + c$|Plano inclinado|Rampa|Lineal|
> |$z = x^2$|Cilindro parabólico|Valle/canal|Independiente de $y$|
> |$z = e^{-(x^2+y^2)}$|Campana gaussiana|Colina suave|Decae exponencialmente|
> |$z = \sin(\sqrt{x^2+y^2})$|Ondas radiales|Ondas concéntricas|Oscilante|

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica
> 
> ### Nivel Básico
> 
> **1. Identificar el tipo de superficie:** a) $z = 4 - x^2 - y^2$ b) $z = x^2 + 4y^2$ c) $z = 3x + 2y - 1$ d) $z = |x| + |y|$
> 
> **2. Encontrar trazas horizontales para $z = k$:** Para $z = x^2 + y^2$, encontrar las curvas cuando: a) $z = 0$ b) $z = 4$ c) $z = 9$
> 
> **3. Encontrar trazas verticales:** Para $z = x^2 - y^2$, encontrar las curvas cuando:
> a) $x = 0$ b) $y = 0$ c) $x = 1$
> 
> ---
> 
> ### Nivel Intermedio
> 
> **4. Analizar completamente estas superficies:**
> 
> a) $z = 16 - x^2 - y^2$
> 
> - Dominio
> - Rango
> - Trazas horizontales para $z = 16, 12, 7, 0$
> - Trazas verticales en $x = 0$ y $y = 0$
> - Tipo de superficie
> 
> b) $z = xy$
> 
> - ¿Qué forma tiene?
> - ¿Dónde es positiva? ¿Negativa?
> - Trazas en $z = 1, 0, -1$
> 
> c) $z = \sqrt{x^2 + y^2}$
> 
> - Dominio y rango
> - Forma general
> - Diferencia con $z = x^2 + y^2$
> 
> **5. Superficies cilíndricas:** Para cada función, determinar si es cilíndrica y en qué dirección: a) $z = x^2$ b) $z = \sin(y)$ c) $z = x^2 + y^2$
> 
> **6. Intersecciones:** Encontrar la curva de intersección entre: a) $z = x^2 + y^2$ y el plano $z = 4$ b) $z = 4 - x^2 - y^2$ y el plano $z = 0$ c) $z = x^2 - y^2$ y el plano $z = 0$
> 
> ---
> 
> ### Nivel Avanzado
> 
> **7. Superficies complejas:**
> 
> a) $z = \sin(x)\cos(y)$
> 
> - Rango
> - Comportamiento periódico
> - Puntos críticos
> 
> b) $z = e^{-(x^2+y^2)}\cos(\sqrt{x^2+y^2})$
> 
> - Combina decaimiento y oscilación
> - Comportamiento cerca del origen
> - Comportamiento en infinito
> 
> c) $z = \frac{xy}{x^2+y^2+1}$
> 
> - Dominio
> - Rango (ayuda: usar $xy \leq \frac{x^2+y^2}{2}$)
> - Simetría
> 
> **8. Comparar superficies:** Graficar mentalmente y describir diferencias: a) $z = x^2 + y^2$ vs $z = (x^2 + y^2)^2$ b) $z = x^2 + y^2$ vs $z = |x| + |y|$ c) $z = \sqrt{9-x^2-y^2}$ vs $z = 9-x^2-y^2$
> 
> **9. Problema aplicado:** Una montaña tiene forma descrita por: $$h(x,y) = 1000e^{-(x^2+y^2)/100}$$ donde $h$ es la altura en metros y $(x,y)$ son coordenadas horizontales en metros.
> 
> a) ¿Cuál es la altura máxima? b) ¿A qué distancia del centro la altura es 500 m? c) Describir las curvas de nivel (ver tema siguiente)

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1. Identificar superficies:**
> 
> a) $z = 4 - x^2 - y^2$
> 
> - **Paraboloide circular hacia abajo**
> - Vértice en $(0,0,4)$
> - Abre hacia abajo
> 
> b) $z = x^2 + 4y^2$
> 
> - **Paraboloide elíptico hacia arriba**
> - Vértice en $(0,0,0)$
> - Más "estrecho" en dirección $y$
> 
> c) $z = 3x + 2y - 1$
> 
> - **Plano inclinado**
> - Pendiente 3 en $x$, pendiente 2 en $y$
> - Intercepto $z = -1$ cuando $x=y=0$
> 
> d) $z = |x| + |y|$
> 
> - **Pirámide cuadrada** (sin punta, con vértice)
> - Vértice en origen
> - Caras son planos
> 
> ---
> 
> **2. Trazas horizontales $z = x^2 + y^2$:**
> 
> a) $z = 0$: $x^2 + y^2 = 0$ → **Punto** $(0,0)$
> 
> b) $z = 4$: $x^2 + y^2 = 4$ → **Círculo** de radio 2
> 
> c) $z = 9$: $x^2 + y^2 = 9$ → **Círculo** de radio 3
> 
> ---
> 
> **3. Trazas verticales $z = x^2 - y^2$:**
> 
> a) $x = 0$: $z = -y^2$ → **Parábola** hacia abajo en plano $yz$
> 
> b) $y = 0$: $z = x^2$ → **Parábola** hacia arriba en plano $xz$
> 
> c) $x = 1$: $z = 1 - y^2$ → **Parábola** hacia abajo, vértice en $(1,0,1)$

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a) Análisis completo de $z = 16 - x^2 - y^2$:**
> 
> **Dominio:** $\mathbb{R}^2$ (todo el plano)
> 
> **Rango:** $(-\infty, 16]$
> 
> - Máximo: $z = 16$ en $(0,0)$
> - Sin cota inferior
> 
> **Trazas horizontales:**
> 
> - $z = 16$: $x^2 + y^2 = 0$ → punto $(0,0)$
> - $z = 12$: $x^2 + y^2 = 4$ → círculo radio 2
> - $z = 7$: $x^2 + y^2 = 9$ → círculo radio 3
> - $z = 0$: $x^2 + y^2 = 16$ → círculo radio 4
> 
> **Trazas verticales:**
> 
> - $x = 0$: $z = 16 - y^2$ (parábola hacia abajo)
> - $y = 0$: $z = 16 - x^2$ (parábola hacia abajo)
> 
> **Tipo:** Paraboloide circular hacia abajo
> 
> ---
> 
> **4b) Análisis de $z = xy$:**
> 
> **Forma:** Silla de montar (paraboloide hiperbólico)
> 
> **Regiones:**
> 
> - $z > 0$ cuando $xy > 0$ (cuadrantes I y III)
> - $z < 0$ cuando $xy < 0$ (cuadrantes II y IV)
> - $z = 0$ en los ejes $x$ e $y$
> 
> **Trazas horizontales:**
> 
> - $z = 1$: $xy = 1$ → hipérbola
> - $z = 0$: $xy = 0$ → ejes coordenados
> - $z = -1$: $xy = -1$ → hipérbola (cuadrantes II y IV)
> 
> ---
> 
> **5. Superficies cilíndricas:**
> 
> a) $z = x^2$ → **SÍ es cilíndrica** en dirección $y$ (no depende de $y$)
> 
> b) $z = \sin(y)$ → **SÍ es cilíndrica** en dirección $x$ (no depende de $x$)
> 
> c) $z = x^2 + y^2$ → **NO es cilíndrica** (depende de ambas variables)
> 
> ---
> 
> **6. Intersecciones:**
> 
> a) $z = x^2 + y^2$ con $z = 4$: $$4 = x^2 + y^2$$
> 
> - **Círculo** de radio 2 a altura $z = 4$
> - Puntos: $(x, y, 4)$ donde $x^2 + y^2 = 4$
> 
> b) $z = 4 - x^2 - y^2$ con $z = 0$: $$0 = 4 - x^2 - y^2$$ $$x^2 + y^2 = 4$$
> 
> - **Círculo** de radio 2 en el plano $xy$
> 
> c) $z = x^2 - y^2$ con $z = 0$: $$0 = x^2 - y^2$$ $$x^2 = y^2$$ $$y = \pm x$$
> 
> - **Dos rectas** que pasan por el origen: $y = x$ y $y = -x$

---

## 🎨 Herramientas Tecnológicas

> [!tip]- 💻 Software para Visualizar Superficies
> 
> ### Software Gratuito
> 
> **1. GeoGebra 3D**
> 
> - Gratuito y en línea
> - Interfaz intuitiva
> - Comando: `Superficie(x^2 + y^2, x, -3, 3, y, -3, 3)`
> - URL: www.geogebra.org/3d
> 
> **2. Desmos 3D Calculator**
> 
> - En línea, gratuito
> - Muy visual y fácil de usar
> - URL: www.desmos.com/3d
> 
> **3. WolframAlpha**
> 
> - Gratuito (con límites)
> - Comando: `plot z = x^2 + y^2`
> - URL: www.wolframalpha.com
> 
> **4. Python con Matplotlib**
> 
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> from mpl_toolkits.mplot3d import Axes3D
> 
> # Crear malla
> x = np.linspace(-5, 5, 100)
> y = np.linspace(-5, 5, 100)
> X, Y = np.meshgrid(x, y)
> Z = X**2 + Y**2  # Función
> 
> # Graficar
> fig = plt.figure()
> ax = fig.add_subplot(111, projection='3d')
> ax.plot_surface(X, Y, Z, cmap='viridis')
> plt.show()
> ```
> 
> **5. Octave/MATLAB**
> 
> ```matlab
> [X, Y] = meshgrid(-5:0.1:5, -5:0.1:5);
> Z = X.^2 + Y.^2;
> surf(X, Y, Z)
> xlabel('x'); ylabel('y'); zlabel('z')
> ```
> 
> ---
> 
> ### Software Profesional
> 
> **1. MATLAB** (de pago)
> 
> - Estándar en ingeniería
> - Excelentes gráficos 3D
> 
> **2. Mathematica** (de pago)
> 
> - Comando: `Plot3D[x^2 + y^2, {x, -3, 3}, {y, -3, 3}]`
> - Visualización de alta calidad
> 
> **3. Maple** (de pago)
> 
> - Especializado en matemática simbólica
> - Buenas herramientas de visualización

---

## 🔬 Conceptos Avanzados (Vista Previa)

> [!info]- 🎓 Temas Relacionados Avanzados
> 
> ### 1. Diferenciabilidad
> 
> Una superficie "suave" sin "esquinas" es diferenciable.
> 
> - $z = x^2 + y^2$ → **diferenciable** en todo punto
> - $z = |x| + |y|$ → **no diferenciable** en el origen (tiene "aristas")
> 
> ### 2. Plano Tangente
> 
> En cada punto de una superficie diferenciable existe un **plano tangente**.
> 
> - Es la mejor aproximación lineal a la superficie en ese punto
> - Se calcula usando derivadas parciales (tema futuro)
> 
> ### 3. Vector Normal
> 
> Perpendicular a la superficie en un punto.
> 
> - Útil para calcular ángulos, reflexiones
> - Se obtiene del gradiente
> 
> ### 4. Curvatura
> 
> Mide qué tan "curva" es la superficie.
> 
> - Paraboloide: curvatura positiva en todas direcciones
> - Silla de montar: curvatura positiva en una dirección, negativa en otra
> 
> ### 5. Optimización
> 
> Encontrar máximos y mínimos de la superficie.
> 
> - Puntos críticos: donde las derivadas parciales son cero
> - Clasificación: máximo, mínimo, punto silla

---

## 📊 Comparación: Curvas vs Superficies

> [!note]- 📐 Analogías 1D → 2D
> 
> |Concepto|Función 1 Variable|Función 2 Variables|
> |---|---|---|
> |**Entrada**|Número $x$|Punto $(x,y)$|
> |**Salida**|Número $y$|Número $z$|
> |**Gráfica**|Curva en $\mathbb{R}^2$|Superficie en $\mathbb{R}^3$|
> |**Dominio**|Intervalo en $\mathbb{R}$|Región en $\mathbb{R}^2$|
> |**Rango**|Intervalo en $\mathbb{R}$|Intervalo en $\mathbb{R}$|
> |**Traza**|Puntos (intersección con rectas)|Curvas (intersección con planos)|
> |**Tangente**|Recta tangente|Plano tangente|
> |**Derivada**|$f'(x)$ (número)|$\nabla f$ (vector)|
> |**Extremos**|Máximos/mínimos|Máximos/mínimos/sillas|
> |**Concavidad**|$f''(x)$|Matriz Hessiana|

---

## 🎯 Resumen de Superficies Importantes

> [!success]- 📋 Tabla Resumen
> 
> ### Superficies Cuadráticas (Segundo Grado)
> 
> |Ecuación General|Nombre|Forma Visual|
> |---|---|---|
> |$z = ax^2 + by^2$ (a,b > 0)|Paraboloide elíptico ↑|Cuenco|
> |$z = -ax^2 - by^2$ (a,b > 0)|Paraboloide elíptico ↓|Montaña|
> |$z = ax^2 - by^2$|Paraboloide hiperbólico|Silla|
> |$x^2 + y^2 + z^2 = r^2$|Esfera|Pelota|
> |$z = \sqrt{r^2-x^2-y^2}$|Hemisferio|Media pelota|
> |$x^2 + y^2 = r^2$|Cilindro circular|Tubo|
> |$z^2 = x^2 + y^2$|Cono|Cono helado|
> |$\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1$|Elipsoide|Pelota aplastada|
> |$\frac{x^2}{a^2}+\frac{y^2}{b^2}-\frac{z^2}{c^2}=1$|Hiperboloide de 1 hoja|Torre de enfriamiento|
> |$\frac{z^2}{c^2}-\frac{x^2}{a^2}-\frac{y^2}{b^2}=1$|Hiperboloide de 2 hojas|Dos cuencos opuestos|
> 
> ### Superficies No Cuadráticas
> 
> |Ecuación|Nombre|Características|
> |---|---|---|
> |$z = e^{-(x^2+y^2)}$|Gaussiana|Campana, decae exponencialmente|
> |$z = \sin(x)\cos(y)$|Onda 2D|Periódica en ambas direcciones|
> |$z = \ln(x^2+y^2)$|Logarítmica|Pozo infinito en origen|
> |$z = \frac{1}{x^2+y^2+1}$|Campana racional|Similar a gaussiana|

---

## 💡 Tips para Visualizar Mentalmente

> [!tip]- 🧠 Estrategias de Visualización
> 
> **1. Empieza con lo conocido:**
> 
> - Si reconoces $x^2 + y^2$, piensa en "distancia al origen"
> - Si ves $x^2 - y^2$, piensa en "diferencia de cuadrados → hipérbola"
> 
> **2. Analiza el signo:**
> 
> - Coeficiente positivo → "abre hacia arriba"
> - Coeficiente negativo → "abre hacia abajo"
> 
> **3. Busca simetrías:**
> 
> - Si solo aparece $x^2 + y^2$ (no $x$ o $y$ solos) → **simetría radial**
> - Si falta una variable → **superficie cilíndrica**
> 
> **4. Compara exponentes:**
> 
> - Grado 1 → **plano**
> - Grado 2 → **cuádrica** (paraboloide, silla, etc.)
> - Grado mayor → más complicada
> 
> **5. Evalúa casos especiales:**
> 
> - ¿Qué pasa en el origen?
> - ¿Qué pasa en los ejes?
> - ¿Hay máximos/mínimos evidentes?
> 
> **6. Usa trazas mentalmente:**
> 
> - "Si corto con $z = 0$, ¿qué obtengo?"
> - "Si corto con $x = 0$, ¿qué curva veo?"
> 
> **7. Piensa en contexto físico:**
> 
> - $z = c - x^2 - y^2$ → montaña con pico en centro
> - $z = x^2 + y^2$ → valle con fondo en centro
> - $z = xy$ → silla de montar

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones
> 
> **Este tema es prerequisito para:**
> 
> - [[04 - Curvas de Nivel]] - Proyección de las trazas horizontales
> - [[08 - Derivadas Parciales]] - Pendiente de la superficie en direcciones
> - [[11 - Gradiente]] - Vector perpendicular a curvas de nivel
> - **Planos Tangentes** - Aproximación lineal a la superficie
> - **Optimización** - Encontrar puntos más altos/bajos
> 
> **Temas relacionados:**
> 
> - [[01 - Definición de Funciones]] - Qué estamos graficando
> - [[02 - Dominio y Rango]] - Dónde existe la superficie
> - **Geometría Analítica 3D** - Ecuaciones de superficies
> - **Cálculo Vectorial** - Campos vectoriales sobre superficies
> 
> **Aplicaciones:**
> 
> - 🏔️ **Topografía** - Mapas de elevación
> - 🌡️ **Física** - Superficies equipotenciales
> - 💰 **Economía** - Superficies de utilidad, costos
> - 📊 **Estadística** - Distribuciones de probabilidad 2D
> - 🎮 **Gráficos por computadora** - Modelado 3D
> 
> **Siguiente tema recomendado:** [[04 - Curvas de Nivel]]

---

**Tags:** #calculo-multivariable #graficas-3d #superficies #visualizacion #paraboloide #geometria-3d #trazas #funciones-dos-variables #representacion-grafica