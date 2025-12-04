# 📘 Estructura General de un Programa en Java

## 🎯 Introducción

> [!info]- 💡 ¿Qué es un Programa en Java? Un programa en Java es un conjunto de instrucciones escritas siguiendo la sintaxis del lenguaje, que se organizan en **clases** y **métodos**. Java es un lenguaje **orientado a objetos**, lo que significa que todo el código debe estar contenido dentro de clases.
> 
> **Características fundamentales:**
> 
> - **Compilado e interpretado:** El código se compila a bytecode (.class) y se ejecuta en la JVM (Java Virtual Machine)
> - **Fuertemente tipado:** Todas las variables deben declararse con un tipo específico
> - **Case-sensitive:** Distingue entre mayúsculas y minúsculas
> - **Orientado a objetos:** Todo se organiza en clases y objetos

---

## 📦 Estructura Básica de un Programa Java

### 🏗️ Anatomía Mínima

> [!example]- 🔵 Programa Java Más Simple
> 
> ```java
> // 1. Declaración de la clase
> public class MiPrimerPrograma {
>     
>     // 2. Método main (punto de entrada)
>     public static void main(String[] args) {
>         
>         // 3. Instrucciones del programa
>         System.out.println("¡Hola, Mundo!");
>     }
> }
> ```
> 
> **Componentes obligatorios:**
> 
> 1. **Clase principal:** Contenedor de todo el código
> 2. **Método main:** Punto de inicio de ejecución
> 3. **Instrucciones:** Código que se ejecuta
> 
> **Reglas importantes:**
> 
> - El nombre del archivo debe coincidir con el nombre de la clase pública
> - Si la clase se llama `MiPrimerPrograma`, el archivo debe ser `MiPrimerPrograma.java`
> - Solo puede haber **una clase pública** por archivo

### 🔍 Análisis Detallado de Cada Componente

> [!note]- 🎯 Desglose Línea por Línea
> 
> ```java
> public class MiPrimerPrograma {
> //  ↑      ↑          ↑
> //  1      2          3
> ```
> 
> 1. **`public`:** Modificador de acceso (la clase es accesible desde cualquier lugar)
> 2. **`class`:** Palabra clave que indica que estamos declarando una clase
> 3. **`MiPrimerPrograma`:** Nombre de la clase (debe empezar con mayúscula por convención)
> 
> ---
> 
> ```java
> public static void main(String[] args) {
> //  ↑      ↑     ↑    ↑         ↑
> //  1      2     3    4         5
> ```
> 
> 4. **`public`:** El método es accesible desde fuera de la clase
> 5. **`static`:** Se puede llamar sin crear un objeto de la clase
> 6. **`void`:** No retorna ningún valor
> 7. **`main`:** Nombre del método (punto de entrada del programa)
> 8. **`String[] args`:** Parámetro que recibe argumentos de línea de comandos
> 
> ---
> 
> ```java
> System.out.println("¡Hola, Mundo!");
> //  ↑     ↑      ↑           ↑
> //  1     2      3           4
> ```
> 
> 9. **`System`:** Clase del paquete java.lang
> 10. **`out`:** Objeto de salida estándar (consola)
> 11. **`println`:** Método que imprime y agrega un salto de línea
> 12. **`"¡Hola, Mundo!"`:** String (cadena de texto) a imprimir

---

## 🧩 Elementos Fundamentales del Lenguaje

### 1️⃣ Comentarios

> [!tip]- 💬 Tipos de Comentarios en Java
> 
> **Comentario de una línea:**
> 
> ```java
> // Este es un comentario de una sola línea
> int edad = 25; // También puede ir al final de una línea
> ```
> 
> **Comentario de múltiples líneas:**
> 
> ```java
> /* 
>  * Este es un comentario
>  * de múltiples líneas
>  * muy útil para explicaciones largas
>  */
> int suma = a + b;
> ```
> 
> **Comentario de documentación (Javadoc):**
> 
> ```java
> /**
>  * Este método calcula la suma de dos números
>  * @param a primer número
>  * @param b segundo número
>  * @return la suma de a y b
>  */
> public int sumar(int a, int b) {
>     return a + b;
> }
> ```
> 
> **Buenas prácticas:**
> 
> - Usar comentarios para explicar el "por qué", no el "qué"
> - Mantener los comentarios actualizados con el código
> - Evitar comentarios obvios: `// Incrementar i` para `i++;`

### 2️⃣ Identificadores

> [!info]- 🏷️ Reglas para Nombres de Variables, Clases y Métodos
> 
> **Reglas obligatorias:**
> 
> - Pueden contener: letras, dígitos, guión bajo (_) y símbolo de dólar ($)
> - **NO pueden** comenzar con un dígito
> - **NO pueden** ser palabras reservadas de Java
> - Son **case-sensitive:** `miVariable` ≠ `MiVariable`
> 
> **Convenciones (estilo recomendado):**
> 
> |Elemento|Convención|Ejemplo|
> |---|---|---|
> |**Clases**|PascalCase (UpperCamelCase)|`MiClase`, `EstudianteUniversitario`|
> |**Métodos**|camelCase|`calcularPromedio()`, `obtenerNombre()`|
> |**Variables**|camelCase|`nombreCompleto`, `edadEstudiante`|
> |**Constantes**|UPPER_SNAKE_CASE|`PI`, `MAX_INTENTOS`|
> |**Paquetes**|lowercase|`com.miempresa.proyecto`|
> 
> **Ejemplos válidos:**
> 
> ```java
> int edad;              // ✅ Correcto
> String nombre_completo; // ✅ Válido (pero no recomendado)
> double $precio;        // ✅ Válido
> int _contador;         // ✅ Válido
> ```
> 
> **Ejemplos inválidos:**
> 
> ```java
> int 123numero;         // ❌ Error: comienza con dígito
> String class;          // ❌ Error: palabra reservada
> double mi-variable;    // ❌ Error: guión no permitido
> ```

### 3️⃣ Palabras Reservadas

