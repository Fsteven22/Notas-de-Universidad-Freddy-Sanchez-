# Módulo 6.3: Manipulación de Datos

> [!quote] "Los datos son el nuevo petróleo, pero solo cuando sabemos refinarlos y extraer su valor." 📊

> [!info]- La manipulación de datos es una habilidad fundamental en el análisis de información. A través de técnicas de filtrado, agregación y transformación, podemos extraer insights valiosos de conjuntos de datos complejos. Este módulo te enseñará las herramientas esenciales para convertir datos crudos en información accionable.

## 📋 Objetivos del Módulo

> [!success]- **Al finalizar este módulo podrás:**
> 
> - Aplicar filtros complejos usando operadores lógicos
> - Realizar agregaciones y cálculos estadísticos descriptivos
> - Utilizar `groupby()` para análisis por categorías
> - Crear visualizaciones básicas para explorar datos
> - Manipular y transformar datos de manera eficiente

## 🔍 1. Filtrado y Operaciones Lógicas

> [!tip]- **Operadores Lógicos en Pandas** 🎯
> 
> Los filtros nos permiten extraer subconjuntos específicos de nuestros datos:
> 
> ### Operadores Principales:
> 
> - **`&`** (AND): Ambas condiciones deben ser verdaderas
> - **`|`** (OR): Al menos una condición debe ser verdadera
> - **`~`** (NOT): Invierte la condición lógica
> 
> ### Sintaxis Básica:
> 
> ```python
> # Filtro simple
> df[df['columna'] > valor]
> 
> # Filtros múltiples
> df[(df['col1'] > valor1) & (df['col2'] == valor2)]
> df[(df['col1'] == 'A') | (df['col1'] == 'B')]
> df[~(df['columna'] == valor)]  # Todos excepto este valor
> ```

> [!example]- **Ejemplo Práctico: Dataset de Vuelos** ✈️
> 
> ```python
> import pandas as pd
> import seaborn as sns
> 
> # Cargar dataset de vuelos
> df = sns.load_dataset('flights')
> 
> # Filtrar vuelos de julio después de 1955
> vuelos_julio_recientes = df[(df['month'] == 'Jul') & (df['year'] > 1955)]
> 
> # Vuelos del primer y último año
> vuelos_extremos = df[(df['year'] == 1949) | (df['year'] == 1960)]
> 
> # Todos los meses excepto diciembre
> sin_diciembre = df[~(df['month'] == 'Dec')]
> ```

> [!warning]- **Sustitución Condicional** 🔄
> 
> Para reemplazar valores basados en condiciones:
> 
> ### `.where()` y `.mask()`:
> 
> ```python
> # .where(): mantiene valores donde la condición es True
> df['nueva_col'] = df['columna'].where(df['columna'] > 100, other='Bajo')
> 
> # .mask(): mantiene valores donde la condición es False
> df['nueva_col'] = df['columna'].mask(df['columna'] <= 100, other='Alto')
> ```

## 📊 2. Estadísticas Descriptivas y Agregaciones

> [!info]- **Resumen Estadístico con `.describe()`** 📈
> 
> El método más rápido para obtener un panorama general:
> 
> ```python
> # Estadísticas completas de columnas numéricas
> print(df.describe())
> 
> # Estadísticas de una columna específica
> print(df['passengers'].describe())
> ```
> 
> ### Métricas Individuales:
> 
> |Método|Descripción|Ejemplo|
> |---|---|---|
> |`.mean()`|Promedio|`df['col'].mean()`|
> |`.median()`|Mediana|`df['col'].median()`|
> |`.mode()`|Moda|`df['col'].mode()`|
> |`.std()`|Desviación estándar|`df['col'].std()`|
> |`.min()/.max()`|Valores extremos|`df['col'].min()`|
> |`.sum()`|Suma total|`df['col'].sum()`|
> |`.count()`|Conteo de valores|`df['col'].count()`|

