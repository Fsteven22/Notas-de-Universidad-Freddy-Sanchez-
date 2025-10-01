# Errores Absolutos y Relativos

> [!quote] "El error no está en equivocarse, sino en no saber cuánto nos equivocamos." 🎯

> [!info]- Toda medición experimental contiene inevitablemente cierto grado de incertidumbre. Los errores absolutos y relativos son herramientas fundamentales para cuantificar y comparar la precisión de nuestras mediciones, permitiéndonos evaluar la confiabilidad de nuestros resultados experimentales.

## 🔧 Conceptos Fundamentales

> [!info]- **Definiciones Básicas** 📐
> 
> ### Terminología Esencial:
> 
> |Concepto|Símbolo|Definición|Ejemplo|
> |---|---|---|---|
> |**Valor verdadero**|V_v|Valor real de la magnitud|10.000 m|
> |**Valor medido**|V_m|Resultado de la medición|9.97 m|
> |**Error absoluto**|Δx|V_m - V_v|-0.03 m|
> |**Error relativo**|ε_r|Δx/V_v|-0.003|
> |**Error porcentual**|ε_%|ε_r × 100%|-0.3%|
> |**Incertidumbre**|u|Rango de confianza|±0.02 m|
> 
> ### Características Importantes:
> 
> - **Error absoluto**: Tiene las **mismas unidades** que la magnitud medida
> - **Error relativo**: Es **adimensional** (número puro)
> - **Error porcentual**: Se expresa en **porcentaje (%)**
> - **Signo del error**: Positivo si se sobrestima, negativo si se subestima

> [!tip]- **Tipos de Errores** 🌊
> 
> ### Clasificación por Origen:
> 
> **Errores Sistemáticos**:
> 
> - ✅ **Reproducibles** y constantes
> - ✅ **Corregibles** si se conoce la causa
> - ❌ **Sesgan** todas las mediciones en la misma dirección
> - **Ejemplos**: Calibración incorrecta, temperatura ambiente, paralaje
> 
> **Errores Aleatorios (Estadísticos)**:
> 
> - ✅ **Se promedian** con múltiples mediciones
> - ✅ **Siguen** distribuciones estadísticas conocidas
> - ❌ **Impredecibles** en mediciones individuales
> - **Ejemplos**: Vibración, fluctuaciones eléctricas, fatiga del operador
> 
> **Errores Groseros (Equivocaciones)**:
> 
> - ❌ **No son errores** sino equivocaciones
> - ❌ **Deben eliminarse** del análisis
> - **Ejemplos**: Lectura incorrecta de escalas, uso erróneo de instrumentos
> 
> ### Clasificación por Magnitud:
> 
> |Tipo|Valor Típico|Aceptabilidad|Uso|
> |---|---|---|---|
> |**Despreciable**|< 1%|✅ Excelente|Investigación de precisión|
> |**Pequeño**|1-5%|✅ Bueno|Experimentos de laboratorio|
> |**Moderado**|5-10%|⚠️ Aceptable|Mediciones técnicas|
> |**Grande**|> 10%|❌ Inaceptable|Requiere mejora del método|

> [!warning]- **Fórmulas Fundamentales** ⚡
> 
> ### Error Absoluto:
> 
> **Definición**: Δx = x_medido - x_verdadero
> 
> **En la práctica**: Δx = x_medido - x_promedio
> 
> ### Error Relativo:
> 
> **Como fracción**: ε_r = Δx / x_verdadero
> 
> **Como porcentaje**: ε_% = (Δx / x_verdadero) × 100%
> 
> ### Incertidumbre Absoluta:
> 
> **Para medición única**: u = ±(precisión del instrumento/2)
> 
> **Para múltiples mediciones**: u = ±(desviación estándar/√n)
> 
> ### Incertidumbre Relativa:
> 
> **Como fracción**: u_r = u / x_promedio
> 
> **Como porcentaje**: u_% = (u / x_promedio) × 100%

> [!success] 🔗 Proceso de Análisis de Errores
> 
> ```mermaid
> graph TD
>     A[Realizar Mediciones] --> B[Calcular Promedio]
>     B --> C[Determinar Error Absoluto]
>     C --> D[Calcular Error Relativo]
>     D --> E[Evaluar Aceptabilidad]
>     E --> F[Decidir: ¿Repetir o Aceptar?]
>     F --> G[Expresar Resultado Final]
>     
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
>     style E fill:#fce4ec
>     style F fill:#f1f8e9
>     style G fill:#e0f2f1
> ```

> [!note]- **Métodos de Cálculo** 📝
> 
> ### Para Medición Única:
> 
> **Cuando conoces el valor verdadero**:
> 
> ```
> Error absoluto: Δx = x_medido - x_verdadero
> Error relativo: ε_r = Δx / x_verdadero
> Error porcentual: ε_% = ε_r × 100%
> ```
> 
> **Cuando NO conoces el valor verdadero**:
> 
> ```
> Incertidumbre: u = ± (precisión del instrumento / 2)
> Incertidumbre relativa: u_r = u / x_medido
> ```
> 
> ### Para Múltiples Mediciones:
> 
> **Promedio**: x̄ = (x₁ + x₂ + ... + xₙ) / n
> 
> **Desviación estándar**: s = √[Σ(xᵢ - x̄)² / (n-1)]
> 
> **Incertidumbre**: u = ± s / √n
> 
> **Error de cada medición**: Δxᵢ = xᵢ - x̄