> [!warning]- 🚫 Keywords de Java que NO Puedes Usar como Identificadores
> 
> Java tiene **51 palabras reservadas** que tienen significados especiales:
> 
> **Tipos de datos primitivos:**
> 
> ```
> boolean  byte  char  double  float  int  long  short
> ```
> 
> **Control de flujo:**
> 
> ```
> if  else  switch  case  default  for  while  do  break  continue  return
> ```
> 
> **Modificadores:**
> 
> ```
> public  private  protected  static  final  abstract  synchronized  volatile  transient  native
> ```
> 
> **Orientación a objetos:**
> 
> ```
> class  interface  extends  implements  new  this  super  instanceof
> ```
> 
> **Manejo de excepciones:**
> 
> ```
> try  catch  finally  throw  throws
> ```
> 
> **Otros:**
> 
> ```
> package  import  void  null  true  false  const*  goto*
> ```
> 
> *`const` y `goto` están reservadas pero no se usan

---

## 📊 Tipos de Datos en Java

### 🔢 Tipos Primitivos

> [!success]- 🟢 Los 8 Tipos de Datos Primitivos
> 
> **Tipos enteros:**
> 
> |Tipo|Tamaño|Rango|Ejemplo|
> |---|---|---|---|
> |**byte**|8 bits|-128 a 127|`byte edad = 25;`|
> |**short**|16 bits|-32,768 a 32,767|`short poblacion = 15000;`|
> |**int**|32 bits|-2³¹ a 2³¹-1|`int habitantes = 2800000;`|
> |**long**|64 bits|-2⁶³ a 2⁶³-1|`long distancia = 9460730472580800L;`|
> 
> **Tipos de punto flotante:**
> 
> |Tipo|Tamaño|Precisión|Ejemplo|
> |---|---|---|---|
> |**float**|32 bits|~6-7 dígitos decimales|`float precio = 19.99f;`|
> |**double**|64 bits|~15 dígitos decimales|`double pi = 3.14159265359;`|
> 
> **Tipo carácter:**
> 
> |Tipo|Tamaño|Descripción|Ejemplo|
> |---|---|---|---|
> |**char**|16 bits|Un solo carácter Unicode|`char letra = 'A';`|
> 
> **Tipo booleano:**
> 
> |Tipo|Valores|Descripción|Ejemplo|
> |---|---|---|---|
> |**boolean**|true/false|Valor lógico|`boolean esEstudiante = true;`|
> 
> **Valores por defecto:**
> 
> - Enteros: `0`
> - Flotantes: `0.0`
> - char: `'\u0000'` (carácter nulo)
> - boolean: `false`

### 🎭 Tipos de Referencia

> [!note]- 📦 Objetos y Referencias
> 
> **Diferencia con tipos primitivos:**
> 
> - Los tipos primitivos almacenan **valores** directamente
> - Los tipos de referencia almacenan **direcciones de memoria** (referencias a objetos)
> 
> **Tipos de referencia comunes:**
> 
> **1. Clases (String, Scanner, etc.):**
> 
> ```java
> String nombre = "Juan";
> Scanner scanner = new Scanner(System.in);
> ```
> 
> **2. Arrays (arreglos):**
> 
> ```java
> int[] numeros = {1, 2, 3, 4, 5};
> String[] nombres = new String[10];
> ```
> 
> **3. Interfaces:**
> 
> ```java
> List<String> lista = new ArrayList<>();
> ```
> 
> **4. Enumeraciones:**
> 
> ```java
> enum DiaSemana { LUNES, MARTES, MIERCOLES }
> DiaSemana dia = DiaSemana.LUNES;
> ```
> 
> **Valor por defecto:** `null` (ausencia de referencia)

### 🔄 Conversión de Tipos (Casting)

> [!tip]- 🔀 Conversión Implícita y Explícita
> 
> **Conversión implícita (widening):**
> 
> - Automática cuando no hay pérdida de información
> - De menor a mayor capacidad
> 
> ```java
> int x = 100;
> long y = x;        // ✅ Automático: int → long
> float z = y;       // ✅ Automático: long → float
> double w = z;      // ✅ Automático: float → double
> ```
> 
> **Jerarquía de conversión automática:**
> 
> ```
> byte → short → int → long → float → double
>         char ↗
> ```
> 
> **Conversión explícita (narrowing):**
> 
> - Requiere casting manual
> - De mayor a menor capacidad (puede haber pérdida de datos)
> 
> ```java
> double pi = 3.14159;
> int piEntero = (int) pi;     // piEntero = 3 (se trunca)
> 
> long grande = 1000000L;
> int pequeño = (int) grande;  // ⚠️ Puede perder datos si excede rango
> ```
> 
> **Conversión entre tipos primitivos y String:**
> 
> ```java
> // String → primitivo
> int numero = Integer.parseInt("123");
> double decimal = Double.parseDouble("3.14");
> boolean valor = Boolean.parseBoolean("true");
> 
> // Primitivo → String
> String texto1 = String.valueOf(123);
> String texto2 = "" + 123;  // Concatenación con cadena vacía
> ```

---

## ✍️ Declaración e Inicialización de Variables

### 📝 Sintaxis Básica

> [!example]- 🎯 Formas de Declarar Variables
> 
> **Declaración simple:**
> 
> ```java
> int edad;              // Declarada pero no inicializada
> String nombre;         // Valor por defecto: null
> ```
> 
> **Declaración con inicialización:**
> 
> ```java
> int edad = 25;
> double precio = 99.99;
> boolean activo = true;
> String nombre = "María";
> ```
> 
> **Múltiples declaraciones del mismo tipo:**
> 
> ```java
> int x, y, z;                    // Declaradas sin inicializar
> int a = 1, b = 2, c = 3;       // Declaradas e inicializadas
> int m = 0, n, p = 5;           // Mixto
> ```
> 
> **Variables finales (constantes):**
> 
> ```java
> final double PI = 3.14159;
> final int MAX_INTENTOS = 3;
> // PI = 3.14;  // ❌ Error: no se puede reasignar
> ```
> 
> **Variables con ámbito (scope):**
> 
> ```java
> public class Ejemplo {
>     int variableDeInstancia;        // Ámbito: toda la clase
>     static int variableDeClase;     // Ámbito: compartida entre instancias
>     
>     public void metodo() {
>         int variableLocal = 10;     // Ámbito: solo dentro del método
>     }
> }
> ```

