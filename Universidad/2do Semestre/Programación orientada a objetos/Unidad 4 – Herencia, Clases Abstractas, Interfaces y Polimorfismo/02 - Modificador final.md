# 🔒 Modificador `final` en Java

## 🎯 Introducción

> [!info]- 💡 ¿Qué es el Modificador `final`? El modificador **`final`** es una palabra clave que se usa para **prevenir modificaciones**. Puede aplicarse a variables, métodos y clases.
> 
> **Analogía:** Como el cemento que solidifica
> 
> - Una vez que el cemento se endurece, no puede cambiar de forma
> - El modificador `final` "solidifica" lo que defines
> - Garantiza que algo permanezca constante e inmutable
> 
> **¿Por qué usar `final`?**
> 
> - ✅ **Seguridad:** Previene cambios accidentales
> - ✅ **Claridad:** Intención explícita en el código
> - ✅ **Optimización:** El compilador puede optimizar mejor
> - ✅ **Thread-safety:** Variables inmutables son seguras entre hilos
> - ✅ **Diseño:** Evita herencia o sobreescritura no deseada

---

## 📦 Variables `final`

### Variables Primitivas

> [!example]- 🔢 Final con Tipos Primitivos
> 
> ```java
> public class VariablesFinal {
>     public static void main(String[] args) {
>         // Variable final - valor no puede cambiar
>         final int MAX_USUARIOS = 100;
>         final double PI = 3.14159;
>         final boolean DEBUG_MODE = true;
>         
>         System.out.println("Máximo de usuarios: " + MAX_USUARIOS);
>         
>         // ❌ Error de compilación - no se puede reasignar
>         // MAX_USUARIOS = 200;  // Error: cannot assign a value to final variable
>         
>         // ✅ Usar en operaciones está permitido
>         int usuarios = MAX_USUARIOS / 2;
>         System.out.println("Usuarios actuales: " + usuarios);
>         
>         // Variables locales final
>         final int edad = 25;
>         // edad = 26;  // ❌ Error
>         
>         System.out.println("Edad: " + edad);
>     }
> }
> ```
> 
> **Convención de nombres:**
> 
> ```java
> // ✅ CONSTANTES - Todo en mayúsculas con guión bajo
> final int MAX_VALUE = 100;
> final double TAX_RATE = 0.16;
> final String DATABASE_URL = "localhost:3306";
> 
> // ✅ Variables finales locales - camelCase normal
> final int contador = 0;
> final String nombre = "Juan";
> ```

### Variables de Referencia

> [!warning]- 🎯 Final con Objetos - ¡Cuidado!
> 
> ```java
> class Persona {
>     String nombre;
>     int edad;
>     
>     public Persona(String nombre, int edad) {
>         this.nombre = nombre;
>         this.edad = edad;
>     }
>     
>     public void mostrarInfo() {
>         System.out.println(nombre + " - " + edad + " años");
>     }
> }
> 
> public class ReferenciaFinal {
>     public static void main(String[] args) {
>         // ✅ La REFERENCIA es final, no el objeto
>         final Persona persona = new Persona("Ana", 25);
>         
>         persona.mostrarInfo();  // Ana - 25 años
>         
>         // ✅ PERMITIDO - Modificar el contenido del objeto
>         persona.nombre = "María";
>         persona.edad = 30;
>         persona.mostrarInfo();  // María - 30 años
>         
>         // ❌ NO PERMITIDO - Reasignar la referencia
>         // persona = new Persona("Carlos", 35);  // Error!
>         
>         // Ejemplo con arrays
>         final int[] numeros = {1, 2, 3, 4, 5};
>         
>         // ✅ PERMITIDO - Modificar elementos
>         numeros[0] = 10;
>         numeros[2] = 30;
>         System.out.println("Primer elemento: " + numeros[0]);  // 10
>         
>         // ❌ NO PERMITIDO - Reasignar el array
>         // numeros = new int[]{6, 7, 8};  // Error!
>     }
> }
> ```
> 
> **Regla importante:**
> 
> - `final` hace que la **referencia** sea inmutable
> - El **contenido** del objeto puede cambiar
> - Para inmutabilidad completa, necesitas diseñar clases inmutables

