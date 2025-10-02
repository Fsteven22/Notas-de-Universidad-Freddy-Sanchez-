# 🏗️ Definición de Clases en Java

## 🎯 Introducción a las Clases

> [!info]- 💡 ¿Qué es una Clase? Una **clase** es una plantilla o molde que define las características (atributos) y comportamientos (métodos) que tendrán los objetos creados a partir de ella. Es el concepto fundamental de la Programación Orientada a Objetos.
> 
> **Analogías útiles:**
> 
> - **Plano de una casa:** La clase es el plano, las casas construidas son los objetos
> - **Molde de galletas:** La clase es el molde, las galletas son los objetos
> - **Receta de cocina:** La clase es la receta, los platillos preparados son los objetos
> - **Especie biológica:** La clase define qué es un "Perro", cada perro individual es un objeto
> 
> **Diferencia Clase vs Objeto:**
> 
> - **Clase:** Definición abstracta (el concepto de "Estudiante")
> - **Objeto:** Instancia concreta (Juan, María, Pedro - estudiantes específicos)

---

## 📦 Anatomía de una Clase

### 🏗️ Estructura General

> [!example]- 🔵 Componentes de una Clase
> 
> ```java
> // 1. Declaración del paquete (opcional)
> package com.universidad.modelos;
> 
> // 2. Imports (si es necesario)
> import java.util.ArrayList;
> import java.time.LocalDate;
> 
> // 3. Declaración de la clase
> public class Estudiante {
>     
>     // 4. ATRIBUTOS (Variables de instancia)
>     // Características del objeto
>     private String nombre;
>     private String apellido;
>     private int edad;
>     private double promedio;
>     private String carrera;
>     
>     // 5. CONSTRUCTORES
>     // Métodos especiales para crear objetos
>     public Estudiante() {
>         // Constructor sin parámetros
>     }
>     
>     public Estudiante(String nombre, String apellido, int edad) {
>         this.nombre = nombre;
>         this.apellido = apellido;
>         this.edad = edad;
>     }
>     
>     // 6. MÉTODOS
>     // Comportamientos del objeto
>     public void estudiar() {
>         System.out.println(nombre + " está estudiando");
>     }
>     
>     public double calcularPromedio() {
>         // lógica para calcular promedio
>         return promedio;
>     }
>     
>     // 7. GETTERS Y SETTERS
>     // Métodos de acceso a atributos privados
>     public String getNombre() {
>         return nombre;
>     }
>     
>     public void setNombre(String nombre) {
>         this.nombre = nombre;
>     }
> }
> ```
> 
> **Orden recomendado de los elementos:**
> 
> 1. Variables estáticas (static)
> 2. Variables de instancia (atributos)
> 3. Constructores
> 4. Métodos públicos
> 5. Métodos privados
> 6. Getters y Setters (al final)

### 🎨 Sintaxis de Declaración

> [!note]- 📝 Formas de Declarar una Clase
> 
> **Sintaxis básica:**
> 
> ```java
> [modificador] class NombreClase {
>     // Contenido de la clase
> }
> ```
> 
> **Modificadores de acceso para clases:**
> 
> |Modificador|Descripción|Accesible desde|
> |---|---|---|
> |**public**|Accesible desde cualquier lugar|Todas las clases|
> |**(sin modificador)**|Package-private|Solo clases del mismo paquete|
> 
> **Ejemplos:**
> 
> ```java
> // Clase pública (la más común)
> public class Persona {
>     // ...
> }
> 
> // Clase package-private
> class Utilidades {
>     // Solo accesible en el mismo paquete
> }
> 
> // ❌ ERROR: No se permiten otros modificadores para clases de nivel superior
> private class MiClase { }    // ❌ Error
> protected class OtraClase { } // ❌ Error
> ```
> 
> **Reglas importantes:**
> 
> - Solo puede haber **UNA clase pública** por archivo
> - El nombre del archivo debe coincidir con el nombre de la clase pública
> - Puede haber múltiples clases package-private en un archivo
> 
> **Ejemplo de múltiples clases en un archivo:**
> 
> ```java
> // Archivo: Estudiante.java
> 
> public class Estudiante {
>     private String nombre;
>     // ...
> }
> 
> // Clase auxiliar package-private
> class Calificacion {
>     private double nota;
>     // ...
> }
> 
> // Otra clase auxiliar
> class Materia {
>     private String codigo;
>     // ...
> }
> ```

---

## 🎯 Atributos (Variables de Instancia)

### 📊 Definición y Tipos

> [!success]- 🟢 ¿Qué son los Atributos?
> 
> Los **atributos** (también llamados campos, variables de instancia o propiedades) son las características o datos que describe una clase. Cada objeto tendrá su propia copia de estos atributos con valores específicos.
> 
> **Sintaxis:**
> 
> ```java
> [modificador] tipo nombreAtributo [= valorInicial];
> ```
> 
> **Ejemplo completo:**
> 
> ```java
> public class Persona {
>     // Atributos de instancia
>     private String nombre;           // String sin inicializar (null)
>     private String apellido;
>     private int edad;                // int sin inicializar (0)
>     private double altura;           // double sin inicializar (0.0)
>     private boolean esEstudiante;    // boolean sin inicializar (false)
>     
>     // Atributos con valores iniciales
>     private String pais = "Ecuador";
>     private int intentos = 0;
>     private boolean activo = true;
> }
> ```
> 
> **Valores por defecto si no se inicializan:**
> 
> |Tipo|Valor por defecto|
> |---|---|
> |byte, short, int, long|0|
> |float, double|0.0|
> |boolean|false|
> |char|'\u0000'|
> |Referencias (String, objetos)|null|

### 🔒 Modificadores de Acceso para Atributos

> [!tip]- 🛡️ Niveles de Visibilidad
> 
> |Modificador|Clase|Paquete|Subclase|Mundo|
> |---|---|---|---|---|
> |**private**|✅|❌|❌|❌|
> |**(sin modificador)**|✅|✅|❌|❌|
> |**protected**|✅|✅|✅|❌|
> |**public**|✅|✅|✅|✅|
> 
> **Recomendación:** Usar **private** para atributos (principio de encapsulamiento)
> 
> **Ejemplos:**
> 
> ```java
> public class CuentaBancaria {
>     // ✅ RECOMENDADO: Atributos privados
>     private String titular;
>     private double saldo;
>     private String numeroCuenta;
>     
>     // ❌ NO RECOMENDADO: Atributos públicos (rompe encapsulamiento)
>     public String password;  // ¡Cualquiera puede modificarlo!
>     
>     // Package-private (sin modificador)
>     String banco;  // Accesible solo en el mismo paquete
>     
>     // Protected (para herencia)
>     protected int antiguedad;  // Subclases pueden acceder
> }
> ```
> 
> **¿Por qué usar private?**
> 
> - **Control:** Podemos validar datos antes de modificarlos
> - **Seguridad:** Evita cambios no autorizados
> - **Flexibilidad:** Podemos cambiar la implementación interna sin afectar código externo
> - **Mantenibilidad:** Más fácil encontrar dónde se modifica un atributo

### 🎨 Tipos de Atributos

> [!example]- 📦 Clasificación de Atributos
> 
> **1. Atributos primitivos:**
> 
> ```java
> public class Producto {
>     private int codigo;
>     private double precio;
>     private boolean disponible;
>     private char categoria;
>     private long codigoBarras;
> }
> ```
> 
> **2. Atributos de referencia (objetos):**
> 
> ```java
> public class Estudiante {
>     private String nombre;              // String
>     private LocalDate fechaNacimiento;  // Objeto LocalDate
>     private ArrayList<Double> notas;    // Colección
>     private Direccion direccion;        // Objeto personalizado
> }
> ```
> 
> **3. Atributos de tipo array:**
> 
> ```java
> public class Salon {
>     private String[] estudiantes;
>     private double[] calificaciones;
>     private int[][] matrizAsistencia;
> }
> ```
> 
> **4. Atributos estáticos (de clase):**
> 
> ```java
> public class Contador {
>     private static int totalObjetos = 0;  // Compartido por todas las instancias
>     private int id;                        // Único para cada instancia
>     
>     public Contador() {
>         totalObjetos++;  // Se incrementa para todos
>         id = totalObjetos;
>     }
> }
> ```
> 
> **5. Atributos finales (constantes):**
> 
> ```java
> public class Configuracion {
>     // Constante de clase (static final)
>     public static final double PI = 3.14159;
>     public static final int MAX_INTENTOS = 3;
>     
>     // Constante de instancia (final)
>     private final String codigoUnico;
>     
>     public Configuracion(String codigo) {
>         this.codigoUnico = codigo;  // Solo se puede asignar una vez
>     }
> }
> ```

