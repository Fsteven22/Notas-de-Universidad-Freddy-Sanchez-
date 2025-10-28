# 📘 Dominio y Rango

## 🎯 Introducción

> [!info]- 💡 ¿Por qué son importantes el Dominio y Rango? Al igual que en funciones de una variable, necesitamos saber:
> 
> - **Dominio:** ¿Dónde está definida la función? ¿Qué valores de entrada son válidos?
> - **Rango:** ¿Qué valores puede tomar la función? ¿Cuál es el conjunto de salidas posibles?
> 
> **Diferencia clave con funciones de una variable:**
> 
> - En $f(x)$: el dominio es un **intervalo** o **unión de intervalos** en $\mathbb{R}$
> - En $f(x,y)$: el dominio es una **región** en el **plano** $\mathbb{R}^2$
> - En $f(x,y,z)$: el dominio es una **región** en el **espacio** $\mathbb{R}^3$

---

## 📍 Dominio de Funciones Escalares

### 🔍 Definición

> [!example]- 🟢 Dominio: Conjunto de Puntos Válidos
> 
> **Definición formal:** El **dominio** de una función $f$ es el conjunto de todos los puntos en $\mathbb{R}^n$ donde la función está definida.
> 
> $$\text{Dom}(f) = {(x_1, x_2, ..., x_n) \in \mathbb{R}^n : f(x_1, x_2, ..., x_n) \text{ existe}}$$
> 
> **Para funciones de dos variables:** $$\text{Dom}(f) = {(x,y) \in \mathbb{R}^2 : f(x,y) \text{ está definida}}$$
> 
> **Para funciones de tres variables:** $$\text{Dom}(f) = {(x,y,z) \in \mathbb{R}^3 : f(x,y,z) \text{ está definida}}$$
> 
> **Dominio natural o implícito:** Si no se especifica, se asume el **dominio más grande posible** donde la función tiene sentido matemático.

### ⚠️ Restricciones Comunes

> [!warning]- 🚫 Operaciones que Restringen el Dominio
> 
> **1. División: Denominador ≠ 0** $$f(x,y) = \frac{1}{x-y}$$ Restricción: $x - y \neq 0$ → $x \neq y$
> 
> ---
> 
> **2. Raíz cuadrada: Radicando ≥ 0** $$f(x,y) = \sqrt{x + y}$$ Restricción: $x + y \geq 0$ → $y \geq -x$
> 
> ---
> 
> **3. Logaritmo: Argumento > 0** $$f(x,y) = \ln(x^2 + y^2 - 1)$$ Restricción: $x^2 + y^2 - 1 > 0$ → $x^2 + y^2 > 1$
> 
> ---
> 
> **4. Raíz par: Radicando ≥ 0** $$f(x,y) = \sqrt[4]{16 - x^2 - y^2}$$ Restricción: $16 - x^2 - y^2 \geq 0$ → $x^2 + y^2 \leq 16$
> 
> ---
> 
> **5. Tangente: Argumento ≠ π/2 + nπ** $$f(x,y) = \tan(xy)$$ Restricción: $xy \neq \frac{\pi}{2} + n\pi$, $n \in \mathbb{Z}$
> 
> ---
> 
> **6. Composición de restricciones:** $$f(x,y) = \frac{\sqrt{4-x^2-y^2}}{x-1}$$
> 
> - Raíz: $4 - x^2 - y^2 \geq 0$ → $x^2 + y^2 \leq 4$
> - División: $x - 1 \neq 0$ → $x \neq 1$
> - **Dominio:** Disco de radio 2, excluyendo la recta $x=1$

---

## 📚 Ejemplos de Dominios en $\mathbb{R}^2$

> [!example]- 📝 Ejemplo 1: Todo el Plano
> 
> **Función:** $f(x,y) = x^2 + y^2 + 3xy - 5$
> 
> **Análisis:**
> 
> - Solo hay operaciones algebraicas (suma, resta, multiplicación)
> - No hay restricciones
> 
> **Dominio:** $$\text{Dom}(f) = \mathbb{R}^2$$
> 
> **Representación:**
> 
> - Todo el plano $xy$
> - Región: **ilimitada**
> 
> **Otros ejemplos similares:**
> 
> - $f(x,y) = x^3y - xy^2 + 7$
> - $f(x,y) = e^{x+y}$
> - $f(x,y) = \sin(x) + \cos(y)$

> [!example]- 📝 Ejemplo 2: Interior de un Círculo
> 
> **Función:** $f(x,y) = \sqrt{9 - x^2 - y^2}$
> 
> **Restricción:** $$9 - x^2 - y^2 \geq 0$$ $$x^2 + y^2 \leq 9$$
> 
> **Dominio:** $$\text{Dom}(f) = {(x,y) \in \mathbb{R}^2 : x^2 + y^2 \leq 9}$$
> 
> **Representación geométrica:**
> 
> - Disco **cerrado** de radio 3 centrado en el origen
> - Incluye la circunferencia (por el $\leq$)
> - Región: **acotada**
> 
> **Puntos específicos:**
> 
> - $(0,0)$ → $0 + 0 = 0 \leq 9$ ✅ En el dominio
> - $(2,2)$ → $4 + 4 = 8 \leq 9$ ✅ En el dominio
> - $(3,0)$ → $9 + 0 = 9 \leq 9$ ✅ En el dominio (borde)
> - $(3,3)$ → $9 + 9 = 18 > 9$ ❌ Fuera del dominio