> [!example]- **Análisis Exploratorio Básico** 🔍
> 
> ```python
> # Estadísticas clave del dataset de vuelos
> print(f"Promedio mensual: {df['passengers'].mean():.0f} mil pasajeros")
> print(f"Máximo histórico: {df['passengers'].max()} mil pasajeros")
> print(f"Total periodo: {df['passengers'].sum():,} mil pasajeros")
> 
> # Encontrar los 5 meses con más tráfico
> top_5 = df.sort_values('passengers', ascending=False).head()
> print("\nTop 5 meses con más pasajeros:")
> print(top_5[['year', 'month', 'passengers']])
> ```

## 🎲 3. Análisis por Categorías con `groupby()`

> [!success]- **El Poder del GroupBy** 🚀
> 
> `groupby()` es una de las herramientas más poderosas para análisis de datos:
> 
> ### Concepto: **Dividir-Aplicar-Combinar**
> 
> ```mermaid
> graph LR
>     A[DataFrame Original] --> B[Dividir por Categoría]
>     B --> C[Aplicar Función]
>     C --> D[Combinar Resultados]
>     
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
> ```
> 
> ### Sintaxis Básica:
> 
> ```python
> # Agrupar por una columna
> df.groupby('categoria')['valor'].funcion()
> 
> # Agrupar por múltiples columnas
> df.groupby(['cat1', 'cat2'])['valor'].funcion()
> 
> # Múltiples agregaciones
> df.groupby('categoria').agg({
>     'col1': 'sum',
>     'col2': 'mean',
>     'col3': ['min', 'max']
> })
> ```

> [!example]- **Ejemplos Prácticos de GroupBy** 📋
> 
> ```python
> # Análisis temporal: pasajeros por año
> por_año = df.groupby('year')['passengers'].sum()
> print("Evolución anual del tráfico:")
> print(por_año)
> 
> # Análisis estacional: promedio por mes
> estacionalidad = df.groupby('month')['passengers'].mean().sort_values(ascending=False)
> print("\nEstacionalidad mensual:")
> print(estacionalidad)
> 
> # Análisis complejo: estadísticas por década
> df['decade'] = (df['year'] // 10) * 10
> stats_decada = df.groupby('decade')['passengers'].agg(['count', 'mean', 'std', 'sum'])
> print("\nEstadísticas por década:")
> print(stats_decada)
> ```

> [!tip]- **Funciones de Agregación Avanzadas** 🧮
> 
> ```python
> # Múltiples estadísticas a la vez
> resumen_completo = df.groupby('year').agg({
>     'passengers': ['sum', 'mean', 'std', 'count'],
>     'month': 'nunique'  # Número de meses únicos por año
> })
> 
> # Agregaciones personalizadas
> def rango(serie):
>     return serie.max() - serie.min()
> 
> df.groupby('year')['passengers'].apply(rango)
> ```

## 📈 4. Visualización Básica con Pandas

> [!info]- **Integración con Matplotlib** 🎨
> 
> Pandas se integra perfectamente con Matplotlib para crear visualizaciones rápidas:
> 
> ```python
> import matplotlib.pyplot as plt
> 
> # Configuración básica para mejores gráficos
> plt.style.use('seaborn-v0_8')
> plt.rcParams['figure.figsize'] = (12, 8)
> ```

> [!example]- **Gráfico de Líneas: Tendencias Temporales** 📊
> 
> Perfecto para mostrar evolución en el tiempo:
> 
> ```python
> # Evolución anual del tráfico
> pasajeros_anuales = df.groupby('year')['passengers'].sum()
> 
> pasajeros_anuales.plot(kind='line', 
>                       marker='o', 
>                       linewidth=2,
>                       markersize=8,
>                       color='steelblue')
> 
> plt.title('Evolución del Tráfico Aéreo (1949-1960)', fontsize=16, pad=20)
> plt.xlabel('Año', fontsize=12)
> plt.ylabel('Pasajeros (miles)', fontsize=12)
> plt.grid(True, alpha=0.3)
> plt.tight_layout()
> plt.show()
> ```

