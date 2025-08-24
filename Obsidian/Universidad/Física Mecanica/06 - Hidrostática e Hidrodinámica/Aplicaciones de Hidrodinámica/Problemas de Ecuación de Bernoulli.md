# Problemas de Ecuación de Bernoulli

> [!quote] "La ecuación de Bernoulli revela que en el flujo de fluidos, energía y velocidad danzan en perfecto equilibrio: donde una crece, la otra decrece." ⚡

> [!info]- La ecuación de Bernoulli es la manifestación del principio de conservación de energía en fluidos en movimiento. Permite analizar la relación entre presión, velocidad y altura en sistemas de flujo, siendo fundamental para entender desde el vuelo de aviones hasta el funcionamiento de venturímetros.

## 🔧 Conceptos Fundamentales

> [!info]- **Ecuación de Bernoulli** ⚡
> 
> ### Forma General (por unidad de volumen):
> 
> **P + ½ρv² + ρgh = constante**
> 
> ### Formas Alternativas:
> 
> **Por unidad de masa**: P/ρ + ½v² + gh = constante
> 
> **En términos de altura**: P/(ρg) + v²/(2g) + h = H (altura total)
> 
> ### Interpretación de Términos:
> 
> |Término|Nombre|Significado Físico|Unidades|
> |---|---|---|---|
> |P|Presión estática|Energía por compresión|Pa = N/m²|
> |½ρv²|Presión dinámica|Energía cinética por volumen|Pa|
> |ρgh|Presión hidrostática|Energía potencial por volumen|Pa|
> 
> ### Condiciones de Validez:
> 
> - Flujo incompresible (ρ = constante)
> - Flujo no viscoso (sin fricción)
> - Flujo estacionario (∂/∂t = 0)
> - A lo largo de una línea de corriente

> [!tip]- **Aplicaciones de Bernoulli** 🌊
> 
> ### Sistemas Típicos:
> 
> **Tubería horizontal**: P₁ + ½ρv₁² = P₂ + ½ρv₂²
> 
> **Descarga libre**: P₁ + ½ρv₁² + ρgh₁ = P₀ + ½ρv₂²
> 
> **Venturímetro**: Medición de caudal por diferencia de presiones
> 
> **Tubo de Pitot**: Medición de velocidad
> 
> ### Efectos Observables:
> 
> - **Efecto Venturi**: ↓Área → ↑Velocidad → ↓Presión
> - **Sustentación**: Diferencia de velocidades genera fuerza
> - **Cavitación**: Presión local cae por debajo de vapor

> [!warning]- **Limitaciones y Consideraciones** ⚠️
> 
> ### Cuándo NO aplicar Bernoulli:
> 
> - Flujo con viscosidad significativa
> - Flujo compresible (M > 0.3)
> - Flujo no estacionario
> - Presencia de bombas o turbinas
> - Grandes pérdidas por fricción
> 
> ### Correcciones Necesarias:
> 
> - **Pérdidas por fricción**: H_pérdidas
> - **Trabajo de bombas**: H_bomba
> - **Coeficientes de descarga**: C_d para orificios
> - **Factor de corrección de energía cinética**: α

> [!success] 🔗 Metodología de Aplicación
> 
> ```mermaid
> graph TD
>     A[Verificar Condiciones de Validez] --> B[Seleccionar Puntos de Referencia]
>     B --> C[Definir Plano de Referencia]
>     C --> D[Aplicar Ecuación de Bernoulli]
>     D --> E[Combinar con Continuidad]
>     E --> F[Resolver Sistema de Ecuaciones]
>     F --> G[Verificar Coherencia Física]
>     
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
>     style E fill:#fce4ec
>     style F fill:#f1f8e9
>     style G fill:#ffebee
> ```

> [!note]- **Fórmulas Específicas** 📐
> 
> ### Velocidad de Descarga (Torricelli):
> 
> **v = √(2gh)** (descarga libre desde altura h)
> 
> ### Caudal por Orificio:
> 
> **Q = C_d × A × √(2gh)** donde C_d ≈ 0.6 para orificio circular
> 
> ### Venturímetro:
> 
> **v₁ = √[2(P₁-P₂)/(ρ(1-(A₁/A₂)²))]**
> 
> ### Tubo de Pitot:
> 
> **v = √(2ΔP/ρ)** donde ΔP = P_estancamiento - P_estática

