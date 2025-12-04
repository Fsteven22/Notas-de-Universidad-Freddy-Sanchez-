# 📘 Matriz Hessiana

## 🎯 Introducción

> [!info]- 💡 ¿Por qué es importante la Matriz Hessiana?
> 
> La **matriz hessiana** es una herramienta fundamental que generaliza la segunda derivada a funciones de varias variables, permitiéndonos analizar la **curvatura** de superficies y determinar la naturaleza de puntos críticos.
> 
> **Importancia práctica:**
> 
> - **Optimización:** Clasificar máximos, mínimos y puntos de silla
> - **Física:** Análisis de estabilidad en sistemas dinámicos
> - **Economía:** Estudiar concavidad/convexidad de funciones de utilidad
> - **Machine Learning:** Métodos de segundo orden en optimización
> - **Geometría:** Caracterizar curvatura de superficies
> 
> **Analogía con una variable:**
> 
> - En $f(x)$: la segunda derivada $f''(x)$ indica concavidad
> - En $f(x,y)$: la **matriz hessiana** $H_f$ captura información de curvatura en **todas las direcciones**
> - En $f(x,y,z)$: la hessiana extiende este análisis al espacio 3D
> 
> **Nueva dimensión:** La matriz hessiana es una matriz **simétrica** que contiene todas las segundas derivadas parciales, revelando cómo la función se curva en múltiples direcciones simultáneamente.

---

## 🔍 Definición de la Matriz Hessiana

### 📐 Definición Formal

> [!example]- 🟢 Definición: Matriz Hessiana
> 
> **Definición formal:** Sea $f: D \subseteq \mathbb{R}^n \to \mathbb{R}$ una función con segundas derivadas parciales continuas. La **matriz hessiana** de $f$ en un punto $(x_0, y_0, \ldots)$ es la matriz cuadrada de orden $n$ definida por:
> 
> $$H_f(x_0, y_0, \ldots) = \begin{pmatrix} \frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \ \frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \cdots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \ \vdots & \vdots & \ddots & \vdots \ \frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \cdots & \frac{\partial^2 f}{\partial x_n^2} \end{pmatrix}$$
> 
> evaluada en $(x_0, y_0, \ldots)$.
> 
> **Notación compacta:**
> 
> $$H_f = \left[\frac{\partial^2 f}{\partial x_i \partial x_j}\right]_{i,j=1}^n$$
> 
> ---
> 
> **Para dos variables** $(x, y)$:
> 
> $$H_f(x,y) = \begin{pmatrix} f_{xx} & f_{xy} \ f_{yx} & f_{yy} \end{pmatrix} = \begin{pmatrix} \frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \ \frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2} \end{pmatrix}$$
> 
> ---
> 
> **Para tres variables** $(x, y, z)$:
> 
> $$H_f(x,y,z) = \begin{pmatrix} f_{xx} & f_{xy} & f_{xz} \ f_{yx} & f_{yy} & f_{yz} \ f_{zx} & f_{zy} & f_{zz} \end{pmatrix}$$
> 
> ---
> 
> **Elementos de la matriz:**
> 
> - **Diagonal principal:** segundas derivadas parciales "puras" ($f_{xx}$, $f_{yy}$, $f_{zz}$)
> - **Fuera de la diagonal:** derivadas parciales mixtas ($f_{xy}$, $f_{xz}$, $f_{yz}$)

### 🎯 Propiedades Fundamentales

> [!note]- 📊 Propiedades de la Matriz Hessiana
> 
> ### 1. Simetría (Teorema de Schwarz)
> 
> Si las segundas derivadas parciales son **continuas**, entonces:
> 
> $$\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial^2 f}{\partial x_j \partial x_i}$$
> 
> Por lo tanto, la matriz hessiana es **simétrica**: $H_f = H_f^T$
> 
> **Consecuencia:** Solo necesitamos calcular $\frac{n(n+1)}{2}$ derivadas (no $n^2$)
> 
> - Para $n=2$: 3 derivadas en lugar de 4
> - Para $n=3$: 6 derivadas en lugar de 9
> 
> ---
> 
> ### 2. Valores y Vectores Propios
> 
> Como $H_f$ es simétrica y real:
> 
> - Todos los **valores propios** son **reales**
> - Los **vectores propios** correspondientes a valores propios distintos son **ortogonales**
> - $H_f$ es **diagonalizable**
> 
> **Importancia:** Los valores propios determinan la curvatura en direcciones principales
> 
> ---
> 
> ### 3. Definición Positiva/Negativa
> 
> Sea $\lambda_1, \lambda_2, \ldots, \lambda_n$ los valores propios de $H_f$.
> 
> **Definida positiva:** Todos $\lambda_i > 0$
> 
> - La función es **convexa** (localmente)
> - El punto crítico es un **mínimo local**
> 
> **Definida negativa:** Todos $\lambda_i < 0$
> 
> - La función es **cóncava** (localmente)
> - El punto crítico es un **máximo local**
> 
> **Indefinida:** Algunos $\lambda_i > 0$, otros $\lambda_i < 0$
> 
> - El punto crítico es un **punto de silla**
> 
> **Semidefinida:** Algún $\lambda_i = 0$
> 
> - Caso **no concluyente** (requiere análisis adicional)
> 
> ---
> 
> ### 4. Determinante y Traza
> 
> **Determinante:**
> 
> $$\det(H_f) = \prod_{i=1}^n \lambda_i$$
> 
> (producto de valores propios)
> 
> **Traza:**
> 
> $$\text{tr}(H_f) = \sum_{i=1}^n \lambda_i = \sum_{i=1}^n f_{x_i x_i}$$
> 
> (suma de valores propios = suma de elementos diagonales)
> 
> ---
> 
> ### 5. Invariancia
> 
> La **naturaleza** de un punto crítico (máximo, mínimo, silla) es **independiente** del sistema de coordenadas, aunque la representación matricial de $H_f$ cambie.

---

## 📚 Casos Específicos por Dimensión

### Caso 1: Funciones de Dos Variables

> [!example]- 📊 Hessiana en $\mathbb{R}^2$
> 
> **Función:** $f(x,y)$
> 
> **Matriz hessiana:**
> 
> $$H_f(x,y) = \begin{pmatrix} f_{xx}(x,y) & f_{xy}(x,y) \ f_{xy}(x,y) & f_{yy}(x,y) \end{pmatrix}$$
> 
> _(Nota: $f_{xy} = f_{yx}$ por simetría)_
> 
> ---
> 
> ### Discriminante (Criterio de la Segunda Derivada)
> 
> En un punto crítico $(x_0, y_0)$, definimos:
> 
> $$D = \det(H_f) = f_{xx} \cdot f_{yy} - (f_{xy})^2$$
> 
> **Clasificación del punto crítico:**
> 
> |Condición|Tipo de Punto|
> |---|---|
> |$D > 0$ y $f_{xx} > 0$|**Mínimo local**|
> |$D > 0$ y $f_{xx} < 0$|**Máximo local**|
> |$D < 0$|**Punto de silla**|
> |$D = 0$|**Caso no concluyente**|
> 
> **Interpretación geométrica:**
> 
> - $D > 0$: curvatura con el mismo signo en todas direcciones → extremo
> - $D < 0$: curvatura positiva en una dirección, negativa en otra → silla
> - $D = 0$: curvatura "degenerada" → requiere análisis de orden superior
> 
> ---
> 
> ### Valores Propios en 2D
> 
> Los valores propios de $H_f$ son:
> 
> $$\lambda = \frac{(f_{xx} + f_{yy}) \pm \sqrt{(f_{xx} - f_{yy})^2 + 4f_{xy}^2}}{2}$$
> 
> **Relación con el discriminante:**
> 
> - $D > 0 \iff$ ambos valores propios tienen el mismo signo
> - $D < 0 \iff$ valores propios tienen signos opuestos
> - $D = 0 \iff$ al menos un valor propio es cero

### Caso 2: Funciones de Tres Variables

