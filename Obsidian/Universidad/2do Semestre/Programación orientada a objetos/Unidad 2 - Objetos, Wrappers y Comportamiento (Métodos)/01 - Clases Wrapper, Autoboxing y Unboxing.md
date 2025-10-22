# 📦 Clases Wrapper, Autoboxing y Unboxing

## 🎯 Introducción

> [!info]- 💡 ¿Qué son las Clases Wrapper? Las **clases wrapper** (envoltorio) son clases que encapsulan los tipos de datos primitivos de Java, convirtiéndolos en objetos. Java proporciona una clase wrapper para cada tipo primitivo, permitiendo trabajar con ellos como objetos cuando sea necesario.
> 
> **¿Por qué son necesarias?**
> 
> - Los tipos primitivos **no son objetos**, por lo que no pueden usarse donde se requieren objetos
> - Algunas estructuras de datos (como `ArrayList`, `HashMap`) **solo aceptan objetos**
> - Proporcionan **métodos útiles** para convertir, comparar y manipular valores
> - Permiten valores **null** (a diferencia de los primitivos)
> 
> **Concepto clave:**
> 
> ```
> int edad = 25;              // Primitivo: valor directo en memoria
> Integer edadObj = 25;       // Wrapper: objeto que contiene el valor
> ```

---

## 🔄 Tabla de Tipos Primitivos y sus Wrappers

> [!success]- 📊 Correspondencia Primitivo ↔ Wrapper
> 
> |Tipo Primitivo|Clase Wrapper|Paquete|Ejemplo|
> |---|---|---|---|
> |**byte**|`Byte`|java.lang|`Byte b = 127;`|
> |**short**|`Short`|java.lang|`Short s = 32000;`|
> |**int**|`Integer`|java.lang|`Integer i = 100;`|
> |**long**|`Long`|java.lang|`Long l = 1000000L;`|
> |**float**|`Float`|java.lang|`Float f = 3.14f;`|
> |**double**|`Double`|java.lang|`Double d = 3.14159;`|
> |**char**|`Character`|java.lang|`Character c = 'A';`|
> |**boolean**|`Boolean`|java.lang|`Boolean bool = true;`|
> 
> **Características comunes:**
> 
> - Todas las clases wrapper son **inmutables** (no se pueden modificar después de creadas)
> - Todas están en el paquete `java.lang` (no requieren import)
> - Todas heredan de `Object` (pueden usar métodos como `toString()`, `equals()`, etc.)
> - Todas implementan `Comparable` (excepto `Boolean`)

---

## 🎁 Creación de Objetos Wrapper

### 📝 Formas de Crear Wrappers

> [!example]- 🔵 Métodos de Construcción
> 
> **1. Constructor (deprecated desde Java 9):**
> 
> ```java
> // ⚠️ DEPRECATED - No usar en código nuevo
> Integer num1 = new Integer(100);
> Double dec1 = new Double(3.14);
> Boolean bool1 = new Boolean(true);
> ```
> 
> **2. Método valueOf() - RECOMENDADO:**
> 
> ```java
> // ✅ FORMA MODERNA Y EFICIENTE
> Integer num2 = Integer.valueOf(100);
> Double dec2 = Double.valueOf(3.14);
> Boolean bool2 = Boolean.valueOf(true);
> Character c = Character.valueOf('A');
> 
> // También acepta String
> Integer num3 = Integer.valueOf("100");
> Double dec3 = Double.valueOf("3.14");
> Boolean bool3 = Boolean.valueOf("true");
> ```
> 
> **3. Asignación directa (Autoboxing) - MÁS SIMPLE:**
> 
> ```java
> // ✅ AUTOMÁTICO - Java convierte el primitivo a objeto
> Integer num4 = 100;
> Double dec4 = 3.14;
> Boolean bool4 = true;
> Character c2 = 'A';
> ```
> 
> **¿Cuál usar?**
> 
> - **Autoboxing** para código simple y legible
> - **valueOf()** cuando necesites control explícito o conversiones desde String
> - **Constructor** nunca (está obsoleto)

---

## 🔀 Autoboxing y Unboxing

### ⬆️ Autoboxing (Primitivo → Objeto)

> [!tip]- 📦 Conversión Automática a Objeto
> 
> **Concepto:** Autoboxing es la conversión automática de un tipo primitivo a su clase wrapper correspondiente.
> 
> **Sintaxis básica:**
> 
> ```java
> // Autoboxing automático
> Integer num = 100;        // int → Integer
> Double precio = 99.99;    // double → Double
> Boolean activo = true;    // boolean → Boolean
> Character letra = 'X';    // char → Character
> ```
> 
> **En asignaciones:**
> 
> ```java
> int primitivo = 42;
> Integer objeto = primitivo;  // Autoboxing: int → Integer
> 
> // Equivalente manual (lo que hace Java internamente):
> Integer objeto = Integer.valueOf(primitivo);
> ```
> 
> **En parámetros de métodos:**
> 
> ```java
> public void procesar(Integer numero) {
>     System.out.println("Número: " + numero);
> }
> 
> // Llamada con primitivo - Autoboxing automático
> procesar(50);  // int 50 se convierte automáticamente a Integer
> ```
> 
> **En colecciones:**
> 
> ```java
> import java.util.ArrayList;
> 
> ArrayList<Integer> numeros = new ArrayList<>();
> 
> // Autoboxing al agregar primitivos
> numeros.add(10);      // int → Integer
> numeros.add(20);      // int → Integer
> numeros.add(30);      // int → Integer
> 
> // Sin autoboxing tendrías que hacer:
> // numeros.add(Integer.valueOf(10));  // ❌ Tedioso
> ```
> 
> **En operaciones:**
> 
> ```java
> Integer a = 5;        // Autoboxing
> Integer b = 10;       // Autoboxing
> Integer suma = a + b; // Unboxing para sumar, luego Autoboxing del resultado
> // Equivalente a: Integer suma = Integer.valueOf(a.intValue() + b.intValue());
> ```

### ⬇️ Unboxing (Objeto → Primitivo)

> [!info]- 📤 Conversión Automática a Primitivo
> 
> **Concepto:** Unboxing es la conversión automática de un objeto wrapper a su tipo primitivo correspondiente.
> 
> **Sintaxis básica:**
> 
> ```java
> Integer objetoNum = 100;
> int primitivoNum = objetoNum;  // Unboxing: Integer → int
> 
> Double objetoDec = 3.14;
> double primitivoDec = objetoDec;  // Unboxing: Double → double
> ```
> 
> **Equivalente manual:**
> 
> ```java
> Integer objeto = 42;
> 
> // Unboxing automático:
> int primitivo = objeto;
> 
> // Equivalente manual (lo que hace Java):
> int primitivo = objeto.intValue();
> ```
> 
> **En operaciones aritméticas:**
> 
> ```java
> Integer a = 10;
> Integer b = 20;
> 
> // Unboxing automático para la operación
> int resultado = a + b;           // Integer → int, operación, resultado int
> Integer resultadoObj = a + b;    // Unboxing, operación, Autoboxing
> 
> // Equivalente manual:
> int resultado = a.intValue() + b.intValue();
> ```
> 
> **En comparaciones:**
> 
> ```java
> Integer x = 100;
> Integer y = 200;
> 
> // Unboxing para comparación
> if (x < y) {  // Integer → int para comparar
>     System.out.println("x es menor que y");
> }
> 
> // Equivalente manual:
> if (x.intValue() < y.intValue()) {
>     System.out.println("x es menor que y");
> }
> ```
> 
> **En expresiones:**
> 
> ```java
> Integer contador = 0;
> 
> contador++;  // Unboxing → incremento → Autoboxing
> // Equivalente: contador = Integer.valueOf(contador.intValue() + 1);
> 
> contador += 5;  // Unboxing → suma → Autoboxing
> // Equivalente: contador = Integer.valueOf(contador.intValue() + 5);
> ```

### 🔄 Tabla Comparativa

> [!note]- 📋 Autoboxing vs Unboxing
> 
> |Aspecto|Autoboxing|Unboxing|
> |---|---|---|
> |**Dirección**|Primitivo → Objeto|Objeto → Primitivo|
> |**Conversión**|`int` → `Integer`|`Integer` → `int`|
> |**Manual**|`Integer.valueOf(5)`|`objeto.intValue()`|
> |**Automático**|`Integer x = 5;`|`int y = objetoInteger;`|
> |**Cuándo ocurre**|Asignación, parámetros, colecciones|Operaciones, comparaciones|
> |**Riesgo**|Ninguno (siempre seguro)|`NullPointerException` si es null|
> 
> **Ejemplo completo:**
> 
> ```java
> // Autoboxing
> Integer num = 42;              // int → Integer
> 
> // Unboxing
> int valor = num;               // Integer → int
> 
> // Ambos en una operación
> Integer a = 10;                // Autoboxing
> Integer b = 20;                // Autoboxing
> int suma = a + b;              // Unboxing de a y b, suma, resultado int
> Integer sumaObj = a + b;       // Unboxing, suma, Autoboxing del resultado
> ```

---

## 🛠️ Métodos Útiles de las Clases Wrapper

### 🔢 Métodos de Conversión

> [!success]- 🔄 Conversión entre Tipos
> 
> **1. parseXxx() - String → Primitivo:**
> 
> ```java
> // String a primitivo
> int entero = Integer.parseInt("123");
> double decimal = Double.parseDouble("3.14");
> long largo = Long.parseLong("1000000");
> float flotante = Float.parseFloat("2.5");
> boolean bool = Boolean.parseBoolean("true");
> 
> // Con diferentes bases numéricas (solo enteros)
> int binario = Integer.parseInt("1010", 2);      // 10 en decimal
> int octal = Integer.parseInt("17", 8);          // 15 en decimal
> int hexadecimal = Integer.parseInt("FF", 16);   // 255 en decimal
> ```
> 
> **2. valueOf() - String/Primitivo → Objeto:**
> 
> ```java
> // String a objeto wrapper
> Integer num1 = Integer.valueOf("100");
> Double dec1 = Double.valueOf("3.14");
> Boolean bool1 = Boolean.valueOf("true");
> 
> // Primitivo a objeto wrapper
> Integer num2 = Integer.valueOf(100);
> Double dec2 = Double.valueOf(3.14);
> 
> // Con base numérica
> Integer binario = Integer.valueOf("1010", 2);
> ```
> 
> **3. xxxValue() - Objeto → Primitivo:**
> 
> ```java
> Integer objetoInt = 100;
> Double objetoDouble = 3.14;
> 
> // Conversión explícita
> int primitivo = objetoInt.intValue();
> double decimal = objetoDouble.doubleValue();
> 
> // Conversión cruzada
> long largo = objetoInt.longValue();        // Integer → long
> float flotante = objetoDouble.floatValue(); // Double → float
> ```
> 
> **4. toString() - Cualquier tipo → String:**
> 
> ```java
> // Objeto a String
> Integer num = 100;
> String texto1 = num.toString();
> 
> // Primitivo a String (método estático)
> String texto2 = Integer.toString(100);
> String texto3 = Double.toString(3.14);
> String texto4 = Boolean.toString(true);
> 
> // Con base numérica
> String binario = Integer.toString(10, 2);      // "1010"
> String hexadecimal = Integer.toString(255, 16); // "ff"
> ```
> 
> **Tabla resumen de conversiones:**
> 
> |Desde|Hacia|Método|Ejemplo|
> |---|---|---|---|
> |String|Primitivo|`parseXxx()`|`Integer.parseInt("123")`|
> |String|Wrapper|`valueOf()`|`Integer.valueOf("123")`|
> |Primitivo|Wrapper|`valueOf()` o autoboxing|`Integer.valueOf(123)`|
> |Wrapper|Primitivo|`xxxValue()` o unboxing|`objeto.intValue()`|
> |Wrapper|String|`toString()`|`objeto.toString()`|
> |Primitivo|String|`toString()` estático|`Integer.toString(123)`|

### 🔍 Métodos de Comparación

