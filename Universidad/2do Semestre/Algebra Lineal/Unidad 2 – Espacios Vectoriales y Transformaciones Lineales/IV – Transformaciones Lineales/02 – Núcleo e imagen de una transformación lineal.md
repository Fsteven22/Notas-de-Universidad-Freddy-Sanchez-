# 🎯 Núcleo e Imagen de una Transformación Lineal

## 🌟 Concepto Fundamental

> [!info]- Definición Intuitiva **El núcleo y la imagen son dos subespacios fundamentales asociados a toda transformación lineal. El núcleo captura lo que la transformación "destruye" (mapea a cero), mientras que la imagen captura todo lo que la transformación puede "alcanzar". Juntos, estos subespacios revelan la estructura completa de la transformación.**
> 
> **Características clave:**
> 
> - **Núcleo:** Vectores que se colapsan al vector cero
> - **Imagen:** Conjunto de todos los vectores alcanzables
> - **Complementariedad:** Relacionados por el teorema del rango-nulidad
> - **Subespacio:** Ambos son subespacios vectoriales
> - **Información completa:** Determinan completamente el comportamiento de T

### 📖 Contexto Histórico

> [!note]- Desarrollo del Concepto **Orígenes algebraicos (1850-1900):**
> 
> - **Cayley (1858):** Teoría de matrices
>     - Primeras nociones de "soluciones triviales"
>     - Sistemas homogéneos $A\vec{x} = \vec{0}$
> - **Frobenius (1879):** Teorema del rango
>     - Relación entre rango y soluciones
>     - Dimensión de espacios de soluciones
> - **Sylvester (1850s):** Ley de nulidad
>     - Primeras ideas de nullity
>     - Relación rango-nulidad para matrices
> 
> **Formalización geométrica (1900-1930):**
> 
> - **Peano (1888):** Espacios vectoriales abstractos
>     - Marco para definir subespacios
>     - Concepto de subespacio generado
> - **Weyl (1910s):** Álgebra lineal moderna
>     - Kernel como objeto geométrico
>     - Range como espacio imagen
> - **Emmy Noether (1920s):** Álgebra abstracta
>     - Kernel como ideal
>     - Teoremas de isomorfismo
>     - Conexión con teoría de grupos
> 
> **Era funcional (1930-1950):**
> 
> - **von Neumann (1930s):** Operadores en espacios de Hilbert
>     - Kernel cerrado en espacios infinito-dimensionales
>     - Teoría espectral
> - **Banach (1932):** Espacios normados
>     - Operadores acotados
>     - Teorema del rango cerrado
> - **Stone (1930s):** Representación de operadores
>     - Kernel como espacio nulo
>     - Descomposición de espacios
> 
> **Síntesis moderna (1950-presente):**
> 
> - **Bourbaki (1940s-50s):** Formalización completa
>     - Kernel e imagen como functores
>     - Exactitud de sucesiones
> - **Grothendieck (1950s-60s):** Homología
>     - Kernel en contexto homológico
>     - Complejos de cadenas
> - **Aplicaciones computacionales:**
>     - Algoritmos para calcular kernel
>     - Bases ortonormales del núcleo
>     - SVD y pseudoinversas
> - **Machine Learning moderno:**
>     - Kernel methods (SVM)
>     - Espacios de características
>     - Reducción de dimensionalidad

## 📊 Definiciones Formales

> [!important]- Núcleo e Imagen **DEFINICIÓN:**
> 
> Sea $T: V \to W$ una transformación lineal entre espacios vectoriales.
> 
> **1. NÚCLEO (Kernel o Null Space):**
> 
> $$\boxed{\text{Ker}(T) = \text{Nul}(T) = {\vec{v} \in V : T(\vec{v}) = \vec{0}_W}}$$
> 
> El núcleo es el conjunto de todos los vectores del dominio que son mapeados al vector cero del codominio.
> 
> **Notaciones equivalentes:**
> 
> - $\ker(T)$ (minúscula, notación internacional)
> - $\text{Ker}(T)$ (mayúscula)
> - $\text{Nul}(T)$ (null space, espacio nulo)
> - $N(T)$ (notación compacta)
> 
> **2. IMAGEN (Range o Image):**
> 
> $$\boxed{\text{Im}(T) = \text{Range}(T) = {T(\vec{v}) : \vec{v} \in V} = {\vec{w} \in W : \exists \vec{v} \in V, , T(\vec{v}) = \vec{w}}}$$
> 
> La imagen es el conjunto de todos los vectores del codominio que son imagen de al menos un vector del dominio.
> 
> **Notaciones equivalentes:**
> 
> - $\text{Im}(T)$ (imagen)
> - $\text{Range}(T)$ (rango, espacio recorrido)
> - $R(T)$ (notación compacta)
> - $T(V)$ (imagen del espacio completo)
> 
> **INTERPRETACIÓN GEOMÉTRICA:**
> 
> ```
>     DOMINIO V              CODOMINIO W
>     
>     Ker(T) ─────┐
>     (colapsa)   │
>                 ├──→ T ──→ 0
>     resto ──────┘           │
>     (mapea)                 │
>                             ↓
>                          Im(T)
>                       (alcanzable)
> ```
> 
> **Visualización del proceso:**
> 
> $$V = \text{Ker}(T) \oplus U$$
> 
> donde $U$ es un complemento de $\text{Ker}(T)$
> 
> $$T: \begin{cases} \text{Ker}(T) &\to \vec{0} \quad \text{(colapso)} \ U &\xrightarrow{\sim} \text{Im}(T) \quad \text{(isomorfismo)} \end{cases}$$

## 🎯 Propiedades Fundamentales

