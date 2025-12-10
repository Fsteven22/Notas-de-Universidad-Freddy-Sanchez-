# 🔄 Transformaciones Lineales

## 🌟 Concepto Fundamental

> [!info]- Definición Intuitiva
> **Una transformación lineal es una función entre espacios vectoriales que preserva las operaciones de suma de vectores y multiplicación por escalares. Representa el concepto más fundamental del álgebra lineal: funciones que mantienen la estructura lineal del espacio.**
> 
> **Características clave:**
> - **Preservación:** Mantiene combinaciones lineales
> - **Estructura:** Respeta operaciones vectoriales
> - **Representación:** Puede expresarse mediante matrices
> - **Geometría:** Transforma el espacio de manera "lineal"
> - **Universalidad:** Conecta todos los conceptos del álgebra lineal

### 📖 Contexto Histórico

> [!note]- Desarrollo del Concepto
> **Orígenes geométricos (1800-1850):**
> - **Möbius (1827):** Coordenadas baricéntricas
>   - Primeras transformaciones sistemáticas
>   - Geometría proyectiva
> - **Grassmann (1844):** *Ausdehnungslehre*
>   - Primera teoría abstracta de espacios lineales
>   - Concepto de transformación lineal
>   - Adelantado a su época
> - **Cayley (1858):** Teoría de matrices
>   - Representación matricial
>   - Álgebra de transformaciones
> 
> **Formalización abstracta (1850-1900):**
> - **Hamilton (1843):** Cuaterniones
>   - Álgebra no conmutativa
>   - Rotaciones en espacio
> - **Sylvester & Cayley:** Teoría de invariantes
>   - Propiedades preservadas por transformaciones
>   - Valores y vectores propios
> - **Peano (1888):** Axiomas de espacios vectoriales
>   - Definición formal de espacio vectorial
>   - Base para transformaciones abstractas
> 
> **Era moderna (1900-1940):**
> - **Hilbert (1906):** Espacios infinito-dimensionales
>   - Operadores lineales en análisis funcional
>   - Ecuaciones integrales
> - **Von Neumann (1930s):** Teoría de operadores
>   - Operadores en espacios de Hilbert
>   - Mecánica cuántica
>   - Teoría espectral
> - **Banach (1932):** Espacios normados
>   - Operadores acotados
>   - Teoría general
> 
> **Síntesis contemporánea (1940-presente):**
> - **Bourbaki (1940s-50s):** Estructuras algebraicas
>   - Formalización moderna
>   - Morfismos entre estructuras
> - **Álgebra lineal computacional:**
>   - Algoritmos eficientes
>   - Aplicaciones masivas
> - **Aplicaciones modernas:**
>   - Gráficos por computadora
>   - Machine learning
>   - Procesamiento de señales
>   - Física teórica

## 📊 Definición Formal

> [!important]- Transformación Lineal
> **Definición:**
> 
> Sean $V$ y $W$ espacios vectoriales sobre el mismo campo $\mathbb{F}$ (usualmente $\mathbb{R}$ o $\mathbb{C}$).
> 
> Una función $T: V \to W$ es una **transformación lineal** (u **operador lineal**) si satisface:
> 
> **L1) ADITIVIDAD:**
> $$T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v}) \quad \forall \vec{u}, \vec{v} \in V$$
> 
> **L2) HOMOGENEIDAD:**
> $$T(c\vec{u}) = cT(\vec{u}) \quad \forall \vec{u} \in V, \, \forall c \in \mathbb{F}$$
> 
> **FORMA EQUIVALENTE (combinada):**
> 
> $$T(c_1\vec{u} + c_2\vec{v}) = c_1T(\vec{u}) + c_2T(\vec{v})$$
> 
> Para todos $\vec{u}, \vec{v} \in V$ y escalares $c_1, c_2 \in \mathbb{F}$.
> 
> **GENERALIZACIÓN:**
> 
> $$T\left(\sum_{i=1}^n c_i\vec{v}_i\right) = \sum_{i=1}^n c_iT(\vec{v}_i)$$
> 
> *Las transformaciones lineales preservan combinaciones lineales.*
> 
> **Notación:**
> - $T: V \to W$ — transformación de $V$ en $W$
> - $T(\vec{v})$ — imagen de $\vec{v}$ bajo $T$
> - $\mathcal{L}(V,W)$ — espacio de todas las transformaciones lineales de $V$ en $W$
> 
> **Casos especiales:**
> - **Operador lineal:** $T: V \to V$ (mismo espacio)
> - **Funcional lineal:** $T: V \to \mathbb{R}$ (o $\mathbb{C}$)
> - **Isomorfismo:** $T$ lineal, biyectiva

## 🎯 Propiedades Fundamentales

