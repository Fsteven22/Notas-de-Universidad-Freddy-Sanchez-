# Gráficas Lineales

> [!quote] "Una gráfica vale más que mil datos en una tabla: revela patrones que los números ocultan." 📈

> [!info]- Las gráficas lineales son herramientas fundamentales para visualizar, analizar e interpretar relaciones entre variables físicas. Permiten identificar tendencias, extraer parámetros característicos y validar modelos teóricos mediante el análisis de datos experimentales. En física mecánica, la mayoría de las leyes fundamentales pueden expresarse o linealizarse para su análisis gráfico.

## 🔧 Conceptos Fundamentales

> [!info]- **Ecuación de la Recta** 📐
> 
> ### Forma Pendiente-Intercepto:
> 
> ```
> y = mx + b
> ```
> 
> **Parámetros fundamentales**:
> 
> - **m**: Pendiente (slope) - tasa de cambio
> - **b**: Intercepto en y - valor cuando x = 0
> - **x**: Variable independiente (controlada)
> - **y**: Variable dependiente (medida)
> 
> ### Formas Alternativas:
> 
> |Forma|Ecuación|Cuándo Usar|
> |---|---|---|
> |**Punto-Pendiente**|y - y₁ = m(x - x₁)|Conoces un punto y la pendiente|
> |**Dos Puntos**|y - y₁ = [(y₂-y₁)/(x₂-x₁)](x - x₁)|Conoces dos puntos|
> |**General**|Ax + By + C = 0|Forma estándar matemática|
> |**Interceptos**|x/a + y/b = 1|Conoces ambos interceptos|
> 
> ### Interpretación Física:
> 
> **Pendiente (m)**:
> 
> - **Unidades**: [y]/[x] (ej: m/s para velocidad)
> - **Significado**: Cambio en y por unidad de cambio en x
> - **m > 0**: Relación directa (creciente)
> - **m < 0**: Relación inversa (decreciente)
> - **m = 0**: No hay dependencia (horizontal)
> 
> **Intercepto (b)**:
> 
> - **Unidades**: [y] (mismas que la variable dependiente)
> - **Significado**: Valor de y cuando x = 0
> - **Interpretación física**: Condición inicial, offset, sesgo

> [!tip]- **Variables en Física** 🎯
> 
> ### Relaciones Lineales Directas:
> 
> |Ley Física|Ecuación|Gráfica|Pendiente|Intercepto|
> |---|---|---|---|---|
> |**Ley de Hooke**|F = kx|F vs x|k (constante elástica)|0|
> |**Ley de Ohm**|V = IR|V vs I|R (resistencia)|0|
> |**Movimiento uniforme**|x = x₀ + vt|x vs t|v (velocidad)|x₀ (posición inicial)|
> |**Aceleración constante**|v = v₀ + at|v vs t|a (aceleración)|v₀ (velocidad inicial)|
> 
> ### Relaciones Linealizables:
> 
> |Ley Física|Ecuación Original|Linealización|Gráfica|
> |---|---|---|---|
> |**Péndulo simple**|T = 2π√(L/g)|T² = (4π²/g)L|T² vs L|
> |**Caída libre**|h = ½gt²|h = ½g·t²|h vs t²|
> |**Ley de enfriamiento**|T = T₀e^(-kt)|ln(T) = ln(T₀) - kt|ln(T) vs t|
> |**Ley potencial**|y = ax^n|log(y) = log(a) + n·log(x)|log(y) vs log(x)|
> 
> ### Identificación de Patrones:
> 
> **Por la forma de los datos**:
> 
> - **Puntos en línea recta**: Relación lineal directa
> - **Curvatura hacia arriba**: Posible relación cuadrática o exponencial
> - **Curvatura hacia abajo**: Posible relación logarítmica o de saturación
> - **Dispersión aleatoria**: No hay relación aparente

## 📊 Construcción de Gráficas

> [!info]- **Elementos de una Gráfica Científica** 📋
> 
> ### Componentes Esenciales:
> 
> **1. Título descriptivo**:
> 
> ```
> "Fuerza elástica vs Desplazamiento para resorte de acero"
> No: "Gráfico 1" o "F vs x"
> ```
> 
> **2. Ejes con etiquetas completas**:
> 
> ```
> Eje X: "Desplazamiento, x (cm)"
> Eje Y: "Fuerza, F (N)"
> Incluir: nombre de variable, símbolo y unidades
> ```
> 
> **3. Escalas apropiadas**:
> 
> - **Origen**: No siempre debe ser (0,0)
> - **Rango**: Cubrir todo el rango de datos
> - **Intervalos**: Fáciles de leer (1, 2, 5, 10, 20, 50...)
> - **Proporción**: ~3:2 (ancho:alto) para mejor visualización
> 
> **4. Puntos experimentales**:
> 
> - **Símbolos claros**: ●, ▲, ■, ◆ (diferentes para distintas series)
> - **Tamaño adecuado**: Visibles pero no excesivos
> - **Sin unir**: Los puntos representan datos, no la línea
> 
> **5. Barras de error** (cuando aplique):
> 
> - **Verticales**: Incertidumbre en y
> - **Horizontales**: Incertidumbre en x
> - **Ambas**: Si hay incertidumbre significativa en ambas variables
> 
> **6. Línea de mejor ajuste**:
> 
> - **Línea continua**: Para el modelo teórico o ajuste
> - **No forzar por el origen**: A menos que la teoría lo requiera
> - **Color diferente**: Distinguir de los puntos experimentales

