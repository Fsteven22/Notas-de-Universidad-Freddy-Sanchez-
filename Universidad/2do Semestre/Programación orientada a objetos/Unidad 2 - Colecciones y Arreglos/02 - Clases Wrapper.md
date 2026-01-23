# 🎁 Clases Wrapper

## 🎯 Introducción

> [!info]- 💡 ¿Qué son las Clases Wrapper?
> 
> Las **clases wrapper** (envolventes) son clases que **encapsulan tipos primitivos** en objetos. Permiten tratar los tipos primitivos como objetos cuando es necesario.
> 
> **Analogía del mundo real:** Piensa en un wrapper como:
> 
> - **Envoltorio de regalo** → El regalo (dato primitivo) viene dentro de una caja (objeto wrapper)
> - **Sobre para carta** → La carta (int) va dentro del sobre (Integer)
> - **Caja para pizza** → La pizza es el dato, la caja permite transportarla y agregarle funcionalidades
> 
> **Problema que resuelven:**
> 
> ```mermaid
> graph TB
>     A[Necesitas usar<br/>tipos primitivos] --> B{¿En qué contexto?}
>     B -->|Colecciones| C[❌ ArrayList int<br/>no funciona]
>     B -->|Métodos genéricos| D[❌ No se puede<br/>usar int]
>     B -->|Parámetros null| E[❌ Primitivos no<br/>aceptan null]
>     
>     C --> F[✅ ArrayList Integer<br/>SÍ funciona]
>     D --> G[✅ Usar Integer<br/>como objeto]
>     E --> H[✅ Integer puede<br/>ser null]
>     
>     style C fill:#ffe1e1
>     style D fill:#ffe1e1
>     style E fill:#ffe1e1
>     style F fill:#e1ffe1
>     style G fill:#e1ffe1
>     style H fill:#e1ffe1
> ```
> 
> **Tabla de correspondencia:**
> 
> |Tipo Primitivo|Clase Wrapper|Paquete|
> |---|---|---|
> |`byte`|`Byte`|`java.lang`|
> |`short`|`Short`|`java.lang`|
> |`int`|`Integer`|`java.lang`|
> |`long`|`Long`|`java.lang`|
> |`float`|`Float`|`java.lang`|
> |`double`|`Double`|`java.lang`|
> |`char`|`Character`|`java.lang`|
> |`boolean`|`Boolean`|`java.lang`|

---

## 🔄 Autoboxing y Unboxing

### ⚡ Conversión Automática

> [!tip]- 🎪 Boxing y Unboxing Explicado
> 
> **Autoboxing** = Conversión automática de primitivo → objeto  
> **Unboxing** = Conversión automática de objeto → primitivo
> 
> **Antes de Java 5 (manual):**
> 
> ```java
> // ❌ Forma antigua - conversión manual
> int primitivo = 10;
> Integer objeto = new Integer(primitivo);  // Boxing manual
> int deVuelta = objeto.intValue();         // Unboxing manual
> ```
> 
> **Desde Java 5 (automático):**
> 
> ```java
> // ✅ Forma moderna - automático
> int primitivo = 10;
> Integer objeto = primitivo;      // Autoboxing
> int deVuelta = objeto;           // Unboxing automático
> ```
> 
> **Visualización del proceso:**
> 
> ```mermaid
> flowchart LR
>     A[int x = 5] -->|Autoboxing| B[Integer obj = x]
>     B -->|Unboxing| C[int y = obj]
>     
>     D[Primitivo] -.envuelve.-> E[Objeto]
>     E -.desenvuelve.-> F[Primitivo]
>     
>     style A fill:#e1f5ff
>     style B fill:#fff4e1
>     style C fill:#e1f5ff
> ```
> 
> **Ejemplos prácticos:**
> 
> ```java
> // Autoboxing en asignación
> Integer num1 = 100;           // int → Integer
> Double num2 = 3.14;           // double → Double
> Character letra = 'A';        // char → Character
> Boolean activo = true;        // boolean → Boolean
> 
> // Unboxing en asignación
> int valor1 = num1;            // Integer → int
> double valor2 = num2;         // Double → double
> char c = letra;               // Character → char
> boolean flag = activo;        // Boolean → boolean
> 
> // Autoboxing en operaciones
> Integer a = 10;
> Integer b = 20;
> Integer suma = a + b;         // Unboxing → suma → Autoboxing
> // Internamente: int temp1 = a.intValue();
> //              int temp2 = b.intValue();
> //              int resultado = temp1 + temp2;
> //              Integer suma = Integer.valueOf(resultado);
> 
> // Autoboxing en colecciones
> ArrayList<Integer> numeros = new ArrayList<>();
> numeros.add(5);               // Autoboxing: 5 → Integer(5)
> numeros.add(10);              // Autoboxing: 10 → Integer(10)
> int primero = numeros.get(0); // Unboxing: Integer(5) → 5
> ```
> 
> **Tabla comparativa:**
> 
> |Operación|Antes de Java 5|Java 5+|
> |---|---|---|
> |Primitivo → Wrapper|`new Integer(5)`|`Integer x = 5;`|
> |Wrapper → Primitivo|`obj.intValue()`|`int x = obj;`|
> |En colecciones|No se podía|Automático|
> |En operaciones|Manual|Automático|

