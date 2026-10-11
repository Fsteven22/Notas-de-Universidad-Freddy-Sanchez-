---
dg-publish: true
---

# Problemas de Flujo con Viscosidad (Poiseuille)

> [!quote] "La viscosidad es la resistencia silenciosa que gobierna el mundo real; sin ella, Bernoulli sería rey, pero con ella, Poiseuille revela la verdad del flujo." 🌊
>
> [!info] El flujo con viscosidad introduce efectos de fricción que Bernoulli no considera. La ecuación de Poiseuille describe el flujo laminar viscoso en tuberías, fundamental para entender desde la circulación sanguínea hasta el transporte de petróleo en oleoductos.

## 🔧 Conceptos Fundamentales

> [!info] **Viscosidad y Esfuerzo Cortante** 🍯
> 
> ### Definición de Viscosidad:
> 
> **τ = μ(du/dy)** (Ley de Newton de la viscosidad)
> 
> ### Tipos de Viscosidad:
> 
> - **Viscosidad dinámica (μ)**: [Pa·s] o [N·s/m²]
> - **Viscosidad cinemática (ν)**: ν = μ/ρ [m²/s]
> 
> ### Fluidos Comunes:
> 
> |Fluido|μ (Pa·s) a 20°C|Característica|
> |---|---|---|
> |Aire|1.8 × 10⁻⁵|Muy poco viscoso|
> |Agua|1.0 × 10⁻³|Referencia estándar|
> |Aceite SAE 30|0.2|Moderadamente viscoso|
> |Miel|2-10|Muy viscoso|
> |Glicerina|1.5|Viscosidad alta|
> 
> ### Perfiles de Velocidad:
> 
> - **Flujo laminar**: Perfil parabólico
> - **Flujo turbulento**: Perfil más plano
> - **Velocidad máxima**: En el centro del tubo
>
> [!tip] **Ecuación de Poiseuille** 🧪
> 
> ### Para Tubo Circular:
> 
> **Q = (π × ΔP × R⁴)/(8 × μ × L)**
> 
> ### Formas Alternativas:
> 
> **ΔP = (8μLQ)/(πR⁴) = (128μLQ)/(πD⁴)**
> 
> **v_max = (ΔP × R²)/(4μL)**
> 
> **v_promedio = v_max/2**
> 
> ### Variables:
> 
> - **Q**: Caudal volumétrico [m³/s]
> - **ΔP**: Diferencia de presión [Pa]
> - **R**: Radio del tubo [m]
> - **D**: Diámetro del tubo [m]
> - **μ**: Viscosidad dinámica [Pa·s]
> - **L**: Longitud del tubo [m]
>
> [!warning] **Número de Reynolds** ⚡
> 
> ### Definición:
> 
> **Re = (ρvD)/μ = (vD)/ν**
> 
> ### Criterios de Flujo:
> 
> - **Re < 2,100**: Flujo laminar (Poiseuille válida)
> - **2,100 < Re < 4,000**: Flujo de transición
> - **Re > 4,000**: Flujo turbulento (Poiseuille NO válida)
> 
> ### Implicaciones:
> 
> |Tipo de Flujo|Características|Pérdidas|
> |---|---|---|
> |Laminar|Ordenado, predecible|∝ v¹|
> |Transición|Inestable, variable|Variable|
> |Turbulento|Caótico, mezclado|∝ v²|
>
> [!success] 🔗 Resistencia Hidráulica
> 
> ```mermaid
> graph TD
>     A[Flujo Viscoso] --> B[Resistencia Lineal]
>     A --> C[Resistencia Local]
>     B --> D[Fricción en Paredes]
>     C --> E[Cambios de Dirección]
>     C --> F[Cambios de Sección]
>     D --> G[Factor de Fricción f]
>     E --> H[Coeficiente K]
>     F --> I[Pérdidas Menores]
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
>     style G fill:#fce4ec
> ```
>
> [!note] **Analogía con Circuitos Eléctricos** ⚡
> 
> ### Resistencia Hidráulica:
> 
> **R_h = (8μL)/(πR⁴)** (equivalente a resistencia eléctrica)
> 
> ### Ley de "Ohm" para Fluidos:
> 
> **ΔP = R_h × Q** (similar a V = R × I)
> 
> ### Resistencias en Serie:
> 
> **R_total = R₁ + R₂ + R₃ + ...**
> 
> ### Resistencias en Paralelo:
> 
> **1/R_total = 1/R₁ + 1/R₂ + 1/R₃ + ...**

