# 🎭 Sobreescritura vs. Sobrecarga de Métodos en Java

## 🎯 Introducción

> [!info]- 💡 ¿Qué son Sobrecarga y Sobreescritura? Dos conceptos fundamentales de **polimorfismo** en Java que permiten usar el mismo nombre de método de diferentes formas:
> 
> - **Sobrecarga (Overloading):** Múltiples métodos con el **mismo nombre** pero **diferentes parámetros** en la **misma clase**
> - **Sobreescritura (Overriding):** Redefinir un método heredado en una **subclase** para cambiar su comportamiento
> 
> **Analogía:** Como un control remoto universal
> 
> - **Sobrecarga:** El botón "Play" funciona diferente según el dispositivo (TV, DVD, música)
> - **Sobreescritura:** Reemplazar el botón "Play" original con uno personalizado que hace exactamente lo que tú quieres
> 
> **Diferencia clave:**
> 
> - ✅ **Sobrecarga:** Se resuelve en **tiempo de compilación** (compile-time polymorphism)
> - ✅ **Sobreescritura:** Se resuelve en **tiempo de ejecución** (runtime polymorphism)

---

## 📦 Sobrecarga de Métodos (Overloading)

### ¿Qué es la Sobrecarga?

> [!example]- 🔄 Concepto Básico
> 
> **Definición:** Crear múltiples métodos con el **mismo nombre** pero **diferente firma** (número, tipo u orden de parámetros) dentro de la misma clase.
> 
> ```java
> public class Calculadora {
>     
>     // Método 1: suma de dos enteros
>     public int sumar(int a, int b) {
>         System.out.println("Sumando dos enteros");
>         return a + b;
>     }
>     
>     // Método 2: suma de tres enteros
>     public int sumar(int a, int b, int c) {
>         System.out.println("Sumando tres enteros");
>         return a + b + c;
>     }
>     
>     // Método 3: suma de dos doubles
>     public double sumar(double a, double b) {
>         System.out.println("Sumando dos doubles");
>         return a + b;
>     }
>     
>     // Método 4: suma de un entero y un double
>     public double sumar(int a, double b) {
>         System.out.println("Sumando int y double");
>         return a + b;
>     }
>     
>     // Método 5: suma de un double y un entero (orden diferente)
>     public double sumar(double a, int b) {
>         System.out.println("Sumando double y int");
>         return a + b;
>     }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         Calculadora calc = new Calculadora();
>         
>         System.out.println("Resultado: " + calc.sumar(5, 3));           // Método 1
>         System.out.println("Resultado: " + calc.sumar(5, 3, 2));        // Método 2
>         System.out.println("Resultado: " + calc.sumar(5.5, 3.2));       // Método 3
>         System.out.println("Resultado: " + calc.sumar(5, 3.2));         // Método 4
>         System.out.println("Resultado: " + calc.sumar(5.5, 3));         // Método 5
>     }
> }
> ```
> 
> **Salida:**
> 
> ```
> Sumando dos enteros
> Resultado: 8
> Sumando tres enteros
> Resultado: 10
> Sumando dos doubles
> Resultado: 8.7
> Sumando int y double
> Resultado: 8.2
> Sumando double y int
> Resultado: 8.5
> ```

### Reglas de la Sobrecarga

> [!success]- 📋 Requisitos para Sobrecargar
> 
> **✅ DEBE cambiar:**
> 
> 1. **Número de parámetros**
> 2. **Tipo de parámetros**
> 3. **Orden de parámetros**
> 
> **❌ NO importa cambiar:**
> 
> - Tipo de retorno (solo)
> - Modificadores de acceso
> - Excepciones lanzadas
> 
> ```java
> public class EjemplosValidos {
>     // ✅ VÁLIDO: diferente número de parámetros
>     public void mostrar(String texto) { }
>     public void mostrar(String texto, int veces) { }
>     
>     // ✅ VÁLIDO: diferente tipo de parámetros
>     public void procesar(int numero) { }
>     public void procesar(String texto) { }
>     
>     // ✅ VÁLIDO: diferente orden de parámetros
>     public void calcular(int a, double b) { }
>     public void calcular(double a, int b) { }
>     
>     // ✅ VÁLIDO: diferente tipo de retorno + diferentes parámetros
>     public int obtener(String clave) { return 0; }
>     public String obtener(int id) { return ""; }
> }
> 
> public class EjemplosInvalidos {
>     // ❌ INVÁLIDO: solo cambia el tipo de retorno
>     // public int calcular(int a) { return a * 2; }
>     // public double calcular(int a) { return a * 2.0; }  // ERROR DE COMPILACIÓN
>     
>     // ❌ INVÁLIDO: solo cambian los nombres de parámetros
>     // public void mostrar(int numero) { }
>     // public void mostrar(int cantidad) { }  // ERROR: misma firma
>     
>     // ❌ INVÁLIDO: solo cambia el modificador de acceso
>     // public void guardar(String dato) { }
>     // private void guardar(String dato) { }  // ERROR
> }
> ```

### Sobrecarga con Varargs

> [!tip]- 🔢 Argumentos Variables
> 
> ```java
> public class OperacionesMatematicas {
>     
>     // Método con número fijo de parámetros
>     public int sumar(int a, int b) {
>         System.out.println("Método con 2 parámetros");
>         return a + b;
>     }
>     
>     // Método con varargs (número variable)
>     public int sumar(int... numeros) {
>         System.out.println("Método con varargs (" + numeros.length + " argumentos)");
>         int suma = 0;
>         for (int num : numeros) {
>             suma += num;
>         }
>         return suma;
>     }
>     
>     // Método con parámetro fijo + varargs
>     public int sumar(String etiqueta, int... numeros) {
>         System.out.println(etiqueta + " - varargs");
>         int suma = 0;
>         for (int num : numeros) {
>             suma += num;
>         }
>         return suma;
>     }
>     
>     public static void main(String[] args) {
>         OperacionesMatematicas op = new OperacionesMatematicas();
>         
>         // El método más específico tiene prioridad
>         System.out.println(op.sumar(5, 3));              // Usa el de 2 parámetros
>         System.out.println(op.sumar(5, 3, 2));           // Usa varargs
>         System.out.println(op.sumar(5, 3, 2, 1, 4));     // Usa varargs
>         System.out.println(op.sumar("Total", 5, 3, 2));  // Usa String + varargs
>     }
> }
> ```
> 
> **⚠️ Precaución con varargs:**
> 
> ```java
> public class AmbiguedadVarargs {
>     // ❌ AMBIGUO: puede causar problemas
>     public void metodo(int... numeros) { }
>     public void metodo(int a, int... numeros) { }
>     
>     public static void main(String[] args) {
>         AmbiguedadVarargs obj = new AmbiguedadVarargs();
>         // obj.metodo(1, 2);  // ¿Cuál método usar? AMBIGUO
>     }
> }
> ```

### Promoción de Tipos (Type Promotion)

> [!warning]- ⚡ Conversiones Automáticas
> 
> Java puede **promocionar** automáticamente tipos de datos para encontrar un método sobrecargado:
> 
> ```java
> public class PromocionTipos {
>     
>     public void procesar(int numero) {
>         System.out.println("Procesando int: " + numero);
>     }
>     
>     public void procesar(double numero) {
>         System.out.println("Procesando double: " + numero);
>     }
>     
>     public void procesar(String texto) {
>         System.out.println("Procesando String: " + texto);
>     }
>     
>     public static void main(String[] args) {
>         PromocionTipos obj = new PromocionTipos();
>         
>         byte b = 10;
>         short s = 20;
>         int i = 30;
>         long l = 40L;
>         float f = 50.5f;
>         double d = 60.5;
>         
>         obj.procesar(b);  // byte → int (promoción)
>         obj.procesar(s);  // short → int (promoción)
>         obj.procesar(i);  // int exacto
>         obj.procesar(l);  // long → double (promoción)
>         obj.procesar(f);  // float → double (promoción)
>         obj.procesar(d);  // double exacto
>     }
> }
> ```
> 
> **Cadena de promoción:**
> 
> ```
> byte → short → int → long → float → double
>           ↓
>         char → int
> ```

---

## 🎨 Sobreescritura de Métodos (Overriding)

### ¿Qué es la Sobreescritura?

> [!example]- 🔄 Concepto Básico
> 
> **Definición:** Redefinir un método de la **clase padre** en la **clase hija** para cambiar su comportamiento, manteniendo la **misma firma**.
> 
> ```java
> // Clase Padre
> public class Animal {
>     public void hacerSonido() {
>         System.out.println("El animal hace un sonido");
>     }
>     
>     public void moverse() {
>         System.out.println("El animal se mueve");
>     }
>     
>     public void dormir() {
>         System.out.println("El animal duerme");
>     }
> }
> 
> // Clase Hija 1
> public class Perro extends Animal {
>     @Override  // Anotación opcional pero recomendada
>     public void hacerSonido() {
>         System.out.println("El perro ladra: ¡Guau guau!");
>     }
>     
>     @Override
>     public void moverse() {
>         System.out.println("El perro corre en cuatro patas");
>     }
>     
>     // dormir() NO se sobreescribe, usa el de Animal
> }
> 
> // Clase Hija 2
> public class Gato extends Animal {
>     @Override
>     public void hacerSonido() {
>         System.out.println("El gato maúlla: ¡Miau!");
>     }
>     
>     @Override
>     public void moverse() {
>         System.out.println("El gato camina sigilosamente");
>     }
> }
> 
> // Clase Hija 3
> public class Pajaro extends Animal {
>     @Override
>     public void hacerSonido() {
>         System.out.println("El pájaro canta: ¡Pío pío!");
>     }
>     
>     @Override
>     public void moverse() {
>         System.out.println("El pájaro vuela");
>     }
> }
> 
> // USO: Polimorfismo en acción
> public class Main {
>     public static void main(String[] args) {
>         // Polimorfismo: referencia de tipo padre, objetos de tipo hijo
>         Animal animal1 = new Perro();
>         Animal animal2 = new Gato();
>         Animal animal3 = new Pajaro();
>         
>         Animal[] animales = {animal1, animal2, animal3};
>         
>         System.out.println("=== DEMOSTRACIÓN DE POLIMORFISMO ===\n");
>         for (Animal animal : animales) {
>             animal.hacerSonido();  // Método sobreescrito
>             animal.moverse();      // Método sobreescrito
>             animal.dormir();       // Método heredado (no sobreescrito)
>             System.out.println();
>         }
>     }
> }
> ```
> 
> **Salida:**
> 
> ```
> === DEMOSTRACIÓN DE POLIMORFISMO ===
> 
> El perro ladra: ¡Guau guau!
> El perro corre en cuatro patas
> El animal duerme
> 
> El gato maúlla: ¡Miau!
> El gato camina sigilosamente
> El animal duerme
> 
> El pájaro canta: ¡Pío pío!
> El pájaro vuela
> El animal duerme
> ```