## 🎯 Estrategias de Resolución

> [!tip]- **Método PEACE (Puntos-Energía-Aplicar-Continuidad-Evaluar)** 🧠
> 
> ### **P**untos - Selecciona ubicaciones estratégicas
> 
> 1. Identifica puntos donde conoces o necesitas información
> 2. Elige puntos en la misma línea de corriente
> 3. Prefiere superficies libres, estancamientos o secciones conocidas
> 
> ### **E**nergía - Define el plano de referencia
> 
> 4. Establece un nivel de referencia para h
> 5. Determina alturas relativas de cada punto
> 6. Identifica energías conocidas en cada punto
> 
> ### **A**plicar - Escribe la ecuación de Bernoulli
> 
> 7. Aplica P₁ + ½ρv₁² + ρgh₁ = P₂ + ½ρv₂² + ρgh₂
> 8. Sustituye valores conocidos
> 9. Identifica incógnitas restantes
> 
> ### **C**ontinuidad - Relaciona velocidades y áreas
> 
> 10. Usa A₁v₁ = A₂v₂ cuando sea necesario
> 11. Relaciona variables cinemáticas
> 12. Sustituye relaciones en Bernoulli
> 
> ### **E**valuar - Resuelve y verifica
> 
> 13. Resuelve el sistema de ecuaciones
> 14. Verifica unidades y signos
> 15. Comprueba coherencia física del resultado

## 📚 Problemas Tipo

> [!example]- **Problema 1: Descarga por Orificio (Torricelli)** 💧
> 
> ### Enunciado:
> 
> Un tanque grande contiene agua hasta una altura de 4 m. En el fondo tiene un orificio circular de 5 cm de diámetro. Calcula: a) La velocidad de salida del agua b) El caudal de descarga c) El tiempo para vaciar el tanque si tiene base cuadrada de 2m × 2m
> 
> ### Datos:
> 
> - Altura del agua: h = 4 m
> - Diámetro del orificio: d = 5 cm = 0.05 m
> - Tanque: base 2m × 2m
> - Coeficiente de descarga: C_d = 0.6
> 
> ### Solución:
> 
> **Selección de puntos:**
> 
> - Punto 1: Superficie libre del tanque
> - Punto 2: Salida del orificio
> 
> **a) Velocidad de salida:**
> 
> Aplicando Bernoulli (tomando el orificio como referencia, h₂ = 0):
> 
> - P₁ = P₂ = P_atm (ambos expuestos a la atmósfera)
> - v₁ ≈ 0 (tanque grande, A₁ >> A₂)
> - h₁ = 4 m, h₂ = 0
> 
> **P_atm + 0 + ρg(4) = P_atm + ½ρv₂² + 0**
> 
> **v₂ = √(2gh) = √(2 × 9.8 × 4) = 8.85 m/s**
> 
> **b) Caudal real:**
> 
> - Área del orificio: A = π(0.025)² = 1.96 × 10⁻³ m²
> - **Q = C_d × A × v₂ = 0.6 × 1.96 × 10⁻³ × 8.85 = 0.0104 m³/s = 10.4 L/s**
> 
> **c) Tiempo de vaciado:**
> 
> - Volumen inicial: V₀ = 2² × 4 = 16 m³
> - **t = V₀/Q = 16/0.0104 = 1,538 s ≈ 25.6 minutos**
> 
> _(Nota: Este es aproximado, ya que la velocidad disminuye conforme baja el nivel)_