> [!example]- 📝 Ejemplo 3: Exterior de un Círculo
> 
> **Función:** $f(x,y) = \ln(x^2 + y^2 - 4)$
> 
> **Restricción:** $$x^2 + y^2 - 4 > 0$$ $$x^2 + y^2 > 4$$
> 
> **Dominio:** $$\text{Dom}(f) = {(x,y) \in \mathbb{R}^2 : x^2 + y^2 > 4}$$
> 
> **Representación geométrica:**
> 
> - **Exterior** de la circunferencia de radio 2
> - **No incluye** la circunferencia (por el $>$)
> - Región: **ilimitada**
> 
> **Frontera:** Circunferencia $x^2 + y^2 = 4$ (no incluida)

> [!example]- 📝 Ejemplo 4: Semiplano
> 
> **Función:** $f(x,y) = \sqrt{y - x^2}$
> 
> **Restricción:** $$y - x^2 \geq 0$$ $$y \geq x^2$$
> 
> **Dominio:** $$\text{Dom}(f) = {(x,y) \in \mathbb{R}^2 : y \geq x^2}$$
> 
> **Representación geométrica:**
> 
> - Región **arriba** de la parábola $y = x^2$
> - Incluye la parábola misma
> - Región: **ilimitada**
> 
> **Puntos de verificación:**
> 
> - $(0,0)$ → $0 \geq 0$ ✅ En el dominio (sobre la parábola)
> - $(1,2)$ → $2 \geq 1$ ✅ En el dominio
> - $(2,3)$ → $3 \geq 4$ ❌ Fuera del dominio
> - $(0,5)$ → $5 \geq 0$ ✅ En el dominio

> [!example]- 📝 Ejemplo 5: Anillo
> 
> **Función:** $f(x,y) = \sqrt{25 - x^2 - y^2} + \sqrt{x^2 + y^2 - 9}$
> 
> **Restricciones:**
> 
> 1. Primera raíz: $25 - x^2 - y^2 \geq 0$ → $x^2 + y^2 \leq 25$
> 2. Segunda raíz: $x^2 + y^2 - 9 \geq 0$ → $x^2 + y^2 \geq 9$
> 
> **Dominio (intersección):** $$\text{Dom}(f) = {(x,y) : 9 \leq x^2 + y^2 \leq 25}$$
> 
> **Representación geométrica:**
> 
> - **Anillo** (corona circular)
> - Radio interior: 3 (incluido)
> - Radio exterior: 5 (incluido)
> - Región: **acotada**

> [!example]- 📝 Ejemplo 6: Cuadrantes
> 
> **Función:** $f(x,y) = \ln(xy)$
> 
> **Restricción:** $$xy > 0$$
> 
> **Análisis:** $xy > 0$ cuando:
> 
> - $x > 0$ y $y > 0$ (primer cuadrante), O
> - $x < 0$ y $y < 0$ (tercer cuadrante)
> 
> **Dominio:** $$\text{Dom}(f) = {(x,y) : xy > 0}$$
> 
> **Representación geométrica:**
> 
> - **Primer y tercer cuadrante** (sin los ejes)
> - Región: **ilimitada** y **disconectada** (dos partes separadas)

> [!example]- 📝 Ejemplo 7: Dominio con Recta Excluida
> 
> **Función:** $f(x,y) = \frac{x + y}{x - y}$
> 
> **Restricción:** $$x - y \neq 0$$ $$x \neq y$$
> 
> **Dominio:** $$\text{Dom}(f) = {(x,y) \in \mathbb{R}^2 : x \neq y}$$
> 
> **Representación geométrica:**
> 
> - Todo el plano **excepto** la recta $y = x$
> - La recta $y = x$ es una **discontinuidad**
> - Región: **ilimitada**

> [!example]- 📝 Ejemplo 8: Dominio Complejo
> 
> **Función:** $f(x,y) = \frac{\sqrt{16 - x^2 - y^2}}{x + y - 2}$
> 
> **Restricciones:**
> 
> 1. Raíz: $16 - x^2 - y^2 \geq 0$ → $x^2 + y^2 \leq 16$
> 2. División: $x + y - 2 \neq 0$ → $x + y \neq 2$
> 
> **Dominio:** $$\text{Dom}(f) = {(x,y) : x^2 + y^2 \leq 16 \text{ y } x + y \neq 2}$$
> 
> **Representación geométrica:**
> 
> - Disco de radio 4
> - Sin la cuerda donde la recta $x + y = 2$ corta el disco
> - La recta atraviesa el disco desde $(-2,4)$ hasta $(4,-2)$