### Reglas de la Sobreescritura

> [!success]- 📋 Requisitos para Sobreescribir
> 
> **✅ DEBE mantener:**
> 
> 1. **Mismo nombre** del método
> 2. **Misma firma** (mismo tipo y número de parámetros)
> 3. **Mismo tipo de retorno** (o subtipo - covariante desde Java 5)
> 
> **✅ PUEDE cambiar:**
> 
> - Modificador de acceso (solo **ampliar**, no restringir)
> - Excepciones (solo **reducir** o **eliminar**, no ampliar)
> - Implementación del método
> 
> **❌ NO PUEDE:**
> 
> - Hacer el método **menos accesible**
> - Lanzar **nuevas** excepciones checked
> - Cambiar el tipo de retorno a uno **incompatible**
> - Sobreescribir métodos `final`
> - Sobreescribir métodos `static` (se ocultan, no se sobreescriben)
> - Sobreescribir métodos `private` (no son heredados)
> 
> ```java
> public class ClasePadre {
>     // Método público con excepción
>     public Number calcular(int x) throws IOException {
>         return x * 2;
>     }
>     
>     public final void metodoFinal() {
>         System.out.println("No se puede sobreescribir");
>     }
>     
>     public static void metodoEstatico() {
>         System.out.println("Método estático padre");
>     }
>     
>     private void metodoPrivado() {
>         System.out.println("No visible para hijos");
>     }
> }
> 
> public class ClaseHija extends ClasePadre {
>     // ✅ VÁLIDO: tipo de retorno covariante (Integer es subtipo de Number)
>     @Override
>     public Integer calcular(int x) {  // No lanza excepciones (reducción)
>         return x * 3;
>     }
>     
>     // ❌ INVÁLIDO: no se puede sobreescribir método final
>     // @Override
>     // public void metodoFinal() { }  // ERROR
>     
>     // ⚠️ NO ES SOBREESCRITURA: es "method hiding" (ocultar método)
>     public static void metodoEstatico() {
>         System.out.println("Método estático hijo");
>     }
>     
>     // ❌ NO ES SOBREESCRITURA: el método privado no se hereda
>     private void metodoPrivado() {
>         System.out.println("Método propio del hijo");
>     }
> }
> ```

### Anotación @Override

> [!tip]- 🏷️ Ventajas de usar @Override
> 
> **Beneficios:**
> 
> 1. ✅ Detecta errores en tiempo de compilación
> 2. ✅ Mejora la legibilidad del código
> 3. ✅ Facilita el mantenimiento
> 4. ✅ Documenta la intención del programador
> 
> ```java
> public class Vehiculo {
>     public void acelerar(int velocidad) {
>         System.out.println("Acelerando a " + velocidad + " km/h");
>     }
> }
> 
> public class Auto extends Vehiculo {
>     // ❌ SIN @Override - error NO detectado
>     // public void aselerar(int velocidad) {  // Typo en nombre
>     //     System.out.println("Auto acelerando");
>     // }
>     
>     // ✅ CON @Override - error DETECTADO
>     @Override
>     public void acelerar(int velocidad) {  // Error detectado si hay typo
>         System.out.println("Auto acelerando a " + velocidad + " km/h");
>     }
>     
>     // ❌ Ejemplo de error detectado por @Override
>     // @Override
>     // public void acelerar(double velocidad) {  // ERROR: no existe en padre
>     //     System.out.println("Método incorrecto");
>     // }
> }
> ```

### Uso de super

> [!example]- 🔗 Llamar al Método del Padre
> 
> Usa `super.metodo()` para invocar la implementación del padre desde el hijo:
> 
> ```java
> public class CuentaBancaria {
>     protected String titular;
>     protected double saldo;
>     
>     public CuentaBancaria(String titular, double saldoInicial) {
>         this.titular = titular;
>         this.saldo = saldoInicial;
>     }
>     
>     public void depositar(double monto) {
>         saldo += monto;
>         System.out.println("Depósito: $" + monto);
>         System.out.println("Nuevo saldo: $" + saldo);
>     }
>     
>     public boolean retirar(double monto) {
>         if (monto <= saldo) {
>             saldo -= monto;
>             System.out.println("Retiro: $" + monto);
>             return true;
>         }
>         System.out.println("Fondos insuficientes");
>         return false;
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("Titular: " + titular);
>         System.out.println("Saldo: $" + saldo);
>     }
> }
> 
> public class CuentaAhorro extends CuentaBancaria {
>     private double tasaInteres;
>     private int retirosGratis;
>     private int retirosRealizados;
>     
>     public CuentaAhorro(String titular, double saldoInicial, double tasaInteres) {
>         super(titular, saldoInicial);
>         this.tasaInteres = tasaInteres;
>         this.retirosGratis = 3;
>         this.retirosRealizados = 0;
>     }
>     
>     @Override
>     public void depositar(double monto) {
>         // Llamar al método del padre
>         super.depositar(monto);
>         
>         // Agregar funcionalidad adicional
>         double interes = monto * tasaInteres;
>         saldo += interes;
>         System.out.println("Interés ganado: $" + interes);
>     }
>     
>     @Override
>     public boolean retirar(double monto) {
>         double montoTotal = monto;
>         
>         // Cobrar comisión si excede retiros gratis
>         if (retirosRealizados >= retirosGratis) {
>             montoTotal += 2.0;  // Comisión de $2
>             System.out.println("Comisión por retiro: $2.00");
>         }
>         
>         // Usar el método del padre para realizar el retiro
>         boolean exito = super.retirar(montoTotal);
>         
>         if (exito) {
>             retirosRealizados++;
>         }
>         
>         return exito;
>     }
>     
>     @Override
>     public void mostrarInfo() {
>         // Reutilizar método del padre
>         super.mostrarInfo();
>         
>         // Agregar información específica
>         System.out.println("Tasa de interés: " + (tasaInteres * 100) + "%");
>         System.out.println("Retiros realizados: " + retirosRealizados + "/" + retirosGratis);
>     }
>     
>     public void aplicarIntereses() {
>         double interes = saldo * tasaInteres;
>         saldo += interes;
>         System.out.println("Intereses aplicados: $" + interes);
>     }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         System.out.println("=== CUENTA DE AHORRO ===\n");
>         
>         CuentaAhorro cuenta = new CuentaAhorro("María García", 1000.0, 0.05);
>         
>         cuenta.mostrarInfo();
>         System.out.println();
>         
>         cuenta.depositar(500.0);  // Usa super + funcionalidad extra
>         System.out.println();
>         
>         cuenta.retirar(100.0);    // Primer retiro (gratis)
>         System.out.println();
>         
>         cuenta.retirar(50.0);     // Segundo retiro (gratis)
>         System.out.println();
>         
>         cuenta.retirar(30.0);     // Tercer retiro (gratis)
>         System.out.println();
>         
>         cuenta.retirar(20.0);     // Cuarto retiro (con comisión)
>         System.out.println();
>         
>         cuenta.aplicarIntereses();
>         System.out.println();
>         
>         cuenta.mostrarInfo();
>     }
> }
> ```

---

## 🆚 Comparación: Sobrecarga vs. Sobreescritura

> [!note]- 📊 Tabla Comparativa
> 
> |Característica|Sobrecarga (Overloading)|Sobreescritura (Overriding)|
> |---|---|---|
> |**Definición**|Múltiples métodos con mismo nombre|Redefinir método heredado|
> |**Ubicación**|Misma clase|Clase padre e hija|
> |**Firma**|Debe cambiar|Debe ser igual|
> |**Tipo de retorno**|Puede cambiar|Mismo o covariante|
> |**Modificadores**|No importan|No puede restringir acceso|
> |**Resolución**|Tiempo de compilación (estática)|Tiempo de ejecución (dinámica)|
> |**Polimorfismo**|Compile-time polymorphism|Runtime polymorphism|
> |**Herencia**|No requiere|Requiere|
> |**Palabra clave**|Ninguna|`@Override` (recomendada)|
> |**Uso de super**|No aplica|`super.metodo()`|
> |**Métodos static**|Sí|No (se ocultan)|
> |**Métodos private**|Sí|No (no se heredan)|
> |**Métodos final**|Sí|No|

### Ejemplo Completo Comparativo

