---
dg-publish: true
---

# Flujo Laminar y Ecuación de Poiseuille 🌊

> [!info]+ Fundamentos del Flujo Laminar El **flujo laminar** es un régimen de movimiento de fluidos caracterizado por capas que se deslizan suavemente unas sobre otras sin mezclarse. Es predecible, ordenado y ocurre cuando las fuerzas viscosas dominan sobre las inerciales (Re < 2300).
> 
> 💧 **Visualización**: Como capas de líquido deslizándose en paralelo, similar a cartas deslizándose en una baraja
> 
> La **Ecuación de Poiseuille** describe matemáticamente el flujo laminar en conductos circulares, siendo fundamental en ingeniería y medicina.

## Características del Flujo Laminar

> [!tip]+ Propiedades Fundamentales
> 
> ### 🔍 Perfil de Velocidades
> 
> En un conducto circular, la velocidad varía parabólicamente: $$u(r) = u_{max}\left(1 - \frac{r^2}{R^2}\right)$$
> 
> **Donde:**
> 
> - $u(r)$: Velocidad a distancia $r$ del centro (m/s)
> - $u_{max}$: Velocidad máxima en el centro (m/s)
> - $R$: Radio del conducto (m)
> - $r$: Distancia radial desde el centro (m)
>
> [!abstract]+ Perfil Parabólico Visual
> 
> ### 📊 Distribución de Velocidades
> 
> ```mermaid
> graph TD
>     A[Pared del tubo<br/>v = 0] --> B[Perfil Parabólico]
>     B --> C[Centro del tubo<br/>v = vmáx]
>     B --> D[Velocidad promedio<br/>v̄ = vmáx/2]
>     E[Características] --> F[Sin mezclado<br/>entre capas]
>     E --> G[Pérdidas mínimas<br/>por fricción]
>     E --> H[Flujo predecible<br/>y estable]
>     style A fill:#ff6b6b,stroke:#d63384,color:#fff
>     style C fill:#45b7d1,stroke:#0d6efd,color:#fff
>     style D fill:#96ceb4,stroke:#198754,color:#fff
> ```

## Ecuación de Poiseuille

> [!note]+ Derivación y Forma Final
> 
> ### 🧮 Ecuación Completa para Tubería Circular
> 
> $$Q = \frac{\pi R^4 \Delta P}{8 \mu L}$$
> 
> **Forma alternativa con diámetro:** $$Q = \frac{\pi D^4 \Delta P}{128 \mu L}$$
> 
> **Variables:**
> 
> - $Q$: Caudal volumétrico (m³/s)
> - $R$: Radio del tubo (m)
> - $D$: Diámetro del tubo (m)
> - $\Delta P$: Diferencia de presión (Pa)
> - $\mu$: Viscosidad dinámica (Pa·s)
> - $L$: Longitud del tubo (m)
>
> [!warning]+ Condiciones de Validez
> 
> - ⚠️ **Flujo completamente desarrollado**: Entrada estabilizada
> - ⚠️ **Régimen laminar**: Re < 2300
> - ⚠️ **Fluido newtoniano**: Viscosidad constante
> - ⚠️ **Conducto circular**: Sección transversal uniforme
> - ⚠️ **Paredes rígidas**: Sin deformación
> - ⚠️ **Estado estacionario**: Sin variaciones temporales

## Relaciones Derivadas

> [!example]+ Ecuaciones Útiles Relacionadas
> 
> ### ⚖️ Velocidades Características
> 
> **Velocidad promedio:** $$\bar{v} = \frac{Q}{A} = \frac{\Delta P \cdot D^2}{32 \mu L}$$
> 
> **Velocidad máxima:** $$v_{max} = 2\bar{v} = \frac{\Delta P \cdot R^2}{4 \mu L}$$
> 
> **Gradiente de presión:** $$\frac{dP}{dx} = -\frac{32 \mu \bar{v}}{D^2}$$
>
> [!tip]+ Factor de Fricción para Flujo Laminar
> 
> ### 🔧 Coeficiente de Pérdidas
> 
> $$f = \frac{64}{Re}$$
> 
> **Pérdida de presión:** $$\Delta P = f \cdot \frac{L}{D} \cdot \frac{\rho v^2}{2}$$
> 
> Sustituyendo el factor de fricción: $$\Delta P = \frac{64}{Re} \cdot \frac{L}{D} \cdot \frac{\rho v^2}{2} = \frac{32 \mu v L}{D^2}$$

## Comparación: Laminar vs Turbulento