---

## 🏗️ Atributos `final` en Clases

### Inicialización de Atributos Final

> [!success]- ⚙️ Tres Formas de Inicializar
> 
> ```java
> public class Empleado {
>     // 1️⃣ Inicialización directa
>     private final String EMPRESA = "Tech Corp";
>     
>     // 2️⃣ Inicialización en constructor
>     private final String id;
>     private final String nombre;
>     
>     // 3️⃣ Inicialización en bloque de instancia
>     private final long timestamp;
>     {
>         timestamp = System.currentTimeMillis();
>     }
>     
>     // Atributos normales (no final)
>     private int edad;
>     private double salario;
>     
>     // Constructor - DEBE inicializar todos los final
>     public Empleado(String id, String nombre, int edad) {
>         this.id = id;        // ✅ Inicialización requerida
>         this.nombre = nombre; // ✅ Inicialización requerida
>         this.edad = edad;
>         this.salario = 0.0;
>         
>         System.out.println("✓ Empleado creado: " + nombre);
>     }
>     
>     // ❌ Este constructor daría error - no inicializa 'nombre'
>     /*
>     public Empleado(String id) {
>         this.id = id;
>         // Error: variable nombre might not have been initialized
>     }
>     */
>     
>     // ✅ Getters - No hay setters para final
>     public String getId() { return id; }
>     public String getNombre() { return nombre; }
>     public String getEmpresa() { return EMPRESA; }
>     
>     // ✅ Setters solo para no-final
>     public void setEdad(int edad) { this.edad = edad; }
>     public void setSalario(double salario) { this.salario = salario; }
>     
>     public void mostrarInfo() {
>         System.out.println("\n=== EMPLEADO ===");
>         System.out.println("ID: " + id);
>         System.out.println("Nombre: " + nombre);
>         System.out.println("Empresa: " + EMPRESA);
>         System.out.println("Edad: " + edad);
>         System.out.println("Salario: $" + salario);
>         System.out.println("Timestamp: " + timestamp);
>     }
>     
>     public static void main(String[] args) {
>         Empleado emp = new Empleado("EMP001", "Juan Pérez", 30);
>         emp.setSalario(50000);
>         emp.mostrarInfo();
>         
>         // emp.id = "EMP002";  // ❌ Error - id es final
>         emp.setEdad(31);       // ✅ OK - edad no es final
>         
>         emp.mostrarInfo();
>     }
> }
> ```

### Constantes de Clase

> [!tip]- 📌 Constantes Públicas con `static final`
> 
> ```java
> public class Configuracion {
>     // Constantes públicas - accesibles desde cualquier lugar
>     public static final String APP_NAME = "MiAplicación";
>     public static final String VERSION = "2.1.0";
>     public static final int MAX_CONNECTIONS = 100;
>     public static final double DEFAULT_TIMEOUT = 30.0;
>     
>     // Constantes privadas - uso interno
>     private static final String SECRET_KEY = "abc123xyz";
>     private static final int BUFFER_SIZE = 8192;
>     
>     // Constructor privado - clase de utilidades
>     private Configuracion() {
>         throw new AssertionError("No se puede instanciar");
>     }
>     
>     // Métodos que usan las constantes
>     public static void mostrarInfo() {
>         System.out.println("╔════════════════════════════╗");
>         System.out.println("║   " + APP_NAME + " v" + VERSION + "      ║");
>         System.out.println("╚════════════════════════════╝");
>         System.out.println("Max conexiones: " + MAX_CONNECTIONS);
>         System.out.println("Timeout: " + DEFAULT_TIMEOUT + "s");
>     }
> }
> 
> // Clase de colores
> public class Colores {
>     // Constantes para códigos de color
>     public static final String RESET = "\u001B[0m";
>     public static final String ROJO = "\u001B[31m";
>     public static final String VERDE = "\u001B[32m";
>     public static final String AMARILLO = "\u001B[33m";
>     public static final String AZUL = "\u001B[34m";
>     
>     public static String colorear(String texto, String color) {
>         return color + texto + RESET;
>     }
> }
> 
> // USO:
> public class TestSingleton {
>     public static void main(String[] args) {
>         DatabaseConnection db1 = DatabaseConnection.getInstance();
>         DatabaseConnection db2 = DatabaseConnection.getInstance();
>         
>         System.out.println("¿Misma instancia? " + (db1 == db2));
>         System.out.println(db1.getConnectionString());
>     }
> }
> ```

