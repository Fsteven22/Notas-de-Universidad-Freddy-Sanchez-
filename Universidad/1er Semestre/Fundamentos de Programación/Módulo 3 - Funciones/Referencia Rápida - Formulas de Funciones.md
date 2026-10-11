---
dg-publish: true
---

# 🔧 Tabla de Funciones en Python

## 🎯 Referencia Rápida - Módulo 3: Funciones

### 🏗️ **1. DEFINICIÓN BÁSICA DE FUNCIONES**

|Estructura|Descripción|Ejemplo|
|---|---|---|
|`def nombre_funcion():`|Función sin parámetros|`def saludar():`<br>    `print("¡Hola!")`|
|`def nombre_funcion(parametro):`|Función con un parámetro|`def saludar(nombre):`<br>    `print(f"¡Hola {nombre}!")`|
|`def nombre_funcion(param1, param2):`|Función con múltiples parámetros|`def sumar(a, b):`<br>    `return a + b`|
|`return valor`|Devolver un valor|`def cuadrado(x):`<br>    `return x ** 2`|
|`return`|Salir de la función sin valor|`def procesar():`<br>    `if error:`<br>        `return`<br>    `print("Procesando...")`|

### 📞 **2. LLAMADA A FUNCIONES**

|Forma de llamada|Descripción|Ejemplo|
|---|---|---|
|`funcion()`|Llamada sin argumentos|`saludar()`|
|`funcion(argumento)`|Llamada con argumento|`saludar("Ana")`|
|`variable = funcion()`|Asignar resultado|`resultado = sumar(5, 3)`|
|`funcion(arg1, arg2)`|Múltiples argumentos|`resultado = dividir(10, 2)`|
|`funcion(param=valor)`|Argumento nombrado|`saludar(nombre="Carlos")`|

### 🎛️ **3. PARÁMETROS AVANZADOS**

|Tipo de parámetro|Descripción|Ejemplo|
|---|---|---|
|Parámetros por defecto|Valor predeterminado|`def saludar(nombre, saludo="Hola"):`<br>    `print(f"{saludo}, {nombre}")`|
|`*args`|Argumentos posicionales variables|`def sumar_todos(*numeros):`<br>    `return sum(numeros)`|
|`**kwargs`|Argumentos nombrados variables|`def info_persona(**datos):`<br>    `for clave, valor in datos.items():`<br>        `print(f"{clave}: {valor}")`|
|Parámetros mixtos|Combinación de tipos|`def funcion(pos, *args, **kwargs):`<br>    `print(pos, args, kwargs)`|
|Parámetros solo nombrados|Después de `*`|`def funcion(a, *, b, c):`<br>    `return a + b + c`|

### 📤 **4. VALORES DE RETORNO**

|Tipo de retorno|Descripción|Ejemplo|
|---|---|---|
|Retorno simple|Un solo valor|`def cuadrado(x):`<br>    `return x ** 2`|
|Múltiples valores|Tupla de valores|`def operaciones(a, b):`<br>    `return a+b, a-b, a*b`|
|Sin retorno explícito|Retorna `None`|`def imprimir_info(dato):`<br>    `print(f"Info: {dato}")`|
|Retorno condicional|Diferentes valores según condición|`def absoluto(x):`<br>    `if x >= 0:`<br>        `return x`<br>    `else:`<br>        `return -x`|
|Retorno temprano|Salir antes con return|`def validar(edad):`<br>    `if edad < 0:`<br>        `return "Edad inválida"`<br>    `return "Edad válida"`|

### 🌐 **5. ÁMBITO Y VARIABLES (SCOPE)**

|Concepto|Descripción|Ejemplo|
|---|---|---|
|Variable local|Solo existe dentro de la función|`def funcion():`<br>    `x = 10 # Variable local`<br>    `print(x)`|
|Variable global|Accesible desde cualquier lugar|`x = 10 # Global`<br>`def funcion():`<br>    `print(x) # Accede a global`|
|`global` keyword|Modificar variable global|`x = 10`<br>`def cambiar():`<br>    `global x`<br>    `x = 20`|
|`nonlocal` keyword|Variable en función anidada|`def externa():`<br>    `x = 10`<br>    `def interna():`<br>        `nonlocal x`<br>        `x = 20`|

