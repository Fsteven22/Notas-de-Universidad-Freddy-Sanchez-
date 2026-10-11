---
dg-publish: true
---

# Incertidumbres Experimentales

> [!quote] "La incertidumbre no es ignorancia, sino conocimiento preciso de lo que no podemos conocer con exactitud." 🔍
>
> [!info] Las incertidumbres experimentales describen el rango de valores dentro del cual esperamos que se encuentre el valor verdadero de una magnitud. Cuando combinamos mediciones para calcular resultados indirectos, las incertidumbres se propagan siguiendo reglas matemáticas específicas que nos permiten estimar la confiabilidad del resultado final.

## 🔧 Conceptos Fundamentales

> [!info] **Tipos de Incertidumbres** 📐
> 
> ### Clasificación Principal:
> 
> |Tipo|Símbolo|Origen|Cálculo|Ejemplo|
> |---|---|---|---|---|
> |**Instrumental**|u_inst|Limitación del instrumento|± precisión/2|Regla: ±0.5 mm|
> |**Estadística**|u_est|Dispersión de mediciones|s/√n|±0.03 s|
> |**Sistemática**|u_sis|Error conocido del método|Estimación/análisis|±2% calibración|
> |**Combinada**|u_c|Suma de todas las fuentes|√(u₁² + u₂² + u₃²)|±0.12 m|
> 
> ### Características:
> 
> - **Incertidumbre absoluta**: Mismas unidades que la magnitud (±0.05 m)
> - **Incertidumbre relativa**: Adimensional (u/x = 0.02 = 2%)
> - **Nivel de confianza**: Generalmente 68% (1σ) o 95% (2σ)
> - **Distribución**: Asumimos distribución normal para la mayoría de casos
>
> [!tip] **Fuentes de Incertidumbre** 🌊
> 
> ### Instrumentales:
> 
> **Resolución del instrumento**:
> 
> - **Regla**: ±(menor división/2) = ±0.5 mm
> - **Calibrador digital**: ±0.01 mm (según especificaciones)
> - **Cronómetro**: ±0.01 s (tiempo de reacción humana: ±0.2 s)
> - **Balanza**: ±0.1 g o según calibración
> 
> **Condiciones ambientales**:
> 
> - **Temperatura**: Dilatación térmica
> - **Presión**: Afecta densidad del aire
> - **Humedad**: Afecta propiedades de materiales
> - **Vibración**: Afecta instrumentos sensibles
> 
> ### Metodológicas:
> 
> **Técnica de medición**:
> 
> - **Paralaje**: Error de perspectiva
> - **Tiempo de reacción**: En mediciones manuales
> - **Definición del punto de medición**: ¿Dónde exactamente medir?
> - **Estabilidad del sistema**: Oscilaciones, movimiento
> 
> **Aproximaciones del modelo**:
> 
> - **Resistencia del aire**: Despreciada en caída libre
> - **Masa del hilo**: Despreciada en péndulo
> - **Deformación**: En mediciones de sólidos
> - **Fricción**: En experimentos de mecánica
>
> [!warning] **Propagación de Incertidumbres** ⚡
> 
> ### Reglas Fundamentales:
> 
> **Para Suma y Resta**: z = x ± y
> 
> ```
> u_z = √(u_x² + u_y²)
> ```
> 
> **Para Multiplicación y División**: z = xy o z = x/y
> 
> ```
> u_z/z = √((u_x/x)² + (u_y/y)²)
> ```
> 
> **Para Potencias**: z = x^n
> 
> ```
> u_z/z = |n| × (u_x/x)
> ```
> 
> **Para Funciones Generales**: z = f(x, y, ...)
> 
> ```
> u_z = √[(∂f/∂x)² × u_x² + (∂f/∂y)² × u_y² + ...]
> ```
> 
> ### Casos Especiales:
> 
> |Operación|Fórmula|Propagación|
> |---|---|---|
> |z = x + y|u_z = √(u_x² + u_y²)|Se suman cuadráticamente|
> |z = x - y|u_z = √(u_x² + u_y²)|Igual que suma|
> |z = kx|u_z =|k|
> |z = x²|u_z = 2|x|
> |z = √x|u_z = u_x/(2√x)|Reduce incertidumbre relativa|
> |z = ln(x)|u_z = u_x/x|Incertidumbre relativa se conserva|
>
> [!success] 🔗 Proceso de Análisis de Incertidumbres
> 
> ```mermaid
> graph TD
>     A[Identificar Variables] --> B[Determinar Incertidumbres Individuales]
>     B --> C[Escribir Función Matemática]
>     C --> D[Aplicar Reglas de Propagación]
>     D --> E[Calcular Incertidumbre Combinada]
>     E --> F[Expresar Resultado Final]
>     F --> G[Verificar Coherencia]
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
>     style E fill:#fce4ec
>     style F fill:#f1f8e9
>     style G fill:#e0f2f1
> ```
>
> [!note] **Método de Derivadas Parciales** 📝
> 
> ### Fundamento Matemático:
> 
> Para una función z = f(x, y, ...), la incertidumbre se calcula como:
> 
> ```
> u_z = √[(∂f/∂x)² × u_x² + (∂f/∂y)² × u_y² + ...]
> ```
> 
> ### Derivadas Útiles:
> 
> |Función|Derivada Parcial|Aplicación|
> |---|---|---|
> |f = x + y|∂f/∂x = 1|Suma de longitudes|
> |f = xy|∂f/∂x = y|Área de rectángulo|
> |f = x/y|∂f/∂x = 1/y|Velocidad v = d/t|
> |f = x²|∂f/∂x = 2x|Área de círculo|
> |f = √x|∂f/∂x = 1/(2√x)|Período de péndulo|
> |f = sin(x)|∂f/∂x = cos(x)|Oscilaciones|
> 
> ### Ejemplo de Aplicación:
> 
> **Para densidad ρ = m/V donde V = πr²h**:
> 
> 1. **Función completa**: ρ = m/(πr²h)
> 2. **Derivadas parciales**:
>     - ∂ρ/∂m = 1/(πr²h)
>     - ∂ρ/∂r = -2m/(πr³h)
>     - ∂ρ/∂h = -m/(πr²h²)
> 3. **Incertidumbre**: u_ρ = √[(∂ρ/∂m)²u_m² + (∂ρ/∂r)²u_r² + (∂ρ/∂h)²u_h²]