---

## 🏗️ Constructores

### 🎯 ¿Qué es un Constructor?

> [!info]- 🔨 Definición y Propósito
> 
> Un **constructor** es un método especial que se ejecuta automáticamente cuando se crea un objeto. Su propósito es **inicializar** los atributos del objeto.
> 
> **Características especiales:**
> 
> - Tiene el **mismo nombre** que la clase
> - **NO tiene tipo de retorno** (ni siquiera void)
> - Se invoca automáticamente con la palabra clave `new`
> - Puede haber múltiples constructores (sobrecarga)
> 
> **Sintaxis básica:**
> 
> ```java
> [modificador] NombreClase(parámetros) {
>     // Código de inicialización
> }
> ```
> 
> **Comparación con métodos normales:**
> 
> ```java
> public class Ejemplo {
>     // CONSTRUCTOR (sin tipo de retorno)
>     public Ejemplo() {
>         // ...
>     }
>     
>     // MÉTODO normal (con tipo de retorno)
>     public void metodo() {
>         // ...
>     }
> }
> ```

### 🔧 Tipos de Constructores

> [!example]- 🟢 Constructor por Defecto
> 
> **Constructor sin parámetros** (también llamado constructor por defecto o no-args constructor)
> 
> ```java
> public class Persona {
>     private String nombre;
>     private int edad;
>     
>     // Constructor sin parámetros
>     public Persona() {
>         this.nombre = "Sin nombre";
>         this.edad = 0;
>         System.out.println("Objeto Persona creado");
>     }
> }
> 
> // Uso:
> Persona p1 = new Persona();  // Llama al constructor sin parámetros
> ```
> 
> **⚠️ Constructor por defecto automático:**
> 
> - Si NO defines NINGÚN constructor, Java crea uno automáticamente
> - Si defines AL MENOS UN constructor, Java NO crea el constructor por defecto
> 
> ```java
> // Caso 1: Sin constructores definidos
> public class Auto {
>     private String marca;
>     // Java crea automáticamente: public Auto() { }
> }
> Auto a = new Auto();  // ✅ Funciona
> 
> // Caso 2: Con constructor parametrizado
> public class Moto {
>     private String marca;
>     
>     public Moto(String marca) {
>         this.marca = marca;
>     }
>     // Java NO crea constructor por defecto
> }
> Moto m1 = new Moto();          // ❌ Error: no existe constructor sin parámetros
> Moto m2 = new Moto("Yamaha");  // ✅ Funciona
> ```

> [!example]- 🔵 Constructor Parametrizado
> 
> **Constructor que recibe valores para inicializar atributos**
> 
> ```java
> public class Estudiante {
>     private String nombre;
>     private String apellido;
>     private int edad;
>     private String carrera;
>     
>     // Constructor parametrizado
>     public Estudiante(String nombre, String apellido, int edad, String carrera) {
>         this.nombre = nombre;
>         this.apellido = apellido;
>         this.edad = edad;
>         this.carrera = carrera;
>     }
> }
> 
> // Uso:
> Estudiante est1 = new Estudiante("Juan", "Pérez", 20, "Ingeniería");
> Estudiante est2 = new Estudiante("María", "García", 22, "Medicina");
> ```
> 
> **La palabra clave `this`:**
> 
> - Hace referencia al objeto actual
> - Necesaria cuando el parámetro tiene el mismo nombre que el atributo
> 
> ```java
> // ✅ CORRECTO: Usar this para diferenciar
> public Estudiante(String nombre, int edad) {
>     this.nombre = nombre;  // this.nombre es el atributo, nombre es el parámetro
>     this.edad = edad;
> }
> 
> // ✅ ALTERNATIVA: Nombres diferentes (no necesita this)
> public Estudiante(String n, int e) {
>     nombre = n;  // No hay ambigüedad
>     edad = e;
> }
> 
> // ❌ ERROR: Ambigüedad sin this
> public Estudiante(String nombre, int edad) {
>     nombre = nombre;  // ¡Asigna el parámetro a sí mismo!
>     edad = edad;      // No modifica el atributo
> }
> ```

> [!success]- 🟡 Sobrecarga de Constructores
> 
> **Múltiples constructores con diferentes parámetros**
> 
> ```java
> public class Producto {
>     private String nombre;
>     private double precio;
>     private int stock;
>     private String categoria;
>     
>     // Constructor 1: Sin parámetros
>     public Producto() {
>         this.nombre = "Sin nombre";
>         this.precio = 0.0;
>         this.stock = 0;
>         this.categoria = "General";
>     }
>     
>     // Constructor 2: Solo nombre
>     public Producto(String nombre) {
>         this.nombre = nombre;
>         this.precio = 0.0;
>         this.stock = 0;
>         this.categoria = "General";
>     }
>     
>     // Constructor 3: Nombre y precio
>     public Producto(String nombre, double precio) {
>         this.nombre = nombre;
>         this.precio = precio;
>         this.stock = 0;
>         this.categoria = "General";
>     }
>     
>     // Constructor 4: Todos los parámetros
>     public Producto(String nombre, double precio, int stock, String categoria) {
>         this.nombre = nombre;
>         this.precio = precio;
>         this.stock = stock;
>         this.categoria = categoria;
>     }
> }
> 
> // Uso: El compilador elige el constructor según los argumentos
> Producto p1 = new Producto();
> Producto p2 = new Producto("Laptop");
> Producto p3 = new Producto("Mouse", 15.99);
> Producto p4 = new Producto("Teclado", 45.50, 20, "Periféricos");
> ```
> 
> **Encadenamiento de constructores con `this()`:**
> 
> ```java
> public class Producto {
>     private String nombre;
>     private double precio;
>     private int stock;
>     private String categoria;
>     
>     // Constructor principal (más completo)
>     public Producto(String nombre, double precio, int stock, String categoria) {
>         this.nombre = nombre;
>         this.precio = precio;
>         this.stock = stock;
>         this.categoria = categoria;
>     }
>     
>     // Constructores que llaman al principal
>     public Producto() {
>         this("Sin nombre", 0.0, 0, "General");  // Llama al constructor principal
>     }
>     
>     public Producto(String nombre) {
>         this(nombre, 0.0, 0, "General");
>     }
>     
>     public Producto(String nombre, double precio) {
>         this(nombre, precio, 0, "General");
>     }
> }
> ```
> 
> **⚠️ Reglas del encadenamiento:**
> 
> - `this()` debe ser la **primera línea** del constructor
> - Solo se puede llamar a **un** constructor
> - No puede haber referencias circulares

> [!tip]- 🔨 Constructor Copia
> 
> **Constructor que crea un objeto copiando otro objeto del mismo tipo**
> 
> ```java
> public class Punto {
>     private double x;
>     private double y;
>     
>     // Constructor normal
>     public Punto(double x, double y) {
>         this.x = x;
>         this.y = y;
>     }
>     
>     // Constructor copia
>     public Punto(Punto otro) {
>         this.x = otro.x;
>         this.y = otro.y;
>         System.out.println("Punto copiado");
>     }
> }
> 
> // Uso:
> Punto p1 = new Punto(5.0, 10.0);
> Punto p2 = new Punto(p1);  // Copia de p1
> 
> // p1 y p2 tienen los mismos valores pero son objetos diferentes
> ```
> 
> **Copia superficial vs profunda:**
> 
> ```java
> public class Estudiante {
>     private String nombre;
>     private ArrayList<Double> notas;  // Objeto mutable
>     
>     // Constructor normal
>     public Estudiante(String nombre) {
>         this.nombre = nombre;
>         this.notas = new ArrayList<>();
>     }
>     
>     // ❌ Constructor copia superficial (shallow copy)
>     public Estudiante(Estudiante otro) {
>         this.nombre = otro.nombre;
>         this.notas = otro.notas;  // ¡Ambos comparten el mismo ArrayList!
>     }
>     
>     // ✅ Constructor copia profunda (deep copy)
>     public Estudiante(Estudiante otro) {
>         this.nombre = otro.nombre;
>         this.notas = new ArrayList<>(otro.notas);  // Crea nuevo ArrayList
>     }
> }
> ```

### 🎯 Validación en Constructores