> [!success]- Teoremas sobre Núcleo e Imagen **TEOREMA 1: Núcleo e Imagen son Subespacios**
> 
> Si $T: V \to W$ es transformación lineal, entonces:
> 
> **a) $\text{Ker}(T)$ es subespacio de $V$**
> 
> **DEMOSTRACIÓN:**
> 
> Verificar tres condiciones de subespacio:
> 
> **(S1) Contiene el vector cero:**
> 
> $$T(\vec{0}_V) = \vec{0}_W$$
> 
> Por tanto $\vec{0}_V \in \text{Ker}(T)$ ✓
> 
> **(S2) Cerrado bajo suma:**
> 
> Sean $\vec{u}, \vec{v} \in \text{Ker}(T)$, es decir: $$T(\vec{u}) = \vec{0}, \quad T(\vec{v}) = \vec{0}$$
> 
> Entonces: $$T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v}) = \vec{0} + \vec{0} = \vec{0}$$
> 
> Por tanto $\vec{u} + \vec{v} \in \text{Ker}(T)$ ✓
> 
> **(S3) Cerrado bajo multiplicación escalar:**
> 
> Sea $\vec{u} \in \text{Ker}(T)$ y $c \in \mathbb{F}$: $$T(c\vec{u}) = cT(\vec{u}) = c\vec{0} = \vec{0}$$
> 
> Por tanto $c\vec{u} \in \text{Ker}(T)$ ✓
> 
> **b) $\text{Im}(T)$ es subespacio de $W$**
> 
> **DEMOSTRACIÓN:**
> 
> **(S1) Contiene el vector cero:**
> 
> $$\vec{0}_W = T(\vec{0}_V) \in \text{Im}(T)$$ ✓
> 
> **(S2) Cerrado bajo suma:**
> 
> Sean $\vec{w}_1, \vec{w}_2 \in \text{Im}(T)$. Entonces existen $\vec{v}_1, \vec{v}_2 \in V$ tales que: $$\vec{w}_1 = T(\vec{v}_1), \quad \vec{w}_2 = T(\vec{v}_2)$$
> 
> Entonces: $$\vec{w}_1 + \vec{w}_2 = T(\vec{v}_1) + T(\vec{v}_2) = T(\vec{v}_1 + \vec{v}_2) \in \text{Im}(T)$$ ✓
> 
> **(S3) Cerrado bajo multiplicación escalar:**
> 
> Sea $\vec{w} \in \text{Im}(T)$ con $\vec{w} = T(\vec{v})$ y $c \in \mathbb{F}$: $$c\vec{w} = cT(\vec{v}) = T(c\vec{v}) \in \text{Im}(T)$$ ✓
> 
> ---
> 
> **TEOREMA 2: Caracterizaciones Alternativas**
> 
> Para $T: V \to W$ lineal:
> 
> **a) Imagen como span de imágenes:**
> 
> Si ${\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_n}$ genera $V$, entonces: $$\text{Im}(T) = \text{span}{T(\vec{v}_1), T(\vec{v}_2), \ldots, T(\vec{v}_n)}$$
> 
> En particular, si ${\vec{v}_1, \ldots, \vec{v}_n}$ es base de $V$: $$\text{Im}(T) = \text{span}{T(\vec{v}_1), \ldots, T(\vec{v}_n)}$$
> 
> **b) Núcleo como solución homogénea:**
> 
> Si $T(\vec{x}) = A\vec{x}$ (representación matricial): $$\text{Ker}(T) = {\vec{x} : A\vec{x} = \vec{0}}$$
> 
> Es el **espacio de soluciones del sistema homogéneo** $A\vec{x} = \vec{0}$.
> 
> **c) Imagen como espacio columna:**
> 
> Si $T(\vec{x}) = A\vec{x}$: $$\text{Im}(T) = \text{Col}(A)$$
> 
> Es el **espacio generado por las columnas de $A$**.
> 
> ---
> 
> **TEOREMA 3: Relación con Inyectividad y Sobreyectividad**
> 
> **a) Inyectividad:**
> 
> $$\boxed{T \text{ es inyectiva} \iff \text{Ker}(T) = {\vec{0}}}$$
> 
> **DEMOSTRACIÓN:**
> 
> $(\longrightarrow)$ Suponer $T$ inyectiva.
> 
> Sea $\vec{v} \in \text{Ker}(T)$, entonces $T(\vec{v}) = \vec{0}$.
> 
> Como $T(\vec{0}) = \vec{0}$ y $T$ es inyectiva: $$T(\vec{v}) = T(\vec{0}) \implies \vec{v} = \vec{0}$$
> 
> Por tanto $\text{Ker}(T) = {\vec{0}}$ ✓
> 
> $(\longleftarrow)$ Suponer $\text{Ker}(T) = {\vec{0}}$.
> 
> Sean $\vec{u}, \vec{v} \in V$ con $T(\vec{u}) = T(\vec{v})$.
> 
> Entonces: $$T(\vec{u}) - T(\vec{v}) = \vec{0}$$ $$T(\vec{u} - \vec{v}) = \vec{0}$$ $$\implies \vec{u} - \vec{v} \in \text{Ker}(T) = {\vec{0}}$$ $$\implies \vec{u} - \vec{v} = \vec{0}$$ $$\implies \vec{u} = \vec{v}$$
> 
> Por tanto $T$ es inyectiva ✓
> 
> **b) Sobreyectividad:**
> 
> $$\boxed{T \text{ es sobreyectiva} \iff \text{Im}(T) = W}$$
> 
> Esto es directo de la definición de sobreyectividad.

## 📏 Dimensiones: Nulidad y Rango

> [!important]- Medidas Fundamentales **DEFINICIONES:**
> 
> Sea $T: V \to W$ transformación lineal donde $V$ tiene dimensión finita.
> 
> **1. NULIDAD (Nullity):**
> 
> $$\boxed{\text{nullity}(T) = \dim(\text{Ker}(T))}$$
> 
> Dimensión del núcleo de $T$.
> 
> **Interpretación:**
> 
> - Mide "cuánta información pierde" $T$
> - Número de "grados de libertad" en las soluciones de $T(\vec{x}) = \vec{0}$
> - Dimensión del subespacio que colapsa a cero
> 
> **2. RANGO (Rank):**
> 
> $$\boxed{\text{rank}(T) = \dim(\text{Im}(T))}$$
> 
> Dimensión de la imagen de $T$.
> 
> **Interpretación:**
> 
> - Mide "cuánto alcanza" $T$
> - Dimensión efectiva de la transformación
> - Número de vectores básicos necesarios para generar la imagen
> 
> **RELACIÓN CON MATRICES:**
> 
> Si $T(\vec{x}) = A\vec{x}$ donde $A$ es $m \times n$:
> 
> $$\text{nullity}(T) = \text{nullity}(A) = n - \text{rank}(A)$$
> 
> $$\text{rank}(T) = \text{rank}(A) = \text{número de columnas pivote}$$
> 
> **PROPIEDADES:**
> 
> **P1) Rango máximo:**
> 
> $$\text{rank}(T) \leq \min{\dim(V), \dim(W)}$$
> 
> **P2) Nulidad máxima:**
> 
> $$\text{nullity}(T) \leq \dim(V)$$
> 
> **P3) Extremos:**
> 
> - $\text{nullity}(T) = 0 \iff T$ inyectiva
> - $\text{rank}(T) = \dim(W) \iff T$ sobreyectiva
> - Ambas condiciones $\iff T$ biyectiva (si $\dim(V) = \dim(W)$)