---

## 🔮 Ejemplos de Dominios en $\mathbb{R}^3$

> [!example]- 📝 Ejemplo 9: Todo el Espacio
> 
> **Función:** $f(x,y,z) = x^2 + y^2 + z^2 + xyz$
> 
> **Dominio:** $$\text{Dom}(f) = \mathbb{R}^3$$
> 
> **Representación:** Todo el espacio tridimensional (no se puede visualizar completamente, pero conceptualmente es "todo")

> [!example]- 📝 Ejemplo 10: Interior de una Esfera
> 
> **Función:** $f(x,y,z) = \sqrt{25 - x^2 - y^2 - z^2}$
> 
> **Restricción:** $$25 - x^2 - y^2 - z^2 \geq 0$$ $$x^2 + y^2 + z^2 \leq 25$$
> 
> **Dominio:** $$\text{Dom}(f) = {(x,y,z) \in \mathbb{R}^3 : x^2 + y^2 + z^2 \leq 25}$$
> 
> **Representación geométrica:**
> 
> - **Bola sólida** de radio 5 centrada en el origen
> - Incluye la superficie esférica
> - Región: **acotada** en $\mathbb{R}^3$

> [!example]- 📝 Ejemplo 11: Región entre Planos
> 
> **Función:** $f(x,y,z) = \sqrt{z - x - y} \cdot \sqrt{5 - z}$
> 
> **Restricciones:**
> 
> 1. Primera raíz: $z - x - y \geq 0$ → $z \geq x + y$
> 2. Segunda raíz: $5 - z \geq 0$ → $z \leq 5$
> 
> **Dominio:** $$\text{Dom}(f) = {(x,y,z) : z \geq x + y \text{ y } z \leq 5}$$
> 
> **Representación geométrica:**
> 
> - Región entre el plano $z = x + y$ y el plano $z = 5$
> - Arriba del plano inclinado, abajo del plano horizontal
> - Región: **ilimitada** (se extiende infinitamente en $x$ e $y$)

> [!example]- 📝 Ejemplo 12: Cono Truncado
> 
> **Función:** $f(x,y,z) = \ln(z^2 - x^2 - y^2)$
> 
> **Restricción:** $$z^2 - x^2 - y^2 > 0$$ $$z^2 > x^2 + y^2$$ $$|z| > \sqrt{x^2 + y^2}$$
> 
> **Dominio:** Exterior del cono doble $z^2 = x^2 + y^2$
> 
> **Representación geométrica:**
> 
> - Región **fuera** del cono circular recto
> - No incluye el cono mismo
> - Región: **ilimitada**

---

## 🎨 Rango de Funciones Escalares

### 🔍 Definición

> [!example]- 🟡 Rango: Conjunto de Valores Posibles
> 
> **Definición formal:** El **rango** (o imagen) de una función $f$ es el conjunto de todos los valores que la función puede tomar.
> 
> $$\text{Ran}(f) = {z \in \mathbb{R} : z = f(x,y) \text{ para algún } (x,y) \in \text{Dom}(f)}$$
> 
> **En otras palabras:** Es el conjunto de todas las **salidas posibles** de la función.
> 
> **Notación alternativa:**
> 
> - $\text{Ran}(f)$ o $\text{Im}(f)$ (imagen)
> - $f(\text{Dom}(f))$ (imagen del dominio)

### 📊 Métodos para Encontrar el Rango

> [!tip]- 🔧 Estrategias
> 
> **Método 1: Análisis algebraico**
> 
> - Despejar la variable dependiente
> - Determinar valores posibles
> 
> **Método 2: Valores extremos**
> 
> - Encontrar máximos y mínimos
> - Usar derivadas (si se conocen)
> 
> **Método 3: Análisis geométrico**
> 
> - Interpretar la función geométricamente
> - Visualizar la superficie
> 
> **Método 4: Sustitución**
> 
> - Evaluar en puntos específicos
> - Encontrar cotas superiores e inferiores

---

## 📚 Ejemplos de Rangos

> [!example]- 📝 Ejemplo 13: Paraboloide
> 
> **Función:** $f(x,y) = x^2 + y^2$
> 
> **Dominio:** $\mathbb{R}^2$ (todo el plano)
> 
> **Análisis del rango:**
> 
> - $x^2 \geq 0$ y $y^2 \geq 0$ para todo $x,y \in \mathbb{R}$
> - Por tanto: $x^2 + y^2 \geq 0$
> - El valor mínimo es $f(0,0) = 0$
> - No hay cota superior (crece infinitamente)
> 
> **Rango:** $$\text{Ran}(f) = [0, +\infty)$$
> 
> **Interpretación geométrica:** La función representa un paraboloide que se abre hacia arriba, con vértice en el origen a altura $z = 0$.