> [!warning]- ⚠️ Asegurar Datos Válidos desde la Creación
> 
> ```java
> public class CuentaBancaria {
>     private String titular;
>     private double saldo;
>     private String numeroCuenta;
>     
>     public CuentaBancaria(String titular, double saldoInicial, String numeroCuenta) {
>         // Validar titular
>         if (titular == null || titular.trim().isEmpty()) {
>             throw new IllegalArgumentException("El titular no puede estar vacío");
>         }
>         
>         // Validar saldo inicial
>         if (saldoInicial < 0) {
>             throw new IllegalArgumentException("El saldo inicial no puede ser negativo");
>         }
>         
>         // Validar número de cuenta
>         if (numeroCuenta == null || numeroCuenta.length() != 10) {
>             throw new IllegalArgumentException("Número de cuenta inválido");
>         }
>         
>         // Si todas las validaciones pasan, asignar valores
>         this.titular = titular.trim();
>         this.saldo = saldoInicial;
>         this.numeroCuenta = numeroCuenta;
>     }
> }
> 
> // Uso:
> try {
>     CuentaBancaria c1 = new CuentaBancaria("", 100, "1234567890");  // ❌ Error
> } catch (IllegalArgumentException e) {
>     System.out.println(e.getMessage());
> }
> 
> CuentaBancaria c2 = new CuentaBancaria("Juan Pérez", 500, "9876543210");  // ✅ OK
> ```

---

## 🎬 Métodos (Comportamientos)

### 📝 Definición de Métodos

> [!info]- 🔧 ¿Qué son los Métodos?
> 
> Los **métodos** son funciones que definen el comportamiento de los objetos. Representan las acciones que un objeto puede realizar.
> 
> **Sintaxis completa:**
> 
> ```java
> [modificador] tipoRetorno nombreMetodo(parámetros) {
>     // Cuerpo del método
>     return valor;  // Si no es void
> }
> ```
> 
> **Componentes:**
> 
> 1. **Modificador:** public, private, protected, static, final, etc.
> 2. **Tipo de retorno:** tipo de dato que devuelve (o void si no devuelve nada)
> 3. **Nombre:** identificador del método (camelCase)
> 4. **Parámetros:** datos que recibe el método (opcional)
> 5. **Cuerpo:** código que se ejecuta
> 6. **return:** valor que devuelve (obligatorio si no es void)
> 
> **Ejemplo básico:**
> 
> ```java
> public class Calculadora {
>     
>     // Método que NO retorna valor (void)
>     public void saludar() {
>         System.out.println("Hola desde Calculadora");
>     }
>     
>     // Método que SÍ retorna valor
>     public int sumar(int a, int b) {
>         int resultado = a + b;
>         return resultado;
>     }
>     
>     // Método sin parámetros que retorna valor
>     public double obtenerPI() {
>         return 3.14159;
>     }
>     
>     // Método con múltiples parámetros
>     public double calcularPromedio(double n1, double n2, double n3) {
>         return (n1 + n2 + n3) / 3.0;
>     }
> }
> ```

### 🎯 Tipos de Métodos

> [!example]- 🟢 Métodos de Instancia vs Métodos de Clase (static)
> 
> **Métodos de instancia (normales):**
> 
> - Se invocan sobre un objeto específico
> - Pueden acceder a atributos de instancia
> - Usan `this` para referirse al objeto actual
> 
> ```java
> public class Estudiante {
>     private String nombre;
>     private double[] notas;
>     
>     // Método de instancia
>     public double calcularPromedio() {
>         double suma = 0;
>         for (double nota : notas) {
>             suma += nota;
>         }
>         return suma / notas.length;
>     }
>     
>     // Otro método de instancia
>     public void mostrarInfo() {
>         System.out.println("Estudiante: " + this.nombre);
>         System.out.println("Promedio: " + this.calcularPromedio());
>     }
> }
> 
> // Uso: Se invoca sobre un objeto
> Estudiante est = new Estudiante();
> double promedio = est.calcularPromedio();  // Método de instancia
> est.mostrarInfo();
> ```
> 
> **Métodos estáticos (static):**
> 
> - Se invocan sobre la clase, no sobre objetos
> - NO pueden acceder a atributos de instancia
> - NO pueden usar `this`
> - Se usan para utilidades o funciones independientes
> 
> ```java
> public class Matematicas {
>     
>     // Método estático
>     public static int factorial(int n) {
>         if (n <= 1) return 1;
>         return n * factorial(n - 1);
>     }
>     
>     // Otro método estático
>     public static double calcularAreaCirculo(double radio) {
>         return Math.PI * radio * radio;
>     }
> }
> 
> // Uso: Se invoca sobre la clase
> int fact = Matematicas.factorial(5);  // No necesita objeto
> double area = Matematicas.calcularAreaCirculo(10.0);
> ```
> 
> **Comparación:**
> 
> ```java
> public class Ejemplo {
>     private int instancia = 10;
>     private static int clase = 20;
>     
>     // ✅ Método de instancia puede acceder a todo
>     public void metodoInstancia() {
>         System.out.println(instancia);  // ✅ OK
>         System.out.println(clase);      // ✅ OK
>         this.otroMetodoInstancia();     // ✅ OK
>         metodoEstatico();               // ✅ OK
>     }
>     
>     // ⚠️ Método estático tiene limitaciones
>     public static void metodoEstatico() {
>         // System.out.println(instancia);  // ❌ Error: no puede acceder
>         System.out.println(clase);         // ✅ OK
>         // this.metodoInstancia();         // ❌ Error: no hay this
>         otroMetodoEstatico();              // ✅ OK
>     }
>     
>     public void otroMetodoInstancia() { }
>     public static void otroMetodoEstatico() { }
> }
> ```

> [!success]- 🔵 Getters y Setters (Métodos de Acceso)
> 
> **¿Por qué usar getters y setters?**
> 
> - Controlar el acceso a atributos privados
> - Validar datos antes de modificarlos
> - Mantener el encapsulamiento
> 
> **Convenciones de nombres:**
> 
> - **Getter:** `getTipo()` o `isTipo()` (para boolean)
> - **Setter:** `setTipo(tipo valor)`
> 
> ```java
> public class Persona {
>     private String nombre;
>     private int edad;
>     private double salario;
>     private boolean activo;
>     
>     // GETTERS (obtener valores)
>     public String getNombre() {
>         return nombre;
>     }
>     
>     public int getEdad() {
>         return edad;
>     }
>     
>     public double getSalario() {
>         return salario;
>     }
>     
>     // Para boolean: usar "is" en lugar de "get"
>     public boolean isActivo() {
>         return activo;
>     }
>     
>     // SETTERS (modificar valores con validación)
>     public void setNombre(String nombre) {
>         if (nombre != null && !nombre.trim().isEmpty()) {
>             this.nombre = nombre.trim();
>         } else {
>             throw new IllegalArgumentException("Nombre inválido");
>         }
>     }
>     
>     public void setEdad(int edad) {
>         if (edad >= 0 && edad <= 150) {
>             this.edad = edad;
>         } else {
>             throw new IllegalArgumentException("Edad debe estar entre 0 y 150");
>         }
>     }
>     
>     public void setSalario(double salario) {
>         if (salario >= 0) {
>             this.salario = salario;
>         } else {
>             throw new IllegalArgumentException("Salario no puede ser negativo");
>         }
>     }
>     
>     public void setActivo(boolean activo) {
>         this.activo = activo;
>     }
> }
> 
> // Uso:
> Persona p = new Persona();
> p.setNombre("Juan");
> p.setEdad(25);
> 
> System.out.println(p.getNombre());  // Juan
> System.out.println(p.getEdad());    // 25
> ```
> 
> **Getters/Setters con lógica adicional:**
> 
> ```java
> public class CuentaBancaria {
>     private double saldo;
>     private final double SALDO_MINIMO = 10.0;
>     
>     public double getSaldo() {
>         return saldo;
>     }
>     
>     // Setter con validación de negocio
>     public void setSaldo(double saldo) {
>         if (saldo < SALDO_MINIMO) {
>             System.out.println("Advertencia: Saldo menor al mínimo");
>         }
>         this.saldo = saldo;
>     }
>     
>     // Getter calculado (no simplemente devolver el atributo)
>     public String getSaldoFormateado() {
>         return String.format("$%.2f", saldo);
>     }
> }
> ```
> 
> **Atributos de solo lectura (solo getter):**
> 
> ```java
> public class Producto {
>     private final String codigo;  // Asignado en constructor
>
>     private String nombre;
>     
>     public Producto(String codigo, String nombre) {
>         this.codigo = codigo;
>         this.nombre = nombre;
>     }
>     
>     // Solo getter para código (NO hay setter)
>     public String getCodigo() {
>         return codigo;
>     }
>     
>     // Getter y setter para nombre (modificable)
>     public String getNombre() {
>         return nombre;
>     }
>     
>     public void setNombre(String nombre) {
>         this.nombre = nombre;
>     }
> }
> ```

### 🔄 Sobrecarga de Métodos (Overloading)

