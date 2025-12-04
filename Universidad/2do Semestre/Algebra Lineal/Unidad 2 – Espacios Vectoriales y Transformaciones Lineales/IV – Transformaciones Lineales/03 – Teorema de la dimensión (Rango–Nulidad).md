# 📐 Teorema de la Dimensión (Rango–Nulidad)

## 🌟 Concepto Fundamental

> [!info]- Definición Intuitiva **El Teorema de la Dimensión, también conocido como Teorema del Rango-Nulidad, es uno de los resultados más fundamentales del álgebra lineal. Establece que la dimensión del dominio de una transformación lineal se "conserva" dividiéndose entre lo que se "pierde" (núcleo) y lo que se "alcanza" (imagen). Esta conservación dimensional es una ley fundamental de las transformaciones lineales.**
> 
> **Características clave:**
> 
> - **Conservación:** La dimensión total se preserva
> - **Partición:** Divide entre pérdida y alcance
> - **Universalidad:** Vale para todas las transformaciones lineales
> - **Predictibilidad:** Conociendo dos valores, determina el tercero
> - **Fundamento:** Base para teoría de transformaciones

### 📖 Contexto Histórico

> [!note]- Desarrollo del Concepto **Orígenes matriciales (1850-1880):**
> 
> - **Sylvester (1850s):** Ley de nulidad
>     - Primera versión para matrices
>     - "Nullity law": relaciona rango y soluciones
>     - Contexto: teoría de invariantes
> - **Cayley (1858):** Teoría de matrices
>     - Álgebra de transformaciones lineales
>     - Concepto de rango de matriz
> - **Frobenius (1879):** Teorema del rango
>     - Formulación precisa para matrices
>     - Relación rango-defecto
>     - "Rank theorem" en teoría de matrices
> 
> **Formulación geométrica (1880-1920):**
> 
> - **Grassmann (1844/1862):** Ausdehnungslehre
>     - Espacios lineales abstractos
>     - Dimensión como concepto geométrico
>     - Adelantado a su tiempo
> - **Peano (1888):** Axiomas de espacios vectoriales
>     - Marco formal para el teorema
>     - Dimensión bien definida
> - **Weyl (1910s):** Síntesis geométrica-algebraica
>     - Interpretación en espacios vectoriales
>     - Aplicaciones a ecuaciones diferenciales
> 
> **Era abstracta (1920-1940):**
> 
> - **Emmy Noether (1920s):** Álgebra moderna
>     - Teorema fundamental de homomorfismos
>     - $V/\text{Ker}(T) \cong \text{Im}(T)$
>     - Marco categórico
> - **van der Waerden (1930):** "Moderne Algebra"
>     - Presentación moderna del teorema
>     - Enfoque estructural
> - **Banach (1932):** Espacios normados
>     - Versión para espacios infinito-dimensionales
>     - Operadores acotados
> 
> **Análisis funcional (1940-1960):**
> 
> - **von Neumann (1930s-40s):** Operadores en Hilbert
>     - Teoría espectral
>     - Dimensión de subespacios invariantes
> - **Atiyah-Singer (1960s):** Teorema del índice
>     - Generalización topológica profunda
>     - Índice = dim(Ker) - dim(Coker)
>     - Conexión análisis-topología
> 
> **Síntesis contemporánea (1960-presente):**
> 
> - **Bourbaki:** Formalización categórica
>     - Exactitud de sucesiones
>     - Teorema como caso especial
> - **Aplicaciones masivas:**
>     - Machine learning (dimensión efectiva)
>     - Compresión de datos
>     - Teoría de control
>     - Procesamiento de señales
> 
> **Nota histórica:** El nombre "Rank-Nullity Theorem" es predominante en literatura anglosajona, mientras que "Teorema de la Dimensión" es común en literatura europea. Ambos se refieren al mismo resultado fundamental.

## 📊 Enunciado del Teorema

> [!important]- Teorema de la Dimensión (Rank-Nullity) **TEOREMA:**
> 
> Sea $T: V \to W$ una transformación lineal donde $V$ tiene dimensión finita.
> 
> $$\boxed{\dim(V) = \dim(\text{Ker}(T)) + \dim(\text{Im}(T))}$$
> 
> **O equivalentemente:**
> 
> $$\boxed{\dim(V) = \text{nullity}(T) + \text{rank}(T)}$$
> 
> donde:
> 
> - $\dim(V)$ = dimensión del dominio
> - $\text{nullity}(T) = \dim(\text{Ker}(T))$ = dimensión del núcleo
> - $\text{rank}(T) = \dim(\text{Im}(T))$ = dimensión de la imagen
> 
> **NOTACIÓN ALTERNATIVA:**
> 
> Para matriz $A$ de $m \times n$: $$\boxed{n = \text{nullity}(A) + \text{rank}(A)}$$
> 
> El número de columnas es la suma del rango y la nulidad.
> 
> **INTERPRETACIÓN VISUAL:**
> 
> ```
>           Dimensión de V (total)
>           ╱─────────────────╲
>          ╱                   ╲
>     nullity(T)           rank(T)
>    (se pierde)          (se alcanza)
>         │                    │
>         │                    │
>         ↓                    ↓
>      Ker(T)               Im(T)
>    (colapsa a 0)     (espacio imagen)
> ```
> 
> **PRINCIPIO DE CONSERVACIÓN:**
> 
> La dimensión del dominio se **conserva** pero se **distribuye**:
> 
> - Una parte en el núcleo (información perdida)
> - Una parte en la imagen (información preservada)