> [!success]- Consecuencias de la Linealidad
> **Teorema: Propiedades básicas**
> 
> Si $T: V \to W$ es lineal, entonces:
> 
> **P1) Preserva el vector cero:**
> $$T(\vec{0}_V) = \vec{0}_W$$
> 
> **DEMOSTRACIÓN:**
> $$T(\vec{0}) = T(0 \cdot \vec{v}) = 0 \cdot T(\vec{v}) = \vec{0} \quad \checkmark$$
> 
> **P2) Preserva negativos:**
> $$T(-\vec{v}) = -T(\vec{v})$$
> 
> **DEMOSTRACIÓN:**
> $$T(-\vec{v}) = T((-1)\vec{v}) = (-1)T(\vec{v}) = -T(\vec{v}) \quad \checkmark$$
> 
> **P3) Preserva restas:**
> $$T(\vec{u} - \vec{v}) = T(\vec{u}) - T(\vec{v})$$
> 
> **DEMOSTRACIÓN:**
> $$T(\vec{u} - \vec{v}) = T(\vec{u} + (-\vec{v})) = T(\vec{u}) + T(-\vec{v}) = T(\vec{u}) - T(\vec{v}) \quad \checkmark$$
> 
> **P4) Preserva combinaciones lineales:**
> $$T\left(\sum_{i=1}^n c_i\vec{v}_i\right) = \sum_{i=1}^n c_iT(\vec{v}_i)$$
> 
> **P5) La imagen de un subespacio es un subespacio:**
> 
> Si $U \subseteq V$ es subespacio, entonces $T(U) = \{T(\vec{u}) : \vec{u} \in U\} \subseteq W$ es subespacio.
> 
> **DEMOSTRACIÓN:**
> 
> (S1) $\vec{0} \in U \implies T(\vec{0}) = \vec{0} \in T(U)$ ✓
> 
> (S2) Sean $\vec{w}_1, \vec{w}_2 \in T(U)$, entonces $\exists \vec{u}_1, \vec{u}_2 \in U$ tales que:
> $$\vec{w}_1 = T(\vec{u}_1), \quad \vec{w}_2 = T(\vec{u}_2)$$
> 
> Como $U$ es subespacio: $\vec{u}_1 + \vec{u}_2 \in U$
> 
> $$\vec{w}_1 + \vec{w}_2 = T(\vec{u}_1) + T(\vec{u}_2) = T(\vec{u}_1 + \vec{u}_2) \in T(U) \quad \checkmark$$
> 
> (S3) Similar para multiplicación escalar ✓
> 
> **P6) La preimagen de un subespacio es un subespacio:**
> 
> Si $U \subseteq W$ es subespacio, entonces:
> $$T^{-1}(U) = \{\vec{v} \in V : T(\vec{v}) \in U\}$$
> 
> es subespacio de $V$.
> 
> **TEST DE LINEALIDAD:**
> 
> Para verificar si $T$ es lineal, basta probar:
> $$T(c_1\vec{v}_1 + c_2\vec{v}_2) = c_1T(\vec{v}_1) + c_2T(\vec{v}_2)$$
> 
> para todos $\vec{v}_1, \vec{v}_2$ y escalares $c_1, c_2$.

## 🔢 Representación Matricial

> [!important]- Matrices y Transformaciones Lineales
> **Teorema fundamental de representación:**
> 
> Sea $T: \mathbb{R}^n \to \mathbb{R}^m$ una transformación lineal.
> 
> Entonces existe una **única** matriz $A$ de $m \times n$ tal que:
> $$T(\vec{x}) = A\vec{x} \quad \forall \vec{x} \in \mathbb{R}^n$$
> 
> **CONSTRUCCIÓN DE LA MATRIZ:**
> 
> Sean $\vec{e}_1, \vec{e}_2, \ldots, \vec{e}_n$ los vectores estándar de $\mathbb{R}^n$:
> 
> $$\vec{e}_1 = \begin{bmatrix} 1 \\ 0 \\ \vdots \\ 0 \end{bmatrix}, \quad \vec{e}_2 = \begin{bmatrix} 0 \\ 1 \\ \vdots \\ 0 \end{bmatrix}, \quad \ldots, \quad \vec{e}_n = \begin{bmatrix} 0 \\ 0 \\ \vdots \\ 1 \end{bmatrix}$$
> 
> La **matriz estándar** de $T$ es:
> 
> $$\boxed{A = \begin{bmatrix} | & | & & | \\ T(\vec{e}_1) & T(\vec{e}_2) & \cdots & T(\vec{e}_n) \\ | & | & & | \end{bmatrix}}$$
> 
> Las columnas de $A$ son las imágenes de los vectores estándar.
> 
> **DEMOSTRACIÓN:**
> 
> Todo vector $\vec{x} \in \mathbb{R}^n$ se escribe:
> $$\vec{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} = x_1\vec{e}_1 + x_2\vec{e}_2 + \cdots + x_n\vec{e}_n$$
> 
> Por linealidad:
> $$T(\vec{x}) = T(x_1\vec{e}_1 + \cdots + x_n\vec{e}_n) = x_1T(\vec{e}_1) + \cdots + x_nT(\vec{e}_n)$$
> 
> $$= \begin{bmatrix} | & | & & | \\ T(\vec{e}_1) & T(\vec{e}_2) & \cdots & T(\vec{e}_n) \\ | & | & & | \end{bmatrix}\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix} = A\vec{x} \quad \checkmark$$
> 
> **EJEMPLO:**
> 
> Sea $T: \mathbb{R}^2 \to \mathbb{R}^3$ definida por:
> $$T\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} 2x + y \\ x - 3y \\ 4x \end{bmatrix}$$
> 
> Encontrar la matriz estándar.
> 
> **SOLUCIÓN:**
> 
> $$T(\vec{e}_1) = T\begin{pmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix}\end{pmatrix} = \begin{bmatrix} 2(1) + 0 \\ 1 - 3(0) \\ 4(1) \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \\ 4 \end{bmatrix}$$
> 
> $$T(\vec{e}_2) = T\begin{pmatrix}\begin{bmatrix} 0 \\ 1 \end{bmatrix}\end{pmatrix} = \begin{bmatrix} 2(0) + 1 \\ 0 - 3(1) \\ 4(0) \end{bmatrix} = \begin{bmatrix} 1 \\ -3 \\ 0 \end{bmatrix}$$
> 
> $$A = \begin{bmatrix} 2 & 1 \\ 1 & -3 \\ 4 & 0 \end{bmatrix}$$
> 
> **VERIFICACIÓN:**
> $$T\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} 2 & 1 \\ 1 & -3 \\ 4 & 0 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 2x + y \\ x - 3y \\ 4x \end{bmatrix} \quad \checkmark$$

