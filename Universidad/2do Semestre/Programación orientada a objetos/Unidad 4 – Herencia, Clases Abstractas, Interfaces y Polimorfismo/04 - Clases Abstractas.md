# 🎭 Clases Abstractas en Java

## 🎯 Introducción

> [!info]- 💡 ¿Qué son las Clases Abstractas? Una **clase abstracta** es una clase que no puede ser instanciada directamente y sirve como plantilla para otras clases. Define un contrato parcial que las subclases deben completar.
> 
> **Analogía:** Como un plano arquitectónico
> 
> - **Plano (clase abstracta):** Define estructura general, pero no es una casa real
> - **Casa construida (clase concreta):** Implementación específica del plano
> 
> **Características principales:**
> 
> - **No instanciable:** No se pueden crear objetos directamente
> - **Puede tener métodos abstractos:** Sin implementación (solo firma)
> - **Puede tener métodos concretos:** Con implementación completa
> - **Puede tener atributos:** Como cualquier clase normal
> - **Soporta herencia:** Se extiende con `extends`

---

## 📝 Sintaxis Básica

### 🔷 Declaración de Clase Abstracta

> [!example]- 📋 Estructura Fundamental
> 
> ```java
> // Declaración con 'abstract'
> public abstract class Figura {
>     // Atributos (pueden ser privados, protected, public)
>     protected String color;
>     protected double x, y;
>     
>     // Constructor (sí puede tener constructores)
>     public Figura(String color, double x, double y) {
>         this.color = color;
>         this.x = x;
>         this.y = y;
>     }
>     
>     // Método abstracto (sin implementación)
>     public abstract double calcularArea();
>     public abstract double calcularPerimetro();
>     
>     // Método concreto (con implementación)
>     public void mostrarPosicion() {
>         System.out.println("Posición: (" + x + ", " + y + ")");
>     }
>     
>     // Getter/Setter normales
>     public String getColor() {
>         return color;
>     }
> }
> ```
> 
> **Reglas importantes:**
> 
> - Clase con `abstract` → No se puede instanciar
> - Método con `abstract` → No tiene cuerpo `{}`
> - Si una clase tiene método abstracto → La clase DEBE ser abstracta
> - Una clase abstracta puede NO tener métodos abstractos

### 🔶 Implementación de Subclases

> [!success]- ✅ Clases Concretas que Heredan
> 
> ```java
> // Subclase DEBE implementar todos los métodos abstractos
> public class Rectangulo extends Figura {
>     private double ancho;
>     private double alto;
>     
>     public Rectangulo(String color, double x, double y, 
>                      double ancho, double alto) {
>         super(color, x, y);  // Llamar constructor padre
>         this.ancho = ancho;
>         this.alto = alto;
>     }
>     
>     // ✅ OBLIGATORIO: Implementar métodos abstractos
>     @Override
>     public double calcularArea() {
>         return ancho * alto;
>     }
>     
>     @Override
>     public double calcularPerimetro() {
>         return 2 * (ancho + alto);
>     }
>     
>     // Puede agregar sus propios métodos
>     public double getDiagonal() {
>         return Math.sqrt(ancho * ancho + alto * alto);
>     }
> }
> 
> public class Circulo extends Figura {
>     private double radio;
>     
>     public Circulo(String color, double x, double y, double radio) {
>         super(color, x, y);
>         this.radio = radio;
>     }
>     
>     @Override
>     public double calcularArea() {
>         return Math.PI * radio * radio;
>     }
>     
>     @Override
>     public double calcularPerimetro() {
>         return 2 * Math.PI * radio;
>     }
> }
> ```

---

## 🎯 Ejemplo Completo: Sistema de Empleados

