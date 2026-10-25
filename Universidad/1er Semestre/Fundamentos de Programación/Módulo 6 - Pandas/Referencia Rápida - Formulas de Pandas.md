---
dg-publish: true
---

# 📊 Tabla de Fórmulas y Métodos de Pandas

## 🎯 Referencia Rápida - Módulo 6: Pandas 

### 📚 **1. IMPORTACIÓN Y CONFIGURACIÓN**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`import pandas as pd`|Importar Pandas con alias estándar|`import pandas as pd`|
|`pd.set_option()`|Configurar opciones de visualización|`pd.set_option('display.max_columns', None)`|
|`pd.__version__`|Verificar versión de Pandas|`print(pd.__version__)`|

### 🏗️ **2. CREACIÓN DE ESTRUCTURAS DE DATOS**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`pd.Series()`|Crear una Serie (array 1D)|`pd.Series([1, 2, 3], index=['a', 'b', 'c'])`|
|`pd.DataFrame()`|Crear DataFrame desde diccionario|`pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})`|
|`pd.DataFrame(data, columns=[], index=[])`|DataFrame con columnas e índices específicos|`pd.DataFrame(data, columns=['A', 'B'])`|

### 📁 **3. LECTURA Y ESCRITURA DE ARCHIVOS**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`pd.read_csv()`|Leer archivo CSV|`pd.read_csv('archivo.csv')`|
|`pd.read_excel()`|Leer archivo Excel|`pd.read_excel('archivo.xlsx', sheet_name='Hoja1')`|
|`pd.read_json()`|Leer archivo JSON|`pd.read_json('archivo.json')`|
|`df.to_csv()`|Guardar DataFrame como CSV|`df.to_csv('salida.csv', index=False)`|
|`df.to_excel()`|Guardar DataFrame como Excel|`df.to_excel('salida.xlsx', index=False)`|

### 🔍 **4. EXPLORACIÓN Y INFORMACIÓN DEL DATAFRAME**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`df.shape`|Dimensiones (filas, columnas)|`print(df.shape)`|
|`df.head(n)`|Primeras n filas|`df.head(5)`|
|`df.tail(n)`|Últimas n filas|`df.tail(3)`|
|`df.sample(n)`|Muestra aleatoria de n filas|`df.sample(10)`|
|`df.info()`|Información general del DataFrame|`df.info()`|
|`df.describe()`|Estadísticas descriptivas|`df.describe()`|
|`df.dtypes`|Tipos de datos de las columnas|`df.dtypes`|
|`df.columns`|Lista de columnas|`list(df.columns)`|
|`df.index`|Información del índice|`df.index`|
|`df.size`|Total de elementos|`df.size`|
|`df.memory_usage()`|Uso de memoria|`df.memory_usage(deep=True)`|

### 🎯 **5. SELECCIÓN DE DATOS**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`df['columna']`|Seleccionar una columna (Series)|`df['Nombre']`|
|`df[['col1', 'col2']]`|Seleccionar múltiples columnas|`df[['Nombre', 'Edad']]`|
|`df.loc[fila, columna]`|Selección por etiquetas|`df.loc[0, 'Nombre']`|
|`df.iloc[posición]`|Selección por posición numérica|`df.iloc[0:5, 1:3]`|
|`df.loc[inicio:fin]`|Rango por etiquetas (inclusivo)|`df.loc[2:5]`|
|`df.iloc[inicio:fin]`|Rango por posición (exclusivo)|`df.iloc[0:3]`|
|`df.select_dtypes(include=[])`|Seleccionar por tipo de datos|`df.select_dtypes(include=[np.number])`|

### 🔍 **6. FILTRADO CONDICIONAL**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`df[df['col'] > valor]`|Filtro simple|`df[df['Edad'] > 25]`|
|`df[condición1 & condición2]`|Filtro con AND (&)|`df[(df['Edad'] > 20) & (df['Activo'] == True)]`|
|`df[condición1 \| condición2]`|Filtro con OR (\|)|`df[(df['Edad'] < 18) \| (df['Edad'] > 65)]`|
|`df[~condición]`|Filtro con NOT (~)|`df[~(df['Departamento'] == 'IT')]`|
|`df['col'].isin(lista)`|Filtrar por lista de valores|`df[df['Ciudad'].isin(['Quito', 'Guayaquil'])]`|
|`df.query('condición')`|Filtro con sintaxis SQL|`df.query('Edad > 25 and Activo == True')`|
|`df['col'].between(min, max)`|Filtrar por rango|`df[df['Salario'].between(30000, 50000)]`|