## 🎯 Estrategias de Cálculo

> [!tip]- **Método VERA (Valor-Error-Relativo-Análisis)** 🧠
> 
> ### **V**alor - Determina el valor de referencia
> 
> 1. **Si conoces el valor verdadero**: Úsalo como referencia
> 2. **Si no lo conoces**: Usa el promedio de tus mediciones
> 3. **Para comparar instrumentos**: Usa el más preciso como referencia
> 
> ### **E**rror - Calcula el error absoluto
> 
> 4. **Error individual**: Δx = x_medido - x_referencia
> 5. **Signo importante**: Positivo = sobrestimación, Negativo = subestimación
> 6. **Unidades**: Mismas que la magnitud medida
> 
> ### **R**elativo - Calcula el error relativo
> 
> 7. **División**: ε_r = Δx / x_referencia
> 8. **Multiplicar por 100**: Para obtener porcentaje
> 9. **Adimensional**: Permite comparar diferentes magnitudes
> 
> ### **A**nálisis - Evalúa y concluye
> 
> 10. **Compara** con criterios de aceptabilidad
> 11. **Identifica** posibles fuentes de error
> 12. **Decide** si es necesario mejorar la técnica

## 📚 Ejemplos Prácticos

> [!example]- **Ejemplo 1: Medición de Longitud** 📏
> 
> ### Situación:
> 
> Se mide la longitud de una mesa con una regla. El valor verdadero es 1.500 m.
> 
> ### Datos:
> 
> - **Valor verdadero**: V_v = 1.500 m
> - **Valor medido**: V_m = 1.485 m
> - **Precisión de la regla**: 1 mm = 0.001 m
> 
> ### Cálculos:
> 
> **Error Absoluto**: Δx = V_m - V_v = 1.485 - 1.500 = **-0.015 m**
> 
> **Error Relativo**: ε_r = Δx / V_v = -0.015 / 1.500 = **-0.01 = -1.0%**
> 
> **Error Porcentual**: ε_% = ε_r × 100% = **-1.0%**
> 
> ### Interpretación:
> 
> - **Subestimación** de 1.5 cm (error negativo)
> - **Error relativo del 1.0%** (aceptable para mediciones con regla)
> - **Posible causa**: Paralaje, deformación de la regla, error de lectura

> [!example]- **Ejemplo 2: Múltiples Mediciones** 🔢
> 
> ### Situación:
> 
> Se mide el período de un péndulo 5 veces. Valor teórico: T = 2.00 s
> 
> ### Datos Experimentales:
> 
> |Medición|Tiempo (s)|Error Absoluto (s)|
> |---|---|---|
> |1|1.98|-0.02|
> |2|2.03|+0.03|
> |3|1.97|-0.03|
> |4|2.01|+0.01|
> |5|2.02|+0.02|
> 
> ### Cálculos:
> 
> **Promedio**: x̄ = (1.98 + 2.03 + 1.97 + 2.01 + 2.02) / 5 = **2.002 s**
> 
> **Error absoluto del promedio**: Δx̄ = 2.002 - 2.000 = **+0.002 s**
> 
> **Error relativo del promedio**: ε_r = 0.002 / 2.000 = **0.001 = 0.1%**
> 
> **Desviación estándar**: s = √[Σ(xᵢ - x̄)² / (n-1)] = **0.025 s**
> 
> **Incertidumbre del promedio**: u = s / √n = 0.025 / √5 = **±0.011 s**
> 
> ### Resultado Final:
> 
> **T = (2.002 ± 0.011) s** con error relativo de **0.1%**

> [!example]- **Ejemplo 3: Comparación de Instrumentos** 🔍
> 
> ### Situación:
> 
> Se mide el diámetro de una esfera con diferentes instrumentos.
> 
> ### Resultados:
> 
> - **Regla graduada**: 25.2 ± 0.5 mm
> - **Calibrador vernier**: 25.34 ± 0.05 mm
> - **Micrómetro**: 25.347 ± 0.005 mm
> - **Valor de referencia** (micrómetro): 25.347 mm
> 
> ### Análisis de Errores:
> 
> **Regla graduada**:
> 
> - Error absoluto: 25.2 - 25.347 = **-0.147 mm**
> - Error relativo: -0.147 / 25.347 = **-0.58%**
> 
> **Calibrador vernier**:
> 
> - Error absoluto: 25.34 - 25.347 = **-0.007 mm**
> - Error relativo: -0.007 / 25.347 = **-0.028%**
> 
> ### Conclusión:
> 
> |Instrumento|Error Absoluto|Error Relativo|Precisión|
> |---|---|---|---|
> |Regla|-0.147 mm|-0.58%|Baja|
> |Calibrador|-0.007 mm|-0.028%|Media|
> |Micrómetro|0.000 mm|0.000%|Alta|

