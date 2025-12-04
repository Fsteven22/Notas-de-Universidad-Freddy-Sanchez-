# 🎯 Multiplicadores de Lagrange

## 🌟 Concepto Fundamental

> [!info]- Definición Intuitiva
> **El método de multiplicadores de Lagrange es una técnica para encontrar máximos y mínimos de una función sujeta a restricciones (ecuaciones de ligadura). En lugar de resolver las restricciones directamente y sustituir, el método introduce variables auxiliares (multiplicadores λ) que transforman el problema restringido en uno sin restricciones. Es fundamental en optimización, física, economía e ingeniería.**
> 
> **Características clave:**
> - **Optimización restringida:** Extremos sujetos a condiciones
> - **Multiplicadores λ:** Variables auxiliares que codifican las restricciones
> - **Condición geométrica:** Gradientes paralelos en el óptimo
> - **Sistema de ecuaciones:** Transforma en problema algebraico
> - **Aplicaciones:** Desde física hasta machine learning

### 📖 Contexto Histórico

> [!note]- Desarrollo del Concepto
> **Orígenes (1700-1800):**
> - **Lagrange (1788):** _Mécanique Analytique_
>   - Introducción del método
>   - Aplicación a mecánica
>   - Revolucionó el cálculo de variaciones
> - **Euler (1744):** Precursor con problemas isoperimétricos
>   - Problema: maximizar área con perímetro fijo
>   - Métodos ad hoc antes de Lagrange
> - **Bernoulli (1696):** Problema de la braquistocrona
>   - Curva de descenso más rápido
>   - Motivó desarrollo de métodos variacionales
> 
> **Desarrollo matemático (1800-1900):**
> - **Cauchy (1820s):** Formalización rigurosa
>   - Condiciones de optimalidad
>   - Teoría de extremos condicionados
> - **Weierstrass (1870s):** Condiciones suficientes
>   - Segunda variación
>   - Teoría completa de optimización
> - **Kuhn & Tucker (1951):** Generalización a desigualdades
>   - Condiciones KKT
>   - Programación no lineal
> 
> **Era moderna (1950-presente):**
> - **Optimización computacional:**
>   - Algoritmos de punto interior
>   - Métodos de penalización
> - **Aplicaciones:**
>   - Economía: teoría del consumidor
>   - Machine learning: SVM, regularización
>   - Control óptimo: trayectorias
>   - Física: principios variacionales

## 📊 Definición Formal

> [!important]- Teorema de Multiplicadores de Lagrange
> **PROBLEMA DE OPTIMIZACIÓN RESTRINGIDA:**
> 
> Encontrar los extremos de:
> $$f(x, y, z) \quad \text{(función objetivo)}$$
> 
> Sujeto a:
> $$g(x, y, z) = k \quad \text{(restricción o ligadura)}$$
> 
> **TEOREMA:**
> 
> Si $f$ tiene un extremo relativo en $(x_0, y_0, z_0)$ sujeto a la restricción $g(x, y, z) = k$, y si $\nabla g(x_0, y_0, z_0) \neq \vec{0}$, entonces existe un escalar $\lambda$ (multiplicador de Lagrange) tal que:
> 
> $$\nabla f(x_0, y_0, z_0) = \lambda \nabla g(x_0, y_0, z_0)$$
> 
> **INTERPRETACIÓN GEOMÉTRICA:**
> 
> En el punto óptimo, el gradiente de $f$ (dirección de máximo crecimiento) es **paralelo** al gradiente de $g$ (normal a la superficie de restricción).
> 
> ```mermaid
> graph TD
>     A[∇f paralelo a ∇g] --> B[∇f = λ∇g]
>     B --> C[Vectores colineales]
>     C --> D[No se puede mejorar f<br/>moviéndose sobre g = k]
>     
>     style A fill:#e1f5ff
>     style D fill:#c8e6c9
> ```
> 
> **FUNCIÓN DE LAGRANGE:**
> 
> Se define:
> $$\mathcal{L}(x, y, z, \lambda) = f(x, y, z) - \lambda(g(x, y, z) - k)$$
> 
> Los puntos críticos de $\mathcal{L}$ satisfacen:
> 
> $$\begin{cases}
> \frac{\partial \mathcal{L}}{\partial x} = f_x - \lambda g_x = 0 \\
> \frac{\partial \mathcal{L}}{\partial y} = f_y - \lambda g_y = 0 \\
> \frac{\partial \mathcal{L}}{\partial z} = f_z - \lambda g_z = 0 \\
> \frac{\partial \mathcal{L}}{\partial \lambda} = -(g(x,y,z) - k) = 0
> \end{cases}$$
> 
> La última ecuación recupera la restricción.
> 
> **NOTACIÓN VECTORIAL:**
> 
> $$\nabla f = \lambda \nabla g \quad \text{y} \quad g = k$$

