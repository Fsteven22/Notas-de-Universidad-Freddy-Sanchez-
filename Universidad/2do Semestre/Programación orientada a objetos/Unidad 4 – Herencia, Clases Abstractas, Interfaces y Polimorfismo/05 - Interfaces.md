# 🔌 Interfaces en Java

## 🎯 Introducción

> [!info]- 💡 ¿Qué es una Interface? Una **interface** es un contrato puro que define QUÉ debe hacer una clase, sin especificar CÓMO lo hace. Es una colección de métodos abstractos y constantes que las clases deben implementar.
> 
> **Analogía:** Como un enchufe eléctrico estándar
> 
> - **Interface (enchufe):** Define el contrato - forma, voltaje, conexiones
> - **Implementación (aparato):** Cada dispositivo lo usa diferente (TV, lámpara, cargador)
> - **Compatibilidad:** Si cumple el contrato, funciona sin importar el aparato
> 
> **Características principales:**
> 
> - **Contrato puro:** Solo define firmas de métodos
> - **Herencia múltiple:** Una clase puede implementar varias interfaces
> - **100% abstracto:** Todos los métodos son abstractos (por defecto)
> - **Sin estado:** Solo constantes (`public static final`)
> - **Polimorfismo:** Referencia común para diferentes implementaciones

---

## 📝 Sintaxis Básica

### 🔷 Declaración de Interface

> [!example]- 📋 Estructura Fundamental
> 
> ```java
> // Declaración con 'interface'
> public interface Volador {
>     // Constantes (public static final - automático)
>     double VELOCIDAD_MAXIMA = 1000.0;
>     int ALTURA_MAXIMA = 10000;
>     
>     // Métodos abstractos (public abstract - automático)
>     void volar();
>     void aterrizar();
>     void despegar();
>     
>     // Desde Java 8: Métodos default (con implementación)
>     default void mostrarInfo() {
>         System.out.println("Soy un objeto volador");
>     }
>     
>     // Desde Java 8: Métodos static
>     static void mostrarLimites() {
>         System.out.println("Velocidad máx: " + VELOCIDAD_MAXIMA);
>         System.out.println("Altura máx: " + ALTURA_MAXIMA);
>     }
> }
> ```
> 
> **Reglas importantes:**
> 
> - Todos los métodos son `public abstract` por defecto
> - Todas las variables son `public static final` por defecto
> - No puede tener constructores
> - No puede tener atributos de instancia
> - No puede tener métodos private (excepto desde Java 9 para helpers)

### 🔶 Implementación de Interface

> [!success]- ✅ Clases que Implementan
> 
> ```java
> // Una clase implementa UNA interface
> public class Avion implements Volador {
>     private String modelo;
>     private double velocidadActual;
>     
>     public Avion(String modelo) {
>         this.modelo = modelo;
>         this.velocidadActual = 0;
>     }
>     
>     // ✅ OBLIGATORIO: Implementar TODOS los métodos abstractos
>     @Override
>     public void volar() {
>         System.out.println(modelo + " está volando a " + 
>                          velocidadActual + " km/h");
>     }
>     
>     @Override
>     public void aterrizar() {
>         velocidadActual = 0;
>         System.out.println(modelo + " ha aterizado");
>     }
>     
>     @Override
>     public void despegar() {
>         velocidadActual = 200;
>         System.out.println(modelo + " ha despegado");
>     }
> }
> 
> // Una clase implementa MÚLTIPLES interfaces
> public class Pato implements Volador, Nadador, Caminante {
>     @Override
>     public void volar() {
>         System.out.println("Pato volando bajo");
>     }
>     
>     @Override
>     public void aterrizar() {
>         System.out.println("Pato aterrizando en el agua");
>     }
>     
>     @Override
>     public void despegar() {
>         System.out.println("Pato despegando del agua");
>     }
>     
>     @Override
>     public void nadar() {
>         System.out.println("Pato nadando");
>     }
>     
>     @Override
>     public void caminar() {
>         System.out.println("Pato caminando");
>     }
> }
> ```

