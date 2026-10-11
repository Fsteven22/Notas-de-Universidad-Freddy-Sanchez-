---
dg-publish: true
---

# Estadística Básica

> [!quote] "En cada medición repetida se esconde una historia que solo la estadística puede revelar." 📊

> [!info] La estadística básica proporciona las herramientas fundamentales para analizar datos experimentales en física. Permite extraer información significativa de conjuntos de mediciones, cuantificar la dispersión de los datos y establecer intervalos de confianza. Estas técnicas son esenciales para validar hipótesis y reportar resultados con rigor científico.

## 🔧 Conceptos Fundamentales

> [!info] **Población vs Muestra** 🎯
> 
> ### Definiciones Básicas:
> 
> |Concepto|Definición|Símbolo|Ejemplo|
> |---|---|---|---|
> |**Población**|Conjunto completo de datos de interés|N|Todas las mediciones posibles de g|
> |**Muestra**|Subconjunto de la población que medimos|n|20 mediciones de g en el laboratorio|
> |**Parámetro**|Característica de la población|μ, σ|Valor verdadero de g = 9.81 m/s²|
> |**Estadístico**|Característica calculada de la muestra|x̄, s|Promedio observado ḡ = 9.83 m/s²|
> 
> ### Tipos de Variables:
> 
> **Variables Continuas**:
> 
> - Pueden tomar cualquier valor en un intervalo
> - Ejemplos: longitud, tiempo, masa, temperatura
> - Se miden con instrumentos (regla, cronómetro, balanza)
> 
> **Variables Discretas**:
> 
> - Solo pueden tomar valores específicos
> - Ejemplos: número de oscilaciones, número de mediciones
> - Se cuentan directamente
> 
> ### Escalas de Medición:
> 
> |Escala|Características|Operaciones Válidas|Ejemplo Físico|
> |---|---|---|---|
> |**Razón**|Cero absoluto, razones significativas|+, -, ×, ÷|Masa, longitud, tiempo|
> |**Intervalo**|Diferencias significativas, sin cero absoluto|+, -|Temperatura en °C|
> |**Ordinal**|Solo orden relativo|Comparaciones|Dureza de materiales|
> |**Nominal**|Solo clasificación|Conteos|Tipo de material|

> [!tip] **Distribución de Datos** 📈
> 
> ### Formas de Distribución:
> 
> **Simétrica (Normal)**:
> 
> - Media = Mediana = Moda
> - Forma de campana
> - Común en mediciones físicas
> 
> **Asimétrica Positiva**:
> 
> - Media > Mediana > Moda
> - Cola hacia valores altos
> - Ejemplo: tiempos de reacción
> 
> **Asimétrica Negativa**:
> 
> - Media < Mediana < Moda
> - Cola hacia valores bajos
> - Menos común en física
> 
> ### Indicadores de Distribución:
> 
> ```
> Asimetría = 0: Distribución simétrica
> Asimetría > 0: Asimétrica positiva
> Asimetría < 0: Asimétrica negativa
> 
> Curtosis = 3: Distribución normal
> Curtosis > 3: Más puntiaguda (leptocúrtica)
> Curtosis < 3: Más plana (platicúrtica)
> ```

## 📊 Media Aritmética

> [!info] **Definición y Cálculo** 🎯
> 
> ### Fórmula Fundamental:
> 
> **Para una muestra**:
> 
> ```
> x̄ = (x₁ + x₂ + x₃ + ... + xₙ)/n = (1/n)∑ᵢ₌₁ⁿ xᵢ
> ```
> 
> **Para una población**:
> 
> ```
> μ = (1/N)∑ᵢ₌₁ᴺ xᵢ
> ```
> 
> ### Propiedades Matemáticas:
> 
> |Propiedad|Fórmula|Interpretación|
> |---|---|---|
> |**Linealidad**|x̄ + ȳ = (x + y)‾|Media de suma = suma de medias|
> |**Escalamiento**|kx̄ = k·x̄|Constante sale del promedio|
> |**Mínimos Cuadrados**|∑(xᵢ - x̄)² es mínimo|x̄ minimiza la suma de desviaciones²|
> |**Suma de Desviaciones**|∑(xᵢ - x̄) = 0|Las desviaciones se cancelan|
> 
> ### Interpretación Física:
> 
> **Centro de masa estadístico**:
> 
> - La media es el "punto de equilibrio" de los datos
> - Análoga al centro de masa en mecánica
> - Sensible a valores extremos (outliers)

