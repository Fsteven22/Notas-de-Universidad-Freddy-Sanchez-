# 📊 Tabla de Variables y Tipos de Datos en Python

## 🎯 Referencia Rápida - Módulo 2: Variables y Tipos de Datos

### 📝 **1. VARIABLES BÁSICAS**

|Concepto|Descripción|Ejemplo|
|---|---|---|
|Asignación simple|Asignar valor a variable|`nombre = "Ana"`<br>`edad = 25`<br>`activo = True`|
|Asignación múltiple|Varias variables en una línea|`x, y, z = 1, 2, 3`<br>`nombre, apellido = "Ana", "García"`|
|Intercambio de valores|Swap sin variable temporal|`a, b = 10, 20`<br>`a, b = b, a # a=20, b=10`|
|Asignación en cadena|Mismo valor a múltiples variables|`x = y = z = 0`|
|Variables con mismo valor|Múltiples variables iguales|`precio = costo = descuento = 100`|

### 🏷️ **2. TIPOS DE DATOS NUMÉRICOS**

|Tipo|Descripción|Ejemplo|
|---|---|---|
|`int`|Números enteros|`edad = 25`<br>`negativo = -10`<br>`grande = 1000000`|
|`float`|Números decimales|`precio = 19.99`<br>`pi = 3.14159`<br>`cientifico = 1.5e10`|
|`complex`|Números complejos|`complejo = 3 + 4j`<br>`otro = complex(2, 5)`|
|Conversión numérica|Cambiar tipo de número|`int(3.14) # 3`<br>`float(5) # 5.0`<br>`str(42) # "42"`|

### 🔤 **3. TIPOS DE DATOS DE TEXTO**

|Elemento|Descripción|Ejemplo|
|---|---|---|
|`str` comillas simples|Cadenas con comillas simples|`nombre = 'Ana'`<br>`mensaje = 'Hola mundo'`|
|`str` comillas dobles|Cadenas con comillas dobles|`apellido = "García"`<br>`frase = "Él dijo 'hola'"`|
|`str` triple comillas|Cadenas multilínea|`texto = """Este es un`<br>`texto de múltiples`<br>`líneas"""`|
|Caracteres de escape|Caracteres especiales|`texto = "Línea 1\nLínea 2"`<br>`ruta = "C:\\Users\\Ana"`|
|f-strings|Cadenas formateadas|`nombre = "Ana"`<br>`saludo = f"Hola {nombre}"`|

### ✅ **4. TIPO BOOLEANO**

|Valor|Descripción|Ejemplo|
|---|---|---|
|`True`|Verdadero|`activo = True`<br>`encontrado = True`|
|`False`|Falso|`terminado = False`<br>`oculto = False`|
|Conversión booleana|Evaluar como bool|`bool(1) # True`<br>`bool(0) # False`<br>`bool("") # False`|
|Valores falsy|Se evalúan como False|`None, 0, "", [], {}, False`|
|Valores truthy|Se evalúan como True|`Cualquier valor no falsy`|

### ➕ **5. OPERACIONES ARITMÉTICAS**

|Operador|Descripción|Ejemplo|
|---|---|---|
|`+`|Suma|`5 + 3 # 8`|
|`-`|Resta|`10 - 4 # 6`|
|`*`|Multiplicación|`7 * 6 # 42`|
|`/`|División (float)|`15 / 4 # 3.75`|
|`//`|División entera|`15 // 4 # 3`|
|`%`|Módulo (resto)|`15 % 4 # 3`|
|`**`|Potencia|`2 ** 3 # 8`|
|`abs()`|Valor absoluto|`abs(-5) # 5`|

### 🔧 **6. OPERADORES DE ASIGNACIÓN**

|Operador|Descripción|Ejemplo|
|---|---|---|
|`=`|Asignación básica|`x = 10`|
|`+=`|Suma y asigna|`x += 5 # x = x + 5`|
|`-=`|Resta y asigna|`x -= 3 # x = x - 3`|
|`*=`|Multiplica y asigna|`x *= 2 # x = x * 2`|
|`/=`|Divide y asigna|`x /= 4 # x = x / 4`|
|`//=`|División entera y asigna|`x //= 3 # x = x // 3`|
|`%=`|Módulo y asigna|`x %= 2 # x = x % 2`|
|`**=`|Potencia y asigna|`x **= 3 # x = x ** 3`|

### 📋 **7. LISTAS - CREACIÓN Y ACCESO**

|Operación|Descripción|Ejemplo|
|---|---|---|
|Lista vacía|Crear lista sin elementos|`lista = []`<br>`otra = list()`|
|Lista con elementos|Crear con valores iniciales|`numeros = [1, 2, 3, 4, 5]`<br>`nombres = ["Ana", "Luis", "Carlos"]`|
|Lista mixta|Diferentes tipos de datos|`mixta = [1, "texto", True, 3.14]`|
|Acceso por índice|Obtener elemento específico|`primer_elemento = lista[0]`<br>`ultimo = lista[-1]`|
|Slicing|Obtener sublista|`sublista = lista[1:4]`<br>`copia = lista[:]`|

