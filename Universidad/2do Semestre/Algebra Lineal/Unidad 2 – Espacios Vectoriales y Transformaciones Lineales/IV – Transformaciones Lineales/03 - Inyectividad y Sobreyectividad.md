# 🎯 Inyectividad y Sobreyectividad

## 🌟 Concepto Fundamental

> [!info]- Definición Intuitiva **La inyectividad y sobreyectividad son dos propiedades fundamentales que caracterizan cómo una transformación lineal "mapea" vectores entre espacios. La inyectividad garantiza que vectores distintos tienen imágenes distintas (no hay "colisiones"), mientras que la sobreyectividad asegura que todo vector del codominio es alcanzable (no hay "huecos"). Juntas, estas propiedades determinan completamente el comportamiento estructural de una transformación lineal.**
> 
> **Características clave:**
> 
> - **Inyectividad:** Preserva la distinción entre vectores
> - **Sobreyectividad:** Garantiza cobertura total del codominio
> - **Biyectividad:** Combinación de ambas (correspondencia perfecta)
> - **Invertibilidad:** Equivalente a biyectividad
> - **Detección:** Completamente caracterizada por núcleo e imagen

### 📖 Contexto Histórico

> [!note]- Desarrollo del Concepto **Orígenes algebraicos (1800-1850):**
> 
> - **Gauss (1801-1830):** Teoría de congruencias
>     - Funciones uno-a-uno en aritmética modular
>     - Primeras nociones de invertibilidad
>     - "Disquisitiones Arithmeticae"
> - **Galois (1830):** Teoría de grupos
>     - Permutaciones inyectivas (biyectivas)
>     - Automorfismos de cuerpos
>     - Transformaciones reversibles
> - **Cayley (1854):** Grupos abstractos
>     - Isomorfismos como biyecciones
>     - Preservación de estructura
> 
> **Formalización de funciones (1850-1900):**
> 
> - **Dirichlet (1837):** Concepto moderno de función
>     - Correspondencia arbitraria
>     - Más allá de fórmulas explícitas
> - **Dedekind (1872):** Inyecciones y sobreyecciones
>     - Terminología formal
>     - "Eineindeutig" (uno-a-uno)
>     - Conjuntos infinitos
> - **Cantor (1874-1895):** Teoría de conjuntos
>     - Biyecciones entre infinitos
>     - Cardinalidad
>     - Paradoja: $\mathbb{N} \left\right\arrow \mathbb{Q}$ (sobreyección)
> 
> **Álgebra lineal moderna (1900-1940):**
> 
> - **Frobenius (1878):** Matrices e invertibilidad
>     - Determinante y biyectividad
>     - Rango completo
> - **Steinitz (1913):** Bases e isomorfismos
>     - Espacios de igual dimensión
>     - Clasificación dimensional
> - **Emmy Noether (1920s):** Homomorfismos
>     - Teoremas de isomorfismo
>     - $V/\ker(T) \cong \text{Im}(T)$
>     - Marco categórico abstracto
> - **van der Waerden (1930):** "Moderne Algebra"
>     - Presentación sistemática
>     - Inyectividad ↔ núcleo trivial
>     - Sobreyectividad ↔ imagen completa
> 
> **Teoría de categorías (1940-1960):**
> 
> - **Eilenberg-MacLane (1945):** Categorías
>     - Monomorfismos (inyecciones)
>     - Epimorfismos (sobreyecciones)
>     - Isomorfismos (biyecciones)
>     - Flechas como morfismos
> - **Grothendieck (1950s-60s):** Funtores
>     - Preservación de propiedades
>     - Inyectividad funcional
> 
> **Análisis funcional (1950-presente):**
> 
> - **Banach:** Teorema de aplicación abierta
>     - Sobreyecciones continuas
>     - Teorema del gráfico cerrado
> - **Atkinson (1951):** Operadores de Fredholm
>     - Índice = dim(Ker) - dim(Coker)
>     - Cuasi-inyectividad/sobreyectividad
> - **Aplicaciones modernas:**
>     - Machine learning (inyectividad en embeddings)
>     - Teoría de información
>     - Compresión de datos
>     - Criptografía (funciones unidireccionales)
> 
> **Nota histórica:** La terminología varía según la escuela: "one-to-one" vs "injective", "onto" vs "surjective", "bijection" vs "one-to-one correspondence". La notación moderna se estandarizó principalmente en la segunda mitad del siglo XX.

## 📊 Definiciones Formales

> [!important]- Inyectividad (One-to-One) **DEFINICIÓN (Inyectividad):**
> 
> Una transformación lineal $T: V \to W$ es **inyectiva** (o uno-a-uno) si:
> 
> $$\boxed{T(\vec{u}) = T(\vec{v}) \implies \vec{u} = \vec{v}}$$
> 
> **O equivalentemente:**
> 
> $$\boxed{\vec{u} \neq \vec{v} \implies T(\vec{u}) \neq T(\vec{v})}$$
> 
> **CARACTERIZACIÓN POR EL NÚCLEO:**
> 
> $$\boxed{T \text{ es inyectiva} \iff \text{Ker}(T) = {\vec{0}}}$$
> 
> **INTERPRETACIÓN:**
> 
> - Vectores distintos tienen imágenes distintas
> - No hay "colisiones" en el mapeo
> - La transformación preserva la información
> - Cada vector del codominio tiene **a lo más** una preimagen
> 
> **VISUALIZACIÓN:**
> 
> ```
>      V                    W
>   
>    v₁ ──────────────────→ T(v₁)
>    v₂ ──────────────────→ T(v₂)
>    v₃ ──────────────────→ T(v₃)
>    
>   (todas diferentes)   (todas diferentes)
>   
>   ✓ INYECTIVA: Vectores distintos → Imágenes distintas
> ```
> 
> **VISUALIZACIÓN (NO INYECTIVA):**
> 
> ```
>      V                    W
>   
>    v₁ ─────┐
>            ├───────────→ T(v₁) = T(v₂)
>    v₂ ─────┘
>    v₃ ──────────────────→ T(v₃)
>    
>   ✗ NO INYECTIVA: v₁ ≠ v₂ pero T(v₁) = T(v₂)
> ```

