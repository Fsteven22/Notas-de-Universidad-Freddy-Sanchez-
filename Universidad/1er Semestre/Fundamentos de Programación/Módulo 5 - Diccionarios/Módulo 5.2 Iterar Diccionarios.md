---
dg-publish: true
---

# 🔄 Módulo 5.2: Iteración de Diccionarios en Python

## 🎯 Introducción a la Iteración

> [!info] 🌟 **¿Qué es la Iteración de Diccionarios?** La iteración es el proceso de recorrer sistemáticamente todos los elementos de un diccionario. A diferencia de las listas que tienen un índice numérico, los diccionarios requieren técnicas específicas para acceder a claves, valores o ambos durante la iteración.
>
> [!tip] 🔑 **Conceptos Clave**
> 
> - **Objetos Vista**: `.keys()`, `.values()`, `.items()` devuelven vistas dinámicas
> - **Iteración Eficiente**: Los métodos de vista no crean copias innecesarias
> - **Orden Garantizado**: Desde Python 3.7+ mantiene orden de inserción
> - **Flexibilidad**: Diferentes formas según lo que necesites acceder

## 📊 Métodos de Vista Dinámicas

> [!info] 🔍 **¿Qué son los Objetos Vista?** Los métodos `.keys()`, `.values()` e `.items()` devuelven objetos vista que se actualizan automáticamente si el diccionario cambia. No son listas, sino ventanas dinámicas al diccionario original.
>
> [!example] **Demostración de Vista Dinámica**
> 
> ```python
> inventario = {'manzanas': 50, 'naranjas': 35}
> vista_claves = inventario.keys()
> 
> print(list(vista_claves))  # ['manzanas', 'naranjas']
> 
> # Modificamos el diccionario
> inventario['bananas'] = 40
> 
> print(list(vista_claves))  # ['manzanas', 'naranjas', 'bananas']
> # ¡La vista se actualizó automáticamente!
> ```

## 🔑 Iteración por Claves

> [!tip] 📝 **Formas de Iterar sobre Claves**
> 
> **Forma implícita (por defecto):**
> 
> ```python
> inventario = {'manzanas': 50, 'naranjas': 35, 'bananas': 40}
> 
> # Por defecto, itera sobre las claves
> for fruta in inventario:
>    print(f"Producto: {fruta}")
>    print(f"Cantidad: {inventario[fruta]}")
> ```
> 
> **Forma explícita con `.keys()`:**
> 
> ```python
> for fruta in inventario.keys():
>    print(f"Clave: {fruta}")
>    cantidad = inventario[fruta]
>    print(f"Valor: {cantidad}")
> ```
>
> [!warning] ⚠️ **Cuándo Usar Cada Forma**
> 
> - **Implícita**: Cuando solo necesitas las claves o es obvio que iteras claves
> - **Explícita**: Cuando quieres ser claro en tu intención o trabajas en equipo

## 📦 Iteración por Valores

> [!info] 📊 **Acceso Solo a Valores** Útil cuando solo necesitas procesar los valores sin importar las claves asociadas.
> 
> ```python
> calificaciones = {'Ana': 8.5, 'Juan': 7.2, 'María': 9.1}
> 
> # Calcular promedio general
> total = 0
> contador = 0
> 
> for nota in calificaciones.values():
>    total += nota
>    contador += 1
>    
> promedio = total / contador
> print(f"Promedio general: {promedio:.2f}")
> ```
>
> [!example] 🔢 **Operaciones Estadísticas**
> 
> ```python
> ventas_mensuales = {
>    'Enero': 15000, 'Febrero': 18000, 'Marzo': 22000,
>    'Abril': 19000, 'Mayo': 25000, 'Junio': 21000
> }
> 
> # Encontrar máxima y mínima venta
> ventas = list(ventas_mensuales.values())
> venta_maxima = max(ventas)
> venta_minima = min(ventas)
> 
> print(f"Venta máxima: ${venta_maxima:,}")
> print(f"Venta mínima: ${venta_minima:,}")
> print(f"Diferencia: ${venta_maxima - venta_minima:,}")
> ```

## 🧩 Iteración por Pares Clave-Valor

> [!tip] ⭐ **Método Más Eficiente y Completo** `.items()` es generalmente la forma más útil de iterar, ya que te da acceso tanto a la clave como al valor en una sola operación.
> 
> ```python
> inventario = {'manzanas': 50, 'naranjas': 35, 'bananas': 40}
> 
> for fruta, cantidad in inventario.items():
>    print(f"Hay {cantidad} unidades de {fruta}")
>    
>    # Lógica basada en ambos valores
>    if cantidad < 40:
>        print(f"  ⚠️ Stock bajo de {fruta}")
>    else:
>        print(f"  ✅ Stock suficiente de {fruta}")
> ```
>
> [!example] 📊 **Análisis de Datos Complejo**
> 
> ```python
> empleados = {
>    'Ana': {'sueldo': 45000, 'departamento': 'IT'},
>    'Juan': {'sueldo': 38000, 'departamento': 'Ventas'},
>    'María': {'sueldo': 52000, 'departamento': 'IT'},
>    'Carlos': {'sueldo': 41000, 'departamento': 'Marketing'}
> }
> 
> # Análisis por departamento
> sueldos_por_depto = {}
> 
> for nombre, info in empleados.items():
>    depto = info['departamento']
>    sueldo = info['sueldo']
>    
>    if depto not in sueldos_por_depto:
>        sueldos_por_depto[depto] = []
>    
>    sueldos_por_depto[depto].append(sueldo)
>    
> # Calcular promedio por departamento
> for depto, sueldos in sueldos_por_depto.items():
>    promedio = sum(sueldos) / len(sueldos)
>    print(f"{depto}: Promedio ${promedio:,.2f}")
> ```

