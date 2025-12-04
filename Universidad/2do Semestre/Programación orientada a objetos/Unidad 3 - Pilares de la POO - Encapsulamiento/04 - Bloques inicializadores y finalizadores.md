# 📘 Bloques Inicializadores y Finalizadores en Java

## 🎯 Introducción

> [!info]- 💡 ¿Qué son? Los **bloques inicializadores** son secciones de código que se ejecutan automáticamente cuando se crea un objeto o se carga una clase. Permiten inicializar atributos con lógica más compleja que una simple asignación.
> 
> **Tipos:**
> 
> - **Bloques de instancia:** Se ejecutan al crear cada objeto
> - **Bloques estáticos:** Se ejecutan una vez al cargar la clase
> 
> **Finalizadores:** Métodos especiales que se ejecutan antes de que el objeto sea eliminado por el Garbage Collector (uso desaconsejado en Java moderno).

---

## 🔧 Bloques de Instancia

> [!example]- 📦 Inicialización de Objetos
> 
> **Sintaxis:**
> 
> ```java
> public class Ejemplo {
>     private int valor;
>     
>     // Bloque de instancia (sin modificador)
>     {
>         valor = 10;
>         System.out.println("Bloque de instancia ejecutado");
>     }
>     
>     public Ejemplo() {
>         System.out.println("Constructor ejecutado");
>     }
> }
> ```
> 
> **Orden de ejecución:**
> 
> 1. Inicialización de atributos (valores por defecto)
> 2. Bloques de instancia (en orden de aparición)
> 3. Constructor
> 
> **Ejemplo práctico:**
> 
> ```java
> public class CuentaBancaria {
>     private String numeroCuenta;
>     private double saldo;
>     private List<String> historial;
>     
>     // Bloque de instancia - inicialización compleja
>     {
>         historial = new ArrayList<>();
>         historial.add("Cuenta creada: " + LocalDateTime.now());
>         saldo = 0.0;
>     }
>     
>     public CuentaBancaria(String numero) {
>         this.numeroCuenta = numero;
>         historial.add("Número asignado: " + numero);
>     }
> }
> ```
> 
> **Cuándo usar:**
> 
> - ✅ Inicialización común a todos los constructores
> - ✅ Lógica de inicialización compleja (bucles, try-catch)
> - ✅ Inicializar colecciones o estructuras de datos
> - ❌ No usar para lógica simple (mejor en el constructor)

---

## ⚡ Bloques Estáticos

> [!success]- 🔷 Inicialización de Clase
> 
> **Sintaxis:**
> 
> ```java
> public class Configuracion {
>     private static Map<String, String> config;
>     
>     // Bloque estático
>     static {
>         config = new HashMap<>();
>         config.put("idioma", "es");
>         config.put("zona", "UTC-5");
>         System.out.println("Configuración cargada");
>     }
> }
> ```
> 
> **Características:**
> 
> - Se ejecuta **una sola vez** al cargar la clase
> - Antes de cualquier instancia
> - Ideal para inicializar atributos estáticos
> 
> **Ejemplo con validación:**
> 
> ```java
> public class BaseDatos {
>     private static Connection conexion;
>     private static final String URL = "jdbc:mysql://localhost/db";
>     
>     static {
>         try {
>             Class.forName("com.mysql.jdbc.Driver");
>             conexion = DriverManager.getConnection(URL);
>             System.out.println("✅ Conexión establecida");
>         } catch (Exception e) {
>             System.err.println("❌ Error de conexión: " + e);
>             throw new RuntimeException("No se pudo conectar a BD");
>         }
>     }
> }
> ```

---

## 📊 Orden de Ejecución Completo

> [!note]- 🔢 Secuencia de Inicialización
> 
> ```java
> public class Ejemplo {
>     private static int estatico = inicializarEstatico();
>     private int instancia = inicializarInstancia();
>     
>     static {
>         System.out.println("2. Bloque estático");
>     }
>     
>     {
>         System.out.println("4. Bloque de instancia");
>     }
>     
>     public Ejemplo() {
>         System.out.println("5. Constructor");
>     }
>     
>     private static int inicializarEstatico() {
>         System.out.println("1. Inicialización atributo estático");
>         return 10;
>     }
>     
>     private int inicializarInstancia() {
>         System.out.println("3. Inicialización atributo instancia");
>         return 20;
>     }
> }
> 
> // Salida al crear objeto:
> // 1. Inicialización atributo estático
> // 2. Bloque estático
> // 3. Inicialización atributo instancia
> // 4. Bloque de instancia
> // 5. Constructor
> ```

