# 📘 Métodos en Java y Comportamiento de un Objeto

## 🎯 Introducción

> [!info]- 💡 ¿Qué son los Métodos? Los **métodos** son bloques de código que definen el **comportamiento** de un objeto. Representan las **acciones** que un objeto puede realizar o las operaciones que se pueden ejecutar sobre él.
> 
> **Conceptos fundamentales:**
> 
> - **Método = Acción/Verbo:** Los métodos representan lo que un objeto _hace_
> - **Encapsulan funcionalidad:** Agrupan código relacionado en unidades reutilizables
> - **Modularización:** Dividen programas complejos en partes manejables
> - **Reutilización:** Un método se escribe una vez y se usa múltiples veces

---

## 🏗️ Anatomía de un Método

### 📋 Estructura Básica

> [!example]- 🔵 Componentes de un Método
> 
> ```java
> modificadorAcceso modificador tipoRetorno nombreMetodo(parametros) {
>     // Cuerpo del método
>     return valor; // Si no es void
> }
> ```
> 
> **Ejemplo detallado:**
> 
> ```java
> public static double calcularPromedio(double a, double b) {
> //  ①     ②      ③           ④              ⑤
>     double suma = a + b;
>     double promedio = suma / 2;
>     return promedio;  // ⑥
> }
> ```
> 
> **Desglose:**
> 
> 1. **Modificador de acceso** (`public`): Quién puede usar el método
> 2. **Modificador** (`static`): Método de clase vs instancia
> 3. **Tipo de retorno** (`double`): Qué devuelve el método
> 4. **Nombre** (`calcularPromedio`): Identificador del método (camelCase)
> 5. **Parámetros** (`double a, double b`): Datos de entrada
> 6. **return**: Devuelve el resultado

---

## 🎨 Tipos de Métodos

### 1️⃣ Métodos sin Retorno (void)

> [!success]- 🟢 Métodos que Realizan Acciones
> 
> **Sintaxis:**
> 
> ```java
> public void nombreMetodo(parametros) {
>     // Código que ejecuta acción
>     // NO tiene return (o return vacío)
> }
> ```
> 
> **Ejemplos:**
> 
> ```java
> // Imprimir saludo
> public void saludar(String nombre) {
>     System.out.println("¡Hola, " + nombre + "!");
> }
> 
> // Mostrar información
> public void mostrarDatos() {
>     System.out.println("Nombre: " + this.nombre);
>     System.out.println("Edad: " + this.edad);
> }
> 
> // Modificar estado
> public void incrementarContador() {
>     this.contador++;
> }
> 
> // Llamadas:
> saludar("Ana");           // Imprime: ¡Hola, Ana!
> mostrarDatos();           // Muestra información
> incrementarContador();    // No devuelve nada
> ```

### 2️⃣ Métodos con Retorno

> [!info]- 🔵 Métodos que Devuelven Valores
> 
> **Sintaxis:**
> 
> ```java
> public tipoRetorno nombreMetodo(parametros) {
>     // Procesamiento
>     return valorDelTipoRetorno;
> }
> ```
> 
> **Ejemplos por tipo:**
> 
> ```java
> // Retorna int
> public int sumar(int a, int b) {
>     return a + b;
> }
> 
> // Retorna boolean
> public boolean esMayorDeEdad(int edad) {
>     return edad >= 18;
> }
> 
> // Retorna String
> public String obtenerNombreCompleto() {
>     return this.nombre + " " + this.apellido;
> }
> 
> // Retorna double
> public double calcularArea(double radio) {
>     return Math.PI * radio * radio;
> }
> 
> // Retorna objeto
> public Estudiante crearEstudiante(String nombre, int edad) {
>     return new Estudiante(nombre, edad);
> }
> 
> // Uso:
> int resultado = sumar(5, 3);              // resultado = 8
> boolean adulto = esMayorDeEdad(20);       // adulto = true
> String nombre = obtenerNombreCompleto();  // nombre = "Juan Pérez"
> ```

### 3️⃣ Métodos con Parámetros

