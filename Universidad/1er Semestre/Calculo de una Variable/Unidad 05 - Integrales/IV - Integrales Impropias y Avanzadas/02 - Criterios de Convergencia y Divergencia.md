# Criterios de Convergencia y Divergencia

>[!quote] *"En el infinito matemático, no todas las sumas llegan a un destino finito. Los criterios de convergencia son las brújulas que nos guían en el vasto océano de las series infinitas, distinguiendo entre aquellas que convergen hacia un valor específico y las que divergen hacia el infinito o la oscilación eterna."*

> [!info]+ Definiciones Fundamentales 📏
> ### Convergencia de Series
> Una **serie infinita** $\sum_{n=1}^{\infty} a_n$ **converge** si la sucesión de sumas parciales $S_n = \sum_{k=1}^{n} a_k$ tiene un límite finito cuando $n \to \infty$.
> 
> **$$\sum_{n=1}^{\infty} a_n = L \quad \text{si} \quad \lim_{n \to \infty} S_n = L < \infty$$**
> 
> ### Divergencia de Series
> Una serie **diverge** si:
> - La sucesión de sumas parciales tiende a $\pm\infty$
> - Las sumas parciales oscilan sin límite
> - El límite no existe o no es finito
> 
> ### Convergencia de Sucesiones
> Una sucesión $\{a_n\}$ **converge** a $L$ si: $\lim_{n \to \infty} a_n = L$

> [!note]- Clasificación de Comportamientos ⚖️
> ### Tipos de Convergencia y Divergencia
> ```mermaid
> graph TB
>     A[Series Infinitas] --> B[Convergentes]
>     A --> C[Divergentes]
>     
>     B --> D["Convergencia Absoluta<br/>Σ|an| converge"]
>     B --> E["Convergencia Condicional<br/>Σan converge, Σ|an| diverge"]
>     
>     C --> F["Divergencia a +∞<br/>Sn → +∞"]
>     C --> G["Divergencia a -∞<br/>Sn → -∞"]
>     C --> H["Divergencia Oscilatoria<br/>Sn oscila sin límite"]
>     
>     I[Ejemplos] --> J["Geométrica |r|<1: Converge<br/>Armónica: Diverge<br/>Alternada armónica: Conv. Cond."]
>     
>     style A fill:#e8f5e8
>     style B fill:#e1f5fe
>     style C fill:#ffcdd2
>     style D fill:#c8e6c9
>     style E fill:#fff3e0
> ```

> [!tip]- Criterios de Convergencia para Series Positivas 🔬
> ### 1. Criterio de Comparación
> **Sean $\sum a_n$ y $\sum b_n$ series con $a_n, b_n \geq 0$ y $a_n \leq b_n$ para $n$ suficientemente grande:**
> - Si $\sum b_n$ converge → $\sum a_n$ converge
> - Si $\sum a_n$ diverge → $\sum b_n$ diverge
> 
> ### 2. Criterio de Comparación por Límite
> **Si $\lim_{n \to \infty} \frac{a_n}{b_n} = L$ donde $0 < L < \infty$:**
> - $\sum a_n$ y $\sum b_n$ tienen el mismo comportamiento
> 
> ### 3. Criterio de la Razón (D'Alembert)
> **Para $\sum a_n$ con $a_n > 0$:**
> 
> **$$L = \lim_{n \to \infty} \frac{a_{n+1}}{a_n}$$**
> 
> - Si $L < 1$ → Serie converge
> - Si $L > 1$ → Serie diverge  
> - Si $L = 1$ → Criterio no decide
> 
> ### 4. Criterio de la Raíz (Cauchy)
> **$$L = \lim_{n \to \infty} \sqrt[n]{a_n}$$**
> 
> - Si $L < 1$ → Serie converge
> - Si $L > 1$ → Serie diverge
> - Si $L = 1$ → Criterio no decide