> [!example]- ⚖️ Comparar Valores
> 
> **1. equals() - Comparar contenido:**
> 
> ```java
> Integer a = 100;
> Integer b = 100;
> Integer c = 200;
> 
> System.out.println(a.equals(b));  // true (mismo valor)
> System.out.println(a.equals(c));  // false (valores diferentes)
> 
> // ⚠️ NO usar == con wrappers (compara referencias)
> Integer x = 1000;
> Integer y = 1000;
> System.out.println(x == y);       // false (diferentes objetos)
> System.out.println(x.equals(y));  // true (mismo valor)
> ```
> 
> **2. compareTo() - Comparación ordenada:**
> 
> ```java
> Integer a = 10;
> Integer b = 20;
> Integer c = 10;
> 
> // Retorna: negativo si menor, 0 si igual, positivo si mayor
> System.out.println(a.compareTo(b));  // -1 (10 < 20)
> System.out.println(b.compareTo(a));  // 1  (20 > 10)
> System.out.println(a.compareTo(c));  // 0  (10 == 10)
> 
> // Uso en ordenamiento
> if (a.compareTo(b) < 0) {
>     System.out.println("a es menor que b");
> }
> ```
> 
> **3. compare() - Método estático:**
> 
> ```java
> // Comparar sin crear objetos
> int resultado1 = Integer.compare(10, 20);    // -1
> int resultado2 = Double.compare(3.14, 2.5);  // 1
> int resultado3 = Boolean.compare(true, false); // 1
> ```
> 
> **⚠️ Trampa común con cache de wrappers:**
> 
> ```java
> // Para valores pequeños (-128 a 127), Java reutiliza objetos
> Integer a = 100;
> Integer b = 100;
> System.out.println(a == b);  // true (mismo objeto del cache)
> 
> // Para valores grandes, crea objetos nuevos
> Integer x = 1000;
> Integer y = 1000;
> System.out.println(x == y);  // false (objetos diferentes)
> 
> // ✅ SIEMPRE usa equals() para comparar valores
> System.out.println(x.equals(y));  // true (mismo valor)
> ```

### 🎯 Métodos Específicos por Clase

> [!tip]- 🔧 Métodos Especiales de Integer
> 
> ```java
> // Valores máximo y mínimo
> System.out.println(Integer.MAX_VALUE);  // 2147483647
> System.out.println(Integer.MIN_VALUE);  // -2147483648
> 
> // Número de bits
> System.out.println(Integer.SIZE);       // 32
> System.out.println(Integer.BYTES);      // 4
> 
> // Operaciones bit a bit
> int x = 10;  // 1010 en binario
> System.out.println(Integer.bitCount(x));      // 2 (dos unos)
> System.out.println(Integer.highestOneBit(x)); // 8 (bit más alto)
> System.out.println(Integer.reverse(x));       // Invertir bits
> 
> // Conversiones de base
> System.out.println(Integer.toBinaryString(10));   // "1010"
> System.out.println(Integer.toOctalString(10));    // "12"
> System.out.println(Integer.toHexString(255));     // "ff"
> 
> // Suma segura (evita overflow)
> try {
>     int resultado = Math.addExact(Integer.MAX_VALUE, 1);
> } catch (ArithmeticException e) {
>     System.out.println("Overflow detectado");
> }
> ```

> [!tip]- 🔧 Métodos Especiales de Double
> 
> ```java
> // Constantes especiales
> System.out.println(Double.MAX_VALUE);        // 1.7976931348623157E308
> System.out.println(Double.MIN_VALUE);        // 4.9E-324 (positivo más pequeño)
> System.out.println(Double.POSITIVE_INFINITY);
> System.out.println(Double.NEGATIVE_INFINITY);
> System.out.println(Double.NaN);              // Not a Number
> 
> // Verificaciones especiales
> double x = 0.0 / 0.0;  // NaN
> double y = 1.0 / 0.0;  // Infinity
> 
> System.out.println(Double.isNaN(x));         // true
> System.out.println(Double.isInfinite(y));    // true
> System.out.println(Double.isFinite(3.14));   // true
> 
> // Comparación con epsilon (para decimales)
> double a = 0.1 + 0.2;
> double b = 0.3;
> double epsilon = 0.0001;
> 
> if (Math.abs(a - b) < epsilon) {
>     System.out.println("Son aproximadamente iguales");
> }
> ```

> [!tip]- 🔧 Métodos Especiales de Character
> 
> ```java
> char c = 'A';
> 
> // Verificaciones de tipo
> System.out.println(Character.isDigit('5'));        // true
> System.out.println(Character.isLetter('A'));       // true
> System.out.println(Character.isUpperCase('A'));    // true
> System.out.println(Character.isLowerCase('a'));    // true
> System.out.println(Character.isWhitespace(' '));   // true
> System.out.println(Character.isLetterOrDigit('7')); // true
> 
> // Conversiones
> System.out.println(Character.toUpperCase('a'));    // 'A'
> System.out.println(Character.toLowerCase('Z'));    // 'z'
> 
> // Valores numéricos
> System.out.println(Character.getNumericValue('5')); // 5
> System.out.println(Character.getNumericValue('A')); // 10 (hexadecimal)
> 
> // Código Unicode
> char letra = 'Ñ';
> System.out.println((int) letra);                   // 209
> System.out.println(Character.toString(209));       // "Ñ"
> ```

> [!tip]- 🔧 Métodos Especiales de Boolean
> 
> ```java
> // Operaciones lógicas estáticas
> System.out.println(Boolean.logicalAnd(true, false));  // false
> System.out.println(Boolean.logicalOr(true, false));   // true
> System.out.println(Boolean.logicalXor(true, false));  // true
> 
> // Conversión desde String (case-insensitive)
> Boolean b1 = Boolean.valueOf("true");    // true
> Boolean b2 = Boolean.valueOf("TRUE");    // true
> Boolean b3 = Boolean.valueOf("yes");     // false (solo "true" es true)
> 
> // Comparación
> System.out.println(Boolean.compare(true, false));  // 1
> System.out.println(Boolean.compare(false, true));  // -1
> 
> // Parseo
> boolean primitivo = Boolean.parseBoolean("true");
> ```

---

## ⚠️ Problemas Comunes y Soluciones

### 🚨 NullPointerException

> [!warning]- ❌ El Peligro del Unboxing con null
> 
> **El problema:**
> 
> ```java
> // ❌ ERROR: NullPointerException
> Integer numero = null;
> int valor = numero;  // Unboxing de null causa excepción
> 
> // También en operaciones
> Integer a = null;
> Integer b = 10;
> int suma = a + b;  // ❌ NullPointerException al hacer unboxing de 'a'
> ```
> 
> **¿Por qué ocurre?** Cuando Java intenta hacer unboxing de un wrapper que es `null`, llama al método `xxxValue()` sobre un objeto nulo, causando la excepción.
> 
> **✅ Soluciones:**
> 
> **1. Validar antes de usar:**
> 
> ```java
> Integer numero = obtenerNumero();  // Puede retornar null
> 
> if (numero != null) {
>     int valor = numero;  // Seguro
>     System.out.println(valor);
> } else {
>     System.out.println("Valor no disponible");
> }
> ```
> 
> **2. Usar valor por defecto:**
> 
> ```java
> Integer numero = null;
> int valor = (numero != null) ? numero : 0;  // Usa 0 si es null
> ```
> 
> **3. Usar Optional (Java 8+):**
> 
> ```java
> import java.util.Optional;
> 
> Optional<Integer> numeroOpt = Optional.ofNullable(obtenerNumero());
> int valor = numeroOpt.orElse(0);  // Valor por defecto si es null
> ```
> 
> **4. Trabajar con wrappers sin unboxing:**
> 
> ```java
> Integer a = null;
> Integer b = 10;
> 
> // ❌ MAL: causa NullPointerException
> // int suma = a + b;
> 
> // ✅ BIEN: trabaja con objetos
> Integer suma = (a != null && b != null) ? a + b : null;
> ```
> 
> **Ejemplo práctico:**
> 
> ```java
> public class ManejadorSeguro {
>     
>     // ✅ Método seguro que maneja nulls
>     public static int sumarSeguro(Integer a, Integer b) {
>         // Validar ambos parámetros
>         if (a == null || b == null) {
>             return 0;  // O lanzar excepción, según necesidad
>         }
>         return a + b;  // Unboxing seguro
>     }
>     
>     public static void main(String[] args) {
>         Integer x = 10;
>         Integer y = null;
>         
>         int resultado = sumarSeguro(x, y);
>         System.out.println(resultado);  // 0 (sin excepción)
>     }
> }
> ```

### 🔄 Comparación con == vs equals()

> [!danger]- ⚡ La Trampa del Cache de Integers
> 
> **El problema del cache:**
> 
> ```java
> // Rango del cache: -128 a 127
> Integer a = 100;
> Integer b = 100;
> System.out.println(a == b);  // true (mismo objeto del cache)
> 
> Integer x = 1000;
> Integer y = 1000;
> System.out.println(x == y);  // false (objetos diferentes)
> 
> // ¿Confundido? Java cachea valores pequeños para eficiencia
> ```
> 
> **Explicación del cache:**
> 
> - Java mantiene un cache de objetos `Integer` para valores entre -128 y 127
> - Si creas un `Integer` en este rango, Java reutiliza el objeto del cache
> - Fuera de este rango, se crean nuevos objetos
> 
> **Demostración:**
> 
> ```java
> // Objetos del cache
> Integer cache1 = 50;
> Integer cache2 = 50;
> System.out.println(cache1 == cache2);        // true (mismo objeto)
> System.out.println(cache1.equals(cache2));   // true (mismo valor)
> 
> // Objetos fuera del cache
> Integer fuera1 = 500;
> Integer fuera2 = 500;
> System.out.println(fuera1 == fuera2);        // false (objetos distintos)
> System.out.println(fuera1.equals(fuera2));   // true (mismo valor)
> 
> // Con constructor (siempre crea nuevo objeto)
> Integer nuevo1 = new Integer(50);
> Integer nuevo2 = new Integer(50);
> System.out.println(nuevo1 == nuevo2);        // false
> System.out.println(nuevo1.equals(nuevo2));   // true
> ```
> 
> **✅ Regla de oro:**
> 
> ```java
> // ❌ NUNCA uses == para comparar wrappers
> Integer a = 100;
> Integer b = 100;
> if (a == b) { }  // ❌ Funciona por casualidad (cache)
> 
> // ✅ SIEMPRE usa equals()
> if (a.equals(b)) { }  // ✅ Correcto (compara valores)
> 
> // Excepción: comparar con null
> Integer numero = obtenerNumero();
> if (numero == null) { }  // ✅ Correcto (verificar nulidad)
> ```
> 
> **Tabla comparativa:**
> 
> |Operador|Qué compara|Cuándo usar|
> |---|---|---|
> |`==`|Referencias (identidad)|Solo para verificar null|
> |`.equals()`|Valores (contenido)|Para comparar valores|
> 
> **Ejemplo completo:**
> 
> ```java
> public class ComparacionWrappers {
>     public static void main(String[] args) {
>         // Caso 1: Cache
>         Integer a = 100;
>         Integer b = 100;
>         System.out.println("Cache:");
>         System.out.println("a == b: " + (a == b));          // true
>         System.out.println("a.equals(b): " + a.equals(b));  // true
>         
>         // Caso 2: Fuera del cache
>         Integer x = 1000;
>         Integer y = 1000;
>         System.out.println("\nFuera del cache:");
>         System.out.println("x == y: " + (x == y));          // false
>         System.out.println("x.equals(y): " + x.equals(y));  // true
>         
>         // Caso 3: Comparación correcta
>         Integer num1 = obtenerNumero1();
>         Integer num2 = obtenerNumero2();
>         
>         // ✅ Forma correcta
>         if (num1 != null && num1.equals(num2)) {
>             System.out.println("Los números son iguales");
>         }
>     }
>     
>     static Integer obtenerNumero1() { return 1000; }
>     static Integer obtenerNumero2() { return 1000; }
> }
> ```

### 🐌 Consideraciones de Rendimiento

