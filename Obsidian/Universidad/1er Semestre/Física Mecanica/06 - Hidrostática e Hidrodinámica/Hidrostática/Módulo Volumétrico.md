# Módulo de Compresibilidad (Módulo Volumétrico)

>[!quote] _"Los fluidos, como todo en la naturaleza, responden a las fuerzas aplicadas. El módulo de compresibilidad nos revela cuán resistente es un material a cambiar su volumen bajo presión, una propiedad fundamental que gobierna desde el comportamiento del agua en las profundidades oceánicas hasta el diseño de sistemas hidráulicos industriales."_

> [!info]+ Definición Fundamental 📏 El **módulo de compresibilidad** (K) o **módulo volumétrico** es una propiedad elástica que mide la **resistencia de un material a cambios de volumen** cuando se le aplica una presión uniforme. Se define como la relación entre el esfuerzo volumétrico aplicado y la deformación volumétrica resultante.
> 
> **Fórmula:** K = -ΔP / (ΔV/V₀)
> 
> Donde:
> 
> - K = Módulo de compresibilidad
> - ΔP = Cambio de presión aplicada
> - ΔV = Cambio de volumen
> - V₀ = Volumen original

> [!note]- Fundamento Teórico ⚖️
> 
> ### Base Física
> 
> El módulo de compresibilidad se fundamenta en la **ley de elasticidad volumétrica**:
> 
> - Mayor módulo K → Material más rígido (menos compresible)
> - Menor módulo K → Material más flexible (más compresible)
> - El signo negativo indica que un aumento de presión causa disminución de volumen
> 
> ### Relación con Otras Propiedades
> 
> ```mermaid
> graph TB
>     A[Módulo de Compresibilidad K] --> B[Compresibilidad β = 1/K]
>     A --> C[Velocidad del Sonido<br/>v = √K/ρ]
>     A --> D[Densidad del Material ρ]
>     
>     E[Presión ΔP] --> A
>     A --> F[Deformación Volumétrica<br/>ΔV/V₀]
>     
>     style A fill:#e8f5e8
>     style B fill:#fff3e0
>     style C fill:#e1f5fe
>     style E fill:#fce4ec
>     style F fill:#f3e5f5
> ```

> [!tip]- Tipos de Módulo de Compresibilidad 🔬
> 
> ### Módulo Isotérmico (K_T)
> 
> |Característica|Descripción|
> |---|---|
> |🌡️ **Condición**|Temperatura constante durante la compresión|
> |📐 **Fórmula**|K_T = -V(∂P/∂V)_T|
> |🎯 **Aplicación**|Procesos lentos, equilibrio térmico|
> 
> ### Módulo Adiabático (K_S)
> 
> |Característica|Descripción|
> |---|---|
> |🔥 **Condición**|Sin intercambio de calor (proceso adiabático)|
> |📐 **Fórmula**|K_S = -V(∂P/∂V)_S|
> |⚡ **Aplicación**|Procesos rápidos, ondas sonoras|
> 
> ### Relación entre Módulos
> 
> - **K_S > K_T** (el módulo adiabático siempre es mayor)
> - **K_S/K_T = γ** (relación de calores específicos)

> [!example]- Valores Típicos y Aplicaciones 🏗️
> 
> ### Módulos de Compresibilidad Comunes
> 
> |Material|K (GPa)|Compresibilidad|
> |---|---|---|
> |💎 **Diamante**|442|Extremadamente rígido|
> |🔩 **Acero**|160|Muy rígido|
> |🌊 **Agua**|2.2|Ligeramente compresible|
> |⛽ **Gasolina**|1.3|Más compresible|
> |🌬️ **Aire (1 atm)**|0.0001|Altamente compresible|
> 
> ### Aplicaciones Prácticas
> 
> ```mermaid
> mindmap
>   root((Aplicaciones))
>     Ingeniería Civil
>       Cimentaciones profundas
>       Estructuras submarinas
>       Presas y embalses
>     Industria Petrolífera
>       Exploración marina
>       Cálculo de reservorios
>       Transporte por tuberías
>     Sistemas Hidráulicos
>       Frenos hidráulicos
>       Prensas industriales
>       Elevadores hidráulicos
>     Geofísica
>       Propagación de ondas sísmicas
>       Estudios de la corteza terrestre
>       Exploración sísmica
> ```