### Template Method con `final`

> [!success]- 📋 Flujo de Trabajo Fijo
> 
> ```java
> abstract class ProcesoDocumento {
>     // Método template - final para prevenir modificación
>     public final void procesar() {
>         System.out.println("\n╔═══ PROCESANDO DOCUMENTO ═══╗");
>         
>         abrirDocumento();
>         validarFormato();
>         extraerDatos();
>         procesarContenido();
>         guardarResultado();
>         cerrarDocumento();
>         
>         System.out.println("╚════════════════════════════╝");
>     }
>     
>     // Métodos abstractos - las subclases los implementan
>     protected abstract void abrirDocumento();
>     protected abstract void validarFormato();
>     protected abstract void extraerDatos();
>     protected abstract void procesarContenido();
>     
>     // Métodos concretos - comportamiento común
>     private final void guardarResultado() {
>         System.out.println("💾 Guardando resultado...");
>     }
>     
>     private final void cerrarDocumento() {
>         System.out.println("🔒 Cerrando documento");
>     }
> }
> 
> class ProcesadorPDF extends ProcesoDocumento {
>     @Override
>     protected void abrirDocumento() {
>         System.out.println("📄 Abriendo archivo PDF");
>     }
>     
>     @Override
>     protected void validarFormato() {
>         System.out.println("✓ Validando formato PDF");
>     }
>     
>     @Override
>     protected void extraerDatos() {
>         System.out.println("📊 Extrayendo texto del PDF");
>     }
>     
>     @Override
>     protected void procesarContenido() {
>         System.out.println("⚙️ Procesando contenido PDF");
>     }
> }
> 
> class ProcesadorExcel extends ProcesoDocumento {
>     @Override
>     protected void abrirDocumento() {
>         System.out.println("📊 Abriendo archivo Excel");
>     }
>     
>     @Override
>     protected void validarFormato() {
>         System.out.println("✓ Validando formato Excel");
>     }
>     
>     @Override
>     protected void extraerDatos() {
>         System.out.println("📈 Extrayendo celdas de Excel");
>     }
>     
>     @Override
>     protected void procesarContenido() {
>         System.out.println("⚙️ Calculando fórmulas");
>     }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         // Acceder a constantes
>         System.out.println("App: " + Configuracion.APP_NAME);
>         System.out.println("Versión: " + Configuracion.VERSION);
>         
>         Configuracion.mostrarInfo();
>         
>         // Usar colores
>         System.out.println(Colores.colorear("¡Éxito!", Colores.VERDE));
>         System.out.println(Colores.colorear("Error", Colores.ROJO));
>         System.out.println(Colores.colorear("Advertencia", Colores.AMARILLO));
>     }
> }
> ```

---

## 🎭 Métodos `final`

### Prevenir Sobreescritura

