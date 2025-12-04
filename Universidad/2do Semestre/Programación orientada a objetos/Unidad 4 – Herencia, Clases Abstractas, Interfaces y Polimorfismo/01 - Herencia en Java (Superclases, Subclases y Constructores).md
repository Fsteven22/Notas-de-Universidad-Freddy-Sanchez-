# 🌳 Herencia en Java

## 🎯 Introducción

> [!info]- 💡 ¿Qué es la Herencia? La **herencia** es uno de los pilares fundamentales de la POO que permite crear nuevas clases basadas en clases existentes, **reutilizando** y **extendiendo** su funcionalidad.
> 
> **Analogía:** Como un árbol genealógico
> 
> - **Padre (Superclase):** Transmite características a sus hijos
> - **Hijo (Subclase):** Hereda características y puede agregar las propias
> - Los hijos comparten rasgos con los padres, pero son únicos
> 
> **Relación "ES UN":**
> 
> - Un Perro **ES UN** Animal
> - Un Estudiante **ES UNA** Persona
> - Un Auto **ES UN** Vehículo
> 
> **Ventajas principales:**
> 
> - ✅ **Reutilización:** No repetir código
> - ✅ **Organización:** Jerarquías lógicas
> - ✅ **Mantenibilidad:** Cambios centralizados
> - ✅ **Extensibilidad:** Fácil agregar funcionalidad
> - ✅ **Polimorfismo:** Base para comportamiento flexible

---

## 📝 Sintaxis Básica

### Declaración de Herencia

> [!example]- 🔤 Palabra Clave `extends`
> 
> ```java
> // SUPERCLASE (Clase Padre/Base)
> public class Animal {
>     protected String nombre;
>     protected int edad;
>     
>     public Animal(String nombre, int edad) {
>         this.nombre = nombre;
>         this.edad = edad;
>     }
>     
>     public void comer() {
>         System.out.println(nombre + " está comiendo");
>     }
>     
>     public void dormir() {
>         System.out.println(nombre + " está durmiendo");
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("Nombre: " + nombre);
>         System.out.println("Edad: " + edad + " años");
>     }
> }
> 
> // SUBCLASE (Clase Hija/Derivada)
> public class Perro extends Animal {  // ← extends indica herencia
>     private String raza;
>     
>     public Perro(String nombre, int edad, String raza) {
>         super(nombre, edad);  // Llama al constructor del padre
>         this.raza = raza;
>     }
>     
>     // Método propio de Perro
>     public void ladrar() {
>         System.out.println(nombre + " dice: ¡Guau guau!");
>     }
>     
>     // Sobrescribir método heredado
>     @Override
>     public void mostrarInfo() {
>         super.mostrarInfo();  // Llama a la versión del padre
>         System.out.println("Raza: " + raza);
>     }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         Perro miPerro = new Perro("Max", 3, "Labrador");
>         
>         // Métodos heredados de Animal
>         miPerro.comer();      // "Max está comiendo"
>         miPerro.dormir();     // "Max está durmiendo"
>         
>         // Método propio de Perro
>         miPerro.ladrar();     // "Max dice: ¡Guau guau!"
>         
>         // Método sobrescrito
>         miPerro.mostrarInfo();
>         // Nombre: Max
>         // Edad: 3 años
>         // Raza: Labrador
>     }
> }
> ```
> 
> **Características clave:**
> 
> - Java solo permite **herencia simple** (una clase, una superclase directa)
> - Todas las clases heredan implícitamente de `Object`
> - Los miembros `private` NO se heredan (no son accesibles)
> - Los miembros `protected` SÍ se heredan y son accesibles en subclases

---

## 🏗️ Superclases y Subclases

### Jerarquía de Clases