## 🎯 Estrategias de Resolución

> [!tip] **Método VAPOR (Viscosidad-Área-Presión-Ohm-Reynolds)** 🧠
> 
> ### **V**iscosidad - Identifica las propiedades del fluido
> 
> 1. Determina μ (viscosidad dinámica) del fluido
> 2. Considera variación con temperatura si es relevante
> 3. Verifica si el fluido es newtoniano
> 
> ### **A**rea - Analiza la geometría del sistema
> 
> 4. Calcula el radio o diámetro efectivo
> 5. Identifica la longitud característica
> 6. Considera rugosidad si es significativa
> 
> ### **P**resión - Establece la diferencia de presión
> 
> 7. Identifica presiones en entrada y salida
> 8. Considera efectos de altura si es relevante
> 9. Distingue entre presión manométrica y absoluta
> 
> ### **O**hm - Aplica la analogía eléctrica
> 
> 10. Calcula la resistencia hidráulica
> 11. Usa ΔP = R_h × Q para relacionar variables
> 12. Considera sistemas en serie/paralelo
> 
> ### **R**eynolds - Verifica el régimen de flujo
> 
> 13. Calcula Re = ρvD/μ
> 14. Confirma que Re < 2,100 para usar Poiseuille
> 15. Ajusta método si el flujo no es laminar

## 📚 Problemas Tipo