## 🎯 Demostración Completa

> [!success]- Prueba del Teorema **DEMOSTRACIÓN:**
> 
> Sea $T: V \to W$ transformación lineal con $\dim(V) = n$.
> 
> **Objetivo:** Probar que $n = \dim(\text{Ker}(T)) + \dim(\text{Im}(T))$
> 
> ---
> 
> **PASO 1: Construir base del núcleo**
> 
> Sea $k = \dim(\text{Ker}(T))$.
> 
> Elegir base de $\text{Ker}(T)$: $$\mathcal{B}_{\text{Ker}} = {\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k}$$
> 
> Por definición, estos vectores son linealmente independientes y generan $\text{Ker}(T)$.
> 
> ---
> 
> **PASO 2: Extender a base de V**
> 
> Por el **Teorema de Extensión de Bases**:
> 
> Todo conjunto L.I. en un espacio vectorial puede extenderse a una base completa.
> 
> Extender $\mathcal{B}_{\text{Ker}}$ a base de $V$: $$\mathcal{B}_V = {\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k, \vec{u}_1, \vec{u}_2, \ldots, \vec{u}_r}$$
> 
> donde $k + r = n = \dim(V)$.
> 
> Los vectores ${\vec{u}_1, \ldots, \vec{u}_r}$ son los **nuevos vectores** añadidos.
> 
> ---
> 
> **PASO 3: Considerar las imágenes de los vectores base**
> 
> Aplicar $T$ a cada vector de la base:
> 
> **Para vectores del núcleo:** $$T(\vec{v}_i) = \vec{0} \quad \text{para } i = 1, \ldots, k$$
> 
> (por definición de núcleo)
> 
> **Para los nuevos vectores:** $$T(\vec{u}_j) \quad \text{para } j = 1, \ldots, r$$
> 
> (estos vectores NO están en el núcleo)
> 
> ---
> 
> **PASO 4: Probar que ${T(\vec{u}_1), \ldots, T(\vec{u}_r)}$ genera Im(T)**
> 
> Sea $\vec{w} \in \text{Im}(T)$ arbitrario.
> 
> Por definición: $\exists \vec{v} \in V$ tal que $\vec{w} = T(\vec{v})$.
> 
> Como $\mathcal{B}_V$ es base de $V$: $$\vec{v} = c_1\vec{v}_1 + \cdots + c_k\vec{v}_k + d_1\vec{u}_1 + \cdots + d_r\vec{u}_r$$
> 
> Aplicando $T$ y usando linealidad: $$\vec{w} = T(\vec{v}) = c_1T(\vec{v}_1) + \cdots + c_kT(\vec{v}_k) + d_1T(\vec{u}_1) + \cdots + d_rT(\vec{u}_r)$$
> 
> Como $T(\vec{v}_i) = \vec{0}$ para $i = 1, \ldots, k$: $$\vec{w} = d_1T(\vec{u}_1) + \cdots + d_rT(\vec{u}_r)$$
> 
> Por tanto, $\vec{w} \in \text{span}{T(\vec{u}_1), \ldots, T(\vec{u}_r)}$.
> 
> Como $\vec{w}$ era arbitrario: $$\text{Im}(T) = \text{span}{T(\vec{u}_1), \ldots, T(\vec{u}_r)}$$ ✓
> 
> ---
> 
> **PASO 5: Probar que ${T(\vec{u}_1), \ldots, T(\vec{u}_r)}$ son L.I.**
> 
> Suponer que: $$c_1T(\vec{u}_1) + c_2T(\vec{u}_2) + \cdots + c_rT(\vec{u}_r) = \vec{0}$$
> 
> Por linealidad de $T$: $$T(c_1\vec{u}_1 + c_2\vec{u}_2 + \cdots + c_r\vec{u}_r) = \vec{0}$$
> 
> Esto significa que: $$c_1\vec{u}_1 + c_2\vec{u}_2 + \cdots + c_r\vec{u}_r \in \text{Ker}(T)$$
> 
> Como ${\vec{v}_1, \ldots, \vec{v}_k}$ es base de $\text{Ker}(T)$: $$c_1\vec{u}_1 + \cdots + c_r\vec{u}_r = a_1\vec{v}_1 + \cdots + a_k\vec{v}_k$$
> 
> para algunos escalares $a_1, \ldots, a_k$.
> 
> Reordenando: $$c_1\vec{u}_1 + \cdots + c_r\vec{u}_r - a_1\vec{v}_1 - \cdots - a_k\vec{v}_k = \vec{0}$$
> 
> Pero $\mathcal{B}_V = {\vec{v}_1, \ldots, \vec{v}_k, \vec{u}_1, \ldots, \vec{u}_r}$ es base de $V$, por tanto estos vectores son **linealmente independientes**.
> 
> La única solución es: $$c_1 = c_2 = \cdots = c_r = a_1 = a_2 = \cdots = a_k = 0$$
> 
> En particular: $c_1 = c_2 = \cdots = c_r = 0$.
> 
> Por tanto ${T(\vec{u}_1), \ldots, T(\vec{u}_r)}$ son **linealmente independientes** ✓
> 
> ---
> 
> **PASO 6: Conclusión**
> 
> Hemos probado que ${T(\vec{u}_1), \ldots, T(\vec{u}_r)}$:
> 
> - Genera $\text{Im}(T)$ (Paso 4)
> - Son linealmente independientes (Paso 5)
> 
> Por tanto, ${T(\vec{u}_1), \ldots, T(\vec{u}_r)}$ es **base de Im(T)**.
> 
> Consecuencia: $$\dim(\text{Im}(T)) = r$$
> 
> De Paso 2 sabemos que: $$k + r = n = \dim(V)$$
> 
> Sustituyendo $k = \dim(\text{Ker}(T))$ y $r = \dim(\text{Im}(T))$:
> 
> $$\boxed{\dim(\text{Ker}(T)) + \dim(\text{Im}(T)) = \dim(V)}$$ ✓
> 
> **Q.E.D.**
> 
> ---
> 
> **DIAGRAMA DE LA DEMOSTRACIÓN:**
> 
> ```
> V (dim = n)
> Base: {v₁,...,vₖ, u₁,...,uᵣ}
>       ↙           ↘
>   Ker(T)         resto
>  (dim = k)      (dim = r)
>      ↓             ↓
>      0          T(u₁),...,T(uᵣ)
>                     ↓
>                  Im(T)
>                 (dim = r)
> 
> n = k + r ✓
> ```