---

## 🛠️ Creación de Objetos Wrapper

### 📝 Formas de Instanciar

> [!example]- 🔨 Métodos de Creación
> 
> **1. Autoboxing (recomendado):**
> 
> ```java
> // ✅ Forma moderna y recomendada
> Integer num1 = 100;
> Double num2 = 3.14;
> Character letra = 'A';
> Boolean activo = true;
> ```
> 
> **2. Método valueOf() (recomendado):**
> 
> ```java
> // ✅ Usa caché para valores comunes
> Integer num1 = Integer.valueOf(100);
> Double num2 = Double.valueOf(3.14);
> Character letra = Character.valueOf('A');
> Boolean activo = Boolean.valueOf(true);
> 
> // Desde String
> Integer num3 = Integer.valueOf("42");
> Double num4 = Double.valueOf("3.14");
> Boolean flag = Boolean.valueOf("true");
> ```
> 
> **3. Constructor (⚠️ DEPRECADO desde Java 9):**
> 
> ```java
> // ❌ NO recomendado - deprecado
> Integer num1 = new Integer(100);
> Double num2 = new Double(3.14);
> 
> // Razones para no usar:
> // - Crea nuevos objetos siempre (no usa caché)
> // - Menos eficiente en memoria
> // - Deprecado oficialmente
> ```
> 
> **Caché de valores:**
> 
> ```java
> // Integer cachea valores de -128 a 127
> Integer a = 100;
> Integer b = 100;
> System.out.println(a == b);  // true (mismo objeto del caché)
> 
> Integer c = 200;
> Integer d = 200;
> System.out.println(c == d);  // false (fuera del caché, objetos diferentes)
> 
> // ✅ Siempre usar equals() para comparar contenido
> System.out.println(c.equals(d));  // true
> ```
> 
> **Visualización del caché:**
> 
> ```mermaid
> graph TB
>     A[Integer.valueOf 100] --> B{¿Valor en<br/>caché?}
>     B -->|Sí -128 a 127| C[Retornar objeto<br/>del caché]
>     B -->|No > 127 o < -128| D[Crear nuevo<br/>objeto]
>     
>     E[Integer a = 100<br/>Integer b = 100] --> F[a == b<br/>✅ true]
>     
>     G[Integer c = 200<br/>Integer d = 200] --> H[c == d<br/>❌ false]
>     
>     style C fill:#e1ffe1
>     style D fill:#fff4e1
>     style F fill:#e1ffe1
>     style H fill:#ffe1e1
> ```

---

## 🔧 Métodos Útiles

### 🎯 Conversiones