> [!important]- Sobreyectividad (Onto) **DEFINICIÓN (Sobreyectividad):**
> 
> Una transformación lineal $T: V \to W$ es **sobreyectiva** (u onto) si:
> 
> $$\boxed{\forall \vec{w} \in W, \exists \vec{v} \in V : T(\vec{v}) = \vec{w}}$$
> 
> **CARACTERIZACIÓN POR LA IMAGEN:**
> 
> $$\boxed{T \text{ es sobreyectiva} \iff \text{Im}(T) = W}$$
> 
> **INTERPRETACIÓN:**
> 
> - Todo vector del codominio es alcanzable
> - No hay "huecos" en la cobertura
> - La imagen llena completamente el codominio
> - Cada vector del codominio tiene **al menos** una preimagen
> 
> **VISUALIZACIÓN:**
> 
> ```
>      V                    W
>   
>    v₁ ──────────────────→ w₁
>    v₂ ──────────────────→ w₂
>    v₃ ──────────────────→ w₃
>    v₄ ──────────────────→ w₄
>    
>   ✓ SOBREYECTIVA: Todo w ∈ W es alcanzado
> ```
> 
> **VISUALIZACIÓN (NO SOBREYECTIVA):**
> 
> ```
>      V                    W
>   
>    v₁ ──────────────────→ w₁
>    v₂ ──────────────────→ w₂
>    v₃ ──────────────────→ w₃
>                           w₄ (no alcanzado)
>                           w₅ (no alcanzado)
>    
>   ✗ NO SOBREYECTIVA: Existen w sin preimagen
> ```

> [!important]- Biyectividad (Isomorfismo) **DEFINICIÓN (Biyectividad):**
> 
> Una transformación lineal $T: V \to W$ es **biyectiva** si es:
> 
> - **Inyectiva** Y
> - **Sobreyectiva**
> 
> $$\boxed{T \text{ es biyectiva} \iff T \text{ es inyectiva y sobreyectiva}}$$
> 
> **CARACTERIZACIÓN COMPLETA:**
> 
> $$\boxed{T \text{ es biyectiva} \iff \text{Ker}(T) = {\vec{0}} \land \text{Im}(T) = W}$$
> 
> **INTERPRETACIÓN:**
> 
> - Correspondencia perfecta uno-a-uno entre V y W
> - Cada vector de W tiene **exactamente** una preimagen
> - La transformación es **invertible**
> - V y W son "esencialmente iguales" (isomorfos)
> 
> **VISUALIZACIÓN:**
> 
> ```
>      V           ←→          W
>   
>    v₁ ←─────────────────────→ w₁
>    v₂ ←─────────────────────→ w₂
>    v₃ ←─────────────────────→ w₃
>    
>   ✓ BIYECTIVA: Correspondencia perfecta
>                Existe T⁻¹: W → V
> ```
> 
> **TEOREMA (Invertibilidad):**
> 
> $$\boxed{T \text{ es biyectiva} \iff \exists T^{-1}: W \to V \text{ lineal}}$$
> 
> donde $T^{-1}$ satisface:
> 
> - $T^{-1} \circ T = \text{Id}_V$
> - $T \circ T^{-1} = \text{Id}_W$

## 🎯 Caracterizaciones Fundamentales