> [!success]- 🌲 Árbol de Herencia
> 
> ```java
> // ========================
> // NIVEL 1: SUPERCLASE BASE
> // ========================
> public class Vehiculo {
>     protected String marca;
>     protected String modelo;
>     protected int año;
>     protected double precio;
>     
>     public Vehiculo(String marca, String modelo, int año, double precio) {
>         this.marca = marca;
>         this.modelo = modelo;
>         this.año = año;
>         this.precio = precio;
>     }
>     
>     public void encender() {
>         System.out.println("El vehículo está encendido");
>     }
>     
>     public void apagar() {
>         System.out.println("El vehículo está apagado");
>     }
>     
>     public void mostrarInfo() {
>         System.out.println(marca + " " + modelo + " (" + año + ")");
>         System.out.println("Precio: $" + precio);
>     }
> }
> 
> // ========================
> // NIVEL 2: SUBCLASES
> // ========================
> public class Auto extends Vehiculo {
>     private int numeroPuertas;
>     private String tipoTransmision;
>     
>     public Auto(String marca, String modelo, int año, double precio,
>                 int puertas, String transmision) {
>         super(marca, modelo, año, precio);
>         this.numeroPuertas = puertas;
>         this.tipoTransmision = transmision;
>     }
>     
>     public void abrirMaletero() {
>         System.out.println("Maletero abierto");
>     }
>     
>     @Override
>     public void mostrarInfo() {
>         super.mostrarInfo();
>         System.out.println("Puertas: " + numeroPuertas);
>         System.out.println("Transmisión: " + tipoTransmision);
>     }
> }
> 
> public class Motocicleta extends Vehiculo {
>     private String tipoMotor;
>     private int cilindrada;
>     
>     public Motocicleta(String marca, String modelo, int año, double precio,
>                        String tipoMotor, int cilindrada) {
>         super(marca, modelo, año, precio);
>         this.tipoMotor = tipoMotor;
>         this.cilindrada = cilindrada;
>     }
>     
>     public void hacerCaballito() {
>         System.out.println("¡Haciendo caballito!");
>     }
>     
>     @Override
>     public void mostrarInfo() {
>         super.mostrarInfo();
>         System.out.println("Motor: " + tipoMotor);
>         System.out.println("Cilindrada: " + cilindrada + " cc");
>     }
> }
> 
> // ========================
> // NIVEL 3: SUBCLASES DE SUBCLASES
> // ========================
> public class AutoDeportivo extends Auto {
>     private int velocidadMaxima;
>     private double aceleracion0a100;
>     
>     public AutoDeportivo(String marca, String modelo, int año, double precio,
>                          int puertas, String transmision,
>                          int velocidadMax, double aceleracion) {
>         super(marca, modelo, año, precio, puertas, transmision);
>         this.velocidadMaxima = velocidadMax;
>         this.aceleracion0a100 = aceleracion;
>     }
>     
>     public void activarModoDeportivo() {
>         System.out.println("🏎️ Modo deportivo activado");
>     }
>     
>     @Override
>     public void mostrarInfo() {
>         super.mostrarInfo();
>         System.out.println("Velocidad máxima: " + velocidadMaxima + " km/h");
>         System.out.println("0-100 km/h: " + aceleracion0a100 + " segundos");
>     }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         System.out.println("=== AUTO NORMAL ===");
>         Auto auto = new Auto("Toyota", "Corolla", 2023, 25000, 4, "Automática");
>         auto.encender();        // Heredado de Vehiculo
>         auto.abrirMaletero();   // Propio de Auto
>         auto.mostrarInfo();
>         
>         System.out.println("\n=== MOTOCICLETA ===");
>         Motocicleta moto = new Motocicleta("Yamaha", "R1", 2024, 18000, 
>                                            "4 tiempos", 998);
>         moto.encender();        // Heredado de Vehiculo
>         moto.hacerCaballito();  // Propio de Motocicleta
>         moto.mostrarInfo();
>         
>         System.out.println("\n=== AUTO DEPORTIVO ===");
>         AutoDeportivo deportivo = new AutoDeportivo(
>             "Ferrari", "F8", 2024, 280000, 2, "Automática", 340, 2.9
>         );
>         deportivo.encender();              // De Vehiculo
>         deportivo.abrirMaletero();         // De Auto
>         deportivo.activarModoDeportivo();  // Propio
>         deportivo.mostrarInfo();
>     }
> }
> ```

---

## 🔧 Constructores en Herencia

### La Palabra Clave `super`

> [!warning]- ⚡ Constructor de la Superclase **Reglas importantes:**
> 
> - La **primera línea** de un constructor debe ser `super()` o `this()`
> - Si no se especifica, Java llama automáticamente a `super()` (sin argumentos)
> - Si la superclase NO tiene constructor sin argumentos, DEBES llamar explícitamente a `super(args)`
> 
> ```java
> public class Persona {
>     protected String nombre;
>     protected int edad;
>     
>     // Constructor con parámetros
>     public Persona(String nombre, int edad) {
>         System.out.println("Constructor Persona ejecutado");
>         this.nombre = nombre;
>         this.edad = edad;
>     }
>     
>     public void presentarse() {
>         System.out.println("Hola, soy " + nombre);
>     }
> }
> 
> public class Estudiante extends Persona {
>     private String carrera;
>     private double promedio;
>     
>     // ✅ CORRECTO - Llama explícitamente a super
>     public Estudiante(String nombre, int edad, String carrera, double promedio) {
>         super(nombre, edad);  // ← DEBE ser la primera línea
>         System.out.println("Constructor Estudiante ejecutado");
>         this.carrera = carrera;
>         this.promedio = promedio;
>     }
>     
>     // ❌ ERROR - Si Persona no tiene constructor sin argumentos
>     // public Estudiante(String carrera) {
>     //     // Java intenta llamar super() automáticamente
>     //     // Error: no existe Persona()
>     //     this.carrera = carrera;
>     // }
>     
>     @Override
>     public void presentarse() {
>         super.presentarse();  // Llama al método del padre
>         System.out.println("Estudio " + carrera);
>         System.out.println("Mi promedio es: " + promedio);
>     }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         System.out.println("Creando estudiante:");
>         Estudiante est = new Estudiante("Ana", 20, "Ingeniería", 9.5);
>         // Salida:
>         // Constructor Persona ejecutado
>         // Constructor Estudiante ejecutado
>         
>         System.out.println("\nPresentación:");
>         est.presentarse();
>         // Hola, soy Ana
>         // Estudio Ingeniería
>         // Mi promedio es: 9.5
>     }
> }
> ```

### Orden de Ejecución de Constructores