---

## 🎯 Ejemplo Completo: Sistema de Pagos

> [!example]- 💳 Caso Práctico con Múltiples Implementaciones
> 
> ```java
> // ========================
> // INTERFACE PRINCIPAL
> // ========================
> public interface MetodoPago {
>     // Constantes
>     double COMISION_MINIMA = 0.50;
>     double COMISION_MAXIMA = 100.0;
>     
>     // Métodos abstractos
>     boolean procesarPago(double monto);
>     boolean validarPago(double monto);
>     double calcularComision(double monto);
>     String obtenerDetalles();
>     
>     // Método default (común para todos)
>     default void mostrarResumen(double monto) {
>         System.out.println("\n--- RESUMEN DE PAGO ---");
>         System.out.println("Método: " + obtenerDetalles());
>         System.out.println("Monto: $" + monto);
>         System.out.println("Comisión: $" + calcularComision(monto));
>         System.out.println("Total: $" + (monto + calcularComision(monto)));
>     }
>     
>     // Método static (utilidad)
>     static boolean montoValido(double monto) {
>         return monto > 0 && monto <= 100000;
>     }
> }
> 
> // ========================
> // IMPLEMENTACIONES
> // ========================
> public class TarjetaCredito implements MetodoPago {
>     private String numeroTarjeta;
>     private String titular;
>     private String fechaExpiracion;
>     private String cvv;
>     
>     public TarjetaCredito(String numeroTarjeta, String titular,
>                          String fechaExpiracion, String cvv) {
>         this.numeroTarjeta = numeroTarjeta;
>         this.titular = titular;
>         this.fechaExpiracion = fechaExpiracion;
>         this.cvv = cvv;
>     }
>     
>     @Override
>     public boolean procesarPago(double monto) {
>         if (!validarPago(monto)) {
>             return false;
>         }
>         
>         System.out.println("💳 Procesando pago con tarjeta...");
>         // Simulación de procesamiento
>         System.out.println("✅ Pago aprobado");
>         return true;
>     }
>     
>     @Override
>     public boolean validarPago(double monto) {
>         if (!MetodoPago.montoValido(monto)) {
>             System.out.println("❌ Monto inválido");
>             return false;
>         }
>         
>         if (!validarTarjeta()) {
>             System.out.println("❌ Tarjeta inválida");
>             return false;
>         }
>         
>         return true;
>     }
>     
>     @Override
>     public double calcularComision(double monto) {
>         double comision = monto * 0.03;  // 3%
>         return Math.max(COMISION_MINIMA, 
>                        Math.min(comision, COMISION_MAXIMA));
>     }
>     
>     @Override
>     public String obtenerDetalles() {
>         String ultimos4 = numeroTarjeta.substring(
>             numeroTarjeta.length() - 4
>         );
>         return "Tarjeta de Crédito **** " + ultimos4;
>     }
>     
>     private boolean validarTarjeta() {
>         // Validación básica
>         return numeroTarjeta != null && 
>                numeroTarjeta.length() == 16 &&
>                cvv != null && cvv.length() == 3;
>     }
> }
> 
> public class PayPal implements MetodoPago {
>     private String email;
>     private String password;
>     
>     public PayPal(String email, String password) {
>         this.email = email;
>         this.password = password;
>     }
>     
>     @Override
>     public boolean procesarPago(double monto) {
>         if (!validarPago(monto)) {
>             return false;
>         }
>         
>         System.out.println("💙 Procesando pago con PayPal...");
>         System.out.println("✅ Pago aprobado");
>         return true;
>     }
>     
>     @Override
>     public boolean validarPago(double monto) {
>         if (!MetodoPago.montoValido(monto)) {
>             System.out.println("❌ Monto inválido");
>             return false;
>         }
>         
>         if (!email.contains("@")) {
>             System.out.println("❌ Email inválido");
>             return false;
>         }
>         
>         return true;
>     }
>     
>     @Override
>     public double calcularComision(double monto) {
>         // PayPal cobra 2.9% + $0.30
>         return (monto * 0.029) + 0.30;
>     }
>     
>     @Override
>     public String obtenerDetalles() {
>         return "PayPal (" + email + ")";
>     }
> }
> 
> public class TransferenciaBancaria implements MetodoPago {
>     private String numeroCuenta;
>     private String banco;
>     
>     public TransferenciaBancaria(String numeroCuenta, String banco) {
>         this.numeroCuenta = numeroCuenta;
>         this.banco = banco;
>     }
>     
>     @Override
>     public boolean procesarPago(double monto) {
>         if (!validarPago(monto)) {
>             return false;
>         }
>         
>         System.out.println("🏦 Procesando transferencia bancaria...");
>         System.out.println("⏳ Procesamiento puede tardar 24-48 horas");
>         System.out.println("✅ Transferencia iniciada");
>         return true;
>     }
>     
>     @Override
>     public boolean validarPago(double monto) {
>         if (!MetodoPago.montoValido(monto)) {
>             System.out.println("❌ Monto inválido");
>             return false;
>         }
>         
>         if (numeroCuenta.length() != 20) {
>             System.out.println("❌ Número de cuenta inválido");
>             return false;
>         }
>         
>         return true;
>     }
>     
>     @Override
>     public double calcularComision(double monto) {
>         // Comisión fija
>         return monto > 1000 ? 5.0 : 2.0;
>     }
>     
>     @Override
>     public String obtenerDetalles() {
>         return "Transferencia - " + banco + " ****" + 
>                numeroCuenta.substring(numeroCuenta.length() - 4);
>     }
> }
> 
> public class Efectivo implements MetodoPago {
>     private double montoRecibido;
>     
>     @Override
>     public boolean procesarPago(double monto) {
>         if (!validarPago(monto)) {
>             return false;
>         }
>         
>         System.out.println("💵 Procesando pago en efectivo...");
>         
>         if (montoRecibido >= monto) {
>             double cambio = montoRecibido - monto;
>             System.out.println("✅ Pago recibido");
>             if (cambio > 0) {
>                 System.out.println("💰 Cambio: $" + cambio);
>             }
>             return true;
>         } else {
>             System.out.println("❌ Efectivo insuficiente");
>             return false;
>         }
>     }
>     
>     @Override
>     public boolean validarPago(double monto) {
>         return MetodoPago.montoValido(monto);
>     }
>     
>     @Override
>     public double calcularComision(double monto) {
>         return 0.0;  // Sin comisión en efectivo
>     }
>     
>     @Override
>     public String obtenerDetalles() {
>         return "Efectivo";
>     }
>     
>     public void setMontoRecibido(double monto) {
>         this.montoRecibido = monto;
>     }
> }
> 
> // ========================
> // PROCESADOR DE PAGOS
> // ========================
> public class ProcesadorPagos {
>     // Polimorfismo - acepta cualquier método de pago
>     public boolean realizarPago(MetodoPago metodoPago, double monto) {
>         System.out.println("\n╔═══════════════════════════════╗");
>         System.out.println("║   PROCESANDO PAGO             ║");
>         System.out.println("╚═══════════════════════════════╝");
>         
>         boolean exito = metodoPago.procesarPago(monto);
>         
>         if (exito) {
>             metodoPago.mostrarResumen(monto);
>         }
>         
>         return exito;
>     }
>     
>     public void compararComisiones(double monto) {
>         System.out.println("\n=== COMPARACIÓN DE COMISIONES ===");
>         System.out.println("Monto: $" + monto);
>         
>         MetodoPago[] metodos = {
>             new TarjetaCredito("1234567890123456", "Juan", "12/25", "123"),
>             new PayPal("user@email.com", "pass"),
>             new TransferenciaBancaria("12345678901234567890", "Banco XYZ"),
>             new Efectivo()
>         };
>         
>         for (MetodoPago metodo : metodos) {
>             double comision = metodo.calcularComision(monto);
>             double total = monto + comision;
>             System.out.printf("%s: $%.2f (Total: $%.2f)\n",
>                 metodo.obtenerDetalles(), comision, total);
>         }
>     }
> }
> 
> // ========================
> // PROGRAMA PRINCIPAL
> // ========================
> public class SistemaPagos {
>     public static void main(String[] args) {
>         ProcesadorPagos procesador = new ProcesadorPagos();
>         
>         // Diferentes métodos de pago - mismo procesador
>         MetodoPago tarjeta = new TarjetaCredito(
>             "4532123456789012", 
>             "María García",
>             "08/26",
>             "321"
>         );
>         
>         MetodoPago paypal = new PayPal(
>             "maria@email.com",
>             "password123"
>         );
>         
>         MetodoPago transferencia = new TransferenciaBancaria(
>             "12345678901234567890",
>             "Banco Nacional"
>         );
>         
>         Efectivo efectivo = new Efectivo();
>         efectivo.setMontoRecibido(150);
>         
>         // Procesar con diferentes métodos
>         double monto = 100.0;
>         
>         procesador.realizarPago(tarjeta, monto);
>         procesador.realizarPago(paypal, monto);
>         procesador.realizarPago(transferencia, monto);
>         procesador.realizarPago(efectivo, monto);
>         
>         // Comparar comisiones
>         procesador.compararComisiones(500);
>         
>         // Usar método static de la interface
>         System.out.println("\n¿Monto válido? " + 
>             MetodoPago.montoValido(50000));
>     }
> }
> ```