> [!example]- 📝 Ejemplo 14: Hemisferio
> 
> **Función:** $f(x,y) = \sqrt{9 - x^2 - y^2}$
> 
> **Dominio:** ${(x,y) : x^2 + y^2 \leq 9}$
> 
> **Análisis del rango:**
> 
> - En el centro $(0,0)$: $f(0,0) = \sqrt{9} = 3$ (valor máximo)
> - En el borde, cuando $x^2 + y^2 = 9$: $f = \sqrt{0} = 0$ (valor mínimo)
> - Por continuidad, toma todos los valores entre 0 y 3
> 
> **Rango:** $$\text{Ran}(f) = [0, 3]$$
> 
> **Interpretación geométrica:** Hemisferio superior de radio 3.

> [!example]- 📝 Ejemplo 15: Función Periódica
> 
> **Función:** $f(x,y) = \sin(x) + \cos(y)$
> 
> **Dominio:** $\mathbb{R}^2$
> 
> **Análisis del rango:**
> 
> - $\sin(x) \in [-1, 1]$
> - $\cos(y) \in [-1, 1]$
> - Suma: mínimo cuando ambos son $-1$: $-1 + (-1) = -2$
> - Suma: máximo cuando ambos son $1$: $1 + 1 = 2$
> - Por continuidad, toma todos los valores intermedios
> 
> **Rango:** $$\text{Ran}(f) = [-2, 2]$$

> [!example]- 📝 Ejemplo 16: Función Racional
> 
> **Función:** $f(x,y) = \frac{xy}{x^2 + y^2}$ para $(x,y) \neq (0,0)$
> 
> **Dominio:** $\mathbb{R}^2 \setminus {(0,0)}$
> 
> **Análisis (usando coordenadas polares):** Sea $x = r\cos\theta$, $y = r\sin\theta$: $$f = \frac{r^2\cos\theta\sin\theta}{r^2} = \cos\theta\sin\theta = \frac{1}{2}\sin(2\theta)$$
> 
> Como $\sin(2\theta) \in [-1, 1]$:
> 
> **Rango:** $$\text{Ran}(f) = \left[-\frac{1}{2}, \frac{1}{2}\right]$$

> [!example]- 📝 Ejemplo 17: Función con Rango Discreto
> 
> **Función:** $f(x,y) = \lfloor x \rfloor + \lfloor y \rfloor$
> 
> Donde $\lfloor \cdot \rfloor$ es la función piso (parte entera).
> 
> **Dominio:** $\mathbb{R}^2$
> 
> **Análisis:**
> 
> - $\lfloor x \rfloor \in \mathbb{Z}$ (enteros)
> - $\lfloor y \rfloor \in \mathbb{Z}$ (enteros)
> - Suma de enteros es entero
> 
> **Rango:** $$\text{Ran}(f) = \mathbb{Z}$$
> 
> **Observación:** El rango es **discreto**, no un intervalo continuo.

> [!example]- 📝 Ejemplo 18: Exponencial
> 
> **Función:** $f(x,y) = e^{-(x^2+y^2)}$
> 
> **Dominio:** $\mathbb{R}^2$
> 
> **Análisis del rango:**
> 
> - $x^2 + y^2 \geq 0$ siempre
> - Cuando $(x,y) = (0,0)$: $f(0,0) = e^0 = 1$ (máximo)
> - Cuando $x^2 + y^2 \to \infty$: $f \to e^{-\infty} = 0$ (ínfimo, nunca alcanzado)
> - $e^{-t} \in (0,1]$ para $t \geq 0$
> 
> **Rango:** $$\text{Ran}(f) = (0, 1]$$
> 
> **Nota:** El 0 no se alcanza, pero 1 sí (en el origen).

---

## 🖼️ Representación Gráfica

### 📊 Graficación de Dominios en $\mathbb{R}^2$

> [!note]- 🎨 Cómo Representar Dominios en el Plano
> 
> **Pasos para graficar:**
> 
> 1. **Identificar restricciones** (desigualdades)
> 2. **Graficar las fronteras** (igualdades)
> 3. **Determinar el lado correcto** (probar un punto)
> 4. **Sombrear la región del dominio**
> 5. **Indicar si se incluyen las fronteras** (línea sólida vs punteada)
> 
> **Convenciones:**
> 
> - **Línea sólida (—):** Frontera incluida ($\leq$ o $\geq$)
> - **Línea punteada (- - -):** Frontera no incluida ($<$ o $>$)
> - **Sombreado:** Región del dominio

### 🎯 Ejemplos Visualizados

> [!example]- 🖼️ Ejemplo Visual 1: Disco
> 
> **Función:** $f(x,y) = \sqrt{4 - x^2 - y^2}$
> 
> **Dominio:** $x^2 + y^2 \leq 4$
> 
> **Representación:**
> 
> ```
>      y
>      |
>    2 |     ●●●●●
>      |   ●●●●●●●●●
>    1 | ●●●●●●●●●●●●
>   ---|●●●●●●●●●●●●●|--- x
>   -2 | ●●●●●●●●●●●●  2
>   -1 | ●●●●●●●●●●●●
>      |   ●●●●●●●●●
>   -2 |     ●●●●●
>      |
> ```
> 
> - Círculo centrado en el origen
> - Radio = 2
> - Frontera **incluida** (línea sólida)

