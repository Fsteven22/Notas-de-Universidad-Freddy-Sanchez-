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
> - [[Límites de Sucesiones]]
> - [[Propiedades de la Sumatoria]]
> - [[Teorema fundamental del cálculo]]
> - [[Integral de Riemann]]

## Notas Recomendadas

> [!info] Prerrequisitos
> - [[Límites de Sucesiones]]
> - [[Propiedades de la Sumatoria]]
> - [[Concepto Intuitivo de Límite]]

> [!tip] Continuación del Tema
> - [[Series de Potencias]]
> - [[Series de Taylor y Maclaurin]]
> - [[Integración Numérica]]
> - [[Métodos de Aproximación]]

---

**Tags:** #matemáticas #series #convergencia #divergencia #límites #análisis #criterios-convergencia #series-infinitas #sucesiones #cálculo-avanzado