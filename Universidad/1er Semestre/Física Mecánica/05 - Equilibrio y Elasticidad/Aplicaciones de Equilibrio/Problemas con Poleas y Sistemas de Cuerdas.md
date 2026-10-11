---
dg-publish: true
---

# Problemas con Poleas y Sistemas de Cuerdas

> [!quote] "Las poleas transforman la dirección y magnitud de las fuerzas, creando sistemas mecánicos donde la geometría define el equilibrio." 🔄
>
> [!info] Los problemas con poleas y sistemas de cuerdas representan aplicaciones fundamentales del equilibrio estático, donde las fuerzas se redistribuyen a través de cuerdas inextensibles y poleas que pueden ser fijas, móviles, o tener masa propia. Estos sistemas requieren análisis cuidadoso de las tensiones, considerando las restricciones geométricas y las condiciones de equilibrio.

## 🔄 Tipos de Poleas y Sistemas

> [!info] **Polea Fija (Ideal)** 📌
> 
> ### Características:
> 
> - **Posición**: Fija, no se traslada
> - **Función**: Cambia la dirección de la fuerza
> - **Ventaja mecánica**: VM = 1 (no multiplica fuerza)
> - **Tensión**: Constante en toda la cuerda
> 
> ### Propiedades en Equilibrio:
> 
> |Característica|Valor|Observación|
> |---|---|---|
> |Tensión en cuerda|T = constante|Sin fricción ni masa|
> |Fuerza aplicada|F = T|Misma magnitud que tensión|
> |Ventaja mecánica|VM = 1|Solo cambia dirección|
> |Equilibrio|ΣF = 0|En cada punto de la cuerda|
> 
> ### Ecuaciones de Equilibrio:
> 
> - **En la polea**: R₁ + R₂ + \vec{T}₁ + \vec{T}₂ = 0
> - **En la cuerda**: |T₁| = |T₂| = T
>
> [!tip] **Polea Móvil (Ideal)** 🔄
> 
> ### Características:
> 
> - **Posición**: Se mueve con la carga
> - **Función**: Multiplica la fuerza por 2
> - **Ventaja mecánica**: VM = 2
> - **Carga**: Soportada por dos segmentos de cuerda
> 
> ### Análisis de Fuerzas:
> 
> - **Carga total**: W
> - **Tensión en cuerda**: T = W/2
> - **Fuerza aplicada**: F = T = W/2
> - **Reacción en apoyo fijo**: R = T = W/2
> 
> ### Equilibrio de la Polea Móvil:
> 
> ΣF↑ = 2T - W = 0 → **T = W/2**
>
> [!warning] **Polea con Masa** ⚖️
> 
> ### Consideraciones Adicionales:
> 
> - **Peso de la polea**: Wₚ = mₚg
> - **Momento de inercia**: I (si hay rotación)
> - **Equilibrio traslacional**: ΣF = 0
> - **Equilibrio rotacional**: ΣM = 0
> 
> ### Para Polea Fija con Masa:
> 
> - Tensiones pueden ser diferentes: T₁ ≠ T₂
> - Equilibrio rotacional: (T₁ - T₂)R = 0 → T₁ = T₂ (sin fricción)
> - Equilibrio del eje: Rₓ² + Rᵧ² = (T₁ + T₂)²
> 
> ### Para Polea Móvil con Masa:
> 
> - Equilibrio vertical: T₁ + T₂ - W - Wₚ = 0
> - Si cuerda continua: T₁ = T₂ = T
> - Resultado: 2T = W + Wₚ → **T = (W + Wₚ)/2**
>
> [!success] 🔗 Configuraciones de Sistemas
> 
> ```mermaid
> graph TD
>     A[Sistema de Poleas] --> B[Poleas Fijas]
>     A --> C[Poleas Móviles]
>     A --> D[Sistemas Combinados]
>     B --> B1[Una Polea]
>     B --> B2[Múltiples Poleas]
>     C --> C1[Una Polea Móvil]
>     C --> C2[Polipastos]
>     D --> D1[Fijas + Móviles]
>     D --> D2[Planos Inclinados]
>     D --> D3[Masas Múltiples]
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
> ```
>
> [!note] **Restricciones Geométricas** 📐
> 
> ### Cuerdas Inextensibles:
> 
> - **Longitud total**: L = constante
> - **Relaciones**: Σlᵢ = L
> - **Velocidades**: Relacionadas por geometría
> 
> ### Sistemas con Múltiples Cuerdas:
> 
> #### **Cuerda Continua**:
> 
> - Misma tensión en todos los segmentos
> - T₁ = T₂ = ... = Tₙ = T
> 
> #### **Cuerdas Separadas**:
> 
> - Tensiones independientes
> - Cada cuerda analizada por separado
> 
> ### Relaciones Cinemáticas:
> 
> - **Desplazamientos**: Relacionados por geometría del sistema
> - **Aceleraciones**: Misma relación que desplazamientos
> - **Signos**: Consistentes con sistema de coordenadas