> [!success]- 🔄 Parseo y Conversión
> 
> **1. String → Primitivo (parseXxx):**
> 
> ```java
> // Retorna tipo primitivo
> int num1 = Integer.parseInt("123");          // String → int
> double num2 = Double.parseDouble("3.14");    // String → double
> boolean flag = Boolean.parseBoolean("true"); // String → boolean
> long num3 = Long.parseLong("999999");        // String → long
> 
> // ⚠️ Puede lanzar NumberFormatException
> try {
>     int invalido = Integer.parseInt("abc");
> } catch (NumberFormatException e) {
>     System.out.println("❌ Error: no es un número válido");
> }
> ```
> 
> **2. String → Wrapper (valueOf):**
> 
> ```java
> // Retorna objeto Wrapper
> Integer obj1 = Integer.valueOf("123");       // String → Integer
> Double obj2 = Double.valueOf("3.14");        // String → Double
> Boolean obj3 = Boolean.valueOf("true");      // String → Boolean
> 
> // También acepta primitivos
> Integer obj4 = Integer.valueOf(42);          // int → Integer
> ```
> 
> **3. Wrapper/Primitivo → String:**
> 
> ```java
> // Forma 1: toString() en el wrapper
> Integer num = 123;
> String str1 = num.toString();                // "123"
> 
> // Forma 2: toString() estático
> String str2 = Integer.toString(456);         // "456"
> 
> // Forma 3: String.valueOf()
> String str3 = String.valueOf(789);           // "789"
> 
> // Forma 4: Concatenación
> String str4 = "" + 100;                      // "100"
> ```
> 
> **4. Conversión entre tipos numéricos:**
> 
> ```java
> Integer num = 100;
> 
> // Wrapper → otros primitivos
> byte b = num.byteValue();
> short s = num.shortValue();
> int i = num.intValue();
> long l = num.longValue();
> float f = num.floatValue();
> double d = num.doubleValue();
> 
> System.out.println("byte: " + b);    // 100
> System.out.println("double: " + d);  // 100.0
> ```
> 
> **Diagrama de conversiones:**
> 
> ```mermaid
> graph TB
>     A[String 123] -->|parseInt| B[int 123]
>     A -->|valueOf| C[Integer 123]
>     
>     B -->|autoboxing| C
>     C -->|unboxing| B
>     
>     B -->|toString| D[String 123]
>     C -->|toString| D
>     
>     C -->|intValue| B
>     C -->|doubleValue| E[double 123.0]
>     
>     style A fill:#e1f5ff
>     style B fill:#fff4e1
>     style C fill:#ffe1e1
>     style D fill:#e1f5ff
> ```

### 🧮 Métodos de Utilidad

