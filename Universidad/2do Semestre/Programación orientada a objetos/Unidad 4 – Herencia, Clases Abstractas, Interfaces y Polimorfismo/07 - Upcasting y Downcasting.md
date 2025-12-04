# 🔄 Upcasting y Downcasting en Java

## 🎯 Introducción

> [!info]- 💡 ¿Qué es el Casting? El **casting** es la conversión de un tipo de dato a otro. En POO, se refiere específicamente a la conversión entre tipos de una jerarquía de herencia.
> 
> **Analogía:** Como diferentes niveles de zoom en un mapa
> 
> - **Upcasting (alejar zoom):** Ver la categoría general - "Es un Animal"
> - **Downcasting (acercar zoom):** Ver detalles específicos - "Es un Perro con collar"
> 
> **Dos tipos principales:**
> 
> - **Upcasting ⬆️:** Hijo → Padre (implícito, siempre seguro)
> - **Downcasting ⬇️:** Padre → Hijo (explícito, puede fallar)
> 
> **Conceptos clave:**
> 
> - **Tipo de referencia:** Lo que "ve" el compilador
> - **Tipo real (objeto):** Lo que realmente es en memoria
> - **instanceof:** Operador para verificar tipos

---

## ⬆️ Upcasting (Conversión Ascendente)

### 🔷 Concepto Fundamental

> [!success]- ✅ De Específico a General (Siempre Seguro) **Definición:** Convertir una referencia de clase hija a clase padre. Es **implícito** (automático) y **siempre seguro**.
> 
> ```java
> // Jerarquía de clases
> public class Animal {
>     protected String nombre;
>     
>     public Animal(String nombre) {
>         this.nombre = nombre;
>     }
>     
>     public void comer() {
>         System.out.println(nombre + " está comiendo");
>     }
>     
>     public void dormir() {
>         System.out.println(nombre + " está durmiendo");
>     }
> }
> 
> public class Perro extends Animal {
>     private String raza;
>     
>     public Perro(String nombre, String raza) {
>         super(nombre);
>         this.raza = raza;
>     }
>     
>     public void ladrar() {
>         System.out.println(nombre + " dice: ¡Guau guau!");
>     }
>     
>     @Override
>     public void comer() {
>         System.out.println(nombre + " está comiendo croquetas");
>     }
> }
> 
> // ========================
> // UPCASTING EN ACCIÓN
> // ========================
> public class EjemploUpcasting {
>     public static void main(String[] args) {
>         // Crear objeto Perro
>         Perro miPerro = new Perro("Firulais", "Labrador");
>         
>         // ✅ UPCASTING IMPLÍCITO (automático)
>         Animal animal = miPerro;  // Perro → Animal
>         
>         // También se puede escribir explícito (innecesario)
>         Animal animal2 = (Animal) miPerro;
>         
>         System.out.println("=== DESPUÉS DEL UPCASTING ===");
>         
>         // ✅ Puede llamar métodos de Animal
>         animal.comer();    // Ejecuta versión de Perro (polimorfismo)
>         animal.dormir();   // Método de Animal
>         
>         // ❌ NO puede llamar métodos específicos de Perro
>         // animal.ladrar();  // ERROR de compilación
>         // animal.raza;      // ERROR de compilación
>         
>         // El objeto sigue siendo un Perro en memoria
>         System.out.println("\n¿Qué tipo es realmente?");
>         System.out.println("instanceof Perro: " + (animal instanceof Perro));
>         System.out.println("instanceof Animal: " + (animal instanceof Animal));
>     }
> }
> ```
> 
> **Salida:**
> 
> ```
> === DESPUÉS DEL UPCASTING ===
> Firulais está comiendo croquetas
> Firulais está durmiendo
> 
> ¿Qué tipo es realmente?
> instanceof Perro: true
> instanceof Animal: true
> ```

### 📊 ¿Por Qué es Siempre Seguro?

> [!note]- 🛡️ Garantía de Seguridad
> 
> ```java
> public class Vehiculo {
>     public void acelerar() {
>         System.out.println("Vehículo acelerando");
>     }
> }
> 
> public class Auto extends Vehiculo {
>     public void tocarBocina() {
>         System.out.println("¡Beep beep!");
>     }
>     
>     @Override
>     public void acelerar() {
>         System.out.println("Auto acelerando rápido");
>     }
> }
> 
> // ¿Por qué es seguro?
> Auto auto = new Auto();
> 
> // Un Auto SIEMPRE ES UN Vehículo
> Vehiculo vehiculo = auto;  // ✅ Seguro
> 
> // Todo Auto tiene los métodos de Vehículo
> vehiculo.acelerar();  // ✅ Funciona (aunque usa versión de Auto)
> 
> // Pero Vehículo NO tiene todos los métodos de Auto
> // vehiculo.tocarBocina();  // ❌ No disponible desde referencia Vehiculo
> ```
> 
> **Razón:** Un objeto hijo **SIEMPRE tiene** todo lo que tiene el padre (herencia), por lo que es seguro tratarlo como padre.

### 🎯 Casos de Uso de Upcasting