> [!example]- 📊 Hessiana en $\mathbb{R}^3$
> 
> **Función:** $f(x,y,z)$
> 
> **Matriz hessiana:**
> 
> $$H_f(x,y,z) = \begin{pmatrix} f_{xx} & f_{xy} & f_{xz} \ f_{xy} & f_{yy} & f_{yz} \ f_{xz} & f_{yz} & f_{zz} \end{pmatrix}$$
> 
> _(Matriz simétrica de $3 \times 3$)_
> 
> ---
> 
> ### Criterio de Sylvester (Menores Principales)
> 
> Para clasificar un punto crítico en 3D, calculamos los **menores principales**:
> 
> **Primer menor:**
> 
> $$D_1 = f_{xx}$$
> 
> **Segundo menor:**
> 
> $$D_2 = \begin{vmatrix} f_{xx} & f_{xy} \ f_{xy} & f_{yy} \end{vmatrix} = f_{xx} f_{yy} - f_{xy}^2$$
> 
> **Tercer menor (determinante completo):**
> 
> $$D_3 = \det(H_f) = \begin{vmatrix} f_{xx} & f_{xy} & f_{xz} \ f_{xy} & f_{yy} & f_{yz} \ f_{xz} & f_{yz} & f_{zz} \end{vmatrix}$$
> 
> ---
> 
> ### Clasificación
> 
> |Condición|Tipo de Punto|
> |---|---|
> |$D_1 > 0$, $D_2 > 0$, $D_3 > 0$|**Mínimo local**|
> |$D_1 < 0$, $D_2 > 0$, $D_3 < 0$|**Máximo local**|
> |Signos alternados en otros patrones|**Punto de silla**|
> |Algún $D_i = 0$|**No concluyente**|
> 
> **Regla mnemotécnica:**
> 
> - **Mínimo:** todos positivos
> - **Máximo:** signos alternados empezando por negativo ($-, +, -$)
> - **Silla:** cualquier otra combinación (excepto ceros)

---

## 🧮 Ejemplos Detallados

### Ejemplo 1: Función Cuadrática Simple

> [!example]- 📝 Ejemplo 1: Paraboloide Elíptico
> 
> **Función:** $$f(x,y) = x^2 + 2y^2$$
> 
> **Paso 1: Calcular primeras derivadas**
> 
> $$f_x = 2x, \quad f_y = 4y$$
> 
> **Punto crítico:** $\nabla f = (0,0) \implies (x,y) = (0,0)$
> 
> ---
> 
> **Paso 2: Calcular segundas derivadas**
> 
> $$f_{xx} = 2, \quad f_{yy} = 4, \quad f_{xy} = 0$$
> 
> ---
> 
> **Paso 3: Construir la hessiana**
> 
> $$H_f(0,0) = \begin{pmatrix} 2 & 0 \ 0 & 4 \end{pmatrix}$$
> 
> ---
> 
> **Paso 4: Calcular el discriminante**
> 
> $$D = f_{xx} \cdot f_{yy} - (f_{xy})^2 = 2 \cdot 4 - 0^2 = 8 > 0$$
> 
> Como $D > 0$ y $f_{xx} = 2 > 0$:
> 
> **Conclusión:** $(0,0)$ es un **mínimo local** ✓
> 
> ---
> 
> **Verificación con valores propios:**
> 
> La hessiana es diagonal, así que los valores propios son:
> 
> $$\lambda_1 = 2 > 0, \quad \lambda_2 = 4 > 0$$
> 
> Ambos positivos → **mínimo local** ✓
> 
> ---
> 
> **Interpretación geométrica:**
> 
> La función $f(x,y) = x^2 + 2y^2$ es un paraboloide que abre hacia arriba, con:
> 
> - Curvatura en dirección $x$: $\lambda_1 = 2$
> - Curvatura en dirección $y$: $\lambda_2 = 4$ (más pronunciada)
> - El punto $(0,0)$ está en el fondo del "cuenco"

### Ejemplo 2: Punto de Silla

> [!example]- 📝 Ejemplo 2: Silla de Montar
> 
> **Función:** $$f(x,y) = x^2 - y^2$$
> 
> **Paso 1: Punto crítico**
> 
> $$f_x = 2x = 0, \quad f_y = -2y = 0$$
> 
> Punto crítico: $(0,0)$
> 
> ---
> 
> **Paso 2: Segundas derivadas**
> 
> $$f_{xx} = 2, \quad f_{yy} = -2, \quad f_{xy} = 0$$
> 
> ---
> 
> **Paso 3: Matriz hessiana**
> 
> $$H_f(0,0) = \begin{pmatrix} 2 & 0 \ 0 & -2 \end{pmatrix}$$
> 
> ---
> 
> **Paso 4: Discriminante**
> 
> $$D = 2 \cdot (-2) - 0^2 = -4 < 0$$
> 
> **Conclusión:** Como $D < 0$, el punto $(0,0)$ es un **punto de silla** ✓
> 
> ---
> 
> **Valores propios:**
> 
> $$\lambda_1 = 2 > 0, \quad \lambda_2 = -2 < 0$$
> 
> Signos opuestos → **punto de silla** ✓
> 
> ---
> 
> **Interpretación:**
> 
> - En dirección $x$: la función es cóncava hacia arriba (mínimo)
> - En dirección $y$: la función es cóncava hacia abajo (máximo)
> - El punto $(0,0)$ es como un **puerto de montaña**: mínimo en una dirección, máximo en otra

### Ejemplo 3: Función con Derivadas Mixtas

> [!example]- 📝 Ejemplo 3: Función con Acoplamiento
> 
> **Función:** $$f(x,y) = x^2 + xy + y^2$$
> 
> **Paso 1: Punto crítico**
> 
> $$f_x = 2x + y = 0$$ $$f_y = x + 2y = 0$$
> 
> De la primera: $y = -2x$  
> Sustituyendo: $x + 2(-2x) = x - 4x = -3x = 0$
> 
> Punto crítico: $(0,0)$
> 
> ---
> 
> **Paso 2: Segundas derivadas**
> 
> $$f_{xx} = 2, \quad f_{yy} = 2, \quad f_{xy} = 1$$
> 
> ---
> 
> **Paso 3: Matriz hessiana**
> 
> $$H_f(0,0) = \begin{pmatrix} 2 & 1 \ 1 & 2 \end{pmatrix}$$
> 
> ---
> 
> **Paso 4: Discriminante**
> 
> $$D = 2 \cdot 2 - 1^2 = 4 - 1 = 3 > 0$$
> 
> Como $D > 0$ y $f_{xx} = 2 > 0$:
> 
> **Conclusión:** $(0,0)$ es un **mínimo local** ✓
> 
> ---
> 
> **Valores propios:**
> 
> Ecuación característica: $\det(H_f - \lambda I) = 0$
> 
> $$\begin{vmatrix} 2-\lambda & 1 \ 1 & 2-\lambda \end{vmatrix} = (2-\lambda)^2 - 1 = 0$$
> 
> $$(2-\lambda)^2 = 1$$ $$2-\lambda = \pm 1$$
> 
> $$\lambda_1 = 1, \quad \lambda_2 = 3$$
> 
> Ambos positivos → **mínimo local** ✓
> 
> ---
> 
> **Interpretación:**
> 
> La función tiene curvatura positiva en todas direcciones, pero la derivada mixta $f_{xy} = 1$ indica que las variables están "acopladas". Las direcciones principales de curvatura no son los ejes coordenados, sino direcciones rotadas a $45°$.

### Ejemplo 4: Función en Tres Variables

> [!example]- 📝 Ejemplo 4: Caso 3D
> 
> **Función:** $$f(x,y,z) = x^2 + y^2 + z^2 - xy - xz$$
> 
> **Paso 1: Punto crítico**
> 
> $$\nabla f = (2x - y - z, 2y - x, 2z - x) = (0,0,0)$$
> 
> Sistema: $$2x - y - z = 0$$ $$2y - x = 0 \implies x = 2y$$ $$2z - x = 0 \implies x = 2z$$
> 
> De las últimas dos: $2y = 2z \implies y = z$
> 
> Sustituyendo en la primera: $$2(2y) - y - y = 4y - 2y = 2y = 0$$
> 
> Por lo tanto: $y = z = 0$ y $x = 0$
> 
> Punto crítico: $(0,0,0)$
> 
> ---
> 
> **Paso 2: Segundas derivadas**
> 
> $$f_{xx} = 2, \quad f_{yy} = 2, \quad f_{zz} = 2$$ $$f_{xy} = -1, \quad f_{xz} = -1, \quad f_{yz} = 0$$
> 
> ---
> 
> **Paso 3: Matriz hessiana**
> 
> $$H_f(0,0,0) = \begin{pmatrix} 2 & -1 & -1 \ -1 & 2 & 0 \ -1 & 0 & 2 \end{pmatrix}$$
> 
> ---
> 
> **Paso 4: Menores principales**
> 
> **Primer menor:** $$D_1 = 2 > 0$$ ✓
> 
> **Segundo menor:** $$D_2 = \begin{vmatrix} 2 & -1 \ -1 & 2 \end{vmatrix} = 4 - 1 = 3 > 0$$ ✓
> 
> **Tercer menor:** $$D_3 = \begin{vmatrix} 2 & -1 & -1 \ -1 & 2 & 0 \ -1 & 0 & 2 \end{vmatrix}$$
> 
> Expandiendo por la primera fila: $$D_3 = 2\begin{vmatrix} 2 & 0 \ 0 & 2 \end{vmatrix} - (-1)\begin{vmatrix} -1 & 0 \ -1 & 2 \end{vmatrix} + (-1)\begin{vmatrix} -1 & 2 \ -1 & 0 \end{vmatrix}$$
> 
> $$= 2(4) + 1(-2) - 1(0 - (-2))$$ $$= 8 - 2 - 2 = 4 > 0$$ ✓
> 
> ---
> 
> **Conclusión:** Como $D_1 > 0$, $D_2 > 0$, $D_3 > 0$:
> 
> El punto $(0,0,0)$ es un **mínimo local** ✓