## 🎓 Teorema del Rango-Nulidad

> [!success]- Teorema Fundamental **TEOREMA DEL RANGO-NULIDAD (Rank-Nullity Theorem):**
> 
> Sea $T: V \to W$ transformación lineal donde $\dim(V) = n$ es finita.
> 
> $$\boxed{\dim(V) = \text{nullity}(T) + \text{rank}(T)}$$
> 
> O equivalentemente:
> 
> $$\boxed{n = \dim(\text{Ker}(T)) + \dim(\text{Im}(T))}$$
> 
> **INTERPRETACIÓN GEOMÉTRICA:**
> 
> ```
>           V (dim = n)
>           /        \
>          /          \
>     Ker(T)          complemento U
>    (dim = k)        (dim = n-k)
>        |                 |
>        |                 | isomorfismo
>        ↓                 ↓
>        0              Im(T)
>                      (dim = n-k)
> ```
> 
> La dimensión del dominio se "conserva": parte se pierde en el núcleo, parte se proyecta en la imagen.
> 
> **DEMOSTRACIÓN:**
> 
> **Paso 1:** Elegir base del núcleo
> 
> Sea $\text{Ker}(T)$ subespacio de $V$ con $\dim(\text{Ker}(T)) = k$.
> 
> Elegir base: $\mathcal{B}_{\text{Ker}} = {\vec{v}_1, \vec{v}_2, \ldots, \vec{v}_k}$
> 
> **Paso 2:** Extender a base de $V$
> 
> Por teorema de extensión de bases: $$\mathcal{B}_V = {\vec{v}_1, \ldots, \vec{v}_k, \vec{u}_1, \ldots, \vec{u}_r}$$
> 
> donde $k + r = n = \dim(V)$.
> 
> **Paso 3:** Probar que ${T(\vec{u}_1), \ldots, T(\vec{u}_r)}$ es base de $\text{Im}(T)$
> 
> **a) Generan $\text{Im}(T)$:**
> 
> Sea $\vec{w} \in \text{Im}(T)$. Entonces $\exists \vec{v} \in V$ con $\vec{w} = T(\vec{v})$.
> 
> Como $\mathcal{B}_V$ es base de $V$: $$\vec{v} = c_1\vec{v}_1 + \cdots + c_k\vec{v}_k + d_1\vec{u}_1 + \cdots + d_r\vec{u}_r$$
> 
> Aplicando $T$: $$\vec{w} = T(\vec{v}) = c_1T(\vec{v}_1) + \cdots + c_kT(\vec{v}_k) + d_1T(\vec{u}_1) + \cdots + d_rT(\vec{u}_r)$$
> 
> Como $\vec{v}_i \in \text{Ker}(T)$: $T(\vec{v}_i) = \vec{0}$
> 
> $$\vec{w} = d_1T(\vec{u}_1) + \cdots + d_rT(\vec{u}_r)$$
> 
> Por tanto ${T(\vec{u}_1), \ldots, T(\vec{u}_r)}$ genera $\text{Im}(T)$ ✓
> 
> **b) Son linealmente independientes:**
> 
> Suponer: $$c_1T(\vec{u}_1) + \cdots + c_rT(\vec{u}_r) = \vec{0}$$
> 
> Por linealidad: $$T(c_1\vec{u}_1 + \cdots + c_r\vec{u}_r) = \vec{0}$$
> 
> Por tanto: $$c_1\vec{u}_1 + \cdots + c_r\vec{u}_r \in \text{Ker}(T)$$
> 
> Como ${\vec{v}_1, \ldots, \vec{v}_k}$ es base de $\text{Ker}(T)$: $$c_1\vec{u}_1 + \cdots + c_r\vec{u}_r = a_1\vec{v}_1 + \cdots + a_k\vec{v}_k$$
> 
> Reordenando: $$c_1\vec{u}_1 + \cdots + c_r\vec{u}_r - a_1\vec{v}_1 - \cdots - a_k\vec{v}_k = \vec{0}$$
> 
> Como $\mathcal{B}_V$ es base (linealmente independiente): $$c_1 = \cdots = c_r = a_1 = \cdots = a_k = 0$$
> 
> En particular $c_1 = \cdots = c_r = 0$, por tanto son L.I. ✓
> 
> **Conclusión:**
> 
> $$\dim(\text{Im}(T)) = r = n - k = \dim(V) - \dim(\text{Ker}(T))$$ ✓
> 
> **CONSECUENCIAS IMPORTANTES:**
> 
> **C1) Inyectividad en espacios de igual dimensión:**
> 
> Si $\dim(V) = \dim(W)$ y $T: V \to W$ lineal: $$T \text{ inyectiva} \iff T \text{ sobreyectiva} \iff T \text{ biyectiva}$$
> 
> **DEMOSTRACIÓN:**
> 
> $T$ inyectiva $\iff \text{nullity}(T) = 0$
> 
> Por teorema: $\text{rank}(T) = \dim(V) - 0 = \dim(V) = \dim(W)$
> 
> $\iff T$ sobreyectiva ✓
> 
> **C2) Imposibilidad de inyección:**
> 
> Si $\dim(V) > \dim(W)$, entonces $T: V \to W$ no puede ser inyectiva.
> 
> **DEMOSTRACIÓN:**
> 
> $$\text{rank}(T) \leq \dim(W) < \dim(V)$$
> 
> Por teorema: $$\text{nullity}(T) = \dim(V) - \text{rank}(T) > 0$$
> 
> Por tanto $\text{Ker}(T) \neq {\vec{0}}$, no es inyectiva ✓
> 
> **C3) Imposibilidad de sobreyección:**
> 
> Si $\dim(V) < \dim(W)$, entonces $T: V \to W$ no puede ser sobreyectiva.
> 
> **DEMOSTRACIÓN:**
> 
> $$\text{rank}(T) \leq \dim(V) < \dim(W)$$
> 
> Por tanto $\text{Im}(T) \neq W$, no es sobreyectiva ✓