> [!example] **Ejemplo: Mediciones de Gravedad** ⚖️
> 
> ### Datos Experimentales:
> 
> Mediciones de g (m/s²): 9.78, 9.82, 9.80, 9.84, 9.79, 9.81, 9.83, 9.77, 9.85, 9.80
> 
> ### Cálculo Paso a Paso:
> 
> **Suma total**:
> 
> ```
> ∑xᵢ = 9.78 + 9.82 + 9.80 + 9.84 + 9.79 + 9.81 + 9.83 + 9.77 + 9.85 + 9.80
> ∑xᵢ = 98.09 m/s²
> ```
> 
> **Número de datos**: n = 10
> 
> **Media aritmética**:
> 
> ```
> ḡ = ∑xᵢ/n = 98.09/10 = 9.809 m/s²
> ```
> 
> ### Verificación:
> 
> **Suma de desviaciones**:
> 
> ```
> ∑(gᵢ - ḡ) = (9.78-9.809) + (9.82-9.809) + ... + (9.80-9.809)
> ∑(gᵢ - ḡ) = -0.029 + 0.011 + ... + (-0.009) ≈ 0 ✓
> ```
> 
> ### Análisis:
> 
> - **Resultado**: ḡ = 9.809 m/s²
> - **Diferencia con valor teórico**: |9.809 - 9.81| = 0.001 m/s²
> - **Conclusión**: Excelente concordancia con el valor esperado

> [!warning] **Limitaciones y Consideraciones** ⚠️
> 
> ### Sensibilidad a Outliers:
> 
> **Ejemplo**: Si una medición fuera 10.20 m/s² en lugar de 9.80 m/s²:
> 
> ```
> Nueva suma = 98.49 m/s²
> Nueva media = 9.849 m/s²
> Cambio = +0.040 m/s² (4% de error por un solo outlier)
> ```
> 
> ### Alternativas Robustas:
> 
> |Medida|Fórmula|Resistencia a Outliers|Uso|
> |---|---|---|---|
> |**Media**|∑xᵢ/n|Baja|Distribuciones normales|
> |**Mediana**|Valor central ordenado|Alta|Distribuciones asimétricas|
> |**Media Truncada**|Media sin extremos|Media|Datos con algunos outliers|
> |**Media Ponderada**|∑(wᵢxᵢ)/∑wᵢ|Depende de pesos|Diferentes precisiones|
> 
> ### Cuándo NO usar la Media:
> 
> - **Distribuciones muy asimétricas**: Usar mediana
> - **Presencia de outliers**: Investigar y posiblemente excluir
> - **Datos categóricos**: Sin sentido matemático
> - **Escalas no lineales**: Considerar media geométrica

## 📏 Desviación Estándar

> [!info] **Concepto y Cálculo** 📐
> 
> ### Definiciones Fundamentales:
> 
> **Varianza de la muestra**:
> 
> ```
> s² = ∑(xᵢ - x̄)²/(n-1)
> ```
> 
> **Desviación estándar de la muestra**:
> 
> ```
> s = √[∑(xᵢ - x̄)²/(n-1)]
> ```
> 
> **Varianza de la población**:
> 
> ```
> σ² = ∑(xᵢ - μ)²/N
> ```
> 
> **Desviación estándar de la población**:
> 
> ```
> σ = √[∑(xᵢ - μ)²/N]
> ```
> 
> ### ¿Por qué n-1? (Corrección de Bessel):
> 
> **Grados de libertad**:
> 
> - Con n datos y conociendo x̄, solo (n-1) datos son independientes
> - El último dato está determinado por los otros (n-1) y la media
> - Usar n subestimaría la variabilidad poblacional
> - **Regla práctica**: Para n > 30, la diferencia es mínima