> [!example]- 🎭 Sobrecarga vs. Sobreescritura en Acción
> 
> ```java
> // Clase Padre
> public class Empleado {
>     protected String nombre;
>     protected double salarioBase;
>     
>     public Empleado(String nombre, double salarioBase) {
>         this.nombre = nombre;
>         this.salarioBase = salarioBase;
>     }
>     
>     // Método para sobreescribir
>     public double calcularSalario() {
>         return salarioBase;
>     }
>     
>     // SOBRECARGA en la misma clase
>     public double calcularSalario(int horasExtra) {
>         return salarioBase + (horasExtra * 10);
>     }
>     
>     // SOBRECARGA con diferente tipo
>     public double calcularSalario(double bono) {
>         return salarioBase + bono;
>     }
>     
>     // SOBRECARGA con dos parámetros
>     public double calcularSalario(int horasExtra, double bono) {
>         return salarioBase + (horasExtra * 10) + bono;
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("Empleado: " + nombre);
>         System.out.println("Salario base: $" + salarioBase);
>     }
> }
> 
> // Clase Hija 1
> public class Desarrollador extends Empleado {
>     private String lenguaje;
>     
>     public Desarrollador(String nombre, double salarioBase, String lenguaje) {
>         super(nombre, salarioBase);
>         this.lenguaje = lenguaje;
>     }
>     
>     // SOBREESCRITURA del método del padre
>     @Override
>     public double calcularSalario() {
>         // Desarrolladores tienen bono técnico del 20%
>         return salarioBase * 1.20;
>     }
>     
>     // SOBRECARGA en la clase hija
>     public double calcularSalario(int proyectosCompletados) {
>         double bonoProyecto = proyectosCompletados * 500;
>         return calcularSalario() + bonoProyecto;
>     }
>     
>     @Override
>     public void mostrarInfo() {
>         super.mostrarInfo();
>         System.out.println("Lenguaje: " + lenguaje);
>         System.out.println("Salario con bono técnico: $" + calcularSalario());
>     }
> }
> 
> // Clase Hija 2
> public class Gerente extends Empleado {
>     private int empleadosACargo;
>     
>     public Gerente(String nombre, double salarioBase, int empleados) {
>         super(nombre, salarioBase);
>         this.empleadosACargo = empleados;
>     }
>     
>     // SOBREESCRITURA del método del padre
>     @Override
>     public double calcularSalario() {
>         // Gerentes tienen bono del 50% + $100 por empleado a cargo
>         double bonoGerencia = salarioBase * 0.50;
>         double bonoEquipo = empleadosACargo * 100;
>         return salarioBase + bonoGerencia + bonoEquipo;
>     }
>     
>     // SOBRECARGA específica para gerentes
>     public double calcularSalario(boolean metaCumplida) {
>         double salario = calcularSalario();
>         if (metaCumplida) {
>             salario += 2000;  // Bono por meta cumplida
>         }
>         return salario;
>     }
>     
>     @Override
>     public void mostrarInfo() {
>         super.mostrarInfo();
>         System.out.println("Empleados a cargo: " + empleadosACargo);
>         System.out.println("Salario total: $" + calcularSalario());
>     }
> }
> 
> // Demostración
> public class SistemaEmpleados {
>     public static void main(String[] args) {
>         System.out.println("╔════════════════════════════════════╗");
>         System.out.println("║  SOBRECARGA VS. SOBREESCRITURA     ║");
>         System.out.println("╚════════════════════════════════════╝\n");
>         
>         // Crear empleados
>         Empleado emp = new Empleado("Juan Pérez", 3000);
>         Desarrollador dev = new Desarrollador("Ana López", 4000, "Java");
>         Gerente ger = new Gerente("Carlos Ruiz", 5000, 10);
>         
>         // === DEMOSTRACIÓN DE SOBRECARGA ===
>         System.out.println("=== SOBRECARGA (Mismo nombre, diferentes parámetros) ===\n");
>         
>         System.out.println("--- Empleado Base ---");
>         System.out.println("Sin parámetros: $" + emp.calcularSalario());
>         System.out.println("Con horas extra (10): $" + emp.calcularSalario(10));
>         System.out.println("Con bono (500.0): $" + emp.calcularSalario(500.0));
>         System.out.println("Con horas y bono (10, 500.0): $" + emp.calcularSalario(10, 500.0));
>         System.out.println();
>         
>         System.out.println("--- Desarrollador ---");
>         System.out.println("Sin parámetros: $" + dev.calcularSalario());
>         System.out.println("Con proyectos (3): $" + dev.calcularSalario(3));
>         System.out.println();
>         
>         System.out.println("--- Gerente ---");
>         System.out.println("Sin parámetros: $" + ger.calcularSalario());
>         System.out.println("Meta cumplida (true): $" + ger.calcularSalario(true));
>         
>         System.out.println("Meta NO cumplida (false): $" + ger.calcularSalario(false));
>         System.out.println();
>         
>         // === DEMOSTRACIÓN DE SOBREESCRITURA ===
>         System.out.println("\n=== SOBREESCRITURA (Polimorfismo en tiempo de ejecución) ===\n");
>         
>         // Array de empleados (polimorfismo)
>         Empleado[] empleados = {emp, dev, ger};
>         
>         System.out.println("Llamando al mismo método calcularSalario() en diferentes tipos:\n");
>         for (Empleado e : empleados) {
>             System.out.println("Tipo: " + e.getClass().getSimpleName());
>             System.out.println("Salario: $" + e.calcularSalario());  // Método sobreescrito
>             System.out.println();
>         }
>         
>         // === INFORMACIÓN COMPLETA ===
>         System.out.println("\n=== INFORMACIÓN DETALLADA ===\n");
>         for (Empleado e : empleados) {
>             e.mostrarInfo();  // Método sobreescrito
>             System.out.println("---");
>         }
>     }
> }
> ```
> 

---

## 🎯 Casos de Uso Comunes

### 1️⃣ Sistema de Figuras Geométricas

> [!example]- 📐 Cálculo de Áreas y Perímetros
> 
> ```java
> // Clase abstracta padre
> public abstract class Figura {
>     protected String color;
>     
>     public Figura(String color) {
>         this.color = color;
>     }
>     
>     // Métodos abstractos para sobreescribir
>     public abstract double calcularArea();
>     public abstract double calcularPerimetro();
>     
>     // Método concreto con SOBRECARGA
>     public void dibujar() {
>         System.out.println("Dibujando " + this.getClass().getSimpleName() + 
>                            " de color " + color);
>     }
>     
>     public void dibujar(int x, int y) {
>         System.out.println("Dibujando " + this.getClass().getSimpleName() + 
>                            " en posición (" + x + ", " + y + ")");
>     }
>     
>     public void dibujar(int x, int y, double escala) {
>         System.out.println("Dibujando " + this.getClass().getSimpleName() + 
>                            " en (" + x + ", " + y + ") con escala " + escala);
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("\n=== " + this.getClass().getSimpleName() + " ===");
>         System.out.println("Color: " + color);
>         System.out.println("Área: " + String.format("%.2f", calcularArea()));
>         System.out.println("Perímetro: " + String.format("%.2f", calcularPerimetro()));
>     }
> }
> 
> // Clase Círculo
> public class Circulo extends Figura {
>     private double radio;
>     
>     public Circulo(String color, double radio) {
>         super(color);
>         this.radio = radio;
>     }
>     
>     // SOBREESCRITURA
>     @Override
>     public double calcularArea() {
>         return Math.PI * radio * radio;
>     }
>     
>     @Override
>     public double calcularPerimetro() {
>         return 2 * Math.PI * radio;
>     }
>     
>     // SOBRECARGA específica
>     public double calcularArea(int segmentos) {
>         // Aproximación del área usando polígono regular
>         double anguloSegmento = (2 * Math.PI) / segmentos;
>         double ladoSegmento = 2 * radio * Math.sin(anguloSegmento / 2);
>         return (segmentos * ladoSegmento * radio * Math.cos(anguloSegmento / 2)) / 2;
>     }
> }
> 
> // Clase Rectángulo
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
>     // SOBREESCRITURA
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
>     // SOBRECARGA con padding
>     public double calcularArea(double padding) {
>         return (ancho + 2 * padding) * (alto + 2 * padding);
>     }
>     
>     public boolean esCuadrado() {
>         return ancho == alto;
>     }
> }
> 
> // Clase Triángulo
> public class Triangulo extends Figura {
>     private double lado1, lado2, lado3;
>     
>     public Triangulo(String color, double lado1, double lado2, double lado3) {
>         super(color);
>         this.lado1 = lado1;
>         this.lado2 = lado2;
>         this.lado3 = lado3;
>     }
>     
>     // SOBREESCRITURA
>     @Override
>     public double calcularArea() {
>         // Fórmula de Herón
>         double s = calcularPerimetro() / 2;
>         return Math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3));
>     }
>     
>     @Override
>     public double calcularPerimetro() {
>         return lado1 + lado2 + lado3;
>     }
>     
>     // SOBRECARGA para triángulo rectángulo
>     public double calcularArea(boolean esRectangulo) {
>         if (esRectangulo) {
>             // Asumiendo que lado1 y lado2 son los catetos
>             return (lado1 * lado2) / 2;
>         }
>         return calcularArea();
>     }
> }
> 
> // Demostración
> public class SistemaFiguras {
>     public static void main(String[] args) {
>         System.out.println("╔══════════════════════════════════════╗");
>         System.out.println("║   SISTEMA DE FIGURAS GEOMÉTRICAS     ║");
>         System.out.println("╚══════════════════════════════════════╝");
>         
>         // Crear figuras
>         Circulo circulo = new Circulo("Rojo", 5.0);
>         Rectangulo rectangulo = new Rectangulo("Azul", 4.0, 6.0);
>         Triangulo triangulo = new Triangulo("Verde", 3.0, 4.0, 5.0);
>         
>         // Array polimórfico
>         Figura[] figuras = {circulo, rectangulo, triangulo};
>         
>         // SOBREESCRITURA: cada figura calcula área de forma diferente
>         System.out.println("\n=== CÁLCULOS (Sobreescritura) ===");
>         for (Figura fig : figuras) {
>             fig.mostrarInfo();
>         }
>         
>         // SOBRECARGA: diferentes formas de dibujar
>         System.out.println("\n=== DIBUJO (Sobrecarga) ===");
>         circulo.dibujar();
>         circulo.dibujar(10, 20);
>         circulo.dibujar(10, 20, 1.5);
>         
>         // SOBRECARGA específica de cada clase
>         System.out.println("\n=== MÉTODOS SOBRECARGADOS ESPECÍFICOS ===");
>         System.out.println("Área círculo (normal): " + circulo.calcularArea());
>         System.out.println("Área círculo (8 segmentos): " + circulo.calcularArea(8));
>         
>         System.out.println("\nÁrea rectángulo (normal): " + rectangulo.calcularArea());
>         System.out.println("Área rectángulo (padding 2): " + rectangulo.calcularArea(2));
>         
>         System.out.println("\nÁrea triángulo (Herón): " + triangulo.calcularArea());
>         System.out.println("Área triángulo (rectángulo): " + triangulo.calcularArea(true));
>     }
> }
> ```

### 2️⃣ Sistema de Notificaciones