### 🏢 **6. FUNCIONES ANIDADAS Y CLOSURES**

|Concepto|Descripción|Ejemplo|
|---|---|---|
|Función anidada|Función dentro de función|`def externa(x):`<br>    `def interna(y):`<br>        `return x + y`<br>    `return interna`|
|Closure|Función que "recuerda" variables|`def multiplicador(n):`<br>    `def multiplicar(x):`<br>        `return x * n`<br>    `return multiplicar`|
|Decorador básico|Función que modifica otra función|`def mi_decorador(func):`<br>    `def wrapper():`<br>        `print("Antes")`<br>        `func()`<br>        `print("Después")`<br>    `return wrapper`|

### ⚡ **7. FUNCIONES LAMBDA**

|Uso|Descripción|Ejemplo|
|---|---|---|
|Lambda básica|Función anónima simple|`cuadrado = lambda x: x**2`|
|Lambda con múltiples parámetros|Varios argumentos|`sumar = lambda a, b: a + b`|
|Lambda en `map()`|Aplicar función a lista|`numeros = [1, 2, 3, 4]`<br>`cuadrados = list(map(lambda x: x**2, numeros))`|
|Lambda en `filter()`|Filtrar elementos|`numeros = [1, 2, 3, 4, 5, 6]`<br>`pares = list(filter(lambda x: x%2==0, numeros))`|
|Lambda en `sorted()`|Criterio de ordenamiento|`estudiantes = [("Ana", 85), ("Luis", 90)]`<br>`sorted(estudiantes, key=lambda x: x[1])`|

### 🔧 **8. FUNCIONES INCORPORADAS ÚTILES**

|Función|Descripción|Ejemplo|
|---|---|---|
|`len()`|Longitud de secuencia|`len([1, 2, 3, 4]) # 4`|
|`max()` / `min()`|Valor máximo/mínimo|`max([1, 5, 3]) # 5`|
|`sum()`|Suma de elementos|`sum([1, 2, 3, 4]) # 10`|
|`abs()`|Valor absoluto|`abs(-5) # 5`|
|`round()`|Redondear número|`round(3.14159, 2) # 3.14`|
|`type()`|Tipo de dato|`type(42) # <class 'int'>`|
|`isinstance()`|Verificar tipo|`isinstance(42, int) # True`|
|`range()`|Secuencia de números|`list(range(5)) # [0,1,2,3,4]`|

### 🗂️ **9. FUNCIONES DE ORDEN SUPERIOR**

|Función|Descripción|Ejemplo|
|---|---|---|
|`map(funcion, iterable)`|Aplicar función a cada elemento|`list(map(str.upper, ["a", "b", "c"]))`<br>`# ['A', 'B', 'C']`|
|`filter(funcion, iterable)`|Filtrar elementos|`list(filter(lambda x: x > 0, [-1, 0, 1, 2]))`<br>`# [1, 2]`|
|`reduce(funcion, iterable)`|Reducir a un valor (importar)|`from functools import reduce`<br>`reduce(lambda x,y: x+y, [1,2,3,4]) # 10`|
|`sorted(iterable, key=funcion)`|Ordenar con criterio|`sorted(["banana", "pie", "manzana"], key=len)`|
|`any(iterable)`|True si alguno es verdadero|`any([False, True, False]) # True`|
|`all(iterable)`|True si todos son verdaderos|`all([True, True, False]) # False`|

### 📋 **10. DOCUMENTACIÓN Y DOCSTRINGS**