> [!success]- Teoremas de Caracterización **TEOREMA 1: Caracterización por el núcleo (Inyectividad)**
> 
> Sea $T: V \to W$ transformación lineal.
> 
> $$\boxed{T \text{ es inyectiva} \iff \text{Ker}(T) = {\vec{0}}}$$
> 
> **DEMOSTRACIÓN:**
> 
> **($\right\arrow$) Si T es inyectiva, entonces Ker(T) = {0}:**
> 
> Sea $\vec{v} \in \text{Ker}(T)$, entonces $T(\vec{v}) = \vec{0}$.
> 
> También sabemos que $T(\vec{0}) = \vec{0}$ (propiedad de T lineal).
> 
> Por inyectividad: $T(\vec{v}) = T(\vec{0}) \implies \vec{v} = \vec{0}$
> 
> Por tanto: $\text{Ker}(T) = {\vec{0}}$ ✓
> 
> **($\left\arrow$) Si Ker(T) = {0}, entonces T es inyectiva:**
> 
> Suponer $T(\vec{u}) = T(\vec{v})$.
> 
> Entonces: $T(\vec{u}) - T(\vec{v}) = \vec{0}$
> 
> Por linealidad: $T(\vec{u} - \vec{v}) = \vec{0}$
> 
> Esto significa: $\vec{u} - \vec{v} \in \text{Ker}(T) = {\vec{0}}$
> 
> Por tanto: $\vec{u} - \vec{v} = \vec{0} \implies \vec{u} = \vec{v}$ ✓
> 
> **Q.E.D.**
> 
> ---
> 
> **TEOREMA 2: Caracterización dimensional (Inyectividad)**
> 
> Sea $T: V \to W$ transformación lineal con $\dim(V) = n$.
> 
> $$\boxed{T \text{ es inyectiva} \iff \text{rank}(T) = n}$$
> 
> **DEMOSTRACIÓN:**
> 
> Por el Teorema de la Dimensión: $n = \text{nullity}(T) + \text{rank}(T)$
> 
> $T$ inyectiva $\iff \text{Ker}(T) = {\vec{0}} \iff \text{nullity}(T) = 0$
> 
> $\iff n = 0 + \text{rank}(T) \iff \text{rank}(T) = n$ ✓
> 
> ---
> 
> **TEOREMA 3: Caracterización por la imagen (Sobreyectividad)**
> 
> Sea $T: V \to W$ transformación lineal.
> 
> $$\boxed{T \text{ es sobreyectiva} \iff \text{Im}(T) = W}$$
> 
> **DEMOSTRACIÓN:** Directa de la definición ✓
> 
> ---
> 
> **TEOREMA 4: Caracterización dimensional (Sobreyectividad)**
> 
> Sea $T: V \to W$ transformación lineal con $\dim(W) = m$.
> 
> $$\boxed{T \text{ es sobreyectiva} \iff \text{rank}(T) = m}$$
> 
> **DEMOSTRACIÓN:**
> 
> $T$ sobreyectiva $\iff \text{Im}(T) = W$
> 
> $\iff \dim(\text{Im}(T)) = \dim(W)$
> 
> $\iff \text{rank}(T) = m$ ✓
> 
> ---
> 
> **TEOREMA 5: Equivalencia en dimensiones iguales**
> 
> Si $\dim(V) = \dim(W) = n$, entonces:
> 
> $$\boxed{T \text{ inyectiva} \iff T \text{ sobreyectiva} \iff T \text{ biyectiva}}$$
> 
> **DEMOSTRACIÓN:**
> 
> Por Teorema de la Dimensión: $n = \text{nullity}(T) + \text{rank}(T)$
> 
> **T inyectiva:**
> 
> - $\text{nullity}(T) = 0$
> - $\implies \text{rank}(T) = n$
> - $\implies \text{Im}(T) = W$ (ya que $\dim(W) = n$)
> - $\implies T$ sobreyectiva ✓
> 
> **T sobreyectiva:**
> 
> - $\text{rank}(T) = n$
> - $\implies \text{nullity}(T) = 0$
> - $\implies \text{Ker}(T) = {\vec{0}}$
> - $\implies T$ inyectiva ✓
> 
> Por tanto, en dimensiones iguales, las tres propiedades son equivalentes ✓

## 🚫 Teoremas de Imposibilidad

> [!warning]- Restricciones Dimensionales **TEOREMA 6: Imposibilidad de inyección**
> 
> Si $\dim(V) > \dim(W)$, entonces **NO EXISTE** transformación lineal inyectiva $T: V \to W$.
> 
> $$\boxed{\dim(V) > \dim(W) \implies T \text{ no puede ser inyectiva}}$$
> 
> **DEMOSTRACIÓN:**
> 
> Sean $\dim(V) = n$ y $\dim(W) = m$ con $n > m$.
> 
> Por Teorema de la Dimensión: $$\text{rank}(T) = n - \text{nullity}(T) \leq n$$
> 
> Además: $\text{rank}(T) \leq \dim(W) = m < n$
> 
> Por tanto: $\text{rank}(T) < n$
> 
> Esto implica: $\text{nullity}(T) = n - \text{rank}(T) > 0$
> 
> Conclusión: $\text{Ker}(T) \neq {\vec{0}}$, por tanto T no es inyectiva ✓
> 
> **INTUICIÓN:** "No se puede inyectar un espacio grande en uno pequeño sin colapsar vectores."
> 
> **EJEMPLO:** No existe $T: \mathbb{R}^3 \to \mathbb{R}^2$ inyectiva. Cualquier T debe "colapsar" al menos una dirección.
> 
> ---
> 
> **TEOREMA 7: Imposibilidad de sobreyección**
> 
> Si $\dim(V) < \dim(W)$, entonces **NO EXISTE** transformación lineal sobreyectiva $T: V \to W$.
> 
> $$\boxed{\dim(V) < \dim(W) \implies T \text{ no puede ser sobreyectiva}}$$
> 
> **DEMOSTRACIÓN:**
> 
> Sean $\dim(V) = n$ y $\dim(W) = m$ con $n < m$.
> 
> Por Teorema de la Dimensión: $$\text{rank}(T) = n - \text{nullity}(T) \leq n < m = \dim(W)$$
> 
> Por tanto: $\dim(\text{Im}(T)) < \dim(W)$
> 
> Conclusión: $\text{Im}(T) \neq W$, por tanto T no es sobreyectiva ✓
> 
> **INTUICIÓN:** "No se puede cubrir un espacio grande desde uno pequeño."
> 
> **EJEMPLO:** No existe $T: \mathbb{R}^2 \to \mathbb{R}^3$ sobreyectiva. La imagen será a lo más un plano en $\mathbb{R}^3$.
> 
> ---
> 
> **TEOREMA 8: Existencia de biyección**
> 
> Existe transformación lineal biyectiva $T: V \to W$ si y solo si:
> 
> $$\boxed{\dim(V) = \dim(W)}$$
> 
> **DEMOSTRACIÓN:**
> 
> **($\right\arrow$) Si existe T biyectiva, entonces dim(V) = dim(W):**
> 
> T biyectiva $\implies$ T inyectiva y sobreyectiva
> 
> $\implies \text{rank}(T) = \dim(V)$ y $\text{rank}(T) = \dim(W)$
> 
> $\implies \dim(V) = \dim(W)$ ✓
> 
> **($\left\arrow$) Si dim(V) = dim(W), existe T biyectiva:**
> 
> Sean $\mathcal{B}_V = {\vec{v}_1, \ldots, \vec{v}_n}$ base de V
> 
> y $\mathcal{B}_W = {\vec{w}_1, \ldots, \vec{w}_n}$ base de W
> 
> Definir $T(\vec{v}_i) = \vec{w}_i$ para $i = 1, \ldots, n$
> 
> Esta T es lineal (por definición en base) y biyectiva ✓