> [!example]- **Problema 2: Venturímetro** 🌪️
> 
> ### Enunciado:
> 
> Un venturímetro tiene una sección de entrada de 20 cm de diámetro y una garganta de 10 cm de diámetro. Transporta agua y se mide una diferencia de presión de 35 kPa entre la entrada y la garganta. Calcula: a) La velocidad en ambas secciones b) El caudal
> 
> ### Datos:
> 
> - D₁ = 20 cm = 0.20 m (entrada)
> - D₂ = 10 cm = 0.10 m (garganta)
> - ΔP = P₁ - P₂ = 35 kPa = 35,000 Pa
> - Fluido: agua (ρ = 1000 kg/m³)
> - Venturímetro horizontal (h₁ = h₂)
> 
> ### Solución:
> 
> **Áreas transversales:**
> 
> - A₁ = π(0.10)² = 0.0314 m²
> - A₂ = π(0.05)² = 0.00785 m²
> 
> **Por continuidad:**
> 
> - A₁v₁ = A₂v₂ → v₂ = v₁(A₁/A₂) = v₁(0.0314/0.00785) = 4v₁
> 
> **Por Bernoulli (horizontal):**
> 
> - P₁ + ½ρv₁² = P₂ + ½ρv₂²
> - P₁ - P₂ = ½ρ(v₂² - v₁²) = ½ρ((4v₁)² - v₁²) = ½ρ(15v₁²)
> 
> **Resolviendo para v₁:**
> 
> - 35,000 = ½ × 1000 × 15v₁²
> - v₁² = 35,000/(7,500) = 4.67
> - **v₁ = 2.16 m/s**
> - **v₂ = 4 × 2.16 = 8.64 m/s**
> 
> **b) Caudal:**
> 
> - **Q = A₁v₁ = 0.0314 × 2.16 = 0.0678 m³/s = 67.8 L/s**

> [!example]- **Problema 3: Sifón** 🏔️
> 
> ### Enunciado:
> 
> Un sifón evacua agua de un tanque. El punto más alto del sifón está 2 m por encima del nivel del agua y 5 m por encima del nivel de descarga. El diámetro del tubo es constante de 3 cm. Calcula: a) La velocidad de descarga b) La presión en el punto más alto c) ¿Habrá cavitación si P_vapor = 2.3 kPa?
> 
> ### Datos:
> 
> - Altura del punto alto sobre el agua: h₁ = 2 m
> - Altura total de descarga: h_total = 5 m
> - Diámetro constante: d = 3 cm
> - P_vapor = 2.3 kPa
> - P_atm = 101.3 kPa
> 
> ### Solución:
> 
> **Selección de puntos:**
> 
> - Punto 1: Superficie del tanque
> - Punto 2: Punto más alto del sifón
> - Punto 3: Descarga libre
> 
> **a) Velocidad de descarga (1→3):**
> 
> Por Bernoulli (tomando descarga como referencia):
> 
> - P₁ = P₃ = P_atm, v₁ ≈ 0, h₁ = 5 m, h₃ = 0
> 
> **P_atm + 0 + ρg(5) = P_atm + ½ρv₃² + 0**
> 
> **v₃ = √(2gh_total) = √(2 × 9.8 × 5) = 9.90 m/s**
> 
> **b) Presión en el punto alto (1→2):**
> 
> Como el diámetro es constante: v₂ = v₃ = 9.90 m/s
> 
> **P_atm + 0 + ρg(0) = P₂ + ½ρv₂² + ρg(2)**
> 
> **P₂ = P_atm - ½ρv₂² - ρg(2)**
> 
> P₂ = 101,300 - ½(1000)(9.90)² - (1000)(9.8)(2) P₂ = 101,300 - 49,005 - 19,600 = **32,695 Pa = 32.7 kPa**
> 
> **c) Cavitación:**
> 
> Como P₂ = 32.7 kPa > P_vapor = 2.3 kPa
> 
> **No habrá cavitación** (el margen de seguridad es amplio)

## 🧮 Técnicas de Memorización

> [!tip]- **Mnemotecnia: "VELOZ"** 🏃‍♂️
> 
> **V**elocidad alta → **E**nergía cinética alta → presión **L**ow **V**elocidad **O**baja → energía cinética low → presión high **Z**
> 
> **Regla de Intercambio**: Presión ↔ Velocidad (inversamente proporcionales)

> [!tip]- **Analogía del Tobogán** 🎢
> 
> - **Arriba del tobogán**: Energía potencial alta, velocidad baja
> - **Abajo del tobogán**: Energía potencial baja, velocidad alta
> - **Energía total**: Siempre se conserva (sin fricción)

## ⚠️ Errores Comunes

