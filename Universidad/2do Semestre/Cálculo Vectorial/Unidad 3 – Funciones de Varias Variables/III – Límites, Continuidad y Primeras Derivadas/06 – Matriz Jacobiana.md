# 📘 Matriz Jacobiana

## 🎯 Introducción

> [!info]- 💡 ¿Por qué es importante la Matriz Jacobiana?
> 
> Cuando trabajamos con funciones de una variable, la derivada nos dice cómo cambia la función. Pero, **¿qué pasa cuando tenemos una función que toma varios inputs y produce varios outputs?** La matriz Jacobiana es la generalización natural de la derivada a este contexto.
> 
> **Motivación:**
> 
> - Una función $f: \mathbb{R} \to \mathbb{R}$ tiene derivada $f'(x)$ (un número)
> - Una función $f: \mathbb{R}^n \to \mathbb{R}$ tiene gradiente $\nabla f$ (un vector)
> - Una función $\vec{F}: \mathbb{R}^n \to \mathbb{R}^m$ tiene **matriz Jacobiana** $J_{\vec{F}}$ (una matriz)
> 
> **Analogía:**
> 
> - **Derivada (1D):** Pendiente de una curva
> - **Gradiente:** Vector de pendientes (para funciones escalares)
> - **Jacobiana:** Matriz de todas las derivadas parciales (para funciones vectoriales)
> 
> **Preguntas que responde:**
> 
> - ¿Cómo cambian múltiples outputs cuando varían múltiples inputs?
> - ¿Cómo se comporta una transformación cerca de un punto?
> - ¿Es una transformación invertible localmente?
> 
> **Aplicaciones prácticas:**
> 
> - **Robótica:** Cómo pequeños movimientos en las articulaciones afectan la posición del brazo
> - **Economía:** Cómo cambios en variables económicas afectan múltiples indicadores
> - **Física:** Transformaciones de coordenadas (cartesianas ↔ polares ↔ esféricas)
> - **Machine Learning:** Backpropagation en redes neuronales
> - **Optimización:** Método de Newton para sistemas no lineales
> - **Análisis de sensibilidad:** Cómo errores en inputs se propagan a outputs

---

## 📝 Definición de la Matriz Jacobiana

### 🔑 Definición Formal

> [!example]- 🟢 Definición: Matriz Jacobiana
> 
> **Contexto:** Sea $\vec{F}: \mathbb{R}^n \to \mathbb{R}^m$ una función vectorial:
> 
> $$\vec{F}(\vec{x}) = \vec{F}(x_1, x_2, \ldots, x_n) = \begin{bmatrix} F_1(x_1, \ldots, x_n) \ F_2(x_1, \ldots, x_n) \ \vdots \ F_m(x_1, \ldots, x_n) \end{bmatrix}$$
> 
> **Definición:** La **matriz Jacobiana** de $\vec{F}$ es la matriz $m \times n$ de todas las derivadas parciales:
> 
> $$J_{\vec{F}}(\vec{x}) = \begin{bmatrix} \frac{\partial F_1}{\partial x_1} & \frac{\partial F_1}{\partial x_2} & \cdots & \frac{\partial F_1}{\partial x_n} \[0.3em] \frac{\partial F_2}{\partial x_1} & \frac{\partial F_2}{\partial x_2} & \cdots & \frac{\partial F_2}{\partial x_n} \[0.3em] \vdots & \vdots & \ddots & \vdots \[0.3em] \frac{\partial F_m}{\partial x_1} & \frac{\partial F_m}{\partial x_2} & \cdots & \frac{\partial F_m}{\partial x_n} \end{bmatrix}$$
> 
> **En notación compacta:**
> 
> $$J_{\vec{F}} = \begin{bmatrix} \nabla F_1^T \ \nabla F_2^T \ \vdots \ \nabla F_m^T \end{bmatrix} \quad \text{o} \quad [J_{\vec{F}}]_{ij} = \frac{\partial F_i}{\partial x_j}$$
> 
> ---
> 
> **Notaciones alternativas:**
> 
> - $J_{\vec{F}}(\vec{x})$ - Jacobiana de $\vec{F}$ en $\vec{x}$
> - $D\vec{F}(\vec{x})$ - Derivada de $\vec{F}$ en $\vec{x}$
> - $\vec{F}'(\vec{x})$ - Derivada de $\vec{F}$
> - $\frac{\partial \vec{F}}{\partial \vec{x}}$ - Derivada parcial (notación física)
> - $\frac{\partial(F_1, \ldots, F_m)}{\partial(x_1, \ldots, x_n)}$ - Notación de Jacobi
> 
> ---
> 
> **Estructura:**
> 
> - **Filas:** Cada fila es el gradiente (transpuesto) de una función componente $F_i$
> - **Columnas:** Cada columna contiene las derivadas de todas las componentes respecto a $x_j$
> - **Dimensión:** $m \times n$ (outputs × inputs)
> 
> ---
> 
> **Interpretación:**
> 
> - La Jacobiana describe cómo cambia $\vec{F}$ en todas las direcciones
> - Es la **mejor aproximación lineal** de $\vec{F}$ cerca de un punto
> - Generaliza el concepto de derivada a funciones vectoriales

### 🎯 Casos Especiales

> [!note]- 📋 Casos Importantes
> 
> ### 1. Función Escalar: $f: \mathbb{R}^n \to \mathbb{R}$
> 
> La Jacobiana es una matriz $1 \times n$ (fila):
> 
> $$J_f = \begin{bmatrix} \frac{\partial f}{\partial x_1} & \frac{\partial f}{\partial x_2} & \cdots & \frac{\partial f}{\partial x_n} \end{bmatrix} = \nabla f^T$$
> 
> Es el **gradiente transpuesto**.
> 
> **Ejemplo:** $f(x,y) = x^2 + y^2$
> 
> $$J_f = \begin{bmatrix} 2x & 2y \end{bmatrix}$$
> 
> ---
> 
> ### 2. Campo Vectorial en el Plano: $\vec{F}: \mathbb{R}^2 \to \mathbb{R}^2$
> 
> La Jacobiana es una matriz $2 \times 2$:
> 
> $$J_{\vec{F}} = \begin{bmatrix} \frac{\partial F_1}{\partial x} & \frac{\partial F_1}{\partial y} \[0.3em] \frac{\partial F_2}{\partial x} & \frac{\partial F_2}{\partial y} \end{bmatrix}$$
> 
> **Ejemplo:** $\vec{F}(x,y) = \begin{bmatrix} x^2 - y^2 \ 2xy \end{bmatrix}$
> 
> $$J_{\vec{F}} = \begin{bmatrix} 2x & -2y \ 2y & 2x \end{bmatrix}$$
> 
> ---
> 
> ### 3. Función de Variable Escalar: $\vec{F}: \mathbb{R} \to \mathbb{R}^m$
> 
> La Jacobiana es una matriz $m \times 1$ (columna):
> 
> $$J_{\vec{F}} = \begin{bmatrix} F_1'(t) \ F_2'(t) \ \vdots \ F_m'(t) \end{bmatrix} = \vec{F}'(t)$$
> 
> Es el **vector derivada** de una curva parametrizada.
> 
> **Ejemplo:** $\vec{r}(t) = \begin{bmatrix} \cos t \ \sin t \ t \end{bmatrix}$
> 
> $$J_{\vec{r}} = \begin{bmatrix} -\sin t \ \cos t \ 1 \end{bmatrix}$$
> 
> ---
> 
> ### 4. Función Identidad: $\vec{F}(\vec{x}) = \vec{x}$
> 
> La Jacobiana es la **matriz identidad**:
> 
> $$J_{\vec{F}} = I_n = \begin{bmatrix} 1 & 0 & \cdots & 0 \ 0 & 1 & \cdots & 0 \ \vdots & \vdots & \ddots & \vdots \ 0 & 0 & \cdots & 1 \end{bmatrix}$$
> 
> ---
> 
> ### 5. Transformación Lineal: $\vec{F}(\vec{x}) = A\vec{x}$
> 
> La Jacobiana es la **matriz constante** $A$:
> 
> $$J_{\vec{F}} = A$$
> 
> Esto tiene sentido porque las transformaciones lineales son su propia derivada.

---

## 📊 Ejemplos Básicos

### Ejemplo 1: Función $\mathbb{R}^2 \to \mathbb{R}^2$