## 📐 Propiedades y Resultados

> [!note]- Propiedades Adicionales **PROPIEDAD 1: Composición de inyectivas**
> 
> Si $S: U \to V$ y $T: V \to W$ son inyectivas, entonces:
> 
> $$\boxed{T \circ S: U \to W \text{ es inyectiva}}$$
> 
> **DEMOSTRACIÓN:**
> 
> Sea $\vec{u} \in \text{Ker}(T \circ S)$
> 
> Entonces: $(T \circ S)(\vec{u}) = T(S(\vec{u})) = \vec{0}$
> 
> $\implies S(\vec{u}) \in \text{Ker}(T) = {\vec{0}}$ (T inyectiva)
> 
> $\implies S(\vec{u}) = \vec{0}$
> 
> $\implies \vec{u} \in \text{Ker}(S) = {\vec{0}}$ (S inyectiva)
> 
> $\implies \vec{u} = \vec{0}$
> 
> Por tanto: $\text{Ker}(T \circ S) = {\vec{0}}$ ✓
> 
> ---
> 
> **PROPIEDAD 2: Composición de sobreyectivas**
> 
> Si $S: U \to V$ y $T: V \to W$ son sobreyectivas, entonces:
> 
> $$\boxed{T \circ S: U \to W \text{ es sobreyectiva}}$$
> 
> **DEMOSTRACIÓN:**
> 
> Sea $\vec{w} \in W$ arbitrario.
> 
> Como T es sobreyectiva: $\exists \vec{v} \in V : T(\vec{v}) = \vec{w}$
> 
> Como S es sobreyectiva: $\exists \vec{u} \in U : S(\vec{u}) = \vec{v}$
> 
> Entonces: $(T \circ S)(\vec{u}) = T(S(\vec{u})) = T(\vec{v}) = \vec{w}$
> 
> Por tanto: $\text{Im}(T \circ S) = W$ ✓
> 
> ---
> 
> **PROPIEDAD 3: Cancelación (inyectividad)**
> 
> Si $T \circ S$ es inyectiva, entonces:
> 
> $$\boxed{S \text{ es inyectiva}}$$
> 
> (pero T puede no serlo)
> 
> **DEMOSTRACIÓN:**
> 
> $\text{Ker}(S) \subseteq \text{Ker}(T \circ S) = {\vec{0}}$
> 
> Por tanto: $\text{Ker}(S) = {\vec{0}}$ ✓
> 
> ---
> 
> **PROPIEDAD 4: Cancelación (sobreyectividad)**
> 
> Si $T \circ S$ es sobreyectiva, entonces:
> 
> $$\boxed{T \text{ es sobreyectiva}}$$
> 
> (pero S puede no serlo)
> 
> **DEMOSTRACIÓN:**
> 
> $\text{Im}(T) \supseteq \text{Im}(T \circ S) = W$
> 
> Por tanto: $\text{Im}(T) = W$ ✓
> 
> ---
> 
> **PROPIEDAD 5: Rango e inyectividad**
> 
> $$\boxed{\text{rank}(T) = \dim(V) \iff T \text{ es inyectiva}}$$
> 
> (cuando $\dim(V)$ es finita)
> 
> ---
> 
> **PROPIEDAD 6: Rango y sobreyectividad**
> 
> $$\boxed{\text{rank}(T) = \dim(W) \iff T \text{ es sobreyectiva}}$$
> 
> (cuando $\dim(W)$ es finita)

## 💎 Ejemplos Resueltos Detallados