> [!success] 🔗 Proceso de Construcción de Gráficas
> 
> ```mermaid
> graph TD
>     A[Identificar Variables] --> B[Determinar Escalas]
>     B --> C[Etiquetar Ejes Completamente]
>     C --> D[Graficar Puntos Experimentales]
>     D --> E[Añadir Barras de Error]
>     E --> F[Trazar Línea de Mejor Ajuste]
>     F --> G[Incluir Título Descriptivo]
>     G --> H[Verificar Legibilidad]
>     H --> I[Analizar e Interpretar]
>     
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
>     style E fill:#fce4ec
>     style F fill:#f1f8e9
>     style G fill:#e0f2f1
>     style H fill:#f3e5f5
>     style I fill:#e1f5fe
> ```

> [!warning]- **Selección de Escalas** 📏
> 
> ### Criterios para Ejes:
> 
> **Rango de datos**:
> 
> ```
> Datos: x ∈ [12, 87], y ∈ [245, 890]
> Escalas sugeridas:
> Eje X: 0 a 100 (o 10 a 90)
> Eje Y: 200 a 900 (o 0 a 1000)
> ```
> 
> **Intervalos de graduación**:
> 
> - **Buenos**: 1, 2, 5, 10, 20, 25, 50, 100, 200, 500...
> - **Malos**: 3, 6, 7, 9, 11, 13, 15, 30, 60, 70...
> - **Regla**: Fácil interpolación mental
> 
> ### Tipos de Escalas:
> 
> |Tipo|Cuándo usar|Ventaja|Desventaja|
> |---|---|---|---|
> |**Lineal**|Relaciones lineales|Interpretación directa|No sirve para relaciones exponenciales|
> |**Logarítmica**|Relaciones exponenciales|Linealiza exponenciales|Difícil interpretar|
> |**Semi-log**|Una variable exponencial|Híbrido útil|Requiere cuidado en interpretación|
> |**Log-log**|Relaciones potenciales|Linealiza potencias|Ambas escalas no lineales|
> 
> ### Optimización Visual:
> 
> **Principio de máxima resolución**:
> 
> - Usar todo el espacio disponible
> - Los puntos deben ocupar ~75% del área de la gráfica
> - Evitar espacios en blanco excesivos
> 
> **Proporciones**:
> 
> - **Aspecto**: Relación ancho/alto ≈ 1.6 (proporción áurea)
> - **Puntos**: No más de ~50 puntos por gráfica
> - **Texto**: Tamaño legible (>8pt para impresión)

> [!example]- **Ejemplo: Construcción Paso a Paso** 📈
> 
> ### Experimento: Ley de Hooke
> 
> **Datos experimentales**:
> 
> ```
> x (cm): 0.0, 2.1, 4.3, 6.2, 8.1, 10.0, 12.2, 14.1
> F (N):  0.0, 1.05, 2.15, 3.10, 4.05, 5.00, 6.10, 7.05
> u_x:    ±0.1 cm para todas las mediciones
> u_F:    ±0.05 N para todas las mediciones
> ```
> 
> ### Paso 1: Identificar Variables
> 
> - **Variable independiente**: x (desplazamiento) - controlada
> - **Variable dependiente**: F (fuerza) - medida
> - **Relación esperada**: F = kx (lineal, pasa por origen)
> 
> ### Paso 2: Determinar Escalas
> 
> ```
> Rango x: 0 a 14.1 cm → Escala: 0 a 16 cm (intervalos de 2 cm)
> Rango F: 0 a 7.05 N → Escala: 0 a 8 N (intervalos de 1 N)
> ```
> 
> ### Paso 3: Etiquetar Ejes
> 
> ```
> Eje X: "Desplazamiento, x (cm)"
> Eje Y: "Fuerza aplicada, F (N)"
> Título: "Verificación de la Ley de Hooke - Resorte de acero"
> ```
> 
> ### Paso 4: Graficar Puntos
> 
> - Usar símbolos sólidos (●) para buena visibilidad
> - Incluir barras de error (±0.1 cm horizontal, ±0.05 N vertical)
> - No conectar los puntos con líneas
> 
> ### Paso 5: Análisis Preliminar
> 
> - Los puntos muestran tendencia lineal clara
> - Pasan cerca del origen (consistente con F = kx)
> - Dispersión pequeña → buena precisión experimental

## 📏 Interpretación de Pendiente e Intercepto