> [!example]- 🔐 Métodos que No Pueden Ser Sobrescritos
> 
> ```java
> class Animal {
>     // Método normal - puede ser sobrescrito
>     public void hacerSonido() {
>         System.out.println("El animal hace un sonido");
>     }
>     
>     // Método final - NO puede ser sobrescrito
>     public final void respirar() {
>         System.out.println("El animal respira oxígeno");
>     }
>     
>     // Método final con lógica crítica
>     public final void validarEstado() {
>         System.out.println("Validando estado vital del animal...");
>         // Lógica crítica que no debe modificarse
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("Información del animal");
>     }
> }
> 
> class Perro extends Animal {
>     // ✅ PERMITIDO - Sobrescribir método normal
>     @Override
>     public void hacerSonido() {
>         System.out.println("El perro ladra: ¡Guau!");
>     }
>     
>     // ❌ ERROR - No se puede sobrescribir método final
>     /*
>     @Override
>     public void respirar() {
>         System.out.println("El perro respira");
>     }
>     */
>     
>     // ✅ PERMITIDO - Agregar nuevos métodos
>     public void moverCola() {
>         System.out.println("El perro mueve la cola");
>     }
> }
> 
> public class TestMetodosFinal {
>     public static void main(String[] args) {
>         Perro perro = new Perro();
>         
>         perro.hacerSonido();    // Versión sobrescrita
>         perro.respirar();       // Versión original (final)
>         perro.validarEstado();  // Versión original (final)
>         perro.moverCola();      // Método propio
>     }
> }
> ```

### Caso de Uso: Plantilla con Pasos Fijos

> [!success]- 🎯 Patrón Template Method
> 
> ```java
> abstract class ProcesoPago {
>     // Método final - define el flujo que no puede cambiar
>     public final void procesarPago(double monto) {
>         System.out.println("\n╔═══════════════════════════╗");
>         System.out.println("║   PROCESANDO PAGO         ║");
>         System.out.println("╚═══════════════════════════╝");
>         
>         // 1. Validar (puede variar por tipo de pago)
>         if (!validarPago(monto)) {
>             System.out.println("❌ Pago inválido");
>             return;
>         }
>         
>         // 2. Procesar (específico de cada tipo)
>         realizarTransaccion(monto);
>         
>         // 3. Registrar (fijo para todos)
>         registrarEnSistema(monto);
>         
>         // 4. Notificar (puede variar)
>         notificarCliente(monto);
>         
>         System.out.println("✓ Pago completado");
>     }
>     
>     // Métodos que las subclases pueden/deben implementar
>     protected abstract boolean validarPago(double monto);
>     protected abstract void realizarTransaccion(double monto);
>     protected abstract void notificarCliente(double monto);
>     
>     // Método final privado - uso interno
>     private final void registrarEnSistema(double monto) {
>         System.out.println("📝 Registrando pago de $" + monto + " en el sistema");
>     }
> }
> 
> class PagoTarjeta extends ProcesoPago {
>     @Override
>     protected boolean validarPago(double monto) {
>         System.out.println("🔍 Validando tarjeta...");
>         return monto > 0 && monto < 10000;
>     }
>     
>     @Override
>     protected void realizarTransaccion(double monto) {
>         System.out.println("💳 Procesando con tarjeta: $" + monto);
>     }
>     
>     @Override
>     protected void notificarCliente(double monto) {
>         System.out.println("📧 Email enviado: Pago de $" + monto + " procesado");
>     }
> }
> 
> class PagoEfectivo extends ProcesoPago {
>     @Override
>     protected boolean validarPago(double monto) {
>         System.out.println("🔍 Validando efectivo...");
>         return monto > 0;
>     }
>     
>     @Override
>     protected void realizarTransaccion(double monto) {
>         System.out.println("💵 Recibiendo efectivo: $" + monto);
>     }
>     
>     @Override
>     protected void notificarCliente(double monto) {
>         System.out.println("🧾 Imprimiendo recibo de $" + monto);
>     }
> }
> 
> public class SistemaPagos {
>     public static void main(String[] args) {
>         ProcesoPago pagoTarjeta = new PagoTarjeta();
>         pagoTarjeta.procesarPago(150.50);
>         
>         ProcesoPago pagoEfectivo = new PagoEfectivo();
>         pagoEfectivo.procesarPago(200.00);
>     }
> }
> ```

---

## 🏛️ Clases `final`

### Prevenir Herencia