## 💎 Consecuencias Fundamentales

> [!success]- Corolarios Importantes **COROLARIO 1: Inyectividad en dimensiones iguales**
> 
> Sea $T: V \to W$ lineal con $\dim(V) = \dim(W) = n$.
> 
> Entonces las siguientes afirmaciones son **equivalentes**:
> 
> 1. $T$ es inyectiva
> 2. $T$ es sobreyectiva
> 3. $T$ es biyectiva (isomorfismo)
> 4. $\text{Ker}(T) = {\vec{0}}$
> 5. $\text{Im}(T) = W$
> 6. $\text{rank}(T) = n$
> 7. $\text{nullity}(T) = 0$
> 
> **DEMOSTRACIÓN:**
> 
> Por teorema: $n = \text{nullity}(T) + \text{rank}(T)$
> 
> $(1) \Rightarrow (4)$: Por definición de inyectividad ✓
> 
> $(4) \Rightarrow (7)$: $\text{Ker}(T) = {\vec{0}} \implies \text{nullity}(T) = 0$ ✓
> 
> $(7) \Rightarrow (6)$: $n = 0 + \text{rank}(T) \implies \text{rank}(T) = n$ ✓
> 
> $(6) \Rightarrow (5)$: $\text{rank}(T) = \dim(\text{Im}(T)) = n = \dim(W) \implies \text{Im}(T) = W$ ✓
> 
> $(5) \Rightarrow (2)$: Por definición de sobreyectividad ✓
> 
> $(2) \land (1) \Rightarrow (3)$: Definición de biyectividad ✓
> 
> $(3) \Rightarrow (1)$: Biyectiva implica inyectiva ✓
> 
> ---
> 
> **COROLARIO 2: Imposibilidad de inyección**
> 
> Si $\dim(V) > \dim(W)$, entonces **NO EXISTE** transformación lineal inyectiva $T: V \to W$.
> 
> **DEMOSTRACIÓN:**
> 
> Sea $\dim(V) = n$ y $\dim(W) = m$ con $n > m$.
> 
> Para cualquier $T: V \to W$: $$\text{rank}(T) = \dim(\text{Im}(T)) \leq \dim(W) = m < n$$
> 
> Por teorema: $$\text{nullity}(T) = n - \text{rank}(T) \geq n - m > 0$$
> 
> Por tanto $\dim(\text{Ker}(T)) > 0$, lo que implica $\text{Ker}(T) \neq {\vec{0}}$.
> 
> Conclusión: $T$ **no puede ser inyectiva** ✓
> 
> **Intuición:** "No se puede inyectar un espacio grande en uno pequeño sin colapsar algo."
> 
> ---
> 
> **COROLARIO 3: Imposibilidad de sobreyección**
> 
> Si $\dim(V) < \dim(W)$, entonces **NO EXISTE** transformación lineal sobreyectiva $T: V \to W$.
> 
> **DEMOSTRACIÓN:**
> 
> Sea $\dim(V) = n$ y $\dim(W) = m$ con $n < m$.
> 
> Por teorema: $$\text{rank}(T) = n - \text{nullity}(T) \leq n < m = \dim(W)$$
> 
> Por tanto $\dim(\text{Im}(T)) < \dim(W)$, lo que implica $\text{Im}(T) \neq W$.
> 
> Conclusión: $T$ **no puede ser sobreyectiva** ✓
> 
> **Intuición:** "No se puede cubrir un espacio grande desde uno pequeño."
> 
> ---
> 
> **COROLARIO 4: Rango máximo**
> 
> Para cualquier $T: V \to W$: $$\boxed{\text{rank}(T) \leq \min{\dim(V), \dim(W)}}$$
> 
> **DEMOSTRACIÓN:**
> 
> - $\text{rank}(T) = \dim(\text{Im}(T)) \leq \dim(W)$ (la imagen está contenida en $W$)
> - $\text{rank}(T) \leq \dim(V)$ (por teorema, ya que nullity ≥ 0)
> 
> Por tanto: $\text{rank}(T) \leq \min{\dim(V), \dim(W)}$ ✓
> 
> ---
> 
> **COROLARIO 5: Determinación de valores**
> 
> Conociendo **cualquier dos** de los tres valores:
> 
> - $\dim(V)$
> - $\text{nullity}(T)$
> - $\text{rank}(T)$
> 
> Se puede determinar el **tercero** usando: $$\dim(V) = \text{nullity}(T) + \text{rank}(T)$$
> 
> **EJEMPLOS:**
> 
> a) Si $T: \mathbb{R}^7 \to \mathbb{R}^5$ con $\text{rank}(T) = 4$: $$\text{nullity}(T) = 7 - 4 = 3$$
> 
> b) Si $T: \mathbb{R}^6 \to \mathbb{R}^4$ con $\text{nullity}(T) = 2$: $$\text{rank}(T) = 6 - 2 = 4$$
> 
> c) Si $T: \mathbb{R}^n \to \mathbb{R}^m$ es inyectiva (nullity = 0): $$\text{rank}(T) = n$$