## 🔢 Cálculo del Núcleo

> [!note]- Métodos para Encontrar Ker(T) **MÉTODO 1: Definición Directa**
> 
> Para $T: V \to W$, resolver la ecuación: $$T(\vec{v}) = \vec{0}_W$$
> 
> **ALGORITMO:**
> 
> 1. Plantear $T(\vec{v}) = \vec{0}$
> 2. Usar la definición de $T$ para obtener ecuaciones
> 3. Resolver el sistema resultante
> 4. Expresar solución en forma paramétrica
> 5. Identificar base del núcleo
> 
> **EJEMPLO:**
> 
> $T: \mathbb{R}^3 \to \mathbb{R}^2$ definida por: $$T\begin{pmatrix}\begin{bmatrix} x \ y \ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x + 2y - z \\ 2x + 4y - 2z \end{bmatrix}$$
> 
> **Paso 1:** Plantear $T(\vec{v}) = \vec{0}$
> 
> $$\begin{bmatrix} x + 2y - z \\ 2x + 4y - 2z \end{bmatrix} = \begin{bmatrix} 0 \ 0 \end{bmatrix}$$
> 
> **Paso 2:** Sistema de ecuaciones
> 
> $$\begin{cases} x + 2y - z = 0 \\ 2x + 4y - 2z = 0 \end{cases}$$
> 
> **Paso 3:** Resolver (segunda ecuación es 2 × primera)
> 
> $$x + 2y - z = 0 \implies x = -2y + z$$
> 
> **Paso 4:** Forma paramétrica ($y, z$ libres)
> 
> $$\begin{bmatrix} x \ y \ z \end{bmatrix} = \begin{bmatrix} -2y + z \ y \ z \end{bmatrix} = y\begin{bmatrix} -2 \ 1 \ 0 \end{bmatrix} + z\begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}$$
> 
> **Paso 5:** Base del núcleo
> 
> $$\boxed{\text{Ker}(T) = \text{span}\left\\{\begin{bmatrix} -2 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \ 1 \end{bmatrix}\right\\}}$$
> 
> $$\dim(\text{Ker}(T)) = 2$$
> 
> ---
> 
> **MÉTODO 2: Usando Matriz Estándar**
> 
> Si $T: \mathbb{R}^n \to \mathbb{R}^m$ con matriz $A$:
> 
> $$\text{Ker}(T) = \text{Nul}(A) = {\vec{x} : A\vec{x} = \vec{0}}$$
> 
> **ALGORITMO:**
> 
> 6. Encontrar matriz estándar $A$ de $T$
> 7. Formar sistema homogéneo $A\vec{x} = \vec{0}$
> 8. Reducir a forma escalonada reducida
> 9. Identificar variables libres
> 10. Expresar solución en términos de variables libres
> 11. Vectores correspondientes forman base del núcleo
> 
> **EJEMPLO:**
> 
> $$A = \begin{bmatrix} 1 & 2 & -1 & 3 \\ 2 & 4 & -2 & 6 \ -1 & -2 & 1 & -3 \end{bmatrix}$$
> 
> **Paso 1:** Reducir $A$ a forma escalonada
> 
> $$\begin{bmatrix} 1 & 2 & -1 & 3 \\ 2 & 4 & -2 & 6 \\ -1 & -2 & 1 & -3 \end{bmatrix} \xrightarrow{RREF} \begin{bmatrix} 1 & 2 & -1 & 3 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
> 
> **Paso 2:** Identificar variables
> 
> - Variable básica: $x_1$
> - Variables libres: $x_2, x_3, x_4$
> 
> **Paso 3:** Ecuación pivote
> 
> $$x_1 + 2x_2 - x_3 + 3x_4 = 0$$ $$x_1 = -2x_2 + x_3 - 3x_4$$
> 
> **Paso 4:** Solución general
> 
> $$\vec{x} = \begin{bmatrix} -2x_2 + x_3 - 3x_4 \ x_2 \ x_3 \ x_4 \end{bmatrix} = x_2\begin{bmatrix} -2 \ 1 \ 0 \ 0 \end{bmatrix} + x_3\begin{bmatrix} 1 \ 0 \ 1 \ 0 \end{bmatrix} + x_4\begin{bmatrix} -3 \ 0 \ 0 \ 1 \end{bmatrix}$$
> 
> **Paso 5:** Base
> 
> $$\boxed{\text{Base de Ker}(T): \left\\{\begin{bmatrix} -2 \ 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 1 \ 0 \ 1 \ 0 \end{bmatrix}, \begin{bmatrix} -3 \ 0 \ 0 \ 1 \end{bmatrix}\right\\}}$$
> 
> $$\text{nullity}(T) = 3$$
> 
> **VERIFICACIÓN:** $\dim(\mathbb{R}^4) = 4 = 3 + 1 = \text{nullity} + \text{rank}$ ✓

## 🎨 Cálculo de la Imagen