> [!note]- 🟡 Entrada de Datos
> 
> **Sin parámetros:**
> 
> ```java
> public void saludar() {
>     System.out.println("¡Hola!");
> }
> ```
> 
> **Un parámetro:**
> 
> ```java
> public void saludar(String nombre) {
>     System.out.println("¡Hola, " + nombre + "!");
> }
> ```
> 
> **Múltiples parámetros:**
> 
> ```java
> public double calcularPromedio(double nota1, double nota2, double nota3) {
>     return (nota1 + nota2 + nota3) / 3;
> }
> ```
> 
> **Parámetros de diferentes tipos:**
> 
> ```java
> public void registrarEstudiante(String nombre, int edad, double promedio) {
>     System.out.println("Nombre: " + nombre);
>     System.out.println("Edad: " + edad);
>     System.out.println("Promedio: " + promedio);
> }
> ```
> 
> **⚠️ Importante:**
> 
> - Los parámetros son **variables locales** del método
> - Se pasan **por valor** (primitivos) o **por referencia** (objetos)
> - El orden importa: `metodo(5, "Hola")` ≠ `metodo("Hola", 5)`

---

## 🔄 Métodos Static vs Métodos de Instancia

### ⚡ Métodos Static

> [!tip]- 🔷 Métodos de Clase
> 
> **Características:**
> 
> - Pertenecen a la **clase**, no a objetos individuales
> - Se llaman con el **nombre de la clase**: `NombreClase.metodo()`
> - **NO** pueden acceder a variables de instancia directamente
> - **NO** pueden usar `this`
> 
> **Ejemplo:**
> 
> ```java
> public class Calculadora {
>     
>     // Método static
>     public static int sumar(int a, int b) {
>         return a + b;
>     }
>     
>     public static double areaCirculo(double radio) {
>         return Math.PI * radio * radio;
>     }
> }
> 
> // Uso (sin crear objeto):
> int resultado = Calculadora.sumar(5, 3);
> double area = Calculadora.areaCirculo(5.0);
> ```
> 
> **Cuándo usar static:**
> 
> - Métodos utilitarios que no dependen de estado del objeto
> - Funciones matemáticas
> - Métodos auxiliares generales

### 👤 Métodos de Instancia

> [!success]- 🔶 Métodos de Objeto
> 
> **Características:**
> 
> - Pertenecen a **cada objeto** de la clase
> - Se llaman con una **instancia**: `objeto.metodo()`
> - **SÍ** pueden acceder a variables de instancia
> - **SÍ** pueden usar `this`
> 
> **Ejemplo:**
> 
> ```java
> public class Estudiante {
>     // Variables de instancia
>     private String nombre;
>     private double[] notas;
>     
>     // Métodos de instancia
>     public double calcularPromedio() {
>         double suma = 0;
>         for (double nota : notas) {
>             suma += nota;
>         }
>         return suma / notas.length;
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("Nombre: " + this.nombre);
>         System.out.println("Promedio: " + this.calcularPromedio());
>     }
> }
> 
> // Uso (requiere objeto):
> Estudiante estudiante = new Estudiante("Ana", new double[]{8.5, 9.0, 7.5});
> double promedio = estudiante.calcularPromedio();
> estudiante.mostrarInfo();
> ```

---

## 📦 Getters y Setters (Accesores y Mutadores)

### 🔓 Métodos Getter

> [!example]- 📖 Obtener Valores (Accesores)
> 
> **Propósito:** Leer el valor de atributos privados
> 
> **Convención de nombres:** `getTipoAtributo()` o `isAtributo()` para boolean
> 
> ```java
> public class Persona {
>     private String nombre;
>     private int edad;
>     private boolean activo;
>     
>     // Getter para String
>     public String getNombre() {
>         return this.nombre;
>     }
>     
>     // Getter para int
>     public int getEdad() {
>         return this.edad;
>     }
>     
>     // Getter para boolean (is en lugar de get)
>     public boolean isActivo() {
>         return this.activo;
>     }
> }
> 
> // Uso:
> Persona persona = new Persona();
> String nombre = persona.getNombre();
> int edad = persona.getEdad();
> boolean activo = persona.isActivo();
> ```

### 🔒 Métodos Setter