---

## 🔄 Herencia Múltiple con Interfaces

> [!tip]- 🎭 Múltiples Capacidades
> 
> ```java
> // Múltiples interfaces
> interface Volador {
>     void volar();
>     void aterrizar();
> }
> 
> interface Nadador {
>     void nadar();
>     void sumergirse();
> }
> 
> interface Caminante {
>     void caminar();
>     void correr();
> }
> 
> // Clase que implementa TRES interfaces
> public class SuperHeroe implements Volador, Nadador, Caminante {
>     private String nombre;
>     
>     public SuperHeroe(String nombre) {
>         this.nombre = nombre;
>     }
>     
>     // Implementar TODOS los métodos de TODAS las interfaces
>     @Override
>     public void volar() {
>         System.out.println(nombre + " está volando 🦸");
>     }
>     
>     @Override
>     public void aterrizar() {
>         System.out.println(nombre + " ha aterrizado");
>     }
>     
>     @Override
>     public void nadar() {
>         System.out.println(nombre + " está nadando 🏊");
>     }
>     
>     @Override
>     public void sumergirse() {
>         System.out.println(nombre + " se ha sumergido");
>     }
>     
>     @Override
>     public void caminar() {
>         System.out.println(nombre + " está caminando 🚶");
>     }
>     
>     @Override
>     public void correr() {
>         System.out.println(nombre + " está corriendo 🏃");
>     }
> }
> 
> // USO con polimorfismo
> SuperHeroe superman = new SuperHeroe("Superman");
> 
> // Puede ser tratado como cualquiera de sus interfaces
> Volador v = superman;
> v.volar();
> 
> Nadador n = superman;
> n.nadar();
> 
> Caminante c = superman;
> c.caminar();
> ```