> [!tip] **Interpretación Física** 🎯
> 
> ### Significado Geométrico:
> 
> **Dispersión como "radio estadístico"**:
> 
> - σ representa la "distancia típica" desde la media
> - Análogo al radio de giro en mecánica
> - Mayor σ = datos más dispersos
> - Menor σ = datos más concentrados alrededor de la media
> 
> ### Unidades:
> 
> - **Varianza**: [Variable]² (ejemplo: m² para longitudes)
> - **Desviación estándar**: [Variable] (ejemplo: m para longitudes)
> - La desviación estándar tiene las mismas unidades que los datos originales
> 
> ### Regla Empírica (Para distribuciones normales):
> 
> ```
> ~68% de los datos están en [μ - σ, μ + σ]
> ~95% de los datos están en [μ - 2σ, μ + 2σ]
> ~99.7% de los datos están en [μ - 3σ, μ + 3σ]
> ```

> [!example] **Ejemplo: Cálculo Detallado** 📊
> 
> ### Datos: Período de un Péndulo
> 
> Mediciones T (s): 2.01, 1.98, 2.03, 1.99, 2.02, 2.00, 2.04, 1.97, 2.01, 1.95
> 
> ### Paso 1: Calcular la Media
> 
> ```
> T̄ = (2.01 + 1.98 + 2.03 + 1.99 + 2.02 + 2.00 + 2.04 + 1.97 + 2.01 + 1.95)/10
> T̄ = 20.00/10 = 2.000 s
> ```
> 
> ### Paso 2: Calcular Desviaciones
> 
> |i|Tᵢ (s)|Tᵢ - T̄ (s)|(Tᵢ - T̄)² (s²)|
> |---|---|---|---|
> |1|2.01|+0.010|0.000100|
> |2|1.98|-0.020|0.000400|
> |3|2.03|+0.030|0.000900|
> |4|1.99|-0.010|0.000100|
> |5|2.02|+0.020|0.000400|
> |6|2.00|0.000|0.000000|
> |7|2.04|+0.040|0.001600|
> |8|1.97|-0.030|0.000900|
> |9|2.01|+0.010|0.000100|
> |10|1.95|-0.050|0.002500|
> |**Suma**|-|0.000|**0.007000**|
> 
> ### Paso 3: Calcular Varianza y Desviación Estándar
> 
> ```
> s² = ∑(Tᵢ - T̄)²/(n-1) = 0.007000/9 = 0.000778 s²
> s = √(0.000778) = 0.0279 s ≈ 0.028 s
> ```
> 
> ### Paso 4: Análisis del Resultado
> 
> **Período del péndulo**: T = (2.000 ± 0.028) s **Coeficiente de variación**: CV = s/T̄ = 0.028/2.000 = 1.4% **Interpretación**: Los datos muestran poca dispersión (CV < 5%)

> [!note] **Fórmulas Alternativas de Cálculo** 🧮
> 
> ### Fórmula de Cálculo Rápido:
> 
> **Para evitar errores de redondeo**:
> 
> ```
> s² = [∑xᵢ² - (∑xᵢ)²/n]/(n-1)
> ```
> 
> ### Desviación Estándar de la Media:
> 
> **Error estándar**:
> 
> ```
> σₓ̄ = σ/√n  (población conocida)
> sₓ̄ = s/√n   (muestra)
> ```
> 
> **Interpretación**: La precisión de la media mejora con √n
> 
> ### Desviación Estándar Ponderada:
> 
> **Cuando las mediciones tienen diferentes precisiones**:
> 
> ```
> s²ᵨ = ∑wᵢ(xᵢ - x̄ᵨ)²/∑wᵢ
> donde wᵢ = 1/uᵢ² (peso inversamente proporcional a la incertidumbre)
> ```
> 
> ### Desviación Estándar Pooled:
> 
> **Para combinar múltiples muestras**:
> 
> ```
> s²ₚ = [(n₁-1)s₁² + (n₂-1)s₂²]/[(n₁-1) + (n₂-1)]
> ```

## 🔔 Distribución Normal

