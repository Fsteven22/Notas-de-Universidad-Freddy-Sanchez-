# Problemas de Conservación de Energía Mecánica

> [!quote] "La energía no se crea ni se destruye, solo se transforma; en cada problema de conservación encontramos la poesía del movimiento convertida en matemáticas." ⚡

> [!info]- La conservación de la energía mecánica es uno de los principios más poderosos de la física, permitiendo resolver problemas complejos de movimiento sin necesidad de analizar fuerzas. Cuando solo actúan fuerzas conservativas, la energía mecánica total del sistema permanece constante, transformándose entre energía cinética y potencial.

## ⚖️ Fundamentos de la Conservación

> [!info]- **Energía Mecánica Total** ⚡
> 
> ### Definición:
> 
> **E_mecánica = E_cinética + E_potencial**
> 
> - **E_c = ½mv²**: Energía cinética de traslación
> - **E_p = mgh**: Energía potencial gravitatoria
> - **E_p = ½kx²**: Energía potencial elástica
> 
> ### Principio de Conservación:
> 
> **E_inicial = E_final** (cuando solo actúan fuerzas conservativas)
> 
> |Tipo de Fuerza|Conserva Energía|Ejemplos|
> |---|---|---|
> |Conservativas|✅ Sí|Gravitatoria, elástica, eléctrica|
> |No conservativas|❌ No|Fricción, resistencia del aire|

> [!tip]- **Condiciones para Aplicar Conservación** 🎯
> 
> ### Requisitos Esenciales:
> 
> 1. **Solo fuerzas conservativas** actúan en el sistema
> 2. **Sistema aislado** (sin intercambio de energía externo)
> 3. **No hay fricción** o se desprecia
> 4. **Fuerzas internas** son conservativas
> 
> ### Casos Especiales:
> 
> - **Con fricción**: E_inicial = E_final + W_fricción
> - **Con fuerzas externas**: E_inicial + W_externo = E_final
> - **Sistemas con resortes**: Incluir E_p elástica
> - **Movimiento circular**: Considerar fuerza centrípeta

> [!warning]- **Tipos de Energía Potencial** 🏔️
> 
> ### Energía Potencial Gravitatoria:
> 
> - **Cerca de la superficie**: E_p = mgh
> - **Campo gravitatorio**: E_p = -GMm/r
> - **Referencia**: Nivel donde E_p = 0
> 
> ### Energía Potencial Elástica:
> 
> - **Resorte ideal**: E_p = ½kx²
> - **Deformación**: x medida desde posición natural
> - **Siempre positiva**: independiente del sentido

> [!success] 🔗 Estrategia de Resolución
> 
> ```mermaid
> graph TD
>     A[Identificar Sistema] --> B[Definir Estados Inicial y Final]
>     B --> C[Establecer Nivel de Referencia]
>     C --> D[Calcular Energías en Cada Estado]
>     D --> E[Aplicar Conservación: E₁ = E₂]
>     E --> F[Resolver para la Incógnita]
>     F --> G[Verificar Resultado Físicamente]
>     
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
>     style E fill:#fce4ec
>     style F fill:#fff8e1
>     style G fill:#f1f8e9
> ```

> [!note]- **Ecuaciones Fundamentales** 📐
> 
> ### Conservación General:
> 
> **½m₁v₁² + m₁gh₁ + ½k₁x₁² = ½m₂v₂² + m₂gh₂ + ½k₂x₂²**
> 
> ### Casos Particulares:
> 
> - **Caída libre**: mgh₁ = ½mv₂² + mgh₂
> - **Péndulo**: mgl(1-cosθ₁) = ½mv₂² + mgl(1-cosθ₂)
> - **Resorte**: ½kx₁² = ½mv₂² + ½kx₂²
> - **Montaña rusa**: ½mv₁² + mgh₁ = ½mv₂² + mgh₂

## 🎯 Estrategias de Resolución