> [!example]- **Gráfico de Barras: Comparación de Categorías** 📊
> 
> Ideal para comparar valores entre diferentes grupos:
> 
> ```python
> # Análisis estacional
> estacionalidad = df.groupby('month')['passengers'].mean()
> 
> # Reordenar meses cronológicamente
> orden_meses = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
>                'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
> estacionalidad = estacionalidad.reindex(orden_meses)
> 
> estacionalidad.plot(kind='bar', 
>                    color='lightcoral',
>                    edgecolor='black',
>                    alpha=0.8)
> 
> plt.title('Estacionalidad del Tráfico Aéreo', fontsize=16, pad=20)
> plt.xlabel('Mes', fontsize=12)
> plt.ylabel('Promedio de Pasajeros (miles)', fontsize=12)
> plt.xticks(rotation=45)
> plt.tight_layout()
> plt.show()
> ```

> [!example]- **Boxplot: Distribución por Categorías** 📦
> 
> Excelente para entender la distribución y variabilidad:
> 
> ```python
> # Distribución anual de pasajeros
> df.boxplot(column='passengers', 
>           by='year', 
>           figsize=(14, 8),
>           patch_artist=True)
> 
> plt.suptitle('')  # Remover título automático
> plt.title('Distribución Mensual de Pasajeros por Año', fontsize=16, pad=20)
> plt.xlabel('Año', fontsize=12)
> plt.ylabel('Pasajeros (miles)', fontsize=12)
> plt.tight_layout()
> plt.show()
> ```

## 🛠️ Técnicas Avanzadas de Manipulación

> [!tip]- **Transformaciones y Operaciones Vectorizadas** ⚡
> 
> ```python
> # Crear nuevas variables derivadas
> df['passengers_scaled'] = df['passengers'] / 1000  # En millones
> df['season'] = df['month'].map({
>     'Dec': 'Winter', 'Jan': 'Winter', 'Feb': 'Winter',
>     'Mar': 'Spring', 'Apr': 'Spring', 'May': 'Spring',
>     'Jun': 'Summer', 'Jul': 'Summer', 'Aug': 'Summer',
>     'Sep': 'Fall', 'Oct': 'Fall', 'Nov': 'Fall'
> })
> 
> # Calcular cambios porcentuales
> df_sorted = df.sort_values(['year', 'month'])
> df_sorted['pct_change'] = df_sorted['passengers'].pct_change() * 100
> 
> # Crear rangos categóricos
> df['traffic_level'] = pd.cut(df['passengers'], 
>                             bins=[0, 200, 400, 600], 
>                             labels=['Bajo', 'Medio', 'Alto'])
> ```

> [!warning]- **Pivoting y Reshaping** 🔄
> 
> ```python
> # Crear tabla pivot para análisis cruzado
> pivot_table = df.pivot_table(values='passengers',
>                             index='month',
>                             columns='year',
>                             aggfunc='sum')
> 
> # Melt para convertir de wide a long format
> df_melted = pd.melt(pivot_table.reset_index(),
>                    id_vars=['month'],
>                    var_name='year',
>                    value_name='passengers')
> ```

## 💡 Estrategias de Análisis

> [!success]- **Metodología EDA (Exploratory Data Analysis)** 🔍
> 
> ### 1. **Comprensión Inicial**
> 
> ```python
> # Información general del dataset
> print(df.info())
> print(df.head())
> print(df.shape)
> ```
> 
> ### 2. **Análisis Estadístico**
> 
> ```python
> # Estadísticas descriptivas
> print(df.describe())
> print(df.isnull().sum())
> ```
> 
> ### 3. **Análisis por Categorías**
> 
> ```python
> # Patrones por grupos
> for col in df.select_dtypes(include=['object']).columns:
>     print(f"\n{col}:")
>     print(df[col].value_counts())
> ```
> 
> ### 4. **Visualización Exploratoria**
> 
> ```python
> # Distribuciones y relaciones
> df.hist(figsize=(15, 10), bins=20)
> plt.tight_layout()
> plt.show()
> ```

## ⚠️ Errores Comunes y Mejores Prácticas