|Elemento|Descripción|Ejemplo|
|---|---|---|
|Docstring simple|Descripción básica|`def saludar(nombre):`<br>    `"""Saluda a una persona"""`<br>    `print(f"Hola {nombre}")`|
|Docstring detallado|Con parámetros y retorno|`def dividir(a, b):`<br>    `"""`<br>    `Divide dos números.`<br>    `Args:`<br>        `a: Dividendo`<br>        `b: Divisor`<br>    `Returns:`<br>        `float: Resultado de a/b`<br>    `"""`<br>    `return a / b`|
|`help(funcion)`|Mostrar documentación|`help(print)`|
|`funcion.__doc__`|Acceder al docstring|`print(dividir.__doc__)`|

### 🎯 **11. PATRONES COMUNES**

|Patrón|Descripción|Ejemplo|
|---|---|---|
|Función validadora|Verificar condiciones|`def es_email_valido(email):`<br>    `return "@" in email and "." in email`|
|Función calculadora|Operaciones matemáticas|`def calcular(operacion, a, b):`<br>    `if operacion == "+":`<br>        `return a + b`<br>    `elif operacion == "-":`<br>        `return a - b`|
|Función factory|Crear otras funciones|`def crear_multiplicador(n):`<br>    `return lambda x: x * n`|
|Función recursiva|Se llama a sí misma|`def factorial(n):`<br>    `if n <= 1:`<br>        `return 1`<br>    `return n * factorial(n-1)`|
|Memoización|Cache de resultados|`def fibonacci(n, memo={}):`<br>    `if n in memo:`<br>        `return memo[n]`<br>    `memo[n] = fibonacci(n-1) + fibonacci(n-2)`<br>    `return memo[n]`|

### 🛡️ **12. MANEJO DE ERRORES EN FUNCIONES**

|Concepto|Descripción|Ejemplo|
|---|---|---|
|`try-except` en función|Capturar errores|`def dividir_seguro(a, b):`<br>    `try:`<br>        `return a / b`<br>    `except ZeroDivisionError:`<br>        `return "No se puede dividir por cero"`|
|Validación de parámetros|Verificar tipos/valores|`def potencia(base, exponente):`<br>    `if not isinstance(base, (int, float)):`<br>        `raise TypeError("Base debe ser numérica")`<br>    `return base ** exponente`|
|Función con assert|Verificaciones rápidas|`def raiz_cuadrada(x):`<br>    `assert x >= 0, "No se puede sacar raíz de negativo"`<br>    `return x ** 0.5`|

### ⚙️ **13. DECORADORES**

|Tipo|Descripción|Ejemplo|
|---|---|---|
|Decorador simple|Modificar comportamiento|`@mi_decorador`<br>`def mi_funcion():`<br>    `print("Función original")`|
|Decorador con parámetros|Configurar decorador|`def repetir(veces):`<br>    `def decorador(func):`<br>        `def wrapper():`<br>            `for _ in range(veces):`<br>                `func()`<br>        `return wrapper`<br>    `return decorador`|
|`@property`|Convertir método en atributo|`class Persona:`<br>    `@property`<br>    `def nombre_completo(self):`<br>        `return f"{self.nombre} {self.apellido}"`|

---

## 💡 **NOTAS IMPORTANTES**

- 🔸 **Nombres**: Usar nombres descriptivos para funciones (verbos): `calcular_promedio()`, `validar_email()`
- 🔸 **Una responsabilidad**: Cada función debe hacer una sola cosa bien
- 🔸 **DRY**: Don't Repeat Yourself - si escribes el mismo código 3 veces, crea una función
- 🔸 **Parámetros**: Orden recomendado: posicionales, *args, nombrados, **kwargs
- 🔸 **Retorno**: Siempre documenta qué devuelve tu función
- 🔸 **Recursión**: Siempre define un caso base para evitar recursión infinita
- 🔸 **Testing**: Prueba tus funciones con diferentes inputs, incluyendo casos límite

---

_Esta tabla cubre las funciones principales del Módulo 3. Para casos más avanzados, consultar la documentación oficial de Python._