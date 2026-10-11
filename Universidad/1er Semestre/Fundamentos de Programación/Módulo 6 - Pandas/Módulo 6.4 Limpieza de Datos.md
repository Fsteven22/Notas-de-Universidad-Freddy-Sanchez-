---
dg-publish: true
---

# Módulo 6.4: Limpieza de Datos

> [!quote] "Los datos sucios son como diamantes en bruto: requieren paciencia, técnica y precisión para revelar su verdadero valor." 💎
>
> [!info] La limpieza de datos es una etapa fundamental en cualquier proyecto de análisis. Los datos del mundo real raramente vienen perfectos: tienen valores faltantes, duplicados, tipos incorrectos y inconsistencias. Este módulo te enseñará las técnicas esenciales para transformar datos "sucios" en información confiable y lista para el análisis.

## 📋 Objetivos del Módulo

> [!success] **Al finalizar este módulo podrás:**
> 
> - Identificar y manejar valores faltantes de manera estratégica
> - Detectar y eliminar duplicados efectivamente
> - Transformar tipos de datos para optimizar el análisis
> - Aplicar funciones personalizadas para limpiar y categorizar datos
> - Realizar filtros avanzados con múltiples criterios
> - Implementar un flujo completo de limpieza de datos

## 🚨 1. El Desafío de los Datos Reales (Messy Data)

> [!warning] **La Realidad de los Datos** 🌪️
> 
> Los datos perfectos son una utopía. En el mundo real, nos enfrentamos a:
> 
> ### Problemas Comunes:
> 
> - **Valores faltantes** (NaN, None, espacios vacíos)
> - **Tipos de datos incorrectos** (números como texto)
> - **Duplicados** que sesgan el análisis
> - **Inconsistencias** en formato y nomenclatura
> - **Outliers** y valores imposibles
> - **Codificaciones mixtas** (0/1 vs Si/No)
>
> [!example] **Dataset de Ejemplo: Titanic** 🚢
> 
> Trabajaremos con el famoso dataset del Titanic, que presenta múltiples desafíos reales:
> 
> ```python
> import pandas as pd
> import numpy as np
> import seaborn as sns
> 
> # Cargar el dataset del Titanic
> titanic = sns.load_dataset('titanic')
> 
> # Primer vistazo a nuestros datos "sucios"
> print("Forma del dataset:", titanic.shape)
> print("\nPrimeras 5 filas:")
> print(titanic.head())
> 
> # Información general del dataset
> print("\nInformación del dataset:")
> print(titanic.info())
> ```
> 
> ### Problemas Identificados:
> 
> |Problema|Columna|Descripción|
> |---|---|---|
> |Valores faltantes|`age`, `deck`|Edades y cubiertas sin registrar|
> |Tipos mixtos|`survived`, `pclass`|Números que representan categorías|
> |Codificación poco clara|`survived`|0/1 en lugar de No/Sí|
> |Potenciales duplicados|Múltiples|Registros repetidos|

## 🔍 2. Detección y Manejo de Valores Faltantes

> [!tip] **Estrategia de Detección** 🕵️
> 
> Antes de decidir qué hacer con los valores faltantes, debemos entender su patrón:
> 
> ```python
> # Análisis completo de valores nulos
> def analizar_nulos(df):
>     # Conteo de nulos por columna
>     nulos = df.isnull().sum()
>     porcentaje = (nulos / len(df)) * 100
>     
>     # Crear resumen
>     resumen = pd.DataFrame({
>         'Valores_Nulos': nulos,
>         'Porcentaje': porcentaje.round(2)
>     }).sort_values('Valores_Nulos', ascending=False)
>     
>     return resumen[resumen['Valores_Nulos'] > 0]
> 
> print("Análisis de valores faltantes:")
> print(analizar_nulos(titanic))
> ```
>
> [!info] **Métodos de Detección** 🔎
> 
> ### Funciones Principales:
> 
> ```python
> # Detectar valores nulos
> titanic.isnull()          # DataFrame booleano
> titanic.isna()            # Sinónimo de isnull()
> titanic.isnull().sum()    # Conteo por columna
> titanic.isnull().any()    # ¿Hay algún nulo por columna?
> titanic.isnull().all()    # ¿Son todos nulos por columna?
> 
> # Detectar valores no nulos
> titanic.notnull()         # Opuesto a isnull()
> titanic.notna()           # Sinónimo de notnull()
> ```
> 
> ### Visualización de Patrones:
> 
> ```python
> import matplotlib.pyplot as plt
> 
> # Mapa de calor de valores faltantes
> plt.figure(figsize=(12, 8))
> sns.heatmap(titanic.isnull(), cbar=True, yticklabels=False, cmap='viridis')
> plt.title('Patrón de Valores Faltantes')
> plt.show()
> ```