### 📊 **7. ANÁLISIS ESTADÍSTICO**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`df['col'].mean()`|Promedio de una columna|`df['Salario'].mean()`|
|`df['col'].median()`|Mediana de una columna|`df['Salario'].median()`|
|`df['col'].max()`|Valor máximo|`df['Salario'].max()`|
|`df['col'].min()`|Valor mínimo|`df['Salario'].min()`|
|`df['col'].std()`|Desviación estándar|`df['Salario'].std()`|
|`df['col'].value_counts()`|Conteo de valores únicos|`df['Departamento'].value_counts()`|
|`df['col'].nunique()`|Número de valores únicos|`df['Ciudad'].nunique()`|
|`df['col'].quantile(q)`|Cuantil específico|`df['Salario'].quantile(0.75)`|

### 🔧 **8. MANEJO DE VALORES NULOS**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`df.isnull()`|Detectar valores nulos|`df.isnull().sum()`|
|`df.isna()`|Detectar valores nulos (alias)|`df.isna().sum()`|
|`df.notnull()`|Detectar valores no nulos|`df.notnull().sum()`|
|`df.dropna()`|Eliminar filas con valores nulos|`df.dropna()`|
|`df.fillna(valor)`|Rellenar valores nulos|`df.fillna(0)`|

### 🔄 **9. MANIPULACIÓN DE DATOS**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`df.copy()`|Crear copia del DataFrame|`df_copia = df.copy()`|
|`df.duplicated()`|Detectar duplicados|`df.duplicated().sum()`|
|`df.drop_duplicates()`|Eliminar duplicados|`df.drop_duplicates()`|
|`df.set_index('col')`|Establecer columna como índice|`df.set_index('ID')`|
|`df.reset_index()`|Resetear índice|`df.reset_index(drop=True)`|
|`df.sort_values('col')`|Ordenar por columna|`df.sort_values('Salario', ascending=False)`|

### 🎨 **10. OPERACIONES CON STRINGS**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`df['col'].str.contains('texto')`|Buscar texto en string|`df['Nombre'].str.contains('Ana')`|
|`df['col'].str.upper()`|Convertir a mayúsculas|`df['Ciudad'].str.upper()`|
|`df['col'].str.lower()`|Convertir a minúsculas|`df['Ciudad'].str.lower()`|
|`df['col'].str.len()`|Longitud del string|`df['Nombre'].str.len()`|

### 📈 **11. AGRUPACIÓN Y AGREGACIÓN**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`df.groupby('col')`|Agrupar por columna|`df.groupby('Departamento')`|
|`df.groupby('col').agg({})`|Agregar con múltiples funciones|`df.groupby('Depto').agg({'Salario': ['mean', 'max']})`|
|`df.groupby('col').mean()`|Promedio por grupo|`df.groupby('Departamento')['Salario'].mean()`|
|`df.groupby('col').count()`|Conteo por grupo|`df.groupby('Ciudad').count()`|

### ⚙️ **12. CONFIGURACIÓN Y UTILIDADES**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`pd.ExcelWriter()`|Escribir múltiples hojas Excel|`with pd.ExcelWriter('archivo.xlsx') as writer:`|
|`pd.json_normalize()`|Normalizar datos JSON|`pd.json_normalize(data)`|
|`pd.read_sql_query()`|Leer desde base de datos|`pd.read_sql_query('SELECT * FROM tabla', conn)`|
|`df.pipe(función)`|Aplicar función al DataFrame|`df.pipe(mi_funcion)`|

---

## 💡 **NOTAS IMPORTANTES**

- 🔸 **Paréntesis**: Usar paréntesis en condiciones múltiples: `(condición1) & (condición2)`
- 🔸 **Operadores lógicos**: `&` (AND), `|` (OR), `~` (NOT) en lugar de `and`, `or`, `not`
- 🔸 **Cadenas**: Usar `.str` para métodos de string: `df['col'].str.contains()`
- 🔸 **Copias**: Siempre usar `.copy()` para evitar modificaciones no deseadas
- 🔸 **Índices**: `.loc` para etiquetas, `.iloc` para posiciones numéricas

---

_Esta tabla cubre las fórmulas y métodos principales del Módulo 6.2. Para casos más avanzados, consultar la documentación oficial de Pandas._