> [!tip]- 🎯 Múltiples Métodos con el Mismo Nombre
> 
> La **sobrecarga** permite tener varios métodos con el mismo nombre pero diferentes parámetros (cantidad, tipo o orden).
> 
> **Reglas de sobrecarga:**
> - Mismo nombre de método
> - Diferente lista de parámetros (firma del método)
> - El tipo de retorno puede ser diferente, pero NO es suficiente para diferenciar
> 
> ```java
> public class Calculadora {
>     
>     // Método 1: Suma de 2 enteros
>     public int sumar(int a, int b) {
>         return a + b;
>     }
>     
>     // Método 2: Suma de 3 enteros
>     public int sumar(int a, int b, int c) {
>         return a + b + c;
>     }
>     
>     // Método 3: Suma de 2 decimales
>     public double sumar(double a, double b) {
>         return a + b;
>     }
>     
>     // Método 4: Suma de un array
>     public int sumar(int[] numeros) {
>         int suma = 0;
>         for (int num : numeros) {
>             suma += num;
>         }
>         return suma;
>     }
>     
>     // Método 5: Concatenar strings (mismo nombre, diferente propósito)
>     public String sumar(String a, String b) {
>         return a + b;
>     }
> }
> 
> // Uso: El compilador elige el método correcto según los argumentos
> Calculadora calc = new Calculadora();
> 
> int r1 = calc.sumar(5, 3);              // Llama al método 1
> int r2 = calc.sumar(5, 3, 2);           // Llama al método 2
> double r3 = calc.sumar(5.5, 3.2);       // Llama al método 3
> int r4 = calc.sumar(new int[]{1,2,3});  // Llama al método 4
> String r5 = calc.sumar("Hola", "Mundo"); // Llama al método 5
> ```
> 
> **✅ Ejemplos válidos de sobrecarga:**
> ```java
> // Diferente número de parámetros
> public void metodo(int a) { }
> public void metodo(int a, int b) { }
> 
> // Diferente tipo de parámetros
> public void metodo(int a) { }
> public void metodo(double a) { }
> 
> // Diferente orden de parámetros
> public void metodo(int a, String b) { }
> public void metodo(String a, int b) { }
> ```
> 
> **❌ Errores comunes de sobrecarga:**
> ```java
> // ❌ ERROR: Solo difieren en el tipo de retorno
> public int metodo(int a) { return a; }
> public double metodo(int a) { return a; }  // Error de compilación
> 
> // ❌ ERROR: Solo difieren en nombres de parámetros
> public void metodo(int a) { }
> public void metodo(int x) { }  // Error: misma firma
> 
> // ❌ ERROR: Solo difieren en modificadores
> public void metodo(int a) { }
> private void metodo(int a) { }  // Error: misma firma
> ```
> 
> **Ejemplo práctico: Sistema de impresión:**
> ```java
> public class Impresora {
>     
>     public void imprimir(String texto) {
>         System.out.println(texto);
>     }
>     
>     public void imprimir(int numero) {
>         System.out.println("Número: " + numero);
>     }
>     
>     public void imprimir(double decimal) {
>         System.out.printf("Decimal: %.2f\n", decimal);
>     }
>     
>     public void imprimir(String[] array) {
>         System.out.println("Array:");
>         for (String item : array) {
>             System.out.println("  - " + item);
>         }
>     }
>     
>     public void imprimir(boolean valor) {
>         System.out.println(valor ? "VERDADERO" : "FALSO");
>     }
> }
> 
> // Uso intuitivo:
> Impresora imp = new Impresora();
> imp.imprimir("Hola");
> imp.imprimir(42);
> imp.imprimir(3.14);
> imp.imprimir(new String[]{"A", "B", "C"});
> imp.imprimir(true);
> ```

### 📤 Return en Métodos

> [!note]- ↩️ Retorno de Valores
> 
> **Métodos void (sin retorno):**
> ```java
> public void saludar() {
>     System.out.println("Hola");
>     // return es opcional aquí
> }
> 
> public void procesar(int numero) {
>     if (numero < 0) {
>         System.out.println("Error: número negativo");
>         return;  // Salida temprana del método
>     }
>     System.out.println("Procesando: " + numero);
> }
> ```
> 
> **Métodos con retorno único:**
> ```java
> public int suma(int a, int b) {
>     return a + b;  // Retorna un valor
> }
> 
> public String getNombreCompleto() {
>     return nombre + " " + apellido;
> }
> ```
> 
> **Métodos con múltiples puntos de retorno:**
> ```java
> public String calificar(double nota) {
>     if (nota >= 9.0) {
>         return "Excelente";
>     } else if (nota >= 7.0) {
>         return "Bueno";
>     } else if (nota >= 5.0) {
>         return "Regular";
>     } else {
>         return "Insuficiente";
>     }
>     // No hay código después de los return
> }
> 
> public int buscar(int[] array, int valor) {
>     for (int i = 0; i < array.length; i++) {
>         if (array[i] == valor) {
>             return i;  // Retorna inmediatamente cuando encuentra
>         }
>     }
>     return -1;  // No encontrado
> }
> ```
> 
> **Retornar objetos:**
> ```java
> public Estudiante crearEstudiante(String nombre, int edad) {
>     Estudiante nuevo = new Estudiante(nombre, edad);
>     return nuevo;
> }
> 
> public ArrayList<Integer> obtenerPares(int[] array) {
>     ArrayList<Integer> pares = new ArrayList<>();
>     for (int num : array) {
>         if (num % 2 == 0) {
>             pares.add(num);
>         }
>     }
>     return pares;
> }
> ```
> 
> **⚠️ Errores comunes con return:**
> ```java
> // ❌ ERROR: No todos los caminos retornan valor
> public int metodo(int x) {
>     if (x > 0) {
>         return 1;
>     }
>     // Falta return aquí si x <= 0
> }
> 
> // ✅ CORRECTO: Siempre hay un return
> public int metodo(int x) {
>     if (x > 0) {
>         return 1;
>     }
>     return -1;  // Camino por defecto
> }
> 
> // ❌ ERROR: Código inalcanzable después de return
> public void metodo() {
>     return;
>     System.out.println("Esto nunca se ejecuta");  // Unreachable code
> }
> ```

---

## 🎨 Ejemplo Completo: Clase Estudiante

