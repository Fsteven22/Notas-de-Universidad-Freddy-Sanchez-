# Viscosidad y Número de Reynolds 🌡️

> [!info]+ Conceptos Fundamentales La **viscosidad** es la propiedad de los fluidos que caracteriza su resistencia interna al flujo. Representa la fricción entre las capas del fluido cuando se mueven una respecto a otra.
> 
> 🧪 **Analogía**: Como la "pegajosidad" del fluido - la miel es más viscosa que el agua
> 
> El **Número de Reynolds** es un parámetro adimensional que predice el tipo de flujo (laminar o turbulento) basándose en la relación entre fuerzas inerciales y viscosas.

## Viscosidad Dinámica y Cinemática

> [!tip]+ Definiciones y Relaciones
> 
> ### 🔬 Viscosidad Dinámica (μ)
> 
> **Ley de Newton de la viscosidad:** $$\tau = \mu \frac{du}{dy}$$
> 
> **Donde:**
> 
> - $\tau$: Esfuerzo cortante (Pa)
> - $\mu$: Viscosidad dinámica (Pa·s)
> - $\frac{du}{dy}$: Gradiente de velocidad (s⁻¹)
> 
> ### 💧 Viscosidad Cinemática (ν)
> 
> $$\nu = \frac{\mu}{\rho}$$
> 
> **Donde:**
> 
> - $\nu$: Viscosidad cinemática (m²/s)
> - $\rho$: Densidad del fluido (kg/m³)

> [!note]+ Unidades de Viscosidad
> 
> ### 📏 Sistemas de Unidades
> 
> |Tipo|SI|CGS|Conversión|
> |---|---|---|---|
> |**Dinámica**|Pa·s|Poise (P)|1 Pa·s = 10 P|
> |**Cinemática**|m²/s|Stokes (St)|1 m²/s = 10⁴ St|
> |**Práctica**|cP (centipoise)|cSt (centistokes)|Agua ≈ 1 cP|

## Comportamiento Viscoso

> [!abstract]+ Tipos de Fluidos
> 
> ### 🌊 Clasificación por Viscosidad
> 
> ```mermaid
> graph TD
>     A[Fluidos] --> B[Newtonianos]
>     A --> C[No Newtonianos]
>     
>     B --> D[Viscosidad constante<br/>τ ∝ du/dy]
>     B --> E[Ejemplos:<br/>Agua, Aire, Aceites]
>     
>     C --> F[Pseudoplásticos<br/>Adelgazantes]
>     C --> G[Dilatantes<br/>Espesantes]
>     C --> H[Plásticos<br/>Bingham]
>     
>     F --> I[Pintura, Sangre<br/>μ disminuye con velocidad]
>     G --> J[Almidón, Arena húmeda<br/>μ aumenta con velocidad]
>     H --> K[Pasta dental, Lodo<br/>Requiere τ mínimo]
>     
>     style B fill:#96ceb4,stroke:#198754,color:#fff
>     style C fill:#ff6b6b,stroke:#d63384,color:#fff
>     style D fill:#45b7d1,stroke:#0d6efd,color:#fff
> ```

## Tabla de Viscosidades

> [!example]+ Valores Típicos a 20°C
> 
> ### 🌡️ Viscosidades Comunes
> 
> |Fluido|μ (Pa·s)|μ (cP)|ν (m²/s)|Clasificación|
> |---|---|---|---|---|
> |**Aire**|1.8 × 10⁻⁵|0.018|1.5 × 10⁻⁵|🌬️ Gas ligero|
> |**Agua**|1.0 × 10⁻³|1.0|1.0 × 10⁻⁶|💧 Referencia|
> |**Sangre**|3-4 × 10⁻³|3-4|3 × 10⁻⁶|🩸 Biológico|
> |**Aceite motor**|0.1-0.2|100-200|1 × 10⁻⁴|⚙️ Lubricante|
> |**Miel**|2-10|2000-10000|1.4 × 10⁻³|🍯 Muy viscoso|
> |**Glicerina**|1.5|1500|1.2 × 10⁻³|🧪 Laboratorio|