> [!example]- 🖼️ Ejemplo Visual 2: Región Parabólica
> 
> **Función:** $f(x,y) = \sqrt{y - x^2}$
> 
> **Dominio:** $y \geq x^2$
> 
> **Representación:**
> 
> ```
>      y
>    5 |  ●●●●●●●●●●●●●
>      |  ●●●●●●●●●●●●●
>    3 |  ●●●●●●●●●●●●●
>      |  ●●●●●●●●●●●●●
>    1 |  ●●●●●●●●●●●●●
>      |   ●●●●●●●●●●●
>    0 |    ●●●—————●●●
>      |     ●●   ●●
>   ---|-------|-------|--- x
>     -2      0       2
> ```
> 
> - Región **arriba** de la parábola $y = x^2$
> - La parábola está **incluida** (línea sólida)
> - Se extiende infinitamente hacia arriba

> [!example]- 🖼️ Ejemplo Visual 3: Anillo
> 
> **Función:** Anillo entre $r=1$ y $r=3$
> 
> **Dominio:** $1 \leq x^2 + y^2 \leq 9$
> 
> **Representación:**
> 
> ```
>      y
>    3 |    ●●●●●●●●●
>      |  ●●●●●●●●●●●●●
>    2 | ●●●●       ●●●●
>      | ●●●         ●●●
>    1 | ●●   (···)   ●●
>   ---●●     ···     ●●--- x
>   -1 | ●●   (···)   ●●
>      | ●●●         ●●●
>   -2 | ●●●●       ●●●●
>      |  ●●●●●●●●●●●●●
>   -3 |    ●●●●●●●●●
> ```
> 
> - Anillo entre radio 1 y radio 3
> - Ambas circunferencias **incluidas**

---

## 🎓 Dominio vs Rango: Tabla Resumen

> [!note]- 📋 Comparación
> 
> |Aspecto|Dominio|Rango|
> |---|---|---|
> |**Definición**|Conjunto de **entradas** válidas|Conjunto de **salidas** posibles|
> |**Notación**|$\text{Dom}(f)$|$\text{Ran}(f)$ o $\text{Im}(f)$|
> |**Para $f:\mathbb{R}^2\to\mathbb{R}$**|Región en el plano $xy$|Intervalo en el eje $z$|
> |**Para $f:\mathbb{R}^3\to\mathbb{R}$**|Región en el espacio $xyz$|Intervalo en $\mathbb{R}$|
> |**Cómo encontrarlo**|Analizar restricciones|Analizar valores extremos|
> |**Representación**|Gráfica en $\mathbb{R}^n$|Intervalo o conjunto en $\mathbb{R}$|

---

## 💡 Consejos Prácticos

> [!tip]- ⭐ Estrategias para Encontrar Dominios
> 
> **Checklist de verificación:**
> 
> 1. ✅ **¿Hay raíces pares?** → Radicando ≥ 0
> 2. ✅ **¿Hay divisiones?** → Denominador ≠ 0
> 3. ✅ **¿Hay logaritmos?** → Argumento > 0
> 4. ✅ **¿Hay tangentes/secantes?** → Evitar asíntotas verticales
> 5. ✅ **¿Hay arcoseno/arcocoseno?** → Argumento ∈ [-1,1]
> 6. ✅ **¿Hay múltiples restricciones?** → Intersección de todas
> 
> **Errores comunes:**
> 
> - ❌ Olvidar que $\sqrt{x}$ requiere $x \geq 0$ (no solo $x > 0$)
> - ❌ Confundir $<$ con $\leq$ en las fronteras
> - ❌ No considerar todas las restricciones simultáneamente
> - ❌ Olvidar que $\ln(x)$ requiere $x > 0$ (estrictamente positivo)

---

## 📝 Ejercicios Propuestos