> [!info]- **Significado Físico de la Pendiente** ⚡
> 
> ### Cálculo de la Pendiente:
> 
> **Entre dos puntos**:
> 
> ```
> m = (y₂ - y₁)/(x₂ - x₁) = Δy/Δx
> ```
> 
> **Interpretación general**:
> 
> - **m**: Cambio en y por cada unidad de cambio en x
> - **Unidades**: [m] = [y]/[x]
> - **Signo**: Indica dirección de la relación
> 
> ### Ejemplos Físicos Específicos:
> 
> **1. Gráfica posición vs tiempo (x vs t)**:
> 
> ```
> Pendiente = Δx/Δt = velocidad promedio
> Unidades: [m]/[s] = m/s
> Interpretación: rapidez del movimiento
> ```
> 
> **2. Gráfica velocidad vs tiempo (v vs t)**:
> 
> ```
> Pendiente = Δv/Δt = aceleración promedio
> Unidades: [m/s]/[s] = m/s²
> Interpretación: cambio de velocidad en el tiempo
> ```
> 
> **3. Gráfica fuerza vs desplazamiento (F vs x)**:
> 
> ```
> Pendiente = ΔF/Δx = constante elástica k
> Unidades: [N]/[m] = N/m
> Interpretación: rigidez del resorte
> ```
> 
> **4. Gráfica período² vs longitud (T² vs L)**:
> 
> ```
> Pendiente = ΔT²/ΔL = 4π²/g
> Unidades: [s²]/[m] = s²/m
> Interpretación: permite calcular g = 4π²/pendiente
> ```
> 
> ### Sensibilidad y Precisión:
> 
> **Sensibilidad del sistema**:
> 
> - **Alta pendiente**: Cambio grande en y por pequeño cambio en x
> - **Baja pendiente**: Sistema poco sensible
> - **Cero**: Variable y independiente de x
> 
> **Precisión en la medición de pendiente**:
> 
> ```
> u_m ≈ √[(u_y₂² + u_y₁²)/(x₂ - x₁)² + m²(u_x₂² + u_x₁²)/(x₂ - x₁)²]
> ```

> [!tip]- **Significado Físico del Intercepto** 🎯
> 
> ### Interpretación General:
> 
> **Intercepto en y (b)**:
> 
> - **Definición**: Valor de y cuando x = 0
> - **Unidades**: Mismas que la variable dependiente
> - **Significado físico**: Depende del contexto
> 
> ### Casos Comunes:
> 
> **1. Condición inicial**:
> 
> ```
> x = x₀ + vt
> Intercepto = x₀ (posición inicial)
> ```
> 
> **2. Offset del instrumento**:
> 
> ```
> Lectura = Valor_real + Calibración
> Intercepto = error de calibración
> ```
> 
> **3. Valor basal o background**:
> 
> ```
> Señal_total = Señal_útil + Ruido_fondo
> Intercepto = nivel de ruido
> ```
> 
> **4. Valor teórico esperado**:
> 
> ```
> Para F = kx (Ley de Hooke)
> Intercepto teórico = 0
> Intercepto experimental ≠ 0 → investigar causas
> ```
> 
> ### Intercepto en x:
> 
> **Cálculo**: Hacer y = 0 y resolver para x
> 
> ```
> 0 = mx + b  →  x_intercepto = -b/m
> ```
> 
> **Interpretación física**: Valor de x donde y se anula
> 
> - Punto de equilibrio
> - Umbral de activación
> - Condición límite

> [!example]- **Ejemplo: Análisis de Pendiente e Intercepto** ⚖️
> 
> ### Experimento: Aceleración de un Carro
> 
> **Situación**: Un carro inicialmente en reposo acelera bajo fuerza constante. **Datos**: Gráfica velocidad vs tiempo
> 
> ```
> Ecuación del ajuste: v = 0.85t + 0.12
> Unidades: v en m/s, t en s
> ```
> 
> ### Análisis de la Pendiente:
> 
> **Valor**: m = 0.85 m/s² **Interpretación física**:
> 
> - La aceleración del carro es 0.85 m/s²
> - Por cada segundo que pasa, la velocidad aumenta en 0.85 m/s
> - Es constante (movimiento uniformemente acelerado)
> 
> **Comparación**:
> 
> ```
> Valor teórico esperado: a = F/m
> Si F = 8.5 N y m = 10 kg → a_teórica = 0.85 m/s²
> Concordancia excelente ✓
> ```
> 
> ### Análisis del Intercepto:
> 
> **Valor**: b = 0.12 m/s **Interpretación física**:
> 
> - El carro tenía una velocidad inicial de 0.12 m/s
> - **Problema**: Se suponía en reposo (v₀ = 0)
> 
> **Posibles causas del intercepto no nulo**:
> 
> 1. **Error de medición**: Calibración del sensor de velocidad
> 2. **Condiciones iniciales**: Carro no completamente en reposo
> 3. **Error sistemático**: Deriva del instrumento
> 4. **Modelo incompleto**: Fricción no considerada
> 
> **Acción correctiva**: Verificar calibración y repetir experimento
> 
> ### Cálculo del Intercepto en x:
> 
> ```
> x_intercepto = -b/m = -0.12/0.85 = -0.14 s
> ```
> 
> **Interpretación**: El carro habría estado en reposo 0.14 s antes del tiempo t = 0 **Significado físico**: Tiempo de referencia o sincronización del experimento

## 📏 Línea de Mejor Ajuste