> [!example]- 🎓 Implementación Completa
> 
> ```java
> /**
>  * Clase que representa a un estudiante universitario
>  * @author Tu Nombre
>  * @version 1.0
>  */
> public class Estudiante {
>     
>     // ============================================
>     // ATRIBUTOS (variables de instancia)
>     // ============================================
>     private String nombre;
>     private String apellido;
>     private int edad;
>     private String carrera;
>     private double promedio;
>     private String[] materias;
>     private int creditosCompletados;
>     
>     // Atributos estáticos (compartidos por todos)
>     private static int totalEstudiantes = 0;
>     private static final int EDAD_MINIMA = 17;
>     private static final int CREDITOS_GRADUACION = 240;
>     
>     // ============================================
>     // CONSTRUCTORES
>     // ============================================
>     
>     /**
>      * Constructor por defecto
>      */
>     public Estudiante() {
>         this.nombre = "Sin nombre";
>         this.apellido = "Sin apellido";
>         this.edad = EDAD_MINIMA;
>         this.carrera = "No definida";
>         this.promedio = 0.0;
>         this.materias = new String[0];
>         this.creditosCompletados = 0;
>         totalEstudiantes++;
>     }
>     
>     /**
>      * Constructor con parámetros básicos
>      */
>     public Estudiante(String nombre, String apellido, int edad) {
>         this();  // Llama al constructor por defecto
>         setNombre(nombre);
>         setApellido(apellido);
>         setEdad(edad);
>     }
>     
>     /**
>      * Constructor completo
>      */
>     public Estudiante(String nombre, String apellido, int edad, 
>                      String carrera, double promedio) {
>         this(nombre, apellido, edad);  // Llama al constructor anterior
>         setCarrera(carrera);
>         setPromedio(promedio);
>     }
>     
>     /**
>      * Constructor copia
>      */
>     public Estudiante(Estudiante otro) {
>         this.nombre = otro.nombre;
>         this.apellido = otro.apellido;
>         this.edad = otro.edad;
>         this.carrera = otro.carrera;
>         this.promedio = otro.promedio;
>         this.materias = otro.materias.clone();  // Copia profunda
>         this.creditosCompletados = otro.creditosCompletados;
>         totalEstudiantes++;
>     }
>     
>     // ============================================
>     // GETTERS Y SETTERS
>     // ============================================
>     
>     public String getNombre() {
>         return nombre;
>     }
>     
>     public void setNombre(String nombre) {
>         if (nombre != null && !nombre.trim().isEmpty()) {
>             this.nombre = nombre.trim();
>         } else {
>             throw new IllegalArgumentException("Nombre no puede estar vacío");
>         }
>     }
>     
>     public String getApellido() {
>         return apellido;
>     }
>     
>     public void setApellido(String apellido) {
>         if (apellido != null && !apellido.trim().isEmpty()) {
>             this.apellido = apellido.trim();
>         } else {
>             throw new IllegalArgumentException("Apellido no puede estar vacío");
>         }
>     }
>     
>     public int getEdad() {
>         return edad;
>     }
>     
>     public void setEdad(int edad) {
>         if (edad >= EDAD_MINIMA && edad <= 100) {
>             this.edad = edad;
>         } else {
>             throw new IllegalArgumentException(
>                 "Edad debe estar entre " + EDAD_MINIMA + " y 100");
>         }
>     }
>     
>     public String getCarrera() {
>         return carrera;
>     }
>     
>     public void setCarrera(String carrera) {
>         if (carrera != null && !carrera.trim().isEmpty()) {
>             this.carrera = carrera.trim();
>         }
>     }
>     
>     public double getPromedio() {
>         return promedio;
>     }
>     
>     public void setPromedio(double promedio) {
>         if (promedio >= 0.0 && promedio <= 10.0) {
>             this.promedio = promedio;
>         } else {
>             throw new IllegalArgumentException("Promedio debe estar entre 0 y 10");
>         }
>     }
>     
>     public int getCreditosCompletados() {
>         return creditosCompletados;
>     }
>     
>     public void setCreditosCompletados(int creditos) {
>         if (creditos >= 0) {
>             this.creditosCompletados = creditos;
>         }
>     }
>     
>     // ============================================
>     // MÉTODOS DE INSTANCIA (comportamientos)
>     // ============================================
>     
>     /**
>      * Obtiene el nombre completo del estudiante
>      */
>     public String getNombreCompleto() {
>         return nombre + " " + apellido;
>     }
>     
>     /**
>      * Verifica si el estudiante es mayor de edad
>      */
>     public boolean esMayorDeEdad() {
>         return edad >= 18;
>     }
>     
>     /**
>      * Calcula cuántos créditos faltan para graduarse
>      */
>     public int creditosFaltantes() {
>         return CREDITOS_GRADUACION - creditosCompletados;
>     }
>     
>     /**
>      * Verifica si el estudiante puede graduarse
>      */
>     public boolean puedeGraduarse() {
>         return creditosCompletados >= CREDITOS_GRADUACION && promedio >= 7.0;
>     }
>     
>     /**
>      * Calcula el porcentaje de avance en la carrera
>      */
>     public double porcentajeAvance() {
>         return (creditosCompletados * 100.0) / CREDITOS_GRADUACION;
>     }
>     
>     /**
>      * Matricula al estudiante en materias
>      */
>     public void matricular(String[] nuevasMaterias) {
>         if (nuevasMaterias != null && nuevasMaterias.length > 0) {
>             this.materias = nuevasMaterias.clone();
>             System.out.println(getNombreCompleto() + " matriculado en " + 
>                              nuevasMaterias.length + " materias");
>         }
>     }
>     
>     /**
>      * Actualiza el promedio con una nueva calificación
>      */
>     public void agregarCalificacion(double nuevaNota) {
>         if (nuevaNota >= 0 && nuevaNota <= 10) {
>             // Fórmula simplificada: promedio ponderado
>             this.promedio = (this.promedio + nuevaNota) / 2.0;
>         }
>     }
>     
>     /**
>      * Obtiene el nivel académico según créditos
>      */
>     public String getNivelAcademico() {
>         if (creditosCompletados < 60) {
>             return "Primer Ciclo";
>         } else if (creditosCompletados < 120) {
>             return "Segundo Ciclo";
>         } else if (creditosCompletados < 180) {
>             return "Tercer Ciclo";
>         } else if (creditosCompletados < 240) {
>             return "Cuarto Ciclo";
>         } else {
>             return "Egresado";
>         }
>     }
>     
>     /**
>      * Muestra toda la información del estudiante
>      */
>     public void mostrarInformacion() {
>         System.out.println("╔═══════════════════════════════════════╗");
>         System.out.println("║     INFORMACIÓN DEL ESTUDIANTE        ║");
>         System.out.println("╠═══════════════════════════════════════╣");
>         System.out.println("║ Nombre: " + getNombreCompleto());
>         System.out.println("║ Edad: " + edad + " años");
>         System.out.println("║ Carrera: " + carrera);
>         System.out.printf("║ Promedio: %.2f\n", promedio);
>         System.out.println("║ Créditos: " + creditosCompletados + "/" + 
>                          CREDITOS_GRADUACION);
>         System.out.printf("║ Avance: %.1f%%\n", porcentajeAvance());
>         System.out.println("║ Nivel: " + getNivelAcademico());
>         System.out.println("║ Mayor de edad: " + (esMayorDeEdad() ? "Sí" : "No"));
>         System.out.println("║ Puede graduarse: " + (puedeGraduarse() ? "Sí" : "No"));
>         System.out.println("╚═══════════════════════════════════════╝");
>     }
>     
>     /**
>      * Representa el objeto como String
>      */
>     @Override
>     public String toString() {
>         return String.format("Estudiante{nombre='%s', apellido='%s', " +
>                            "edad=%d, carrera='%s', promedio=%.2f}",
>                            nombre, apellido, edad, carrera, promedio);
>     }
>     
>     // ============================================
>     // MÉTODOS ESTÁTICOS (de clase)
>     // ============================================
>     
>     /**
>      * Obtiene el total de estudiantes creados
>      */
>     public static int getTotalEstudiantes() {
>         return totalEstudiantes;
>     }
>     
>     /**
>      * Obtiene la edad mínima permitida
>      */
>     public static int getEdadMinima() {
>         return EDAD_MINIMA;
>     }
>     
>     /**
>      * Obtiene los créditos necesarios para graduarse
>      */
>     public static int getCreditosGraduacion() {
>         return CREDITOS_GRADUACION;
>     }
>     
>     /**
>      * Compara dos estudiantes por promedio
>      */
>     public static Estudiante mejorPromedio(Estudiante e1, Estudiante e2) {
>         if (e1 == null) return e2;
>         if (e2 == null) return e1;
>         return (e1.promedio >= e2.promedio) ? e1 : e2;
>     }
>     
>     /**
>      * Verifica si una edad es válida
>      */
>     public static boolean edadValida(int edad) {
>         return edad >= EDAD_MINIMA && edad <= 100;
>     }
> }
> ```

---

## 🎮 Programa de Prueba (Main)

> [!example]- 🧪 Probando la Clase Estudiante
> 
> ```java
> public class PruebaEstudiante {
>     public static void main(String[] args) {
>         System.out.println("=== SISTEMA DE GESTIÓN DE ESTUDIANTES ===\n");
>         
>         // Crear estudiantes con diferentes constructores
>         Estudiante est1 = new Estudiante();
>         System.out.println("Estudiante 1 (constructor por defecto):");
>         est1.mostrarInformacion();
>         
>         System.out.println("\n");
>         
>         Estudiante est2 = new Estudiante("María", "García", 20);
>         est2.setCarrera("Ingeniería en Sistemas");
>         est2.setPromedio(8.5);
>         est2.setCreditosCompletados(120);
>         System.out.println("Estudiante 2:");
>         est2.mostrarInformacion();
>         
>         System.out.println("\n");
>         
>         Estudiante est3 = new Estudiante("Carlos", "Mendoza", 22, 
>                                         "Medicina", 9.2);
>         est3.setCreditosCompletados(200);
>         System.out.println("Estudiante 3:");
>         est3.mostrarInformacion();
>         
>         System.out.println("\n=== PRUEBAS DE MÉTODOS ===\n");
>         
>         // Probar métodos
>         System.out.println("Nombre completo: " + est2.getNombreCompleto());
>         System.out.println("Es mayor de edad: " + est2.esMayorDeEdad());
>         System.out.println("Créditos faltantes: " + est2.creditosFaltantes());
>         System.out.println("Puede graduarse: " + est2.puedeGraduarse());
>         System.out.printf("Porcentaje de avance: %.1f%%\n", est2.porcentajeAvance());
>         
>         // Matricular materias
>         String[] materias = {"Programación", "Matemáticas", "Física"};
>         est2.matricular(materias);
>         
>         // Agregar calificación
>         System.out.println("\nPromedio antes: " + est2.getPromedio());
>         est2.agregarCalificacion(9.0);
>         System.out.println("Promedio después: " + est2.getPromedio());
>         
>         // Usar métodos estáticos
>         System.out.println("\n=== INFORMACIÓN ESTÁTICA ===");
>         System.out.println("Total de estudiantes: " + 
>                          Estudiante.getTotalEstudiantes());
>         System.out.println("Edad mínima: " + Estudiante.getEdadMinima());
>         System.out.println("Créditos para graduación: " + 
>                          Estudiante.getCreditosGraduacion());
>         
>         // Comparar estudiantes
>         Estudiante mejor = Estudiante.mejorPromedio(est2, est3);
>         System.out.println("\nMejor promedio: " + mejor.getNombreCompleto() + 
>                          " con " + mejor.getPromedio());
>         
>         // Usar toString
>         System.out.println("\n=== REPRESENTACIÓN toString ===");
>         System.out.println(est2);
>         System.out.println(est3);
>         
>         // Constructor copia
>         System.out.println("\n=== PRUEBA DE CONSTRUCTOR COPIA ===");
>         Estudiante copiaEst2 = new Estudiante(est2);
>         System.out.println("Original: " + est2.getNombreCompleto());
>         System.out.println("Copia: " + copiaEst2.getNombreCompleto());
>         
>         // Son objetos diferentes
>         System.out.println("¿Son el mismo objeto? " + (est2 == copiaEst2));
>         System.out.println("¿Tienen los mismos datos? " + 
>                          (est2.getNombre().equals(copiaEst2.getNombre())));
>     }
> }
> ```
> 
> **Salida esperada:**
> ```
> === SISTEMA DE GESTIÓN DE ESTUDIANTES ===
> 
> Estudiante 1 (constructor por defecto):
> ╔═══════════════════════════════════════╗
> ║     INFORMACIÓN DEL ESTUDIANTE        ║
> ╠═══════════════════════════════════════╣
> ║ Nombre: Sin nombre Sin apellido
> ║ Edad: 17 años
> ║ Carrera: No definida
> ║ Promedio: 0.00
> ║ Créditos: 0/240
> ║ Avance: 0.0%
> ║ Nivel: Primer Ciclo
> ║ Mayor de edad: No
> ║ Puede graduarse: No
> ╚═══════════════════════════════════════╝
> 
> ...
> ```