> [!example]- 💪 Práctica Guiada
> 
> ### Nivel Básico
> 
> **1. Encontrar el dominio de las siguientes funciones:**
> 
> a) $f(x,y) = x^2 + y^2 - 3xy + 7$
> 
> b) $f(x,y) = \sqrt{x + y}$
> 
> c) $f(x,y) = \frac{1}{x + y}$
> 
> d) $f(x,y) = \ln(x - y)$
> 
> e) $f(x,y) = \sqrt{16 - x^2 - y^2}$
> 
> ---
> 
> **2. Determinar si los siguientes puntos están en el dominio:**
> 
> Para $f(x,y) = \sqrt{9 - x^2 - y^2}$:
> 
> - $(0,0)$
> - $(3,0)$
> - $(2,2)$
> - $(1,1)$
> - $(4,0)$
> 
> ---
> 
> ### Nivel Intermedio
> 
> **3. Encontrar dominio y rango:**
> 
> a) $f(x,y) = 4 - x^2 - y^2$
> 
> b) $f(x,y) = \sqrt{x^2 + y^2 - 1}$
> 
> c) $f(x,y) = e^{-(x^2+y^2)}$
> 
> d) $f(x,y) = \frac{xy}{x^2 + y^2 + 1}$
> 
> e) $f(x,y) = \arcsin(x + y)$
> 
> ---
> 
> **4. Funciones de tres variables:**
> 
> a) $f(x,y,z) = \sqrt{1 - x^2 - y^2 - z^2}$
> 
> b) $f(x,y,z) = \frac{1}{\sqrt{x^2 + y^2 + z^2 - 4}}$
> 
> c) $f(x,y,z) = \ln(z - x^2 - y^2)$
> 
> ---
> 
> ### Nivel Avanzado
> 
> **5. Dominios complejos:**
> 
> a) $f(x,y) = \sqrt{y - x^2} + \sqrt{1 - x^2 - y^2}$
> 
> b) $f(x,y) = \frac{\sqrt{9 - x^2 - y^2}}{x^2 + y^2 - 1}$
> 
> c) $f(x,y) = \ln(xy) + \sqrt{4 - x^2 - y^2}$
> 
> d) $f(x,y) = \frac{1}{\sqrt{x + y}} + \frac{1}{\sqrt{1 - x - y}}$
> 
> ---
> 
> **6. Determinar el rango:**
> 
> a) $f(x,y) = x^2 + 2y^2 + 1$
> 
> b) $f(x,y) = \sin(x)\cos(y)$
> 
> c) $f(x,y) = \frac{x^2 + y^2}{x^2 + y^2 + 1}$
> 
> ---
> 
> **7. Problemas aplicados:**
> 
> a) La temperatura en una placa metálica está dada por $T(x,y) = 100 - x^2 - y^2$ (en °C). ¿Cuál es el rango de temperaturas si la placa es un disco de radio 5?
> 
> b) El costo de producción está dado por $C(x,y) = 500 + 3x + 4y$ donde $x$ e $y$ son cantidades de dos materiales. Si se necesita que $x + y \leq 100$ y ambos sean no negativos, ¿cuál es el dominio y el rango de costos posibles?

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas de Ejercicios Básicos
> 
> **1a)** $f(x,y) = x^2 + y^2 - 3xy + 7$
> 
> - **Dominio:** $\mathbb{R}^2$ (todo el plano)
> - No hay restricciones
> 
> ---
> 
> **1b)** $f(x,y) = \sqrt{x + y}$
> 
> - **Restricción:** $x + y \geq 0$ → $y \geq -x$
> - **Dominio:** ${(x,y) : y \geq -x}$
> - Semiplano arriba de la recta $y = -x$ (incluye la recta)
> 
> ---
> 
> **1c)** $f(x,y) = \frac{1}{x + y}$
> 
> - **Restricción:** $x + y \neq 0$ → $y \neq -x$
> - **Dominio:** ${(x,y) : y \neq -x}$
> - Todo el plano excepto la recta $y = -x$
> 
> ---
> 
> **1d)** $f(x,y) = \ln(x - y)$
> 
> - **Restricción:** $x - y > 0$ → $y < x$
> - **Dominio:** ${(x,y) : y < x}$
> - Semiplano debajo de la recta $y = x$ (no incluye la recta)
> 
> ---
> 
> **1e)** $f(x,y) = \sqrt{16 - x^2 - y^2}$
> 
> - **Restricción:** $16 - x^2 - y^2 \geq 0$ → $x^2 + y^2 \leq 16$
> - **Dominio:** Disco cerrado de radio 4
> - **Rango:** $[0, 4]$
> 
> ---
> 
> **2)** Para $f(x,y) = \sqrt{9 - x^2 - y^2}$, verificar $x^2 + y^2 \leq 9$:
> 
> - $(0,0)$: $0 + 0 = 0 \leq 9$ ✅
> - $(3,0)$: $9 + 0 = 9 \leq 9$ ✅ (en la frontera)
> - $(2,2)$: $4 + 4 = 8 \leq 9$ ✅
> - $(1,1)$: $1 + 1 = 2 \leq 9$ ✅
> - $(4,0)$: $16 + 0 = 16 > 9$ ❌