> [!example] **Problema 1: Flujo en Tubería Simple** 🔧
> 
> ### Enunciado:
> 
> Aceite SAE 30 (μ = 0.2 Pa·s, ρ = 900 kg/m³) fluye por una tubería horizontal de 10 mm de diámetro y 2 m de longitud. Si la diferencia de presión es 50 kPa, calcula: a) El caudal b) La velocidad promedio c) Verifica que el flujo sea laminar
> 
> ### Datos:
> 
> - μ = 0.2 Pa·s
> - ρ = 900 kg/m³
> - D = 10 mm = 0.01 m → R = 0.005 m
> - L = 2 m
> - ΔP = 50 kPa = 50,000 Pa
> 
> ### Solución:
> 
> **a) Caudal usando Poiseuille:**
> 
> Q = (π × ΔP × R⁴)/(8 × μ × L)
> 
> Q = (π × 50,000 × (0.005)⁴)/(8 × 0.2 × 2)
> 
> Q = (π × 50,000 × 6.25 × 10⁻¹⁰)/(3.2)
> 
> **Q = 3.07 × 10⁻⁵ m³/s = 0.0307 L/s = 1.84 L/min**
> 
> **b) Velocidad promedio:**
> 
> A = π(0.005)² = 7.85 × 10⁻⁵ m²
> 
> **v = Q/A = (3.07 × 10⁻⁵)/(7.85 × 10⁻⁵) = 0.391 m/s**
> 
> **c) Verificación del régimen:**
> 
> Re = (ρvD)/μ = (900 × 0.391 × 0.01)/0.2 = 17.6
> 
> **Como Re = 17.6 << 2,100, el flujo es LAMINAR** ✓
> 
> La aplicación de Poiseuille es válida.
>
> [!example] **Problema 2: Sistema de Tuberías en Serie** 🔗
> 
> ### Enunciado:
> 
> Agua (μ = 1×10⁻³ Pa·s) fluye por un sistema de dos tuberías en serie: Tubería 1: D₁ = 20 mm, L₁ = 5 m; Tubería 2: D₂ = 15 mm, L₂ = 3 m. Si el caudal total es 0.5 L/s, calcula: a) La caída de presión en cada tubería b) La caída de presión total
> 
> ### Datos:
> 
> - μ = 1×10⁻³ Pa·s
> - Q = 0.5 L/s = 5×10⁻⁴ m³/s
> - Tubería 1: D₁ = 20 mm, L₁ = 5 m
> - Tubería 2: D₂ = 15 mm, L₂ = 3 m
> 
> ### Solución:
> 
> **Resistencias hidráulicas:**
> 
> R₁ = (8μL₁)/(πR₁⁴) = (8μL₁)/(π(D₁/2)⁴) = (128μL₁)/(πD₁⁴)
> 
> R₁ = (128 × 1×10⁻³ × 5)/(π × (0.02)⁴) = 0.64/(π × 1.6×10⁻⁷) = **1.27 × 10⁹ Pa·s/m³**
> 
> R₂ = (128 × 1×10⁻³ × 3)/(π × (0.015)⁴) = 0.384/(π × 5.06×10⁻⁸) = **2.42 × 10⁹ Pa·s/m³**
> 
> **a) Caídas de presión:**
> 
> ΔP₁ = R₁ × Q = 1.27 × 10⁹ × 5×10⁻⁴ = **635,000 Pa = 635 kPa**
> 
> ΔP₂ = R₂ × Q = 2.42 × 10⁹ × 5×10⁻⁴ = **1,210,000 Pa = 1,210 kPa**
> 
> **b) Caída total:**
> 
> **ΔP_total = ΔP₁ + ΔP₂ = 635 + 1,210 = 1,845 kPa**
> 
> **Observación**: La tubería más estrecha (menor D) tiene mayor resistencia y mayor caída de presión.
>
> [!example] **Problema 3: Flujo Sanguíneo (Aplicación Biomédica)** ❤️
> 
> ### Enunciado:
> 
> En una arteria coronaria de 2 mm de diámetro y 40 mm de longitud, la sangre (μ = 4×10⁻³ Pa·s, ρ = 1060 kg/m³) tiene una diferencia de presión de 3 mmHg. Calcula: a) El caudal sanguíneo b) La velocidad promedio c) ¿Es válida la aproximación de Poiseuille?
> 
> ### Datos:
> 
> - D = 2 mm = 0.002 m
> - L = 40 mm = 0.04 m
> - μ = 4×10⁻³ Pa·s (sangre)
> - ρ = 1060 kg/m³
> - ΔP = 3 mmHg = 3 × 133.3 = 400 Pa
> 
> ### Solución:
> 
> **a) Caudal sanguíneo:**
> 
> Q = (π × ΔP × R⁴)/(8 × μ × L)
> 
> R = 0.001 m
> 
> Q = (π × 400 × (0.001)⁴)/(8 × 4×10⁻³ × 0.04)
> 
> Q = (π × 400 × 10⁻¹²)/(1.28×10⁻³)
> 
> **Q = 9.82 × 10⁻⁷ m³/s = 0.982 mL/s = 58.9 mL/min**
> 
> **b) Velocidad promedio:**
> 
> A = π(0.001)² = 3.14 × 10⁻⁶ m²
> 
> **v = Q/A = (9.82 × 10⁻⁷)/(3.14 × 10⁻⁶) = 0.313 m/s = 31.3 cm/s**
> 
> **c) Verificación de Reynolds:**
> 
> Re = (ρvD)/μ = (1060 × 0.313 × 0.002)/(4×10⁻³) = 166
> 
> **Como Re = 166 < 2,100, el flujo es LAMINAR**
> 
> La ecuación de Poiseuille es aplicable, aunque hay que considerar que la sangre no es completamente newtoniana.
> 
> **Nota médica**: Este caudal está dentro del rango normal para arterias coronarias.

## 🧮 Técnicas de Memorización

