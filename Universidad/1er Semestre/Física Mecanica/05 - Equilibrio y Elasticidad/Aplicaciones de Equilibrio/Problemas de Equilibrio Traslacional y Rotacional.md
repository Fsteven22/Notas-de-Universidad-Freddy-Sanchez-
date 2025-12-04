# Problemas de Equilibrio Traslacional y Rotacional

> [!quote] "En equilibrio, las fuerzas se anulan y los torques se equilibran; la estática es la sinfonía perfecta entre la traslación y la rotación en reposo." ⚖️

> [!info]- Los problemas de equilibrio traslacional y rotacional forman la base de la estática, donde los cuerpos permanecen en reposo o en movimiento rectilíneo uniforme. Estos problemas requieren la aplicación simultánea de las condiciones de equilibrio de fuerzas y torques para determinar fuerzas desconocidas, puntos de aplicación y condiciones de estabilidad.

## ⚖️ Condiciones de Equilibrio

> [!info]- **Equilibrio Traslacional** ➡️
> 
> ### Condición Fundamental:
> 
> **ΣF⃗ = 0** (La suma vectorial de todas las fuerzas es nula)
> 
> ### En Componentes:
> 
> - **ΣFₓ = 0**: Suma de componentes horizontales
> - **ΣFᵧ = 0**: Suma de componentes verticales
> - **ΣFᵤ = 0**: Suma de componentes en la dirección z (3D)
> 
> ### Interpretación Física:
> 
> |Condición|Significado|Resultado|
> |---|---|---|
> |ΣFₓ = 0|No hay aceleración horizontal|vₓ = constante|
> |ΣFᵧ = 0|No hay aceleración vertical|vᵧ = constante|
> |Ambas cumplen|Equilibrio traslacional completo|v⃗ = constante|

> [!tip]- **Equilibrio Rotacional** 🔄
> 
> ### Condición Fundamental:
> 
> **Στ = 0** (La suma algebraica de todos los torques es nula)
> 
> ### Características del Torque:
> 
> - **Definición**: τ = r⃗ × F⃗ = rF sen(θ)
> - **Brazo de palanca**: Distancia perpendicular desde el eje hasta la línea de acción
> - **Signo**: Positivo (antihorario) o negativo (horario) por convención
> - **Punto de referencia**: Puede elegirse arbitrariamente
> 
> ### Elementos Clave:
> 
> - **Magnitud**: |τ| = rF sen(θ) = r⊥F = rF⊥
> - **Dirección**: Determinada por la regla de la mano derecha
> - **Unidades**: N·m (Newton-metro)

> [!warning]- **Equilibrio Estático Completo** 🏗️
> 
> ### Condiciones Simultáneas:
> 
> Para que un cuerpo esté en equilibrio estático completo debe cumplir:
> 
> 1. **ΣF⃗ = 0** (Equilibrio traslacional)
> 2. **Στ = 0** (Equilibrio rotacional)
> 
> ### Tipos de Equilibrio:
> 
> - **Estable**: Pequeñas perturbaciones restauran el equilibrio
> - **Inestable**: Pequeñas perturbaciones alejan del equilibrio
> - **Neutro**: Perturbaciones no cambian la energía potencial
> 
> ### Centro de Gravedad:
> 
> - Para equilibrio estable: CG debe estar sobre la base de sustentación
> - Altura del CG afecta la estabilidad
> - Base más amplia proporciona mayor estabilidad

> [!success] 🔗 Estrategia de Análisis
> 
> ```mermaid
> graph TD
>     A[Problema de Equilibrio] --> B[Identificar el Cuerpo]
>     B --> C[Dibujar DCL]
>     C --> D[Elegir Sistema de Coordenadas]
>     D --> E[Elegir Punto de Referencia para Torques]
>     E --> F[Aplicar ΣF = 0]
>     F --> G[Aplicar Στ = 0]
>     G --> H[Resolver Sistema de Ecuaciones]
>     H --> I[Verificar Resultados]
>     
>     style A fill:#e1f5fe
>     style C fill:#f3e5f5
>     style F fill:#fff3e0
>     style G fill:#e8f5e8
> ```