> [!tip]- 📧 Envío de Mensajes
> 
> ```java
> // Clase abstracta base
> public abstract class Notificacion {
>     protected String destinatario;
>     protected String mensaje;
>     
>     public Notificacion(String destinatario, String mensaje) {
>         this.destinatario = destinatario;
>         this.mensaje = mensaje;
>     }
>     
>     // Método abstracto para sobreescribir
>     public abstract boolean enviar();
>     
>     // SOBRECARGA del método enviar
>     public boolean enviar(boolean urgente) {
>         if (urgente) {
>             System.out.println("⚡ URGENTE ⚡");
>         }
>         return enviar();
>     }
>     
>     public boolean enviar(String asunto, boolean urgente) {
>         System.out.println("Asunto: " + asunto);
>         return enviar(urgente);
>     }
>     
>     protected void registrarEnvio() {
>         System.out.println("✓ Notificación registrada en el sistema");
>     }
> }
> 
> // Email
> public class NotificacionEmail extends Notificacion {
>     private String asunto;
>     
>     public NotificacionEmail(String email, String asunto, String mensaje) {
>         super(email, mensaje);
>         this.asunto = asunto;
>     }
>     
>     // SOBREESCRITURA
>     @Override
>     public boolean enviar() {
>         System.out.println("\n📧 Enviando Email...");
>         System.out.println("Para: " + destinatario);
>         System.out.println("Asunto: " + asunto);
>         System.out.println("Mensaje: " + mensaje);
>         registrarEnvio();
>         return true;
>     }
>     
>     // SOBRECARGA específica
>     public boolean enviar(String[] cc) {
>         System.out.println("\n📧 Enviando Email con copia...");
>         System.out.println("Para: " + destinatario);
>         System.out.print("CC: ");
>         for (String correo : cc) {
>             System.out.print(correo + " ");
>         }
>         System.out.println();
>         return enviar();
>     }
> }
> 
> // SMS
> public class NotificacionSMS extends Notificacion {
>     
>     public NotificacionSMS(String telefono, String mensaje) {
>         super(telefono, mensaje);
>     }
>     
>     // SOBREESCRITURA
>     @Override
>     public boolean enviar() {
>         System.out.println("\n📱 Enviando SMS...");
>         System.out.println("Teléfono: " + destinatario);
>         
>         // SMS tiene límite de caracteres
>         if (mensaje.length() > 160) {
>             System.out.println("⚠️ Mensaje truncado a 160 caracteres");
>             System.out.println("Mensaje: " + mensaje.substring(0, 160) + "...");
>         } else {
>             System.out.println("Mensaje: " + mensaje);
>         }
>         
>         registrarEnvio();
>         return true;
>     }
>     
>     // SOBRECARGA con código de país
>     public boolean enviar(String codigoPais) {
>         System.out.println("\n📱 Enviando SMS Internacional...");
>         System.out.println("Teléfono: " + codigoPais + "-" + destinatario);
>         return enviar();
>     }
> }
> 
> // Push Notification
> public class NotificacionPush extends Notificacion {
>     private String titulo;
>     
>     public NotificacionPush(String usuarioId, String titulo, String mensaje) {
>         super(usuarioId, mensaje);
>         this.titulo = titulo;
>     }
>     
>     // SOBREESCRITURA
>     @Override
>     public boolean enviar() {
>         System.out.println("\n🔔 Enviando Push Notification...");
>         System.out.println("Usuario: " + destinatario);
>         System.out.println("Título: " + titulo);
>         System.out.println("Mensaje: " + mensaje);
>         registrarEnvio();
>         return true;
>     }
>     
>     // SOBRECARGA con badge
>     public boolean enviar(int badgeNumber) {
>         System.out.println("\n🔔 Push con Badge...");
>         System.out.println("Badge: " + badgeNumber);
>         return enviar();
>     }
>     
>     // SOBRECARGA con sonido personalizado
>     public boolean enviar(String sonido, int badge) {
>         System.out.println("\n🔔 Push Personalizado...");
>         System.out.println("Sonido: " + sonido);
>         System.out.println("Badge: " + badge);
>         return enviar();
>     }
> }
> 
> // Sistema de notificaciones
> public class SistemaNotificaciones {
>     public static void main(String[] args) {
>         System.out.println("╔════════════════════════════════════╗");
>         System.out.println("║   SISTEMA DE NOTIFICACIONES        ║");
>         System.out.println("╚════════════════════════════════════╝");
>         
>         // Crear notificaciones
>         NotificacionEmail email = new NotificacionEmail(
>             "usuario@example.com",
>             "Bienvenido",
>             "Gracias por registrarte en nuestro sistema"
>         );
>         
>         NotificacionSMS sms = new NotificacionSMS(
>             "1234567890",
>             "Tu código de verificación es: 123456"
>         );
>         
>         NotificacionPush push = new NotificacionPush(
>             "user_123",
>             "Nueva actualización",
>             "Hay una nueva versión disponible"
>         );
>         
>         // POLIMORFISMO (Sobreescritura)
>         System.out.println("\n=== ENVÍO POLIMÓRFICO ===");
>         Notificacion[] notificaciones = {email, sms, push};
>         
>         for (Notificacion notif : notificaciones) {
>             notif.enviar();  // Método sobreescrito en cada clase
>         }
>         
>         // SOBRECARGA (Diferentes formas de enviar)
>         System.out.println("\n\n=== MÉTODOS SOBRECARGADOS ===");
>         
>         email.enviar(true);  // Con urgencia
>         email.enviar(new String[]{"cc1@example.com", "cc2@example.com"});  // Con CC
>         
>         sms.enviar("+1");  // Con código de país
>         
>         push.enviar(5);  // Con badge
>         push.enviar("custom_sound.mp3", 3);  // Con sonido y badge
>     }
> }
> ```

### 3️⃣ Sistema de Pagos

> [!example]- 💳 Procesamiento de Transacciones
> 
> ```java
> // Clase base abstracta
> public abstract class MetodoPago {
>     protected String titular;
>     protected double monto;
>     
>     public MetodoPago(String titular) {
>         this.titular = titular;
>     }
>     
>     // Método abstracto para sobreescribir
>     public abstract boolean procesarPago(double monto);
>     
>     // SOBRECARGA para pagos con descripción
>     public boolean procesarPago(double monto, String descripcion) {
>         System.out.println("Descripción: " + descripcion);
>         return procesarPago(monto);
>     }
>     
>     // SOBRECARGA para pagos con cuotas
>     public boolean procesarPago(double monto, int cuotas) {
>         System.out.println("Pago en " + cuotas + " cuotas de $" + 
>                            String.format("%.2f", monto / cuotas));
>         return procesarPago(monto);
>     }
>     
>     protected void registrarTransaccion(double monto, boolean exitoso) {
>         System.out.println("Transacción " + (exitoso ? "EXITOSA" : "RECHAZADA"));
>         System.out.println("Monto: $" + String.format("%.2f", monto));
>     }
>     
>     public abstract String obtenerTipo();
> }
> 
> // Tarjeta de Crédito
> public class TarjetaCredito extends MetodoPago {
>     private String numeroTarjeta;
>     private double limiteCredito;
>     private double saldoUtilizado;
>     
>     public TarjetaCredito(String titular, String numero, double limite) {
>         super(titular);
>         this.numeroTarjeta = numero;
>         this.limiteCredito = limite;
>         this.saldoUtilizado = 0;
>     }
>     
>     // SOBREESCRITURA
>     @Override
>     public boolean procesarPago(double monto) {
>         System.out.println("\n💳 Procesando con Tarjeta de Crédito...");
>         System.out.println("Titular: " + titular);
>         System.out.println("Tarjeta: **** " + numeroTarjeta.substring(12));
>         
>         double disponible = limiteCredito - saldoUtilizado;
>         
>         if (monto <= disponible) {
>             saldoUtilizado += monto;
>             registrarTransaccion(monto, true);
>             System.out.println("Disponible: $" + String.format("%.2f", disponible - monto));
>             return true;
>         }
>         
>         System.out.println("❌ Límite de crédito insuficiente");
>         registrarTransaccion(monto, false);
>         return false;
>     }
>     
>     // SOBRECARGA específica para diferir pago
>     public boolean procesarPago(double monto, int mesesSinIntereses, double comision) {
>         System.out.println("\n💳 Pago con Meses Sin Intereses...");
>         System.out.println("Cuotas: " + mesesSinIntereses + " MSI");
>         System.out.println("Comisión: " + (comision * 100) + "%");
>         
>         double montoTotal = monto * (1 + comision);
>         return procesarPago(montoTotal);
>     }
>     
>     @Override
>     public String obtenerTipo() {
>         return "Tarjeta de Crédito";
>     }
> }
> 
> // Tarjeta de Débito
> public class TarjetaDebito extends MetodoPago {
>     private String numeroCuenta;
>     private double saldoDisponible;
>     
>     public TarjetaDebito(String titular, String cuenta, double saldo) {
>         super(titular);
>         this.numeroCuenta = cuenta;
>         this.saldoDisponible = saldo;
>     }
>     
>     // SOBREESCRITURA
>     @Override
>     public boolean procesarPago(double monto) {
>         System.out.println("\n💳 Procesando con Tarjeta de Débito...");
>         System.out.println("Titular: " + titular);
>         System.out.println("Cuenta: **** " + numeroCuenta.substring(6));
>         
>         if (monto <= saldoDisponible) {
>             saldoDisponible -= monto;
>             registrarTransaccion(monto, true);
>             System.out.println("Saldo restante: $" + String.format("%.2f", saldoDisponible));
>             return true;
>         }
>         
>         System.out.println("❌ Saldo insuficiente");
>         registrarTransaccion(monto, false);
>         return false;
>     }
>     
>     // SOBRECARGA con PIN
>     public boolean procesarPago(double monto, String pin) {
>         System.out.println("\n💳 Validando PIN...");
>         if (validarPIN(pin)) {
>             System.out.println("✓ PIN válido");
>             return procesarPago(monto);
>         }
>         System.out.println("❌ PIN inválido");
>         return false;
>     }
>     
>     private boolean validarPIN(String pin) {
>         return pin.length() == 4;  // Validación simplificada
>     }
>     
>     @Override
>     public String obtenerTipo() {
>         return "Tarjeta de Débito";
>     }
> }
> 
> // PayPal
> public class PayPal extends MetodoPago {
>     private String email;
>     private double saldoPayPal;
>     
>     public PayPal(String titular, String email, double saldo) {
>         super(titular);
>         this.email = email;
>         this.saldoPayPal = saldo;
>     }
>     
>     // SOBREESCRITURA
>     @Override
>     public boolean procesarPago(double monto) {
>         System.out.println("\n🔵 Procesando con PayPal...");
>         System.out.println("Email: " + email);
>         
>         double comision = monto * 0.04;  // 4% de comisión
>         double montoTotal = monto + comision;
>         
>         System.out.println("Comisión PayPal: $" + String.format("%.2f", comision));
>         
>         if (montoTotal <= saldoPayPal) {
>             saldoPayPal -= montoTotal;
>             registrarTransaccion(monto, true);
>             System.out.println("Saldo PayPal: $" + String.format("%.2f", saldoPayPal));
>             return true;
>         }
>         
>         System.out.println("❌ Saldo PayPal insuficiente");
>         registrarTransaccion(monto, false);
>         return false;
>     }
>     
>     // SOBRECARGA para transferencia entre usuarios
>     public boolean procesarPago(double monto, String emailDestino) {
>         System.out.println("\n🔵 Transferencia PayPal...");
>         System.out.println("Destinatario: " + emailDestino);
>         return procesarPago(monto);
>     }
>     
>     // SOBRECARGA con moneda
>     public boolean procesarPago(double monto, String moneda, double tasaCambio) {
>         System.out.println("\n🔵 Pago Internacional PayPal...");
>         System.out.println("Moneda: " + moneda);
>         System.out.println("Tasa de cambio: " + tasaCambio);
>         
>         double montoConvertido = monto * tasaCambio;
>         System.out.println("Monto convertido: $" + String.format("%.2f", montoConvertido));
>         
>         return procesarPago(montoConvertido);
>     }
>     
>     @Override
>     public String obtenerTipo() {
>         return "PayPal";
>     }
> }
> 
> // Sistema de procesamiento
> public class SistemaPagos {
>     public static void main(String[] args) {
>         System.out.println("╔════════════════════════════════════╗");
>         System.out.println("║   SISTEMA DE PROCESAMIENTO         ║");
>         System.out.println("║         DE PAGOS                   ║");
>         System.out.println("╚════════════════════════════════════╝");
>         
>         // Crear métodos de pago
>         TarjetaCredito tarjetaCredito = new TarjetaCredito(
>             "Juan Pérez",
>             "1234567890123456",
>             5000.0
>         );
>         
>         TarjetaDebito tarjetaDebito = new TarjetaDebito(
>             "María García",
>             "9876543210",
>             1000.0
>         );
>         
>         PayPal paypal = new PayPal(
>             "Carlos López",
>             "carlos@example.com",
>             2000.0
>         );
>         
>         // POLIMORFISMO (Sobreescritura)
>         System.out.println("\n=== PROCESAMIENTO POLIMÓRFICO ===");
>         MetodoPago[] metodos = {tarjetaCredito, tarjetaDebito, paypal};
>         
>         double montoPago = 150.0;
>         for (MetodoPago metodo : metodos) {
>             System.out.println("\nTipo: " + metodo.obtenerTipo());
>             metodo.procesarPago(montoPago);  // Método sobreescrito
>         }
>         
>         // SOBRECARGA (Diferentes formas de pagar)
>         System.out.println("\n\n=== MÉTODOS SOBRECARGADOS ===");
>         
>         tarjetaCredito.procesarPago(500.0, "Compra de laptop");
>         tarjetaCredito.procesarPago(1200.0, 6, 0.05);  // 6 MSI con 5% comisión
>         
>         tarjetaDebito.procesarPago(200.0, "1234");  // Con PIN
>         
>         paypal.procesarPago(100.0, "amigo@example.com");  // Transferencia
>         paypal.procesarPago(75.0, "EUR", 1.1);  // Pago internacional
>     }
> }
> ```

