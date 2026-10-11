---
dg-publish: true
---

# Módulo 6.3: Manipulación de Datos  📊

> [!quote] "Los datos son el nuevo petróleo, pero solo cuando sabemos refinarlos y extraer su valor real." 🛢️
>
> [!info] La manipulación de datos es una habilidad fundamental en el análisis de información moderna. En la era del Big Data, la capacidad de filtrar, agregar, transformar y visualizar datos determina la calidad de nuestras decisiones. Pandas, la biblioteca más poderosa de Python para análisis de datos, nos proporciona herramientas intuitivas y eficientes para convertir datos crudos en insights accionables. Este módulo te enseñará las técnicas esenciales de manipulación de datos usando el dataset de vuelos como caso de estudio práctico.

## Conceptos Fundamentales

> [!info] **Dataset de Referencia: Vuelos de Aerolíneas** ✈️
> 
> Para este módulo utilizaremos el dataset `flights` de Seaborn, que contiene registros históricos de pasajeros de aerolíneas (en miles) organizados por mes y año, cubriendo el período 1949-1960. Este dataset es perfecto para análisis temporal y estacional.
> 
> **Características del Dataset:**
> 
> - **Filas:** 144 registros (12 años × 12 meses)
> - **Columnas:** 3 variables (year, month, passengers)
> - **Período:** 1949-1960
> - **Medición:** Miles de pasajeros por mes
> 
> **Carga del Dataset:**
> 
> ```python
> import pandas as pd
> import seaborn as sns
> import matplotlib.pyplot as plt 
> 
> # Carga directa desde Seaborn
> df = sns.load_dataset('flights')
> print("Dataset de Vuelos:")
> print(df.head())
> print(f"Forma: {df.shape}")
> ```
> 
> |Variable|Tipo|Descripción|
> |---|---|---|
> |year|int64|Año (1949-1960)|
> |month|object|Mes abreviado (Jan, Feb, etc.)|
> |passengers|int64|Miles de pasajeros transportados|
>
> [!tip] **Operadores Lógicos para Filtrado** 🔍
> 
> Los operadores lógicos son la base del filtrado inteligente en Pandas. Permiten crear condiciones complejas para extraer subconjuntos específicos de datos.
> 
> **Tabla de Operadores:**
> 
> |Operador|Significado|Función|Ejemplo|
> |---|---|---|---|
> |`&`|AND (Y)|Ambas condiciones verdaderas|`(df['year'] > 1955) & (df['month'] == 'Jul')`|
> |`\|`|OR (O)|Al menos una condición verdadera|`(df['year'] == 1949) \| (df['year'] == 1960)`|
> |`~`|NOT (NO)|Invierte la condición|`~(df['month'] == 'Dec')`|
> 
> **Reglas Críticas:**
> 
> - Siempre usar paréntesis en condiciones múltiples
> - Los operadores de Pandas (`&`, `|`, `~`) son diferentes a Python (`and`, `or`, `not`)
> - Cada condición debe ser una expresión booleana válida
> 
> **Patrones Comunes:**
> 
> ```python
> # Filtro simple
> df[df['columna'] > valor]
> 
> # Filtro múltiple
> df[(condición1) & (condición2)]
> 
> # Exclusión
> df[~(df['columna'] == valor)]
> ```
>
> [!warning] **Sustitución Condicional: .where() vs .mask()** 🔄
> 
> Estos métodos permiten reemplazar valores basados en condiciones lógicas sin eliminar filas del DataFrame.
> 
> **Diferencias Fundamentales:**
> 
> |Método|Comportamiento|Mantiene cuando|Reemplaza cuando|
> |---|---|---|---|
> |`.where()`|Mantiene valores TRUE|Condición = True|Condición = False|
> |`.mask()`|Mantiene valores FALSE|Condición = False|Condición = True|
> 
> **Sintaxis y Ejemplos:**
> 
> ```python
> # .where(): mantiene donde condición es True
> df['nueva'] = df['columna'].where(df['columna'] > 100, 'Bajo')
> 
> # .mask(): mantiene donde condición es False  
> df['nueva'] = df['columna'].mask(df['columna'] <= 100, 'Alto')
> 
> # Ejemplo práctico: Categorizar décadas
> df['decada'] = df['year'].where(df['year'] >= 1955, 'Inicio')
> df['decada'] = df['decada'].mask(df['year'] >= 1955, 'Final')
> ```
> 
> **⚠️ Precauciones:**
> 
> - El parámetro `other` define el valor de reemplazo
> - Sin `other`, los valores reemplazados se vuelven NaN
> - Útil para categorización y limpieza de datos
>
> [!info] **Estadísticas Descriptivas Esenciales** 📈
> 
> Las estadísticas descriptivas proporcionan un resumen cuantitativo completo de nuestros datos, revelando patrones, tendencias y anomalías.
> 
> **Métodos de Resumen Rápido:**
> 
> |Método|Output|Información Clave|
> |---|---|---|
> |`.describe()`|8 estadísticas principales|count, mean, std, min, 25%, 50%, 75%, max|
> |`.info()`|Metadata del DataFrame|tipos, memoria, valores nulos|
> |`.shape`|Dimensiones|(filas, columnas)|
> 
> **Estadísticas Individuales:**
> 
> |Medida|Método|Descripción|Interpretación|
> |---|---|---|---|
> |**Tendencia Central**|`.mean()`|Promedio aritmético|Valor típico esperado|
> ||`.median()`|Valor central|Menos afectado por outliers|
> ||`.mode()`|Valor más frecuente|Patrón más común|
> |**Dispersión**|`.std()`|Desviación estándar|Variabilidad alrededor de la media|
> ||`.var()`|Varianza|Dispersión al cuadrado|
> |**Extremos**|`.min()` / `.max()`|Valores límite|Rango de datos|
> ||`.sum()`|Suma total|Agregación completa|
> |**Conteo**|`.count()`|Valores no nulos|Completitud de datos|
> 
> **Ejemplo Completo:**
> 
> ```python
> # Resumen completo
> stats = df['passengers'].describe()
> print("Estadísticas de Pasajeros:")
> print(f"Promedio: {df['passengers'].mean():.0f} mil")
> print(f"Mediana: {df['passengers'].median():.0f} mil") 
> print(f"Desv. Estándar: {df['passengers'].std():.2f}")
> print(f"Rango: {df['passengers'].max() - df['passengers'].min()}")
> ```

