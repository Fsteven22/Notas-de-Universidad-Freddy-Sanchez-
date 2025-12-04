# Problemas de Velocidad Final usando Impulso

> [!quote] "El impulso es el mensajero del cambio; en cada golpe, en cada empujón, porta consigo la promesa de una nueva velocidad." 🚀

> [!info]- El impulso representa el efecto acumulativo de una fuerza actuando durante un tiempo determinado, resultando en un cambio de momentum. Esta aproximación es especialmente útil cuando conocemos las fuerzas y el tiempo de aplicación, pero no necesariamente los detalles del movimiento intermedio.

## ⚡ Fundamentos del Impulso y Momentum

> [!info]- **Definiciones Fundamentales** 🎯
> 
> ### Momentum Lineal:
> 
> **p⃗ = mv⃗** (kilogramo-metro por segundo, kg⋅m/s)
> 
> ### Impulso:
> 
> **J⃗ = ∫F⃗ dt = Δp⃗** (Newton-segundo, N⋅s)
> 
> ### Teorema Impulso-Momentum:
> 
> **J⃗ = Δp⃗ = p⃗f - p⃗i = m(v⃗f - v⃗i)**
> 
> ### Características del Impulso:
> 
> |Aspecto|Descripción|Unidades|
> |---|---|---|
> |Magnitud vectorial|Tiene dirección y sentido|N⋅s = kg⋅m/s|
> |Área bajo curva|J = ∫F dt en gráfico F-t|N⋅s|
> |Efecto acumulativo|Suma de todos los impulsos|kg⋅m/s|
> |Cambio instantáneo|Δp en tiempo infinitesimal|kg⋅m/s|

> [!tip]- **Tipos de Impulso** 🔨
> 
> ### 1. Impulso de Fuerza Constante:
> 
> **J = F⃗ × Δt** (cuando F es constante)
> 
> ### 2. Impulso de Fuerza Variable:
> 
> **J = ∫t₁ᵗ² F⃗(t) dt** (integración necesaria)
> 
> ### 3. Impulso Promedio:
> 
> **F̄ = J/Δt** (fuerza promedio equivalente)
> 
> ### 4. Impulso en Colisiones:
> 
> - **Elásticas**: Se conservan momentum y energía cinética
> - **Inelásticas**: Solo se conserva momentum
> - **Perfectamente inelásticas**: Los objetos se pegan

> [!warning]- **Conservación del Momentum** ⚖️
> 
> ### Principio Fundamental:
> 
> **Σp⃗inicial = Σp⃗final** (en ausencia de fuerzas externas)
> 
> ### Condiciones de Aplicación:
> 
> 1. **Sistema aislado** o fuerzas externas despreciables
> 2. **Fuerzas internas** pueden ser grandes (colisiones)
> 3. **Tiempo corto** donde fuerzas externas no tienen efecto significativo
> 
> ### Aplicaciones Típicas:
> 
> - Colisiones entre vehículos
> - Explosiones y fragmentaciones
> - Propulsión a reacción
> - Interacciones subatómicas

> [!success] 🔗 Estrategia General
> 
> ```mermaid
> graph TD
>     A[Problema de Velocidad Final] --> B[Tipo de Análisis]
>     B --> C[Impulso Directo]
>     B --> D[Conservación Momentum]
>     B --> E[Combinado]
>     
>     C --> C1[J = FΔt]
>     C --> C2[J = ∫F dt]
>     C --> C3[J = Δp]
>     
>     D --> D1[Sistema Aislado]
>     D --> D2[Colisiones]
>     D --> D3[Explosiones]
>     
>     E --> E1[Múltiples Fuerzas]
>     E --> E2[Sistemas Complejos]
>     E --> E3[Análisis por Etapas]
>     
>     style A fill:#e1f5fe
>     style C fill:#f3e5f5
>     style D fill:#fff3e0
>     style E fill:#e8f5e8
> ```

## 🧮 Cálculo de Impulso

