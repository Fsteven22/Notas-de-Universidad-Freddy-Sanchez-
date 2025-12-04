# Longitud de Curva

>[!quote] *"La geometría se revela en el movimiento: cada curva traza una historia en el espacio, y su longitud es la medida de ese viaje infinitesimal. Desde el arco más simple hasta las espirales más complejas, la longitud de curva transforma el análisis diferencial en un instrumento de medición geométrica."*

> [!info]+ Definiciones Fundamentales 📏
> ### Longitud de Arco
> La **longitud de arco** de una curva es la distancia medida a lo largo de la curva entre dos puntos específicos.
> 
> **Para una curva parametrizada $\mathbf{r}(t) = (x(t), y(t))$ en el intervalo $[a,b]$:**
> 
> **$$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt = \int_a^b \|\mathbf{r}'(t)\| \, dt$$**
> 
> ### Elemento Diferencial de Arco
> El **elemento diferencial de longitud de arco** es:
> $$ds = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt = \|\mathbf{r}'(t)\| \, dt$$
> 
> ### Curva Rectificable
> Una curva es **rectificable** si su longitud es finita, es decir, si la integral de longitud de arco converge.

> [!note]- Clasificación de Representaciones de Curvas 📐
> ### Tipos de Parametrizaciones
> ```mermaid
> graph TB
>     A[Representaciones de Curvas] --> B[Paramétrica]
>     A --> C[Cartesiana]
>     A --> D[Polar]
>     A --> E[Vectorial 3D]
>     
>     B --> F["r(t) = (x(t), y(t))<br/>L = ∫√(x'² + y'²)dt"]
>     C --> G["y = f(x)<br/>L = ∫√(1 + (f'(x))²)dx"]
>     D --> H["r = f(θ)<br/>L = ∫√(r² + (dr/dθ)²)dθ"]
>     E --> I["r(t) = (x(t), y(t), z(t))<br/>L = ∫√(x'² + y'² + z'²)dt"]
>     
>     J[Ejemplos] --> K[Círculo: 2πR<br/>Semicírculo: πR<br/>Espiral: Integral compleja]
>     
>     style A fill:#e8f5e8
>     style B fill:#e1f5fe
>     style C fill:#fff3e0
>     style D fill:#e8eaf6
>     style E fill:#f3e5f5
> ```