## Estrategias y Métodos

> [!tip] **Método FILTRA para Filtrado Sistemático** 🎯
> 
> **F**ormular pregunta específica **I**dentificar columnas relevantes  
> **L**ógica de condiciones (AND/OR/NOT) **T**estear filtro con subset pequeño **R**evisar resultados y validar **A**plicar a análisis completo
> 
> **Proceso Detallado:**
> 
> 1. **Formular:** "¿Qué registros necesito exactamente?"
> 2. **Identificar:** Determinar columnas clave para el filtro
> 3. **Lógica:** Construir condiciones con operadores apropiados
> 4. **Testear:** Probar con `.head()` o `.sample()`
> 5. **Revisar:** Verificar que los resultados tengan sentido
> 6. **Aplicar:** Usar en análisis o visualización final
> 
> **Ejemplo Aplicado:**
> 
> ```python
> # 1. Formular: "Vuelos de verano en años recientes"
> # 2. Identificar: 'month' y 'year' 
> # 3. Lógica: (year > 1955) AND (month in [Jun,Jul,Aug])
> # 4. Testear:
> filtro = (df['year'] > 1955) & (df['month'].isin(['Jun','Jul','Aug']))
> resultado = df[filtro]
> print(f"Registros encontrados: {len(resultado)}")
> # 5. Revisar: ¿Sentido lógico? ¿Cantidad esperada?
> # 6. Aplicar: Usar para análisis estacional
> ```
>
> [!tip] **Método AGRUPA para GroupBy Efectivo** 🎲
> 
> **A**nalizar objetivo de agrupación **G**rupar por categoría relevante **R**evisar grupos formados **U**sar función de agregación apropiada **P**rocesar resultados (ordenar/formatear) **A**nalizar e interpretar patrones
> 
> **Guía de Funciones de Agregación:**
> 
> |Objetivo|Función|Cuándo Usar|
> |---|---|---|
> |**Totales**|`.sum()`|Acumulación por período/categoría|
> |**Promedios**|`.mean()`|Tendencias típicas por grupo|
> |**Conteos**|`.count()`|Frecuencias y distribuciones|
> |**Extremos**|`.min()/.max()`|Valores límite por categoría|
> |**Variabilidad**|`.std()`|Consistencia dentro de grupos|
> |**Múltiples**|`.agg(['mean','sum'])`|Análisis comprehensivo|
> 
> **Implementación Sistemática:**
> 
> ```python
> # A: Objetivo = "Tendencia anual de tráfico"
> # G: Agrupar por 'year'
> grupos = df.groupby('year')
> # R: Revisar grupos
> print(f"Número de grupos: {grupos.ngroups}")
> # U: Función = sum (total anual)
> resultado = grupos['passengers'].sum()
> # P: Procesar (ya está ordenado por año)
> # A: Analizar tendencia de crecimiento
> ```

