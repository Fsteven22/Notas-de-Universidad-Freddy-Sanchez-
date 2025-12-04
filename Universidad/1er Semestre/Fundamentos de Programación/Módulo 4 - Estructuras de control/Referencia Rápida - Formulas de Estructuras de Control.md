# 🔄 Tabla de Estructuras de Control en Python

## 🎯 Referencia Rápida - Módulo 4: Estructuras de Control

### 🔀 **1. CONDICIONALES BÁSICAS**

|Estructura|Descripción|Ejemplo|
|---|---|---|
|`if condición:`|Condicional simple|`if edad >= 18:`<br>    `print("Eres mayor de edad")`|
|`if-else`|Condicional con alternativa|`if edad >= 18:`<br>    `print("Mayor")`<br>`else:`<br>    `print("Menor")`|
|`if-elif-else`|Múltiples condiciones|`if nota >= 90:`<br>    `print("Excelente")`<br>`elif nota >= 70:`<br>    `print("Bueno")`<br>`else:`<br>    `print("Mejorar")`|
|`if anidado`|Condicionales dentro de condicionales|`if edad >= 18:`<br>    `if licencia:`<br>        `print("Puede conducir")`|

### ⚖️ **2. OPERADORES DE COMPARACIÓN**

| Operador | Descripción         | Ejemplo                      |
| -------- | ------------------- | ---------------------------- |
| `"=="`   | Igual a             | `if x == 5:`                 |
| `!=`     | Diferente de        | `if x != 0:`                 |
| `>`      | Mayor que           | `if edad > 18:`              |
| `<`      | Menor que           | `if temperatura < 0:`        |
| `>=`     | Mayor o igual       | `if puntos >= 100:`          |
| `<=`     | Menor o igual       | `if descuento <= 50:`        |
| `in`     | Pertenece a         | `if nombre in lista:`        |
| `not in` | No pertenece a      | `if item not in inventario:` |
| `is`     | Identidad de objeto | `if valor is None:`          |
| `is not` | No identidad        | `if lista is not None:`      |

### 🔗 **3. OPERADORES LÓGICOS**

|Operador|Descripción|Ejemplo|
|---|---|---|
|`and`|Y lógico (ambas condiciones)|`if edad >= 18 and licencia:`|
|`or`|O lógico (una o ambas condiciones)|`if es_fin_de_semana or es_feriado:`|
|`not`|Negación lógica|`if not es_estudiante:`|
|`and-or combinados`|Múltiples operadores|`if (edad >= 18 and licencia) or es_instructor:`|

### 🔄 **4. BUCLE FOR - ITERACIONES BÁSICAS**

|Estructura|Descripción|Ejemplo|
|---|---|---|
|`for elemento in secuencia:`|Iterar sobre secuencia|`for numero in [1, 2, 3, 4, 5]:`<br>    `print(numero)`|
|`range(n)`|Secuencia de 0 a n-1|`for i in range(5):`<br>    `print(i) # 0,1,2,3,4`|
|`range(inicio, fin)`|Secuencia con inicio y fin|`for i in range(2, 8):`<br>    `print(i) # 2,3,4,5,6,7`|
|`range(inicio, fin, paso)`|Secuencia con paso|`for i in range(0, 10, 2):`<br>    `print(i) # 0,2,4,6,8`|
|`enumerate()`|Iterar con índice|`for i, valor in enumerate(lista):`<br>    `print(f"{i}: {valor}")`|

### 📝 **5. BUCLE FOR - ITERACIONES AVANZADAS**

|Estructura|Descripción|Ejemplo|
|---|---|---|
|`for con strings`|Iterar sobre caracteres|`for letra in "Python":`<br>    `print(letra)`|
|`for con diccionarios`|Iterar sobre claves|`for clave in diccionario:`<br>    `print(clave)`|
|`dict.items()`|Iterar clave-valor|`for clave, valor in dict.items():`<br>    `print(f"{clave}: {valor}")`|
|`dict.keys()`|Iterar solo claves|`for clave in dict.keys():`|
|`dict.values()`|Iterar solo valores|`for valor in dict.values():`|
|`zip()`|Iterar múltiples secuencias|`for a, b in zip(lista1, lista2):`<br>    `print(a, b)`|
|`for anidado`|Bucles dentro de bucles|`for i in range(3):`<br>    `for j in range(3):`<br>        `print(i, j)`|

### ⏰ **6. BUCLE WHILE**

|Estructura|Descripción|Ejemplo|
|---|---|---|
|`while condición:`|Bucle mientras condición sea verdadera|`contador = 0`<br>`while contador < 5:`<br>    `print(contador)`<br>    `contador += 1`|
|`while con else`|Ejecuta else si no hay break|`while contador < 3:`<br>    `contador += 1`<br>`else:`<br>    `print("Terminó normalmente")`|
|`while True`|Bucle infinito controlado|`while True:`<br>    `entrada = input("Comando: ")`<br>    `if entrada == "salir":`<br>        `break`|