> [!example]- 💼 Situaciones Prácticas
> 
> **1. Arrays polimórficos:**
> 
> ```java
> public class Animal {
>     public void hacerSonido() {
>         System.out.println("Sonido genérico");
>     }
> }
> 
> public class Perro extends Animal {
>     @Override
>     public void hacerSonido() {
>         System.out.println("¡Guau!");
>     }
> }
> 
> public class Gato extends Animal {
>     @Override
>     public void hacerSonido() {
>         System.out.println("¡Miau!");
>     }
> }
> 
> // Array de tipo padre puede contener cualquier hijo
> Animal[] animales = new Animal[3];
> animales[0] = new Perro();    // ✅ Upcasting automático
> animales[1] = new Gato();     // ✅ Upcasting automático
> animales[2] = new Animal();   // ✅ Tipo exacto
> 
> // Tratar a todos como Animal
> for (Animal a : animales) {
>     a.hacerSonido();  // Polimorfismo en acción
> }
> ```
> 
> **2. Parámetros de métodos:**
> 
> ```java
> public class Veterinaria {
>     // Método acepta cualquier Animal (y sus hijos)
>     public void atender(Animal animal) {
>         System.out.println("Atendiendo animal...");
>         animal.comer();
>         animal.dormir();
>     }
>     
>     public double calcularCosto(Animal animal) {
>         double costoBase = 50.0;
>         
>         // instanceof para costos específicos
>         if (animal instanceof Perro) {
>             costoBase += 20.0;  // Baño adicional
>         } else if (animal instanceof Gato) {
>             costoBase += 15.0;  // Cuidado especial
>         }
>         
>         return costoBase;
>     }
> }
> 
> // USO
> Veterinaria vet = new Veterinaria();
> 
> Perro perro = new Perro("Rex", "Bulldog");
> Gato gato = new Gato("Michi", "Persa");
> 
> // Upcasting automático al pasar parámetros
> vet.atender(perro);  // Perro → Animal
> vet.atender(gato);   // Gato → Animal
> 
> System.out.println("Costo perro: $" + vet.calcularCosto(perro));
> System.out.println("Costo gato: $" + vet.calcularCosto(gato));
> ```
> 
> **3. Colecciones heterogéneas:**
> 
> ```java
> import java.util.ArrayList;
> import java.util.List;
> 
> public class GestorAnimales {
>     // Lista que puede contener cualquier tipo de Animal
>     private List<Animal> animales;
>     
>     public GestorAnimales() {
>         animales = new ArrayList<>();
>     }
>     
>     public void agregar(Animal animal) {
>         animales.add(animal);  // Upcasting automático
>         System.out.println("✅ Animal agregado");
>     }
>     
>     public void alimentarTodos() {
>         System.out.println("\n🍖 ALIMENTANDO TODOS LOS ANIMALES");
>         for (Animal a : animales) {
>             a.comer();  // Polimorfismo
>         }
>     }
> }
> 
> // USO
> GestorAnimales gestor = new GestorAnimales();
> gestor.agregar(new Perro("Max", "Pastor"));      // Upcasting
> gestor.agregar(new Gato("Luna", "Siamés"));      // Upcasting
> gestor.agregar(new Pajaro("Piolín", "Canario")); // Upcasting
> gestor.alimentarTodos();
> ```
> 
> **4. Valores de retorno:**
> 
> ```java
> public class FabricaAnimales {
>     // Retorna tipo padre, pero puede ser cualquier hijo
>     public Animal crearAnimal(String tipo) {
>         switch (tipo.toLowerCase()) {
>             case "perro":
>                 return new Perro("Desconocido", "Mestizo");  // ✅ Upcasting
>             case "gato":
>                 return new Gato("Desconocido", "Común");     // ✅ Upcasting
>             case "pajaro":
>                 return new Pajaro("Desconocido", "Común");   // ✅ Upcasting
>             default:
>                 return new Animal("Desconocido");
>         }
>     }
> }
> 
> // USO
> FabricaAnimales fabrica = new FabricaAnimales();
> 
> Animal animal1 = fabrica.crearAnimal("perro");  // Tipo de retorno: Animal
> Animal animal2 = fabrica.crearAnimal("gato");   // Tipo de retorno: Animal
> 
> animal1.comer();  // Ejecuta método de Perro (polimorfismo)
> animal2.comer();  // Ejecuta método de Gato (polimorfismo)
> ```

---

## ⬇️ Downcasting (Conversión Descendente)

### 🔶 Concepto Fundamental

> [!warning]- ⚠️ De General a Específico (Puede Fallar) **Definición:** Convertir una referencia de clase padre a clase hija. Es **explícito** (manual) y **puede fallar** en tiempo de ejecución.
> 
> ```java
> public class Animal {
>     public void comer() {
>         System.out.println("Animal comiendo");
>     }
> }
> 
> public class Perro extends Animal {
>     public void ladrar() {
>         System.out.println("¡Guau guau!");
>     }
>     
>     public void jugar() {
>         System.out.println("Perro jugando");
>     }
> }
> 
> public class Gato extends Animal {
>     public void maullar() {
>         System.out.println("¡Miau!");
>     }
> }
> 
> // ========================
> // DOWNCASTING
> // ========================
> public class EjemploDowncasting {
>     public static void main(String[] args) {
>         // Escenario 1: Downcasting CORRECTO
>         Animal animal1 = new Perro();  // Upcasting primero
>         
>         // El objeto realmente ES un Perro
>         if (animal1 instanceof Perro) {
>             // ✅ DOWNCASTING EXPLÍCITO
>             Perro perro = (Perro) animal1;  // Animal → Perro
>             
>             perro.comer();   // Método heredado
>             perro.ladrar();  // Método específico de Perro
>             perro.jugar();   // Método específico de Perro
>         }
>         
>         System.out.println();
>         
>         // Escenario 2: Downcasting INCORRECTO
>         Animal animal2 = new Gato();  // Upcasting
>         
>         // Intentar hacer downcasting incorrecto
>         try {
>             // ❌ PELIGRO - animal2 NO es un Perro
>             Perro perro2 = (Perro) animal2;  // ClassCastException
>             perro2.ladrar();
>         } catch (ClassCastException e) {
>             System.out.println("❌ Error: No se puede convertir Gato a Perro");
>             System.out.println("   Tipo real: " + animal2.getClass().getName());
>         }
>         
>         // ✅ FORMA SEGURA - Verificar antes
>         if (animal2 instanceof Perro) {
>             Perro perro3 = (Perro) animal2;
>             perro3.ladrar();
>         } else {
>             System.out.println("ℹ️  animal2 no es un Perro");
>         }
>     }
> }
> ```