## 🎨 Transformaciones Geométricas en ℝ²

> [!note]- Transformaciones Estándar en el Plano
> **1. ROTACIÓN (ángulo θ en sentido antihorario):**
> 
> $$R_\theta\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix}$$
> 
> **Ejemplo:** Rotación de 90° (θ = π/2):
> $$R_{90°} = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$$
> 
> $$R_{90°}\begin{pmatrix}\begin{bmatrix} 1 \\ 0 \end{bmatrix}\end{pmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$$
> 
> **Visualización:**
> ```
>      y
>      |     (0,1)
>      |      ↑
>      |      |
>      |      | rotación 90°
>      |      |
>      +------→------- x
>           (1,0)
> ```
> 
> **2. REFLEXIÓN (respecto al eje x):**
> 
> $$\text{Ref}_x\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} x \\ -y \end{bmatrix}$$
> 
> **Reflexión respecto al eje y:**
> $$\text{Ref}_y = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}$$
> 
> **Reflexión respecto a la recta y = x:**
> $$\text{Ref}_{y=x} = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$$
> 
> **3. ESCALAMIENTO:**
> 
> $$S_{(a,b)}\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} a & 0 \\ 0 & b \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} ax \\ by \end{bmatrix}$$
> 
> - $a > 0, b > 0$: estiramiento
> - $0 < a < 1$: contracción horizontal
> - $a = b$: escalamiento uniforme
> 
> **4. PROYECCIÓN (sobre el eje x):**
> 
> $$\text{Proj}_x\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} x \\ 0 \end{bmatrix}$$
> 
> **Proyección sobre el eje y:**
> $$\text{Proj}_y = \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}$$
> 
> **5. CIZALLAMIENTO (shear horizontal):**
> 
> $$\text{Shear}_x(k) = \begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}$$
> 
> Transforma $\begin{bmatrix} x \\ y \end{bmatrix} \mapsto \begin{bmatrix} x + ky \\ y \end{bmatrix}$
> 
> **Cizallamiento vertical:**
> $$\text{Shear}_y(k) = \begin{bmatrix} 1 & 0 \\ k & 1 \end{bmatrix}$$
> 
> **6. TRANSFORMACIÓN IDENTIDAD:**
> 
> $$I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$
> 
> $$I(\vec{v}) = \vec{v} \quad \forall \vec{v}$$
> 
> **7. TRANSFORMACIÓN CERO:**
> 
> $$\mathbf{0} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$$
> 
> $$\mathbf{0}(\vec{v}) = \vec{0} \quad \forall \vec{v}$$

## 🔍 Núcleo e Imagen

> [!important]- Subespacios Fundamentales
> **DEFINICIONES:**
> 
> Sea $T: V \to W$ transformación lineal.
> 
> **1. NÚCLEO (Kernel):**
> 
> $$\text{Ker}(T) = \text{Nul}(T) = \{\vec{v} \in V : T(\vec{v}) = \vec{0}\}$$
> 
> Conjunto de vectores que $T$ "aniquila" o mapea al vector cero.
> 
> **2. IMAGEN (Range):**
> 
> $$\text{Im}(T) = \text{Range}(T) = \{T(\vec{v}) : \vec{v} \in V\} = \{vec{w} \in W : \exists \vec{v} \in V, \, T(\vec{v}) = \vec{w}\}$$
> 
> Conjunto de todos los vectores que son imagen de algún vector en $V$.
> 
> **TEOREMA: Son subespacios**
> 
> **a) Ker(T) es subespacio de V:**
> 
> (S1) $T(\vec{0}) = \vec{0} \implies \vec{0} \in \text{Ker}(T)$ ✓
> 
> (S2) Sean $\vec{u}, \vec{v} \in \text{Ker}(T)$:
> $$T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v}) = \vec{0} + \vec{0} = \vec{0}$$
> $$\implies \vec{u} + \vec{v} \in \text{Ker}(T) \quad \checkmark$$
> 
> (S3) Sea $\vec{u} \in \text{Ker}(T)$, $c \in \mathbb{F}$:
> $$T(c\vec{u}) = cT(\vec{u}) = c\vec{0} = \vec{0}$$
> $$\implies c\vec{u} \in \text{Ker}(T) \quad \checkmark$$
> 
> **b) Im(T) es subespacio de W:**
> 
> (Demostración similar, usando linealidad de $T$)
> 
> **RELACIÓN CON MATRICES:**
> 
> Si $T(\vec{x}) = A\vec{x}$:
> 
> $$\text{Ker}(T) = \text{Nul}(A) = \{\vec{x} : A\vec{x} = \vec{0}\}$$
> 
> $$\text{Im}(T) = \text{Col}(A) = \text{span}\{\text{columnas de } A\}$$
> 
> **DIMENSIONES:**
> 
> $$\text{nullity}(T) = \dim(\text{Ker}(T))$$
> 
> $$\text{rank}(T) = \dim(\text{Im}(T))$$