> [!example]- 💼 Caso Práctico con Herencia
> 
> ```java
> // ========================
> // CLASE ABSTRACTA BASE
> // ========================
> public abstract class Empleado {
>     protected String nombre;
>     protected String id;
>     protected double salarioBase;
>     
>     public Empleado(String nombre, String id, double salarioBase) {
>         if (salarioBase < 0) {
>             throw new IllegalArgumentException("Salario no puede ser negativo");
>         }
>         this.nombre = nombre;
>         this.id = id;
>         this.salarioBase = salarioBase;
>     }
>     
>     // Método abstracto - cada tipo calcula diferente
>     public abstract double calcularSalario();
>     
>     // Método abstracto - bonos específicos por tipo
>     public abstract double calcularBono();
>     
>     // Método concreto - común para todos
>     public void mostrarInfo() {
>         System.out.println("\n--- EMPLEADO ---");
>         System.out.println("Nombre: " + nombre);
>         System.out.println("ID: " + id);
>         System.out.println("Salario base: $" + salarioBase);
>         System.out.println("Salario total: $" + calcularSalario());
>         System.out.println("Bono: $" + calcularBono());
>     }
>     
>     // Getters
>     public String getNombre() { return nombre; }
>     public String getId() { return id; }
>     public double getSalarioBase() { return salarioBase; }
> }
> 
> // ========================
> // SUBCLASES CONCRETAS
> // ========================
> public class EmpleadoTiempoCompleto extends Empleado {
>     private double bonoAnual;
>     
>     public EmpleadoTiempoCompleto(String nombre, String id, 
>                                   double salarioBase, double bonoAnual) {
>         super(nombre, id, salarioBase);
>         this.bonoAnual = bonoAnual;
>     }
>     
>     @Override
>     public double calcularSalario() {
>         return salarioBase + (bonoAnual / 12);  // Mensual
>     }
>     
>     @Override
>     public double calcularBono() {
>         return bonoAnual;
>     }
> }
> 
> public class EmpleadoPorHoras extends Empleado {
>     private int horasTrabajadas;
>     private double tarifaPorHora;
>     
>     public EmpleadoPorHoras(String nombre, String id, 
>                            int horasTrabajadas, double tarifaPorHora) {
>         super(nombre, id, 0);  // Sin salario base
>         this.horasTrabajadas = horasTrabajadas;
>         this.tarifaPorHora = tarifaPorHora;
>     }
>     
>     @Override
>     public double calcularSalario() {
>         double salario = horasTrabajadas * tarifaPorHora;
>         // Horas extra (más de 160 al mes = 40 semanales)
>         if (horasTrabajadas > 160) {
>             int horasExtra = horasTrabajadas - 160;
>             salario += horasExtra * tarifaPorHora * 0.5;  // 50% extra
>         }
>         return salario;
>     }
>     
>     @Override
>     public double calcularBono() {
>         // Bono si trabaja más de 180 horas
>         return horasTrabajadas > 180 ? 200 : 0;
>     }
> }
> 
> public class Gerente extends Empleado {
>     private double bonoDesempeño;
>     private int empleadosACargo;
>     
>     public Gerente(String nombre, String id, double salarioBase,
>                   double bonoDesempeño, int empleadosACargo) {
>         super(nombre, id, salarioBase);
>         this.bonoDesempeño = bonoDesempeño;
>         this.empleadosACargo = empleadosACargo;
>     }
>     
>     @Override
>     public double calcularSalario() {
>         // Salario base + bono por empleados a cargo
>         return salarioBase + (empleadosACargo * 100);
>     }
>     
>     @Override
>     public double calcularBono() {
>         return bonoDesempeño;
>     }
> }
> 
> // ========================
> // USO DEL SISTEMA
> // ========================
> public class SistemaEmpleados {
>     public static void main(String[] args) {
>         // ❌ ERROR - No se puede instanciar clase abstracta
>         // Empleado emp = new Empleado("Juan", "001", 3000);
>         
>         // ✅ CORRECTO - Instanciar clases concretas
>         Empleado[] empleados = new Empleado[3];
>         
>         empleados[0] = new EmpleadoTiempoCompleto(
>             "Ana López", "E001", 3000, 6000
>         );
>         
>         empleados[1] = new EmpleadoPorHoras(
>             "Carlos Pérez", "E002", 185, 15
>         );
>         
>         empleados[2] = new Gerente(
>             "María García", "E003", 5000, 8000, 10
>         );
>         
>         // Polimorfismo - Todos son tratados como Empleado
>         System.out.println("=== NÓMINA MENSUAL ===");
>         double totalNomina = 0;
>         
>         for (Empleado emp : empleados) {
>             emp.mostrarInfo();  // Método concreto
>             totalNomina += emp.calcularSalario();  // Método abstracto
>         }
>         
>         System.out.println("\n💰 Total nómina: $" + totalNomina);
>     }
> }
> ```

---

## 🆚 Clases Abstractas vs Interfaces

> [!tip]- 📊 Comparación Clave
> 
> |Característica|Clase Abstracta|Interface|
> |---|---|---|
> |**Palabra clave**|`abstract class`|`interface`|
> |**Herencia**|`extends` (una sola)|`implements` (múltiples)|
> |**Métodos abstractos**|✅ Sí|✅ Sí (todos por defecto)|
> |**Métodos concretos**|✅ Sí|✅ Sí (desde Java 8: `default`)|
> |**Atributos**|✅ Cualquier tipo|❌ Solo `public static final`|
> |**Constructores**|✅ Sí|❌ No|
> |**Modificadores acceso**|✅ Todos|❌ Solo `public`|
> 
> **¿Cuándo usar cada una?**
> 
> **Clase Abstracta:**
> 
> ```java
> // ✅ Cuando hay relación "ES-UN"
> abstract class Animal {
>     protected String nombre;  // Estado común
>     
>     public Animal(String nombre) {  // Constructor
>         this.nombre = nombre;
>     }
>     
>     public void comer() {  // Comportamiento común
>         System.out.println(nombre + " está comiendo");
>     }
>     
>     public abstract void hacerSonido();  // Cada uno diferente
> }
> ```
> 
> **Interface:**
> 
> ```java
> // ✅ Cuando defines capacidades "PUEDE-HACER"
> interface Volador {
>     void volar();
>     void aterrizar();
> }
> 
> interface Nadador {
>     void nadar();
> }
> 
> // Pato puede volar Y nadar
> class Pato extends Animal implements Volador, Nadador {
>     // Implementa todos los métodos
> }
> ```