## 🎯 Estrategias de Resolución

> [!tip] **Método PACES (Poleas-Análisis-Cuerdas-Equilibrio-Sistema)** 🧠
> 
> ### **P**oleas - Identifica tipos y configuración
> 
> 1. Clasifica cada polea (fija, móvil, con masa)
> 2. Determina las funciones de cada polea
> 3. Identifica puntos de apoyo y conexiones
> 
> ### **A**nálisis - Examina el sistema completo
> 
> 4. Cuenta el número total de incógnitas
> 5. Identifica masas y cargas conocidas
> 6. Determina las restricciones geométricas
> 
> ### **C**uerdas - Analiza las conexiones
> 
> 7. Identifica si las cuerdas son continuas o separadas
> 8. Determina las tensiones en cada segmento
> 9. Aplica la condición de inextensibilidad
> 
> ### **E**quilibrio - Aplica condiciones para cada elemento
> 
> 10. Equilibrio de cada masa: ΣF = 0
> 11. Equilibrio de cada polea: ΣF = 0, ΣM = 0
> 12. Considera restricciones de movimiento
> 
> ### **S**istema - Resuelve ecuaciones simultáneas
> 
> 13. Plantea sistema de ecuaciones
> 14. Resuelve para encontrar tensiones y reacciones
> 15. Verifica coherencia física de resultados
>
> [!tip] **Técnicas Especializadas** 🔧
> 
> ### **Método del Cuerpo Libre**:
> 
> - Aislar cada masa y cada polea
> - Dibujar DCL para cada elemento
> - Aplicar equilibrio independientemente
> 
> ### **Método de la Cuerda Virtual**:
> 
> - Para sistemas con múltiples poleas móviles
> - Seguir el camino de la cuerda
> - Relacionar fuerzas por ventaja mecánica
> 
> ### **Principio del Trabajo Virtual**:
> 
> - Para sistemas complejos
> - Considerar desplazamientos virtuales
> - δW = ΣFᵢδxᵢ = 0 para equilibrio

## 📚 Problemas Tipo