---

## 🔢 Expresiones y Operadores

### ➕ Operadores Aritméticos

> [!success]- 🧮 Operaciones Matemáticas Básicas
> 
> |Operador|Nombre|Ejemplo|Resultado|
> |---|---|---|---|
> |`+`|Suma|`5 + 3`|`8`|
> |`-`|Resta|`5 - 3`|`2`|
> |`*`|Multiplicación|`5 * 3`|`15`|
> |`/`|División|`10 / 3`|`3` (división entera)|
> |`/`|División|`10.0 / 3`|`3.333...` (división real)|
> |`%`|Módulo (residuo)|`10 % 3`|`1`|
> 
> **Operadores de incremento/decremento:**
> 
> ```java
> int x = 5;
> x++;        // Post-incremento: x = 6
> ++x;        // Pre-incremento: x = 7
> x--;        // Post-decremento: x = 6
> --x;        // Pre-decremento: x = 5
> ```
> 
> **Diferencia pre/post:**
> 
> ```java
> int a = 5;
> int b = a++;    // b = 5, a = 6 (primero asigna, luego incrementa)
> 
> int c = 5;
> int d = ++c;    // d = 6, c = 6 (primero incrementa, luego asigna)
> ```
> 
> **Operadores de asignación compuesta:**
> 
> ```java
> int x = 10;
> x += 5;     // Equivalente a: x = x + 5;  → x = 15
> x -= 3;     // Equivalente a: x = x - 3;  → x = 12
> x *= 2;     // Equivalente a: x = x * 2;  → x = 24
> x /= 4;     // Equivalente a: x = x / 4;  → x = 6
> x %= 4;     // Equivalente a: x = x % 4;  → x = 2
> ```

### 🔍 Operadores Relacionales

> [!info]- ⚖️ Comparaciones entre Valores
> 
> |Operador|Significado|Ejemplo|Resultado|
> |---|---|---|---|
> |`==`|Igual a|`5 == 5`|`true`|
> |`!=`|Diferente de|`5 != 3`|`true`|
> |`>`|Mayor que|`5 > 3`|`true`|
> |`<`|Menor que|`5 < 3`|`false`|
> |`>=`|Mayor o igual|`5 >= 5`|`true`|
> |`<=`|Menor o igual|`5 <= 3`|`false`|
> 
> **⚠️ Importante con Strings:**
> 
> ```java
> String s1 = "Hola";
> String s2 = "Hola";
> String s3 = new String("Hola");
> 
> // ❌ NO usar == para comparar Strings
> s1 == s2;           // true (misma referencia en pool)
> s1 == s3;           // false (diferentes referencias)
> 
> // ✅ Usar .equals() para comparar contenido
> s1.equals(s3);      // true (mismo contenido)
> ```

### 🧠 Operadores Lógicos

> [!note]- 🔗 Conectores Lógicos (como en tu nota de referencia)
> 
> |Operador|Símbolo Lógico|Nombre|Ejemplo|
> |---|---|---|---|
> |`!`|¬|NOT (negación)|`!true` = `false`|
> |`&&`|∧|AND (conjunción)|`true && false` = `false`|
> |`\|`|∨|OR (disyunción)|`true \| false` = `true`|
> 
> **Tablas de verdad:**
> 
> ```java
> // AND (&&): verdadero solo si AMBOS son verdaderos
> true  && true   // true
> true  && false  // false
> false && true   // false
> false && false  // false
> 
> // OR (||): verdadero si AL MENOS UNO es verdadero
> true  || true   // true
> true  || false  // true
> false || true   // true
> false || false  // false
> 
> // NOT (!): invierte el valor
> !true           // false
> !false          // true
> ```
> 
> **Evaluación en cortocircuito:**
> 
> ```java
> // Con && si el primero es false, no evalúa el segundo
> boolean resultado1 = false && (10 / 0 > 5);  // No lanza excepción
> 
> // Con || si el primero es true, no evalúa el segundo
> boolean resultado2 = true || (10 / 0 > 5);   // No lanza excepción
> ```
> 
> **Precedencia de operadores lógicos:**
> 
> 1. `!` (NOT) - Mayor precedencia
> 2. `&&` (AND)
> 3. `||` (OR) - Menor precedencia
> 
> ```java
> boolean x = true;
> boolean y = false;
> boolean z = true;
> 
> // Se evalúa como: (!y) && z
> boolean resultado = !y && z;  // true
> 
> // Usar paréntesis para claridad
> boolean resultado2 = !(y && z);  // true
> ```

### 🎯 Precedencia de Operadores

> [!warning]- ⚡ Orden de Evaluación
> 
> **De mayor a menor precedencia:**
> 
> 1. **Paréntesis** `()`
> 2. **Post-incremento/decremento** `x++`, `x--`
> 3. **Pre-incremento/decremento, NOT** `++x`, `--x`, `!`
> 4. **Multiplicación, División, Módulo** `*`, `/`, `%`
> 5. **Suma, Resta** `+`, `-`
> 6. **Relacionales** `<`, `>`, `<=`, `>=`
> 7. **Igualdad** `==`, `!=`
> 8. **AND lógico** `&&`
> 9. **OR lógico** `||`
> 10. **Asignación** `=`, `+=`, `-=`, etc.
> 
> **Ejemplos:**
> 
> ```java
> int resultado = 2 + 3 * 4;        // 14 (no 20)
> int resultado = (2 + 3) * 4;      // 20 (con paréntesis)
> 
> boolean test = 5 > 3 && 10 < 20;  // true
> boolean test2 = 5 > 3 || 10 > 20 && false;  // true (cuidado con precedencia)
> ```

---

## 🔀 Estructuras de Control

### 🛤️ Estructuras Condicionales