> [!example]- Aplicaciones y Verificaciones **EJEMPLO 1: Verificación de inyectividad**
> 
> Sea $T: \mathbb{R}^3 \to \mathbb{R}^3$ definida por:
> 
> $$T\begin{pmatrix}\begin{bmatrix} x \ y \ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x + y \\ y + z \\ x + z \end{bmatrix}$$
> 
> ¿Es T inyectiva?
> 
> **SOLUCIÓN:**
> 
> **Método 1: Verificar núcleo**
> 
> Encontrar $\text{Ker}(T)$:
> 
> $$T\begin{pmatrix}\begin{bmatrix} x \ y \ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} 0 \ 0 \ 0 \end{bmatrix}$$
> 
> Sistema: $$\begin{cases} x + y = 0 \\ y + z = 0 \\ x + z = 0 \end{cases}$$
> 
> De (1): $y = -x$
> 
> De (2): $z = -y = x$
> 
> Verificar en (3): $x + x = 2x = 0 \implies x = 0$
> 
> Por tanto: $x = y = z = 0$
> 
> $$\boxed{\text{Ker}(T) = {\vec{0}} \implies T \text{ es INYECTIVA}}$$
> 
> **Método 2: Calcular rango**
> 
> Matriz asociada: $$A = \begin{bmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{bmatrix}$$
> 
> Calcular determinante: $$\det(A) = 1(1 - 0) - 1(0 - 1) + 0 = 1 + 1 = 2 \neq 0$$
> 
> $$\boxed{\text{rank}(T) = 3 = \dim(\mathbb{R}^3) \implies T \text{ es INYECTIVA}}$$
> 
> ---
> 
> **EJEMPLO 2: Transformación no inyectiva**
> 
> Sea $T: \mathbb{R}^3 \to \mathbb{R}^2$ definida por:
> 
> $$T\begin{pmatrix}\begin{bmatrix} x \ y \ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x + y \\ 2x + 2y \end{bmatrix}$$
> 
> a) ¿Es T inyectiva? b) Encontrar dos vectores distintos con la misma imagen
> 
> **SOLUCIÓN:**
> 
> **a) Verificar inyectividad:**
> 
> Encontrar $\text{Ker}(T)$:
> 
> $$\begin{cases} x + y = 0 \\ 2x + 2y = 0 \end{cases}$$
> 
> La segunda ecuación es redundante: $y = -x$, $z$ es libre
> 
> $$\text{Ker}(T) = \left\{\begin{bmatrix} -t \ t \ s \end{bmatrix} : t, s \in \mathbb{R}\right\}$$
> 
> $$\text{Ker}(T) = \text{span}\left\{\begin{bmatrix} -1 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}\right\}$$
> 
> $$\boxed{\text{Ker}(T) \neq {\vec{0}} \implies T \text{ NO es inyectiva}}$$
> 
> **b) Vectores con misma imagen:**
> 
> Elegir $\vec{v}_1 = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}$ y $\vec{v}_2 = \begin{bmatrix} 0 \ 1 \ 1 \end{bmatrix}$
> 
> $$T(\vec{v}_1) = \begin{bmatrix} 1 \ 2 \end{bmatrix}$$
> 
> $$T(\vec{v}_2) = \begin{bmatrix} 1 \ 2 \end{bmatrix}$$
> 
> $$\boxed{\vec{v}_1 \neq \vec{v}_2 \text{ pero } T(\vec{v}_1) = T(\vec{v}_2)} \text{ ✓}$$
> 
> ---
> 
> **EJEMPLO 3: Verificación de sobreyectividad**
> 
> Sea $T: \mathbb{R}^3 \to \mathbb{R}^2$ definida por:
> 
> $$T\begin{pmatrix}\begin{bmatrix} x \ y \ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x + y + z \ 2x - y + z \end{bmatrix}$$
> 
> ¿Es T sobreyectiva?
> 
> **SOLUCIÓN:**
> 
> **Método 1: Verificar imagen**
> 
> Dado $\vec{w} = \begin{bmatrix} a \ b \end{bmatrix} \in \mathbb{R}^2$ arbitrario, ¿existe $\vec{v} \in \mathbb{R}^3$ tal que $T(\vec{v}) = \vec{w}$?
> Sistema: $$\begin{cases} x + y + z = a \\ 2x - y + z = b \end{cases}$$
> 
> Restar: $(2x - y + z) - (x + y + z) = b - a$
> 
> $\implies x - 2y = b - a$
> 
> Elegir $z = 0$ (parámetro libre):
> 
> - $y = t$ (libre)
> - $x = b - a + 2t$
> - De (1): $z = a - x - y = a - (b - a + 2t) - t = 2a - b - 3t$
> 
> Solución: $\vec{v} = \begin{bmatrix} b - a + 2t \ t \ 2a - b - 3t \end{bmatrix}$ existe para cualquier $a, b$
> 
> $$\boxed{\text{Im}(T) = \mathbb{R}^2 \implies T \text{ es SOBREYECTIVA}}$$
> 
> **Método 2: Calcular rango**
> 
> Matriz: $$A = \begin{bmatrix} 1 & 1 & 1 \\ 2 & -1 & 1 \end{bmatrix}$$
> 
> Forma escalonada: $$\begin{bmatrix} 1 & 1 & 1 \\ 0 & -3 & -1 \end{bmatrix}$$
> 
> Dos filas pivote $\implies \text{rank}(T) = 2 = \dim(\mathbb{R}^2)$
> 
> $$\boxed{T \text{ es SOBREYECTIVA}}$$
> 
> ---
> 
> **EJEMPLO 4: Operador de derivación**
> 
> Sea $D: \mathcal{P}_3 \to \mathcal{P}_2$ definido por $D(p(x)) = p'(x)$
> 
> Determinar si D es: a) Inyectiva b) Sobreyectiva
> 
> **SOLUCIÓN:**
> 
> **a) Inyectividad:**
> 
> $p(x) \in \text{Ker}(D) \iff p'(x) = 0$
> 
> $\iff p(x) = c$ (constante)
> 
> $$\text{Ker}(D) = {c : c \in \mathbb{R}} = \text{span}{1}$$
> 
> $$\boxed{\text{Ker}(D) \neq {\vec{0}} \implies D \text{ NO es inyectiva}}$$
> 
> **b) Sobreyectividad:**
> 
> Dado $q(x) = ax^2 + bx + c \in \mathcal{P}_2$, ¿existe $p(x) \in \mathcal{P}_3$ tal que $p'(x) = q(x)$?
> 
> Sí: $p(x) = \frac{a}{3}x^3 + \frac{b}{2}x^2 + cx + d$ (donde $d$ es arbitrario)
> 
> Verificar: $p'(x) = ax^2 + bx + c = q(x)$ ✓
> 
> $$\boxed{\text{Im}(D) = \mathcal{P}_2 \implies D \text{ es SOBREYECTIVA}}$$
> 
> **Verificación dimensional:**
> 
> - $\dim(\mathcal{P}_3) = 4$
> - $\text{nullity}(D) = 1$
> - $\text{rank}(D) = 4 - 1 = 3 = \dim(\mathcal{P}_2)$ ✓
> 
> ---
> 
> **EJEMPLO 5: Análisis completo**
> 
> Sea $T: \mathbb{R}^4 \to \mathbb{R}^3$ con matriz:
> 
> $$A = \begin{bmatrix} 1 & 2 & 0 & 1 \\ 0 & 1 & 1 & 0 \\ 1 & 3 & 1 & 1 \end{bmatrix}$$
> 
> Determinar: a) ¿Es inyectiva? b) ¿Es sobreyectiva? c) Dimensión del núcleo d) Dimensión de la imagen
> 
> **SOLUCIÓN:**
> 
> **Forma escalonada reducida:**
> 
> $$\text{rref}(A) = \begin{bmatrix} 1 & 0 & -2 & 1 \\ 0 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
> 
> **c) Dimensión del núcleo:**
> 
> Variables libres: $x_3, x_4$
> 
> $$\boxed{\text{nullity}(T) = 2}$$
> 
> **d) Dimensión de la imagen:**
> 
> Número de pivotes = 2
> 
> $$\boxed{\text{rank}(T) = 2}$$
> 
> **Verificación:** $4 = 2 + 2$ ✓
> 
> **a) Inyectividad:**
> 
> $$\text{nullity}(T) = 2 \neq 0$$
> 
> $$\boxed{T \text{ NO es inyectiva}}$$
> 
> Alternativamente: $\dim(\mathbb{R}^4) > \dim(\mathbb{R}^3)$ (imposible ser inyectiva)
> 
> **b) Sobreyectividad:**
> 
> $$\text{rank}(T) = 2 \neq 3 = \dim(\mathbb{R}^3)$$
> 
> $$\boxed{T \text{ NO es sobreyectiva}}$$