## Ejemplos Prácticos

> [!example] **Ejemplo 1: Análisis de Filtrado Avanzado** 🔍
> 
> **Objetivo:** Identificar patrones en vuelos de julio posteriores a 1955 y comparar con el resto de datos.
> 
> **Desarrollo Paso a Paso:**
> 
> ```python
> # Paso 1: Filtro específico
> vuelos_julio_recientes = df[(df['month'] == 'Jul') & (df['year'] > 1955)]
> print("Vuelos de Julio después de 1955:")
> print(vuelos_julio_recientes)
> print(f"Registros encontrados: {len(vuelos_julio_recientes)}")
> 
> # Paso 2: Estadísticas del subset
> promedio_julio = vuelos_julio_recientes['passengers'].mean()
> max_julio = vuelos_julio_recientes['passengers'].max()
> print(f"Promedio Julio reciente: {promedio_julio:.1f} mil")
> print(f"Máximo Julio reciente: {max_julio} mil")
> 
> # Paso 3: Comparación con promedio general
> promedio_general = df['passengers'].mean()
> diferencia = promedio_julio - promedio_general
> print(f"Diferencia vs promedio general: {diferencia:.1f} mil")
> 
> # Paso 4: Análisis de exclusión (NOT)
> sin_julio_reciente = df[~((df['month'] == 'Jul') & (df['year'] > 1955))]
> print(f"Registros SIN julio reciente: {len(sin_julio_reciente)}")
> ```
> 
> **Resultados y Análisis:**
> 
> - Registros filtrados: 5 (años 1956-1960)
> - Promedio específico vs general: Comparación de tendencias
> - Validación de lógica con operador NOT
> 
> **Insight:** Los julios recientes muestran el impacto del crecimiento del tráfico aéreo en el período de post-guerra.
>
> [!example] **Ejemplo 2: GroupBy para Análisis Temporal y Estacional** 📅
> 
> **Objetivo:** Analizar la evolución anual y los patrones estacionales del tráfico aéreo.
> 
> **Análisis Anual Completo:**
> 
> ```python
> # Análisis por año - Dividir, Aplicar, Combinar
> print("=== ANÁLISIS ANUAL ===")
> 
> # Dividir por año, aplicar suma, combinar resultados
> pasajeros_por_año = df.groupby('year')['passengers'].sum()
> print("Evolución anual del tráfico:")
> print(pasajeros_por_año)
> 
> # Identificar año pico
> año_pico = pasajeros_por_año.idxmax()
> tráfico_pico = pasajeros_por_año.max()
> print(f"\nAño con más tráfico: {año_pico} ({tráfico_pico:,} mil)")
> 
> # Calcular crecimiento total
> crecimiento = ((pasajeros_por_año.iloc[-1] / pasajeros_por_año.iloc[0]) - 1) * 100
> print(f"Crecimiento total período: {crecimiento:.1f}%")
> ```
> 
> **Análisis Estacional:**
> 
> ```python
> print("\n=== ANÁLISIS ESTACIONAL ===")
> 
> # Promedio por mes para identificar estacionalidad
> estacionalidad = df.groupby('month')['passengers'].mean().sort_values(ascending=False)
> print("Ranking estacional (promedio por mes):")
> for i, (mes, promedio) in enumerate(estacionalidad.items(), 1):
>     print(f"{i:2d}. {mes}: {promedio:5.1f} mil pasajeros")
> 
> # Cálculo de amplitud estacional
> pico_estacional = estacionalidad.max()
> valle_estacional = estacionalidad.min()
> amplitud = pico_estacional - valle_estacional
> 
> print(f"\nPico estacional: {estacionalidad.idxmax()} ({pico_estacional:.1f})")
> print(f"Valle estacional: {estacionalidad.idxmin()} ({valle_estacional:.1f})")
> print(f"Amplitud estacional: {amplitud:.1f} mil pasajeros")
> ```
> 
> **Resultados Esperados:**
> 
> - Crecimiento sostenido año tras año
> - Estacionalidad clara con picos en verano
> - Patrones consistentes a lo largo del período
>
> [!example] **Ejemplo 3: Visualización Integrada con Análisis** 📊
> 
> **Objetivo:** Crear visualizaciones que complementen el análisis de datos para identificar tendencias y patrones.
> 
> **Gráfico de Tendencia Anual:**
> 
> ```python
> # Configuración de visualización
> plt.style.use('seaborn-v0_8')
> 
> # Gráfico 1: Evolución anual
> pasajeros_por_año = df.groupby('year')['passengers'].sum()
> 
> plt.figure(figsize=(12, 6))
> pasajeros_por_año.plot(kind='line', marker='o', linewidth=3, markersize=8, color='steelblue')
> 
> plt.title('Evolución del Tráfico Anual de Pasajeros (1949-1960)', fontsize=14)
> plt.ylabel('Total de Pasajeros (miles)', fontsize=12)
> plt.xlabel('Año', fontsize=12)
> plt.grid(True, alpha=0.3)
> 
> # Anotación del pico
> año_max = pasajeros_por_año.idxmax()
> valor_max = pasajeros_por_año.max()
> plt.annotate(f'Pico: {valor_max:,}', 
>              xy=(año_max, valor_max),
>              xytext=(año_max-1, valor_max+100),
>              arrowprops=dict(arrowstyle='->', color='red'))
> plt.show()
> ```
> 
> **Gráfico de Estacionalidad:**
> 
> ```python
> # Gráfico 2: Patrones estacionales
> estacionalidad = df.groupby('month')['passengers'].mean()
> 
> plt.figure(figsize=(12, 6))
> estacionalidad.plot(kind='bar', color='coral', edgecolor='black', alpha=0.8)
> 
> plt.title('Patrones Estacionales - Promedio de Pasajeros por Mes', fontsize=14)
> plt.ylabel('Promedio de Pasajeros (miles)', fontsize=12)
> plt.xlabel('Mes', fontsize=12)
> plt.xticks(rotation=45)
> 
> # Línea de referencia (promedio general)
> promedio_general = df['passengers'].mean()
> plt.axhline(y=promedio_general, color='red', linestyle='--', 
>             label=f'Promedio general: {promedio_general:.0f}')
> plt.legend()
> plt.tight_layout()
> plt.show()
> ```
> 
> **Boxplot de Distribución:**
> 
> ```python
> # Gráfico 3: Distribución anual (variabilidad)
> plt.figure(figsize=(14, 8))
> df.boxplot(column='passengers', by='year', figsize=(14, 8))
> 
> plt.title('Distribución del Tráfico Mensual por Año')
> plt.suptitle('')  # Quitar título automático
> plt.ylabel('Pasajeros (miles)')
> plt.xlabel('Año')
> plt.show()
> ```