## 🎯 Técnicas Avanzadas de Iteración

> [!tip] 🔍 **Iteración Condicional**
> 
> ```python
> productos = {
>    'laptop': 1200, 'mouse': 25, 'teclado': 80,
>    'monitor': 300, 'webcam': 60, 'auriculares': 45
> }
> 
> # Filtrar productos caros (>100)
> productos_caros = []
> for producto, precio in productos.items():
>    if precio > 100:
>        productos_caros.append((producto, precio))
> 
> print("Productos caros:")
> for producto, precio in productos_caros:
>    print(f"  {producto}: ${precio}")
> ```
>
> [!info] 🔄 **Modificación Durante Iteración (CUIDADO)**
> 
> ```python
> inventario = {'manzanas': 5, 'naranjas': 35, 'bananas': 2}
> 
> # ❌ INCORRECTO: Modificar durante iteración directa
> # for fruta, cantidad in inventario.items():
> #     if cantidad < 10:
> #         del inventario[fruta]  # Error!
> 
> # ✅ CORRECTO: Crear lista de claves a eliminar
> claves_a_eliminar = []
> for fruta, cantidad in inventario.items():
>    if cantidad < 10:
>        claves_a_eliminar.append(fruta)
> 
> # Eliminar después de la iteración
> for fruta in claves_a_eliminar:
>    del inventario[fruta]
> 
> print(inventario)  # {'naranjas': 35}
> ```

## 📈 Casos de Uso Prácticos

> [!example] 📊 **Contador de Frecuencias**
> 
> ```python
> def analizar_frecuencia(texto):
>    """Cuenta frecuencia de palabras en un texto"""
>    texto_limpio = texto.lower().replace(",", "").replace(".", "")
>    palabras = texto_limpio.split()
>    
>    frecuencia = {}
>    for palabra in palabras:
>        if palabra in frecuencia:
>            frecuencia[palabra] += 1
>        else:
>            frecuencia[palabra] = 1
>    
>    return frecuencia
> 
> # Uso
> texto = "Python es genial. Python es poderoso. Es fácil aprender Python."
> resultado = analizar_frecuencia(texto)
> 
> # Mostrar resultados ordenados por frecuencia
> print("Frecuencia de palabras:")
> for palabra, freq in sorted(resultado.items(), key=lambda x: x[1], reverse=True):
>    print(f"  '{palabra}': {freq} veces")
> ```
>
> [!example] 🔄 **Invertir Diccionario**
> 
> ```python
> def invertir_diccionario(dict_original):
>    """Intercambia claves y valores"""
>    dict_invertido = {}
>    
>    for clave, valor in dict_original.items():
>        # Verificar si el valor ya existe como clave
>        if valor in dict_invertido:
>            print(f"⚠️ Valor duplicado '{valor}' - sobrescribiendo")
>        dict_invertido[valor] = clave
>    
>    return dict_invertido
> 
> # Uso
> capitales = {
>    'Argentina': 'Buenos Aires', 
>    'España': 'Madrid', 
>    'Francia': 'París'
> }
> 
> ciudades = invertir_diccionario(capitales)
> print("Diccionario invertido:")
> for ciudad, pais in ciudades.items():
>    print(f"  {ciudad} es capital de {pais}")
> ```
>
> [!example] ➕ **Combinar Inventarios**
> 
> ```python
> def combinar_inventarios(tienda1, tienda2):
>    """Suma cantidades de productos comunes"""
>    inventario_total = {}
>    
>    # Procesar primera tienda
>    for producto, cantidad in tienda1.items():
>        inventario_total[producto] = cantidad
>    
>    # Procesar segunda tienda
>    for producto, cantidad in tienda2.items():
>        if producto in inventario_total:
>            inventario_total[producto] += cantidad
>            print(f"📦 Combinando {producto}: {tienda1.get(producto, 0)} + {cantidad} = {inventario_total[producto]}")
>        else:
>            inventario_total[producto] = cantidad
>            print(f"🆕 Nuevo producto: {producto} con {cantidad} unidades")
>    
>    return inventario_total
> 
> # Uso
> tienda_a = {'manzanas': 50, 'naranjas': 35, 'bananas': 20}
> tienda_b = {'manzanas': 20, 'peras': 30, 'bananas': 15}
> 
> total = combinar_inventarios(tienda_a, tienda_b)
> print("\nInventario final:")
> for producto, cantidad in total.items():
>    print(f"  {producto}: {cantidad} unidades")
> ```