> [!note]- ⚡ Impacto en Performance
> 
> **Autoboxing/Unboxing tiene un costo:**
> 
> ```java
> // ❌ INEFICIENTE: Boxing/Unboxing repetido
> Integer suma = 0;
> for (int i = 0; i < 1000000; i++) {
>     suma += i;  // Unboxing de suma, operación, Autoboxing del resultado
> }
> // Millones de conversiones innecesarias
> 
> // ✅ EFICIENTE: Usar primitivos cuando sea posible
> int suma = 0;
> for (int i = 0; i < 1000000; i++) {
>     suma += i;  // Operación directa, sin conversiones
> }
> ```
> 
> **En bucles intensivos:**
> 
> ```java
> // ❌ MAL: Wrapper en operaciones intensivas
> public Long factorial(int n) {
>     Long resultado = 1L;
>     for (int i = 2; i <= n; i++) {
>         resultado *= i;  // Unboxing → multiplicación → Autoboxing
>     }
>     return resultado;
> }
> 
> // ✅ MEJOR: Primitivo en cálculos, wrapper solo para retorno
> public Long factorial(int n) {
>     long resultado = 1L;  // Primitivo para cálculos
>     for (int i = 2; i <= n; i++) {
>         resultado *= i;  // Sin conversiones
>     }
>     return resultado;  // Un solo Autoboxing al retornar
> }
> ```
> 
> **En colecciones (inevitable):**
> 
> ```java
> import java.util.ArrayList;
> 
> // Aquí el autoboxing es necesario (ArrayList solo acepta objetos)
> ArrayList<Integer> lista = new ArrayList<>();
> for (int i = 0; i < 1000; i++) {
>     lista.add(i);  // Autoboxing necesario
> }
> 
> // Minimizar accesos repetidos
> int suma = 0;
> for (Integer num : lista) {  // Unboxing en cada iteración
>     suma += num;
> }
> ```
> 
> 
> |Escenario|Usar|Razón|
> |---|---|---|
> |Cálculos matemáticos intensivos|Primitivos|Mejor rendimiento|
> |Variables de clase/instancia|Primitivos (si no necesitan null)|Menos memoria|
> |Colecciones (ArrayList, HashMap)|Wrappers|Obligatorio|
> |Métodos que pueden retornar null|Wrappers|Permiten null|
> |APIs genéricas|Wrappers|Requerido por generics|
> |Bucles simples|Primitivos|Evitar conversiones|
> 
> **Benchmark aproximado:**
> 
> ```java
> // Ejemplo de diferencia de rendimiento
> 
> // Con primitivos: ~5ms
> long inicio = System.currentTimeMillis();
> int suma = 0;
> for (int i = 0; i < 10_000_000; i++) {
>     suma += i;
> }
> long fin = System.currentTimeMillis();
> System.out.println("Primitivos: " + (fin - inicio) + "ms");
> 
> // Con wrappers: ~150ms (30x más lento)
> inicio = System.currentTimeMillis();
> Integer sumaWrapper = 0;
> for (int i = 0; i < 10_000_000; i++) {
>     sumaWrapper += i;  // Unboxing → operación → Autoboxing
> }
> fin = System.currentTimeMillis();
> System.out.println("Wrappers: " + (fin - inicio) + "ms");
> ```
> 
> **Recomendaciones:**
> 
> - ✅ Usa primitivos para cálculos y variables locales
> - ✅ Usa wrappers cuando necesites null, colecciones o APIs genéricas
> - ✅ Evita autoboxing/unboxing innecesario en bucles
> - ✅ Convierte una sola vez si es necesario

---

## 🎯 Casos de Uso Prácticos

### 📊 Colecciones con Wrappers

> [!example]- 📦 ArrayList, HashMap y Estructuras Genéricas
> 
> **ArrayList con Integer:**
> 
> ```java
> import java.util.ArrayList;
> 
> public class EjemploArrayList {
>     public static void main(String[] args) {
>         // ❌ NO se puede: ArrayList<int>
>         // ✅ Correcto: ArrayList<Integer>
>         ArrayList<Integer> numeros = new ArrayList<>();
>         
>         // Agregar elementos (autoboxing automático)
>         numeros.add(10);      // int → Integer
>         numeros.add(20);
>         numeros.add(30);
>         
>         // Acceder elementos (unboxing automático)
>         int primero = numeros.get(0);  // Integer → int
>         System.out.println("Primer elemento: " + primero);
>         
>         // Iterar con for-each
>         int suma = 0;
>         for (Integer num : numeros) {  // Unboxing en cada iteración
>             suma += num;
>         }
>         System.out.println("Suma total: " + suma);
>         
>         // Buscar elemento
>         boolean contiene = numeros.contains(20);  // Autoboxing del 20
>         System.out.println("Contiene 20: " + contiene);
>         
>         // Remover elemento
>         numeros.remove(Integer.valueOf(20));  // Importante: usar valueOf
>         // numeros.remove(20);  // ❌ Esto remueve por índice, no por valor
>     }
> }
> ```
> 
> **HashMap con wrappers:**
> 
> ```java
> import java.util.HashMap;
> import java.util.Map;
> 
> public class EjemploHashMap {
>     public static void main(String[] args) {
>         // Mapa de estudiantes: ID → Edad
>         HashMap<Integer, Integer> edades = new HashMap<>();
>         
>         // Agregar elementos (autoboxing)
>         edades.put(1001, 20);  // Ambos int → Integer
>         edades.put(1002, 22);
>         edades.put(1003, 19);
>         
>         // Obtener valor (unboxing)
>         int edad = edades.get(1001);  // Integer → int
>         System.out.println("Edad del estudiante 1001: " + edad);
>         
>         // Verificar existencia
>         if (edades.containsKey(1002)) {
>             System.out.println("Estudiante 1002 existe");
>         }
>         
>         // Iterar sobre el mapa
>         for (Map.Entry<Integer, Integer> entrada : edades.entrySet()) {
>             int id = entrada.getKey();      // Unboxing
>             int edadEstudiante = entrada.getValue();  // Unboxing
>             System.out.println("ID: " + id + ", Edad: " + edadEstudiante);
>         }
>     }
> }
> ```
> 
> **Set con Double:**
> 
> ```java
> import java.util.HashSet;
> import java.util.Set;
> 
> public class EjemploSet {
>     public static void main(String[] args) {
>         Set<Double> precios = new HashSet<>();
>         
>         // Agregar precios (autoboxing)
>         precios.add(19.99);
>         precios.add(29.99);
>         precios.add(19.99);  // Duplicado, no se agrega
>         
>         System.out.println("Número de precios únicos: " + precios.size());
>         
>         // Calcular precio máximo
>         double maximo = 0.0;
>         for (Double precio : precios) {
>             if (precio > maximo) {
>                 maximo = precio;
>             }
>         }
>         System.out.println("Precio máximo: $" + maximo);
>     }
> }
> ```

### 🔄 Conversión de Datos de Usuario

> [!success]- ⌨️ Procesamiento de Entrada con Scanner
> 
> **Validación robusta de entrada:**
> 
> ```java
> import java.util.Scanner;
> 
> public class ValidadorEntrada {
>     
>     // Método para leer un entero de forma segura
>     public static Integer leerEnteroSeguro(Scanner scanner, String mensaje) {
>         System.out.print(mensaje);
>         
>         if (scanner.hasNextInt()) {
>             return scanner.nextInt();  // Autoboxing
>         } else {
>             scanner.next();  // Limpiar entrada inválida
>             return null;     // Retornar null si falla
>         }
>     }
>     
>     // Método para leer entero con reintentos
>     public static int leerEnteroConReintentos(Scanner scanner, String mensaje) {
>         Integer numero = null;
>         
>         while (numero == null) {
>             System.out.print(mensaje);
>             
>             if (scanner.hasNextInt()) {
>                 numero = scanner.nextInt();
>             } else {
>                 System.out.println("❌ Error: debes ingresar un número entero");
>                 scanner.next();  // Limpiar buffer
>             }
>         }
>         
>         return numero;  // Unboxing seguro (nunca es null aquí)
>     }
>     
>     public static void main(String[] args) {
>         Scanner scanner = new Scanner(System.in);
>         
>         // Ejemplo 1: Con manejo de null
>         Integer edad = leerEnteroSeguro(scanner, "Ingresa tu edad: ");
>         
>         if (edad != null) {
>             System.out.println("Edad válida: " + edad);
>         } else {
>             System.out.println("Entrada inválida");
>         }
>         
>         // Ejemplo 2: Con reintentos
>         int cantidad = leerEnteroConReintentos(scanner, "Ingresa cantidad: ");
>         System.out.println("Cantidad ingresada: " + cantidad);
>         
>         scanner.close();
>     }
> }
> ```
> 
> **Parseando datos de formulario:**
> 
> ```java
> import java.util.HashMap;
> import java.util.Map;
> 
> public class FormularioEstudiante {
>     
>     public static Map<String, Object> procesarFormulario(String[] datos) {
>         Map<String, Object> estudiante = new HashMap<>();
>         
>         try {
>             // Parsear datos con wrappers
>             Integer id = Integer.valueOf(datos[0]);
>             String nombre = datos[1];
>             Integer edad = Integer.valueOf(datos[2]);
>             Double promedio = Double.valueOf(datos[3]);
>             Boolean activo = Boolean.valueOf(datos[4]);
>             
>             // Almacenar en mapa
>             estudiante.put("id", id);
>             estudiante.put("nombre", nombre);
>             estudiante.put("edad", edad);
>             estudiante.put("promedio", promedio);
>             estudiante.put("activo", activo);
>             
>             return estudiante;
>             
>         } catch (NumberFormatException e) {
>             System.out.println("❌ Error: formato de datos incorrecto");
>             return null;
>         }
>     }
>     
>     public static void main(String[] args) {
>         // Simular datos de formulario
>         String[] datosEstudiante = {"1001", "Ana García", "20", "8.5", "true"};
>         
>         Map<String, Object> estudiante = procesarFormulario(datosEstudiante);
>         
>         if (estudiante != null) {
>             System.out.println("Estudiante procesado:");
>             System.out.println("ID: " + estudiante.get("id"));
>             System.out.println("Nombre: " + estudiante.get("nombre"));
>             System.out.println("Edad: " + estudiante.get("edad"));
>             System.out.println("Promedio: " + estudiante.get("promedio"));
>             System.out.println("Activo: " + estudiante.get("activo"));
>         }
>     }
> }
> ```

### 🧮 Métodos Genéricos y Wrappers

> [!info]- 🔧 Generics Requieren Wrappers
> 
> **Método genérico para encontrar máximo:**
> 
> ```java
> public class Utilidades {
>     
>     // ❌ NO se puede hacer genérico con primitivos
>     // public static <T> T maximo(T a, T b) { }
>     
>     // ✅ Genérico con wrappers (que implementan Comparable)
>     public static <T extends Comparable<T>> T maximo(T a, T b) {
>         if (a == null) return b;
>         if (b == null) return a;
>         return (a.compareTo(b) >= 0) ? a : b;
>     }
>     
>     public static void main(String[] args) {
>         // Con Integer
>         Integer maxInt = maximo(10, 20);  // Autoboxing
>         System.out.println("Máximo entero: " + maxInt);
>         
>         // Con Double
>         Double maxDouble = maximo(3.14, 2.71);
>         System.out.println("Máximo decimal: " + maxDouble);
>         
>         // Con String (también implementa Comparable)
>         String maxString = maximo("Ana", "Beatriz");
>         System.out.println("Máximo string: " + maxString);
>     }
> }
> ```
> 
> **Clase genérica para par de valores:**
> 
> ```java
> public class Par<T, U> {
>     private T primero;
>     private U segundo;
>     
>     public Par(T primero, U segundo) {
>         this.primero = primero;
>         this.segundo = segundo;
>     }
>     
>     public T getPrimero() { return primero; }
>     public U getSegundo() { return segundo; }
>     
>     @Override
>     public String toString() {
>         return "(" + primero + ", " + segundo + ")";
>     }
>     
>     public static void main(String[] args) {
>         // Par de Integer
>         Par<Integer, Integer> coordenadas = new Par<>(10, 20);
>         System.out.println("Coordenadas: " + coordenadas);
>         
>         // Par mixto
>         Par<String, Double> productoConPrecio = new Par<>("Laptop", 999.99);
>         System.out.println("Producto: " + productoConPrecio);
>         
>         // Usar valores (unboxing)
>         int x = coordenadas.getPrimero();
>         int y = coordenadas.getSegundo();
>         System.out.println("X=" + x + ", Y=" + y);
>     }
> }
> ```
> 
> **Lista genérica con operaciones:**
> 
> ```java
> import java.util.ArrayList;
> import java.util.List;
> 
> public class OperacionesLista {
>     
>     // Sumar lista de números (genérico con Number)
>     public static double sumar(List<? extends Number> lista) {
>         double suma = 0.0;
>         for (Number numero : lista) {
>             suma += numero.doubleValue();  // Conversión a double
>         }
>         return suma;
>     }
>     
>     // Promedio de lista
>     public static double promedio(List<? extends Number> lista) {
>         if (lista.isEmpty()) return 0.0;
>         return sumar(lista) / lista.size();
>     }
>     
>     public static void main(String[] args) {
>         // Lista de Integer
>         List<Integer> enteros = new ArrayList<>();
>         enteros.add(10);
>         enteros.add(20);
>         enteros.add(30);
>         
>         System.out.println("Suma de enteros: " + sumar(enteros));
>         System.out.println("Promedio: " + promedio(enteros));
>         
>         // Lista de Double
>         List<Double> decimales = new ArrayList<>();
>         decimales.add(3.14);
>         decimales.add(2.71);
>         decimales.add(1.41);
>         
>         System.out.println("Suma de decimales: " + sumar(decimales));
>         System.out.println("Promedio: " + promedio(decimales));
>     }
> }
> ```