---

## 🎯 Buenas Prácticas en Diseño de Clases

> [!tip]- ✅ Principios de Diseño
> 
> **1. Principio de Responsabilidad Única (SRP):**
> - Una clase debe tener una sola razón para cambiar
> - Cada clase debe representar un concepto claro
> 
> ```java
> // ✅ CORRECTO: Clases con responsabilidades claras
> public class Estudiante {
>     // Solo maneja datos y comportamiento del estudiante
> }
> 
> public class CalificacionManager {
>     // Solo maneja el cálculo de calificaciones
> }
> 
> public class RepositorioEstudiantes {
>     // Solo maneja persistencia de datos
> }
> 
> // ❌ INCORRECTO: Clase que hace demasiado
> public class Estudiante {
>     // Datos del estudiante
>     // Cálculos de calificaciones
>     // Conexión a base de datos
>     // Generación de reportes
>     // Envío de emails
>     // etc... (demasiadas responsabilidades)
> }
> ```
> 
> **2. Encapsulamiento fuerte:**
> ```java
> // ✅ CORRECTO
> public class CuentaBancaria {
>     private double saldo;  // Privado
>     
>     // Acceso controlado
>     public void depositar(double monto) {
>         if (monto > 0) {
>             saldo += monto;
>         }
>     }
>     
>     public boolean retirar(double monto) {
>         if (monto > 0 && monto <= saldo) {
>             saldo -= monto;
>             return true;
>         }
>         return false;
>     }
> }
> 
> // ❌ INCORRECTO
> public class CuentaBancaria {
>     public double saldo;  // ¡Cualquiera puede modificar!
> }
> ```
> 
> **3. Inmutabilidad cuando sea apropiado:**
> ```java
> // Clase inmutable (no se puede modificar después de crearse)
> public final class Punto {
>     private final double x;
>     private final double y;
>     
>     public Punto(double x, double y) {
>         this.x = x;
>         this.y = y;
>     }
>     
>     // Solo getters, NO setters
>     public double getX() { return x; }
>     public double getY() { return y; }
>     
>     // Para "modificar", crear nuevo objeto
>     public Punto mover(double dx, double dy) {
>         return new Punto(x + dx, y + dy);
>     }
> }
> ```
> 
> **4. Nombres descriptivos:**
> ```java
> // ✅ CORRECTO: Nombres que expresan intención
> public class ClientePreferencial { }
> public void calcularDescuentoPorVolumen() { }
> private boolean esPedidoUrgente() { }
> 
> // ❌ INCORRECTO: Nombres vagos
> public class Datos { }
> public void procesar() { }
> private boolean check() { }
> ```
> 
> **5. Documentación clara:**
> ```java
> /**
>  * Representa una cuenta bancaria con operaciones básicas.
>  * Esta clase mantiene el saldo y permite depositar y retirar fondos.
>  * 
>  * @author Tu Nombre
>  * @version 1.0
>  * @since 2025-01-01
>  */
> public class CuentaBancaria {
>     
>     /**
>      * Realiza un depósito en la cuenta.
>      * 
>      * @param monto la cantidad a depositar (debe ser positiva)
>      * @return true si el depósito fue exitoso, false en caso contrario
>      * @throws IllegalArgumentException si el monto es negativo
>      */
>     public boolean depositar(double monto) {
>         // ...
>     }
> }
> ```

---

## 🔍 Diferencias Clave: Clase vs Objeto

> [!note]- ⚖️ Comparación Conceptual
> 
> | Aspecto | Clase | Objeto |
> |---------|-------|--------|
> | **Definición** | Plantilla o molde | Instancia concreta |
> | **Naturaleza** | Abstracta | Concreta |
> | **Cantidad** | Una por tipo | Múltiples |
> | **Memoria** | No ocupa espacio (salvo atributos static) | Ocupa espacio en heap |
> | **Cuándo existe** | En tiempo de compilación | En tiempo de ejecución |
> | **Sintaxis** | `class NombreClase { }` | `new NombreClase()` |
> 
> **Ejemplo visual:**
> ```java
> // CLASE: La receta (definición)
> public class Galleta {
>     private String sabor;
>     private double tamaño;
>     
>     public Galleta(String sabor, double tamaño) {
>         this.sabor = sabor;
>         this.tamaño = tamaño;
>     }
> }
> 
> // OBJETOS: Las galletas individuales (instancias)
> Galleta galleta1 = new Galleta("Chocolate", 5.0);  // Objeto 1
> Galleta galleta2 = new Galleta("Vainilla", 4.5);   // Objeto 2
> Galleta galleta3 = new Galleta("Fresa", 5.5);      // Objeto 3
> 
> // Cada objeto tiene sus propios valores pero comparten la estructura
> ```
>


---

## 🧮 Ejercicios Prácticos

> [!example]- 💪 Ejercicios de Práctica
> 
> **Nivel Básico:**
> 
> **1. Clase Rectangulo:**
> Crear una clase `Rectangulo` con:
> - Atributos: ancho, alto
> - Constructores: por defecto y parametrizado
> - Métodos: calcularArea(), calcularPerimetro(), esCuadrado()
> 
> **2. Clase Libro:**
> Crear una clase `Libro` con:
> - Atributos: título, autor, páginas, precio
> - Constructores: varios con sobrecarga
> - Métodos: mostrarInfo(), aplicarDescuento(porcentaje), esCaro() (>$50)
> 
> **3. Clase Persona:**
> Crear una clase `Persona` con:
> - Atributos: nombre, edad, altura, peso
> - Métodos: calcularIMC(), esMayorDeEdad(), presentarse()
> 
> **Nivel Intermedio:**
> 
> **4. Clase CuentaBancaria:**
> Implementar con:
> - Atributos: titular, numeroCuenta, saldo, PIN
> - Métodos: depositar(), retirar(), transferir(), consultarSaldo()
> - Validaciones: PIN correcto, saldo suficiente
> - Contador estático de cuentas creadas
> 
> **5. Clase Producto:**
> Crear un sistema de inventario con:
> - Atributos: código, nombre, precio, stock, categoría
> - Métodos: vender(cantidad), reabastecer(cantidad), aplicarDescuento()
> - Método estático: compararPrecios(producto1, producto2)
> 
> **6. Clase Fecha:**
> Implementar una clase para manejar fechas:
> - Atributos: día, mes, año
> - Validación en constructor
> - Métodos: esBisiesto(), diasDelMes(), esValida(), compararCon(otraFecha)
> 
> **Nivel Avanzado:**
> 
> **7. Clase Empleado:**
> Sistema completo de empleados:
> - Atributos: nombre, cargo, salario, antiguedad, departamento
> - Métodos: calcularSalarioAnual(), aplicarAumento(), obtenerBono()
> - Método estático: empleadoMejorPagado(array de empleados)
> - Contador de empleados por departamento
> 
> **8. Clase Vector2D:**
> Crear una clase para vectores matemáticos:
> - Atributos: x, y
> - Métodos: sumar(otroVector), restar(), multiplicarEscalar(), magnitud()
> - Método estático: distancia(vector1, vector2)
> 
> **9. Sistema de Calificaciones:**
> Crear dos clases relacionadas:
> - Clase `Materia`: nombre, código, créditos
> - Clase `Estudiante`: con array de materias y calificaciones
> - Métodos para calcular promedio ponderado, mejor materia, peor materia