> [!warning]- 🚫 Clases que No Pueden Ser Extendidas
> 
> ```java
> // ✅ Clase final - no se puede heredar
> public final class Matematicas {
>     // Constructor privado - clase de utilidades
>     private Matematicas() {
>         throw new AssertionError("No se puede instanciar");
>     }
>     
>     // Métodos estáticos de utilidad
>     public static int sumar(int a, int b) {
>         return a + b;
>     }
>     
>     public static double calcularPromedio(int[] numeros) {
>         if (numeros.length == 0) return 0;
>         
>         int suma = 0;
>         for (int num : numeros) {
>             suma += num;
>         }
>         return (double) suma / numeros.length;
>     }
>     
>     public static int maximo(int a, int b) {
>         return (a > b) ? a : b;
>     }
> }
> 
> // ❌ ERROR - No se puede heredar de clase final
> /*
> class MiMatematicas extends Matematicas {
>     // Error: cannot inherit from final Matematicas
> }
> */
> 
> // ✅ USO CORRECTO
> public class TestMatematicas {
>     public static void main(String[] args) {
>         int suma = Matematicas.sumar(5, 3);
>         System.out.println("Suma: " + suma);
>         
>         int[] numeros = {10, 20, 30, 40, 50};
>         double promedio = Matematicas.calcularPromedio(numeros);
>         System.out.println("Promedio: " + promedio);
>         
>         // No se puede instanciar
>         // Matematicas m = new Matematicas();  // Error
>     }
> }
> ```

### Clases Inmutables

> [!tip]- 🔒 Diseño de Clases Inmutables
> 
> ```java
> // Clase final e inmutable
> public final class Punto {
>     // Atributos finales
>     private final int x;
>     private final int y;
>     
>     // Constructor
>     public Punto(int x, int y) {
>         this.x = x;
>         this.y = y;
>     }
>     
>     // Solo getters - NO setters
>     public int getX() { return x; }
>     public int getY() { return y; }
>     
>     // Métodos que retornan NUEVAS instancias
>     public Punto mover(int deltaX, int deltaY) {
>         return new Punto(this.x + deltaX, this.y + deltaY);
>     }
>     
>     public double distanciaOrigen() {
>         return Math.sqrt(x * x + y * y);
>     }
>     
>     public double distancia(Punto otro) {
>         int dx = this.x - otro.x;
>         int dy = this.y - otro.y;
>         return Math.sqrt(dx * dx + dy * dy);
>     }
>     
>     @Override
>     public String toString() {
>         return "(" + x + ", " + y + ")";
>     }
>     
>     @Override
>     public boolean equals(Object obj) {
>         if (this == obj) return true;
>         if (!(obj instanceof Punto)) return false;
>         Punto otro = (Punto) obj;
>         return this.x == otro.x && this.y == otro.y;
>     }
> }
> 
> // Clase inmutable con objetos internos
> public final class Persona {
>     private final String nombre;
>     private final int edad;
>     private final int[] calificaciones;  // ⚠️ Array es mutable
>     
>     public Persona(String nombre, int edad, int[] calificaciones) {
>         this.nombre = nombre;
>         this.edad = edad;
>         // ✅ Copia defensiva - no guardar referencia original
>         this.calificaciones = calificaciones.clone();
>     }
>     
>     public String getNombre() { return nombre; }
>     public int getEdad() { return edad; }
>     
>     public int[] getCalificaciones() {
>         // ✅ Retornar copia - no exponer array interno
>         return calificaciones.clone();
>     }
>     
>     public double getPromedio() {
>         int suma = 0;
>         for (int cal : calificaciones) {
>             suma += cal;
>         }
>         return (double) suma / calificaciones.length;
>     }
>     
>     @Override
>     public String toString() {
>         return nombre + " (" + edad + " años) - Promedio: " + 
>                String.format("%.2f", getPromedio());
>     }
> }
> 
> // USO:
> public class TestInmutabilidad {
>     public static void main(String[] args) {
>         // Punto inmutable
>         Punto p1 = new Punto(3, 4);
>         System.out.println("Punto original: " + p1);
>         
>         // Mover crea un NUEVO punto
>         Punto p2 = p1.mover(2, 3);
>         System.out.println("Punto original: " + p1);  // No cambió
>         System.out.println("Punto nuevo: " + p2);
>         
>         System.out.println("Distancia al origen: " + p1.distanciaOrigen());
>         
>         // Persona inmutable
>         int[] notas = {85, 90, 78, 92};
>         Persona persona = new Persona("Ana", 20, notas);
>         
>         System.out.println("\n" + persona);
>         
>         // Modificar array original NO afecta a persona
>         notas[0] = 100;
>         System.out.println("Después de modificar array original:");
>         System.out.println(persona);  // Promedio no cambió
>         
>         // Modificar array retornado tampoco afecta
>         int[] notasObtenidas = persona.getCalificaciones();
>         notasObtenidas[0] = 0;
>         System.out.println("Después de modificar copia:");
>         System.out.println(persona);  // Promedio sigue igual
>     }
> }
> ```