---

## 🎨 Ejemplos Completos de Programas

> [!example]- 🟢 Programa 1: Calculadora Estadística
> 
> ```java
> import java.util.ArrayList;
> import java.util.Collections;
> import java.util.Scanner;
> 
> public class CalculadoraEstadistica {
>     
>     private ArrayList<Double> datos;
>     
>     public CalculadoraEstadistica() {
>         this.datos = new ArrayList<>();
>     }
>     
>     // Agregar dato
>     public void agregarDato(double valor) {
>         datos.add(valor);  // Autoboxing
>     }
>     
>     // Calcular promedio
>     public Double calcularPromedio() {
>         if (datos.isEmpty()) return null;
>         
>         double suma = 0.0;
>         for (Double dato : datos) {  // Unboxing
>             suma += dato;
>         }
>         return suma / datos.size();
>     }
>     
>     // Encontrar mínimo
>     public Double encontrarMinimo() {
>         if (datos.isEmpty()) return null;
>         return Collections.min(datos);
>     }
>     
>     // Encontrar máximo
>     public Double encontrarMaximo() {
>         if (datos.isEmpty()) return null;
>         return Collections.max(datos);
>     }
>     
>     // Calcular mediana
>     public Double calcularMediana() {
>         if (datos.isEmpty()) return null;
>         
>         ArrayList<Double> ordenados = new ArrayList<>(datos);
>         Collections.sort(ordenados);
>         
>         int tamaño = ordenados.size();
>         if (tamaño % 2 == 0) {
>             // Par: promedio de los dos centrales
>             double medio1 = ordenados.get(tamaño / 2 - 1);
>             double medio2 = ordenados.get(tamaño / 2);
>             return (medio1 + medio2) / 2.0;
>         } else {
>             // Impar: elemento central
>             return ordenados.get(tamaño / 2);
>         }
>     }
>     
>     // Mostrar estadísticas
>     public void mostrarEstadisticas() {
>         System.out.println("\n═══ ESTADÍSTICAS ═══");
>         System.out.println("Cantidad de datos: " + datos.size());
>         
>         Double promedio = calcularPromedio();
>         if (promedio != null) {
>             System.out.printf("Promedio: %.2f\n", promedio);
>         }
>         
>         Double minimo = encontrarMinimo();
>         if (minimo != null) {
>             System.out.printf("Mínimo: %.2f\n", minimo);
>         }
>         
>         Double maximo = encontrarMaximo();
>         if (maximo != null) {
>             System.out.printf("Máximo: %.2f\n", maximo);
>         }
>         
>         Double mediana = calcularMediana();
>         if (mediana != null) {
>             System.out.printf("Mediana: %.2f\n", mediana);
>         }
>     }
>     
>     public static void main(String[] args) {
>         Scanner scanner = new Scanner(System.in);
>         CalculadoraEstadistica calc = new CalculadoraEstadistica();
>         
>         System.out.println("═══ CALCULADORA ESTADÍSTICA ═══");
>         System.out.print("¿Cuántos datos deseas ingresar? ");
>         int cantidad = scanner.nextInt();
>         
>         // Leer datos
>         for (int i = 1; i <= cantidad; i++) {
>             System.out.print("Dato " + i + ": ");
>             double valor = scanner.nextDouble();
>             calc.agregarDato(valor);
>         }
>         
>         // Mostrar resultados
>         calc.mostrarEstadisticas();
>         
>         scanner.close();
>     }
> }
> ```

> [!example]- 🟡 Programa 2: Gestor de Inventario
> 
> ```java
> import java.util.HashMap;
> import java.util.Map;
> import java.util.Scanner;
> 
> public class GestorInventario {
>     
>     // Mapa: código producto → cantidad disponible
>     private Map<Integer, Integer> inventario;
>     // Mapa: código producto → precio
>     private Map<Integer, Double> precios;
>     // Mapa: código producto → nombre
>     private Map<Integer, String> nombres;
>     
>     public GestorInventario() {
>         inventario = new HashMap<>();
>         precios = new HashMap<>();
>         nombres = new HashMap<>();
>     }
>     
>     // Agregar producto
>     public void agregarProducto(int codigo, String nombre, 
>                                 int cantidad, double precio) {
>         nombres.put(codigo, nombre);          // Autoboxing del código
>         inventario.put(codigo, cantidad);     // Autoboxing de ambos
>         precios.put(codigo, precio);          // Autoboxing de ambos
>         System.out.println("✓ Producto agregado correctamente");
>     }
>     
>     // Consultar stock
>     public Integer consultarStock(int codigo) {
>         return inventario.get(codigo);  // Puede retornar null
>     }
>     
>     // Vender producto
>     public boolean vender(int codigo, int cantidad) {
>         Integer stockActual = inventario.get(codigo);
>         
>         if (stockActual == null) {
>             System.out.println("❌ Producto no existe");
>             return false;
>         }
>         
>         if (stockActual < cantidad) {
>             System.out.println("❌ Stock insuficiente");
>             System.out.println("   Disponible: " + stockActual);
>             return false;
>         }
>         
>         // Actualizar stock
>         inventario.put(codigo, stockActual - cantidad);
>         
>         // Calcular monto
>         Double precio = precios.get(codigo);
>         double total = precio * cantidad;
>         
>         System.out.println("✓ Venta realizada");
>         System.out.printf("  Total: $%.2f\n", total);
>         return true;
>     }
>     
>     // Reabastecer
>     public void reabastecer(int codigo, int cantidad) {
>         Integer stockActual = inventario.get(codigo);
>         
>         if (stockActual == null) {
>             System.out.println("❌ Producto no existe");
>             return;
>         }
>         
>         inventario.put(codigo, stockActual + cantidad);
>         System.out.println("✓ Reabastecimiento exitoso");
>         System.out.println("  Nuevo stock: " + inventario.get(codigo));
>     }
>     
>     // Mostrar inventario completo
>     public void mostrarInventario() {
>         System.out.println("\n═══ INVENTARIO COMPLETO ═══");
>         
>         if (inventario.isEmpty()) {
>             System.out.println("(No hay productos)");
>             return;
>         }
>         
>         System.out.println("Código | Nombre              | Stock | Precio");
>         System.out.println("─".repeat(55));
>         
>         for (Map.Entry<Integer, Integer> entrada : inventario.entrySet()) {
>             int codigo = entrada.getKey();      // Unboxing
>             int stock = entrada.getValue();     // Unboxing
>             String nombre = nombres.get(codigo);
>             double precio = precios.get(codigo);  // Unboxing
>             
>             System.out.printf("%-6d | %-19s | %-5d | $%.2f\n",
>                             codigo, nombre, stock, precio);
>         }
>     }
>     
>     // Calcular valor total del inventario
>     public double calcularValorTotal() {
>         double valorTotal = 0.0;
>         
>         for (Map.Entry<Integer, Integer> entrada : inventario.entrySet()) {
>             int codigo = entrada.getKey();
>             int stock = entrada.getValue();
>             double precio = precios.get(codigo);
>             
>             valorTotal += stock * precio;
>         }
>         
>         return valorTotal;
>     }
>     
>     public static void main(String[] args) {
>         Scanner scanner = new Scanner(System.in);
>         GestorInventario gestor = new GestorInventario();
>         
>         // Datos iniciales
>         gestor.agregarProducto(101, "Laptop", 15, 899.99);
>         gestor.agregarProducto(102, "Mouse", 50, 12.99);
>         gestor.agregarProducto(103, "Teclado", 30, 45.50);
>         gestor.agregarProducto(104, "Monitor", 20, 299.99);
>         
>         boolean continuar = true;
>         
>         while (continuar) {
>             System.out.println("\n═══ MENÚ ═══");
>             System.out.println("1. Ver inventario");
>             System.out.println("2. Consultar stock");
>             System.out.println("3. Vender producto");
>             System.out.println("4. Reabastecer");
>             System.out.println("5. Valor total inventario");
>             System.out.println("6. Salir");
>             System.out.print("Opción: ");
>             
>             int opcion = scanner.nextInt();
>             
>             switch (opcion) {
>                 case 1:
>                     gestor.mostrarInventario();
>                     break;
>                     
>                 case 2:
>                     System.out.print("Código de producto: ");
>                     int codigoConsulta = scanner.nextInt();
>                     Integer stock = gestor.consultarStock(codigoConsulta);
>                     if (stock != null) {
>                         System.out.println("Stock disponible: " + stock);
>                     } else {
>                         System.out.println("❌ Producto no encontrado");
>                     }
>                     break;
>                     
>                 case 3:
>                     System.out.print("Código de producto: ");
>                     int codigoVenta = scanner.nextInt();
>                     System.out.print("Cantidad a vender: ");
>                     int cantidadVenta = scanner.nextInt();
>                     gestor.vender(codigoVenta, cantidadVenta);
>                     break;
>                     
>                 case 4:
>                     System.out.print("Código de producto: ");
>                     int codigoReab = scanner.nextInt();
>                     System.out.print("Cantidad a agregar: ");
>                     int cantidadReab = scanner.nextInt();
>                     gestor.reabastecer(codigoReab, cantidadReab);
>                     break;
>                     
>                 case 5:
>                     double valorTotal = gestor.calcularValorTotal();
>                     System.out.printf("Valor total del inventario: $%.2f\n", 
>                                     valorTotal);
>                     break;
>                     
>                 case 6:
>                     continuar = false;
>                     System.out.println("¡Hasta luego!");
>                     break;
>                     
>                 default:
>                     System.out.println("❌ Opción inválida");
>             }
>         }
>         
>         scanner.close();
>     }
> }
> ```

