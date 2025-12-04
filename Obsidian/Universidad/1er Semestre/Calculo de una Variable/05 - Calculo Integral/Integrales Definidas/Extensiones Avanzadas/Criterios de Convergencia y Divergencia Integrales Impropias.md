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
>     A --> D[∫₀^∞ e^(-ax) dx]
>     A --> E[∫₋∞^∞ e^(-x²) dx]
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
> - [[Integrales Impropias]]
> - [[Integral de Riemann]]
> - [[Teorema fundamental del cálculo]]
> - [[Criterios de Convergencia y Divergencia]] (para series)

## Notas Recomendadas

> [!info] Prerrequisitos
> - [[Integral de Riemann]]
> - [[Teorema fundamental del cálculo]]
> - [[Límites al Infinito]]
> - [[Límites Infinitos]]

> [!tip] Continuación del Tema
> - [[Integración Numérica]]
> - [[Métodos de Integración Definida]]
> - [[Series de Fourier]]
> - [[Transformadas de Laplace]]

---

**Tags:** #matemáticas #integrales-impropias #convergencia #divergencia #criterios-integrales #análisis #cálculo-integral #límites-infinitos #discontinuidades #comparación