> [!note]- Métodos para Encontrar Im(T) **MÉTODO 1: Usando la Definición**
> 
> $$\text{Im}(T) = {T(\vec{v}) : \vec{v} \in V}$$
> 
> Si ${\vec{v}_1, \ldots, \vec{v}_n}$ es base de $V$: $$\text{Im}(T) = \text{span}{T(\vec{v}_1), \ldots, T(\vec{v}_n)}$$
> 
> **ALGORITMO:**
> 
> 1. Identificar base de $V$
> 2. Calcular imagen de cada vector base
> 3. Formar conjunto ${T(\vec{v}_1), \ldots, T(\vec{v}_n)}$
> 4. Encontrar subconjunto L.I. máximo (base de la imagen
)
> **EJEMPLO:**
> 
> $T: \mathbb{R}^3 \to \mathbb{R}^3$ definida por: $$T\begin{pmatrix}\begin{bmatrix} x \ y \ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x + y \ 2x + 2y \ x + y + z \end{bmatrix}$$
> 
> **Paso 1:** Base estándar de $\mathbb{R}^3$
> 
> $$\vec{e}_1 = \begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \quad \vec{e}_2 = \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}, \quad \vec{e}_3 = \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}$$
> 
> **Paso 2:** Calcular imágenes
> 
> $$T(\vec{e}_1) = \begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix}, \quad T(\vec{e}_2) = \begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix}, \quad T(\vec{e}_3) = \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}$$
> 
> **Paso 3:** Observar que $T(\vec{e}_1) = T(\vec{e}_2)$
> 
> $$\text{Im}(T) = \text{span}\left\\{\begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}\right\\}$$
> 
> **Paso 4:** Verificar L.I. (claramente independientes)
> 
> $$\boxed{\text{Base de Im}(T): \left\\{\begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix}, \begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}\right\\}}$$
> 
> $$\text{rank}(T) = 2$$
> 
> ---
> 
> **MÉTODO 2: Espacio Columna de la Matriz**
> 
> Si $T(\vec{x}) = A\vec{x}$: $$\text{Im}(T) = \text{Col}(A)$$
> 
> **ALGORITMO:**
> 
> 5. Encontrar matriz estándar $A$
> 6. Reducir $A$ a forma escalonada
> 7. Identificar columnas pivote en la forma escalonada
> 8. Tomar las columnas correspondientes de $A$ **original**
> 9. Estas columnas forman base de $\text{Im}(T)$
> 
> **⚠️ CUIDADO:** Usar columnas de la matriz **ORIGINAL**, no de la forma escalonada.
> 
> **EJEMPLO:**
> 
> $$A = \begin{bmatrix} 1 & 2 & 0 & 3 \\ 2 & 4 & 1 & 7 \\ -1 & -2 & 2 & -1 \end{bmatrix}$$
> 
> **Paso 1:** Reducir a forma escalonada
> 
> $$\begin{bmatrix} 1 & 2 & 0 & 3 \\ 2 & 4 & 1 & 7 \\ -1 & -2 & 2 & -1 \end{bmatrix} \xrightarrow{RREF} \begin{bmatrix} 1 & 2 & 0 & 3 \\ 0 & 0 & 1 & 1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
> 
> **Paso 2:** Columnas pivote: 1 y 3
> 
> **Paso 3:** Tomar columnas 1 y 3 de $A$ **original**
> 
> $$\boxed{\text{Base de Im}(T): \left\\{\begin{bmatrix} 1 \ 2 \ -1 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 2 \end{bmatrix}\right\\}}$$
> 
> $$\text{rank}(T) = 2$$
> 
> **VERIFICACIÓN:**
> 
> $$\dim(\mathbb{R}^4) = 4 = 2 + 2 = \text{nullity}(T) + \text{rank}(T)$$
> 
> (Donde nullity = 2 porque hay 2 variables libres)

## 💡 Ejemplos Resueltos Completos