## 🛠️ 3. Estrategias para Valores Faltantes

> [!success] **Opción 1: Eliminación con `.dropna()`** 🗑️
> 
> ### Eliminar Filas:
> 
> ```python
> # Crear copia para trabajar seguro
> titanic_limpio = titanic.copy()
> 
> # Eliminar filas con cualquier valor nulo
> titanic_sin_nulos = titanic_limpio.dropna()
> 
> # Eliminar filas solo si faltan valores en columnas específicas
> titanic_edad_completa = titanic_limpio.dropna(subset=['age'])
> 
> # Eliminar solo si faltan TODOS los valores en la fila
> titanic_limpio.dropna(how='all', inplace=True)
> ```
> 
> ### Eliminar Columnas:
> 
> ```python
> # Eliminar columnas con muchos nulos (ej: >50% faltantes)
> umbral_nulos = len(titanic) * 0.5
> titanic_limpio.dropna(axis=1, thresh=umbral_nulos, inplace=True)
> 
> # Eliminar columna específica
> titanic_limpio.drop('deck', axis=1, inplace=True)
> 
> print(f"Columnas restantes: {list(titanic_limpio.columns)}")
> ```
>
> [!tip] **Opción 2: Imputación con `.fillna()`** 🔧
> 
> ### Estrategias por Tipo de Variable:
> 
> #### Variables Numéricas:
> 
> ```python
> # Rellenar con medidas de tendencia central
> titanic_limpio['age'].fillna(titanic_limpio['age'].median(), inplace=True)
> titanic_limpio['fare'].fillna(titanic_limpio['fare'].mean(), inplace=True)
> 
> # Imputación por grupos (más sofisticada)
> edad_por_clase = titanic_limpio.groupby('pclass')['age'].median()
> titanic_limpio['age'] = titanic_limpio.apply(
>     lambda row: edad_por_clase[row['pclass']] if pd.isna(row['age']) else row['age'],
>     axis=1
> )
> ```
> 
> #### Variables Categóricas:
> 
> ```python
> # Rellenar con la moda (valor más frecuente)
> moda_embarque = titanic_limpio['embark_town'].mode()[0]
> titanic_limpio['embark_town'].fillna(moda_embarque, inplace=True)
> titanic_limpio['embarked'].fillna(moda_embarque[0], inplace=True)
> 
> # Crear categoría "Desconocido"
> titanic_limpio['deck'].fillna('Desconocido', inplace=True)
> ```
> 
> #### Imputación Avanzada:
> 
> ```python
> # Forward fill (propagar último valor válido)
> titanic_limpio['columna'].fillna(method='ffill', inplace=True)
> 
> # Backward fill (propagar siguiente valor válido)
> titanic_limpio['columna'].fillna(method='bfill', inplace=True)
> 
> # Interpolación lineal para series temporales
> titanic_limpio['columna'].interpolate(method='linear', inplace=True)
> ```
>
> [!example] **Ejemplo Completo: Estrategia Híbrida** 🎯
> 
> ```python
> def limpiar_valores_faltantes(df):
>     """
>     Función comprehensiva para manejo de valores faltantes
>     """
>     df_limpio = df.copy()
>     
>     # 1. Eliminar columnas con >70% de valores faltantes
>     umbral = len(df_limpio) * 0.3
>     df_limpio = df_limpio.dropna(axis=1, thresh=umbral)
>     
>     # 2. Imputar variables numéricas con mediana por grupo
>     if 'age' in df_limpio.columns:
>         edad_por_genero = df_limpio.groupby('sex')['age'].median()
>         for genero in df_limpio['sex'].unique():
>             mask = (df_limpio['sex'] == genero) & (df_limpio['age'].isna())
>             df_limpio.loc[mask, 'age'] = edad_por_genero[genero]
>     
>     # 3. Imputar variables categóricas con moda
>     cols_categoricas = df_limpio.select_dtypes(include=['object']).columns
>     for col in cols_categoricas:
>         if df_limpio[col].isna().any():
>             moda = df_limpio[col].mode()[0] if not df_limpio[col].mode().empty else 'Desconocido'
>             df_limpio[col].fillna(moda, inplace=True)
>     
>     return df_limpio
> 
> # Aplicar nuestra función
> titanic_limpio = limpiar_valores_faltantes(titanic)
> print("Verificación final de nulos:")
> print(titanic_limpio.isnull().sum())
> ```

