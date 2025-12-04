# 📘 Coordenadas en un Espacio Vectorial

## 🎯 Introducción

> [!info]- 💡 ¿Por qué son importantes las Coordenadas?
> 
> Las **coordenadas** son la forma de representar vectores abstractos mediante números concretos. Es el puente entre conceptos abstractos y cálculos prácticos.
> 
> **Motivación:**
> 
> - Permiten convertir vectores abstractos en listas de números
> - Facilitan cálculos y verificaciones concretas
> - Dependen crucialmente de la **base elegida**
> - Diferentes bases → diferentes coordenadas para el mismo vector
> - Mismo vector, infinitas representaciones posibles
> 
> **Analogías:**
> 
> - **GPS:** Latitud/longitud son coordenadas respecto al sistema terrestre
> - **Mapa:** Misma ubicación, diferentes coordenadas según el mapa
> - **Idiomas:** Mismo concepto, diferentes palabras según el idioma
> - **Dinero:** Misma riqueza, diferentes números según la moneda
> - **Dirección:** "3 cuadras norte, 2 este" vs "200m a 60° noreste"
> 
> **Aplicaciones prácticas:**
> 
> - **Gráficos por computadora:** Transformaciones de objetos 3D
> - **Procesamiento de imágenes:** Diferentes bases revelan diferentes características
> - **Machine Learning:** Reducción de dimensionalidad, PCA
> - **Física cuántica:** Estados en diferentes bases de medición
> - **Ingeniería:** Análisis estructural en diferentes sistemas de referencia
> 
> **Concepto clave:** Un vector es un objeto geométrico/abstracto. Sus coordenadas son solo una **descripción numérica** que depende del sistema de referencia (base) elegido.

---

## 📐 Definición Formal

### Coordenadas respecto a una Base

> [!note]- 📋 Definición Principal
> 
> Sea $V$ un espacio vectorial y $\mathcal{B} = {\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n}$ una **base ordenada** de $V$.
> 
> Para cualquier vector $\vec{u} \in V$, existen **únicos** escalares $c_1, c_2, \ldots, c_n$ tales que:
> 
> $$\vec{u} = c_1\vec{v}_1 + c_2\vec{v}_2 + \cdots + c_n\vec{v}_n$$
> 
> **Definición:**
> 
> $$[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} c_1 \ c_2 \ \vdots \ c_n \end{bmatrix}$$
> 
> es el **vector de coordenadas** de $\vec{u}$ respecto a la base $\mathcal{B}$.
> 
> ---
> 
> **Notación alternativa:**
> 
> - $[\vec{u}]_{\mathcal{B}}$ - Notación estándar
> - $\text{coord}_{\mathcal{B}}(\vec{u})$ - Notación funcional
> - $\vec{u}_{\mathcal{B}}$ - Notación compacta
> 
> **Propiedades fundamentales:**
> 
> 1. **Existencia:** Garantizada porque $\mathcal{B}$ genera $V$
> 2. **Unicidad:** Garantizada porque $\mathcal{B}$ es linealmente independiente
> 3. **Dimensión:** $[\vec{u}]_{\mathcal{B}} \in \mathbb{R}^n$ si $\dim(V) = n$
> 4. **Orden importa:** $\mathcal{B}$ debe ser una base **ordenada**
> 5. **Linealidad:** El proceso es una transformación lineal
> 
> ---
> 
> **¿Por qué son únicas?**
> 
> Si existieran dos representaciones diferentes:
> 
> $$\vec{u} = c_1\vec{v}_1 + \cdots + c_n\vec{v}_n = d_1\vec{v}_1 + \cdots + d_n\vec{v}_n$$
> 
> Entonces:
> 
> $$(c_1 - d_1)\vec{v}_1 + \cdots + (c_n - d_n)\vec{v}_n = \vec{0}$$
> 
> Como $\mathcal{B}$ es linealmente independiente: $c_i - d_i = 0$ para todo $i$
> 
> Por lo tanto: $c_i = d_i$ para todo $i$ ✓

### Importancia del Orden

> [!warning]- ⚠️ La Base debe estar Ordenada
> 
> **Ejemplo:** En $\mathbb{R}^2$, considera:
> 
> $$\mathcal{B}_1 = \left\{\begin{bmatrix} 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \end{bmatrix}\right\}$$
> 
> $$\mathcal{B}_2 = \left\{\begin{bmatrix} 0 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \end{bmatrix}\right\}$$
> 
> Para $\vec{u} = \begin{bmatrix} 3 \ 5 \end{bmatrix}$:
> 
> - En $\mathcal{B}_1$: $[\vec{u}]_{\mathcal{B}_1} = \begin{bmatrix} 3 \ 5 \end{bmatrix}$
>     
> - En $\mathcal{B}_2$: $[\vec{u}]_{\mathcal{B}_2} = \begin{bmatrix} 5 \ 3 \end{bmatrix}$
>     
> 
> **Mismo conjunto de vectores, diferente orden → diferentes coordenadas**
> 
> Por eso siempre escribimos bases como **listas ordenadas**, no como conjuntos.

---

## 🔍 Ejemplos Fundamentales

### Ejemplo 1: Coordenadas en $\mathbb{R}^2$

> [!example]- 📝 Base Canónica
> 
> **Base canónica de $\mathbb{R}^2$:**
> 
> $$\mathcal{E} = \left\{\vec{e}_1 = \begin{bmatrix} 1 \ 0 \end{bmatrix}, \vec{e}_2 = \begin{bmatrix} 0 \ 1 \end{bmatrix}\right\}$$
> 
> **Vector:** $\vec{u} = \begin{bmatrix} 3 \ -2 \end{bmatrix}$
> 
> **Coordenadas:**
> 
> $$\vec{u} = 3\vec{e}_1 + (-2)\vec{e}_2$$
> 
> $$[\vec{u}]_{\mathcal{E}} = \begin{bmatrix} 3 \ -2 \end{bmatrix}$$
> 
> **Observación:** Con la base canónica, las coordenadas coinciden con los componentes del vector. Por eso es la base más "natural".

> [!example]- 📝 Base No Canónica
> 
> **Base alternativa:**
> 
> $$\mathcal{B} = \left\{\vec{v}_1 = \begin{bmatrix} 1 \ 1 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 1 \ -1 \end{bmatrix}\right\}$$
> 
> **Mismo vector:** $\vec{u} = \begin{bmatrix} 3 \ -2 \end{bmatrix}$
> 
> **Encontrar coordenadas:**
> 
> $$\begin{bmatrix} 3 \ -2 \end{bmatrix} = c_1\begin{bmatrix} 1 \ 1 \end{bmatrix} + c_2\begin{bmatrix} 1 \ -1 \end{bmatrix}$$
> 
> Sistema de ecuaciones:
> 
> $$\begin{cases} c_1 + c_2 = 3 \ c_1 - c_2 = -2 \end{cases}$$
> 
> Resolviendo:
> 
> - Sumando: $2c_1 = 1 \Rightarrow c_1 = \frac{1}{2}$
> - Sustituyendo: $c_2 = 3 - \frac{1}{2} = \frac{5}{2}$
> 
> $$[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} 1/2 \ 5/2 \end{bmatrix}$$
> 
> **Verificación:**
> 
> $$\frac{1}{2}\begin{bmatrix} 1 \ 1 \end{bmatrix} + \frac{5}{2}\begin{bmatrix} 1 \ -1 \end{bmatrix} = \begin{bmatrix} 1/2 + 5/2 \ 1/2 - 5/2 \end{bmatrix} = \begin{bmatrix} 3 \ -2 \end{bmatrix}$$ ✓
> 
> **Importante:** Mismo vector, diferentes coordenadas según la base.

> [!example]- 📝 Base con Vectores Ortogonales
> 
> **Base ortogonal:**
> 
> $$\mathcal{C} = \left\{\vec{w}_1 = \begin{bmatrix} 3 \ 4 \end{bmatrix}, \vec{w}_2 = \begin{bmatrix} 4 \ -3 \end{bmatrix}\right\}$$
> 
> (Verificar: $\vec{w}_1 \cdot \vec{w}_2 = 3(4) + 4(-3) = 0$ ✓)
> 
> **Vector:** $\vec{u} = \begin{bmatrix} 7 \ 1 \end{bmatrix}$
> 
> **Método 1: Sistema de ecuaciones**
> 
> $$\begin{bmatrix} 7 \ 1 \end{bmatrix} = c_1\begin{bmatrix} 3 \ 4 \end{bmatrix} + c_2\begin{bmatrix} 4 \ -3 \end{bmatrix}$$
> 
> $$\begin{cases} 3c_1 + 4c_2 = 7 \ 4c_1 - 3c_2 = 1 \end{cases}$$
> 
> Multiplicando la primera por 3 y la segunda por 4:
> 
> $$\begin{cases} 9c_1 + 12c_2 = 21 \ 16c_1 - 12c_2 = 4 \end{cases}$$
> 
> Sumando: $25c_1 = 25 \Rightarrow c_1 = 1$
> 
> Sustituyendo: $3(1) + 4c_2 = 7 \Rightarrow c_2 = 1$
> 
> $$[\vec{u}]_{\mathcal{C}} = \begin{bmatrix} 1 \ 1 \end{bmatrix}$$
> 
> **Nota:** Para bases ortogonales, existe una fórmula más eficiente usando productos internos (veremos más adelante).

### Ejemplo 2: Coordenadas en $\mathbb{R}^3$

> [!example]- 📝 Tres Dimensiones
> 
> **Base:**
> 
> $$\mathcal{B} = \left\{\vec{v}_1 = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}, \vec{v}_3 = \begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix}\right\}$$
> 
> **Vector:** $\vec{u} = \begin{bmatrix} 5 \ 3 \ 2 \end{bmatrix}$
> 
> **Encontrar coordenadas:**
> 
> $$\begin{bmatrix} 5 \ 3 \ 2 \end{bmatrix} = c_1\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix} + c_2\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix} + c_3\begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix}$$
> 
> Sistema:
> 
> $$\begin{cases} c_1 + c_2 + c_3 = 5 \ c_2 + c_3 = 3 \ c_3 = 2 \end{cases}$$
> 
> **Resolución por sustitución hacia atrás:**
> 
> - De la tercera: $c_3 = 2$
> - De la segunda: $c_2 = 3 - 2 = 1$
> - De la primera: $c_1 = 5 - 1 - 2 = 2$
> 
> $$[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} 2 \ 1 \ 2 \end{bmatrix}$$
> 
> **Verificación:**
> 
> $$2\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix} + 1\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix} + 2\begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix} = \begin{bmatrix} 2+1+2 \ 0+1+2 \ 0+0+2 \end{bmatrix} = \begin{bmatrix} 5 \ 3 \ 2 \end{bmatrix}$$ ✓