> [!info]- **Métodos de Ajuste** 🎯
> 
> ### 1. Ajuste Visual (Manual):
> 
> **Procedimiento**:
> 
> 1. Dibujar una línea recta que pase "cerca" de la mayoría de los puntos
> 2. Balancear puntos por encima y por debajo de la línea
> 3. Dar más peso a puntos con menor incertidumbre
> 4. Evitar que outliers dominen el ajuste
> 
> **Ventajas**:
> 
> - Simple y rápido
> - Control visual directo
> - Útil para análisis preliminar
> 
> **Desventajas**:
> 
> - Subjetivo y no reproducible
> - No cuantifica la calidad del ajuste
> - No proporciona incertidumbres de parámetros
> 
> ### 2. Método de Mínimos Cuadrados:
> 
> **Principio**: Minimizar la suma de cuadrados de residuos
> 
> ```
> S = Σ(yᵢ - mxᵢ - b)² = mínimo
> ```
> 
> **Fórmulas para ajuste y = mx + b**:
> 
> ```
> m = [n·Σ(xᵢyᵢ) - Σ(xᵢ)·Σ(yᵢ)] / [n·Σ(xᵢ²) - (Σxᵢ)²]
> 
> b = [Σ(yᵢ) - m·Σ(xᵢ)] / n
> ```
> 
> donde n es el número de puntos de datos.
> 
> **Propiedades del ajuste por mínimos cuadrados**:
> 
> - La línea pasa por el punto (x̄, ȳ)
> - Suma de residuos es cero: Σ(yᵢ - ŷᵢ) = 0
> - Es el estimador no sesgado de mínima varianza
> - Asume errores solo en y, con varianza constante

> [!warning]- **Supuestos del Método de Mínimos Cuadrados** ⚠️
> 
> ### Condiciones para Validez:
> 
> **1. Linealidad**:
> 
> - La relación verdadera debe ser lineal
> - Verificar con inspección visual o análisis de residuos
> 
> **2. Independencia**:
> 
> - Las mediciones deben ser independientes
> - No debe haber correlación temporal o espacial
> 
> **3. Homocedasticidad**:
> 
> - Varianza constante en todos los puntos
> - Errores no deben aumentar/disminuir con x
> 
> **4. Normalidad de residuos**:
> 
> - Los errores siguen distribución normal
> - Importante para intervalos de confianza
> 
> **5. No hay errores en x**:
> 
> - Solo la variable y tiene incertidumbre
> - Si x también tiene error, usar regresión ortogonal
> 
> ### Verificación de Supuestos:
> 
> **Gráfica de residuos**:
> 
> ```
> Residuo = yᵢ - ŷᵢ (diferencia observado - predicho)
> Graficar: residuos vs valores predichos
> ```
> 
> **Patrones problemáticos**:
> 
> - **Forma de embudo**: Varianza no constante
> - **Curva sistemática**: Relación no lineal
> - **Puntos agrupados**: Falta de independencia
> - **Outliers evidentes**: Valores atípicos

> [!note]- **Cálculo de Incertidumbres** 📊
> 
> ### Incertidumbres de los Parámetros:
> 
> **Error estándar de la pendiente**:
> 
> ```
> u_m = s_y√[n/(n·Σxᵢ² - (Σxᵢ)²)]
> ```
> 
> **Error estándar del intercepto**:
> 
> ```
> u_b = s_y√[Σxᵢ²/(n·Σxᵢ² - (Σxᵢ)²)]
> ```
> 
> **Error estándar de la regresión**:
> 
> ```
> s_y = √[Σ(yᵢ - ŷᵢ)²/(n - 2)]
> ```
> 
> ### Intervalos de Confianza:
> 
> **Para los parámetros** (95% confianza):
> 
> ```
> m ± t₀.₀₂₅,n₋₂ · u_m
> b ± t₀.₀₂₅,n₋₂ · u_b
> ```
> 
> donde t₀.₀₂₅,n₋₂ es el valor crítico de la distribución t.
> 
> **Para predicciones**:
> 
> ```
> ŷ ± t₀.₀₂₅,n₋₂ · s_y√[1 + 1/n + (x - x̄)²/Σ(xᵢ - x̄)²]
> ```

> [!example]- **Ejemplo: Cálculo Completo de Ajuste** 📐
> 
> ### Datos: Ley de Hooke
> 
> ```
> x (cm): 2.0,  4.0,  6.0,  8.0,  10.0
> F (N):  1.1,  2.0,  2.9,  4.1,   5.0
> n = 5 puntos
> ```
> 
> ### Cálculos Intermedios:
> 
> ```
> Σxᵢ = 30.0        Σyᵢ = 15.1
> Σxᵢ² = 220.0      Σyᵢ² = 51.93
> Σxᵢyᵢ = 100.2     x̄ = 6.0    ȳ = 3.02
> ```
> 
> ### Parámetros de la Recta:
> 
> **Pendiente**:
> 
> ```
> m = [5×100.2 - 30.0×15.1] / [5×220.0 - (30.0)²]
> m = [501 - 453] / [1100 - 900] = 48/200 = 0.240 N/cm
> ```
> 
> **Intercepto**:
> 
> ```
> b = [15.1 - 0.240×30.0] / 5 = [15.1 - 7.2] / 5 = 1.58 N
> ```
> 
> **Ecuación del ajuste**: F = 0.240x + 1.58
> 
> ### Análisis de la Calidad del Ajuste:
> 
> **Cálculo de residuos**:
> 
> ```
> x=2: F_pred=2.06, residuo=1.1-2.06=-0.96
> x=4: F_pred=2.54, residuo=2.0-2.54=-0.54
> x=6: F_pred=3.02, residuo=2.9-3.02=-0.12
> x=8: F_pred=3.50, residuo=4.1-3.50=+0.60
> x=10: F_pred=3.98, residuo=5.0-3.98=+1.02
> ```
> 
> **Error estándar de la regresión**:
> 
> ```
> s_y = √[(0.96² + 0.54² + 0.12² + 0.60² + 1.02²)/(5-2)]
> s_y = √[2.55/3] = 0.92 N
> ```
> 
> ### Incertidumbres de los Parámetros:
> 
> **Error en la pendiente**:
> 
> ```
> u_m = 0.92√[5/(5×220-900)] = 0.92√[5/200] = 0.15 N/cm
> ```
> 
> **Error en el intercepto**:
> 
> ```
> u_b = 0.92√[220/(5×220-900)] = 0.92√[220/200] = 0.96 N
> ```
> 
> ### Resultado Final:
> 
> ```
> Pendiente: k = (0.24 ± 0.15) N/cm
> Intercepto: b = (1.6 ± 1.0) N
> 
> Interpretación física:
> - Constante elástica: k = 0.24 N/cm = 24 N/m
> - Intercepto no nulo sugiere precarga o error sistemático
> ```