---

## ⚡ Ventajas de Clases Abstractas

> [!success]- 🎯 Beneficios Prácticos
> 
> **1. Reutilización de código:**
> 
> ```java
> abstract class Vehiculo {
>     protected String marca;
>     protected String modelo;
>     
>     // Código común - se hereda automáticamente
>     public void encender() {
>         System.out.println("Motor encendido");
>     }
>     
>     // Específico de cada vehículo
>     public abstract void acelerar();
> }
> ```
> 
> **2. Fuerza un contrato:**
> 
> ```java
> // Todas las formas DEBEN implementar estos métodos
> abstract class Forma {
>     public abstract double calcularArea();
>     public abstract double calcularPerimetro();
> }
> // Si no los implementas → Error de compilación
> ```
> 
> **3. Polimorfismo:**
> 
> ```java
> Forma[] formas = {
>     new Circulo(5),
>     new Rectangulo(4, 6),
>     new Triangulo(3, 4, 5)
> };
> 
> for (Forma f : formas) {
>     System.out.println("Área: " + f.calcularArea());
> }
> ```
> 
> **4. Encapsulamiento con herencia:**
> 
> ```java
> abstract class CuentaBancaria {
>     protected double saldo;  // Protegido para subclases
>     
>     public abstract void calcularInteres();
>     
>     // Método template - define estructura
>     public final void procesarMes() {
>         calcularInteres();
>         cobrarComisiones();
>         generarEstado();
>     }
>     
>     protected abstract void cobrarComisiones();
>     private void generarEstado() { /* ... */ }
> }
> ```

---

## 🎨 Patrón Template Method

> [!note]- 🏗️ Patrón de Diseño con Abstractas
> 
> ```java
> // Define el esqueleto de un algoritmo
> public abstract class ProcesamientoDatos {
>     // Método template (final - no se puede sobreescribir)
>     public final void procesar() {
>         leerDatos();
>         validarDatos();
>         procesarDatos();
>         guardarResultados();
>     }
>     
>     // Pasos específicos (abstractos)
>     protected abstract void leerDatos();
>     protected abstract void procesarDatos();
>     
>     // Pasos comunes (concretos)
>     private void validarDatos() {
>         System.out.println("Validando datos...");
>     }
>     
>     private void guardarResultados() {
>         System.out.println("Guardando resultados...");
>     }
> }
> 
> // Implementaciones específicas
> public class ProcesamientoCSV extends ProcesamientoDatos {
>     @Override
>     protected void leerDatos() {
>         System.out.println("Leyendo CSV...");
>     }
>     
>     @Override
>     protected void procesarDatos() {
>         System.out.println("Procesando CSV...");
>     }
> }
> 
> public class ProcesamientoJSON extends ProcesamientoDatos {
>     @Override
>     protected void leerDatos() {
>         System.out.println("Leyendo JSON...");
>     }
>     
>     @Override
>     protected void procesarDatos() {
>         System.out.println("Procesando JSON...");
>     }
> }
> ```

---

## 💡 Casos de Uso Comunes

> [!example]- 🎯 Aplicaciones Reales
> 
> **1. Jerarquías de tipos:**
> 
> ```java
> abstract class Documento {
>     protected String titulo;
>     public abstract void exportar();
> }
> 
> class PDF extends Documento { /* ... */ }
> class Word extends Documento { /* ... */ }
> ```
> 
> **2. Frameworks y extensibilidad:**
> 
> ```java
> abstract class Servlet {
>     public abstract void doGet();
>     public abstract void doPost();
> }
> ```
> 
> **3. Cálculos con variaciones:**
> 
> ```java
> abstract class CalculadoraImpuestos {
>     public abstract double calcular(double monto);
>     
>     public double aplicarDescuento(double monto, double desc) {
>         return monto * (1 - desc);
>     }
> }
> ```

---

## 📚 Resumen Ejecutivo

> [!quote]- 🌟 Puntos Clave **Has aprendido:**
> 
> - ✅ Clases abstractas como plantillas
> - ✅ Métodos abstractos vs concretos
> - ✅ Herencia e implementación obligatoria
> - ✅ Diferencias con interfaces
> - ✅ Patrón Template Method
> 
> **Próximos temas:**
> 
> - **[[05 - Interfaces]]** - Contratos puros
> - **[[06 - Polimorfismo]]** - Poder de la abstracción
> - **[[Herencia Múltiple]]** - Interfaces múltiples

---

**Tags:** #java #poo #clases-abstractas #abstract #herencia #polimorfismo #template-method #interfaces