> [!info]- 📋 Cadena de Constructores
> 
> ```java
> public class A {
>     public A() {
>         System.out.println("1. Constructor A");
>     }
> }
> 
> public class B extends A {
>     public B() {
>         // super() se llama implícitamente aquí
>         System.out.println("2. Constructor B");
>     }
> }
> 
> public class C extends B {
>     public C() {
>         // super() se llama implícitamente aquí
>         System.out.println("3. Constructor C");
>     }
> }
> 
> // USO:
> C objeto = new C();
> // Salida:
> // 1. Constructor A
> // 2. Constructor B
> // 3. Constructor C
> 
> // ⚠️ Los constructores se ejecutan desde la raíz hacia las hojas
> ```
> 
> **Orden completo de inicialización:**
> 
> ```java
> public class Padre {
>     private int x = inicializarX();  // 2. Variables de instancia del padre
>     
>     static {
>         System.out.println("1. Bloque static del padre");
>     }
>     
>     {
>         System.out.println("3. Bloque de inicialización del padre");
>     }
>     
>     public Padre() {
>         System.out.println("4. Constructor del padre");
>     }
>     
>     private int inicializarX() {
>         System.out.println("2. Inicializar variable del padre");
>         return 10;
>     }
> }
> 
> public class Hijo extends Padre {
>     private int y = inicializarY();  // 6. Variables de instancia del hijo
>     
>     static {
>         System.out.println("5. Bloque static del hijo");
>     }
>     
>     {
>         System.out.println("7. Bloque de inicialización del hijo");
>     }
>     
>     public Hijo() {
>         System.out.println("8. Constructor del hijo");
>     }
>     
>     private int inicializarY() {
>         System.out.println("6. Inicializar variable del hijo");
>         return 20;
>     }
> }
> 
> // USO:
> Hijo h = new Hijo();
> // Orden de ejecución exacto (ver números)
> ```

---

## 🔒 Modificadores de Acceso en Herencia

### Visibilidad de Miembros Heredados

> [!tip]- 🔍 Tabla de Acceso
> 
> |Modificador|Misma Clase|Subclase (mismo paquete)|Subclase (otro paquete)|Cualquier Clase|
> |---|---|---|---|---|
> |**private**|✅|❌|❌|❌|
> |**default**|✅|✅|❌|❌|
> |**protected**|✅|✅|✅|❌|
> |**public**|✅|✅|✅|✅|
> 
> **Ejemplo práctico:**
> 
> ```java
> // Paquete: com.ejemplo.animales
> public class Animal {
>     private String id;              // NO heredable
>     String habitat;                 // Heredable solo en mismo paquete
>     protected String nombre;        // Heredable siempre
>     public int edad;                // Heredable y accesible siempre
>     
>     private void metodoPrivado() {
>         System.out.println("Solo en Animal");
>     }
>     
>     protected void metodoProtegido() {
>         System.out.println("Visible en subclases");
>     }
>     
>     public void metodoPublico() {
>         System.out.println("Visible para todos");
>     }
> }
> 
> // Paquete: com.ejemplo.animales (mismo paquete)
> public class Perro extends Animal {
>     public void probar() {
>         // this.id = "123";              // ❌ Error: private no se hereda
>         this.habitat = "Casa";           // ✅ OK: default en mismo paquete
>         this.nombre = "Max";             // ✅ OK: protected
>         this.edad = 3;                   // ✅ OK: public
>         
>         // metodoPrivado();              // ❌ Error: private
>         metodoProtegido();               // ✅ OK: protected
>         metodoPublico();                 // ✅ OK: public
>     }
> }
> 
> // Paquete: com.ejemplo.mascotas (otro paquete)
> import com.ejemplo.animales.Animal;
> 
> public class Gato extends Animal {
>     public void probar() {
>         // this.habitat = "Jardín";      // ❌ Error: default no visible
>         this.nombre = "Misu";            // ✅ OK: protected
>         this.edad = 2;                   // ✅ OK: public
>         
>         metodoProtegido();               // ✅ OK: protected
>         metodoPublico();                 // ✅ OK: public
>     }
> }
> ```

---

## 🎭 Sobrescritura de Métodos (`@Override`)

### Reglas de Sobrescritura

> [!success]- ✏️ Method Overriding **Sobrescribir** = Redefinir un método heredado con nueva implementación
> 
> **Reglas obligatorias:**
> 
> 1. Misma **firma** (nombre y parámetros)
> 2. Mismo **tipo de retorno** (o covariante)
> 3. No puede ser **más restrictivo** en acceso
> 4. No puede lanzar **más excepciones checked**
> 5. Usar anotación `@Override` (recomendado)
> 
> ```java
> public class Figura {
>     protected String color;
>     
>     public Figura(String color) {
>         this.color = color;
>     }
>     
>     // Método para sobrescribir
>     public double calcularArea() {
>         return 0.0;
>     }
>     
>     public void dibujar() {
>         System.out.println("Dibujando figura de color " + color);
>     }
>     
>     // Método final - NO se puede sobrescribir
>     public final void identificar() {
>         System.out.println("Soy una figura");
>     }
> }
> 
> public class Circulo extends Figura {
>     private double radio;
>     
>     public Circulo(String color, double radio) {
>         super(color);
>         this.radio = radio;
>     }
>     
>     // ✅ CORRECTO - Sobrescritura válida
>     @Override
>     public double calcularArea() {
>         return Math.PI * radio * radio;
>     }
>     
>     // ✅ CORRECTO - Sobrescritura válida
>     @Override
>     public void dibujar() {
>         super.dibujar();  // Llama a la versión del padre
>         System.out.println("Es un círculo de radio " + radio);
>     }
>     
>     // ❌ ERROR - No se puede sobrescribir método final
>     // @Override
>     // public void identificar() { }
> }
> 
> public class Rectangulo extends Figura {
>     private double ancho;
>     private double alto;
>     
>     public Rectangulo(String color, double ancho, double alto) {
>         super(color);
>         this.ancho = ancho;
>         this.alto = alto;
>     }
>     
>     @Override
>     public double calcularArea() {
>         return ancho * alto;
>     }
>     
>     @Override
>     public void dibujar() {
>         System.out.println("Dibujando rectángulo " + ancho + "x" + alto);
>     }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         Circulo circulo = new Circulo("Rojo", 5.0);
>         Rectangulo rect = new Rectangulo("Azul", 4.0, 6.0);
>         
>         System.out.println("Área del círculo: " + circulo.calcularArea());
>         System.out.println("Área del rectángulo: " + rect.calcularArea());
>         
>         circulo.dibujar();
>         rect.dibujar();
>     }
> }
> ```