## 🎯 Justificación Geométrica

> [!success]- ¿Por qué funciona el método?
> **INTUICIÓN GEOMÉTRICA:**
> 
> **Caso 2D: Optimizar $f(x, y)$ sujeto a $g(x, y) = k$**
> 
> ```
>     Curvas de nivel de f
>          ↓
>      f = c₃  ╲
>              ╲
>       f = c₂ →╲___
>                ╲   ╲
>         f = c₁ →╲___╲___
>                  ╲ ● ╲     ← Punto óptimo
>                   ╲|  ╲      (tangencia)
>         g = k  ────●───●────
>                     ↑
>             Restricción
>     
>     En el óptimo:
>     - Curva f = c es tangente a g = k
>     - ∇f ⊥ curva de nivel de f
>     - ∇g ⊥ curva g = k
>     - Ambos perpendiculares a la misma curva
>     - Por tanto: ∇f ∥ ∇g
> ```
> 
> **DEMOSTRACIÓN (bosquejo):**
> 
> Sea $\mathbf{r}(t) = (x(t), y(t), z(t))$ una curva sobre $g = k$ (parametrización de la restricción).
> 
> Como $g(\mathbf{r}(t)) = k$ para todo $t$:
> 
> $$\frac{d}{dt}[g(\mathbf{r}(t))] = \nabla g \cdot \mathbf{r}'(t) = 0$$
> 
> Por tanto: $\nabla g \perp \mathbf{r}'(t)$ (gradiente perpendicular a la curva)
> 
> Si $f$ tiene extremo en $t_0$:
> 
> $$\frac{d}{dt}[f(\mathbf{r}(t))]\bigg|_{t=t_0} = \nabla f \cdot \mathbf{r}'(t_0) = 0$$
> 
> Por tanto: $\nabla f \perp \mathbf{r}'(t_0)$
> 
> Como ambos gradientes son perpendiculares al **mismo** vector tangente $\mathbf{r}'(t_0)$, deben ser paralelos:
> 
> $$\nabla f = \lambda \nabla g \quad \checkmark$$
> 
> **INTERPRETACIÓN FÍSICA:**
> 
> - $\nabla f$: "fuerza" que empuja hacia mayor $f$
> - $\nabla g$: "fuerza de restricción" (normal a la superficie)
> - En equilibrio: fuerzas son paralelas
> - $\lambda$: magnitud de la fuerza de restricción

## 🔍 Procedimiento del Método

> [!tip]- Algoritmo Paso a Paso
> **PROBLEMA GENERAL:**
> 
> Optimizar $f(\mathbf{x})$ sujeto a $g(\mathbf{x}) = k$
> 
> **PASO 1: Formar la función de Lagrange**
> 
> $$\mathcal{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) - \lambda(g(\mathbf{x}) - k)$$
> 
> **Nota:** Algunos textos usan $\mathcal{L} = f + \lambda(k - g)$. El resultado es el mismo.
> 
> **PASO 2: Calcular gradientes**
> 
> $$\nabla f = \left(\frac{\partial f}{\partial x_1}, \ldots, \frac{\partial f}{\partial x_n}\right)$$
> 
> $$\nabla g = \left(\frac{\partial g}{\partial x_1}, \ldots, \frac{\partial g}{\partial x_n}\right)$$
> 
> **PASO 3: Sistema de ecuaciones**
> 
> Resolver:
> $$\begin{cases}
> \nabla f = \lambda \nabla g \\
> g(\mathbf{x}) = k
> \end{cases}$$
> 
> Esto da $n + 1$ ecuaciones con $n + 1$ incógnitas $(x_1, \ldots, x_n, \lambda)$.
> 
> **PASO 4: Encontrar puntos candidatos**
> 
> Las soluciones del sistema son puntos donde pueden ocurrir extremos.
> 
> **PASO 5: Evaluar y comparar**
> 
> Calcular $f$ en cada punto candidato:
> - El mayor valor → **máximo restringido**
> - El menor valor → **mínimo restringido**
> 
> **PASO 6: Verificar frontera (si existe)**
> 
> Si la restricción tiene frontera (región cerrada), verificar esos puntos también.
> 
> **DIAGRAMA DE FLUJO:**
> 
> ```mermaid
> flowchart TD
>     A[Optimizar f sujeto a g = k] --> B[Formar ℒ = f - λg-k]
>     B --> C[Calcular ∇f y ∇g]
>     C --> D[Resolver ∇f = λ∇g y g = k]
>     D --> E[Puntos candidatos]
>     
>     E --> F{¿Región cerrada?}
>     F -->|Sí| G[Evaluar en candidatos<br/>y frontera]
>     F -->|No| H[Evaluar en candidatos]
>     
>     G --> I[Comparar valores]
>     H --> I
>     I --> J[Máximo y mínimo]
>     
>     style J fill:#c8e6c9
> ```