---

## ⚠️ Errores Comunes y Mejores Prácticas


> [!warning]- 🚫 Errores Frecuentes
> 
> ### 1. Confundir Sobrecarga con Sobreescritura
> 
> ```java
> // ❌ INCORRECTO: Intentar sobreescribir pero en realidad está sobrecargando
> public class Padre {
>     public void mostrar(int numero) {
>         System.out.println("Número: " + numero);
>     }
> }
> 
> public class Hijo extends Padre {
>     // ❌ NO es sobreescritura, es sobrecarga (parámetro double vs int)
>     public void mostrar(double numero) {
>         System.out.println("Double: " + numero);
>     }
> }
> 
> // ✅ CORRECTO: Verdadera sobreescritura
> public class HijoCorrecto extends Padre {
>     @Override  // Esta anotación hubiera detectado el error
>     public void mostrar(int numero) {
>         System.out.println("Sobreescrito: " + numero);
>     }
> }
> ```
> 
> ---
> 
> ### 2. Olvidar @Override
> 
> ```java
> public class Animal {
>     public void hacerSonido() {
>         System.out.println("Sonido genérico");
>     }
> }
> 
> public class Perro extends Animal {
>     // ❌ SIN @Override - typo no detectado
>     public void haserSonido() {  // Error de ortografía
>         System.out.println("Guau");
>     }
> 
>     // ✅ CON @Override - error detectado en compilación
>     @Override
>     public void hacerSonido() {
>         System.out.println("Guau");
>     }
> }
> ```
> 
> ---
> 
> ### 3. Restringir Acceso al Sobreescribir
> 
> ```java
> public class Padre {
>     public void metodo() {
>         System.out.println("Público en padre");
>     }
> 
>     protected void otroMetodo() {
>         System.out.println("Protegido en padre");
>     }
> }
> 
> public class Hijo extends Padre {
>     // ❌ ERROR: no se puede hacer más restrictivo
>     // @Override
>     // protected void metodo() { }  // ERROR DE COMPILACIÓN
> 
>     // ✅ CORRECTO: puede ser igual o más amplio
>     @Override
>     public void metodo() {
>         System.out.println("Público en hijo");
>     }
> 
>     // ✅ CORRECTO: protected → public (ampliación)
>     @Override
>     public void otroMetodo() {
>         System.out.println("Ahora público en hijo");
>     }
> }
> ```
> 
> ---
> 
> ### 4. Sobrecarga Ambigua
> 
> ```java
> public class Calculadora {
>     // ❌ AMBIGUO: puede causar problemas
>     public void calcular(long a, int b) {
>         System.out.println("long, int");
>     }
> 
>     public void calcular(int a, long b) {
>         System.out.println("int, long");
>     }
> 
>     public static void main(String[] args) {
>         Calculadora calc = new Calculadora();
>         // calc.calcular(5, 5);  // ❌ ERROR: llamada ambigua
>         calc.calcular(5L, 5);   // ✅ OK: específico
>         calc.calcular(5, 5L);   // ✅ OK: específico
>     }
> }
> ```
> 
> ---
> 
> ### 5. Intentar Sobreescribir Métodos `static`
> 
> ```java
> public class Padre {
>     public static void metodoEstatico() {
>         System.out.println("Método estático del padre");
>     }
> }
> 
> public class Hijo extends Padre {
>     // ⚠️ NO es sobreescritura, es "method hiding" (ocultar método)
>     public static void metodoEstatico() {
>         System.out.println("Método estático del hijo");
>     }
> 
>     public static void main(String[] args) {
>         Padre p = new Hijo();
>         p.metodoEstatico();  // Imprime: "Método estático del padre"
>         // Los métodos estáticos se resuelven en tiempo de compilación,
>         // no en tiempo de ejecución (no hay polimorfismo)
> 
>         Hijo h = new Hijo();
>         h.metodoEstatico();  // Imprime: "Método estático del hijo"
>     }
> }
> ```
> 
> ---
> 
> ### 6. Tipo de Retorno Incompatible
> 
> ```java
> public class Padre {
>     public Number obtenerValor() {
>         return 10;
>     }
> }
> 
> public class Hijo extends Padre {
>     // ✅ CORRECTO: tipo covariante (Integer es subtipo de Number)
>     @Override
>     public Integer obtenerValor() {
>         return 20;
>     }
> }
> 
> public class HijoIncorrecto extends Padre {
>     // ❌ ERROR: Double no es compatible (no es subtipo específico)
>     // @Override
>     // public Double obtenerValor() {  // ERROR DE COMPILACIÓN
>     //     return 20.0;
>     // }
> }
> ```
> 
> ---
> 
> ### 7. Excepciones Más Amplias al Sobreescribir
> 
> ```java
> import java.io.IOException;
> import java.io.FileNotFoundException;
> 
> public class Padre {
>     public void leerArchivo() throws FileNotFoundException {
>         System.out.println("Leyendo archivo");
>     }
> }
> 
> public class Hijo extends Padre {
>     // ❌ ERROR: IOException es más amplia que FileNotFoundException
>     // @Override
>     // public void leerArchivo() throws IOException {  // ERROR
>     //     System.out.println("Leyendo archivo en hijo");
>     // }
> 
>     // ✅ CORRECTO: misma excepción o ninguna
>     @Override
>     public void leerArchivo() throws FileNotFoundException {
>         System.out.println("Leyendo archivo en hijo");
>     }
> 
>     // ✅ CORRECTO: sin excepciones (reducción)
>     // @Override
>     // public void leerArchivo() {
>     //     System.out.println("Sin excepciones");
>     // }
> }
> ```
> 

### Mejores Prácticas

> [!tip]- ✅ Recomendaciones
> 
> **1. Siempre usar @Override**
> ```java
> // ✅ BUENA PRÁCTICA
> public class Animal {
>     public void hacerSonido() { }
> }
> 
> public class Perro extends Animal {
>     @Override  // Detecta errores en tiempo de compilación
>     public void hacerSonido() {
>         System.out.println("Guau");
>     }
> }
> ```
> 
> **2. Documentar Sobrecarga Claramente**
> ```java
> public class Utilidades {
>     /**
>      * Formatea un número entero.
>      * @param numero El número a formatear
>      * @return String formateado
>      */
>     public String formatear(int numero) {
>         return String.valueOf(numero);
>     }
>     
>     /**
>      * Formatea un número decimal con precisión específica.
>      * @param numero El número a formatear
>      * @param decimales Cantidad de decimales
>      * @return String formateado
>      */
>     public String formatear(double numero, int decimales) {
>         return String.format("%." + decimales + "f", numero);
>     }
> }
> ```
> 
> **3. Preferir Métodos más Específicos**
> ```java
> public class Calculadora {
>     // ✅ BUENO: métodos específicos en lugar de varargs genéricos
>     public int sumar(int a, int b) {
>         return a + b;
>     }
>     
>     public int sumar(int a, int b, int c) {
>         return a + b + c;
>     }
>     
>     // Varargs como respaldo
>     public int sumar(int... numeros) {
>         int suma = 0;
>         for (int n : numeros) suma += n;
>         return suma;
>     }
> }
> ```
> 
> **4. Llamar a super cuando sea apropiado**
> ```java
> public class Vehiculo {
>     protected String marca;
>     
>     public void mostrarInfo() {
>         System.out.println("Marca: " + marca);
>     }
> }
> 
> public class Auto extends Vehiculo {
>     private int puertas;
>     
>     @Override
>     public void mostrarInfo() {
>         // ✅ BUENO: reutilizar código del padre
>         super.mostrarInfo();
>         System.out.println("Puertas: " + puertas);
>     }
> }
> ```
> 
> **5. Mantener Contratos Consistentes**
> ```java
> public class Figura {
>     /**
>      * Calcula el área de la figura.
>      * @return Área en unidades cuadradas (nunca negativo)
>      */
>     public double calcularArea() {
>         return 0.0;
>     }
> }
> 
> public class Circulo extends Figura {
>     private double radio;
>     
>     @Override
>     public double calcularArea() {
>         // ✅ BUENO: mantener el contrato (nunca retorna negativo)
>         if (radio < 0) return 0.0;
>         return Math.PI * radio * radio;
>     }
> }
> ```

---

## 🎯 Ejercicios Propuestos