> [!warning]- **Confusiones Frecuentes** ⚠️
> 
> 1. **Olvidar las condiciones de validez**: Aplicar Bernoulli cuando hay viscosidad significativa
> 2. **Plano de referencia inconsistente**: Cambiar la referencia entre puntos
> 3. **Presión manométrica vs absoluta**: No especificar qué tipo se usa
> 4. **Velocidad en tanques grandes**: Asumir v = 0 cuando A_tanque no >> A_salida
> 5. **Signos en diferencias de altura**: Confundir h₁ - h₂ con h₂ - h₁
> 6. **Unidades inconsistentes**: Mezclar Pa, kPa, mmHg sin conversión
> 7. **Ignorar pérdidas reales**: Usar Bernoulli ideal cuando hay fricción significativa

## 🎯 Aplicaciones Prácticas

> [!info]- **Ejemplos del Mundo Real** 🌍
> 
> ### Aeronáutica:
> 
> - Sustentación de alas (diferencia de velocidades)
> - Tubos de Pitot para medir velocidad de vuelo
> - Diseño de toberas de propulsión
> 
> ### Ingeniería Hidráulica:
> 
> - Diseño de vertederos y compuertas
> - Sistemas de sifón para drenaje
> - Medidores de caudal tipo Venturi
> 
> ### Industria:
> 
> - Eyectores y bombas de chorro
> - Carburadores en motores de combustión
> - Aspersores y sistemas de rociado
> 
> ### Medicina:
> 
> - Angioplastia (estrechamiento de arterias)
> - Nebulizadores y inhaladores
> - Sistemas de aspiración quirúrgica
> 
> ### Deportes:
> 
> - Efecto Magnus en pelotas curvas
> - Diseño de cascos aerodinámicos
> - Velas de barcos y análisis del viento

## 📖 Referencias

> [!quote]- **Notas Relacionadas**
> 
> - [[Problemas de Ecuación de Continuidad]] - Conservación de masa
> - [[Ecuación de Continuidad y Bernoulli]] - Teoría fundamental
> - [[Presión y Densidad]] - Propiedades básicas
> - [[Flujo Laminar y Ecuación de Poiseuille]] - Efectos de viscosidad
> - **Próximo tema**: [[Problemas de Flujo con Viscosidad]]

## 📚 Notas Recomendadas

> [!note]- **Prerrequisitos**
> 
> - [[Trabajo y Energía]] - Conservación de energía
> - [[Problemas de Ecuación de Continuidad]] - Conservación de masa
> - **Matemáticas**: Álgebra, resolución de sistemas de ecuaciones
> 
> ### **Conocimientos Previos**:
> 
> - Energía cinética y potencial
> - Presión hidrostática
> - Flujo incompresible e invíscido

> [!note]- **Aplicaciones Avanzadas**
> 
> - **Mecánica de Fluidos Computacional (CFD)**
> - **Análisis de turbomaquinaria**
> - **Diseño aerodinámico**
> - **Hidráulica de canales abiertos**

---

**Tags:** #hidrodinamica #bernoulli #conservacion-energia #presion #velocidad #venturi #torricelli #sifon #cavitacion #fisica-mecanica #problemas #aerodinamica #sustentacion

# Problemas del Teorema de Torricelli

>[!quote] "El agua encuentra su velocidad perfecta al escapar: Torricelli nos enseñó que la naturaleza convierte la altura en movimiento con la precisión de una ecuación matemática." 💧

> [!info]- El Teorema de Torricelli, formulado por Evangelista Torricelli en 1643, describe la velocidad de salida de un fluido a través de un orificio en un recipiente bajo la influencia de la gravedad. Este principio fundamental de la hidrodinámica es una aplicación directa del principio de Bernoulli y tiene innumerables aplicaciones en ingeniería y la vida cotidiana.

## 🌊 Fundamentos Teóricos

> [!info]- **Teorema de Torricelli Básico** 💫
> 
> ### Formulación Fundamental:
> 
> **v = √(2gh)**
> 
> - **v**: Velocidad de salida del fluido (m/s)
> - **g**: Aceleración gravitacional (9.81 m/s²)
> - **h**: Altura del líquido sobre el orificio (m)
> 
> ### Deducción desde Bernoulli:
> 
> **Punto 1 (superficie)**: P₁ + ½ρv₁² + ρgh₁ = constante
> **Punto 2 (orificio)**: P₂ + ½ρv₂² + ρgh₂ = constante
> 
> **Condiciones**:
> - P₁ = P₂ = P_atm (ambos expuestos al aire)
> - v₁ ≈ 0 (área superficie >> área orificio)
> - h = h₁ - h₂ (diferencia de alturas)
> 
> **Resultado**: v₂ = √(2gh)
> 
> ### Interpretación Física:
> |Parámetro|Significado Físico|Observaciones|
> |---|---|---|
> |Energía potencial|ρgh|Se convierte en cinética|
> |Energía cinética|½ρv²|Máxima en el orificio|
> |Velocidad teórica|√(2gh)|Sin fricción ni viscosidad|
> |Equivalencia|v = √(2gh) = gt_caída|Velocidad de caída libre|