> [!info]- **Métodos de Cálculo del Impulso** 📊
> 
> ### 1. Fuerza Constante:
> 
> **J = F⃗ × Δt**
> 
> - **Aplicación**: Cuando F no cambia durante Δt
> - **Ejemplo**: Empuje de cohete con fuerza constante
> - **Ventaja**: Cálculo directo y simple
> 
> ### 2. Fuerza Variable - Función Conocida:
> 
> **J = ∫t₁ᵗ² F(t) dt**
> 
> - **Aplicación**: Cuando conocemos F(t) analíticamente
> - **Ejemplo**: F(t) = F₀e^(-t/τ) (fuerza exponencial)
> - **Método**: Integración analítica
> 
> ### 3. Fuerza Variable - Datos Experimentales:
> 
> **J ≈ Σ F̄ᵢ × Δtᵢ** (suma de Riemann)
> 
> - **Aplicación**: Datos discretos de F vs t
> - **Ejemplo**: Mediciones de sensores durante impacto
> - **Método**: Integración numérica
> 
> ### 4. Área bajo Curva F-t:
> 
> **J = Área bajo gráfico F vs t**
> 
> - **Aplicación**: Análisis gráfico
> - **Método**: Conteo de cuadrículas, regla del trapecio
> - **Ventaja**: Visualización clara del impulso

> [!tip]- **Técnicas de Integración para Impulso** 🔢
> 
> ### Funciones Comunes:
> 
> |Función F(t)|Integral ∫F(t)dt|Aplicación|
> |---|---|---|
> |F₀ (constante)|F₀t|Fuerzas uniformes|
> |F₀t|½F₀t²|Fuerzas linealmente crecientes|
> |F₀e^(-t/τ)|F₀τ(1-e^(-t/τ))|Decaimiento exponencial|
> |F₀ sen(ωt)|-(F₀/ω)cos(ωt)|Fuerzas oscilatorias|
> |F₀/t|F₀ ln(t)|Fuerzas inversas (raras)|
> 
> ### Métodos Numéricos:
> 
> - **Regla del rectángulo**: J ≈ Σ F(tᵢ)Δt
> - **Regla del trapecio**: J ≈ Σ ½(Fᵢ + Fᵢ₊₁)Δt
> - **Regla de Simpson**: Mayor precisión para curvas suaves

> [!example]- **Cálculo 1: Impulso con Fuerza Exponencial** 📈
> 
> ### Enunciado:
> 
> Durante el despegue de un cohete, la fuerza del motor varía según F(t) = 50000(1 - e^(-t/10)) N durante los primeros 30 segundos. Calcula: a) El impulso total b) El impulso promedio por segundo c) La fuerza promedio equivalente
> 
> ### Solución:
> 
> **Datos**: F(t) = 50000(1 - e^(-t/10)) N, t ∈ [0, 30] s
> 
> **a) Impulso total**:
> 
> J = ∫₀³⁰ F(t) dt = ∫₀³⁰ 50000(1 - e^(-t/10)) dt
> 
> J = 50000 ∫₀³⁰ (1 - e^(-t/10)) dt J = 50000 [t + 10e^(-t/10)]₀³⁰ J = 50000 [(30 + 10e^(-3)) - (0 + 10e⁰)] J = 50000 [30 + 10(0.0498) - 10] J = 50000 [20.498] **J = 1,024,900 N⋅s**
> 
> **b) Impulso promedio por segundo**:
> 
> **J̄/s = J_total/Δt = 1,024,900/30 = 34,163 N⋅s por segundo**
> 
> **c) Fuerza promedio equivalente**:
> 
> **F̄ = J/Δt = 1,024,900/30 = 34,163 N**

> [!example]- **Cálculo 2: Impulso por Integración Numérica** 📊
> 
> ### Enunciado:
> 
> Los datos de fuerza vs tiempo durante un impacto son:
> 
> |t(ms)|0|2|4|6|8|10|
> |---|---|---|---|---|---|---|
> |F(N)|0|1200|2000|1500|800|0|
> 
> Calcula el impulso usando: a) Regla del trapecio b) Aproximación rectangular c) ¿Cuál es más precisa?
> 
> ### Solución:
> 
> **Datos**: Δt = 2 ms = 0.002 s entre mediciones
> 
> **a) Regla del trapecio**:
> 
> J = Δt/2 × Σ(Fᵢ + Fᵢ₊₁) J = 0.002/2 × [(0+1200) + (1200+2000) + (2000+1500) + (1500+800) + (800+0)] J = 0.001 × [1200 + 3200 + 3500 + 2300 + 800] J = 0.001 × 11000 **J = 11 N⋅s**
> 
> **b) Aproximación rectangular** (usando valor al inicio):
> 
> J = Δt × Σ Fᵢ = 0.002 × (0 + 1200 + 2000 + 1500 + 800) **J = 0.002 × 5500 = 11 N⋅s**
> 
> **c) Precisión**: La regla del trapecio es generalmente **más precisa** para curvas suaves, pero en este caso ambos métodos dan el mismo resultado debido a la simetría de los datos.

