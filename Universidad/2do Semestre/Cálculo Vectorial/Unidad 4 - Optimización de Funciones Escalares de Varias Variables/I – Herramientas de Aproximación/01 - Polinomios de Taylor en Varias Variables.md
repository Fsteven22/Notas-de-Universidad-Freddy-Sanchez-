# 📐 Polinomios de Taylor en Varias Variables

## 🌟 Concepto Fundamental

> [!info]- Definición Intuitiva
> **Los polinomios de Taylor en varias variables son aproximaciones polinomiales de funciones multivariables alrededor de un punto dado. Extienden la idea de los polinomios de Taylor de una variable al utilizar derivadas parciales para capturar el comportamiento local de funciones de $\mathbb{R}^n$ en $\mathbb{R}$. Estos polinomios son fundamentales para el análisis local, optimización y aproximación numérica de funciones complejas.**
> 
> **Características clave:**
> - **Aproximación local:** Representa la función cerca de un punto específico
> - **Derivadas parciales:** Utiliza todas las derivadas direccionales
> - **Generalización natural:** Extiende el caso univariable a múltiples dimensiones
> - **Términos multinomiales:** Incluye productos de variables elevadas a potencias
> - **Precisión creciente:** Mayor orden implica mejor aproximación

### 📖 Contexto Histórico

> [!note]- Desarrollo del Concepto
> **Orígenes (1700-1800):**
> - **Brook Taylor (1715):** Serie de Taylor univariable
>   - *Methodus Incrementorum Directa et Inversa*
>   - Primera formulación sistemática
> - **Colin Maclaurin (1742):** Caso especial en el origen
>   - Series de Maclaurin
>   - Aplicaciones a geometría
> - **Joseph-Louis Lagrange (1770s):** Forma del residuo
>   - Teorema del valor medio
>   - Análisis del error
> 
> **Extensión multivariable (1800-1900):**
> - **Augustin-Louis Cauchy (1820s):** Análisis riguroso
>   - Convergencia de series
>   - Radio de convergencia multivariable
> - **Karl Weierstrass (1860s):** Teoría de aproximación
>   - Funciones analíticas de varias variables
>   - Convergencia uniforme
> - **Sonya Kovalevskaya (1870s):** Ecuaciones diferenciales
>   - Teorema de Cauchy-Kovalevskaya
>   - Soluciones analíticas
> 
> **Era moderna (1900-presente):**
> - **Henri Cartan (1930s-40s):** Análisis complejo multivariable
>   - Dominios de holomorfia
>   - Generalización a espacios de Banach
> - **Laurent Schwartz (1950s):** Teoría de distribuciones
>   - Series formales
>   - Análisis funcional
> - **Aplicaciones computacionales:**
>   - Métodos de elementos finitos
>   - Aprendizaje automático (gradientes)
>   - Optimización numérica

## 📊 Definición Formal

> [!important]- Polinomio de Taylor de Orden n
> **Definición:**
> 
> Sea $f: \mathbb{R}^n \to \mathbb{R}$ una función con derivadas parciales continuas hasta orden $k$ en una vecindad del punto $\mathbf{a} = (a_1, a_2, \ldots, a_n)$.
> 
> El **polinomio de Taylor de orden $k$** de $f$ centrado en $\mathbf{a}$ es:
> 
> $$P_k(\mathbf{x}) = \sum_{|\alpha| = 0}^{k} \frac{1}{\alpha!} D^{\alpha}f(\mathbf{a}) (\mathbf{x} - \mathbf{a})^{\alpha}$$
> 
> donde:
> - $\alpha = (\alpha_1, \alpha_2, \ldots, \alpha_n)$ es un **multi-índice** con $\alpha_i \in \mathbb{N} \cup \{0\}$
> - $|\alpha| = \alpha_1 + \alpha_2 + \cdots + \alpha_n$ (orden total)
> - $\alpha! = \alpha_1! \cdot \alpha_2! \cdots \alpha_n!$
> - $D^{\alpha}f = \frac{\partial^{|\alpha|} f}{\partial x_1^{\alpha_1} \partial x_2^{\alpha_2} \cdots \partial x_n^{\alpha_n}}$
> - $(\mathbf{x} - \mathbf{a})^{\alpha} = (x_1 - a_1)^{\alpha_1}(x_2 - a_2)^{\alpha_2} \cdots (x_n - a_n)^{\alpha_n}$
> 
> **Notación alternativa (más explícita):**
> 
> Para $f(x, y)$ en dos variables centrado en $(a, b)$:
> 
> $$P_k(x,y) = \sum_{m=0}^{k} \sum_{j=0}^{m} \frac{1}{j!(m-j)!} \frac{\partial^m f}{\partial x^j \partial y^{m-j}}\bigg|_{(a,b)} (x-a)^j(y-b)^{m-j}$$