## 📐 Teorema del Rango-Nulidad

> [!success]- Teorema Fundamental de las Transformaciones Lineales
> **Teorema del Rango-Nulidad (Rank-Nullity Theorem):**
> 
> Sea $T: V \to W$ transformación lineal donde $V$ es de dimensión finita.
> 
> $$\boxed{\dim(V) = \dim(\text{Ker}(T)) + \dim(\text{Im}(T))}$$
> 
> O equivalentemente:
> 
> $$\boxed{\dim(V) = \text{nullity}(T) + \text{rank}(T)}$$
> 
> **INTERPRETACIÓN:**
> 
> La dimensión del dominio se "conserva": parte se "pierde" en el núcleo y parte se "proyecta" en la imagen.
> 
> ```mermaid
> graph LR
>     A[V<br/>dim = n] --> B[Ker T<br/>dim = k]
>     A --> C[complemento<br/>dim = n-k]
>     C --> D[Im T<br/>dim = n-k]
>     
>     B -.mapea a.- E[0]
>     C -.isomorfismo.- D
>     
>     style A fill:#e1f5ff
>     style B fill:#ffccbc
>     style C fill:#c8e6c9
>     style D fill:#c8e6c9
> ```
> 
> **DEMOSTRACIÓN (esquema):**
> 
> 1. Sea $\{\vec{v}_1, \ldots, \vec{v}_k\}$ base de $\text{Ker}(T)$
> 
> 2. Extender a base de $V$: $\{\vec{v}_1, \ldots, \vec{v}_k, \vec{u}_1, \ldots, \vec{u}_r\}$ donde $k + r = n = \dim(V)$
> 
> 3. Demostrar que $\{T(\vec{u}_1), \ldots, T(\vec{u}_r)\}$ es base de $\text{Im}(T)$
> 
> 4. Por tanto: $\dim(\text{Im}(T)) = r = n - k$ ✓
> 
> **EJEMPLO:**
> 
> $T: \mathbb{R}^5 \to \mathbb{R}^3$ con $\text{rank}(T) = 2$
> 
> Por teorema:
> $$5 = \text{nullity}(T) + 2$$
> $$\implies \text{nullity}(T) = 3$$
> 
> $$\dim(\text{Ker}(T)) = 3$$
> 
> **CONSECUENCIAS:**
> 
> **C1)** $T$ inyectiva $\iff \text{Ker}(T) = \{\vec{0}\} \iff \text{nullity}(T) = 0$
> 
> **C2)** Si $\dim(V) = \dim(W)$ y $T$ inyectiva $\implies T$ sobreyectiva
> 
> **C3)** Si $\dim(V) < \dim(W)$, entonces $T$ no puede ser sobreyectiva
> 
> **C4)** Si $\dim(V) > \dim(W)$, entonces $T$ no puede ser inyectiva

## 🔄 Inyectividad y Sobreyectividad