> [!example]- 📝 Ejemplo 1: Transformación Simple
> 
> **Función:** $$\vec{F}(x,y) = \begin{bmatrix} x + y \ xy \end{bmatrix}$$
> 
> **Componentes:**
> 
> - $F_1(x,y) = x + y$
> - $F_2(x,y) = xy$
> 
> ---
> 
> **Calcular la Jacobiana:**
> 
> **Fila 1:** Derivadas de $F_1$
> 
> $$\frac{\partial F_1}{\partial x} = 1, \quad \frac{\partial F_1}{\partial y} = 1$$
> 
> **Fila 2:** Derivadas de $F_2$
> 
> $$\frac{\partial F_2}{\partial x} = y, \quad \frac{\partial F_2}{\partial y} = x$$
> 
> **Matriz Jacobiana:**
> 
> $$J_{\vec{F}}(x,y) = \begin{bmatrix} 1 & 1 \ y & x \end{bmatrix}$$
> 
> ---
> 
> **Evaluar en un punto específico:** $(2, 3)$
> 
> $$J_{\vec{F}}(2,3) = \begin{bmatrix} 1 & 1 \ 3 & 2 \end{bmatrix}$$
> 
> ---
> 
> **Interpretación:**
> 
> Esta matriz describe cómo pequeños cambios en $(x,y)$ cerca de $(2,3)$ afectan a $\vec{F}$:
> 
> $$\Delta \vec{F} \approx J_{\vec{F}}(2,3) \begin{bmatrix} \Delta x \ \Delta y \end{bmatrix} = \begin{bmatrix} 1 & 1 \ 3 & 2 \end{bmatrix} \begin{bmatrix} \Delta x \ \Delta y \end{bmatrix}$$

### Ejemplo 2: Coordenadas Polares

> [!example]- 📝 Ejemplo 2: Transformación a Polares
> 
> **Transformación:** De coordenadas cartesianas a polares
> 
> $$\vec{F}(r, \theta) = \begin{bmatrix} r\cos\theta \ r\sin\theta \end{bmatrix} = \begin{bmatrix} x \ y \end{bmatrix}$$
> 
> **Componentes:**
> 
> - $F_1(r,\theta) = r\cos\theta = x$
> - $F_2(r,\theta) = r\sin\theta = y$
> 
> ---
> 
> **Calcular la Jacobiana:**
> 
> $$\frac{\partial F_1}{\partial r} = \cos\theta, \quad \frac{\partial F_1}{\partial \theta} = -r\sin\theta$$
> 
> $$\frac{\partial F_2}{\partial r} = \sin\theta, \quad \frac{\partial F_2}{\partial \theta} = r\cos\theta$$
> 
> **Matriz Jacobiana:**
> 
> $$J_{\vec{F}}(r,\theta) = \begin{bmatrix} \cos\theta & -r\sin\theta \ \sin\theta & r\cos\theta \end{bmatrix}$$
> 
> ---
> 
> **Determinante (Jacobiano):**
> 
> $$\det(J_{\vec{F}}) = \cos\theta \cdot r\cos\theta - (-r\sin\theta) \cdot \sin\theta$$
> 
> $$= r\cos^2\theta + r\sin^2\theta = r(\cos^2\theta + \sin^2\theta) = r$$
> 
> $$\boxed{\det(J_{\vec{F}}) = r}$$
> 
> ---
> 
> **Importancia:**
> 
> Este determinante aparece en el factor de cambio de variables en integrales:
> 
> $$\iint_R f(x,y) , dx,dy = \iint_S f(r\cos\theta, r\sin\theta) \cdot r , dr,d\theta$$
> 
> El factor $r$ es el **Jacobiano** de la transformación.

### Ejemplo 3: Función $\mathbb{R}^3 \to \mathbb{R}^2$

> [!example]- 📝 Ejemplo 3: Dimensiones Diferentes
> 
> **Función:** $$\vec{F}(x,y,z) = \begin{bmatrix} x^2 + y^2 \ xyz \end{bmatrix}$$
> 
> **Componentes:**
> 
> - $F_1(x,y,z) = x^2 + y^2$
> - $F_2(x,y,z) = xyz$
> 
> ---
> 
> **Calcular la Jacobiana:**
> 
> **Fila 1:** Derivadas de $F_1$
> 
> $$\frac{\partial F_1}{\partial x} = 2x, \quad \frac{\partial F_1}{\partial y} = 2y, \quad \frac{\partial F_1}{\partial z} = 0$$
> 
> **Fila 2:** Derivadas de $F_2$
> 
> $$\frac{\partial F_2}{\partial x} = yz, \quad \frac{\partial F_2}{\partial y} = xz, \quad \frac{\partial F_2}{\partial z} = xy$$
> 
> **Matriz Jacobiana:**
> 
> $$J_{\vec{F}}(x,y,z) = \begin{bmatrix} 2x & 2y & 0 \ yz & xz & xy \end{bmatrix}$$
> 
> Dimensión: $2 \times 3$
> 
> ---
> 
> **Evaluar en $(1, 2, 3)$:**
> 
> $$J_{\vec{F}}(1,2,3) = \begin{bmatrix} 2 & 4 & 0 \ 6 & 3 & 2 \end{bmatrix}$$
> 
> ---
> 
> **Observación:**
> 
> Como la matriz no es cuadrada, no tiene determinante. Esto es típico cuando el número de inputs y outputs no coincide.

### Ejemplo 4: Coordenadas Esféricas

> [!example]- 📝 Ejemplo 4: Transformación Esférica
> 
> **Transformación:** De coordenadas esféricas a cartesianas
> 
> $$\vec{F}(\rho, \phi, \theta) = \begin{bmatrix} \rho\sin\phi\cos\theta \ \rho\sin\phi\sin\theta \ \rho\cos\phi \end{bmatrix} = \begin{bmatrix} x \ y \ z \end{bmatrix}$$
> 
> **Componentes:**
> 
> - $F_1 = \rho\sin\phi\cos\theta$ (coordenada $x$)
> - $F_2 = \rho\sin\phi\sin\theta$ (coordenada $y$)
> - $F_3 = \rho\cos\phi$ (coordenada $z$)
> 
> ---
> 
> **Calcular derivadas parciales:**
> 
> **Respecto a $\rho$:** $$\frac{\partial F_1}{\partial \rho} = \sin\phi\cos\theta$$ $$\frac{\partial F_2}{\partial \rho} = \sin\phi\sin\theta$$ $$\frac{\partial F_3}{\partial \rho} = \cos\phi$$
> 
> **Respecto a $\phi$:** $$\frac{\partial F_1}{\partial \phi} = \rho\cos\phi\cos\theta$$ $$\frac{\partial F_2}{\partial \phi} = \rho\cos\phi\sin\theta$$ $$\frac{\partial F_3}{\partial \phi} = -\rho\sin\phi$$
> 
> **Respecto a $\theta$:** $$\frac{\partial F_1}{\partial \theta} = -\rho\sin\phi\sin\theta$$ $$\frac{\partial F_2}{\partial \theta} = \rho\sin\phi\cos\theta$$ $$\frac{\partial F_3}{\partial \theta} = 0$$
> 
> ---
> 
> **Matriz Jacobiana:**
> 
> $$J_{\vec{F}} = \begin{bmatrix} \sin\phi\cos\theta & \rho\cos\phi\cos\theta & -\rho\sin\phi\sin\theta \ \sin\phi\sin\theta & \rho\cos\phi\sin\theta & \rho\sin\phi\cos\theta \ \cos\phi & -\rho\sin\phi & 0 \end{bmatrix}$$
> 
> ---
> 
> **Determinante (Jacobiano):**
> 
> Después de cálculos (usando cofactores o regla de Sarrus):
> 
> $$\boxed{\det(J_{\vec{F}}) = \rho^2\sin\phi}$$
> 
> Este es el factor que aparece en integrales triples en coordenadas esféricas:
> 
> $$\iiint_V f(x,y,z) , dx,dy,dz = \iiint_S f(\vec{F}(\rho,\phi,\theta)) \cdot \rho^2\sin\phi , d\rho,d\phi,d\theta$$

---

## 🧮 Interpretación Geométrica