## 📈 Coeficiente de Correlación

> [!info]- **Definición y Cálculo** 📢
> 
> ### Coeficiente de Correlación de Pearson:
> 
> **Fórmula**:
> 
> ```
> r = Σ(xᵢ - x̄)(yᵢ - ȳ) / √[Σ(xᵢ - x̄)²·Σ(yᵢ - ȳ)²]
> ```
> 
> **Forma alternativa para cálculo**:
> 
> ```
> r = [n·Σ(xᵢyᵢ) - Σ(xᵢ)·Σ(yᵢ)] / √[(n·Σxᵢ² - (Σxᵢ)²)·(n·Σyᵢ² - (Σyᵢ)²)]
> ```
> 
> ### Propiedades Fundamentales:
> 
> |Propiedad|Valor|Interpretación|
> |---|---|---|
> |**Rango**|-1 ≤ r ≤ +1|Siempre acotado|
> |**r = +1**|Correlación perfecta positiva|Todos los puntos en línea recta creciente|
> |**r = -1**|Correlación perfecta negativa|Todos los puntos en línea recta decreciente|
> |**r = 0**|No correlación lineal|Sin relación lineal aparente|
> |**Adimensional**|Sin unidades|Independiente de las escalas de x e y|
> 
> ### Interpretación Cualitativa:
> |r| ≥ 0.9:  Correlación muy fuerte
> 0.7 ≤ |r| < 0.9:  Correlación fuerte  
> 0.5 ≤ |r| < 0.7:  Correlación moderada
> 0.3 ≤ |r| < 0.5:  Correlación débil
> |r| < 0.3:  Correlación muy débil o nula
> 

> [!tip]- **Coeficiente de Determinación (R²)** 📊
> 
> ### Definición:
> 
> ```
> R² = r²  (cuadrado del coeficiente de correlación)
> ```
> 
> ### Interpretación Estadística:
> 
> **R² representa**:
> 
> - Fracción de la variabilidad en y explicada por x
> - Porcentaje de varianza explicada por el modelo lineal
> - Qué tan bien la línea de ajuste representa los datos
> 
> **Ejemplos de interpretación**:
> 
> ```
> R² = 0.81 (r = 0.90):
> "El 81% de la variabilidad en y se explica por x"
> "El modelo lineal explica 81% de los datos"
> ```
> 
> ### Relación con Error:
> 
> **Varianza total**:
> 
> ```
> SS_total = Σ(yᵢ - ȳ)²  (suma total de cuadrados)
> SS_regresión = Σ(ŷᵢ - ȳ)²  (explicada por el modelo)
> SS_residual = Σ(yᵢ - ŷᵢ)²  (no explicada)
> 
> R² = SS_regresión / SS_total = 1 - SS_residual / SS_total
> ```
> 
> ### Criterios de Calidad:
> 
> |R²|Interpretación|Uso recomendado|
> |---|---|---|
> |**R² > 0.95**|Excelente ajuste|Aceptar modelo lineal|
> |**0.80 < R² ≤ 0.95**|Buen ajuste|Modelo útil, verificar residuos|
> |**0.60 < R² ≤ 0.80**|Ajuste moderado|Considerar otros modelos|
> |**R² ≤ 0.60**|Ajuste pobre|Revisar modelo o datos|

> [!warning]- **Limitaciones del Coeficiente de Correlación** ⚠️
> 
> ### Lo que NO mide:
> 
> **1. Causalidad**:
> 
> - r alto no implica que x cause y
> - Pueden existir variables confundidas
> - Correlación ≠ Causación
> 
> **2. Relaciones no lineales**:
> 
> - r puede ser bajo para relaciones curvas fuertes
> - Ejemplo: y = x², r ≈ 0 cerca del origen
> - Solo detecta asociaciones lineales
> 
> **3. Efectos de outliers**:
> 
> - Un solo outlier puede cambiar dramáticamente r
> - Verificar siempre con gráfica de dispersión
> - Considerar correlación robusta si hay outliers
> 
> ### Casos Problemáticos:
> 
> **Correlación espuria**:
> 
> ```
> Variables no relacionadas físicamente pero correlacionadas
> Ejemplo: ventas de helado vs ahogamientos (ambos aumentan en verano)
> ```
> 
> **Restricción de rango**:
> 
> ```
> Si se mide solo una porción del rango, r puede aparecer bajo
> Ejemplo: altura vs peso solo en adultos vs toda la población
> ```
> 
> **Datos agrupados**:
> 
> ```
> Correlación alta entre grupos pero baja dentro de cada grupo
> Puede llevar a conclusiones erróneas sobre individuos
> ```