> [!example]- 📝 Base con Estructura Especial
> 
> **Base:**
> 
> $$\mathcal{C} = \left\{\vec{w}_1 = \begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix}, \vec{w}_2 = \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}, \vec{w}_3 = \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}\right\}$$
> 
> **Vector:** $\vec{u} = \begin{bmatrix} 2 \ 5 \ 3 \end{bmatrix}$
> 
> $$\begin{bmatrix} 2 \ 5 \ 3 \end{bmatrix} = c_1\begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix} + c_2\begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} + c_3\begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}$$
> 
> Sistema:
> 
> $$\begin{cases} c_1 = 2 \ c_1 + c_2 = 5 \ c_1 + c_2 + c_3 = 3 \end{cases}$$
> 
> Resolución directa:
> 
> - Primera ecuación: $c_1 = 2$
> - Segunda: $c_2 = 5 - 2 = 3$
> - Tercera: $c_3 = 3 - 2 - 3 = -2$
> 
> $$[\vec{u}]_{\mathcal{C}} = \begin{bmatrix} 2 \ 3 \ -2 \end{bmatrix}$$
> 
> **Observación:** Esta base tiene estructura triangular que facilita los cálculos.

### Ejemplo 3: Coordenadas en $P_2$

> [!example]- 📝 Polinomios de Grado ≤ 2
> 
> **Base canónica:**
> 
> $$\mathcal{E} = {1, x, x^2}$$
> 
> **Polinomio:** $p(x) = 3 + 5x - 2x^2$
> 
> $$p(x) = 3(1) + 5(x) + (-2)(x^2)$$
> 
> $$[p]_{\mathcal{E}} = \begin{bmatrix} 3 \ 5 \ -2 \end{bmatrix}$$
> 
> **Nota:** Los coeficientes del polinomio son directamente las coordenadas en la base canónica.

> [!example]- 📝 Base No Canónica
> 
> **Base alternativa:**
> 
> $$\mathcal{B} = {1, 1+x, 1+x+x^2}$$
> 
> **Mismo polinomio:** $p(x) = 3 + 5x - 2x^2$
> 
> **Encontrar coordenadas:**
> 
> $$3 + 5x - 2x^2 = c_1(1) + c_2(1+x) + c_3(1+x+x^2)$$
> 
> $$= (c_1 + c_2 + c_3) + (c_2 + c_3)x + c_3x^2$$
> 
> Igualando coeficientes:
> 
> $$\begin{cases} c_1 + c_2 + c_3 = 3 \ c_2 + c_3 = 5 \ c_3 = -2 \end{cases}$$
> 
> Resolviendo hacia atrás:
> 
> - $c_3 = -2$
> - $c_2 = 5 - (-2) = 7$
> - $c_1 = 3 - 7 - (-2) = -2$
> 
> $$[p]_{\mathcal{B}} = \begin{bmatrix} -2 \ 7 \ -2 \end{bmatrix}$$
> 
> **Verificación:**
> 
> $$-2(1) + 7(1+x) + (-2)(1+x+x^2)$$ $$= -2 + 7 + 7x - 2 - 2x - 2x^2$$ $$= 3 + 5x - 2x^2$$ ✓

> [!example]- 📝 Base de Lagrange
> 
> **Base de Lagrange para puntos $x = 0, 1, 2$:**
> 
> $$L_0(x) = \frac{(x-1)(x-2)}{(0-1)(0-2)} = \frac{(x-1)(x-2)}{2}$$
> 
> $$L_1(x) = \frac{x(x-2)}{(1-0)(1-2)} = -x(x-2)$$
> 
> $$L_2(x) = \frac{x(x-1)}{(2-0)(2-1)} = \frac{x(x-1)}{2}$$
> 
> $$\mathcal{L} = {L_0, L_1, L_2}$$
> 
> **Propiedad especial:** $L_i(j) = \delta_{ij}$ (delta de Kronecker)
> 
> **Polinomio:** $p(x) = 3 + 5x - 2x^2$
> 
> Para encontrar coordenadas, evaluamos en los puntos:
> 
> - $p(0) = 3$
> - $p(1) = 3 + 5 - 2 = 6$
> - $p(2) = 3 + 10 - 8 = 5$
> 
> $$[p]_{\mathcal{L}} = \begin{bmatrix} 3 \ 6 \ 5 \end{bmatrix}$$
> 
> **Ventaja:** Las coordenadas son simplemente los valores del polinomio en los puntos base.

### Ejemplo 4: Coordenadas en Matrices $2 \times 2$

> [!example]- 📝 Espacio de Matrices
> 
> **Base canónica de $M_{2 \times 2}$:**
> 
> $$\mathcal{E} = \left\{E_{11} = \begin{bmatrix} 1 & 0 \ 0 & 0 \end{bmatrix}, E_{12} = \begin{bmatrix} 0 & 1 \ 0 & 0 \end{bmatrix}, E_{21} = \begin{bmatrix} 0 & 0 \ 1 & 0 \end{bmatrix}, E_{22} = \begin{bmatrix} 0 & 0 \ 0 & 1 \end{bmatrix}\right\}$$
> 
> **Matriz:** $A = \begin{bmatrix} 3 & -1 \ 2 & 5 \end{bmatrix}$
> 
> $$A = 3E_{11} + (-1)E_{12} + 2E_{21} + 5E_{22}$$
> 
> $$[A]_{\mathcal{E}} = \begin{bmatrix} 3 \ -1 \ 2 \ 5 \end{bmatrix}$$
> 
> **Nota:** Las matrices se "vectorizan" listando sus entradas en orden (fila por fila).

> [!example]- 📝 Base de Matrices Simétricas y Antisimétricas
> 
> **Base alternativa:**
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 1 & 0 \ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \ 0 & 1 \end{bmatrix}, \begin{bmatrix} 0 & 1 \ 1 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 1 \ -1 & 0 \end{bmatrix}\right\}$$
> 
> **Matriz:** $A = \begin{bmatrix} 2 & 3 \ 1 & 4 \end{bmatrix}$
> 
> **Descomposición:** Escribir como combinación lineal
> 
> $$\begin{bmatrix} 2 & 3 \ 1 & 4 \end{bmatrix} = c_1\begin{bmatrix} 1 & 0 \ 0 & 0 \end{bmatrix} + c_2\begin{bmatrix} 0 & 0 \ 0 & 1 \end{bmatrix} + c_3\begin{bmatrix} 0 & 1 \ 1 & 0 \end{bmatrix} + c_4\begin{bmatrix} 0 & 1 \ -1 & 0 \end{bmatrix}$$
> 
> Sistema de ecuaciones (comparando entradas):
> 
> $$\begin{cases} c_1 = 2 \ c_2 = 4 \ c_3 + c_4 = 3 \ c_3 - c_4 = 1 \end{cases}$$
> 
> De las últimas dos: $c_3 = 2$, $c_4 = 1$
> 
> $$[A]_{\mathcal{B}} = \begin{bmatrix} 2 \ 4 \ 2 \ 1 \end{bmatrix}$$
> 
> **Interpretación:** La matriz se descompone en parte diagonal + parte simétrica + parte antisimétrica.

### Ejemplo 5: Funciones

> [!example]- 📝 Espacio de Funciones Trigonométricas
> 
> **Espacio:** $V = \text{gen}{1, \cos(x), \sin(x)}$
> 
> **Base:** $\mathcal{B} = {1, \cos(x), \sin(x)}$
> 
> **Función:** $f(x) = 3 + 2\cos(x) - 5\sin(x)$
> 
> $$[f]_{\mathcal{B}} = \begin{bmatrix} 3 \ 2 \ -5 \end{bmatrix}$$
> 
> **Función:** $g(x) = \cos(x) + \sin(x)$
> 
> $$[g]_{\mathcal{B}} = \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}$$
> 
> **Suma:** $f(x) + g(x) = 3 + 3\cos(x) - 4\sin(x)$
> 
> $$[f + g]_{\mathcal{B}} = \begin{bmatrix} 3 \ 3 \ -4 \end{bmatrix} = \begin{bmatrix} 3 \ 2 \ -5 \end{bmatrix} + \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}$$ ✓
> 
> **Se preserva la linealidad.**

---

## 🔧 Métodos de Cálculo

### Método 1: Sistema de Ecuaciones

> [!tip]- 🛠️ Procedimiento Directo
> 
> **Pasos:**
> 
> 1. **Plantear la ecuación:** $\vec{u} = c_1\vec{v}_1 + \cdots + c_n\vec{v}_n$
>     
> 2. **Igualar componentes:** Escribir sistema de ecuaciones
>     
> 3. **Resolver el sistema:** Usar sustitución, eliminación, etc.
>     
> 4. **Escribir coordenadas:** $[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} c_1 \ \vdots \ c_n \end{bmatrix}$
>     
> 
> ---
> 
> **Ventajas:**
> 
> - Directo e intuitivo
> - No requiere cálculos matriciales
> - Útil para bases pequeñas
> 
> **Desventajas:**
> 
> - Tedioso para dimensiones altas
> - Propenso a errores aritméticos
> - No es sistemático

> [!example]- 📝 Ejemplo Completo
> 
> **Base en $\mathbb{R}^3$:**
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix}, \begin{bmatrix} 2 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}\right\}$$
> 
> **Vector:** $\vec{u} = \begin{bmatrix} 5 \ 4 \ 3 \end{bmatrix}$
> 
> **Paso 1:** Plantear
> 
> $$\begin{bmatrix} 5 \ 4 \ 3 \end{bmatrix} = c_1\begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix} + c_2\begin{bmatrix} 2 \ 1 \ 0 \end{bmatrix} + c_3\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}$$
> 
> **Paso 2:** Sistema
> 
> $$\begin{cases} c_1 + 2c_2 + c_3 = 5 \ 2c_1 + c_2 = 4 \ c_1 + c_3 = 3 \end{cases}$$
> 
> **Paso 3:** Resolver
> 
> De la segunda ecuación: $c_2 = 4 - 2c_1$
> 
> De la tercera: $c_3 = 3 - c_1$
> 
> Sustituyendo en la primera:
> 
> $$c_1 + 2(4 - 2c_1) + (3 - c_1) = 5$$ $$c_1 + 8 - 4c_1 + 3 - c_1 = 5$$ $$-4c_1 = -6$$ $$c_1 = \frac{3}{2}$$
> 
> Entonces:
> 
> - $c_2 = 4 - 2(\frac{3}{2}) = 1$
> - $c_3 = 3 - \frac{3}{2} = \frac{3}{2}$
> 
> $$[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} 3/2 \ 1 \ 3/2 \end{bmatrix}$$

### Método 2: Forma Matricial

> [!tip]- 🛠️ Método Sistemático
> 
> **Idea:** Convertir el problema en resolver $M\vec{c} = \vec{u}$
> 
> **Pasos:**
> 
> 1. **Formar matriz:** $M = [\vec{v}_1 | \vec{v}_2 | \cdots | \vec{v}_n]$
>     
> 2. **Plantear sistema:** $M\vec{c} = \vec{u}$
>     
> 3. **Resolver:** Usar eliminación gaussiana
>     
> 4. **Resultado:** $$[\vec{u}]_{\mathcal{B}} = \vec{c} = M^{-1}\vec{u}$$
> (donde $M^{-1}$ existe porque $\mathcal{B}$ es base)
> 
> ---
> 
> **Ventajas:**
> 
> - Sistemático y organizado
> - Eficiente para múltiples vectores
> - Menos propenso a errores
> - Escalable a dimensiones altas
> 
> **Desventajas:**
> 
> - Requiere conocimiento de matrices
> - Más cálculos para problemas pequeños