> [!tip]- **Factores de Corrección Real** 🔧
> 
> ### Coeficiente de Velocidad (Cv):
> 
> **v_real = Cv × √(2gh)**
> 
> - **Cv**: Coeficiente de velocidad (0.95-0.99)
> - Considera pérdidas por fricción y viscosidad
> - Depende de Re (número de Reynolds)
> 
> ### Coeficiente de Contracción (Cc):
> 
> **A_efectiva = Cc × A_orificio**
> 
> - **Cc**: Coeficiente de contracción (0.6-0.65)
> - **Vena contracta**: Sección mínima del chorro
> - Depende de la geometría del orificio
> 
> ### Coeficiente de Descarga (Cd):
> 
> **Q_real = Cd × A × √(2gh)**
> 
> **Cd = Cv × Cc** (típicamente 0.6-0.65)
> 
> ### Factores que Afectan los Coeficientes:
> - **Forma del orificio**: Circular, rectangular, triangular
> - **Espesor de pared**: Delgada vs gruesa
> - **Acabado superficial**: Rugosidad del borde
> - **Número de Reynolds**: Régimen de flujo

> [!warning]- **Variaciones del Teorema** 🔄
> 
> ### Torricelli con Presión Adicional:
> 
> **v = √(2gh + 2ΔP/ρ)**
> 
> - **ΔP**: Diferencia de presión adicional
> - **ρ**: Densidad del fluido
> - Ejemplo: Tanques presurizados
> 
> ### Orificio Sumergido:
> 
> **v = √(2g(h₁ - h₂))**
> 
> - **h₁**: Altura del fluido superior
> - **h₂**: Altura del fluido inferior
> - Aplicación: Desagües sumergidos
> 
> ### Flujo a Través de Pared Inclinada:
> 
> **v = √(2gh_efectiva)**
> 
> - **h_efectiva = h × cos²(α)**
> - **α**: Ángulo de inclinación de la pared

>[!success] 🔗 Aplicaciones del Teorema de Torricelli
> 
> ```mermaid
> graph TD
>     A[Teorema de Torricelli] --> B[Vaciado de Tanques]
>     A --> C[Sistemas de Riego]
>     A --> D[Medición de Flujo]
>     A --> E[Fuentes Ornamentales]
>     
>     B --> F[Tiempo de vaciado]
>     B --> G[Velocidad variable]
>     
>     C --> H[Aspersores]
>     C --> I[Goteo controlado]
>     
>     D --> J[Orificios calibrados]
>     D --> K[Aforadores]
>     
>     E --> L[Altura del chorro]
>     E --> M[Alcance horizontal]
>     
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
>     style E fill:#fce4ec
> ```

> [!note]- **Ecuaciones Derivadas Importantes** 📊
> 
> ### Tiempo de Vaciado:
> 
> **Para tanque cilíndrico con orificio en el fondo**:
> 
> **t = (2A_tanque/A_orificio) × √(h₀/2g)**
> 
> - **A_tanque**: Área de la sección transversal del tanque
> - **A_orificio**: Área del orificio de salida
> - **h₀**: Altura inicial del líquido
> 
> ### Alcance Horizontal (Proyectil):
> 
> **x = √(4h_orificio × h_líquido)**
> 
> - **h_orificio**: Altura del orificio sobre el suelo
> - **h_líquido**: Altura del líquido sobre el orificio
> 
> ### Caudal Instantáneo:
> 
> **Q(t) = Cd × A × √(2gh(t))**
> 
> - **h(t)**: Altura variable con el tiempo
> - Para vaciado: h(t) = h₀ - f(Q,t)

## 🎯 Estrategias de Resolución