---

## 🆚 Interface vs Clase Abstracta

> [!info]- 📊 Diferencias Detalladas
> 
> |Característica|Interface|Clase Abstracta|
> |---|---|---|
> |**Herencia**|Múltiple (`implements`)|Simple (`extends`)|
> |**Métodos**|Todos abstractos (excepto default/static)|Abstractos + concretos|
> |**Atributos**|Solo constantes|Cualquier tipo|
> |**Constructores**|❌ No|✅ Sí|
> |**Estado**|❌ No tiene|✅ Sí tiene|
> |**Modificadores**|Solo `public`|Todos|
> |**Relación**|"PUEDE-HACER"|"ES-UN"|
> 
> **Ejemplo comparativo:**
> 
> ```java
> // INTERFACE - Define capacidad
> interface Dibujable {
>     void dibujar();  // QUÉ hacer
> }
> 
> // CLASE ABSTRACTA - Define jerarquía
> abstract class Figura {
>     protected String color;  // Estado compartido
>     
>     public Figura(String color) {  // Constructor
>         this.color = color;
>     }
>     
>     public abstract double calcularArea();  // QUÉ hacer
>     
>     public void mostrarColor() {  // CÓMO hacerlo
>         System.out.println("Color: " + color);
>     }
> }
> 
> // Clase que hereda Y implementa
> class Circulo extends Figura implements Dibujable {
>     private double radio;
>     
>     public Circulo(String color, double radio) {
>         super(color);
>         this.radio = radio;
>     }
>     
>     @Override
>     public double calcularArea() {
>         return Math.PI * radio * radio;
>     }
>     
>     @Override
>     public void dibujar() {
>         System.out.println("Dibujando círculo");
>     }
> }
> ```