> [!example]- **Cálculo 3: Impulso en Función Periódica** 🌊
> 
> ### Enunciado:
> 
> Una fuerza oscilante F(t) = 100 sen(πt) N actúa durante 3 segundos completos. Calcula: a) El impulso total b) El impulso en cada medio período c) ¿Por qué el impulso total es cero?
> 
> ### Solución:
> 
> **Datos**: F(t) = 100 sen(πt) N, t ∈ [0, 3] s
> 
> **a) Impulso total**:
> 
> J = ∫₀³ 100 sen(πt) dt = 100 ∫₀³ sen(πt) dt J = 100 [-cos(πt)/π]₀³ = (100/π)[-cos(3π) + cos(0)] J = (100/π)[-(-1) + 1] = (100/π)[2] = 200/π
> 
> Pero cos(3π) = cos(π) = -1, entonces: **J = (100/π)[1 - (-1)] = 0**
> 
> **b) Impulso en cada medio período**:
> 
> Período T = 2π/π = 2 s, medio período = 1 s
> 
> Primer medio período [0,1]: J₁ = ∫₀¹ 100 sen(πt) dt = (100/π)[-cos(πt)]₀¹ = (100/π)[1-(-1)] = **200/π ≈ 63.7 N⋅s**
> 
> Segundo medio período [1,2]: J₂ = ∫₁² 100 sen(πt) dt = (100/π)[-cos(πt)]₁² = (100/π)[-1-1] = **-200/π ≈ -63.7 N⋅s**
> 
> **c) ¿Por qué el impulso total es cero?**
> 
> El impulso total es cero porque la función seno es **antisimétrica** alrededor de cada período completo. Los impulsos positivos y negativos se cancelan exactamente, resultando en **cambio neto de momentum cero**.

## 🎯 Estrategias de Resolución

> [!tip]- **Método IMPULSO (Identificar-Momentum-Período-Unidades-Límites-Sumar-Obtener)** 🧠
> 
> ### **I**dentificar - Tipo de problema y fuerzas
> 
> 1. Determinar si la fuerza es constante o variable
> 2. Identificar el intervalo de tiempo relevante
> 3. Establecer sistema de coordenadas y signos
> 
> ### **M**omentum - Estados inicial y final
> 
> 4. Calcular momentum inicial: p⃗ᵢ = mᵢv⃗ᵢ
> 5. Identificar la incógnita (generalmente v⃗f)
> 6. Establecer dirección positiva de referencia
> 
> ### **P**eríodo - Intervalo de tiempo
> 
> 7. Determinar t₁ y t₂ para la integración
> 8. Verificar continuidad de la función F(t)
> 9. Dividir en subintervalos si es necesario
> 
> ### **U**nidades - Verificar consistencia
> 
> 10. Confirmar que F esté en Newtons
> 11. Tiempo en segundos
> 12. Masa en kilogramos
> 
> ### **L**ímites - Establecer límites de integración
> 
> 13. Definir límites inferior y superior
> 14. Considerar cambios de dirección de la fuerza
> 15. Verificar puntos de discontinuidad
> 
> ### **S**umar - Calcular el impulso
> 
> 16. Integrar ∫F(t)dt o sumar FΔt
> 17. Aplicar J = Δp = m(v⃗f - v⃗ᵢ)
> 18. Considerar múltiples fuerzas si existen
> 
> ### **O**btener - Resolver para velocidad final
> 
> 19. Despejar v⃗f = v⃗ᵢ + J/m
> 20. Verificar dirección y magnitud
> 21. Comprobar coherencia física del resultado

## 📚 Problemas Tipo