### Sobrescritura vs Sobrecarga

> [!note]- ⚖️ Overriding vs Overloading
> 
> **Sobrescritura (Overriding):**
> 
> - Mismo nombre, mismos parámetros
> - En herencia (subclase redefine método del padre)
> - Polimorfismo en tiempo de ejecución
> 
> **Sobrecarga (Overloading):**
> 
> - Mismo nombre, diferentes parámetros
> - En la misma clase o en herencia
> - Polimorfismo en tiempo de compilación
> 
> ```java
> public class Calculadora {
>     // SOBRECARGA - Diferentes parámetros
>     public int sumar(int a, int b) {
>         return a + b;
>     }
>     
>     public double sumar(double a, double b) {
>         return a + b;
>     }
>     
>     public int sumar(int a, int b, int c) {
>         return a + b + c;
>     }
> }
> 
> public class CalculadoraCientifica extends Calculadora {
>     // SOBRESCRITURA - Misma firma que el padre
>     @Override
>     public int sumar(int a, int b) {
>         System.out.println("Suma científica");
>         return super.sumar(a, b);
>     }
>     
>     // SOBRECARGA - Nuevo método con diferentes parámetros
>     public double sumar(double a, double b, double c) {
>         return a + b + c;
>     }
> }
> ```

---

## 🚫 La Palabra Clave `final`

### Clases y Métodos Finales

> [!warning]- 🔒 Prevenir Herencia y Sobrescritura
> 
> **`final` en clases:**
> 
> ```java
> // Clase final - NO se puede heredar
> public final class String {
>     // Implementación...
> }
> 
> // ❌ ERROR - No se puede heredar de clase final
> // public class MiString extends String { }
> 
> // Ejemplos de clases final en Java:
> // - String
> // - Math
> // - System
> // - Todos los enums
> // - Todas las clases wrapper (Integer, Double, etc.)
> ```
> 
> **`final` en métodos:**
> 
> ```java
> public class CuentaBancaria {
>     private double saldo;
>     
>     // Método final - NO se puede sobrescribir
>     public final void validarSaldo() {
>         if (saldo < 0) {
>             throw new IllegalStateException("Saldo negativo no permitido");
>         }
>     }
>     
>     // Método normal - Sí se puede sobrescribir
>     public void retirar(double monto) {
>         validarSaldo();
>         if (monto <= saldo) {
>             saldo -= monto;
>         }
>     }
> }
> 
> public class CuentaAhorro extends CuentaBancaria {
>     // ❌ ERROR - No se puede sobrescribir método final
>     // @Override
>     // public void validarSaldo() { }
>     
>     // ✅ OK - Se puede sobrescribir método normal
>     @Override
>     public void retirar(double monto) {
>         System.out.println("Retiro de cuenta de ahorro");
>         super.retirar(monto);
>     }
> }
> ```
> 
> **Cuándo usar `final`:**
> 
> - ✅ Clases de utilidad (Math, Collections)
> - ✅ Clases inmutables (String, Integer)
> - ✅ Métodos críticos de seguridad
> - ✅ Métodos llamados en constructores
> - ✅ Prevenir mal uso de herencia

---

## 🎨 Ejemplo Completo: Sistema de Empleados

