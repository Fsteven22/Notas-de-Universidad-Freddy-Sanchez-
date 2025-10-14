# 🌐 Nociones Topológicas en ℝⁿ

## 🎯 Fundamentos de Topología en Espacios Euclidianos

> [!info]- 💡 Introducción a la Topología de ℝⁿ La **topología** es la rama de las matemáticas que estudia las propiedades de los espacios que se preservan bajo deformaciones continuas. En ℝⁿ, la topología proporciona un marco riguroso para conceptos intuitivos como "cercanía", "continuidad" y "límite".
> 
> **Analogías útiles:**
> 
> - **Bola abierta:** Interior de una esfera sin su superficie (como una burbuja)
> - **Conjunto abierto:** Región donde puedes moverte sin tocar el borde
> - **Conjunto cerrado:** Región que incluye su frontera (como un país con fronteras)
> - **Conjunto compacto:** Región "finita" y "cerrada" (como una isla)
> 
> **Importancia histórica:**
> 
> - **Bolzano (1817):** Primeros conceptos de continuidad rigurosa
> - **Cauchy (1821):** Límites y convergencia
> - **Weierstrass (1850s):** Formalización del análisis
> - **Cantor (1872):** Teoría de conjuntos y puntos límite
> - **Hausdorff (1914):** Espacios topológicos abstractos
> 
> **¿Por qué estudiar topología en ℝⁿ?**
> 
> - Fundamenta rigurosamente el cálculo multivariable
> - Permite demostrar teoremas importantes (compacidad, conexidad)
> - Esencial para análisis avanzado y ecuaciones diferenciales
> - Base para geometría diferencial y análisis funcional
> - Aplicaciones en optimización, física matemática, y ciencia de datos

### 📊 Jerarquía de Conceptos

> [!note]- 🌟 Estructura de Ideas Topológicas
> 
> ```mermaid
> graph TD
>     A[ℝⁿ con métrica euclidiana] --> B[Bolas abiertas]
>     B --> C[Conjuntos abiertos]
>     C --> D[Conjuntos cerrados]
>     C --> E[Interior de un conjunto]
>     D --> F[Clausura de un conjunto]
>     D --> G[Frontera de un conjunto]
>     C --> H[Puntos de acumulación]
>     H --> I[Conjuntos derivados]
>     D --> J[Conjuntos compactos]
>     C --> K[Conjuntos conexos]
>     J --> L[Teorema de Heine-Borel]
>     K --> M[Conjuntos arco-conexos]
> ```
> 
> **Niveles de abstracción:**
> 
> |Nivel|Concepto|Intuición|
> |---|---|---|
> |0|**Métrica**|Noción de distancia|
> |1|**Bolas**|Vecindades básicas|
> |2|**Abiertos**|Uniones arbitrarias de bolas|
> |3|**Topología**|Colección de abiertos|
> |4|**Propiedades**|Compacidad, conexidad, etc.|

## 📏 Métrica Euclidiana en ℝⁿ

### 🔢 Definición de Distancia

> [!example]- 🟢 Métrica Euclidiana
> 
> **Definición:** Para **x** = (x₁, x₂, ..., xₙ) y **y** = (y₁, y₂, ..., yₙ) en ℝⁿ:
> 
> $$d(\mathbf{x}, \mathbf{y}) = |\mathbf{x} - \mathbf{y}| = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}$$
> 
> **Casos particulares:**
> 
> - **ℝ¹:** d(x, y) = |x - y|
> - **ℝ²:** d((x₁,x₂), (y₁,y₂)) = √[(x₁-y₁)² + (x₂-y₂)²]
> - **ℝ³:** d((x₁,x₂,x₃), (y₁,y₂,y₃)) = √[(x₁-y₁)² + (x₂-y₂)² + (x₃-y₃)²]
> 
> **Axiomas de métrica:**
> 
> 1. **No negatividad:** d(x, y) ≥ 0, y d(x, y) = 0 ⟺ x = y
> 2. **Simetría:** d(x, y) = d(y, x)
> 3. **Desigualdad triangular:** d(x, z) ≤ d(x, y) + d(y, z)
> 
> **Propiedades de la norma euclidiana:**
> 
> 4. ‖x‖ ≥ 0, y ‖x‖ = 0 ⟺ x = 0
> 5. ‖αx‖ = |α|·‖x‖ (homogeneidad)
> 6. ‖x + y‖ ≤ ‖x‖ + ‖y‖ (desigualdad triangular)
> 
> **Desigualdades importantes:**
> 
> **Cauchy-Schwarz:** $$|\mathbf{x} \cdot \mathbf{y}| \leq |\mathbf{x}| \cdot |\mathbf{y}|$$
> 
> **Minkowski (desigualdad triangular):** $$|\mathbf{x} + \mathbf{y}| \leq |\mathbf{x}| + |\mathbf{y}|$$

### 🎨 Otras Métricas en ℝⁿ