### 🔨 **8. LISTAS - MÉTODOS Y OPERACIONES**

|Método|Descripción|Ejemplo|
|---|---|---|
|`.append(elemento)`|Agregar al final|`lista.append(6)`|
|`.insert(indice, elemento)`|Insertar en posición|`lista.insert(0, "nuevo")`|
|`.remove(elemento)`|Eliminar primera ocurrencia|`lista.remove("Ana")`|
|`.pop(indice)`|Eliminar y retornar elemento|`elemento = lista.pop(0)`|
|`.extend(iterable)`|Agregar múltiples elementos|`lista.extend([7, 8, 9])`|
|`.index(elemento)`|Encontrar índice|`posicion = lista.index("Luis")`|
|`.count(elemento)`|Contar ocurrencias|`veces = lista.count(5)`|
|`.sort()`|Ordenar lista|`lista.sort()`<br>`lista.sort(reverse=True)`|
|`.reverse()`|Invertir orden|`lista.reverse()`|
|`.clear()`|Vaciar lista|`lista.clear()`|

### 🎯 **9. TUPLAS**

|Operación|Descripción|Ejemplo|
|---|---|---|
|Tupla vacía|Crear tupla sin elementos|`tupla = ()`<br>`otra = tuple()`|
|Tupla con elementos|Crear con valores|`coordenadas = (10, 20)`<br>`colores = ("rojo", "azul", "verde")`|
|Tupla de un elemento|Necesita coma|`tupla_uno = (42,)`<br>`sin_parentesis = 42,`|
|Acceso por índice|Obtener elemento|`x = coordenadas[0]`<br>`y = coordenadas[1]`|
|Desempaquetado|Asignar a variables|`x, y = coordenadas`<br>`r, g, b = colores`|
|Inmutabilidad|No se puede modificar|`# tupla[0] = 5 # ERROR`|
|`.count()` y `.index()`|Métodos disponibles|`tupla.count(10)`<br>`tupla.index("rojo")`|

### 🔄 **10. CONVERSIÓN ENTRE TIPOS**

|Conversión|Descripción|Ejemplo|
|---|---|---|
|Lista a tupla|`tuple(lista)`|`tupla = tuple([1, 2, 3])`|
|Tupla a lista|`list(tupla)`|`lista = list((1, 2, 3))`|
|String a lista|`list(string)` o `.split()`|`list("abc") # ['a','b','c']`<br>`"a,b,c".split(',') # ['a','b','c']`|
|Lista a string|`.join()`|`",".join(['a','b','c']) # 'a,b,c'`|
|Números a string|`str(numero)`|`str(42) # "42"`|
|String a número|`int()` o `float()`|`int("42") # 42`<br>`float("3.14") # 3.14`|

### 🎲 **11. ALEATORIEDAD - MÓDULO RANDOM**

|Función|Descripción|Ejemplo|
|---|---|---|
|`import random`|Importar módulo|`import random`|
|`random.random()`|Float entre 0 y 1|`aleatorio = random.random()`|
|`random.randint(a, b)`|Entero entre a y b (inclusivo)|`dado = random.randint(1, 6)`|
|`random.uniform(a, b)`|Float entre a y b|`precio = random.uniform(10.0, 50.0)`|
|`random.choice(secuencia)`|Elemento aleatorio de lista|`color = random.choice(["rojo", "azul", "verde"])`|
|`random.choices(lista, k=n)`|Múltiples elementos con reposición|`muestra = random.choices([1,2,3,4], k=3)`|
|`random.sample(lista, k)`|Múltiples elementos sin reposición|`muestra = random.sample([1,2,3,4,5], k=3)`|
|`random.shuffle(lista)`|Mezclar lista in-place|`random.shuffle(mi_lista)`|

### 🎯 **12. ALEATORIEDAD - APLICACIONES PRÁCTICAS**

|Aplicación|Descripción|Ejemplo|
|---|---|---|
|Simulación de dado|Número aleatorio 1-6|`dado = random.randint(1, 6)`|
|Moneda|Cara o cruz|`resultado = random.choice(["Cara", "Cruz"])`|
|Password aleatorio|Generar contraseña|`import string`<br>`chars = string.ascii_letters + string.digits`<br>`password = ''.join(random.choices(chars, k=8))`|
|Selección aleatoria|Elegir ganador|`ganador = random.choice(participantes)`|
|Muestra estadística|Subset de datos|`muestra = random.sample(poblacion, 100)`|
|Seed para reproducibilidad|Resultados consistentes|`random.seed(42)`<br>`# Ahora todos los random serán iguales`|