## 🔄 4. Manejo de Duplicados

> [!warning] **Detección de Duplicados** 👥
> 
> Los duplicados pueden sesgar significativamente nuestro análisis:
> 
> ```python
> # Detectar filas completamente duplicadas
> duplicados_completos = titanic_limpio.duplicated()
> print(f"Filas completamente duplicadas: {duplicados_completos.sum()}")
> 
> # Detectar duplicados en columnas específicas
> duplicados_parciales = titanic_limpio.duplicated(subset=['name', 'age', 'sex'])
> print(f"Posibles pasajeros duplicados: {duplicados_parciales.sum()}")
> 
> # Ver las filas duplicadas
> filas_duplicadas = titanic_limpio[duplicados_completos]
> print("Ejemplos de duplicados:")
> print(filas_duplicadas)
> ```
>
> [!tip] **Eliminación Inteligente de Duplicados** 🧹
> 
> ```python
> # Eliminar duplicados completos (conservar el primero)
> titanic_limpio.drop_duplicates(inplace=True)
> 
> # Eliminar duplicados basados en columnas clave (conservar el último)
> titanic_limpio.drop_duplicates(
>     subset=['name', 'age', 'sex'], 
>     keep='last', 
>     inplace=True
> )
> 
> # Función personalizada para duplicados complejos
> def eliminar_duplicados_inteligente(df):
>     """
>     Elimina duplicados conservando el registro más completo
>     """
>     # Crear score de completitud por fila
>     df['completitud'] = df.count(axis=1)
>     
>     # Eliminar duplicados conservando el más completo
>     df_sin_duplicados = df.loc[df.groupby(['name', 'age', 'sex'])['completitud'].idxmax()]
>     
>     # Eliminar columna temporal
>     df_sin_duplicados.drop('completitud', axis=1, inplace=True)
>     
>     return df_sin_duplicados
> 
> titanic_limpio = eliminar_duplicados_inteligente(titanic_limpio)
> print(f"Filas después de limpieza: {len(titanic_limpio)}")
> ```

## 🔧 5. Transformación y Estandarización de Datos

> [!success] **Transformación de Tipos de Datos** 📊
> 
> ### Conversiones Básicas:
> 
> ```python
> # Convertir a tipos apropiados
> titanic_limpio['pclass'] = titanic_limpio['pclass'].astype('category')
> titanic_limpio['survived'] = titanic_limpio['survived'].astype('bool')
> titanic_limpio['age'] = pd.to_numeric(titanic_limpio['age'], errors='coerce')
> 
> # Verificar cambios
> print("Nuevos tipos de datos:")
> print(titanic_limpio.dtypes)
> ```
> 
> ### Mapeo de Valores:
> 
> ```python
> # Mapear valores para mejor legibilidad
> mapeo_supervivencia = {0: 'No', 1: 'Sí', False: 'No', True: 'Sí'}
> titanic_limpio['survived'] = titanic_limpio['survived'].map(mapeo_supervivencia)
> 
> # Mapear múltiples columnas
> mapeos = {
>     'sex': {'male': 'Masculino', 'female': 'Femenino'},
>     'embarked': {'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'}
> }
> 
> for columna, mapeo in mapeos.items():
>     if columna in titanic_limpio.columns:
>         titanic_limpio[columna] = titanic_limpio[columna].map(mapeo)
> ```
>
> [!example] **Funciones Personalizadas con `.apply()`** ⚙️
> 
> ### Categorización Automática:
> 
> ```python
> # Función para categorizar edad
> def categorizar_edad(edad):
>     """Categoriza la edad en grupos demográficos"""
>     if pd.isna(edad):
>         return 'Desconocido'
>     elif edad < 12:
>         return 'Niño'
>     elif 12 <= edad < 18:
>         return 'Adolescente'  
>     elif 18 <= edad < 65:
>         return 'Adulto'
>     else:
>         return 'Adulto Mayor'
> 
> # Aplicar función a la columna
> titanic_limpio['grupo_edad'] = titanic_limpio['age'].apply(categorizar_edad)
> 
> # Verificar distribución
> print("Distribución por grupos de edad:")
> print(titanic_limpio['grupo_edad'].value_counts())
> ```
> 
> ### Extracción de Información:
> 
> ```python
> # Extraer título del nombre
> def extraer_titulo(nombre):
>     """Extrae el título del nombre completo"""
>     import re
>     titulo = re.search(r' ([A-Za-z]+)\.', nombre)
>     return titulo.group(1) if titulo else 'Desconocido'
> 
> titanic_limpio['titulo'] = titanic_limpio['name'].apply(extraer_titulo)
> 
> # Estandarizar títulos poco comunes
> titulos_raros = ['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona']
> titanic_limpio['titulo'] = titanic_limpio['titulo'].replace(titulos_raros, 'Especial')
> 
> print("Títulos encontrados:")
> print(titanic_limpio['titulo'].value_counts())
> ```