> [!tip]- 📏 Familia de Métricas
> 
> **1. Métrica del taxista (Manhattan, ℓ¹):**
> 
> $$d_1(\mathbf{x}, \mathbf{y}) = \sum_{i=1}^n |x_i - y_i|$$
> 
> - Nombre: distancia recorrida en calles perpendiculares
> - Ejemplo en ℝ²: d₁((0,0), (3,4)) = 3 + 4 = 7
> 
> **2. Métrica del máximo (Chebyshev, ℓ∞):**
> 
> $$d_\infty(\mathbf{x}, \mathbf{y}) = \max_{1 \leq i \leq n} |x_i - y_i|$$
> 
> - Nombre: distancia de rey en ajedrez
> - Ejemplo en ℝ²: d∞((0,0), (3,4)) = max(3, 4) = 4
> 
> **3. Métrica ℓᵖ (Minkowski generalizada):**
> 
> $$d_p(\mathbf{x}, \mathbf{y}) = \left(\sum_{i=1}^n |x_i - y_i|^p\right)^{1/p}$$
> 
> donde p ≥ 1
> 
> - p = 1: métrica del taxista
> - p = 2: métrica euclidiana
> - p → ∞: métrica del máximo
> 
> **Comparación en ℝ²:**
> 
> Para punto (x, y) a distancia r del origen:
> 
> - **ℓ¹:** |x| + |y| = r (diamante/rombo)
> - **ℓ²:** x² + y² = r² (círculo)
> - **ℓ∞:** max(|x|, |y|) = r (cuadrado)
> 
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> 
> # Visualizar "bolas unitarias" en diferentes métricas
> theta = np.linspace(0, 2*np.pi, 1000)
> 
> # Métrica euclidiana (círculo)
> x_l2 = np.cos(theta)
> y_l2 = np.sin(theta)
> 
> # Métrica del taxista (diamante)
> x_l1 = np.sign(np.cos(theta)) * (1 - np.abs(np.sin(theta)))
> y_l1 = np.sign(np.sin(theta)) * (1 - np.abs(np.cos(theta)))
> 
> # Métrica del máximo (cuadrado)
> x_linf = np.sign(np.cos(theta))
> y_linf = np.sign(np.sin(theta))
> 
> plt.figure(figsize=(10, 10))
> plt.plot(x_l2, y_l2, label='ℓ² (Euclidiana)', linewidth=2)
> plt.plot(x_l1, y_l1, label='ℓ¹ (Taxista)', linewidth=2)
> plt.plot(x_linf, y_linf, label='ℓ∞ (Máximo)', linewidth=2)
> plt.axis('equal')
> plt.grid(True, alpha=0.3)
> plt.legend(fontsize=12)
> plt.title('Bolas Unitarias en Diferentes Métricas', fontsize=14)
> plt.xlabel('x')
> plt.ylabel('y')
> plt.show()
> ```
> 
> **Equivalencia de métricas:**
> 
> En ℝⁿ, todas las métricas ℓᵖ son **equivalentes**, es decir:
> 
> $$\exists, c_1, c_2 > 0: \quad c_1 d_p(\mathbf{x}, \mathbf{y}) \leq d_q(\mathbf{x}, \mathbf{y}) \leq c_2 d_p(\mathbf{x}, \mathbf{y})$$
> 
> Esto significa que generan la **misma topología** (mismos abiertos).

## 🔵 Bolas Abiertas y Cerradas

### 📐 Definiciones Básicas

> [!example]- ⚪ Bolas en ℝⁿ
> 
> **Bola abierta:**
> 
> $$B(\mathbf{a}, r) = {\mathbf{x} \in \mathbb{R}^n : d(\mathbf{x}, \mathbf{a}) < r}$$
> 
> - Centro: **a**
> - Radio: r > 0
> - **NO incluye** los puntos de la frontera
> - También notada: B_r(**a**) o U_r(**a**)
> 
> **Bola cerrada:**
> 
> $$\overline{B}(\mathbf{a}, r) = {\mathbf{x} \in \mathbb{R}^n : d(\mathbf{x}, \mathbf{a}) \leq r}$$
> 
> - **SÍ incluye** los puntos de la frontera
> - También notada: B̄_r(**a**)
> 
> **Esfera:**
> 
> $$S(\mathbf{a}, r) = {\mathbf{x} \in \mathbb{R}^n : d(\mathbf{x}, \mathbf{a}) = r}$$
> 
> - Solo la frontera
> - S(**a**, r) = ∂B(**a**, r)
> - También notada: S_r(**a**) o Sⁿ⁻¹
> 
> **Ejemplos en diferentes dimensiones:**
> 
> |Dimensión|Bola abierta|Bola cerrada|Esfera|
> |---|---|---|---|
> |**ℝ¹**|Intervalo abierto (a-r, a+r)|Intervalo cerrado [a-r, a+r]|Dos puntos {a-r, a+r}|
> |**ℝ²**|Disco abierto (interior)|Disco cerrado|Círculo (circunferencia)|
> |**ℝ³**|Esfera abierta (interior)|Esfera cerrada|Superficie esférica|
> |**ℝⁿ**|n-esfera abierta|n-esfera cerrada|(n-1)-esfera|

### ✅ Ejemplos Concretos

> [!example]- 💪 Casos Prácticos
> 
> **Ejemplo 1 - Bola abierta en ℝ²:**
> 
> B((0,0), 2) = {(x, y) ∈ ℝ² : x² + y² < 4}
> 
> - Interior de círculo de radio 2
> - Punto (1, 1) ∈ B (pues √2 < 2)
> - Punto (2, 0) ∉ B (pues 2 = 2, no < 2)
> 
> **Ejemplo 2 - Bola cerrada en ℝ³:**
> 
> B̄((1, -1, 2), 3) = {(x, y, z) : (x-1)² + (y+1)² + (z-2)² ≤ 9}
> 
> - Incluye interior y superficie
> - Punto (1, -1, 5) ∈ B̄ (pues d = 3 ≤ 3)
> - Punto (4, 2, 2) ∉ B̄ (pues d = √18 > 3)
> 
> **Ejemplo 3 - Intersección de bolas:**
> 
> B₁ = B((0,0), 2) y B₂ = B((2,0), 2) en ℝ²
> 
> B₁ ∩ B₂ = {(x,y) : x² + y² < 4 y (x-2)² + y² < 4}
> 
> Es una "lente" (región lenticular)
> 
> **Ejemplo 4 - Unión de bolas:**
> 
> Para cualquier colección de bolas {B_α}, la unión ⋃B_α es un conjunto abierto.
> 
> **Ejemplo 5 - Bola en métrica del taxista (ℝ²):**
> 
> B₁((0,0), 1) = {(x,y) : |x| + |y| < 1}
> 
> - Forma de diamante/rombo
> - Vértices en (±1, 0) y (0, ±1)
> 
> **Ejemplo 6 - Bola en métrica del máximo (ℝ²):**
> 
> B∞((0,0), 1) = {(x,y) : max(|x|, |y|) < 1}
> 
> - Forma de cuadrado
> - Vértices en (±1, ±1)

### 🎨 Propiedades de las Bolas

> [!note]- 📋 Características Importantes
> 
> **1. Bolas abiertas son conjuntos abiertos:**
> 
> Para todo **x** ∈ B(**a**, r), existe ε > 0 tal que B(**x**, ε) ⊂ B(**a**, r)
> 
> **Demostración:**
> 
> ```
> Sea d(x, a) = d₀ < r
> Tomar ε = r - d₀ > 0
> Si y ∈ B(x, ε), entonces:
>   d(y, a) ≤ d(y, x) + d(x, a) < ε + d₀ = r
> Por tanto B(x, ε) ⊂ B(a, r)
> ```
> 
> **2. Bolas cerradas son conjuntos cerrados:**
> 
> El complemento de B̄(**a**, r) es abierto.
> 
> **3. Contenencia:**
> 
> - B(**a**, r) ⊂ B̄(**a**, r)
> - B̄(**a**, r) = B(**a**, r) ∪ S(**a**, r)
> - S(**a**, r) = B̄(**a**, r) \ B(**a**, r)
> 
> **4. Propiedades algebraicas:**
> 
> - B(**a**, r₁) ∪ B(**a**, r₂) = B(**a**, max(r₁, r₂))
> - B(**a**, r₁) ∩ B(**a**, r₂) = B(**a**, min(r₁, r₂))
> 
> **5. Escalamiento:**
> 
> - B(**a**, αr) = **a** + α·B(**0**, r) para α > 0
> 
> **6. Traslación:**
> 
> - B(**a** + **b**, r) = **b** + B(**a**, r)

## 🔓 Conjuntos Abiertos

### 📐 Definición Formal

> [!success]- 🟢 Conjuntos Abiertos en ℝⁿ
> 
> **Definición:** Un conjunto A ⊂ ℝⁿ es **abierto** si para todo **x** ∈ A, existe ε > 0 tal que:
> 
> $$B(\mathbf{x}, \varepsilon) \subseteq A$$
> 
> **Intuición:**
> 
> - Puedes moverte en cualquier dirección desde cualquier punto sin salir del conjunto
> - No tiene "borde" (frontera no incluida)
> - Todo punto es un "punto interior"
> 
> **Caracterización alternativa:** A es abierto ⟺ A es unión de bolas abiertas
> 
> **Ejemplos de conjuntos abiertos:**
> 
> 1. **Bolas abiertas:** B(**a**, r)
> 2. **ℝⁿ completo:** todo el espacio
> 3. **Conjunto vacío:** ∅
> 4. **Intervalos abiertos en ℝ:** (a, b)
> 5. **Productos cartesianos de abiertos:** (a, b) × (c, d) en ℝ²
> 6. **Complementos de cerrados**
> 7. **Uniones arbitrarias de abiertos**
> 8. **Intersecciones finitas de abiertos**
> 
> **Ejemplos de conjuntos NO abiertos:**
> 
> 1. **Intervalos cerrados:** [a, b]
> 2. **Intervalos semi-abiertos:** [a, b)
> 3. **Bolas cerradas:** B̄(**a**, r)
> 4. **Esferas:** S(**a**, r)
> 5. **Conjuntos finitos:** {p₁, p₂, ..., pₙ}
> 6. **ℤⁿ ⊂ ℝⁿ:** puntos con coordenadas enteras

### 🎯 Propiedades de los Abiertos

> [!tip]- 📊 Axiomas de Topología
> 
> **Propiedades fundamentales (Axiomas de Topología):**
> 
> Sean 𝒯 = {A ⊂ ℝⁿ : A es abierto}. Entonces:
> 
> **A1. ∅ ∈ 𝒯 y ℝⁿ ∈ 𝒯**
> 
> - El vacío y el total son abiertos
> 
> **A2. Si {A_α}_{α∈I} ⊂ 𝒯, entonces ⋃_{α∈I} A_α ∈ 𝒯**
> 
> - La unión arbitraria (incluso infinita) de abiertos es abierta
> 
> **A3. Si A₁, A₂, ..., Aₙ ∈ 𝒯, entonces ⋂ᵢ₌₁ⁿ Aᵢ ∈ 𝒯**
> 
> - La intersección **finita** de abiertos es abierta
> 
> **⚠️ ADVERTENCIA:** La intersección infinita de abiertos puede NO ser abierta
> 
> **Contraejemplo:**
> 
> Considerar Aₙ = (-1/n, 1/n) en ℝ para n = 1, 2, 3, ...
> 
> Cada Aₙ es abierto, pero:
> 
> $$\bigcap_{n=1}^\infty A_n = {0}$$
> 
> que NO es abierto (un punto no es abierto en ℝ).
> 
> **Otro contraejemplo:**
> 
> En ℝ², considerar Bₙ = B((0,0), 1 + 1/n)
> 
> $$\bigcap_{n=1}^\infty B_n = \overline{B}((0,0), 1)$$
> 
> que es cerrado, no abierto.

### ✅ Ejemplos Detallados

> [!example]- 💪 Casos Prácticos de Abiertos
> 
> **Ejemplo 1 - Cuadrante abierto en ℝ²:**
> 
> Q₁ = {(x, y) : x > 0, y > 0}
> 
> **Demostración de que es abierto:**
> 
> ```
> Sea (x₀, y₀) ∈ Q₁, entonces x₀ > 0, y₀ > 0
> Tomar ε = min(x₀, y₀) > 0
> 
> Si (x, y) ∈ B((x₀, y₀), ε), entonces:
>   |x - x₀| < ε ≤ x₀ ⟹ x > 0
>   |y - y₀| < ε ≤ y₀ ⟹ y > 0
> 
> Por tanto B((x₀, y₀), ε) ⊂ Q₁
> ```
> 
> **Ejemplo 2 - Banda horizontal abierta:**
> 
> B = {(x, y) ∈ ℝ² : 1 < y < 3}
> 
> Es abierto (producto cartesiano ℝ × (1, 3))
> 
> **Ejemplo 3 - Complemento de un punto:**
> 
> A = ℝⁿ \ {**p**} es abierto
> 
> Para cualquier **x** ≠ **p**, tomar ε = d(**x**, **p**)/2
> 
> **Ejemplo 4 - Conjunto de puntos con norma acotada:**
> 
> A = {**x** ∈ ℝⁿ : ‖**x**‖ < M} = B(**0**, M)
> 
> Es la bola abierta centrada en el origen, por tanto abierto.
> 
> **Ejemplo 5 - Unión infinita:**
> 
> A = ⋃_{n=1}^∞ (1/n, 2 - 1/n) = (0, 2)
> 
> Unión de abiertos ⟹ abierto
> 
> **Ejemplo 6 - Conjunto definido por desigualdad estricta:**
> 
> A = {(x, y, z) : x² + 2y² + 3z² < 6}
> 
> Es un elipsoide abierto en ℝ³
> 
> **Para demostrar:** f(x,y,z) = x² + 2y² + 3z² es continua, y A = f⁻¹((-∞, 6)) es preimagen de abierto por función continua.

## 🔒 Conjuntos Cerrados

### 📐 Definición y Caracterizaciones

> [!example]- 🔴 Conjuntos Cerrados en ℝⁿ
> 
> **Definición 1 (Por complemento):** Un conjunto F ⊂ ℝⁿ es **cerrado** si su complemento Fᶜ = ℝⁿ \ F es abierto.
> 
> **Definición 2 (Por límites):** F es cerrado si contiene todos sus puntos límite:
> 
> Si (xₙ) es sucesión en F y xₙ → **x**, entonces **x** ∈ F
> 
> **Definición 3 (Por puntos de acumulación):** F es cerrado si contiene todos sus puntos de acumulación.
> 
> **Equivalencia:** Todas estas definiciones son equivalentes en ℝⁿ.
> 
> **Ejemplos de conjuntos cerrados:**
> 
> 1. **Bolas cerradas:** B̄(**a**, r)
> 2. **Intervalos cerrados:** [a, b]
> 3. **Esferas:** S(**a**, r)
> 4. **Conjuntos finitos:** {p₁, p₂, ..., pₙ}
> 5. **ℝⁿ completo:** todo el espacio
> 6. **Conjunto vacío:** ∅
> 7. **Semiespacios cerrados:** {**x** : **a** · **x** ≤ b}
> 8. **Clausuras de conjuntos**
> 
> **Ejemplos de conjuntos NO cerrados:**
> 
> 1. **Bolas abiertas:** B(**a**, r)
> 2. **Intervalos abiertos:** (a, b)
> 3. **Intervalos semi-abiertos:** [a, b)
> 4. **ℚⁿ ⊂ ℝⁿ:** racionales (denso pero no cerrado)
> 
> **⚠️ IMPORTANTE:** Un conjunto puede ser:
> 
> - Abierto y NO cerrado: (0, 1)
> - Cerrado y NO abierto: [0, 1]
> - Abierto Y cerrado: ∅, ℝⁿ
> - Ni abierto NI cerrado: [0, 1)

### 🎯 Propiedades de los Cerrados

> [!note]- 📊 Axiomas Duales
> 
> **Propiedades fundamentales (Duales a los abiertos):**
> 
> Sea ℱ = {F ⊂ ℝⁿ : F es cerrado}. Entonces:
> 
> **C1. ∅ ∈ ℱ y ℝⁿ ∈ ℱ**
> 
> - El vacío y el total son cerrados
> 
> **C2. Si {F_α}_{α∈I} ⊂ ℱ, entonces ⋂_{α∈I} F_α ∈ ℱ**
> 
> - La intersección arbitraria (incluso infinita) de cerrados es cerrada
> 
> **C3. Si F₁, F₂, ..., Fₙ ∈ ℱ, entonces ⋃ᵢ₌₁ⁿ Fᵢ ∈ ℱ**
> 
> - La unión **finita** de cerrados es cerrada
> 
> **⚠️ ADVERTENCIA:** La unión infinita de cerrados puede NO ser cerrada
> 
> **Contraejemplo:**
> 
> Considerar Fₙ = [1/n, 1 - 1/n] en ℝ para n = 2, 3, 4, ...
> 
> Cada Fₙ es cerrado, pero:
> 
> $$\bigcup_{n=2}^\infty F_n = (0, 1)$$
> 
> que es abierto, NO cerrado.
> 
> **Leyes de De Morgan:**
> 
> $$\left(\bigcup_\alpha A_\alpha\right)^c = \bigcap_\alpha A_\alpha^c$$
> 
> $$\left(\bigcap_\alpha A_\alpha\right)^c = \bigcup_\alpha A_\alpha^c$$
> 
> Estas relacionan propiedades de abiertos y cerrados.

### ✅ Ejemplos Detallados

> [!example]- 💪 Casos Prácticos de Cerrados
> 
> **Ejemplo 1 - Intervalo cerrado:**
> 
> [a, b] es cerrado en ℝ
> 
> **Demostración:**
> 
> ```
> Complemento: (-∞, a) ∪ (b, ∞)
> Unión de dos abiertos ⟹ abierto
> Por tanto [a, b] es cerrado
> ```
> 
> **Ejemplo 2 - Disco cerrado:**
> 
> D̄ = {(x, y) : x² + y² ≤ 1} es cerrado en ℝ²
> 
> **Por sucesiones:** Si (xₙ, yₙ) ∈ D̄ y (xₙ, yₙ) → (x, y), entonces:
> 
> ```
> xₙ² + yₙ² ≤ 1 para todo n
> Por continuidad: x² + y² ≤ 1
> Por tanto (x, y) ∈ D̄
> ```
> 
> **Ejemplo 3 - Semiplano cerrado:**
> 
> H = {(x, y) : ax + by ≤ c} es cerrado en ℝ²
> 
> Complemento: {(x, y) : ax + by > c} es abierto
> 
> **Ejemplo 4 - Conjunto definido por igualdad:**
> 
> F = {(x, y, z) : x² + y² = z²}
> 
> > (Cono) es cerrado (nivel de función continua)
> 
> **Demostración:**
> 
> ```
> f(x,y,z) = x² + y² - z² es continua
> F = f⁻¹({0}) = {nivel de función continua}
> Los conjuntos de nivel de funciones continuas son cerrados
> ```
> 
> **Ejemplo 5 - Unión finita de cerrados:**
> 
> F = [0, 1] ∪ [2, 3] ∪ {5} en ℝ
> 
> Unión de tres cerrados ⟹ cerrado
> 
> **Ejemplo 6 - Intersección infinita:**
> 
> F = ⋂_{n=1}^∞ [-n, n] = ℝ
> 
> Intersección de cerrados ⟹ cerrado
> 
> **Ejemplo 7 - Clausura de racionales:**
> 
> ℚ̄ = cl(ℚ) = ℝ en ℝ
> 
> (Los racionales son densos en los reales)
> 
> **Ejemplo 8 - Gráfica de función continua:**
> 
> G(f) = {(x, f(x)) : x ∈ [a, b]} es cerrado en ℝ²
> 
> (Gráfica de función continua sobre compacto es cerrada)

## 🎯 Puntos Interiores, Exteriores y Frontera

### 📐 Definiciones Fundamentales

> [!success]- 🟢 Clasificación de Puntos
> 
> Sea A ⊂ ℝⁿ y **p** ∈ ℝⁿ
> 
> **1. Punto interior:**
> 
> **p** es **interior** a A si existe ε > 0 tal que B(**p**, ε) ⊂ A
> 
> - Notación: **p** ∈ int(A) o **p** ∈ Å
> - Intuición: está "completamente dentro" de A
> 
> **2. Punto exterior:**
> 
> **p** es **exterior** a A si existe ε > 0 tal que B(**p**, ε) ⊂ Aᶜ
> 
> - Equivalente: **p** es interior a Aᶜ
> - Notación: **p** ∈ ext(A)
> - Intuición: está "completamente fuera" de A
> 
> **3. Punto frontera:**
> 
> **p** es **punto frontera** de A si para todo ε > 0:
> 
> - B(**p**, ε) ∩ A ≠ ∅ **Y**
>     
> - B(**p**, ε) ∩ Aᶜ ≠ ∅
>     
> - Notación: **p** ∈ ∂A o **p** ∈ Fr(A)
>     
> - Intuición: está en el "borde" de A
>     
> 
> **Relaciones:**
> 
> - ℝⁿ = int(A) ∪ ext(A) ∪ ∂A (partición disjunta)
> - ∂A = ∂(Aᶜ) (frontera es simétrica)
> - int(A) ∩ ∂A = ∅
> - ext(A) ∩ ∂A = ∅
> 
> **Propiedades:**
> 
> - int(A) es el mayor abierto contenido en A
> - int(A) ⊂ A
> - A es abierto ⟺ A = int(A)
> - ∂A es siempre cerrado

### 🎨 Ejemplos Visuales

> [!example]- 💪 Casos Ilustrativos
> 
> **Ejemplo 1 - Intervalo semi-abierto [0, 1) en ℝ:**
> 
> ```
> int([0,1)) = (0,1)        - puntos interiores
> ext([0,1)) = (-∞,0) ∪ (1,∞) - puntos exteriores  
> ∂([0,1)) = {0, 1}         - frontera
> ```
> 
> Nota: 0 ∈ [0,1) pero 0 ∈ ∂([0,1)), no es interior 1 ∉ [0,1) pero 1 ∈ ∂([0,1)), está en frontera
> 
> **Ejemplo 2 - Disco unitario en ℝ²:**
> 
> A = {(x,y) : x² + y² < 1}
> 
> ```
> int(A) = A                    - todo el disco es interior
> ext(A) = {(x,y) : x² + y² > 1} - fuera del círculo
> ∂A = {(x,y) : x² + y² = 1}    - el círculo
> ```
> 
> **Ejemplo 3 - Disco cerrado:**
> 
> B = {(x,y) : x² + y² ≤ 1}
> 
> ```
> int(B) = {(x,y) : x² + y² < 1}
> ext(B) = {(x,y) : x² + y² > 1}
> ∂B = {(x,y) : x² + y² = 1}
> ```
> 
> **Ejemplo 4 - Racionales en ℝ:**
> 
> A = ℚ
> 
> ```
> int(ℚ) = ∅               - no hay puntos interiores
> ext(ℚ) = ∅               - no hay puntos exteriores
> ∂(ℚ) = ℝ                 - toda la recta es frontera
> ```
> 
> (ℚ es denso: toda bola contiene racionales e irracionales)
> 
> **Ejemplo 5 - Conjunto finito:**
> 
> A = {(0,0), (1,0), (0,1)} en ℝ²
> 
> ```
> int(A) = ∅
> ext(A) = ℝ² \ A
> ∂A = A
> ```
> 
> **Ejemplo 6 - Cuadrante cerrado:**
> 
> Q = {(x,y) : x ≥ 0, y ≥ 0}
> 
> ```
> int(Q) = {(x,y) : x > 0, y > 0}
> ext(Q) = {(x,y) : x < 0, y < 0} ∪ {(x,y) : x < 0, y > 0} ∪ {(x,y) : x > 0, y < 0}
> ∂Q = {(x,y) : x = 0, y ≥ 0} ∪ {(x,y) : x ≥ 0, y = 0}
> ```

### 🔧 Propiedades Algebraicas

> [!tip]- 📊 Relaciones entre Operadores
> 
> **1. Interior:**
> 
> - int(A ∩ B) = int(A) ∩ int(B)
> - int(A ∪ B) ⊃ int(A) ∪ int(B) (puede ser estricta)
> - int(int(A)) = int(A) (idempotente)
> - int(∅) = ∅, int(ℝⁿ) = ℝⁿ
> 
> **2. Frontera:**
> 
> - ∂(∂A) ⊂ ∂A (frontera de frontera en la frontera)
> - ∂(A ∪ B) ⊂ ∂A ∪ ∂B
> - ∂(A ∩ B) ⊂ ∂A ∪ ∂B
> - ∂A = A̅ ∩ Āᶜ (intersección de clausuras)
> - ∂A = A̅ \ int(A)
> 
> **3. Relación interior-frontera:**
> 
> - A = int(A) ∪ ∂A ∪ (∂A ∩ Aᶜ)
> - Si A es abierto: A = int(A) y ∂A ∩ A = ∅
> - Si A es cerrado: ∂A ⊂ A
> 
> **Ejemplo donde int(A ∪ B) ≠ int(A) ∪ int(B):**
> 
> ```
> A = [0,1], B = [1,2] en ℝ
> 
> int(A) = (0,1)
> int(B) = (1,2)
> int(A) ∪ int(B) = (0,1) ∪ (1,2)
> 
> A ∪ B = [0,2]
> int(A ∪ B) = (0,2)
> 
> (0,2) ≠ (0,1) ∪ (1,2) pues 1 ∈ (0,2) pero 1 ∉ (0,1) ∪ (1,2)
> ```

## 🔄 Clausura y Adherencia

### 📐 Definición de Clausura

> [!example]- 🔵 Clausura de un Conjunto
> 
> **Definición 1 (Por puntos de acumulación):**
> 
> La **clausura** de A, notada A̅ o cl(A), es:
> 
> $$\overline{A} = A \cup A'$$
> 
> donde A' es el conjunto de **puntos de acumulación** de A
> 
> **Definición 2 (Por cerrados):**
> 
> A̅ es el **menor cerrado** que contiene a A:
> 
> $$\overline{A} = \bigcap {F \text{ cerrado} : A \subseteq F}$$
> 
> **Definición 3 (Por adherencia):**
> 
> **x** ∈ A̅ si y solo si para todo ε > 0:
> 
> $$B(\mathbf{x}, \varepsilon) \cap A \neq \emptyset$$
> 
> **Punto de adherencia:** **x** "toca" A
> 
> **Definición 4 (Por sucesiones):**
> 
> **x** ∈ A̅ si y solo si existe una sucesión (xₙ) en A tal que xₙ → **x**
> 
> **Propiedades básicas:**
> 
> - A ⊂ A̅
> - A̅ es cerrado
> - A es cerrado ⟺ A = A̅
> - ∅̅ = ∅
> - R̅ⁿ = ℝⁿ
> - A ⊂ B ⟹ A̅ ⊂ B̅
> 
> **Relación con interior y frontera:**
> 
> $$\overline{A} = \text{int}(A) \cup \partial A$$
> 
> $$\partial A = \overline{A} \cap \overline{A^c}$$

### 🎯 Propiedades de la Clausura

> [!note]- 📊 Axiomas de Kuratowski
> 
> **Propiedades fundamentales (Axiomas de Clausura):**
> 
> **K1. A̅ = A̅̅ (Idempotencia)**
> 
> La clausura de la clausura es la clausura
> 
> **K2. A ⊂ A̅ (Extensividad)**
> 
> Todo conjunto está contenido en su clausura
> 
> **K3. ∅̅ = ∅ (Normalización)**
> 
> **K4. A̅ ∪ B̅ = A ∪ B̅ (Aditividad finita)**
> 
> La clausura de la unión es la unión de las clausuras
> 
> **⚠️ Nota:** Para intersección, solo tenemos:
> 
> $$\overline{A \cap B} \subseteq \overline{A} \cap \overline{B}$$
> 
> (puede ser estricta)
> 
> **Contraejemplo:**
> 
> ```
> A = (0,1), B = (1,2) en ℝ
> 
> A ∩ B = ∅
> A̅ ∩ B = ∅̅ = ∅
> 
> A̅ = [0,1], B̅ = [1,2]
> A̅ ∩ B̅ = {1}
> 
> ∅ ≠ {1}
> ```
> 
> **Otras propiedades:**
> 
> - cl(Aᶜ) = (int(A))ᶜ
> - int(Aᶜ) = (cl(A))ᶜ
> - ∂A = A̅ \ int(A)

### ✅ Ejemplos de Clausura

> [!example]- 💪 Cálculo de Clausuras
> 
> **Ejemplo 1 - Intervalo abierto:**
> 
> A = (0, 1) en ℝ
> 
> A̅ = [0, 1]
> 
> (Añade los puntos frontera 0 y 1)
> 
> **Ejemplo 2 - Racionales:**
> 
> A = ℚ en ℝ
> 
> A̅ = ℝ
> 
> (ℚ es denso en ℝ: todo real es límite de racionales)
> 
> **Ejemplo 3 - Disco abierto:**
> 
> A = {(x,y) : x² + y² < 1}
> 
> A̅ = {(x,y) : x² + y² ≤ 1}
> 
> (Añade el círculo frontera)
> 
> **Ejemplo 4 - Conjunto numerable:**
> 
> A = {1/n : n ∈ ℕ} en ℝ
> 
> A̅ = A ∪ {0} = {0} ∪ {1/n : n ∈ ℕ}
> 
> (0 es punto de acumulación: 1/n → 0)
> 
> **Ejemplo 5 - Gráfica:**
> 
> A = {(x, sin(1/x)) : x ∈ (0, 1)}
> 
> A̅ = A ∪ ({0} × [-1, 1])
> 
> (La "pared oscilante" de la función sin(1/x))
> 
> **Ejemplo 6 - Conjunto en ℝ²:**
> 
> A = {(x, y) : 0 < x < 1, 0 < y < 1}
> 
> A̅ = {(x, y) : 0 ≤ x ≤ 1, 0 ≤ y ≤ 1}
> 
> **Ejemplo 7 - Unión infinita:**
> 
> A = ⋃_{n=1}^∞ (1/n, 2 - 1/n)
> 
> A = (0, 2) A̅ = [0, 2]

## 🎪 Puntos de Acumulación

### 📐 Definición y Caracterizaciones

> [!success]- 🟢 Puntos Límite
> 
> **Definición 1 (Por bolas perforadas):**
> 
> **p** es **punto de acumulación** (o punto límite) de A si:
> 
> Para todo ε > 0: (B(**p**, ε) \ {**p**}) ∩ A ≠ ∅
> 
> Es decir, toda bola alrededor de **p** contiene puntos de A distintos de **p**
> 
> **Definición 2 (Por sucesiones):**
> 
> **p** es punto de acumulación de A si existe una sucesión (xₙ) en A \ {**p**} tal que xₙ → **p**
> 
> **Notación:**
> 
> - A' = conjunto derivado de A (puntos de acumulación)
> - También: acc(A) o lim(A)
> 
> **Diferencia con punto de adherencia:**
> 
> - **Adherencia:** toda bola toca A (puede ser solo el propio punto)
> - **Acumulación:** toda bola contiene otros puntos de A (infinitos)
> 
> **Punto aislado:**
> 
> **p** ∈ A es **aislado** si existe ε > 0 tal que B(**p**, ε) ∩ A = {**p**}
> 
> - No es punto de acumulación
> - Sí es punto de adherencia
> - **p** ∈ A pero **p** ∉ A'
> 
> **Relación con clausura:**
> 
> $$\overline{A} = A \cup A'$$
> 
> **Teorema:** A es cerrado ⟺ A' ⊂ A (contiene sus puntos de acumulación)

### 🎯 Propiedades del Conjunto Derivado

> [!tip]- 📊 Operador Derivado
> 
> **Propiedades:**
> 
> 1. **A' es cerrado**
>     - (A')' ⊂ A'
> 2. **Monotonía:**
>     - A ⊂ B ⟹ A' ⊂ B'
> 3. **Unión:**
>     - (A ∪ B)' = A' ∪ B'
> 4. **Intersección:**
>     - (A ∩ B)' ⊂ A' ∩ B' (puede ser estricta)
> 5. **Iteración:**
>     - (A')' puede ser diferente de A'
>     - Ejemplo: A = {1/n : n ∈ ℕ}, A' = {0}, (A')' = ∅
> 
> **Clasificación de conjuntos:**
> 
> - **Perfecto:** A = A' (todo punto es de acumulación)
>     - Ejemplo: [a, b], ℝ, Conjunto de Cantor
> - **Discreto:** A' = ∅ (sin puntos de acumulación)
>     - Ejemplo: ℤ, conjunto finito
> - **Denso en sí mismo:** A ⊂ A' (todo punto es de acumulación)
>     - Ejemplo: ℚ, (0, 1)

### ✅ Ejemplos de Puntos de Acumulación

> [!example]- 💪 Casos Detallados
> 
> **Ejemplo 1 - Conjunto finito:**
> 
> A = {1, 2, 3, 4, 5}
> 
> A' = ∅
> 
> (Sin puntos de acumulación: todos son aislados)
> 
> **Ejemplo 2 - Enteros:**
> 
> A = ℤ en ℝ
> 
> A' = ∅
> 
> (Cada entero es aislado: B(n, 1/2) ∩ ℤ = {n})
> 
> **Ejemplo 3 - Sucesión convergente:**
> 
> A = {1/n : n ∈ ℕ}
> 
> A' = {0}
> 
> (0 es el único punto de acumulación: 1/n → 0)
> 
> **Ejemplo 4 - Intervalo:**
> 
> A = (0, 1)
> 
> A' = [0, 1]
> 
> (Todo punto del intervalo cerrado es límite)
> 
> **Ejemplo 5 - Racionales:**
> 
> A = ℚ en ℝ
> 
> A' = ℝ
> 
> (Todo real es límite de racionales: densidad)
> 
> **Ejemplo 6 - Cantor modificado:**
> 
> A = {1/n : n ∈ ℕ} ∪ {0}
> 
> - 0 ∈ A pero también 0 ∈ A'
> - 1/n ∈ A pero 1/n ∉ A' (cada 1/n es aislado)
> 
> A' = {0}
> 
> **Ejemplo 7 - Conjunto en ℝ²:**
> 
> A = {(1/n, 1/m) : n, m ∈ ℕ}
> 
> A' = {(0, 1/m) : m ∈ ℕ} ∪ {(1/n, 0) : n ∈ ℕ} ∪ {(0, 0)}
> 
> (Puntos en los ejes y el origen)

## 📦 Conjuntos Compactos

### 📐 Definiciones de Compacidad

> [!example]- 🔴 Compacidad en ℝⁿ
> 
> **Definición 1 (Por cubrimientos):**
> 
> K ⊂ ℝⁿ es **compacto** si de todo cubrimiento abierto se puede extraer un subcubrimiento finito.
> 
> Formalmente: Si K ⊂ ⋃_{α∈I} U_α con U_α abiertos, entonces existen α₁, ..., αₙ tales que:
> 
> $$K \subseteq \bigcup_{i=1}^n U_{\alpha_i}$$
> 
> **Definición 2 (Por sucesiones - Bolzano-Weierstrass):**
> 
> K es compacto si toda sucesión en K tiene una subsucesión convergente a un punto de K.
> 
> **Definición 3 (Equivalente en ℝⁿ):**
> 
> K es compacto si es **cerrado y acotado** (Teorema de Heine-Borel)
> 
> **Teorema de Heine-Borel:**
> 
> En ℝⁿ con la topología usual:
> 
> $$K \text{ es compacto} \iff K \text{ es cerrado y acotado}$$
> 
> **Acotado:** Existe M > 0 tal que K ⊂ B(**0**, M)
> 
> **Importancia:** En ℝⁿ, verificar compacidad es fácil (solo cerrado + acotado)

### 🎯 Propiedades de Compactos

> [!note]- 📊 Teoremas Fundamentales
> 
> **Propiedades básicas:**
> 
> 1. **Todo compacto es cerrado**
>     - (En espacios de Hausdorff como ℝⁿ)
> 2. **Todo compacto es acotado**
>     - (En espacios métricos)
> 3. **Cerrado dentro de compacto es compacto**
>     - Si F cerrado y F ⊂ K compacto, entonces F compacto
> 4. **Intersección de compactos es compacta**
>     - K₁ ∩ K₂ compacto si K₁, K₂ compactos
> 5. **Unión finita de compactos es compacta**
>     - K₁ ∪ K₂ ∪ ... ∪ Kₙ compacto
> 6. **Producto de compactos es compacto** (Teorema de Tychonoff)
>     - K₁ × K₂ × ... × Kₙ compacto si cada Kᵢ compacto
> 
> **Teoremas importantes:**
> 
> **Teorema del Valor Extremo:** Si f: K → ℝ es continua y K es compacto, entonces f alcanza su máximo y mínimo.
> 
> $$\exists, \mathbf{x}_{\min}, \mathbf{x}_{\max} \in K: \quad f(\mathbf{x}_{\min}) \leq f(\mathbf{x}) \leq f(\mathbf{x}_{\max}) \quad \forall \mathbf{x} \in K$$
> 
> **Teorema:** Imagen continua de compacto es compacta
> 
> Si f: K → ℝᵐ es continua y K es compacto, entonces f(K) es compacto
> 
> **Teorema:** Función continua en compacto es uniformemente continua
> 
> Si f: K → ℝᵐ es continua y K compacto, entonces f es uniformemente continua

### ✅ Ejemplos de Conjuntos Compactos

> [!example]- 💪 Casos Prácticos
> 
> **Ejemplo 1 - Intervalo cerrado:**
> 
> [a, b] es compacto en ℝ
> 
> ✓ Cerrado: complemento (−∞, a) ∪ (b, ∞) es abierto ✓ Acotado: [a, b] ⊂ B(0, max(|a|, |b|) + 1)
> 
> **Ejemplo 2 - Disco cerrado:**
> 
> D̄ = {(x, y) : x² + y² ≤ 1} es compacto en ℝ²
> 
> ✓ Cerrado (nivel de función continua) ✓ Acotado (contenido en B((0,0), 2))
> 
> **Ejemplo 3 - Esfera:**
> 
> Sⁿ⁻¹ = {**x** ∈ ℝⁿ : ‖**x**‖ = 1} es compacta
> 
> ✓ Cerrada (nivel de función continua) ✓ Acotada (‖**x**‖ = 1 para todo **x**)
> 
> **Ejemplo 4 - Producto de intervalos:**
> 
> [a₁, b₁] × [a₂, b₂] × ... × [aₙ, bₙ] es compacto en ℝⁿ
> 
> (Producto de compactos)
> 
> **Ejemplo 5 - Conjunto de Cantor:**
> 
> C (conjunto de Cantor) es compacto
> 
> ✓ Cerrado (intersección de cerrados) ✓ Acotado (C ⊂ [0, 1])
> 
> **Ejemplos de NO compactos:**
> 
> 1. **(0, 1):** Abierto (no cerrado) ✗
>     
> 2. **[0, ∞):** No acotado ✗
>     
> 3. **ℝⁿ:** No acotado ✗
>     
> 4. **ℚ ∩ [0, 1]:** No cerrado (falta puntos de acumulación) ✗
>     
> 5. **{1/n : n ∈ ℕ}:** No cerrado (falta 0) ✗
>     
> 6. **Bola abierta B(**a**, r):** No cerrada ✗
>     

## 🔗 Conjuntos Conexos

### 📐 Definición de Conexidad

> [!success]- 🟢 Conjuntos Conexos
> 
> **Definición 1 (Por separación):**
> 
> A ⊂ ℝⁿ es **conexo** si NO puede escribirse como unión disjunta de dos abiertos no vacíos:
> 
> $$A \neq U \cup V$$
> 
> donde U, V abiertos en A, U ∩ V = ∅, U ≠ ∅, V ≠ ∅
> 
> **Definición 2 (Por funciones continuas):**
> 
> A es conexo si no existe función continua f: A → {0, 1} sobreyectiva.
> 
> (No puede "partirse" continuamente en dos piezas)
> 
> **Definición 3 (Por clausuras):**
> 
> A es conexo si no existen B, C ⊂ A no vacíos tales que:
> 
> - A = B ∪ C
> - B̄ ∩ C = ∅
> - B ∩ C̄ = ∅
> 
> **Desconexo:** Un conjunto que NO es conexo
> 
> **Ejemplo visual:**
> 
> - Conexo: [0, 2] (intervalo continuo)
> - Desconexo: [0, 1] ∪ [2, 3] (dos piezas separadas)

### 🎨 Conexidad por Caminos

> [!tip]- 🛤️ Arco-Conexidad
> 
> **Definición:**
> 
> A es **arco-conexo** (o conexo por caminos) si para cualesquiera **p**, **q** ∈ A, existe una función continua:
> 
> $$\gamma: [0, 1] \to A$$
> 
> tal que γ(0) = **p** y γ(1) = **q**
> 
> Es decir, se puede "caminar" continuamente de cualquier punto a cualquier otro.
> 
> **Teorema:** Arco-conexo ⟹ Conexo
> 
> (El recíproco es falso en general)
> 
> > **Teorema:** En ℝⁿ, los abiertos conexos son arco-conexos
> 
> **Contraejemplo (conexo pero no arco-conexo):**
> 
> El **seno del topólogo**:
> 
> $$T = {(x, \sin(1/x)) : 0 < x \leq 1} \cup {0} \times [-1, 1]$$
> 
> - Es conexo
> - NO es arco-conexo (no hay camino continuo de (1, sin 1) a (0, 0))
> 
> **Componentes conexas:**
> 
> Para A ⊂ ℝⁿ, las **componentes conexas** son los subconjuntos conexos maximales.
> 
> - A es unión disjunta de sus componentes conexas
> - Cada componente es cerrada en A
> 
> **Componentes arco-conexas:**
> 
> Análogamente para arco-conexidad (pueden ser diferentes de las conexas)

### 🎯 Propiedades de Conjuntos Conexos

> [!note]- 📊 Teoremas de Conexidad
> 
> **Propiedades básicas:**
> 
> 1. **Imagen continua de conexo es conexa**
>     - Si f: A → ℝᵐ continua y A conexo, entonces f(A) conexo
> 2. **Clausura de conexo es conexa**
>     - Si A conexo, entonces Ā conexo
> 3. **Unión de conexos con intersección no vacía es conexa**
>     - Si A_α conexos y ⋂A_α ≠ ∅, entonces ⋃A_α conexo
> 4. **Producto de conexos es conexo**
>     - A × B conexo si A y B conexos
> 5. **Intervalo conecta conexos**
>     - Si A, B conexos y A ∩ B̄ ≠ ∅ y Ā ∩ B ≠ ∅, entonces A ∪ B conexo
> 
> **Teorema del Valor Intermedio (generalizado):**
> 
> Si f: A → ℝ es continua, A conexo, y f(a) < c < f(b) para algunos a, b ∈ A, entonces existe x ∈ A tal que f(x) = c.
> 
> **Caracterización en ℝ:**
> 
> Los conjuntos conexos de ℝ son exactamente los **intervalos** (de cualquier tipo).
> 
> **Tipos de intervalos:**
> 
> - [a, b], (a, b), [a, b), (a, b]
> - [a, ∞), (a, ∞), (-∞, b], (-∞, b)
> - ℝ, {a} (punto aislado)

### ✅ Ejemplos de Conjuntos Conexos

> [!example]- 💪 Casos Ilustrativos
> 
> **Ejemplos CONEXOS:**
> 
> 1. **Intervalos en ℝ:** [a, b], (a, b), ℝ
>     
> 2. **Discos en ℝ²:** D = {(x,y) : x² + y² ≤ 1}
>     
> 3. **Bolas en ℝⁿ:** B(**a**, r), B̄(**a**, r)
>     
> 4. **Anillo:** A = {(x,y) : 1 ≤ x² + y² ≤ 4}
>     
> 5. **Plano sin punto:** ℝ² \ {(0,0)}
>     
>     - Es arco-conexo (se puede rodear el origen)
> 6. **Gráfica de función continua:**
>     
>     - G(f) = {(x, f(x)) : x ∈ [a, b]}
> 7. **Unión de segmentos:** Línea quebrada continua
>     
> 
> **Ejemplos DESCONEXOS:**
> 
> 8. **Unión disjunta:** [0, 1] ∪ [2, 3]
>     - Dos componentes conexas
> 9. **Hipérbola:** {(x,y) : xy = 1}
>     - Dos ramas separadas
> 10. **Círculos concéntricos:** S₁ ∪ S₂
>     - Dos componentes (las circunferencias)
> 11. **Racionales:** ℚ ⊂ ℝ
>     - Totalmente desconexo (cada punto es componente)
> 12. **Conjunto de Cantor:** C
>     - Totalmente desconexo
> 13. **ℝ² sin recta:** ℝ² \ {(x, 0) : x ∈ ℝ}
>     - Dos componentes (semiplanos)
> 14. **Esfera sin dos puntos:** S² \ {N, S}
>     - Conexo en S² pero no en ℝ³

## 💻 Implementación Computacional

> [!success]- 🔧 Código Python para Topología
> 
> ```python
> import numpy as np
> import matplotlib.pyplot as plt
> from scipy.spatial.distance import cdist
> 
> class ConjuntoTopologico:
>     """
>     Clase para analizar propiedades topológicas de conjuntos en ℝⁿ
>     """
>     
>     def __init__(self, puntos, dimension=2):
>         """
>         Parámetros:
>         -----------
>         puntos : array-like
>             Conjunto de puntos en ℝⁿ
>         dimension : int
>             Dimensión del espacio ambiente
>         """
>         self.puntos = np.array(puntos)
>         self.dim = dimension
>         
>     def distancia(self, p, q):
>         """Distancia euclidiana entre dos puntos"""
>         return np.linalg.norm(np.array(p) - np.array(q))
>     
>     def bola_abierta(self, centro, radio):
>         """
>         Retorna puntos del conjunto dentro de bola abierta
>         """
>         centro = np.array(centro)
>         distancias = np.linalg.norm(self.puntos - centro, axis=1)
>         return self.puntos[distancias < radio]
>     
>     def bola_cerrada(self, centro, radio):
>         """
>         Retorna puntos del conjunto dentro de bola cerrada
>         """
>         centro = np.array(centro)
>         distancias = np.linalg.norm(self.puntos - centro, axis=1)
>         return self.puntos[distancias <= radio]
>     
>     def es_punto_interior(self, punto, epsilon=0.01):
>         """
>         Verifica si un punto es interior al conjunto
>         (versión discreta - aproximada)
>         """
>         punto = np.array(punto)
>         bola = self.bola_abierta(punto, epsilon)
>         
>         # Criterio: si hay suficientes puntos en vecindad
>         return len(bola) > 10  # Umbral arbitrario
>     
>     def es_punto_frontera(self, punto, epsilon=0.01):
>         """
>         Verifica si un punto está en la frontera
>         (versión aproximada)
>         """
>         punto = np.array(punto)
>         bola = self.bola_abierta(punto, epsilon)
>         
>         # Punto frontera: vecindad contiene puntos dentro y fuera
>         if len(bola) == 0:
>             return False
>         
>         # Generar puntos de prueba alrededor
>         theta = np.linspace(0, 2*np.pi, 20)
>         puntos_prueba = punto + epsilon/2 * np.column_stack([
>             np.cos(theta), np.sin(theta)
>         ])
>         
>         # Verificar si algunos están dentro y otros fuera
>         dentro = 0
>         for p in puntos_prueba:
>             if len(self.bola_abierta(p, epsilon/4)) > 0:
>                 dentro += 1
>         
>         return 0 < dentro < len(puntos_prueba)
>     
>     def es_acotado(self):
>         """Verifica si el conjunto es acotado"""
>         if len(self.puntos) == 0:
>             return True
>         
>         # Calcular radio que contiene todos los puntos
>         centro = np.mean(self.puntos, axis=0)
>         radio_max = np.max(np.linalg.norm(self.puntos - centro, axis=1))
>         
>         return radio_max < np.inf  # Siempre true para finitos
>     
>     def diametro(self):
>         """Calcula el diámetro del conjunto"""
>         if len(self.puntos) < 2:
>             return 0
>         
>         distancias = cdist(self.puntos, self.puntos)
>         return np.max(distancias)
>     
>     def puntos_acumulacion_aproximados(self, umbral=0.05):
>         """
>         Encuentra puntos de acumulación aproximados
>         (puntos con muchos vecinos cercanos)
>         """
>         acumulacion = []
>         
>         for punto in self.puntos:
>             vecinos = self.bola_abierta(punto, umbral)
>             # Si tiene muchos vecinos cercanos
>             if len(vecinos) > 5:
>                 acumulacion.append(punto)
>         
>         return np.array(acumulacion) if acumulacion else np.array([])
>     
>     def visualizar_bolas(self, centro, radios=[0.5, 1.0, 1.5]):
>         """
>         Visualiza bolas concéntricas alrededor de un centro
>         """
>         if self.dim != 2:
>             print("Visualización solo para dimensión 2")
>             return
>         
>         plt.figure(figsize=(10, 10))
>         
>         # Graficar puntos del conjunto
>         if len(self.puntos) > 0:
>             plt.scatter(self.puntos[:, 0], self.puntos[:, 1], 
>                        alpha=0.5, s=20, c='blue', label='Conjunto')
>         
>         # Graficar bolas
>         centro = np.array(centro)
>         plt.plot(centro[0], centro[1], 'ro', markersize=10, 
>                 label=f'Centro {tuple(centro)}')
>         
>         colors = ['red', 'green', 'purple']
>         for r, color in zip(radios, colors):
>             circle = plt.Circle(centro, r, fill=False, 
>                               edgecolor=color, linewidth=2,
>                               linestyle='--', label=f'r = {r}')
>             plt.gca().add_patch(circle)
>         
>         plt.axis('equal')
>         plt.grid(True, alpha=0.3)
>         plt.legend()
>         plt.title('Bolas Concéntricas')
>         plt.xlabel('x')
>         plt.ylabel('y')
>         plt.show()
> 
> # ========== FUNCIONES AUXILIARES ==========
> 
> def generar_conjunto_ejemplos(tipo='disco'):
>     """
>     Genera conjuntos de ejemplo
>     """
>     if tipo == 'disco':
>         # Disco unitario
>         theta = np.random.uniform(0, 2*np.pi, 500)
>         r = np.random.uniform(0, 1, 500)
>         x = r * np.cos(theta)
>         y = r * np.sin(theta)
>         return np.column_stack([x, y])
>     
>     elif tipo == 'anillo':
>         # Anillo
>         theta = np.random.uniform(0, 2*np.pi, 500)
>         r = np.random.uniform(0.5, 1.5, 500)
>         x = r * np.cos(theta)
>         y = r * np.sin(theta)
>         return np.column_stack([x, y])
>     
>     elif tipo == 'dos_discos':
>         # Dos discos separados (desconexo)
>         theta1 = np.random.uniform(0, 2*np.pi, 250)
>         r1 = np.random.uniform(0, 0.5, 250)
>         x1 = -2 + r1 * np.cos(theta1)
>         y1 = r1 * np.sin(theta1)
>         
>         theta2 = np.random.uniform(0, 2*np.pi, 250)
>         r2 = np.random.uniform(0, 0.5, 250)
>         x2 = 2 + r2 * np.cos(theta2)
>         y2 = r2 * np.sin(theta2)
>         
>         return np.vstack([
>             np.column_stack([x1, y1]),
>             np.column_stack([x2, y2])
>         ])
>     
>     elif tipo == 'cuadrado':
>         # Cuadrado [0,1]×[0,1]
>         x = np.random.uniform(0, 1, 500)
>         y = np.random.uniform(0, 1, 500)
>         return np.column_stack([x, y])
>     
>     elif tipo == 'frontera_cuadrado':
>         # Solo frontera del cuadrado
>         puntos = []
>         # Lado inferior
>         puntos.append(np.column_stack([
>             np.linspace(0, 1, 125),
>             np.zeros(125)
>         ]))
>         # Lado derecho
>         puntos.append(np.column_stack([
>             np.ones(125),
>             np.linspace(0, 1, 125)
>         ]))
>         # Lado superior
>         puntos.append(np.column_stack([
>             np.linspace(1, 0, 125),
>             np.ones(125)
>         ]))
>         # Lado izquierdo
>         puntos.append(np.column_stack([
>             np.zeros(125),
>             np.linspace(1, 0, 125)
>         ]))
>         return np.vstack(puntos)
> 
> def visualizar_topologia(conjunto, titulo='Conjunto'):
>     """
>     Visualiza propiedades topológicas de un conjunto
>     """
>     fig, axes = plt.subplots(2, 2, figsize=(14, 14))
>     
>     # 1. Conjunto completo
>     ax1 = axes[0, 0]
>     if len(conjunto.puntos) > 0:
>         ax1.scatter(conjunto.puntos[:, 0], conjunto.puntos[:, 1],
>                    alpha=0.6, s=20)
>     ax1.set_title(f'{titulo}\n{len(conjunto.puntos)} puntos')
>     ax1.set_xlabel('x')
>     ax1.set_ylabel('y')
>     ax1.grid(True, alpha=0.3)
>     ax1.axis('equal')
>     
>     # 2. Puntos de acumulación
>     ax2 = axes[0, 1]
>     if len(conjunto.puntos) > 0:
>         ax2.scatter(conjunto.puntos[:, 0], conjunto.puntos[:, 1],
>                    alpha=0.3, s=10, c='lightblue', label='Conjunto')
>     acum = conjunto.puntos_acumulacion_aproximados()
>     if len(acum) > 0:
>         ax2.scatter(acum[:, 0], acum[:, 1],
>                    alpha=0.8, s=50, c='red', marker='x',
>                    label='Acumulación')
>     ax2.set_title('Puntos de Acumulación (aprox.)')
>     ax2.set_xlabel('x')
>     ax2.set_ylabel('y')
>     ax2.legend()
>     ax2.grid(True, alpha=0.3)
>     ax2.axis('equal')
>     
>     # 3. Bola alrededor de punto central
>     ax3 = axes[1, 0]
>     if len(conjunto.puntos) > 0:
>         centro = np.mean(conjunto.puntos, axis=0)
>         radio = 0.3
>         
>         ax3.scatter(conjunto.puntos[:, 0], conjunto.puntos[:, 1],
>                    alpha=0.3, s=10, c='lightblue')
>         bola = conjunto.bola_abierta(centro, radio)
>         if len(bola) > 0:
>             ax3.scatter(bola[:, 0], bola[:, 1],
>                        alpha=0.8, s=30, c='green', label=f'Bola(c, {radio})')
>         ax3.plot(centro[0], centro[1], 'ro', markersize=10, label='Centro')
>         
>         circle = plt.Circle(centro, radio, fill=False, 
>                           edgecolor='red', linewidth=2, linestyle='--')
>         ax3.add_patch(circle)
>         
>         ax3.set_title(f'Bola Abierta B(c, {radio})')
>         ax3.set_xlabel('x')
>         ax3.set_ylabel('y')
>         ax3.legend()
>         ax3.grid(True, alpha=0.3)
>         ax3.axis('equal')
>     
>     # 4. Información numérica
>     ax4 = axes[1, 1]
>     ax4.axis('off')
>     
>     info_texto = f"""
>     PROPIEDADES TOPOLÓGICAS
>     ========================
>     
>     Número de puntos: {len(conjunto.puntos)}
>     
>     Dimensión: {conjunto.dim}
>     
>     Diámetro: {conjunto.diametro():.4f}
>     
>     Acotado: {'Sí' if conjunto.es_acotado() else 'No'}
>     
>     Puntos de acumulación (aprox.): {len(acum)}
>     
>     Centroide: ({np.mean(conjunto.puntos[:, 0]) if len(conjunto.puntos) > 0 else 0:.3f}, 
>                 {np.mean(conjunto.puntos[:, 1]) if len(conjunto.puntos) > 0 else 0:.3f})
>     """
>     
>     ax4.text(0.1, 0.5, info_texto, fontsize=12,
>             verticalalignment='center', family='monospace')
>     
>     plt.tight_layout()
>     plt.show()
> 
> # ========== EJEMPLOS DE USO ==========
> 
> if __name__ == "__main__":
>     
>     print("="*50)
>     print("ANÁLISIS TOPOLÓGICO DE CONJUNTOS EN ℝ²")
>     print("="*50)
>     
>     # Ejemplo 1: Disco
>     print("\n1. Disco unitario (compacto, conexo)")
>     puntos_disco = generar_conjunto_ejemplos('disco')
>     disco = ConjuntoTopologico(puntos_disco)
>     visualizar_topologia(disco, 'Disco Unitario')
>     
>     # Ejemplo 2: Anillo
>     print("\n2. Anillo (compacto, conexo)")
>     puntos_anillo = generar_conjunto_ejemplos('anillo')
>     anillo = ConjuntoTopologico(puntos_anillo)
>     visualizar_topologia(anillo, 'Anillo')
>     
>     # Ejemplo 3: Dos discos (desconexo)
>     print("\n3. Dos discos separados (desconexo)")
>     puntos_dos = generar_conjunto_ejemplos('dos_discos')
>     dos_discos = ConjuntoTopologico(puntos_dos)
>     visualizar_topologia(dos_discos, 'Dos Discos (Desconexo)')
>     
>     # Ejemplo 4: Frontera de cuadrado
>     print("\n4. Frontera de cuadrado (compacto, conexo)")
>     puntos_frontera = generar_conjunto_ejemplos('frontera_cuadrado')
>     frontera = ConjuntoTopologico(puntos_frontera)
>     visualizar_topologia(frontera, 'Frontera de Cuadrado')
>     
>     # Ejemplo 5: Visualizar bolas
>     print("\n5. Bolas concéntricas")
>     disco.visualizar_bolas(centro=[0, 0], radios=[0.3, 0.6, 1.0])
> ```

## 🧪 Ejercicios Progresivos

> [!example]- 💪 Práctica Graduada
> 
> **Nivel 1 - Conceptos Básicos:** 🟢
> 
> 1. **Bolas:**
>     - Describe B((1, 2), 3) en ℝ²
>     - Respuesta: Disco abierto de radio 3 centrado en (1, 2)
> 2. **Abierto vs Cerrado:**
>     - ¿Es (0, 1) abierto, cerrado, ambos o ninguno en ℝ?
>     - Respuesta: Abierto (no cerrado)
> 3. **Interior:**
>     - Calcular int([0, 1]) en ℝ
>     - Respuesta: (0, 1)
> 4. **Frontera:**
>     - Calcular ∂((0, 1)) en ℝ
>     - Respuesta: {0, 1}
> 5. **Clausura:**
>     - Calcular (0, 1)̄ en ℝ
>     - Respuesta: [0, 1]
> 6. **Compacidad:**
>     - ¿Es [0, 1] compacto en ℝ?
>     - Respuesta: Sí (cerrado y acotado)
> 
> **Nivel 2 - Aplicaciones:** 🟡
> 
> 7. **Puntos de acumulación:**
>     - Encontrar A' para A = {1/n : n ∈ ℕ}
>     - Respuesta: A' = {0}
> 8. **Interior de unión:**
>     - Calcular int([0, 1] ∪ [2, 3])
>     - Respuesta: (0, 1) ∪ (2, 3)
> 9. **Frontera de intersección:**
>     - A = {(x,y) : x² + y² ≤ 1}, B = {(x,y) : x ≥ 0}
>     - Calcular ∂(A ∩ B)
>     - Respuesta: Semicírculo derecho unido con diámetro vertical
> 10. **Conexidad:**
>     - ¿Es ℝ² \ {(0,0)} conexo?
>     - Respuesta: Sí (arco-conexo: se puede rodear el origen)
> 11. **Clausura en ℝ²:**
>     - A = {(x, y) : 0 < x < 1, 0 < y < 1}
>     - Calcular Ā
>     - Respuesta: {(x, y) : 0 ≤ x ≤ 1, 0 ≤ y ≤ 1}
> 12. **Compacto o no:**
>     - ¿Es {(x, y) : x² + y² < 1} compacto en ℝ²?
>     - Respuesta: No (abierto, no cerrado)
> 
> **Nivel 3 - Demostraciones:** 🔴
> 
> 13. **Demostrar:**
>     - Si A ⊂ B, entonces Ā ⊂ B̄
> 14. **Demostrar:**
>     - int(A ∩ B) = int(A) ∩ int(B)
> 15. **Demostrar:**
>     - Si K es compacto y F cerrado con F ⊂ K, entonces F es compacto
> 16. **Contraejemplo:**
>     - Mostrar que ⋂_{n=1}^∞ (−1/n, 1/n) no es abierto
> 
> **Nivel 4 - Problemas Avanzados:** 🟣
> 
> 17. **Teorema del punto fijo:**
>     - Demostrar que toda función continua f: [0,1] → [0,1] tiene un punto fijo
> 18. **Conexidad:**
>     - Demostrar que la imagen continua de un conexo es conexa
> 19. **Compacidad:**
>     - Demostrar que [0,1] es compacto usando el teorema de Heine-Borel
> 20. **Topología cociente:**
>     - Describir la topología de [0,1]/(0∼1) (círculo)

## 📊 Tabla Resumen

> [!abstract]- 📋 Compendio de Conceptos
> 
> |Concepto|Definición|Notación|Propiedades Clave|
> |---|---|---|---|
> |**Bola abierta**|{**x** : d(**x**, **a**) < r}|B(**a**, r)|Es conjunto abierto|
> |**Bola cerrada**|{**x** : d(**x**, **a**) ≤ r}|B̄(**a**, r)|Es conjunto cerrado|
> |**Conjunto abierto**|Unión de bolas abiertas|A abierto|A = int(A)|
> |**Conjunto cerrado**|Complemento es abierto|F cerrado|F = F̄|
> |**Interior**|Mayor abierto en A|int(A), Å|int(A) ⊂ A|
> |**Clausura**|Menor cerrado que contiene A|Ā, cl(A)|A ⊂ Ā|
> |**Frontera**|Ā ∩ Āᶜ|∂A, Fr(A)|Siempre cerrado|
> |**Acumulación**|Punto límite|A'|A cerrado ⟺ A' ⊂ A|
> |**Compacto**|Cerrado y acotado (en ℝⁿ)|K compacto|Heine-Borel|
> |**Conexo**|No separable en abiertos|A conexo|Intervalos en ℝ|
> 
> ### Relaciones entre Conjuntos
> 
> ```
> int(A) ⊂ A ⊂ Ā
>        ↓
>     ∂A = Ā \ int(A)
>     
> A abierto ⟺ A = int(A) ⟺ ∂A ∩ A = ∅
> A cerrado ⟺ A = Ā ⟺ ∂A ⊂ A
> ```
> 
> ### Operaciones
> 
> |Operación|Abiertos|Cerrados|
> |---|---|---|
> |Unión finita|✓|✓|
> |Unión infinita|✓|✗|
> |Intersección finita|✓|✓|
> |Intersección infinita|✗|✓|

## 🌐 Conexiones Conceptuales

> [!quote]- 🔗 Enlaces con Otros Temas
> 
> **Prerequisitos:**
> 
> - [[Conjuntos y Lógica]] - Teoría básica de conjuntos
> - [[Sucesiones y Límites]] - Convergencia
> - [[Funciones Continuas]] - Continuidad
> - [[Espacios Métricos]] - Distancias
> 
> **Temas relacionados:**
> 
> - [[Cálculo Multivariable]] - Límites y continuidad
> - [[Funciones de Varias Variables]] - Dominios abiertos
> - [[Integrales Múltiples]] - Regiones de integración
> - [[Análisis Vectorial]] - Campos vectoriales
> 
> **Aplicaciones directas:**
> 
> - [[Optimización]] - Compacidad garantiza extremos
> - [[Ecuaciones Diferenciales]] - Existencia y unicidad
> - [[Teoría de la Medida]] - Conjuntos medibles
> - [[Análisis Funcional]] - Espacios de Banach
> 
> **Temas avanzados:**
> 
> - [[Topología Algebraica]] - Homología, cohomología
> - [[Geometría Diferencial]] - Variedades topológicas
> - [[Topología General]] - Espacios abstractos
> - [[Análisis Real]] - Teoría de la medida
> 
> **Aplicaciones interdisciplinarias:**
> 
> - [[Ciencia de Datos]] - Clustering topológico
> - [[Física]] - Continuidad de campos
> - [[Economía]] - Teorema del punto fijo de Brouwer
> - [[Biología]] - Morfología topológica