> [!example]- Criterios Especiales y Avanzados 🧮
> ### 5. Criterio de Condensación de Cauchy
> **Para sucesiones decrecientes $a_n \geq a_{n+1} \geq 0$:**
> $$\sum_{n=1}^{\infty} a_n \text{ y } \sum_{k=0}^{\infty} 2^k a_{2^k} \text{ tienen el mismo comportamiento}$$
> 
> ### 6. Criterio Integral
> **Si $f(x)$ es positiva, continua y decreciente para $x \geq 1$:**
> $$\sum_{n=1}^{\infty} f(n) \text{ y } \int_1^{\infty} f(x)dx \text{ tienen el mismo comportamiento}$$
> 
> ### 7. Criterio de Dirichlet
> **Para $\sum a_n b_n$ donde:**
> - $\{a_n\}$ es monótona y $\lim_{n \to \infty} a_n = 0$
> - Las sumas parciales de $\sum b_n$ están acotadas
> 
> **→ La serie $\sum a_n b_n$ converge**
> 
> ### 8. Criterio de Abel
> **Para $\sum a_n b_n$ donde:**
> - $\{a_n\}$ es monótona y acotada
> - $\sum b_n$ converge
> 
> **→ La serie $\sum a_n b_n$ converge**

> [!abstract]- Ejemplos Prácticos con Aplicación de Criterios 📚
> ### Ejemplo 1: Serie Geométrica
> **Serie:** $\sum_{n=0}^{\infty} r^n$
> 
> **Criterio de la Razón:**
> ```
> L = lim(n→∞) |r^(n+1)/r^n| = lim(n→∞) |r| = |r|
> 
> Si |r| < 1 → Converge a 1/(1-r)
> Si |r| ≥ 1 → Diverge
> ```
> 
> ### Ejemplo 2: Serie Armónica
> **Serie:** $\sum_{n=1}^{\infty} \frac{1}{n}$
> 
> **Criterio Integral:**
> ```
> ∫₁^∞ (1/x)dx = lim(t→∞) [ln(t) - ln(1)] = ∞
> 
> Por tanto, la serie armónica diverge
> ```
> 
> ### Ejemplo 3: Serie p
> **Serie:** $\sum_{n=1}^{\infty} \frac{1}{n^p}$
> 
> **Criterio Integral:**
> ```
> Para p > 1: ∫₁^∞ x^(-p)dx = 1/(p-1) < ∞ → Converge
> Para p ≤ 1: ∫₁^∞ x^(-p)dx = ∞ → Diverge
> ```
> 
> ### Ejemplo 4: Serie Factorial
> **Serie:** $\sum_{n=1}^{\infty} \frac{1}{n!}$
> 
> **Criterio de la Razón:**
> ```
> L = lim(n→∞) |1/(n+1)! / 1/n!| = lim(n→∞) n!/(n+1)! = lim(n→∞) 1/(n+1) = 0 < 1
> 
> Por tanto, converge (de hecho, converge a e-1)
> ```

> [!success]- Series Alternadas y Convergencia Condicional 🔄
> ### Criterio de Leibniz (Series Alternadas)
> **Para series de la forma $\sum_{n=1}^{\infty} (-1)^{n+1} a_n$ donde $a_n > 0$:**
> 
> **Condiciones para convergencia:**
> 1. $a_n$ es decreciente: $a_{n+1} \leq a_n$
> 2. $\lim_{n \to \infty} a_n = 0$
> 
> **Ejemplo:** Serie armónica alternada $\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}$
> ```
> 3. 1/n es decreciente ✓
> 4. lim(n→∞) 1/n = 0 ✓
> → Converge condicionalmente a ln(2)
> ```
> 
> ### Convergencia Absoluta vs Condicional
> ```mermaid
> graph LR
>     A["Serie Σan"] --> B{"¿Σ|an| converge?"}
>     B -->|Sí| C[Convergencia Absoluta<br/>Σan converge]
>     B -->|No| D{¿Σan converge?}
>     D -->|Sí| E[Convergencia Condicional]
>     D -->|No| F[Divergencia]
>     
>     style C fill:#c8e6c9
>     style E fill:#fff3e0
>     style F fill:#ffcdd2
> ```

> [!warning]- Estrategia para Aplicar Criterios ⚠️
> ### Orden de Aplicación Recomendado
> 
> **1. Verificar condición necesaria:**
> - Si $\lim_{n \to \infty} a_n \neq 0$ → **Diverge** (Test de divergencia)
> 
> **2. Para series con términos positivos:**
> - **Comparación directa** si se conoce una serie similar
> - **Criterio de la razón** si hay factoriales, exponenciales
> - **Criterio de la raíz** si hay potencias de n
> - **Criterio integral** para funciones conocidas
> 
> **3. Para series alternadas:**
> - **Criterio de Leibniz** primero
> - Verificar **convergencia absoluta**
> 
> **4. Para productos de sucesiones:**
> - **Criterios de Dirichlet o Abel**
> 
> ### Errores Comunes
> - **🔄 Confundir convergencia de $a_n$ con convergencia de $\sum a_n$**
> - **📊 Aplicar criterio incorrecto para el tipo de serie**
> - **⚠️ No verificar las condiciones del criterio**
> - **🔍 Concluir cuando el criterio no decide (L=1)**