### Ejemplo 5: Caso No Concluyente

> [!example]- 📝 Ejemplo 5: Discriminante Nulo
> 
> **Función:** $$f(x,y) = x^4 + y^4$$
> 
> **Paso 1: Punto crítico**
> 
> $$f_x = 4x^3 = 0 \implies x = 0$$ $$f_y = 4y^3 = 0 \implies y = 0$$
> 
> Punto crítico: $(0,0)$
> 
> ---
> 
> **Paso 2: Segundas derivadas en $(0,0)$**
> 
> $$f_{xx} = 12x^2 \bigg|_{(0,0)} = 0$$ $$f_{yy} = 12y^2 \bigg|_{(0,0)} = 0$$ $$f_{xy} = 0$$
> 
> ---
> 
> **Paso 3: Matriz hessiana**
> 
> $$H_f(0,0) = \begin{pmatrix} 0 & 0 \ 0 & 0 \end{pmatrix}$$
> 
> ---
> 
> **Paso 4: Discriminante**
> 
> $$D = 0 \cdot 0 - 0^2 = 0$$
> 
> **Problema:** El criterio de la segunda derivada es **no concluyente** ❌
> 
> ---
> 
> **Paso 5: Análisis directo**
> 
> Observemos que: $$f(x,y) = x^4 + y^4 \geq 0$$
> 
> para todo $(x,y)$, con igualdad solo en $(0,0)$.
> 
> **Conclusión:** A pesar de que $D = 0$, por análisis directo sabemos que $(0,0)$ es un **mínimo global** ✓
> 
> ---
> 
> **Lección:** Cuando $D = 0$, el criterio de la segunda derivada falla y debemos usar otros métodos (análisis directo, derivadas de orden superior, etc.)

### Ejemplo 6: Función Racional

> [!example]- 📝 Ejemplo 6: Optimización con Hessiana
> 
> **Función:** $$f(x,y) = x^2 + y^2 + \frac{4}{xy}$$
> 
> **Dominio:** $x \neq 0$, $y \neq 0$
> 
> **Paso 1: Puntos críticos**
> 
> $$f_x = 2x - \frac{4}{x^2y} = 0$$ $$f_y = 2y - \frac{4}{xy^2} = 0$$
> 
> De la primera: $2x = \frac{4}{x^2y} \implies 2x^3y = 4 \implies x^3y = 2$
> 
> De la segunda: $2y = \frac{4}{xy^2} \implies 2xy^3 = 4 \implies xy^3 = 2$
> 
> Dividiendo: $$\frac{x^3y}{xy^3} = \frac{2}{2} = 1 \implies \frac{x^2}{y^2} = 1 \implies x^2 = y^2$$
> 
> Como buscamos en el primer cuadrante (por simetría), tomamos $x = y$.
> 
> Sustituyendo en $x^3y = 2$: $$x^4 = 2 \implies x = 2^{1/4} = \sqrt[4]{2}$$
> 
> Punto crítico: $(\sqrt[4]{2}, \sqrt[4]{2})$
> 
> ---
> 
> **Paso 2: Segundas derivadas**
> 
> $$f_{xx} = 2 + \frac{8}{x^3y}$$ $$f_{yy} = 2 + \frac{8}{xy^3}$$ $$f_{xy} = \frac{4}{x^2y^2}$$
> 
> ---
> 
> **Paso 3: Evaluar en el punto crítico**
> 
> Sea $a = \sqrt[4]{2}$, entonces en $(a,a)$:
> 
> $$f_{xx} = 2 + \frac{8}{a^4} = 2 + \frac{8}{2} = 6$$ $$f_{yy} = 6$$ (por simetría) $$f_{xy} = \frac{4}{a^4} = \frac{4}{2} = 2$$
> 
> $$H_f(a,a) = \begin{pmatrix} 6 & 2 \ 2 & 6 \end{pmatrix}$$
> 
> ---
> 
> **Paso 4: Discriminante**
> 
> $$D = 6 \cdot 6 - 2^2 = 36 - 4 = 32 > 0$$
> 
> Como $D > 0$ y $f_{xx} = 6 > 0$:
> 
> **Conclusión:** $(\sqrt[4]{2}, \sqrt[4]{2})$ es un **mínimo local** ✓

---

## 🎯 Criterio de Sylvester (Generalización)

> [!note]- 📐 Criterio para $n$ Variables
> 
> Para una función $f: \mathbb{R}^n \to \mathbb{R}$ con matriz hessiana $H_f$, definimos los **menores principales líderes**:
> 
> $$D_1 = f_{x_1 x_1}$$
> 
> $$D_2 = \begin{vmatrix} f_{x_1 x_1} & f_{x_1 x_2} \ f_{x_2 x_1} & f_{x_2 x_2} \end{vmatrix}$$
> 
> $$D_3 = \begin{vmatrix} f_{x_1 x_1} & f_{x_1 x_2} & f_{x_1 x_3} \ f_{x_2 x_1} & f_{x_2 x_2} & f_{x_2 x_3} \ f_{x_3 x_1} & f_{x_3 x_2} & f_{x_3 x_3} \end{vmatrix}$$
> 
> $$\vdots$$
> 
> $$D_
n = \det(H_f)$$
> ---
> 
> ### Clasificación de Puntos Críticos
> 
> |Condición|Naturaleza|Tipo de Punto|
> |---|---|---|
> |Todos $D_i > 0$|Definida positiva|**Mínimo local**|
> |$D_i$ alterna en signo: $D_1 < 0, D_2 > 0, D_3 < 0, \ldots$|Definida negativa|**Máximo local**|
> |Otro patrón (no todos positivos ni alternados)|Indefinida|**Punto de silla**|
> |Algún $D_i = 0$|Semidefinida|**No concluyente**|
> 
> ---
> 
> ### Reglas Mnemotécnicas
> 
> **Para mínimo local:**
> 
> - "Todo positivo" ✓
> - $D_1 > 0, D_2 > 0, D_3 > 0, \ldots, D_n > 0$
> 
> **Para máximo local:**
> 
> - "Signos alternados empezando por negativo" ✓
> - $D_1 < 0, D_2 > 0, D_3 < 0, D_4 > 0, \ldots$
> - O equivalentemente: $(-1)^k D_k > 0$ para $k = 1, 2, \ldots, n$
> 
> **Para punto de silla:**
> 
> - "Cualquier otro patrón" ✓
> - Ejemplo: $D_1 > 0, D_2 < 0$ (ya sabemos que es silla)
> 
> ---
> 
> ### Ejemplo en 4D
> 
> Si $H_f$ en un punto crítico tiene menores:
> 
> $$D_1 = 3 > 0, \quad D_2 = 5 > 0, \quad D_3 = 2 > 0, \quad D_4 = 1 > 0$$
> 
> **Conclusión:** Todos positivos → **Mínimo local** ✓
> 
> ---
> 
> Si los menores fueran:
> 
> $$D_1 = -2 < 0, \quad D_2 = 4 > 0, \quad D_3 = -3 < 0, \quad D_4 = 1 > 0$$
> 
> **Conclusión:** Signos alternados ($-, +, -, +$) → **Máximo local** ✓

---

## 🔬 Relación con la Aproximación Cuadrática