> [!tip]- 🎲 Funciones Adicionales
> 
> **1. Comparación:**
> 
> ```java
> Integer a = 100;
> Integer b = 200;
> 
> // Comparar objetos
> int resultado = a.compareTo(b);
> // resultado < 0  → a menor que b
> // resultado == 0 → a igual a b
> // resultado > 0  → a mayor que b
> 
> System.out.println(a.compareTo(b));  // -1 (100 < 200)
> 
> // Método estático compare
> int comp = Integer.compare(100, 200);
> System.out.println(comp);            // -1
> ```
> 
> **2. Valores límite (constantes):**
> 
> ```java
> // Valores máximos y mínimos
> System.out.println("int MAX: " + Integer.MAX_VALUE);      // 2147483647
> System.out.println("int MIN: " + Integer.MIN_VALUE);      // -2147483648
> 
> System.out.println("double MAX: " + Double.MAX_VALUE);    // 1.7976931348623157E308
> System.out.println("double MIN: " + Double.MIN_VALUE);    // 4.9E-324
> 
> System.out.println("byte MAX: " + Byte.MAX_VALUE);        // 127
> System.out.println("byte MIN: " + Byte.MIN_VALUE);        // -128
> 
> // Tamaño en bits
> System.out.println("int SIZE: " + Integer.SIZE);          // 32 bits
> System.out.println("long SIZE: " + Long.SIZE);            // 64 bits
> ```
> 
> **3. Operaciones matemáticas (Integer/Long):**
> 
> ```java
> // Suma con detección de overflow
> try {
>     int suma = Math.addExact(Integer.MAX_VALUE, 1);
> } catch (ArithmeticException e) {
>     System.out.println("❌ Overflow detectado");
> }
> 
> // Máximo y mínimo
> int max = Integer.max(10, 20);        // 20
> int min = Integer.min(10, 20);        // 10
> 
> // Suma sin signo
> int sumaSinSigno = Integer.sum(10, 20);  // 30
> ```
> 
> **4. Manipulación de bits (Integer):**
> 
> ```java
> int num = 5;  // Binario: 101
> 
> // Contar bits en 1
> int bits = Integer.bitCount(num);              // 2
> 
> // Representación binaria
> String binario = Integer.toBinaryString(num);  // "101"
> 
> // Representación hexadecimal
> String hex = Integer.toHexString(num);         // "5"
> 
> // Representación octal
> String octal = Integer.toOctalString(num);     // "5"
> 
> System.out.println("Decimal: " + num);         // 5
> System.out.println("Binario: " + binario);     // 101
> System.out.println("Hexadecimal: " + hex);     // 5
> ```
> 
> **5. Character - métodos especiales:**
> 
> ```java
> char letra = 'A';
> 
> // Verificaciones
> boolean esLetra = Character.isLetter(letra);         // true
> boolean esDigito = Character.isDigit('5');           // true
> boolean esEspacio = Character.isWhitespace(' ');     // true
> boolean esMayuscula = Character.isUpperCase(letra);  // true
> boolean esMinuscula = Character.isLowerCase('a');    // true
> 
> // Conversiones
> char minuscula = Character.toLowerCase('A');         // 'a'
> char mayuscula = Character.toUpperCase('b');         // 'B'
> 
> // Valor numérico
> int valor = Character.getNumericValue('5');          // 5
> ```
> 
> **Tabla de métodos comunes:**
> 
> |Método|Descripción|Ejemplo|Resultado|
> |---|---|---|---|
> |`parseInt(String)`|String → primitivo|`Integer.parseInt("123")`|`123`|
> |`valueOf(String)`|String → Wrapper|`Integer.valueOf("123")`|`Integer(123)`|
> |`toString()`|Wrapper → String|`num.toString()`|`"123"`|
> |`compareTo()`|Comparar|`a.compareTo(b)`|`-1, 0, 1`|
> |`equals()`|Igualdad de contenido|`a.equals(b)`|`true/false`|
> |`MAX_VALUE`|Valor máximo|`Integer.MAX_VALUE`|`2147483647`|
> |`MIN_VALUE`|Valor mínimo|`Integer.MIN_VALUE`|`-2147483648`|

---

## ⚠️ Comparación: == vs equals()

### 🔍 Diferencias Críticas