> [!note]- **Tipos de Apoyos y Reacciones** 🔧
> 
> ### Apoyos Simples:
> 
> #### **Apoyo de Rodillo** 🎳:
> 
> - **Reacciones**: 1 fuerza perpendicular a la superficie
> - **Grados de libertad restringidos**: 1
> - **Símbolo**: ∧ con círculo
> 
> #### **Apoyo de Pasador/Articulación** 📌:
> 
> - **Reacciones**: 2 fuerzas (horizontal y vertical)
> - **Grados de libertad restringidos**: 2
> - **Símbolo**: ○ con líneas
> 
> #### **Empotramiento** 🔒:
> 
> - **Reacciones**: 2 fuerzas + 1 momento
> - **Grados de libertad restringidos**: 3
> - **Símbolo**: Líneas paralelas rayadas
> 
> ### Tabla de Reacciones:
> 
> |Tipo de Apoyo|Rₓ|Rᵧ|M|Total|
> |---|---|---|---|---|
> |Rodillo|❌|✅|❌|1|
> |Pasador|✅|✅|❌|2|
> |Empotramiento|✅|✅|✅|3|

## 🎯 Estrategias de Resolución

> [!tip]- **Método DICES (DCL-Incógnitas-Coordenadas-Equilibrio-Solución)** 🧠
> 
> ### **D**CL - Diagrama de Cuerpo Libre
> 
> 1. Aisla el cuerpo de interés
> 2. Dibuja todas las fuerzas externas
> 3. Incluye reacciones en los apoyos
> 4. Representa el peso en el centro de gravedad
> 
> ### **I**ncógnitas - Identifica variables desconocidas
> 
> 5. Lista todas las fuerzas y momentos desconocidos
> 6. Cuenta el número total de incógnitas
> 7. Verifica que el problema sea determinado
> 
> ### **C**oordenadas - Define sistema de referencia
> 
> 8. Elige ejes x, y convenientes
> 9. Selecciona punto de referencia para torques
> 10. Define convención de signos para torques
> 
> ### **E**quilibrio - Aplica condiciones
> 
> 11. Escribe ΣFₓ = 0
> 12. Escribe ΣFᵧ = 0
> 13. Escribe Στ = 0 (respecto al punto elegido)
> 
> ### **S**olución - Resuelve y verifica
> 
> 14. Resuelve el sistema de ecuaciones
> 15. Verifica signos y unidades
> 16. Comprueba coherencia física

> [!tip]- **Estrategias Avanzadas** 🎯
> 
> ### **Elección Inteligente del Punto de Referencia**:
> 
> - Elegir punto donde pasan varias fuerzas desconocidas
> - Minimiza el número de términos en la ecuación de torques
> - Facilita la resolución del sistema
> 
> ### **Método de las Secciones**:
> 
> - Para estructuras complejas (armaduras)
> - Cortar la estructura imaginariamente
> - Analizar el equilibrio de cada sección
> 
> ### **Principio de Superposición**:
> 
> - Para cargas múltiples
> - Analizar cada carga por separado
> - Sumar los efectos algebraicamente

## 📚 Problemas Tipo