> [!example] **Problema 1: Sistema Simple con Polea Fija** 🔄
> 
> ### Enunciado:
> 
> Dos masas m₁ = 10 kg y m₂ = 15 kg están conectadas por una cuerda inextensible que pasa sobre una polea fija ideal. Determina: a) La tensión en la cuerda para equilibrio b) La masa adicional necesaria en m₁ para lograr equilibrio
> 
> ### Solución:
> 
> **Parte a) Tensión actual (sistema no en equilibrio)**:
> 
> **DCL de cada masa**:
> 
> - m₁: T - m₁g = m₁a (↑)
> - m₂: m₂g - T = m₂a (↓)
> 
> **Si fuera equilibrio** (a = 0):
> 
> - m₁: T = m₁g = 10(9.8) = 98 N
> - m₂: T = m₂g = 15(9.8) = 147 N
> 
> **Conflicto**: 98 N ≠ 147 N → **No hay equilibrio natural**
> 
> **Parte b) Masa adicional para equilibrio**:
> 
> Sea Δm la masa adicional en m₁: (m₁ + Δm)g = m₂g (10 + Δm)(9.8) = 15(9.8) 10 + Δm = 15 **Δm = 5 kg**
> 
> **Tensión en equilibrio**: T = 15(9.8) = **147 N**
>
> [!example] **Problema 2: Sistema con Polea Móvil** 🏋️
> 
> ### Enunciado:
> 
> Un sistema consiste en una polea móvil ideal que soporta una masa de 20 kg. La cuerda pasa sobre una polea fija y se aplica una fuerza F en el extremo libre. Determina: a) La fuerza F necesaria para equilibrio b) La tensión en cada segmento de cuerda
> 
> ### Solución:
> 
> **Análisis del sistema**:
> 
> - Masa suspendida: m = 20 kg, W = 196 N
> - Polea móvil ideal (sin masa)
> - Cuerda continua → misma tensión T en toda la cuerda
> 
> **Equilibrio de la polea móvil**: La polea está soportada por dos segmentos de cuerda: ΣF↑ = 2T - W = 0 2T = 196 N **T = 98 N**
> 
> **Fuerza aplicada**: Como la cuerda es continua y la polea fija es ideal: **F = T = 98 N**
> 
> **Ventaja mecánica**: VM = W/F = 196/98 = **2**
> 
> **Verificación**: La polea móvil multiplica la fuerza por 2, permitiendo levantar 196 N con solo 98 N.
>
> [!example] **Problema 3: Sistema con Polea de Masa** ⚖️
> 
> ### Enunciado:
> 
> Una polea uniforme de masa M = 5 kg y radio R = 0.3 m puede rotar libremente alrededor de un eje fijo. Dos masas m₁ = 8 kg y m₂ = 12 kg cuelgan de los extremos de una cuerda que pasa sobre la polea. Determina las tensiones en la cuerda cuando el sistema está en equilibrio rotacional.
> 
> ### Solución:
> 
> **Datos**:
> 
> - Polea: M = 5 kg, R = 0.3 m
> - Masas: m₁ = 8 kg, m₂ = 12 kg
> - Sistema en equilibrio rotacional (ω = 0, α = 0)
> 
> **Equilibrio de cada masa**:
> 
> - Masa m₁: T₁ - m₁g = 0 → T₁ = 8(9.8) = 78.4 N
> - Masa m₂: T₂ - m₂g = 0 → T₂ = 12(9.8) = 117.6 N
> 
> **Equilibrio rotacional de la polea**: Para equilibrio rotacional: ΣM = 0 T₁R - T₂R = 0 T₁ = T₂
> 
> **Contradicción**: 78.4 N ≠ 117.6 N
> 
> **Interpretación**: El sistema NO puede estar en equilibrio estático con estas masas. La masa m₂ es mayor, por lo que el sistema tendrá aceleración angular.
> 
> **Para equilibrio estático**: Se necesitaría m₁ = m₂, entonces: **T₁ = T₂ = mg** (donde m sería la masa común)
>
> [!example] **Problema 4: Sistema Combinado (Atwood Modificado)** 🔗
> 
> ### Enunciado:
> 
> Un sistema consiste en dos poleas fijas: la masa m₁ = 6 kg cuelga directamente, la masa m₂ = 4 kg está sobre un plano inclinado 30° (sin fricción) conectada por cuerda que pasa sobre la segunda polea. Las cuerdas están conectadas entre sí. Determina las tensiones para equilibrio.
> 
> ### Solución:
> 
> **Configuración**:
> 
> - m₁ = 6 kg (cuelga verticalmente)
> - m₂ = 4 kg (en plano inclinado θ = 30°)
> - Cuerdas conectadas → misma tensión T
> 
> **Análisis de fuerzas**:
> 
> **Para m₁** (vertical): ΣF = 0: T - m₁g = 0 T = 6(9.8) = 58.8 N ... (1)
> 
> **Para m₂** (en plano inclinado): Componente paralela al plano: m₂g sen(30°) ΣF∥ = 0: T - m₂g sen(30°) = 0 T = 4(9.8)(0.5) = 19.6 N ... (2)
> 
> **Conflicto**: 58.8 N ≠ 19.6 N
> 
> **Interpretación**: Sistema no en equilibrio natural.
> 
> **Para lograr equilibrio**, necesitamos: m₁g = m₂g sen(θ) 6(9.8) = 4(9.8) sen(θ) sen(θ) = 6/4 = 1.5
> 
> Como sen(θ) > 1, **no es posible equilibrio** con estas masas.
> 
> **Alternativa**: Cambiar m₂ para θ = 30°: m₁g = m₂g sen(30°) 6 = m₂(0.5) **m₂ = 12 kg** (masa necesaria para equilibrio)
> 
> **Tensión en equilibrio**: T = 58.8 N
>
> [!example] **Problema 5: Polipasto (Sistema de Poleas Múltiples)** 🏗️
> 
> ### Enunciado:
> 
> Un polipasto consiste en una polea fija y dos poleas móviles en serie. Una carga de 480 N se suspende del último elemento móvil. Determina: a) La fuerza necesaria para levantar la carga b) La ventaja mecánica del sistema c) Las tensiones en cada segmento
> 
> ### Solución:
> 
> **Configuración**:
> 
> - 1 polea fija + 2 poleas móviles en serie
> - Carga: W = 480 N
> 
> **Análisis desde la carga hacia arriba**:
> 
> **Primera polea móvil** (más cercana a la carga):
> 
> - Soporta directamente W = 480 N
> - Tensión en cuerda que la sostiene: T₁ = W/2 = 240 N
> 
> **Segunda polea móvil**:
> 
> - Soporta el peso de la primera polea móvil
> - Carga efectiva = T₁ × 2 = 240 N × 2 = 480 N
> - Tensión que la sostiene: T₂ = 240/2 = 120 N
> 
> **Polea fija**:
> 
> - Solo cambia dirección
> - Tensión de salida = T₂ = 120 N
> 
> **Resultados**:
> 
> - **Fuerza aplicada**: F = 120 N
> - **Ventaja mecánica**: VM = W/F = 480/120 = **4**
> - **Tensiones**: T₁ = 240 N, T₂ = 120 N, F = 120 N
> 
> **Verificación**: Con n poleas móviles, VM = 2ⁿ = 2² = 4 ✓