> [!success]- 🔑 Respuestas de Ejercicios Intermedios
> 
> **3a)** $f(x,y) = 4 - x^2 - y^2$
> 
> - **Dominio:** $\mathbb{R}^2$
> - **Rango:** $(-\infty, 4]$
>     - Máximo en $(0,0)$: $f(0,0) = 4$
>     - Sin cota inferior
> 
> ---
> 
> **3b)** $f(x,y) = \sqrt{x^2 + y^2 - 1}$
> 
> - **Dominio:** ${(x,y) : x^2 + y^2 \geq 1}$ (exterior del círculo unitario, incluye la circunferencia)
> - **Rango:** $[0, +\infty)$
>     - Mínimo en la circunferencia: $f = 0$
>     - Sin cota superior
> 
> ---
> 
> **3c)** $f(x,y) = e^{-(x^2+y^2)}$
> 
> - **Dominio:** $\mathbb{R}^2$
> - **Rango:** $(0, 1]$
>     - Máximo en $(0,0)$: $f(0,0) = e^0 = 1$
>     - Ínfimo (no alcanzado): $\lim_{x^2+y^2\to\infty} f = 0$
> 
> ---
> 
> **3d)** $f(x,y) = \frac{xy}{x^2 + y^2 + 1}$
> 
> - **Dominio:** $\mathbb{R}^2$
> - **Rango:** $\left[-\frac{1}{2}, \frac{1}{2}\right]$
>     - Usando desigualdad AM-GM o coordenadas polares
> 
> ---
> 
> **3e)** $f(x,y) = \arcsin(x + y)$
> 
> - **Restricción:** $-1 \leq x + y \leq 1$
> - **Dominio:** ${(x,y) : -1 \leq x + y \leq 1}$ (franja entre dos rectas paralelas)
> - **Rango:** $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$
> 
> ---
> 
> **4a)** $f(x,y,z) = \sqrt{1 - x^2 - y^2 - z^2}$
> 
> - **Dominio:** ${(x,y,z) : x^2 + y^2 + z^2 \leq 1}$ (bola unitaria sólida)
> - **Rango:** $[0, 1]$
> 
> ---
> 
> **4b)** $f(x,y,z) = \frac{1}{\sqrt{x^2 + y^2 + z^2 - 4}}$
> 
> - **Restricción:** $x^2 + y^2 + z^2 - 4 > 0$ → $x^2 + y^2 + z^2 > 4$
> - **Dominio:** Exterior de la esfera de radio 2 (no incluye la esfera)
> - **Rango:** $(0, +\infty)$

---

## 🎯 Casos Especiales y Consideraciones

> [!warning]- ⚠️ Situaciones Especiales
> 
> ### 1. Funciones Definidas por Partes
> 
> **Ejemplo:** $$f(x,y) = \begin{cases} \frac{xy}{x^2 + y^2} & \text{si } (x,y) \neq (0,0) \ 0 & \text{si } (x,y) = (0,0) \end{cases}$$
> 
> - **Dominio:** $\mathbb{R}^2$ (todo el plano)
> - El origen está **explícitamente definido**
> 
> ---
> 
> ### 2. Dominios No Conexos
> 
> **Ejemplo:** $f(x,y) = \sqrt{(x^2 + y^2 - 1)(9 - x^2 - y^2)}$
> 
> **Restricción:** $(x^2 + y^2 - 1)(9 - x^2 - y^2) \geq 0$
> 
> Esto se cumple cuando:
> 
> - Ambos factores son no negativos, O
> - Ambos factores son no positivos
> 
> **Análisis:**
> 
> - Factor 1 positivo y Factor 2 positivo: $1 \leq x^2 + y^2 \leq 9$ (anillo)
> - Factor 1 negativo y Factor 2 negativo: imposible
> 
> **Dominio:** Anillo entre $r=1$ y $r=3$
> 
> ---
> 
> ### 3. Dominios con Agujeros
> 
> **Ejemplo:** $f(x,y) = \frac{1}{(x^2 + y^2 - 1)(x^2 + y^2 - 4)}$
> 
> **Restricciones:**
> 
> - $x^2 + y^2 \neq 1$ (circunferencia interior)
> - $x^2 + y^2 \neq 4$ (circunferencia exterior)
> 
> **Dominio:** $\mathbb{R}^2$ menos dos circunferencias
> 
> ---
> 
> ### 4. Dominios en Contextos Aplicados
> 
> **Ejemplo:** Costo de producción $C(x,y) = 500 + 20x + 30y$
> 
> **Restricciones prácticas:**
> 
> - $x \geq 0$ (no se puede producir cantidad negativa)
> - $y \geq 0$
> - $x + y \leq 100$ (capacidad máxima)
> - Tal vez: $x \leq 60$, $y \leq 80$ (disponibilidad de materiales)
> 
> **Dominio:** Región poligonal en el primer cuadrante
> 
> ---
> 
> ### 5. Funciones con Dominio Discreto
> 
> **Ejemplo:** $f(x,y) = x! + y!$ (factorial)
> 
> **Dominio:** Solo enteros no negativos $$\text{Dom}(f) = {(x,y) : x,y \in \mathbb{Z}, x \geq 0, y \geq 0}$$
> 
> **Observación:** El dominio es un conjunto de **puntos aislados**, no una región continua.

---

## 🔬 Relación Dominio-Rango con la Gráfica