> [!summary]+ Tabla Resumen de Criterios 📋
> ### Criterios Principales
> | Criterio | Condición | Conclusión | Mejor Uso |
> |----------|-----------|------------|-----------|
> | **Divergencia** | $\lim a_n \neq 0$ | Diverge | Verificación inicial |
> | **Comparación** | $a_n \leq b_n$ | Como $\sum b_n$ | Series similares conocidas |
> | **Razón** | $L = \lim \frac{a_{n+1}}{a_n}$ | L<1 conv, L>1 div | Factoriales, exponenciales |
> | **Raíz** | $L = \lim \sqrt[n]{a_n}$ | L<1 conv, L>1 div | Potencias de n |
> | **Integral** | $\int f(x)dx$ | Como la integral | Funciones conocidas |
> | **Leibniz** | Alternada decreciente → 0 | Converge | Series alternadas |
> 
> ### Series de Referencia Importantes
> ```
> Geométrica:     Σrⁿ converge si |r| < 1
> p-series:       Σ(1/nᵖ) converge si p > 1  
> Armónica:       Σ(1/n) diverge
> Factorial:      Σ(1/n!) converge
> Exponencial:    Σ(1/aⁿ) converge si a > 1
> ```

> [!brain]+ Técnica de Memorización: CONVERDIV 🧠
> **C** - Condición necesaria: lim aₙ = 0
> **O** - Orden de criterios: divergencia → comparación → razón/raíz
> **N** - Números de referencia: p-series, geométrica, armónica
> **V** - Verificar condiciones del criterio antes de aplicar
> **E** - Evaluar límites cuidadosamente
> **R** - Razón y raíz para factoriales/exponenciales
> **D** - Dirichlet y Abel para productos
> **I** - Integral para funciones continuas decrecientes
> **V** - Verificar convergencia absoluta en alternadas

> [!success]- Puntos Clave para Recordar 🎯
> 1. **🔍 Condición necesaria**: Si $\lim a_n \neq 0$, la serie diverge
> 2. **📊 Criterio apropiado**: Elegir según la estructura de la serie
> 3. **⚖️ Convergencia absoluta**: Implica convergencia simple
> 4. **🔄 Series alternadas**: Leibniz para convergencia condicional
> 5. **📈 L = 1**: El criterio no decide, probar otro método
> 6. **🎯 Series de referencia**: Memorizar comportamiento de series básicas

---

## Referencias

> [!quote] Notas Relacionadas
> - [[01 - Límites al Infinito y Sucesiones]]
> - [[03 - Propiedades de la Sumatoria]]
> - [[04 - Teorema Fundamental del Cálculo]]
> - [[01 - Integral de Riemann]]

## Notas Recomendadas

> [!info] Prerrequisitos
> - [[01 - Límites al Infinito y Sucesiones]]
> - [[03 - Propiedades de la Sumatoria]]
> - [[01 - Concepto y Definición Formal del Límite]]

> [!tip] Continuación del Tema
> - [[Series de Potencias]]
> - [[Series de Taylor y Maclaurin]]
> - [[01 - Integración Numérica]]
> - [[Métodos de Aproximación]]

---

**Tags:** #matemáticas #series #convergencia #divergencia #límites #análisis #criterios-convergencia #series-infinitas #sucesiones #cálculo-avanzado

# Criterios de Convergencia y Divergencia - Integrales Impropias

>[!quote] *"Cuando los límites de integración se extienden al infinito o cuando la función presenta discontinuidades, entramos en el reino de las integrales impropias. Aquí, los criterios de convergencia son nuestros guardianes, determinando si estas integrales tienen valores finitos o se pierden en la inmensidad del infinito matemático."*