> [!tip] **Mnemotecnia: "RADIO"** 🎯
> 
> **R**⁴ en el numerador → **R**adio a la cuarta potencia es clave **A**umento de radio → **D**ismunuye resistencia enormemente **D**iámetro doble → resistencia 1/16 (porque R⁴) **I**nverso de viscosidad → más viscoso, menos caudal **O**hm hidráulico → ΔP = R × Q
>
> [!tip] **Regla del Radio** 📏
> 
> **"El radio gobierna"**: Si R se duplica, Q aumenta 16 veces
> 
> - R × 2 → Q × 16
> - R × 1/2 → Q × 1/16
> 
> **Efecto Dominante**: El radio tiene más impacto que cualquier otra variable

## ⚠️ Errores Comunes

> [!warning] **Confusiones Frecuentes** ⚠️
> 
> 1. **Confundir radio con diámetro**: Usar D en lugar de R en la fórmula de Poiseuille
> 2. **Ignorar el régimen de flujo**: Aplicar Poiseuille cuando Re > 2,100
> 3. **Unidades inconsistentes**: Mezclar mm, cm, m sin conversión adecuada
> 4. **Viscosidad dinámica vs cinemática**: Usar ν en lugar de μ
> 5. **Presión mal definida**: No especificar si es manométrica o absoluta
> 6. **Efectos de temperatura**: Ignorar variación de viscosidad con T
> 7. **Fluidos no newtonianos**: Aplicar a sangre, pinturas, etc. sin considerar limitaciones
> 8. **Entrada del tubo**: No considerar longitud de desarrollo del flujo

## 🎯 Aplicaciones Prácticas

> [!info] **Ejemplos del Mundo Real** 🌍
> 
> ### Biomedicina:
> 
> - **Circulación sanguínea**: Arterias, venas, capilares
> - **Microfluidica**: Dispositivos lab-on-chip
> - **Sistemas de infusión**: Goteros, bombas de insulina
> - **Diálisis**: Filtros de sangre
> 
> ### Industria Petrolera:
> 
> - **Oleoductos**: Transporte de crudo viscoso
> - **Perforación**: Lodos de perforación
> - **Refinería**: Flujo de productos pesados
> 
> ### Ingeniería Química:
> 
> - **Reactores tubulares**: Tiempo de residencia
> - **Intercambiadores de calor**: Flujo en tubos pequeños
> - **Procesos de separación**: Membranas
> 
> ### Lubricación:
> 
> - **Cojinetes**: Película lubricante
> - **Sistemas hidráulicos**: Aceites de alta presión
> - **Motores**: Circulación de aceite
> 
> ### HVAC:
> 
> - **Sistemas de calefacción**: Radiadores
> - **Aire acondicionado**: Tuberías de refrigerante
> - **Ventilación**: Conductos de baja velocidad

## 📖 Referencias

> [!quote] **Notas Relacionadas**
> 
> - [[Problemas de Ecuación de Bernoulli]] - Flujo ideal sin viscosidad
> - [[Viscosidad y Número de Reynolds]] - Caracterización del flujo
> - [[Flujo Laminar y Ecuación de Poiseuille]] - Teoría fundamental
> - [[Problemas de Ecuación de Continuidad]] - Conservación de masa
> - **Próximo tema**: [[Problemas de Flotabilidad en Fluidos en Movimiento]]

## 📚 Notas Recomendadas

> [!note] **Prerrequisitos**
> 
> - [[Problemas de Ecuación de Continuidad]] - Conservación de masa
> - [[Presión y Densidad]] - Propiedades de fluidos
> - **Matemáticas**: Cálculo diferencial, ecuaciones diferenciales básicas
> 
> ### **Conocimientos Previos**:
> 
> - Concepto de viscosidad y esfuerzo cortante
> - Perfiles de velocidad en flujo laminar
> - Analogías con circuitos eléctricos
>
> [!note] **Temas Avanzados**
> 
> - **Flujo no newtoniano**: Fluidos complejos
> - **Flujo en medios porosos**: Ley de Darcy
> - **Microfluidica**: Efectos a escala micrométrica
> - **Lubricación hidrodinámica**: Teoría de Reynolds

---

**Tags:** #hidrodinamica #viscosidad #poiseuille #flujo-laminar #reynolds #resistencia-hidraulica #tuberia #caudal #presion #biomedica #lubricacion #fisica-mecanica #problemas