> [!info] **Características Fundamentales** 📊
> 
> ### Función de Densidad:
> 
> ```
> f(x) = (1/σ√2π) exp[-(x-μ)²/(2σ²)]
> ```
> 
> **Parámetros**:
> 
> - **μ**: Media (centro de la distribución)
> - **σ**: Desviación estándar (dispersión)
> - **σ²**: Varianza
> 
> ### Propiedades Clave:
> 
> |Propiedad|Descripción|Valor|
> |---|---|---|
> |**Forma**|Campana simétrica|Bell curve|
> |**Centro**|Media = Mediana = Moda|x = μ|
> |**Dispersión**|Determinada por σ|68-95-99.7 rule|
> |**Asimetría**|Perfectamente simétrica|Skewness = 0|
> |**Curtosis**|Forma estándar|Kurtosis = 3|
> |**Área total**|Probabilidad total|∫f(x)dx = 1|
> 
> ### Notación Estándar:
> 
> ```
> X ~ N(μ, σ²)  "X sigue una distribución normal con media μ y varianza σ²"
> ```

> [!tip] **Regla 68-95-99.7** 📏
> 
> ### Intervalos de Confianza:
> 
> **Para una distribución N(μ, σ)**:
> 
> ```
> P(μ - σ ≤ X ≤ μ + σ) ≈ 0.6827 (68.27%)
> P(μ - 2σ ≤ X ≤ μ + 2σ) ≈ 0.9545 (95.45%)
> P(μ - 3σ ≤ X ≤ μ + 3σ) ≈ 0.9973 (99.73%)
> ```
> 
> ### Interpretación Práctica:
> 
> **En mediciones físicas**:
> 
> - **1σ**: Rango de variabilidad típica
> - **2σ**: Intervalo de confianza común (≈95%)
> - **3σ**: Valores extremos raros (<0.3% de probabilidad)
> 
> ### Detección de Outliers:
> 
> **Criterio 3σ**:
> 
> - Si |x - μ| > 3σ → Posible outlier
> - Probabilidad < 0.3% de ocurrencia natural
> - **Investigar**: ¿Error experimental o fenómeno real?
> 
> ### Aplicación en Control de Calidad:
> 
> ```
> Límite de control superior: μ + 3σ
> Límite de control inferior: μ - 3σ
> Línea central: μ
> ```

> [!warning] **Distribución Normal Estándar** 📈
> 
> ### Transformación Z:
> 
> **Estandarización**:
> 
> ```
> Z = (X - μ)/σ
> ```
> 
> **Propiedades de Z ~ N(0,1)**:
> 
> - Media = 0
> - Desviación estándar = 1
> - Permite usar tablas estándar
> 
> ### Valores Críticos Importantes:
> 
> |Confianza|Z crítico|Interpretación|
> |---|---|---|
> |90%|±1.645|Intervalos de confianza común|
> |95%|±1.960|Estándar científico|
> |99%|±2.576|Alta confianza|
> |99.9%|±3.291|Muy alta confianza|
> 
> ### Cálculo de Probabilidades:
> 
> **Para encontrar P(a ≤ X ≤ b)**:
> 
> ```
> Z₁ = (a - μ)/σ
> Z₂ = (b - μ)/σ
> P(a ≤ X ≤ b) = Φ(Z₂) - Φ(Z₁)
> ```
> 
> donde Φ es la función de distribución acumulativa estándar.

> [!example] **Ejemplo: Análisis de Mediciones** 🔬
> 
> ### Situación Experimental:
> 
> Un estudiante mide la constante elástica k de un resorte 50 veces y obtiene:
> 
> - **Media**: k̄ = 125.3 N/m
> - **Desviación estándar**: s = 3.2 N/m
> - **Distribución**: Aproximadamente normal
> 
> ### Análisis Estadístico:
> 
> **Intervalos de confianza**:
> 
> ```
> 68%: k ∈ [125.3 - 3.2, 125.3 + 3.2] = [122.1, 128.5] N/m
> 95%: k ∈ [125.3 - 2×3.2, 125.3 + 2×3.2] = [118.9, 131.7] N/m
> 99.7%: k ∈ [125.3 - 3×3.2, 125.3 + 3×3.2] = [115.7, 134.9] N/m
> ```
> 
> ### Detección de Outliers:
> 
> **Si se observa k = 140.0 N/m**:
> 
> ```
> Z = (140.0 - 125.3)/3.2 = 4.59
> ```
> 
> **Análisis**: |Z| = 4.59 > 3 → Outlier muy probable **Acción**: Investigar la medición (¿error experimental?)
> 
> ### Probabilidad de Eventos:
> 
> **¿Cuál es la probabilidad de medir k > 130 N/m?**
> 
> ```
> Z = (130 - 125.3)/3.2 = 1.47
> P(k > 130) = P(Z > 1.47) ≈ 0.071 = 7.1%
> ```
> 
> **Interpretación**: Aproximadamente 1 de cada 14 mediciones será mayor a 130 N/m.