> [!example]- Problemas Detallados **PROBLEMA 1: Análisis Completo de una Transformación**
> 
> Sea $T: \mathbb{R}^4 \to \mathbb{R}^3$ definida por: $$T\begin{pmatrix}\begin{bmatrix} w \ x \ y \ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} w + x + 2y + z \ 2w + 2x + 4y + 2z \ w - x + y + 3z \end{bmatrix}$$
> 
> Encontrar:
> 
> - a) Matriz estándar de $T$
> - b) Base y dimensión de $\text{Ker}(T)$
> - c) Base y dimensión de $\text{Im}(T)$
> - d) ¿Es $T$ inyectiva? ¿Sobreyectiva?
> - e) Verificar teorema del rango-nulidad
> 
> **SOLUCIÓN:**
> 
> **a) Matriz estándar:**
> 
> Calcular imágenes de vectores estándar:
> 
> $$T(\vec{e}_1) = T\begin{pmatrix}\begin{bmatrix} 1\\0\\0\\0 \end{bmatrix}\end{pmatrix} = \begin{bmatrix} 1\\2\\1 \end{bmatrix}$$
> 
> $$T(\vec{e}_2) = \begin{bmatrix} 1\\2\\-1 \end{bmatrix}, \quad T(\vec{e}_3) = \begin{bmatrix} 2\\4\\1 \end{bmatrix}, \quad T(\vec{e}_4) = \begin{bmatrix} 1\\2\\3 \end{bmatrix}$$
> 
> $$A = \begin{bmatrix} 1 & 1 & 2 & 1 \\ 2 & 2 & 4 & 2 \\ 1 & -1 & 1 & 3 \end{bmatrix}$$
> 
> **b) Núcleo:**
> 
> Resolver $A\vec{x} = \vec{0}$:
> 
> $$\begin{bmatrix} 1 & 1 & 2 & 1 \\ 2 & 2 & 4 & 2 \\ 1 & -1 & 1 & 3 \end{bmatrix} \xrightarrow{RREF} \begin{bmatrix} 1 & 0 & \frac{3}{2} & 2 \\ 0 & 1 & \frac{1}{2} & -1 \\ 0 & 0 & 0 & 0 \end{bmatrix}$$
> 
> Variables básicas: $w, x$ Variables libres: $y, z$
> 
> Sistema: $$\begin{cases} w + \frac{3}{2}y + 2z = 0 \ x + \frac{1}{2}y - z = 0 \end{cases}$$
> 
> Solución: $$w = -\frac{3}{2}y - 2z, \quad x = -\frac{1}{2}y + z$$
> 
> $$\vec{x} = \begin{bmatrix} -\frac{3}{2}y - 2z \ -\frac{1}{2}y + z \ y \ z \end{bmatrix} = y\begin{bmatrix} -3/2 \ -1/2 \ 1 \ 0 \end{bmatrix} + z\begin{bmatrix} -2 \ 1 \ 0 \ 1 \end{bmatrix}$$
> 
> Multiplicar primer vector por 2:
> 
> $$\boxed{\text{Base de Ker}(T): \left\\{\begin{bmatrix} -3 \ -1 \ 2 \ 0 \end{bmatrix}, \begin{bmatrix} -2 \ 1 \ 0 \ 1 \end{bmatrix}\right\\}}$$
> 
> $$\boxed{\dim(\text{Ker}(T)) = 2}$$
> 
> **c) Imagen:**
> 
> Columnas pivote en RREF: 1 y 2
> 
> Tomar columnas 1 y 2 de $A$ original:
> 
> $$\boxed{\text{Base de Im}(T): \left\\{\begin{bmatrix} 1 \ 2 \ 1 \end{bmatrix}, \begin{bmatrix} 1 \ 2 \ -1 \end{bmatrix}\right\\}}$$
> 
> $$\boxed{\dim(\text{Im}(T)) = 2}$$
> 
> **d) Inyectividad y sobreyectividad:**
> 
> - **Inyectiva:** $\text{Ker}(T) \neq {\vec{0}}$ ❌ **NO es inyectiva**
> - **Sobreyectiva:** $\dim(\text{Im}(T)) = 2 < 3 = \dim(\mathbb{R}^3)$ ❌ **NO es sobreyectiva**
> 
> **e) Verificación:**
> 
> $$\dim(\mathbb{R}^4) = 4 = 2 + 2 = \text{nullity}(T) + \text{rank}(T)$$ ✅
> 
> ---
> 
> **PROBLEMA 2: Transformación con Polinomios**
> 
> Sea $T: \mathcal{P}_2 \to \mathcal{P}_3$ definida por: $$T(p(x)) = xp(x) + p'(x)$$
> 
> donde $\mathcal{P}_n$ es el espacio de polinomios de grado ≤ $n$.
> 
> Encontrar $\text{Ker}(T)$ e $\text{Im}(T)$.
> 
> **SOLUCIÓN:**
> 
> **Núcleo:**
> 
> Sea $p(x) = ax^2 + bx + c \in \mathcal{P}_2$
> 
> $$T(p(x)) = x(ax^2 + bx + c) + (2ax + b)$$ $$= ax^3 + bx^2 + cx + 2ax + b$$ $$= ax^3 + bx^2 + (c + 2a)x + b$$
> 
> Para que $T(p(x)) = 0$: $$ax^3 + bx^2 + (c + 2a)x + b = 0$$
> 
> Coeficientes deben ser cero: $$\begin{cases} a = 0 \ b = 0 \ c + 2a = 0 \ b = 0 \end{cases}$$
> 
> De primera y tercera: $a = 0, c = 0$ De segunda y cuarta: $b = 0$
> 
> $$\boxed{\text{Ker}(T) = {0}}$$ $$\boxed{\dim(\text{Ker}(T)) = 0}$$
> 
> $T$ es **inyectiva** ✅
> 
> **Imagen:**
> 
> Base estándar de $\mathcal{P}_2$: ${1, x, x^2}$
> 
> $$T(1) = x \cdot 1 + 0 = x$$ $$T(x) = x \cdot x + 1 = x^2 + 1$$ $$T(x^2) = x \cdot x^2 + 2x = x^3 + 2x$$
> 
> $$\text{Im}(T) = \text{span}{x, x^2 + 1, x^3 + 2x}$$
> 
> Verificar independencia lineal:
> 
> $$c_1 x + c_2(x^2 + 1) + c_3(x^3 + 2x) = 0$$ $$c_3 x^3 + c_2 x^2 + (c_1 + 2c_3)x + c_2 = 0$$
> 
> $$\begin{cases} c_3 = 0 \ c_2 = 0 \ c_1 + 2c_3 = 0 \ c_2 = 0 \end{cases}$$
> 
> $$\implies c_1 = c_2 = c_3 = 0$$
> 
> Son L.I. ✅
> 
> $$\boxed{\text{Base de Im}(T): {x, x^2 + 1, x^3 + 2x}}$$ $$\boxed{\dim(\text{Im}(T)) = 3}$$
> 
> **Verificación:** $$\dim(\mathcal{P}_2) = 3 = 0 + 3 = \text{nullity}(T) + \text{rank}(T)$$ ✅
> 
> ---
> 
> **PROBLEMA 3: Proyección Ortogonal**
> 
> Sea $T: \mathbb{R}^3 \to \mathbb{R}^3$ la proyección sobre el plano $xy$: $$T\begin{pmatrix}\begin{bmatrix} x \ y \ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x \ y \ 0 \end{bmatrix}$$
> 
> **a)** Encontrar $\text{Ker}(T)$ e $\text{Im}(T)$ con interpretación geométrica **b)** Verificar que $\mathbb{R}^3 = \text{Ker}(T) \oplus \text{Im}(T)$
> 
> **SOLUCIÓN:**
> 
> **a) Núcleo:**
> 
> $$T\begin{pmatrix}\begin{bmatrix} x \ y \ z \end{bmatrix}\end{pmatrix} = \begin{bmatrix} 0 \ 0 \ 0 \end{bmatrix}$$
> 
> $$\begin{bmatrix} x \ y \ 0 \end{bmatrix} = \begin{bmatrix} 0 \ 0 \ 0 \end{bmatrix}$$
> 
> $$\implies x = 0, y = 0, z \text{ libre}$$
> 
> $$\boxed{\text{Ker}(T) = \text{span}\left\\{\begin{bmatrix} 0 \ 0 \ 1 \end{bmatrix}\right\\} = \text{eje } z}$$
> 
> **Interpretación:** El núcleo es el eje $z$ (todos los vectores perpendiculares al plano $xy$).
> 
> **Imagen:**
> 
> Todo vector en la imagen tiene forma $\begin{bmatrix} x \ y \ 0 \end{bmatrix}$
> 
> $$\boxed{\text{Im}(T) = \text{span}\left\\{\begin{bmatrix} 1 \ 0 \ 0 \end{bmatrix}, \begin{bmatrix} 0 \ 1 \ 0 \end{bmatrix}\right\\} = \text{plano } xy}$$
> 
> **Interpretación:** La imagen es el plano $xy$ completo.
> 
> **b) Suma directa:**
> 
> Todo vector $\vec{v} = \begin{bmatrix} x \ y \ z \end{bmatrix}$ se puede escribir:
> 
> $$\vec{v} = \begin{bmatrix} x \ y \ 0 \end{bmatrix} + \begin{bmatrix} 0 \ 0 \ z \end{bmatrix}$$
> 
> donde:
> 
> - $\begin{bmatrix} x \ y \ 0 \end{bmatrix} \in \text{Im}(T)$ (componente en el plano)
> - $\begin{bmatrix} 0 \ 0 \ z \end{bmatrix} \in \text{Ker}(T)$ (componente perpendicular)
> 
> Esta descomposición es **única** ✅
> 
> $$\boxed{\mathbb{R}^3 = \text{Ker}(T) \oplus \text{Im}(T)}$$
> 
> **Verificación dimensional:** $$3 = 1 + 2 = \dim(\text{Ker}(T)) + \dim(\text{Im}(T))$$ ✅