> [!tip]- Tipos de Transformaciones
> **DEFINICIONES:**
> 
> Sea $T: V \to W$ transformación lineal.
> 
> **1. INYECTIVA (One-to-one):**
> 
> $$T \text{ es inyectiva} \iff T(\vec{u}) = T(\vec{v}) \implies \vec{u} = \vec{v}$$
> 
> Vectores diferentes tienen imágenes diferentes.
> 
> **CARACTERIZACIÓN PARA T.L.:**
> 
> $$\boxed{T \text{ inyectiva} \iff \text{Ker}(T) = \{\vec{0}\}}$$
> 
> **DEMOSTRACIÓN:**
> 
> $(\right\arrow)$ Suponer $T$ inyectiva. Como $T(\vec{0}) = \vec{0}$, si $T(\vec{v}) = \vec{0}$, entonces $T(\vec{v}) = T(\vec{0})$, luego $\vec{v} = \vec{0}$. Por tanto $\text{Ker}(T) = \{\vec{0}\}$ ✓
> 
> $(\left\arrow)$ Suponer $\text{Ker}(T) = \{\vec{0}\}$. Si $T(\vec{u}) = T(\vec{v})$:
> $$T(\vec{u}) - T(\vec{v}) = \vec{0}$$
> $$T(\vec{u} - \vec{v}) = \vec{0}$$
> $$\implies \vec{u} - \vec{v} \in \text{Ker}(T) = \{\vec{0}\}$$
> $$\implies \vec{u} - \vec{v} = \vec{0}$$
> $$\implies \vec{u} = \vec{v} \quad \checkmark$$
> 
> **2. SOBREYECTIVA (Onto):**
> 
> $$T \text{ es sobreyectiva} \iff \text{Im}(T) = W$$
> 
> Todo vector en $W$ es imagen de algún vector en $V$.
> 
> **CARACTERIZACIÓN:**
> 
> $$\boxed{T \text{ sobreyectiva} \iff \text{rank}(T) = \dim(W)}$$
> 
> **3. BIYECTIVA (Isomorfismo):**
> 
> $$T \text{ es biyectiva} \iff T \text{ es inyectiva Y sobreyectiva}$$
> 
> **TEOREMA:** Si $T$ es biyectiva, existe transformación inversa $T^{-1}: W \to V$ que también es lineal.
> 
> $$T^{-1}(T(\vec{v})) = \vec{v} \quad \forall \vec{v} \in V$$
> $$T(T^{-1}(\vec{w})) = \vec{w} \quad \forall \vec{w} \in W$$
> 
> **EJEMPLOS:**
> 
> **Ejemplo 1:** $T: \mathbb{R}^3 \to \mathbb{R}^2$ definida por:
> $$T\begin{pmatrix}\begin{bmatrix} x \\ y \\ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x + y \\ 2z \end{bmatrix}$$
> 
> Matriz: $A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 0 & 2 \end{bmatrix}$
> 
> **¿Inyectiva?**
> 
> $\text{Ker}(T) = \{\vec{x} : A\vec{x} = \vec{0}\}$
> 
> $$\begin{bmatrix} 1 & 1 & 0 \\ 0 & 0 & 2 \end{bmatrix}\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
> 
> $\implies x + y = 0, \, 2z = 0$
> 
> $\implies z = 0, \, y = -x$
> 
> $$\text{Ker}(T) = \text{span}\left\\{\begin{bmatrix} 1 \\ -1 \\ 0 \end{bmatrix}\right\\} \neq \{\vec{0}\}$$
> 
> **NO es inyectiva** ❌
> 
> **¿Sobreyectiva?**
> 
> $\text{rank}(A) = 2 = \dim(\mathbb{R}^2)$
> 
> **SÍ es sobreyectiva** ✅
> 
> **Ejemplo 2:** $T: \mathbb{R}^2 \to \mathbb{R}^3$ definida por:
> $$T\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x \ y \ 0 \end{bmatrix}$$
>
> **¿Inyectiva?** 
> 
> $\text{Ker}(T) = \{\vec{0}\}$ ✅ **Sí**
> 
> **¿Sobreyectiva?**
> 
> $\text{Im}(T) = \text{plano } xy \neq \mathbb{R}^3$ ❌ **No**

## 💡 Ejemplos Resueltos