## 🧮 Fórmulas y Relaciones

> [!tip] **Ventajas Mecánicas** 🔢
> 
> ### Sistemas Básicos:
> 
> #### **Polea Fija**:
> 
> - **VM = 1**
> - **F = W**
> - **Función**: Solo cambia dirección
> 
> #### **Polea Móvil**:
> 
> - **VM = 2**
> - **F = W/2**
> - **Cuerda**: 2 segmentos soportan la carga
> 
> #### **n Poleas Móviles en Serie**:
> 
> - **VM = 2ⁿ**
> - **F = W/2ⁿ**
> - **Longitud de cuerda**: (2ⁿ - 1) × distancia de elevación
> 
> ### Sistemas Combinados:
> 
> - **Poleas fijas**: No afectan VM, solo dirigen
> - **Poleas móviles**: Cada una multiplica VM por 2
> - **VM_total = ∏VM_individual**
>
> [!tip] **Relaciones Geométricas** 📐
> 
> ### Para Cuerdas Inextensibles:
> 
> #### **Sistema Simple** (2 masas, 1 polea):
> 
> - x₁ + x₂ = constante
> - v₁ = -v₂ (velocidades opuestas)
> - a₁ = -a₂ (aceleraciones opuestas)
> 
> #### **Sistema con Polea Móvil**:
> 
> - x_masa + 2×x_polea = constante
> - v_masa + 2×v_polea = 0
> - a_masa + 2×a_polea = 0
> 
> ### Longitud de Cuerda:
> 
> - **Sistema simple**: L = x₁ + x₂ + perímetro_polea
> - **Con polea móvil**: L = x₁ + 2×x_polea + constantes geométricas

## ⚠️ Errores Comunes