> [!note]- 🎨 Visualización de la Jacobiana
> 
> ### Aproximación Lineal
> 
> La Jacobiana proporciona la **mejor aproximación lineal** de $\vec{F}$ cerca de un punto $\vec{a}$:
> 
> $$\vec{F}(\vec{a} + \vec{h}) \approx \vec{F}(\vec{a}) + J_{\vec{F}}(\vec{a}) \vec{h}$$
> 
> **Interpretación:**
> 
> - $\vec{F}(\vec{a})$ : Valor en el punto
> - $J_{\vec{F}}(\vec{a}) \vec{h}$ : Cambio aproximado para desplazamiento pequeño $\vec{h}$
> 
> ---
> 
> ### Transformación de Vectores Tangentes
> 
> Si pensamos en $\vec{h}$ como un vector tangente en $\vec{a}$, entonces $J_{\vec{F}}(\vec{a})\vec{h}$ es el vector tangente correspondiente en la imagen.
> 
> ```
>     Espacio de entrada          Espacio de salida
>            ℝⁿ                          ℝᵐ
>     
>         •─→ h                      •─→ J_F(a)h
>         a                          F(a)
>           ╲                          ╲
>            ╲ F                        ╲
>             ╲                          ╲
>              ↓                          ↓
>         superficie                 superficie
>           curva                      imagen
> ```
> 
> La Jacobiana **transforma vectores tangentes** del dominio en vectores tangentes del codominio.
> 
> ---
> 
> ### Determinante: Factor de Escala
> 
> Para $\vec{F}: \mathbb{R}^n \to \mathbb{R}^n$ (funciones cuadradas), el **determinante Jacobiano** mide:
> 
> - **Cambio de volumen** bajo la transformación
> - $|\det(J_{\vec{F}})|$ = factor por el cual $\vec{F}$ expande o contrae volúmenes localmente
> 
> **Casos:**
> 
> - $|\det(J_{\vec{F}})| > 1$ : Expansión local
> - $|\det(J_{\vec{F}})| < 1$ : Contracción local
> - $\det(J_{\vec{F}}) = 0$ : Degeneración (pérdida de dimensión)
> - $\det(J_{\vec{F}}) < 0$ : Inversión de orientación
> 
> ---
> 
> ### Ejemplo Visual: Rotación y Escala
> 
> **Transformación:** $\vec{F}(x,y) = \begin{bmatrix} 2x \ 2y \end{bmatrix}$ (escala por 2)
> 
> $$J_{\vec{F}} = \begin{bmatrix} 2 & 0 \ 0 & 2 \end{bmatrix}$$
> 
> $$\det(J_{\vec{F}}) = 4$$
> 
> **Interpretación:** Esta transformación multiplica áreas por 4.
> 
> ```
>     Entrada              Salida
>     
>     □ (área 1)    →     ▢ (área 4)
>     1×1                  2×2
> ```

---

## 🔧 Propiedades de la Matriz Jacobiana

> [!note]- ⭐ Propiedades Fundamentales
> 
> ### 1. Linealidad en las Funciones
> 
> Si $\vec{F}$ y $\vec{G}$ son funciones vectoriales y $c_1, c_2 \in \mathbb{R}$:
> 
> $$J_{c_1\vec{F} + c_2\vec{G}} = c_1 J_{\vec{F}} + c_2 J_{\vec{G}}$$
> 
> ---
> 
> ### 2. Regla de la Cadena
> 
> Si $\vec{F}: \mathbb{R}^n \to \mathbb{R}^m$ y $\vec{G}: \mathbb{R}^m \to \mathbb{R}^p$, entonces:
> 
> $$J_{\vec{G} \circ \vec{F}}(\vec{x}) = J_{\vec{G}}(\vec{F}(\vec{x})) \cdot J_{\vec{F}}(\vec{x})$$
> 
> **En palabras:** La Jacobiana de una composición es el **producto** de las Jacobianas.
> 
> **Dimensiones:**
> 
> - $J_{\vec{F}}$ es $m \times n$
> - $J_{\vec{G}}$ es $p \times m$
> - $J_{\vec{G} \circ \vec{F}}$ es $p \times n$
> 
> ---
> 
> ### 3. Transformación Lineal
> 
> Si $\vec{F}(\vec{x}) = A\vec{x}$ (transformación lineal), entonces:
> 
> $$J_{\vec{F}}(\vec{x}) = A$$ para todo $\vec{x}$
> 
> La Jacobiana es **constante** y es la matriz de la transformación.
> 
> ---
> 
> ### 4. Función Identidad
> 
> Si $\vec{F}(\vec{x}) = \vec{x}$, entonces:
> 
> $$J_{\vec{F}} = I_n$$
> 
> (matriz identidad)
> 
> ---
> 
> ### 5. Continuidad
> 
> Si $\vec{F} \in C^1$ (todas las derivadas parciales son continuas), entonces:
> 
> - $J_{\vec{F}}$ es una función continua
> - La función $\vec{x} \mapsto J_{\vec{F}}(\vec{x})$ es continua
> 
> ---
> 
> ### 6. Rango y Dimensión
> 
> El **rango** de $J_{\vec{F}}(\vec{a})$ da información sobre el comportamiento local de $\vec{F}$:
> 
> - $\text{rank}(J_{\vec{F}}(\vec{a})) = m$ : $\vec{F}$ es localmente sobreyectiva (sumersión)
> - $\text{rank}(J_{\vec{F}}(\vec{a})) = n$ : $\vec{F}$ es localmente inyectiva (inmersión)
> - $\text{rank}(J_{\vec{F}}(\vec{a})) < \min(m,n)$ : Punto singular

---

## 📐 El Jacobiano (Determinante)

> [!note]- 🎯 Determinante de la Jacobiana
> 
> ### Definición
> 
> Para funciones $\vec{F}: \mathbb{R}^n \to \mathbb{R}^n$ (cuadradas), el **Jacobiano** es:
> 
> $$\mathcal{J}_{\vec{F}}(\vec{x}) = \det(J_{\vec{F}}(\vec{x}))$$
> 
> También se denota:
> 
> - $\frac{\partial(F_1, \ldots, F_n)}{\partial(x_1, \ldots, x_n)}$
> - $\text{Jac}(\vec{F})$
> 
> ---
> 
> ### Interpretación Geométrica
> 
> **Factor de cambio de volumen:**
> 
> Si $V$ es un volumen pequeño en el dominio, entonces:
> 
> $$\text{Vol}(\vec{F}(V)) \approx |\mathcal{J}_{\vec{F}}(\vec{x})| \cdot \text{Vol}(V)$$
> 
> donde $\vec{x}$ es un punto en $V$.
> 
> ---
> 
> ### Aplicación: Cambio de Variables en Integrales
> 
> **Teorema del Cambio de Variables:**
> 
> Si $\vec{F}: U \to V$ es un difeomorfismo ($C^1$ e invertible), entonces:
> 
> $$\int_V f(\vec{y}) , d\vec{y} = \int_U f(\vec{F}(\vec{x})) \cdot |\mathcal{J}_{\vec{F}}(\vec{x})| , d\vec{x}$$
> 
> ---
> 
> ### Casos Importantes
> 
> **1. Coordenadas polares 2D:** $$\mathcal{J} = r$$
> 
> **2. Coordenadas cilíndricas:** $$\mathcal{J} = r$$
> 
> **3. Coordenadas esféricas:** $$\mathcal{J} = \rho^2\sin\phi$$
> 
> ---
> 
> ### Invertibilidad Local
> 
> **Teorema de la Función Inversa:**
> 
> Si $\vec{F} \in C^1$ y $\mathcal{J}_{\vec{F}}(\vec{a}) \neq 0$, entonces:
> 
> - $\vec{F}$ es **localmente invertible** cerca de $\vec{a}$
> - Existe $\vec{F}^{-1}$ definida en un entorno de $\vec{F}(\vec{a})$
> - La Jacobiana de la inversa es:
> 
> $$J_{\vec{F}^{-1}}(\vec{F}(\vec{a})) = [J_{\vec{F}}(\vec{a})]^{-1}$$

---

## 📚 Regla de la Cadena Multivariable