> [!tip]- **Método CERES (Conservación-Estados-Referencia-Ecuación-Solución)** 🧠
> 
> ### **C**onservación - Verificar condiciones
> 
> 1. Identificar si solo actúan fuerzas conservativas
> 2. Determinar si el sistema está aislado
> 3. Verificar ausencia de fricción significativa
> 
> ### **E**stados - Definir inicial y final
> 
> 4. Estado inicial: posición, velocidad, deformación
> 5. Estado final: posición, velocidad, deformación
> 6. Identificar el momento de interés
> 
> ### **R**eferencia - Establecer niveles cero
> 
> 7. Elegir nivel de referencia para E_p gravitatoria
> 8. Definir posición natural para E_p elástica
> 9. Mantener consistencia en todo el problema
> 
> ### **E**cuación - Aplicar conservación
> 
> 10. E_inicial = E_final
> 11. Sustituir valores conocidos
> 12. Simplificar la ecuación
> 
> ### **S**olución - Resolver y verificar
> 
> 13. Despejar la incógnita
> 14. Verificar unidades y signo
> 15. Comprobar coherencia física

## 📚 Problemas Tipo

> [!example]- **Problema 1: Caída Libre desde Reposo** 🪂
> 
> ### Enunciado:
> 
> Una pelota se deja caer desde una altura de 20 m. Determina: a) La velocidad al llegar al suelo b) La velocidad cuando ha caído 15 m c) La altura cuando su velocidad es 10 m/s
> 
> ### Solución:
> 
> **Datos**: h₀ = 20 m, v₀ = 0 m/s, g = 9.8 m/s² **Referencia**: Suelo (h = 0)
> 
> **a) Velocidad al llegar al suelo**:
> 
> - Estado inicial: E₁ = mgh₀ = mg(20)
> - Estado final: E₂ = ½mv²
> - Conservación: mg(20) = ½mv²
> - **v = √(2gh₀) = √(2×9.8×20) = 19.8 m/s**
> 
> **b) Velocidad después de caer 15 m**:
> 
> - Altura actual: h = 20 - 15 = 5 m
> - mg(20) = ½mv² + mg(5)
> - **v = √(2g×15) = 17.1 m/s**
> 
> **c) Altura cuando v = 10 m/s**:
> 
> - mg(20) = ½m(10)² + mgh
> - 20g = 50 + gh
> - **h = (20g - 50)/g = 14.9 m**

> [!example]- **Problema 2: Péndulo Simple** 🕰️
> 
> ### Enunciado:
> 
> Un péndulo de 2 m de longitud se suelta desde un ángulo de 60° con la vertical. Encuentra: a) La velocidad en el punto más bajo b) El ángulo máximo si se le da velocidad inicial de 2 m/s
> 
> ### Solución:
> 
> **Datos**: L = 2 m, θ₀ = 60°, v₀ = 0 (parte a) **Referencia**: Punto más bajo del péndulo
> 
> **a) Velocidad en el punto más bajo**:
> 
> - Altura inicial: h₁ = L(1 - cos60°) = 2(1 - 0.5) = 1 m
> - Estado inicial: E₁ = mgh₁ = mg(1)
> - Estado final: E₂ = ½mv²
> - Conservación: mg(1) = ½mv²
> - **v = √(2g) = √(19.6) = 4.43 m/s**
> 
> **b) Con velocidad inicial de 2 m/s**:
> 
> - Estado inicial: E₁ = ½m(2)² + mg(1) = 2m + mg
> - Estado final: E₂ = mgh_máx = mgL(1 - cosθ_máx)
> - Conservación: 2 + g = gL(1 - cosθ_máx)
> - 2 + 9.8 = 9.8×2(1 - cosθ_máx)
> - cosθ_máx = 1 - 11.8/19.6 = 0.398
> - **θ_máx = 66.5°**

> [!example]- **Problema 3: Sistema Resorte-Masa** 🔗
> 
> ### Enunciado:
> 
> Una masa de 0.5 kg comprime un resorte (k = 200 N/m) una distancia de 0.3 m. Al soltarse, la masa se mueve sobre una superficie sin fricción y luego sube por una rampa de 30°. Determina la altura máxima alcanzada.
> 
> ### Solución:
> 
> **Datos**: m = 0.5 kg, k = 200 N/m, x = 0.3 m, θ = 30° **Referencia**: Nivel del resorte
> 
> **Estado inicial**: E₁ = ½kx² = ½(200)(0.3)² = 9 J **Estado final**: E₂ = mgh = 0.5×9.8×h = 4.9h J
> 
> **Conservación**: 9 = 4.9h **h = 9/4.9 = 1.84 m**
> 
> **Distancia sobre la rampa**: d = h/sin30° = 1.84/0.5 = 3.68 m