## 🔍 Interpretaciones Geométricas

> [!note]- Visualización del Teorema **INTERPRETACIÓN 1: Descomposición del dominio**
> 
> El teorema establece una descomposición fundamental: $$V = \text{Ker}(T) \oplus U$$
> 
> donde $U$ es complemento de $\text{Ker}(T)$ con $\dim(U) = \text{rank}(T)$.
> 
> ```
>          V
>         ╱ ╲
>        ╱   ╲
>    Ker(T)   U
>       ↓      ↓
>       0   Im(T)
>             (isomorfismo)
> ```
> 
> - La parte $\text{Ker}(T)$ se "colapsa" a cero
> - La parte $U$ se mapea isomórficamente a $\text{Im}(T)$
> - Dimensiones: $\dim(V) = \dim(\text{Ker}(T)) + \dim(U)$
> 
> ---
> 
> **INTERPRETACIÓN 2: Conservación de información**
> 
> La transformación $T$ actúa como un "canal" que transmite información:
> 
> ```
> Información total = Información perdida + Información transmitida
>       dim(V)      =    nullity(T)     +      rank(T)
> ```
> 
> - **Información perdida:** Dimensión del núcleo
> - **Información transmitida:** Dimensión de la imagen
> - **Total conservado:** Dimensión del dominio
> 
> ---
> 
> **INTERPRETACIÓN 3: Grados de libertad**
> 
> Para ecuación $T(\vec{x}) = \vec{b}$:
> 
> - **Si tiene solución:**
>     - Solución particular: $\vec{x}_p$
>     - Soluciones generales: $\vec{x} = \vec{x}_p + \vec{h}$ donde $\vec{h} \in \text{Ker}(T)$
>     - Grados de libertad: $\dim(\text{Ker}(T))$ parámetros libres
> - **Restricciones vs Libertad:**
>     - $\text{rank}(T)$ = número de restricciones efectivas
>     - $\text{nullity}(T)$ = número de parámetros libres
>     - Suma = dimensión total del espacio
> 
> ---
> 
> **INTERPRETACIÓN 4: Proyección y pérdida**
> 
> Para proyección $P: \mathbb{R}^3 \to \mathbb{R}^3$ sobre el plano $xy$:
> 
> $$P\begin{pmatrix}\begin{bmatrix} x \ y \ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x \ y \ 0 \end{bmatrix}$$
> 
> ```
>       ℝ³ (dim = 3)
>        │
>    ┌───┴───┐
>    │       │
> eje z   plano xy
> (ker)   (imagen)
> dim=1   dim=2
> 
> 3 = 1 + 2 ✓
> ```
> 
> - **Se pierde:** Componente $z$ (núcleo, dim = 1)
> - **Se preserva:** Componentes $x, y$ (imagen, dim = 2)
> - **Total:** 3 dimensiones

## 📝 Ejemplos Resueltos Detallados