> [!tip]- **Método TORRE (Tanque-Orificio-Referencia-Régimen-Evaluación)** 🧠
> 
> ### **T**anque - Geometría del recipiente
> 
> 1. Identifica forma del tanque (cilíndrico, cónico, prismático)
> 2. Determina dimensiones (área transversal, altura)
> 3. Localiza nivel inicial del líquido
> 4. Considera efectos de forma en el vaciado
> 
> ### **O**rificio - Características de salida
> 
> 5. Define geometría del orificio (circular, rectangular)
> 6. Determina área efectiva de salida
> 7. Evalúa coeficientes de corrección (Cd, Cv, Cc)
> 8. Considera ubicación (lateral, fondo, múltiples)
> 
> ### **R**eferencia - Sistema de coordenadas
> 
> 9. Establece nivel de referencia (altura = 0)
> 10. Mide altura del líquido desde el orificio
> 11. Considera presiones adicionales
> 12. Define dirección positiva de velocidades
> 
> ### **R**égimen - Tipo de flujo
> 
> 13. Evalúa si es flujo permanente o transitorio
> 14. Calcula número de Reynolds (si es necesario)
> 15. Determina si aplica Torricelli ideal
> 16. Considera efectos viscosos
> 
> ### **E**valuación - Cálculo y verificación
> 
> 17. Aplica v = √(2gh) o variaciones
> 18. Calcula caudales y tiempos
> 19. Verifica coherencia física de resultados
> 20. Interpreta en contexto del problema

## 📚 Problemas Tipo

> [!example]- **Problema 1: Vaciado de Tanque Cilíndrico** 🛢️
> 
> ### Enunciado:
> 
> Un tanque cilíndrico vertical de 2 m de diámetro contiene agua hasta una altura de 3 m. En el fondo tiene un orificio circular de 5 cm de diámetro con Cd = 0.62. Determina: a) La velocidad inicial de salida b) El caudal inicial c) El tiempo total de vaciado
> 
> ### Solución:
> 
> **Datos dados**:
> - D_tanque = 2 m → A_tanque = π(1)² = 3.14 m²
> - h₀ = 3 m
> - d_orificio = 5 cm → A_orificio = π(0.025)² = 1.96×10⁻³ m²
> - Cd = 0.62
> 
> **a) Velocidad inicial de salida**:
> - v₀ = √(2gh₀) = √(2 × 9.81 × 3) = 7.67 m/s
> 
> **b) Caudal inicial**:
> - Q₀ = Cd × A_orificio × v₀ = 0.62 × 1.96×10⁻³ × 7.67 = 9.32×10⁻³ m³/s
> - Q₀ = 9.32 L/s
> 
> **c) Tiempo total de vaciado**:
> - t = (2A_tanque)/(Cd × A_orificio) × √(h₀/(2g))
> - t = (2 × 3.14)/(0.62 × 1.96×10⁻³) × √(3/(2×9.81))
> - t = 5164 × 0.392 = 2024 segundos = 33.7 minutos

> [!example]- **Problema 2: Alcance de Chorro Horizontal** 🎯
> 
> ### Enunciado:
> 
> Un tanque de agua tiene un orificio lateral a 1.5 m de altura sobre el suelo. El nivel del agua está 2 m por encima del orificio. Determina: a) La velocidad de salida b) El tiempo de vuelo c) El alcance horizontal máximo d) La altura máxima del chorro si sale a 30° sobre la horizontal
> 
> ### Solución:
> 
> **Datos**:
> - h_líquido = 2 m (altura sobre orificio)
> - h_orificio = 1.5 m (altura sobre suelo)
> - α = 30° (para inciso d)
> 
> **a) Velocidad de salida**:
> - v = √(2gh_líquido) = √(2 × 9.81 × 2) = 6.26 m/s
> 
> **b) Tiempo de vuelo** (movimiento parabólico):
> - h_orificio = ½gt² → t = √(2h_orificio/g) = √(2×1.5/9.81) = 0.553 s
> 
> **c) Alcance horizontal**:
> - x = v × t = 6.26 × 0.553 = 3.46 m
> - Fórmula directa: x = √(4h_orificio × h_líquido) = √(4×1.5×2) = 3.46 m ✓
> 
> **d) Altura máxima con ángulo 30°**:
> - vᵧ = v × sen(30°) = 6.26 × 0.5 = 3.13 m/s
> - h_max = vᵧ²/(2g) = (3.13)²/(2×9.81) = 0.5 m sobre el orificio
> - Altura total sobre suelo: 1.5 + 0.5 = 2 m