## 🔍 6. Filtros y Búsquedas Avanzadas

> [!tip] **Filtrado con Múltiples Criterios** 🎯
> 
> ### Usar `.isin()` para Múltiples Valores:
> 
> ```python
> # Filtrar pasajeros de primera y segunda clase
> clases_premium = [1, 2]
> pasajeros_premium = titanic_limpio[titanic_limpio['pclass'].isin(clases_premium)]
> 
> # Filtrar por múltiples puertos de embarque
> puertos_principales = ['Southampton', 'Cherbourg']
> desde_puertos_principales = titanic_limpio[titanic_limpio['embarked'].isin(puertos_principales)]
> 
> print(f"Pasajeros de clase premium: {len(pasajeros_premium)}")
> print(f"Desde puertos principales: {len(desde_puertos_principales)}")
> ```
>
> [!example] **Búsquedas en Texto con `.str`** 🔤
> 
> ```python
> # Buscar patrones en nombres
> apellidos_nobles = titanic_limpio[titanic_limpio['name'].str.contains('Lord|Lady|Sir|Count', case=False, na=False)]
> 
> # Buscar por longitud de nombre
> nombres_largos = titanic_limpio[titanic_limpio['name'].str.len() > 30]
> 
> # Extraer información con regex
> import re
> 
> # Encontrar pasajeros con iniciales en el nombre
> con_iniciales = titanic_limpio[titanic_limpio['name'].str.contains(r'\b[A-Z]\.$', na=False)]
> 
> print(f"Pasajeros con títulos nobles: {len(apellidos_nobles)}")
> print(f"Nombres muy largos: {len(nombres_largos)}")
> print(f"Con iniciales: {len(con_iniciales)}")
> ```
>
> [!warning] **Query Avanzado** 🔍
> 
> ```python
> # Usar .query() para filtros complejos más legibles
> supervivientes_jovenes = titanic_limpio.query('survived == "Sí" and age < 30 and pclass in [1, 2]')
> 
> familias_grandes = titanic_limpio.query('sibsp + parch > 3')
> 
> mujeres_primera_clase = titanic_limpio.query('sex == "Femenino" and pclass == 1 and age >= 18')
> 
> print(f"Supervivientes jóvenes de clase alta: {len(supervivientes_jovenes)}")
> print(f"Familias grandes: {len(familias_grandes)}")
> print(f"Mujeres adultas de primera clase: {len(mujeres_primera_clase)}")
> ```

## 🧼 7. Pipeline Completo de Limpieza