> [!example]- ✏️ Modificar Valores (Mutadores)
> 
> **Propósito:** Modificar el valor de atributos privados (con validación)
> 
> **Convención de nombres:** `setAtributo(tipo valor)`
> 
> ```java
> public class Persona {
>     private String nombre;
>     private int edad;
>     private double salario;
>     
>     // Setter simple
>     public void setNombre(String nombre) {
>         this.nombre = nombre;
>     }
>     
>     // Setter con validación
>     public void setEdad(int edad) {
>         if (edad >= 0 && edad <= 120) {
>             this.edad = edad;
>         } else {
>             System.out.println("Edad inválida");
>         }
>     }
>     
>     // Setter con lógica adicional
>     public void setSalario(double salario) {
>         if (salario >= 0) {
>             this.salario = salario;
>         }
>     }
> }
> 
> // Uso:
> Persona persona = new Persona();
> persona.setNombre("Juan");
> persona.setEdad(25);
> persona.setSalario(2500.0);
> ```

---

## 🎯 Sobrecarga de Métodos (Overloading)

> [!note]- 🔄 Múltiples Versiones del Mismo Método
> 
> **Definición:** Varios métodos con el **mismo nombre** pero **diferentes parámetros**
> 
> **Reglas:**
> 
> - Mismo nombre
> - Diferente número de parámetros, O
> - Diferente tipo de parámetros, O
> - Diferente orden de parámetros
> 
> **Ejemplos:**
> 
> ```java
> public class Calculadora {
>     
>     // Sumar dos enteros
>     public int sumar(int a, int b) {
>         return a + b;
>     }
>     
>     // Sumar tres enteros
>     public int sumar(int a, int b, int c) {
>         return a + b + c;
>     }
>     
>     // Sumar dos decimales
>     public double sumar(double a, double b) {
>         return a + b;
>     }
>     
>     // Sumar un entero y un decimal
>     public double sumar(int a, double b) {
>         return a + b;
>     }
> }
> 
> // Uso - Java elige automáticamente:
> Calculadora calc = new Calculadora();
> int r1 = calc.sumar(5, 3);           // Usa versión (int, int)
> int r2 = calc.sumar(5, 3, 2);        // Usa versión (int, int, int)
> double r3 = calc.sumar(5.5, 3.2);    // Usa versión (double, double)
> double r4 = calc.sumar(5, 3.2);      // Usa versión (int, double)
> ```
> 
> **Ejemplo práctico - Constructor:**
> 
> ```java
> public class Estudiante {
>     private String nombre;
>     private int edad;
>     private double promedio;
>     
>     // Constructor sin parámetros
>     public Estudiante() {
>         this.nombre = "Sin nombre";
>         this.edad = 0;
>         this.promedio = 0.0;
>     }
>     
>     // Constructor con nombre
>     public Estudiante(String nombre) {
>         this.nombre = nombre;
>         this.edad = 0;
>         this.promedio = 0.0;
>     }
>     
>     // Constructor completo
>     public Estudiante(String nombre, int edad, double promedio) {
>         this.nombre = nombre;
>         this.edad = edad;
>         this.promedio = promedio;
>     }
> }
> 
> // Uso:
> Estudiante e1 = new Estudiante();
> Estudiante e2 = new Estudiante("Ana");
> Estudiante e3 = new Estudiante("Carlos", 20, 8.5);
> ```

---

## 🎭 Comportamiento de un Objeto