> [!note]- 📊 Desarrollo de Taylor de Segundo Orden
> 
> ### Aproximación Cuadrática
> 
> Sea $f$ una función con segundas derivadas continuas, y sea $(x_0, y_0)$ un punto crítico (donde $\nabla f = 0$).
> 
> La **aproximación de Taylor de segundo orden** alrededor de $(x_0, y_0)$ es:
> 
> $$f(x,y) \approx f(x_0, y_0) + \frac{1}{2}[(x-x_0) \quad (y-y_0)] \begin{pmatrix} f_{xx} & f_{xy} \ f_{xy} & f_{yy} \end{pmatrix} \begin{pmatrix} x-x_0 \ y-y_0 \end{pmatrix}$$
> 
> O en notación vectorial, con $\mathbf{h} = (h_1, h_2) = (x-x_0, y-y_0)$:
> 
> $$f(\mathbf{x}_0 + \mathbf{h}) \approx f(\mathbf{x}_0) + \frac{1}{2}\mathbf{h}^T H_f(\mathbf{x}_0) \mathbf{h}$$
> 
> ---
> 
> ### Interpretación
> 
> La matriz hessiana $H_f$ determina la **forma cuadrática** que aproxima la función cerca del punto crítico.
> 
> **El término cuadrático:** $$Q(\mathbf{h}) = \frac{1}{2}\mathbf{h}^T H_f \mathbf{h}$$
> 
> controla el comportamiento local:
> 
> - Si $Q(\mathbf{h}) > 0$ para todo $\mathbf{h} \neq 0$ → $H_f$ definida positiva → **mínimo**
> - Si $Q(\mathbf{h}) < 0$ para todo $\mathbf{h} \neq 0$ → $H_f$ definida negativa → **máximo**
> - Si $Q(\mathbf{h})$ cambia de signo → $H_f$ indefinida → **silla**
> 
> ---
> 
> ### Ejemplo Explícito
> 
> **Función:** $f(x,y) = x^2 - y^2$
> 
> **Punto crítico:** $(0,0)$
> 
> **Hessiana:** $$H_f = \begin{pmatrix} 2 & 0 \ 0 & -2 \end{pmatrix}$$
> 
> **Aproximación cuadrática:**
> 
> $$f(x,y) \approx 0 + \frac{1}{2}[x \quad y] \begin{pmatrix} 2 & 0 \ 0 & -2 \end{pmatrix} \begin{pmatrix} x \ y \end{pmatrix}$$
> 
> $$= \frac{1}{2}(2x^2 - 2y^2) = x^2 - y^2$$
> 
> (En este caso, la aproximación es exacta porque $f$ es cuadrática)
> 
> **Análisis:**
> 
> - Para $\mathbf{h} = (h, 0)$: $Q(h,0) = h^2 > 0$ (aumenta)
> - Para $\mathbf{h} = (0, h)$: $Q(0,h) = -h^2 < 0$ (disminuye)
> 
> Por lo tanto: **punto de silla** ✓

---

## 🌟 Aplicaciones Prácticas

> [!tip]- 💼 Aplicaciones de la Matriz Hessiana
> 
> ### 1. Optimización en Machine Learning
> 
> **Métodos de segundo orden:**
> 
> - **Método de Newton:** Usa $H_f^{-1}$ para encontrar la dirección de descenso óptima
> - **Actualización:** $$\mathbf{x}_{n+1} = \mathbf{x}_n - \alpha H_f^{-1}(\mathbf{x}_n) \nabla f(\mathbf{x}_n)$$
> - Converge más rápido que el descenso por gradiente, pero requiere calcular/invertir $H_f$
> 
> **Condicionamiento:**
> 
> - El **número de condición** $\kappa(H_f) = \frac{\lambda_{\max}}{\lambda_{\min}}$ indica la dificultad de optimización
> - $\kappa$ grande → problema mal condicionado → convergencia lenta
> 
> ---
> 
> ### 2. Economía: Análisis de Convexidad
> 
> **Funciones de utilidad:**
> 
> Sea $U(x,y)$ la utilidad de consumir $x$ del bien 1 e $y$ del bien 2.
> 
> - Si $H_U$ es definida negativa → $U$ es **cóncava** → utilidad marginal decreciente
> - Importante para teoría del consumidor y equilibrio
> 
> **Funciones de costo:**
> 
> Sea $C(q_1, q_2)$ el costo de producir $q_1$ y $q_2$ unidades.
> 
> - Si $H_C$ es definida positiva → $C$ es **convexa** → costos marginales crecientes
> - Relevante para decisiones de producción
> 
> ---
> 
> ### 3. Física: Análisis de Estabilidad
> 
> **Energía potencial:**
> 
> Sea $V(x,y,z)$ la energía potencial de un sistema.
> 
> En un punto de equilibrio (donde $\nabla V = 0$):
> 
> - $H_V$ definida positiva → **equilibrio estable** (mínimo de energía)
> - $H_V$ definida negativa → **equilibrio inestable** (máximo de energía)
> - $H_V$ indefinida → **punto de silla** (inestable)
> 
> **Ejemplo:** Péndulo
> 
> - Posición inferior: $H_V$ positiva → estable
> - Posición superior: $H_V$ negativa → inestable
> 
> ---
> 
> ### 4. Estadística: Análisis de Máxima Verosimilitud
> 
> **Función de log-verosimilitud:**
> 
> Sea $\ell(\theta_1, \theta_2)$ la log-verosimilitud de parámetros $\theta = (\theta_1, \theta_2)$.
> 
> El **estimador de máxima verosimilitud** (MLE) maximiza $\ell$.
> 
> **Matriz de información de Fisher:**
> 
> $$\mathcal{I}(\theta) = -\mathbb{E}[H_\ell(\theta)]$$
> 
> (negativo de la esperanza de la hessiana)
> 
> **Propiedades:**
> 
> - $\mathcal{I}^{-1}$ aproxima la matriz de covarianza del MLE
> - Valores propios grandes de $\mathcal{I}$ → parámetros bien estimados
> - Valores propios pequeños → alta incertidumbre
> 
> ---
> 
> ### 5. Geometría Diferencial: Curvatura
> 
> **Curvatura gaussiana:**
> 
> Para una superficie $z = f(x,y)$, la curvatura gaussiana en un punto es:
> 
> $$K = \frac{f_{xx} f_{yy} - f_{xy}^2}{(1 + f_x^2 + f_y^2)^2} = \frac{\det(H_f)}{(1 + |\nabla f|^2)^2}$$
> 
> **Interpretación:**
> 
> - $K > 0$: superficie curva como una esfera (elíptica)
> - $K < 0$: superficie tipo silla de montar (hiperbólica)
> - $K = 0$: superficie plana o cilíndrica (parabólica)
> 
> ---
> 
> ### 6. Ingeniería: Análisis de Sensibilidad
> 
> **Diseño óptimo:**
> 
> Sea $f(x,y)$ una función objetivo a minimizar (ej: costo, peso, etc.).
> 
> En el óptimo $\mathbf{x}^*$:
> 
> - Los valores propios de $H_f(\mathbf{x}^*)$ indican la **sensibilidad** del diseño
> - Valores propios grandes → cambios pequeños en $\mathbf{x}$ afectan mucho a $f$
> - Valores propios pequeños → diseño robusto en esas direcciones
> 
> **Tolerancias de manufactura:**
> 
> - Direcciones con valores propios pequeños permiten mayores tolerancias
> - Direcciones con valores propios grandes requieren mayor precisión

---

## 📊 Métodos Computacionales

> [!tip]- 💻 Cálculo Numérico de la Hessiana
> 
> ### 1. Diferencias Finitas
> 
> Cuando las derivadas analíticas son difíciles de obtener, usamos aproximaciones numéricas.
> 
> **Aproximación de $f_{xx}$:**
> 
> $$f_{xx}(x,y) \approx \frac{f(x+h, y) - 2f(x,y) + f(x-h, y)}{h^2}$$
> 
> **Aproximación de $f_{xy}$:**
> 
> $$f_{xy}(x,y) \approx \frac{f(x+h, y+h) - f(x+h, y-h) - f(x-h, y+h) + f(x-h, y-h)}{4h^2}$$
> 
> **Ventajas:**
> 
> - Fácil de implementar
> - No requiere fórmulas analíticas
> 
> **Desventajas:**
> 
> - Error de truncamiento $O(h^2)$
> - Error de redondeo si $h$ es muy pequeño
> - Requiere muchas evaluaciones de función
> 
> ---
> 
> ### 2. Diferenciación Automática
> 
> Técnica moderna que calcula derivadas exactas (hasta precisión de máquina) sin aproximaciones numéricas.
> 
> **Modos:**
> 
> - **Forward mode:** Eficiente para $n$ pequeño
> - **Reverse mode:** Eficiente para $m$ pequeño (usado en backpropagation)
> 
> **Herramientas:**
> 
> - Python: `autograd`, `JAX`, `PyTorch`, `TensorFlow`
> - MATLAB: `Automatic Differentiation Toolbox`
> - Julia: `ForwardDiff.jl`, `Zygote.jl`
> 
> ---
> 
> ### 3. Aproximaciones de Bajo Rango
> 
> Para problemas de alta dimensión, calcular y almacenar $H_f$ completa es costoso ($O(n^2)$ memoria).
> 
> **Métodos cuasi-Newton:**
> 
> - **BFGS:** Aproxima $H_f$ o $H_f^{-1}$ usando solo gradientes
> - **L-BFGS:** Versión de memoria limitada (almacena solo vectores, no matrices)
> 
> **Actualización BFGS:**
> 
> $$H_{k+1} = H_k + \frac{\mathbf{y}_k \mathbf{y}_k^T}{\mathbf{y}_k^T \mathbf{s}_k} - \frac{H_k \mathbf{s}_k \mathbf{s}_k^T H_k}{\mathbf{s}_k^T H_k \mathbf{s}_k}$$
> 
> donde $\mathbf{s}_k = \mathbf{x}_{k+1} - \mathbf{x}_k$ y $\mathbf{y}_k = \nabla f(\mathbf{x}_{k+1}) - \nabla f(\mathbf{x}_k)$
> 
> ---
> 
> ### 4. Cálculo de Valores Propios
> 
> Para clasificar puntos críticos, necesitamos los valores propios de $H_f$.
> 
> **Métodos numéricos:**
> 
> - **Algoritmo QR:** Iterativo, converge a forma triangular superior
> - **Método de potencias:** Para el valor propio dominante
> - **Descomposición espectral:** $H_f = Q\Lambda Q^T$ donde $\Lambda$ es diagonal
> 
> **Librerías:**
> 
> - Python: `numpy.linalg.eig(H)`
> - MATLAB: `eig(H)`
> - Julia: `eigvals(H)`
> 
> **Optimización:** Para matrices grandes, a menudo solo necesitamos saber el **signo** de los valores propios, no sus valores exactos. Se pueden usar métodos especializados más rápidos.