---

## 🎯 Parámetros `final`

### En Métodos

> [!example]- 📝 Parámetros Inmutables
> 
> ```java
> public class ParametrosFinal {
>     // Parámetro final - no se puede reasignar
>     public static void imprimirMensaje(final String mensaje) {
>         System.out.println("Mensaje: " + mensaje);
>         
>         // ❌ Error - no se puede modificar
>         // mensaje = "Otro mensaje";
>         
>         // ✅ Usar en operaciones está bien
>         String mensajeMayusculas = mensaje.toUpperCase();
>         System.out.println("En mayúsculas: " + mensajeMayusculas);
>     }
>     
>     // Múltiples parámetros final
>     public static int calcular(final int a, final int b, final String operacion) {
>         return switch (operacion) {
>             case "suma" -> a + b;
>             case "resta" -> a - b;
>             case "multiplicacion" -> a * b;
>             case "division" -> b != 0 ? a / b : 0;
>             default -> 0;
>         };
>     }
>     
>     // Con objetos - la referencia es final
>     public static void procesarPersona(final Persona persona) {
>         // ✅ Modificar el objeto está permitido
>         persona.nombre = "Nombre Modificado";
>         
>         // ❌ Reasignar la referencia NO está permitido
>         // persona = new Persona("Otro", 30);
>     }
>     
>     public static void main(String[] args) {
>         imprimirMensaje("Hola Mundo");
>         
>         int resultado = calcular(10, 5, "suma");
>         System.out.println("Resultado: " + resultado);
>     }
> }
> ```

### En Lambdas y Clases Anónimas

> [!success]- 🎭 Variables Efectivamente Final
> 
> ```java
> import java.util.function.Consumer;
> 
> public class VariablesEfectivamenteFinal {
>     public static void main(String[] args) {
>         // Variable efectivamente final (no se modifica después)
>         String prefijo = "Usuario: ";
>         int contador = 0;  // Efectivamente final
>         
>         // ✅ Lambdas pueden acceder a variables efectivamente final
>         Consumer<String> imprimir = nombre -> {
>             System.out.println(prefijo + nombre);
>             // System.out.println("Contador: " + contador);  // OK
>         };
>         
>         imprimir.accept("Juan");
>         imprimir.accept("María");
>         
>         // ❌ Si modificas la variable, ya no es efectivamente final
>         // contador++;  // Error en la lambda si descomentamos esto
>         
>         // Variable explícitamente final
>         final String sufijo = " - Activo";
>         
>         Consumer<String> imprimirConSufijo = nombre -> {
>             System.out.println(nombre + sufijo);
>         };
>         
>         imprimirConSufijo.accept("Pedro");
>         
>         // Clase anónima
>         Runnable tarea = new Runnable() {
>             @Override
>             public void run() {
>                 // Puede acceder a variables final o efectivamente final
>                 System.out.println("Tarea ejecutada: " + prefijo);
>             }
>         };
>         
>         tarea.run();
>     }
> }
> ```

---

## 🎨 Ejemplo Completo: Sistema de Configuración