> [!example]- Problemas Detallados
> **Problema 1: Verificar linealidad**
> 
> Determinar si las siguientes funciones son transformaciones lineales:
> 
> **a)** $T: \mathbb{R}^2 \to \mathbb{R}^2$ definida por $T\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} 2x + 3y \\ x - y \end{bmatrix}$
> 
> **SOLUCIÓN:**
> 
> Verificar: $T(c_1\vec{u} + c_2\vec{v}) = c_1T(\vec{u}) + c_2T(\vec{v})$
> 
> Sean $\vec{u} = \begin{bmatrix} u_1 \\ u_2 \end{bmatrix}$, $\vec{v} = \begin{bmatrix} v_1 \\ v_2 \end{bmatrix}$
> 
> $$T(c_1\vec{u} + c_2\vec{v}) = T\begin{pmatrix}\begin{bmatrix} c_1u_1 + c_2v_1 \\ c_1u_2 + c_2v_2 \end{bmatrix}\end{pmatrix}$$
> 
> $$= \begin{bmatrix} 2(c_1u_1 + c_2v_1) + 3(c_1u_2 + c_2v_2) \\ (c_1u_1 + c_2v_1) - (c_1u_2 + c_2v_2) \end{bmatrix}$$
> 
> $$= \begin{bmatrix} c_1(2u_1 + 3u_2) + c_2(2v_1 + 3v_2) \\ c_1(u_1 - u_2) + c_2(v_1 - v_2) \end{bmatrix}$$
> 
> $$= c_1\begin{bmatrix} 2u_1 + 3u_2 \\ u_1 - u_2 \end{bmatrix} + c_2\begin{bmatrix} 2v_1 + 3v_2 \\ v_1 - v_2 \end{bmatrix}$$
> 
> $$= c_1T(\vec{u}) + c_2T(\vec{v}) \quad \checkmark$$
> 
> **ES LINEAL** ✅
> 
> **b)** $T: \mathbb{R}^2 \to \mathbb{R}$ definida por $T\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = xy$
> 
> **SOLUCIÓN:**
> 
> Probar con contraejemplo:
> 
> $$T\begin{pmatrix}\begin{bmatrix} 1 \\ 1 \end{bmatrix} + \begin{bmatrix} 1 \\ 1 \end{bmatrix}\end{pmatrix} = T\begin{pmatrix}\begin{bmatrix} 2 \\ 2 \end{bmatrix}\end{pmatrix} = 2 \cdot 2 = 4$$
> 
> $$T\begin{pmatrix}\begin{bmatrix} 1 \\ 1 \end{bmatrix}\end{pmatrix} + T\begin{pmatrix}\begin{bmatrix} 1 \\ 1 \end{bmatrix}\end{pmatrix} = 1 \cdot 1 + 1 \cdot 1 = 2$$
> 
> $$4 \neq 2$$
> 
> **NO ES LINEAL** ❌
> 
> **c)** $T: \mathbb{R}^2 \to \mathbb{R}^2$ definida por $T\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x + 1 \\ y \end{bmatrix}$
> 
> **SOLUCIÓN:**
> 
> Verificar si $T(\vec{0}) = \vec{0}$:
> 
> $$T\begin{pmatrix}\begin{bmatrix} 0 \\ 0 \end{bmatrix}\end{pmatrix} = \begin{bmatrix} 0 + 1 \\ 0 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \neq \vec{0}$$
> 
> **NO ES LINEAL** ❌ (transformación afín)
> 
> ---
> 
> **Problema 2: Encontrar núcleo e imagen**
> 
> Para $T: \mathbb{R}^4 \to \mathbb{R}^3$ definida por:
> $$T\begin{pmatrix}\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x_1 + 2x_2 + x_3 \\ 2x_1 + 4x_2 + 3x_3 + x_4 \\ x_1 + 2x_2 + 2x_3 + x_4 \end{bmatrix}$$
> 
> Encontrar bases de $\text{Ker}(T)$ e $\text{Im}(T)$.
> 
> **SOLUCIÓN:**
> 
> Matriz estándar:
> $$A = \begin{bmatrix} 1 & 2 & 1 & 0 \\ 2 & 4 & 3 & 1 \\ 1 & 2 & 2 & 1 \end{bmatrix}$$
> 
> **PARTE A: Núcleo**
> 
> Resolver $A\vec{x} = \vec{0}$:
> 
> $$\begin{bmatrix} 1 & 2 & 1 & 0 \\ 2 & 4 & 3 & 1 \\ 1 & 2 & 2 & 1 \end{bmatrix} \right\arrow \begin{bmatrix} 1 & 2 & 1 & 0 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 1 & 1 \end{bmatrix}$$
> 
> $$\right\arrow \begin{bmatrix} 1 & 2 & 0 & -1 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
> 
> Variables: $x_1, x_3$ básicas; $x_2, x_4$ libres
> 
> $$x_3 = -x_4$$
> $$x_1 = -2x_2 + x_4$$
> 
> $$\vec{x} = \begin{bmatrix} -2x_2 + x_4 \\ x_2 \\ -x_4 \\ x_4 \end{bmatrix} = x_2\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + x_4\begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix}$$
> 
> $$\boxed{\text{Base de Ker}(T): \left\\{\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix}, \begin{bmatrix} 1 \\ 0 \\ -1 \\ 1 \end{bmatrix}\right\\}}$$
> 
> $$\dim(\text{Ker}(T)) = 2$$
> 
> **PARTE B: Imagen**
> 
> Columnas pivote: 1 y 3
> 
> Tomar columnas 1 y 3 de $A$ original:
> 
> $$\boxed{\text{Base de Im}(T): \left\\{\begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix}, \begin{bmatrix} 1 \\ 3 \\ 2 \end{bmatrix}\right\\}}$$
> 
> $$\dim(\text{Im}(T)) = 2$$
> 
> **VERIFICACIÓN del teorema:**
> $$\dim(\mathbb{R}^4) = 4 = 2 + 2 = \text{nullity}(T) + \text{rank}(T) \quad \checkmark$$
> 
> ---
> 
> **Problema 3: Composición de transformaciones**
> 
> Sean $T: \mathbb{R}^2 \to \mathbb{R}^3$ y $S: \mathbb{R}^3 \to \mathbb{R}^2$ definidas por:
> 
> $$T\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x + y \\ 2x \\ y \end{bmatrix}, \quad S\begin{pmatrix}\begin{bmatrix} x \\ y \\ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x - z \\ y + z \end{bmatrix}$$
> 
> Encontrar la matriz de $S \circ T$.
> 
> **SOLUCIÓN:**
> 
> **Matrices:**
> $$[T] = \begin{bmatrix} 1 & 1 \\ 2 & 0 \\ 0 & 1 \end{bmatrix}, \quad [S] = \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 1 \end{bmatrix}$$
> 
> **Composición:**
> $$(S \circ T)(\vec{x}) = S(T(\vec{x}))$$
> 
> Matriz de composición:
> $$[S \circ T] = [S][T]$$
> 
> $$= \begin{bmatrix} 1 & 0 & -1 \\ 0 & 1 & 1 \end{bmatrix}\begin{bmatrix} 1 & 1 \\ 2 & 0 \\ 0 & 1 \end{bmatrix}$$
> 
> $$= \begin{bmatrix} 1(1) + 0(2) + (-1)(0) & 1(1) + 0(0) + (-1)(1) \\ 0(1) + 1(2) + 1(0) & 0(1) + 1(0) + 1(1) \end{bmatrix}$$
> 
> $$\boxed{[S \circ T] = \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}}$$
> 
> **VERIFICACIÓN:**
> 
> $$(S \circ T)\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = S\begin{pmatrix}\begin{bmatrix} x+y \\ 2x \\ y \end{bmatrix}\end{pmatrix}$$
> 
> $$= \begin{bmatrix} (x+y) - y \\ 2x + y \end{bmatrix} = \begin{bmatrix} x \\ 2x + y \end{bmatrix}$$
> 
> $$= \begin{bmatrix} 1 & 0 \\ 2 & 1 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} \quad \checkmark$$