---

## 🎨 Ejemplo Completo Adicional: Clase Producto

> [!example]- 🛒 Sistema de Gestión de Productos
> 
> ```java
> /**
>  * Clase que representa un producto en un sistema de inventario
>  */
> public class Producto {
>     
>     // ============================================
>     // ATRIBUTOS
>     // ============================================
>     private String codigo;
>     private String nombre;
>     private double precio;
>     private int stock;
>     private String categoria;
>     private boolean disponible;
>     
>     // Atributos estáticos
>     private static int totalProductos = 0;
>     private static final double IVA = 0.12;
>     private static final int STOCK_MINIMO = 5;
>     
>     // ============================================
>     // CONSTRUCTORES
>     // ============================================
>     
>     public Producto() {
>         this.codigo = generarCodigoAutomatico();
>         this.nombre = "Producto sin nombre";
>         this.precio = 0.0;
>         this.stock = 0;
>         this.categoria = "General";
>         this.disponible = false;
>         totalProductos++;
>     }
>     
>     public Producto(String nombre, double precio) {
>         this();
>         setNombre(nombre);
>         setPrecio(precio);
>     }
>     
>     public Producto(String nombre, double precio, int stock, String categoria) {
>         this(nombre, precio);
>         setStock(stock);
>         setCategoria(categoria);
>     }
>     
>     // ============================================
>     // GETTERS Y SETTERS
>     // ============================================
>     
>     public String getCodigo() {
>         return codigo;
>     }
>     
>     public String getNombre() {
>         return nombre;
>     }
>     
>     public void setNombre(String nombre) {
>         if (nombre != null && !nombre.trim().isEmpty()) {
>             this.nombre = nombre.trim();
>         }
>     }
>     
>     public double getPrecio() {
>         return precio;
>     }
>     
>     public void setPrecio(double precio) {
>         if (precio >= 0) {
>             this.precio = precio;
>             actualizarDisponibilidad();
>         } else {
>             throw new IllegalArgumentException("El precio no puede ser negativo");
>         }
>     }
>     
>     public int getStock() {
>         return stock;
>     }
>     
>     public void setStock(int stock) {
>         if (stock >= 0) {
>             this.stock = stock;
>             actualizarDisponibilidad();
>         } else {
>             throw new IllegalArgumentException("El stock no puede ser negativo");
>         }
>     }
>     
>     public String getCategoria() {
>         return categoria;
>     }
>     
>     public void setCategoria(String categoria) {
>         if (categoria != null && !categoria.trim().isEmpty()) {
>             this.categoria = categoria.trim();
>         }
>     }
>     
>     public boolean isDisponible() {
>         return disponible;
>     }
>     
>     // ============================================
>     // MÉTODOS DE INSTANCIA
>     // ============================================
>     
>     /**
>      * Actualiza la disponibilidad según precio y stock
>      */
>     private void actualizarDisponibilidad() {
>         this.disponible = (this.precio > 0 && this.stock > 0);
>     }
>     
>     /**
>      * Calcula el precio con IVA incluido
>      */
>     public double getPrecioConIVA() {
>         return precio * (1 + IVA);
>     }
>     
>     /**
>      * Verifica si el stock está bajo
>      */
>     public boolean stockBajo() {
>         return stock > 0 && stock <= STOCK_MINIMO;
>     }
>     
>     /**
>      * Verifica si el producto está agotado
>      */
>     public boolean agotado() {
>         return stock == 0;
>     }
>     
>     /**
>      * Vende una cantidad de productos
>      */
>     public boolean vender(int cantidad) {
>         if (cantidad <= 0) {
>             System.out.println("Cantidad inválida");
>             return false;
>         }
>         
>         if (!disponible) {
>             System.out.println("Producto no disponible");
>             return false;
>         }
>         
>         if (cantidad > stock) {
>             System.out.println("Stock insuficiente. Disponible: " + stock);
>             return false;
>         }
>         
>         stock -= cantidad;
>         actualizarDisponibilidad();
>         System.out.println("Venta realizada: " + cantidad + " unidades");
>         
>         if (stockBajo()) {
>             System.out.println("⚠️ ALERTA: Stock bajo del producto " + nombre);
>         }
>         
>         return true;
>     }
>     
>     /**
>      * Reabastece el inventario
>      */
>     public void reabastecer(int cantidad) {
>         if (cantidad > 0) {
>             stock += cantidad;
>             actualizarDisponibilidad();
>             System.out.println("Reabastecimiento: +" + cantidad + " unidades. " +
>                              "Nuevo stock: " + stock);
>         }
>     }
>     
>     /**
>      * Aplica un descuento porcentual al precio
>      */
>     public void aplicarDescuento(double porcentaje) {
>         if (porcentaje > 0 && porcentaje <= 100) {
>             double descuento = precio * (porcentaje / 100.0);
>             precio -= descuento;
>             System.out.printf("Descuento aplicado: %.0f%% (-$%.2f). " +
>                             "Nuevo precio: $%.2f\n", 
>                             porcentaje, descuento, precio);
>         } else {
>             System.out.println("Porcentaje de descuento inválido");
>         }
>     }
>     
>     /**
>      * Calcula el valor total del inventario de este producto
>      */
>     public double valorInventario() {
>         return precio * stock;
>     }
>     
>     /**
>      * Muestra información detallada del producto
>      */
>     public void mostrarInfo() {
>         System.out.println("╔════════════════════════════════════════╗");
>         System.out.println("║       INFORMACIÓN DEL PRODUCTO         ║");
>         System.out.println("╠════════════════════════════════════════╣");
>         System.out.println("║ Código: " + codigo);
>         System.out.println("║ Nombre: " + nombre);
>         System.out.printf("║ Precio: $%.2f\n", precio);
>         System.out.printf("║ Precio con IVA: $%.2f\n", getPrecioConIVA());
>         System.out.println("║ Stock: " + stock + " unidades");
>         System.out.println("║ Categoría: " + categoria);
>         System.out.println("║ Disponible: " + (disponible ? "Sí" : "No"));
>         
>         if (stockBajo()) {
>             System.out.println("║ Estado: ⚠️ STOCK BAJO");
>         } else if (agotado()) {
>             System.out.println("║ Estado: ❌ AGOTADO");
>         } else {
>             System.out.println("║ Estado: ✅ DISPONIBLE");
>         }
>         
>         System.out.printf("║ Valor en inventario: $%.2f\n", valorInventario());
>         System.out.println("╚════════════════════════════════════════╝");
>     }
>     
>     @Override
>     public String toString() {
>         return String.format("Producto{codigo='%s', nombre='%s', " +
>                            "precio=%.2f, stock=%d, categoria='%s'}",
>                            codigo, nombre, precio, stock, categoria);
>     }
>     
>     // ============================================
>     // MÉTODOS ESTÁTICOS
>     // ============================================
>     
>     /**
>      * Genera un código automático para el producto
>      */
>     private static String generarCodigoAutomatico() {
>         return "PROD-" + String.format("%04d", totalProductos + 1);
>     }
>     
>     /**
>      * Obtiene el total de productos creados
>      */
>     public static int getTotalProductos() {
>         return totalProductos;
>     }
>     
>     /**
>      * Obtiene el valor del IVA
>      */
>     public static double getIVA() {
>         return IVA;
>     }
>     
>     /**
>      * Compara precios de dos productos
>      */
>     public static Producto masCaro(Producto p1, Producto p2) {
>         if (p1 == null) return p2;
>         if (p2 == null) return p1;
>         return (p1.precio >= p2.precio) ? p1 : p2;
>     }
>     
>     /**
>      * Calcula el precio promedio de un array de productos
>      */
>     public static double precioPromedio(Producto[] productos) {
>         if (productos == null || productos.length == 0) {
>             return 0.0;
>         }
>         
>         double suma = 0;
>         int contador = 0;
>         
>         for (Producto p : productos) {
>             if (p != null) {
>                 suma += p.precio;
>                 contador++;
>             }
>         }
>         
>         return (contador > 0) ? suma / contador : 0.0;
>     }
>     
>     /**
>      * Encuentra el producto con mayor stock
>      */
>     public static Producto mayorStock(Producto[] productos) {
>         if (productos == null || productos.length == 0) {
>             return null;
>         }
>         
>         Producto mayor = productos[0];
>         for (Producto p : productos) {
>             if (p != null && p.stock > mayor.stock) {
>                 mayor = p;
>             }
>         }
>         
>         return mayor;
>     }
> }
> ```
> 
> **Programa de prueba:**
> ```java
> public class PruebaProducto {
>     public static void main(String[] args) {
>         System.out.println("=== SISTEMA DE GESTIÓN DE PRODUCTOS ===\n");
>         
>         // Crear productos
>         Producto p1 = new Producto("Laptop Dell", 850.00, 15, "Electrónica");
>         Producto p2 = new Producto("Mouse Logitech", 25.50, 50, "Periféricos");
>         Producto p3 = new Producto("Teclado Mecánico", 120.00, 8, "Periféricos");
>         Producto p4 = new Producto("Monitor 24\"", 280.00, 3, "Electrónica");
>         
>         // Mostrar información
>         p1.mostrarInfo();
>         System.out.println();
>         
>         // Realizar ventas
>         System.out.println("=== OPERACIONES DE VENTA ===");
>         p1.vender(5);
>         p2.vender(25);
>         p4.vender(2);  // Debería generar alerta de stock bajo
>         System.out.println();
>         
>         // Aplicar descuentos
>         System.out.println("=== APLICAR DESCUENTOS ===");
>         p2.aplicarDescuento(15);
>         System.out.println();
>         
>         // Reabastecer
>         System.out.println("=== REABASTECIMIENTO ===");
>         p4.reabastecer(20);
>         System.out.println();
>         
>         // Métodos estáticos
>         System.out.println("=== ESTADÍSTICAS GENERALES ===");
>         System.out.println("Total de productos: " + Producto.getTotalProductos());
>         System.out.println("IVA vigente: " + (Producto.getIVA() * 100) + "%");
>         
>         Producto[] productos = {p1, p2, p3, p4};
>         double promedio = Producto.precioPromedio(productos);
>         System.out.printf("Precio promedio: $%.2f\n", promedio);
>         
>         Producto caro = Producto.masCaro(p1, p3);
>         System.out.println("Producto más caro entre Laptop y Teclado: " + 
>                          caro.getNombre());
>         
>         Producto mayor = Producto.mayorStock(productos);
>         System.out.println("Producto con mayor stock: " + mayor.getNombre() + 
>                          " (" + mayor.getStock() + " unidades)");
>         
>         // Mostrar estado final
>         System.out.println("\n=== ESTADO FINAL DE PRODUCTOS ===");
>         for (Producto p : productos) {
>             System.out.println(p);
>         }
>     }
> }
> ```