> [!example]- 🔵 Programa 3: Conversor de Unidades Avanzado
> ```java
> import java.util.HashMap;
import java.util.InputMismatchException;
import java.util.Map;
import java.util.Scanner;
> 
> public class ConversorUnidades {
> 
>     // Factores de conversión (respecto a la unidad base)
>     // Se elimina el mapa TEMPERATURA_OFFSETS ya que no se usa.
>     private static final Map<String, Double> LONGITUD_FACTORES = new HashMap<>();
>     private static final Map<String, Double> PESO_FACTORES = new HashMap<>();
> 
>     static {
>         // Longitud (base: metro)
>         LONGITUD_FACTORES.put("m", 1.0);
>         LONGITUD_FACTORES.put("km", 1000.0);
>         LONGITUD_FACTORES.put("cm", 0.01);
>         LONGITUD_FACTORES.put("mm", 0.001);
>         LONGITUD_FACTORES.put("mi", 1609.34);      // milla
>         LONGITUD_FACTORES.put("ft", 0.3048);       // pie
>         LONGITUD_FACTORES.put("in", 0.0254);       // pulgada
> 
>         // Peso (base: kilogramo)
>         PESO_FACTORES.put("kg", 1.0);
>         PESO_FACTORES.put("g", 0.001);
>         PESO_FACTORES.put("mg", 0.000001);
>         PESO_FACTORES.put("lb", 0.453592);         // libra
>         PESO_FACTORES.put("oz", 0.0283495);        // onza
>         PESO_FACTORES.put("ton", 1000.0);          // tonelada (métrica)
>     }
> 
>     // Convertir temperatura (origen: valor a Celsius; destino: Celsius a unidad final)
>     public static Double convertirTemperatura(double valor,
>                                               String origen, String destino) {
>         // Primero convertir a Celsius
>         double celsius;
>         switch (origen.toLowerCase()) {
>             case "c":
>                 celsius = valor;
>                 break;
>             case "f":
>                 celsius = (valor - 32) * 5.0 / 9.0;
>                 break;
>             case "k":
>                 celsius = valor - 273.15;
>                 break;
>             default:
>                 return null;
>         }
> 
>         // Luego convertir de Celsius a destino
>         switch (destino.toLowerCase()) {
>             case "c":
>                 return celsius;
>             case "f":
>                 return celsius * 9.0 / 5.0 + 32;
>             case "k":
>                 return celsius + 273.15;
>             default:
>                 return null;
>         }
>     }
> 
>     // Convertir longitud
>     public static Double convertirLongitud(double valor,
>                                            String origen, String destino) {
>         Double factorOrigen = LONGITUD_FACTORES.get(origen.toLowerCase());
>         Double factorDestino = LONGITUD_FACTORES.get(destino.toLowerCase());
> 
>         if (factorOrigen == null || factorDestino == null) {
>             return null;
>         }
> 
>         // Convertir a metros (base), luego a unidad destino
>         double metros = valor * factorOrigen;
>         return metros / factorDestino;
>     }
> 
>     // Convertir peso
>     public static Double convertirPeso(double valor,
>                                        String origen, String destino) {
>         Double factorOrigen = PESO_FACTORES.get(origen.toLowerCase());
>         Double factorDestino = PESO_FACTORES.get(destino.toLowerCase());
> 
>         if (factorOrigen == null || factorDestino == null) {
>             return null;
>         }
> 
>         // Convertir a kilogramos (base), luego a unidad destino
>         double kilogramos = valor * factorOrigen;
>         return kilogramos / factorDestino;
>     }
> 
>     // Mostrar menú de unidades
>     public static void mostrarUnidades(String tipo) {
>         System.out.println("\nUnidades disponibles:");
>         switch (tipo) {
>             case "temperatura":
>                 System.out.println("  C   - Celsius");
>                 System.out.println("  F   - Fahrenheit");
>                 System.out.println("  K   - Kelvin");
>                 break;
>             case "longitud":
>                 System.out.println("  m   - Metro");
>                 System.out.println("  km  - Kilómetro");
>                 System.out.println("  cm  - Centímetro");
>                 System.out.println("  mm  - Milímetro");
>                 System.out.println("  mi  - Milla");
>                 System.out.println("  ft  - Pie");
>                 System.out.println("  in  - Pulgada");
>                 break;
>             case "peso":
>                 System.out.println("  kg  - Kilogramo");
>                 System.out.println("  g   - Gramo");
>                 System.out.println("  mg  - Miligramo");
>                 System.out.println("  lb  - Libra");
>                 System.out.println("  oz  - Onza");
>                 System.out.println("  ton - Tonelada");
>                 break;
>         }
>     }
> 
>     public static void main(String[] args) {
>         Scanner scanner = new Scanner(System.in);
>         boolean continuar = true;
> 
>         System.out.println("═══ CONVERSOR DE UNIDADES AVANZADO ═══");
> 
>         while (continuar) {
>             System.out.println("\n═══ MENÚ PRINCIPAL ═══");
>             System.out.println("1. Convertir Temperatura");
>             System.out.println("2. Convertir Longitud");
>             System.out.println("3. Convertir Peso");
>             System.out.println("4. Salir");
>             System.out.print("Selecciona una opción (1-4): ");
> 
>             // Leer la opción como String para manejar mejor la entrada incorrecta
>             String opcionStr = scanner.nextLine().trim();
>             int opcion = 0;
> 
>             try {
>                 opcion = Integer.parseInt(opcionStr);
>             } catch (NumberFormatException e) {
>                 opcion = 0; // Se establece a 0 para que caiga en la opción inválida
>             }
> 
>             if (opcion < 1 || opcion > 4) {
>                 System.out.println("❌ Opción inválida. Por favor, selecciona un número entre 1 y 4.");
>                 continue;
>             }
> 
>             if (opcion == 4) {
>                 continuar = false;
>                 System.out.println("¡Ha sido un placer ayudarte! ¡Sigue practicando! 👋");
>                 break;
>             }
> 
>             // --- Leer Valor a Convertir ---
>             System.out.print("\nIngresa el valor a convertir: ");
>             String valorStr = scanner.nextLine().trim();
>             Double valor = null;
> 
>             try {
>                 valor = Double.parseDouble(valorStr);
>             } catch (NumberFormatException e) {
>                 System.out.println("❌ Error de entrada: El valor debe ser un número válido.");
>                 continue;
>             }
> 
>             String tipoConversion = "";
>             Double resultado = null;
>             String unidadOrigen, unidadDestino;
> 
>             switch (opcion) {
>                 case 1:
>                     tipoConversion = "temperatura";
>                     mostrarUnidades(tipoConversion);
>                     System.out.print("Unidad origen (C, F, K): ");
>                     unidadOrigen = scanner.nextLine();
>                     System.out.print("Unidad destino (C, F, K): ");
>                     unidadDestino = scanner.nextLine();
>                     resultado = convertirTemperatura(valor, unidadOrigen, unidadDestino);
>                     break;
> 
>                 case 2:
>                     tipoConversion = "longitud";
>                     mostrarUnidades(tipoConversion);
>                     System.out.print("Unidad origen (ej. m, km, mi): ");
>                     unidadOrigen = scanner.nextLine();
>                     System.out.print("Unidad destino (ej. m, km, mi): ");
>                     unidadDestino = scanner.nextLine();
>                     resultado = convertirLongitud(valor, unidadOrigen, unidadDestino);
>                     break;
> 
>                 case 3:
>                     tipoConversion = "peso";
>                     mostrarUnidades(tipoConversion);
>                     System.out.print("Unidad origen (ej. kg, lb, oz): ");
>                     unidadOrigen = scanner.nextLine();
>                     System.out.print("Unidad destino (ej. kg, lb, oz): ");
>                     unidadDestino = scanner.nextLine();
>                     resultado = convertirPeso(valor, unidadOrigen, unidadDestino);
>                     break;
>             }
> 
>             // Mostrar resultado
>             if (resultado != null) {
>                 System.out.println("\n✅ Conversión Exitosa:");
>                 System.out.printf("  %.4f → %.4f\n", valor, resultado);
>             } else {
>                 System.out.println("❌ Error: Una de las unidades de conversión no es válida para " + tipoConversion + ".");
>             }
>         }
> 
>         scanner.close();
>     }
> }
> ```

> [!example]- 🟣 Programa 4: Analizador de Texto
> 
> ```java
> import java.util.HashMap;
> import java.util.Map;
> import java.util.Scanner;
> 
> public class AnalizadorTexto {
>     
>     private String texto;
>     private Map<Character, Integer> frecuenciaCaracteres;
>     private Map<String, Integer> frecuenciaPalabras;
>     
>     public AnalizadorTexto(String texto) {
>         this.texto = texto;
>         this.frecuenciaCaracteres = new HashMap<>();
>         this.frecuenciaPalabras = new HashMap<>();
>         analizar();
>     }
>     
>     // Analizar el texto
>     private void analizar() {
>         if (texto == null || texto.isEmpty()) {
>             return;
>         }
>         
>         // Analizar caracteres
>         for (char c : texto.toCharArray()) {
>             Character caracter = c;  // Autoboxing
>             Integer frecuencia = frecuenciaCaracteres.get(caracter);
>             
>             if (frecuencia == null) {
>                 frecuenciaCaracteres.put(caracter, 1);
>             } else {
>                 frecuenciaCaracteres.put(caracter, frecuencia + 1);
>             }
>         }
>         
>         // Analizar palabras
>         String[] palabras = texto.toLowerCase()
>                                  .replaceAll("[^a-záéíóúñ\\s]", "")
>                                  .split("\\s+");
>         
>         for (String palabra : palabras) {
>             if (!palabra.isEmpty()) {
>                 Integer frecuencia = frecuenciaPalabras.get(palabra);
>                 
>                 if (frecuencia == null) {
>                     frecuenciaPalabras.put(palabra, 1);
>                 } else {
>                     frecuenciaPalabras.put(palabra, frecuencia + 1);
>                 }
>             }
>         }
>     }
>     
>     // Contar total de caracteres
>     public Integer contarCaracteres() {
>         return texto.length();  // Autoboxing
>     }
>     
>     // Contar caracteres sin espacios
>     public Integer contarCaracteresSinEspacios() {
>         int contador = 0;
>         for (char c : texto.toCharArray()) {
>             if (!Character.isWhitespace(c)) {
>                 contador++;
>             }
>         }
>         return contador;  // Autoboxing
>     }
>     
>     // Contar palabras
>     public Integer contarPalabras() {
>         if (texto.trim().isEmpty()) {
>             return 0;
>         }
>         String[] palabras = texto.trim().split("\\s+");
>         return palabras.length;  // Autoboxing
>     }
>     
>     // Contar oraciones
>     public Integer contarOraciones() {
>         String[] oraciones = texto.split("[.!?]+");
>         int contador = 0;
>         for (String oracion : oraciones) {
>             if (!oracion.trim().isEmpty()) {
>                 contador++;
>             }
>         }
>         return contador;  // Autoboxing
>     }
>     
>     // Contar vocales
>     public Integer contarVocales() {
>         int contador = 0;
>         String vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ";
>         
>         for (char c : texto.toCharArray()) {
>             if (vocales.indexOf(c) != -1) {
>                 contador++;
>             }
>         }
>         return contador;  // Autoboxing
>     }
>     
>     // Contar consonantes
>     public Integer contarConsonantes() {
>         int contador = 0;
>         
>         for (char c : texto.toCharArray()) {
>             if (Character.isLetter(c)) {
>                 String vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ";
>                 if (vocales.indexOf(c) == -1) {
>                     contador++;
>                 }
>             }
>         }
>         return contador;  // Autoboxing
>     }
>     
>     // Palabra más frecuente
>     public String palabraMasFrecuente() {
>         if (frecuenciaPalabras.isEmpty()) {
>             return null;
>         }
>         
>         String palabraMasFrecuente = null;
>         Integer maxFrecuencia = 0;
>         
>         for (Map.Entry<String, Integer> entrada : frecuenciaPalabras.entrySet()) {
>             if (entrada.getValue() > maxFrecuencia) {
>                 maxFrecuencia = entrada.getValue();
>                 palabraMasFrecuente = entrada.getKey();
>             }
>         }
>         
>         return palabraMasFrecuente + " (" + maxFrecuencia + " veces)";
>     }
>     
>     // Carácter más frecuente (excluyendo espacios)
>     public String caracterMasFrecuente() {
>         Character caracterMasFrecuente = null;
>         Integer maxFrecuencia = 0;
>         
>         for (Map.Entry<Character, Integer> entrada : frecuenciaCaracteres.entrySet()) {
>             Character c = entrada.getKey();
>             Integer frecuencia = entrada.getValue();
>             
>             if (!Character.isWhitespace(c) && frecuencia > maxFrecuencia) {
>                 maxFrecuencia = frecuencia;
>                 caracterMasFrecuente = c;
>             }
>         }
>         
>         return (caracterMasFrecuente != null) 
>                ? caracterMasFrecuente + " (" + maxFrecuencia + " veces)" 
>                : "N/A";
>     }
>     
>     // Calcular promedio de palabras por oración
>     public Double promedioLongitudPalabra() {
>         if (frecuenciaPalabras.isEmpty()) {
>             return 0.0;
>         }
>         
>         int totalCaracteres = 0;
>         int totalPalabras = 0;
>         
>         for (Map.Entry<String, Integer> entrada : frecuenciaPalabras.entrySet()) {
>             String palabra = entrada.getKey();
>             Integer frecuencia = entrada.getValue();
>             
>             totalCaracteres += palabra.length() * frecuencia;
>             totalPalabras += frecuencia;
>         }
>         
>         return (double) totalCaracteres / totalPalabras;
>     }
>     
>     // Mostrar estadísticas completas
>     public void mostrarEstadisticas() {
>         System.out.println("\n═══ ANÁLISIS DE TEXTO ═══");
>         System.out.println("Texto analizado:");
>         System.out.println("\"" + texto + "\"");
>         
>         System.out.println("\n─── Estadísticas Básicas ───");
>         System.out.println("Total de caracteres: " + contarCaracteres());
>         System.out.println("Caracteres sin espacios: " + contarCaracteresSinEspacios());
>         System.out.println("Total de palabras: " + contarPalabras());
>         System.out.println("Total de oraciones: " + contarOraciones());
>         
>         System.out.println("\n─── Análisis de Caracteres ───");
>         System.out.println("Vocales: " + contarVocales());
>         System.out.println("Consonantes: " + contarConsonantes());
>         System.out.println("Carácter más frecuente: " + caracterMasFrecuente());
>         
>         System.out.println("\n─── Análisis de Palabras ───");
>         System.out.println("Palabra más frecuente: " + palabraMasFrecuente());
>         System.out.printf("Longitud promedio de palabra: %.2f caracteres\n", 
>                          promedioLongitudPalabra());
>         System.out.println("Palabras únicas: " + frecuenciaPalabras.size());
>     }
>     
>     // Mostrar top palabras
>     public void mostrarTopPalabras(int top) {
>         System.out.println("\n─── Top " + top + " Palabras Más Frecuentes ───");
>         
>         // Crear lista ordenada por frecuencia
>         frecuenciaPalabras.entrySet()
>             .stream()
>             .sorted((e1, e2) -> e2.getValue().compareTo(e1.getValue()))
>             .limit(top)
>             .forEach(entrada -> {
>                 System.out.printf("  %-15s : %d veces\n", 
>                                 entrada.getKey(), entrada.getValue());
>             });
>     }
>     
>     public static void main(String[] args) {
>         Scanner scanner = new Scanner(System.in);
>         
>         System.out.println("═══ ANALIZADOR DE TEXTO ═══");
>         System.out.println("Ingresa un texto para analizar:");
>         System.out.println("(Presiona Enter dos veces para terminar)");
>         
>         StringBuilder textoBuilder = new StringBuilder();
>         String linea;
>         int lineasVacias = 0;
>         
>         while (scanner.hasNextLine()) {
>             linea = scanner.nextLine();
>             
>             if (linea.isEmpty()) {
>                 lineasVacias++;
>                 if (lineasVacias >= 2) {
>                     break;
>                 }
>             } else {
>                 lineasVacias = 0;
>                 textoBuilder.append(linea).append(" ");
>             }
>         }
>         
>         String texto = textoBuilder.toString().trim();
>         
>         if (texto.isEmpty()) {
>             System.out.println("❌ No se ingresó texto");
>             scanner.close();
>             return;
>         }
>         
>         // Crear analizador
>         AnalizadorTexto analizador = new AnalizadorTexto(texto);
>         
>         // Mostrar resultados
>         analizador.mostrarEstadisticas();
>         analizador.mostrarTopPalabras(5);
>         
>         scanner.close();
>     }
> }
> ```