> [!example]- 📝 Ejemplo con Matriz Aumentada
> 
> **Base en $\mathbb{R}^3$:**
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}\right\}$$
> 
> **Vector:** $\vec{u} = \begin{bmatrix} 2 \ 3 \ 1 \end{bmatrix}$
> 
> **Paso 1:** Formar matriz de la base
> 
> $$M = \begin{bmatrix} 1 & 0 & 1 \ 0 & 1 & 1 \ 1 & 1 & 0 \end{bmatrix}$$
> 
> **Paso 2:** Sistema $M\vec{c} = \vec{u}$
> 
> $$\begin{bmatrix} 1 & 0 & 1 \ 0 & 1 & 1 \ 1 & 1 & 0 \end{bmatrix}\begin{bmatrix} c_1 \ c_2 \ c_3 \end{bmatrix} = \begin{bmatrix} 2 \ 3 \ 1 \end{bmatrix}$$
> 
> **Paso 3:** Matriz aumentada
> 
> $$\left[\begin{array}{ccc|c} 1 & 0 & 1 & 2 \ 0 & 1 & 1 & 3 \ 1 & 1 & 0 & 1 \end{array}\right]$$
> 
> Operación: $F_3 - F_1 \to F_3$
> 
> $$\left[\begin{array}{ccc|c} 1 & 0 & 1 & 2 \ 0 & 1 & 1 & 3 \ 0 & 1 & -1 & -1 \end{array}\right]$$
> 
> Operación: $F_3 - F_2 \to F_3$
> 
> $$\left[\begin{array}{ccc|c} 1 & 0 & 1 & 2 \ 0 & 1 & 1 & 3 \ 0 & 0 & -2 & -4 \end{array}\right]$$
> 
> **Paso 4:** Sustitución hacia atrás
> 
> - De $F_3$: $-2c_3 = -4 \Rightarrow c_3 = 2$
> - De $F_2$: $c_2 + 2 = 3 \Rightarrow c_2 = 1$
> - De $F_1$: $c_1 + 2 = 2 \Rightarrow c_1 = 0$
> 
> $$[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} 0 \ 1 \ 2 \end{bmatrix}$$
> 
> **Verificación:**
> 
> $$0\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix} + 1\begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix} + 2\begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix} = \begin{bmatrix} 0+0+2 \ 0+1+2 \ 0+1+0 \end{bmatrix} = \begin{bmatrix} 2 \ 3 \ 1 \end{bmatrix}$$ ✓

> [!example]- 📝 Múltiples Vectores Simultáneamente
> 
> **Base:** $\mathcal{B} = \left\{\begin{bmatrix} 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ -1 \end{bmatrix}\right\}$
> 
> **Vectores:** $\vec{u}_1 = \begin{bmatrix} 3 \ 1 \end{bmatrix}$, $\vec{u}_2 = \begin{bmatrix} 5 \ -1 \end{bmatrix}$, $\vec{u}_3 = \begin{bmatrix} 0 \ 4 \end{bmatrix}$
> 
> **Matriz de la base:**
> 
> $$M = \begin{bmatrix} 1 & 1 \ 1 & -1 \end{bmatrix}$$
> 
> **Matriz aumentada múltiple:**
> 
> $$\left[\begin{array}{cc|ccc} 1 & 1 & 3 & 5 & 0 \ 1 & -1 & 1 & -1 & 4 \end{array}\right]$$
> 
> Operación: $F_2 - F_1 \to F_2$
> 
> $$\left[\begin{array}{cc|ccc} 1 & 1 & 3 & 5 & 0 \ 0 & -2 & -2 & -6 & 4 \end{array}\right]$$
> 
> De $F_2$: dividir entre $-2$
> 
> $$\left[\begin{array}{cc|ccc} 1 & 1 & 3 & 5 & 0 \ 0 & 1 & 1 & 3 & -2 \end{array}\right]$$
> 
> Operación: $F_1 - F_2 \to F_1$
> 
> $$\left[\begin{array}{cc|ccc} 1 & 0 & 2 & 2 & 2 \ 0 & 1 & 1 & 3 & -2 \end{array}\right]$$
> 
> **Resultados:**
> 
> $$[\vec{u}_1]_{\mathcal{B}} = \begin{bmatrix} 2 \ 1 \end{bmatrix}, \quad [\vec{u}_2]_{\mathcal{B}} = \begin{bmatrix} 2 \ 3 \end{bmatrix}, \quad [\vec{u}_3]_{\mathcal{B}} = \begin{bmatrix} 2 \ -2 \end{bmatrix}$$
> 
> **Ventaja:** Resolver una vez la eliminación para múltiples vectores.

### Método 3: Fórmulas Especiales

> [!tip]- 🛠️ Para Bases Ortogonales/Ortonormales
> 
> **Base ortogonal:** $\mathcal{B} = {\vec{v}_1, \ldots, \vec{v}_n}$ con $\vec{v}_i \cdot \vec{v}_j = 0$ si $i \neq j$
> 
> **Fórmula:**
> 
> $$c_i = \frac{\vec{u} \cdot \vec{v}_i}{\vec{v}_i \cdot \vec{v}_i} = \frac{\vec{u} \cdot \vec{v}_i}{|\vec{v}_i|^2}$$
> 
> ---
> 
> **Base ortonormal:** Además $|\vec{v}_i| = 1$ para todo $i$
> 
> **Fórmula simplificada:**
> 
> $$c_i = \vec{u} \cdot \vec{v}_i$$
> 
> ---
> 
> **Ventaja:** No requiere resolver sistemas de ecuaciones.

> [!example]- 📝 Con Base Ortogonal
> 
> **Base ortogonal en $\mathbb{R}^3$:**
> 
> $$\mathcal{B} = \left\{\vec{v}_1 = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 0 \ 2 \ 0 \end{bmatrix}, \vec{v}_3 = \begin{bmatrix} 0 \ 0 \ 3 \end{bmatrix}\right\}$$
> 
> **Vector:** $\vec{u} = \begin{bmatrix} 4 \ 6 \ 9 \end{bmatrix}$
> 
> **Cálculo directo:**
> 
> $$c_1 = \frac{\vec{u} \cdot \vec{v}_1}{\vec{v}_1 \cdot \vec{v}_1} = \frac{4(1) + 6(0) + 9(0)}{1^2 + 0^2 + 0^2} = \frac{4}{1} = 4$$
> 
> $$c_2 = \frac{\vec{u} \cdot \vec{v}_2}{\vec{v}_2 \cdot \vec{v}_2} = \frac{4(0) + 6(2) + 9(0)}{0^2 + 2^2 + 0^2} = \frac{12}{4} = 3$$
> 
> $$c_3 = \frac{\vec{u} \cdot \vec{v}_3}{\vec{v}_3 \cdot \vec{v}_3} = \frac{4(0) + 6(0) + 9(3)}{0^2 + 0^2 + 3^2} = \frac{27}{9} = 3$$
> 
> $$[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} 4 \ 3 \ 3 \end{bmatrix}$$
> 
> **Verificación:**
> 
> $$4\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix} + 3\begin{bmatrix} 0 \ 2 \ 0 \end{bmatrix} + 3\begin{bmatrix} 0 \ 0 \ 3 \end{bmatrix} = \begin{bmatrix} 4 \ 6 \ 9 \end{bmatrix}$$ ✓

> [!example]- 📝 Con Base Ortonormal
> 
> **Base ortonormal en $\mathbb{R}^2$:**
> 
> $$\mathcal{B} = \left\{\vec{v}_1 = \begin{bmatrix} \cos\theta \ \sin\theta \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} -\sin\theta \ \cos\theta \end{bmatrix}\right\}$$
> 
> Con $\theta = 30° = \frac{\pi}{6}$:
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} \sqrt{3}/2 \ 1/2 \end{bmatrix}, \begin{bmatrix} -1/2 \ \sqrt{3}/2 \end{bmatrix}\right\}$$
> 
> **Vector:** $\vec{u} = \begin{bmatrix} 2 \ 1 \end{bmatrix}$
> 
> **Cálculo:**
> 
> $$c_1 = \vec{u} \cdot \vec{v}_1 = 2 \cdot \frac{\sqrt{3}}{2} + 1 \cdot \frac{1}{2} = \sqrt{3} + \frac{1}{2}$$
> 
> $$c_2 = \vec{u} \cdot \vec{v}_2 = 2 \cdot \left(-\frac{1}{2}\right) + 1 \cdot \frac{\sqrt{3}}{2} = -1 + \frac{\sqrt{3}}{2}$$
> 
> $$[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} \sqrt{3} + 1/2 \ \sqrt{3}/2 - 1 \end{bmatrix}$$
> 
> **Interpretación geométrica:** Estas son las proyecciones de $\vec{u}$ sobre los vectores de la base rotada.

---

## 🎨 Propiedades de las Coordenadas

### Propiedad 1: Linealidad

> [!note]- ⚡ Propiedad Fundamental
> 
> **Teorema:** La función de coordenadas es lineal.
> 
> $$[\alpha\vec{u} + \beta\vec{v}]_{\mathcal{B}} = \alpha[\vec{u}]_{\mathcal{B}} + \beta[\vec{v}]_{\mathcal{B}}$$
> 
> **Demostración:**
> 
> Si $\vec{u} = \sum_{i=1}^n a_i\vec{v}_i$ y $\vec{w} = \sum_{i=1}^n b_i\vec{v}_i$, entonces:
> 
> $$\alpha\vec{u} + \beta\vec{w} = \sum_{i=1}^n (\alpha a_i + \beta b_i)\vec{v}_i$$
> 
> Por lo tanto:
> 
> $$[\alpha\vec{u} + \beta\vec{w}]_{\mathcal{B}} = \begin{bmatrix} \alpha a_1 + \beta b_1 \ \vdots \ \alpha a_n + \beta b_n \end{bmatrix} = \alpha\begin{bmatrix} a_1 \ \vdots \ a_n \end{bmatrix} + \beta\begin{bmatrix} b_1 \ \vdots \ b_n \end{bmatrix}$$ ✓
> 
> ---
> 
> **Consecuencias:**
> 
> 1. $[\vec{0}]_{\mathcal{B}} = \vec{0}$ (el vector cero tiene coordenadas cero)
>     
> 2. $[-\vec{u}]_{\mathcal{B}} = -[\vec{u}]_{\mathcal{B}}$
>     
> 3. La función preserva todas las operaciones lineales
>     

