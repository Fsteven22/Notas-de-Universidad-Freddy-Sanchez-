---
dg-publish: true
---

# 🛠️ Funciones Built-in de Python

> [!info] 📋 ¿Qué son las Funciones Built-in?
> Las funciones built-in (incorporadas) son funciones predefinidas que vienen integradas en Python y están disponibles en cualquier momento sin necesidad de importar módulos adicionales. Son herramientas fundamentales que facilitan tareas comunes de programación como conversiones de tipos, manipulación de secuencias, cálculos matemáticos básicos y más.

## 🎯 Funciones Esenciales

### Funciones de Conversión de Tipos

> [!tip] 🔄 Conversiones Básicas
> 
> **`int()`** - Convierte a entero
> ```python
> int("123")     # 123
> int(45.7)      # 45
> int("FF", 16)  # 255 (hexadecimal)
> ```
> 
> **`float()`** - Convierte a decimal
> ```python
> float("3.14")  # 3.14
> float(42)      # 42.0
> ```
> 
> **`str()`** - Convierte a cadena
> ```python
> str(123)       # "123"
> str(3.14)      # "3.14"
> ```
> 
> **`bool()`** - Convierte a booleano
> ```python
> bool(1)        # True
> bool(0)        # False
> bool("")       # False
> bool("Hola")   # True
> ```

### Funciones de Secuencias y Colecciones

> [!tip] 📊 Trabajando con Datos
> 
> **`len()`** - Longitud de secuencia
> ```python
> len("Python")     # 6
> len([1, 2, 3])    # 3
> len({"a": 1})     # 1
> ```
> 
> **`list()`** - Convierte a lista
> ```python
> list("abc")       # ['a', 'b', 'c']
> list(range(3))    # [0, 1, 2]
> ```
> 
> **`tuple()`** - Convierte a tupla
> ```python
> tuple([1, 2, 3])  # (1, 2, 3)
> tuple("abc")      # ('a', 'b', 'c')
> ```
> 
> **`set()`** - Convierte a conjunto
> ```python
> set([1, 2, 2, 3]) # {1, 2, 3}
> set("hello")      # {'h', 'e', 'l', 'o'}
> ```

### Funciones Matemáticas

> [!example] 🧮 Cálculos Básicos
> 
> **`abs()`** - Valor absoluto
> ```python
> abs(-5)    # 5
> abs(3.2)   # 3.2
> ```
> 
> **`min()`** - Valor mínimo
> ```python
> min(1, 5, 3)        # 1
> min([10, 2, 8])     # 2
> min("abc")          # 'a'
> ```
> 
> **`max()`** - Valor máximo
> ```python
> max(1, 5, 3)        # 5
> max([10, 2, 8])     # 10
> max("abc")          # 'c'
> ```
> 
> **`sum()`** - Suma de elementos
> ```python
> sum([1, 2, 3, 4])   # 10
> sum(range(5))       # 10
> sum([1, 2], 10)     # 13 (con valor inicial)
> ```
> 
> **`round()`** - Redondeo
> ```python
> round(3.7)          # 4
> round(3.14159, 2)   # 3.14
> ```

## 🔄 Funciones de Iteración Avanzada

### range() - Generador de Secuencias

> [!tip] 📈 Generando Rangos
> ```python
> # Uso básico
> range(5)        # 0, 1, 2, 3, 4
> range(2, 8)     # 2, 3, 4, 5, 6, 7
> range(0, 10, 2) # 0, 2, 4, 6, 8
> 
> # Casos especiales
> range(10, 0, -1)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
> list(range(3))    # [0, 1, 2]
> ```

### enumerate() - Índice y Valor

> [!example] 🔢 Numeración Automática
> ```python
> frutas = ["manzana", "banana", "cereza"]
> 
> for indice, fruta in enumerate(frutas):
>     print(f"{indice}: {fruta}")
> # 0: manzana
> # 1: banana  
> # 2: cereza
> 
> # Con inicio personalizado
> for i, fruta in enumerate(frutas, 1):
>     print(f"{i}. {fruta}")
> # 1. manzana
> # 2. banana
> # 3. cereza
> ```

### zip() - Combinando Secuencias

> [!tip] 🤝 Emparejamiento de Datos
> ```python
> nombres = ["Ana", "Luis", "Sofia"]
> edades = [25, 30, 28]
> ciudades = ["Madrid", "Barcelona", "Valencia"]
> 
> for nombre, edad, ciudad in zip(nombres, edades, ciudades):
>     print(f"{nombre}, {edad} años, vive en {ciudad}")
> 
> # Crear diccionario
> dict(zip(nombres, edades))  # {'Ana': 25, 'Luis': 30, 'Sofia': 28}
> ```

## 🔍 Funciones de Filtrado y Verificación

### Funciones de Verificación

> [!warning] ✅ Validaciones Importantes
> 
> **`isinstance()`** - Verificar tipo
> ```python
> isinstance(42, int)        # True
> isinstance("hello", str)   # True
> isinstance([1, 2], list)   # True
> ```
> 
> **`callable()`** - Verificar si es invocable
> ```python
> callable(print)   # True
> callable(42)      # False
> ```

### Funciones any() y all()