## ⚡ Isomorfismos

> [!important]- Espacios Isomorfos
> **DEFINICIÓN:**
> 
> Espacios vectoriales $V$ y $W$ son **isomorfos** (notación: $V \cong W$) si existe transformación lineal $T: V \to W$ que es biyectiva.
> 
> A $T$ se le llama **isomorfismo**.
> 
> **TEOREMA: Caracterización de isomorfismos**
> 
> $V$ y $W$ son isomorfos $\iff \dim(V) = \dim(W)$
> 
> **CONSECUENCIA:**
> 
> Todo espacio vectorial de dimensión $n$ sobre $\mathbb{R}$ es isomorfo a $\mathbb{R}^n$.
> 
> **EJEMPLOS:**
> 
> **1.** $\mathbb{R}^3 \cong \mathcal{P}_2$ (polinomios de grado ≤ 2)
> 
> Isomorfismo: $T: \mathbb{R}^3 \to \mathcal{P}_2$
> 
> $$T\begin{pmatrix}\begin{bmatrix} a \\ b \\ c \end{bmatrix}\end{pmatrix} = a + bx + cx^2$$
> 
> **2.** $M_{2 \times 2} \cong \mathbb{R}^4$
> 
> Isomorfismo: $T: M_{2 \times 2} \to \mathbb{R}^4$
> 
> $$T\begin{pmatrix}\begin{bmatrix} a & b \\ c & d \end{bmatrix}\end{pmatrix} = \begin{bmatrix} a \\ b \\ c \\ d \end{bmatrix}$$
> 
> **PROPIEDADES DE ISOMORFISMOS:**
> 
> Si $T: V \to W$ es isomorfismo:
> 
> **I1)** $T^{-1}: W \to V$ existe y también es isomorfismo
> 
> **I2)** $T$ mapea bases en bases:
> Si $\{\vec{v}_1, \ldots, \vec{v}_n\}$ es base de $V$, entonces $\{T(\vec{v}_1), \ldots, T(\vec{v}_n)\}$ es base de $W$
> 
> **I3)** $T$ preserva independencia lineal y generación
> 
> **I4)** $V$ y $W$ son "esencialmente el mismo" espacio algebraicamente

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes
> **1. "T(vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v}) implica linealidad"**
> 
> ⚠️ **INCOMPLETO**
> 
> También debe cumplir $T(c\vec{v}) = cT(\vec{v})$
> 
> **Contraejemplo:**
> $T(x) = x + 1$ cumple aditividad pero no homogeneidad.
> 
> ---
> 
> **2. "Toda función entre espacios vectoriales es lineal"**
> 
> ❌ **FALSO**
> 
> Ejemplo: $T(x) = x^2$ NO es lineal.
> 
> $$T(2x) = (2x)^2 = 4x^2 \neq 2T(x) = 2x^2$$
> 
> ---
> 
> **3. "Si T(\vec{0}) = \vec{0}, entonces T es lineal"**
> 
> ❌ **FALSO**
> 
> Es condición **necesaria** pero NO suficiente.
> 
> Contraejemplo: $T(x) = x^2$
> $$T(0) = 0 \text{ pero } T \text{ no es lineal}$$
> 
> ---
> 
> **4. "La matriz de T se forma con cualquier base"**
> 
> ⚠️ **CUIDADO**
> 
> La matriz **estándar** usa la base estándar.
> 
> Para otras bases, la matriz cambia (concepto de cambio de base).
> 
> ---
> 
> **5. "Ker(T) = {0} implica que T es biyectiva"**
> 
> ❌ **FALSO**
> 
> Solo implica **inyectividad**, no sobreyectividad.
> 
> Ejemplo: $T: \mathbb{R}^2 \to \mathbb{R}^3$, $T\begin{pmatrix}\begin{bmatrix} x \\ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x \\ y \\ 0 \end{bmatrix}$
> 
> Ker(T) = {0} pero Im(T) ≠ ℝ³
> 
> ---
> 
> **6. "rank(T) + nullity(T) = dim(W)"**
> 
> ❌ **FALSO**
> 
> $$\text{rank}(T) + \text{nullity}(T) = \dim(V) \text{ (dominio)}$$
> 
> No el codominio.
> 
> ---
> 
> **7. "Composición: [T ∘ S] = [T][S]"**
> 
> ❌ **FALSO** (orden incorrecto)
> 
> $$\boxed{[T \circ S] = [T][S]}$$
> 
> Pero se aplica de derecha a izquierda: primero $S$, luego $T$.

## 🔗 Conexiones con Otros Temas