> [!example]- **Ejemplo: Cálculo del Coeficiente de Correlación** 📊
> 
> ### Datos del Experimento de Péndulo:
> 
> **Mediciones**: Período² vs Longitud
> 
> ```
> L (m):  0.20, 0.40, 0.60, 0.80, 1.00
> T² (s²): 0.81, 1.60, 2.41, 3.24, 4.05
> ```
> 
> ### Cálculos Intermedios:
> 
> ```
> n = 5
> Σxᵢ = 3.00       Σyᵢ = 12.11      x̄ = 0.60    ȳ = 2.422
> Σxᵢ² = 2.20      Σyᵢ² = 32.05
> Σxᵢyᵢ = 8.166
> ```
> 
> ### Cálculo del Coeficiente de Correlación:
> 
> ```
> Numerador: n·Σ(xᵢyᵢ) - Σ(xᵢ)·Σ(yᵢ)
>            = 5×8.166 - 3.00×12.11 = 40.83 - 36.33 = 4.50
> 
> Denominador: √[(n·Σxᵢ² - (Σxᵢ)²)·(n·Σyᵢ² - (Σyᵢ)²)]
>              = √[(5×2.20 - 9.00)·(5×32.05 - 146.65)]
>              = √[2.00 × 13.60] = √27.20 = 5.22
> 
> r = 4.50 / 5.22 = 0.862
> ```
> 
> ### Interpretación:
> 
> **Coeficiente de correlación**: r = 0.862 **Coeficiente de determinación**: R² = 0.743
> 
> **Significado**:
> 
> - Correlación fuerte y positiva entre L y T²
> - 74.3% de la variabilidad en T² se explica por L
> - Consistente con la teoría: T² = (4π²/g)L
> 
> ### Verificación Teórica:
> 
> **Para péndulo simple**: T = 2π√(L/g) **Predicción teórica**: r ≈ 1 (correlación perfecta) **Valor experimental**: r = 0.862
> 
> **Posibles causas de r < 1**:
> 
> - Errores experimentales aleatorios
> - Aproximación de pequeñas oscilaciones
> - Efectos de la masa del hilo
> - Resistencia del aire

## 🎯 Análisis Gráfico Avanzado

> [!info]- **Análisis de Residuos** 📈
> 
> ### Definición de Residuos:
> 
> ```
> Residuo = yᵢ - ŷᵢ = valor observado - valor predicho
> ```
> 
> ### Gráficas de Diagnóstico:
> 
> **1. Residuos vs Valores Predichos**:
> 
> - **Patrón aleatorio**: Buen ajuste lineal
> - **Patrón curvo**: Relación no lineal
> - **Forma de embudo**: Varianza no constante
> 
> **2. Residuos vs Variable Independiente**:
> 
> - Similar interpretación que la anterior
> - Útil para identificar tendencias sistemáticas
> 
> **3. Q-Q Plot de Residuos**:
> 
> - Verifica normalidad de los errores
> - Puntos en línea recta → distribución normal
> - Desviaciones sistemáticas → no normalidad
> 
> ### Criterios de Calidad:
> 
> **Residuos "bien comportados"**:
> 
> ```
> - Media ≈ 0
> - Desviación estándar constante
> - Distribución aproximadamente normal
> - Sin patrones sistemáticos
> - Sin outliers extremos
> ```

> [!note]- **Linealización de Relaciones** 🔄
> 
> ### Técnicas Comunes:
> 
> **1. Relación Exponencial**: y = ae^(bx)
> 
> ```
> Linealización: ln(y) = ln(a) + bx
> Gráfica: ln(y) vs x
> Pendiente = b, Intercepto = ln(a)
> ```
> 
> **2. Relación Potencial**: y = ax^n
> 
> ```
> Linealización: log(y) = log(a) + n·log(x)
> Gráfica: log(y) vs log(x)
> Pendiente = n, Intercepto = log(a)
> ```
> 
> **3. Relación Recíproca**: y = a/(x + b)
> 
> ```
> Linealización: 1/y = b/a · (1/x) + 1/a
> Gráfica: 1/y vs 1/x
> ```
> 
> **4. Ley de Enfriamiento**: T = T∞ + (T₀ - T∞)e^(-kt)
> 
> ```
> Linealización: ln(T - T∞) = ln(T₀ - T∞) - kt
> Gráfica: ln(T - T∞) vs t
> ```
> 
> ### Ejemplo: Péndulo Simple
> 
> **Relación teórica**: T = 2π√(L/g) **Elevando al cuadrado**: T² = (4π²/g)L **Forma lineal**: T² = (4π²/g)L + 0
> 
> **Parámetros**:
> 
> - Variable independiente: L
> - Variable dependiente: T²
> - Pendiente: 4π²/g → permite calcular g
> - Intercepto teórico: 0

## 🔬 Aplicaciones en Física Experimental