> [!abstract]+ Diferencias Fundamentales
> 
> ### 🌪️ Contraste de Regímenes
> 
> |Característica|Flujo Laminar|Flujo Turbulento|
> |---|---|---|
> |**Reynolds**|Re < 2300|Re > 4000|
> |**Perfil velocidad**|🍃 Parabólico suave|⚡ Plano con fluctuaciones|
> |**Mezclado**|🚫 Sin mezclado radial|✅ Mezclado intenso|
> |**Factor fricción**|$f = 64/Re$|$f = f(Re, rugosidad)$|
> |**Pérdidas presión**|📉 Proporcional a $v$|📈 Proporcional a $v^2$|
> |**Estabilidad**|🎯 Muy estable|🌊 Fluctuante|
> |**Aplicaciones**|Microfluidica, medicina|HVAC, grandes tuberías|

## Problemas Resueltos

> [!example]+ Problema 1: Caudal en Capilar
> 
> ### 💉 Aplicación Médica
> 
> **Datos:**
> 
> - Diámetro: D = 0.5 mm = 0.0005 m
> - Longitud: L = 10 mm = 0.01 m
> - Diferencia de presión: ΔP = 1000 Pa
> - Fluido: Agua (μ = 1.0 × 10⁻³ Pa·s)
> 
> **Verificación de régimen laminar:** Primero calculamos velocidad promedio y Reynolds: $$\bar{v} = \frac{\Delta P \cdot D^2}{32 \mu L} = \frac{1000 \times (0.0005)^2}{32 \times 1.0 \times 10^{-3} \times 0.01} = 0.78 \text{ m/s}$$
> 
> $$Re = \frac{\rho \bar{v} D}{\mu} = \frac{1000 \times 0.78 \times 0.0005}{1.0 \times 10^{-3}} = 390 < 2300$$ ✅
> 
> **Caudal usando Poiseuille:** $$Q = \frac{\pi D^4 \Delta P}{128 \mu L} = \frac{\pi \times (0.0005)^4 \times 1000}{128 \times 1.0 \times 10^{-3} \times 0.01}$$ $$Q = 1.53 \times 10^{-7} \text{ m³/s} = 0.153 \text{ ml/s}$$
>
> [!example]+ Problema 2: Pérdida de Presión
> 
> ### 🏭 Aplicación Industrial
> 
> **Datos:**
> 
> - Tubería: D = 5 cm = 0.05 m, L = 100 m
> - Fluido: Aceite (ρ = 900 kg/m³, μ = 0.1 Pa·s)
> - Caudal: Q = 0.001 m³/s
> 
> **Velocidad promedio:** $$\bar{v} = \frac{Q}{A} = \frac{0.001}{\pi (0.025)^2} = 0.51 \text{ m/s}$$
> 
> **Verificación laminar:** $$Re = \frac{900 \times 0.51 \times 0.05}{0.1} = 229.5 < 2300$$ ✅
> 
> **Pérdida de presión:** $$\Delta P = \frac{32 \mu \bar{v} L}{D^2} = \frac{32 \times 0.1 \times 0.51 \times 100}{(0.05)^2} = 65,280 \text{ Pa} = 65.3 \text{ kPa}$$

## Aplicaciones Específicas

> [!success]+ Casos Prácticos Importantes
> 
> ### 🩺 Aplicaciones Médicas
> 
> **Sistema Circulatorio:**
> 
> - **Capilares**: D ≈ 5-10 μm, flujo laminar ideal
> - **Viscosidad sanguínea**: 3-4 cP (3-4 veces la del agua)
> - **Efecto Fahraeus-Lindqvist**: Viscosidad efectiva menor en capilares
> 
> **Jeringas y catéteres:** $$\text{Fuerza requerida} = \frac{128 \mu L Q}{\pi D^4}$$
> 
> ### 🔬 Microfluidica
> 
> |Aplicación|Dimensión típica|Reynolds|Ventaja|
> |---|---|---|---|
> |**Lab-on-chip**|10-100 μm|Re < 1|Control preciso|
> |**Dosificación**|100-1000 μm|Re < 100|Mezclado controlado|
> |**Separación**|50-500 μm|Re < 10|Patrones estables|

## Limitaciones y Modificaciones

> [!warning]+ Desviaciones del Modelo Ideal
> 
> ### 🔧 Correcciones Necesarias
> 
> **Efectos de entrada:**
> 
> - Longitud de desarrollo: $L_e = 0.06 \cdot Re \cdot D$
> - Factor de corrección para tubos cortos
> 
> **Fluidos no-newtonianos:** $$Q = \frac{\pi R^4 \Delta P}{8 \mu_{eff} L} \cdot f(n)$$ Donde $f(n)$ depende del índice de comportamiento de flujo
> 
> **Rugosidad de superficie:**
> 
> - Poiseuille asume paredes lisas
> - Rugosidad excesiva puede inducir turbulencia prematura