> [!example]- **Problema 4: Montaña Rusa** 🎢
> 
> ### Enunciado:
> 
> Un carrito de montaña rusa (m = 500 kg) parte del reposo desde una altura de 30 m. Si en el punto más bajo del recorrido alcanza una velocidad de 20 m/s, calcula: a) La energía perdida por fricción b) La altura máxima que alcanzaría sin fricción
> 
> ### Solución:
> 
> **Datos**: m = 500 kg, h₁ = 30 m, v₀ = 0, v₂ = 20 m/s **Referencia**: Punto más bajo
> 
> **a) Energía perdida por fricción**:
> 
> - E_inicial = mgh₁ = 500×9.8×30 = 147,000 J
> - E_final = ½mv₂² = ½×500×(20)² = 100,000 J
> - **E_perdida = 147,000 - 100,000 = 47,000 J**
> 
> **b) Altura máxima sin fricción**:
> 
> - Sin fricción: E_inicial = E_final
> - mgh₁ = ½mv_máx²
> - **v_máx = √(2gh₁) = √(2×9.8×30) = 24.2 m/s**
> - Esta sería la velocidad en el punto bajo, permitiendo volver a los 30 m

## 🧮 Técnicas de Memorización

> [!tip]- **Mnemotecnia: "GRAVE"** 📝
> 
> **G**ravitatoria - mgh para altura **R**esorte - ½kx² para deformación  
> **A**ltura - siempre respecto a referencia **V**elocidad - ½mv² para movimiento **E**nergía - se conserva sin fricción

> [!tip]- **Regla de los Estados** 🔄
> 
> - **Estado 1**: Donde conoces más datos
> - **Estado 2**: Donde está la incógnita
> - **Referencia**: Donde E_p = 0 (conveniente)
> - **Conservación**: E₁ = E₂ (sin pérdidas)

## ⚠️ Errores Comunes

> [!warning]- **Confusiones Frecuentes** ⚠️
> 
> 1. **Mal nivel de referencia**: Cambiar la referencia a mitad del problema
> 2. **Olvidar tipos de energía**: No considerar E_p elástica en problemas con resortes
> 3. **Signos incorrectos**: Velocidad siempre positiva en E_c, altura puede ser negativa
> 4. **Aplicar conservación con fricción**: Sin considerar trabajo de fuerzas no conservativas
> 5. **Confundir distancia con altura**: En planos inclinados usar la componente vertical
> 6. **No verificar condiciones iniciales**: Asumir reposo cuando puede haber velocidad inicial

## 🎯 Aplicaciones Prácticas

> [!info]- **Ejemplos del Mundo Real** 🌍
> 
> ### Ingeniería Civil:
> 
> - Diseño de montañas rusas y toboganes
> - Cálculo de alturas de presas hidroeléctricas
> - Análisis de caída de objetos en construcción
> 
> ### Deportes:
> 
> - Salto con pértiga y trampolín
> - Análisis de trayectorias en balística
> - Optimización en esquí y snowboard
> 
> ### Tecnología:
> 
> - Sistemas de almacenamiento de energía
> - Mecanismos de relojería
> - Diseño de amortiguadores y resortes
> 
> ### Astronomía:
> 
> - Órbitas planetarias y satelitales
> - Velocidades de escape
> - Transferencias orbitales

## 📖 Referencias

> [!quote]- **Notas Relacionadas**
> 
> - [[Trabajo y Energía]] - Fundamentos teóricos
> - [[Principios de Conservación de la Energía]] - Base conceptual
> - [[Diagramas de Energía]] - Representación gráfica
> - [[Potencia y Gradiente de Potencial]] - Aplicaciones avanzadas

## 📚 Notas Recomendadas

> [!note]- **Prerrequisitos**
> 
> - [[Cinemática Traslacional]] - Conceptos de velocidad y aceleración
> - [[Leyes de Newton]] - Fundamentos de fuerzas
> - [[Vectores]] - Manejo de magnitudes vectoriales
> - [[Unidades y Magnitudes Físicas]] - Sistema de unidades

---

**Tags:** #energia-mecanica #conservacion #trabajo-energia #fisica-mecanica #problemas #energia-cinetica #energia-potencial #pendulo #resorte #gravitacion