## 🧮 Técnicas de Memorización

> [!tip]- **Mnemotecnia: "MEDIR"** 🎯
> 
> **M**edición vs valor verdadero **E**rror absoluto = diferencia  
> **D**ividir entre verdadero **I**rrelativo = sin unidades **R**esultado en porcentaje × 100

> [!tip]- **Reglas Prácticas** 📏
> 
> ### Para Error Relativo:
> 
> 1. **< 1%**: Excelente precisión
> 2. **1-5%**: Buena precisión (laboratorio estudiantil)
> 3. **5-10%**: Aceptable (mediciones técnicas)
> 4. **> 10%**: Revisar método o instrumento
> 
> ### Para Múltiples Mediciones:
> 
> - **Más mediciones** → Menor incertidumbre del promedio
> - **Incertidumbre** disminuye como 1/√n
> - **Desviación estándar** indica dispersión de los datos

## ⚠️ Errores Comunes

> [!warning]- **Confusiones Frecuentes** ⚠️
> 
> 1. **Confundir exactitud con precisión**:
>     - **Exactitud**: Cercanía al valor verdadero
>     - **Precisión**: Reproducibilidad de las mediciones
> 2. **Usar valor medido en lugar del verdadero**:
>     - ❌ ε_r = Δx / x_medido
>     - ✅ ε_r = Δx / x_verdadero
> 3. **Olvidar el signo del error**:
>     - **Positivo**: Sobrestimación
>     - **Negativo**: Subestimación
> 4. **Confundir error con incertidumbre**:
>     - **Error**: Diferencia con valor conocido
>     - **Incertidumbre**: Rango de confianza
> 5. **No considerar cifras significativas**:
>     - El error no puede tener más precisión que la medición
> 6. **Eliminar datos "malos"**:
>     - Solo eliminar errores groseros evidentes
>     - No eliminar datos solo porque no "se ven bien"

## 🎯 Criterios de Aceptabilidad

> [!info]- **Estándares por Disciplina** 🌍
> 
> ### Física de Laboratorio (Estudiante):
> 
> - **Excelente**: < 2%
> - **Bueno**: 2-5%
> - **Aceptable**: 5-10%
> - **Requiere mejora**: > 10%
> 
> ### Ingeniería:
> 
> - **Estructural**: < 5% (seguridad crítica)
> - **Mecánica**: < 2% (piezas de precisión)
> - **Eléctrica**: < 1% (instrumentación)
> 
> ### Investigación Científica:
> 
> - **Física de partículas**: < 0.1%
> - **Astronomía**: Depende de la distancia
> - **Química analítica**: < 1%
> 
> ### Aplicaciones Comerciales:
> 
> - **Manufactura**: Según tolerancias de diseño
> - **Calibración**: < 0.5%
> - **Control de calidad**: Según especificaciones

## 🔬 Aplicaciones en Laboratorio

> [!info]- **Experimentos Típicos** 🧪
> 
> ### Mecánica:
> 
> - **Caída libre**: Comparar g_experimental con g_teórico
> - **Péndulo simple**: Verificar T = 2π√(L/g)
> - **Plano inclinado**: Validar predicciones teóricas
> 
> ### Ondas y Acústica:
> 
> - **Velocidad del sonido**: Comparar con valor tabulado
> - **Frecuencias de resonancia**: Verificar modelos teóricos
> 
> ### Óptica:
> 
> - **Índice de refracción**: Comparar con literatura
> - **Focal de lentes**: Validar ecuación de lentes delgadas
> 
> ### Análisis de Resultados:
> 
> 1. **Calcular errores** para cada magnitud medida
> 2. **Identificar** la fuente principal de error
> 3. **Proponer mejoras** al método experimental
> 4. **Discutir** la validez de la teoría

## 📖 Referencias

> [!quote]- **Notas Relacionadas**
> 
> - [[Mediciones Fundamentales]] - Base conceptual
> - [[Uso del Calibrador de Vernier]] - Aplicación práctica
> - [[Incertidumbres Experimentales]] - Análisis avanzado
> - [[Cifras Significativas]] - Expresión correcta de resultados

## 📚 Notas Recomendadas

> [!note]- **Prerrequisitos**
> 
> - [[Mediciones Fundamentales]] - Conceptos básicos
> - **Estadística básica**: Promedio, desviación estándar
> - **Álgebra**: Operaciones con decimales y porcentajes

> [!note]- **Temas Siguientes**
> 
> - [[Incertidumbres Experimentales]] - Propagación de errores
> - [[Tratamiento Estadístico de Datos]] - Análisis avanzado
> - [[Presentación de Resultados]] - Reportes de laboratorio

---

**Tags:** #errores #absolutos #relativos #incertidumbre #precision #exactitud #mediciones #analisis-datos #laboratorio #fisica-mecanica #estadistica