## 🔄 Relación entre Ker(T) e Im(T)

> [!important]- Descomposición del Espacio **TEOREMA: Descomposición en Suma Directa**
> 
> Sea $T: V \to W$ transformación lineal. Aunque en general $V \neq \text{Ker}(T) \oplus \text{Im}(T)$ (están en espacios diferentes), existe una descomposición fundamental:
> 
> $$V = \text{Ker}(T) \oplus U$$
> 
> donde $U$ es un **complemento** de $\text{Ker}(T)$ y: $$T|_U: U \to \text{Im}(T) \text{ es un isomorfismo}$$
> 
> **INTERPRETACIÓN:**
> 
> ```
>         V
>        / \
>       /   \
>   Ker(T)   U
>      |      |
>      |      | T (isomorfismo)
>      ↓      ↓
>      0   Im(T)
> ```
> 
> - $\text{Ker}(T)$ se "colapsa" a $\vec{0}$
> - $U$ se mapea isomórficamente a $\text{Im}(T)$
> - $\dim(U) = \dim(\text{Im}(T))$ (por el isomorfismo)
> - $\dim(V) = \dim(\text{Ker}(T)) + \dim(U) = \dim(\text{Ker}(T)) + \dim(\text{Im}(T))$
> 
> **CASO ESPECIAL: Proyecciones**
> 
> Para proyecciones $P: V \to V$ (con $P^2 = P$): $$\boxed{V = \text{Ker}(P) \oplus \text{Im}(P)}$$
> 
> **EJEMPLO:**
> 
> Proyección sobre plano $xy$ en $\mathbb{R}^3$: $$\mathbb{R}^3 = \text{eje } z \oplus \text{plano } xy$$ $$\mathbb{R}^3 = \text{Ker}(P) \oplus \text{Im}(P)$$

## ⚙️ Aplicaciones Prácticas

> [!tip]- Usos del Núcleo e Imagen **1. SISTEMAS DE ECUACIONES LINEALES**
> 
> Para el sistema $A\vec{x} = \vec{b}$:
> 
> - **Existencia de soluciones:** $\vec{b} \in \text{Col}(A) = \text{Im}(T)$
>     - Si $\vec{b} \notin \text{Im}(T)$, el sistema no tiene solución
> - **Unicidad de soluciones:** $\text{Ker}(T) = {\vec{0}}$
>     - Si $\text{Ker}(T) \neq {\vec{0}}$, hay infinitas soluciones (si existe alguna)
> 
> **Conclusiones:**
> 
> - Solución única ⟺ $\vec{b} \in \text{Im}(T)$ y $\text{Ker}(T) = {\vec{0}}$
> - Infinitas soluciones ⟺ $\vec{b} \in \text{Im}(T)$ y $\text{Ker}(T) \neq {\vec{0}}$
> - Sin solución ⟺ $\vec{b} \notin \text{Im}(T)$
> 
> ---
> 
> **2. ECUACIONES DIFERENCIALES**
> 
> Para la ecuación diferencial lineal: $$Ly = \frac{d^2y}{dx^2} + p(x)\frac{dy}{dx} + q(x)y = f(x)$$
> 
> Definir $L: C^2 \to C$ (operador diferencial)
> 
> - **Solución homogénea:** $\text{Ker}(L)$ (soluciones de $Ly = 0$)
> - **Solución particular:** Cualquier $y_p$ con $Ly_p = f$
> - **Solución general:** $y = y_h + y_p$ donde $y_h \in \text{Ker}(L)$
> 
> **Teorema fundamental:** $$\dim(\text{Ker}(L)) = \text{orden de la ecuación}$$
> 
> ---
> 
> **3. GRÁFICOS POR COMPUTADORA**
> 
> Transformaciones de proyección 3D → 2D:
> 
> $$P: \mathbb{R}^3 \to \mathbb{R}^2$$
> 
> - $\text{Ker}(P)$ = línea de visión (dirección de proyección)
> - $\text{Im}(P)$ = plano de la pantalla
> - Objetos en $\text{Ker}(P)$ son invisibles (en la línea de visión)
> 
> ---
> 
> **4. PROCESAMIENTO DE SEÑALES**
> 
> Transformada de Fourier discreta: $F: \mathbb{C}^n \to \mathbb{C}^n$
> 
> - $\text{Ker}(F) = {\vec{0}}$ (inyectiva)
> - $\text{Im}(F) = \mathbb{C}^n$ (sobreyectiva)
> - $F$ es isomorfismo (reversible)
> 
> Filtros lineales: $H: \mathbb{R}^n \to \mathbb{R}^n$
> 
> - $\text{Ker}(H)$ = señales completamente filtradas
> - $\text{Im}(H)$ = señales que pueden pasar el filtro
> 
> ---
> 
> **5. MACHINE LEARNING**
> 
> PCA (Principal Component Analysis):
> 
> - Transformación $T: \mathbb{R}^n \to \mathbb{R}^k$ (reducción de dimensión)
> - $\text{Im}(T)$ = subespacio de componentes principales
> - $\text{Ker}(T)$ = información descartada
> - $k = \text{rank}(T)$ = dimensión efectiva de los datos
> 
> ---
> 
> **6. TEORÍA DE CONTROL**
> 
> Sistema lineal: $\dot{\vec{x}} = A\vec{x} + B\vec{u}$
> 
> - **Controlabilidad:** Relacionada con $\text{Im}([B, AB, A^2B, \ldots])$
> - **Observabilidad:** Relacionada con $\text{Ker}([C, CA, CA^2, \ldots]^T)$
> 
> Sistema controlable ⟺ imagen del espacio de controlabilidad = $\mathbb{R}^n$

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes **1. "Ker(T) e Im(T) están en el mismo espacio"**
> 
> ❌ **FALSO**
> 
> - $\text{Ker}(T) \subseteq V$ (dominio)
> - $\text{Im}(T) \subseteq W$ (codominio)
> 
> Pueden estar en espacios completamente diferentes.
> 
> ---
> 
> **2. "Si Ker(T) = {0}, entonces T es biyectiva"**
> 
> ❌ **FALSO** (solo garantiza inyectividad)
> 
> Contraejemplo: $T: \mathbb{R}^2 \to \mathbb{R}^3$, $T\begin{pmatrix}\begin{bmatrix} x \ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x \ y \ 0 \end{bmatrix}$
> 
> - $\text{Ker}(T) = {\vec{0}}$ (inyectiva)
> - $\text{Im}(T) = \text{plano } xy \neq \mathbb{R}^3$ (no sobreyectiva)
> 
> ---
> 
> **3. "rank(T) = dim(W)"**
> 
> ❌ **FALSO EN GENERAL**
> 
> $$\text{rank}(T) = \dim(\text{Im}(T)) \leq \dim(W)$$
> 
> Igualdad solo si $T$ es sobreyectiva.
> 
> ---
> 
> **4. "Para encontrar base de Im(T), usar columnas de matriz escalonada"**
> 
> ❌ **ERROR COMÚN**
> 
> ✅ **CORRECTO:** Usar columnas pivote de la matriz **ORIGINAL** correspondientes a las posiciones de pivotes en la forma escalonada.
> 
> ---
> 
> **5. "Si dim(Ker(T)) = 0, entonces Im(T) = W"**
> 
> ❌ **NO NECESARIAMENTE**
> 
> Solo es cierto si $\dim(V) = \dim(W)$.
> 
> Por teorema: $\text{rank}(T) = \dim(V) - 0 = \dim(V)$
> 
> Pero $\text{rank}(T) = \dim(W)$ requiere $\dim(V) = \dim(W)$.
> 
> ---
> 
> **6. "Ker(T) ∩ Im(T) siempre es {0}"**
> 
> ❌ **FALSO**
> 
> Contraejemplo: $P: \mathbb{R}^2 \to \mathbb{R}^2$ proyección sobre eje $x$
> 
> $$P\begin{pmatrix}\begin{bmatrix} x \ y \end{bmatrix}\end{pmatrix} = \begin{bmatrix} x \ 0 \end{bmatrix}$$
> 
> - $\text{Ker}(P) = \text{eje } y$
> - $\text{Im}(P) = \text{eje } x$
> - $\text{Ker}(P) \cap \text{Im}(P) = {\vec{0}}$ ✅ (en este caso sí)
> 
> Pero para $P^2 = P$ (idempotente), se cumple: $$V = \text{Ker}(P) \oplus \text{Im}(P)$$
> 
> En general, no es necesariamente cierto.
> 
> ---
> 
> **7. "nullity(T) + rank(T) = dim(W)"**
> 
> ❌ **ERROR DE FÓRMULA**
> 
> ✅ **CORRECTO:** $$\text{nullity}(T) + \text{rank}(T) = \dim(V) \text{ (DOMINIO)}$$
> 
> No el codominio $W$.