## 🎭 Casos Especiales y Aplicaciones

> [!tip]- Situaciones Particulares **CASO 1: Proyecciones**
> 
> Una proyección $P: V \to V$ satisface $P^2 = P$.
> 
> **Propiedades:**
> 
> - $P$ nunca es inyectiva (salvo que $P = \text{Id}$)
> - $\text{Ker}(P) = {v - P(v) : v \in V}$
> - $\text{Im}(P) = {P(v) : v \in V}$
> - $V = \text{Ker}(P) \oplus \text{Im}(P)$
> 
> **Ejemplo:** Proyección sobre el plano $xy$ en $\mathbb{R}^3$
> 
> $$P\begin{pmatrix}\begin{bmatrix} x \ y \ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x \ y \ 0 \end{bmatrix}$$
> 
> - $\text{Ker}(P) = \text{span}{\vec{e}_3}$ (eje $z$)
> - $\text{Im}(P) = \text{span}{\vec{e}_1, \vec{e}_2}$ (plano $xy$)
> - No inyectiva: $\text{nullity}(P) = 1$
> - Sobreyectiva sobre su imagen (pero $\text{Im}(P) \neq \mathbb{R}^3$)
> 
> ---
> 
> **CASO 2: Rotaciones**
> 
> Rotaciones $R: \mathbb{R}^n \to \mathbb{R}^n$ son siempre biyectivas.
> 
> **Propiedades:**
> 
> - $\text{Ker}(R) = {\vec{0}}$ (inyectiva)
> - $\text{Im}(R) = \mathbb{R}^n$ (sobreyectiva)
> - $\det(R) = \pm 1$
> - Preservan longitudes y ángulos
> 
> ---
> 
> **CASO 3: Dilataciones**
> 
> Dilatación $D_k: \mathbb{R}^n \to \mathbb{R}^n$ con $D_k(\vec{v}) = k\vec{v}$
> 
> **Propiedades:**
> 
> - Si $k \neq 0$: biyectiva
> - Si $k = 0$: $D_0 = T_0$ (transformación cero, no inyectiva ni sobreyectiva)
> 
> ---
> 
> **CASO 4: Inclusión**
> 
> Inclusión $i: V \to W$ donde $V \subseteq W$
> 
> $$i(\vec{v}) = \vec{v}$$
> 
> **Propiedades:**
> 
> - Siempre inyectiva
> - Sobreyectiva $\iff V = W$
> - $\text{Ker}(i) = {\vec{0}}$
> - $\text{Im}(i) = V$
> 
> ---
> 
> **CASO 5: Transformación cero**
> 
> $T_0: V \to W$ con $T_0(\vec{v}) = \vec{0}$ para todo $\vec{v}$
> 
> **Propiedades:**
> 
> - Nunca inyectiva (salvo que $V = {\vec{0}}$)
> - Nunca sobreyectiva (salvo que $W = {\vec{0}}$)
> - $\text{Ker}(T_0) = V$
> - $\text{Im}(T_0) = {\vec{0}}$

## 📊 Tabla de Referencia Rápida