## 🎯 Estrategias de Cálculo

> [!tip] **Método PIPR (Propagar-Identificar-Propagar-Reportar)** 🧠
> 
> ### **P**ropagar - Identifica la función matemática
> 
> 1. **Escribe** la ecuación que relaciona el resultado con las mediciones
> 2. **Identifica** todas las variables independientes
> 3. **Verifica** que no hayas omitido ninguna dependencia
> 
> ### **I**dentificar - Determina las incertidumbres individuales
> 
> 4. **Lista** la incertidumbre de cada variable medida
> 5. **Convierte** a las mismas unidades si es necesario
> 6. **Distingue** entre incertidumbres absolutas y relativas
> 
> ### **P**ropagar - Aplica las reglas matemáticas
> 
> 7. **Selecciona** la regla apropiada (suma, producto, potencia, etc.)
> 8. **Calcula** usando derivadas parciales si es necesario
> 9. **Verifica** que el resultado tenga sentido físico
> 
> ### **R**eportar - Expresa el resultado correctamente
> 
> 10. **Redondea** la incertidumbre a 1-2 cifras significativas
> 11. **Ajusta** el valor principal al mismo número de decimales
> 12. **Incluye** unidades y nivel de confianza

## 📚 Ejemplos Prácticos

> [!example] **Ejemplo 1: Velocidad (División Simple)** 🏃
> 
> ### Situación:
> 
> Calcular velocidad v = d/t con sus respectivas incertidumbres.
> 
> ### Datos:
> 
> - **Distancia**: d = (100.0 ± 0.5) m
> - **Tiempo**: t = (12.5 ± 0.2) s
> 
> ### Cálculo del Valor:
> 
> v = d/t = 100.0/12.5 = **8.00 m/s**
> 
> ### Cálculo de la Incertidumbre:
> 
> **Método 1 - Incertidumbres Relativas**:
> 
> - u_d/d = 0.5/100.0 = 0.005
> - u_t/t = 0.2/12.5 = 0.016
> - u_v/v = √[(u_d/d)² + (u_t/t)²] = √[0.005² + 0.016²] = **0.0167**
> - u_v = 0.0167 × 8.00 = **0.13 m/s**
> 
> **Método 2 - Derivadas Parciales**:
> 
> - ∂v/∂d = 1/t = 1/12.5 = 0.08 s⁻¹
> - ∂v/∂t = -d/t² = -100.0/12.5² = -6.4 m/s²
> - u_v = √[(0.08)² × (0.5)² + (-6.4)² × (0.2)²] = **0.13 m/s**
> 
> ### Resultado Final:
> 
> **v = (8.00 ± 0.13) m/s** con incertidumbre relativa de 1.6%
>
> [!example] **Ejemplo 2: Área de un Círculo** 🔵
> 
> ### Situación:
> 
> Calcular el área A = πr² de un círculo midiendo su radio.
> 
> ### Datos:
> 
> - **Radio**: r = (5.24 ± 0.05) cm
> - **π**: Consideramos exacto (sin incertidumbre)
> 
> ### Cálculo del Valor:
> 
> A = πr² = π × (5.24)² = **86.3 cm²**
> 
> ### Cálculo de la Incertidumbre:
> 
> **Para potencias**: A = πr², entonces u_A/A = 2 × (u_r/r)
> 
> - u_r/r = 0.05/5.24 = 0.0095
> - u_A/A = 2 × 0.0095 = **0.019**
> - u_A = 0.019 × 86.3 = **1.6 cm²**
> 
> **Verificación con derivadas**:
> 
> - ∂A/∂r = 2πr = 2π × 5.24 = 32.9 cm
> - u_A = |∂A/∂r| × u_r = 32.9 × 0.05 = **1.6 cm²** ✓
> 
> ### Resultado Final:
> 
> **A = (86.3 ± 1.6) cm²** con incertidumbre relativa de 1.9%
>
> [!example] **Ejemplo 3: Densidad (Función Compuesta)** ⚖️
> 
> ### Situación:
> 
> Calcular densidad ρ = m/V de un cilindro donde V = πr²h.
> 
> ### Datos:
> 
> - **Masa**: m = (127.3 ± 0.1) g
> - **Radio**: r = (1.25 ± 0.02) cm
> - **Altura**: h = (8.50 ± 0.05) cm
> 
> ### Cálculo de Valores:
> 
> - V = πr²h = π × (1.25)² × 8.50 = **41.7 cm³**
> - ρ = m/V = 127.3/41.7 = **3.05 g/cm³**
> 
> ### Cálculo de Incertidumbres:
> 
> **Paso 1: Incertidumbre del volumen** Para V = πr²h, usando incertidumbres relativas:
> 
> - u_r/r = 0.02/1.25 = 0.016
> - u_h/h = 0.05/8.50 = 0.0059
> - u_V/V = √[(2 × u_r/r)² + (u_h/h)²] = √[(2 × 0.016)² + (0.0059)²] = **0.032**
> - u_V = 0.032 × 41.7 = **1.3 cm³**
> 
> **Paso 2: Incertidumbre de la densidad** Para ρ = m/V:
> 
> - u_m/m = 0.1/127.3 = 0.00079
> - u_V/V = 0.032 (calculado arriba)
> - u_ρ/ρ = √[(u_m/m)² + (u_V/V)²] = √[(0.00079)² + (0.032)²] = **0.032**
> - u_ρ = 0.032 × 3.05 = **0.10 g/cm³**
> 
> ### Resultado Final:
> 
> **ρ = (3.05 ± 0.10) g/cm³** con incertidumbre relativa de 3.2%