## 🚀 Técnicas Modernas

> [!tip] ⚡ **Comprensiones de Diccionario**
> 
> ```python
> numeros = [1, 2, 3, 4, 5]
> 
> # Crear diccionario: número -> cuadrado
> cuadrados = {n: n**2 for n in numeros}
> print(cuadrados)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
> 
> # Filtrar durante iteración
> inventario = {'manzanas': 50, 'naranjas': 15, 'bananas': 40, 'uvas': 5}
> stock_alto = {k: v for k, v in inventario.items() if v >= 20}
> print(stock_alto)  # {'manzanas': 50, 'bananas': 40}
> 
> # Transformar valores
> precios = {'laptop': 1000, 'mouse': 50, 'teclado': 100}
> precios_con_iva = {producto: precio * 1.21 for producto, precio in precios.items()}
> print(precios_con_iva)
> ```
>
> [!tip] 🔗 **Enumerate con Diccionarios**
> 
> ```python
> estudiantes = {'Ana': 8.5, 'Juan': 7.2, 'María': 9.1, 'Carlos': 6.8}
> 
> # Añadir números de posición
> print("Ranking de estudiantes:")
> for posicion, (nombre, nota) in enumerate(estudiantes.items(), 1):
>    print(f"  {posicion}. {nombre}: {nota}")
> ```

## 📊 Visualización de Métodos de Iteración

```mermaid
graph TD
    A[🗂️ Diccionario] --> B{Métodos de Iteración}
    
    B --> C[🔑 .keys()]
    B --> D[📦 .values()] 
    B --> E[🧩 .items()]
    
    C --> C1["for clave in dict.keys()"]
    C --> C2["Solo necesitas las claves"]
    C --> C3["Verificaciones, filtros"]
    
    D --> D1["for valor in dict.values()"]
    D --> D2["Cálculos estadísticos"]
    D --> D3["Suma, promedio, máx/mín"]
    
    E --> E1["for clave, valor in dict.items()"]
    E --> E2["Acceso completo a datos"]
    E --> E3["Análisis complejos"]
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#f1f8e9
    
    style E fill:#c8e6c9
    style E1 fill:#a5d6a7
    style E2 fill:#a5d6a7
    style E3 fill:#a5d6a7
```

## 🧠 Técnicas de Estudio y Memorización

> [!tip] 🎯 **Mnemotecnia para Iteración**
> 
> **KVI = Keys, Values, Items**
> 
> - **K**eys (🔑): Solo las llaves del coche
> - **V**alues (📦): Solo el contenido de las cajas
> - **I**tems (🧩): La pieza completa (llave + contenido)
> 
> **Regla de Oro**: "Cuando necesites AMBOS, usa .items() - es MÁS eficiente que acceder por separado"
> 
> **Método 3-2-1:**
> 
> - 📅 3 días: Practicar .keys() y .values()
> - 📅 2 días: Dominar .items()
> - 📅 1 día: Técnicas avanzadas y comprensiones
>
> [!info] 🔄 **Comparación de Eficiencia**
> 
> |Necesidad|❌ Ineficiente|✅ Eficiente|
> |---|---|---|
> |Solo claves|`for k in dict.keys()`|`for k in dict:`|
> |Solo valores|`for k in dict: valor = dict[k]`|`for v in dict.values():`|
> |Ambos|`for k in dict: v = dict[k]`|`for k, v in dict.items():`|

## 🔗 Referencias

> [!quote] **Notas Relacionadas**
> 
> - [[Módulo 5.1 Diccionarios]] - Conceptos fundamentales
> - [[Módulo 4.2 Iteradores for]] - Fundamentos de iteración
> - [[Comprensiones en Python]] - Sintaxis avanzada
> - [[Funciones Built-in]] - enumerate, zip, sorted
> - [[Manejo de Errores con try, except, finally]] - Iteración segura

## 📚 Notas Recomendadas para Estudio

> [!info] 📖 **Temas Complementarios**
> 
> **Prerrequisitos:**
> 
> - [[Módulo 5.1: Diccionarios en Python]] - Creación y manipulación básica
> - [[Bucles for en Python]] - Conceptos de iteración
> - [[Variables y Desempaquetado]] - Sintaxis de desempaquetado
> 
> **Para Profundizar:**
> 
> - [[Comprensiones Avanzadas]] - Dict/List/Set comprehensions
> - [[Collections Module]] - defaultdict, Counter para iteración especializada
> - [[Algoritmos de Ordenamiento]] - Ordenar diccionarios por claves/valores
> - [[Programación Funcional]] - map(), filter(), reduce() con diccionarios
> - [[Estructuras de Datos Avanzadas]] - Diccionarios anidados y complejos
> - [[Optimización de Código]] - Técnicas de iteración eficiente

---

**Tags:** #python #diccionarios #iteracion #bucles-for #keys #values #items #estructuras-datos #modulo5 #programacion-intermedia #objetos-vista #comprensiones