## 🔗 Conexiones con Otros Temas

> [!quote]- Enlaces Conceptuales **Fundamentos previos:**
> 
> - [[01 - Vectores en espacios vectoriales]] - Estructura de espacios
> - [[05 - Combinaciones lineales]] - Generación de subespacios
> - [[06 - Independencia lineal]] - Bases
> - [[08 - Subespacios vectoriales]] - Teoría de subespacios
> - [[01 – Transformaciones lineales]] - Definición de T
> 
> **Temas directamente relacionados:**
> 
> - [[05 – Espacio columna]] - Im(T) = Col(A)
> - [[17 - Espacio nulo]] - Ker(T) = Nul(A)
> - [[20 - Rango y nulidad]] - Teorema fundamental
> - [[21 - Sistemas de ecuaciones lineales]] - Solubilidad
> 
> **Aplicaciones posteriores:**
> 
> - [[24 - Valores propios]] - Ker(T - λI)
> - [[25 - Diagonalización]] - Descomposición espectral
> - [[30 - Proyecciones]] - Descomposición ortogonal
> - [[35 - SVD]] - Cuatro subespacios fundamentales
> - [[40 - Pseudoinversa]] - Inversa generalizada

## 🎓 Conceptos Clave - Resumen

> [!important]- Ideas Fundamentales para Recordar
> 
> **DEFINICIONES CENTRALES:**
> 
> $$\boxed{\text{Ker}(T) = {\vec{v} \in V : T(\vec{v}) = \vec{0}} \subseteq V}$$
> 
> $$\boxed{\text{Im}(T) = {T(\vec{v}) : \vec{v} \in V} \subseteq W}$$
> 
> **AMBOS SON SUBESPACIOS:**
> 
> - $\text{Ker}(T)$ es subespacio de $V$ (dominio)
> - $\text{Im}(T)$ es subespacio de $W$ (codominio)
> 
> **DIMENSIONES:**
> 
> $$\boxed{\text{nullity}(T) = \dim(\text{Ker}(T))}$$
> 
> $$\boxed{\text{rank}(T) = \dim(\text{Im}(T))}$$
> 
> **TEOREMA DEL RANGO-NULIDAD:**
> 
> $$\boxed{\dim(V) = \text{nullity}(T) + \text{rank}(T)}$$
> 
> **CARACTERIZACIONES:**
> 
> $$T \text{ inyectiva} \iff \text{Ker}(T) = {\vec{0}} \iff \text{nullity}(T) = 0$$
> 
> $$T \text{ sobreyectiva} \iff \text{Im}(T) = W \iff \text{rank}(T) = \dim(W)$$
> 
> **PARA MATRICES:**
> 
> Si $T(\vec{x}) = A\vec{x}$:
> 
> $$\text{Ker}(T) = \text{Nul}(A) \quad \text{(soluciones de } A\vec{x} = \vec{0}\text{)}$$
> 
> $$\text{Im}(T) = \text{Col}(A) \quad \text{(columnas pivote de } A\text{)}$$
> 
> **ALGORITMO DE CÁLCULO:**
> 
> 1. Formar matriz estándar $A$
> 2. Reducir a RREF
> 3. **Núcleo:** Resolver $A\vec{x} = \vec{0}$, expresar en forma paramétrica
> 4. **Imagen:** Identificar columnas pivote, tomar de $A$ **original**
> 5. Verificar: $n = \text{nullity} + \text{rank}$

---

**Tags:** #algebra-lineal #transformaciones-lineales #nucleo #imagen #kernel #range #nulidad #rango #teorema-rango-nulidad #inyectividad #sobreyectividad #subespacios #espacios-vectoriales