---

## 🎨 Interfaces Funcionales (Java 8+)

> [!example]- ⚡ Interfaces con un Solo Método
> 
> ```java
> // Interface funcional - un solo método abstracto
> @FunctionalInterface
> public interface Operacion {
>     double calcular(double a, double b);
>     
>     // Puede tener default/static
>     static void info() {
>         System.out.println("Interface para operaciones");
>     }
> }
> 
> // Uso con lambda expressions
> public class CalculadoraLambda {
>     public static void main(String[] args) {
>         // Implementación tradicional
>         Operacion suma = new Operacion() {
>             @Override
>             public double calcular(double a, double b) {
>                 return a + b;
>             }
>         };
>         
>         // ✨ Con lambda (Java 8+)
>         Operacion resta = (a, b) -> a - b;
>         Operacion multiplicacion = (a, b) -> a * b;
>         Operacion division = (a, b) -> a / b;
>         
>         System.out.println("5 + 3 = " + suma.calcular(5, 3));
>         System.out.println("5 - 3 = " + resta.calcular(5, 3));
>         System.out.println("5 * 3 = " + multiplicacion.calcular(5, 3));
>         System.out.println("5 / 3 = " + division.calcular(5, 3));
>     }
> }
> 
> // Interfaces funcionales comunes de Java
> import java.util.function.*;
> 
> // Predicate<T> - Retorna boolean
> Predicate<Integer> esPar = n -> n % 2 == 0;
> System.out.println(esPar.test(4));  // true
> 
> // Consumer<T> - No retorna nada
> Consumer<String> imprimir = s -> System.out.println(s);
> imprimir.accept("Hola");
> 
> // Function<T, R> - Transforma T en R
> Function<String, Integer> longitud = s -> s.length();
> System.out.println(longitud.apply("Java"));  // 4
> 
> // Supplier<T> - Provee un valor
> Supplier<Double> random = () -> Math.random();
> System.out.println(random.get());
> ```

---

## 🏗️ Patrones de Diseño con Interfaces

> [!note]- 🎯 Strategy Pattern
> 
> ```java
> // Interface Strategy
> interface EstrategiaDescuento {
>     double calcularDescuento(double precio);
> }
> 
> // Estrategias concretas
> class DescuentoRegular implements EstrategiaDescuento {
>     @Override
>     public double calcularDescuento(double precio) {
>         return precio * 0.10;  // 10%
>     }
> }
> 
> class DescuentoVIP implements EstrategiaDescuento {
>     @Override
>     public double calcularDescuento(double precio) {
>         return precio * 0.25;  // 25%
>     }
> }
> 
> class DescuentoTemporada implements EstrategiaDescuento {
>     @Override
>     public double calcularDescuento(double precio) {
>         return precio * 0.40;  // 40%
>     }
> }
> 
> // Contexto que usa la estrategia
> class CarritoCompras {
>     private EstrategiaDescuento estrategia;
>     
>     public void setEstrategia(EstrategiaDescuento estrategia) {
>         this.estrategia = estrategia;
>     }
>     
>     public double calcularTotal(double precio) {
>         if (estrategia == null) {
>             return precio;
>         }
>         double descuento = estrategia.calcularDescuento(precio);
>         return precio - descuento;
>     }
> }
> 
> // USO
> CarritoCompras carrito = new CarritoCompras();
> double precio = 1000;
> 
> carrito.setEstrategia(new DescuentoRegular());
> System.out.println("Regular: $" + carrito.calcularTotal(precio));
> 
> carrito.setEstrategia(new DescuentoVIP());
> System.out.println("VIP: $" + carrito.calcularTotal(precio));
> ```