> [!example]- ⚙️ Aplicación Real con `final`
> 
> ```java
> // =============================
> // CLASE DE CONFIGURACIÓN
> // =============================
> 
> public final class ConfiguracionSistema {
>     // Constantes públicas
>     public static final String APP_NAME = "Sistema de Ventas";
>     public static final String VERSION = "3.0.1";
>     public static final int MAX_INTENTOS_LOGIN = 3;
>     public static final double IVA = 0.16;
>     
>     // Constantes privadas
>     private static final String DB_HOST = "localhost";
>     private static final int DB_PORT = 5432;
>     private static final String DB_NAME = "ventas_db";
>     
>     // Atributos de instancia final
>     private final String idSesion;
>     private final long timestampInicio;
>     private final String usuario;
>     
>     // Atributo mutable
>     private int intentosLogin;
>     
>     // Constructor
>     public ConfiguracionSistema(final String usuario) {
>         this.idSesion = generarIdSesion();
>         this.timestampInicio = System.currentTimeMillis();
>         this.usuario = usuario;
>         this.intentosLogin = 0;
>         
>         System.out.println("✓ Sesión iniciada para: " + usuario);
>     }
>     
>     // Método final - no puede ser sobrescrito (aunque la clase ya es final)
>     public final String getConnectionString() {
>         return String.format("jdbc:postgresql://%s:%d/%s", 
>                            DB_HOST, DB_PORT, DB_NAME);
>     }
>     
>     private String generarIdSesion() {
>         return "SES-" + System.currentTimeMillis() + 
>                "-" + (int)(Math.random() * 1000);
>     }
>     
>     public boolean intentarLogin() {
>         intentosLogin++;
>         if (intentosLogin > MAX_INTENTOS_LOGIN) {
>             System.out.println("❌ Máximo de intentos alcanzado");
>             return false;
>         }
>         return true;
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("\n╔═══════════════════════════════╗");
>         System.out.println("║   " + APP_NAME + " v" + VERSION + "   ║");
>         System.out.println("╚═══════════════════════════════╝");
>         System.out.println("ID Sesión: " + idSesion);
>         System.out.println("Usuario: " + usuario);
>         System.out.println("Intentos login: " + intentosLogin);
>         System.out.println("IVA: " + (IVA * 100) + "%");
>     }
>     
>     // Getters para atributos final
>     public String getIdSesion() { return idSesion; }
>     public String getUsuario() { return usuario; }
>     public long getTimestampInicio() { return timestampInicio; }
> }
> 
> // =============================
> // CLASE PRODUCTO INMUTABLE
> // =============================
> 
> public final class Producto {
>     private final String codigo;
>     private final String nombre;
>     private final double precio;
>     private final String categoria;
>     
>     public Producto(final String codigo, final String nombre, 
>                     final double precio, final String categoria) {
>         // Validación en constructor
>         if (precio < 0) {
>             throw new IllegalArgumentException("Precio no puede ser negativo");
>         }
>         
>         this.codigo = codigo;
>         this.nombre = nombre;
>         this.precio = precio;
>         this.categoria = categoria;
>     }
>     
>     // Solo getters - inmutable
>     public String getCodigo() { return codigo;
> ```

# 📚 Referencias y Conexiones - Modificador `final`