> [!example]- 🔵 if, else if, else
> 
> **Sintaxis básica:**
> 
> ```java
> if (condición) {
>     // Código si la condición es verdadera
> }
> ```
> 
> **if-else:**
> 
> ```java
> int edad = 18;
> 
> if (edad >= 18) {
>     System.out.println("Eres mayor de edad");
> } else {
>     System.out.println("Eres menor de edad");
> }
> ```
> 
> **if-else if-else (múltiples condiciones):**
> 
> ```java
> int nota = 85;
> 
> if (nota >= 90) {
>     System.out.println("Excelente");
> } else if (nota >= 80) {
>     System.out.println("Muy bien");
> } else if (nota >= 70) {
>     System.out.println("Bien");
> } else if (nota >= 60) {
>     System.out.println("Aprobado");
> } else {
>     System.out.println("Reprobado");
> }
> ```
> 
> **if anidados:**
> 
> ```java
> int edad = 20;
> boolean tieneCarnet = true;
> 
> if (edad >= 18) {
>     if (tieneCarnet) {
>         System.out.println("Puedes conducir");
>     } else {
>         System.out.println("Necesitas sacar el carnet");
>     }
> } else {
>     System.out.println("Eres muy joven para conducir");
> }
> ```
> 
> **Operador ternario (if compacto):**
> 
> ```java
> int edad = 20;
> String mensaje = (edad >= 18) ? "Mayor de edad" : "Menor de edad";
> 
> // Equivalente a:
> String mensaje;
> if (edad >= 18) {
>     mensaje = "Mayor de edad";
> } else {
>     mensaje = "Menor de edad";
> }
> ```

> [!example]- 🟡 switch-case
> 
> **Sintaxis:**
> 
> ```java
> int dia = 3;
> 
> switch (dia) {
>     case 1:
>         System.out.println("Lunes");
>         break;
>     case 2:
>         System.out.println("Martes");
>         break;
>     case 3:
>         System.out.println("Miércoles");
>         break;
>     case 4:
>         System.out.println("Jueves");
>         break;
>     case 5:
>         System.out.println("Viernes");
>         break;
>     case 6:
>     case 7:
>         System.out.println("Fin de semana");
>         break;
>     default:
>         System.out.println("Día inválido");
> }
> ```
> 
> **⚠️ Importante sobre break:**
> 
> - Si omites `break`, la ejecución "cae" al siguiente caso
> 
> ```java
> int mes = 2;
> int dias;
> 
> switch (mes) {
>     case 1: case 3: case 5: case 7: case 8: case 10: case 12:
>         dias = 31;
>         break;
>     case 4: case 6: case 9: case 11:
>         dias = 30;
>         break;
>     case 2:
>         dias = 28;  // Simplificado (sin considerar año bisiesto)
>         break;
>     default:
>         dias = 0;
>         System.out.println("Mes inválido");
> }
> ```
> 
> **Switch con String (Java 7+):**
> 
> ```java
> String dia = "lunes";
> 
> switch (dia.toLowerCase()) {
>     case "lunes":
>     case "martes":
>     case "miércoles":
>     case "jueves":
>     case "viernes":
>         System.out.println("Día laboral");
>         break;
>     case "sábado":
>     case "domingo":
>         System.out.println("Fin de semana");
>         break;
>     default:
>         System.out.println("Día no reconocido");
> }
> ```

### 🔁 Estructuras de Repetición (Bucles)

> [!success]- 🟢 for (bucle con contador)
> 
> **Sintaxis básica:**
> 
> ```java
> for (inicialización; condición; actualización) {
>     // Código a repetir
> }
> ```
> 
> **Ejemplo simple:**
> 
> ```java
> // Imprimir números del 1 al 10
> for (int i = 1; i <= 10; i++) {
>     System.out.println(i);
> }
> ```
> 
> **Variaciones:**
> 
> ```java
> // Contar hacia atrás
> for (int i = 10; i >= 1; i--) {
>     System.out.println(i);
> }
> 
> // Incrementar de 2 en 2
> for (int i = 0; i < 20; i += 2) {
>     System.out.println(i);  // 0, 2, 4, 6, ...
> }
> 
> // Múltiples variables
> for (int i = 0, j = 10; i < j; i++, j--) {
>     System.out.println("i=" + i + ", j=" + j);
> }
> ```
> 
> **for-each (para arrays y colecciones):**
> 
> ```java
> int[] numeros = {10, 20, 30, 40, 50};
> 
> for (int num : numeros) {
>     System.out.println(num);
> }
> 
> String[] nombres = {"Ana", "Juan", "María"};
> for (String nombre : nombres) {
>     System.out.println("Hola, " + nombre);
> }
> ```

> [!info]- 🔵 while (bucle con condición previa)
> 
> **Sintaxis:**
> 
> ```java
> while (condición) {
>     // Código a repetir
> }
> ```
> 
> **Ejemplo:**
> 
> ```java
> int contador = 1;
> 
> while (contador <= 5) {
>     System.out.println("Contador: " + contador);
>     contador++;
> }
> ```
> 
> **Uso común - entrada de usuario:**
> 
> ```java
> Scanner scanner = new Scanner(System.in);
> String respuesta = "";
> 
> while (!respuesta.equals("salir")) {
>     System.out.print("Escribe 'salir' para terminar: ");
>     respuesta = scanner.nextLine();
> }
> ```
> 
> **⚠️ Cuidado con bucles infinitos:**
> 
> ```java
> // ❌ Bucle infinito (la condición siempre es true)
> while (true) {
>     System.out.println("Esto se repite infinitamente");
> }
> 
> // ✅ Con condición de salida
> while (true) {
>     System.out.print("Continuar (s/n)? ");
>     String resp = scanner.nextLine();
>     if (resp.equals("n")) {
>         break;  // Sale del bucle
>     }
> }
> ```

> [!note]- 🟡 do-while (bucle con condición posterior)
> 
> **Sintaxis:**
> 
> ```java
> do {
>     // Código a repetir
> } while (condición);
> ```
> 
> **Diferencia clave:** Se ejecuta **al menos una vez**, incluso si la condición es falsa
> 
> **Ejemplo:**
> 
> ```java
> Scanner scanner = new Scanner(System.in);
> int numero;
> 
> do {
>     System.out.print("Ingresa un número positivo: ");
>     numero = scanner.nextInt();
> } while (numero <= 0);
> 
> System.out.println("Número válido: " + numero);
> ```
> 
> **Comparación while vs do-while:**
> 
> ```java
> // Con while: podría no ejecutarse nunca
> int x = 10;
> while (x < 5) {
>     System.out.println("Esto NO se imprime");
> }
> 
> // Con do-while: se ejecuta al menos una vez
> int y = 10;
> do {
>     System.out.println("Esto SÍ se imprime una vez");
> } while (y < 5);
> ```