> [!example]- 👔 Jerarquía Completa con Herencia
> 
> ```java
> // ===========================
> // SUPERCLASE BASE
> // ===========================
> public class Empleado {
>     protected String nombre;
>     protected String id;
>     protected double salarioBase;
>     protected int añosExperiencia;
>     
>     public Empleado(String nombre, String id, double salarioBase, int experiencia) {
>         this.nombre = nombre;
>         this.id = id;
>         this.salarioBase = salarioBase;
>         this.añosExperiencia = experiencia;
>         System.out.println("✓ Empleado base creado: " + nombre);
>     }
>     
>     // Método para calcular salario (será sobrescrito)
>     public double calcularSalario() {
>         return salarioBase;
>     }
>     
>     // Método para bonificación por experiencia
>     protected double calcularBonificacionExperiencia() {
>         return salarioBase * 0.02 * añosExperiencia;
>     }
>     
>     public void trabajar() {
>         System.out.println(nombre + " está trabajando");
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("\n=== INFORMACIÓN DEL EMPLEADO ===");
>         System.out.println("Nombre: " + nombre);
>         System.out.println("ID: " + id);
>         System.out.println("Salario base: $" + String.format("%.2f", salarioBase));
>         System.out.println("Experiencia: " + añosExperiencia + " años");
>         System.out.println("Salario total: $" + String.format("%.2f", calcularSalario()));
>     }
>     
>     // Getters
>     public String getNombre() { return nombre; }
>     public String getId() { return id; }
> }
> 
> // ===========================
> // SUBCLASE: PROGRAMADOR
> // ===========================
> public class Programador extends Empleado {
>     private String lenguajePrincipal;
>     private int lineasCodigoPorDia;
>     private double bonoProyecto;
>     
>     public Programador(String nombre, String id, double salarioBase, 
>                        int experiencia, String lenguaje, int lineasCodigo) {
>         super(nombre, id, salarioBase, experiencia);
>         this.lenguajePrincipal = lenguaje;
>         this.lineasCodigoPorDia = lineasCodigo;
>         this.bonoProyecto = 0;
>         System.out.println("  → Programador especializado en " + lenguaje);
>     }
>     
>     // Sobrescribir cálculo de salario
>     @Override
>     public double calcularSalario() {
>         double salario = salarioBase;
>         salario += calcularBonificacionExperiencia();
>         salario += bonoProyecto;
>         
>         // Bono por productividad
>         if (lineasCodigoPorDia > 500) {
>             salario += salarioBase * 0.10;
>         }
>         
>         return salario;
>     }
>     
>     // Método propio
>     public void programar() {
>         System.out.println(nombre + " está programando en " + lenguajePrincipal);
>     }
>     
>     public void asignarBonoProyecto(double bono) {
>         this.bonoProyecto = bono;
>         System.out.println("✓ Bono de proyecto asignado: $" + bono);
>     }
>     
>     @Override
>     public void mostrarInfo() {
>         super.mostrarInfo();
>         System.out.println("Lenguaje: " + lenguajePrincipal);
>         System.out.println("Líneas/día: " + lineasCodigoPorDia);
>         if (bonoProyecto > 0) {
>             System.out.println("Bono proyecto: $" + String.format("%.2f", bonoProyecto));
>         }
>     }
> }
> 
> // ===========================
> // SUBCLASE: GERENTE
> // ===========================
> public class Gerente extends Empleado {
>     private String departamento;
>     private int numeroEmpleados;
>     private double bonoGerencial;
>     
>     public Gerente(String nombre, String id, double salarioBase, 
>                    int experiencia, String departamento, int numEmpleados) {
>         super(nombre, id, salarioBase, experiencia);
>         this.departamento = departamento;
>         this.numeroEmpleados = numEmpleados;
>         this.bonoGerencial = salarioBase * 0.20;  // 20% extra
>         System.out.println("  → Gerente del departamento de " + departamento);
>     }
>     
>     @Override
>     public double calcularSalario() {
>         double salario = salarioBase;
>         salario += calcularBonificacionExperiencia();
>         salario += bonoGerencial;
>         
>         // Bono por equipo grande
>         if (numeroEmpleados > 10) {
>             salario += salarioBase * 0.15;
>         }
>         
>         return salario;
>     }
>     
>     public void dirigirReunion() {
>         System.out.println(nombre + " está dirigiendo una reunión en " + departamento);
>     }
>     
>     public void evaluarEmpleado(Empleado emp) {
>         System.out.println(nombre + " está evaluando a " + emp.getNombre());
>     }
>     
>     @Override
>     public void mostrarInfo() {
>         super.mostrarInfo();
>         System.out.println("Departamento: " + departamento);
>         System.out.println("Empleados a cargo: " + numeroEmpleados);
>         System.out.println("Bono gerencial: $" + String.format("%.2f", bonoGerencial));
>     }
> }
> 
> // ===========================
> // SUBCLASE: VENDEDOR
> // ===========================
> public class Vendedor extends Empleado {
>     private String region;
>     private double ventasMensuales;
>     private double comision;
>     
>     public Vendedor(String nombre, String id, double salarioBase, 
>                     int experiencia, String region) {
>         super(nombre, id, salarioBase, experiencia);
>         this.region = region;
>         this.ventasMensuales = 0;
>         this.comision = 0.05;  // 5% de comisión
>         System.out.println("  → Vendedor asignado a región " + region);
>     }
>     
>     @Override
>     public double calcularSalario() {
>         double salario = salarioBase;
>         salario += calcularBonificacionExperiencia();
>         salario += ventasMensuales * comision;
>         return salario;
>     }
>     
>     public void registrarVenta(double monto) {
>         ventasMensuales += monto;
>         System.out.println("✓ Venta registrada: $" + monto);
>         System.out.println("  Total del mes: $" + ventasMensuales);
>     }
>     
>     public void vender() {
>         System.out.println(nombre + " está vendiendo en la región " + region);
>     }
>     
>     @Override
>     public void mostrarInfo() {
>         super.mostrarInfo();
>         System.out.println("Región: " + region);
>         System.out.println("Ventas del mes: $" + String.format("%.2f", ventasMensuales));
>         System.out.println("Comisión: " + (comision * 100) + "%");
>     }
> }
> 
> // ===========================
> // SUBCLASE DE SUBCLASE
> // ===========================
> public class GerenteGeneral extends Gerente {
>     private double bonoEjecutivo;
>     private int numeroSucursales;
>     
>     public GerenteGeneral(String nombre, String id, double salarioBase, 
>                           int experiencia, int numSucursales) {
>         super(nombre, id, salarioBase, experiencia, "Dirección General", 50);
>         this.numeroSucursales = numSucursales;
>         this.bonoEjecutivo = salarioBase * 0.50;  // 50% extra
>         System.out.println("  → Gerente General con " + numSucursales + " sucursales");
>     }
>     
>     @Override
>     public double calcularSalario() {
>         double salario = super.calcularSalario();  // Usa cálculo de Gerente
>         salario += bonoEjecutivo;
>         
>         // Bono por cada sucursal
>         salario += numeroSucursales * 1000;
>         
>         return salario;
>     }
>     
>     public void planificarEstrategia() {
>         System.out.println(nombre + " está planificando estrategia corporativa");
>     }
>     
>     @Override
>     public void mostrarInfo() {
>         super.mostrarInfo();
>         System.out.println("Sucursales: " + numeroSucursales);
>         System.out.println("Bono ejecutivo: $" + String.format("%.2f", bonoEjecutivo));
>     }
> }
> 
> // ===========================
> // CLASE PRINCIPAL
> // ===========================
> public class SistemaEmpleados {
>     public static void main(String[] args) {
>         System.out.println("╔════════════════════════════════════════╗");
>         System.out.println("║   SISTEMA DE GESTIÓN DE EMPLEADOS     ║");
>         System.out.println("╚════════════════════════════════════════╝\n");
>         
>         // Crear diferentes tipos de empleados
>         System.out.println("--- CREANDO EMPLEADOS ---");
>         
>         Programador prog = new Programador(
>             "Ana García", "P001", 3000, 5, "Java", 600
>         );
>         
>         Gerente gerente = new Gerente(
>             "Carlos Ruiz", "G001", 5000, 10, "Desarrollo", 15
>         );
>         
>         Vendedor vendedor = new Vendedor(
>             "María López", "V001", 2000, 3, "Costa"
>         );
>         
>         GerenteGeneral gg = new GerenteGeneral(
>             "Roberto Sánchez", "GG001", 8000, 20, 5
>         );
>         
>         // Realizar actividades
>         System.out.println("\n--- ACTIVIDADES ---");
>         prog.programar();
>         prog.trabajar();  // Heredado de Empleado
>         prog.asignarBonoProyecto(500);
>         
>         System.out.println();
>         gerente.dirigirReunion();
>         gerente.evaluarEmpleado(prog);
>         
>         System.out.println();
>         vendedor.vender();
>         vendedor.registrarVenta(15000);
>         vendedor.registrarVenta(8000);
>         
>         System.out.println();
>         gg.planificarEstrategia();
>         gg.dirigirReunion();  // Heredado de Gerente
>         
>         // Mostrar información
>         System.out.println("\n--- INFORMACIÓN DETALLADA ---");
>         prog.mostrarInfo();
>         gerente.mostrarInfo();
>         vendedor.mostrarInfo();
>         gg.mostrarInfo();
>         
>         // Calcular nómina total
>         System.out.println("\n--- NÓMINA TOTAL ---");
>         double nominaTotal = prog.calcularSalario() + 
>                              gerente.calcularSalario() +
>                              vendedor.calcularSalario() +
>                              gg.calcularSalario();
>         System.out.println("Total nómina: $" + String.format("%.2f", nominaTotal));
>         
>         // Demostrar polimorfismo (se verá en próximo tema)
>         System.out.println("\n--- ARRAY POLIMÓRFICO ---");
>         Empleado[] empleados = {prog, gerente, vendedor, gg};
>         for (Empleado emp : empleados) {
>             System.out.println(emp.getNombre() + ": $" + 
>                                String.format("%.2f", emp.calcularSalario()));
>         }
>     }
> }
> ```