---

## 🔍 Casos Especiales y Degenerados

> [!warning]- ⚠️ Situaciones Problemáticas
> 
> ### 1. Hessiana Singular
> 
> **Problema:** $\det(H_f) = 0$ → la matriz no es invertible
> 
> **Causas:**
> 
> - Al menos un valor propio es cero
> - La función es "plana" en alguna dirección
> - Punto crítico degenerado
> 
> **Ejemplo:**
> 
> $$f(x,y) = x^4 + y^4$$
> 
> En $(0,0)$:
> 
> $$H_f = \begin{pmatrix} 0 & 0 \ 0 & 0 \end{pmatrix}$$
> 
> $\det(H_f) = 0$, pero $(0,0)$ es un mínimo global.
> 
> **Solución:** Examinar derivadas de orden superior o usar análisis directo.
> 
> ---
> 
> ### 2. Hessiana Semidefinida
> 
> **Problema:** Algunos valores propios son cero, otros no.
> 
> **Interpretación:**
> 
> - La función es convexa/cóncava en algunas direcciones
> - "Plana" en otras direcciones
> - Clasificación no concluyente con criterio estándar
> 
> **Ejemplo:**
> 
> $$f(x,y) = x^2 + y^4$$
> 
> En $(0,0)$:
> 
> $$H_f = \begin{pmatrix} 2 & 0 \ 0 & 0 \end{pmatrix}$$
> 
> $D = 0$ (no concluyente), pero $f(x,y) \geq 0$ → mínimo global.
> 
> ---
> 
> ### 3. Múltiples Puntos Críticos
> 
> Cuando hay varios puntos críticos, debemos:
> 
> 1. Calcular $H_f$ en **cada** punto crítico
> 2. Clasificar cada uno independientemente
> 3. Comparar valores de función para determinar extremos globales
> 
> **Ejemplo:**
> 
> $$f(x,y) = x^3 - 3xy + y^3$$
> 
> Tiene dos puntos críticos:
> 
> - $(0,0)$: punto de silla
> - $(1,1)$: punto de silla
> 
> ¡Ambos son sillas! No hay extremos locales.
> 
> ---
> 
> ### 4. Funciones No Diferenciables
> 
> Si $f$ no tiene segundas derivadas continuas, la hessiana puede:
> 
> - No existir en algunos puntos
> - No ser simétrica
> - Cambiar discontinuamente
> 
> **Ejemplo:**
> 
> $$f(x,y) = |x| + |y|$$
> 
> En $(0,0)$ las derivadas parciales no existen → $H_f$ indefinida.
> 
> **Alternativas:**
> 
> - Subdiferenciales (análisis convexo)
> - Derivadas generalizadas
> - Métodos numéricos robustos
> 
> ---
> 
> ### 5. Dimensión Alta
> 
> Para $n$ grande (ej: $n > 1000$ en ML):
> 
> **Desafíos:**
> 
> - Calcular $H_f$ requiere $O(n^2)$ operaciones
> - Almacenar $H_f$ requiere $O(n^2)$ memoria
> - Invertir $H_f$ requiere $O(n^3)$ operaciones
> 
> **Soluciones:**
> 
> - Métodos cuasi-Newton (BFGS, L-BFGS)
> - Aproximaciones de bajo rango
> - Métodos de primer orden (solo gradiente)
> - Hessian-free optimization
> - Estructura especial (hessiana sparse, diagonal, etc.)

---

## 📝 Ejercicios Propuestos

> [!example]- 💪 Práctica Nivel Básico
> 
> **1. Calcular la matriz hessiana de las siguientes funciones:**
> 
> a) $f(x,y) = 3x^2 + 4y^2 + 2xy$
> 
> b) $f(x,y) = e^{x+y}$
> 
> c) $f(x,y) = x^3 + y^3 - 3xy$
> 
> d) $f(x,y) = \sin(x)\cos(y)$
> 
> e) $f(x,y) = \ln(x^2 + y^2)$
> 
> ---
> 
> **2. Para cada función, encontrar puntos críticos y clasificarlos:**
> 
> a) $f(x,y) = x^2 + 4y^2 - 2x + 8y$
> 
> b) $f(x,y) = x^2 - y^2 + 2x - 4y$
> 
> c) $f(x,y) = xy - x - y$
> 
> d) $f(x,y) = x^2 + xy + y^2$
> 
> ---
> 
> **3. Determinar si las siguientes matrices hessianas corresponden a mínimo, máximo o silla:**
> 
> a) $H_f = \begin{pmatrix} 4 & 1 \ 1 & 4 \end{pmatrix}$
> 
> b) $H_f = \begin{pmatrix} -2 & 0 \ 0 & -3 \end{pmatrix}$
> 
> c) $H_f = \begin{pmatrix} 1 & 2 \ 2 & 1 \end{pmatrix}$
> 
> d) $H_f = \begin{pmatrix} 0 & 1 \ 1 & 0 \end{pmatrix}$

> [!example]- 💪 Práctica Nivel Intermedio
> 
> **4. Funciones en tres variables:**
> 
> a) Calcular $H_f$ para $f(x,y,z) = x^2 + 2y^2 + 3z^2 + xy - xz$
> 
> b) Clasificar el punto crítico $(0,0,0)$
> 
> c) Verificar usando los menores principales de Sylvester
> 
> ---
> 
> **5. Análisis completo:**
> 
> Para $f(x,y) = x^3 + y^3 - 3xy$:
> 
> a) Encontrar todos los puntos críticos
> 
> b) Calcular $H_f$ en cada punto crítico
> 
> c) Clasificar cada punto
> 
> d) ¿Cuál es el mínimo global? ¿Y el máximo global?
> 
> ---
> 
> **6. Verificación con valores propios:**
> 
> Para $f(x,y) = x^2 + 4xy + 5y^2$ en $(0,0)$:
> 
> a) Calcular $H_f(0,0)$
> 
> b) Encontrar los valores propios
> 
> c) Clasificar usando valores propios
> 
> d) Verificar con el discriminante
> 
> ---
> 
> **7. Caso no concluyente:**
> 
> Para $f(x,y) = x^3y + xy^3$:
> 
> a) Encontrar el punto crítico
> 
> b) Calcular $H_f$ en ese punto
> 
> c) ¿Qué dice el criterio de la segunda derivada?
> 
> d) Analizar directamente la función para clasificar el punto

> [!example]- 💪 Práctica Nivel Avanzado
> 
> **8. Optimización con restricciones:**
> 
> Considere $f(x,y) = x^2 + y^2$ sujeto a $g(x,y) = x + y - 1 = 0$.
> 
> a) Usar multiplicadores de Lagrange para encontrar puntos críticos
> 
> b) Calcular la hessiana del Lagrangiano
> 
> c) Clasificar el punto crítico
> 
> ---
> 
> **9. Análisis de curvatura:**
> 
> Para $f(x,y) = e^{-(x^2+y^2)}$:
> 
> a) Calcular $H_f(0,0)$
> 
> b) Encontrar las direcciones principales de curvatura
> 
> c) Calcular la curvatura gaussiana en el origen
> 
> ---
> 
> **10. Aplicación económica:**
> 
> Una función de utilidad es $U(x,y) = xy$ donde $x, y > 0$.
> 
> a) ¿Es $U$ cóncava? (verificar con $H_U$)
> 
> b) Maximizar $U$ sujeto a $2x + 3y = 60$ (restricción presupuestaria)
> 
> c) Verificar que el punto encontrado es realmente un máximo
> 
> ---
> 
> **11. Análisis numérico:**
> 
> Para $f(x,y) = \sin(xy)$:
> 
> a) Calcular $H_f(\pi/4, \pi/4)$ analíticamente
> 
> b) Aproximar $H_f$ usando diferencias finitas con $h = 0.01$
> 
> c) Comparar resultados y calcular el error
> 
> ---
> 
> **12. Dimensión superior:**
> 
> Para $f(x_1, x_2, x_3, x_4) = \sum_{i=1}^4 x_i^2 - \sum_{i=1}^3 x_i x_{i+1}$:
> 
> a) Escribir $H_f$ explícitamente
> 
> b) Calcular los menores principales
> 
> c) Clasificar el punto crítico $(0,0,0,0)$