> [!example]- **Problema 1: Viga Simplemente Apoyada** 🌉
> 
> ### Enunciado:
> 
> Una viga uniforme de 8 m de longitud y 200 N de peso está apoyada en sus extremos A y B. Una carga concentrada de 500 N se aplica a 3 m del extremo A. Determina las reacciones en los apoyos.
> 
> ### Solución:
> 
> **Datos**:
> 
> - L = 8 m, W = 200 N (peso de la viga)
> - P = 500 N aplicada a 3 m de A
> - Apoyos: A (rodillo), B (rodillo)
> 
> **DCL y coordenadas**:
> 
> - Fuerzas: Rₐ (↑), R᷇ᵦ (↑), W (↓) en L/2, P (↓) a 3m de A
> 
> **Equilibrio traslacional**: ΣFᵧ = 0: Rₐ + R᷇ᵦ - W - P = 0 Rₐ + R᷇ᵦ = 700 N ... (1)
> 
> **Equilibrio rotacional** (tomando momentos respecto a A): ΣΜₐ = 0: -W(4) - P(3) + R᷇ᵦ(8) = 0 -200(4) - 500(3) + R᷇ᵦ(8) = 0 -800 - 1500 + 8R᷇ᵦ = 0 **R᷇ᵦ = 287.5 N**
> 
> De ecuación (1): **Rₐ = 412.5 N**
> 
> **Verificación** (momentos respecto a B): ΣΜᵦ = 0: Rₐ(8) - W(4) - P(5) = 412.5(8) - 200(4) - 500(5) = 0 ✓

> [!example]- **Problema 2: Viga en Voladizo** 🏗️
> 
> ### Enunciado:
> 
> Una viga uniforme de 6 m y 300 N está empotrada en A. Una carga distribuida de 100 N/m actúa sobre los primeros 4 m desde A. Determina las reacciones en el empotramiento.
> 
> ### Solución:
> 
> **Datos**:
> 
> - L = 6 m, W = 300 N
> - Carga distribuida: w = 100 N/m sobre 4 m
> - Carga total distribuida: Wᵈ = 100 × 4 = 400 N (actúa en el centro: 2 m de A)
> 
> **Incógnitas en el empotramiento**:
> 
> - Rₓ (horizontal), Rᵧ (vertical), Mₐ (momento)
> 
> **Equilibrio traslacional**: ΣFₓ = 0: Rₓ = 0 (no hay fuerzas horizontales) ΣFᵧ = 0: Rᵧ - W - Wᵈ = 0 **Rᵧ = 300 + 400 = 700 N** (↑)
> 
> **Equilibrio rotacional** (respecto a A): ΣΜₐ = 0: Mₐ - W(3) - Wᵈ(2) = 0 Mₐ = 300(3) + 400(2) = 900 + 800 **Mₐ = 1700 N·m** (antihorario)

> [!example]- **Problema 3: Estructura con Cable** 🎪
> 
> ### Enunciado:
> 
> Una barra uniforme AB de 4 m y 80 N está articulada en A y sostenida por un cable en B que forma 60° con la horizontal. Si se cuelga una carga de 120 N en el punto medio de la barra, determina: a) La tensión en el cable b) Las reacciones en A
> 
> ### Solución:
> 
> **Datos**:
> 
> - L = 4 m, W_barra = 80 N
> - Cable en B: θ = 60° con horizontal
> - Carga: P = 120 N en el punto medio (2 m de A)
> 
> **DCL de la barra**:
> 
> - En A: Rₐₓ (→), Rₐᵧ (↑)
> - En B: T cos(60°) (←), T sen(60°) (↑)
> - Cargas: W_barra (↓) en 2m, P (↓) en 2m
> 
> **Equilibrio traslacional**: ΣFₓ = 0: Rₐₓ - T cos(60°) = 0 Rₐₓ = T/2 ... (1)
> 
> ΣFᵧ = 0: Rₐᵧ + T sen(60°) - 80 - 120 = 0 Rₐᵧ = 200 - T(√3/2) ... (2)
> 
> **Equilibrio rotacional** (respecto a A): ΣΜₐ = 0: T sen(60°)(4) + T cos(60°)(0) - 80(2) - 120(2) = 0 4T(√3/2) = 160 + 240 = 400 2√3 T = 400 **T = 200/√3 = 115.47 N**
> 
> **Reacciones en A**: Rₐₓ = 115.47/2 = **57.74 N** (→) Rₐᵧ = 200 - 115.47(√3/2) = **100 N** (↑)