### 🚫 **7. CONTROL DE FLUJO**

|Palabra clave|Descripción|Ejemplo|
|---|---|---|
|`break`|Termina el bucle inmediatamente|`for i in range(10):`<br>    `if i == 5:`<br>        `break`<br>    `print(i)`|
|`continue`|Salta a la siguiente iteración|`for i in range(5):`<br>    `if i == 2:`<br>        `continue`<br>    `print(i) # No imprime 2`|
|`pass`|Placeholder sin acción|`for i in range(3):`<br>    `if i == 1:`<br>        `pass # No hacer nada`<br>    `else:`<br>        `print(i)`|
|`else en bucles`|Se ejecuta si no hay break|`for i in range(3):`<br>    `print(i)`<br>`else:`<br>    `print("Bucle completado")`|

### 🎨 **8. COMPRENSIONES (LIST/DICT COMPREHENSIONS)**

|Estructura|Descripción|Ejemplo|
|---|---|---|
|`[expr for item in lista]`|List comprehension básica|`cuadrados = [x**2 for x in range(5)]`|
|`[expr for item in lista if cond]`|Con condición|`pares = [x for x in range(10) if x % 2 == 0]`|
|`{k:v for item in lista}`|Dict comprehension|`cuadrados_dict = {x: x**2 for x in range(5)}`|
|`{expr for item in lista}`|Set comprehension|`únicos = {x for x in [1,2,2,3,3,4]}`|
|Comprehension anidada|Múltiples bucles|`matriz = [[i*j for j in range(3)] for i in range(3)]`|

### ⚡ **9. PATRONES COMUNES**

|Patrón|Descripción|Ejemplo|
|---|---|---|
|Contador en bucle|Contar elementos que cumplen condición|`contador = 0`<br>`for numero in lista:`<br>    `if numero > 10:`<br>        `contador += 1`|
|Acumulador|Sumar/acumular valores|`suma = 0`<br>`for numero in lista:`<br>    `suma += numero`|
|Búsqueda|Encontrar elemento|`encontrado = False`<br>`for item in lista:`<br>    `if item == buscado:`<br>        `encontrado = True`<br>        `break`|
|Validación entrada|Validar input del usuario|`while True:`<br>    `edad = input("Edad: ")`<br>    `if edad.isdigit():`<br>        `break`<br>    `print("Ingrese un número")`|

### 🔍 **10. CONDICIONALES ESPECIALES**

|Estructura|Descripción|Ejemplo|
|---|---|---|
|Operador ternario|Condicional en una línea|`resultado = "par" if numero % 2 == 0 else "impar"`|
|`if` con `any()`|Si alguno es verdadero|`if any(x > 10 for x in lista):`|
|`if` con `all()`|Si todos son verdaderos|`if all(x > 0 for x in lista):`|
|Múltiples comparaciones|Comparaciones encadenadas|`if 18 <= edad <= 65:`|
|`match-case` (Python 3.10+)|Switch-case moderno|`match valor:`<br>    `case 1:`<br>        `print("Uno")`<br>    `case 2:`<br>        `print("Dos")`<br>    `case _:`<br>        `print("Otro")`|

### 🛠️ **11. MEJORES PRÁCTICAS**

|Práctica|Descripción|Ejemplo Correcto|
|---|---|---|
|Usar `range()` eficientemente|Evitar crear listas innecesarias|✅ `for i in range(1000000):`<br>❌ `for i in list(range(1000000)):`|
|Evitar modificar lista en bucle|Usar copia o comprensión|✅ `for item in lista.copy():`<br>❌ `for item in lista:` (modificando lista)|
|Usar `enumerate()`|En lugar de range(len())|✅ `for i, valor in enumerate(lista):`<br>❌ `for i in range(len(lista)):`|
|`while` con contador seguro|Evitar bucles infinitos|✅ Siempre incrementar contador<br>❌ Olvidar actualizar condición|
|Indentación consistente|Usar 4 espacios|✅ 4 espacios por nivel<br>❌ Mezclar tabs y espacios|

---

## 💡 **NOTAS IMPORTANTES**

- 🔸 **Indentación**: Python usa indentación para definir bloques de código (4 espacios recomendados)
- 🔸 **Dos puntos**: Siempre usar `:` al final de `if`, `for`, `while`, `else`, `elif`
- 🔸 **Bucles infinitos**: Cuidado con `while True`, siempre incluir condición de salida
- 🔸 **Performance**: List comprehensions son más rápidas que bucles tradicionales para crear listas
- 🔸 **Legibilidad**: Usar paréntesis en condiciones complejas: `if (condicion1 and condicion2) or condicion3:`
- 🔸 **Debugging**: Usar `print()` dentro de bucles para verificar el flujo

---

_Esta tabla cubre las estructuras de control principales del Módulo 4. Para casos más avanzados, consultar la documentación oficial de Python._