> [!example]- 💪 Práctica
> 
> ### Nivel Básico:
> 
> **1. Sistema de Conversión de Unidades**
> - Crear clase `Conversor` con métodos sobrecargados:
>   - `convertir(double metros)` → a kilómetros
>   - `convertir(double valor, String unidad)` → conversión específica
>   - `convertir(double valor, String de, String a)` → entre unidades
> 
> **2. Jerarquía de Vehículos**
> - Clase `Vehiculo` con método `calcularCosto()`
> - Clases hijas: `Auto`, `Moto`, `Camion`
> - Sobreescribir cálculo según tipo de vehículo
> - Agregar sobrecarga para cálculo con descuento
> 
> **3. Sistema de Impresión**
> - Clase `Impresora` con método `imprimir()`
> - Sobrecargar para: `String`, `int`, array de `String`
> - Crear subclases: `ImpresoraLaser`, `ImpresoraInkjet`
> - Sobreescribir según características de cada impresora
> 
> ### Nivel Intermedio:
> 
> **4. Sistema de Reservas de Hotel**
> ```java
> abstract class Habitacion {
>     // Método para sobreescribir
>     abstract double calcularPrecio(int noches);
>     
>     // Métodos para sobrecargar
>     double calcularPrecio(int noches, boolean incluyeDesayuno) { }
>     double calcularPrecio(int noches, int personas) { }
> }
> 
> class Simple extends Habitacion { }
> class Doble extends Habitacion { }
> class Suite extends Habitacion { }
> ```
> 
> **5. Sistema de Mensajería**
> - Clase abstracta `Mensaje` con método `enviar()`
> - Subclases: `MensajeTexto`, `MensajeMultimedia`, `MensajeVoz`
> - Sobrecargar `enviar()` con diferentes parámetros (prioridad, programado, etc.)
> - Implementar cola de mensajes con polimorfismo
> 
> **6. Calculadora Científica**
> - Extender clase `Calculadora` básica
> - Sobrecargar operaciones: `calcular(double a, double b, String operacion)`
> - Agregar funciones científicas: potencia, raíz, logaritmo
> - Soportar operaciones con múltiples parámetros
> 
> ### Nivel Avanzado:
> 
> **7. Sistema de Procesamiento de Pedidos**
> ```java
> abstract class Pedido {
>     abstract double calcularTotal();
>     abstract void procesar();
>     
>     // Sobrecargar para diferentes formas de procesamiento
>     void procesar(boolean express) { }
>     void procesar(String direccion, String metodoEnvio) { }
>     void procesar(MetodoPago pago, int cuotas) { }
> }
> ```
> 
> **8. Framework de Validación**
> - Clase `Validador<T>` con método `validar(T dato)`
> - Subclases para diferentes tipos: email, teléfono, DNI
> - Sobrecargar `validar()` con diferentes niveles de estrictez
> - Implementar cadena de validadores
> 
> **9. Motor de Renderizado Gráfico**
> - Clase abstracta `Renderizador`
> - Método `renderizar(Figura figura)`
> - Sobrecargar para diferentes tipos de salida (pantalla, archivo, impresora)
> - Sobreescribir en subclases: `Renderizador2D`, `Renderizador3D`
> 
> **10. Sistema de Logging Multinivel**
> - Clase base `Logger` con método `log(String mensaje)`
> - Sobrecargar con nivel, timestamp, contexto
> - Subclases: `ConsoleLogger`, `FileLogger`, `DatabaseLogger`
> - Implementar formateo específico en cada subclase

---

## 🔍 Preguntas Técnicas Frecuentes

> [!question]- 🤔 FAQ
> 
> **1. ¿Cuál es más eficiente: sobrecarga o sobreescritura?**
> - **Sobrecarga:** Más eficiente - se resuelve en compilación
> - **Sobreescritura:** Pequeño overhead - se resuelve en ejecución mediante dynamic dispatch
> - La diferencia de rendimiento es mínima en aplicaciones modernas
> 
> **2. ¿Puedo sobrecargar métodos estáticos?**
> ```java
> // ✅ SÍ - La sobrecarga funciona con métodos estáticos
> public class MathUtils {
>     public static int max(int a, int b) {
>         return a > b ? a : b;
>     }
>     
>     public static double max(double a, double b) {
>         return a > b ? a : b;
>     }
> }
> ```
> 
> **3. ¿Puedo sobreescribir métodos privados?**
> ```java
> // ❌ NO - Los métodos privados no se heredan
> public class Padre {
>     private void metodoPrivado() { }
> }
> 
> public class Hijo extends Padre {
>     // NO es sobreescritura, es un método nuevo
>     private void metodoPrivado() { }
> }
> ```
> 
> **4. ¿Qué es "method hiding"?**
> ```java
> // Ocurre con métodos estáticos
> public class A {
>     public static void metodo() {
>         System.out.println("A");
>     }
> }
> 
> public class B extends A {
>     public static void metodo() {  // Oculta, no sobreescribe
>         System.out.println("B");
>     }
> }
> 
> // Se resuelve según el tipo de referencia, no el tipo de objeto
> A obj = new B();
> obj.metodo();  // Imprime "A" (tipo de referencia)
> ```
> 
> **5. ¿Cuántos métodos sobrecargados puedo tener?**
> - No hay límite técnico
> - Límite práctico: mantener código legible y mantenible
> - Recomendación: máximo 3-5 variantes
> - Considerar usar Builder pattern si hay muchas variaciones
> 
> **6. ¿Puedo usar sobrecarga con constructores?**
> ```java
> // ✅ SÍ - Muy común
> public class Persona {
>     private String nombre;
>     private int edad;
>     
>     public Persona() {
>         this("Sin nombre", 0);
>     }
>     
>     public Persona(String nombre) {
>         this(nombre, 0);
>     }
>     
>     public Persona(String nombre, int edad) {
>         this.nombre = nombre;
>         this.edad = edad;
>     }
> }
> ```
> 
> **7. ¿Qué pasa si dos métodos sobrecargados son igualmente específicos?**
> ```java
> public class Ambiguo {
>     public void metodo(Object o, String s) { }
>     public void metodo(String s, Object o) { }
>     
>     public static void main(String[] args) {
>         Ambiguo a = new Ambiguo();
>         // a.metodo("hola", "mundo");  // ❌ ERROR: ambiguo
>         a.metodo((Object)"hola", "mundo");  // ✅ OK: cast explícito
>     }
> }
> ```
> 
> **8. ¿Puedo sobreescribir y sobrecargar al mismo tiempo?**
> ```java
> // ✅ SÍ - Perfectamente válido
> public class Padre {
>     public void metodo(int x) {
>         System.out.println("Padre: " + x);
>     }
> }
> 
> public class Hijo extends Padre {
>     @Override
>     public void metodo(int x) {  // Sobreescritura
>         System.out.println("Hijo: " + x);
>     }
>     
>     public void metodo(double x) {  // Sobrecarga
>         System.out.println("Hijo double: " + x);
>     }
> }
> ```

---

## 📊 Tabla de Decisión

> [!note]- 🎯 ¿Cuándo usar cada uno?
> 
> | Escenario | Usar Sobrecarga | Usar Sobreescritura |
> |-----------|-----------------|---------------------|
> | **Misma clase, diferentes parámetros** | ✅ | ❌ |
> | **Cambiar comportamiento heredado** | ❌ | ✅ |
> | **Múltiples formas de hacer lo mismo** | ✅ | ❌ |
> | **Polimorfismo runtime** | ❌ | ✅ |
> | **Mantener API flexible** | ✅ | ❌ |
> | **Implementar jerarquía de clases** | ❌ | ✅ |
> | **Diferentes tipos de entrada** | ✅ | ❌ |
> | **Especializar comportamiento por tipo** | ❌ | ✅ |
> | **Métodos estáticos** | ✅ | ❌ |
> | **Constructores** | ✅ | ❌ |

---

## 🌟 Ejemplo Final: Sistema Completo