> [!info]+ Definiciones Fundamentales 📏
> ### Integrales Impropias - Tipos
> Una **integral impropia** es aquella que tiene al menos una de estas características:
> 
> **Tipo I - Límites Infinitos:**
> - $\int_a^{\infty} f(x)dx = \lim_{t \to \infty} \int_a^t f(x)dx$
> - $\int_{-\infty}^b f(x)dx = \lim_{t \to -\infty} \int_t^b f(x)dx$
> - $\int_{-\infty}^{\infty} f(x)dx = \int_{-\infty}^c f(x)dx + \int_c^{\infty} f(x)dx$
> 
> **Tipo II - Discontinuidades:**
> - $\int_a^b f(x)dx$ donde $f$ tiene discontinuidad en $a$, $b$, o punto interior
> - $\int_a^b \frac{1}{(x-c)^p}dx$ donde $a < c < b$

> [!note]- Clasificación de Convergencia y Divergencia 📊
> ### Estados de una Integral Impropia
> ```mermaid
> graph TB
>     A[Integral Impropia] --> B[Convergente]
>     A --> C[Divergente]
>     
>     B --> D["Convergencia Absoluta<br/>∫|f(x)|dx converge"]
>     B --> E["Convergencia Condicional<br/>∫f(x)dx converge, ∫|f(x)|dx diverge"]
>     
>     C --> F["Diverge a +∞<br/>Límite = +∞"]
>     C --> G["Diverge a -∞<br/>Límite = -∞"]
>     C --> H[Oscila<br/>Límite no existe]
>     
>     I[Ejemplos Clásicos] --> J["∫₁^∞ 1/x² dx = 1 (Converge)<br/>∫₁^∞ 1/x dx = ∞ (Diverge)<br/>∫₀¹ 1/√x dx = 2 (Converge)"]
>     
>     style A fill:#e8f5e8
>     style B fill:#c8e6c9
>     style C fill:#ffcdd2
>     style D fill:#e1f5fe
>     style E fill:#fff3e0
> ```

> [!tip]- Criterios de Convergencia para Integrales Tipo I (∞) 🔬
> ### 1. Criterio de Comparación Directa
> **Para funciones $f(x), g(x) \geq 0$ en $[a,\infty)$ con $0 \leq f(x) \leq g(x)$:**
> - Si $\int_a^{\infty} g(x)dx$ converge → $\int_a^{\infty} f(x)dx$ converge
> - Si $\int_a^{\infty} f(x)dx$ diverge → $\int_a^{\infty} g(x)dx$ diverge
> 
> ### 2. Criterio de Comparación por Límite
> **Para $f(x), g(x) > 0$ y $\lim_{x \to \infty} \frac{f(x)}{g(x)} = L$:**
> 
> - Si $0 < L < \infty$ → Ambas integrales tienen el mismo comportamiento
> - Si $L = 0$ y $\int g(x)dx$ converge → $\int f(x)dx$ converge
> - Si $L = \infty$ y $\int g(x)dx$ diverge → $\int f(x)dx$ diverge
> 
> ### 3. Criterio p para el Infinito
> **Integral de referencia:** $\int_1^{\infty} \frac{1}{x^p}dx$
> 
> ```
> Converge si p > 1
> Diverge si p ≤ 1
> ```
> 
> **Resultado:** $\int_1^{\infty} \frac{1}{x^p}dx = \frac{1}{p-1}$ si $p > 1$

> [!example]- Criterios para Integrales Tipo II (Discontinuidades) 🧮
> ### 4. Criterio p en Discontinuidades
> **Para discontinuidad en $x = a$:** $\int_a^b \frac{1}{(x-a)^p}dx$
> 
> ```
> Converge si p < 1
> Diverge si p ≥ 1
> ```
> 
> **Resultado:** $\int_a^{a+h} \frac{1}{(x-a)^p}dx = \frac{h^{1-p}}{1-p}$ si $p < 1$
> 
> ### 5. Comparación en Discontinuidades
> **Cerca de $x = c$ donde $f$ tiene discontinuidad:**
> - Comparar comportamiento de $f(x)$ cerca de $c$
> - Usar funciones de referencia como $\frac{1}{(x-c)^p}$
> 
> ### 6. Criterio de Comparación Asintótica
> **Si cerca de la discontinuidad $x = c$:**
> $$f(x) \sim \frac{A}{(x-c)^p} \quad \text{cuando } x \to c$$
> 
> - Si $p < 1$ → Integral converge
> - Si $p \geq 1$ → Integral diverge