### 🛡️ Operador instanceof

> [!tip]- 🔍 Verificación Segura de Tipos
> 
> ```java
> public class Animal { }
> public class Perro extends Animal { 
>     public void ladrar() { System.out.println("Guau"); }
> }
> public class Gato extends Animal { 
>     public void maullar() { System.out.println("Miau"); }
> }
> public class Caniche extends Perro {
>     public void hacerTruco() { System.out.println("Dando vueltas"); }
> }
> 
> // ========================
> // USO DE instanceof
> // ========================
> public class TestInstanceof {
>     public static void main(String[] args) {
>         Animal animal1 = new Perro();
>         Animal animal2 = new Gato();
>         Animal animal3 = new Caniche();
>         Animal animal4 = new Animal();
>         
>         // Verificar tipos
>         System.out.println("=== VERIFICACIÓN DE TIPOS ===");
>         
>         // animal1 (Perro)
>         System.out.println("animal1 instanceof Animal: " + 
>                          (animal1 instanceof Animal));   // true
>         System.out.println("animal1 instanceof Perro: " + 
>                          (animal1 instanceof Perro));    // true
>         System.out.println("animal1 instanceof Gato: " + 
>                          (animal1 instanceof Gato));     // false
>         
>         // animal3 (Caniche)
>         System.out.println("\nanimal3 instanceof Animal: " + 
>                          (animal3 instanceof Animal));   // true
>         System.out.println("animal3 instanceof Perro: " + 
>                          (animal3 instanceof Perro));    // true (hereda)
>         System.out.println("animal3 instanceof Caniche: " + 
>                          (animal3 instanceof Caniche));  // true
>         
>         // Uso práctico
>         System.out.println("\n=== USO PRÁCTICO ===");
>         procesarAnimal(animal1);
>         procesarAnimal(animal2);
>         procesarAnimal(animal3);
>         procesarAnimal(animal4);
>     }
>     
>     public static void procesarAnimal(Animal animal) {
>         System.out.println("\n--- Procesando: " + 
>                          animal.getClass().getSimpleName() + " ---");
>         
>         // Verificar y hacer downcasting seguro
>         if (animal instanceof Caniche) {
>             // Más específico primero
>             Caniche caniche = (Caniche) animal;
>             caniche.hacerTruco();
>             caniche.ladrar();
>         } else if (animal instanceof Perro) {
>             Perro perro = (Perro) animal;
>             perro.ladrar();
>         } else if (animal instanceof Gato) {
>             Gato gato = (Gato) animal;
>             gato.maullar();
>         } else {
>             System.out.println("Animal genérico");
>         }
>     }
> }
> ```
> 
> **Reglas de instanceof:**
> 
> - ✅ Retorna `true` si el objeto es del tipo o **subtipo**
> - ✅ Retorna `false` si el objeto NO es compatible
> - ✅ Retorna `false` si la referencia es `null`
> - ⚠️ Verificar tipos **más específicos primero** en if-else

### 🎯 Cuándo Usar Downcasting