> [!example]- 🎮 Sistema de Juego RPG
> 
> ```java
> // ═══════════════════════════════════════════
> // CLASE BASE
> // ═══════════════════════════════════════════
> 
> public abstract class Personaje {
>     protected String nombre;
>     protected int vida;
>     protected int vidaMaxima;
>     protected int nivel;
>     
>     public Personaje(String nombre, int vidaMaxima) {
>         this.nombre = nombre;
>         this.vidaMaxima = vidaMaxima;
>         this.vida = vidaMaxima;
>         this.nivel = 1;
>     }
>     
>     // Método abstracto para sobreescribir
>     public abstract int atacar();
>     
>     // SOBRECARGA del método atacar
>     public int atacar(boolean critico) {
>         int danio = atacar();
>         if (critico) {
>             danio *= 2;
>             System.out.println("¡GOLPE CRÍTICO!");
>         }
>         return danio;
>     }
>     
>     public int atacar(Personaje objetivo) {
>         int danio = atacar();
>         objetivo.recibirDanio(danio);
>         return danio;
>     }
>     
>     public int atacar(Personaje objetivo, boolean critico) {
>         int danio = atacar(critico);
>         objetivo.recibirDanio(danio);
>         return danio;
>     }
>     
>     // Método para sobreescribir
>     public void recibirDanio(int danio) {
>         vida -= danio;
>         if (vida < 0) vida = 0;
>         System.out.println(nombre + " recibe " + danio + " de daño (Vida: " + vida + "/" + vidaMaxima + ")");
>     }
>     
>     // SOBRECARGA de curación
>     public void curar() {
>         vida = vidaMaxima;
>         System.out.println(nombre + " ha sido completamente curado");
>     }
>     
>     public void curar(int cantidad) {
>         vida = Math.min(vida + cantidad, vidaMaxima);
>         System.out.println(nombre + " se cura " + cantidad + " puntos");
>     }
>     
>     public void curar(double porcentaje) {
>         int cantidad = (int)(vidaMaxima * porcentaje);
>         curar(cantidad);
>     }
>     
>     public boolean estaVivo() {
>         return vida > 0;
>     }
>     
>     public void mostrarEstado() {
>         System.out.println("\n--- " + nombre + " ---");
>         System.out.println("Clase: " + this.getClass().getSimpleName());
>         System.out.println("Nivel: " + nivel);
>         System.out.println("Vida: " + vida + "/" + vidaMaxima);
>     }
>     
>     public String getNombre() { return nombre; }
> }
> 
> // ═══════════════════════════════════════════
> // CLASES ESPECÍFICAS
> // ═══════════════════════════════════════════
> 
> public class Guerrero extends Personaje {
>     private int fuerza;
>     private int armadura;
>     
>     public Guerrero(String nombre) {
>         super(nombre, 150);
>         this.fuerza = 20;
>         this.armadura = 10;
>     }
>     
>     // SOBREESCRITURA
>     @Override
>     public int atacar() {
>         System.out.println(nombre + " ataca con su espada");
>         return fuerza + (nivel * 2);
>     }
>     
>     // SOBRECARGA específica del Guerrero
>     public int atacar(String tipoAtaque) {
>         int danio;
>         switch (tipoAtaque.toLowerCase()) {
>             case "normal":
>                 danio = atacar();
>                 break;
>             case "fuerte":
>                 System.out.println(nombre + " usa GOLPE FUERTE");
>                 danio = (int)(fuerza * 1.5);
>                 break;
>             case "giratorio":
>                 System.out.println(nombre + " usa ATAQUE GIRATORIO");
>                 danio = (int)(fuerza * 1.3);
>                 break;
>             default:
>                 danio = atacar();
>         }
>         return danio;
>     }
>     
>     // SOBREESCRITURA con armadura
>     @Override
>     public void recibirDanio(int danio) {
>         int danioReducido = Math.max(1, danio - armadura);
>         System.out.println("Armadura bloquea " + (danio - danioReducido) + " de daño");
>         super.recibirDanio(danioReducido);
>     }
>     
>     @Override
>     public void mostrarEstado() {
>         super.mostrarEstado();
>         System.out.println("Fuerza: " + fuerza);
>         System.out.println("Armadura: " + armadura);
>     }
> }
> 
> public class Mago extends Personaje {
>     private int mana;
>     private int manaMaximo;
>     private int poder;
>     
>     public Mago(String nombre) {
>         super(nombre, 80);
>         this.manaMaximo = 100;
>         this.mana = manaMaximo;
>         this.poder = 25;
>     }
>     
>     // SOBREESCRITURA
>     @Override
>     public int atacar() {
>         if (mana >= 10) {
>             mana -= 10;
>             System.out.println(nombre + " lanza un hechizo (Mana: " + mana + "/" + manaMaximo + ")");
>             return poder + (nivel * 3);
>         } else {
>             System.out.println(nombre + " no tiene suficiente mana");
>             return 5;  // Ataque débil sin mana
>         }
>     }
>     
>     // SOBRECARGA específica del Mago
>     public int atacar(String hechizo) {
>         int danio = 0;
>         switch (hechizo.toLowerCase()) {
>             case "bola de fuego":
>                 if (mana >= 20) {
>                     mana -= 20;
>                     System.out.println(nombre + " lanza BOLA DE FUEGO");
>                     danio = (int)(poder * 2);
>                 } else {
>                     System.out.println("Mana insuficiente para Bola de Fuego");
>                 }
>                 break;
>             case "rayo":
>                 if (mana >= 15) {
>                     mana -= 15;
>                     System.out.println(nombre + " lanza RAYO");
>                     danio = (int)(poder * 1.5);
>                 } else {
>                     System.out.println("Mana insuficiente para Rayo");
>                 }
>                 break;
>             default:
>                 danio = atacar();
>         }
>         return danio;
>     }
>     
>     public void restaurarMana(int cantidad) {
>         mana = Math.min(mana + cantidad, manaMaximo);
>         System.out.println(nombre + " restaura " + cantidad + " de mana");
>     }
>     
>     @Override
>     public void mostrarEstado() {
>         super.mostrarEstado();
>         System.out.println("Mana: " + mana + "/" + manaMaximo);
>         System.out.println("Poder: " + poder);
>     }
> }
> 
> public class Arquero extends Personaje {
>     private int flechas;
>     private int precision;
>     
>     public Arquero(String nombre) {
>         super(nombre, 100);
>         this.flechas = 30;
>         this.precision = 15;
>     }
>     
>     // SOBREESCRITURA
>     @Override
>     public int atacar() {
>         if (flechas > 0) {
>             flechas--;
>             System.out.println(nombre + " dispara una flecha (Flechas: " + flechas + ")");
>             return precision + (nivel * 2);
>         } else {
>             System.out.println(nombre + " no tiene flechas");
>             return 3;  // Ataque cuerpo a cuerpo débil
>         }
>     }
>     
>     // SOBRECARGA específica del Arquero
>     public int atacar(int numeroFlechas) {
>         if (flechas >= numeroFlechas) {
>             flechas -= numeroFlechas;
>             System.out.println(nombre + " dispara " + numeroFlechas + " flechas");
>             return (precision + nivel) * numeroFlechas;
>         } else {
>             System.out.println("No hay suficientes flechas");
>             return atacar();
>         }
>     }
>     
>     public int atacar(String tipoFlecha, int cantidad) {
>         int multiplicador = 1;
>         switch (tipoFlecha.toLowerCase()) {
>             case "fuego":
>                 multiplicador = 2;
>                 System.out.println(nombre + " usa FLECHAS DE FUEGO");
>                 break;
>             case "hielo":
>                 multiplicador = 2;
>                 System.out.println(nombre + " usa FLECHAS DE HIELO");
>                 break;
>             case "veneno":
>                 multiplicador = 3;
>                 System.out.println(nombre + " usa FLECHAS ENVENENADAS");
>                 break;
>         }
>         
>         if (flechas >= cantidad) {
>             flechas -= cantidad;
>             return (precision + nivel) * cantidad * multiplicador;
>         }
>         return 0;
>     }
>     
>     public void recargarFlechas(int cantidad) {
>         flechas += cantidad;
>         System.out.println(nombre + " recarga " + cantidad + " flechas (Total: " + flechas + ")");
>     }
>     
>     @Override
>     public void mostrarEstado() {
>         super.mostrarEstado();
>         System.out.println("Flechas: " + flechas);
>         System.out.println("Precisión: " + precision);
>     }
> }
> 
> // ═══════════════════════════════════════════
> // SISTEMA DE COMBATE
> // ═══════════════════════════════════════════
> 
> public class SistemaCombate {
>     public static void main(String[] args) {
>         System.out.println("╔════════════════════════════════════════════╗");
>         System.out.println("║         SISTEMA DE COMBATE RPG             ║");
>         System.out.println("║  Sobrecarga + Sobreescritura en Acción     ║");
>         System.out.println("╚════════════════════════════════════════════╝\n");
>         
>         // Crear personajes
>         Guerrero guerrero = new Guerrero("Arthas");
>         Mago mago = new Mago("Jaina");
>         Arquero arquero = new Arquero("Sylvanas");
>         
>         // ═══════════════════════════════════════════
>         // DEMOSTRACIÓN DE POLIMORFISMO (Sobreescritura)
>         // ═══════════════════════════════════════════
>         System.out.println("=== POLIMORFISMO: Mismo método, diferentes comportamientos ===\n");
>         
>         Personaje[] personajes = {guerrero, mago, arquero};
>         
>         for (Personaje p : personajes) {
>             p.mostrarEstado();
>             int danio = p.atacar();  // Método sobreescrito en cada clase
>             System.out.println("Daño infligido: " + danio);
>             System.out.println();
>         }
>         
>         // ═══════════════════════════════════════════
>         // DEMOSTRACIÓN DE SOBRECARGA
>         // ═══════════════════════════════════════════
>         System.out.println("\n=== SOBRECARGA: Múltiples formas de atacar ===\n");
>         
>         // Guerrero - diferentes ataques
>         System.out.println("--- GUERRERO ---");
>         guerrero.atacar();                        // Ataque básico
>         guerrero.atacar(true);                    // Ataque crítico
>         guerrero.atacar("fuerte");                // Ataque fuerte
>         guerrero.atacar("giratorio");             // Ataque giratorio
>         System.out.println();
>         
>         // Mago - diferentes hechizos
>         System.out.println("--- MAGO ---");
>         mago.atacar();                            // Hechizo básico
>         mago.atacar("bola de fuego");             // Hechizo poderoso
>         mago.atacar("rayo");                      // Otro hechizo
>         mago.atacar();                            // Sin mana suficiente
>         mago.restaurarMana(50);
>         System.out.println();
>         
>         // Arquero - múltiples flechas
>         System.out.println("--- ARQUERO ---");
>         arquero.atacar();                         // Una flecha
>         arquero.atacar(3);                        // Tres flechas
>         arquero.atacar("fuego", 2);               // Flechas especiales
>         arquero.recargarFlechas(10);
>         System.out.println();
>         
>         // ═══════════════════════════════════════════
>         // COMBATE SIMULADO
>         // ═══════════════════════════════════════════
>         System.out.println("\n=== COMBATE: Guerrero vs Mago ===\n");
>         
>         System.out.println("¡COMIENZA LA BATALLA!\n");
>         
>         // Turno 1
>         System.out.println("--- TURNO 1 ---");
>         guerrero.atacar(mago);
>         mago.atacar(guerrero, true);  // Con crítico
>         
>         // Turno 2
>         System.out.println("\n--- TURNO 2 ---");
> 	        guerrero.atacar(mago, "fuerte");
> 	        mago.atacar(guerrero, "bola de fuego");
>         
>         // Turno 3
>         System.out.println("\n--- TURNO 3 ---");
>         guerrero.curar(0.3);  // Curar 30%
>         mago.atacar(guerrero);
>         
>         // Estado final
>         System.out.println("\n=== ESTADO FINAL DE LA BATALLA ===");
>         guerrero.mostrarEstado();
>         mago.mostrarEstado();
>         
>         // ═══════════════════════════════════════════
>         // DEMOSTRACIÓN DE CURACIÓN (Sobrecarga)
>         // ═══════════════════════════════════════════
>         System.out.println("\n\n=== CURACIÓN: Diferentes formas ===\n");
>         
>         arquero.recibirDanio(50);  // Simular daño
>         
>         System.out.println("--- Curación completa ---");
>         arquero.curar();  // Sin parámetros
>         
>         arquero.recibirDanio(40);  // Más daño
>         
>         System.out.println("\n--- Curación por cantidad ---");
>         arquero.curar(20);  // Cantidad específica
>         
>         arquero.recibirDanio(30);
>         
>         System.out.println("\n--- Curación por porcentaje ---");
>         arquero.curar(0.5);  // 50% de vida máxima
>         
>         arquero.mostrarEstado();
>         
>         // ═══════════════════════════════════════════
>         // BATALLA MÚLTIPLE
>         // ═══════════════════════════════════════════
>         System.out.println("\n\n=== BATALLA MÚLTIPLE ===\n");
>         
>         Guerrero boss = new Guerrero("Boss Final");
>         boss.curar();  // Vida completa
>         
>         System.out.println("¡Los héroes enfrentan al Boss Final!\n");
>         
>         int turno = 1;
>         while (boss.estaVivo() && (guerrero.estaVivo() || mago.estaVivo() || arquero.estaVivo())) {
>             System.out.println("--- TURNO " + turno + " ---");
>             
>             if (guerrero.estaVivo()) {
>                 guerrero.atacar(boss, turno % 3 == 0);  // Crítico cada 3 turnos
>             }
>             
>             if (mago.estaVivo()) {
>                 if (turno % 2 == 0) {
>                     mago.atacar(boss, "bola de fuego");
>                 } else {
>                     mago.atacar(boss);
>                 }
>             }
>             
>             if (arquero.estaVivo()) {
>                 if (turno % 4 == 0) {
>                     arquero.atacar(boss, "veneno", 2);
>                 } else {
>                     arquero.atacar(boss);
>                 }
>             }
>             
>             // Boss contraataca
>             if (boss.estaVivo()) {
>                 System.out.println("\n" + boss.getNombre() + " contraataca:");
>                 if (guerrero.estaVivo()) boss.atacar(guerrero, "fuerte");
>             }
>             
>             System.out.println();
>             turno++;
>             
>             if (turno > 10) break;  // Límite de turnos
>         }
>         
>         // Resultado final
>         System.out.println("\n╔════════════════════════════════════════════╗");
>         System.out.println("║            RESULTADO FINAL                 ║");
>         System.out.println("╚════════════════════════════════════════════╝\n");
>         
>         System.out.println("=== ESTADO DE LOS HÉROES ===");
>         guerrero.mostrarEstado();
>         mago.mostrarEstado();
>         arquero.mostrarEstado();
>         
>         System.out.println("\n=== ESTADO DEL BOSS ===");
>         boss.mostrarEstado();
>         
>         if (boss.estaVivo()) {
>             System.out.println("\n❌ El Boss Final ha derrotado a los héroes...");
>         } else {
>             System.out.println("\n✅ ¡Los héroes han derrotado al Boss Final!");
>         }
>     }
> }
> ```