> [!note]- 🔗 Composición de Funciones
> 
> ### Teorema: Regla de la Cadena
> 
> **Contexto:**
> 
> - $\vec{F}: \mathbb{R}^n \to \mathbb{R}^m$
> - $\vec{G}: \mathbb{R}^m \to \mathbb{R}^p$
> - $\vec{H} = \vec{G} \circ \vec{F}$: $\mathbb{R}^n \to \mathbb{R}^p$
> 
> **Teorema:**
> 
> $$J_{\vec{H}}(\vec{x}) = J_{\vec{G}}(\vec{F}(\vec{x})) \cdot J_{\vec{F}}(\vec{x})$$
> 
> **Dimensiones:**
> 
> 
> J_H: p × n = (J_G: p × m) · (J_F: m × n)
> 
> 
> ---
> 
> ### Caso Especial: Función Escalar Compuesta
> 
> Si $\vec{F}: \mathbb{R}^n \to \mathbb{R}^m$ y $g: \mathbb{R}^m \to \mathbb{R}$:
> 
> $$h(\vec{x}) = g(\vec{F}(\vec{x}))$$
> 
> Entonces:
> 
> $$\nabla h(\vec{x}) = J_{\vec{F}}(\vec{x})^T \cdot \nabla g(\vec{F}(\vec{x}))$$
> 
> o en componentes:
> 
> $$\frac{\partial h}{\partial x_i} = \sum_{j=1}^m \frac{\partial g}{\partial y_j} \cdot \frac{\partial F_j}{\partial x_i}$$
> 
> ---
> 
> ### Ejemplo: Composición Simple
> 
> **Funciones:**
> 
> $$\vec{F}(s,t) = \begin{bmatrix} s + t \\ st \end{bmatrix}, \quad \vec{G}(u,v) = \begin{bmatrix} u^2 + v \\ uv \end{bmatrix}$$
> 
> **Composición:** $\vec{H} = \vec{G} \circ \vec{F}$
> 
> **Jacobianas:**
> 
> $$J_{\vec{F}} = \begin{bmatrix} 1 & 1 \\ t & s \end{bmatrix}$$
> 
> $$J_{\vec{G}}(u,v) = \begin{bmatrix} 2u & 1 \\ v & u \end{bmatrix}$$
> 
> **En el punto $(s,t)$:**
> 
> Primero calcular $\vec{F}(s,t) = (u,v)$ donde $u = s+t$, $v = st$
> 
> $$J_{\vec{G}}(\vec{F}(s,t)) = \begin{bmatrix} 2(s+t) & 1 \\ st & s+t \end{bmatrix}$$
> 
> **Jacobiana de la composición:**
> 
> $$J_{\vec{H}}(s,t) = \begin{bmatrix} 2(s+t) & 1 \\ st & s+t \end{bmatrix} \begin{bmatrix} 1 & 1 \\ t & s \end{bmatrix}$$
> 
> $$= \begin{bmatrix} 2(s+t) + t & 2(s+t) + s \\ st + t(s+t) & st + s(s+t) \end{bmatrix}$$
> 
> $$= \begin{bmatrix} 2s + 3t & 3s + 2t \\ st + st + t^2 & st + s^2 + st \end{bmatrix}$$
> 
> $$= \begin{bmatrix} 2s + 3t & 3s + 2t \\ 2st + t^2 & 2st + s^2 \end{bmatrix}$$
> 

---

## 🎯 Aplicaciones de la Matriz Jacobiana

### Aplicación 1: Cambio de Variables en Integrales

> [!example]- 🔄 Integrales con Cambio de Coordenadas
> 
> **Problema:** Calcular
> 
> $$\iint_R e^{-(x^2+y^2)} , dx,dy$$
> 
> sobre todo el plano $\mathbb{R}^2$.
> 
> ---
> 
> **Solución con coordenadas polares:**
> 
> **Transformación:**
> 
> $$\vec{F}(r,\theta) = \begin{bmatrix} r\cos\theta \ r\sin\theta \end{bmatrix} = \begin{bmatrix} x \ y \end{bmatrix}$$
> 
> **Jacobiana:**
> 
> $$J_{\vec{F}} = \begin{bmatrix} \cos\theta & -r\sin\theta \ \sin\theta & r\cos\theta \end{bmatrix}$$
> 
> **Jacobiano:**
> 
> $$\mathcal{J} = \det(J_{\vec{F}}) = r$$
> 
> ---
> 
> **Cambio de variables:**
> 
> $$\iint_{\mathbb{R}^2} e^{-(x^2+y^2)} , dx,dy = \int_0^{2\pi} \int_0^\infty e^{-r^2} \cdot r , dr,d\theta$$
> 
> **Integral en $r$:**
> 
> $$\int_0^\infty re^{-r^2} , dr = \left[-\frac{1}{2}e^{-r^2}\right]_0^\infty = \frac{1}{2}$$
> 
> **Integral en $\theta$:**
> 
> $$\int_0^{2\pi} d\theta = 2\pi$$
> 
> **Resultado:**
> 
> $$\boxed{\iint_{\mathbb{R}^2} e^{-(x^2+y^2)} , dx,dy = \pi}$$
> 
> El factor $r$ en el integrando proviene del **Jacobiano**.

### Aplicación 2: Método de Newton para Sistemas

> [!example]- 🔧 Resolución de Sistemas No Lineales
> 
> **Problema:** Resolver el sistema no lineal
> 
> $$\vec{F}(\vec{x}) = \vec{0}$$
> 
> donde $\vec{F}: \mathbb{R}^n \to \mathbb{R}^n$
> 
> ---
> 
> **Método de Newton Multivariable:**
> 
> Iteración:
> 
> $$\vec{x}_{k+1} = \vec{x}_k - [J_{\vec{F}}(\vec{x}_k)]^{-1} \vec{F}(\vec{x}_k)$$
> 
> Equivalentemente, resolver:
> 
> $$J_{\vec{F}}(\vec{x}_k) \Delta \vec{x}_k = -\vec{F}(\vec{x}_k)$$
> 
> y actualizar: $\vec{x}_{k+1} = \vec{x}_k + \Delta \vec{x}_k$
> 
> ---
> 
> **Ejemplo:** Resolver
> 
> $$\begin{cases} x^2 + y^2 - 5 = 0 \ x^2 - y - 1 = 0 \end{cases}$$
> 
> **Definir:**
> 
> $$\vec{F}(x,y) = \begin{bmatrix} x^2 + y^2 - 5 \ x^2 - y - 1 \end{bmatrix}$$
> 
> **Jacobiana:**
> 
> $$J_{\vec{F}}(x,y) = \begin{bmatrix} 2x & 2y \ 2x & -1 \end{bmatrix}$$
> 
> **Punto inicial:** $(x_0, y_0) = (2, 1)$
> 
> **Iteración 1:**
> 
> $$\vec{F}(2,1) = \begin{bmatrix} 4 + 1 - 5 \ 4 - 1 - 1 \end{bmatrix} = \begin{bmatrix} 0 \ 2 \end{bmatrix}$$
> 
> $$J_{\vec{F}}(2,1) = \begin{bmatrix} 4 & 2 \ 4 & -1 \end{bmatrix}$$
> 
> Resolver:
> 
> $$\begin{bmatrix} 4 & 2 \ 4 & -1 \end{bmatrix} \begin{bmatrix} \Delta x \ \Delta y \end{bmatrix} = -\begin{bmatrix} 0 \ 2 \end{bmatrix}$$
> 
> Solución: $\Delta x = 1/6$, $\Delta y = -1/3$
> 
> $$\vec{x}_1 = \begin{bmatrix} 2 \ 1 \end{bmatrix} + \begin{bmatrix} 1/6 \ -1/3 \end{bmatrix} = \begin{bmatrix} 2.167 \ 0.667 \end{bmatrix}$$
> 
> Continuar iterando hasta convergencia...

### Aplicación 3: Robótica - Cinemática Inversa

> [!example]- 🤖 Brazo Robótico
> 
> **Problema:** Un brazo robótico con dos articulaciones.
> 
> **Cinemática directa:** Dados ángulos $(\theta_1, \theta_2)$, encontrar posición $(x,y)$:
> 
> $$\vec{F}(\theta_1, \theta_2) = \begin{bmatrix} L_1\cos\theta_1 + L_2\cos(\theta_1 + \theta_2) \ L_1\sin\theta_1 + L_2\sin(\theta_1 + \theta_2) \end{bmatrix}$$
> 
> donde $L_1, L_2$ son las longitudes de los eslabones.
> 
> ---
> 
> **Jacobiana:**
> 
> $$J_{\vec{F}} = \begin{bmatrix} -L_1\sin\theta_1 - L_2\sin(\theta_1+\theta_2) & -L_2\sin(\theta_1+\theta_2) \ L_1\cos\theta_1 + L_2\cos(\theta_1+\theta_2) & L_2\cos(\theta_1+\theta_2) \end{bmatrix}$$
> 
> ---
> 
> **Interpretación:**
> 
> La Jacobiana relaciona **velocidades en las articulaciones** con **velocidades en el espacio de trabajo**:
> 
> $$\begin{bmatrix} \dot{x} \ \dot{y} \end{bmatrix} = J_{\vec{F}} \begin{bmatrix} \dot{\theta}_1 \ \dot{\theta}_2 \end{bmatrix}$$
> 
> **Aplicación práctica:**
> 
> - Si queremos que el extremo del brazo se mueva con velocidad $(\dot{x}, \dot{y})$
> - Necesitamos calcular las velocidades angulares: $\begin{bmatrix} \dot{\theta}_1 \ \dot{\theta}_2 \end{bmatrix} = J_{\vec{F}}^{-1} \begin{bmatrix} \dot{x} \ \dot{y} \end{bmatrix}$
> 
> **Singularidades:**
> 
> Cuando $\det(J_{\vec{F}}) = 0$, el brazo está en una **configuración singular** (brazo completamente extendido o plegado), donde pierde un grado de libertad.