## Número de Reynolds

> [!warning]+ Parámetro Crítico de Flujo
> 
> ### 🔢 Definición Completa
> 
> $$Re = \frac{\rho v D}{\mu} = \frac{v D}{\nu}$$
> 
> **Donde:**
> 
> - $\rho$: Densidad del fluido (kg/m³)
> - $v$: Velocidad característica (m/s)
> - $D$: Longitud característica (m)
> - $\mu$: Viscosidad dinámica (Pa·s)
> - $\nu$: Viscosidad cinemática (m²/s)

> [!tip]+ Interpretación Física
> 
> ### ⚖️ Balance de Fuerzas
> 
> $$Re = \frac{\text{Fuerzas Inerciales}}{\text{Fuerzas Viscosas}}$$
> 
> |Re|Dominan|Tipo de Flujo|Características|
> |---|---|---|---|
> |**Re ≪ 1**|Viscosas|🐌 Flujo reptante|Muy ordenado|
> |**Re < 2300**|Viscosas|📏 Laminar|Ordenado, predecible|
> |**Re > 4000**|Inerciales|🌪️ Turbulento|Caótico, mezclado|
> |**2300 < Re < 4000**|Equilibrio|⚖️ Transición|Inestable|

## Dependencia con la Temperatura

> [!note]+ Efectos Térmicos
> 
> ### 🌡️ Variación de Viscosidad
> 
> **Para líquidos:** $$\mu = A e^{B/T}$$
> 
> - Viscosidad **disminuye** con temperatura
> - Moléculas más móviles → menor resistencia
> 
> **Para gases:** $$\mu = C T^n$$
> 
> - Viscosidad **aumenta** con temperatura
> - Mayor agitación molecular → más colisiones
> 
> ### 📊 Ejemplo: Agua
> 
> |Temperatura (°C)|μ (cP)|Factor|
> |---|---|---|
> |0|1.79|1.79×|
> |20|1.00|1.00×|
> |40|0.65|0.65×|
> |60|0.47|0.47×|
> |100|0.28|0.28×|

## Geometrías y Reynolds Característicos

> [!abstract]+ Longitudes Características
> 
> ### 📐 Diferentes Configuraciones
> 
> |Geometría|Longitud D|Velocidad v|Re crítico|
> |---|---|---|---|
> |**Tubería circular**|Diámetro|Promedio|2300|
> |**Conducto rectangular**|4A/P|Promedio|2300|
> |**Placa plana**|Distancia desde borde|Local|5×10⁵|
> |**Esfera**|Diámetro|Relativa al fluido|1|
> |**Cilindro**|Diámetro|Perpendicular|40|

## Aplicaciones Prácticas

> [!example]+ Cálculo de Reynolds
> 
> ### 🚰 Problema: Tubería de Agua
> 
> **Datos:**
> 
> - Diámetro: D = 5 cm = 0.05 m
> - Velocidad: v = 2 m/s
> - Agua a 20°C: ν = 1.0 × 10⁻⁶ m²/s
> 
> **Cálculo:** $$Re = \frac{vD}{\nu} = \frac{2 \times 0.05}{1.0 \times 10^{-6}} = 100,000$$
> 
> **Resultado**: Re > 4000 → **Flujo Turbulento**

> [!example]+ Problema: Flujo de Miel
> 
> ### 🍯 Cálculo con Fluido Viscoso
> 
> **Datos:**
> 
> - Diámetro: D = 1 cm = 0.01 m
> - Velocidad: v = 0.1 m/s
> - Miel: ν = 1.4 × 10⁻³ m²/s
> 
> **Cálculo:** $$Re = \frac{vD}{\nu} = \frac{0.1 \times 0.01}{1.4 \times 10^{-3}} = 0.7$$
> 
> **Resultado**: Re ≪ 1 → **Flujo Reptante**

## Medición de Viscosidad