> [!tip]+ Fórmulas para Diferentes Representaciones 🔬
> ### 1. Forma Paramétrica
> **Para $\mathbf{r}(t) = (x(t), y(t))$ con $t \in [a,b]$:**
> 
> $$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt$$
> 
> ### 2. Forma Cartesiana
> **Para $y = f(x)$ con $x \in [a,b]$:**
> 
> $$L = \int_a^b \sqrt{1 + \left(\frac{dy}{dx}\right)^2} \, dx = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx$$
> 
> ### 3. Forma Polar
> **Para $r = f(\theta)$ con $\theta \in [\alpha,\beta]$:**
> 
> $$L = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} \, d\theta = \int_\alpha^\beta \sqrt{[f(\theta)]^2 + [f'(\theta)]^2} \, d\theta$$
> 
> ### 4. Forma Vectorial 3D
> **Para $\mathbf{r}(t) = (x(t), y(t), z(t))$ con $t \in [a,b]$:**
> 
> $$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2} \, dt = \int_a^b \|\mathbf{r}'(t)\| \, dt$$

> [!example]- Ejemplos Clásicos y Cálculos Paso a Paso 📚
> ### Ejemplo 1: Semicírculo
> **Curva:** Semicírculo superior de radio $R$: $x^2 + y^2 = R^2$, $y \geq 0$
> 
> **Parametrización:** $x = R\cos t$, $y = R\sin t$, $t \in [0,\pi]$
> 
> **Cálculo:**
> ```
> dx/dt = -R sin t
> dy/dt = R cos t
> 
> ds = √((-R sin t)² + (R cos t)²) dt
>    = √(R² sin² t + R² cos² t) dt
>    = √(R²(sin² t + cos² t)) dt
>    = R dt
> 
> L = ∫₀^π R dt = R[t]₀^π = πR
> ```
> 
> ### Ejemplo 2: Parábola
> **Curva:** $y = x^2$ desde $x = 0$ hasta $x = 1$
> 
> **Cálculo usando forma cartesiana:**
> ```
> f(x) = x², f'(x) = 2x
> 
> L = ∫₀¹ √(1 + (2x)²) dx = ∫₀¹ √(1 + 4x²) dx
> 
> Usando sustitución trigonométrica: x = (1/2)tan θ
> L = (1/4)[2x√(1+4x²) + ln|2x + √(1+4x²)|]₀¹
> L = (1/4)[2√5 + ln(2 + √5)] ≈ 1.478
> ```
> 
> ### Ejemplo 3: Espiral de Arquímedes
> **Curva polar:** $r = a\theta$ para $\theta \in [0,2\pi]$
> 
> **Cálculo:**
> ```
> r = aθ, dr/dθ = a
> 
> L = ∫₀^{2π} √((aθ)² + a²) dθ = ∫₀^{2π} a√(θ² + 1) dθ
> 
> L = a ∫₀^{2π} √(θ² + 1) dθ
> L = a[(θ/2)√(θ²+1) + (1/2)ln|θ + √(θ²+1)|]₀^{2π}
> L = a[π√(4π²+1) + (1/2)ln(2π + √(4π²+1))]
> ```

> [!abstract]- Métodos de Integración para Longitud de Arco 🧮
> ### Técnicas Comunes
> 
> **1. Sustitución Trigonométrica**
> - Para integrales con $\sqrt{a^2 + x^2}$: $x = a\tan\theta$
> - Para integrales con $\sqrt{a^2 - x^2}$: $x = a\sin\theta$
> - Para integrales con $\sqrt{x^2 - a^2}$: $x = a\sec\theta$
> 
> **2. Integración por Partes**
> - Útil cuando aparecen productos de funciones algebraicas y trascendentes
> 
> **3. Sustituciones Algebraicas**
> - Para simplificar radicales complejos
> 
> **4. Aproximaciones Numéricas**
> - Método del Trapecio
> - Regla de Simpson
> - Cuadratura Gaussiana
> 
> ### Casos Especiales Integrables
> ```mermaid
> graph LR
>     A["Curvas con Longitud Exacta"] --> B["Línea Recta<br/>L = √((x₂-x₁)² + (y₂-y₁)²)"]
>     A --> C["Círculo<br/>L = 2πr"]
>     A --> D["Elipse<br/>L ≈ π(a+b) aproximado"]
>     A --> E["Catenaria<br/>y = a cosh(x/a)<br/>Integrable exacta"]
>     A --> F[Cicloide<br/>L = 8a]
>     
>     style A fill:#e8f5e8
>     style B fill:#c8e6c9
>     style C fill:#c8e6c9
>     style D fill:#fff3e0
>     style E fill:#c8e6c9
>     style F fill:#c8e6c9
> ```

> [!success]- Aplicaciones y Contextos Físicos 🌍
> ### Aplicaciones en Física
> 
> **1. Mecánica**
> - **Longitud de trayectoria**: Distancia recorrida por una partícula
> - **Trabajo en campos de fuerza**: $W = \int_C \mathbf{F} \cdot d\mathbf{r}$
> 
> **2. Óptica**
> - **Principio de Fermat**: La luz sigue el camino de menor tiempo
> - **Diseño de lentes**: Cálculo de superficies curvas
> 
> **3. Ingeniería**
> - **Diseño de carreteras**: Cálculo de longitudes de curvas de transición
> - **Cables y estructuras**: Longitud de cables colgantes (catenarias)
> 
> ### Aplicaciones en Geometría
> 
> **1. Perímetros y Contornos**
> - Cálculo de perímetros de figuras con bordes curvos
> - Análisis de formas irregulares
> 
> **2. Geometría Diferencial**
> - **Curvatura**: $\kappa = \frac{||\mathbf{r}' \times \mathbf{r}''||}{||\mathbf{r}'||^3}$
> - **Parametrización por longitud de arco**
> 
> **3. Cartografía**
> - Medición de distancias reales en mapas
> - Cálculo de longitudes de ríos y costas

> [!warning]- Consideraciones Importantes y Errores Comunes ⚠️
> ### Condiciones para la Existencia
> 
> **1. Diferenciabilidad**
> - Las funciones componentes deben ser diferenciables
> - La derivada debe ser continua (curva suave)
> 
> **2. Convergencia de la Integral**
> - La integral de longitud de arco debe converger
> - Verificar comportamiento en los extremos del intervalo
> 
> ### Errores Comunes
> - **🔄 Confundir parametrizaciones**: No todos los parámetros dan la misma fórmula
> - **📊 Olvidar el valor absoluto**: En algunos casos se necesita $|\mathbf{r}'(t)|$
> - **⚠️ Límites de integración incorrectos**: Verificar el dominio de parametrización
> - **🔍 No simplificar antes de integrar**: Buscar simplificaciones algebraicas
> - **📐 Error en coordenadas polares**: Recordar que es $\sqrt{r^2 + (dr/d\theta)^2}$
> 
> ### Casos Problemáticos
> - **Puntos de cúspide**: Donde la derivada no existe
> - **Curvas con auto-intersecciones**: Pueden requerir partición del dominio
> - **Parametrizaciones no regulares**: Donde $\mathbf{r}'(t) = 0$

> [!brain]+ Técnica de Memorización: CURVARC 🧠
> **C** - Calcular la derivada de cada componente
> **U** - Usar la fórmula apropiada según la representación
> **R** - Raíz cuadrada de la suma de cuadrados de derivadas
> **V** - Verificar los límites de integración
> **A** - Aplicar técnicas de integración apropiadas
> **R** - Revisar la convergencia de la integral
> **C** - Comprobar el resultado con casos conocidos

> [!summary]+ Tabla Resumen de Fórmulas 📋
> ### Fórmulas Principales
> | Representación | Forma | Fórmula de Longitud | Mejor Uso |
> |----------------|-------|-------------------|-----------|
> | **Paramétrica** | $\mathbf{r}(t) = (x(t), y(t))$ | $L = \int_a^b \sqrt{x'^2 + y'^2} \, dt$ | Curvas complejas, movimiento |
> | **Cartesiana** | $y = f(x)$ | $L = \int_a^b \sqrt{1 + (f'(x))^2} \, dx$ | Gráficas de funciones |
> | **Polar** | $r = f(\theta)$ | $L = \int_\alpha^\beta \sqrt{r^2 + (r')^2} \, d\theta$ | Curvas con simetría radial |
> | **3D Paramétrica** | $\mathbf{r}(t) = (x(t), y(t), z(t))$ | $L = \int_a^b \sqrt{x'^2 + y'^2 + z'^2} \, dt$ | Curvas espaciales |
> 
> ### Longitudes Exactas Importantes
> ```
> Segmento:       L = √((x₂-x₁)² + (y₂-y₁)²)
> Círculo:        L = 2πr
> Semicírculo:    L = πr
> Cicloide:       L = 8a (una arcada completa)
> Catenaria:      y = a cosh(x/a), integrable exactamente
> Espiral:        Depende del tipo, generalmente compleja
> ```

> [!success]- Puntos Clave para Recordar 🎯
> 1. **📐 Elemento diferencial**: $ds = ||\mathbf{r}'(t)|| \, dt$ es fundamental
> 2. **🔧 Elección de parametrización**: Puede simplificar enormemente el cálculo
> 3. **📊 Técnicas de integración**: Dominar sustituciones trigonométricas
> 4. **⚖️ Verificación de convergencia**: Especialmente en intervalos infinitos
> 5. **🔄 Casos especiales**: Memorizar longitudes de curvas básicas
> 6. **🎯 Aproximaciones numéricas**: Cuando la integral no es elemental
> 7. **📈 Aplicaciones físicas**: Conectar con problemas reales de trayectorias

---

## Referencias

> [!quote] Notas Relacionadas
> - [[Criterios de Convergencia y Divergencia]]
> - [[Integral de Riemann]]
> - [[Teorema fundamental del cálculo]]
> - [[Parametrización de Curvas]]

## Notas Recomendadas

> [!info] Prerrequisitos
> - [[Derivadas de Funciones Paramétricas]]
> - [[Técnicas de Integración]]
> - [[Coordenadas Polares]]
> - [[Criterios de Convergencia y Divergencia]]

> [!tip] Continuación del Tema
> - [[Área de Superficies de Revolución]]
> - [[Integrales de Línea]]
> - [[Curvatura y Torsión]]
> - [[Geometría Diferencial]]

---

**Tags:** #matemáticas #geometría #longitud-arco #curvas #integración #cálculo-diferencial #parametrizaciones #coordenadas-polares #geometría-diferencial #aplicaciones-física