---

## ⚠️ Finalizadores (Deprecated)

> [!warning]- 🚫 Método finalize() - NO Usar
> 
> **Concepto:** Método llamado por el Garbage Collector antes de eliminar el objeto.
> 
> ```java
> // ❌ NO RECOMENDADO - Obsoleto desde Java 9
> public class RecursoAntiguo {
>     @Override
>     protected void finalize() throws Throwable {
>         try {
>             // Liberar recursos
>             System.out.println("Objeto siendo eliminado");
>         } finally {
>             super.finalize();
>         }
>     }
> }
> ```
> 
> **Problemas:**
> 
> - ❌ Ejecución impredecible (puede no ejecutarse nunca)
> - ❌ Impacto en rendimiento
> - ❌ Obsoleto desde Java 9
> 
> **✅ Alternativas modernas:**
> 
> **1. Try-with-resources:**
> 
> ```java
> public class Archivo implements AutoCloseable {
>     private FileWriter writer;
>     
>     public Archivo(String ruta) throws IOException {
>         writer = new FileWriter(ruta);
>     }
>     
>     @Override
>     public void close() throws IOException {
>         if (writer != null) {
>             writer.close();
>             System.out.println("Archivo cerrado");
>         }
>     }
> }
> 
> // Uso:
> try (Archivo archivo = new Archivo("datos.txt")) {
>     // Usar archivo
> } // close() se llama automáticamente
> ```
> 
> **2. Método close() manual:**
> 
> ```java
> public class Conexion {
>     private Socket socket;
>     
>     public void cerrar() {
>         if (socket != null && !socket.isClosed()) {
>             try {
>                 socket.close();
>             } catch (IOException e) {
>                 e.printStackTrace();
>             }
>         }
>     }
> }
> ```

---

## 🎯 Casos de Uso Comunes

> [!example]- 💼 Cuándo Usar Cada Tipo
> 
> **Bloques de instancia:**
> 
> ```java
> public class Juego {
>     private List<Jugador> jugadores;
>     private Tablero tablero;
>     
>     // Inicialización común a todos los constructores
>     {
>         jugadores = new ArrayList<>();
>         tablero = new Tablero(8, 8);
>         System.out.println("Juego inicializado");
>     }
>     
>     public Juego() { }
>     
>     public Juego(int numJugadores) {
>         for (int i = 0; i < numJugadores; i++) {
>             jugadores.add(new Jugador("Jugador " + (i + 1)));
>         }
>     }
> }
> ```
> 
> **Bloques estáticos:**
> 
> ```java
> public class Constantes {
>     public static final Map<String, Integer> CODIGOS_ERROR;
>     
>     static {
>         Map<String, Integer> temp = new HashMap<>();
>         temp.put("NOT_FOUND", 404);
>         temp.put("UNAUTHORIZED", 401);
>         temp.put("SERVER_ERROR", 500);
>         CODIGOS_ERROR = Collections.unmodifiableMap(temp);
>     }
> }
> ```

---

## ✅ Buenas Prácticas

> [!tip]- 🌟 Recomendaciones
> 
> **DO:**
> 
> - ✅ Usar bloques de instancia para inicialización común
> - ✅ Usar bloques estáticos para configuración única
> - ✅ Mantener bloques cortos y claros
> - ✅ Documentar bloques complejos
> 
> **DON'T:**
> 
> - ❌ No usar finalize() (obsoleto)
> - ❌ No poner lógica de negocio en bloques
> - ❌ No lanzar excepciones sin control
> - ❌ No abusar de bloques (preferir constructores cuando sea posible)

---

## 🔗 Resumen Rápido

|Tipo|Ejecución|Uso Principal|
|---|---|---|
|**Bloque instancia**|Cada objeto|Inicialización común|
|**Bloque estático**|Una vez (clase)|Config. estática|
|**finalize()**|❌ Obsoleto|NO USAR|
|**try-with-resources**|✅ Automático|Cerrar recursos|

---

**Tags:** #java #inicializadores #bloques-estaticos #finalize #poo #inicializacion #static