---

## 🎯 Mejores Prácticas y Convenciones

> [!tip]- ✅ Guía de Uso Efectivo
> 
> **1. Cuándo usar primitivos vs wrappers:**
> 
> ```java
> // ✅ Usa primitivos para:
> 
> // Variables locales en cálculos
> public double calcularArea(double radio) {
>     double pi = 3.14159;  // Primitivo
>     return pi * radio * radio;
> }
> 
> // Campos que nunca son null
> public class Persona {
>     private int edad;           // Siempre tiene valor
>     private double altura;      // Siempre tiene valor
> }
> 
> // Bucles e índices
> for (int i = 0; i < 100; i++) {
>     // Primitivo más eficiente
> }
> 
> // ✅ Usa wrappers para:
> 
> // Colecciones
> ArrayList<Integer> numeros = new ArrayList<>();
> Map<String, Double> precios = new HashMap<>();
> 
> // Valores opcionales (que pueden ser null)
> public class Producto {
>     private Integer stock;  // Puede ser null si no se conoce
>     private Double descuento;  // null = sin descuento
> }
> 
> // APIs genéricas
> public <T extends Number> T obtenerMaximo(List<T> lista) {
>     // Requiere wrapper
> }
> ```
> 
> **2. Manejo seguro de nulls:**
> 
> ```java
> // ✅ Validar antes de unboxing
> public int procesarNumero(Integer numero) {
>     if (numero == null) {
>         return 0;  // Valor por defecto
>     }
>     return numero * 2;  // Unboxing seguro
> }
> 
> // ✅ Usar operador ternario
> Integer cantidad = obtenerCantidad();
> int valor = (cantidad != null) ? cantidad : 0;
> 
> // ✅ Trabajar con wrappers sin unboxing
> public Integer sumarSeguro(Integer a, Integer b) {
>     if (a == null || b == null) {
>         return null;
>     }
>     return a + b;  // Autoboxing del resultado
> }
> ```
> 
> **3. Comparación correcta:**
> 
> ```java
> Integer a = 100;
> Integer b = 100;
> 
> // ❌ NUNCA hagas esto
> if (a == b) { }
> 
> // ✅ SIEMPRE usa equals()
> if (a.equals(b)) { }
> 
> // ✅ Validar null antes de equals()
> if (a != null && a.equals(b)) { }
> 
> // ✅ O usar Objects.equals (Java 7+)
> import java.util.Objects;
> if (Objects.equals(a, b)) { }  // Maneja nulls automáticamente
> ```
> 
> **4. Parseo seguro de Strings:**
> 
> ```java
> // ✅ Con manejo de excepciones
> public Integer parsearEntero(String texto) {
>     try {
>         return Integer.parseInt(texto);
>     } catch (NumberFormatException e) {
>         System.out.println("Error al parsear: " + texto);
>         return null;  // O un valor por defecto
>     }
> }
> 
> // ✅ Con validación previa
> public Integer parsearSiValido(String texto) {
>     if (texto == null || texto.trim().isEmpty()) {
>         return null;
>     }
>     
>     try {
>         return Integer.valueOf(texto);
>     } catch (NumberFormatException e) {
>         return null;
>     }
> }
> ```
> 
> **5. Optimización en bucles:**
> 
> ```java
> // ❌ INEFICIENTE
> Integer suma = 0;
> for (int i = 0; i < 1000000; i++) {
>     suma += i;  // Boxing/Unboxing millones de veces
> }
> 
> // ✅ EFICIENTE
> int suma = 0;
> for (int i = 0; i < 1000000; i++) {
>     suma += i;  // Sin conversiones
> }
> Integer sumaFinal = suma;  // Un solo boxing al final
> ```
> 
> **6. Uso correcto de constantes:**
> 
> ```java
> // ✅ Constantes con wrappers
> public class Configuracion {
>     public static final Integer MAX_INTENTOS = 3;
>     public static final Double TASA_IVA = 0.12;
>     
>     // Usar en comparaciones
>     public boolean validarIntentos(Integer intentos) {
>         return intentos != null && intentos < MAX_INTENTOS;
>     }
> }
> ```

---

## 🛠️ Errores Comunes y Soluciones

> [!warning]- ❌ Problemas Frecuentes
> 
> **Error 1: NullPointerException por unboxing**
> 
> ```java
> // ❌ ERROR
> Integer numero = null;
> int valor = numero;  // NullPointerException
> 
> // ✅ SOLUCIÓN 1: Validar
> if (numero != null) {
>     int valor = numero;
> }
> 
> // ✅ SOLUCIÓN 2: Valor por defecto
> int valor = (numero != null) ? numero : 0;
> 
> // ✅ SOLUCIÓN 3: Optional
> import java.util.Optional;
> int valor = Optional.ofNullable(numero).orElse(0);
> ```
> 
> **Error 2: Comparar wrappers con ==**
> 
> ```java
> // ❌ ERROR
> Integer x = 1000;
> Integer y = 1000;
> if (x == y) {  // false (diferentes objetos)
>     System.out.println("Iguales");
> }
> 
> // ✅ SOLUCIÓN
> if (x.equals(y)) {  // true (mismo valor)
>     System.out.println("Iguales");
> }
> ```
> 
> **Error 3: Confundir remove() en ArrayList**
> 
> ```java
> ArrayList<Integer> lista = new ArrayList<>();
> lista.add(10);
> lista.add(20);
> lista.add(30);
> 
> // ❌ ERROR: remueve por índice
> lista.remove(20);  // Intenta remover índice 20 (no existe)
> 
> // ✅ CORRECTO: remueve por valor
> lista.remove(Integer.valueOf(20));  // Remueve el objeto Integer(20)
> ```
> 
> **Error 4: Boxing/Unboxing innecesario en bucles**
> 
> ```java
> // ❌ INEFICIENTE
> public Integer factorial(int n) {
>     Integer resultado = 1;
>     for (int i = 2; i <= n; i++) {
>         resultado *= i;  // Unboxing → operación → Boxing
>     }
>     return resultado;
> }
> 
> // ✅ EFICIENTE
> public Integer factorial(int n) {
>     int resultado = 1;  // Primitivo para cálculos
>     for (int i = 2; i <= n; i++) {
>         resultado *= i;  // Sin conversiones
>     }
>     return resultado;  // Un solo boxing al retornar
> }
> ```
> 
> **Error 5: No manejar NumberFormatException**
> 
> ```java
> // ❌ PELIGROSO
> String entrada = scanner.nextLine();
> int numero = Integer.parseInt(entrada);  // Puede lanzar excepción
> 
> // ✅ SEGURO
> String entrada = scanner.nextLine();
> try {
>     int numero = Integer.parseInt(entrada);
>     System.out.println("Número válido: " + numero);
> } catch (NumberFormatException e) {
>     System.out.println("Error: entrada inválida");
> }
> ```
> 
> **Error 6: Comparar Double con ==**
> 
> ```java
> // ❌ PROBLEMA: precisión de punto flotante
> Double a = 0.1 + 0.2;
> Double b = 0.3;
> System.out.println(a.equals(b));  // false (0.30000000000000004 != 0.3)
> 
> // ✅ SOLUCIÓN: comparar con epsilon
> double epsilon = 0.0001;
> if (Math.abs(a - b) < epsilon) {
>     System.out.println("Son aproximadamente iguales");
> }
> ```
> 
> **Error 7: Usar constructor deprecated**
> 
> ```java
> // ❌ DEPRECATED (Java 9+)
> Integer num = new Integer(100);
> Double dec = new Double(3.14);
> 
> // ✅ MODERNO
> Integer num = Integer.valueOf(100);
> Double dec = Double.valueOf(3.14);
> 
> // ✅ O simplemente autoboxing
> Integer num = 100;
> Double dec = 3.14;
> ```

---

## 📊 Tabla Comparativa Final

> [!note]- 📋 Resumen Completo
> 
> |Aspecto|Primitivo|Wrapper|
> |---|---|---|
> |**Tipo**|Valor|Objeto|
> |**Null**|❌ No puede ser null|✅ Puede ser null|
> |**Memoria**|Menos (4-8 bytes)|Más (16+ bytes)|
> |**Velocidad**|⚡ Más rápido|🐌 Más lento|
> |**Colecciones**|❌ No permitido|✅ Requerido|
> |**Generics**|❌ No permitido|✅ Requerido|
> |**Métodos**|❌ No tiene métodos|✅ Tiene métodos útiles|
> |**Comparación**|Usa `==`|Usa `.equals()`|
> |**Valor por defecto**|0, false, '\u0000'|null|
> |**Inmutabilidad**|N/A|✅ Inmutable|
> |**Cuándo usar**|Cálculos, bucles|APIs, colecciones, nulls|
> 
> **Conversiones:**
> 
> |De|A|Método|Nombre|
> |---|---|---|---|
> |Primitivo|Wrapper|Automático o `valueOf()`|Autoboxing|
> |Wrapper|Primitivo|Automático o `xxxValue()`|Unboxing|
> |String|Primitivo|`parseXxx()`|Parsing|
> |String|Wrapper|`valueOf()`|Parsing + Boxing|
> |Wrapper|String|`toString()`|Conversión a texto|
> |Primitivo|String|`toString()` estático|Conversión a texto|

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica Guiada
> 
> **Nivel Básico:**
> 
> 1. **Conversor de tipos:** Crea un programa que convierta entre primitivos, wrappers y Strings
> 2. **Validador de entrada:** Método que valide entrada numérica y retorne Integer (null si inválido)
> 3. **Comparador seguro:** Método que compare dos Integer manejando nulls correctamente
> 4. **Calculadora con wrappers:** Operaciones básicas que manejen valores null
> 5. **Lista de números:** ArrayList que calcule suma, promedio, máximo y mínimo
> 
> **Nivel Intermedio:**
> 
> 6. **Caché personalizado:** Implementa tu propio caché de Integer similar al de Java
> 7. **Parseador robusto:** Clase que parsee diferentes tipos con manejo de errores
> 8. **Estadísticas de lista:** Calcula media, mediana, moda usando wrappers
> 9. **Conversor de bases:** Convierte números entre binario, octal, decimal y hexadecimal
> 10. **Gestor de configuración:** Almacena configuraciones con valores opcionales (nullables)
> 
> **Nivel Avanzado:**
> 
> 11. **Benchmark:** Mide diferencia de rendimiento entre primitivos y wrappers
> 12. **Calculadora científica:** Con funciones avanzadas usando wrappers
> 13. **Sistema de puntuaciones:** Ranking con HashMap<Integer, Double>
> 14. **Analizador de datos:** Lee CSV y calcula estadísticas con wrappers
> 15. **Cache inteligente:** Implementa LRU cache usando LinkedHashMap con wrappers

---

## 🔗 Conexiones con Temas Siguientes