### 🎮 Sentencias de Control de Flujo

> [!tip]- 🚦 break, continue y return
> 
> **1. break - Salir del bucle completamente:**
> 
> ```java
> // Buscar un número en un array
> int[] numeros = {5, 12, 8, 21, 3, 17};
> int objetivo = 21;
> boolean encontrado = false;
> 
> for (int i = 0; i < numeros.length; i++) {
>     if (numeros[i] == objetivo) {
>         System.out.println("Encontrado en posición: " + i);
>         encontrado = true;
>         break;  // Sale del bucle inmediatamente
>     }
> }
> ```
> 
> **2. continue - Saltar a la siguiente iteración:**
> 
> ```java
> // Imprimir solo números pares
> for (int i = 1; i <= 10; i++) {
>     if (i % 2 != 0) {
>         continue;  // Salta los impares
>     }
>     System.out.println(i);  // Solo imprime pares: 2, 4, 6, 8, 10
> }
> ```
> 
> **3. return - Salir del método:**
> 
> ```java
> public static int buscarPosicion(int[] array, int valor) {
>     for (int i = 0; i < array.length; i++) {
>         if (array[i] == valor) {
>             return i;  // Sale del método y retorna el índice
>         }
>     }
>     return -1;  // Retorna -1 si no se encuentra
> }
> ```
> 
> **break etiquetado (para bucles anidados):**
> 
> ```java
> salir:  // Etiqueta
> for (int i = 0; i < 5; i++) {
>     for (int j = 0; j < 5; j++) {
>         if (i * j > 6) {
>             System.out.println("Saliendo en i=" + i + ", j=" + j);
>             break salir;  // Sale de AMBOS bucles
>         }
>     }
> }
> ```
> 
> **Comparación:**
> 
> ```java
> for (int i = 1; i <= 5; i++) {
>     if (i == 3) break;
>     System.out.println(i);
> }
> // Imprime: 1, 2
> 
> for (int i = 1; i <= 5; i++) {
>     if (i == 3) continue;
>     System.out.println(i);
> }
> // Imprime: 1, 2, 4, 5
> ```

---

## 📥 Entrada y Salida Básica

### 🖨️ Salida de Datos (Output)

> [!example]- 💬 Imprimir en Consola
> 
> **System.out.println() - Con salto de línea:**
> 
> ```java
> System.out.println("Hola, Mundo!");
> System.out.println("Esta es otra línea");
> // Salida:
> // Hola, Mundo!
> // Esta es otra línea
> ```
> 
> **System.out.print() - Sin salto de línea:**
> 
> ```java
> System.out.print("Hola ");
> System.out.print("Mundo");
> System.out.println("!");
> // Salida: Hola Mundo!
> ```
> 
> **Concatenación de valores:**
> 
> ```java
> String nombre = "Ana";
> int edad = 22;
> 
> System.out.println("Nombre: " + nombre);
> System.out.println("Edad: " + edad);
> System.out.println(nombre + " tiene " + edad + " años");
> ```
> 
> **System.out.printf() - Formato con especificadores:**
> 
> ```java
> String nombre = "Carlos";
> int edad = 25;
> double promedio = 8.75;
> 
> // Formato: %s=String, %d=entero, %f=decimal
> System.out.printf("Nombre: %s, Edad: %d, Promedio: %.2f\n", 
>                   nombre, edad, promedio);
> // Salida: Nombre: Carlos, Edad: 25, Promedio: 8.75
> ```
> 
> **Especificadores de formato comunes:**
> 
> |Especificador|Tipo|Ejemplo|
> |---|---|---|
> |`%s`|String|`System.out.printf("%s", "texto");`|
> |`%d`|Entero|`System.out.printf("%d", 42);`|
> |`%f`|Decimal|`System.out.printf("%.2f", 3.14159);`|
> |`%c`|Carácter|`System.out.printf("%c", 'A');`|
> |`%b`|Boolean|`System.out.printf("%b", true);`|
> |`%n`|Salto de línea|`System.out.printf("Línea 1%nLínea 2");`|
> 
> **Formato avanzado:**
> 
> ```java
> int numero = 42;
> System.out.printf("Decimal: %d\n", numero);      // 42
> System.out.printf("Con espacios: %5d\n", numero); // "   42"
> System.out.printf("Con ceros: %05d\n", numero);   // "00042"
> 
> double pi = 3.14159265;
> System.out.printf("2 decimales: %.2f\n", pi);     // 3.14
> System.out.printf("4 decimales: %.4f\n", pi);     // 3.1416
> ```

### ⌨️ Entrada de Datos (Input)