> [!example]- **Problema 3: Vaciado de Tanque Cónico** 🔺
> 
> ### Enunciado:
> 
> Un tanque cónico invertido (vértice hacia abajo) tiene 4 m de altura y 3 m de radio en la parte superior. Contiene agua hasta 3 m de altura. Un orificio de 8 cm de diámetro en el vértice permite el vaciado. Si Cd = 0.6, determina: a) El caudal inicial b) La función h(t) c) El tiempo para reducir el nivel a 1 m
> 
> ### Solución:
> 
> **Datos**:
> - H_tanque = 4 m, R_superior = 3 m
> - h₀ = 3 m, d_orificio = 8 cm
> - A_orificio = π(0.04)² = 5.03×10⁻³ m²
> - Cd = 0.6
> 
> **Relación geométrica del cono**:
> - r(h)/h = R/H = 3/4 → r(h) = 0.75h
> - A(h) = π[r(h)]² = π(0.75h)² = 1.767h² m²
> 
> **a) Caudal inicial**:
> - v₀ = √(2gh₀) = √(2×9.81×3) = 7.67 m/s
> - Q₀ = Cd × A_orificio × v₀ = 0.6 × 5.03×10⁻³ × 7.67 = 2.32×10⁻² m³/s
> 
> **b) Función h(t)**:
> - Ecuación diferencial: A(h)dh/dt = -Q(h)
> - 1.767h² × dh/dt = -Cd × A_orificio × √(2gh)
> - 1.767h² × dh/dt = -0.6 × 5.03×10⁻³ × √(2×9.81×h)
> - Separando variables e integrando: h^(3/2) = h₀^(3/2) - (3k/2)t
> - donde k = (Cd × A_orificio × √(2g))/1.767
> 
> **c) Tiempo para h = 1 m**:
> - k = (0.6 × 5.03×10⁻³ × √(19.62))/1.767 = 9.56×10⁻³
> - 1^(3/2) = 3^(3/2) - (3×9.56×10⁻³/2)t
> - 1 = 5.196 - 0.01434t
> - t = (5.196-1)/0.01434 = 293 segundos = 4.88 minutos

## 🧮 Técnicas de Memorización

> [!tip]- **Mnemotecnia: "TORRE"** 🗼
> 
> **T**orricelli usa raíz de **T**wo g h (√(2gh))
> **O**rificio da velocidad según altura (**O**utlet velocity)
> **R**aíz cuadrada de altura (**R**oot of height)
> **R**elación con caída libre (**R**elation to free fall)
> **E**nergía potencial a cinética (**E**nergy conversion)

> [!info]- **Reglas Nemotécnicas Adicionales** 🎯
> 
> ### "AGUA-CAE": **AGUA** **CAE** con velocidad de Torricelli
> - **A**ltura determina velocidad
> - **G**ravedad acelera el flujo  
> - **U**niforme en orificio pequeño
> - **A**plicable solo en caída libre
> - **C**audal proporcional a √h
> - **A**rea del orificio multiplicada
> - **E**cuivalente a proyectil en caída
> 
> ### "DOS-GE-H": **DOS** veces **GE** por **H** bajo raíz
> - **2** × **g** × **h** dentro de la raíz cuadrada
> - Fácil de recordar para exámenes
> 
> ### "CD-REAL": **CD** para caudal **REAL**
> - **C**oeficiente **D**escarga corrige teoría
> - **R**eal siempre menor que ideal
> - **E**cuación: Q_real = Cd × Q_teórico
> - **A**justable según geometría
> - **L**ímites típicos: 0.6-0.65

## ⚠️ Errores Comunes

> [!warning]- **Confusiones Frecuentes** ⚠️
> 
> 1. **Confundir altura total con altura sobre orificio**: h ≠ h_total
> 2. **Olvidar coeficientes de corrección**: v_real ≠ v_teórica
> 3. **Asumir área constante**: En tanques no cilíndricos A = A(h)
> 4. **Ignorar la vena contracta**: A_efectiva < A_orificio
> 5. **Mal aplicar en flujo no libre**: Torricelli solo para descarga libre
> 6. **Confundir con tuberías**: No aplicable en flujo confinado
> 7. **Usar altura incorrecta en inclinados**: Proyección vertical
> 8. **Despreciar efectos dinámicos**: En orificios grandes o flujo turbulento