> [!example]- **Problema 1: Pelota y Raqueta de Tenis** 🎾
> 
> ### Enunciado:
> 
> Una pelota de tenis de 60 g se mueve a 25 m/s hacia una raqueta. Durante el impacto que dura 8 ms, la raqueta ejerce una fuerza promedio de 400 N. Si la pelota rebota en la misma dirección con la que llegó, determina: a) El impulso ejercido por la raqueta b) La velocidad de la pelota después del impacto c) El cambio de momentum
> 
> ### Solución:
> 
> **Datos**: m = 0.06 kg, vᵢ = -25 m/s (hacia la raqueta), F̄ = 400 N, Δt = 0.008 s
> 
> **Sistema de coordenadas**: Positivo en dirección opuesta al movimiento inicial
> 
> **a) Impulso ejercido por la raqueta**:
> 
> J = F̄ × Δt = 400 × 0.008 = **3.2 N⋅s**
> 
> **b) Velocidad después del impacto**:
> 
> Aplicando teorema impulso-momentum: J = m(vf - vᵢ) 3.2 = 0.06(vf - (-25)) 3.2 = 0.06(vf + 25) vf + 25 = 3.2/0.06 = 53.33 **vf = 28.33 m/s** (en dirección opuesta a la inicial)
> 
> **c) Cambio de momentum**:
> 
> Δp = m(vf - vᵢ) = 0.06(28.33 - (-25)) = 0.06(53.33) = **3.2 kg⋅m/s**
> 
> **Verificación**: Δp = J ✓

> [!example]- **Problema 2: Fuerza Variable en Martillo** 🔨
> 
> ### Enunciado:
> 
> Un martillo de 2 kg golpea un clavo. La fuerza durante el impacto varía según F(t) = 5000t² N durante los primeros 0.01 s del contacto. Si el martillo tenía una velocidad de 8 m/s antes del impacto, determina: a) El impulso durante el contacto b) La velocidad del martillo inmediatamente después c) La fuerza máxima durante el impacto
> 
> ### Solución:
> 
> **Datos**: m = 2 kg, F(t) = 5000t² N, t ∈ [0, 0.01] s, vᵢ = 8 m/s
> 
> **a) Impulso durante el contacto**:
> 
> J = ∫₀^{0.01} F(t) dt = ∫₀^{0.01} 5000t² dt J = 5000 ∫₀^{0.01} t² dt = 5000 [t³/3]₀^{0.01} J = 5000 × (0.01)³/3 = 5000 × 10⁻⁶/3 **J = 1.67 × 10⁻³ N⋅s**
> 
> **b) Velocidad después del impacto**:
> 
> Asumiendo que el martillo se detiene (clavo absorbe momentum): J = m(0 - vᵢ) = -mvᵢ
> 
> Pero el impulso calculado es muy pequeño comparado con mvᵢ = 2×8 = 16 kg⋅m/s
> 
> Por lo tanto: J = m(vf - vᵢ) 1.67×10⁻³ = 2(vf - 8) vf = 8 + (1.67×10⁻³)/2 = **7.999 m/s**
> 
> (El cambio de velocidad es mínimo debido al corto tiempo de contacto)
> 
> **c) Fuerza máxima**:
> 
> F_max = F(0.01) = 5000(0.01)² = **0.5 N**

> [!example]- **Problema 3: Cohete con Empuje Variable** 🚀
> 
> ### Enunciado:
> 
> Un cohete de 1000 kg parte del reposo y experimenta un empuje que varía según F(t) = 20000(1 - e^(-t/5)) N durante 15 segundos. Despreciando la resistencia del aire y el cambio de masa, determina: a) El impulso total b) La velocidad final c) La aceleración promedio
> 
> ### Solución:
> 
> **Datos**: m = 1000 kg, F(t) = 20000(1 - e^(-t/5)) N, t ∈ [0, 15] s, vᵢ = 0
> 
> **a) Impulso total**:
> 
> J = ∫₀¹⁵ 20000(1 - e^(-t/5)) dt J = 20000 ∫₀¹⁵ (1 - e^(-t/5)) dt J = 20000 [t + 5e^(-t/5)]₀¹⁵ J = 20000 [(15 + 5e^(-3)) - (0 + 5e⁰)] J = 20000 [15 + 5(0.0498) - 5] J = 20000 [10.249] **J = 204,980 N⋅s**
> 
> **b) Velocidad final**:
> 
> J = m(vf - vᵢ) 204,980 = 1000(vf - 0) **vf = 204.98 m/s**
> 
> **c) Aceleración promedio**:
> 
> ā = Δv/Δt = (204.98 - 0)/15 = **13.67 m/s²**