> [!success]- 📥 Lectura desde Teclado con Scanner
> 
> **Importar y crear Scanner:**
> 
> ```java
> import java.util.Scanner;
> 
> public class EjemploScanner {
>     public static void main(String[] args) {
>         Scanner scanner = new Scanner(System.in);
>         
>         // ... usar scanner ...
>         
>         scanner.close();  // Cerrar cuando termine
>     }
> }
> ```
> 
> **Métodos principales de Scanner:**
> 
> |Método|Descripción|Ejemplo|
> |---|---|---|
> |`nextLine()`|Lee línea completa (String)|`String nombre = scanner.nextLine();`|
> |`next()`|Lee una palabra (hasta espacio)|`String palabra = scanner.next();`|
> |`nextInt()`|Lee un entero|`int edad = scanner.nextInt();`|
> |`nextDouble()`|Lee un decimal|`double precio = scanner.nextDouble();`|
> |`nextBoolean()`|Lee un booleano|`boolean activo = scanner.nextBoolean();`|
> |`nextByte()`|Lee un byte|`byte valor = scanner.nextByte();`|
> |`nextShort()`|Lee un short|`short num = scanner.nextShort();`|
> |`nextLong()`|Lee un long|`long grande = scanner.nextLong();`|
> |`nextFloat()`|Lee un float|`float decimal = scanner.nextFloat();`|
> 
> **Ejemplo básico:**
> 
> ```java
> Scanner scanner = new Scanner(System.in);
> 
> System.out.print("Ingresa tu nombre: ");
> String nombre = scanner.nextLine();
> 
> System.out.print("Ingresa tu edad: ");
> int edad = scanner.nextInt();
> 
> System.out.println("Hola " + nombre + ", tienes " + edad + " años");
> scanner.close();
> ```
> 
> **⚠️ Problema común con nextLine() después de otros métodos:**
> 
> ```java
> Scanner scanner = new Scanner(System.in);
> 
> System.out.print("Edad: ");
> int edad = scanner.nextInt();  // Lee el número pero deja el \n
> 
> scanner.nextLine();  // ✅ Consumir el salto de línea residual
> 
> System.out.print("Nombre: ");
> String nombre = scanner.nextLine();  // Ahora funciona correctamente
> ```
> 
> **Validación de entrada:**
> 
> ```java
> Scanner scanner = new Scanner(System.in);
> int numero = 0;
> boolean entradaValida = false;
> 
> while (!entradaValida) {
>     System.out.print("Ingresa un número entero: ");
>     
>     if (scanner.hasNextInt()) {
>         numero = scanner.nextInt();
>         entradaValida = true;
>     } else {
>         System.out.println("Error: debes ingresar un número entero");
>         scanner.next();  // Limpiar entrada inválida
>     }
> }
> 
> System.out.println("Número ingresado: " + numero);
> scanner.close();
> ```
> 
> **Métodos de verificación:**
> 
> ```java
> Scanner scanner = new Scanner(System.in);
> 
> if (scanner.hasNextInt()) {
>     int num = scanner.nextInt();
> }
> 
> if (scanner.hasNextDouble()) {
>     double decimal = scanner.nextDouble();
> }
> 
> if (scanner.hasNextLine()) {
>     String linea = scanner.nextLine();
> }
> ```

---

## 🎨 Ejemplos Completos de Programas

> [!example]- 🟢 Programa 1: Calculadora Básica
> 
> ```java
> import java.util.Scanner;
> 
> public class CalculadoraBasica {
>     public static void main(String[] args) {
>         Scanner scanner = new Scanner(System.in);
>         
>         System.out.println("=== CALCULADORA BÁSICA ===");
>         
>         // Entrada de datos
>         System.out.print("Ingresa el primer número: ");
>         double num1 = scanner.nextDouble();
>         
>         System.out.print("Ingresa el segundo número: ");
>         double num2 = scanner.nextDouble();
>         
>         System.out.print("Operación (+, -, *, /): ");
>         char operacion = scanner.next().charAt(0);
>         
>         // Procesamiento
>         double resultado = 0;
>         boolean operacionValida = true;
>         
>         switch (operacion) {
>             case '+':
>                 resultado = num1 + num2;
>                 break;
>             case '-':
>                 resultado = num1 - num2;
>                 break;
>             case '*':
>                 resultado = num1 * num2;
>                 break;
>             case '/':
>                 if (num2 != 0) {
>                     resultado = num1 / num2;
>                 } else {
>                     System.out.println("Error: División por cero");
>                     operacionValida = false;
>                 }
>                 break;
>             default:
>                 System.out.println("Operación no válida");
>                 operacionValida = false;
>         }
>         
>         // Salida
>         if (operacionValida) {
>             System.out.printf("Resultado: %.2f %c %.2f = %.2f\n", 
>                              num1, operacion, num2, resultado);
>         }
>         
>         scanner.close();
>     }
> }
> ```

> [!example]- 🟡 Programa 2: Promedio de Calificaciones
> 
> ```java
> import java.util.Scanner;
> 
> public class PromedioCalificaciones {
>     public static void main(String[] args) {
>         Scanner scanner = new Scanner(System.in);
>         
>         System.out.println("=== CÁLCULO DE PROMEDIO ===");
>         
>         // Solicitar cantidad de materias
>         System.out.print("¿Cuántas materias tienes? ");
>         int numMaterias = scanner.nextInt();
>         scanner.nextLine(); // Consumir salto de línea
>         
>         // Variables acumuladoras
>         double sumaNotas = 0;
>         int aprobadas = 0;
>         int reprobadas = 0;
>         
>         // Leer calificaciones
>         for (int i = 1; i <= numMaterias; i++) {
>             System.out.print("Nombre de la materia " + i + ": ");
>             String materia = scanner.nextLine();
>             
>             System.out.print("Calificación (0-10): ");
>             double nota = scanner.nextDouble();
>             scanner.nextLine(); // Consumir salto de línea
>             
>             // Validar nota
>             while (nota < 0 || nota > 10) {
>                 System.out.print("Error. Ingresa nota entre 0 y 10: ");
>                 nota = scanner.nextDouble();
>                 scanner.nextLine();
>             }
>             
>             // Acumular
>             sumaNotas += nota;
>             
>             // Clasificar
>             if (nota >= 7.0) {
>                 aprobadas++;
>                 System.out.println("  ✓ Aprobada");
>             } else {
>                 reprobadas++;
>                 System.out.println("  ✗ Reprobada");
>             }
>         }
>         
>         // Calcular promedio
>         double promedio = sumaNotas / numMaterias;
>         
>         // Mostrar resultados
>         System.out.println("\n=== RESULTADOS ===");
>         System.out.printf("Promedio general: %.2f\n", promedio);
>         System.out.println("Materias aprobadas: " + aprobadas);
>         System.out.println("Materias reprobadas: " + reprobadas);
>         
>         // Mensaje final
>         if (promedio >= 7.0) {
>             System.out.println("¡Felicidades! Aprobaste el semestre");
>         } else {
>             System.out.println("Debes esforzarte más el próximo semestre");
>         }
>         
>         scanner.close();
>     }
> }
> ```