> [!success] 🔗 Proceso de Análisis Estadístico
> 
> ```mermaid
> graph TD
>     A[Recopilar Datos Experimentales] --> B[Calcular Media Aritmética]
>     B --> C[Calcular Desviación Estándar]
>     C --> D[Verificar Normalidad]
>     D --> E{¿Distribución Normal?}
>     E -->|Sí| F[Aplicar Regla 68-95-99.7]
>     E -->|No| G[Usar Estadísticas No Paramétricas]
>     F --> H[Establecer Intervalos de Confianza]
>     G --> H
>     H --> I[Detectar Outliers]
>     I --> J[Reportar Resultados]
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
>     style E fill:#fce4ec
>     style F fill:#f1f8e9
>     style G fill:#ffebee
>     style H fill:#e0f2f1
>     style I fill:#f3e5f5
>     style J fill:#e1f5fe
> ```

## 🧮 Pruebas de Normalidad

> [!note] **Verificación de Supuestos** 📊
> 
> ### Métodos Gráficos:
> 
> **Histograma**:
> 
> - Forma de campana aproximada
> - Simétrico alrededor de la media
> - Sin colas muy largas
> 
> **Q-Q Plot (Quantile-Quantile)**:
> 
> - Gráfica cuantiles observados vs teóricos
> - Puntos cerca de la línea diagonal → Normalidad
> - Desviaciones sistemáticas → No normalidad
> 
> **Gráfica de Probabilidad Normal**:
> 
> - Versión específica del Q-Q plot
> - Escala modificada para facilitar interpretación
> 
> ### Pruebas Estadísticas:
> 
> |Prueba|Tamaño de muestra|Poder|Uso recomendado|
> |---|---|---|---|
> |**Shapiro-Wilk**|n ≤ 50|Alto|Muestras pequeñas|
> |**Anderson-Darling**|n > 50|Alto|Muestras grandes|
> |**Kolmogorov-Smirnov**|n > 50|Medio|Uso general|
> |**Jarque-Bera**|n > 30|Medio|Basado en asimetría/curtosis|
> 
> ### Criterios de Decisión:
> 
> **Nivel de significancia típico**: α = 0.05
> 
> - **p-valor > 0.05**: No rechazar normalidad
> - **p-valor ≤ 0.05**: Evidencia contra normalidad
> 
> ### Alternativas si No es Normal:
> 
> **Transformaciones de datos**:
> 
> - **Logarítmica**: Para asimetría positiva
> - **Raíz cuadrada**: Para datos de conteo
> - **Box-Cox**: Transformación general
> 
> **Estadística no paramétrica**:
> 
> - **Mediana** en lugar de media
> - **Rango intercuartil** en lugar de desviación estándar
> - **Pruebas de rango** en lugar de pruebas t

## 🎯 Aplicaciones en Física Experimental

> [!info] **Casos de Estudio Típicos** 🔬
> 
> ### Mediciones de Constantes Físicas:
> 
> **Gravedad terrestre (g)**:
> 
> - Múltiples mediciones con péndulo
> - Distribución normal esperada
> - Identificar errores sistemáticos vs aleatorios
> 
> **Velocidad de la luz (c)**:
> 
> - Experimentos históricos de Michelson
> - Análisis de precisión y exactitud
> - Evolución de la incertidumbre
> 
> **Constante de Planck (h)**:
> 
> - Experimento del efecto fotoeléctrico
> - Regresión lineal con incertidumbres
> - Propagación de errores estadísticos
> 
> ### Análisis de Instrumentación:
> 
> **Calibración de instrumentos**:
> 
> - Repetibilidad y reproducibilidad
> - Deriva temporal de las mediciones
> - Límites de detección estadísticos
> 
> **Comparación de métodos**:
> 
> - Pruebas t para medias
> - Pruebas F para varianzas
> - Análisis de concordancia
> 
> ### Control de Calidad:
> 
> **Gráficos de control**:
> 
> - Límites 3σ para detección de anomalías
> - Tendencias y patrones sistemáticos
> - Capacidad de proceso