## 🧮 Técnicas de Memorización

> [!tip] **Mnemotecnia: "SUMAR"** 🎯
> 
> **S**uma cuadrática para suma/resta **U**sa relativas para producto/división **M**ultiplica por |n| para potencias **A**plica derivadas para funciones complejas **R**edondea apropiadamente el resultado
>
> [!tip] **Reglas Rápidas de Propagación** 📏
> 
> ### Jerarquía de Operaciones:
> 
> 1. **Suma/Resta**: Las incertidumbres absolutas se suman cuadráticamente
> 2. **Multiplicación/División**: Las incertidumbres relativas se suman cuadráticamente
> 3. **Potencias**: La incertidumbre relativa se multiplica por el exponente
> 4. **Funciones complejas**: Usar derivadas parciales
> 
> ### Estimaciones Rápidas:
> 
> - **Si una incertidumbre >> otras**: Domina el resultado final
> - **Incertidumbres similares**: Resultado ≈ √2 veces la mayor
> - **Para productos**: Si u_x/x ≈ u_y/y, entonces u_z/z ≈ √2 × (u_x/x)

## ⚠️ Errores Comunes

> [!warning] **Confusiones Frecuentes** ⚠️
> 
> 1. **Sumar incertidumbres linealmente**:
>     - ❌ u_z = u_x + u_y
>     - ✅ u_z = √(u_x² + u_y²)
> 2. **Mezclar incertidumbres absolutas y relativas**:
>     - Para suma: usar absolutas
>     - Para producto: usar relativas
> 3. **Olvidar el valor absoluto en derivadas**:
>     - Si ∂f/∂x es negativo, usar |∂f/∂x|
> 4. **No considerar todas las fuentes**:
>     - Instrumental + estadística + sistemática
> 5. **Redondeo excesivo o insuficiente**:
>     - Incertidumbre: 1-2 cifras significativas
>     - Valor: misma precisión decimal que incertidumbre
> 6. **Usar fórmulas incorrectas para funciones complejas**:
>     - Para f(x,y) ≠ x±y o xy o x/y, usar derivadas parciales