> [!example]- 💼 Casos de Uso Legítimos
> 
> **1. Acceder a métodos específicos:**
> 
> ```java
> public class Empleado {
>     protected String nombre;
>     protected double salario;
>     
>     public Empleado(String nombre, double salario) {
>         this.nombre = nombre;
>         this.salario = salario;
>     }
>     
>     public double calcularPago() {
>         return salario;
>     }
> }
> 
> public class Programador extends Empleado {
>     private String lenguaje;
>     private int horasExtra;
>     
>     public Programador(String nombre, double salario, String lenguaje) {
>         super(nombre, salario);
>         this.lenguaje = lenguaje;
>         this.horasExtra = 0;
>     }
>     
>     public void programar() {
>         System.out.println(nombre + " programando en " + lenguaje);
>     }
>     
>     public void registrarHorasExtra(int horas) {
>         this.horasExtra += horas;
>         System.out.println("Horas extra registradas: " + horas);
>     }
>     
>     @Override
>     public double calcularPago() {
>         return salario + (horasExtra * 50);  // $50 por hora extra
>     }
> }
> 
> public class Gerente extends Empleado {
>     private double bono;
>     
>     public Gerente(String nombre, double salario, double bono) {
>         super(nombre, salario);
>         this.bono = bono;
>     }
>     
>     public void dirigirReunion() {
>         System.out.println(nombre + " dirigiendo reunión");
>     }
>     
>     @Override
>     public double calcularPago() {
>         return salario + bono;
>     }
> }
> 
> // Sistema de nómina
> public class SistemaNomina {
>     public void procesarEmpleado(Empleado empleado) {
>         System.out.println("\n--- Procesando: " + empleado.nombre + " ---");
>         
>         // Pago básico (disponible para todos)
>         double pago = empleado.calcularPago();
>         System.out.println("Pago total: $" + pago);
>         
>         // Funcionalidades específicas con downcasting
>         if (empleado instanceof Programador) {
>             Programador prog = (Programador) empleado;
>             prog.programar();
>             
>             // Dar bonificación si trabajó horas extra
>             prog.registrarHorasExtra(5);
>             System.out.println("Nuevo pago: $" + prog.calcularPago());
>             
>         } else if (empleado instanceof Gerente) {
>             Gerente gerente = (Gerente) empleado;
>             gerente.dirigirReunion();
>         }
>     }
> }
> ```
> 
> **2. Deserialización o lectura de datos:**
> 
> ```java
> import java.util.ArrayList;
> import java.util.List;
> 
> public class GestorDatos {
>     private List<Animal> animales;
>     
>     public GestorDatos() {
>         animales = new ArrayList<>();
>     }
>     
>     public void cargarDatos() {
>         // Simulación de carga desde BD o archivo
>         animales.add(new Perro("Rex", "Labrador"));
>         animales.add(new Gato("Michi", "Siamés"));
>         animales.add(new Perro("Max", "Bulldog"));
>         animales.add(new Pajaro("Piolín", "Canario"));
>     }
>     
>     public void generarReporte() {
>         int totalPerros = 0;
>         int totalGatos = 0;
>         int totalPajaros = 0;
>         
>         System.out.println("\n📊 GENERANDO REPORTE DETALLADO");
>         
>         for (Animal a : animales) {
>             System.out.println("\n" + a.getClass().getSimpleName() + ": ");
>             
>             if (a instanceof Perro) {
>                 Perro perro = (Perro) a;
>                 System.out.println("  Raza: " + perro.getRaza());
>                 perro.ladrar();
>                 totalPerros++;
>                 
>             } else if (a instanceof Gato) {
>                 Gato gato = (Gato) a;
>                 System.out.println("  Raza: " + gato.getRaza());
>                 gato.maullar();
>                 totalGatos++;
>                 
>             } else if (a instanceof Pajaro) {
>                 Pajaro pajaro = (Pajaro) a;
>                 System.out.println("  Especie: " + pajaro.getEspecie());
>                 pajaro.volar();
>                 totalPajaros++;
>             }
>         }
>         
>         System.out.println("\n=== RESUMEN ===");
>         System.out.println("Perros: " + totalPerros);
>         System.out.println("Gatos: " + totalGatos);
>         System.out.println("Pájaros: " + totalPajaros);
>     }
> }
> ```
> 
> **3. Patrones de diseño (Visitor):**
> 
> ```java
> interface Forma {
>     void aceptar(VisitanteForma visitante);
> }
> 
> class Circulo implements Forma {
>     private double radio;
>     
>     public Circulo(double radio) {
>         this.radio = radio;
>     }
>     
>     public double getRadio() { return radio; }
>     
>     @Override
>     public void aceptar(VisitanteForma visitante) {
>         visitante.visitar(this);
>     }
> }
> 
> class Rectangulo implements Forma {
>     private double ancho, alto;
>     
>     public Rectangulo(double ancho, double alto) {
>         this.ancho = ancho;
>         this.alto = alto;
>     }
>     
>     public double getAncho() { return ancho; }
>     public double getAlto() { return alto; }
>     
>     @Override
>     public void aceptar(VisitanteForma visitante) {
>         visitante.visitar(this);
>     }
> }
> 
> interface VisitanteForma {
>     void visitar(Circulo circulo);
>     void visitar(Rectangulo rectangulo);
> }
> 
> class CalculadorArea implements VisitanteForma {
>     private double areaTotal = 0;
>     
>     @Override
>     public void visitar(Circulo circulo) {
>         double area = Math.PI * circulo.getRadio() * circulo.getRadio();
>         areaTotal += area;
>         System.out.println("Área círculo: " + area);
>     }
>     
>     @Override
>     public void visitar(Rectangulo rectangulo) {
>         double area = rectangulo.getAncho() * rectangulo.getAlto();
>         areaTotal += area;
>         System.out.println("Área rectángulo: " + area);
>     }
>     
>     public double getAreaTotal() {
>         return areaTotal;
>     }
> }
> ```

---

## 🎯 Ejemplo Completo: Sistema de Vehículos