> [!abstract]- Ejemplos Detallados con Aplicación de Criterios 📚
> ### Ejemplo 1: Integral Exponencial
> **Integral:** $\int_0^{\infty} e^{-ax}dx$ donde $a > 0$
> 
> **Solución directa:**
> ```
> ∫₀^∞ e^(-ax)dx = lim(t→∞) [-e^(-ax)/a]₀^t
>                 = lim(t→∞) [(-e^(-at) + 1)/a]
>                 = (0 + 1)/a = 1/a
> 
> Converge para todo a > 0
> ```
> 
> ### Ejemplo 2: Criterio de Comparación
> **Integral:** $\int_1^{\infty} \frac{\sin^2 x}{x^2}dx$
> 
> **Aplicación del criterio:**
> ```
> Como 0 ≤ sin²x ≤ 1, tenemos:
> 0 ≤ sin²x/x² ≤ 1/x²
> 
> Sabemos que ∫₁^∞ 1/x² dx = 1 (converge)
> 
> Por criterio de comparación → ∫₁^∞ sin²x/x² dx converge
> ```
> 
> ### Ejemplo 3: Discontinuidad en el Interior
> **Integral:** $\int_0^2 \frac{1}{\sqrt{x-1}}dx$ (discontinuidad en $x = 1$)
> 
> **División en intervalos:**
> ```
> ∫₀² 1/√(x-1) dx = ∫₀¹ 1/√(x-1) dx + ∫₁² 1/√(x-1) dx
> 
> Primera integral:
> ∫₀¹ 1/√(x-1) dx = lim(t→1⁻) ∫₀^t 1/√(x-1) dx
> 
> Sustitución u = x-1, du = dx:
> = lim(t→1⁻) ∫₋₁^(t-1) u^(-1/2) du = lim(t→1⁻) [2√u]₋₁^(t-1)
> 
> Como p = 1/2 < 1, converge a 2√0 - 2√(-1) (complejo)
> 
> La integral diverge debido a la rama negativa
> ```

> [!success]- Criterios Especiales y Avanzados 🎯
> ### 7. Criterio de Dirichlet para Integrales
> **Para $\int_a^{\infty} f(x)g(x)dx$ donde:**
> - $F(x) = \int_a^x f(t)dt$ está acotada
> - $g(x)$ es monótona y $\lim_{x \to \infty} g(x) = 0$
> 
> **→ La integral converge**
> 
> ### 8. Criterio de Abel para Integrales
> **Para $\int_a^{\infty} f(x)g(x)dx$ donde:**
> - $\int_a^{\infty} f(x)dx$ converge
> - $g(x)$ es monótona y acotada
> 
> **→ La integral converge**
> 
> ### 9. Criterio de Condensación
> **Para funciones positivas y decrecientes:**
> $$\int_1^{\infty} f(x)dx \text{ y } \sum_{n=0}^{\infty} 2^n f(2^n) \text{ tienen el mismo comportamiento}$$
> 
> ### Integrales de Referencia Importantes
> ```mermaid
> graph LR
>     A[Integrales de Referencia] --> B[∫₁^∞ 1/xᵖ dx]
>     A --> C[∫₀¹ 1/xᵖ dx] 
>     A --> D["∫₀^∞ e^(-ax) dx"]
>     A --> E["∫₋∞^∞ e^(-x²) dx"]
>     
>     B --> F[p>1: Converge<br/>p≤1: Diverge]
>     C --> G[p<1: Converge<br/>p≥1: Diverge]
>     D --> H[a>0: Converge a 1/a<br/>a≤0: Diverge]
>     E --> I[Converge a √π]
>     
>     style A fill:#e8f5e8
>     style F fill:#c8e6c9
>     style G fill:#c8e6c9
>     style H fill:#c8e6c9
>     style I fill:#c8e6c9
> ```