### 🔍 **13. OPERACIONES ÚTILES CON LISTAS**

|Operación|Descripción|Ejemplo|
|---|---|---|
|`len(lista)`|Longitud de lista|`tamaño = len([1, 2, 3, 4]) # 4`|
|`max(lista)` / `min(lista)`|Máximo y mínimo|`mayor = max([5, 2, 9, 1]) # 9`|
|`sum(lista)`|Suma de elementos|`total = sum([1, 2, 3, 4]) # 10`|
|`in` / `not in`|Verificar pertenencia|`5 in [1, 2, 3, 4, 5] # True`|
|`+` concatenar|Unir listas|`nueva = [1, 2] + [3, 4] # [1,2,3,4]`|
|`*` repetir|Repetir lista|`repetida = [0] * 5 # [0,0,0,0,0]`|
|List comprehension|Crear lista con condición|`pares = [x for x in range(10) if x % 2 == 0]`|
|`enumerate()`|Índice y valor|`for i, valor in enumerate(lista):`|

### 🎨 **14. OPERACIONES CON STRINGS**

|Operación|Descripción|Ejemplo|
|---|---|---|
|Concatenación|Unir strings|`completo = "Hola" + " " + "mundo"`|
|Repetición|Repetir string|`guiones = "-" * 20`|
|`.upper()` / `.lower()`|Mayúsculas/minúsculas|`"Hola".upper() # "HOLA"`|
|`.capitalize()`|Primera letra mayúscula|`"hola".capitalize() # "Hola"`|
|`.title()`|Título (cada palabra)|`"hola mundo".title() # "Hola Mundo"`|
|`.strip()`|Quitar espacios|`" hola ".strip() # "hola"`|
|`.replace(viejo, nuevo)`|Reemplazar texto|`"Hola".replace("o", "a") # "Hala"`|
|`.split(separador)`|Dividir en lista|`"a,b,c".split(",") # ["a","b","c"]`|
|`.join(lista)`|Unir lista con separador|`"-".join(["a","b","c"]) # "a-b-c"`|

### 🎊 **15. PATRONES COMUNES**

|Patrón|Descripción|Ejemplo|
|---|---|---|
|Inicializar lista con ceros|Lista de tamaño fijo|`lista = [0] * 10`|
|Lista de listas|Matriz simple|`matriz = [[0] * 3 for _ in range(3)]`|
|Filtrar lista|Elementos que cumplen condición|`positivos = [x for x in numeros if x > 0]`|
|Transformar lista|Aplicar operación|`cuadrados = [x**2 for x in numeros]`|
|Encontrar elemento|Búsqueda con condición|`encontrado = next((x for x in lista if x > 10), None)`|
|Contar elementos|Elementos que cumplen condición|`contador = sum(1 for x in lista if x > 0)`|
|Lista única|Eliminar duplicados|`unicos = list(set(lista))`|
|Aplanar lista|Lista de listas a lista simple|`plana = [item for sublista in lista for item in sublista]`|

### 💾 **16. INPUT/OUTPUT CON VARIABLES**

|Función|Descripción|Ejemplo|
|---|---|---|
|`input(mensaje)`|Recibir texto del usuario|`nombre = input("Tu nombre: ")`|
|`int(input())`|Recibir número entero|`edad = int(input("Tu edad: "))`|
|`float(input())`|Recibir número decimal|`altura = float(input("Tu altura: "))`|
|`print(variable)`|Mostrar variable|`print(f"Hola {nombre}, tienes {edad} años")`|
|`print()` múltiples valores|Mostrar varias variables|`print("Nombre:", nombre, "Edad:", edad)`|
|`print()` con separador|Personalizar separador|`print("a", "b", "c", sep="-") # a-b-c`|

---

## 💡 **NOTAS IMPORTANTES**

- 🔸 **Nomenclatura**: Usar snake_case para nombres de variables: `mi_variable`, `edad_usuario`
- 🔸 **Nombres descriptivos**: `edad` mejor que `e`, `precio_total` mejor que `pt`
- 🔸 **Mutabilidad**: Las listas son mutables (se pueden modificar), las tuplas son inmutables
- 🔸 **Índices**: Python usa índices base 0 (el primer elemento es [0])
- 🔸 **Índices negativos**: [-1] es el último elemento, [-2] el penúltimo
- 🔸 **Slicing**: [inicio:fin] - inicio inclusivo, fin exclusivo
- 🔸 **Aleatoriedad**: Usar `random.seed()` para reproducir resultados en testing
- 🔸 **Performance**: Tuplas son más rápidas que listas para datos inmutables

---

_Esta tabla cubre variables y tipos de datos principales del Módulo 2. Para casos más avanzados, consultar la documentación oficial de Python._