> [!example] 🎯 Evaluación de Condiciones
> 
> **`any()`** - True si alguno es verdadero
> ```python
> any([False, True, False])   # True
> any([0, "", [], None])      # False
> any([1, 2, 3])             # True
> ```
> 
> **`all()`** - True si todos son verdaderos
> ```python
> all([True, True, True])     # True
> all([1, 2, 3])             # True
> all([1, 0, 3])             # False
> ```

## 📂 Funciones de E/S (Entrada/Salida)

> [!info] 💬 Interacción con el Usuario
> 
> **`print()`** - Mostrar en pantalla
> ```python
> print("Hola mundo")
> print("Valor:", 42, "Fin:", end=" ¡Listo!\n")
> print("A", "B", "C", sep="-")  # A-B-C
> ```
> 
> **`input()`** - Obtener entrada del usuario
> ```python
> nombre = input("¿Cómo te llamas? ")
> edad = int(input("¿Cuántos años tienes? "))
> ```

## 🗂️ Funciones de Ordenamiento

> [!tip] 📊 Organizando Datos
> 
> **`sorted()`** - Ordena y retorna nueva lista
> ```python
> sorted([3, 1, 4, 1, 5])         # [1, 1, 3, 4, 5]
> sorted("python")                # ['h', 'n', 'o', 'p', 't', 'y']
> sorted([3, 1, 4], reverse=True) # [4, 3, 1]
> ```
> 
> **`reversed()`** - Invierte secuencia
> ```python
> list(reversed([1, 2, 3]))       # [3, 2, 1]
> list(reversed("hello"))         # ['o', 'l', 'l', 'e', 'h']
> ```

## 📊 Diagrama de Categorías

```mermaid
mindmap
  root((🛠️ Built-in Functions))
    🔄 Conversión
      int()
      float()
      str()
      bool()
    📊 Secuencias
      len()
      list()
      tuple()
      set()
    🧮 Matemáticas
      abs()
      min()
      max()
      sum()
      round()
    🔄 Iteración
      range()
      enumerate()
      zip()
    ✅ Verificación
      isinstance()
      callable()
      any()
      all()
    💬 E/S
      print()
      input()
    📈 Ordenamiento
      sorted()
      reversed()
```

## 💻 Ejemplos Prácticos Integrados

### Análisis de Calificaciones

> [!example] 🎓 Sistema de Notas
> ```python
> # Datos de estudiantes
> estudiantes = ["Ana", "Luis", "Sofia", "Pedro"]
> calificaciones = [85, 92, 78, 96]
> 
> # Análisis completo
> print("📊 REPORTE DE CALIFICACIONES")
> print("=" * 30)
> 
> # Mostrar con numeración
> for i, (nombre, nota) in enumerate(zip(estudiantes, calificaciones), 1):
>     estado = "✅ Aprobado" if nota >= 80 else "❌ Reprobado"
>     print(f"{i}. {nombre}: {nota} - {estado}")
> 
> # Estadísticas
> print(f"\n📈 Estadísticas:")
> print(f"Promedio: {round(sum(calificaciones) / len(calificaciones), 1)}")
> print(f"Nota máxima: {max(calificaciones)}")
> print(f"Nota mínima: {min(calificaciones)}")
> print(f"Todos aprobaron: {all(nota >= 80 for nota in calificaciones)}")
> print(f"Alguno reprobó: {any(nota < 80 for nota in calificaciones)}")
> ```

### Procesador de Texto

> [!example] 📝 Análisis de Cadenas
> ```python
> def analizar_texto(texto):
>     # Conversiones y análisis
>     palabras = texto.split()
>     
>     print(f"📊 Análisis de: '{texto}'")
>     print(f"Longitud total: {len(texto)}")
>     print(f"Número de palabras: {len(palabras)}")
>     print(f"Palabra más larga: {max(palabras, key=len)}")
>     print(f"Palabra más corta: {min(palabras, key=len)}")
>     
>     # Caracteres únicos ordenados
>     chars_unicos = sorted(set(texto.lower().replace(' ', '')))
>     print(f"Caracteres únicos: {', '.join(chars_unicos)}")
>     
>     return len(palabras)
> 
> # Uso
> num_palabras = analizar_texto("Python es un lenguaje poderoso")
> ```

---

## 📚 Referencias

> [!quote] 🔗 Enlaces a Otras Notas
> - [[Módulo 4.2 Iteradores for]] - Usando range() y enumerate()
> - [[Módulo 2.1 Variables y Tipos de Datos]] - Conversiones de tipos
> - [[Módulo 2.3 Listas y Tuplas en Python]] - Funciones para trabajar con listas
> - [[Módulo 2.2 Operaciones con Datos y Variables]] - Operaciones matemáticas
> - [[Módulo 3.1 Funciones]] - Creando tus propias funciones
> - [[Módulo 4.1 Condicional]] - Usando any() y all() en condiciones

## 🎓 Notas Recomendadas

> [!note] 📖 Para Complementar tu Aprendizaje
> - [[Módulos math y statistics]] - Funciones matemáticas avanzadas
> - [[Comprensiones de Lista]] - Alternativas a filter() y map()
> - [[Manejo de Excepciones]] - Validación con isinstance()
> - [[Programación Funcional]] - filter(), map(), reduce()
> - [[Decoradores]] - Funciones que modifican otras funciones
> - [[Generadores e Iteradores]] - Conceptos avanzados de iteración

---

**Tags:** #python #funciones #built-in #incorporadas #conversiones #tipos #secuencias #matematicas #iteracion #validacion #programacion #fundamentos