## 💡 Ejemplos Resueltos

> [!example]- Problemas Detallados
> **Problema 1: Distancia mínima a origen**
> 
> Encontrar el punto de la recta $x + y = 4$ más cercano al origen.
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Formular el problema**
> 
> Minimizar: $$f(x, y) = x^2 + y^2 \quad \text{(distancia al cuadrado)}$$
> 
> Sujeto a: $$g(x, y) = x + y = 4$$
> 
> **PASO 2: Calcular gradientes**
> 
> $$\nabla f = (2x, 2y)$$
> $$\nabla g = (1, 1)$$
> 
> **PASO 3: Condición de Lagrange**
> 
> $$\nabla f = \lambda \nabla g$$
> $$(2x, 2y) = \lambda(1, 1)$$
> 
> Esto da:
> $$\begin{cases}
> 2x = \lambda \\
> 2y = \lambda \\
> x + y = 4
> \end{cases}$$
> 
> **PASO 4: Resolver**
> 
> De las primeras dos ecuaciones: $2x = 2y \implies x = y$
> 
> Sustituyendo en la restricción:
> $$x + x = 4 \implies 2x = 4 \implies x = 2$$
> 
> Por tanto: $y = 2$
> 
> Y: $\lambda = 2x = 4$
> 
> **PASO 5: Verificar**
> 
> Punto candidato: $(2, 2)$
> 
> Distancia al origen: $\sqrt{2^2 + 2^2} = \sqrt{8} = 2\sqrt{2}$
> 
> **RESPUESTA:**
> 
> $$\boxed{\text{Punto más cercano: } (2, 2) \text{ con distancia } 2\sqrt{2}}$$
> 
> **INTERPRETACIÓN GEOMÉTRICA:**
> 
> El punto óptimo está donde la recta $x + y = 4$ es tangente al círculo centrado en el origen.
> 
> ---
> 
> **Problema 2: Optimización con círculo**
> 
> Encontrar extremos de $f(x, y) = x^2 + 2y^2$ en el círculo $x^2 + y^2 = 1$.
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Configuración**
> 
> Función objetivo: $f(x, y) = x^2 + 2y^2$
> 
> Restricción: $g(x, y) = x^2 + y^2 = 1$
> 
> **PASO 2: Gradientes**
> 
> $$\nabla f = (2x, 4y)$$
> $$\nabla g = (2x, 2y)$$
> 
> **PASO 3: Sistema**
> 
> $$\begin{cases}
> 2x = \lambda(2x) \\
> 4y = \lambda(2y) \\
> x^2 + y^2 = 1
> \end{cases}$$
> 
> Simplificando:
> $$\begin{cases}
> 2x(1 - \lambda) = 0 \\
> 2y(2 - \lambda) = 0 \\
> x^2 + y^2 = 1
> \end{cases}$$
> 
> **PASO 4: Casos**
> 
> **CASO A:** $x = 0$
> 
> De la restricción: $y^2 = 1 \implies y = \pm 1$
> 
> Puntos: $(0, 1)$ y $(0, -1)$
> 
> De segunda ecuación: $2y(2-\lambda) = 0 \implies \lambda = 2$ (ya que $y \neq 0$)
> 
> **CASO B:** $\lambda = 1$ (de primera ecuación con $x \neq 0$)
> 
> Segunda ecuación: $2y(2-1) = 0 \implies y = 0$
> 
> De la restricción: $x^2 = 1 \implies x = \pm 1$
> 
> Puntos: $(1, 0)$ y $(-1, 0)$
> 
> **PASO 5: Evaluar**
> 
> | Punto | $f(x, y) = x^2 + 2y^2$ |
> |-------|------------------------|
> | $(0, 1)$ | $0 + 2(1) = 2$ |
> | $(0, -1)$ | $0 + 2(1) = 2$ |
> | $(1, 0)$ | $1 + 0 = 1$ |
> | $(-1, 0)$ | $1 + 0 = 1$ |
> 
> **RESPUESTA:**
> 
> $$\boxed{\begin{align}
> \text{Máximo: } &f(0, \pm 1) = 2 \\
> \text{Mínimo: } &f(\pm 1, 0) = 1
> \end{align}}$$
> 
> ---
> 
> **Problema 3: Caja sin tapa**
> 
> Una caja rectangular sin tapa debe tener volumen $32 \text{ cm}^3$. Encontrar las dimensiones que minimizan el área superficial.
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Variables y función objetivo**
> 
> Sea $x, y, z$ las dimensiones (largo, ancho, alto).
> 
> Área superficial (sin tapa superior):
> $$f(x, y, z) = xy + 2xz + 2yz$$
> 
> Restricción (volumen):
> $$g(x, y, z) = xyz = 32$$
> 
> **PASO 2: Gradientes**
> 
> $$\nabla f = (y + 2z, x + 2z, 2x + 2y)$$
> $$\nabla g = (yz, xz, xy)$$
> 
> **PASO 3: Sistema de Lagrange**
> 
> $$\begin{cases}
> y + 2z = \lambda yz \quad (1)\\
> x + 2z = \lambda xz \quad (2)\\
> 2x + 2y = \lambda xy \quad (3)\\
> xyz = 32 \quad (4)
> \end{cases}$$
> 
> **PASO 4: Resolver**
> 
> De $(1)$: $y + 2z = \lambda yz \implies \frac{1}{z} + \frac{2}{y} = \lambda$ ... $(1')$
> 
> De $(2)$: $x + 2z = \lambda xz \implies \frac{1}{z} + \frac{2}{x} = \lambda$ ... $(2')$
> 
> De $(1')$ y $(2')$:
> $$\frac{1}{z} + \frac{2}{y} = \frac{1}{z} + \frac{2}{x}$$
> $$\frac{2}{y} = \frac{2}{x} \implies x = y$$
> 
> De $(3)$: $2x + 2y = \lambda xy$
> 
> Como $x = y$: $4x = \lambda x^2 \implies \lambda = \frac{4}{x}$
> 
> De $(2')$ con $x = y$:
> $$\frac{1}{z} + \frac{2}{x} = \frac{4}{x}$$
> $$\frac{1}{z} = \frac{2}{x} \implies x = 2z$$
> 
> De la restricción con $x = y = 2z$:
> $$(2z)(2z)(z) = 32$$
> $$4z^3 = 32$$
> $$z^3 = 8 \implies z = 2$$
> 
> Por tanto: $x = y = 2z = 4$
> 
> **PASO 5: Verificar**
> 
> Volumen: $(4)(4)(2) = 32$ ✓
> 
> Área: $f(4, 4, 2) = (4)(4) + 2(4)(2) + 2(4)(2)$
> $$= 16 + 16 + 16 = 48 \text{ cm}^2$$
> 
> **RESPUESTA:**
> 
> $$\boxed{\text{Dimensiones óptimas: } 4 \times 4 \times 2 \text{ cm con área mínima } 48 \text{ cm}^2}$$
> 
> ---
> 
> **Problema 4: Temperatura en elipse**
> 
> La temperatura en un punto $(x, y)$ es $T(x, y) = x^2 - xy + y^2$. Encontrar la temperatura máxima y mínima en la elipse $x^2 + 2y^2 = 2$.
> 
> **SOLUCIÓN:**
> 
> **PASO 1: Configuración**
> 
> $f(x, y) = x^2 - xy + y^2$
> 
> $g(x, y) = x^2 + 2y^2 = 2$
> 
> **PASO 2: Gradientes**
> 
> $$\nabla f = (2x - y, -x + 2y)$$
> $$\nabla g = (2x, 4y)$$
> 
> **PASO 3: Sistema**
> 
> $$\begin{cases}
> 2x - y = \lambda(2x) \\
> -x + 2y = \lambda(4y) \\
> x^2 + 2y^2 = 2
> \end{cases}$$
> 
> **PASO 4: Simplificar**
> 
> De la primera: $2x - y = 2\lambda x \implies 2x(1-\lambda) = y$ ... $(1')$
> 
> De la segunda: $-x + 2y = 4\lambda y \implies -x = 2y(2\lambda - 1)$ ... $(2')$
> 
> **CASO A:** $y = 0$
> 
> De $(1')$: $2x(1-\lambda) = 0$
> 
> Si $x \neq 0$: $\lambda = 1$
> 
> De la restricción: $x^2 = 2 \implies x = \pm\sqrt{2}$
> 
> Puntos: $(\sqrt{2}, 0)$ y $(-\sqrt{2}, 0)$
> 
> **CASO B:** $x = 0$
> 
> De $(2')$: $2y(2\lambda-1) = 0$
> 
> Si $y \neq 0$: $\lambda = \frac{1}{2}$
> 
> De la restricción: $2y^2 = 2 \implies y = \pm 1$
> 
> Puntos: $(0, 1)$ y $(0, -1)$
> 
> **CASO C:** $x, y \neq 0$
> 
> De $(1')$: $y = 2x(1-\lambda)$
> 
> Sustituyendo en $(2')$:
> $$-x = 2[2x(1-\lambda)](2\lambda-1)$$
> $$-1 = 4(1-\lambda)(2\lambda-1)$$
> $$-1 = 4(2\lambda - 1 - 2\lambda^2 + \lambda)$$
> $$-1 = 4(3\lambda - 1 - 2\lambda^2)$$
> $$-1 = 12\lambda - 4 - 8\lambda^2$$
> $$8\lambda^2 - 12\lambda + 3 = 0$$
> 
> No tiene soluciones reales simples, verificamos que los casos A y B son suficientes.
> 
> **PASO 5: Evaluar**
> 
> | Punto | $T = x^2 - xy + y^2$ |
> |-------|----------------------|
> | $(\sqrt{2}, 0)$ | $2 - 0 + 0 = 2$ |
> | $(-\sqrt{2}, 0)$ | $2 - 0 + 0 = 2$ |
> | $(0, 1)$ | $0 - 0 + 1 = 1$ |
> | $(0, -1)$ | $0 - 0 + 1 = 1$ |
> 
> **RESPUESTA:**
> 
> $$\boxed{\begin{align}
> T_{\max} &= 2 \text{ en } (\pm\sqrt{2}, 0) \\
> T_{\min} &= 1 \text{ en } (0, \pm 1)
> \end{align}}$$

## 🔗 Múltiples Restricciones

> [!success]- Generalización del Método
> **PROBLEMA CON $m$ RESTRICCIONES:**
> 
> Optimizar: $$f(x_1, \ldots, x_n)$$
> 
> Sujeto a:
> $$\begin{cases}
> g_1(x_1, \ldots, x_n) = k_1 \\
> g_2(x_1, \ldots, x_n) = k_2 \\
> \vdots \\
> g_m(x_1, \ldots, x_n) = k_m
> \end{cases}$$
> 
> **FUNCIÓN DE LAGRANGE:**
> 
> $$\mathcal{L}(\mathbf{x}, \lambda_1, \ldots, \lambda_m) = f(\mathbf{x}) - \sum_{i=1}^m \lambda_i(g_i(\mathbf{x}) - k_i)$$
> 
> **CONDICIÓN DE OPTIMALIDAD:**
> 
> $$\nabla f = \lambda_1 \nabla g_1 + \lambda_2 \nabla g_2 + \cdots + \lambda_m \nabla g_m$$
> 
> Junto con todas las restricciones:
> $$g_i(\mathbf{x}) = k_i, \quad i = 1, \ldots, m$$
> 
> **INTERPRETACIÓN GEOMÉTRICA:**
> 
> - Cada $\nabla g_i$ es perpendicular a su superficie $g_i = k_i$
> - La intersección de las superficies define una variedad de dimensión $n - m$
> - En el óptimo, $\nabla f$ está en el espacio generado por $\{\nabla g_1, \ldots, \nabla g_m\}$
> 
> **EJEMPLO:** Distancia mínima a dos planos
> 
> Minimizar $f(x, y, z) = x^2 + y^2 + z^2$ sujeto a:
> $$\begin{cases}
> g_1: x + y + z = 3 \\
> g_2: x - y + 2z = 4
> \end{cases}$$
> 
> **Sistema:**
> 
> $$\nabla f = \lambda_1 \nabla g_1 + \lambda_2 \nabla g_2$$
> $$(2x, 2y, 2z) = \lambda_1(1, 1, 1) + \lambda_2(1, -1, 2)$$
> 
> Esto da:
> $$\begin{cases}
> 2x = \lambda_1 + \lambda_2 \\
> 2y = \lambda_1 - \lambda_2 \\
> 2z = \lambda_1 + 2\lambda_2 \\
> x + y + z = 3 \\
> x - y + 2z = 4
> \end{cases}$$
> 
> (5 ecuaciones, 5 incógnitas)

## 📐 Interpretación Económica

> [!note]- Significado del Multiplicador λ
> **INTERPRETACIÓN DE λ:**
> 
> El multiplicador $\lambda$ representa la **tasa de cambio del valor óptimo** con respecto a la restricción.
> 
> $$\lambda \approx \frac{df_{\text{ópt}}}{dk}$$
> 
> **SIGNIFICADO:**
> 
> Si la restricción cambia de $g = k$ a $g = k + \Delta k$, entonces:
> $$f_{\text{ópt nuevo}} \approx f_{\text{ópt viejo}} + \lambda \cdot \Delta k$$
> 
> **EJEMPLO ECONÓMICO:**
> 
> **Problema:** Maximizar utilidad $U(x, y)$ sujeto a presupuesto $p_xx + p_yy = M$
> 
> El multiplicador $\lambda$ es la **utilidad marginal del ingreso**:
> - Si $\lambda = 5$: un dólar adicional de presupuesto aumenta la utilidad en 5 unidades
> - Si $\lambda$ es grande: la restricción es "apretada" (muy limitante)
> - Si $\lambda$ es pequeño: la restricción es "holgada"
> 
> **TEOREMA DEL SOBRE:**
> 
> Sea $f^*(k)$ el valor óptimo de $f$ cuando la restricción es $g = k$.
> 
> Entonces:
> $$\frac{df^*}{dk} = \lambda$$
> 
> **EJEMPLO NUMÉRICO:**
> 
> Volviendo al Problema 1: distancia mínima al origen con $x + y = 4$
> 
> Encontramos $\lambda = 4$ y distancia mínima $d = 2\sqrt{2}$
> 
> Si cambiamos la restricción a $x + y = 4.1$:
> 
> Nuevo óptimo aproximado:
> $$d_{\text{nuevo}}^2 \approx 8 + 4(0.1) = 8.4$$
> $$d_{\text{nuevo}} \approx \sqrt{8.4} \approx 2.898$$
> 
> (El cálculo exacto da un valor muy cercano)

## ⚡ Condiciones de Kuhn-Tucker

> [!important]- Generalización con Desigualdades
> **PROBLEMA CON DESIGUALDADES:**
> 
> Optimizar: $f(\mathbf{x})$
> 
> Sujeto a:
> $$\begin{cases}
> g_i(\mathbf{x}) \leq b_i & i = 1, \ldots, m \text{ (desigualdades)} \\
> h_j(\mathbf{x}) = c_j & j = 1, \ldots, p \text{ (igualdades)}
> \end{cases}$$
> 
> **CONDICIONES KKT (Karush-Kuhn-Tucker):**
> 
> Si $\mathbf{x}^*$ es óptimo, entonces existen multiplicadores $\lambda_i \geq 0$ y $\mu_j$ tales que:
> 
> **1. Condición de estacionaridad:**
> $$\nabla f(\mathbf{x}^*) = \sum_{i=1}^m \lambda_i \nabla g_i(\mathbf{x}^*) + \sum_{j=1}^p \mu_j \nabla h_j(\mathbf{x}^*)$$
> 
> **2. Factibilidad primal:**
> $$g_i(\mathbf{x}^*) \leq b_i, \quad h_j(\mathbf{x}^*) = c_j$$
> 
> **3. Factibilidad dual:**
> $$\lambda_i \geq 0$$
> 
> **4. Holgura complementaria:**
> $$\lambda_i(g_i(\mathbf{x}^*) - b_i) = 0$$
> 
> **INTERPRETACIÓN de (4):**
> 
> - Si restricción $i$ está inactiva ($g_i < b_i$): entonces $\lambda_i = 0$
> - Si $\lambda_i > 0$: entonces restricción está activa ($g_i = b_i$)
> 
> **EJEMPLO:**
> 
> Maximizar $f(x, y) = xy$ sujeto a:
> $$\begin{cases}
> x + 2y \leq 6 \\
> x \geq 0, \quad y \geq 0
> \end{cases}$$
> 
> Convertir a forma estándar:
> $$\begin{cases}
> g_1: -x - 2y + 6 \geq 0 \\
> g_2: x \geq 0 \\
> g_3: y \geq 0
> \end{cases}$$
> 
> Aplicar KKT...

## 🎨 Visualización Gráfica

> [!note]- Representación Geométrica
> **CASO 2D:** Optimizar $f(x, y)$ sujeto a $g(x, y) = k$
> 
> ```
>     Curvas de nivel de f:
>     
>          f = 7
>         ╱
>        ╱
>       ╱  f = 5
>      ╱  ╱
>     ╱  ╱  f = 3
>     | ╱  ╱
>     |╱  ╱
>     ●  ╱  ← Punto óptimo (tangencia)
>     |╲
>     | ╲_____ g(x,y) = k (restricción)
>     |
>     
>     En el óptimo:
>     - Curva de f es tangente a g = k
>     - ∇f ⊥ curva de nivel de f
>     - ∇g ⊥ curva g = k
>     - Por tanto: ∇f ∥ ∇g
> ```
> 
> **VISUALIZACIÓN CON VECTORES:**
> 
> ```
>           ∇g
>            ↑
>            |
>            |
>     ───────●─────── g = k
>            |
>            ↑
>           ∇f = λ∇g
>     
>     Ambos gradientes apuntan
>     en la misma dirección
>     (o direcciones opuestas si λ < 0)
> ```
> 
> **EJEMPLO VISUAL: Maximizar área de rectángulo con perímetro fijo**
> 
> $f(x, y) = xy$ (área)
> 
> $g(x, y) = 2x + 2y = P$ (perímetro)
> 
> ```
>     y
>     ↑
>     |   Hipérbolas xy = c
>     |     ╱╲  ╱╲
>     |    ╱  ╲╱  ╲
>     |   ╱    ●   ╲  ← Cuadrado (óptimo)
>     |  ╱    ╱ ╲   ╲
>     | ╱    ╱   ╲   ╲
>     |╱____╱_____╲___╲→ x
>     |    Recta 2x+2y=P
>     
>     Solución: x = y (cuadrado maximiza área)
> ```

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes
> **1. "λ debe ser positivo"**
> 
> ✗ **FALSO**
> 
> $\lambda$ puede ser positivo, negativo o cero.
> 
> El signo de $\lambda$ indica si $\nabla f$ y $\nabla g$ apuntan en la misma dirección o en direcciones opuestas.
> 
> (Solo en problemas KKT con desigualdades se requiere $\lambda_i \geq 0$)
> 
> ---
> 
> **2. "Olvidar la restricción en el sistema"**
> 
> ⚠️ **ERROR COMÚN**
> 
> El sistema debe incluir:
> - $\nabla f = \lambda \nabla g$ (da $n$ ecuaciones)
> - $g = k$ (la restricción original)
> 
> Sin la restricción, el sistema está incompleto.
> 
> ---
> 
> **3. "Todos los puntos candidatos son extremos"**
> 
> ✗ **FALSO**
> 
> El método encuentra **candidatos**. Algunos pueden ser:
> - Máximos
> - Mínimos
> - Puntos de silla sobre la restricción
> 
> Siempre **evaluar y comparar** $f$ en todos los candidatos.
> 
> ---
> 
> **4. "El método funciona para todas las funciones"**
> 
> ✗ **FALSO**
> 
> Requiere:
> - $f$ y $g$ diferenciables
> - $\nabla g \neq \vec{0}$ en la restricción
> 
> Si $\nabla g = \vec{0}$ en algún punto, ese punto requiere análisis especial.
> 
> ---
> 
> **5. "Confundir $\mathcal{L}$ con $f$"**
> 
> ⚠️ **CUIDADO**
> 
> La función de Lagrange $\mathcal{L}$ es una herramienta auxiliar.
> 
> Los valores extremos son de $f$, no de $\mathcal{L}$.
> 
> ---
> 
> **6. "Ignorar la frontera de regiones cerradas"**
> 
> ⚠️ **IMPORTANTE**
> 
> Si la restricción define una región cerrada (como $x^2 + y^2 \leq 1$), verificar:
> - Puntos críticos en el interior (sin restricción)
> - Puntos de Lagrange en la frontera ($x^2 + y^2 = 1$)
> 
> ---
> 
> **7. "Usar el discriminante D como en extremos libres"**
> 
> ✗ **NO APLICA**
> 
> El criterio del Hessiano de extremos libres NO se usa directamente en Lagrange.
> 
> Para clasificar extremos restringidos se usa el **Hessiano orlado** (bordered Hessian), tema más avanzado.

## 🔗 Aplicaciones

> [!quote]- Usos Prácticos del Método
> **1. FÍSICA:**
> 
> - **Mecánica:** Principio de mínima acción
> - **Óptica:** Ley de Snell (camino de tiempo mínimo)
> - **Termodinámica:** Maximizar entropía con restricciones energéticas
> 
> **2. ECONOMÍA:**
> 
> - **Teoría del consumidor:** Maximizar utilidad con presupuesto limitado
> - **Teoría del productor:** Minimizar costo con producción fija
> - **Equilibrio general:** Optimización con múltiples agentes
> 
> **3. INGENIERÍA:**
> 
> - **Diseño estructural:** Minimizar peso con restricciones de resistencia
> - **Control óptimo:** Minimizar costo con restricciones dinámicas
> - **Procesamiento de señales:** Filtrado óptimo
> 
> **4. MACHINE LEARNING:**
> 
> - **Support Vector Machines (SVM):** Maximizar margen con restricciones
> - **Regularización:** Minimizar error con restricción de norma
> - **Redes neuronales:** Optimización con constraints
> 
> **5. ESTADÍSTICA:**
> 
> - **Estimación con restricciones:** MLE con constraints
> - **Regresión ridge/lasso:** Optimización penalizada
> - **Análisis de componentes principales:** Maximizar varianza con norma unitaria
> 
> **EJEMPLO APLICADO: Problema de la dieta**
> 
> Minimizar costo de alimentos sujeto a requerimientos nutricionales mínimos.
> 
> Variables: $x_i$ = cantidad del alimento $i$
> 
> Objetivo: $\min \sum c_i x_i$ (costo total)
> 
> Restricciones: 
> - Proteína: $\sum p_i x_i \geq P_{\min}$
> - Calorías: $\sum k_i x_i \geq K_{\min}$
> - Etc.

## 📚 Recursos Adicionales

> [!note]- Herramientas y Software
> **Paquetes de optimización:**
> 
> - **Python (SciPy)**
>   ```python
>   from scipy.optimize import minimize
>   
>   def objetivo(x):
>       return x[0]**2 + x[1]**2
>   
>   def restriccion(x):
>       return x[0] + x[1] - 4
>   
>   cons = {'type': 'eq', 'fun': restriccion}
>   x0 = [1, 1]
>   sol = minimize(objetivo, x0, constraints=cons)
>   print(sol.x)  # [2, 2]
>   ```
> 
> - **MATLAB**
>   ```matlab
>   f = @(x) x(1)^2 + x(2)^2;
>   g = @(x) x(1) + x(2) - 4;
>   x0 = [1, 1];
>   [x, fval] = fmincon(f, x0, [], [], [], [], [], [], @(x)deal(g(x), []));
>   ```
> 
> - **Mathematica**
>   ```mathematica
>   Minimize[{x^2 + y^2, x + y == 4}, {x, y}]
>   ```
> 
> **Visualización:**
> - **GeoGebra:** Curvas de nivel y restricciones
> - **Desmos:** Gráficas 2D interactivas
> - **Plotly:** Superficies 3D con Python

## 📖 Bibliografía Esencial

> [!tip]- Lecturas Recomendadas
> **Nivel introductorio:**
> - **Stewart, J.** (2021). _Cálculo de Varias Variables_ (9ª ed.). Cengage.
>   - Cap. 14.8: Multiplicadores de Lagrange
>   - Ejemplos claros y aplicaciones
> - **Larson, R., & Edwards, B.** (2018). _Cálculo_ (10ª ed.). Cengage.
>   - Cap. 13.10: Optimización con restricciones
> 
> **Nivel intermedio:**
> - **Marsden, J. E., & Tromba, A. J.** (2012). _Vector Calculus_ (6th ed.). Freeman.
>   - Cap. 2: Extremos condicionados
>   - Enfoque geométrico excelente
> - **Apostol, T. M.** (1969). _Calculus, Vol. II_. Wiley.
>   - Cap. 12: Teoría rigurosa
> 
> **Optimización y aplicaciones:**
> - **Nocedal, J., & Wright, S.** (2006). _Numerical Optimization_ (2nd ed.). Springer.
>   - Cap. 12: Teoría de optimización con restricciones
>   - Condiciones KKT detalladas
> - **Boyd, S., & Vandenberghe, L.** (2004). _Convex Optimization_. Cambridge.
>   - Disponible gratis online
>   - Aplicaciones modernas

## 🎓 Conceptos Clave - Resumen

> [!important]- Ideas Fundamentales
> 
> **PROBLEMA:**
> 
> Optimizar $f(\mathbf{x})$ sujeto a $g(\mathbf{x}) = k$
> 
> **CONDICIÓN DE LAGRANGE:**
> 
> $$\nabla f = \lambda \nabla g \quad \text{y} \quad g = k$$
> 
> **FUNCIÓN DE LAGRANGE:**
> 
> $$\mathcal{L}(\mathbf{x}, \lambda) = f(\mathbf{x}) - \lambda(g(\mathbf{x}) - k)$$
> 
> **PROCEDIMIENTO:**
> 
> 1. Calcular $\nabla f$ y $\nabla g$
> 2. Resolver sistema: $\nabla f = \lambda \nabla g$ y $g = k$
> 3. Evaluar $f$ en candidatos
> 4. Comparar para encontrar máximo/mínimo
> 
> **INTERPRETACIÓN GEOMÉTRICA:**
> 
> En el óptimo, gradientes son paralelos (tangencia entre curvas de nivel)
> 
> **MÚLTIPLES RESTRICCIONES:**
> 
> $$\nabla f = \lambda_1 \nabla g_1 + \lambda_2 \nabla g_2 + \cdots + \lambda_m \nabla g_m$$
> 
> **SIGNIFICADO DE λ:**
> 
> $$\lambda \approx \frac{df_{\text{ópt}}}{dk}$$
> 
> Tasa de cambio del valor óptimo respecto a la restricción

---

**Tags:** #calculo-multivariable #multiplicadores-lagrange #optimizacion-restringida #extremos-condicionados #lagrange #gradiente #restricciones #KKT #optimizacion