> [!info]- **Casos de Estudio** 🧪
> 
> ### 1. Verificación de la Ley de Hooke
> 
> **Objetivo**: Determinar constante elástica k **Gráfica**: F vs x (fuerza vs desplazamiento) **Ecuación**: F = kx
> 
> **Análisis esperado**:
> 
> - Pendiente = k (constante elástica)
> - Intercepto = 0 (sin precarga)
> - r ≈ 1 (relación lineal perfecta)
> 
> **Desviaciones comunes**:
> 
> - Intercepto ≠ 0: Precarga o error de calibración
> - r < 0.95: Deformación plástica, no linealidad
> - Curvatura: Límites de la región elástica
> 
> ### 2. Determinación de la Gravedad
> 
> **Método del péndulo**:
> 
> - Gráfica: T² vs L
> - Ecuación: T² = (4π²/g)L
> - Pendiente = 4π²/g → g = 4π²/pendiente
> 
> **Método de caída libre**:
> 
> - Gráfica: h vs t²
> - Ecuación: h = h₀ + ½gt²
> - Pendiente = ½g → g = 2×pendiente
> 
> ### 3. Ley de Ohm
> 
> **Gráfica**: V vs I (voltaje vs corriente) **Ecuación**: V = RI **Análisis**:
> 
> - Pendiente = R (resistencia)
> - Intercepto = 0 (elemento óhmico ideal)
> - Linealidad confirma comportamiento óhmico
> 
> ### 4. Capacitor Descargándose
> 
> **Relación**: V(t) = V₀e^(-t/RC) **Linealización**: ln(V) = ln(V₀) - t/(RC) **Gráfica**: ln(V) vs t **Análisis**:
> 
> - Pendiente = -1/(RC)
> - Intercepto = ln(V₀)
> - Permite determinar constante de tiempo τ = RC

> [!example]- **Ejemplo Integral: Análisis Completo** 🔬
> 
> ### Experimento: Viscosidad por Ley de Stokes
> 
> **Objetivo**: Determinar coeficiente de viscosidad η **Teoría**: v = (2gr²/9η)(ρ_esfera - ρ_fluido) **Método**: Medir velocidad terminal vs radio de esferas
> 
> ### Datos Experimentales:
> 
> ```
> r (mm): 0.5, 1.0, 1.5, 2.0, 2.5, 3.0
> v (m/s): 0.012, 0.045, 0.098, 0.175, 0.269, 0.385
> Incertidumbres: u_r = ±0.05 mm, u_v = ±0.005 m/s
> ```
> 
> ### Linealización:
> 
> **Predicción teórica**: v ∝ r² **Gráfica**: v vs r² **Forma lineal**: v = (2g/9η)(ρ_esfera - ρ_fluido) × r²
> 
> ### Construcción de la Gráfica:
> 
> **Variables transformadas**:
> 
> ```
> x = r² (mm²): 0.25, 1.00, 2.25, 4.00, 6.25, 9.00
> y = v (m/s): 0.012, 0.045, 0.098, 0.175, 0.269, 0.385
> ```
> 
> **Elementos gráficos**:
> 
> - Título: "Velocidad Terminal vs Cuadrado del Radio - Esferas en Glicerina"
> - Eje X: "Radio², r² (mm²)"
> - Eje Y: "Velocidad terminal, v (m/s)"
> - Escala X: 0 a 10 mm², intervalos de 1 mm²
> - Escala Y: 0 a 0.4 m/s, intervalos de 0.05 m/s
> 
> ### Análisis de Regresión:
> 
> **Cálculos**:
> 
> ```
> n = 6, Σx = 22.75, Σy = 0.984
> Σx² = 123.06, Σy² = 0.225, Σxy = 5.29
> 
> m = [6×5.29 - 22.75×0.984] / [6×123.06 - (22.75)²]
>   = [31.74 - 22.39] / [738.36 - 517.56] = 0.0424 m/s·mm⁻²
> 
> b = [0.984 - 0.0424×22.75] / 6 = -0.0006 m/s
> 
> Ecuación: v = 0.0424r² - 0.0006
> ```
> 
> ### Evaluación de la Calidad:
> 
> **Coeficiente de correlación**:
> 
> ```
> r = 0.9987 → R² = 0.9974
> ```
> 
> **Interpretación**:
> 
> - Correlación casi perfecta (r > 0.99)
> - 99.74% de variabilidad explicada
> - Intercepto ≈ 0 (consistente con teoría)
> - Excelente validación de v ∝ r²
> 
> ### Cálculo de Parámetros Físicos:
> 
> **De la pendiente**:
> 
> ```
> Pendiente = (2g/9η)(ρ_esfera - ρ_fluido)
> 0.0424 = (2×9.81/9η)(ρ_acero - ρ_glicerina)
> 
> Con ρ_acero = 7800 kg/m³, ρ_glicerina = 1260 kg/m³:
> η = (2×9.81×6540) / (9×0.0424) = 3.36 Pa·s
> ```
> 
> **Comparación**:
> 
> ```
> Valor experimental: η = 3.36 Pa·s
> Valor de literatura: η = 3.18 Pa·s
> Error relativo: |3.36 - 3.18|/3.18 = 5.7%
> ```

## ⚠️ Errores Comunes y Precauciones

> [!warning]- **Errores Frecuentes en Construcción** ❌
> 
> 1. **Escalas inapropiadas**:
>     - ❌ Usar escalas que no permiten ver tendencias
>     - ❌ Intervalos difíciles de leer (3, 7, 11...)
>     - ✅ Escalas que usen todo el espacio disponible
> 2. **Ejes mal etiquetados**:
>     - ❌ "x" en lugar de "Tiempo, t (s)"
>     - ❌ Omitir unidades
>     - ✅ Incluir nombre de variable, símbolo y unidades
> 3. **Conectar puntos experimentales**:
>     - ❌ Líneas quebradas conectando cada punto
>     - ✅ Puntos individuales + línea de mejor ajuste suave
> 4. **Forzar paso por el origen**:
>     - ❌ Forzar b = 0 sin justificación teórica
>     - ✅ Permitir que los datos determinen el intercepto
> 5. **Ignorar barras de error**:
>     - ❌ No mostrar incertidumbres experimentales
>     - ✅ Incluir barras de error cuando sean significativas