> [!example]- **Problema 4: Escalera Apoyada en Pared** 🪜
> 
> ### Enunciado:
> 
> Una escalera uniforme de 5 m y 40 N se apoya contra una pared vertical lisa. El coeficiente de fricción estática entre la escalera y el suelo es μₛ = 0.3. Un hombre de 700 N sube hasta una distancia de 3 m desde la base. Determina: a) El ángulo mínimo con la vertical para que no resbale b) Las fuerzas de reacción
> 
> ### Solución:
> 
> **Datos**:
> 
> - L = 5 m, W_escalera = 40 N, W_hombre = 700 N
> - μₛ = 0.3, pared lisa (solo reacción normal)
> - Hombre a 3 m de la base
> 
> **DCL de la escalera**:
> 
> - Base: N₁ (↑), f (→) ≤ μₛN₁
> - Pared: N₂ (←)
> - Pesos: W_escalera en L/2, W_hombre a 3m de la base
> 
> **Equilibrio traslacional**: ΣFₓ = 0: f - N₂ = 0 → f = N₂ ... (1) ΣFᵧ = 0: N₁ - 40 - 700 = 0 → **N₁ = 740 N** ... (2)
> 
> **Equilibrio rotacional** (respecto a la base): ΣΜ_base = 0: N₂L sen(θ) - W_escalera(L/2)cos(θ) - W_hombre(3)cos(θ) = 0 N₂(5)sen(θ) = 40(2.5)cos(θ) + 700(3)cos(θ) 5N₂ sen(θ) = (100 + 2100)cos(θ) N₂ = 2200 cos(θ)/(5 sen(θ)) = **440 cot(θ)** ... (3)
> 
> **Condición de no deslizamiento**: f ≤ μₛN₁ → N₂ ≤ 0.3(740) = 222 N
> 
> 440 cot(θ) ≤ 222 cot(θ) ≤ 0.5045 tan(θ) ≥ 1.982 **θ_min = 63.2°** con la vertical
> 
> **Para θ = 63.2°**: N₂ = 440 × 0.5045 = **222 N** (←) f = **222 N** (→)

## 🧮 Técnicas Especializadas

> [!tip]- **Análisis de Armaduras** 🔗
> 
> ### Método de los Nudos:
> 
> 1. Calcular reacciones externas
> 2. Analizar equilibrio en cada nudo
> 3. Asumir todas las barras en tensión
> 4. Resultado negativo indica compresión
> 
> ### Método de las Secciones:
> 
> 5. Cortar la armadura por una sección
> 6. Considerar equilibrio de una parte
> 7. Aplicar ΣF = 0 y ΣΜ = 0
> 8. Máximo 3 barras cortadas por sección

> [!tip]- **Centros de Gravedad Compuestos** ⚖️
> 
> ### Para áreas compuestas:
> 
> x̄ = (A₁x₁ + A₂x₂ + ... + Aₙxₙ)/(A₁ + A₂ + ... + Aₙ) ȳ = (A₁y₁ + A₂y₂ + ... + Aₙyₙ)/(A₁ + A₂ + ... + Aₙ)
> 
> ### Formas comunes:
> 
> - **Rectángulo**: CG en el centro geométrico
> - **Triángulo**: CG a h/3 desde la base
> - **Semicírculo**: CG a 4R/(3π) desde el diámetro
> - **Cuarto de círculo**: CG a 4R/(3π) de cada eje

> [!tip]- **Estabilidad de Estructuras** 🏗️
> 
> ### Criterios de Estabilidad:
> 
> #### **Determinación Estática**:
> 
> - **Externamente**: r = 3 (2D), r = 6 (3D)
> - **Internamente**: m = 2j - 3 (armaduras planas)
> - **Condición**: r + m = total de incógnitas
> 
> #### **Tipos de Estructuras**:
> 
> - **Estáticamente determinada**: r + m = incógnitas
> - **Estáticamente indeterminada**: r + m > incógnitas
> - **Inestable**: r + m < incógnitas
> 
> ### Análisis de Pandeo:
> 
> - **Carga crítica**: P_cr = π²EI/(KL)²
> - **Factor de longitud efectiva**: K (depende de apoyos)
> - **Esbeltez**: λ = KL/r (r = radio de giro)