### Aplicación 4: Machine Learning - Backpropagation

> [!example]- 🧠 Redes Neuronales
> 
> **Contexto:** Red neuronal con función de pérdida $L(\vec{w})$ donde $\vec{w}$ son los pesos.
> 
> **Estructura en capas:**
> 
> $$\vec{x} \xrightarrow{\vec{F}_1} \vec{h}_1 \xrightarrow{\vec{F}_2} \vec{h}_2 \xrightarrow{\vec{F}_3} \vec{y} \xrightarrow{L} \text{pérdida}$$
> 
> ---
> 
> **Gradiente de la pérdida:**
> 
> Usando la regla de la cadena:
> 
> $$\frac{\partial L}{\partial \vec{w}_1} = \frac{\partial L}{\partial \vec{y}} \cdot \frac{\partial \vec{y}}{\partial \vec{h}_2} \cdot \frac{\partial \vec{h}_2}{\partial \vec{h}_1} \cdot \frac{\partial \vec{h}_1}{\partial \vec{w}_1}$$
> 
> En términos de Jacobianas:
> 
> $$\nabla_{\vec{w}_1} L = J_{\vec{F}_1}^T \cdot J_{\vec{F}_2}^T \cdot J_{\vec{F}_3}^T \cdot \nabla_{\vec{y}} L$$
> 
> ---
> 
> **Backpropagation:**
> 
> Calcular los gradientes **hacia atrás** (de salida a entrada):
> 
> 1. Calcular $\delta_3 = \nabla_{\vec{y}} L$
> 2. Propagar: $\delta_2 = J_{\vec{F}_3}^T \delta_3$
> 3. Propagar: $\delta_1 = J_{\vec{F}_2}^T \delta_2$
> 4. Gradiente final: $\nabla_{\vec{w}_1} L = J_{\vec{F}_1}^T \delta_1$
> 
> **Ventaja:** Eficiencia computacional - calcular una vez las Jacobianas y reutilizarlas.

### Aplicación 5: Análisis de Sensibilidad

> [!example]- 📊 Propagación de Errores
> 
> **Problema:** Medir indirectamente una cantidad $\vec{y} = \vec{F}(\vec{x})$ con errores en $\vec{x}$.
> 
> ---
> 
> **Propagación lineal de errores:**
> 
> Si $\Delta \vec{x}$ es un error pequeño en la entrada:
> 
> $$\Delta \vec{y} \approx J_{\vec{F}}(\vec{x}) \Delta \vec{x}$$
> 
> ---
> 
> **Ejemplo:** Ley de gases ideales
> 
> $$P = \frac{nRT}{V}$$
> 
> Medir $P$ requiere medir $n$, $T$, y $V$.
> 
> **Función vectorial:** Si medimos $(T, V)$ para obtener $(P, E)$ (presión y energía):
> 
> $$\vec{F}(T, V) = \begin{bmatrix} \frac{nRT}{V} \ \frac{3}{2}nRT \end{bmatrix}$$
> 
> **Jacobiana:**
> 
> $$J_{\vec{F}} = \begin{bmatrix} \frac{nR}{V} & -\frac{nRT}{V^2} \[0.3em] \frac{3}{2}nR & 0 \end{bmatrix}$$
> 
> **Interpretación:**
> 
> - $\frac{\partial P}{\partial T} = \frac{nR}{V}$ : Sensibilidad de presión a temperatura
> - $\frac{\partial P}{\partial V} = -\frac{nRT}{V^2}$ : Sensibilidad de presión a volumen
> 
> Si los errores en $T$ y $V$ son $\Delta T$ y $\Delta V$:
> 
> $$\Delta P \approx \frac{nR}{V} \Delta T - \frac{nRT}{V^2} \Delta V$$

---

## 🧮 Algoritmo: Cálculo de la Jacobiana

> [!note]- 🔧 Procedimiento Sistemático
> 
> ### Método Directo
> 
> **Paso 1: Identificar componentes**
> 
> Escribir $\vec{F}(\vec{x})$ en componentes:
> 
> $$\vec{F}(x_1, \ldots, x_n) = \begin{bmatrix} F_1(x_1, \ldots, x_n) \ \vdots \ F_m(x_1, \ldots, x_n) \end{bmatrix}$$
> 
> ---
> 
> **Paso 2: Calcular derivadas parciales**
> 
> Para cada $i = 1, \ldots, m$ y $j = 1, \ldots, n$:
> 
> $$\frac{\partial F_i}{\partial x_j}$$
> 
> ---
> 
> **Paso 3: Formar la matriz**
> 
> $$J_{\vec{F}} = \begin{bmatrix} \frac{\partial F_1}{\partial x_1} & \cdots & \frac{\partial F_1}{\partial x_n} \ \vdots & \ddots & \vdots \ \frac{\partial F_m}{\partial x_1} & \cdots & \frac{\partial F_m}{\partial x_n} \end{bmatrix}$$
> 
> **Fila $i$** = gradiente de $F_i$
> 
> ---
> 
> **Paso 4: Simplificar**
> 
> Simplificar expresiones si es posible.
> 
> ---
> 
> **Paso 5: Evaluar en un punto (opcional)**
> 
> Si se requiere en un punto específico $\vec{a}$, sustituir:
> 
> $$J_{\vec{F}}(\vec{a})$$

---

## 📊 Tabla de Jacobianas Comunes