> [!example]- 🔵 Programa 3: Adivina el Número
> 
> ```java
> import java.util.Scanner;
> import java.util.Random;
> 
> public class AdivinaNumero {
>     public static void main(String[] args) {
>         Scanner scanner = new Scanner(System.in);
>         Random random = new Random();
>         
>         // Generar número aleatorio entre 1 y 100
>         int numeroSecreto = random.nextInt(100) + 1;
>         int intentos = 0;
>         int maxIntentos = 10;
>         boolean adivinado = false;
>         
>         System.out.println("=== ADIVINA EL NÚMERO ===");
>         System.out.println("He pensado un número entre 1 y 100");
>         System.out.println("Tienes " + maxIntentos + " intentos");
>         
>         while (intentos < maxIntentos && !adivinado) {
>             intentos++;
>             System.out.print("\nIntento " + intentos + ": ");
>             
>             // Validar entrada
>             while (!scanner.hasNextInt()) {
>                 System.out.print("Por favor ingresa un número: ");
>                 scanner.next();
>             }
>             
>             int intento = scanner.nextInt();
>             
>             // Verificar
>             if (intento == numeroSecreto) {
>                 adivinado = true;
>                 System.out.println("¡FELICIDADES! Adivinaste en " + 
>                                  intentos + " intentos");
>             } else if (intento < numeroSecreto) {
>                 System.out.println("Muy bajo. Intenta con un número mayor");
>             } else {
>                 System.out.println("Muy alto. Intenta con un número menor");
>             }
>             
>             // Mostrar pistas adicionales
>             if (!adivinado && intentos < maxIntentos) {
>                 int diferencia = Math.abs(numeroSecreto - intento);
>                 if (diferencia <= 5) {
>                     System.out.println("¡Caliente! Estás muy cerca");
>                 } else if (diferencia <= 15) {
>                     System.out.println("Tibio, te estás acercando");
>                 } else {
>                     System.out.println("Frío, estás lejos");
>                 }
>             }
>         }
>         
>         // Mensaje final si no adivinó
>         if (!adivinado) {
>             System.out.println("\n¡Se acabaron los intentos!");
>             System.out.println("El número era: " + numeroSecreto);
>         }
>         
>         scanner.close();
>     }
> }
> ```

> [!example]- 🟣 Programa 4: Tabla de Multiplicar
> 
> ```java
> import java.util.Scanner;
> 
> public class TablaMultiplicar {
>     public static void main(String[] args) {
>         Scanner scanner = new Scanner(System.in);
>         String continuar;
>         
>         do {
>             System.out.println("\n=== TABLA DE MULTIPLICAR ===");
>             System.out.print("¿Qué tabla quieres ver? (1-12): ");
>             int numero = scanner.nextInt();
>             
>             System.out.print("¿Hasta qué número? (1-20): ");
>             int limite = scanner.nextInt();
>             scanner.nextLine(); // Consumir salto de línea
>             
>             System.out.println("\nTabla del " + numero + ":");
>             System.out.println("─".repeat(25));
>             
>             for (int i = 1; i <= limite; i++) {
>                 int resultado = numero * i;
>                 System.out.printf("%2d × %2d = %3d\n", numero, i, resultado);
>             }
>             
>             System.out.println("─".repeat(25));
>             
>             System.out.print("\n¿Otra tabla? (s/n): ");
>             continuar = scanner.nextLine().toLowerCase();
>             
>         } while (continuar.equals("s") || continuar.equals("si"));
>         
>         System.out.println("¡Hasta luego!");
>         scanner.close();
>     }
> }
> ```

---

## 🎯 Mejores Prácticas y Convenciones

> [!tip]- ✅ Recomendaciones de Estilo
> 
> **1. Nomenclatura:**
> 
> ```java
> // ✅ CORRECTO
> public class EstudianteUniversitario { }
> int edadEstudiante = 20;
> final double PI = 3.14159;
> public void calcularPromedio() { }
> 
> // ❌ INCORRECTO
> public class estudianteuniversitario { }
> int Edad_Estudiante = 20;
> final double pi = 3.14159;
> public void CalcularPromedio() { }
> ```
> 
> **2. Indentación y espaciado:**
> 
> ```java
> // ✅ CORRECTO
> public class Ejemplo {
>     public void metodo() {
>         if (condicion) {
>             // código indentado
>             for (int i = 0; i < 10; i++) {
>                 System.out.println(i);
>             }
>         }
>     }
> }
> 
> // ❌ INCORRECTO (difícil de leer)
> public class Ejemplo{
> public void metodo(){
> if(condicion){
> for(int i=0;i<10;i++){
> System.out.println(i);}}}
> }
> ```
> 
> **3. Comentarios útiles:**
> 
> ```java
> // ✅ CORRECTO - Explica el "por qué"
> // Validamos que el divisor no sea cero para evitar excepción
> if (divisor != 0) {
>     resultado = dividendo / divisor;
> }
> 
> // ❌ INCORRECTO - Comenta lo obvio
> // Incrementar i en 1
> i++;
> ```
> 
> **4. Constantes en lugar de números mágicos:**
> 
> ```java
> // ✅ CORRECTO
> final int EDAD_MINIMA_CONDUCIR = 18;
> final double IVA = 0.12;
> 
> if (edad >= EDAD_MINIMA_CONDUCIR) {
>     // ...
> }
> 
> // ❌ INCORRECTO
> if (edad >= 18) {  // ¿Por qué 18?
>     // ...
> }
> ```
> 
> **5. Una responsabilidad por método:**
> 
> ```java
> // ✅ CORRECTO - Métodos específicos
> public void validarEntrada() { }
> public void calcularResultado() { }
> public void mostrarResultado() { }
> 
> // ❌ INCORRECTO - Método que hace demasiado
> public void hacerTodo() {
>     // validar
>     // calcular
>     // mostrar
>     // guardar
>     // etc.
> }
> ```

---

## 🐛 Errores Comunes y Cómo Evitarlos