---

## 🎓 Conceptos Avanzados

### Covarianza de Tipos de Retorno

> [!note]- 🔄 Tipos de Retorno Covariantes
> 
> Desde Java 5, puedes usar un subtipo como tipo de retorno al sobreescribir:
> 
> ```java
> // Jerarquía de clases
> class Animal {
>     public String getNombre() {
>         return "Animal genérico";
>     }
> }
> 
> class Perro extends Animal {
>     @Override
>     public String getNombre() {
>         return "Perro";
>     }
> }
> 
> class Gato extends Animal {
>     @Override
>     public String getNombre() {
>         return "Gato";
>     }
> }
> 
> // Clase que crea animales
> class FabricaAnimales {
>     // Método que retorna Animal
>     public Animal crearAnimal() {
>         return new Animal();
>     }
> }
> 
> // Fábrica especializada con covarianza
> class FabricaPerros extends FabricaAnimales {
>     // ✅ VÁLIDO: Perro es subtipo de Animal
>     @Override
>     public Perro crearAnimal() {  // Tipo de retorno covariante
>         return new Perro();
>     }
> }
> 
> class FabricaGatos extends FabricaAnimales {
>     @Override
>     public Gato crearAnimal() {  // Tipo de retorno covariante
>         return new Gato();
>     }
> }
> 
> // Ejemplo más complejo
> class Contenedor<T> {
>     protected T contenido;
>     
>     public T obtener() {
>         return contenido;
>     }
> }
> 
> class ContenedorNumeros extends Contenedor<Number> {
>     @Override
>     public Number obtener() {
>         return contenido;
>     }
> }
> 
> class ContenedorEnteros extends ContenedorNumeros {
>     // ✅ VÁLIDO: Integer es subtipo de Number
>     @Override
>     public Integer obtener() {
>         return (Integer) contenido;
>     }
> }
> 
> // Demostración
> public class CovarianzaDemo {
>     public static void main(String[] args) {
>         System.out.println("=== COVARIANZA DE TIPOS DE RETORNO ===\n");
>         
>         // Uso polimórfico con tipos más específicos
>         FabricaAnimales fabrica1 = new FabricaPerros();
>         FabricaAnimales fabrica2 = new FabricaGatos();
>         
>         Animal animal1 = fabrica1.crearAnimal();  // Retorna Perro
>         Animal animal2 = fabrica2.crearAnimal();  // Retorna Gato
>         
>         System.out.println("Animal 1: " + animal1.getNombre());
>         System.out.println("Animal 2: " + animal2.getNombre());
>         
>         // Uso con tipo específico
>         FabricaPerros fabricaPerros = new FabricaPerros();
>         Perro perro = fabricaPerros.crearAnimal();  // No necesita cast
>         System.out.println("Perro: " + perro.getNombre());
>     }
> }
> ```

### Bridge Methods (Métodos Puente)

> [!info]- 🌉 Métodos Generados por el Compilador
> 
> El compilador a veces genera métodos "puente" para mantener compatibilidad:
> 
> ```java
> class Nodo<T> {
>     public T dato;
>     
>     public Nodo(T dato) {
>         this.dato = dato;
>     }
>     
>     public void setDato(T dato) {
>         this.dato = dato;
>     }
> }
> 
> class NodoEntero extends Nodo<Integer> {
>     public NodoEntero(Integer dato) {
>         super(dato);
>     }
>     
>     // Sobreescritura con tipo específico
>     @Override
>     public void setDato(Integer dato) {
>         System.out.println("Estableciendo entero: " + dato);
>         super.setDato(dato);
>     }
>     
>     // El compilador genera un "bridge method" así:
>     // public void setDato(Object dato) {
>     //     setDato((Integer) dato);
>     // }
>     // Este método permite polimorfismo correcto
> }
> 
> public class BridgeMethodDemo {
>     public static void main(String[] args) {
>         NodoEntero nodo = new NodoEntero(10);
>         
>         // Ambas llamadas funcionan gracias al bridge method
>         nodo.setDato(20);                    // Llamada directa
>         ((Nodo<Integer>) nodo).setDato(30);  // A través del padre
>     }
> }
> ```

### Resolución de Métodos

> [!example]- 🔍 Cómo Java Elige el Método Correcto
> 
> **Para Sobrecarga (Compile-time):**
> 
> ```java
> public class ResolucionSobrecarga {
>     public void procesar(Object o) {
>         System.out.println("Object");
>     }
>     
>     public void procesar(String s) {
>         System.out.println("String");
>     }
>     
>     public void procesar(Integer i) {
>         System.out.println("Integer");
>     }
>     
>     public static void main(String[] args) {
>         ResolucionSobrecarga obj = new ResolucionSobrecarga();
>         
>         // El compilador elige el método más específico
>         obj.procesar("texto");           // String (más específico)
>         obj.procesar(123);               // Integer (más específico)
>         obj.procesar(new Object());      // Object (único compatible)
>         
>         // Con polimorfismo
>         Object o1 = "texto";
>         Object o2 = 123;
>         
>         obj.procesar(o1);  // Object (tipo de referencia)
>         obj.procesar(o2);  // Object (tipo de referencia)
>         
>         // Esto demuestra que la sobrecarga se resuelve
>         // según el tipo de REFERENCIA, no el tipo de OBJETO
>     }
> }
> ```
> 
> **Para Sobreescritura (Runtime):**
> 
> ```java
> class A {
>     public void metodo() {
>         System.out.println("A");
>     }
> }
> 
> class B extends A {
>     @Override
>     public void metodo() {
>         System.out.println("B");
>     }
> }
> 
> class C extends B {
>     @Override
>     public void metodo() {
>         System.out.println("C");
>     }
> }
> 
> public class ResolucionSobreescritura {
>     public static void main(String[] args) {
>         // La JVM busca el método en tiempo de ejecución
>         A obj1 = new A();
>         A obj2 = new B();
>         A obj3 = new C();
>         
>         obj1.metodo();  // "A" - sin sobreescritura
>         obj2.metodo();  // "B" - método de B
>         obj3.metodo();  // "C" - método de C
>         
>         // Esto demuestra que la sobreescritura se resuelve
>         // según el tipo de OBJETO, no el tipo de REFERENCIA
>         
>         // Proceso de búsqueda en runtime:
>         // 1. Busca en la clase del objeto (C)
>         // 2. Si no encuentra, busca en la superclase (B)
>         // 3. Continúa hasta encontrar o llegar a Object
>     }
> }
> ```

---

## 📚 Resumen Final

> [!quote]- 🎯 Puntos Clave
> 
> ### Sobrecarga (Overloading)
> - ✅ Mismo nombre, diferentes parámetros
> - ✅ Misma clase o clase hija
> - ✅ Resuelto en tiempo de compilación
> - ✅ No requiere herencia
> - ✅ Aumenta flexibilidad de API
> - ✅ También funciona con constructores
> 
> ### Sobreescritura (Overriding)
> - ✅ Mismo nombre y misma firma
> - ✅ Requiere herencia (clase padre → hija)
> - ✅ Resuelto en tiempo de ejecución
> - ✅ Permite polimorfismo runtime
> - ✅ Usa anotación @Override
> - ✅ Puede usar super.metodo()
> 
> ### Combinación Poderosa
> - 🎭 Ambos trabajan juntos para crear código flexible
> - 🎯 Sobrecarga para conveniencia del API
> - 🎨 Sobreescritura para polimorfismo
> - 💡 Fundamentales en diseño orientado a objetos
> 
> ### Cuándo Usar Cada Uno
> | Necesidad | Solución |
> |-----------|----------|
> | Múltiples formas de llamar mismo método | Sobrecarga |
> | Cambiar comportamiento heredado | Sobreescritura |
> | Diferentes tipos de entrada | Sobrecarga |
> | Especialización por tipo de objeto | Sobreescritura |
> | API flexible y conveniente | Sobrecarga |
> | Jerarquía de clases polimórfica | Sobreescritura |

---

## 🔗 Conexión con Próximos Temas

> [!note]- 🌟 Continuando el Aprendizaje
> 
> **Has dominado:**
> - ✅ Diferencias entre sobrecarga y sobreescritura
> - ✅ Cuándo y cómo usar cada técnica
> - ✅ Reglas y restricciones de cada una
> - ✅ Polimorfismo en tiempo de compilación vs ejecución
> - ✅ Patrones y mejores prácticas
> - ✅ Casos de uso reales y complejos
> 
> **Próximos temas relacionados:**
> - **[[Polimorfismo Avanzado]]** - Interfaces, clases abstractas
> - **[[Clases Abstractas]]** - Contratos con implementación parcial
> - **[[Interfaces]]** - Contratos puros y herencia múltiple
> - **[[Genéricos]]** - Type safety con tipos parametrizados
> - **[[Design Patterns]]** - Strategy, Template Method, Factory
> - **[[SOLID Principles]]** - Principios de diseño orientado a objetos

---

## 📖 Glosario Rápido

> [!info]- 📝 Términos Importantes
> 
> - **Sobrecarga (Overloading):** Múltiples métodos con mismo nombre pero diferentes parámetros
> - **Sobreescritura (Overriding):** Redefinir método heredado en subclase
> - **Firma del método:** Nombre + tipos de parámetros (no incluye tipo de retorno)
> - **Polimorfismo:** Capacidad de un objeto de tomar múltiples formas
> - **Compile-time polymorphism:** Polimorfismo resuelto en compilación (sobrecarga)
> - **Runtime polymorphism:** Polimorfismo resuelto en ejecución (sobreescritura)
> - **Type promotion:** Conversión automática de tipos en sobrecarga
> - **Covariant return type:** Subtipo como tipo de retorno en sobreescritura
> - **Method hiding:** Ocultar método estático del padre (no sobreescritura)
> - **Bridge method:** Método generado por compilador para compatibilidad
> - **Dynamic dispatch:** Selección del método en runtime basado en tipo de objeto
> - **Varargs:** Número variable de argumentos (...)

---

**Tags:** #java #sobrecarga #sobreescritura #overloading #overriding #polimorfismo #poo #herencia #métodos #buenas-practicas