> [!note]- 📋 Transformaciones Estándar
> 
> |Transformación|Función|Jacobiana|Jacobiano|
> |---|---|---|---|
> |**Polares 2D**|$\begin{bmatrix} r\cos\theta \ r\sin\theta \end{bmatrix}$|$\begin{bmatrix} \cos\theta & -r\sin\theta \ \sin\theta & r\cos\theta \end{bmatrix}$|$r$|
> |**Cilíndricas**|$\begin{bmatrix} r\cos\theta \ r\sin\theta \ z \end{bmatrix}$|$\begin{bmatrix} \cos\theta & -r\sin\theta & 0 \ \sin\theta & r\cos\theta & 0 \ 0 & 0 & 1 \end{bmatrix}$|$r$|
> |**Esféricas**|$\begin{bmatrix} \rho\sin\phi\cos\theta \ \rho\sin\phi\sin\theta \ \rho\cos\phi \end{bmatrix}$|(ver Ejemplo 4)|$\rho^2\sin\phi$|
> |**Lineal**|$A\vec{x}$|$A$|$\det(A)$|
> |**Identidad**|$\vec{x}$|$I_n$|$1$|
> |**Rotación 2D**|$\begin{bmatrix} \cos\alpha & -\sin\alpha \ \sin\alpha & \cos\alpha \end{bmatrix}\begin{bmatrix} x \ y \end{bmatrix}$|$\begin{bmatrix} \cos\alpha & -\sin\alpha \ \sin\alpha & \cos\alpha \end{bmatrix}$|$1$|
> |**Escala**|$\begin{bmatrix} ax \ by \end{bmatrix}$|$\begin{bmatrix} a & 0 \ 0 & b \end{bmatrix}$|$ab$|

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Calcular Jacobianas:**
> 
> Calcular la matriz Jacobiana de cada función:
> 
> a) $\vec{F}(x,y) = \begin{bmatrix} x^2 \ y^2 \end{bmatrix}$
> 
> b) $\vec{F}(x,y) = \begin{bmatrix} 3x + 2y \ x - y \end{bmatrix}$
> 
> c) $\vec{F}(x,y,z) = \begin{bmatrix} x + y + z \ xyz \end{bmatrix}$
> 
> d) $\vec{F}(x,y) = \begin{bmatrix} e^x\cos y \ e^x\sin y \end{bmatrix}$
> 
> ---
> 
> **2. Evaluar en puntos:**
> 
> Para $\vec{F}(x,y) = \begin{bmatrix} x^2 - y^2 \ 2xy \end{bmatrix}$:
> 
> a) Calcular $J_{\vec{F}}(x,y)$
> 
> b) Evaluar $J_{\vec{F}}(1,0)$
> 
> c) Evaluar $J_{\vec{F}}(1,1)$
> 
> d) ¿Qué función reconoces? (Pista: función compleja)
> 
> ---
> 
> **3. Determinantes:**
> 
> Calcular el Jacobiano (determinante) de:
> 
> a) $\vec{F}(x,y) = \begin{bmatrix} 2x \ 3y \end{bmatrix}$
> 
> b) $\vec{F}(x,y) = \begin{bmatrix} x + y \ x - y \end{bmatrix}$
> 
> c) $\vec{F}(x,y) = \begin{bmatrix} x\cos\theta - y\sin\theta \ x\sin\theta + y\cos\theta \end{bmatrix}$ (rotación por ángulo $\theta$)

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Regla de la cadena:**
> 
> Sean $\vec{F}(x,y) = \begin{bmatrix} x^2 + y \ xy \end{bmatrix}$ y $\vec{G}(u,v) = \begin{bmatrix} u + v \ uv \ u - v \end{bmatrix}$
> 
> a) Calcular $J_{\vec{F}}$ y $J_{\vec{G}}$
> 
> b) Calcular $J_{\vec{G} \circ \vec{F}}$ usando la regla de la cadena
> 
> c) Verificar calculando $\vec{G} \circ \vec{F}$ explícitamente y luego su Jacobiana
> 
> ---
> 
> **5. Coordenadas elípticas:**
> 
> La transformación a coordenadas elípticas es:
> 
> $$\vec{F}(u,v) = \begin{bmatrix} a\cosh u \cos v \ b\sinh u \sin v \end{bmatrix}$$
> 
> a) Calcular $J_{\vec{F}}$
> 
> b) Calcular el Jacobiano $\det(J_{\vec{F}})$
> 
> c) Simplificar usando identidades hiperbólicas
> 
> ---
> 
> **6. Aproximación lineal:**
> 
> Para $\vec{F}(x,y) = \begin{bmatrix} e^{x+y} \ \sin(x)\cos(y) \end{bmatrix}$:
> 
> a) Calcular $J_{\vec{F}}(0,0)$
> 
> b) Usar la Jacobiana para aproximar $\vec{F}(0.1, 0.1)$
> 
> c) Comparar con el valor exacto

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **7. Teorema de la función inversa:**
> 
> Para $\vec{F}(x,y) = \begin{bmatrix} x^2 - y^2 \ 2xy \end{bmatrix}$:
> 
> a) Calcular $J_{\vec{F}}$ y su determinante
> 
> b) ¿En qué puntos es $\vec{F}$ localmente invertible?
> 
> c) Encontrar $J_{\vec{F}^{-1}}$ en el punto $(1,0)$ (donde $\vec{F}(1,0) = (1,0)$)
> 
> ---
> 
> **8. Cambio de variables:**
> 
> Usar coordenadas polares para calcular:
> 
> $$\iint_R x^2y , dA$$
> 
> donde $R$ es el disco $x^2 + y^2 \leq 4$ en el primer cuadrante.
> 
> a) Expresar en coordenadas polares
> 
> b) Incluir el Jacobiano
> 
> c) Evaluar la integral
> 
> ---
> 
> **9. Sistema no lineal:**
> 
> Aplicar una iteración del método de Newton para resolver:
> 
> $$\begin{cases} x^2 + y^2 = 4 \ xy = 1 \end{cases}$$
> 
> Con punto inicial $(x_0, y_0) = (1.5, 1.5)$
> 
> ---
> 
> **10. Funciones complejas:**
> 
> Una función compleja $f(z) = u(x,y) + iv(x,y)$ es diferenciable (holomorfa) si satisface las ecuaciones de Cauchy-Riemann:
> 
> $$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$
> 
> a) Para $\vec{F}(x,y) = \begin{bmatrix} u(x,y) \ v(x,y) \end{bmatrix}$, escribir $J_{\vec{F}}$ en términos de derivadas de $u$ y $v$
> 
> b) Demostrar que si $f$ satisface Cauchy-Riemann, entonces $\det(J_{\vec{F}}) = |\frac{\partial u}{\partial x}|^2 + |\frac{\partial u}{\partial y}|^2$
> 
> c) Verificar para $f(z) = z^2$

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $\vec{F}(x,y) = \begin{bmatrix} x^2 \ y^2 \end{bmatrix}$
> 
> $$J_{\vec{F}} = \begin{bmatrix} 2x & 0 \ 0 & 2y \end{bmatrix}$$
> 
> Matriz diagonal.
> 
> ---
> 
> **1b)** $\vec{F}(x,y) = \begin{bmatrix} 3x + 2y \ x - y \end{bmatrix}$
> 
> $$J_{\vec{F}} = \begin{bmatrix} 3 & 2 \ 1 & -1 \end{bmatrix}$$
> 
> Matriz constante (transformación lineal).
> 
> ---
> 
> **2a)** $\vec{F}(x,y) = \begin{bmatrix} x^2 - y^2 \ 2xy \end{bmatrix}$
> 
> $$J_{\vec{F}} = \begin{bmatrix} 2x & -2y \ 2y & 2x \end{bmatrix}$$
> 
> **2b)** En $(1,0)$:
> 
> $$J_{\vec{F}}(1,0) = \begin{bmatrix} 2 & 0 \ 0 & 2 \end{bmatrix} = 2I$$
> 
> **2d)** Esta es la función $f(z) = z^2$ en forma real (Cauchy-Riemann).
> 
> ---
> 
> **3c)** Rotación: $\vec{F}(x,y) = \begin{bmatrix} x\cos\theta - y\sin\theta \ x\sin\theta + y\cos\theta \end{bmatrix}$
> 
> $$J_{\vec{F}} = \begin{bmatrix} \cos\theta & -\sin\theta \ \sin\theta & \cos\theta \end{bmatrix}$$
> 
> $$\det(J_{\vec{F}}) = \cos^2\theta + \sin^2\theta = 1$$
> 
> Las rotaciones preservan áreas.

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **5b)** Coordenadas elípticas:
> 
> Después de calcular:
> 
> $$\det(J_{\vec{F}}) = ab(\cosh^2 u \sin^2 v + \sinh^2 u \cos^2 v)$$
> 
> Usando $\cosh^2 u - \sinh^2 u = 1$, esto se simplifica a:
> 
> $$\det(J_{\vec{F}}) = ab(\sinh^2 u + \sin^2 v)$$
> 
> ---
> 
> **6.** $\vec{F}(x,y) = \begin{bmatrix} e^{x+y} \ \sin x \cos y \end{bmatrix}$
> 
> **a)** En $(0,0)$:
> 
> $$J_{\vec{F}}(0,0) = \begin{bmatrix} 1 & 1 \ 1 & 0 \end{bmatrix}$$
> 
> **b)** Aproximación:
> 
> $$\vec{F}(0.1, 0.1) \approx \vec{F}(0,0) + J_{\vec{F}}(0,0)\begin{bmatrix} 0.1 \ 0.1 \end{bmatrix}$$
> $$= \begin{bmatrix} 1 \ 0 \end{bmatrix} + \begin{bmatrix} 1 & 1 \ 1 & 0 \end{bmatrix}\begin{bmatrix} 0.1 \ 0.1 \end{bmatrix}$$
> 
> $$= \begin{bmatrix} 1 \ 0 \end{bmatrix} + \begin{bmatrix} 0.2 \ 0.1 \end{bmatrix} = \begin{bmatrix} 1.2 \ 0.1 \end{bmatrix}$$
> 
> **c)** Valor exacto:
> 
> $$\vec{F}(0.1, 0.1) = \begin{bmatrix} e^{0.2} \ \sin(0.1)\cos(0.1) \end{bmatrix} \approx \begin{bmatrix} 1.2214 \ 0.0995 \end{bmatrix}$$
> 
> Error pequeño, la aproximación es buena cerca del origen.