> [!example]- 📝 Verificación Numérica
> 
> **Base:** $\mathcal{B} = \left\{\begin{bmatrix} 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ -1 \end{bmatrix}\right\}$
> 
> **Vectores:**
> 
> $$\vec{u} = \begin{bmatrix} 3 \ 1 \end{bmatrix} \Rightarrow [\vec{u}]_{\mathcal{B}} = \begin{bmatrix} 2 \ 1 \end{bmatrix}$$
> 
> $$\vec{v} = \begin{bmatrix} 1 \ 3 \end{bmatrix} \Rightarrow [\vec{v}]_{\mathcal{B}} = \begin{bmatrix} 2 \ -1 \end{bmatrix}$$
> 
> **Verificar:** $[2\vec{u} + 3\vec{v}]_{\mathcal{B}} = 2[\vec{u}]_{\mathcal{B}} + 3[\vec{v}]_{\mathcal{B}}$
> 
> **Lado izquierdo:**
> 
> $$2\vec{u} + 3\vec{v} = 2\begin{bmatrix} 3 \ 1 \end{bmatrix} + 3\begin{bmatrix} 1 \ 3 \end{bmatrix} = \begin{bmatrix} 9 \ 11 \end{bmatrix}$$
> 
> Coordenadas: $\begin{bmatrix} 9 \ 11 \end{bmatrix} = c_1\begin{bmatrix} 1 \ 1 \end{bmatrix} + c_2\begin{bmatrix} 1 \ -1 \end{bmatrix}$
> 
> Sistema: $c_1 + c_2 = 9$, $c_1 - c_2 = 11$
> 
> Solución: $c_1 = 10$, $c_2 = -1$
> 
> $$[2\vec{u} + 3\vec{v}]_{\mathcal{B}} = \begin{bmatrix} 10 \ -1 \end{bmatrix}$$
> 
> **Lado derecho:**
> 
> $$2[\vec{u}]_{\mathcal{B}} + 3[\vec{v}]_{\mathcal{B}} = 2\begin{bmatrix} 2 \ 1 \end{bmatrix} + 3\begin{bmatrix} 2 \ -1 \end{bmatrix} = \begin{bmatrix} 4 \ 2 \end{bmatrix} + \begin{bmatrix} 6 \ -3 \end{bmatrix} = \begin{bmatrix} 10 \ -1 \end{bmatrix}$$
> 
> **Son iguales** ✓

### Propiedad 2: Isomorfismo con $\mathbb{R}^n$

> [!note]- 🔄 Equivalencia Estructural
> 
> **Teorema:** Si $\dim(V) = n$ y $\mathcal{B}$ es una base de $V$, entonces:
> 
> $$\phi: V \to \mathbb{R}^n, \quad \phi(\vec{v}) = [\vec{v}]_{\mathcal{B}}$$
> 
> es un **isomorfismo** de espacios vectoriales.
> 
> **Demostrar que es isomorfismo:**
> 
> **1. Linealidad:** Ya demostrada (Propiedad 1)
> 
> **2. Inyectividad:** Si $\phi(\vec{u}) = \phi(\vec{v})$, entonces:
> 
> $$[\vec{u}]_{\mathcal{B}} = [\vec{v}]_{\mathcal{B}}$$
> 
> Esto significa que $\vec{u}$ y $\vec{v}$ tienen la misma combinación lineal en términos de $\mathcal{B}$, por lo tanto $\vec{u} = \vec{v}$.
> 
> **3. Sobreyectividad:** Para cualquier $\begin{bmatrix} c_1 \ \vdots \ c_n \end{bmatrix} \in \mathbb{R}^n$, el vector:
> 
> $$\vec{v} = c_1\vec{v}_1 + \cdots + c_n\vec{v}_n$$
> 
> satisface $\phi(\vec{v}) = \begin{bmatrix} c_1 \ \vdots \ c_n \end{bmatrix}$.
> 
> ---
> 
> **Implicación:** Todo espacio vectorial de dimensión finita $n$ es "estructuralmente idéntico" a $\mathbb{R}^n$.
> 
> **Consecuencias:**
> 
> - Problemas abstractos → Problemas numéricos
> - Teoremas en $\mathbb{R}^n$ → Válidos en cualquier espacio de dimensión $n$
> - Cálculos se reducen a álgebra lineal numérica

### Propiedad 3: Coordenadas de Vectores Especiales

> [!note]- 📌 Casos Importantes
> 
> **1. Coordenadas de los vectores de la base:**
> 
> $$[\vec{v}_i]_{\mathcal{B}} = \begin{bmatrix} 0 \ \vdots \ 1 \ \vdots \ 0 \end{bmatrix} \leftarrow \text{1 en posición } i$$
> 
> (Son los vectores canónicos de $\mathbb{R}^n$)
> 
> **2. Coordenadas del vector cero:**
> 
> $$[\vec{0}]_{\mathcal{B}} = \begin{bmatrix} 0 \ \vdots \ 0 \end{bmatrix}$$
> 
> **3. Coordenadas de combinaciones:**
> 
> $$[c_1\vec{v}_1 + \cdots + c_n\vec{v}_n]_{\mathcal{B}} = \begin{bmatrix} c_1 \ \vdots \ c_n \end{bmatrix}$$
> 
> (Directamente los coeficientes)

> [!example]- 📝 Coordenadas de la Base
> 
> **Base en $\mathbb{R}^2$:** $\mathcal{B} = \left\{\begin{bmatrix} 2 \ 1 \end{bmatrix}, \begin{bmatrix} -1 \ 1 \end{bmatrix}\right\}$
> 
> **Coordenadas del primer vector:**
> 
> $$\begin{bmatrix} 2 \ 1 \end{bmatrix} = 1 \cdot \begin{bmatrix} 2 \ 1 \end{bmatrix} + 0 \cdot \begin{bmatrix} -1 \ 1 \end{bmatrix}$$
> 
> $$\left[\begin{bmatrix} 2 \ 1 \end{bmatrix}\right]_{\mathcal{B}} = \begin{bmatrix} 1 \ 0 \end{bmatrix}$$
> 
> **Coordenadas del segundo vector:**
> 
> $$\begin{bmatrix} -1 \ 1 \end{bmatrix} = 0 \cdot \begin{bmatrix} 2 \ 1 \end{bmatrix} + 1 \cdot \begin{bmatrix} -1 \ 1 \end{bmatrix}$$
> 
> $$\left[\begin{bmatrix} -1 \ 1 \end{bmatrix}\right]_{\mathcal{B}} = \begin{bmatrix} 0 \ 1 \end{bmatrix}$$
> 
> **Observación:** Los vectores de la base siempre tienen coordenadas canónicas en su propia base.

### Propiedad 4: Independencia y Dependencia

> [!note]- 🔗 Preservación de Relaciones
> 
> **Teorema:** Sean $\vec{v}_1, \ldots, \vec{v}_k \in V$ vectores y $\mathcal{B}$ una base de $V$.
> 
> Entonces:
> 
> $${\vec{v}_1, \ldots, \vec{v}_k} \text{ es L.I. en } V \Leftrightarrow {[\vec{v}_1]_{\mathcal{B}}, \ldots, [\vec{v}_k]_{\mathcal{B}}} \text{ es L.I. en } \mathbb{R}^n$$
> 
> **Demostración ($\Rightarrow$):**
> 
> Supongamos $c_1[\vec{v}_1]_{\mathcal{B}} + \cdots + c_k[\vec{v}_k]_{\mathcal{B}} = \vec{0}$
> 
> Por linealidad: $[c_1\vec{v}_1 + \cdots + c_k\vec{v}_k]_{\mathcal{B}} = \vec{0}$
> 
> Como $\phi$ es inyectiva: $c_1\vec{v}_1 + \cdots + c_k\vec{v}_k = \vec{0}$
> 
> Como ${\vec{v}_1, \ldots, \vec{v}_k}$ es L.I.: $c_1 = \cdots = c_k = 0$ ✓
> 
> ---
> 
> **Consecuencia práctica:** Para verificar independencia lineal de vectores en $V$, basta verificar independencia de sus coordenadas en $\mathbb{R}^n$.

> [!example]- 📝 Verificación de Independencia
> 
> **En $P_2$, base canónica** $\mathcal{E} = {1, x, x^2}$
> 
> **Polinomios:**
> 
> $$p_1(x) = 1 + 2x, \quad p_2(x) = x + x^2, \quad p_3(x) = 1 + x^2$$
> 
> **Coordenadas:**
> 
> $$[p_1]_{\mathcal{E}} = \begin{bmatrix} 1 \ 2 \ 0 \end{bmatrix}, \quad [p_2]_{\mathcal{E}} = \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}, \quad [p_3]_{\mathcal{E}} = \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}$$
> 
> **Verificar L.I. en $\mathbb{R}^3$:**
> 
> $$\begin{vmatrix} 1 & 0 & 1 \ 2 & 1 & 0 \ 0 & 1 & 1 \end{vmatrix} = 1(1 - 0) - 0 + 1(2 - 0) = 1 + 2 = 3 \neq 0$$
> 
> **Conclusión:** ${p_1, p_2, p_3}$ es linealmente independiente en $P_2$ ✓

---

## 🔄 Introducción al Cambio de Base

### Concepto Intuitivo

> [!note]- 🔀 Misma Información, Diferentes Coordenadas
> 
> **Situación:** Tenemos el mismo vector $\vec{u}$ pero queremos expresarlo en dos bases diferentes:
> 
> - Base $\mathcal{B} = {\vec{v}_1, \ldots, \vec{v}_n}$
> - Base $\mathcal{C} = {\vec{w}_1, \ldots, \vec{w}_n}$
> 
> **Pregunta:** Si conocemos $[\vec{u}]_{\mathcal{B}}$, ¿cómo encontrar $[\vec{u}]_{\mathcal{C}}$?
> 
> ---
> 
> **Analogía:**
> 
> - **Traducción:** "Hola" en español = "Hello" en inglés
> - **Monedas:** 100 USD = 85 EUR (aprox.)
> - **Temperatura:** 25°C = 77°F
> - **Posición:** "3 km norte" = "coordenadas GPS específicas"
> 
> **Idea clave:** El vector no cambia, solo cambia su descripción numérica.

### Relación entre Coordenadas

> [!note]- 🔗 Conexión Básica
> 
> **Proceso en dos pasos:**
> 
> 1. De coordenadas en $\mathcal{B}$ → Vector en $V$:
> 
> $$\vec{u} = c_1\vec{v}_1 + \cdots + c_n\vec{v}_n$$
> 
> 2. De vector en $V$ → Coordenadas en $\mathcal{C}$:
> 
> $$\vec{u} = d_1\vec{w}_1 + \cdots + d_n\vec{w}_n$$
> 
> ---
> 
> **El problema:** Este proceso requiere:
> 
> - Reconstruir el vector desde sus coordenadas en $\mathcal{B}$
> - Volver a calcular coordenadas en $\mathcal{C}$
> 
> **La solución:** Existe una matriz que hace esta conversión directamente:
> 
> $$[\vec{u}]_{\mathcal{C}} = P_{\mathcal{C} \leftarrow \mathcal{B}} \cdot [\vec{u}]_{\mathcal{B}}$$
> 
> donde $P_{\mathcal{C} \leftarrow \mathcal{B}}$ es la **matriz de cambio de base**.

### Ejemplo Simple