> [!example]- Aplicaciones del Teorema **EJEMPLO 1: Determinar posibilidades**
> 
> Sea $T: \mathbb{R}^5 \to \mathbb{R}^3$ transformación lineal con $\text{rank}(T) = 3$.
> 
> Determinar:
> 
> - a) $\text{nullity}(T)$
> - b) ¿Es $T$ inyectiva?
> - c) ¿Es $T$ sobreyectiva?
> - d) Dimensión del conjunto de soluciones de $T(\vec{x}) = \vec{0}$
> 
> **SOLUCIÓN:**
> 
> **a) Nulidad:**
> 
> Por teorema: $$5 = \text{nullity}(T) + 3$$ $$\boxed{\text{nullity}(T) = 2}$$
> 
> **b) Inyectividad:**
> 
> $T$ es inyectiva $\iff \text{nullity}(T) = 0$
> 
> Como $\text{nullity}(T) = 2 \neq 0$: $$\boxed{\text{NO es inyectiva}}$$
> 
> **c) Sobreyectividad:**
> 
> $T$ es sobreyectiva $\iff \text{rank}(T) = \dim(\mathbb{R}^3) = 3$
> 
> Como $\text{rank}(T) = 3$: $$\boxed{\text{SÍ es sobreyectiva}}$$
> 
> **d) Espacio de soluciones:**
> 
> El conjunto de soluciones de $T(\vec{x}) = \vec{0}$ es $\text{Ker}(T)$.
> 
> $$\boxed{\dim(\text{soluciones}) = \dim(\text{Ker}(T)) = 2}$$
> 
> Es un subespacio de dimensión 2 en $\mathbb{R}^5$ (un "plano" en 5D).
> 
> ---
> 
> **EJEMPLO 2: Análisis de matriz**
> 
> Sea $A$ matriz de $4 \times 6$ con $\text{nullity}(A) = 2$.
> 
> Encontrar:
> 
> - a) $\text{rank}(A)$
> - b) Dimensión de $\text{Col}(A)$
> - c) Número de columnas pivote
> - d) Número de variables libres en $A\vec{x} = \vec{0}$
> 
> **SOLUCIÓN:**
> 
> **a) Rango:**
> 
> $A$ tiene 6 columnas, por tanto $\dim(\text{dominio}) = 6$
> 
> Por teorema: $$6 = 2 + \text{rank}(A)$$ $$\boxed{\text{rank}(A) = 4}$$
> 
> **b) Espacio columna:**
> 
> $$\text{Col}(A) = \text{Im}(A)$$ $$\boxed{\dim(\text{Col}(A)) = \text{rank}(A) = 4}$$
> 
> **c) Columnas pivote:**
> 
> El número de columnas pivote = $\text{rank}(A)$ $$\boxed{\text{4 columnas pivote}}$$
> 
> **d) Variables libres:**
> 
> Variables libres = Variables totales - Variables básicas $$= 6 - 4 = 2$$
> 
> O equivalentemente: Variables libres = $\text{nullity}(A)$ $$\boxed{\text{2 variables libres}}$$
> 
> ---
> 
> **EJEMPLO 3: Transformación entre espacios de polinomios**
> 
> Sea $T: \mathcal{P}_3 \to \mathcal{P}_2$ definida por: $$T(p(x)) = p'(x)$$ (derivada del polinomio)
> 
> Determinar:
> 
> - a) $\dim(\mathcal{P}_3)$ y $\dim(\mathcal{P}_2)$
> - b) $\text{Ker}(T)$ y su dimensión
> - c) $\text{Im}(T)$ y su dimensión
> - d) Verificar el teorema
> 
> **SOLUCIÓN:**
> 
> **a) Dimensiones:**
> 
> $$\dim(\mathcal{P}_3) = 4 \quad \text{(base: } {1, x, x^2, x^3}\text{)}$$ $$\dim(\mathcal{P}_2) = 3 \quad \text{(base: } {1, x, x^2}\text{)}$$
> 
> **b) Núcleo:**
> 
> $p(x) \in \text{Ker}(T) \iff T(p(x)) = p'(x) = 0$
> 
> Un polinomio tiene derivada cero $\iff$ es constante
> 
> $$\boxed{\text{Ker}(T) = {c : c \in \mathbb{R}} = \text{span}{1}}$$ $$\boxed{\text{nullity}(T) = 1}$$
> 
> **c) Imagen:**
> 
> Base de $\mathcal{P}_3$: ${1, x, x^2, x^3}$
> 
> Imágenes: $$T(1) = 0$$ $$T(x) = 1$$ $$T(x^2) = 2x$$ $$T(x^3) = 3x^2$$
> 
> $$\text{Im}(T) = \text{span}{0, 1, 2x, 3x^2} = \text{span}{1, x, x^2} = \mathcal{P}_2$$
> 
> $$\boxed{\text{Im}(T) = \mathcal{P}_2}$$ $$\boxed{\text{rank}(T) = 3}$$
> 
> **d) Verificación:**
> 
> $$\dim(\mathcal{P}_3) = 4 = 1 + 3 = \text{nullity}(T) + \text{rank}(T)$$ ✅
> ---
> 
> **EJEMPLO 4: Restricciones dimensionales**
> 
> ¿Puede existir una transformación lineal $T: \mathbb{R}^4 \to \mathbb{R}^6$ que sea:
> 
> - a) Inyectiva?
> - b) Sobreyectiva?
> - c) Biyectiva?
> - d) Con $\text{nullity}(T) = 1$ y $\text{rank}(T) = 4$?
> 
> **SOLUCIÓN:**
> 
> **a) ¿Inyectiva?**
> 
> Por Corolario 2: Si $\dim(V) < \dim(W)$, puede existir inyectiva.
> 
> $T$ inyectiva requiere $\text{nullity}(T) = 0$
> 
> Por teorema: $\text{rank}(T) = 4 - 0 = 4 \leq 6$ ✓
> 
> $$\boxed{\text{SÍ puede existir inyectiva}}$$
> 
> Ejemplo: $T\begin{pmatrix}\begin{bmatrix} x_1\\x_2\\x_3\\x_4 \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x_1\\x_2\\x_3\\x_4\\0\\0 \end{bmatrix}$
> 
> **b) ¿Sobreyectiva?**
> 
> Por Corolario 3: Si $\dim(V) < \dim(W)$, **NO** puede ser sobreyectiva.
> 
> $T$ sobreyectiva requiere $\text{rank}(T) = 6$
> 
> Pero por teorema: $\text{rank}(T) \leq 4 < 6$
> 
> $$\boxed{\text{NO puede existir sobreyectiva}}$$
> 
> **c) ¿Biyectiva?**
> 
> Biyectiva requiere inyectiva Y sobreyectiva.
> 
> Como no puede ser sobreyectiva: $$\boxed{\text{NO puede existir biyectiva}}$$
> 
> **d) ¿Con nullity = 1 y rank = 4?**
> 
> Verificar teorema: $$\dim(\mathbb{R}^4) = 1 + 4 = 5$$
> 
> Pero $\dim(\mathbb{R}^4) = 4 \neq 5$ ✗
> 
> $$\boxed{\text{NO puede existir (viola el teorema)}}$$