> [!warning]- ⚠️ Problemas Frecuentes para Principiantes
> 
> **1. Error: variable not initialized**
> 
> ```java
> // ❌ ERROR
> int x;
> System.out.println(x);  // Variable no inicializada
> 
> // ✅ CORRECTO
> int x = 0;
> System.out.println(x);
> ```
> 
> **2. Error: = vs ==**
> 
> ```java
> // ❌ ERROR - Asignación en lugar de comparación
> if (x = 5) {  // Error de compilación
>     System.out.println("Es 5");
> }
> 
> // ✅ CORRECTO
> if (x == 5) {
>     System.out.println("Es 5");
> }
> ```
> 
> **3. Error: división entera trunca decimales**
> 
> ```java
> // ❌ PROBLEMA
> int a = 5;
> int b = 2;
> double resultado = a / b;  // resultado = 2.0 (no 2.5)
> 
> // ✅ CORRECTO
> double resultado = (double) a / b;  // resultado = 2.5
> // o
> double resultado = a / (double) b;
> // o
> double resultado = a * 1.0 / b;
> ```
> 
> **4. Error: comparar Strings con ==**
> 
> ```java
> String s1 = "Hola";
> String s2 = new String("Hola");
> 
> // ❌ INCORRECTO - Compara referencias
> if (s1 == s2) {  // false
>     System.out.println("Iguales");
> }
> 
> // ✅ CORRECTO - Compara contenido
> if (s1.equals(s2)) {  // true
>     System.out.println("Iguales");
> }
> ```
> 
> **5. Error: olvidar break en switch**
> 
> ```java
> // ❌ PROBLEMA - Fall-through no intencional
> switch (dia) {
>     case 1:
>         System.out.println("Lunes");
>     case 2:
>         System.out.println("Martes");  // Se ejecuta también
> }
> 
> // ✅ CORRECTO
> switch (dia) {
>     case 1:
>         System.out.println("Lunes");
>         break;
>     case 2:
>         System.out.println("Martes");
>         break;
> }
> ```
> 
> **6. Error: ArrayIndexOutOfBoundsException**
> 
> ```java
> int[] numeros = {1, 2, 3, 4, 5};
> 
> // ❌ ERROR - Índice fuera de rango
> System.out.println(numeros[5]);  // Excepción (último índice es 4)
> 
> // ✅ CORRECTO
> System.out.println(numeros[4]);  // Último elemento
> ```
> 
> **7. Error: Scanner y nextLine()**
> 
> ```java
> Scanner sc = new Scanner(System.in);
> 
> // ❌ PROBLEMA
> int edad = sc.nextInt();
> String nombre = sc.nextLine();  // Lee línea vacía
> 
> // ✅ CORRECTO
> int edad = sc.nextInt();
> sc.nextLine();  // Consumir el \n residual
> String nombre = sc.nextLine();  // Ahora funciona bien
> ```

---

## 📚 Resumen Visual

```mermaid
graph TB
    A[Programa Java] --> B[Estructura Básica]
    A --> C[Tipos de Datos]
    A --> D[Expresiones]
    A --> E[Control de Flujo]
    
    B --> B1[Clase]
    B --> B2[Método main]
    B --> B3[Instrucciones]
    
    C --> C1[Primitivos]
    C --> C2[Referencia]
    C1 --> C1A[int, double, boolean, char]
    C2 --> C2A[String, Arrays, Objetos]
    
    D --> D1[Aritméticos]
    D --> D2[Relacionales]
    D --> D3[Lógicos]
    D1 --> D1A[+, -, *, /, %]
    D2 --> D2A[==, !=, <, >, <=, >=]
    D3 --> D3A[&&, ||, !]
    
    E --> E1[Condicionales]
    E --> E2[Bucles]
    E1 --> E1A[if/else, switch]
    E2 --> E2A[for, while, do-while]
    
    style A fill:#e3f2fd
    style B fill:#c8e6c9
    style C fill:#fff9c4
    style D fill:#ffccbc
    style E fill:#e1bee7
```

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica Guiada
> 
> **Nivel Básico:**
> 
> 1. **Calculadora de IMC:** Programa que calcule el Índice de Masa Corporal
> 2. **Conversor de temperatura:** Celsius ↔ Fahrenheit
> 3. **Verificador de números:** Par/impar, positivo/negativo
> 4. **Año bisiesto:** Determinar si un año es bisiesto
> 5. **Mayor de tres números:** Encontrar el mayor de 3 números ingresados
> 
> **Nivel Intermedio:**
> 
> 6. **Cajero automático:** Simular operaciones básicas (consulta, retiro, depósito)
> 7. **Factorial:** Calcular n! usando bucles
> 8. **Serie Fibonacci:** Generar los primeros n términos
> 9. **Números primos:** Verificar si un número es primo
> 10. **Suma de dígitos:** Sumar los dígitos de un número entero
> 
> **Nivel Avanzado:**
> 
> 11. **Menú interactivo:** Sistema con múltiples opciones
> 12. **Juego de Piedra/Papel/Tijera:** Contra la computadora
> 13. **Calculadora científica:** Incluir potencias, raíces, etc.
> 14. **Generador de patrones:** Triángulos, pirámides con asteriscos
> 15. **Sistema de notas:** Con validación, estadísticas y clasificación

---

## 🔗 Conexiones con Temas Siguientes

> [!quote]- 🌐 ¿Qué Sigue Después?
> 
> **Este tema es prerequisito para:**
> 
> - **[[Clases y Objetos]]** - Definir tus propios tipos de datos
> - **[[Métodos y Parámetros]]** - Modularizar el código
> - **[[Constructores]]** - Inicializar objetos
> - **[[Encapsulamiento]]** - Proteger datos con modificadores de acceso
> - **[[Modificador Static]]** - Variables y métodos de clase
> - **[[Arrays y Colecciones]]** - Estructuras de datos
> - **[[Herencia]]** - Reutilización de código
> - **[[Polimorfismo]]** - Flexibilidad en el diseño
> 
> **Fundamentos que ya dominas:**
> 
> - ✅ Sintaxis básica de Java
> - ✅ Tipos de datos y variables
> - ✅ Operadores y expresiones
> - ✅ Estructuras de control
> - ✅ Entrada/salida básica
> 
> **Próximo paso recomendado:** [[Definición de Clases]]

---

**Tags:** #java #programacion #estructura-programa #tipos-datos #operadores #control-flujo #entrada-salida #poo #fundamentos #university #programming-basics