## Proceso de Análisis

> [!success] 🔄 **Flujo de Manipulación de Datos**
> 
> ```mermaid
> graph TD
>     A[📥 Cargar Dataset] --> B[🔍 Exploración Inicial]
>     B --> C[📊 Estadísticas Descriptivas]
>     C --> D{🤔 ¿Filtrado Necesario?}
>     D -->|Sí| E[⚙️ Aplicar Filtros]
>     D -->|No| F[🎲 GroupBy Análisis]
>     E --> F
>     F --> G[📈 Agregaciones]
>     G --> H[📊 Visualización]
>     H --> I[🧠 Interpretación]
>     I --> J[📝 Conclusiones]
>     style A fill:#e1f5fe
>     style F fill:#f3e5f5
>     style H fill:#fff3e0
>     style J fill:#e8f5e8
> ```

## Técnicas de Implementación

> [!note] **Herramientas y Configuración Óptima** 🛠️
> 
> **Librerías Esenciales:**
> 
> ```python
> import pandas as pd           # Manipulación de datos
> import seaborn as sns        # Datasets y visualización avanzada  
> import matplotlib.pyplot as plt  # Visualización básica
> import numpy as np           # Operaciones numéricas
> ```
> 
> **Configuración Recomendada:**
> 
> ```python
> # Configuración de pandas
> pd.set_option('display.max_columns', None)
> pd.set_option('display.width', None)
> pd.set_option('display.precision', 2)
> 
> # Configuración de matplotlib
> plt.style.use('seaborn-v0_8')
> plt.rcParams['figure.figsize'] = (12, 8)
> plt.rcParams['font.size'] = 12
> ```
> 
> **Procedimiento de Carga de Datos:**
> 
> ```python
> # Método 1: Desde Seaborn (datasets integrados)
> df = sns.load_dataset('flights')
> 
> # Método 2: Desde archivo CSV
> df = pd.read_csv('archivo.csv')
> 
> # Método 3: Desde Excel
> df = pd.read_excel('archivo.xlsx', sheet_name='Hoja1')
> 
> # Verificación post-carga
> print(f"Forma: {df.shape}")
> print(f"Columnas: {list(df.columns)}")
> print(f"Tipos: {df.dtypes.to_dict()}")
> ```
> 
> **Materiales de Práctica:**
> 
> - Dataset flights (integrado en Seaborn)
> - Jupyter Notebook o IDE Python
> - Documentación oficial de Pandas
> - Ejemplos de referencia guardados