## 🎭 Casos Especiales

> [!tip]- Situaciones Particulares **CASO 1: Transformaciones entre espacios de igual dimensión**
> 
> Si $\dim(V) = \dim(W) = n$ y $T: V \to W$:
> 
> $$\begin{array}{|c|c|c|} \hline \text{Propiedad} & \text{nullity}(T) & \text{rank}(T) \\ \hline \text{Inyectiva} & 0 & n \\ \text{Sobreyectiva} & \text{cualquiera} & n \\ \text{Biyectiva} & 0 & n \\ \text{No inyectiva} & >0 & < n \\ \hline \end{array}$$
> 
> **Conclusión:** En dimensiones iguales, inyectiva ⟺ sobreyectiva ⟺ biyectiva
> 
> ---
> 
> **CASO 2: Operadores (T: V → V)**
> 
> Para $T: V \to V$ (mismo espacio):
> 
> $$n = \text{nullity}(T) + \text{rank}(T)$$
> 
> **Situaciones posibles:**
> 
> |nullity|rank|Tipo|
> |---|---|---|
> |0|n|Isomorfismo|
> |k|n-k|Proyección (si $T^2 = T$)|
> |n|0|Transformación cero|
> 
> ---
> 
> **CASO 3: Matrices cuadradas**
> 
> Para matriz $A$ de $n \times n$:
> 
> $$n = \text{nullity}(A) + \text{rank}(A)$$
> 
> **Equivalencias:**
> 
> - $A$ invertible
> - $\iff \text{nullity}(A) = 0$
> - $\iff \text{rank}(A) = n$
> - $\iff \det(A) \neq 0$
> - $\iff A\vec{x} = \vec{b}$ tiene solución única para todo $\vec{b}$
> 
> ---
> 
> **CASO 4: Matrices rectangulares**
> 
> Para matriz $A$ de $m \times n$:
> 
> **a) Matriz "alta" ($m > n$):**
> 
> - $\text{rank}(A) \leq n < m$
> - No puede ser sobreyectiva
> - Puede ser inyectiva si $\text{rank}(A) = n$
> 
> **b) Matriz "ancha" ($m < n$):**
> 
> - $\text{rank}(A) \leq m < n$
> - No puede ser inyectiva
> - Puede ser sobreyectiva si $\text{rank}(A) = m$
> 
> ---
> 
> **CASO 5: Composición de transformaciones**
> 
> Para $S \circ T$ donde $T: U \to V$ y $S: V \to W$:
> 
> $$\text{rank}(S \circ T) \leq \min{\text{rank}(S), \text{rank}(T)}$$
> 
> **Interpretación:** La composición no puede aumentar el rango.

## 🔗 Relación con Otros Teoremas