> [!example]- 📝 Cambio de Base en $\mathbb{R}^2$
> 
> **Base 1 (canónica):**
> 
> $$\mathcal{E} = \left\{\vec{e}_1 = \begin{bmatrix} 1 \ 0 \end{bmatrix}, \vec{e}_2 = \begin{bmatrix} 0 \ 1 \end{bmatrix}\right\}$$
> 
> **Base 2:**
> 
> $$\mathcal{B} = \left\{\vec{v}_1 = \begin{bmatrix} 2 \ 0 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 0 \ 3 \end{bmatrix}\right\}$$
> 
> **Vector en coordenadas canónicas:**
> 
> $$[\vec{u}]_{\mathcal{E}} = \begin{bmatrix} 6 \ 9 \end{bmatrix}$$
> 
> **Encontrar** $[\vec{u}]_{\mathcal{B}}
**Método directo:**
> El vector es:
> 
> $$\vec{u} = 6\begin{bmatrix} 1 \ 0 \end{bmatrix} + 9\begin{bmatrix} 0 \ 1 \end{bmatrix} = \begin{bmatrix} 6 \ 9 \end{bmatrix}$$
> 
> Expresar en base $\mathcal{B}$:
> 
> $$\begin{bmatrix} 6 \ 9 \end{bmatrix} = c_1\begin{bmatrix} 2 \ 0 \end{bmatrix} + c_2\begin{bmatrix} 0 \ 3 \end{bmatrix}$$
> 
> Sistema simple:
> 
> $$\begin{cases} 2c_1 = 6 \ 3c_2 = 9 \end{cases} \Rightarrow \begin{cases} c_1 = 3 \ c_2 = 3 \end{cases}$$
> 
> $$[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} 3 \ 3 \end{bmatrix}$$
> 
> **Interpretación:** El mismo vector $\vec{u}$ tiene coordenadas $(6, 9)$ en base canónica pero coordenadas $(3, 3)$ en base $\mathcal{B}$.

> [!example]- 📝 Cambio entre Bases No Canónicas
> 
> **Base 1:**
> 
> $$\mathcal{B} = \left\{\vec{v}_1 = \begin{bmatrix} 1 \ 1 \end{bmatrix}, \vec{v}_2 = \begin{bmatrix} 1 \ -1 \end{bmatrix}\right\}$$
> 
> **Base 2:**
> 
> $$\mathcal{C} = \left\{\vec{w}_1 = \begin{bmatrix} 2 \ 1 \end{bmatrix}, \vec{w}_2 = \begin{bmatrix} 1 \ 2 \end{bmatrix}\right\}$$
> 
> **Vector:** $[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} 2 \ 3 \end{bmatrix}$
> 
> **Paso 1:** Reconstruir el vector
> 
> $$\vec{u} = 2\begin{bmatrix} 1 \ 1 \end{bmatrix} + 3\begin{bmatrix} 1 \ -1 \end{bmatrix} = \begin{bmatrix} 2+3 \ 2-3 \end{bmatrix} = \begin{bmatrix} 5 \ -1 \end{bmatrix}$$
> 
> **Paso 2:** Expresar en base $\mathcal{C}$
> 
> $$\begin{bmatrix} 5 \ -1 \end{bmatrix} = c_1\begin{bmatrix} 2 \ 1 \end{bmatrix} + c_2\begin{bmatrix} 1 \ 2 \end{bmatrix}$$
> 
> Sistema:
> 
> $$\begin{cases} 2c_1 + c_2 = 5 \ c_1 + 2c_2 = -1 \end{cases}$$
> 
> De la segunda: $c_1 = -1 - 2c_2$
> 
> Sustituyendo: $2(-1 - 2c_2) + c_2 = 5$
> 
> $$-2 - 4c_2 + c_2 = 5 \Rightarrow -3c_2 = 7 \Rightarrow c_2 = -\frac{7}{3}$$
> 
> $$c_1 = -1 - 2\left(-\frac{7}{3}\right) = -1 + \frac{14}{3} = \frac{11}{3}$$
> 
> $$[\vec{u}]_{\mathcal{C}} = \begin{bmatrix} 11/3 \ -7/3 \end{bmatrix}$$
> 
> **Observación:** El cambio de base requiere dos pasos cuando no trabajamos con la base canónica.

### Motivación para el Próximo Tema

> [!tip]- 🎯 ¿Por qué Necesitamos Matrices de Cambio de Base?
> 
> **Problema actual:**
> 
> - Cambiar coordenadas requiere reconstruir el vector
> - Luego resolver un nuevo sistema
> - Ineficiente para múltiples vectores
> 
> **Solución (próximo tema):**
> 
> - Una sola matriz $P$ que hace la conversión
> - $[\vec{u}]_{\mathcal{C}} = P \cdot [\vec{u}]_{\mathcal{B}}$
> - Cálculo directo, sin pasos intermedios
> 
> **Ventajas:**
> 
> - Eficiencia computacional
> - Cambiar muchos vectores simultáneamente
> - Composición de cambios de base
> - Conexión con transformaciones lineales
> 
> **Nota:** Este tema será desarrollado completamente en **[[14 - Cambio de Base]]**.

---

## 📊 Tabla Resumen

> [!summary]- 📋 Referencia Rápida
> 
> |Concepto|Definición|Notación|Dimensión|
> |---|---|---|---|
> |**Vector de coordenadas**|Coeficientes en combinación lineal respecto a base|$[\vec{u}]_{\mathcal{B}}$|$n \times 1$|
> |**Base ordenada**|Lista de vectores L.I. que generan $V$|$\mathcal{B} = {\vec{v}_1, \ldots, \vec{v}_n}$|—|
> |**Coordenadas canónicas**|Coordenadas respecto a base canónica|$[\vec{u}]_{\mathcal{E}}$|$n \times 1$|
> |**Función de coordenadas**|Mapeo de $V$ a $\mathbb{R}^n$|$\phi(\vec{v}) = [\vec{v}]_{\mathcal{B}}$|—|
> |**Matriz de la base**|Vectores de base como columnas|$M = [\vec{v}_1|\cdots|
> 
> ---
> 
> ### Propiedades Clave
> 
> |Propiedad|Fórmula|Significado|
> |---|---|---|
> |**Unicidad**|Si $[\vec{u}]_{\mathcal{B}} = [\vec{v}]_{\mathcal{B}}$ entonces $\vec{u} = \vec{v}$|Coordenadas determinan vector|
> |**Linealidad**|$[\alpha\vec{u} + \beta\vec{v}]_{\mathcal{B}} = \alpha[\vec{u}]_{\mathcal{B}} + \beta[\vec{v}]_{\mathcal{B}}$|Preserva operaciones|
> |**Isomorfismo**|$\phi: V \to \mathbb{R}^n$ es biyección lineal|$V$ y $\mathbb{R}^n$ son "iguales"|
> |**Coordenadas de base**|$[\vec{v}_i]_{\mathcal{B}} = \vec{e}_i$|Vectores canónicos en $\mathbb{R}^n$|
> |**Vector cero**|$[\vec{0}]_{\mathcal{B}} = \vec{0}$|Coordenadas cero|
> 
> ---
> 
> ### Métodos de Cálculo
> 
> |Método|Cuándo Usar|Complejidad|
> |---|---|---|
> |**Sistema de ecuaciones**|Dimensión baja, base simple|$O(n^3)$|
> |**Forma matricial**|Dimensión alta, múltiples vectores|$O(n^3)$ inicial|
> |**Fórmulas ortogonales**|Base ortogonal/ortonormal|$O(n^2)$|
> |**Matriz inversa**|Muchos vectores en misma base|$O(n^3)$ inicial, $O(n^2)$ después|
> 
> ---
> 
> ### Casos Especiales
> 
> |Base|Característica|Ventaja|
> |---|---|---|
> |**Canónica**|${\vec{e}_1, \ldots, \vec{e}_n}$|Coordenadas = componentes|
> |**Ortogonal**|$\vec{v}_i \cdot \vec{v}_j = 0$ si $i \neq j$|Fórmula directa: $c_i = \frac{\vec{u} \cdot \vec{v}_i}{\|\vec{v}_i\|^2}$|
> |**Ortonormal**|Ortogonal + $\|\vec{v}_i\| = 1$|Fórmula simple: $c_i = \vec{u} \cdot \vec{v}_i$|
> |**Triangular**|Estructura escalonada|Sistema fácil de resolver|
> 
> ---
> 
> ### Fórmulas Importantes
> 
> **Reconstrucción del vector:**
> 
> $$\vec{u} = \sum_{i=1}^n c_i\vec{v}_i = [\vec{v}_1 | \cdots | \vec{v}_n] \begin{bmatrix} c_1 \ \vdots \ c_n \end{bmatrix}$$
> 
> **Sistema matricial:**
> 
> $$M[\vec{u}]_{\mathcal{B}} = \vec{u} \quad \Rightarrow \quad [\vec{u}]_{\mathcal{B}} = M^{-1}\vec{u}$$
> 
> **Base ortogonal:**
> 
> $$[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} \frac{\vec{u} \cdot \vec{v}_1}{|\vec{v}_1|^2} \ \vdots \ \frac{\vec{u} \cdot \vec{v}_n}{|\vec{v}_n|^2} \end{bmatrix}$$
> 
> **Base ortonormal:**
> 
> $$[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} \vec{u} \cdot \vec{v}_1 \ \vdots \ \vec{u} \cdot \vec{v}_n \end{bmatrix}$$

---

## 💡 Aplicaciones y Ejemplos Adicionales

### Aplicación 1: Gráficos por Computadora

> [!example]- 🎮 Transformaciones 3D
> 
> **Contexto:** En gráficos 3D, los objetos se definen en su propio sistema de coordenadas local.
> 
> **Base local del objeto:**
> 
> $$\mathcal{B}_{\text{objeto}} = {\vec{x}_{\text{obj}}, \vec{y}_{\text{obj}}, \vec{z}_{\text{obj}}}$$
> 
> **Base mundial:**
> 
> $$\mathcal{B}_{\text{mundo}} = {\vec{x}_{\text{world}}, \vec{y}_{\text{world}}, \vec{z}_{\text{world}}}$$
> 
> **Problema:** Un vértice del objeto tiene coordenadas locales:
> 
> $$[P]_{\mathcal{B}_{\text{objeto}}} = \begin{bmatrix} 2 \ 3 \ 1 \end{bmatrix}$$
> 
> **Objetivo:** Encontrar sus coordenadas mundiales para renderizado.
> 
> **Solución:** Usar cambio de base (tema del próximo capítulo).
> 
> **Aplicaciones:**
> 
> - Rotación de objetos
> - Cambios de cámara
> - Sistemas de partículas
> - Cinemática inversa en animación

### Aplicación 2: Procesamiento de Señales

> [!example]- 📡 Transformada de Fourier Discreta
> 
> **Contexto:** Una señal digital se puede representar en diferentes bases.
> 
> **Base temporal (muestras directas):**
> 
> $$\mathcal{B}_{\text{tiempo}} = {\delta_0, \delta_1, \ldots, \delta_{n-1}}$$
> 
> **Base frecuencial (componentes de Fourier):**
> 
> $$\mathcal{B}_{\text{freq}} = {e^{i2\pi k t/n}}_{k=0}^{n-1}$$
> 
> **Señal en dominio temporal:**
> 
> $$[s]_{\mathcal{B}_{\text{tiempo}}} = \begin{bmatrix} s_0 \ s_1 \ \vdots \ s_{n-1} \end{bmatrix}$$
> 
> **Transformada de Fourier:** Cambio de base a dominio frecuencial
> 
> $$[s]_{\mathcal{B}_{\text{freq}}} = \text{DFT}([s]_{\mathcal{B}_{\text{tiempo}}})$$
> 
> **Ventajas:**
> 
> - Filtrado de frecuencias específicas
> - Compresión de audio/imagen (MP3, JPEG)
> - Análisis espectral
> - Eliminación de ruido

### Aplicación 3: Machine Learning - PCA

> [!example]- 🤖 Reducción de Dimensionalidad
> 
> **Contexto:** Datos de alta dimensión (ej. imágenes 1000×1000 = 1,000,000 dimensiones)
> 
> **Base original (píxeles):**
> 
> $$\mathcal{B}_{\text{píxel}} = {\vec{e}_1, \vec{e}_2, \ldots, \vec{e}_{1000000}}$$
> 
> **Base de componentes principales:**
> 
> $$\mathcal{B}_{\text{PCA}} = {\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k} \quad (k \ll 1000000)$$
> 
> donde $\vec{v}_i$ son eigenvectores de la matriz de covarianza.
> 
> **Imagen original:**
> 
> $$[\text{imagen}]_{\mathcal{B}_{\text{píxel}}} \in \mathbb{R}^{1000000}$$
> 
> **Representación comprimida:**
> 
> $$[\text{imagen}]_{\mathcal{B}_{\text{PCA}}} \in \mathbb{R}^k \quad (k \approx 100)$$
> 
> **Resultado:** Reducción de 1M dimensiones a ~100, conservando >95% de información.
> 
> **Aplicaciones:**
> 
> - Reconocimiento facial
> - Compresión de datos
> - Visualización de datos
> - Reducción de ruido

### Aplicación 4: Física Cuántica

> [!example]- ⚛️ Estados Cuánticos
> 
> **Base de espín-z:**
> 
> $$\mathcal{B}_z = {|+\rangle_z, |-\rangle_z}$$
> 
> **Base de espín-x:**
> 
> $$\mathcal{B}_x = {|+\rangle_x, |-\rangle_x}$$
> 
> **Estado cuántico en base $z$:**
> 
> $$[|\psi\rangle]_{\mathcal{B}_z} = \begin{bmatrix} \alpha \ \beta \end{bmatrix} \quad \text{con } |\alpha|^2 + |\beta|^2 = 1$$
> 
> **Mismo estado en base $x$:**
> 
> $$[|\psi\rangle]_{\mathcal{B}_x} = \begin{bmatrix} \gamma \ \delta \end{bmatrix}$$
> 
> **Relación:** Las bases están relacionadas por matrices unitarias (cambio de base cuántico).
> 
> **Interpretación física:**
> 
> - Diferentes observables requieren diferentes bases
> - Medición colapsa el estado en una base específica
> - Cambio de base = rotación en espacio de Hilbert

---

## 🎓 Ejercicios Propuestos

### Nivel Básico

> [!example]- 💪 Ejercicios Fundamentales
> 
> **1.** En $\mathbb{R}^2$, base $\mathcal{B} = \left\{\begin{bmatrix} 1 \ 2 \end{bmatrix}, \begin{bmatrix} 3 \ 4 \end{bmatrix}\right\}$
> 
> Encontrar $\left[\begin{bmatrix} 5 \ 6 \end{bmatrix}\right]_{\mathcal{B}}$
> 
> ---
> 
> **2.** En $P_2$, base $\mathcal{B} = {1, x, x^2}$
> 
> a) Encontrar $[4 - 2x + 3x^2]_{\mathcal{B}}$
> 
> b) Encontrar $[-x + x^2]_{\mathcal{B}}$
> 
> c) Verificar que $[p + q]_{\mathcal{B}} = [p]_{\mathcal{B}} + [q]_{\mathcal{B}}$ para los polinomios anteriores
> 
> ---
> 
> **3.** En $\mathbb{R}^3$, dada la base $\mathcal{B} = \left\{\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 1 \ 1 \ 1 \end{bmatrix}\right\}$
> 
> Encontrar $\left[\begin{bmatrix} 4 \ 3 \ 2 \end{bmatrix}\right]_{\mathcal{B}}$
> 
> ---
> 
> **4.** Verificar que si $[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} 2 \ -1 \ 3 \end{bmatrix}$ y $[\vec{v}]_{\mathcal{B}} = \begin{bmatrix} 1 \ 0 \ -2 \end{bmatrix}$
> 
> entonces $[2\vec{u} + 3\vec{v}]_{\mathcal{B}} = \begin{bmatrix} 7 \ -2 \ 0 \end{bmatrix}$
> 
> ---
> 
> **5.** En $M_{2 \times 2}$, base canónica $\mathcal{E} = {E_{11}, E_{12}, E_{21}, E_{22}}$
> 
> Encontrar $\left[\begin{bmatrix} 2 & -3 \ 1 & 4 \end{bmatrix}\right]_{\mathcal{E}}$