> [!example]- **Problema 4: Colisión de Vehículos** 🚗💥
> 
> ### Enunciado:
> 
> Un automóvil de 1200 kg que viaja a 15 m/s colisiona frontalmente con un camión de 3000 kg que se mueve a 8 m/s en sentido contrario. Después del impacto, ambos vehículos se mueven juntos. Determina: a) La velocidad común después del impacto b) El impulso sobre cada vehículo c) La pérdida de energía cinética
> 
> ### Solución:
> 
> **Datos**: m₁ = 1200 kg, v₁ᵢ = 15 m/s, m₂ = 3000 kg, v₂ᵢ = -8 m/s (opuesto)
> 
> **Sistema**: Positivo en dirección inicial del auto
> 
> **a) Velocidad común después del impacto**:
> 
> Conservación de momentum: m₁v₁ᵢ + m₂v₂ᵢ = (m₁ + m₂)vf 1200(15) + 3000(-8) = (1200 + 3000)vf 18000 - 24000 = 4200vf -6000 = 4200vf **vf = -1.43 m/s** (en dirección del camión)
> 
> **b) Impulso sobre cada vehículo**:
> 
> Para el automóvil: J₁ = m₁(vf - v₁ᵢ) = 1200(-1.43 - 15) = 1200(-16.43) = **-19,716 N⋅s**
> 
> Para el camión: J₂ = m₂(vf - v₂ᵢ) = 3000(-1.43 - (-8)) = 3000(6.57) = **19,710 N⋅s**
> 
> **Verificación**: J₁ + J₂ ≈ 0 ✓ (principio de acción-reacción)
> 
> **c) Pérdida de energía cinética**:
> 
> Ec_inicial = ½m₁v₁ᵢ² + ½m₂v₂ᵢ² = ½(1200)(15)² + ½(3000)(8)² = 135,000 + 96,000 = 231,000 J
> 
> Ec_final = ½(m₁ + m₂)vf² = ½(4200)(1.43)² = 4,305 J
> 
> **Pérdida = 231,000 - 4,305 = 226,695 J** (transformada en calor, sonido, deformación)

> [!example]- **Problema 5: Explosión en el Espacio** 💥
> 
> ### Enunciado:
> 
> En el espacio, un objeto de 500 kg inicialmente en reposo explota en tres fragmentos: - Fragmento A: 200 kg se mueve a 30 m/s hacia el este - Fragmento B: 150 kg se mueve a 40 m/s hacia el norte - Fragmento C: 150 kg se mueve con velocidad desconocida
> 
> Determina: a) La velocidad del fragmento C b) El impulso total de la explosión c) La energía liberada en la explosión
> 
> ### Solución:
> 
> **Datos**: m_total = 500 kg, vᵢ = 0 mA = 200 kg, v⃗A = 30î m/s mB = 150 kg, v⃗B = 40ĵ m/s  
> mC = 150 kg, v⃗C = ?
> 
> **a) Velocidad del fragmento C**:
> 
> Conservación de momentum: p⃗ᵢ = p⃗f → 0 = mAv⃗A + mBv⃗B + mCv⃗C
> 
> 0 = 200(30î) + 150(40ĵ) + 150v⃗C 0 = 6000î + 6000ĵ + 150v⃗C 150v⃗C = -6000î - 6000ĵ **v⃗C = -40î - 40ĵ m/s**
> 
> |v⃗C| = √(40² + 40²) = 56.57 m/s a 225° (suroeste)
> 
> **b) Impulso total de la explosión**:
> 
> El impulso total sobre el sistema es **cero** porque no hay fuerzas externas (espacio). Los impulsos internos se cancelan entre sí.
> 
> **c) Energía liberada**:
> 
> Ec_inicial = 0 J (en reposo)
> 
> Ec_final = ½mAv²A + ½mBv²B + ½mCv²C Ec_final = ½(200)(30)² + ½(150)(40)² + ½(150)(56.57)² Ec_final = 90,000 + 120,000 + 240,000 = **450,000 J**
> 
> **Energía liberada = 450,000 J** (toda se convirtió en energía cinética)

## 🧮 Técnicas de Memorización

> [!tip]- **Mnemotecnia: "IMPULSO"** 📝
> 
> **I**ntegral - J = ∫F dt para fuerzas variables **M**omento - Cambia el momentum: J = Δp **P**roducto - J = F×t para fuerzas constantes **U**nidades - Newton-segundo = kg⋅m/s **L**ineal - Solo afecta momentum lineal **S**igno - Dirección importa: impulso vectorial **O**posición - Fuerzas internas se cancelan