---

## ✅ Soluciones Selectas

> [!success]- 🔑 Respuestas Ejercicios Básicos
> 
> **1a)** $f(x,y) = 3x^2 + 4y^2 + 2xy$
> 
> $$f_x = 6x + 2y, \quad f_y = 4y + 2x$$ $$f_{xx} = 6, \quad f_{yy} = 8, \quad f_{xy} = 2$$
> 
> $$H_f = \begin{pmatrix} 6 & 2 \ 2 & 8 \end{pmatrix}$$
> 
> ---
> 
> **1c)** $f(x,y) = x^3 + y^3 - 3xy$
> 
> $$f_x = 3x^2 - 3y, \quad f_y = 3y^2 - 3x$$ $$f_{xx} = 6x, \quad f_{yy} = 6y, \quad f_{xy} = -3$$
> 
> $$H_f = \begin{pmatrix} 6x & -3 \ -3 & 6y \end{pmatrix}$$
> 
> ---
> 
> **2a)** $f(x,y) = x^2 + 4y^2 - 2x + 8y$
> 
> **Puntos críticos:** $$f_x = 2x - 2 = 0 \implies x = 1$$ $$f_y = 8y + 8 = 0 \implies y = -1$$
> 
> Punto crítico: $(1, -1)$
> 
> **Hessiana:** $$H_f = \begin{pmatrix} 2 & 0 \ 0 & 8 \end{pmatrix}$$
> 
> **Discriminante:** $$D = 2 \cdot 8 - 0^2 = 16 > 0$$
> 
> Como $D > 0$ y $f_{xx} = 2 > 0$:
> 
> **Conclusión:** $(1,-1)$ es un **mínimo local** ✓
> 
> ---
> 
> **2b)** $f(x,y) = x^2 - y^2 + 2x - 4y$
> 
> **Puntos críticos:** $$f_x = 2x + 2 = 0 \implies x = -1$$ $$f_y = -2y - 4 = 0 \implies y = -2$$
> 
> Punto crítico: $(-1, -2)$
> 
> **Hessiana:** $$H_f = \begin{pmatrix} 2 & 0 \ 0 & -2 \end{pmatrix}$$
> 
> **Discriminante:** $$D = 2 \cdot (-2) - 0^2 = -4 < 0$$
> 
> **Conclusión:** $(-1,-2)$ es un **punto de silla** ✓
> 
> ---
> 
> **3a)** $H_f = \begin{pmatrix} 4 & 1 \ 1 & 4 \end{pmatrix}$
> 
> $$D = 4 \cdot 4 - 1^2 = 15 > 0$$ $$f_{xx} = 4 > 0$$
> 
> **Conclusión:** **Mínimo local** ✓
> 
> ---
> 
> **3b)** $H_f = \begin{pmatrix} -2 & 0 \ 0 & -3 \end{pmatrix}$
> 
> $$D = (-2)(-3) - 0^2 = 6 > 0$$ $$f_{xx} = -2 < 0$$
> 
> **Conclusión:** **Máximo local** ✓
> 
> ---
> 
> **3c)** $H_f = \begin{pmatrix} 1 & 2 \ 2 & 1 \end{pmatrix}$
> 
> $$D = 1 \cdot 1 - 2^2 = -3 < 0$$
**Conclusión:** **Punto de silla** ✓
> ---
> 
> **3d)** $H_f = \begin{pmatrix} 0 & 1 \ 1 & 0 \end{pmatrix}$
> 
> $$D = 0 \cdot 0 - 1^2 = -1 < 0$$
> 
> **Conclusión:** **Punto de silla** ✓

> [!success]- 🔑 Respuestas Ejercicios Intermedios
> 
> **4a)** $f(x,y,z) = x^2 + 2y^2 + 3z^2 + xy - xz$
> 
> **Primeras derivadas:** $$f_x = 2x + y - z$$ $$f_y = 4y + x$$ $$f_z = 6z - x$$
> 
> **Segundas derivadas:** $$f_{xx} = 2, \quad f_{yy} = 4, \quad f_{zz} = 6$$ $$f_{xy} = 1, \quad f_{xz} = -1, \quad f_{yz} = 0$$
> 
> **Matriz hessiana:** $$H_f = \begin{pmatrix} 2 & 1 & -1 \ 1 & 4 & 0 \ -1 & 0 & 6 \end{pmatrix}$$
> 
> ---
> 
> **4b) y 4c)** Clasificación del punto $(0,0,0)$:
> 
> **Menores principales:**
> 
> $$D_1 = 2 > 0$$ ✓
> 
> $$D_2 = \begin{vmatrix} 2 & 1 \ 1 & 4 \end{vmatrix} = 8 - 1 = 7 > 0$$ ✓
> 
> $$D_3 = \begin{vmatrix} 2 & 1 & -1 \ 1 & 4 & 0 \ -1 & 0 & 6 \end{vmatrix}$$
> 
> Expandiendo por la tercera fila: $$= -1 \cdot \begin{vmatrix} 1 & -1 \ 4 & 0 \end{vmatrix} + 6 \cdot \begin{vmatrix} 2 & 1 \ 1 & 4 \end{vmatrix}$$
> 
> $$= -1(0 - (-4)) + 6(7) = -4 + 42 = 38 > 0$$ ✓
> 
> Como $D_1 > 0$, $D_2 > 0$, $D_3 > 0$:
> 
> **Conclusión:** $(0,0,0)$ es un **mínimo local** ✓
> 
> ---
> 
> **5a)** $f(x,y) = x^3 + y^3 - 3xy$
> 
> **Puntos críticos:** $$f_x = 3x^2 - 3y = 0 \implies y = x^2$$ $$f_y = 3y^2 - 3x = 0 \implies x = y^2$$
> 
> Sustituyendo $y = x^2$ en $x = y^2$: $$x = (x^2)^2 = x^4$$ $$x^4 - x = 0$$ $$x(x^3 - 1) = 0$$
> 
> Por lo tanto: $x = 0$ o $x = 1$
> 
> - Si $x = 0$: $y = 0^2 = 0$ → punto $(0,0)$
> - Si $x = 1$: $y = 1^2 = 1$ → punto $(1,1)$
> 
> **Puntos críticos:** $(0,0)$ y $(1,1)$
> 
> ---
> 
> **5b) y 5c)** Clasificación:
> 
> **Hessiana general:** $$H_f = \begin{pmatrix} 6x & -3 \ -3 & 6y \end{pmatrix}$$
> 
> **En $(0,0)$:** $$H_f(0,0) = \begin{pmatrix} 0 & -3 \ -3 & 0 \end{pmatrix}$$
> 
> $$D = 0 \cdot 0 - (-3)^2 = -9 < 0$$
> 
> **Conclusión:** $(0,0)$ es un **punto de silla** ✓
> 
> **En $(1,1)$:** $$H_f(1,1) = \begin{pmatrix} 6 & -3 \ -3 & 6 \end{pmatrix}$$
> 
> $$D = 6 \cdot 6 - (-3)^2 = 36 - 9 = 27 > 0$$ $$f_{xx} = 6 > 0$$
> 
> **Conclusión:** $(1,1)$ es un **mínimo local** ✓
> 
> ---
> 
> **5d)** Extremos globales:
> 
> Evaluando la función:
> 
> - $f(0,0) = 0$
> - $f(1,1) = 1 + 1 - 3 = -1$
> 
> Analizando el comportamiento en el infinito:
> 
> - Cuando $x \to \pm\infty$ o $y \to \pm\infty$: $f(x,y) \to \pm\infty$
> 
> **Conclusión:**
> 
> - **Mínimo local** en $(1,1)$ con $f = -1$
> - **No hay máximo global** (la función no está acotada superiormente)
> - **No hay mínimo global** (aunque $(1,1)$ es mínimo local, la función puede decrecer más en otras regiones o en el infinito)
> 
> ---
> 
> **6a)** $f(x,y) = x^2 + 4xy + 5y^2$
> 
> $$f_{xx} = 2, \quad f_{yy} = 10, \quad f_{xy} = 4$$
> 
> $$H_f(0,0) = \begin{pmatrix} 2 & 4 \ 4 & 10 \end{pmatrix}$$
> 
> ---
> 
> **6b)** Valores propios:
> 
> Ecuación característica: $$\det(H_f - \lambda I) = 0$$
> 
> $$\begin{vmatrix} 2-\lambda & 4 \ 4 & 10-\lambda \end{vmatrix} = 0$$
> 
> $$(2-\lambda)(10-\lambda) - 16 = 0$$ $$20 - 10\lambda - 2\lambda + \lambda^2 - 16 = 0$$ $$\lambda^2 - 12\lambda + 4 = 0$$
> 
> Usando la fórmula cuadrática: $$\lambda = \frac{12 \pm \sqrt{144 - 16}}{2} = \frac{12 \pm \sqrt{128}}{2} = \frac{12 \pm 8\sqrt{2}}{2} = 6 \pm 4\sqrt{2}$$
> 
> $$\lambda_1 = 6 + 4\sqrt{2} \approx 11.66 > 0$$ $$\lambda_2 = 6 - 4\sqrt{2} \approx 0.34 > 0$$
> 
> ---
> 
> **6c)** Ambos valores propios son positivos → **mínimo local** ✓
> 
> ---
> 
> **6d)** Verificación con discriminante:
> 
> $$D = 2 \cdot 10 - 4^2 = 20 - 16 = 4 > 0$$ $$f_{xx} = 2 > 0$$
> 
> **Conclusión:** **Mínimo local** ✓ (coincide)
> 
> ---
> 
> **7a)** $f(x,y) = x^3y + xy^3$
> 
> $$f_x = 3x^2y + y^3 = y(3x^2 + y^2) = 0$$ $$f_y = x^3 + 3xy^2 = x(x^2 + 3y^2) = 0$$
> 
> De la primera: $y = 0$ o $3x^2 + y^2 = 0$  
> De la segunda: $x = 0$ o $x^2 + 3y^2 = 0$
> 
> Como $3x^2 + y^2 = 0$ solo si $x = y = 0$ (ambos términos son $\geq 0$)  
> Similarmente para $x^2 + 3y^2 = 0$
> 
> **Punto crítico único:** $(0,0)$
> 
> ---
> 
> **7b)** Segundas derivadas:
> 
> $$f_{xx} = 6xy, \quad f_{yy} = 6xy, \quad f_{xy} = 3x^2 + 3y^2$$
> 
> En $(0,0)$: $$H_f(0,0) = \begin{pmatrix} 0 & 0 \ 0 & 0 \end{pmatrix}$$
> 
> ---
> 
> **7c)** Discriminante:
> 
> $$D = 0 \cdot 0 - 0^2 = 0$$
> 
> El criterio de la segunda derivada es **no concluyente** ❌
> 
> ---
> 
> **7d)** Análisis directo:
> 
> $$f(x,y) = x^3y + xy^3 = xy(x^2 + y^2)$$
> 
> Consideremos diferentes caminos:
> 
> - **Por $y = x$:** $f(x,x) = x^4 + x^4 = 2x^4 \geq 0$
> - **Por $y = -x$:** $f(x,-x) = -x^4 - x^4 = -2x^4 \leq 0$
> 
> La función cambia de signo en diferentes direcciones.
> 
> **Conclusión:** $(0,0)$ es un **punto de silla** ✓