> [!danger]- ⚡ Comportamiento de Comparación
> 
> **Regla de oro:**
> 
> - `"=="` compara **referencias** (direcciones de memoria)
> - `equals()` compara **contenido** (valores)
> 
> **Ejemplo del problema:**
> 
> ```java
> // Valores dentro del caché (-128 a 127)
> Integer a = 100;
> Integer b = 100;
> System.out.println(a == b);        // ✅ true (mismo objeto del caché)
> System.out.println(a.equals(b));   // ✅ true (mismo contenido)
> 
> // Valores fuera del caché
> Integer c = 200;
> Integer d = 200;
> System.out.println(c == d);        // ❌ false (objetos diferentes)
> System.out.println(c.equals(d));   // ✅ true (mismo contenido)
> 
> // Con new (nunca usa caché)
> Integer e = new Integer(100);
> Integer f = new Integer(100);
> System.out.println(e == f);        // ❌ false (objetos diferentes)
> System.out.println(e.equals(f));   // ✅ true (mismo contenido)
> ```
> 
> **Visualización en memoria:**
> 
> ```mermaid
> graph TB
>     subgraph "Valores en caché -128 a 127"
>         A[Integer a = 100] --> C[Objeto: 100<br/>en caché]
>         B[Integer b = 100] --> C
>     end
>     
>     subgraph "Valores fuera de caché"
>         D[Integer c = 200] --> F[Objeto 1: 200]
>         E[Integer d = 200] --> G[Objeto 2: 200]
>     end
>     
>     H[a == b] --> I[✅ true<br/>misma referencia]
>     J[c == d] --> K[❌ false<br/>diferentes referencias]
>     
>     style I fill:#e1ffe1
>     style K fill:#ffe1e1
> ```
> 
> **Mejor práctica:**
> 
> ```java
> // ❌ NUNCA uses "==" para comparar Wrappers
> Integer x = 1000;
> Integer y = 1000;
> if (x == y) {  // ❌ MAL - impredecible
>     System.out.println("Iguales");
> }
> 
> // ✅ SIEMPRE usa equals()
> if (x.equals(y)) {  // ✅ BIEN - siempre correcto
>     System.out.println("Iguales");
> }
> 
> // ⚠️ Cuidado con null
> Integer z = null;
> if (z != null && z.equals(100)) {  // ✅ Verificar null primero
>     System.out.println("Es 100");
> }
> ```
> 
> **Tabla resumen:**
> 
> |Comparación|Tipo Primitivo|Wrapper|
> |---|---|---|
> |**Operador "=="**|✅ Compara valores|❌ Compara referencias|
> |**Método equals()**|N/A|✅ Compara contenido|
> |**Recomendación**|Usar `"=="`|Usar `equals()`|

---

## 💾 Uso con Colecciones

### 📦 Integración con Estructuras de Datos

> [!success]- 🗂️ Wrappers en Collections
> 
> **Por qué son necesarios:**
> 
> ```java
> // ❌ NO FUNCIONA - colecciones solo aceptan objetos
> // ArrayList<int> numeros = new ArrayList<>();  // ❌ Error de compilación
> 
> // ✅ FUNCIONA - usar wrapper
> ArrayList<Integer> numeros = new ArrayList<>();
> ```
> 
> **Uso práctico:**
> 
> ```java
> import java.util.*;
> 
> // ArrayList con Integer
> ArrayList<Integer> numeros = new ArrayList<>();
> numeros.add(10);        // Autoboxing: 10 → Integer(10)
> numeros.add(20);
> numeros.add(30);
> 
> int primero = numeros.get(0);  // Unboxing: Integer(10) → 10
> System.out.println("Primer número: " + primero);
> 
> // HashSet con Double
> HashSet<Double> precios = new HashSet<>();
> precios.add(19.99);     // Autoboxing
> precios.add(25.50);
> precios.add(19.99);     // Duplicado, no se agrega
> 
> System.out.println("Precios únicos: " + precios.size());  // 2
> 
> // HashMap con Integer como clave
> HashMap<Integer, String> estudiantes = new HashMap<>();
> estudiantes.put(1, "Ana");     // Autoboxing en la clave
> estudiantes.put(2, "Luis");
> estudiantes.put(3, "María");
> 
> String nombre = estudiantes.get(2);  // Unboxing automático
> System.out.println("Estudiante 2: " + nombre);
> ```
> 
> **Operaciones con colecciones:**
> 
> ```java
> ArrayList<Integer> lista = new ArrayList<>();
> lista.add(5);
> lista.add(10);
> lista.add(15);
> lista.add(20);
> 
> // Remover por valor (requiere Integer)
> lista.remove(Integer.valueOf(10));  // Remueve el 10
> 
> // ⚠️ Remover por índice
> lista.remove(0);  // Remueve el elemento en posición 0
> 
> // Buscar
> boolean contiene = lista.contains(15);  // true
> 
> // Iterar
> for (Integer num : lista) {
>     System.out.println(num * 2);  // Unboxing automático
> }
> 
> // Convertir a array
> Integer[] array = lista.toArray(new Integer[0]);
> ```
> 
> **Ejemplo completo - contador de frecuencias:**
> 
> ```java
> public static void contarFrecuencias(int[] numeros) {
>     HashMap<Integer, Integer> frecuencias = new HashMap<>();
>     
>     for (int num : numeros) {
>         // getOrDefault evita null
>         Integer count = frecuencias.getOrDefault(num, 0);
>         frecuencias.put(num, count + 1);
>     }
>     
>     // Mostrar resultados
>     for (Map.Entry<Integer, Integer> entry : frecuencias.entrySet()) {
>         System.out.println(entry.getKey() + " aparece " + 
>                          entry.getValue() + " veces");
>     }
> }
> 
> // Uso
> int[] datos = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4};
> contarFrecuencias(datos);
> // Salida:
> // 1 aparece 1 veces
> // 2 aparece 2 veces
> // 3 aparece 3 veces
> // 4 aparece 4 veces
> ```