> [!example] **Ejemplo Integral: Experimento de Caída Libre** 🏃‍♂️
> 
> ### Diseño Experimental:
> 
> **Objetivo**: Determinar g mediante caída libre **Método**: Medir tiempo de caída desde altura h = 2.00 m **Instrumentación**: Cronómetro digital (precisión ±0.01 s) **Réplicas**: n = 25 mediciones
> 
> ### Datos Experimentales (tiempos en segundos):
> 
> ```
> 0.64, 0.65, 0.63, 0.66, 0.64, 0.65, 0.62, 0.67, 0.64, 0.63,
> 0.65, 0.66, 0.64, 0.65, 0.63, 0.66, 0.67, 0.64, 0.65, 0.63,
> 0.66, 0.64, 0.65, 0.62, 0.67
> ```
> 
> ### Análisis Estadístico Completo:
> 
> **Paso 1: Media Aritmética**
> 
> ```
> t̄ = ∑tᵢ/n = 16.13/25 = 0.645 s
> ```
> 
> **Paso 2: Desviación Estándar**
> 
> ```
> s = √[∑(tᵢ - t̄)²/(n-1)] = 0.0154 s
> ```
> 
> **Paso 3: Cálculo de g**
> 
> ```
> g = 2h/t̄² = 2(2.00)/(0.645)² = 9.61 m/s²
> ```
> 
> **Paso 4: Propagación de Incertidumbres**
> 
> ```
> ∂g/∂t = -4h/t³ = -4(2.00)/(0.645)³ = -29.8 m/s³
> u_g = |∂g/∂t| × s_t̄ = 29.8 × (0.0154/√25) = 0.092 m/s²
> ```
> 
> **Paso 5: Verificación de Normalidad**
> 
> - Histograma: Forma aproximadamente normal
> - Prueba Shapiro-Wilk: p = 0.342 > 0.05 ✓
> 
> **Paso 6: Intervalos de Confianza**
> 
> ```
> IC 95% para t: 0.645 ± 1.96(0.0154/√25) = 0.645 ± 0.006 s
> IC 95% para g: 9.61 ± 1.96(0.092) = 9.61 ± 0.18 m/s²
> ```
> 
> ### Resultado Final:
> 
> **g = (9.61 ± 0.18) m/s²** con 95% de confianza
> 
> **Análisis**:
> 
> - Diferencia con valor teórico: |9.61 - 9.81| = 0.20 m/s²
> - La diferencia está dentro del intervalo de confianza
> - Posibles fuentes de error sistemático: resistencia del aire, tiempo de reacción

## ⚠️ Errores Comunes y Precauciones

> [!warning] **Confusiones Frecuentes** ⚠️
> 
> 1. **Confundir σ con σ_x̄**:
>     
>     - ❌ Usar σ como incertidumbre de la media
>         
>     - ✅ Usar σ_x̄ = σ/√n para la media
>         
>     
>     2. **Usar n en lugar de (n-1)**:
>     
>     - ❌ s = √[∑(xᵢ - x̄)²/n] (subestima la variabilidad)
>     - ✅ s = √[∑(xᵢ - x̄)²/(n-1)] (estimador insesgado)
> 2. **Asumir normalidad sin verificar**:
>     - Siempre verificar gráficamente o con pruebas
>     - La regla 68-95-99.7 solo aplica para distribuciones normales
> 3. **Malinterpretar intervalos de confianza**:
>     - ❌ "95% de probabilidad de que μ esté en el intervalo"
>     - ✅ "95% de confianza en el método que genera el intervalo"
> 4. **Ignorar outliers**:
>     - Investigar antes de eliminar
>     - Documentar decisiones sobre exclusión de datos
> 5. **Confundir precisión con exactitud**:
>     - **Precisión**: Baja dispersión (σ pequeña)
>     - **Exactitud**: Cerca del valor verdadero
>     - Posible tener alta precisión pero baja exactitud