> [!abstract]- Cálculos y Ejemplos Prácticos 🧮
> 
> ### Ejemplo 1: Compresión del Agua
> 
> **Problema:** Un volumen de 1 m³ de agua se somete a una presión adicional de 10 MPa. ¿Cuál es la reducción de volumen?
> 
> **Datos:**
> 
> - V₀ = 1 m³
> - ΔP = 10 MPa = 10 × 10⁶ Pa
> - K_agua = 2.2 × 10⁹ Pa
> 
> **Solución:**
> 
> ```
> K = -ΔP / (ΔV/V₀)
> ΔV/V₀ = -ΔP/K = -(10×10⁶)/(2.2×10⁹) = -0.0045
> ΔV = V₀ × (-0.0045) = 1 × (-0.0045) = -0.0045 m³
> ```
> 
> **Resultado:** El agua se comprime 4.5 litros (0.45% del volumen original)
> 
> ### Ejemplo 2: Velocidad del Sonido
> 
> **Cálculo de la velocidad del sonido en el agua:**
> 
> ```
> v = √(K/ρ) = √(2.2×10⁹ Pa / 1000 kg/m³) = √(2.2×10⁶) ≈ 1483 m/s
> ```

> [!warning]- Limitaciones y Consideraciones ⚠️
> 
> ### Limitaciones del Concepto
> 
> - **🔄 Validez en pequeñas deformaciones**: La ley de Hooke solo aplica para deformaciones elásticas
> - **🌡️ Dependencia de temperatura**: K varía significativamente con la temperatura
> - **📊 Dependencia de presión**: Para grandes presiones, K no es constante
> - **⏱️ Efectos temporales**: Diferencia entre comportamiento estático y dinámico
> 
> ### Factores que Afectan el Módulo
> 
> - **🌡️ Temperatura**: Generalmente K disminuye con el aumento de temperatura
> - **📈 Presión**: K puede aumentar con la presión en algunos materiales
> - **🧪 Composición**: Impurezas y aleaciones modifican significativamente K
> - **⚗️ Estado físico**: Sólido, líquido o gas tienen comportamientos muy diferentes

> [!summary]+ Fórmulas y Relaciones Clave 📊
> 
> ### Fórmulas Fundamentales
> 
> ```
> Módulo de Compresibilidad:     K = -ΔP / (ΔV/V₀)
> Compresibilidad:               β = 1/K = -(ΔV/V₀)/ΔP
> Velocidad del Sonido:          v = √(K/ρ)
> Deformación Volumétrica:       εᵥ = ΔV/V₀ = -ΔP/K
> ```
> 
> ### Relaciones Termodinámicas
> 
> ```
> Módulo Isotérmico:    K_T = -V(∂P/∂V)_T
> Módulo Adiabático:    K_S = -V(∂P/∂V)_S
> Relación de módulos:  K_S/K_T = γ = Cp/Cv
> ```

> [!brain]+ Técnica de Memorización: COMPRESS 🧠 **C** - Compresibilidad inversa del módulo **O** - Opuesto al cambio volumétrico **M** - Mayor módulo, menor compresión **P** - Presión causa la deformación **R** - Resistencia al cambio de volumen **E** - Elasticidad volumétrica fundamental **S** - Sonido viaja más rápido en materiales rígidos **S** - Signo negativo por convención física

> [!success]- Puntos Clave para Recordar 🎯
> 
> 1. **📐 Definición inversa**: K = 1/β (compresibilidad)
> 2. **🔍 Signo negativo**: Convención física estándar
> 3. **🌊 Líquidos vs gases**: Los líquidos son mucho menos compresibles
> 4. **⚡ Velocidad del sonido**: Directamente relacionada con √(K/ρ)
> 5. **🌡️ Dependencia térmica**: K varía con temperatura y presión
> 6. **🔧 Aplicaciones prácticas**: Fundamental en hidráulica e ingeniería

---

## Referencias

> [!quote] Notas Relacionadas
> 
> - [[Presión y Densidad]]
> - [[El Principio de Pascal]]
> - [[Elasticidad]]
> - [[Ecuación de Continuidad y Bernoulli]]

## Notas Recomendadas

> [!info] Prerrequisitos
> 
> - [[Presión y Densidad]]
> - [[Elasticidad]]
> - [[Trabajo y Energía]]

> [!tip] Continuación del Tema
> 
> - [[Viscosidad y Número de Reynolds]]
> - [[El Principio de Arquímedes y Flotación 1]]
> - [[Flujo Laminar y Ecuación de Poiseuille]]

---

**Tags:** #física #hidrostática #elasticidad #módulo-compresibilidad #presión #deformación #materiales #ondas-sonoras #ingeniería-hidráulica