> [!quote]- Enlaces Conceptuales
> **Fundamentos previos:**
> - [[01 - Vectores en espacios vectoriales]] - Espacios vectoriales
> - [[05 - Combinaciones lineales]] - Estructura lineal
> - [[06 - Independencia lineal]] - Bases
> - [[05 – Espacio columna]] - Imagen
> - [[06 – Espacio fila]] - Dualidad
> 
> **Temas relacionados:**
> - [[19 - Espacio nulo]] - Núcleo
> - [[20 - Rango y nulidad]] - Teorema fundamental
> - [[21 - Matrices y operadores]] - Representación
> - [[22 - Cambio de base]] - Representaciones múltiples
> 
> **Aplicaciones posteriores:**
> - [[24 - Valores propios]] - Operadores especiales
> - [[25 - Diagonalización]] - Simplificación
> - [[30 - Formas cuadráticas]] - Aplicaciones
> - [[35 - SVD]] - Descomposición

## 📚 Recursos Adicionales

> [!note]- Herramientas y Referencias
> **Software de álgebra lineal:**
> 
> - **MATLAB**
>   ```matlab
>   A = [1 2; 3 4];
>   T = @(x) A*x;  % Definir transformación
>   v = [1; 0];
>   w = T(v);      % Aplicar transformación
>   rank_T = rank(A);
>   null_T = null(A, 'r');  % Base del núcleo
>   ```
> 
> - **Python (NumPy)**
>   ```python
>   import numpy as np
>   from scipy.linalg import null_space
>   
>   A = np.array([[1, 2], [3, 4]])
>   T = lambda x: A @ x
>   v = np.array([1, 0])
>   w = T(v)
>   
>   rank_T = np.linalg.matrix_rank(A)
>   ker_T = null_space(A)
>   ```
> 
> - **Wolfram Alpha**
>   - "linear transformation {{1,2},{3,4}}"
>   - "kernel of {{1,2,3},{4,5,6}}"
>   - "is T(x,y) = (x+y, 2x) linear?"
> 
> **Visualizadores:**
> - **3Blue1Brown** - "Linear transformations and matrices" (YouTube)
> - **GeoGebra** - Transformaciones en 2D/3D
> - **Desmos** - Transformaciones en el plano

## 📖 Bibliografía Esencial

> [!tip]- Lecturas Recomendadas
> **Nivel introductorio:**
> - **Lay, D. C.** (2016). _Álgebra Lineal y sus Aplicaciones_ (5ª ed.). Pearson.
>   - **Cap. 1.8-1.9:** Transformaciones lineales ⭐
>   - Excelente introducción geométrica
> 
> - **Poole, D.** (2011). _Álgebra Lineal: Una Introducción Moderna_ (3ª ed.). Cengage.
>   - Cap. 3: Matrices y transformaciones lineales
>   - Muchas aplicaciones visuales
> 
> **Nivel intermedio:**
> - **Strang, G.** (2016). _Introduction to Linear Algebra_ (5th ed.). Wellesley-Cambridge.
>   - Cap. 3: Vector Spaces and Subspaces
>   - Cap. 8: Linear Transformations
>   - Videos MIT OCW disponibles
> 
> - **Anton, H., & Rorres, C.** (2014). _Elementary Linear Algebra_ (11th ed.). Wiley.
>   - Cap. 4: General Vector Spaces
>   - Cap. 8: Linear Transformations
> 
> **Nivel avanzado:**
> - **Axler, S.** (2015). _Linear Algebra Done Right_ (3rd ed.). Springer.
>   - **Cap. 3: Linear Maps** ⭐⭐⭐
>   - Tratamiento abstracto y elegante
>   - Enfoque sin determinantes
> 
> - **Hoffman, K., & Kunze, R.** (1971). _Linear Algebra_ (2nd ed.). Prentice Hall.
>   - Tratamiento riguroso y completo
>   - Para estudiantes avanzados

## 🎓 Conceptos Clave - Resumen

> [!important]- Ideas Fundamentales
> 
> **DEFINICIÓN:**
> 
> $T: V \to W$ es lineal si:
> $$T(c_1\vec{v}_1 + c_2\vec{v}_2) = c_1T(\vec{v}_1) + c_2T(\vec{v}_2)$$
> 
> **REPRESENTACIÓN MATRICIAL:**
> 
> Para $T: \mathbb{R}^n \to \mathbb{R}^m$:
> $$T(\vec{x}) = A\vec{x}$$
> 
> donde columnas de $A$ son $T(\vec{e}_i)$
> 
> **SUBESPACIOS FUNDAMENTALES:**
> 
> $$\text{Ker}(T) = \{\vec{v} : T(\vec{v}) = \vec{0}\} \subseteq V$$
> 
> $$\text{Im}(T) = \{T(\vec{v}) : \vec{v} \in V\} \subseteq W$$
> 
> **TEOREMA DEL RANGO-NULIDAD:**
> 
> $$\boxed{\dim(V) = \dim(\text{Ker}(T)) + \dim(\text{Im}(T))}$$
> 
> **INYECTIVIDAD Y SOBREYECTIVIDAD:**
> 
> $$T \text{ inyectiva} \iff \text{Ker}(T) = \{\vec{0}\}$$
> 
> $$T \text{ sobreyectiva} \iff \text{Im}(T) = W$$
> 
> **ISOMORFISMO:**
> 
> $$V \cong W \iff \dim(V) = \dim(W)$$

---

**Tags:** #algebra-lineal #transformaciones-lineales #operadores #nucleo #imagen #rango-nulidad #inyectividad #sobreyectividad #isomorfismo #representacion-matricial #espacios-vectoriales