> [!tip]- **Reglas de Cálculo** 🔑
> 
> ### Para Fuerza Constante:
> 
> **J = F⃗ × Δt**
> 
> ### Para Fuerza Variable:
> 
> **J = ∫F⃗(t) dt**
> 
> ### Teorema Fundamental:
> 
> **J = Δp = m(v⃗f - v⃗ᵢ)**
> 
> ### Conservación (sistema aislado):
> 
> **Σpᵢ = Σpf**
> 
> ### Colisión perfectamente inelástica:
> 
> **m₁v₁ᵢ + m₂v₂ᵢ = (m₁ + m₂)vf**

## ⚠️ Errores Comunes

> [!warning]- **Confusiones Frecuentes** ⚠️
> 
> 1. **Confundir impulso con momentum**: J ≠ p, sino J = Δp
> 2. **Olvidar la naturaleza vectorial**: Impulso tiene dirección y sentido
> 3. **Signo incorrecto en velocidades**: Establecer mal el sistema de coordenadas
> 4. **No conservar momentum en explosiones**: Olvidar que Σpᵢ = Σpf = 0
> 5. **Aplicar conservación con fuerzas externas**: Solo válida en sistemas aislados
> 6. **Unidades inconsistentes**: Mezclar kg, g o N, dyn en el mismo problema
> 7. **Integración incorrecta**: Errores en límites o evaluación de integrales
> 8. **Confundir fuerza promedio**: F̄ = J/Δt, no el promedio aritmético de valores

## 🎯 Aplicaciones Prácticas

> [!info]- **Ejemplos del Mundo Real** 🌍
> 
> ### Deportes:
> 
> - **Golf y tenis**: Impulso de raqueta/palo sobre pelota
> - **Boxeo**: Análisis de impacto de golpes
> - **Salto con pértiga**: Transferencia de momentum horizontal a vertical
> - **Béisbol**: Velocidad de pelota después del bate
> 
> ### Ingeniería Automotriz:
> 
> - **Airbags**: Aumentar tiempo de contacto, reducir fuerza
> - **Parachoques**: Diseño para absorber impulso
> - **Análisis de colisiones**: Reconstrucción de accidentes
> - **Pruebas de seguridad**: Evaluación de impactos
> 
> ### Aeronáutica y Espacial:
> 
> - **Propulsión de cohetes**: Impulso específico de motores
> - **Maniobras orbitales**: Cambios de velocidad con propulsores
> - **Aterrizaje de naves**: Control de velocidad de descenso
> - **Eyección de pilotos**: Sistemas de escape rápido
> 
> ### Balística y Defensa:
> 
> - **Proyectiles**: Velocidad de salida de cañones
> - **Retroceso de armas**: Conservación de momentum
> - **Sistemas de protección**: Absorción de impactos
> - **Análisis forense**: Reconstrucción de disparos
> 
> ### Procesos Industriales:
> 
> - **Martillos neumáticos**: Transferencia de impulso
> - **Prensas hidráulicas**: Aplicación de fuerzas controladas
> - **Sistemas de transporte**: Aceleración y frenado
> - **Maquinaria de impacto**: Forjado y estampado

## 📖 Referencias

> [!quote]- **Notas Relacionadas**
> 
> - [[Impulso Lineal]] - Fundamentos teóricos del impulso
> - [[Momentum Lineal y Su Conservación]] - Principios de conservación
> - [[Choques Uni-Bidimensionales]] - Aplicaciones en colisiones
> - [[Trabajo y Energía]] - Relación con energía cinética

## 📚 Notas Recomendadas

> [!note]- **Prerrequisitos**
> 
> - [[Leyes de Newton]] - Segunda ley como base del impulso
> - [[Cinemática Traslacional]] - Conceptos de velocidad y aceleración
> - [[Vectores]] - Manejo de magnitudes vectoriales
> - [[Unidades y Magnitudes Físicas]] - Consistencia dimensional

---

**Tags:** #impulso-lineal #momentum #velocidad-final #colisiones #conservacion-momentum #fisica-mecanica #integracion #fuerzas-variables #explosiones #calculo-impulso