---

## ⚠️ Errores Comunes en Herencia

> [!warning]- 🚫 Errores Frecuentes y Soluciones
> 
> **1. No llamar al constructor del padre:**
> ```java
> // ❌ MAL
> public class Estudiante extends Persona {
>     private String carrera;
>     
>     public Estudiante(String nombre, String carrera) {
>         // super(nombre) falta
>         this.carrera = carrera;  // Error: nombre no inicializado
>     }
> }
> 
> // ✅ BIEN
> public class Estudiante extends Persona {
>     private String carrera;
>     
>     public Estudiante(String nombre, String carrera) {
>         super(nombre);  // Llamar primero
>         this.carrera = carrera;
>     }
> }
> ```
> 
> **2. Confundir sobrescritura con sobrecarga:**
> ```java
> public class Padre {
>     public void metodo(int x) {
>         System.out.println("Padre: " + x);
>     }
> }
> 
> // ❌ SOBRECARGA (no sobrescritura) - parámetro diferente
> public class Hijo extends Padre {
>     public void metodo(double x) {  // double != int
>         System.out.println("Hijo: " + x);
>     }
> }
> 
> Hijo h = new Hijo();
> h.metodo(5);     // Llama a Padre.metodo(int)
> h.metodo(5.0);   // Llama a Hijo.metodo(double)
> 
> // ✅ SOBRESCRITURA - misma firma
> public class Hijo extends Padre {
>     @Override
>     public void metodo(int x) {  // Mismo tipo
>         System.out.println("Hijo: " + x);
>     }
> }
> ```
> 
> **3. Intentar acceder a miembros private del padre:**
> ```java
> public class Padre {
>     private int x = 10;
>     protected int y = 20;
> }
> 
> public class Hijo extends Padre {
>     public void mostrar() {
>         // System.out.println(x);  // ❌ Error: x es private
>         System.out.println(y);     // ✅ OK: y es protected
>     }
> }
> ```
> 
> **4. Hacer el modificador más restrictivo:**
> ```java
> public class Padre {
>     public void metodo() { }
> }
> 
> // ❌ MAL - No se puede hacer más restrictivo
> public class Hijo extends Padre {
>     @Override
>     protected void metodo() { }  // Error de compilación
> }
> 
> // ✅ BIEN - Se puede mantener o hacer menos restrictivo
> public class Hijo extends Padre {
>     @Override
>     public void metodo() { }  // OK: mismo nivel
> }
> ```
> 
> **5. Confundir herencia con composición:**
> ```java
> // ❌ MAL USO DE HERENCIA
> class Stack extends ArrayList {  // Stack NO ES un ArrayList
>     // ...
> }
> 
> // ✅ USAR COMPOSICIÓN
> class Stack {
>     private ArrayList items = new ArrayList();  // TIENE un ArrayList
>     // ...
> }
> ```

---

## 🎯 Herencia vs Composición

### Cuándo Usar Cada Uno