> [!note]- Conexiones Fundamentales 
> **1. TEOREMA DE ISOMORFISMO (First Isomorphism Theorem)**
> 
> Para $T: V \to W$ lineal: $$\boxed{V/\text{Ker}(T) \cong \text{Im}(T)}$$
> 
> **Conexión con Rango-Nulidad:**
> 
> Tomando dimensiones: $$\dim(V/\text{Ker}(T)) = \dim(\text{Im}(T))$$
> 
> Como $\dim(V/\text{Ker}(T)) = \dim(V) - \dim(\text{Ker}(T))$: $$\dim(V) - \dim(\text{Ker}(T)) = \dim(\text{Im}(T))$$ $$\dim(V) = \dim(\text{Ker}(T)) + \dim(\text{Im}(T))$$ ✓
> 
> El teorema del rango-nulidad es la **versión dimensional** del teorema de isomorfismo.
> 
> ---
> 
> **2. TEOREMA DE LA BASE**
> 
> Todo espacio vectorial de dimensión finita tiene una base.
> 
> **Uso en la demostración:**
> 
> - Permite construir base de $\text{Ker}(T)$
> - Permite extender a base completa de $V$
> - Fundamental para probar el teorema
> 
> ---
> 
> **3. TEOREMA DEL RANGO DE MATRICES**
> 
> Para matriz $A$: $$\text{rank}(\text{Row}(A)) = \text{rank}(\text{Col}(A))$$
> 
> **Conexión:** $$\text{rank}(A) = \text{rank}(\text{Col}(A)) = \dim(\text{Im}(T_A))$$
> 
> donde $T_A(\vec{x}) = A\vec{x}$.
> 
> ---
> 
> **4. TEOREMA DE INVERTIBILIDAD**
> 
> Para matriz cuadrada $A$ de $n \times n$, son equivalentes:
> 
> - $A$ es invertible
> - $\text{rank}(A) = n$
> - $\text{nullity}(A) = 0$
> 
> **Justificación:** Por rango-nulidad, estas dos últimas son equivalentes cuando la matriz es cuadrada.

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes **1. "nullity + rank = dim(W)"**
> 
> ❌ **ERROR DE FÓRMULA**
> 
> ✅ **CORRECTO:** $$\text{nullity}(T) + \text{rank}(T) = \dim(V) \quad \text{(DOMINIO)}$$
> 
> No confundir con la dimensión del codominio.
> 
> ---
> 
> **2. "Si rank(T) = dim(W), entonces T es inyectiva"**
> 
> ❌ **FALSO**
> 
> $\text{rank}(T) = \dim(W)$ implica que $T$ es **sobreyectiva**, no inyectiva.
> 
> Para inyectividad se requiere: $\text{nullity}(T) = 0$
> 
> ---
> 
> **3. "El teorema solo vale para matrices"**
> 
> ❌ **FALSO**
> 
> El teorema vale para **todas** las transformaciones lineales entre espacios vectoriales de dimensión finita, no solo las representadas por matrices.
> 
> ---
> 
> **4. "Si dim(V) = dim(W), entonces toda T es biyectiva"**
> 
> ❌ **FALSO**
> 
> Dimensiones iguales no garantizan biyectividad.
> 
> Contraejemplo: $T: \mathbb{R}^2 \to \mathbb{R}^2$, $T\begin{pmatrix}\begin{bmatrix} x\y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x\0 \end{bmatrix}$
> 
> - $\dim(\mathbb{R}^2) = \dim(\mathbb{R}^2) = 2$
> - Pero $\text{nullity}(T) = 1 \neq 0$ (no inyectiva)
> - Y $\text{rank}(T) = 1 \neq 2$ (no sobreyectiva)
> 
> ---
> 
> **5. "nullity(T) puede ser negativa"**
> 
> ❌ **IMPOSIBLE**
> 
> La nulidad es una dimensión, por tanto: $$\text{nullity}(T) \geq 0 \quad \text{SIEMPRE}$$
> 
> El mínimo valor es 0 (transformación inyectiva).
> 
> ---
> 
> **6. "rank(T) > dim(V)"**
> 
> ❌ **IMPOSIBLE**
> 
> Por el teorema: $$\text{rank}(T) = \dim(V) - \text{nullity}(T) \leq \dim(V)$$
> 
> El rango nunca puede exceder la dimensión del dominio.
> 
> ---
> 
> **7. "El teorema no requiere dim(V) finita"**
> 
> ⚠️ **CUIDADO**
> 
> El teorema **requiere** que $\dim(V)$ sea finita.
> 
> En espacios infinito-dimensionales, existen versiones más sofisticadas (teoría de operadores).

## 📊 Tabla de Referencia Rápida

> [!note]- Guía de Consulta **FÓRMULA FUNDAMENTAL:**
> 
> $$\boxed{\dim(V) = \text{nullity}(T) + \text{rank}(T)}$$
> 
> **TABLA DE DETERMINACIÓN:**
> 
>| Conocido            | Conocido            | Se calcula                     |
|---------------------|----------------------|--------------------------------|
| $\dim(V)$, nullity  | —                    | $\operatorname{rank} = \dim(V) - \operatorname{nullity}$ |
| $\dim(V)$, rank     | —                    | $\operatorname{nullity} = \dim(V) - \operatorname{rank}$ |
| nullity, rank       | —                    | $\dim(V) = \operatorname{nullity} + \operatorname{rank}$ |
> 
> **CARACTERIZACIONES:**
> 
> |Propiedad|Condición equivalente|
> |---|---|
> |Inyectiva|nullity(T) = 0|
> |Inyectiva|rank(T) = dim(V)|
> |Sobreyectiva|rank(T) = dim(W)|
> |Sobreyectiva|Im(T) = W|
> |Biyectiva (si dim(V)=dim(W))|nullity(T) = 0|
> |Biyectiva (si dim(V)=dim(W))|rank(T) = dim(V) = dim(W)|
> 
> **RESTRICCIONES DIMENSIONALES:**
> 
> |Relación|Conclusión|
> |---|---|
> |dim(V) > dim(W)|No puede ser inyectiva|
> |dim(V) < dim(W)|No puede ser sobreyectiva|
> |dim(V) = dim(W)|Inyectiva ⟺ Sobreyectiva ⟺ Biyectiva|
> 
> **LÍMITES:**
> 
> $$0 \leq \text{nullity}(T) \leq \dim(V)$$ $$0 \leq \text{rank}(T) \leq \min{\dim(V), \dim(W)}$$

## 🔗 Conexiones con Otros Temas