> [!success] **Función Integral de Limpieza** 🏭
> 
> ```python
> def pipeline_limpieza_completo(df, config=None):
>     """
>     Pipeline completo de limpieza de datos
>     """
>     if config is None:
>         config = {
>             'umbral_nulos_columnas': 0.7,
>             'columnas_eliminar': ['deck'],  # Columnas específicas a eliminar
>             'imputacion_numericas': 'median',
>             'imputacion_categoricas': 'mode',
>             'eliminar_duplicados': True,
>             'estandarizar_texto': True
>         }
>     
>     print("🧼 Iniciando pipeline de limpieza...")
>     df_limpio = df.copy()
>     original_shape = df_limpio.shape
>     
>     # 1. Eliminar columnas problemáticas
>     if config['columnas_eliminar']:
>         df_limpio.drop(columns=config['columnas_eliminar'], errors='ignore', inplace=True)
>         print(f"✅ Eliminadas columnas específicas: {config['columnas_eliminar']}")
>     
>     # 2. Eliminar columnas con muchos nulos
>     umbral = len(df_limpio) * (1 - config['umbral_nulos_columnas'])
>     df_limpio = df_limpio.dropna(axis=1, thresh=umbral)
>     
>     # 3. Manejar valores faltantes
>     # Numéricas
>     cols_numericas = df_limpio.select_dtypes(include=[np.number]).columns
>     for col in cols_numericas:
>         if df_limpio[col].isna().any():
>             if config['imputacion_numericas'] == 'median':
>                 valor = df_limpio[col].median()
>             elif config['imputacion_numericas'] == 'mean':
>                 valor = df_limpio[col].mean()
>             else:
>                 valor = 0
>             df_limpio[col].fillna(valor, inplace=True)
>     
>     # Categóricas
>     cols_categoricas = df_limpio.select_dtypes(include=['object']).columns
>     for col in cols_categoricas:
>         if df_limpio[col].isna().any():
>             if config['imputacion_categoricas'] == 'mode':
>                 moda = df_limpio[col].mode()
>                 valor = moda[0] if not moda.empty else 'Desconocido'
>             else:
>                 valor = 'Desconocido'
>             df_limpio[col].fillna(valor, inplace=True)
>     
>     # 4. Eliminar duplicados
>     if config['eliminar_duplicados']:
>         df_limpio.drop_duplicates(inplace=True)
>         print(f"✅ Eliminados {original_shape[0] - len(df_limpio)} duplicados")
>     
>     # 5. Estandarizar texto
>     if config['estandarizar_texto']:
>         for col in cols_categoricas:
>             df_limpio[col] = df_limpio[col].str.strip().str.title()
>     
>     # 6. Optimizar tipos de datos
>     df_limpio = optimizar_tipos_datos(df_limpio)
>     
>     print(f"🎉 Limpieza completada!")
>     print(f"📊 Forma original: {original_shape}")
>     print(f"📊 Forma final: {df_limpio.shape}")
>     print(f"📉 Reducción: {((original_shape[0] - df_limpio.shape[0]) / original_shape[0] * 100):.1f}% filas")
>     
>     return df_limpio
> 
> def optimizar_tipos_datos(df):
>     """Optimiza los tipos de datos para ahorrar memoria"""
>     for col in df.columns:
>         if df[col].dtype == 'object':
>             if df[col].nunique() / len(df) < 0.5:  # Si tiene pocos valores únicos
>                 df[col] = df[col].astype('category')
>         elif df[col].dtype in ['int64', 'float64']:
>             if df[col].min() >= 0 and df[col].max() < 255:
>                 df[col] = df[col].astype('uint8')
>             elif df[col].min() >= -128 and df[col].max() < 127:
>                 df[col] = df[col].astype('int8')
>     
>     return df
> 
> # Aplicar pipeline completo
> titanic_final = pipeline_limpieza_completo(titanic)
> ```

## 📊 8. Validación de la Limpieza