> [!quote] 🔗 Notas Relacionadas
> 
> 
> ### Conceptos Fundamentales
> 
> - [[01 - Introducción a POO]] - Fundamentos de programación orientada a objetos
> - [[Variables y Tipos de Datos]] - Base de variables en Java
> - [[Constructores]] - Inicialización de atributos final
> 
> ### Modificadores y Palabras Clave
> 
> - [[03 - Modificador static]] - Combinar `static final` para constantes
> - [[04 - Modificadores de Acceso]] - public/private con final
> - [[05 - Modificador abstract]] - Diferencias con final
> - [[Herencia]] - Cómo final previene la herencia
> - [[Sobrescritura de Métodos]] - final previene @Override
> 
> ### Inmutabilidad y Diseño
> 
> - [[Clases Inmutables]] - Diseño completo de objetos inmutables
> - [[Records (Java 14+)]] - Sintaxis moderna para inmutabilidad
> - [[Value Objects]] - Objetos de valor inmutables
> - [[DTOs]] - Data Transfer Objects inmutables
> - [[Defensive Copying]] - Copias defensivas con final
> 
> ### Patrones de Diseño
> 
> - [[Singleton Pattern]] - Implementación thread-safe con final
> - [[Builder Pattern]] - Construir objetos inmutables
> - [[Template Method Pattern]] - Métodos final en plantillas
> - [[Factory Pattern]] - Crear instancias inmutables
> 
> ### Colecciones y Estructuras
> 
> - [[Collections Framework]] - Colecciones inmutables
> - [[Collections.unmodifiable]] - Wrappers inmutables
> - [[List.of(), Set.of(), Map.of()]] - Colecciones inmutables (Java 9+)
> 
> ### Concurrencia
> 
> - [[Thread Safety]] - final y seguridad entre hilos
> - [[Volatile vs Final]] - Diferencias en concurrencia
> - [[Happens-Before]] - Garantías de memoria con final
> 
> ### Características Modernas
> 
> - [[Java 8 - Lambdas]] - Variables efectivamente final
> - [[Java 14 - Records]] - Clases inmutables automáticas
> - [[Java 15 - Sealed Classes]] - Control de herencia avanzado
> 
> ### Principios SOLID
> 
> - [[Single Responsibility]] - Una razón para cambiar
> - [[Open-Closed Principle]] - final y extensibilidad
> - [[Liskov Substitution]] - final y sustitución
> 

---

## 📊 Tablón de Referencias Rápidas

> [!success] Comparativas Clave
> 
> 
> **`final` vs `static`**
> 
> ```java
> private final String id;           // Por instancia, no cambia
> private static int contador;       // Compartido, puede cambiar
> public static final int MAX = 100; // Compartido y constante
> ```
> 
> **`final` vs Inmutabilidad**
> 
> ```java
> // Solo referencia final
> final List<String> lista = new ArrayList<>();
> lista.add("x"); // ✅ OK
> 
> // Inmutabilidad completa
> final List<String> inmutable = List.of("a", "b");
> // inmutable.add("x"); // ❌ Error
> ```
> 
> **`final` vs `sealed` (Java 15+)**
> 
> ```java
> public final class A { }              // No herencia
> public sealed class B permits C { }   // Herencia controlada
> ```
> 
> ### Cuándo Usar `final`
> 
> |Contexto|Usar `final`|Ejemplo|
> |---|---|---|
> |**Constantes**|✅ Siempre|`public static final int MAX = 100;`|
> |**IDs únicos**|✅ Siempre|`private final String id;`|
> |**Configuración**|✅ Recomendado|`private final String apiKey;`|
> |**Timestamps**|✅ Recomendado|`private final long createdAt;`|
> |**DTOs**|✅ Recomendado|Toda la clase final e inmutable|
> |**Clases utilidad**|✅ Siempre|`public final class Utils { }`|
> |**Métodos críticos**|✅ Recomendado|`public final void validate()`|
> |**Variables locales**|⚠️ Opcional|`final int temp = 5;`|
> |**Parámetros**|⚠️ Opcional|`void process(final String data)`|
> |**Arrays/Collections**|⚠️ Cuidado|Solo referencia, no contenido|
> 
> ### Clases Final en Java Core
> 
> - `String` - Inmutable y final
> - `Integer`, `Double`, etc. - Wrapper classes (final)
> - `Math` - Clase de utilidad (final)
> - `System` - Clase del sistema (final)
> 
> ### Evolución del Concepto
> 
> - **Java 5**: Generics con final
> - **Java 8**: Variables efectivamente final en lambdas
> - **Java 9**: `List.of()`, `Set.of()`, `Map.of()` inmutables
> - **Java 14**: Records (clases inmutables automáticas)
> - **Java 15**: Sealed classes (control de herencia)
> 

---

## 🏷️ Tags

#java #final #modificadores #inmutabilidad` ` #constantes` ` #thread-safety` ` #poo` ` #encapsulamiento` ` #herencia` ` #polimorfismo` ` #singleton` ` #builder` ` #template-method` ` #value-object` ` #dto` ` #factory
#java8` ` #java14` ` #java15 #records #sealed-classes #lambdas
#buenas-practicas #clean-code  #solid #diseño` 

---