> [!tip]- ⚖️ Decidir Entre Herencia y Composición
> 
> **Usar HERENCIA cuando:**
> - ✅ Relación "ES UN" clara y verdadera
> - ✅ La subclase es una especialización
> - ✅ Necesitas polimorfismo
> - ✅ Hay comportamiento común a reutilizar
> 
> **Ejemplo válido de herencia:**
> ```java
> // Perro ES UN Animal ✅
> public class Animal {
>     public void comer() { }
>     public void dormir() { }
> }
> 
> public class Perro extends Animal {
>     public void ladrar() { }
> }
> ```
> 
> **Usar COMPOSICIÓN cuando:**
> - ✅ Relación "TIENE UN"
> - ✅ Quieres reutilizar funcionalidad sin jerarquía
> - ✅ Necesitas mayor flexibilidad
> - ✅ Quieres cambiar comportamiento en tiempo de ejecución
> 
> **Ejemplo: composición preferible:**
> ```java
> // ❌ MAL: Auto NO ES UN Motor
> public class Auto extends Motor { }
> 
> // ✅ BIEN: Auto TIENE UN Motor
> public class Auto {
>     private Motor motor;  // Composición
>     
>     public Auto(Motor motor) {
>         this.motor = motor;
>     }
>     
>     public void encender() {
>         motor.arrancar();
>     }
> }
> ```
> 
> **Comparación práctica:**
> ```java
> // HERENCIA - Relación "ES UN"
> public abstract class Empleado {
>     protected String nombre;
>     protected double salario;
>     
>     public abstract double calcularSalario();
> }
> 
> public class Programador extends Empleado {  // ES UN Empleado
>     @Override
>     public double calcularSalario() {
>         return salario * 1.2;
>     }
> }
> 
> // COMPOSICIÓN - Relación "TIENE UN"
> public class Empleado {
>     private String nombre;
>     private CalculadoraSalario calculadora;  // TIENE UN calculadora
>     
>     public Empleado(CalculadoraSalario calc) {
>         this.calculadora = calc;
>     }
>     
>     public double calcularSalario() {
>         return calculadora.calcular();
>     }
>     
>     // Se puede cambiar el calculador en tiempo de ejecución
>     public void setCalculadora(CalculadoraSalario calc) {
>         this.calculadora = calc;
>     }
> }
> ```
> 
> **Regla general:** "Favor Composition over Inheritance" (Preferir composición sobre herencia)

---

## 📊 Jerarquías Profundas vs Planas

> [!note]- 🌳 Diseño de Jerarquías
> 
> **Jerarquía profunda (evitar):**
> ```java
> // ❌ Demasiado profundo - difícil de mantener
> class SerVivo { }
> class Animal extends SerVivo { }
> class Mamifero extends Animal { }
> class Carnivoro extends Mamifero { }
> class Felino extends Carnivoro { }
> class Gato extends Felino { }
> class GatoPersa extends Gato { }
> class GatoPersaDePeloLargo extends GatoPersa { }  // ¡8 niveles!
> ```
> 
> **Jerarquía plana (preferible):**
> ```java
> // ✅ Más plano - más fácil de entender
> class Animal { }
> class Perro extends Animal { }
> class Gato extends Animal { }
> class Pajaro extends Animal { }
> ```
> 
> **Recomendaciones:**
> - Máximo 3-4 niveles de herencia
> - Si necesitas más, considera composición o interfaces
> - Cada nivel debe agregar valor significativo

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica con Herencia
> 
> **Nivel Básico:**
> 
> 1. **Jerarquía de Figuras:**
>    - Clase base `Figura` con `calcularArea()` y `calcularPerimetro()`
>    - Subclases: `Circulo`, `Rectangulo`, `Triangulo`
> 
> 2. **Sistema de Vehículos:**
>    - Clase `Vehiculo` con atributos comunes
>    - Subclases: `Carro`, `Moto`, `Bicicleta`
>    - Cada una con métodos específicos
> 
> 3. **Instrumentos Musicales:**
>    - Clase `Instrumento` con `tocar()` y `afinar()`
>    - Subclases: `Guitarra`, `Piano`, `Bateria`
> 
> **Nivel Intermedio:**
> 
> 4. **Sistema Bancario:**
>    - Clase `CuentaBancaria` base
>    - Subclases: `CuentaAhorro`, `CuentaCorriente`, `CuentaNomina`
>    - Cada una con reglas de retiro y depósito diferentes
> 
> 5. **Tienda Online:**
>    - Clase `Producto` base
>    - Subclases: `Libro`, `Electronico`, `Ropa`
>    - Cada una con cálculo de precio diferente (descuentos, impuestos)
> 
> 6. **Sistema Educativo:**
>    - Clase `Persona` base
>    - Subclases: `Estudiante`, `Profesor`, `Administrativo`
>    - Incluir jerarquía de estudiantes (Pregrado, Postgrado)
> 
> **Nivel Avanzado:**
> 
> 7. **Juego de Rol (RPG):**
>    - Clase `Personaje` base
>    - Subclases: `Guerrero`, `Mago`, `Arquero`
>    - Sistema de combate y habilidades especiales
>    - Incluir inventario y equipamiento
> 
> 8. **Sistema de Transporte:**
>    - Jerarquía completa: `Vehiculo` → `VehiculoTerrestre/Aereo/Maritimo`
>    - Múltiples niveles de especialización
>    - Calcular costos de operación diferentes
> 
> 9. **Procesador de Documentos:**
>    - Clase `Documento` base
>    - Subclases: `PDF`, `Word`, `Excel`, `Texto`
>    - Métodos para abrir, guardar, convertir
> 
> 10. **Red Social:**
>     - Clase `Usuario` base
>     - Subclases: `UsuarioRegular`, `UsuarioPremium`, `Administrador`
>     - Sistema de permisos y funcionalidades