> [!info] **Verificación de Calidad** ✅
> 
> ```python
> def reporte_calidad_datos(df, df_original):
>     """
>     Genera un reporte completo de calidad de datos
>     """
>     print("=" * 50)
>     print("📋 REPORTE DE CALIDAD DE DATOS")
>     print("=" * 50)
>     
>     # Información básica
>     print(f"📊 Registros originales: {len(df_original):,}")
>     print(f"📊 Registros finales: {len(df):,}")
>     print(f"📉 Pérdida de datos: {((len(df_original) - len(df)) / len(df_original) * 100):.2f}%")
>     
>     # Valores nulos
>     nulos_restantes = df.isnull().sum().sum()
>     print(f"\n🔍 Valores nulos restantes: {nulos_restantes}")
>     
>     # Duplicados
>     duplicados_restantes = df.duplicated().sum()
>     print(f"👥 Duplicados restantes: {duplicados_restantes}")
>     
>     # Tipos de datos
>     print(f"\n📈 Resumen de tipos:")
>     print(df.dtypes.value_counts().to_string())
>     
>     # Memory usage
>     memoria_mb = df.memory_usage(deep=True).sum() / 1024**2
>     print(f"\n💾 Uso de memoria: {memoria_mb:.2f} MB")
>     
>     # Completitud por columna
>     completitud = ((df.count() / len(df)) * 100).round(2)
>     print(f"\n✅ Completitud por columna:")
>     for col, pct in completitud.items():
>         status = "✅" if pct == 100 else "⚠️" if pct > 90 else "❌"
>         print(f"   {status} {col}: {pct}%")
>     
>     return {
>         'registros_finales': len(df),
>         'perdida_datos_pct': ((len(df_original) - len(df)) / len(df_original) * 100),
>         'nulos_restantes': nulos_restantes,
>         'duplicados_restantes': duplicados_restantes,
>         'memoria_mb': memoria_mb,
>         'completitud_promedio': completitud.mean()
>     }
> 
> # Generar reporte
> metricas = reporte_calidad_datos(titanic_final, titanic)
> ```

## ⚠️ Errores Comunes y Mejores Prácticas

> [!warning] **Errores Frecuentes** 🚫
> 
> ### 1. **Eliminar Datos Sin Análisis Previo**
> 
> ```python
> # ❌ Malo: Eliminar sin entender el impacto
> df.dropna()  # Puede eliminar 90% de los datos
> 
> # ✅ Bueno: Analizar primero
> print(f"Impacto de eliminar nulos: {(df.dropna().shape[0] / df.shape[0] * 100):.1f}% datos restantes")
> ```
> 
> ### 2. **Imputación Ingenua**
> 
> ```python
> # ❌ Malo: Usar siempre la media
> df['age'].fillna(df['age'].mean())
> 
> # ✅ Bueno: Imputación contextual
> df['age'].fillna(df.groupby(['sex', 'pclass'])['age'].transform('median'))
> ```
> 
> ### 3. **No Validar Después de Limpiar**
> 
> ```python
> # ❌ Malo: Asumir que todo está bien
> df_limpio = limpiar_datos(df)
> 
> # ✅ Bueno: Validar siempre
> assert df_limpio.isnull().sum().sum() == 0, "¡Aún hay valores nulos!"
> assert df_limpio.duplicated().sum() == 0, "¡Aún hay duplicados!"
> ```
>
> [!tip] **Mejores Prácticas** ⭐
> 
> ### 1. **Trabajar con Copias**
> 
> ```python
> # Siempre trabajar con copias
> df_trabajo = df.copy()
> # Aplicar transformaciones...
> ```
> 
> ### 2. **Documentar Decisiones**
> 
> ```python
> # Documentar el proceso
> log_limpieza = {
>     'fecha': pd.Timestamp.now(),
>     'filas_originales': len(df),
>     'columnas_eliminadas': ['deck'],
>     'estrategia_nulos': 'mediana para numéricas, moda para categóricas',
>     'duplicados_eliminados': df.duplicated().sum()
> }
> ```
> 
> ### 3. **Preservar Datos Originales**
> 
> ```python
> # Guardar versión original
> df.to_pickle('datos_originales.pkl')
> # Guardar versión limpia
> df_limpio.to_pickle('datos_limpios.pkl')
> ```

## 🎯 Ejercicios Prácticos

> [!example] **Ejercicio 1: Limpieza Completa del Titanic** 🚢
> 
> Implementa un pipeline personalizado que:
> 
> 1. Analice el patrón de valores faltantes
> 2. Decida estrategias específicas por columna
> 3. Cree nuevas variables derivadas
> 4. Valide la calidad final
> 
> ```python
> def mi_pipeline_titanic(df):
>     """
>     Tu implementación personalizada aquí
>     """
>     # Pistas:
>     # - La edad puede imputarse por título y clase
>     # - El puerto de embarque
> ```