> [!success]- 🔑 Respuestas Ejercicios Avanzados
> 
> **7.** $\vec{F}(x,y) = \begin{bmatrix} x^2 - y^2 \ 2xy \end{bmatrix}$
> 
> **a)** Jacobiana:
> 
> $$J_{\vec{F}} = \begin{bmatrix} 2x & -2y \ 2y & 2x \end{bmatrix}$$
> 
> Determinante:
> 
> $$\det(J_{\vec{F}}) = 4x^2 + 4y^2 = 4(x^2 + y^2)$$
> 
> **b)** $\vec{F}$ es localmente invertible cuando $\det(J_{\vec{F}}) \neq 0$
> 
> $$\boxed{(x,y) \neq (0,0)}$$
> 
> En todos los puntos excepto el origen.
> 
> **c)** En $(1,0)$:
> 
> $$J_{\vec{F}}(1,0) = \begin{bmatrix} 2 & 0 \ 0 & 2 \end{bmatrix}$$
> 
> Inversa:
> 
> $$J_{\vec{F}^{-1}}(\vec{F}(1,0)) = [J_{\vec{F}}(1,0)]^{-1} = \begin{bmatrix} 1/2 & 0 \ 0 & 1/2 \end{bmatrix}$$
> 
> ---
> 
> **8.** Integral en coordenadas polares:
> 
> **a)** Transformación:
> 
> $$x = r\cos\theta, \quad y = r\sin\theta$$
> 
> $$x^2y = r^2\cos^2\theta \cdot r\sin\theta = r^3\cos^2\theta\sin\theta$$
> 
> **b)** Región: $0 \leq r \leq 2$, $0 \leq \theta \leq \pi/2$
> 
> Jacobiano: $r$
> 
> **c)** Integral:
> 
> $$\int_0^{\pi/2}\int_0^2 r^3\cos^2\theta\sin\theta \cdot r , dr,d\theta$$
> 
> $$= \int_0^{\pi/2}\cos^2\theta\sin\theta , d\theta \int_0^2 r^4 , dr$$
> 
> Integral en $r$:
> 
> $$\int_0^2 r^4 , dr = \left[\frac{r^5}{5}\right]_0^2 = \frac{32}{5}$$
> 
> Integral en $\theta$ (sustitución $u = \cos\theta$):
> 
> $$\int_0^{\pi/2}\cos^2\theta\sin\theta , d\theta = \int_1^0 u^2 (-du) = \int_0^1 u^2 , du = \frac{1}{3}$$
> 
> **Resultado:**
> 
> $$\boxed{\frac{32}{5} \cdot \frac{1}{3} = \frac{32}{15}}$$
> 
> ---
> 
> **9.** Método de Newton:
> 
> $$\vec{F}(x,y) = \begin{bmatrix} x^2 + y^2 - 4 \ xy - 1 \end{bmatrix}$$
> 
> $$J_{\vec{F}} = \begin{bmatrix} 2x & 2y \ y & x \end{bmatrix}$$
> 
> En $(1.5, 1.5)$:
> 
> $$\vec{F}(1.5, 1.5) = \begin{bmatrix} 4.5 - 4 \ 2.25 - 1 \end{bmatrix} = \begin{bmatrix} 0.5 \ 1.25 \end{bmatrix}$$
> 
> $$J_{\vec{F}}(1.5, 1.5) = \begin{bmatrix} 3 & 3 \ 1.5 & 1.5 \end{bmatrix}$$
> 
> Resolver:
> 
> $$\begin{bmatrix} 3 & 3 \ 1.5 & 1.5 \end{bmatrix}\begin{bmatrix} \Delta x \ \Delta y \end{bmatrix} = -\begin{bmatrix} 0.5 \ 1.25 \end{bmatrix}$$
> 
> Usando eliminación o matriz inversa:
> 
> (La matriz es singular - método falla. Necesitamos mejor punto inicial)

---

## 🌟 Conceptos Clave para Recordar

> [!tip]- 💡 Puntos Esenciales
> 
> ### Sobre la Matriz Jacobiana
> 
> ✅ **Definición:**
> 
> - Matriz de todas las derivadas parciales
> - Fila $i$ = gradiente de la componente $F_i$
> - Columna $j$ = derivadas de todas las componentes respecto a $x_j$
> - Dimensión: $m \times n$ (outputs × inputs)
> 
> ✅ **Interpretación:**
> 
> - **Mejor aproximación lineal** de una función vectorial
> - Describe cómo cambian múltiples outputs con múltiples inputs
> - Generalización natural de la derivada
> 
> ✅ **Casos especiales:**
> 
> - Función escalar: Jacobiana = gradiente transpuesto ($1 \times n$)
> - Transformación lineal: Jacobiana = matriz de la transformación
> - Función identidad: Jacobiana = matriz identidad
> 
> ---
> 
> ### El Jacobiano (Determinante)
> 
> ✅ **Para funciones cuadradas ($n \times n$):**
> 
> - Mide **cambio de volumen** local
> - Aparece en cambio de variables en integrales
> - Determina invertibilidad local
> 
> ✅ **Valores importantes:**
> 
> - $|\det(J)| > 1$ : Expansión
> - $|\det(J)| < 1$ : Contracción
> - $\det(J) = 0$ : Singularidad (no invertible)
> - $\det(J) < 0$ : Inversión de orientación
> 
> ---
> 
> ### Regla de la Cadena
> 
> ✅ **Composición:**
> 
> - $J_{\vec{G} \circ \vec{F}} = J_{\vec{G}}(\vec{F}(\vec{x})) \cdot J_{\vec{F}}(\vec{x})$
> - Producto de matrices (orden importa)
> - Dimensiones deben ser compatibles
> 
> ---
> 
> ### Aplicaciones Clave
> 
> ✅ **Cambio de variables:**
> 
> - Factor de corrección en integrales múltiples
> - Coordenadas polares, cilíndricas, esféricas
> 
> ✅ **Optimización:**
> 
> - Método de Newton para sistemas
> - Gradiente descendente en ML
> 
> ✅ **Análisis:**
> 
> - Teorema de la función inversa
> - Teorema de la función implícita
> - Propagación de errores

---

## 🔗 Relaciones Importantes

> [!quote]- 🌐 Conexiones con Otros Temas
> 
> ### Prerequisitos:
> 
> - **[[08 - Derivadas Parciales]]** - Componentes de la Jacobiana
> - **[[09 - Derivada Direccional]]** - Caso especial: $D_{\vec{u}}f = J_f \cdot \vec{u}$
> - **[[10 - Diferenciabilidad]]** - Condición necesaria
> - **[[11 - Gradiente]]** - Fila de la Jacobiana para funciones escalares
> - **Álgebra Lineal: Matrices** - Operaciones matriciales
> - **Álgebra Lineal: Determinantes** - Jacobiano
> 
> ### Este tema es prerequisito para:
> 
> - **[[13 - Teorema de la Función Implícita]]** - Usa rango de la Jacobiana
> - **[[14 - Teorema de la Función Inversa]]** - Requiere Jacobiano no nulo
> - **[[15 - Multiplicadores de Lagrange]]** - Condiciones usando Jacobianas
> - **[[16 - Integrales Múltiples]]** - Cambio de variables
> - **[[17 - Teoremas Integrales]]** - Green, Stokes, Gauss
> - **Optimización Numérica** - Métodos de Newton
> - **Ecuaciones Diferenciales** - Sistemas no lineales
> 
> ### Conceptos relacionados:
> 
> - **Gradiente** - Caso $m=1$: $J_f = \nabla f^T$
> - **Hessiana** - Jacobiana del gradiente (segundas derivadas)
> - **Diferencial Total** - $d\vec{F} = J_{\vec{F}} \cdot d\vec{x}$
> - **Transformaciones Lineales** - Jacobiana constante
> - **Difeomorfismos** - Jacobiano siempre no nulo
> - **Rango de Matrices** - Dimensión de la imagen
> 
> ### Diagrama de Flujo:
> 
> ```
> Derivadas Parciales
>          ↓
>      Gradiente
>          ↓
>   Matriz Jacobiana
>          ↓
>     ┌────┴────┐
>     ↓         ↓
> Jacobiano   Regla de la Cadena
>     ↓         ↓
> Cambio de   Función Inversa
> Variables   Función Implícita
> ```
> 
> ### Siguiente tema recomendado:
> 
> **[[13 - Teorema de la Función Implícita]]** - Aplicación profunda de la Jacobiana