> [!warning]- Estrategia y Errores Comunes ⚠️
> ### Estrategia de Análisis
> **1. Identificar el tipo de integral impropia:**
> - ¿Límites infinitos? → Tipo I
> - ¿Discontinuidades? → Tipo II
> - ¿Ambos? → Combinar técnicas
> 
> **2. Localizar puntos problemáticos:**
> - En infinito: comportamiento asintótico
> - En discontinuidades: comportamiento local
> 
> **3. Seleccionar criterio apropiado:**
> - Comparación directa para funciones obvias
> - Comparación por límite para casos complejos
> - Criterios p como referencia estándar
> 
> ### Errores Frecuentes
> - **🔄 Confundir los criterios p**: En ∞ converge si p>1, en discontinuidad si p<1
> - **📊 No identificar todas las discontinuidades**: Verificar en todo el intervalo
> - **⚠️ División incorrecta**: $\int_{-\infty}^{\infty}$ requiere punto de división
> - **🔍 Aplicar criterio sin verificar condiciones**: Verificar positividad, monotonía, etc.
> 
> ### Precauciones Importantes
> - **🧮 Cálculo vs Existencia**: Determinar convergencia antes de calcular
> - **📈 Convergencia condicional**: Puede cambiar con reordenamiento
> - **⚖️ Valor principal de Cauchy**: Para integrales simétricas divergentes

> [!summary]+ Tabla Resumen de Criterios 📋
> ### Criterios Principales
> | Criterio | Tipo | Condiciones | Uso Típico |
> |----------|------|-------------|------------|
> | **Comparación Directa** | I, II | $0 \leq f(x) \leq g(x)$ | Funciones evidentemente menores/mayores |
> | **Comparación por Límite** | I, II | $\lim \frac{f(x)}{g(x)} = L$ | Comportamiento asintótico similar |
> | **Criterio p (infinito)** | I | $\int \frac{1}{x^p}dx$ | Referencia estándar para $x \to \infty$ |
> | **Criterio p (discontinuidad)** | II | $\int \frac{1}{(x-c)^p}dx$ | Referencia para discontinuidades |
> | **Dirichlet** | I | Producto de funciones especiales | Integrales oscilatorias |
> | **Abel** | I | Una converge, otra acotada | Productos con integral conocida |
> 
> ### Integrales de Referencia
> ```
> ∫₁^∞ 1/xᵖ dx:     Converge si p > 1
> ∫₀¹ 1/xᵖ dx:      Converge si p < 1  
> ∫₀^∞ e^(-ax) dx:  Converge si a > 0 → 1/a
> ∫₋∞^∞ e^(-x²) dx: Siempre converge → √π
> ∫₀^∞ sin(x)/x dx: Converge → π/2
> ```

> [!brain]+ Técnica de Memorización: IMPROPIA 🧠
> **I** - Identificar tipo: infinito o discontinuidad
> **M** - Mayorante para comparación directa
> **P** - Criterios p: >1 en infinito, <1 en discontinuidad
> **R** - Referencia: usar integrales conocidas
> **O** - Oscilatoria: Dirichlet y Abel
> **P** - Positivas para comparación simple
> **I** - Intervalos: dividir en partes manejables
> **A** - Asintótico: comportamiento en límites

> [!success]- Puntos Clave para Recordar 🎯
> 1. **🔍 Identificación correcta**: Tipo I (∞) vs Tipo II (discontinuidades)
> 2. **⚖️ Criterios p opuestos**: >1 para ∞, <1 para discontinuidades
> 3. **📊 Comparación efectiva**: Encontrar mayorantes o minorantes adecuadas
> 4. **🎯 Integrales de referencia**: Memorizar comportamiento de casos estándar
> 5. **🧮 División apropiada**: Separar cada problema por punto conflictivo
> 6. **⚠️ Verificar condiciones**: Positividad, monotonía según el criterio

---

## Referencias

> [!quote] Notas Relacionadas
> - [[01 - Integrales Impropias]]
> - [[01 - Integral de Riemann]]
> - [[04 - Teorema Fundamental del Cálculo]]
> - [[02 - Criterios de Convergencia y Divergencia]] (para series)

## Notas Recomendadas

> [!info] Prerrequisitos
> - [[01 - Integral de Riemann]]
> - [[04 - Teorema Fundamental del Cálculo]]
> - [[01 - Límites al Infinito y Sucesiones]]
> - [[01 - Límites al Infinito y Sucesiones]]

> [!tip] Continuación del Tema
> - [[01 - Integración Numérica]]
> - [[01 - Métodos de Integración Definida]]
> - [[Series de Fourier]]
> - [[Transformadas de Laplace]]

---

**Tags:** #matemáticas #integrales-impropias #convergencia #divergencia #criterios-integrales #análisis #cálculo-integral #límites-infinitos #discontinuidades #comparación