> [!info]- 📐 Interpretación Geométrica
> 
> Para una función $z = f(x,y)$:
> 
> ### Dominio
> 
> - Es la **"sombra"** de la superficie en el plano $xy$
> - Es la **proyección** de la superficie sobre el plano $xy$
> - Representa **dónde existe** la superficie
> 
> ### Rango
> 
> - Es el **intervalo de alturas** que alcanza la superficie
> - Se proyecta sobre el **eje $z$**
> - Representa **qué tan alto y bajo** llega la superficie
> 
> ### Ejemplo Visual: Hemisferio
> 
> **Función:** $z = \sqrt{9 - x^2 - y^2}$
> 
> ```
>         z
>         |
>       3 |     ___
>         |   /     \
>       2 |  |       |
>         |  |       |
>       1 |  |       |
>         |   \_____/
>     ----+----------------- y
>        /|  -3  0  3
>       / |
>      /  |
>     x   |
> ```
> 
> - **Superficie:** Hemisferio superior de radio 3
> - **Dominio (sombra en xy):** Disco $x^2 + y^2 \leq 9$
> - **Rango (proyección en z):** $[0, 3]$
> 
> ---
> 
> ### Ejemplo Visual: Paraboloide
> 
> **Función:** $z = x^2 + y^2$
> 
> - **Superficie:** Paraboloide que se abre hacia arriba
> - **Dominio:** Todo el plano $xy$ (la superficie está definida en todas partes)
> - **Rango:** $[0, +\infty)$ (la superficie empieza en $z=0$ y crece sin límite)

---

## 📊 Resumen Visual: Tipos de Dominios Comunes

> [!note]- 🗺️ Galería de Dominios en $\mathbb{R}^2$
> 
> |Descripción|Condición|Representación|
> |---|---|---|
> |**Todo el plano**|Sin restricciones|$\mathbb{R}^2$|
> |**Disco cerrado**|$x^2 + y^2 \leq r^2$|⬤ (círculo relleno)|
> |**Disco abierto**|$x^2 + y^2 < r^2$|○ (círculo sin borde)|
> |**Exterior de círculo**|$x^2 + y^2 > r^2$|Todo excepto disco|
> |**Anillo**|$r_1^2 \leq x^2 + y^2 \leq r_2^2$|🍩 (corona)|
> |**Semiplano superior**|$y > mx + b$|Región arriba de recta|
> |**Semiplano inferior**|$y < mx + b$|Región abajo de recta|
> |**Franja horizontal**|$a < y < b$|Entre dos rectas paralelas|
> |**Franja vertical**|$a < x < b$|Entre dos rectas paralelas|
> |**Cuadrantes I y III**|$xy > 0$|Dos regiones opuestas|
> |**Cuadrantes II y IV**|$xy < 0$|Dos regiones opuestas|
> |**Región parabólica**|$y > x^2$|Arriba de parábola|
> |**Interior de elipse**|$\frac{x^2}{a^2} + \frac{y^2}{b^2} < 1$|Elipse rellena|

---

## 🎓 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Importantes
> 
> **Sobre el Dominio:**
> 
> 1. ✅ El dominio es un **subconjunto de $\mathbb{R}^n$** (región geométrica)
> 2. ✅ Siempre verifica **todas** las restricciones simultáneamente
> 3. ✅ Usa líneas **sólidas** para fronteras incluidas ($\leq, \geq$)
> 4. ✅ Usa líneas **punteadas** para fronteras excluidas ($<, >$)
> 5. ✅ El dominio puede ser **ilimitado** (se extiende al infinito)
> 6. ✅ El dominio puede ser **disconectado** (varias partes separadas)
> 
> **Sobre el Rango:**
> 
> 1. ✅ El rango es un **subconjunto de $\mathbb{R}$** (intervalo o unión de intervalos)
> 2. ✅ Encuentra valores **máximos y mínimos** para determinar el rango
> 3. ✅ El rango puede ser **acotado** o **no acotado**
> 4. ✅ Verifica si los extremos se **alcanzan** o solo se aproximan
> 5. ✅ Para funciones continuas en dominios compactos, se alcanzan máx y mín (Teorema del Valor Extremo)
> 
> **Estrategias:**
> 
> - 🔍 Para **dominio**: piensa "¿dónde tiene sentido la función?"
> - 🔍 Para **rango**: piensa "¿qué valores puede dar como salida?"
> - 🔍 Usa la **geometría** para visualizar regiones
> - 🔍 **Prueba puntos** específicos para verificar tus conclusiones

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones
> 
> **Este tema es prerequisito para:**
> 
> - [[03 - Gráfico de Funciones]] - Para graficar, primero necesitas saber dónde está definida
> - [[04 - Curvas de Nivel]] - Las curvas de nivel solo existen en el dominio
> - [[06 - Límites]] - Los límites se analizan en puntos del dominio o frontera
> - [[07 - Continuidad]] - Una función solo es continua en su dominio
> - [[08 - Derivadas Parciales]] - Solo se calculan en puntos del dominio
> 
> **Conceptos relacionados:**
> 
> - **Conjuntos abiertos/cerrados** - Propiedades topológicas del dominio
> - **Conjuntos compactos** - Importantes para teoremas de existencia
> - **Fronteras** - Puntos límite entre dominio y exterior
> - **Conexidad** - ¿El dominio es una sola pieza o varias?
> 
> **Siguiente tema recomendado:** [[03 - Gráfico de una función z=f(x,y)]]

---

**Tags:** #calculo-multivariable #dominio #rango #funciones-varias-variables #restricciones #regiones #geometria-analitica #conjuntos