---

## 📊 Mapa Conceptual

> [!note]- 🌳 Árbol de Conceptos
> 
> ```
> MATRIZ JACOBIANA
> │
> ├─ DEFINICIÓN
> │  ├─ Matriz de derivadas parciales
> │  ├─ Dimensión: m × n (outputs × inputs)
> │  ├─ Fila i = ∇Fᵢᵀ
> │  └─ Columna j = derivadas respecto a xⱼ
> │
> ├─ CASOS ESPECIALES
> │  ├─ Función escalar: J = ∇f ᵀ (1 × n)
> │  ├─ Curva: J = F'(t) (m × 1)
> │  ├─ Transformación lineal: J = A (constante)
> │  └─ Función cuadrada: J tiene determinante
> │
> ├─ INTERPRETACIÓN
> │  ├─ Aproximación lineal local
> │  ├─ Transformación de vectores tangentes
> │  ├─ Matriz de sensibilidad
> │  └─ Diferencial: dF = J·dx
> │
> ├─ JACOBIANO (DETERMINANTE)
> │  ├─ Solo para funciones n → n
> │  ├─ Factor de cambio de volumen
> │  ├─ Criterio de invertibilidad
> │  └─ Cambio de variables en integrales
> │
> ├─ PROPIEDADES
> │  ├─ Linealidad: J(aF + bG) = aJ_F + bJ_G
> │  ├─ Regla de la cadena: J(G∘F) = J_G · J_F
> │  ├─ Función inversa: J(F⁻¹) = (J_F)⁻¹
> │  └─ Continuidad si F ∈ C¹
> │
> ├─ APLICACIONES
> │  ├─ Cambio de coordenadas
> │  │  ├─ Polares, cilíndricas, esféricas
> │  │  └─ Integrales múltiples
> │  ├─ Optimización numérica
> │  │  ├─ Método de Newton
> │  │  └─ Gradiente descendente
> │  ├─ Análisis de sensibilidad
> │  │  └─ Propagación de errores
> │  ├─ Robótica
> │  │  └─ Cinemática inversa
> │  └─ Machine Learning
> │     └─ Backpropagation
> │
> └─ TEOREMAS RELACIONADOS
>    ├─ Teorema de la función inversa
>    ├─ Teorema de la función implícita
>    └─ Teorema del cambio de variables
> ```

---

## ✨ Comentarios Finales

> [!note]- 🎓 Para Llevar
> 
> ### Lo Esencial
> 
> 1. **La Jacobiana es la derivada de funciones vectoriales**
>     - Generaliza gradiente (escalar) y derivada (1D)
>     - Matriz de todas las derivadas parciales
>     - Herramienta fundamental del cálculo multivariable
> 2. **Dos roles principales:**
>     - **Aproximación lineal:** $\vec{F}(\vec{a} + \vec{h}) \approx \vec{F}(\vec{a}) + J_{\vec{F}}(\vec{a})\vec{h}$
>     - **Cambio de variables:** Factor de corrección en integrales
> 3. **El determinante es crucial:**
>     - Mide cambio de volumen
>     - Determina invertibilidad local
>     - Aparece en todas las integrales con cambio de variables
> 4. **Regla de la cadena matricial:**
>     - Composición → producto de Jacobianas
>     - Orden importa (no conmutativo)
>     - Base de backpropagation en ML
> 5. **Ubicuidad en aplicaciones:**
>     - Física: transformaciones de coordenadas
>     - Ingeniería: análisis de sensibilidad
>     - Computación: optimización numérica
>     - Machine Learning: entrenamiento de redes
> 
> ---
> 
> ### Conexión con Álgebra Lineal
> 
> La Jacobiana es donde el **cálculo** y el **álgebra lineal** se encuentran:
> 
> - **Cálculo:** Derivadas y tasas de cambio
> - **Álgebra Lineal:** Matrices y transformaciones lineales
> - **Síntesis:** Aproximación lineal local de funciones no lineales
> 
> "Localmente, toda función suave se comporta linealmente"
> 
> ---
> 
> ### Estrategia de Cálculo
> 
> **Para calcular Jacobianas:**
> 
> 1. ✅ Identificar componentes de $\vec{F}$
> 2. ✅ Calcular derivadas parciales sistemáticamente
> 3. ✅ Organizar en matriz (filas = componentes)
> 4. ✅ Simplificar expresiones
> 5. ✅ Verificar dimensiones: $m \times n$
> 
> **Errores comunes:**
> 
> - ❌ Confundir filas con columnas
> - ❌ Olvidar normalizar vectores (en direcciones)
> - ❌ Invertir orden en la regla de la cadena
> - ❌ Olvidar el valor absoluto del Jacobiano en integrales
> 
> ---
> 
> ### Próximos Pasos
> 
> Con la Jacobiana dominada, estás listo para:
> 
> - **Teorema de la Función Implícita:** Despejar variables usando Jacobianas
> - **Teorema de la Función Inversa:** Invertibilidad local
> - **Integrales Múltiples:** Cambio de variables con Jacobiano
> - **Optimización Avanzada:** Métodos de Newton y quasi-Newton
> - **Ecuaciones Diferenciales:** Sistemas no lineales y estabilidad
> 
> ---
> 
> ### Reflexión Final
> 
> La matriz Jacobiana es uno de los conceptos más poderosos del cálculo:
> 
> - **Unifica:** Conecta todos los tipos de derivadas
> - **Simplifica:** Convierte problemas complejos en álgebra lineal
> - **Generaliza:** Extiende ideas de 1D a dimensiones arbitrarias
> - **Aplica:** Aparece en todas las áreas de ciencia e ingeniería
> 
> **Mensaje clave:** Si entiendes la Jacobiana, entiendes cómo funciones complejas se comportan localmente como transformaciones lineales. Esta es la esencia del cálculo avanzado y la base de toda la matemática aplicada moderna.
> 
> **Analogía final:**
> 
> - Derivada (1D) = pendiente de una curva
> - Gradiente = vector de pendientes
> - **Jacobiana = matriz de todas las pendientes posibles**
> 
> Es la herramienta más completa para entender el cambio en sistemas multidimensionales.

---

## 📖 Fórmulas de Referencia Rápida

> [!note]- 📋 Resumen de Fórmulas
> 
> ### Definición General
> 
> $$J_{\vec{F}} = \begin{bmatrix} \frac{\partial F_1}{\partial x_1} & \cdots & \frac{\partial F_1}{\partial x_n} \ \vdots & \ddots & \vdots \ \frac{\partial F_m}{\partial x_1} & \cdots & \frac{\partial F_m}{\partial x_n} \end{bmatrix}_{m \times n}$$
> 
> ### Casos Especiales
> 
> |Caso|Dimensión|Fórmula|
> |---|---|---|
> |Función escalar|$1 \times n$|$J_f = \nabla f^T$|
> |Curva|$m \times 1$|$J_{\vec{r}} = \vec{r}'(t)$|
> |Transformación lineal|$m \times n$|$J_{A\vec{x}} = A$|
> 
> ### Regla de la Cadena
> 
> $$J_{\vec{H}}(\vec{x}) = J_{\vec{G}}(\vec{F}(\vec{x})) \cdot J_{\vec{F}}(\vec{x})$$
> 
> ### Jacobiano
> 
> $$\mathcal{J}_{\vec{F}} = \det(J_{\vec{F}}) \quad \text{(solo para } n \times n\text{)}$$
> 
> ### Cambio de Variables
> 
> $$\int_V f(\vec{y}) , d\vec{y} = \int_U f(\vec{F}(\vec{x})) |\mathcal{J}_{\vec{F}}(\vec{x})| , d\vec{x}$$
> 
> ### Función Inversa
> 
> $$J_{\vec{F}^{-1}}(\vec{F}(\vec{a})) = [J_{\vec{F}}(\vec{a})]^{-1}$$
> 
> ### Aproximación Lineal
> 
> $$\vec{F}(\vec{a} + \vec{h}) \approx \vec{F}(\vec{a}) + J_{\vec{F}}(\vec{a})\vec{h}$$

---

**Tags:** #calculo-multivariable #matriz-jacobiana #derivadas-parciales #transformaciones #cambio-variables #regla-cadena #jacobiano #determinante #optimizacion #integrales-multiples #funciones-vectoriales #analisis-vectorial #diferenciabilidad