## ⚠️ Errores Comunes

> [!warning]- **Confusiones Frecuentes** ⚠️
> 
> 1. **Olvidar incluir el peso propio** del elemento estructural
> 2. **Confundir el punto de aplicación** de cargas distribuidas
> 3. **Elegir mal el punto de referencia** para calcular momentos
> 4. **No verificar** el equilibrio usando otro punto de referencia
> 5. **Ignorar la dirección** de las reacciones en los apoyos
> 6. **Aplicar ΣΜ = 0** respecto a puntos que se mueven
> 7. **No considerar la geometría** correcta para calcular brazos de palanca
> 8. **Confundir tensión con compresión** en elementos estructurales
> 9. **No verificar** si la estructura es estáticamente determinada

## 🎯 Aplicaciones Prácticas

> [!info]- **Ejemplos del Mundo Real** 🌍
> 
> ### Ingeniería Civil:
> 
> - Diseño de puentes y estructuras
> - Análisis de edificios y torres
> - Cálculo de cimentaciones
> - Diseño de grúas y equipos de construcción
> 
> ### Ingeniería Mecánica:
> 
> - Diseño de máquinas y mecanismos
> - Análisis de estructuras de soporte
> - Cálculo de esfuerzos en elementos mecánicos
> - Diseño de herramientas y dispositivos
> 
> ### Biomecánica:
> 
> - Análisis del equilibrio corporal
> - Diseño de prótesis y órtesis
> - Estudio de la postura humana
> - Análisis de movimientos articulares
> 
> ### Ingeniería Naval y Aeronáutica:
> 
> - Estabilidad de embarcaciones
> - Diseño de estructuras aeronáuticas
> - Análisis de cargas en vuelo
> - Cálculo de centros de gravedad

## 📖 Referencias y Notas Relacionadas

> [!quote]- **Notas Relacionadas**
> 
> - [[Equilibrio]] - Fundamentos teóricos del equilibrio
> - [[Centro de Gravedad (CG)]] - Localización del centro de gravedad
> - [[Torque y Equilibrio Rotacional]] - Análisis detallado de torques
> - [[Fuerzas y Diagramas de Cuerpo Libre]] - Técnicas de DCL
> - [[Aplicaciones de Equilibrio]] - Ejercicios adicionales
> - [[Elasticidad]] - Deformaciones en equilibrio

## 🔧 Formulario de Consulta Rápida

> [!note]- **Ecuaciones Esenciales**
> 
> ### Condiciones de Equilibrio:
> 
> - **Traslacional**: ΣFₓ = 0, ΣFᵧ = 0, ΣFᵤ = 0
> - **Rotacional**: ΣΜ = 0 (respecto a cualquier punto)
> 
> ### Torque:
> 
> - **Magnitud**: τ = r × F = rF sen(θ) = r⊥F
> - **Convención**: (+) antihorario, (-) horario
> 
> ### Centro de Gravedad:
> 
> - **Compuesto**: x̄ = ΣAᵢxᵢ/ΣAᵢ, ȳ = ΣAᵢyᵢ/ΣAᵢ
> 
> ### Reacciones en Apoyos:
> 
> - **Rodillo**: 1 reacción perpendicular
> - **Pasador**: 2 reacciones (Rₓ, Rᵧ)
> - **Empotramiento**: 3 reacciones (Rₓ, Rᵧ, M)
> 
> ### Fricción:
> 
> - **Estática**: f ≤ μₛN
> - **Cinética**: f = μₖN

---

**Tags:** #equilibrio #estatica #torque #momento #reacciones #apoyos #DCL #estructuras #estabilidad #centro-gravedad #armaduras #vigas