> [!quote]- 🌐 ¿Qué Sigue Después?
> 
> **Este tema es prerequisito para:**
> 
> - **[[Colecciones en Java]]** - ArrayList, HashMap requieren wrappers
> - **[[Generics]]** - Solo funcionan con tipos de referencia (wrappers)
> - **[[Streams y Lambda]]** - Operaciones funcionales con wrappers
> - **[[Optional]]** - Alternativa moderna para manejar valores null
> - **[[Serialización]]** - Los wrappers son Serializable
> - **[[Reflection]]** - Inspeccionar tipos en tiempo de ejecución
> - **[[JDBC]]** - Mapeo de tipos SQL a Java usa wrappers
> - **[[JPA/Hibernate]]** - Entidades usan wrappers para campos opcionales
> 
> **Fundamentos que ya dominas:**
> 
> - ✅ Tipos primitivos de Java
> - ✅ Clases wrapper y sus métodos
> - ✅ Autoboxing y unboxing automático
> - ✅ Conversión entre tipos
> - ✅ Manejo de null con wrappers
> - ✅ Comparación correcta de objetos
> - ✅ Uso en colecciones
> 
> **Próximo paso recomendado:** [[Arrays y Colecciones en Java]]

---

## 📝 Resumen Ejecutivo

> [!summary]- 🎯 Puntos Clave para Recordar
> 
> **Conceptos fundamentales:**
> 
> 1. **Wrapper = Objeto que envuelve un primitivo**
> 2. **Autoboxing = Primitivo → Wrapper (automático)**
> 3. **Unboxing = Wrapper → Primitivo (automático)**
> 4. **Cada primitivo tiene su wrapper:** int→Integer, double→Double, etc.
> 
> **Reglas de oro:**
> 
> - ✅ Usa primitivos para cálculos y variables locales
> - ✅ Usa wrappers para colecciones, APIs genéricas y valores opcionales
> - ✅ SIEMPRE valida null antes de unboxing
> - ✅ NUNCA uses == para comparar wrappers (usa .equals())
> - ✅ Evita boxing/unboxing innecesario en bucles
> 
> **Métodos más importantes:**
> 
> ```java
> // Conversión String → Primitivo
> int num = Integer.parseInt("123");
> 
> // Conversión String → Wrapper
> Integer num = Integer.valueOf("123");
> 
> // Conversión Wrapper → Primitivo
> int num = objeto.intValue();
> 
> // Conversión cualquier tipo → String
> String texto = objeto.toString();
> 
> // Comparación segura
> if (obj1 != null && obj1.equals(obj2)) { }
> ```
> 
> **Peligros principales:**
> 
> 1. **NullPointerException** al hacer unboxing de null
> 2. **Comparar con ==** en lugar de .equals()
> 3. **Boxing/Unboxing en bucles** (impacto en rendimiento)
> 4. **Cache de Integer** (-128 a 127) puede confundir con ==
> 
> **Cuándo usar cada uno:**
> 
> |Usa Primitivo|Usa Wrapper|
> |---|---|
> |Variables locales|Colecciones (ArrayList, HashMap)|
> |Parámetros de cálculo|Valores que pueden ser null|
> |Bucles intensivos|APIs genéricas|
> |Campos siempre inicializados|Opcional (puede no existir)|
> |Performance crítica|Campos de base de datos nullable|

---

## 🔍 Preguntas de Autoevaluación

> [!question]- ❓ Verifica tu Comprensión
> 
> **Nivel Básico:**
> 
> 1. ¿Cuál es la diferencia entre `int` e `Integer`?
> 2. ¿Qué es el autoboxing? Da un ejemplo
> 3. ¿Qué es el unboxing? Da un ejemplo
> 4. ¿Por qué `Integer num = null; int x = num;` causa error?
> 5. ¿Cómo convertir un String "123" a int?
> 
> **Nivel Intermedio:**
> 
> 6. ¿Por qué no debes usar == para comparar wrappers?
> 7. ¿Qué es el cache de Integer y qué rango cubre?
> 8. ¿Cuál es la diferencia entre `parseInt()` y `valueOf()`?
> 9. ¿Por qué `ArrayList<int>` no es válido?
> 10. ¿Cómo afecta el boxing/unboxing al rendimiento en bucles?
> 
> **Nivel Avanzado:**
> 
> 11. Explica por qué `new Integer(100) == 100` es true
> 12. ¿Cuándo usarías `xxxValue()` explícitamente?
> 13. ¿Cómo implementarías un método que sume dos Integer permitiendo nulls?
> 14. ¿Qué ventajas tiene usar wrappers en JPA/Hibernate?
> 15. ¿Cómo optimizarías un método que hace muchas operaciones con Integer?
> 
> **Respuestas:**
> 
>**Ver respuestas básicas**
> 
> 16. `int` es un tipo primitivo (valor), `Integer` es una clase (objeto)
> 17. Autoboxing: conversión automática de primitivo a wrapper. `Integer x = 5;`
> 18. Unboxing: conversión automática de wrapper a primitivo. `int y = objetoInteger;`
> 19. No se puede hacer unboxing de null (causa NullPointerException)
> 20. `int num = Integer.parseInt("123");`
> 
> **Ver respuestas intermedias**
> 
> 21. Porque == compara referencias (identidad), no valores. Usar .equals()
> 22. Java cachea Integer entre -128 y 127 para eficiencia
> 23. parseInt() retorna primitivo, valueOf() retorna wrapper
> 24. Los generics solo aceptan tipos de referencia (objetos), no primitivos
> 25. Cada operación causa boxing/unboxing, multiplicando el costo. Mejor usar primitivos
> 
>**Ver respuestas avanzadas**
> 
> 26. Porque el unboxing convierte Integer a int, y luego se compara el valor
> 27. Cuando necesitas conversión cruzada: `Integer.doubleValue()`, o para evitar autoboxing
> 28. 
> ```java
>     public static Integer sumar(Integer a, Integer b) {
>         if (a == null || b == null) return null;
>         return a + b;
>     }
>  ```
>     
> 29. Campos nullable en BD se mapean mejor a wrappers (null = ausencia de valor)
> 30. Usar primitivos para cálculos, convertir a wrapper solo al final
> 
> 

---

## 🎮 Mini-Proyecto Integrador

> [!example]- 🏆 Sistema de Calificaciones Avanzado
> 
> **Descripción del proyecto:** Crea un sistema completo de gestión de calificaciones que use wrappers de forma apropiada, manejando casos especiales como notas ausentes (null), conversiones de String a números, y cálculos estadísticos.
> 
> **Requisitos:**
> 
> ```java
> import java.util.*;
> 
> /**
>  * Sistema completo de gestión de calificaciones
>  * Demuestra uso apropiado de wrappers, autoboxing/unboxing
>  */
> public class SistemaCalificaciones {
>     
>     // Clase interna para representar un estudiante
>     static class Estudiante {
>         private String nombre;
>         private Integer id;
>         private Map<String, Double> calificaciones;  // Materia → Nota
>         
>         public Estudiante(Integer id, String nombre) {
>             this.id = id;
>             this.nombre = nombre;
>             this.calificaciones = new HashMap<>();
>         }
>         
>         public void agregarCalificacion(String materia, Double nota) {
>             if (nota != null && nota >= 0 && nota <= 10) {
>                 calificaciones.put(materia, nota);
>             }
>         }
>         
>         public Double obtenerCalificacion(String materia) {
>             return calificaciones.get(materia);  // Puede retornar null
>         }
>         
>         public Double calcularPromedio() {
>             if (calificaciones.isEmpty()) {
>                 return null;
>             }
>             
>             double suma = 0.0;
>             for (Double nota : calificaciones.values()) {
>                 suma += nota;  // Unboxing
>             }
>             return suma / calificaciones.size();  // Autoboxing
>         }
>         
>         public Integer contarAprobadas(double notaMinima) {
>             int contador = 0;
>             for (Double nota : calificaciones.values()) {
>                 if (nota >= notaMinima) {
>                     contador++;
>                 }
>             }
>             return contador;  // Autoboxing
>         }
>         
>         public String getNombre() { return nombre; }
>         public Integer getId() { return id; }
>         public Map<String, Double> getCalificaciones() { 
>             return new HashMap<>(calificaciones); 
>         }
>     }
>     
>     // Sistema principal
>     private Map<Integer, Estudiante> estudiantes;
>     private Set<String> materiasDisponibles;
>     
>     public SistemaCalificaciones() {
>         this.estudiantes = new HashMap<>();
>         this.materiasDisponibles = new HashSet<>();
>     }
>     
>     public void agregarMateria(String materia) {
>         materiasDisponibles.add(materia);
>     }
>     
>     public void agregarEstudiante(Integer id, String nombre) {
>         if (!estudiantes.containsKey(id)) {
>             estudiantes.put(id, new Estudiante(id, nombre));
>             System.out.println("✓ Estudiante agregado: " + nombre);
>         } else {
>             System.out.println("❌ Ya existe un estudiante con ID " + id);
>         }
>     }
>     
>     public void registrarCalificacion(Integer idEstudiante, 
>                                      String materia, Double nota) {
>         Estudiante est = estudiantes.get(idEstudiante);
>         
>         if (est == null) {
>             System.out.println("❌ Estudiante no encontrado");
>             return;
>         }
>         
>         if (!materiasDisponibles.contains(materia)) {
>             System.out.println("❌ Materia no existe: " + materia);
>             return;
>         }
>         
>         if (nota == null || nota < 0 || nota > 10) {
>             System.out.println("❌ Nota inválida");
>             return;
>         }
>         
>         est.agregarCalificacion(materia, nota);
>         System.out.printf("✓ Calificación registrada: %s - %s: %.2f\n", 
>                          est.getNombre(), materia, nota);
>     }
>     
>     public void mostrarEstadisticasEstudiante(Integer id) {
>         Estudiante est = estudiantes.get(id);
>         
>         if (est == null) {
>             System.out.println("❌ Estudiante no encontrado");
>             return;
>         }
>         
>         System.out.println("\n═══ ESTADÍSTICAS ═══");
>         System.out.println("Estudiante: " + est.getNombre());
>         System.out.println("ID: " + est.getId());
>         
>         Map<String, Double> califs = est.getCalificaciones();
>         
>         if (califs.isEmpty()) {
>             System.out.println("(Sin calificaciones registradas)");
>             return;
>         }
>         
>         System.out.println("\nCalificaciones:");
>         for (Map.Entry<String, Double> entrada : califs.entrySet()) {
>             System.out.printf("  %-20s: %.2f\n", 
>                             entrada.getKey(), entrada.getValue());
>         }
>         
>         Double promedio = est.calcularPromedio();
>         if (promedio != null) {
>             System.out.printf("\nPromedio: %.2f\n", promedio);
>             
>             Integer aprobadas = est.contarAprobadas(7.0);
>             Integer total = califs.size();
>             System.out.println("Materias aprobadas: " + aprobadas + "/" + total);
>         }
>     }
>     
>     public void mostrarRanking() {
>         System.out.println("\n═══ RANKING GENERAL ═══");
>         
>         if (estudiantes.isEmpty()) {
>             System.out.println("(Sin estudiantes)");
>             return;
>         }
>         
>         // Crear lista ordenada por promedio
>         List<Estudiante> ranking = new ArrayList<>(estudiantes.values());
>         
>         // Ordenar (mayor promedio primero)
>         ranking.sort((e1, e2) -> {
>             Double prom1 = e1.calcularPromedio();
>             Double prom2 = e2.calcularPromedio();
>             
>             if (prom1 == null && prom2 == null) return 0;
>             if (prom1 == null) return 1;  // Sin notas va al final
>             if (prom2 == null) return -1;
>             
>             return prom2.compareTo(prom1);  // Descendente
>         });
>         
>         System.out.println("Pos | Nombre              | Promedio | Aprobadas");
>         System.out.println("─".repeat(55));
>         
>         int posicion = 1;
>         for (Estudiante est : ranking) {
>             Double promedio = est.calcularPromedio();
>             
>             if (promedio != null) {
>                 Integer aprobadas = est.contarAprobadas(7.0);
>                 Integer total = est.getCalificaciones().size();
>                 
>                 System.out.printf("%-3d | %-19s | %-8.2f | %d/%d\n",
>                                 posicion++, est.getNombre(), 
>                                 promedio, aprobadas, total);
>             }
>         }
>     }
>     
>     public Map<String, Double> calcularPromediosPorMateria() {
>         Map<String, List<Double>> notasPorMateria = new HashMap<>();
>         
>         // Agrupar notas por materia
>         for (Estudiante est : estudiantes.values()) {
>             for (Map.Entry<String, Double> entrada : 
>                  est.getCalificaciones().entrySet()) {
>                 
>                 String materia = entrada.getKey();
>                 Double nota = entrada.getValue();
>                 
>                 notasPorMateria.putIfAbsent(materia, new ArrayList<>());
>                 notasPorMateria.get(materia).add(nota);
>             }
>         }
>         
>         // Calcular promedios
>         Map<String, Double> promedios = new HashMap<>();
>         
>         for (Map.Entry<String, List<Double>> entrada : 
>              notasPorMateria.entrySet()) {
>             
>             String materia = entrada.getKey();
>             List<Double> notas = entrada.getValue();
>             
>             double suma = 0.0;
>             for (Double nota : notas) {
>                 suma += nota;
>             }
>             
>             Double promedio = suma / notas.size();
>             promedios.put(materia, promedio);
>         }
>         
>         return promedios;
>     }
>     
>     public void mostrarEstadisticasGlobales() {
>         System.out.println("\n═══ ESTADÍSTICAS GLOBALES ═══");
>         
>         System.out.println("Total de estudiantes: " + estudiantes.size());
>         System.out.println("Total de materias: " + materiasDisponibles.size());
>         
>         Map<String, Double> promediosPorMateria = calcularPromediosPorMateria();
>         
>         if (!promediosPorMateria.isEmpty()) {
>             System.out.println("\nPromedios por materia:");
>             for (Map.Entry<String, Double> entrada : 
>                  promediosPorMateria.entrySet()) {
>                 System.out.printf("  %-20s: %.2f\n", 
>                                 entrada.getKey(), entrada.getValue());
>             }
>         }
>         
>         // Calcular promedio general de todos los estudiantes
>         double sumaPromedios = 0.0;
>         int contadorEstudiantes = 0;
>         
>         for (Estudiante est : estudiantes.values()) {
>             Double promedio = est.calcularPromedio();
>             if (promedio != null) {
>                 sumaPromedios += promedio;
>                 contadorEstudiantes++;
>             }
>         }
>         
>         if (contadorEstudiantes > 0) {
>             Double promedioGeneral = sumaPromedios / contadorEstudiantes;
>             System.out.printf("\nPromedio general del curso: %.2f\n", 
>                             promedioGeneral);
>         }
>     }
>     
>     // Parsear nota desde String (manejo robusto)
>     public static Double parsearNota(String texto) {
>         if (texto == null || texto.trim().isEmpty()) {
>             return null;
>         }
>         
>         try {
>             Double nota = Double.valueOf(texto.trim());
>             
>             if (nota < 0 || nota > 10) {
>                 System.out.println("❌ Nota fuera de rango (0-10)");
>                 return null;
>             }
>             
>             return nota;
>         } catch (NumberFormatException e) {
>             System.out.println("❌ Formato de nota inválido");
>             return null;
>         }
>     }
>     
>     public static void main(String[] args) {
>         Scanner scanner = new Scanner(System.in);
>         SistemaCalificaciones sistema = new SistemaCalificaciones();
>         
>         // Datos de ejemplo
>         sistema.agregarMateria("Matemáticas");
>         sistema.agregarMateria("Física");
>         sistema.agregarMateria("Programación");
>         sistema.agregarMateria("Química");
>         sistema.agregarMateria("Literatura");
>         
>         sistema.agregarEstudiante(1001, "Ana García");
>         sistema.agregarEstudiante(1002, "Carlos López");
>         sistema.agregarEstudiante(1003, "María Torres");
>         sistema.agregarEstudiante(1004, "Juan Pérez");
>         
>         // Registrar algunas calificaciones
>         sistema.registrarCalificacion(1001, "Matemáticas", 9.5);
>         sistema.registrarCalificacion(1001, "Física", 8.7);
>         sistema.registrarCalificacion(1001, "Programación", 9.8);
>         
>         sistema.registrarCalificacion(1002, "Matemáticas", 7.5);
>         sistema.registrarCalificacion(1002, "Física", 8.0);
>         sistema.registrarCalificacion(1002, "Programación", 9.0);
>         
>         sistema.registrarCalificacion(1003, "Matemáticas", 8.5);
>         sistema.registrarCalificacion(1003, "Literatura", 9.2);
>         
>         boolean continuar = true;
>         
>         while (continuar) {
>             System.out.println("\n═══ MENÚ PRINCIPAL ═══");
>             System.out.println("1. Agregar estudiante");
>             System.out.println("2. Registrar calificación");
>             System.out.println("3. Ver estadísticas de estudiante");
>             System.out.println("4. Ver ranking");
>             System.out.println("5. Ver estadísticas globales");
>             System.out.println("6. Salir");
>             System.out.print("Opción: ");
>             
>             Integer opcion = null;
>             if (scanner.hasNextInt()) {
>                 opcion = scanner.nextInt();
>                 scanner.nextLine();
>             } else {
>                 scanner.nextLine();
>                 System.out.println("❌ Opción inválida");
>                 continue;
>             }
>             
>             switch (opcion) {
>                 case 1:
>                     System.out.print("ID del estudiante: ");
>                     Integer id = scanner.nextInt();
>                     scanner.nextLine();
>                     System.out.print("Nombre: ");
>                     String nombre = scanner.nextLine();
>                     sistema.agregarEstudiante(id, nombre);
>                     break;
>                     
>                 case 2:
>                     System.out.print("ID del estudiante: ");
>                     Integer idEst = scanner.nextInt();
>                     scanner.nextLine();
>                     System.out.print("Materia: ");
>                     String materia = scanner.nextLine();
>                     System.out.print("Nota (0-10): ");
>                     String notaTexto = scanner.nextLine();
>                     Double nota = parsearNota(notaTexto);
>                     if (nota != null) {
>                         sistema.registrarCalificacion(idEst, materia, nota);
>                     }
>                     break;
>                     
>                 case 3:
>                     System.out.print("ID del estudiante: ");
>                     Integer idConsulta = scanner.nextInt();
>                     sistema.mostrarEstadisticasEstudiante(idConsulta);
>                     break;
>                     
>                 case 4:
>                     sistema.mostrarRanking();
>                     break;
>                     
>                 case 5:
>                     sistema.mostrarEstadisticasGlobales();
>                     break;
>                     
>                 case 6:
>                     continuar = false;
>                     System.out.println("¡Hasta luego!");
>                     break;
>                     
>                 default:
>                     System.out.println("❌ Opción inválida");
>             }
>         }
>         
>         scanner.close();
>     }
> }
> ```
> 
> **Aspectos destacados del código:**
> 
> - ✅ Uso apropiado de wrappers en colecciones
> - ✅ Manejo seguro de valores null
> - ✅ Conversión robusta de String a Double
> - ✅ Comparación correcta con .equals()
> - ✅ Autoboxing/unboxing natural
> - ✅ Retorno de null para indicar ausencia de datos
> - ✅ Validación de rangos con wrappers