> [!tip] **Buenas Prácticas Estadísticas** ✅
> 
> ### Recopilación de Datos:
> 
> **Tamaño de muestra**:
> 
> - **n ≥ 30**: Para aplicar teorema del límite central
> - **n ≥ 10**: Para análisis básicos con normalidad verificada
> - **Regla práctica**: Más datos → mejor estimación
> 
> **Aleatorización**:
> 
> - Orden aleatorio de mediciones
> - Evitar patrones sistemáticos
> - Controlar variables externas
> 
> ### Análisis de Datos:
> 
> **Exploración inicial**:
> 
> 1. Graficar los datos (histograma, boxplot)
> 2. Calcular estadísticos descriptivos
> 3. Identificar valores atípicos
> 4. Verificar supuestos de normalidad
> 
> **Reportar resultados**:
> 
> - Media ± desviación estándar para describir la muestra
> - Media ± error estándar para inferencias sobre la población
> - Intervalos de confianza apropiados
> - Número de mediciones (n)

## 🧪 Herramientas Computacionales

> [!info] **Software y Calculadoras** 💻
> 
> ### Calculadoras Científicas:
> 
> **Funciones estadísticas básicas**:
> 
> - **Σ+**: Acumular datos
> - **x̄**: Media aritmética
> - **σₙ**: Desviación estándar población (÷n)
> - **σₙ₋₁**: Desviación estándar muestra (÷n-1)
> 
> ### Software Especializado:
> 
> |Software|Ventajas|Uso típico|
> |---|---|---|
> |**Excel**|Accesible, interfaz familiar|Análisis básico, gráficos|
> |**R**|Gratuito, muy potente|Análisis estadístico avanzado|
> |**Python (SciPy)**|Programable, versatil|Automatización, scripting|
> |**SPSS**|Interfaz gráfica|Análisis profesional|
> |**Origin**|Especializado en científico|Gráficos de calidad publicación|
> 
> ### Funciones Útiles en Excel:
> 
> ```
> =AVERAGE(range)      → Media aritmética
> =STDEV.S(range)      → Desviación estándar (muestra)
> =STDEV.P(range)      → Desviación estándar (población)
> =CONFIDENCE.NORM()   → Intervalo de confianza
> =NORM.DIST()         → Distribución normal
> =NORM.INV()          → Valores críticos
> ```

## 📖 Aplicaciones Específicas en Mecánica

> [!info] **Experimentos Típicos** ⚙️
> 
> ### Péndulo Simple:
> 
> **Variables a analizar**:
> 
> - Período T: Distribución normal esperada
> - Amplitud inicial: Verificar independencia
> - Longitud L: Propagación de errores
> 
> **Análisis estadístico**:
> 
> ```
> T̄ = media de períodos medidos
> s_T = desviación estándar
> g = 4π²L/T̄² ± propagación de incertidumbres
> ```
> 
> ### Ley de Hooke:
> 
> **Datos pareados (F, x)**:
> 
> - Regresión lineal: F = kx + F₀
> - Análisis de residuos para verificar linealidad
> - Coeficiente de correlación r
> 
> **Constante elástica**:
> 
> ```
> k = pendiente ± incertidumbre de la pendiente
> Verificar R² > 0.95 para buena linealidad
> ```
> 
> ### Movimiento Uniformemente Acelerado:
> 
> **Posición vs tiempo**:
> 
> - Ajuste parabólico: x = x₀ + v₀t + ½at²
> - Análisis de múltiples trayectorias
> - Comparación con predicción teórica
> 
> **Aceleración**:
> 
> ```
> a = coeficiente de t²
> Intervalo de confianza para a
> Comparación con g teórica
> ```

## 🎯 Ejercicios y Problemas Tipo

> [!example] **Problema 1: Análisis Básico** 📝
> 
> ### Enunciado:
> 
> Un estudiante mide la masa de un objeto 15 veces con los siguientes resultados (en gramos):
> 
> ```
> 247.3, 247.8, 247.1, 248.0, 247.6, 247.4, 247.9, 247.2, 
> 247.7, 247.5, 247.8, 247.3, 247.6, 247.4, 247.7
> ```
> 
> **Calcular**: a) Media aritmética b) Desviación estándar de la muestra c) Error estándar de la media d) Intervalo de confianza 95% para la masa verdadera
> 
> ### Solución:
> 
> **a) Media aritmética**:
> 
> ```
> m̄ = (247.3 + 247.8 + ... + 247.7)/15 = 3713.3/15 = 247.55 g
> ```
> 
> **b) Desviación estándar**:
> 
> ```
> Σ(mᵢ - m̄)² = 0.7775 g²
> s = √[0.7775/14] = 0.236 g
> ```
> 
> **c) Error estándar**:
> 
> ```
> s_m̄ = s/√n = 0.236/√15 = 0.061 g
> ```
> 
> **d) Intervalo de confianza 95%**:
> 
> ```
> IC = m̄ ± t₀.₀₂₅,₁₄ × s_m̄ = 247.55 ± 2.145 × 0.061
> IC = 247.55 ± 0.13 = [247.42, 247.68] g
> ```