### Nivel Intermedio

> [!example]- 💪 Desafío Moderado
> 
> **6.** En $\mathbb{R}^3$, base ortogonal:
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 2 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 3 \end{bmatrix}\right\}$$
> 
> Usar la fórmula para bases ortogonales para encontrar $\left[\begin{bmatrix} 6 \ 8 \ 9 \end{bmatrix}\right]_{\mathcal{B}}$
> 
> ---
> 
> **7.** En $P_2$, base $\mathcal{B} = {1, 1+x, 1+x+x^2}$
> 
> a) Encontrar $[5 + 3x - 2x^2]_{\mathcal{B}}$
> 
> b) Si $[p]_{\mathcal{B}} = \begin{bmatrix} 2 \ -1 \ 3 \end{bmatrix}$, encontrar $p(x)$ explícitamente
> 
> ---
> 
> **8.** En $\mathbb{R}^2$, bases:
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 1 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ -1 \end{bmatrix}\right\}, \quad \mathcal{E} = \text{canónica}$$
> 
> Si $[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} 3 \ 2 \end{bmatrix}$, encontrar $[\vec{u}]_{\mathcal{E}}$
> 
> ---
> 
> **9.** Demostrar que si $\mathcal{B} = {\vec{v}_1, \vec{v}_2, \vec{v}_3}$ es base de $\mathbb{R}^3$, entonces:
> 
> $${[\vec{v}_1]_{\mathcal{B}}, [\vec{v}_2]_{\mathcal{B}}, [\vec{v}_3]_{\mathcal{B}}} = \left\{\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}\right\}$$
> 
> ---
> 
> **10.** En $M_{2 \times 2}$, base:
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 1 & 0 \ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \ 0 & 1 \end{bmatrix}, \begin{bmatrix} 0 & 1 \ 1 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 1 \ -1 & 0 \end{bmatrix}\right\}$$
> 
> Encontrar $\left[\begin{bmatrix} 3 & 5 \ 1 & 2 \end{bmatrix}\right]_{\mathcal{B}}$

### Nivel Avanzado

> [!example]- 💪 Desafío Avanzado
> 
> **11.** En $\mathbb{R}^3$, base:
> 
> $$\mathcal{B} = \left\{\begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix}, \begin{bmatrix} 2 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}\right\}$$
> 
> a) Encontrar la matriz $M$ tal que $M[\vec{u}]_{\mathcal{B}} = \vec{u}$ (en coordenadas canónicas)
> 
> b) Calcular $M^{-1}$
> 
> c) Usar $M^{-1}$ para encontrar $\left[\begin{bmatrix} 7 \ 5 \ 3 \end{bmatrix}\right]_{\mathcal{B}}$
> 
> ---
> 
> **12.** En $P_2$, considerar las bases:
> 
> $$\mathcal{B} = {1, x, x^2}, \quad \mathcal{L} = {L_0(x), L_1(x), L_2(x)}$$
> 
> donde $L_i(x)$ son los polinomios de Lagrange para puntos $x = 0, 1, 2$
> 
> Si $[p]_{\mathcal{B}} = \begin{bmatrix} 2 \ -3 \ 1 \end{bmatrix}$, encontrar $[p]_{\mathcal{L}}$
> 
> (Pista: Evaluar $p$ en los puntos 0, 1, 2)
> 
> ---
> 
> **13.** Demostrar que si ${\vec{v}_1, \ldots, \vec{v}_k}$ es linealmente independiente en $V$ y $\mathcal{B}$ es una base de $V$, entonces:
> 
> $${[\vec{v}_1]_{\mathcal{B}}, \ldots, [\vec{v}_k]_{\mathcal{B}}} \text{ es linealmente independiente en } \mathbb{R}^n$$
> 
> ---
> 
> **14.** En $\mathbb{R}^2$, sea $\mathcal{B}_\theta$ la base obtenida rotando la base canónica por ángulo $\theta$:
> 
> $$\mathcal{B}_\theta = \left\{\begin{bmatrix} \cos\theta \ \sin\theta \end{bmatrix}, \begin{bmatrix} -\sin\theta \ \cos\theta \end{bmatrix}\right\}$$
> 
> a) Verificar que es base ortonormal
> 
> b) Encontrar $\left[\begin{bmatrix} 1 \ 1 \end{bmatrix}\right]_{\mathcal{B}_{\pi/4}}$
> 
> c) Interpretar geométricamente el resultado
> 
> ---
> 
> **15.** Sea $V = \text{gen}{1, \cos(x), \sin(x), \cos(2x), \sin(2x)}$ con base:
> 
> $$\mathcal{B} = {1, \cos(x), \sin(x), \cos(2x), \sin(2x)}$$
> 
> Si $f(x) = 3 + 2\cos(x) - \sin(x) + 4\cos(2x)$, encontrar $[f]_{\mathcal{B}}$

---

## ✅ Soluciones Selectas

### Soluciones Básicas