---

## 📚 Recursos Adicionales

> [!info]- 🔗 Para Profundizar
> 
> **Documentación oficial:**
> 
> - [Java Wrapper Classes - Oracle Docs](https://docs.oracle.com/javase/tutorial/java/data/numberclasses.html)
> - [Autoboxing and Unboxing - Oracle](https://docs.oracle.com/javase/tutorial/java/data/autoboxing.html)
> - [Integer API Documentation](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)
> 
> **Temas relacionados:**
> 
> - Number class (superclase de wrappers numéricos)
> - java.util.Objects (métodos utilitarios para comparación)
> - Optional (alternativa moderna a null)
> - Primitive Streams (IntStream, DoubleStream, etc.)
> 
> **Buenas prácticas:**
> 
> - Effective Java - Item 61: Prefer primitive types to boxed primitives
> - Java Performance Tuning - Capítulo sobre boxing/unboxing
> - Clean Code - Manejo de valores opcionales

---

## 🎯 Checklist de Dominio

> [!check]- ✅ ¿Has Dominado el Tema?
> 
> Marca lo que ya sabes hacer:
> 
> **Conceptos básicos:**
> 
> - [ ] Entiendo qué es una clase wrapper
> - [ ] Conozco las 8 clases wrapper y sus primitivos correspondientes
> - [ ] Comprendo qué es autoboxing
> - [ ] Comprendo qué es unboxing
> - [ ] Sé cuándo usar primitivos vs wrappers
> 
> **Conversiones:**
> 
> - [ ] Puedo convertir String a primitivo (parseInt, parseDouble, etc.)
> - [ ] Puedo convertir String a wrapper (valueOf)
> - [ ] Puedo convertir wrapper a primitivo (intValue, doubleValue, etc.)
> - [ ] Puedo convertir cualquier tipo a String (toString)
> - [ ] Entiendo la diferencia entre valueOf() y parseXxx()
> 
> **Operaciones:**
> 
> - [ ] Sé usar métodos útiles de Integer (toBinaryString, compare, etc.)
> - [ ] Sé usar métodos útiles de Double (isNaN, isInfinite, etc.)
> - [ ] Sé usar métodos útiles de Character (isDigit, isLetter, etc.)
> - [ ] Puedo trabajar con constantes (MAX_VALUE, MIN_VALUE, etc.)
> 
> **Manejo de null:**
> 
> - [ ] Valido null antes de hacer unboxing
> - [ ] Sé usar valores por defecto cuando hay null
> - [ ] Puedo diseñar métodos que manejen null apropiadamente
> - [ ] Entiendo cuándo es apropiado retornar null
> 
> **Comparación:**
> 
> - [ ] NUNCA uso == para comparar wrappers
> - [ ] SIEMPRE uso .equals() para comparar valores
> - [ ] Entiendo el cache de Integer (-128 a 127)
> - [ ] Sé usar compareTo() para ordenamiento
> 
> **Colecciones:**
> 
> - [ ] Puedo usar wrappers en ArrayList
> - [ ] Puedo usar wrappers en HashMap
> - [ ] Entiendo por qué los primitivos no funcionan con generics
> - [ ] Manejo autoboxing/unboxing en colecciones
> 
> **Performance:**
> 
> - [ ] Entiendo el impacto de boxing/unboxing
> - [ ] Evito conversiones innecesarias en bucles
> - [ ] Sé cuándo priorizar rendimiento vs funcionalidad
> 
> **Debugging:**
> 
> - [ ] Puedo identificar NullPointerException por unboxing
> - [ ] Puedo identificar problemas de comparación con ==
> - [ ] Puedo detectar NumberFormatException
> - [ ] Sé usar try-catch para parseo robusto
> 
> **¿Cuántas marcaste?**
> 
> - 0-10: Repasa los conceptos básicos
> - 11-20: Buen progreso, practica más
> - 21-30: Dominio sólido
> - 31-38: ¡Excelente! Estás listo para temas avanzados

---

## 🎬 Conclusión

> [!success]- 🏆 Has Completado: Clases Wrapper, Autoboxing y Unboxing
> 
> **Lo que has aprendido:**
> 
> 1. **Fundamentos de Wrappers**
>     - Qué son y por qué existen
>     - Las 8 clases wrapper principales
>     - Diferencias con tipos primitivos
> 2. **Autoboxing y Unboxing**
>     - Conversión automática bidireccional
>     - Cuándo ocurre cada una
>     - Ventajas y desventajas
> 3. **Métodos Útiles**
>     - Conversión entre tipos
>     - Parseo de Strings
>     - Operaciones especiales por clase
> 4. **Mejores Prácticas**
>     - Cuándo usar primitivos vs wrappers
>     - Manejo seguro de null
>     - Comparación correcta
>     - Optimización de rendimiento
> 5. **Problemas Comunes**
>     - NullPointerException
>     - Comparación con ==
>     - Cache de Integer
>     - Boxing/unboxing en bucles
> 
> **Habilidades adquiridas:**
> 
> - ✅ Trabajar con wrappers en colecciones
> - ✅ Convertir entre tipos de forma segura
> - ✅ Manejar valores opcionales (null)
> - ✅ Escribir código robusto y eficiente
> - ✅ Depurar problemas relacionados con wrappers
> 
> **Estás preparado para:**
> 
> - Trabajar con colecciones de Java
> - Usar APIs genéricas
> - Implementar código de producción robusto
> - Optimizar rendimiento cuando sea necesario
> - Avanzar a temas como Streams, Optional y APIs funcionales
> 
> **Recuerda:**
> 
> > "Los wrappers son objetos que te dan flexibilidad, pero los primitivos te dan velocidad. Usa cada uno donde corresponde, y tu código será tanto elegante como eficiente."
> 
> **Próximos pasos:**
> 
> 1. Practica con los ejercicios propuestos
> 2. Implementa el mini-proyecto integrador
> 3. Revisa código existente buscando wrappers
> 4. Continúa con [[Arrays y Colecciones en Java]]

---

**Tags:** #java #wrapper #autoboxing #unboxing #integer #double #character #boolean #tipos-datos #conversion #colecciones #null #poo #best-practices #performance #university #programming