> [!warning]- **Errores en Interpretación** ⚠️
> 
> 6. **Confundir correlación con causalidad**:
>     - r alto no implica que x cause y
>     - Pueden existir variables ocultas
> 7. **Extrapolar más allá de los datos**:
>     - La linealidad solo se verificó en el rango medido
>     - Extrapolación puede no ser válida
> 8. **Asumir linealidad sin verificar**:
>     - Siempre inspeccionar visualmente
>     - Verificar con análisis de residuos
> 9. **Malinterpretar R²**:
>     - R² alto no garantiza modelo correcto
>     - Puede haber modelos mejores con R² similar
> 10. **Ignorar outliers**:
>     - Un outlier puede cambiar completamente el ajuste
>     - Investigar causas antes de eliminar datos

## 🧮 Herramientas Computacionales

> [!info]- **Software para Gráficas** 💻
> 
> ### Software Científico Especializado:
> 
> |Software|Ventajas|Uso típico|Costo|
> |---|---|---|---|
> |**Excel**|Familiar, accesible|Análisis básico, reportes|Comercial|
> |**Origin**|Gráficas de alta calidad|Publicaciones científicas|Comercial|
> |**Python (matplotlib)**|Programable, flexible|Análisis automatizado|Gratuito|
> |**R (ggplot2)**|Estadísticas avanzadas|Análisis estadístico|Gratuito|
> |**GraphPad Prism**|Interface intuitiva|Ciencias biológicas|Comercial|
> |**SigmaPlot**|Gráficas científicas|Ingeniería|Comercial|
> 
> ### Funciones de Excel para Regresión Lineal:
> 
> **Funciones básicas**:
> - `SLOPE(rango_y, rango_x)` → Calcula la pendiente
> - `INTERCEPT(rango_y, rango_x)` → Calcula el intercepto
> - `CORREL(rango_y, rango_x)` → Coeficiente de correlación
> - `RSQ(rango_y, rango_x)` → Coeficiente de determinación R²
> - `LINEST(rango_y, rango_x)` → Estadísticas completas del ajuste
> 
> **Para análisis de incertidumbres**:
> - `STEYX(rango_y, rango_x)` → Error estándar de la estimación
> - `LINEST` con parámetros adicionales → Errores estándar de los parámetros

## 📚 Referencias y Conexiones

> [!quote]- **Notas Relacionadas**
> 
> - [[Estadística Básica]] - Fundamento matemático
> - [[Incertidumbres Experimentales]] - Análisis de errores
> - [[Regresión No Lineal]] - Extensiones avanzadas
> - [[Análisis de Datos]] - Marco general

## 🎯 Ejercicios y Problemas

> [!example]- **Problema Tipo: Análisis Completo** 📐
> 
> ### Enunciado:
> 
> Un estudiante estudia el movimiento de un péndulo midiendo el período T para diferentes longitudes L. Sus datos son:
> 
> ```
> L (m):  0.25, 0.50, 0.75, 1.00, 1.25, 1.50
> T (s):  1.01, 1.43, 1.74, 2.01, 2.25, 2.47
> ```
> 
> **Tareas**:
> 
> 1. Construir gráfica T² vs L
> 2. Calcular línea de mejor ajuste
> 3. Determinar coeficiente de correlación
> 4. Calcular valor de g y su incertidumbre
> 5. Evaluar calidad del ajuste
> 
> ### Solución Parcial:
> 
> **1. Preparación de datos**:
> 
> ```
> L (m):   0.25, 0.50, 0.75, 1.00, 1.25, 1.50
> T² (s²): 1.02, 2.04, 3.03, 4.04, 5.06, 6.10
> ```
> 
> **2. Regresión lineal**:
> 
> ```
> Pendiente: m = 4.01 s²/m
> Intercepto: b = 0.08 s²
> Correlación: r = 0.9996
> ```
> 
> **3. Cálculo de g**:
> 
> ```
> m = 4π²/g → g = 4π²/m = 39.48/4.01 = 9.85 m/s²
> Error: |9.85 - 9.81|/9.81 = 0.4%
> ```
> 
> **Conclusión**: Excelente verificación experimental de la ley del péndulo.

## 📝 Notas Recomendadas

> [!note]- **Prerrequisitos**
> 
> - [[Estadística Básica]] - Media, desviación estándar
> - **Álgebra**: Ecuaciones lineales, sistemas
> - **Geometría**: Conceptos de pendiente y ángulos

> [!note]- **Temas Siguientes**
> 
> - [[Regresión No Lineal]] - Modelos más complejos
> - [[Análisis de Series Temporales]] - Datos en función del tiempo
> - [[Diseño de Experimentos]] - Planificación estadística
> - [[Validación de Modelos]] - Verificación de hipótesis

---

**Tags:** #graficas-lineales #regresion-lineal #pendiente #intercepto #correlacion #minimos-cuadrados #analisis-grafico #fisica-experimental #visualizacion-datos #modelado-matematico