> [!warning]- **Errores Frecuentes** 🚫
> 
> ### 1. **Olvidar Paréntesis en Filtros Múltiples**
> 
> ```python
> # ❌ Incorrecto
> df[df['col1'] > 5 & df['col2'] == 'A']
> 
> # ✅ Correcto  
> df[(df['col1'] > 5) & (df['col2'] == 'A')]
> ```
> 
> ### 2. **Confundir Operadores Lógicos**
> 
> ```python
> # ❌ En Python normal: and, or, not
> # ✅ En Pandas: &, |, ~
> ```
> 
> ### 3. **No Considerar Valores Nulos**
> 
> ```python
> # ❌ Puede causar resultados inesperados
> df[df['col'] > 100]
> 
> # ✅ Manejar nulos explícitamente
> df[df['col'].notna() & (df['col'] > 100)]
> ```

> [!tip]- **Mejores Prácticas** ✨
> 
> ### 1. **Encadenamiento de Métodos**
> 
> ```python
> # Operaciones fluidas
> resultado = (df
>              .query('year > 1955')
>              .groupby('month')['passengers']
>              .mean()
>              .sort_values(ascending=False))
> ```
> 
> ### 2. **Usar `.copy()` para Evitar Warnings**
> 
> ```python
> df_filtrado = df[df['year'] > 1955].copy()
> df_filtrado['nueva_col'] = df_filtrado['passengers'] * 1.1
> ```
> 
> ### 3. **Documentar Análisis Complejos**
> 
> ```python
> # Análisis estacional detallado
> estacional = (df
>               .groupby('month')['passengers']
>               .agg(['mean', 'std', 'min', 'max'])
>               .round(2))
> ```

## 🎯 Ejercicios Prácticos

> [!example]- **Ejercicio 1: Análisis Temporal** 📅
> 
> Usando el dataset de vuelos:
> 
> 1. Encuentra el año con mayor crecimiento porcentual
> 2. Identifica qué meses muestran mayor variabilidad
> 3. Calcula la tasa de crecimiento anual compuesta
> 
> ```python
> # Pista para el crecimiento anual
> crecimiento_anual = df.groupby('year')['passengers'].sum().pct_change()
> ```

> [!example]- **Ejercicio 2: Segmentación de Datos** 🎯
> 
> 4. Clasifica los meses en temporadas
> 5. Compara el comportamiento entre décadas
> 6. Identifica outliers en el tráfico mensual
> 
> ```python
> # Pista para outliers usando IQR
> Q1 = df['passengers'].quantile(0.25)
> Q3 = df['passengers'].quantile(0.75)
> IQR = Q3 - Q1
> outliers = df[(df['passengers'] < Q1 - 1.5*IQR) | 
>               (df['passengers'] > Q3 + 1.5*IQR)]
> ```

## 📚 Referencias y Recursos

> [!note]- **Documentación Oficial** 📖
> 
> - [Pandas Groupby Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
> - [Boolean Indexing Guide](https://pandas.pydata.org/docs/user_guide/indexing.html#boolean-indexing)
> - [Visualization with Pandas](https://pandas.pydata.org/docs/user_guide/visualization.html)

> [!info]- **Conexiones con Otros Módulos** 🔗
> 
> - **[[Módulo 6.1 Introducción a NumPy]]** - Fundamentos de arrays numéricos
> - **[[Módulo 6.2 Intro a Pandas]]** - Conceptos básicos de DataFrames
> - **[[Módulo 5.1 Diccionarios]]** - Estructuras de datos relacionadas
> - **[[Módulo 4.1 Condicional]]** - Lógica de control aplicada a datos

## 🏆 Resumen del Módulo

> [!success]- **Conceptos Clave Dominados** ✅
> 
> - **Filtrado avanzado** con operadores lógicos (`&`, `|`, `~`)
> - **Estadísticas descriptivas** para caracterizar datos
> - **Análisis por categorías** usando `groupby()`
> - **Visualización exploratoria** con Pandas y Matplotlib
> - **Transformaciones** y manipulaciones de datos
> - **Mejores prácticas** para análisis eficiente

> [!quote]- **Reflexión Final** 💭
> 
> _"La manipulación de datos no es solo una habilidad técnica; es el arte de hacer las preguntas correctas y encontrar las respuestas ocultas en la información. Cada filtro, cada agregación, cada visualización nos acerca más a la comprensión profunda de nuestros datos."_

---

**Tags:** #pandas #analisis-datos #groupby #filtros #estadisticas #visualizacion #manipulacion-datos #python #data-science