> [!info]- 🎬 Los Métodos Definen lo que un Objeto HACE
> 
> **Analogía:** Si una clase es un "plano" y un objeto es una "casa construida":
> 
> - **Atributos** = Características (color, tamaño, número de habitaciones)
> - **Métodos** = Acciones (abrir puerta, encender luces, cerrar ventanas)
> 
> **Ejemplo completo:**
> 
> ```java
> public class CuentaBancaria {
>     // ATRIBUTOS (Estado)
>     private String titular;
>     private double saldo;
>     private String numeroCuenta;
>     
>     // Constructor
>     public CuentaBancaria(String titular, String numeroCuenta) {
>         this.titular = titular;
>         this.numeroCuenta = numeroCuenta;
>         this.saldo = 0.0;
>     }
>     
>     // MÉTODOS (Comportamiento)
>     
>     // Comportamiento: Depositar dinero
>     public void depositar(double monto) {
>         if (monto > 0) {
>             this.saldo += monto;
>             System.out.println("Depósito exitoso: $" + monto);
>         }
>     }
>     
>     // Comportamiento: Retirar dinero
>     public boolean retirar(double monto) {
>         if (monto > 0 && monto <= this.saldo) {
>             this.saldo -= monto;
>             System.out.println("Retiro exitoso: $" + monto);
>             return true;
>         }
>         System.out.println("Fondos insuficientes");
>         return false;
>     }
>     
>     // Comportamiento: Consultar saldo
>     public double consultarSaldo() {
>         return this.saldo;
>     }
>     
>     // Comportamiento: Transferir a otra cuenta
>     public void transferir(CuentaBancaria destino, double monto) {
>         if (this.retirar(monto)) {
>             destino.depositar(monto);
>             System.out.println("Transferencia exitosa");
>         }
>     }
>     
>     // Comportamiento: Mostrar información
>     public void mostrarInfo() {
>         System.out.println("Titular: " + this.titular);
>         System.out.println("Cuenta: " + this.numeroCuenta);
>         System.out.println("Saldo: $" + this.saldo);
>     }
> }
> 
> // USO:
> CuentaBancaria cuenta1 = new CuentaBancaria("Ana López", "001");
> CuentaBancaria cuenta2 = new CuentaBancaria("Juan Pérez", "002");
> 
> cuenta1.depositar(1000);        // Comportamiento: depositar
> cuenta1.retirar(200);           // Comportamiento: retirar
> cuenta1.transferir(cuenta2, 300); // Comportamiento: transferir
> cuenta1.mostrarInfo();          // Comportamiento: mostrar info
> ```

---

## 🔗 This - Referencia al Objeto Actual

> [!tip]- 👈 La Palabra Clave `this`
> 
> **Usos de `this`:**
> 
> **1. Diferenciar atributos de parámetros:**
> 
> ```java
> public class Persona {
>     private String nombre;
>     
>     public void setNombre(String nombre) {
>         this.nombre = nombre;  // this.nombre = atributo, nombre = parámetro
>     }
> }
> ```
> 
> **2. Llamar a otros métodos de la misma clase:**
> 
> ```java
> public class Calculadora {
>     public int sumar(int a, int b) {
>         return a + b;
>     }
>     
>     public int sumarTres(int a, int b, int c) {
>         return this.sumar(a, b) + c;  // Llama a sumar()
>     }
> }
> ```
> 
> **3. Llamar a otro constructor (constructor chaining):**
> 
> ```java
> public class Estudiante {
>     private String nombre;
>     private int edad;
>     
>     public Estudiante(String nombre) {
>         this(nombre, 18);  // Llama al constructor de dos parámetros
>     }
>     
>     public Estudiante(String nombre, int edad) {
>         this.nombre = nombre;
>         this.edad = edad;
>     }
> }
> ```

---

## 📊 Ejemplo Completo: Clase Estudiante