---

## 🔍 La Clase `Object`

### Raíz de Todas las Clases

> [!info]- 🌟 Todo Hereda de Object
> En Java, **todas** las clases heredan implícitamente de `java.lang.Object`
> 
> ```java
> // Estas tres declaraciones son equivalentes:
> public class MiClase { }
> public class MiClase extends Object { }
> public class MiClase extends java.lang.Object { }
> ```
> 
> **Métodos importantes de Object:**
> ```java
> public class Persona {
>     private String nombre;
>     private int edad;
>     
>     public Persona(String nombre, int edad) {
>         this.nombre = nombre;
>         this.edad = edad;
>     }
>     
>     // 1. toString() - Representación en String
>     @Override
>     public String toString() {
>         return "Persona{nombre='" + nombre + "', edad=" + edad + "}";
>     }
>     
>     // 2. equals() - Comparación de igualdad
>     @Override
>     public boolean equals(Object obj) {
>         if (this == obj) return true;
>         if (obj == null || getClass() != obj.getClass()) return false;
>         
>         Persona persona = (Persona) obj;
>         return edad == persona.edad && nombre.equals(persona.nombre);
>     }
>     
>     // 3. hashCode() - Código hash (importante para colecciones)
>     @Override
>     public int hashCode() {
>         int result = nombre.hashCode();
>         result = 31 * result + edad;
>         return result;
>     }
>     
>     // Otros métodos de Object que raramente se sobrescriben:
>     // - clone() - Clonar objeto
>     // - finalize() - Llamado por GC (deprecated)
>     // - getClass() - Obtener clase en runtime
>     // - notify(), notifyAll(), wait() - Sincronización de hilos
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         Persona p1 = new Persona("Ana", 25);
>         Persona p2 = new Persona("Ana", 25);
>         Persona p3 = p1;
>         
>         // toString()
>         System.out.println(p1);  // Persona{nombre='Ana', edad=25}
>         
>         // equals()
>         System.out.println(p1.equals(p2));  // true (mismo contenido)
>         System.out.println(p1 == p2);       // false (diferentes objetos)
>         System.out.println(p1 == p3);       // true (misma referencia)
>         
>         // hashCode()
>         System.out.println(p1.hashCode());  // Mismo que p2
>         System.out.println(p2.hashCode());
>     }
> }
> ```

---

## 💡 Mejores Prácticas

> [!success]- ✅ Recomendaciones para Herencia
> 
> **1. Usar @Override siempre:**
> ```java
> // ✅ BIEN - Detecta errores en tiempo de compilación
> @Override
> public String toString() {
>     return "...";
> }
> 
> // ❌ Sin @Override - error de tipeo no detectado
> public String tostring() {  // Letra minúscula - método nuevo, no sobrescribe
>     return "...";
> }
> ```
> 
> **2. Diseñar para herencia o prohibirla:**
> ```java
> // Opción 1: Diseñar para herencia
> public class Vehiculo {
>     protected String marca;  // protected para subclases
>     
>     // Documentar qué pueden sobrescribir
>     public void encender() {
>         validar();  // Llama a método sobrescribible
>     }
>     
>     protected void validar() {  // Protected, puede sobrescribirse
>         // Implementación
>     }
> }
> 
> // Opción 2: Prohibir herencia
> public final class Utilidad {  // final = no heredable
>     private Utilidad() { }  // Constructor privado
>     
>     public static void metodoEstatico() { }
> }
> ```
> 
> **3. No sobrescribir equals() sin hashCode():**
> ```java
> // ❌ MAL - Rompe contrato con HashMap/HashSet
> @Override
> public boolean equals(Object obj) {
>     // ...
> }
> // Falta hashCode()
> 
> // ✅ BIEN - Ambos juntos
> @Override
> public boolean equals(Object obj) { /* ... */ }
> 
> @Override
> public int hashCode() { /* ... */ }
> ```
> 
> **4. Llamar a super en sobrescrituras:**
> ```java
> // ✅ BIEN - Aprovechar lógica del padre
> @Override
> public void mostrarInfo() {
>     super.mostrarInfo();  // Ejecuta del padre primero
>     System.out.println("Info adicional");
> }
> ```
> 
> **5. Preferir composición sobre herencia:**
> ```java
> // ❌ Herencia forzada
> class Stack extends ArrayList { }
> 
> // ✅ Composición flexible
> class Stack {
>     private List items = new ArrayList();
> }
> ```

---

## 🔗 Conexión con Próximos Temas

> [!quote]- 🌟 Continuando el Aprendizaje
> **Has aprendido:**
> - ✅ Qué es la herencia y cuándo usarla
> - ✅ Superclases y subclases
> - ✅ Constructores y la palabra `super`
> - ✅ Sobrescritura de métodos con `@Override`
> - ✅ Modificadores de acceso en herencia
> - ✅ La palabra clave `final`
> - ✅ La clase `Object`
> 
> **Próximos temas relacionados:**
> - **[[Polimorfismo]]** - Usar herencia para flexibilidad
> - **[[Clases Abstractas]]** - Herencia con métodos abstractos
> - **[[Interfaces]]** - "Herencia" de comportamiento
> - **[[Casting]]** - Conversión entre tipos en jerarquías
> - **[[Design Patterns]]** - Patrones que usan herencia

---

**Tags:** #java #herencia #poo #superclase #subclase #extends #super #override #object #final