> [!example]- 🚗 Caso Práctico Integral
> 
> ```java
> // ========================
> // JERARQUÍA DE CLASES
> // ========================
> public abstract class Vehiculo {
>     protected String marca;
>     protected String modelo;
>     protected int año;
>     protected double velocidadActual;
>     
>     public Vehiculo(String marca, String modelo, int año) {
>         this.marca = marca;
>         this.modelo = modelo;
>         this.año = año;
>         this.velocidadActual = 0;
>     }
>     
>     public abstract void acelerar();
>     public abstract void frenar();
>     
>     public void mostrarInfo() {
>         System.out.println(marca + " " + modelo + " (" + año + ")");
>         System.out.println("Velocidad actual: " + velocidadActual + " km/h");
>     }
>     
>     // Getters
>     public String getMarca() { return marca; }
>     public String getModelo() { return modelo; }
>     public int getAño() { return año; }
>     public double getVelocidadActual() { return velocidadActual; }
> }
> 
> public class Auto extends Vehiculo {
>     private int numeroPuertas;
>     private boolean esAutomatico;
>     
>     public Auto(String marca, String modelo, int año, 
>                int numeroPuertas, boolean esAutomatico) {
>         super(marca, modelo, año);
>         this.numeroPuertas = numeroPuertas;
>         this.esAutomatico = esAutomatico;
>     }
>     
>     @Override
>     public void acelerar() {
>         velocidadActual += 20;
>         System.out.println("🚗 Auto acelerando... " + velocidadActual + " km/h");
>     }
>     
>     @Override
>     public void frenar() {
>         velocidadActual = Math.max(0, velocidadActual - 15);
>         System.out.println("🚗 Auto frenando... " + velocidadActual + " km/h");
>     }
>     
>     public void tocarBocina() {
>         System.out.println("¡Beep beep!");
>     }
>     
>     public void activarAireAcondicionado() {
>         System.out.println("❄️  Aire acondicionado activado");
>     }
>     
>     // Getters específicos
>     public int getNumeroPuertas() { return numeroPuertas; }
>     public boolean isAutomatico() { return esAutomatico; }
> }
> 
> public class Moto extends Vehiculo {
>     private int cilindrada;
>     private boolean tieneMaletas;
>     
>     public Moto(String marca, String modelo, int año, int cilindrada) {
>         super(marca, modelo, año);
>         this.cilindrada = cilindrada;
>         this.tieneMaletas = false;
>     }
>     
>     @Override
>     public void acelerar() {
>         velocidadActual += 30;
>         System.out.println("🏍️  Moto acelerando rápido... " + velocidadActual + " km/h");
>     }
>     
>     @Override
>     public void frenar() {
>         velocidadActual = Math.max(0, velocidadActual - 25);
>         System.out.println("🏍️  Moto frenando... " + velocidadActual + " km/h");
>     }
>     
>     public void hacerCaballito() {
>         System.out.println("🤸 ¡Haciendo caballito!");
>     }
>     
>     public void colocarMaletas() {
>         tieneMaletas = true;
>         System.out.println("📦 Maletas colocadas");
>     }
>     
>     // Getters específicos
>     public int getCilindrada() { return cilindrada; }
>     public boolean isTieneMaletas() { return tieneMaletas; }
> }
> 
> public class Camion extends Vehiculo {
>     private double capacidadCarga;
>     private double cargaActual;
>     
>     public Camion(String marca, String modelo, int año, double capacidadCarga) {
>         super(marca, modelo, año);
>         this.capacidadCarga = capacidadCarga;
>         this.cargaActual = 0;
>     }
>     
>     @Override
>     public void acelerar() {
>         velocidadActual += 10;
>         System.out.println("🚚 Camión acelerando lento... " + velocidadActual + " km/h");
>     }
>     
>     @Override
>     public void frenar() {
>         velocidadActual = Math.max(0, velocidadActual - 8);
>         System.out.println("🚚 Camión frenando... " + velocidadActual + " km/h");
>     }
>     
>     public void cargar(double peso) {
>         if (cargaActual + peso <= capacidadCarga) {
>             cargaActual += peso;
>             System.out.println("📦 Cargado: " - peso + " kg. Total: " + cargaActual + " kg");
>     } else {
>         System.out.println("❌ Excede capacidad máxima");
>     }
> }
> 
> public void descargar() {
>     System.out.println("📤 Descargando " + cargaActual + " kg");
>     cargaActual = 0;
> }
> 
> // Getters específicos
> public double getCapacidadCarga() { return capacidadCarga; }
> public double getCargaActual() { return cargaActual; }
> ```
> 
> }
> 
> // ======================== // GESTOR DE VEHÍCULOS // ======================== public class GestorVehiculos { private Vehiculo[] flota; private int cantidad;
> 
> ```
> public GestorVehiculos(int capacidad) {
>     flota = new Vehiculo[capacidad];
>     cantidad = 0;
> }
> 
> // ✅ UPCASTING - Acepta cualquier tipo de vehículo
> public void agregarVehiculo(Vehiculo vehiculo) {
>     if (cantidad < flota.length) {
>         flota[cantidad] = vehiculo;  // Upcasting implícito
>         cantidad++;
>         System.out.println("✅ Vehículo agregado: " + 
>                          vehiculo.getMarca() + " " + vehiculo.getModelo());
>     } else {
>         System.out.println("❌ Flota llena");
>     }
> }
> 
> // Operación polimórfica - sin downcasting
> public void acelerarTodos() {
>     System.out.println("\n🚀 ACELERANDO TODA LA FLOTA");
>     for (int i = 0; i < cantidad; i++) {
>         flota[i].acelerar();  // Polimorfismo
>     }
> }
> 
> // ⬇️ DOWNCASTING - Acceder a características específicas
> public void realizarMantenimientoEspecifico() {
>     System.out.println("\n🔧 MANTENIMIENTO ESPECÍFICO");
>     
>     for (int i = 0; i < cantidad; i++) {
>         Vehiculo v = flota[i];
>         
>         System.out.println("\n--- " + v.getMarca() + " " + v.getModelo() + " ---");
>         
>         // Verificar tipo y hacer downcasting seguro
>         if (v instanceof Auto) {
>             Auto auto = (Auto) v;  // ⬇️ Downcasting
>             System.out.println("Tipo: Auto");
>             System.out.println("Puertas: " + auto.getNumeroPuertas());
>             System.out.println("Transmisión: " + 
>                              (auto.isAutomatico() ? "Automática" : "Manual"));
>             auto.activarAireAcondicionado();
>             
>         } else if (v instanceof Moto) {
>             Moto moto = (Moto) v;  // ⬇️ Downcasting
>             System.out.println("Tipo: Moto");
>             System.out.println("Cilindrada: " + moto.getCilindrada() + " cc");
>             System.out.println("Cambiar aceite de motor");
>             
>         } else if (v instanceof Camion) {
>             Camion camion = (Camion) v;  // ⬇️ Downcasting
>             System.out.println("Tipo: Camión");
>             System.out.println("Capacidad: " + camion.getCapacidadCarga() + " kg");
>             System.out.println("Revisar sistema de frenos pesados");
>         }
>     }
> }
> 
> // Filtrar por tipo específico
> public void listarPorTipo(Class<?> tipo) {
>     System.out.println("\n📋 LISTANDO: " + tipo.getSimpleName());
>     boolean encontrado = false;
>     
>     for (int i = 0; i < cantidad; i++) {
>         if (tipo.isInstance(flota[i])) {
>             flota[i].mostrarInfo();
>             System.out.println();
>             encontrado = true;
>         }
>     }
>     
>     if (!encontrado) {
>         System.out.println("No hay vehículos de este tipo");
>     }
> }
> 
> // Operaciones específicas por tipo
> public void probarCaracteristicasEspeciales() {
>     System.out.println("\n✨ PROBANDO CARACTERÍSTICAS ESPECIALES");
>     
>     for (int i = 0; i < cantidad; i++) {
>         Vehiculo v = flota[i];
>         
>         System.out.println("\n" + v.getMarca() + " " + v.getModelo() + ":");
>         
>         // ⬇️ DOWNCASTING para acceder a métodos específicos
>         if (v instanceof Auto) {
>             Auto auto = (Auto) v;
>             auto.tocarBocina();
>             
>         } else if (v instanceof Moto) {
>             Moto moto = (Moto) v;
>             moto.hacerCaballito();
>             
>         } else if (v instanceof Camion) {
>             Camion camion = (Camion) v;
>             camion.cargar(500);
>             camion.descargar();
>         }
>     }
> }
> 
> // Estadísticas detalladas
> public void generarEstadisticas() {
>     System.out.println("\n📊 ESTADÍSTICAS DE LA FLOTA");
>     System.out.println("Total de vehículos: " + cantidad);
>     
>     int autos = 0, motos = 0, camiones = 0;
>     double velocidadPromedio = 0;
>     
>     for (int i = 0; i < cantidad; i++) {
>         Vehiculo v = flota[i];
>         velocidadPromedio += v.getVelocidadActual();
>         
>         if (v instanceof Auto) {
>             autos++;
>         } else if (v instanceof Moto) {
>             motos++;
>         } else if (v instanceof Camion) {
>             camiones++;
>         }
>     }
>     
>     velocidadPromedio /= cantidad;
>     
>     System.out.println("\nDistribución:");
>     System.out.println("  🚗 Autos: " + autos);
>     System.out.println("  🏍️  Motos: " + motos);
>     System.out.println("  🚚 Camiones: " + camiones);
>     System.out.printf("\nVelocidad promedio: %.2f km/h\n", velocidadPromedio);
> }
> 
> // Método que demuestra casting incorrecto
> public void ejemploCastingIncorrecto() {
>     System.out.println("\n⚠️  DEMOSTRANDO CASTING INCORRECTO");
>     
>     if (cantidad > 0) {
>         Vehiculo v = flota[0];
>         System.out.println("Primer vehículo: " + v.getClass().getSimpleName());
>         
>         // Intentar downcasting sin verificar
>         try {
>             Camion camion = (Camion) v;  // Puede fallar
>             camion.cargar(100);
>         } catch (ClassCastException e) {
>             System.out.println("❌ Error: El vehículo no es un Camión");
>             System.out.println("   Tipo real: " + v.getClass().getSimpleName());
>         }
>     }
> }
> ```
> 
> }
> 
> // ======================== // PROGRAMA PRINCIPAL // ======================== public class SistemaVehiculos { public static void main(String[] args) { System.out.println("╔════════════════════════════════════════╗"); System.out.println("║ SISTEMA DE GESTIÓN DE VEHÍCULOS ║"); System.out.println("╚════════════════════════════════════════╝\n");
> 
> ```
>     GestorVehiculos gestor = new GestorVehiculos(10);
>     
>     // Crear vehículos
>     Auto auto1 = new Auto("Toyota", "Corolla", 2023, 4, true);
>     Auto auto2 = new Auto("Honda", "Civic", 2022, 4, false);
>     Moto moto1 = new Moto("Yamaha", "R6", 2023, 600);
>     Moto moto2 = new Moto("Harley", "Sportster", 2021, 1200);
>     Camion camion1 = new Camion("Mercedes", "Actros", 2023, 20000);
>     
>     // ✅ UPCASTING IMPLÍCITO al agregar
>     System.out.println("=== AGREGANDO VEHÍCULOS ===");
>     gestor.agregarVehiculo(auto1);      // Auto → Vehiculo
>     gestor.agregarVehiculo(auto2);      // Auto → Vehiculo
>     gestor.agregarVehiculo(moto1);      // Moto → Vehiculo
>     gestor.agregarVehiculo(moto2);      // Moto → Vehiculo
>     gestor.agregarVehiculo(camion1);    // Camion → Vehiculo
>     
>     // Operación polimórfica (sin downcasting)
>     gestor.acelerarTodos();
>     
>     // ⬇️ DOWNCASTING para operaciones específicas
>     gestor.realizarMantenimientoEspecifico();
>     
>     // Probar características especiales
>     gestor.probarCaracteristicasEspeciales();
>     
>     // Listar por tipo
>     gestor.listarPorTipo(Auto.class);
>     gestor.listarPorTipo(Moto.class);
>     
>     // Estadísticas
>     gestor.generarEstadisticas();
>     
>     // Demostrar casting incorrecto
>     gestor.ejemploCastingIncorrecto();
>     
>     // ========================
>     // EJEMPLOS ADICIONALES
>     // ========================
>     System.out.println("\n╔════════════════════════════════════════╗");
>     System.out.println("║     EJEMPLOS DE CASTING DIRECTO       ║");
>     System.out.println("╚════════════════════════════════════════╝\n");
>     
>     // Ejemplo 1: Upcasting y polimorfismo
>     System.out.println("=== EJEMPLO 1: Polimorfismo ===");
>     Vehiculo vehiculo = new Moto("Suzuki", "GSX", 2023, 750);
>     vehiculo.acelerar();  // Ejecuta método de Moto
>     vehiculo.mostrarInfo();
>     
>     // Ejemplo 2: Downcasting seguro
>     System.out.println("\n=== EJEMPLO 2: Downcasting seguro ===");
>     if (vehiculo instanceof Moto) {
>         Moto moto = (Moto) vehiculo;
>         moto.hacerCaballito();  // Ahora puede acceder a métodos de Moto
>         moto.colocarMaletas();
>     }
>     
>     // Ejemplo 3: Array polimórfico
>     System.out.println("\n=== EJEMPLO 3: Array polimórfico ===");
>     Vehiculo[] vehiculos = {
>         new Auto("Ford", "Focus", 2023, 4, true),
>         new Moto("Kawasaki", "Ninja", 2023, 650),
>         new Camion("Volvo", "FH16", 2023, 25000)
>     };
>     
>     for (Vehiculo v : vehiculos) {
>         v.acelerar();  // Polimorfismo
>         
>         // Downcasting condicional
>         if (v instanceof Camion) {
>             Camion c = (Camion) v;
>             c.cargar(1000);
>         }
>     }
>     
>     System.out.println("\n✅ Sistema ejecutado exitosamente");
> }
> ```
> 
> }