## 🎯 Aplicaciones Prácticas

> [!info]- **Ejemplos del Mundo Real** 🌍
> 
> ### Sistemas de Drenaje:
> 
> - Desagües de edificios y casas
> - Sistemas pluviales urbanos
> - Drenaje de estacionamientos
> - Canales de evacuación
> 
> ### Industria y Procesamiento:
> 
> - Vaciado de silos y tolvas
> - Sistemas de dosificación
> - Llenado y vaciado de reactores
> - Control de inventarios líquidos
> 
> ### Agricultura e Irrigación:
> 
> - Sistemas de riego por goteo
> - Aspersores y nebulizadores
> - Drenaje de campos cultivados
> - Sistemas de fertirrigación
> 
> ### Ingeniería Hidráulica:
> 
> - Diseño de vertederos
> - Sistemas de alivio en presas
> - Canales de descarga
> - Aforadores y medidores de flujo
> 
> ### Aplicaciones Domésticas:
> 
> - Funcionamiento de inodoros
> - Sistemas de limpieza por presión
> - Fuentes decorativas
> - Mangueras de jardín

## 📈 Casos Especiales

> [!note]- **Situaciones Complejas** 🔬
> 
> ### Múltiples Orificios:
> - **En serie**: Diferentes alturas
> - **En paralelo**: Mismo nivel
> - **Distribución**: Caudal total = Σ caudales individuales
> - **Interferencia**: Efectos de proximidad
> 
> ### Tanques de Forma Irregular:
> - **Función A(h)**: Área variable con altura
> - **Integración numérica**: Para formas complejas
> - **Aproximaciones**: Por tramos lineales
> - **Tanques horizontales**: Geometría cilíndrica horizontal
> 
> ### Efectos de Temperatura:
> - **Viscosidad variable**: μ = μ(T)
> - **Densidad variable**: ρ = ρ(T)
> - **Expansión térmica**: Cambio de dimensiones
> - **Convección natural**: Movimientos internos
> 
> ### Fluidos No Newtonianos:
> - **Modificación de coeficientes**: Cd = Cd(fluido)
> - **Comportamiento reológico**: Viscosidad aparente
> - **Efectos tixotrópicos**: Dependencia temporal
> - **Fluidos con partículas**: Suspensiones y lodos

## 🔬 Extensiones y Aplicaciones Avanzadas

> [!tip]- **Desarrollos Modernos** 🚀
> 
> ### Microfluídica:
> - Dispositivos lab-on-chip
> - Control de microgotas
> - Torricelli a escala microscópica
> 
> ### Simulación Computacional:
> - CFD (Computational Fluid Dynamics)
> - Modelos multifásicos
> - Análisis de turbulencia
> 
> ### Aplicaciones Espaciales:
> - Propulsión por microgravedad
> - Sistemas de combustible en satélites
> - Fluidos en condiciones extremas
> 
> ### Biomecánica:
> - Flujo sanguíneo en arterias
> - Mecánica respiratoria
> - Sistemas de drenaje corporal

## 📖 Referencias

> [!quote]- **Notas Relacionadas**
> 
> - [[Ecuación de Continuidad y Bernoulli]] - Base teórica fundamental
> - [[Presión y Densidad]] - Conceptos previos necesarios
> - [[Aplicaciones de Hidrodinámica]] - Contexto general
> - [[Fundamentos de Hidrostática e Hidrodinámica]] - Principios básicos

## 📚 Notas Recomendadas

> [!note]- **Prerrequisitos**
> 
> - [[Vectores]] - Para análisis de trayectorias
> - [[Unidades y Magnitudes Físicas]] - Consistencia dimensional
> - [[Conocimientos Previos a las Prácticas]] - Fundamentos matemáticos
> - [[Ecuaciones de Movimiento]] - Para movimiento parabólico del chorro

---

**Tags:** #hidrodinamica #teorema-torricelli #vaciado-tanques #velocidad-salida #caudal #orificio #bernoulli #flujo-libre #coeficiente-descarga #aplicaciones-hidraulicas #ingenieria-hidraulica