## Técnicas de Memorización

> [!tip] **Mnemotecnia: "PANDAS"** 🐼
> 
> **P**reguntar qué información necesito **A**plicar filtros con operadores lógicos (&, |, ~)  
> **N**avegar por grupos con groupby() **D**escribir datos con estadísticas (.describe()) **A**gregar funciones de resumen (sum, mean, count) **S**implificar con visualizaciones (.plot())
> 
> **Expansión Detallada:**
> 
> - **P - Preguntar:** Antes de filtrar, definir exactamente qué registros necesito
> - **A - Aplicar:** Usar paréntesis en condiciones múltiples, recordar que & ≠ and
> - **N - Navegar:** GroupBy = dividir-aplicar-combinar, pensar en categorías
> - **D - Describir:** .describe() es el primer paso para entender los datos
> - **A - Agregar:** Elegir la función correcta: sum para totales, mean para promedios
> - **S - Simplificar:** Una visualización vale más que mil números
> 
> **Frase Nemotécnica:** _"Para Analizar Necesito Datos Agregados Sistemáticamente"_
>
> [!tip] **Acrónimos para Operadores Lógicos: "YON"** 🎯
> 
> **Y** → & (AND) - **Y**a que ambas condiciones deben cumplirse **O** → | (OR) - **O**tra opción es que una condición se cumpla  
> **N** → ~ (NOT) - **N**iega o invierte la condición
> 
> **Reglas Mnemotécnicas:**
> 
> - **&**: Piensa en "ANDar" - necesitas ambos pies para andar
> - **|**: Piensa en "ORigen" - múltiples caminos al mismo origen
> - **~**: Piensa en "NO tildes" - la tilde invierte el significado

## Errores Comunes