---

## ⚠️ Errores Comunes y Buenas Prácticas

> [!warning]- 🚫 Problemas Frecuentes
> 
> **1. Downcasting sin verificar:**
> 
> ```java
> // ❌ PELIGROSO - Puede fallar
> public void procesarAnimal(Animal animal) {
>     Perro perro = (Perro) animal;  // Sin verificar
>     perro.ladrar();  // ClassCastException si no es Perro
> }
> 
> // ✅ CORRECTO - Siempre verificar
> public void procesarAnimal(Animal animal) {
>     if (animal instanceof Perro) {
>         Perro perro = (Perro) animal;
>         perro.ladrar();
>     }
> }
> ```
> 
> **2. Usar instanceof excesivamente (Code Smell):**
> 
> ```java
> // ❌ MAL DISEÑO - Demasiados instanceof
> public double calcularCosto(Animal animal) {
>     if (animal instanceof Perro) {
>         return 50.0;
>     } else if (animal instanceof Gato) {
>         return 40.0;
>     } else if (animal instanceof Pajaro) {
>         return 30.0;
>     }
>     return 0;
> }
> 
> // ✅ MEJOR - Usar polimorfismo
> abstract class Animal {
>     public abstract double calcularCosto();
> }
> 
> class Perro extends Animal {
>     @Override
>     public double calcularCosto() {
>         return 50.0;
>     }
> }
> ```
> 
> **3. Orden incorrecto de instanceof:**
> 
> ```java
> public class Animal { }
> public class Perro extends Animal { }
> public class Caniche extends Perro { }
> 
> // ❌ ORDEN INCORRECTO
> public void procesar(Animal animal) {
>     if (animal instanceof Perro) {
>         // Caniche entra aquí primero
>         System.out.println("Es un Perro");
>     } else if (animal instanceof Caniche) {
>         // Nunca se ejecuta para Caniche
>         System.out.println("Es un Caniche");
>     }
> }
> 
> // ✅ ORDEN CORRECTO - Más específico primero
> public void procesar(Animal animal) {
>     if (animal instanceof Caniche) {
>         System.out.println("Es un Caniche");
>     } else if (animal instanceof Perro) {
>         System.out.println("Es un Perro");
>     }
> }
> ```
> 
> **4. Casting cuando no es necesario:**
> 
> ```java
> // ❌ INNECESARIO
> Perro perro = new Perro();
> Animal animal = (Animal) perro;  // Cast explícito innecesario
> 
> // ✅ MEJOR
> Perro perro = new Perro();
> Animal animal = perro;  // Upcasting implícito
> ```
> 
> **5. Null pointer con instanceof:**
> 
> ```java
> Animal animal = null;
> 
> // instanceof retorna false para null (no lanza excepción)
> if (animal instanceof Perro) {
>     // No entra aquí
> }
> 
> // ✅ Verificar null si es necesario
> if (animal != null && animal instanceof Perro) {
>     Perro perro = (Perro) animal;
> }
> ```