---

## 🎯 Conceptos Importantes para Recordar

> [!warning]- 🔥 Puntos Clave
> 
> **1. Una clase es una plantilla, un objeto es una instancia**
> ```java
> // Clase: la receta
> class Galleta { }
> 
> // Objetos: las galletas individuales
> Galleta g1 = new Galleta();
> Galleta g2 = new Galleta();
> ```
> 
> **2. Los atributos deben ser private (encapsulamiento)**
> ```java
> // ✅ CORRECTO
> private String nombre;
> public String getNombre() { return nombre; }
> 
> // ❌ EVITAR
> public String nombre;  // Rompe encapsulamiento
> ```
> 
> **3. Los constructores NO tienen tipo de retorno**
> ```java
> // ✅ CORRECTO
> public MiClase() { }
> 
> // ❌ ERROR
> public void MiClase() { }  // Esto es un método, no constructor
> ```
> 
> **4. Usar `this` para diferenciar atributos de parámetros**
> ```java
> public void setNombre(String nombre) {
>     this.nombre = nombre;  // this.nombre = atributo
>                            // nombre = parámetro
> }
> ```
> 
> **5. Los métodos static NO pueden acceder a atributos de instancia**
> ```java
> private int edad;  // Atributo de instancia
> 
> public static void metodoEstatico() {
>     // System.out.println(edad);  // ❌ ERROR
> }
> ```
> 
> **6. Sobrecarga = mismo nombre, diferentes parámetros**
> ```java
> public void metodo(int a) { }
> public void metodo(double a) { }
> public void metodo(int a, int b) { }
> ```
> 
> **7. Validar datos en constructores y setters**
> ```java
> public void setEdad(int edad) {
>     if (edad >= 0 && edad <= 150) {
>         this.edad = edad;
>     } else {
>         throw new IllegalArgumentException("Edad inválida");
>     }
> }
> ```
> 
> **8. null vs objeto sin inicializar**
> ```java
> Estudiante e1;           // No inicializada
> Estudiante e2 = null;    // Referencia nula
> Estudiante e3 = new Estudiante();  // Objeto creado
> 
> // e1.getNombre();  // ❌ Error: variable no inicializada
> // e2.getNombre();  // ❌ Error: NullPointerException
> e3.getNombre();     // ✅ OK
> ```

---

## 🔗 Resumen Visual

```mermaid
classDiagram
    class Estudiante {
        -String nombre
        -String apellido
        -int edad
        -double promedio
        -int creditos
        +static int totalEstudiantes
        +static final int CREDITOS_GRADUACION
        
        +Estudiante()
        +Estudiante(String, String, int)
        +Estudiante(String, String, int, double)
        +Estudiante(Estudiante)
        
        +getNombre() String
        +setNombre(String) void
        +getEdad() int
        +setEdad(int) void
        +getNombreCompleto() String
        +calcularPromedio() double
        +puedeGraduarse() boolean
        +mostrarInformacion() void
        
        +static getTotalEstudiantes() int
        +static mejorPromedio(Estudiante, Estudiante) Estudiante
    }
    
    note for Estudiante "Atributos privados\nConstructores sobrecargados\nMétodos de instancia y estáticos\nGetters y Setters"
````

---

## 📚 Conexiones con Temas Siguientes

> [!quote]- 🌐 ¿Qué Viene Después?
> 
> **Ya dominaste:**
> 
> - ✅ Estructura general de programas Java
> - ✅ Tipos de datos y operadores
> - ✅ Estructuras de control
> - ✅ Definición de clases y atributos
> - ✅ Constructores y sobrecarga
> - ✅ Métodos y comportamientos
> - ✅ Getters y Setters
> 
> **Próximos temas:**
> 
> 1. **[[Encapsulamiento]]** - Profundizar en modificadores de acceso
>     - public, private, protected, package-private
>     - Principio de ocultamiento de información
>     - Diseño de APIs limpias
> 2. **[[Modificador Static]]** - Variables y métodos de clase
>     - Diferencia entre static y de instancia
>     - Bloques static
>     - Patrones de diseño con static
> 3. **[[Relaciones entre Clases]]** - Composición y Agregación
>     - Has-A relationship
>     - Diseño orientado a objetos
> 4. **[[Herencia]]** - Reutilización de código
>     - Is-A relationship
>     - Clases padre e hija
>     - Palabra clave extends
> 5. **[[Polimorfismo]]** - Flexibilidad en el diseño
>     - Override de métodos
>     - Casting de objetos
> 6. **[[Clases Abstractas e Interfaces]]** - Contratos y abstracción
>     - Definir comportamientos comunes
>     - Implementación de interfaces

---

## 🧪 Ejercicio Final Integrador

> [!example]- 🎯 Proyecto: Sistema de Biblioteca
> 
> **Objetivo:** Crear un sistema de gestión de biblioteca con las siguientes clases:
> 
> **Clase Libro:**
> 
> - Atributos: ISBN, título, autor, añoPublicacion, numeroPaginas, disponible
> - Constructores múltiples
> - Métodos: prestar(), devolver(), mostrarInfo()
> - Validaciones apropiadas
> 
> **Clase Usuario:**
> 
> - Atributos: id, nombre, email, librosPrestados (array), fechaRegistro
> - Constructores con validación
> - Métodos: prestarLibro(Libro), devolverLibro(Libro), listarLibros()
> - Límite de 3 libros prestados simultáneamente
> 
> **Clase Biblioteca:**
> 
> - Atributos: nombre, direccion, catalogo (array de Libros)
> - Métodos: agregarLibro(), buscarPorTitulo(), buscarPorAutor()
> - Método estático: generarReporte(Biblioteca)
> 
> **Requisitos:**
> 
> - Usar encapsulamiento apropiado
> - Implementar al menos 2 constructores por clase
> - Incluir validaciones en setters
> - Usar sobrecarga de métodos
> - Documentar con Javadoc
> - Crear un programa main de prueba

---

**Tags:** #java #poo #clases #objetos #atributos #constructores #métodos #encapsulamiento #getters-setters #sobrecarga #static #instancia #university #programacion-orientada-objetos