> [!note]- Guía de Consulta **CARACTERIZACIONES:**
> 
> |Propiedad|Condición por núcleo|Condición por rango|Condición dimensional|
> |---|---|---|---|
> |**Inyectiva**|$\text{Ker}(T) = {\vec{0}}$|$\text{rank}(T) = \dim(V)$|$\text{nullity}(T) = 0$|
> |**Sobreyectiva**|—|$\text{rank}(T) = \dim(W)$|$\text{Im}(T) = W$|
> |**Biyectiva**|$\text{Ker}(T) = {\vec{0}}$ Y|$\text{rank}(T) = \dim(V)$|Ambas condiciones|
> ||$\text{Im}(T) = W$|$= \dim(W)$||
> 
> **RESTRICCIONES DIMENSIONALES:**
> 
> |Relación|Inyectividad|Sobreyectividad|Biyectividad|
> |---|---|---|---|
> |$\dim(V) > \dim(W)$|❌ Imposible|✓ Posible|❌ Imposible|
> |$\dim(V) = \dim(W)$|✓ Posible|✓ Posible|✓ Posible|
> |$\dim(V) < \dim(W)$|✓ Posible|❌ Imposible|❌ Imposible|
> 
> **EQUIVALENCIAS (dim(V) = dim(W)):**
> 
> $$\text{Inyectiva} \iff \text{Sobreyectiva} \iff \text{Biyectiva} \iff \text{Invertible}$$
> 
> **COMPOSICIÓN:**
> 
> |$S: U \to V$|$T: V \to W$|$T \circ S$|
> |---|---|---|
> |Inyectiva|Inyectiva|Inyectiva|
> |Sobreyectiva|Sobreyectiva|Sobreyectiva|
> |Biyectiva|Biyectiva|Biyectiva|
> 
> **CANCELACIÓN:**
> 
> - Si $T \circ S$ inyectiva $\implies S$ inyectiva
> - Si $T \circ S$ sobreyectiva $\implies T$ sobreyectiva

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes **1. "Inyectiva significa que rank(T) = dim(W)"**
> 
> ❌ **ERROR DE CONFUSIÓN**
> 
> ✅ **CORRECTO:**
> 
> - Inyectiva: $\text{rank}(T) = \dim(V)$
> - Sobreyectiva: $\text{rank}(T) = \dim(W)$
> 
> **Ejemplo:** $T: \mathbb{R}^2 \to \mathbb{R}^3$, $T\begin{pmatrix}\begin{bmatrix} x\y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x\y\0 \end{bmatrix}$
> 
> - Inyectiva: rank(T) = 2 = dim($\mathbb{R}^2$) ✓
> - Pero rank(T) = 2 ≠ 3 = dim($\mathbb{R}^3$) ✗
> 
> ---
> 
> **2. "Si dim(V) = dim(W), entonces T es automáticamente biyectiva"**
> 
> ❌ **FALSO**
> 
> Dimensiones iguales solo significa que **PUEDE** existir biyección, no que toda T lo sea.
> 
> **Contraejemplo:** $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T\begin{pmatrix}\begin{bmatrix} x\y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x\0 \end{bmatrix}$
> 
> - $\dim(\mathbb{R}^2) = \dim(\mathbb{R}^2) = 2$
> - Pero nullity(T) = 1 (no inyectiva)
> - Y rank(T) = 1 ≠ 2 (no sobreyectiva)
> 
> ---
> 
> **3. "Ker(T) = {0} implica que T es sobreyectiva"**
> 
> ❌ **FALSO** (en general)
> 
> Ker(T) = {0} solo implica **inyectividad**.
> 
> ✅ **CORRECTO:** Si además $\dim(V) = \dim(W)$, entonces sí implica sobreyectividad.
> 
> **Contraejemplo:** $T: \mathbb{R}^2 \to \mathbb{R}^3$, $T\begin{pmatrix}\begin{bmatrix} x\y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x\y\0 \end{bmatrix}$
> 
> - Ker(T) = {0} (inyectiva) ✓
> - Pero Im(T) ≠ $\mathbb{R}^3$ (no sobreyectiva)
> 
> ---
> 
> **4. "Si T no es inyectiva, entonces no puede ser sobreyectiva"**
> 
> ❌ **FALSO**
> 
> Las propiedades son independientes cuando las dimensiones son diferentes.
> 
> **Contraejemplo:** $T: \mathbb{R}^3 \to \mathbb{R}^2$, $T\begin{pmatrix}\begin{bmatrix} x\y\z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x+y\y+z \end{bmatrix}$
> 
> - No inyectiva (dim(V) > dim(W))
> - Pero puede ser sobreyectiva (rank = 2)
> 
> ---
> 
> **5. "rank(T) < dim(V) significa que T no es sobreyectiva"**
> 
> ❌ **NO NECESARIAMENTE**
> 
> Depende de dim(W).
> 
> ✅ **CORRECTO:** Si rank(T) < dim(W), entonces T no es sobreyectiva.
> 
> **Ejemplo:** $T: \mathbb{R}^4 \to \mathbb{R}^2$ con rank(T) = 2
> 
> - rank(T) = 2 < 4 = dim(V)
> - Pero rank(T) = 2 = dim(W) (SÍ es sobreyectiva)
> 
> ---
> 
> **6. "Toda transformación lineal es inyectiva o sobreyectiva"**
> 
> ❌ **FALSO**
> 
> Puede no ser ninguna de las dos.
> 
> **Ejemplo:** $T: \mathbb{R}^3 \to \mathbb{R}^3$, $T\begin{pmatrix}\begin{bmatrix} x\y\z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x\0\0 \end{bmatrix}$
> 
> - nullity(T) = 2 ≠ 0 (no inyectiva)
> - rank(T) = 1 ≠ 3 (no sobreyectiva)
> 
> ---
> 
> **7. "Si T: V → V es inyectiva, entonces T² también lo es"**
> 
> ✅ **VERDADERO** (por composición de inyectivas)
> 
> Pero cuidado: Si T no es inyectiva, T² puede serlo o no.

## 🔗 Conexiones con Otros Temas