> [!warning] **Errores Frecuentes en Filtrado y GroupBy** ⚠️
> 
> |Error|Problema|Consecuencia|Corrección|
> |---|---|---|---|
> |**Paréntesis faltantes**|`df[df['A'] > 5 & df['B'] == 'X']`|Error de sintaxis|`df[(df['A'] > 5) & (df['B'] == 'X')]`|
> |**Operadores incorrectos**|`df[(df['A'] > 5) and (df['B'] == 'X')]`|Error de tipos|Usar `&` en lugar de `and`|
> |**Comparación con NaN**|`df[df['col'] == np.nan]`|Siempre devuelve False|`df[df['col'].isna()]`|
> |**GroupBy sin agregación**|`df.groupby('col')`|Solo objeto groupby|`df.groupby('col')['target'].mean()`|
> |**Índices duplicados**|No resetear índice después de filtro|Problemas en operaciones|`df.reset_index(drop=True)`|
> |**Tipos de datos inconsistentes**|Agrupar strings y números|Resultados inesperados|Verificar `.dtypes` antes|
> |**Visualización sin configurar**|Plot directo sin parámetros|Gráficos poco legibles|Configurar `figsize`, títulos, etc.|
> 
> **Debugging Sistemático:**
> 
> ```python
> # 1. Verificar tipos de datos
> print(df.dtypes)
> 
> # 2. Probar filtros paso a paso
> cond1 = df['year'] > 1955
> cond2 = df['month'] == 'Jul'
> resultado = df[cond1 & cond2]
> 
> # 3. Validar grupos antes de agregar
> grupos = df.groupby('year')
> print(f"Grupos creados: {grupos.ngroups}")
> print(f"Tamaños: {grupos.size()}")
> ```

## Criterios de Calidad

> [!info] **Evaluación de Análisis de Datos** ✅
> 
> **Lista de Verificación - Filtrado:**
> 
> - [ ] Condiciones lógicas correctamente parentizadas
> - [ ] Uso apropiado de operadores (&, |, ~)
> - [ ] Validación de resultados con conteos
> - [ ] Manejo adecuado de valores nulos
> - [ ] Filtros documentados y comentados
> 
> **Lista de Verificación - Estadísticas:**
> 
> - [ ] Uso de .describe() para resumen inicial
> - [ ] Cálculo de medidas de tendencia central
> - [ ] Evaluación de dispersión y variabilidad
> - [ ] Identificación de valores extremos
> - [ ] Interpretación contextual de resultados
> 
> **Lista de Verificación - GroupBy:**
> 
> - [ ] Agrupación por variables categóricas apropiadas
> - [ ] Función de agregación alineada con objetivo
> - [ ] Validación del número de grupos generados
> - [ ] Ordenamiento lógico de resultados
> - [ ] Interpretación de patrones encontrados
> 
> **Lista de Verificación - Visualización:**
> 
> - [ ] Tipo de gráfico apropiado para los datos
> - [ ] Títulos y etiquetas descriptivos
> - [ ] Escala y proporción adecuadas
> - [ ] Colores y estilos profesionales
> - [ ] Interpretación clara de insights
> 
> **Criterios de Puntuación (0-100):**
> 
> - **Precisión técnica (30%):** Código funciona sin errores
> - **Apropiada metodología (25%):** Métodos correctos para objetivos
> - **Interpretación (25%):** Insights válidos y relevantes
> - **Presentación (20%):** Visualización clara y profesional

## Aplicaciones Específicas

> [!info] **Contextos de Aplicación en Diferentes Industrias** 🏢
> 
> **Sector Financiero:**
> 
> - Análisis de tendencias de mercado por período
> - Filtrado de transacciones sospechosas
> - Agregación de rendimientos por portafolio
> - Estacionalidad en patrones de gasto
> 
> **Marketing Digital:**
> 
> - Segmentación de clientes por comportamiento
> - Análisis de campañas por canal
> - Patrones temporales de engagement
> - ROI por demografía y región
> 
> **Logística y Supply Chain:**
> 
> - Optimización de rutas por temporada
> - Análisis de demanda por producto/región
> - Identificación de cuellos de botella
> - Patrones de inventario por categoría
> 
> **Recursos Humanos:**
> 
> - Análisis de rotación por departamento
> - Patrones de ausentismo estacional
> - Evaluación de rendimiento por equipo
> - Tendencias salariales por posición
> 
> **Investigación Académica:**
> 
> - Análisis de encuestas por demographics
> - Patrones temporales en datos experimentales
> - Comparaciones entre grupos de control
> - Validación estadística de hipótesis
> 
> **Ejemplo de Implementación - E-commerce:**
> 
> ```python
> # Análisis de ventas por temporada y categoría
> ventas_estacional = df.groupby(['season', 'category']).agg({
>     'revenue': 'sum',
>     'orders': 'count', 
>     'customers': 'nunique'
> })
> 
> # Identificar productos estrella por época
> top_products = df.groupby(['month', 'product'])['revenue'].sum().unstack()
> ```

## Referencias Cruzadas