## Derivación Teórica Simplificada

> [!note]+ Desarrollo Matemático
> 
> ### 📐 Balance de Fuerzas
> 
> **Para una capa cilíndrica de fluido:** $$\text{Fuerza de presión} = \text{Fuerza viscosa}$$ $$\Delta P \cdot \pi r^2 = \tau \cdot 2\pi r L$$
> 
> **Con la ley de Newton de viscosidad:** $$\tau = \mu \frac{du}{dr}$$
> 
> **Integración:** $$\frac{du}{dr} = \frac{\Delta P \cdot r}{2\mu L}$$
> 
> **Perfil de velocidad final:** $$u(r) = \frac{\Delta P}{4\mu L}(R^2 - r^2)$$

## Técnicas de Estudio

> [!tip]+ Mnemotecnia POISEUILLE
> 
> ### 🧠 Regla de Memorización
> 
> - **P**erfil parabólico de velocidades
> - **O**rden laminar sin mezclado
> - **I**nversa dependencia con viscosidad
> - **S**ección elevada a la cuarta potencia
> - **E**cuación válida solo si Re < 2300
> - **U**niforme la presión en sección transversal
> - **I**deal para fluidos newtonianos
> - **L**ongitud en el denominador (mayor L → menor Q)
> - **L**ineal la relación presión-caudal
> - **E**stabilizado el flujo completamente
>
> [!study]+ Método ANALIZAR para Problemas
> 
> ### 📋 Protocolo Sistemático
> 
> 1. **A**notar todas las variables dadas
> 2. **N**aturaleza del fluido (newtoniano, propiedades)
> 3. **A**plicabilidad: verificar Re < 2300
> 4. **L**ongitud y geometría del conducto
> 5. **I**dentificar qué calcular (Q, ΔP, v, etc.)
> 6. **Z**ona de aplicación de Poiseuille
> 7. **A**plicar ecuación apropiada
> 8. **R**evisar unidades y coherencia física

## Instrumentación y Medición

> [!abstract]+ Dispositivos Basados en Poiseuille
> 
> ### 🔬 Aplicaciones en Medición
> 
> |Instrumento|Principio|Medición|Ecuación base|
> |---|---|---|---|
> |**Viscosímetro capilar**|Tiempo flujo|Viscosidad|$\mu = \frac{\pi D^4 \Delta P t}{128 V L}$|
> |**Caudalímetro diferencial**|Caída presión|Caudal|$Q = K\sqrt{\Delta P}$|
> |**Reómetro capilar**|Presión-caudal|Reología|Curva $\tau$ vs $\dot{\gamma}$|

## Análisis Dimensional

> [!tip]+ Verificación de Coherencia
> 
> ### 🔢 Análisis de Unidades
> 
> **Ecuación de Poiseuille:** $$[Q] = \frac{[L^4][M L^{-1} T^{-2}]}{[M L^{-1} T^{-1}][L]} = \frac{L^4 \cdot M L^{-1} T^{-2}}{M L^{-1} T^{-1} \cdot L} = L^3 T^{-1}$$ ✅
> 
> **Verificación correcta**: m³/s para caudal volumétrico

## Referencias y Conexiones

> [!quote]+ Enlaces a Otras Notas
> 
> - [[Viscosidad y Número de Reynolds]]
> - [[Ecuación de Continuidad y Bernoulli]]
> - [[Pérdidas de Carga en Tuberías]]
> - [[Flujo en Conductos No Circulares]]
> - [[Reología y Fluidos No Newtonianos]]

## Notas Complementarias Recomendadas

> [!info]+ Prerrequisitos
> 
> - [[Viscosidad y Número de Reynolds]]
> - [[Esfuerzos Cortantes en Fluidos]]
> - [[Gradientes de Velocidad]]
> - [[Balance de Fuerzas]]
>
> [!success]+ Para Profundizar
> 
> - [[Flujo Turbulento en Tuberías]]
> - [[Pérdidas Singulares y Locales]]
> - [[Redes de Tuberías]]
> - [[Bombas y Sistemas de Bombeo]]
> - [[Transferencia de Calor en Flujo Laminar]]
> - [[Microfluidica Avanzada]]

---

**Tags**: #fisica #mecanica #hidrodinamica #flujo #laminar #poiseuille #viscosidad #tuberias #caudal #medicina #microfluidica