---

## 🔗 Interfaces Anidadas y Herencia

> [!tip]- 🏛️ Estructuras Complejas
> 
> ```java
> // Interface que hereda de otra
> interface Animal {
>     void comer();
>     void dormir();
> }
> 
> interface Mascota extends Animal {
>     void jugar();
>     void hacerTruco();
> }
> 
> // Implementación debe incluir TODOS los métodos
> class Perro implements Mascota {
>     @Override
>     public void comer() {
>         System.out.println("Perro comiendo");
>     }
>     
>     @Override
>     public void dormir() {
>         System.out.println("Perro durmiendo");
>     }
>     
>     @Override
>     public void jugar() {
>         System.out.println("Perro jugando");
>     }
>     
>     @Override
>     public void hacerTruco() {
>         System.out.println("Perro hace trucos");
>     }
> }
> 
> // Interface anidada
> interface BaseDatos {
>     interface Conexion {
>         void conectar();
>         void desconectar();
>     }
>     
>     interface Consulta {
>         void ejecutar(String sql);
>     }
> }
> ```

---

## ⚡ Ventajas de las Interfaces

> [!success]- 🎯 Beneficios Clave
> 
> **1. Flexibilidad extrema:**
> 
> ```java
> // Una clase puede ser muchas cosas a la vez
> class Dron implements Volador, Fotografico, Programable {
>     // Combina múltiples capacidades
> }
> ```
> 
> **2. Desacoplamiento:**
> 
> ```java
> // Código depende de la interface, no de la implementación
> public void procesarPago(MetodoPago metodo) {
>     metodo.procesarPago(100);
>     // No le importa si es tarjeta, PayPal, etc.
> }
> ```
> 
> **3. Testing más fácil:**
> 
> ```java
> // Interface facilita mocks para pruebas
> interface ServicioExterno {
>     String obtenerDatos();
> }
> 
> // Mock para testing
> class ServicioMock implements ServicioExterno {
>     @Override
>     public String obtenerDatos() {
>         return "Datos de prueba";
>     }
> }
> ```
> 
> **4. Polimorfismo puro:**
> 
> ```java
> List<MetodoPago> metodos = new ArrayList<>();
> metodos.add(new TarjetaCredito(...));
> metodos.add(new PayPal(...));
> metodos.add(new Efectivo());
> 
> // Tratar todos igual
> for (MetodoPago m : metodos) {
>     m.procesarPago(100);
> }
> ```

---

## 📚 Resumen Ejecutivo

> [!quote]- 🌟 Puntos Clave **Has aprendido:**
> 
> - ✅ Interfaces como contratos puros
> - ✅ Herencia múltiple con `implements`
> - ✅ Métodos default y static (Java 8+)
> - ✅ Diferencias con clases abstractas
> - ✅ Interfaces funcionales y lambdas
> - ✅ Patrones de diseño (Strategy)
> - ✅ Polimorfismo con interfaces
> 
> **Cuándo usar:**
> 
> - ✅ Definir capacidades ("PUEDE-HACER")
> - ✅ Necesitar herencia múltiple
> - ✅ Crear contratos sin implementación
> - ✅ Desacoplar código
> - ✅ Facilitar testing
> 
> **Próximos temas:**
> 
> - **[[06 - Polimorfismo]]** - Poder de las interfaces
> - **[[07 - Colecciones]]** - List, Set, Map (todas son interfaces)

---

**Tags:** #java #poo #interfaces #herencia-multiple #polimorfismo #strategy-pattern #lambdas #functional-interface #desacoplamiento