> [!quote] **Notas Relacionadas**
> 
> **Fundamentos Previos:**
> 
> - [[NumPy - Arrays y Operaciones Numéricas]] - Base matemática para pandas
> - [[Python - Estructuras de Control]] - Lógica condicional aplicada
> - [[Estadística Descriptiva]] - Interpretación de métricas
> 
> **Temas Complementarios:**
> 
> - [[Pandas - DataFrames y Series]] - Estructuras fundamentales
> - [[Matplotlib - Visualización Básica]] - Gráficos y presentación
> - [[Seaborn - Visualización Estadística]] - Análisis visual avanzado
> 
> **Aplicaciones Avanzadas:**
> 
> - [[Machine Learning - Preprocessing]] - Preparación de datos para ML
> - [[Time Series Analysis]] - Análisis temporal especializado
> - [[SQL - Bases de Datos]] - Integración con sistemas de datos
> 
> **Metodologías:**
> 
> - [[EDA - Exploratory Data Analysis]] - Marco sistemático de exploración
> - [[Business Intelligence - KPIs]] - Métricas empresariales
> - [[Data Visualization Best Practices]] - Principios de presentación efectiva

## Prerrequisitos y Temas Avanzados

> [!note] **Prerrequisitos**
> 
> **Conocimientos Básicos Requeridos:**
> 
> - **Python Fundamentals:** Variables, tipos de datos, estructuras de control
> - **Pandas Básico:** DataFrames, Series, indexación básica
> - **Estadística Descriptiva:** Media, mediana, desviación estándar, percentiles
> - **Lógica Booleana:** Operadores AND, OR, NOT conceptuales
> - **Matemáticas Básicas:** Aritmética, porcentajes, proporciones
> 
> **Habilidades Técnicas:**
> 
> - Instalación y manejo de librerías Python
> - Navegación básica en Jupyter Notebook o IDE
> - Lectura e interpretación de documentación
> - Debugging básico de código Python
> 
> **Conceptos Estadísticos:**
> 
> - Diferencia entre población y muestra
> - Interpretación de medidas de tendencia central
> - Concepto de variabilidad y dispersión
> - Lectura básica de gráficos estadísticos
>
> [!note] **Temas Avanzados**
> 
> **Próximos Pasos en Manipulación de Datos:**
> 
> - **Pandas Avanzado:** MultiIndex, pivot tables, merge/join operations
> - **Cleaning & Preprocessing:** Manejo de datos faltantes, detección de outliers
> - **Time Series Analysis:** Análisis temporal especializado, forecasting
> - **Performance Optimization:** Vectorización, memory management, chunk processing
> 
> **Análisis Estadístico Avanzado:**
> 
> - **Inferential Statistics:** Pruebas de hipótesis, intervalos de confianza
> - **Correlation & Regression:** Análisis de relaciones entre variables
> - **ANOVA:** Comparación de múltiples grupos
> - **Non-parametric Tests:** Alternativas robustas a tests paramétricos
> 
> **Visualización Especializada:**
> 
> - **Interactive Plotting:** Plotly, Bokeh para dashboards dinámicos
> - **Geographic Visualization:** Mapas y análisis espacial
> - **Advanced Seaborn:** Heatmaps, pair plots, distribution analysis
> - **Statistical Visualization:** Q-Q plots, residual analysis
> 
> **Integración con Ecosistema de Datos:**
> 
> - **SQL Integration:** Pandas + SQLAlchemy para bases de datos
> - **Big Data Tools:** Dask para datasets grandes
> - **Machine Learning Pipeline:** Scikit-learn preprocessing
> - **Web Applications:** Streamlit, Flask para deployment
> 
> **Especialización por Dominio:**
> 
> - **Financial Analysis:** Análisis de series temporales financieras
> - **Marketing Analytics:** Customer segmentation, cohort analysis
> - **Scientific Research:** Experimental design, statistical modeling
> - **Business Intelligence:** KPI tracking, automated reporting

---

#pandas #data-manipulation #groupby #filtering #statistics #visualization #python #data-analysis #seaborn #matplotlib #exploratory-data-analysis #business-intelligence #data-science #statistical-analysis #time-series #aggregation #conditional-logic #data-preprocessing #flights-dataset #trend-analysis