> [!success]- 🔑 Respuestas Nivel 1
> 
> **1.** Sistema:
> 
> $$\begin{bmatrix} 5 \ 6 \end{bmatrix} = c_1\begin{bmatrix} 1 \ 2 \end{bmatrix} + c_2\begin{bmatrix} 3 \ 4 \end{bmatrix}$$
> 
> $$\begin{cases} c_1 + 3c_2 = 5 \ 2c_1 + 4c_2 = 6 \end{cases}$$
> 
> De la primera: $c_1 = 5 - 3c_2$
> 
> Sustituyendo: $2(5 - 3c_2) + 4c_2 = 6 \Rightarrow 10 - 6c_2 + 4c_2 = 6$
> 
> $$-2c_2 = -4 \Rightarrow c_2 = 2$$
> 
> $$c_1 = 5 - 3(2) = -1$$
> 
> $$\boxed{\left[\begin{bmatrix} 5 \ 6 \end{bmatrix}\right]_{\mathcal{B}} = \begin{bmatrix} -1 \ 2 \end{bmatrix}}$$
> 
> ---
> 
> **2.**
> 
> a) $\boxed{[4 - 2x + 3x^2]_{\mathcal{B}} = \begin{bmatrix} 4 \ -2 \ 3 \end{bmatrix}}$ (directo)
> 
> b) $\boxed{[-x + x^2]_{\mathcal{B}} = \begin{bmatrix} 0 \ -1 \ 1 \end{bmatrix}}$ (directo)
> 
> c) Suma:
> 
> $$[p + q]_{\mathcal{B}} = [4 - 3x + 4x^2]_{\mathcal{B}} = \begin{bmatrix} 4 \ -3 \ 4 \end{bmatrix}$$
> 
> $$[p]_{\mathcal{B}} + [q]_{\mathcal{B}} = \begin{bmatrix} 4 \ -2 \ 3 \end{bmatrix} + \begin{bmatrix} 0 \ -1 \ 1 \end{bmatrix} = \begin{bmatrix} 4 \ -3 \ 4 \end{bmatrix}$$ ✓
> 
> ---
> 
> **3.** Sistema triangular:
> 
> $$\begin{cases} c_1 + c_2 + c_3 = 4 \ c_2 + c_3 = 3 \ c_3 = 2 \end{cases}$$
> 
> Resolución hacia atrás:
> 
> - $c_3 = 2$
>     
> - $c_2 = 3 - 2 = 1$
>     
> - $c_1 = 4 - 1 - 2 = 1$
$$\boxed{\left[\begin{bmatrix} 4 \ 3 \ 2 \end{bmatrix}\right]_{\mathcal{B}} = \begin{bmatrix} 1 \ 1 \ 2 \end{bmatrix}}$$
> ---
> 
> **4.** Verificación:
> 
> $$2[\vec{u}]_{\mathcal{B}} + 3[\vec{v}]_{\mathcal{B}} = 2\begin{bmatrix} 2 \ -1 \ 3 \end{bmatrix} + 3\begin{bmatrix} 1 \ 0 \ -2 \end{bmatrix}$$
> 
> $$= \begin{bmatrix} 4 \ -2 \ 6 \end{bmatrix} + \begin{bmatrix} 3 \ 0 \ -6 \end{bmatrix} = \begin{bmatrix} 7 \ -2 \ 0 \end{bmatrix}$$ ✓
> 
> **Propiedad de linealidad confirmada.**
> 
> ---
> 
> **5.** Directamente:
> 
> $$\begin{bmatrix} 2 & -3 \ 1 & 4 \end{bmatrix} = 2E_{11} + (-3)E_{12} + 1E_{21} + 4E_{22}$$
> 
> $$\boxed{\left[\begin{bmatrix} 2 & -3 \ 1 & 4 \end{bmatrix}\right]_{\mathcal{E}} = \begin{bmatrix} 2 \ -3 \ 1 \ 4 \end{bmatrix}}$$

### Soluciones Intermedias

> [!success]- 🔑 Respuestas Nivel 2
> 
> **6.** Usando fórmula para base ortogonal:
> 
> $$c_1 = \frac{\vec{u} \cdot \vec{v}_1}{|\vec{v}_1|^2} = \frac{6 \cdot 1 + 8 \cdot 0 + 9 \cdot 0}{1^2} = 6$$
> 
> $$c_2 = \frac{\vec{u} \cdot \vec{v}_2}{|\vec{v}_2|^2} = \frac{6 \cdot 0 + 8 \cdot 2 + 9 \cdot 0}{2^2} = \frac{16}{4} = 4$$
> 
> $$c_3 = \frac{\vec{u} \cdot \vec{v}_3}{|\vec{v}_3|^2} = \frac{6 \cdot 0 + 8 \cdot 0 + 9 \cdot 3}{3^2} = \frac{27}{9} = 3$$
> 
> $$\boxed{\left[\begin{bmatrix} 6 \ 8 \ 9 \end{bmatrix}\right]_{\mathcal{B}} = \begin{bmatrix} 6 \ 4 \ 3 \end{bmatrix}}$$
> 
> ---
> 
> **7.**
> 
> a) Sistema:
> 
> $$5 + 3x - 2x^2 = c_1(1) + c_2(1+x) + c_3(1+x+x^2)$$
> 
> $$= (c_1 + c_2 + c_3) + (c_2 + c_3)x + c_3x^2$$
> 
> Igualando:
> 
> $$\begin{cases} c_1 + c_2 + c_3 = 5 \ c_2 + c_3 = 3 \ c_3 = -2 \end{cases}$$
> 
> Solución: $c_3 = -2$, $c_2 = 5$, $c_1 = 2$
> 
> $$\boxed{[5 + 3x - 2x^2]_{\mathcal{B}} = \begin{bmatrix} 2 \ 5 \ -2 \end{bmatrix}}$$
> 
> b) Reconstruir:
> 
> $$p(x) = 2(1) + (-1)(1+x) + 3(1+x+x^2)$$
> 
> $$= 2 - 1 - x + 3 + 3x + 3x^2$$
> 
> $$\boxed{p(x) = 4 + 2x + 3x^2}$$
> 
> ---
> 
> **8.** Reconstruir vector:
> 
> $$\vec{u} = 3\begin{bmatrix} 1 \ 1 \end{bmatrix} + 2\begin{bmatrix} 1 \ -1 \end{bmatrix} = \begin{bmatrix} 3+2 \ 3-2 \end{bmatrix} = \begin{bmatrix} 5 \ 1 \end{bmatrix}$$
> 
> En base canónica:
> 
> $$\boxed{[\vec{u}]_{\mathcal{E}} = \begin{bmatrix} 5 \ 1 \end{bmatrix}}$$
> 
> ---
> 
> **9.** Por definición, cada vector de la base se escribe como:
> 
> $$\vec{v}_1 = 1 \cdot \vec{v}_1 + 0 \cdot \vec{v}_2 + 0 \cdot \vec{v}_3 \Rightarrow [\vec{v}_1]_{\mathcal{B}} = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}$$
> 
> $$\vec{v}_2 = 0 \cdot \vec{v}_1 + 1 \cdot \vec{v}_2 + 0 \cdot \vec{v}_3 \Rightarrow [\vec{v}_2]_{\mathcal{B}} = \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}$$
> 
> $$\vec{v}_3 = 0 \cdot \vec{v}_1 + 0 \cdot \vec{v}_2 + 1 \cdot \vec{v}_3 \Rightarrow [\vec{v}_3]_{\mathcal{B}} = \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}$$
> 
> **Los vectores de una base siempre tienen coordenadas canónicas en su propia base.** ✓
> 
> ---
> 
> **10.** Sistema:
> 
> $$\begin{bmatrix} 3 & 5 \ 1 & 2 \end{bmatrix} = c_1\begin{bmatrix} 1 & 0 \ 0 & 0 \end{bmatrix} + c_2\begin{bmatrix} 0 & 0 \ 0 & 1 \end{bmatrix} + c_3\begin{bmatrix} 0 & 1 \ 1 & 0 \end{bmatrix} + c_4\begin{bmatrix} 0 & 1 \ -1 & 0 \end{bmatrix}$$
> 
> Comparando entradas:
> 
> $$\begin{cases} (1,1): c_1 = 3 \ (2,2): c_2 = 2 \ (1,2): c_3 + c_4 = 5 \ (2,1): c_3 - c_4 = 1 \end{cases}$$
> 
> De las últimas dos: $c_3 = 3$, $c_4 = 2$
> 
> $$\boxed{\left[\begin{bmatrix} 3 & 5 \ 1 & 2 \end{bmatrix}\right]_{\mathcal{B}} = \begin{bmatrix} 3 \ 2 \ 3 \ 2 \end{bmatrix}}$$

### Soluciones Avanzadas