> [!quote]- Enlaces Conceptuales **Fundamentos previos:**
> 
> - [[01 - Transformaciones lineales]] - Definición básica
> - [[19 - Núcleo e Imagen]] - Subespacios fundamentales
> - [[03 - Teorema de la dimensión]] - Relación rank-nullity
> - [[06 - Independencia lineal]] - Bases y generadores
> 
> **Temas directamente relacionados:**
> 
> - [[04 - Isomorfismos]] - Biyecciones lineales
> - [[05 - Espacio columna]] - Caracterización de imagen
> - [[17 - Espacio nulo]] - Caracterización de núcleo
> - [[21 - Rango de matrices]] - Aplicación matricial
> 
> **Aplicaciones posteriores:**
> 
> - [[22 - Sistemas de ecuaciones lineales]] - Existencia y unicidad
> - [[23 - Matriz inversa]] - Biyectividad y matrices
> - [[24 - Valores propios]] - Análisis de Ker(T - λI)
> - [[30 - Proyecciones]] - Casos no inyectivos
> - [[35 - SVD]] - Descomposición fundamental
> 
> **Conceptos avanzados:**
> 
> - [[40 - Teorema espectral]] - Operadores biyectivos
> - [[45 - Teoría de categorías]] - Monomorfismos/epimorfismos
> - [[50 - Análisis funcional]] - Operadores en espacios infinitos

## 📚 Bibliografía Esencial

> [!tip]- Lecturas Recomendadas **Nivel introductorio:**
> 
> - **Lay, D. C.** (2016). _Álgebra Lineal y sus Aplicaciones_ (5ª ed.). Pearson.
>     - **Cap. 1.7-1.9:** Transformaciones lineales ⭐
>     - Excelentes ejemplos visuales
> - **Strang, G.** (2016). _Introduction to Linear Algebra_ (5th ed.). Wellesley-Cambridge.
>     - **Cap. 3.1:** The Four Fundamental Subspaces
>     - Interpretación geométrica clara
> 
> **Nivel intermedio:**
> 
> - **Poole, D.** (2011). _Álgebra Lineal: Una Introducción Moderna_ (3ª ed.). Cengage.
>     - Cap. 6.2: One-to-One and Onto
>     - Muchos ejemplos aplicados
> - **Anton, H., & Rorres, C.** (2014). _Elementary Linear Algebra_ (11th ed.). Wiley.
>     - Cap. 8: Linear Transformations
>     - Caracterizaciones completas
> 
> **Nivel avanzado:**
> 
> - **Axler, S.** (2015). _Linear Algebra Done Right_ (3rd ed.). Springer.
>     - **Cap. 3.B:** Null Spaces and Ranges ⭐⭐⭐
>     - Tratamiento elegante sin matrices
>     - Enfoque en espacios vectoriales abstractos
> - **Hoffman, K., & Kunze, R.** (1971). _Linear Algebra_ (2nd ed.). Prentice Hall.
>     - Cap. 2.3-2.4: Isomorphism
>     - Tratamiento riguroso completo
> 
> **Contexto teórico:**
> 
> - **Lang, S.** (2004). _Linear Algebra_ (3rd ed.). Springer.
>     - Teoría abstracta completa
>     - Conexión con categorías
> - **MacLane, S., & Birkhoff, G.** (1999). _Algebra_ (3rd ed.). AMS Chelsea.
>     - Monomorfismos y epimorfismos
>     - Perspectiva categórica

## 🎓 Conceptos Clave - Resumen

> [!important]- Ideas Fundamentales para Recordar **DEFINICIONES CENTRALES:**
> 
> $$\boxed{\begin{align} \text{Inyectiva:} & \quad \text{Ker}(T) = {\vec{0}} \ \text{Sobreyectiva:} & \quad \text{Im}(T) = W \ \text{Biyectiva:} & \quad \text{Ambas} \end{align}}$$
> 
> **CARACTERIZACIONES DIMENSIONALES:**
> 
> $$\boxed{\begin{align} T \text{ inyectiva} & \iff \text{rank}(T) = \dim(V) \ T \text{ sobreyectiva} & \iff \text{rank}(T) = \dim(W) \ T \text{ biyectiva} & \iff \text{rank}(T) = \dim(V) = \dim(W) \end{align}}$$
> 
> **TEOREMAS DE IMPOSIBILIDAD:**
> 
> 1. $\dim(V) > \dim(W) \implies$ No puede ser inyectiva
> 2. $\dim(V) < \dim(W) \implies$ No puede ser sobreyectiva
> 3. $\dim(V) \neq \dim(W) \implies$ No puede ser biyectiva
> 
> **EQUIVALENCIA (dim(V) = dim(W)):**
> 
> $$\boxed{\text{Inyectiva} \iff \text{Sobreyectiva} \iff \text{Biyectiva} \iff \text{Invertible}}$$
> 
> **PROPIEDADES DE COMPOSICIÓN:**
> 
> - Inyectiva ∘ Inyectiva = Inyectiva
> - Sobreyectiva ∘ Sobreyectiva = Sobreyectiva
> - Biyectiva ∘ Biyectiva = Biyectiva
> 
> **APLICACIÓN PRÁCTICA:**
> 
> Para verificar:
> 
> 1. **Inyectividad:** Resolver $T(\vec{x}) = \vec{0}$, verificar que solo $\vec{x} = \vec{0}$
> 2. **Sobreyectividad:** Verificar que rank(T) = dim(W) o que todo $\vec{w} \in W$ tiene preimagen
> 3. **Biyectividad:** Verificar ambas o que det(A) ≠ 0 (si es operador cuadrado)
> 
> **CONEXIÓN CON RANGO-NULIDAD:**
> 
> $$\dim(V) = \text{nullity}(T) + \text{rank}(T)$$
> 
> - Inyectiva: nullity = 0, rank = dim(V)
> - Sobreyectiva: rank = dim(W)
> - Biyectiva: nullity = 0, rank = dim(V) = dim(W)

---

**Tags:** #algebra-lineal #transformaciones-lineales #inyectividad #sobreyectividad #biyectividad #isomorfismo #nucleo #imagen #rank-nullity #invertibilidad #espacios-vectoriales