> [!tip]+ Instrumentos de Medición
> 
> ### 🔧 Viscosímetros Principales
> 
> |Tipo|Principio|Rango|Aplicación|
> |---|---|---|---|
> |**Capillar**|Tiempo de flujo|Bajo-Medio|Líquidos transparentes|
> |**Rotacional**|Torque requerido|Amplio|Todo tipo de fluidos|
> |**Caída de esfera**|Velocidad terminal|Bajo-Alto|Fluidos transparentes|
> |**Copa de Ford**|Tiempo de vaciado|Industrial|Control calidad|

## Régimen de Flujo y Aplicaciones

> [!success]+ Implicaciones Prácticas
> 
> ### 🌊 Consecuencias del Tipo de Flujo
> 
> **Flujo Laminar (Re < 2300):**
> 
> - ✅ Pérdidas de presión predecibles
> - ✅ Transferencia de calor controlada
> - ✅ Mezclado mínimo
> - 🎯 **Aplicaciones**: Microfluidica, inyecciones médicas
> 
> **Flujo Turbulento (Re > 4000):**
> 
> - ⚡ Mayor transferencia de calor y masa
> - 🌪️ Mezclado eficiente
> - 📈 Mayores pérdidas de presión
> - 🎯 **Aplicaciones**: Sistemas HVAC, procesos químicos

## Técnicas de Estudio

> [!tip]+ Mnemotecnia VISCOSO
> 
> ### 🧠 Regla de Memorización
> 
> - **V**elocidad en numerador del Reynolds
> - **I**nerciales vs viscosas (fuerzas)
> - **S**istema depende de temperatura
> - **C**rítico en 2300 para tuberías
> - **O**rdenado si laminar, caótico si turbulento
> - **S**uperficie determina esfuerzo cortante
> - **O**bstáculos afectan la longitud característica

> [!study]+ Método de Análisis: EVALUAR
> 
> ### 📋 Protocolo de Cálculo
> 
> 1. **E**stablecer geometría (D, forma)
> 2. **V**elocidad característica (promedio, local)
> 3. **A**notar propiedades del fluido (ρ, μ, ν)
> 4. **L**ongitud característica correcta
> 5. **U**nidades coherentes en cálculo
> 6. **A**plicar criterio de Reynolds
> 7. **R**esultado: tipo de flujo determinado

## Factores que Afectan el Flujo

> [!warning]+ Variables de Influencia
> 
> ### 🎛️ Parámetros de Control
> 
> **Para aumentar Reynolds (favorecer turbulencia):**
> 
> - 🔼 Aumentar velocidad
> - 🔼 Aumentar dimensión característica
> - 🔼 Aumentar densidad del fluido
> - 🔽 Disminuir viscosidad
> 
> **Para disminuir Reynolds (favorecer flujo laminar):**
> 
> - 🔽 Reducir velocidad
> - 🔽 Usar conductos más pequeños
> - 🔼 Usar fluidos más viscosos
> - 🌡️ Enfriar líquidos / Calentar gases

## Referencias y Conexiones

> [!quote]+ Enlaces a Otras Notas
> 
> - [[Ecuación de Continuidad y Bernoulli]]
> - [[Flujo Laminar y Ecuación de Poiseuille]]
> - [[Pérdidas de Carga en Tuberías]]
> - [[Transferencia de Calor en Fluidos]]
> - [[Capa Límite]]

## Notas Complementarias Recomendadas

> [!info]+ Prerrequisitos
> 
> - [[Propiedades de los Fluidos]]
> - [[Esfuerzos Cortantes]]
> - [[Gradientes de Velocidad]]
> - [[Conceptos de Densidad]]

> [!success]+ Para Profundizar
> 
> - [[Flujo Laminar y Ecuación de Poiseuille]]
> - [[Turbulencia y Modelos de Flujo]]
> - [[Reología - Fluidos No Newtonianos]]
> - [[Lubricación y Tribología]]
> - [[Microfluidica]]

---

**Tags**: #fisica #mecanica #hidrodinamica #viscosidad #reynolds #flujo #laminar #turbulento #propiedades #fluidos