> [!success]- 🔑 Respuestas Ejercicios Avanzados
> 
> **8a)** Multiplicadores de Lagrange:
> 
> $$\mathcal{L}(x,y,\lambda) = x^2 + y^2 - \lambda(x + y - 1)$$
> 
> $$\frac{\partial \mathcal{L}}{\partial x} = 2x - \lambda = 0 \implies x = \frac{\lambda}{2}$$ $$\frac{\partial \mathcal{L}}{\partial y} = 2y - \lambda = 0 \implies y = \frac{\lambda}{2}$$ $$\frac{\partial \mathcal{L}}{\partial \lambda} = -(x + y - 1) = 0$$
> 
> De las primeras dos: $x = y$  
> Sustituyendo en la restricción: $x + x - 1 = 0 \implies x = \frac{1}{2}$
> 
> **Punto crítico:** $(\frac{1}{2}, \frac{1}{2})$ con $\lambda = 1$
> 
> ---
> 
> **8b)** Hessiana del Lagrangiano (hessiana orlada):
> 
> Para el problema restringido, la hessiana relevante es:
> 
> $$H_{\mathcal{L}} = \begin{pmatrix} 0 & g_x & g_y \ g_x & \mathcal{L}_{xx} & \mathcal{L}_{xy} \ g_y & \mathcal{L}_{yx} & \mathcal{L}_{yy} \end{pmatrix} = \begin{pmatrix} 0 & 1 & 1 \ 1 & 2 & 0 \ 1 & 0 & 2 \end{pmatrix}$$
> 
> ---
> 
> **8c)** Para clasificar en problemas con restricciones:
> 
> Calculamos el menor principal relevante:
> 
> $$\det(H_{\mathcal{L}}) = 0 \cdot \begin{vmatrix} 2 & 0 \ 0 & 2 \end{vmatrix} - 1 \cdot \begin{vmatrix} 1 & 0 \ 1 & 2 \end{vmatrix} + 1 \cdot \begin{vmatrix} 1 & 2 \ 1 & 0 \end{vmatrix}$$
> 
> $$= -1(2) + 1(-2) = -4 < 0$$
> 
> Para un problema con una restricción ($m=1$), si $(-1)^m \det(H_{\mathcal{L}}) < 0$, el punto es un mínimo.
> 
> $$(-1)^1 \cdot (-4) = 4 > 0$$
> 
> **Conclusión:** $(\frac{1}{2}, \frac{1}{2})$ es un **mínimo local** en la restricción ✓
> 
> ---
> 
> **9a)** $f(x,y) = e^{-(x^2+y^2)}$
> 
> $$f_x = -2xe^{-(x^2+y^2)}$$ $$f_y = -2ye^{-(x^2+y^2)}$$
> 
> $$f_{xx} = (-2 + 4x^2)e^{-(x^2+y^2)}$$ $$f_{yy} = (-2 + 4y^2)e^{-(x^2+y^2)}$$ $$f_{xy} = 4xye^{-(x^2+y^2)}$$
> 
> En $(0,0)$: $$H_f(0,0) = \begin{pmatrix} -2 & 0 \ 0 & -2 \end{pmatrix}$$
> 
> ---
> 
> **9b)** Direcciones principales:
> 
> Los valores propios son: $\lambda_1 = \lambda_2 = -2$
> 
> La matriz es un múltiplo de la identidad, por lo que **todas las direcciones** son direcciones principales.
> 
> **Curvatura:** Igual en todas direcciones (curvatura esférica)
> 
> ---
> 
> **9c)** Curvatura gaussiana:
> 
> $$K = \frac{f_{xx}f_{yy} - f_{xy}^2}{(1 + f_x^2 + f_y^2)^2}$$
> 
> En $(0,0)$: $$K = \frac{(-2)(-2) - 0^2}{(1 + 0 + 0)^2} = \frac{4}{1} = 4 > 0$$
> 
> **Interpretación:** Superficie de tipo elíptico (como una esfera) en el origen.
> 
> ---
> 
> **10a)** $U(x,y) = xy$ para $x, y > 0$
> 
> $$H_U = \begin{pmatrix} 0 & 1 \ 1 & 0 \end{pmatrix}$$
> 
> $$D = 0 \cdot 0 - 1^2 = -1 < 0$$
> 
> La hessiana es indefinida, pero esto no implica que $U$ no sea cóncava en su dominio.
> 
> **Análisis correcto:** Para funciones de dos variables, $U$ es cóncava si la hessiana es **semidefinida negativa** en el dominio relevante.
> 
> Consideremos la forma cuadrática: $$Q(h_1, h_2) = \mathbf{h}^T H_U \mathbf{h} = 2h_1h_2$$
> 
> Esto puede ser positivo o negativo, así que $U(x,y) = xy$ **no es cóncava ni convexa** globalmente.
> 
> Sin embargo, $\ln(U(x,y)) = \ln(x) + \ln(y)$ **es cóncava** (y se usa frecuentemente en economía).
> 
> ---
> 
> **10b)** Maximizar con restricción $2x + 3y = 60$:
> 
> $$\mathcal{L} = xy - \lambda(2x + 3y - 60)$$
> 
> $$\frac{\partial \mathcal{L}}{\partial x} = y - 2\lambda = 0 \implies y = 2\lambda$$ $$\frac{\partial \mathcal{L}}{\partial y} = x - 3\lambda = 0 \implies x = 3\lambda$$ $$\frac{\partial \mathcal{L}}{\partial \lambda} = -(2x + 3y - 60) = 0$$
> 
> Sustituyendo: $$2(3\lambda) + 3(2\lambda) = 60$$ $$6\lambda + 6\lambda = 60$$ $$\lambda = 5$$
> 
> Por lo tanto: $x = 15$, $y = 10$
> 
> **Punto óptimo:** $(15, 10)$ con $U = 150$
> 
> ---
> 
> **10c)** Verificación:
> 
> Dado que el conjunto factible es compacto y $U$ es continua, por el Teorema del Valor Extremo existe un máximo.
> 
> Como solo hay un punto crítico, debe ser el máximo ✓
> 
> Alternativamente, podemos verificar que la hessiana orlada tiene el signo correcto (ya hecho en 8c).

---

## 🌐 Extensiones y Temas Avanzados