> [!success]- Casos Particulares Importantes
> **Orden 0 (aproximación constante):**
> 
> $$P_0(\mathbf{x}) = f(\mathbf{a})$$
> 
> **Orden 1 (aproximación lineal):**
> 
> Para $f(x, y)$ centrado en $(a, b)$:
> 
> $$P_1(x,y) = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$$
> 
> $$= f(a,b) + \nabla f(a,b) \cdot (\mathbf{x} - \mathbf{a})$$
> 
> Este es el **plano tangente** a la superficie en $(a,b)$.
> 
> **Orden 2 (aproximación cuadrática):**
> 
> Para $f(x, y)$ centrado en $(a, b)$:
> 
> $$\begin{align}
> P_2(x,y) &= f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b) \\
> &\quad + \frac{1}{2}f_{xx}(a,b)(x-a)^2 + f_{xy}(a,b)(x-a)(y-b) \\
> &\quad + \frac{1}{2}f_{yy}(a,b)(y-b)^2
> \end{align}$$
> 
> Forma matricial usando la **matriz Hessiana** $H$:
> 
> $$P_2(\mathbf{x}) = f(\mathbf{a}) + \nabla f(\mathbf{a}) \cdot (\mathbf{x} - \mathbf{a}) + \frac{1}{2}(\mathbf{x} - \mathbf{a})^T H(\mathbf{a}) (\mathbf{x} - \mathbf{a})$$
> 
> donde 
> 
> $$H = \begin{bmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{bmatrix}$$

## 🎯 Propiedades Fundamentales

> [!success]- Teoremas Clave
> **Teorema 1: Unicidad**
> 
> El polinomio de Taylor de orden $k$ es el **único** polinomio de grado $\leq k$ que satisface:
> 
> $$D^{\alpha}P_k(\mathbf{a}) = D^{\alpha}f(\mathbf{a}) \quad \text{para todo } |\alpha| \leq k$$
> 
> Es decir, $P_k$ y $f$ tienen las mismas derivadas parciales hasta orden $k$ en $\mathbf{a}$.
> 
> ---
> 
> **Teorema 2: Aproximación Local (Fórmula de Taylor con Residuo)**
> 
> Si $f$ tiene derivadas parciales continuas hasta orden $k+1$ en una vecindad de $\mathbf{a}$:
> 
> $$f(\mathbf{x}) = P_k(\mathbf{x}) + R_k(\mathbf{x})$$
> 
> donde el **residuo** satisface:
> 
> $$\lim_{\mathbf{x} \to \mathbf{a}} \frac{R_k(\mathbf{x})}{\|\mathbf{x} - \mathbf{a}\|^k} = 0$$
> 
> **Forma de Lagrange del residuo:**
> 
> $$R_k(\mathbf{x}) = \sum_{|\alpha| = k+1} \frac{1}{\alpha!} D^{\alpha}f(\mathbf{c}) (\mathbf{x} - \mathbf{a})^{\alpha}$$
> 
> para algún $\mathbf{c}$ en el segmento entre $\mathbf{a}$ y $\mathbf{x}$.
> 
> ---
> 
> **Teorema 3: Convergencia (Serie de Taylor)**
> 
> Si $f$ es **analítica** en una vecindad de $\mathbf{a}$, entonces:
> 
> $$f(\mathbf{x}) = \sum_{|\alpha| = 0}^{\infty} \frac{1}{\alpha!} D^{\alpha}f(\mathbf{a}) (\mathbf{x} - \mathbf{a})^{\alpha}$$
> 
> converge a $f(\mathbf{x})$ en una vecindad de $\mathbf{a}$.
> 
> **Condición suficiente:** Si existe $M > 0$ y $r > 0$ tal que:
> 
> $$|D^{\alpha}f(\mathbf{x})| \leq M \frac{|\alpha|!}{r^{|\alpha|}} \quad \text{para } \|\mathbf{x} - \mathbf{a}\| < r$$
> 
> entonces la serie converge en la bola $\|\mathbf{x} - \mathbf{a}\| < r$.

> [!tip]- Propiedades de Cálculo
> **Linealidad:**
> 
> Si $P_k^f$ y $P_k^g$ son los polinomios de Taylor de $f$ y $g$:
> 
> $$P_k^{af + bg} = aP_k^f + bP_k^g$$
> 
> **Regla del producto (aproximada):**
> 
> $$P_k^{fg}(\mathbf{x}) \approx \left[\sum_{j=0}^{k} P_j^f(\mathbf{x})\right] \cdot \left[\sum_{j=0}^{k} P_j^g(\mathbf{x})\right] \mod \|\mathbf{x}-\mathbf{a}\|^{k+1}$$
> 
> (Mantener solo términos de orden $\leq k$)
> 
> **Composición:**
> 
> Para $h(x, y) = f(g_1(x,y), g_2(x,y))$, el polinomio de Taylor se obtiene componiendo los polinomios de $f$, $g_1$ y $g_2$.

## 📝 Construcción Práctica

> [!example]- Algoritmo Paso a Paso
> **Procedimiento para construir $P_k(x,y)$ centrado en $(a,b)$:**
> 
> **PASO 1: Evaluar la función en el punto**
> 
> $$P_0(x,y) = f(a,b)$$
> 
> **PASO 2: Calcular derivadas de primer orden**
> 
> - $f_x(a,b)$, $f_y(a,b)$
> 
> Agregar términos lineales:
> 
> $$P_1(x,y) = P_0 + f_x(a,b)(x-a) + f_y(a,b)(y-b)$$
> 
> **PASO 3: Calcular derivadas de segundo orden**
> 
> - $f_{xx}(a,b)$, $f_{xy}(a,b)$, $f_{yy}(a,b)$
> 
> Agregar términos cuadráticos:
> 
> $$P_2(x,y) = P_1 + \frac{1}{2}f_{xx}(a,b)(x-a)^2 + f_{xy}(a,b)(x-a)(y-b) + \frac{1}{2}f_{yy}(a,b)(y-b)^2$$
> 
> **PASO 4: Continuar para órdenes superiores**
> 
> Para orden $k$: calcular todas las derivadas parciales de orden $k$ y agregar:
> 
> $$\sum_{j=0}^{k} \frac{1}{j!(k-j)!} \frac{\partial^k f}{\partial x^j \partial y^{k-j}}\bigg|_{(a,b)} (x-a)^j(y-b)^{k-j}$$
> 
> **Organización por orden:**
> 
> | Orden | Número de términos (en 2D) | Derivadas necesarias |
> |-------|---------------------------|---------------------|
> | 0 | 1 | $f$ |
> | 1 | 2 | $f_x$, $f_y$ |
> | 2 | 3 | $f_{xx}$, $f_{xy}$, $f_{yy}$ |
> | 3 | 4 | $f_{xxx}$, $f_{xxy}$, $f_{xyy}$, $f_{yyy}$ |
> | $k$ | $k+1$ | Todas de orden $k$ |
> 
> En $n$ variables, hay $\binom{n+k-1}{k}$ términos de orden $k$.

## 💡 Ejemplos Resueltos

> [!example]- Problema 1: Función Exponencial
> **Encontrar el polinomio de Taylor de orden 2 de $f(x,y) = e^{x+y}$ centrado en $(0,0)$.**
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Evaluar en el origen**
> 
> $$f(0,0) = e^{0+0} = 1$$
> 
> **PASO 2: Derivadas de primer orden**
> 
> $$f_x(x,y) = e^{x+y} \implies f_x(0,0) = 1$$
> 
> $$f_y(x,y) = e^{x+y} \implies f_y(0,0) = 1$$
> 
> **PASO 3: Derivadas de segundo orden**
> 
> $$f_{xx}(x,y) = e^{x+y} \implies f_{xx}(0,0) = 1$$
> 
> $$f_{xy}(x,y) = e^{x+y} \implies f_{xy}(0,0) = 1$$
> 
> $$f_{yy}(x,y) = e^{x+y} \implies f_{yy}(0,0) = 1$$
> 
> **PASO 4: Construir polinomio**
> 
> $$\begin{align}
> P_2(x,y) &= 1 + 1 \cdot x + 1 \cdot y \\
> &\quad + \frac{1}{2}(1)x^2 + (1)xy + \frac{1}{2}(1)y^2 \\
> &= 1 + x + y + \frac{1}{2}x^2 + xy + \frac{1}{2}y^2
> \end{align}$$
> 
> **Forma factorizada:**
> 
> $$P_2(x,y) = 1 + (x + y) + \frac{1}{2}(x + y)^2$$
> 
> **VERIFICACIÓN:**
> 
> Comparar con serie de Taylor univariable: $e^u = 1 + u + \frac{u^2}{2} + \cdots$
> 
> Con $u = x + y$: ¡coincide exactamente! ✓
> 
> **Observación:** Para $e^{x+y}$, el patrón continúa:
> 
> $$P_3(x,y) = 1 + (x+y) + \frac{(x+y)^2}{2} + \frac{(x+y)^3}{6}$$

> [!example]- Problema 2: Función Trigonométrica
> **Encontrar el polinomio de Taylor de orden 2 de $f(x,y) = \cos(x)\sin(y)$ centrado en $(\pi/2, 0)$.**
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Evaluar en el punto**
> 
> $$f\left(\frac{\pi}{2}, 0\right) = \cos\left(\frac{\pi}{2}\right)\sin(0) = 0 \cdot 0 = 0$$
> 
> **PASO 2: Derivadas parciales de primer orden**
> 
> $$f_x(x,y) = -\sin(x)\sin(y)$$
> $$f_x\left(\frac{\pi}{2}, 0\right) = -\sin\left(\frac{\pi}{2}\right)\sin(0) = -1 \cdot 0 = 0$$
> 
> $$f_y(x,y) = \cos(x)\cos(y)$$
> $$f_y\left(\frac{\pi}{2}, 0\right) = \cos\left(\frac{\pi}{2}\right)\cos(0) = 0 \cdot 1 = 0$$
> 
> **PASO 3: Derivadas de segundo orden**
> 
> $$f_{xx}(x,y) = -\cos(x)\sin(y)$$
> $$f_{xx}\left(\frac{\pi}{2}, 0\right) = -\cos\left(\frac{\pi}{2}\right)\sin(0) = 0$$
> 
> $$f_{xy}(x,y) = -\sin(x)\cos(y)$$
> $$f_{xy}\left(\frac{\pi}{2}, 0\right) = -\sin\left(\frac{\pi}{2}\right)\cos(0) = -1 \cdot 1 = -1$$
> 
> $$f_{yy}(x,y) = -\cos(x)\sin(y)$$
> $$f_{yy}\left(\frac{\pi}{2}, 0\right) = -\cos\left(\frac{\pi}{2}\right)\sin(0) = 0$$
> 
> **PASO 4: Construir polinomio**
> 
> Sean $u = x - \frac{\pi}{2}$ y $v = y - 0 = y$:
> 
> $$\begin{align}
> P_2(x,y) &= 0 + 0 \cdot u + 0 \cdot v \\
> &\quad + \frac{1}{2}(0)u^2 + (-1)uv + \frac{1}{2}(0)v^2 \\
> &= -uv \\
> &= -\left(x - \frac{\pi}{2}\right)y
> \end{align}$$
> 
> **RESPUESTA:**
> 
> $$P_2(x,y) = -\left(x - \frac{\pi}{2}\right)y$$
> 
> **INTERPRETACIÓN:**
> 
> El polinomio es de grado 2 (término mixto $xy$), aunque parece lineal en cada variable separadamente. Es un **paraboloide hiperbólico** (silla de montar) cerca del punto.

> [!example]- Problema 3: Función Racional
> **Encontrar el polinomio de Taylor de orden 1 de $f(x,y) = \frac{1}{1+x+y}$ centrado en $(0,0)$.**
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Valor en el origen**
> 
> $$f(0,0) = \frac{1}{1+0+0} = 1$$
> 
> **PASO 2: Derivadas parciales**
> 
> $$f_x(x,y) = -\frac{1}{(1+x+y)^2}$$
> $$f_x(0,0) = -\frac{1}{1^2} = -1$$
> 
> Por simetría:
> $$f_y(x,y) = -\frac{1}{(1+x+y)^2}$$
> $$f_y(0,0) = -1$$
> 
> **PASO 3: Construir $P_1$**
> 
> $$P_1(x,y) = 1 + (-1)x + (-1)y = 1 - x - y$$
> 
> **RESPUESTA:**
> 
> $$P_1(x,y) = 1 - x - y$$
> 
> Este es el **plano tangente** a la superficie en el origen.
> 
> **VERIFICACIÓN con serie geométrica:**
> 
> $$\frac{1}{1+u} = 1 - u + u^2 - u^3 + \cdots$$
> 
> Con $u = x + y$:
> 
> $$\frac{1}{1+x+y} = 1 - (x+y) + (x+y)^2 - \cdots$$
> 
> Primer orden: $1 - x - y$ ✓
> 
> **EXTENSIÓN a orden 2:**
> 
> $$P_2(x,y) = 1 - (x+y) + (x+y)^2 = 1 - x - y + x^2 + 2xy + y^2$$

> [!example]- Problema 4: Estimación de Error
> **Estimar $f(0.1, 0.2)$ donde $f(x,y) = e^{xy}$ usando el polinomio de Taylor de orden 2 centrado en $(0,0)$. Acotar el error.**
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Construir $P_2$**
> 
> $$f(0,0) = e^0 = 1$$
> 
> $$f_x = ye^{xy} \implies f_x(0,0) = 0$$
> $$f_y = xe^{xy} \implies f_y(0,0) = 0$$
> 
> $$f_{xx} = y^2e^{xy} \implies f_{xx}(0,0) = 0$$
> $$f_{xy} = e^{xy} + xye^{xy} \implies f_{xy}(0,0) = 1$$
> $$f_{yy} = x^2e^{xy} \implies f_{yy}(0,0) = 0$$
> 
> $$P_2(x,y) = 1 + 0 + 0 + 0 + xy + 0 = 1 + xy$$
> 
> **PASO 2: Aproximar**
> 
> $$f(0.1, 0.2) \approx P_2(0.1, 0.2) = 1 + (0.1)(0.2) = 1.02$$
> 
> **PASO 3: Acotar error (usando $P_3$)**
> 
> Derivadas de tercer orden:
> $$f_{xxx} = y^3e^{xy}, \quad f_{xxy} = y(1+xy)e^{xy}, \quad \ldots$$
> 
> En la región $|x| \leq 0.1$, $|y| \leq 0.2$:
> $$|xy| \leq 0.02 \implies e^{xy} \leq e^{0.02} \approx 1.02$$
> 
> Máximo de derivadas terceras: $\approx 1.02 \cdot 0.2^3 \approx 0.008$
> 
> Error: 
> $$|R_2| \lesssim \frac{0.008}{3!} \cdot (0.1 + 0.2)^3 \approx 0.000036$$
> 
> **VERIFICACIÓN:**
> 
> Valor real: $e^{0.02} = 1.020201...$
> 
> Aproximación: $1.02$
> 
> Error real: $0.000201$ (dentro de la cota) ✓

## 🎨 Interpretación Geométrica

> [!note]- Visualización en $\mathbb{R}^3$
> **Para $z = f(x,y)$ y polinomios centrados en $(a,b)$:**
> 
> ```mermaid
> graph TD
>     A[Superficie z = f x y] --> B[Aproximaciones polinomiales]
>     B --> C[P₀: punto tangente]
>     B --> D[P₁: plano tangente]
>     B --> E[P₂: paraboloide]
>     B --> F[P₃: superficie cúbica]
>     
>     C --> G[Valor constante]
>     D --> H[Primera derivada<br/>Gradiente]
>     E --> I[Segunda derivada<br/>Curvatura]
>     F --> J[Tercera derivada<br/>Torsión]
>     
>     style A fill:#e1f5ff
>     style D fill:#c8e6c9
>     style E fill:#fff9c4
>     style F fill:#ffccbc
> ```
> 
> **Orden 0:** Aproximación constante
> - Plano horizontal a altura $z = f(a,b)$
> - No captura pendiente ni curvatura
> 
> **Orden 1:** Plano tangente
> - $z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$
> - Captura la **dirección de máximo crecimiento** (gradiente)
> - Buena aproximación solo muy cerca de $(a,b)$
> 
> **Orden 2:** Paraboloide
> - Incluye términos cuadráticos: $x^2$, $xy$, $y^2$
> - Captura **curvatura** de la superficie
> - Formas posibles:
>   - Paraboloide elíptico (mínimo/máximo local)
>   - Paraboloide hiperbólico (punto silla)
>   - Cilindro parabólico (degenerado)
> 
> **Convergencia visual:**
> 
> A medida que aumenta el orden $k$, $P_k$ se "pega" más a $f$:
> - Mayor fidelidad cerca del centro
> - Región de validez limitada (convergencia local)

> [!tip]- Relación con el Gradiente y Hessiano
> **Gradiente (orden 1):**
> 
> $$\nabla f(a,b) = \begin{bmatrix} f_x(a,b) \\ f_y(a,b) \end{bmatrix}$$
> 
> Vector que apunta en la **dirección de máximo crecimiento**.
> 
> $P_1$ es perpendicular al gradiente en el sentido:
> - Gradiente: dirección en el dominio
> - Plano tangente: superficie en el codominio
> 
> **Hessiano (orden 2):**
> 
> $$H(a,b) = \begin{bmatrix} f_{xx}(a,b) & f_{xy}(a,b) \\ f_{xy}(a,b) & f_{yy}(a,b) \end{bmatrix}$$
> 
> Matriz que codifica la **curvatura** en todas direcciones.
> 
> Forma cuadrática asociada:
> 
> $$Q(h,k) = \frac{1}{2}\begin{bmatrix} h & k \end{bmatrix} H \begin{bmatrix} h \\ k \end{bmatrix} = \frac{1}{2}(f_{xx}h^2 + 2f_{xy}hk + f_{yy}k^2)$$
> 
> **Clasificación de puntos críticos:**
> 
> Si $\nabla f(a,b) = \mathbf{0}$:
> - $H$ definido positivo → **mínimo local**
> - $H$ definido negativo → **máximo local**
> - $H$ indefinido → **punto silla**
> - $H$ semidefinido → **prueba inconclusa** (necesita $P_3$ o mayor)

## 🔗 Aplicaciones Prácticas

> [!success]- Optimización
> **Método de Newton en varias variables:**
> 
> Para encontrar mínimos de $f(\mathbf{x})$, iteramos:
> 
> $$\mathbf{x}_{n+1} = \mathbf{x}_n - H^{-1}(\mathbf{x}_n) \nabla f(\mathbf{x}_n)$$
> 
> **Justificación:** Aproximar $f$ por $P_2$ centrado en $\mathbf{x}_n$:
> 
> $$P_2(\mathbf{x}) \approx f(\mathbf{x}_n) + \nabla f(\mathbf{x}_n)^T(\mathbf{x} - \mathbf{x}_n) + \frac{1}{2}(\mathbf{x} - \mathbf{x}_n)^T H(\mathbf{x}_n)(\mathbf{x} - \mathbf{x}_n)$$
> 
> Minimizar $P_2$ (derivar e igualar a cero):
> 
> $$\nabla P_2 = \nabla f(\mathbf{x}_n) + H(\mathbf{x}_n)(\mathbf{x} - \mathbf{x}_n) = 0$$
> 
> $$\mathbf{x} = \mathbf{x}_n - H^{-1}(\mathbf{x}_n)\nabla f(\mathbf{x}_n)$$
> 
> **Ventaja:** Convergencia cuadrática (muy rápida)
> 
> **Desventaja:** Requiere calcular y invertir Hessiano (costoso)

> [!success]- Análisis de Sensibilidad
> **Propagación de errores:**
> 
> Si $x$ y $y$ tienen incertidumbres $\Delta x$ y $\Delta y$, la incertidumbre en $f(x,y)$ es aproximadamente:
> 
> $$\Delta f \approx |f_x|\Delta x + |f_y|\Delta y$$
> 
> (Derivado de $P_1$, ignorando términos de orden superior)
> 
> **Ejemplo:** Para $f(x,y) = xy$:
> 
> $$\Delta(xy) \approx y\Delta x + x\Delta y$$
> 
> Error relativo:
> 
> $$\frac{\Delta(xy)}{xy} \approx \frac{\Delta x}{x} + \frac{\Delta y}{y}$$

> [!success]- Física e Ingeniería
> **Expansión de potencial gravitacional:**
> 
> Para masa puntual en el origen, el potencial a distancia $r$ es:
> 
> $$\Phi(x,y,z) = -\frac{Gm}{\sqrt{x^2 + y^2 + z^2}}$$
> 
> Lejos del origen ($r$ grande), expansión en potencias de $1/r$:
> 
> $$\Phi \approx -\frac{Gm}{r} + O(1/r^2)$$
> 
> (Primer término del desarrollo de Taylor multivarible)
> 
> **Aproximación de pequeñas oscilaciones:**
> 
> Energía potencial $V(x,y)$ cerca de equilibrio $(a,b)$:
> 
> $$V(x,y) \approx V(a,b) + \frac{1}{2}[V_{xx}(x-a)^2 + 2V_{xy}(x-a)(y-b) + V_{yy}(y-b)^2]$$
> 
> (Aproximación armónica, base de la mecánica cuántica molecular)

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes
> **1. "El polinomio de Taylor aproxima bien en todo el dominio"**
> 
> ✗ **FALSO**
> 
> La aproximación es **local** cerca del centro $\mathbf{a}$.
> 
> Lejos de $\mathbf{a}$, el error puede ser enorme, incluso para órdenes altos.
> 
> **Contraejemplo:**
> 
> $f(x,y) = \frac{1}{1+x^2+y^2}$ centrado en $(0,0)$
> 
> Aunque analítica en el origen, la aproximación falla para $x^2 + y^2 \geq 1$.
> 
> ---
> 
> **2. "Olvidar factores $\frac{1}{\alpha!}$ o $\frac{1}{j!(m-j)!}$"**
> 
> ✗ **ERROR COMÚN**
> 
> Estos factoriales son **cruciales** para la corrección del polinomio.
> 
> **Correcto:**
> 
> $$\frac{1}{2}f_{xx}(x-a)^2 \quad \text{NO} \quad f_{xx}(x-a)^2$$
> 
> $$f_{xy}(x-a)(y-b) \quad \text{NO} \quad \frac{1}{2}f_{xy}(x-a)(y-b)$$
> 
> (El término mixto $f_{xy}$ no lleva $\frac{1}{2}$ porque aparece dos veces: $f_{xy}$ y $f_{yx}$)
> 
> ---
> 
> **3. "Confundir derivadas parciales con totales"**
> 
> ✗ **FALSO**
> 
> $f_{xy} \neq \frac{d^2f}{dxdy}$ (la notación $\frac{d}{dx}$ es para funciones de una variable)
> 
> **Correcto:** $f_{xy} = \frac{\partial^2 f}{\partial y \partial x}$
> 
> El orden importa solo si $f$ no es $C^2$ (pero por el teorema de Schwarz, si es $C^2$ entonces $f_{xy} = f_{yx}$).
> 
> ---
> 
> **4. "Mayor orden siempre significa mejor aproximación"**
> 
> ✗ **NO SIEMPRE**
> 
> Fuera del radio de convergencia, $P_k$ puede **diverger** al aumentar $k$.
> 
> **Ejemplo:** $f(x) = \frac{1}{1+25x^2}$ (fenómeno de Runge en 1D, se extiende a 2D)
> 
> ---
> 
> **5. "Usar el polinomio lejos del centro sin cuidado"**
> 
> ✗ **PELIGROSO**
> 
> Siempre verificar:
> - Distancia al centro: $\|\mathbf{x} - \mathbf{a}\|$
> - Magnitud del término siguiente: $|R_k(\mathbf{x})|$
> - Radio de convergencia (si es serie infinita)
> 
> ---
> 
> **6. "Olvidar restar el centro: usar $x^j y^{m-j}$ en lugar de $(x-a)^j(y-b)^{m-j}$"**
> 
> ✗ **ERROR GRAVE**
> 
> **Incorrecto:**
> $$P_1(x,y) = f(a,b) + f_x(a,b)x + f_y(a,b)y$$
> 
> **Correcto:**
> $$P_1(x,y) = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$$
> 
> El desplazamiento $(x-a)$, $(y-b)$ es esencial para que las derivadas coincidan en $\mathbf{a}$.

## 🔗 Conexiones con Otros Temas

> [!quote]- Enlaces Conceptuales
> **Fundamentos previos:**
> - **Derivadas parciales** - Construcción de cada término
> - **Gradiente** - Aproximación de orden 1
> - **Matriz Hessiana** - Aproximación de orden 2
> - **Teorema de Schwarz** - Simetría de derivadas mixtas
> 
> **Temas relacionados:**
> - **Extremos de funciones** - Prueba de la segunda derivada
> - **Multiplicadores de Lagrange** - Optimización restringida
> - **Integrales de línea** - Teorema fundamental del cálculo
> - **Diferenciabilidad** - Relación con existencia de $P_1$
> 
> **Aplicaciones posteriores:**
> - **Ecuaciones diferenciales parciales** - Soluciones locales (teorema de Cauchy-Kovalevskaya)
> - **Análisis complejo multivariable** - Funciones holomorfas
> - **Geometría diferencial** - Expansión de métricas
> - **Machine Learning** - Aproximación de funciones de pérdida (gradiente descendente, Newton)

## 📚 Recursos Adicionales

> [!note]- Herramientas y Referencias
> **Software de cálculo simbólico:**
> 
> - **Mathematica**
>   ```mathematica
>   Series[Exp[x*y], {x, 0, 2}, {y, 0, 2}]
>   ```
> - **Python (SymPy)**
>   ```python
>   from sympy import symbols, exp, series
>   x, y = symbols('x y')
>   f = exp(x*y)
>   series(f, x, 0, 3).removeO()
>   ```
> - **MATLAB**
>   ```matlab
>   syms x y
>   f = exp(x*y);
>   taylor(f, [x y], [0 0], 'Order', 3)
>   ```
> 
> **Visualizadores:**
> - **GeoGebra 3D** - Graficar $f$ y $P_k$ simultáneamente
> - **Wolfram Alpha** - "Taylor series exp(xy) at (0,0) order 2"
> - **Desmos 3D** - Comparar superficies interactivamente

## 📖 Bibliografía Esencial

> [!tip]- Lecturas Recomendadas
> **Nivel introductorio:**
> - **Stewart, J.** (2015). *Cálculo de Varias Variables* (7ª ed.). Cengage Learning.
>   - Cap. 14: Derivadas parciales
>   - Sección 14.9: Aproximación de Taylor
> - **Larson, R., & Edwards, B.** (2016). *Cálculo* (10ª ed.). Cengage.
>   - Cap. 13: Series de Taylor multivariables
> 
> **Nivel intermedio:**
> - **Marsden, J. E., & Tromba, A. J.** (2012). *Vector Calculus* (6th ed.). W. H. Freeman.
>   - Cap. 2: Diferenciación
>   - Aproximaciones polinomiales detalladas
> - **Apostol, T. M.** (1969). *Calculus, Vol. II* (2nd ed.). Wiley.
>   - Cap. 8: Series de potencias multivariables
>   - Tratamiento riguroso de convergencia
> 
> **Nivel avanzado:**
> - **Spivak, M.** (1965). *Calculus on Manifolds*. Westview Press.
>   - Aproximación diferencial abstracta
> - **Hörmander, L.** (1990). *An Introduction to Complex Analysis in Several Variables* (3rd ed.). North-Holland.
>   - Series de Taylor en el contexto complejo

## 🎓 Conceptos Clave - Resumen

> [!important]- Ideas Fundamentales
> 
> **DEFINICIÓN ESENCIAL:**
> 
> $$P_k(\mathbf{x}) = \sum_{|\alpha| = 0}^{k} \frac{1}{\alpha!} D^{\alpha}f(\mathbf{a}) (\mathbf{x} - \mathbf{a})^{\alpha}$$
> 
> **CASOS IMPORTANTES (2 variables):**
> 
> **Orden 1 (plano tangente):**
> $$P_1(x,y) = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)$$
> 
> **Orden 2 (paraboloide):**
> $$P_2(x,y) = P_1 + \frac{1}{2}[f_{xx}(x-a)^2 + 2f_{xy}(x-a)(y-b) + f_{yy}(y-b)^2]$$
> 
> **TEOREMA DEL RESIDUO:**
> 
> $$f(\mathbf{x}) = P_k(\mathbf{x}) + R_k(\mathbf{x}), \quad \lim_{\mathbf{x} \to \mathbf{a}} \frac{R_k(\mathbf{x})}{\|\mathbf{x} - \mathbf{a}\|^k} = 0$$
> 
> **APLICACIONES CLAVE:**
> - Aproximación local de funciones complejas
> - Optimización (método de Newton)
> - Análisis de extremos (prueba de la segunda derivada)
> - Propagación de errores

---

**Tags:** #calculo-vectorial #taylor #polinomios #aproximacion #derivadas-parciales #optimizacion #analisis-multivariable #gradiente #hessiano #serie-de-potencias #convergencia #analisis-local