## 🎯 Aplicaciones Específicas

> [!info] **Experimentos de Laboratorio** 🔬
> 
> ### Cinemática:
> 
> **Velocidad**: v = Δx/Δt
> 
> ```
> u_v/v = √[(u_Δx/Δx)² + (u_Δt/Δt)²]
> ```
> 
> **Aceleración**: a = Δv/Δt
> 
> ```
> u_a/a = √[(u_Δv/Δv)² + (u_Δt/Δt)²]
> ```
> 
> **Aceleración gravitacional**: g = 2h/t²
> 
> ```
> u_g/g = √[(u_h/h)² + (2u_t/t)²]
> ```
> 
> ### Dinámica:
> 
> **Fuerza**: F = ma
> 
> ```
> u_F/F = √[(u_m/m)² + (u_a/a)²]
> ```
> 
> **Momento de inercia**: I = ½mr²
> 
> ```
> u_I/I = √[(u_m/m)² + (2u_r/r)²]
> ```
> 
> ### Energía:
> 
> **Energía cinética**: K = ½mv²
> 
> ```
> u_K/K = √[(u_m/m)² + (2u_v/v)²]
> ```
> 
> **Energía potencial**: U = mgh
> 
> ```
> u_U/U = √[(u_m/m)² + (u_g/g)² + (u_h/h)²]
> ```

## 🔍 Análisis de Dominancia

> [!info] **Identificar Contribuciones Principales** 📊
> 
> ### Método de Análisis:
> 
> Para z = f(x, y), calcular las contribuciones individuales:
> 
> ```
> Contribución de x: C_x = (∂f/∂x)² × u_x²
> Contribución de y: C_y = (∂f/∂y)² × u_y²
> Incertidumbre total: u_z = √(C_x + C_y)
> ```
> 
> ### Interpretación:
> 
> - **C_x >> C_y**: La variable x domina la incertidumbre
> - **C_x ≈ C_y**: Ambas variables contribuyen similarmente
> - **Mejorar precisión**: Enfocarse en la variable dominante
> 
> ### Ejemplo Práctico:
> 
> Para densidad ρ = m/(πr²h):
> 
> - Si C_r >> C_m, C_h → **Mejorar medición del radio**
> - Si C_h >> C_m, C_r → **Mejorar medición de la altura**
> - Esto guía dónde invertir esfuerzo experimental

## 📖 Referencias

> [!quote] **Notas Relacionadas**
> 
> - [[Errores Absolutos y Relativos]] - Conceptos fundamentales
> - [[Derivadas Parciales]] - Herramienta matemática
> - [[Tratamiento Estadístico de Datos]] - Análisis avanzado
> - [[Cifras Significativas]] - Expresión de resultados

## 📚 Notas Recomendadas

> [!note] **Prerrequisitos**
> 
> - [[Errores Absolutos y Relativos]] - Base conceptual
> - **Cálculo diferencial**: Derivadas parciales básicas
> - **Álgebra**: Operaciones con radicales
>
> [!note] **Temas Siguientes**
> 
> - [[Derivadas Parciales]] - Matemáticas para propagación
> - [[Análisis Gráfico]] - Representación de incertidumbres
> - [[Reportes de Laboratorio]] - Presentación de resultados

---

**Tags:** #incertidumbres #propagacion #derivadas-parciales #estadistica #mediciones #analisis-errores #laboratorio #fisica-mecanica #precision #confiabilidad