---

## ⚡ Rendimiento y Consideraciones

### 🎯 Cuándo Usar Primitivos vs Wrappers

> [!warning]- ⚖️ Trade-offs
> 
> **Ventajas y desventajas:**
> 
> |Aspecto|Tipo Primitivo|Clase Wrapper|
> |---|---|---|
> |**Memoria**|✅ Menos (4-8 bytes)|❌ Más (~16 bytes + overhead)|
> |**Velocidad**|✅ Más rápido|⚠️ Más lento (overhead de objetos)|
> |**Null**|❌ No acepta null|✅ Puede ser null|
> |**Colecciones**|❌ No compatible|✅ Compatible|
> |**Métodos**|❌ No tiene|✅ Muchos métodos útiles|
> |**Autoboxing**|N/A|⚠️ Costo de conversión|
> 
> **Impacto en rendimiento:**
> 
> ```java
> // Comparación de memoria
> int primitivo = 10;           // 4 bytes
> Integer wrapper = 10;         // ~16 bytes (objeto) + overhead
> 
> // Operaciones con primitivos (rápido)
> int suma = 0;
> for (int i = 0; i < 1000000; i++) {
>     suma += i;  // Operación directa
> }
> 
> // Operaciones con wrappers (más lento)
> Integer sumaObj = 0;
> for (int i = 0; i < 1000000; i++) {
>     sumaObj += i;  // Unboxing → operación → Autoboxing
> }
> ```
> 
> **Guía de decisión:**
> 
> ```mermaid
> flowchart TD
>     A{¿Para qué lo<br/>necesitas?} --> B[Variables locales<br/>cálculos]
>     A --> C[Colecciones<br/>ArrayList, HashMap]
>     A --> D[Puede ser null]
>     A --> E[Métodos de utilidad<br/>parseInt, etc]
>     
>     B --> F[✅ Usar primitivo<br/>mejor rendimiento]
>     C --> G[✅ Usar Wrapper<br/>única opción]
>     D --> G
>     E --> G
>     
>     style F fill:#e1ffe1
>     style G fill:#fff4e1
> ```
> 
> **Mejores prácticas:**
> 
> ```java
> // ✅ BIEN - primitivos para cálculos
> public double calcularPromedio(int[] calificaciones) {
>     int suma = 0;  // Primitivo
>     for (int cal : calificaciones) {
>         suma += cal;
>     }
>     return (double) suma / calificaciones.length;
> }
> 
> // ✅ BIEN - wrappers en colecciones
> public List<Integer> obtenerCalificacionesAprobadas(int[] todas) {
>     List<Integer> aprobadas = new ArrayList<>();  // Wrapper necesario
>     for (int cal : todas) {
>         if (cal >= 60) {
>             aprobadas.add(cal);  // Autoboxing
>         }
>     }
>     return aprobadas;
> }
> 
> // ✅ BIEN - wrapper cuando puede ser null
> public Integer buscarPorId(int id) {
>     // Retorna Integer (puede ser null si no encuentra)
>     if (encontrado) {
>         return valor;
>     }
>     return null;  // null indica "no encontrado"
> }
> ```

---

## ⚠️ Problemas Comunes y Soluciones