> [!quote]- Enlaces Conceptuales 
> **Fundamentos previos:**
> 
> - [[01 - Vectores en espacios vectoriales]] - Espacios vectoriales
> - [[06 - Independencia lineal]] - Bases y dimensión
> - [[08 - Subespacios vectoriales]] - Teoría de subespacios
> - [[01 – Transformaciones lineales]] - Definición de T
> - [[19 - Núcleo e Imagen]] - Subespacios fundamentales
> 
> **Temas directamente relacionados:**
> 
> - [[05 – Espacio columna]] - Imagen como espacio columna
> - [[17 - Espacio nulo]] - Núcleo como espacio nulo
> - [[21 - Rango de matrices]] - Aplicación a matrices
> - [[22 - Sistemas de ecuaciones lineales]] - Solubilidad
> 
> **Aplicaciones posteriores:**
> 
> - [[24 - Valores propios]] - Ker(T - λI)
> - [[25 - Diagonalización]] - Análisis espectral
> - [[30 - Proyecciones]] - Descomposición
> - [[35 - SVD]] - Descomposición fundamental
> - [[40 - Teorema espectral]] - Operadores autoadjuntos

## 📚 Bibliografía Esencial

> [!tip]- Lecturas Recomendadas **Nivel introductorio:**
> 
> - **Lay, D. C.** (2016). _Álgebra Lineal y sus Aplicaciones_ (5ª ed.). Pearson.
>     - **Cap. 4.2:** Espacios nulos y columna ⭐
>     - Excelente presentación visual
> - **Strang, G.** (2016). _Introduction to Linear Algebra_ (5th ed.). Wellesley-Cambridge.
>     - **Cap. 3.3:** The Four Fundamental Subspaces
>     - Interpretación geométrica clara
> 
> **Nivel intermedio:**
> 
> - **Poole, D.** (2011). _Álgebra Lineal: Una Introducción Moderna_ (3ª ed.). Cengage.
>     - Cap. 6: Espacios vectoriales
>     - Muchos ejemplos aplicados
> - **Anton, H., & Rorres, C.** (2014). _Elementary Linear Algebra_ (11th ed.). Wiley.
>     - Cap. 5: Dimension Theorem
>     - Demostración detallada
> 
> **Nivel avanzado:**
> 
> - **Axler, S.** (2015). _Linear Algebra Done Right_ (3rd ed.). Springer.
>     - **Cap. 3.4:** The Dimension of a Sum ⭐⭐⭐
>     - Tratamiento abstracto y elegante
>     - Enfoque sin determinantes
> - **Hoffman, K., & Kunze, R.** (1971). _Linear Algebra_ (2nd ed.). Prentice Hall.
>     - Cap. 2: Linear Transformations
>     - Tratamiento riguroso completo
> 
> **Contexto avanzado:**
> 
> - **Lang, S.** (2004). _Linear Algebra_ (3rd ed.). Springer.
>     - Teoría abstracta completa
>     - Conexión con teorema de isomorfismo
> - **Roman, S.** (2007). _Advanced Linear Algebra_ (3rd ed.). Springer.
>     - Generalización a módulos
>     - Teoría de categorías

## 🎓 Conceptos Clave - Resumen

> [!important]- Ideas Fundamentales para Recordar
> 
> **TEOREMA CENTRAL:**
> 
> $$\boxed{\dim(V) = \text{nullity}(T) + \text{rank}(T)}$$
> 
> **INTERPRETACIÓN:**
> 
> La dimensión del dominio se conserva, distribuyéndose entre:
> 
> - Lo que se pierde (núcleo)
> - Lo que se alcanza (imagen)
> 
> **CONSECUENCIAS PRINCIPALES:**
> 
> 1. **Determinación:** Conociendo 2 valores, se calcula el tercero
>     
> 2. **Dimensiones iguales:** Si $\dim(V) = \dim(W)$: $$\text{Inyectiva} \iff \text{Sobreyectiva} \iff \text{Biyectiva}$$
>     
> 3. **Imposibilidades:**
>     
>     - $\dim(V) > \dim(W) \implies$ No puede ser inyectiva
>     - $\dim(V) < \dim(W) \implies$ No puede ser sobreyectiva
> 4. **Límites:** $$\text{rank}(T) \leq \min{\dim(V), \dim(W)}$$
>     
> 
> **FÓRMULA CLAVE:**
> 
> $$n = \text{nullity}(A) + \text{rank}(A)$$
> 
> donde $n$ = número de columnas de $A$
> 
> **APLICACIÓN PRÁCTICA:**
> 
> Para sistemas $A\vec{x} = \vec{b}$:
> 
> - Solución única ⟺ nullity = 0 y $\vec{b} \in \text{Im}(A)$
> - Infinitas soluciones ⟺ nullity > 0 y $\vec{b} \in \text{Im}(A)$
> - Sin solución ⟺ $\vec{b} \notin \text{Im}(A)$
> 
> **CONEXIÓN FUNDAMENTAL:**
> 
> El teorema es la versión dimensional del **Primer Teorema de Isomorfismo**: $$V/\text{Ker}(T) \cong \text{Im}(T)$$

---

**Tags:** #algebra-lineal #teorema-dimension #rango-nulidad #rank-nullity #transformaciones-lineales #nucleo #imagen #dimension #espacios-vectoriales #teorema-fundamental #isomorfismo