> [!example] **Problema 2: Detección de Outliers** 🎯
> 
> ### Enunciado:
> 
> En un experimento de caída libre, se registran los siguientes tiempos (en segundos):
> 
> ```
> 0.452, 0.448, 0.455, 0.450, 0.449, 0.453, 0.447, 0.451, 
> 0.454, 0.485, 0.450, 0.452
> ```
> 
> **Investigar**: ¿Hay algún outlier? Si lo hay, ¿se debe eliminar?
> 
> ### Solución:
> 
> **Análisis inicial**:
> 
> ```
> t̄ = 0.4538 s (con todos los datos)
> s = 0.0106 s
> ```
> 
> **Identificación de outlier**:
> 
> ```
> Valor sospechoso: 0.485 s
> Z = (0.485 - 0.4538)/0.0106 = 2.94
> ```
> 
> **Criterio 3σ**: |Z| = 2.94 < 3, técnicamente no es outlier **Criterio 2σ**: |Z| = 2.94 > 2, valor inusual
> 
> **Análisis sin el valor**:
> 
> ```
> t̄ₙuevo = 0.451 s
> sₙuevo = 0.0028 s
> Reducción significativa en dispersión
> ```
> 
> **Recomendación**: Investigar la causa del valor 0.485 s
> 
> - ¿Error en la medición?
> - ¿Condición experimental diferente?
> - Si no hay explicación, mantener pero reportar como atípico

## 📚 Referencias y Conexiones

> [!quote] **Notas Relacionadas**
> 
> - [[Incertidumbres Experimentales]] - Aplicación de estadística
> - [[Análisis de Errores]] - Marco conceptual
> - [[Regresión Lineal]] - Análisis de relaciones
> - [[Pruebas de Hipótesis]] - Inferencia estadística

## 📈 Extensiones Avanzadas

> [!info] **Temas de Profundización** 🚀
> 
> ### Distribuciones Relacionadas:
> 
> **Distribución t de Student**:
> 
> - Para muestras pequeñas (n < 30)
> - Colas más pesadas que la normal
> - Converge a normal cuando n → ∞
> 
> **Distribución Chi-cuadrado (χ²)**:
> 
> - Para análisis de varianzas
> - Pruebas de bondad de ajuste
> - No simétrica, siempre positiva
> 
> **Distribución F**:
> 
> - Para comparar varianzas
> - ANOVA (análisis de varianza)
> - Diseño experimental
> 
> ### Métodos No Paramétricos:
> 
> **Cuando la normalidad falla**:
> 
> - **Mediana y MAD**: Alternativas robustas
> - **Prueba de Wilcoxon**: Comparar medianas
> - **Prueba de Kruskal-Wallis**: ANOVA no paramétrico
> - **Bootstrap**: Remuestreo para intervalos de confianza

## 📝 Notas Recomendadas

> [!note] **Prerrequisitos**
> 
> - [[Conceptos Básicos de Medición]] - Fundamentos experimentales
> - **Matemáticas**: Álgebra básica, funciones
> - **Calculadora científica**: Operaciones estadísticas

> [!note] **Temas Siguientes**
> 
> - [[Incertidumbres Experimentales]] - Aplicación directa
> - [[Regresión y Correlación]] - Análisis de relaciones
> - [[Pruebas de Hipótesis]] - Inferencia estadística
> - [[Diseño de Experimentos]] - Planificación estadística

---

**Tags:** #estadistica #media-aritmetica #desviacion-estandar #distribucion-normal #analisis-datos #fisica-experimental #mediciones #intervalos-confianza #outliers #normalidad