> [!danger]- 🐛 Errores Frecuentes
> 
> **1. NullPointerException con unboxing:**
> 
> ```java
> // ❌ PELIGRO - puede causar NPE
> Integer num = null;
> int valor = num;  // ❌ NullPointerException al hacer unboxing
> 
> // ✅ SOLUCIÓN - verificar null
> Integer num = obtenerValor();  // Puede retornar null
> int valor = (num != null) ? num : 0;  // Valor por defecto si es null
> 
> // ✅ MEJOR - usar método con default
> int valor = Objects.requireNonNullElse(num, 0);
> ```
> 
> **2. Comparación incorrecta:**
> 
> ```java
> // ❌ MAL - comparar con ==
> Integer a = 1000;
> Integer b = 1000;
> if (a == b) {  // false (objetos diferentes)
>     System.out.println("Iguales");
> }
> 
> // ✅ BIEN - usar equals()
> if (a.equals(b)) {  // true (mismo contenido)
>     System.out.println("Iguales");
> }
> ```
> 
> **3. NumberFormatException en parseo:**
> 
> ```java
> // ❌ Sin manejo de errores
> String texto = "abc";
> int numero = Integer.parseInt(texto);  // ❌ NumberFormatException
> 
> // ✅ Con validación
> String texto = obtenerTexto();
> try {
>     int numero = Integer.parseInt(texto);
>     System.out.println("Número: " + numero);
> } catch (NumberFormatException e) {
>     System.out.println("❌ Texto no es un número válido");
> }
> ```
> 
> **4. Uso ineficiente en bucles:**
> 
> ```java
> // ❌ MAL - boxing/unboxing innecesario
> Integer suma = 0;
> for (int i = 0; i < 1000000; i++) {
>     suma += i;  // Unboxing → suma → Autoboxing (lento)
> }
> 
> // ✅ BIEN - usar primitivos
> int suma = 0;
> for (int i = 0; i < 1000000; i++) {
>     suma += i;  // Operación directa (rápido)
> }
> ````
> 
> **5. Modificar wrapper en colección:**
> 
> ```java
> ArrayList<Integer> lista = new ArrayList<>();
> lista.add(10);
> 
> // ❌ NO modifica la lista
> Integer num = lista.get(0);
> num = 20;  // Solo modifica la variable local
> System.out.println(lista.get(0));  // Sigue siendo 10
> 
> // ✅ Modificar correctamente
> lista.set(0, 20);  // Reemplaza el elemento
> System.out.println(lista.get(0));  // Ahora es 20
> ```

---

## 📊 Resumen Visual

```mermaid
mindmap
  root((Clases<br/>Wrapper))
    Propósito
      Encapsular primitivos
      Usar en colecciones
      Aceptar null
      Métodos de utilidad
    Correspondencia
      int → Integer
      double → Double
      char → Character
      boolean → Boolean
    Conversiones
      Autoboxing primitivo → objeto
      Unboxing objeto → primitivo
      parseInt String → primitivo
      valueOf String → Wrapper
    Métodos
      compareTo
      equals
      toString
      MAX_VALUE/MIN_VALUE
      parseXxx
    Consideraciones
      vs comparar con equals
      Verificar null
      Rendimiento primitivos
      Caché -128 a 127
````

> [!quote]- 🎓 Puntos Clave para Recordar
> 
> ✅ **Wrappers = objetos** que envuelven tipos primitivos  
> ✅ **Autoboxing/Unboxing** - conversión automática desde Java 5  
> ✅ **Necesarios en colecciones** - `ArrayList<Integer>`, no `ArrayList<int>`  
> ✅ **Comparar con equals()** - NUNCA con `"=="`  
> ✅ **Pueden ser null** - verificar antes de unboxing  
> ✅ **parseInt() → primitivo** - `Integer.parseInt("123")` → `int`  
> ✅ **valueOf() → Wrapper** - `Integer.valueOf("123")` → `Integer`  
> ✅ **Primitivos para rendimiento** - usar en cálculos intensivos  
> ✅ **Caché de -128 a 127** - `valueOf()` reutiliza objetos

---

**Tags:** #java #wrapper #autoboxing #unboxing #integer #double #character #boolean #colecciones #conversiones #parseo