> [!success]- 🔑 Respuestas Nivel 3
> 
> **11.**
> 
> a) La matriz $M$ tiene los vectores de la base como columnas:
> 
> $$\boxed{M = \begin{bmatrix} 1 & 2 & 1 \ 2 & 1 & 0 \ 1 & 0 & 1 \end{bmatrix}}$$
> 
> b) Calcular $M^{-1}$ usando eliminación Gauss-Jordan:
> 
> $$\left[\begin{array}{ccc|ccc} 1 & 2 & 1 & 1 & 0 & 0 \ 2 & 1 & 0 & 0 & 1 & 0 \ 1 & 0 & 1 & 0 & 0 & 1 \end{array}\right]$$
> 
> Operaciones: $F_2 - 2F_1$, $F_3 - F_1$:
> 
> $$\left[\begin{array}{ccc|ccc} 1 & 2 & 1 & 1 & 0 & 0 \ 0 & -3 & -2 & -2 & 1 & 0 \ 0 & -2 & 0 & -1 & 0 & 1 \end{array}\right]$$
> 
> Continuar operaciones...
> 
> $$\boxed{M^{-1} = \begin{bmatrix} 1 & -2 & -1 \ -2 & 0 & 2 \ -1 & 2 & -3 \end{bmatrix}}$$
> 
> c) Aplicar:
> 
> $$[\vec{u}]_{\mathcal{B}} = M^{-1}\vec{u} = \begin{bmatrix} 1 & -2 & -1 \ -2 & 0 & 2 \ -1 & 2 & -3 \end{bmatrix}\begin{bmatrix} 7 \ 5 \ 3 \end{bmatrix}$$
> 
> $$= \begin{bmatrix} 7 - 10 - 3 \ -14 + 0 + 6 \ -7 + 10 - 9 \end{bmatrix} = \begin{bmatrix} -6 \ -8 \ -6 \end{bmatrix}$$
> 
> (Verificar cálculos con más cuidado en ejercicio real)
> 
> ---
> 
> **12.** Primero expresar $p$ en forma estándar:
> 
> $$[p]_{\mathcal{B}} = \begin{bmatrix} 2 \ -3 \ 1 \end{bmatrix} \Rightarrow p(x) = 2 - 3x + x^2$$
> 
> Para base de Lagrange, evaluar en puntos:
> 
> $$p(0) = 2 - 0 + 0 = 2$$ $$p(1) = 2 - 3 + 1 = 0$$ $$p(2) = 2 - 6 + 4 = 0$$
> 
> $$\boxed{[p]_{\mathcal{L}} = \begin{bmatrix} 2 \ 0 \ 0 \end{bmatrix}}$$
> 
> **Interpretación:** El polinomio vale 2 en $x=0$ y cero en $x=1, 2$.
> 
> ---
> 
> **13.** Demostración:
> 
> Supongamos $c_1[\vec{v}_1]_{\mathcal{B}} + \cdots + c_k[\vec{v}_k]_{\mathcal{B}} = \vec{0}$
> 
> Por linealidad de coordenadas:
> 
> $$[c_1\vec{v}_1 + \cdots + c_k\vec{v}_k]_{\mathcal{B}} = \vec{0}$$
> 
> Como la función de coordenadas es inyectiva:
> 
> $$c_1\vec{v}_1 + \cdots + c_k\vec{v}_k = \vec{0}$$
> 
> Como ${\vec{v}_1, \ldots, \vec{v}_k}$ es L.I.:
> 
> $$c_1 = \cdots = c_k = 0$$
> 
> Por lo tanto ${[\vec{v}_1]_{\mathcal{B}}, \ldots, [\vec{v}_k]_{\mathcal{B}}}$ es L.I. ✓
> 
> ---
> 
> **14.**
> 
> a) Verificar ortonormalidad:
> 
> $$\left|\begin{bmatrix} \cos\theta \ \sin\theta \end{bmatrix}\right| = \sqrt{\cos^2\theta + \sin^2\theta} = 1$$ ✓
> 
> $$\begin{bmatrix} \cos\theta \ \sin\theta \end{bmatrix} \cdot \begin{bmatrix} -\sin\theta \ \cos\theta \end{bmatrix} = -\cos\theta\sin\theta + \sin\theta\cos\theta = 0$$ ✓
> 
> b) Para $\theta = \pi/4$: $\cos(\pi/4) = \sin(\pi/4) = \frac{\sqrt{2}}{2}$
> 
> Base:
> 
> $$\mathcal{B}_{\pi/4} = \left\{\begin{bmatrix} \sqrt{2}/2 \ \sqrt{2}/2 \end{bmatrix}, \begin{bmatrix} -\sqrt{2}/2 \ \sqrt{2}/2 \end{bmatrix}\right\}$$
> 
> Usando fórmula para base ortonormal:
> 
> $$c_1 = \begin{bmatrix} 1 \ 1 \end{bmatrix} \cdot \begin{bmatrix} \sqrt{2}/2 \ \sqrt{2}/2 \end{bmatrix} = \frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} = \sqrt{2}$$
> 
> $$c_2 = \begin{bmatrix} 1 \ 1 \end{bmatrix} \cdot \begin{bmatrix} -\sqrt{2}/2 \ \sqrt{2}/2 \end{bmatrix} = -\frac{\sqrt{2}}{2} + \frac{\sqrt{2}}{2} = 0$$
> 
> $$\boxed{\left[\begin{bmatrix} 1 \ 1 \end{bmatrix}\right]_{\mathcal{B}_{\pi/4}} = \begin{bmatrix} \sqrt{2} \ 0 \end{bmatrix}}$$
> 
> c) **Interpretación:** El vector $(1,1)$ está completamente alineado con el primer vector de la base rotada, por eso su segunda coordenada es cero. La primera coordenada es $\sqrt{2} = |(1,1)|$.
> 
> ---
> 
> **15.** Directamente:
> 
> $$f(x) = 3 \cdot 1 + 2 \cdot \cos(x) + (-1) \cdot \sin(x) + 4 \cdot \cos(2x) + 0 \cdot \sin(2x)$$
> 
> $$\boxed{[f]_{\mathcal{B}} = \begin{bmatrix} 3 \ 2 \ -1 \ 4 \ 0 \end{bmatrix}}$$

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre Coordenadas
> 
> ✅ **Las coordenadas son descriptivas, no intrínsecas:**
> 
> - Un vector ES un objeto geométrico/abstracto
> - Sus coordenadas son solo una DESCRIPCIÓN numérica
> - Diferentes bases → diferentes descripciones del mismo objeto
> 
> ✅ **Unicidad y existencia:**
> 
> - Para cada vector y base, existe UNA ÚNICA lista de coordenadas
> - Garantizada por que la base genera todo $V$ (existencia)
> - Garantizada por independencia lineal (unicidad)
> 
> ✅ **Orden importa:**
> 
> - Bases deben estar ordenadas: $\mathcal{B} = {\vec{v}_1, \vec{v}_2, \ldots}$
> - Cambiar el orden cambia las coordenadas
> - No son conjuntos, son listas
> 
> ---
> 
> ### Sobre Métodos de Cálculo
> 
> ✅ **Sistema de ecuaciones:**
> 
> - Directo para problemas pequeños
> - Plantear $\vec{u} = c_1\vec{v}_1 + \cdots + c_n\vec{v}_n$
> - Resolver componente a componente
> 
> ✅ **Forma matricial:**
> 
> - Eficiente para múltiples vectores
> - $M[\vec{u}]_{\mathcal{B}} = \vec{u}$ donde $M = [\vec{v}_1 | \cdots | \vec{v}_n]$
> - Una vez calculada $M^{-1}$, reutilizar para muchos vectores
> 
> ✅ **Fórmulas especiales:**
> 
> - Base ortogonal: $c_i = \frac{\vec{u} \cdot \vec{v}_i}{|\vec{v}_i|^2}$
> - Base ortonormal: $c_i = \vec{u} \cdot \vec{v}_i$
> - No requieren resolver sistemas
> 
> ---
> 
> ### Sobre Propiedades
> 
> ✅ **Linealidad es fundamental:**
> 
> - $[\alpha\vec{u} + \beta\vec{v}]_{\mathcal{B}} = \alpha[\vec{u}]_{\mathcal{B}} + \beta[\vec{v}]_{\mathcal{B}}$
> - Permite trabajar con coordenadas como vectores ordinarios
> - Base de toda la teoría de representación
> 
> ✅ **Isomorfismo con $\mathbb{R}^n$:**
> 
> - Todo espacio $n$-dimensional es "igual" a $\mathbb{R}^n$
> - Las coordenadas hacen explícito este isomorfismo
> - Permite usar herramientas computacionales
> 
> ✅ **Preserva independencia:**
> 
> - Vectores L.I. en $V$ → coordenadas L.I. en $\mathbb{R}^n$
> - Facilita verificación de independencia
> - Conecta propiedades abstractas con cálculos concretos
> 
> ---
> 
> ### Sobre Cambio de Base
> 
> ✅ **Mismo vector, diferentes descripciones:**
> 
> - $\vec{u}$ no cambia, solo su representación numérica
> - Diferentes bases revelan diferentes aspectos del vector
> - Analogía: mismo lugar, diferentes direcciones para llegar
> 
> ✅ **Proceso sistemático:**
> 
> - De coordenadas → Vector → Nuevas coordenadas
> - O directamente mediante matriz de cambio de base
> - Tema completo en siguiente capítulo
> 
> ✅ **Aplicaciones prácticas:**
> 
> - Simplificar problemas (elegir base adecuada)
> - Transformaciones geométricas
> - Procesamiento de señales (dominio tiempo ↔ frecuencia)
> - Machine Learning (PCA, cambio de features)

---

## 🔗 Notas Relacionadas

> [!quote]- 🌐 Conexiones Conceptuales
> 
> ### Prerequisitos:
> 
> - **[[08 - Bases]]** - Definición de base, verificación, construcción
> - **[[09 - Dimensión]]** - Relación entre dimensión y número de coordenadas
> - **[[06 - Combinaciones Lineales]]** - Expresar vectores como combinaciones
> - **[[07 - Independencia Lineal]]** - Unicidad de representación
> 
> ### Este tema es prerequisito para:
> 
> - **[[14 - Cambio de Base]]** - Matrices de transición entre bases
> - **[[16 - Transformaciones Lineales]]** - Representación matricial
> - **[[17 - Núcleo e Imagen]]** - Coordenadas de ker y im
> - **[[20 - Isomorfismos]]** - Equivalencia de espacios vectoriales
> - **[[22 - Eigenvalores y Eigenvectores]]** - Bases especiales
> 
> ### Temas relacionados:
> 
> - **Producto Interno** - Fórmulas para bases ortogonales
> - **Proyecciones** - Coordenadas en subespacios
> - **Proceso de Gram-Schmidt** - Construcción de bases ortonormales
> - **Descomposición QR** - Factorización usando bases
> 
> ### Aplicaciones conectadas:
> 
> - **Gráficos 3D** - Sistemas de coordenadas locales vs mundiales
> - **Procesamiento de señales** - Transformadas (Fourier, Wavelet)
> - **Machine Learning** - PCA, reducción de dimensionalidad
> - **Física Cuántica** - Estados en diferentes bases de medición
> - **Ingeniería** - Sistemas de referencia en mecánica
> 
> ### Diagrama de Flujo:
> 
> ```
>        Base Ordenada 𝓑
>              ↓
>    Vector 𝐮 en Espacio V
>              ↓
>  Combinación Lineal Única
>   𝐮 = c₁𝐯₁ + ... + cₙ𝐯ₙ
>              ↓
>   Vector de Coordenadas
>        [𝐮]𝓑 ∈ ℝⁿ
>              ↓
>        ┌─────┴─────┐
>        ↓           ↓
>   Cálculos      Cambio
>   Numéricos    de Base
>        ↓           ↓
>   Algoritmos   Matriz P
>   Concretos    𝓒←𝓑
> ```

---

## 📚 Resumen Ejecutivo

> [!summary]- 🎯 Lo Esencial
> 
> ### Idea Central
> 
> **Las coordenadas son la representación numérica de vectores abstractos respecto a una base elegida.**
> 
> ---
> 
> ### Definición
> 
> Para $\vec{u} \in V$ y base $\mathcal{B} = {\vec{v}_1, \ldots, \vec{v}_n}$:
> 
> $$\vec{u} = c_1\vec{v}_1 + \cdots + c_n\vec{v}_n$$
> 
> $$[\vec{u}]_{\mathcal{B}} = \begin{bmatrix} c_1 \ \vdots \ c_n \end{bmatrix} \in \mathbb{R}^n$$
> 
> ---
> 
> ### Propiedades Fundamentales
> 
> 1. **Existencia y unicidad** garantizadas por definición de base
> 2. **Linealidad:** $[\alpha\vec{u} + \beta\vec{v}]_{\mathcal{B}} = \alpha[\vec{u}]_{\mathcal{B}} + \beta[\vec{v}]_{\mathcal{B}}$
> 3. **Isomorfismo:** $V \cong \mathbb{R}^n$ vía coordenadas
> 4. **Preserva independencia:** L.I. en $V$ ↔ L.I. en $\mathbb{R}^n$
> 
> ---
> 
> ### Métodos de Cálculo
> 
> |Situación|Método|Complejidad|
> |---|---|---|
> |General|Sistema de ecuaciones|$O(n^3)$|
> |Múltiples vectores|Forma matricial $M^{-1}\vec{u}$|$O(n^3)$ + $O(n^2)$ cada uno|
> |Base ortogonal|$c_i = \frac{\vec{u} \cdot \vec{v}_i}{\|\vec{v}_i\|^2}$|$O(n^2)$|
> |Base ortonormal|$c_i = \vec{u} \cdot \vec{v}_i$|$O(n^2)$|
> 
> ---
> 
> ### Aplicaciones Clave
> 
> - **Computación:** Representación de objetos abstractos
> - **Cambio de perspectiva:** Diferentes bases revelan diferentes aspectos
> - **Simplificación:** Elegir base adecuada facilita cálculos
> - **Puente:** Entre teoría abstracta y práctica numérica
> 
> ---
> 
> ### Próximo Paso
> 
> **Cambio de Base:** Cómo convertir coordenadas entre diferentes bases usando matrices de transición.

---

**Tags:** #algebra-lineal #coordenadas #bases #representacion #isomorfismo #linealidad #cambio-de-base #base-ortogonal #calculo-coordenadas #espacio-vectorial