---

## 💡 Alternativas al Downcasting

> [!tip]- 🎯 Soluciones Más Elegantes
> 
> **1. Patrón Visitor:**
> 
> ```java
> interface AnimalVisitor {
>     void visitar(Perro perro);
>     void visitar(Gato gato);
> }
> 
> abstract class Animal {
>     public abstract void aceptar(AnimalVisitor visitor);
> }
> 
> class Perro extends Animal {
>     @Override
>     public void aceptar(AnimalVisitor visitor) {
>         visitor.visitar(this);  // Sin downcasting
>     }
> }
> 
> class Gato extends Animal {
>     @Override
>     public void aceptar(AnimalVisitor visitor) {
>         visitor.visitar(this);  // Sin downcasting
>     }
> }
> 
> class VeterinarioVisitor implements AnimalVisitor {
>     @Override
>     public void visitar(Perro perro) {
>         System.out.println("Atendiendo perro");
>     }
>     
>     @Override
>     public void visitar(Gato gato) {
>         System.out.println("Atendiendo gato");
>     }
> }
> ```
> 
> **2. Double Dispatch:**
> 
> ```java
> abstract class Animal {
>     public abstract void interactuar(Animal otro);
>     protected abstract void interactuarConPerro(Perro perro);
>     protected abstract void interactuarConGato(Gato gato);
> }
> 
> class Perro extends Animal {
>     @Override
>     public void interactuar(Animal otro) {
>         otro.interactuarConPerro(this);
>     }
>     
>     @Override
>     protected void interactuarConPerro(Perro perro) {
>         System.out.println("Dos perros jugando");
>     }
>     
>     @Override
>     protected void interactuarConGato(Gato gato) {
>         System.out.println("Perro persiguiendo gato");
>     }
> }
> ```
> 
> **3. Métodos abstractos específicos:**
> 
> ```java
> abstract class Vehiculo {
>     // En lugar de downcasting, definir métodos abstractos
>     public abstract String getTipoVehiculo();
>     public abstract void realizarMantenimiento();
> }
> 
> class Auto extends Vehiculo {
>     @Override
>     public String getTipoVehiculo() {
>         return "Auto";
>     }
>     
>     @Override
>     public void realizarMantenimiento() {
>         System.out.println("Mantenimiento de auto");
>     }
> }
> ```

