# 📚 Tabla de Fórmulas y Métodos de Diccionarios

## 🎯 Referencia Rápida - Módulo 5: Diccionarios en Python

### 🏗️ **1. CREACIÓN DE DICCIONARIOS**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`{}`|Diccionario vacío|`dict_vacio = {}`|
|`dict()`|Constructor de diccionario vacío|`dict_vacio = dict()`|
|`{'clave': 'valor'}`|Diccionario con elementos|`persona = {'nombre': 'Juan', 'edad': 25}`|
|`dict(clave=valor)`|Diccionario usando argumentos|`dict(nombre='Ana', edad=30)`|
|`dict(zip(claves, valores))`|Desde listas separadas|`dict(zip(['a', 'b'], [1, 2]))`|
|`dict.fromkeys(claves, valor)`|Múltiples claves con mismo valor|`dict.fromkeys(['a', 'b', 'c'], 0)`|
|`{k: v for k, v in iterable}`|Comprensión de diccionarios|`{x: x**2 for x in range(5)}`|

### 🔍 **2. ACCESO Y CONSULTA**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`dict['clave']`|Acceso directo (puede dar error)|`persona['nombre']`|
|`dict.get('clave')`|Acceso seguro (devuelve None)|`persona.get('telefono')`|
|`dict.get('clave', valor_default)`|Acceso con valor por defecto|`persona.get('telefono', 'No disponible')`|
|`'clave' in dict`|Verificar si existe la clave|`'nombre' in persona`|
|`'clave' not in dict`|Verificar si NO existe la clave|`'telefono' not in persona`|
|`dict.keys()`|Obtener todas las claves|`persona.keys()`|
|`dict.values()`|Obtener todos los valores|`persona.values()`|
|`dict.items()`|Obtener pares clave-valor|`persona.items()`|

### ✏️ **3. MODIFICACIÓN Y ACTUALIZACIÓN**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`dict['clave'] = valor`|Agregar o modificar elemento|`persona['telefono'] = '123-456-7890'`|
|`dict.update(otro_dict)`|Actualizar con otro diccionario|`persona.update({'ciudad': 'Madrid'})`|
|`dict.update(clave=valor)`|Actualizar con argumentos|`persona.update(edad=26, trabajo='Ingeniero')`|
|`dict.setdefault('clave', valor)`|Establecer si no existe|`persona.setdefault('pais', 'España')`|

### 🗑️ **4. ELIMINACIÓN DE ELEMENTOS**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`del dict['clave']`|Eliminar elemento (puede dar error)|`del persona['edad']`|
|`dict.pop('clave')`|Eliminar y devolver valor|`edad = persona.pop('edad')`|
|`dict.pop('clave', default)`|Eliminar con valor por defecto|`tel = persona.pop('telefono', 'Sin teléfono')`|
|`dict.popitem()`|Eliminar último elemento insertado|`clave, valor = persona.popitem()`|
|`dict.clear()`|Eliminar todos los elementos|`persona.clear()`|

### 🔄 **5. ITERACIÓN Y RECORRIDO**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`for clave in dict:`|Iterar sobre claves|`for k in persona: print(k)`|
|`for valor in dict.values():`|Iterar sobre valores|`for v in persona.values(): print(v)`|
|`for clave, valor in dict.items():`|Iterar sobre pares|`for k, v in persona.items(): print(k, v)`|
|`for i, clave in enumerate(dict):`|Iterar con índice|`for i, k in enumerate(persona): print(i, k)`|

### 📏 **6. INFORMACIÓN Y PROPIEDADES**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`len(dict)`|Número de elementos|`len(persona)`|
|`bool(dict)`|Verificar si está vacío|`bool(persona)`|
|`type(dict)`|Tipo del objeto|`type(persona)`|
|`str(dict)`|Representación como string|`str(persona)`|
|`repr(dict)`|Representación para depuración|`repr(persona)`|

### 🔗 **7. OPERACIONES AVANZADAS**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`dict.copy()`|Copia superficial|`copia = persona.copy()`|
|`dict(**otro_dict)`|Desempaquetar diccionario|`nuevo = dict(**persona, ciudad='Barcelona')`|
|`{**dict1, **dict2}`|Fusionar diccionarios (Python 3.5+)|`completo = {**persona, **contacto}`|
|`dict1 \| dict2`|Operador unión (Python 3.9+)|`completo = persona \| contacto`|
|`dict1 \|= dict2`|Actualización in-place (Python 3.9+)|`persona \|= contacto`|