> [!warning] **Confusiones Frecuentes** ⚠️
> 
> 1. **Asumir que todas las poleas son ideales** sin considerar su masa
> 2. **Confundir polea fija con móvil** al calcular ventajas mecánicas
> 3. **No distinguir entre cuerdas continuas y separadas** para las tensiones
> 4. **Ignorar las restricciones geométricas** de las cuerdas inextensibles
> 5. **Aplicar equilibrio rotacional incorrectamente** en poleas con masa
> 6. **No verificar si el equilibrio es posible** antes de buscar soluciones
> 7. **Confundir la dirección de las tensiones** en sistemas complejos
> 8. **No considerar el peso propio** de poleas y cuerdas cuando es significativo
> 9. **Aplicar fórmulas de ventaja mecánica** sin verificar la configuración real

## 🎯 Aplicaciones Prácticas

> [!info] **Ejemplos del Mundo Real** 🌍
> 
> ### Construcción e Ingeniería:
> 
> - **Grúas de construcción**: Sistemas de poleas múltiples
> - **Montacargas**: Poleas móviles para reducir esfuerzo
> - **Ascensores**: Contrapesos y sistemas de cables
> - **Equipos de izaje**: Polipastos y aparejos
> 
> ### Transporte y Logística:
> 
> - **Sistemas de carga**: En puertos y almacenes
> - **Teleféricos**: Cables y poleas de gran escala
> - **Sistemas de transmisión**: Correas y poleas en maquinaria
> 
> ### Deportes y Recreación:
> 
> - **Equipos de gimnasio**: Poleas para ejercicios con pesas
> - **Alpinismo**: Sistemas de seguridad y rescate
> - **Vela**: Aparejos y sistemas de cabuyería
> 
> ### Maquinaria Industrial:
> 
> - **Tornos y cabrestantes**: Multiplicación de fuerza
> - **Prensas hidráulicas**: Combinación con sistemas de palancas
> - **Líneas de producción**: Transporte de materiales
> 
> ### Aplicaciones Domésticas:
> 
> - **Persianas**: Cuerdas y poleas simples
> - **Pozos de agua**: Poleas para facilitar extracción
> - **Tendederos**: Sistemas de cuerdas con poleas

## 📖 Referencias y Notas Relacionadas

> [!quote] **Notas Relacionadas**
> 
> - [[Equilibrio]] - Fundamentos de equilibrio estático
> - [[Problemas de Cuerdas y Poleas ideales]] - Casos con movimiento
> - [[Torque y Equilibrio Rotacional]] - Análisis de poleas con masa
> - [[Fuerzas y Diagramas de Cuerpo Libre]] - Técnicas de análisis
> - [[Aplicaciones de Equilibrio]] - Ejercicios complementarios
> - [[Segunda ley de Newton para Rotación]] - Para poleas en movimiento

## 🔧 Formulario de Consulta Rápida

> [!note] **Ecuaciones Esenciales**
> 
> ### Equilibrio Básico:
> 
> - **Traslacional**: ΣF = 0 para cada masa
> - **Rotacional**: ΣM = 0 para poleas con masa
> 
> ### Tensiones en Cuerdas:
> 
> - **Cuerda continua**: T = constante en todo el segmento
> - **Polea ideal**: T₁ = T₂ (ambos lados iguales)
> - **Polea con masa**: T₁ ≠ T₂ (pueden diferir)
> 
> ### Ventajas Mecánicas:
> 
> - **Polea fija**: VM = 1, F = W
> - **Polea móvil**: VM = 2, F = W/2
> - **n poleas móviles**: VM = 2ⁿ, F = W/2ⁿ
> 
> ### Restricciones Geométricas:
> 
> - **Cuerda inextensible**: Σlᵢ = constante
> - **Sistema simple**: x₁ + x₂ = constante
> - **Con polea móvil**: x_carga + 2×x_polea = constante
> 
> ### Condiciones de Equilibrio:
> 
> - **Sistema determinado**: n_ecuaciones = n_incógnitas
> - **Masas para equilibrio**: m₁g = m₂g (sistema simple)
> - **Con plano inclinado**: m₁g = m₂g sen(θ)

---

**Tags:** #poleas #cuerdas #tensiones #equilibrio #estatica #ventaja-mecanica #sistemas-mecanicos #DCL #polipastos #maquinas-simples