> [!example]- 🎓 Implementación Completa
> 
> ```java
> public class Estudiante {
>     // ATRIBUTOS
>     private String nombre;
>     private String codigo;
>     private double[] notas;
>     private int numeroNotas;
>     
>     // CONSTRUCTOR
>     public Estudiante(String nombre, String codigo) {
>         this.nombre = nombre;
>         this.codigo = codigo;
>         this.notas = new double[10];
>         this.numeroNotas = 0;
>     }
>     
>     // GETTERS
>     public String getNombre() {
>         return this.nombre;
>     }
>     
>     public String getCodigo() {
>         return this.codigo;
>     }
>     
>     // SETTERS
>     public void setNombre(String nombre) {
>         this.nombre = nombre;
>     }
>     
>     // MÉTODOS DE COMPORTAMIENTO
>     
>     // Agregar nota
>     public void agregarNota(double nota) {
>         if (numeroNotas < notas.length && nota >= 0 && nota <= 10) {
>             notas[numeroNotas] = nota;
>             numeroNotas++;
>             System.out.println("Nota agregada correctamente");
>         } else {
>             System.out.println("Error: nota inválida o límite alcanzado");
>         }
>     }
>     
>     // Calcular promedio
>     public double calcularPromedio() {
>         if (numeroNotas == 0) {
>             return 0.0;
>         }
>         
>         double suma = 0;
>         for (int i = 0; i < numeroNotas; i++) {
>             suma += notas[i];
>         }
>         return suma / numeroNotas;
>     }
>     
>     // Verificar si aprobó
>     public boolean aprobo() {
>         return this.calcularPromedio() >= 7.0;
>     }
>     
>     // Obtener calificación
>     public String obtenerCalificacion() {
>         double promedio = this.calcularPromedio();
>         
>         if (promedio >= 9.0) return "Excelente";
>         if (promedio >= 8.0) return "Muy Bien";
>         if (promedio >= 7.0) return "Bien";
>         if (promedio >= 6.0) return "Aprobado";
>         return "Reprobado";
>     }
>     
>     // Mostrar información completa
>     public void mostrarInfo() {
>         System.out.println("=== INFORMACIÓN DEL ESTUDIANTE ===");
>         System.out.println("Nombre: " + this.nombre);
>         System.out.println("Código: " + this.codigo);
>         System.out.println("Número de notas: " + this.numeroNotas);
>         System.out.printf("Promedio: %.2f\n", this.calcularPromedio());
>         System.out.println("Calificación: " + this.obtenerCalificacion());
>         System.out.println("Estado: " + (this.aprobo() ? "APROBADO" : "REPROBADO"));
>     }
> }
> 
> // PROGRAMA PRINCIPAL
> public class Main {
>     public static void main(String[] args) {
>         // Crear estudiante
>         Estudiante estudiante = new Estudiante("Ana López", "EST-001");
>         
>         // Agregar notas
>         estudiante.agregarNota(8.5);
>         estudiante.agregarNota(9.0);
>         estudiante.agregarNota(7.5);
>         estudiante.agregarNota(8.0);
>         
>         // Mostrar información
>         estudiante.mostrarInfo();
>         
>         // Usar otros métodos
>         System.out.println("\nPromedio: " + estudiante.calcularPromedio());
>         System.out.println("¿Aprobó? " + (estudiante.aprobo() ? "Sí" : "No"));
>     }
> }
> ```

---

## ✅ Mejores Prácticas

> [!tip]- 🎯 Recomendaciones
> 
> **1. Nombres descriptivos:**
> 
> ```java
> // ✅ CORRECTO
> public double calcularPromedioNotas() { }
> public boolean validarEdad(int edad) { }
> 
> // ❌ INCORRECTO
> public double calc() { }
> public boolean check(int x) { }
> ```
> 
> **2. Un método, una responsabilidad:**
> 
> ```java
> // ✅ CORRECTO
> public void validarDatos() { }
> public void guardarDatos() { }
> public void mostrarResultado() { }
> 
> // ❌ INCORRECTO
> public void validarGuardarYMostrar() { }  // Hace demasiado
> ```
> 
> **3. Métodos cortos y legibles:**
> 
> ```java
> // ✅ CORRECTO - Máximo 20-30 líneas
> public double calcularPromedio() {
>     if (notas.length == 0) return 0.0;
>     return sumarNotas() / notas.length;
> }
> ```
> 
> **4. Usar getters/setters para encapsulación:**
> 
> ```java
> // ✅ CORRECTO
> private String nombre;
> public String getNombre() { return nombre; }
> public void setNombre(String nombre) { this.nombre = nombre; }
> 
> // ❌ INCORRECTO
> public String nombre;  // Acceso directo
> ```

---

## 🔗 Próximos Temas

> [!quote]- 🌟 Continuando el Aprendizaje
> 
> **Este tema es prerequisito para:**
> 
> - **[[Constructores]]** - Inicialización especializada de objetos
> - **[[Encapsulamiento]]** - Protección de datos y comportamiento
> - **[[Herencia]]** - Sobrescritura de métodos (Override)
> - **[[Polimorfismo]]** - Comportamiento dinámico
> - **[[Clases Abstractas]]** - Métodos sin implementación

---

**Tags:** #java #metodos #comportamiento #poo #getters #setters #overloading #this #static #instancia