### 🎯 **8. COMPRENSIONES DE DICCIONARIOS**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`{k: v for k, v in items}`|Comprensión básica|`{k: v for k, v in persona.items() if len(k) > 4}`|
|`{k: f(v) for k, v in dict.items()}`|Transformar valores|`{k: str(v).upper() for k, v in persona.items()}`|
|`{f(k): v for k, v in dict.items()}`|Transformar claves|`{k.upper(): v for k, v in persona.items()}`|
|`{k: v for k, v in dict.items() if condition}`|Filtrar elementos|`{k: v for k, v in scores.items() if v >= 8}`|

### 🔍 **9. BÚSQUEDA Y FILTRADO**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`any(condition for k, v in dict.items())`|Algún elemento cumple condición|`any(v > 18 for v in edades.values())`|
|`all(condition for k, v in dict.items())`|Todos los elementos cumplen|`all(v >= 0 for v in precios.values())`|
|`max(dict, key=dict.get)`|Clave con valor máximo|`max(scores, key=scores.get)`|
|`min(dict, key=dict.get)`|Clave con valor mínimo|`min(scores, key=scores.get)`|
|`sorted(dict.items(), key=lambda x: x[1])`|Ordenar por valores|`sorted(scores.items(), key=lambda x: x[1])`|

### 🧮 **10. OPERACIONES MATEMÁTICAS**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`sum(dict.values())`|Suma de valores|`sum(ventas.values())`|
|`max(dict.values())`|Valor máximo|`max(temperaturas.values())`|
|`min(dict.values())`|Valor mínimo|`min(temperaturas.values())`|
|`len([v for v in dict.values() if condition])`|Contar con condición|`len([v for v in scores.values() if v >= 8])`|

### 🔄 **11. TRANSFORMACIONES**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`list(dict.keys())`|Claves como lista|`list(persona.keys())`|
|`list(dict.values())`|Valores como lista|`list(persona.values())`|
|`list(dict.items())`|Pares como lista|`list(persona.items())`|
|`tuple(dict.items())`|Pares como tupla|`tuple(persona.items())`|
|`set(dict.keys())`|Claves como conjunto|`set(persona.keys())`|

### 🎨 **12. DICCIONARIOS ANIDADOS**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`dict['clave']['subclave']`|Acceso anidado|`empresa['empleados']['juan']['edad']`|
|`dict.get('clave', {}).get('subclave')`|Acceso seguro anidado|`empresa.get('datos', {}).get('ventas', 0)`|
|`dict.setdefault('clave', {})['subclave']`|Crear estructura anidada|`datos.setdefault('2024', {})['enero'] = 1000`|

### 🛠️ **13. MÉTODOS ESPECIALES**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`hash(frozenset(dict.items()))`|Hash del diccionario|`hash(frozenset(config.items()))`|
|`dict == otro_dict`|Comparar diccionarios|`persona1 == persona2`|
|`dict != otro_dict`|Verificar diferencia|`config1 != config2`|

### 💡 **14. COLLECTIONS - EXTENSIONES**

|Fórmula/Método|Descripción|Ejemplo|
|---|---|---|
|`collections.defaultdict(tipo)`|Diccionario con valor por defecto|`from collections import defaultdict; dd = defaultdict(list)`|
|`collections.Counter(iterable)`|Contador de elementos|`from collections import Counter; Counter('hello')`|
|`collections.OrderedDict()`|Diccionario ordenado|`from collections import OrderedDict; od = OrderedDict()`|

---

## 💡 **NOTAS IMPORTANTES**

- 🔸 **Claves inmutables**: Solo tipos inmutables (str, int, tuple) pueden ser claves
- 🔸 **Orden preservado**: Desde Python 3.7+, los diccionarios mantienen el orden de inserción
- 🔸 **Acceso seguro**: Usar `.get()` para evitar errores de KeyError
- 🔸 **Copias**: `.copy()` hace copia superficial, usar `copy.deepcopy()` para copia profunda
- 🔸 **Comprensiones**: Más eficientes que loops tradicionales para crear diccionarios
- 🔸 **Mutables**: Los diccionarios son mutables, modifican el objeto original

---

## 🎯 **PATRONES COMUNES**

```python
# 🔄 Intercambiar claves y valores
invertido = {v: k for k, v in diccionario.items()}

# 📊 Agrupar elementos
grupos = {}
for item in lista:
    grupos.setdefault(criterio(item), []).append(item)

# 🔍 Filtrar diccionario
filtrado = {k: v for k, v in dict.items() if condicion(k, v)}

# 🔗 Fusionar múltiples diccionarios
resultado = {}
for d in lista_diccionarios:
    resultado.update(d)
```

---

_Esta tabla cubre las operaciones fundamentales con diccionarios en Python. Los diccionarios son una de las estructuras de datos más versátiles y utilizadas en Python._