> [!note]- 🚀 Conceptos Avanzados
> 
> ### 1. Hessiana en Variedades
> 
> Para funciones definidas en **variedades diferenciables** (superficies curvas), la hessiana se define usando la **conexión de Levi-Civita**.
> 
> **Hessiana riemanniana:**
> 
> $$\text{Hess}_f(X,Y) = \langle \nabla_X(\nabla f), Y \rangle$$
> 
> donde $\nabla_X$ es la derivada covariante.
> 
> **Aplicación:** Geometría diferencial, relatividad general
> 
> ---
> 
> ### 2. Hessiana Generalizada
> 
> Para funciones **no diferenciables**, se define el **subdiferencial** y la **hessiana generalizada**.
> 
> **Hessiana de Clarke:**
> 
> Para funciones localmente Lipschitz, la hessiana generalizada es un conjunto (no una única matriz).
> 
> **Aplicación:** Optimización no suave, análisis convexo
> 
> ---
> 
> ### 3. Hessiana Estocástica
> 
> En **machine learning** con datos masivos, calcular $H_f$ exacta es prohibitivo.
> 
> **Aproximación estocástica:**
> 
> $$H_f \approx \frac{1}{B}\sum_{i \in \text{batch}} H_{f_i}$$
> 
> donde $f = \frac{1}{n}\sum_{i=1}^n f_i$ y el batch es una muestra aleatoria.
> 
> **Métodos relacionados:**
> 
> - Hessian-free optimization
> - Natural gradient (usa la métrica de Fisher)
> - K-FAC (aproximación por factores de Kronecker)
> 
> ---
> 
> ### 4. Condiciones de Segundo Orden en Optimización
> 
> **Condiciones necesarias:**
> 
> Si $\mathbf{x}^*$ es un mínimo local de $f$:
> 
> 1. $\nabla f(\mathbf{x}^*) = 0$ (primer orden)
> 2. $H_f(\mathbf{x}^*)$ es semidefinida positiva (segundo orden)
> 
> **Condiciones suficientes:**
> 
> Si en $\mathbf{x}^*$:
> 
> 1. $\nabla f(\mathbf{x}^*) = 0$
> 2. $H_f(\mathbf{x}^*)$ es **definida positiva** (segundo orden)
> 
> Entonces $\mathbf{x}^*$ es un **mínimo local estricto**.
> 
> ---
> 
> ### 5. Análisis de Perturbaciones
> 
> La inversa de la hessiana $H_f^{-1}$ en un óptimo mide la **sensibilidad** del óptimo a perturbaciones.
> 
> **Teorema del función implícita aplicado:**
> 
> Si $\mathbf{x}^*$ minimiza $f(\mathbf{x}, \mathbf{p})$ para parámetros $\mathbf{p}$, entonces:
> 
> $$\frac{d\mathbf{x}^*}{d\mathbf{p}} = -H_f^{-1} \frac{\partial^2 f}{\partial \mathbf{x} \partial \mathbf{p}}$$
> 
> **Aplicación:** Análisis de sensibilidad en ingeniería y economía
> 
> ---
> 
> ### 6. Hessiana en Optimización Convexa
> 
> Para funciones **convexas**, la hessiana tiene propiedades especiales:
> 
> **Teorema:** $f$ es convexa $\iff$ $H_f$ es semidefinida positiva en todo el dominio
> 
> **Teorema:** Si $f$ es estrictamente convexa ($H_f$ definida positiva), entonces:
> 
> - Existe a lo más un mínimo global
> - Todo mínimo local es mínimo global
> - Todo punto crítico es mínimo global
> 
> **Implicación:** La optimización convexa es "fácil" - los métodos locales encuentran el óptimo global

---

## 📖 Resumen de Conceptos Clave

> [!tip]- 💡 Puntos Esenciales para Recordar
> 
> ### Definición y Estructura
> 
> ✅ **Matriz hessiana:** Matriz simétrica de segundas derivadas parciales
> 
> ✅ **Elementos:** $H_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}$
> 
> ✅ **Simetría:** $H_{ij} = H_{ji}$ (por Teorema de Schwarz si derivadas continuas)
> 
> ---
> 
> ### Clasificación de Puntos Críticos (2D)
> 
> ✅ **Discriminante:** $D = f_{xx}f_{yy} - f_{xy}^2 = \det(H_f)$
> 
> |$D$|$f_{xx}$|Tipo|
> |---|---|---|
> |$> 0$|$> 0$|Mínimo|
> |$> 0$|$< 0$|Máximo|
> |$< 0$|-|Silla|
> |$= 0$|-|No concluyente|
> 
> ---
> 
> ### Criterio de Sylvester (nD)
> 
> ✅ **Mínimo:** Todos los menores principales $> 0$
> 
> ✅ **Máximo:** Menores alternando en signo: $-, +, -, +, \ldots$
> 
> ✅ **Silla:** Cualquier otro patrón (excepto ceros)
> 
> ---
> 
> ### Valores Propios
> 
> ✅ **Definida positiva:** Todos $\lambda_i > 0$ → mínimo
> 
> ✅ **Definida negativa:** Todos $\lambda_i < 0$ → máximo
> 
> ✅ **Indefinida:** Algunos $\lambda_i > 0$, otros $< 0$ → silla
> 
> ✅ **Semidefinida:** Algún $\lambda_i = 0$ → no concluyente
> 
> ---
> 
> ### Aplicaciones Clave
> 
> ✅ **Optimización:** Clasificar extremos locales
> 
> ✅ **Aproximación:** Taylor de segundo orden
> 
> ✅ **Curvatura:** Análisis geométrico de superficies
> 
> ✅ **Estabilidad:** Sistemas dinámicos y físicos
> 
> ---
> 
> ### Casos Especiales
> 
> ⚠️ **$D = 0$:** Criterio no concluyente, analizar orden superior
> 
> ⚠️ **Hessiana singular:** $\det(H) = 0$, no invertible
> 
> ⚠️ **Dimensión alta:** Usar métodos numéricos o aproximaciones

---

## 🔗 Conexiones con Otros Temas

> [!quote]- 🌐 Relaciones Importantes
> 
> **Este tema se conecta con:**
> 
> - **Derivadas Parciales** - Base para construir la hessiana
> - **Gradiente** - Primera derivada, necesaria para encontrar puntos críticos
> - **Optimización** - La hessiana clasifica extremos locales
> - **Multiplicadores de Lagrange** - Hessiana orlada en optimización con restricciones
> - **Series de Taylor** - Aproximación cuadrática
> - **Formas Cuadráticas** - Interpretación algebraica de $H_f$
> - **Álgebra Lineal** - Valores/vectores propios, matrices simétricas
> - **Geometría Diferencial** - Curvatura de superficies
> - **Análisis Convexo** - Caracterización de convexidad
> 
> **Prerequisitos:**
> 
> - Derivadas parciales de segundo orden
> - Puntos críticos (gradiente = 0)
> - Álgebra lineal (determinantes, valores propios)
> 
> **Temas posteriores:**
> 
> - Optimización con restricciones
> - Teoría de Morse (puntos críticos no degenerados)
> - Métodos numéricos de optimización
> - Análisis de estabilidad

---

## 📚 Referencias y Lecturas Adicionales

> [!note]- 📖 Para Profundizar
> 
> ### Textos Clásicos
> 
> 1. **James Stewart** - "Cálculo de Varias Variables"
>     - Capítulo sobre extremos y la segunda derivada
>     - Ejemplos accesibles y bien ilustrados
> 2. **Marsden & Tromba** - "Vector Calculus"
>     - Tratamiento riguroso de la hessiana
>     - Conexiones con geometría diferencial
> 3. **Apostol** - "Calculus Vol. II"
>     - Enfoque teórico profundo
>     - Demostraciones completas
> 
> ---
> 
> ### Optimización
> 
> 4. **Boyd & Vandenberghe** - "Convex Optimization"
>     - Hessiana en optimización convexa
>     - Aplicaciones en ML y ingeniería
> 5. **Nocedal & Wright** - "Numerical Optimization"
>     - Métodos de segundo orden
>     - BFGS, Newton, trust region
> 
> ---
> 
> ### Aplicaciones Avanzadas
> 
> 6. **Goodfellow et al.** - "Deep Learning"
>     - Hessiana en redes neuronales
>     - Métodos de segundo orden en ML
> 7. **do Carmo** - "Differential Geometry of Curves and Surfaces"
>     - Hessiana en variedades
>     - Curvatura gaussiana
> 
> ---
> 
> ### Recursos Online
> 
> - **Khan Academy:** Visualizaciones interactivas
> - **3Blue1Brown:** Videos sobre curvatura y formas cuadráticas
> - **MIT OpenCourseWare:** Cursos completos de cálculo multivariable

---

**Tags:** #calculo-multivariable #matriz-hessiana #optimizacion #segundas-derivadas #puntos-criticos #valores-propios #criterio-sylvester #convexidad #curvatura #machine-learning