---

## 📊 Tabla Comparativa

> [!info]- 📋 Resumen Visual
> 
> |Aspecto|Upcasting ⬆️|Downcasting ⬇️|
> |---|---|---|
> |**Dirección**|Hijo → Padre|Padre → Hijo|
> |**Sintaxis**|Implícita|Explícita `(Tipo)`|
> |**Seguridad**|100% seguro|Puede fallar|
> |**Cuándo falla**|Nunca|Si tipo real no coincide|
> |**Verificación**|No necesaria|`instanceof` recomendado|
> |**Acceso métodos**|Solo métodos del padre|Todos los métodos del hijo|
> |**Uso común**|Polimorfismo|Acceso a características específicas|
> |**Excepción**|Ninguna|`ClassCastException`|
> 
> **Ejemplo visual:**
> 
> ```
>      Animal (padre)
>         ↑ ⬆️ Upcasting (seguro)
>         |
>         |
>         ↓ ⬇️ Downcasting (verificar)
>      Perro (hijo)
> ```

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica
> 
> **Nivel Básico:**
> 
> 1. Crear jerarquía `Instrumento → Guitarra, Piano, Bateria`
>     - Practicar upcasting con arrays
>     - Usar instanceof para identificar tipos
> 2. Sistema de `Empleado → Gerente, Vendedor, Tecnico`
>     - Downcasting seguro para acceder a bonos específicos
>     - Generar reporte por tipo
> 
> **Nivel Intermedio:** 3. Sistema de `Producto → Electronico, Ropa, Alimento`
> 
> - Array polimórfico de productos
>     
> - Calcular descuentos específicos con downcasting
>     
> - Implementar filtros por categoría
>     
> 
> 4. Gestor de `Figura → Circulo, Rectangulo, Triangulo`
>     - Operaciones polimórficas (calcularArea)
>     - Downcasting para obtener propiedades específicas
>     - Comparar por área usando instanceof
> 
> **Nivel Avanzado:** 5. Sistema bancario con `Cuenta → CuentaAhorro, CuentaCorriente`
> 
> - Implementar transacciones polimórficas
>     
> - Downcasting para operaciones específicas
>     
> - Evitar instanceof usando polimorfismo
>     
> 
> 6. Simulador de zoológico
>     - Jerarquía compleja de animales
>     - Implementar Visitor pattern
>     - Comparar solución con/sin downcasting

---

## 📚 Resumen Ejecutivo

> [!quote]- 🌟 Puntos Clave **Has aprendido:**
> 
> - ✅ **Upcasting:** Hijo → Padre (implícito, siempre seguro)
> - ✅ **Downcasting:** Padre → Hijo (explícito, puede fallar)
> - ✅ **instanceof:** Verificar tipos antes de cast
> - ✅ Diferencia entre tipo de referencia y tipo real
> - ✅ Cuándo usar cada tipo de casting
> - ✅ Errores comunes y cómo evitarlos
> - ✅ Alternativas al downcasting excesivo
> 
> **Reglas de oro:**
> 
> - 🎯 Upcasting es automático y seguro
> - 🎯 Downcasting SIEMPRE verificar con instanceof
> - 🎯 Preferir polimorfismo sobre instanceof
> - 🎯 Downcasting excesivo = mal diseño
> - 🎯 Verificar tipos más específicos primero
> 
> **Cuándo usar:**
> 
> - ✅ Upcasting: Para polimorfismo y colecciones heterogéneas
> - ✅ Downcasting: Solo cuando necesitas acceso a métodos específicos
> - ⚠️ Evitar: instanceof en cadenas largas de if-else
> 
> **Próximos temas:**
> 
> - **[[08 - Excepciones]]** - Try-catch con jerarquías
> - **[[09 - Genéricos]]** - Type safety sin casting

---

**Tags:** #java #poo #casting #upcasting #downcasting #instanceof #polimorfismo #type-checking #class-cast-exception #herencia