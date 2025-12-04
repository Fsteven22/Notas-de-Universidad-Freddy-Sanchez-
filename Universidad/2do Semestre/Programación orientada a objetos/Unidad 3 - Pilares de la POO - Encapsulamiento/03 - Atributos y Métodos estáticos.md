# 🔷 Atributos y Métodos Estáticos en Java

## 🎯 Introducción

> [!info]- 💡 ¿Qué es `static`? El modificador **`static`** es una palabra clave en Java que indica que un miembro (atributo o método) **pertenece a la clase** en lugar de pertenecer a una instancia específica (objeto) de la clase.
> 
> **Analogía:** La Biblioteca Municipal
> 
> - **Atributos de instancia:** Cada libro tiene su propio título, autor, ISBN → Cada libro es único
> - **Atributos estáticos:** La dirección de la biblioteca, el horario de atención, el reglamento → Son compartidos por todos los libros, pertenecen a la biblioteca misma
> 
> **Diferencia clave:**
> 
> ```java
> // INSTANCIA - Cada estudiante tiene su propio nombre
> Estudiante est1 = new Estudiante("Ana");
> Estudiante est2 = new Estudiante("Carlos");
> 
> // ESTÁTICO - Todos comparten el mismo contador
> System.out.println(Estudiante.totalEstudiantes); // 2
> ```
> 
> **Características principales:**
> 
> - 🏢 **Pertenece a la clase**, no al objeto
> - 🔄 **Compartido** por todas las instancias
> - 📍 **Una sola copia** en memoria
> - ⚡ **Accesible sin crear objetos**
> - 🎯 **Uso:** Contadores, constantes, utilidades, factories

---

## 📊 Atributos Estáticos (Variables de Clase)

### 🔍 Concepto Fundamental

> [!success]- 🏢 Variables Compartidas por Todas las Instancias
> 
> **Definición:** Un atributo estático es una variable que:
> 
> - Existe **una sola vez** en memoria
> - Es **compartida** por todos los objetos de la clase
> - Se accede usando el **nombre de la clase** (no el objeto)
> - Se inicializa **una sola vez** cuando se carga la clase
> 
> **Sintaxis:**
> 
> ```java
> public class MiClase {
>     // Atributo estático
>     private static tipoDato nombreVariable;
>     
>     // Común: static + final = CONSTANTE
>     public static final tipoDato CONSTANTE = valor;
> }
> ```
> 
> **Comparación visual:**
> 
> ```java
> public class Contador {
>     // INSTANCIA - Cada objeto tiene su propia copia
>     private int valorIndividual;
>     
>     // ESTÁTICO - Compartido por todos los objetos
>     private static int valorCompartido = 0;
>     
>     public Contador() {
>         valorIndividual++;      // Solo afecta a este objeto
>         valorCompartido++;      // Afecta a TODOS
>     }
> }
> 
> // USO:
> Contador c1 = new Contador();
> Contador c2 = new Contador();
> Contador c3 = new Contador();
> 
> // c1.valorIndividual = 1
> // c2.valorIndividual = 1  
> // c3.valorIndividual = 1
> // Contador.valorCompartido = 3 ← ¡Compartido!
> ```

### 1️⃣ Atributos Estáticos Básicos

> [!example]- 📝 Contador de Instancias
> 
> **Ejemplo clásico:** Contar cuántos objetos se han creado
> 
> ```java
> public class Estudiante {
>     // Atributos de instancia (cada objeto tiene los suyos)
>     private String nombre;
>     private int edad;
>     private double promedio;
>     
>     // Atributo estático (compartido por todos)
>     private static int totalEstudiantes = 0;
>     
>     // Constructor
>     public Estudiante(String nombre, int edad) {
>         this.nombre = nombre;
>         this.edad = edad;
>         totalEstudiantes++;  // Incrementa el contador compartido
>     }
>     
>     // Getter para atributo estático
>     public static int getTotalEstudiantes() {
>         return totalEstudiantes;
>     }
>     
>     // Getter para atributo de instancia
>     public String getNombre() {
>         return this.nombre;
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("Estudiante: " + nombre);
>         System.out.println("Edad: " + edad);
>         System.out.println("Total estudiantes creados: " + totalEstudiantes);
>     }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         // ✅ Acceso a estático sin crear objetos
>         System.out.println("Inicial: " + Estudiante.getTotalEstudiantes()); // 0
>         
>         // Crear objetos
>         Estudiante est1 = new Estudiante("Ana", 20);
>         System.out.println("Después de Ana: " + Estudiante.getTotalEstudiantes()); // 1
>         
>         Estudiante est2 = new Estudiante("Carlos", 22);
>         Estudiante est3 = new Estudiante("María", 19);
>         
>         // ✅ El contador es compartido
>         System.out.println("Total: " + Estudiante.getTotalEstudiantes()); // 3
>         
>         // ⚠️ También se puede acceder desde instancia (pero no recomendado)
>         System.out.println("Total: " + est1.getTotalEstudiantes()); // 3
>         
>         est1.mostrarInfo();
>         // Salida:
>         // Estudiante: Ana
>         // Edad: 20
>         // Total estudiantes creados: 3
>     }
> }
> ```
> 
> **Memoria - Visualización:**
> 
> ```
> [CLASE Estudiante]
> └── totalEstudiantes = 3  ← Una sola copia en memoria
> 
> [OBJETO est1]           [OBJETO est2]           [OBJETO est3]
> ├── nombre = "Ana"      ├── nombre = "Carlos"   ├── nombre = "María"
> ├── edad = 20           ├── edad = 22           ├── edad = 19
> └── promedio = 0.0      └── promedio = 0.0      └── promedio = 0.0
> ```

### 2️⃣ Constantes (static final)

> [!tip]- 🔒 Valores Inmutables Compartidos
> 
> **Concepto:** Combinar `static` + `final` crea **constantes**
> 
> - `static` → Compartido por todos
> - `final` → No se puede modificar
> - Convención: **MAYÚSCULAS_CON_GUION_BAJO**
> 
> **Ejemplos comunes:**
> 
> ```java
> public class Matematicas {
>     // Constantes matemáticas
>     public static final double PI = 3.141592653589793;
>     public static final double E = 2.718281828459045;
>     public static final double PHI = 1.618033988749895; // Proporción áurea
>     
>     // Constantes de conversión
>     public static final double METROS_A_PIES = 3.28084;
>     public static final double KM_A_MILLAS = 0.621371;
>     public static final int HORAS_DIA = 24;
>     public static final int DIAS_SEMANA = 7;
> }
> 
> // USO:
> double radio = 5.0;
> double area = Matematicas.PI * radio * radio;
> System.out.println("Área: " + area); // 78.539...
> 
> double distanciaKm = 10.0;
> double distanciaMillas = distanciaKm * Matematicas.KM_A_MILLAS;
> ```
> 
> **Ejemplo: Configuración de aplicación**
> 
> ```java
> public class Configuracion {
>     // Configuración de base de datos
>     public static final String DB_URL = "jdbc:mysql://localhost:3306/midb";
>     public static final String DB_USER = "admin";
>     public static final int DB_TIMEOUT = 30;
>     
>     // Límites de la aplicación
>     public static final int MAX_INTENTOS_LOGIN = 3;
>     public static final int LONGITUD_MIN_PASSWORD = 8;
>     public static final int TIMEOUT_SESION = 1800; // segundos
>     
>     // Mensajes
>     public static final String MENSAJE_BIENVENIDA = "¡Bienvenido al sistema!";
>     public static final String MENSAJE_ERROR = "Ha ocurrido un error";
>     
>     // Constructor privado para evitar instanciación
>     private Configuracion() {
>         throw new UnsupportedOperationException("Clase de utilidad");
>     }
> }
> 
> // USO:
> if (password.length() < Configuracion.LONGITUD_MIN_PASSWORD) {
>     System.out.println("Contraseña muy corta");
> }
> ```
> 
> **Ventajas de usar constantes:**
> 
> - ✅ **Legibilidad:** Nombres descriptivos vs números "mágicos"
> - ✅ **Mantenimiento:** Cambiar valor en un solo lugar
> - ✅ **Seguridad:** No se pueden modificar accidentalmente
> - ✅ **Documentación:** El nombre explica el propósito
> 
> ```java
> // ❌ MAL - Números "mágicos"
> if (edad >= 18 && saldo > 500 && intentos < 3) { ... }
> 
> // ✅ BIEN - Constantes descriptivas
> if (edad >= Constantes.EDAD_MAYORIA && 
>     saldo > Constantes.SALDO_MINIMO && 
>     intentos < Constantes.MAX_INTENTOS) { ... }
> ```

### 3️⃣ Variables Estáticas Mutables

> [!warning]- ⚠️ Uso con Precaución
> 
> **Concepto:** Variables estáticas que SÍ se pueden modificar (sin `final`)
> 
> **Casos de uso válidos:**
> 
> ```java
> public class SistemaNotificaciones {
>     // Configuración global que puede cambiar
>     private static boolean notificacionesHabilitadas = true;
>     private static int nivelVolumen = 50; // 0-100
>     
>     // Contador de notificaciones
>     private static int totalNotificacionesEnviadas = 0;
>     
>     // Métodos para modificar configuración
>     public static void habilitarNotificaciones() {
>         notificacionesHabilitadas = true;
>     }
>     
>     public static void deshabilitarNotificaciones() {
>         notificacionesHabilitadas = false;
>     }
>     
>     public static void setVolumen(int volumen) {
>         if (volumen >= 0 && volumen <= 100) {
>             nivelVolumen = volumen;
>         }
>     }
>     
>     public static void enviarNotificacion(String mensaje) {
>         if (notificacionesHabilitadas) {
>             System.out.println("🔔 [Vol: " + nivelVolumen + "%] " + mensaje);
>             totalNotificacionesEnviadas++;
>         }
>     }
>     
>     public static int getTotalNotificaciones() {
>         return totalNotificacionesEnviadas;
>     }
> }
> 
> // USO:
> SistemaNotificaciones.enviarNotificacion("Nueva tarea");
> SistemaNotificaciones.setVolumen(80);
> SistemaNotificaciones.enviarNotificacion("Mensaje importante");
> 
> SistemaNotificaciones.deshabilitarNotificaciones();
> SistemaNotificaciones.enviarNotificacion("No se mostrará");
> 
> System.out.println("Total enviadas: " + 
>     SistemaNotificaciones.getTotalNotificaciones()); // 2
> ```
> 
> **⚠️ Problemas potenciales:**
> 
> ```java
> public class CacheProblematico {
>     // ❌ RIESGO - Cualquiera puede modificar directamente
>     public static List<String> cache = new ArrayList<>();
>     
>     // ✅ MEJOR - Encapsulado
>     private static List<String> cache = new ArrayList<>();
>     
>     public static void agregarACache(String dato) {
>         if (dato != null && !cache.contains(dato)) {
>             cache.add(dato);
>         }
>     }
>     
>     public static List<String> obtenerCache() {
>         // Retornar copia para proteger el original
>         return new ArrayList<>(cache);
>     }
>     
>     public static void limpiarCache() {
>         cache.clear();
>     }
> }
> ```
> 
> **Reglas de oro:**
> 
> - 🔒 Siempre usar `private` con variables estáticas mutables
> - ✅ Proporcionar métodos de acceso controlado
> - 🚫 Evitar exponer colecciones mutables directamente
> - ⚡ Considerar thread-safety en aplicaciones concurrentes

---

## ⚙️ Métodos Estáticos (Métodos de Clase)

### 🔍 Concepto Fundamental

> [!info]- 🎯 Métodos que No Necesitan Objetos
> 
> **Definición:** Un método estático es una función que:
> 
> - Pertenece a la **clase**, no a instancias
> - Se puede llamar **sin crear objetos**
> - **NO puede** acceder a atributos de instancia directamente
> - **SÍ puede** acceder a otros miembros estáticos
> 
> **Sintaxis:**
> 
> ```java
> public class MiClase {
>     public static tipoRetorno nombreMetodo(parametros) {
>         // Código del método
>     }
> }
> 
> // Llamada: NombreClase.nombreMetodo()
> ```
> 
> **Restricciones importantes:**
> 
> ```java
> public class Ejemplo {
>     private int instancia = 10;
>     private static int estatico = 20;
>     
>     public static void metodoEstatico() {
>         // ❌ ERROR - No puede acceder a miembros de instancia
>         // System.out.println(instancia);
>         // this.instancia = 5;
>         
>         // ✅ CORRECTO - Sí puede acceder a miembros estáticos
>         System.out.println(estatico);
>         estatico = 30;
>         
>         // ✅ CORRECTO - Puede llamar otros métodos estáticos
>         otroMetodoEstatico();
>     }
>     
>     public void metodoInstancia() {
>         // ✅ CORRECTO - Métodos de instancia pueden acceder a todo
>         System.out.println(instancia);
>         System.out.println(estatico);
>         metodoEstatico();
>     }
>     
>     private static void otroMetodoEstatico() {
>         System.out.println("Otro método estático");
>     }
> }
> ```

### 1️⃣ Métodos de Utilidad (Utility Methods)

> [!example]- 🛠️ Funciones Auxiliares Sin Estado
> 
> **Concepto:** Métodos que realizan operaciones **sin necesitar** datos del objeto
> 
> **Ejemplo: Clase Matemáticas**
> 
> ```java
> public class Matematicas {
>     // Constructor privado - No se pueden crear instancias
>     private Matematicas() {
>         throw new UnsupportedOperationException("Clase de utilidad");
>     }
>     
>     // Operaciones matemáticas básicas
>     public static int sumar(int a, int b) {
>         return a + b;
>     }
>     
>     public static double dividir(double a, double b) {
>         if (b == 0) {
>             throw new ArithmeticException("División por cero");
>         }
>         return a / b;
>     }
>     
>     public static int factorial(int n) {
>         if (n < 0) {
>             throw new IllegalArgumentException("n debe ser no negativo");
>         }
>         if (n == 0 || n == 1) return 1;
>         
>         int resultado = 1;
>         for (int i = 2; i <= n; i++) {
>             resultado *= i;
>         }
>         return resultado;
>     }
>     
>     public static boolean esPrimo(int n) {
>         if (n <= 1) return false;
>         if (n <= 3) return true;
>         if (n % 2 == 0 || n % 3 == 0) return false;
>         
>         for (int i = 5; i * i <= n; i += 6) {
>             if (n % i == 0 || n % (i + 2) == 0) {
>                 return false;
>             }
>         }
>         return true;
>     }
>     
>     public static double calcularPromedio(double[] numeros) {
>         if (numeros == null || numeros.length == 0) {
>             throw new IllegalArgumentException("Array vacío o null");
>         }
>         
>         double suma = 0;
>         for (double num : numeros) {
>             suma += num;
>         }
>         return suma / numeros.length;
>     }
>     
>     public static int maximoComunDivisor(int a, int b) {
>         a = Math.abs(a);
>         b = Math.abs(b);
>         
>         while (b != 0) {
>             int temp = b;
>             b = a % b;
>             a = temp;
>         }
>         return a;
>     }
> }
> 
> // USO - No se necesitan objetos
> int suma = Matematicas.sumar(5, 3);
> int fact = Matematicas.factorial(5);  // 120
> boolean primo = Matematicas.esPrimo(17);  // true
> 
> double[] notas = {8.5, 7.0, 9.5, 6.5};
> double promedio = Matematicas.calcularPromedio(notas);
> 
> int mcd = Matematicas.maximoComunDivisor(48, 18);  // 6
> ```
> 
> **Ejemplo: Validaciones**
> 
> ```java
> public class Validador {
>     private Validador() {}
>     
>     // Validación de email
>     public static boolean esEmailValido(String email) {
>         if (email == null || email.isEmpty()) {
>             return false;
>         }
>         return email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$");
>     }
>     
>     // Validación de teléfono
>     public static boolean esTelefonoValido(String telefono) {
>         if (telefono == null) return false;
>         return telefono.matches("\\d{10}");
>     }
>     
>     // Validación de cédula (Ecuador - ejemplo simplificado)
>     public static boolean esCedulaValida(String cedula) {
>         if (cedula == null || cedula.length() != 10) {
>             return false;
>         }
>         
>         try {
>             int provincia = Integer.parseInt(cedula.substring(0, 2));
>             if (provincia < 1 || provincia > 24) {
>                 return false;
>             }
>             
>             // Algoritmo del módulo 10
>             int[] coeficientes = {2, 1, 2, 1, 2, 1, 2, 1, 2};
>             int suma = 0;
>             
>             for (int i = 0; i < 9; i++) {
>                 int valor = Character.getNumericValue(cedula.charAt(i)) * coeficientes[i];
>                 if (valor > 9) valor -= 9;
>                 suma += valor;
>             }
>             
>             int verificador = (10 - (suma % 10)) % 10;
>             int ultimoDigito = Character.getNumericValue(cedula.charAt(9));
>             
>             return verificador == ultimoDigito;
>         } catch (NumberFormatException e) {
>             return false;
>         }
>     }
>     
>     // Validación de contraseña fuerte
>     public static boolean esPasswordSegura(String password) {
>         if (password == null || password.length() < 8) {
>             return false;
>         }
>         
>         boolean tieneMayuscula = password.matches(".*[A-Z].*");
>         boolean tieneMinuscula = password.matches(".*[a-z].*");
>         boolean tieneNumero = password.matches(".*\\d.*");
>         boolean tieneEspecial = password.matches(".*[!@#$%^&*()_+\\-=\\[\\]{};':\"\\\\|,.<>/?].*");
>         
>         return tieneMayuscula && tieneMinuscula && tieneNumero && tieneEspecial;
>     }
>     
>     // Validación de rango
>     public static boolean estaEnRango(int valor, int min, int max) {
>         return valor >= min && valor <= max;
>     }
> }
> 
> // USO:
> boolean emailOk = Validador.esEmailValido("usuario@ejemplo.com");
> boolean cedulaOk = Validador.esCedulaValida("1234567890");
> boolean passOk = Validador.esPasswordSegura("MiPass123!");
> ```

### 2️⃣ Métodos Factory (Constructores Alternativos)

> [!tip]- 🏭 Creación Controlada de Objetos
> 
> **Concepto:** Métodos estáticos que crean y retornan instancias de la clase
> 
> **Ventajas sobre constructores:**
> 
> - ✅ Pueden tener **nombres descriptivos**
> - ✅ Pueden **reutilizar** instancias (caché)
> - ✅ Pueden retornar **subclases**
> - ✅ Pueden realizar **validaciones complejas**
> 
> **Ejemplo: Clase Fecha**
> 
> ```java
> public class Fecha {
>     private final int dia;
>     private final int mes;
>     private final int anio;
>     
>     // Constructor privado - Fuerza uso de factory methods
>     private Fecha(int dia, int mes, int anio) {
>         this.dia = dia;
>         this.mes = mes;
>         this.anio = anio;
>     }
>     
>     // Factory method - Fecha desde valores
>     public static Fecha crear(int dia, int mes, int anio) {
>         if (!esValida(dia, mes, anio)) {
>             throw new IllegalArgumentException("Fecha inválida");
>         }
>         return new Fecha(dia, mes, anio);
>     }
>     
>     // Factory method - Fecha de hoy
>     public static Fecha hoy() {
>         java.time.LocalDate ahora = java.time.LocalDate.now();
>         return new Fecha(ahora.getDayOfMonth(), 
>                         ahora.getMonthValue(), 
>                         ahora.getYear());
>     }
>     
>     // Factory method - Fecha desde String
>     public static Fecha desdeString(String fecha) {
>         // Formato esperado: "DD/MM/YYYY"
>         String[] partes = fecha.split("/");
>         if (partes.length != 3) {
>             throw new IllegalArgumentException("Formato inválido");
>         }
>         
>         int dia = Integer.parseInt(partes[0]);
>         int mes = Integer.parseInt(partes[1]);
>         int anio = Integer.parseInt(partes[2]);
>         
>         return crear(dia, mes, anio);
>     }
>     
>     // Factory method - Primer día del mes
>     public static Fecha primerDiaMes(int mes, int anio) {
>         return crear(1, mes, anio);
>     }
>     
>     // Factory method - Último día del mes
>     public static Fecha ultimoDiaMes(int mes, int anio) {
>         int ultimoDia = diasEnMes(mes, anio);
>         return crear(ultimoDia, mes, anio);
>     }
>     
>     // Método auxiliar estático
>     private static boolean esValida(int dia, int mes, int anio) {
>         if (mes < 1 || mes > 12) return false;
>         if (dia < 1 || dia > diasEnMes(mes, anio)) return false;
>         return anio > 0;
>     }
>     
>     private static int diasEnMes(int mes, int anio) {
>         switch (mes) {
>             case 4: case 6: case 9: case 11:
>                 return 30;
>             case 2:
>                 return esBisiesto(anio) ? 29 : 28;
>             default:
>                 return 31;
>         }
>     }
>     
>     private static boolean esBisiesto(int anio) {
>         return (anio % 4 == 0 && anio % 100 != 0) || (anio % 400 == 0);
>     }
>     
>     @Override
>     public String toString() {
>         return String.format("%02d/%02d/%04d", dia, mes, anio);
>     }
> }
> 
> // USO - Nombres descriptivos y claros
> Fecha f1 = Fecha.crear(15, 10, 2024);
> Fecha f2 = Fecha.hoy();
> Fecha f3 = Fecha.desdeString("25/12/2024");
> Fecha f4 = Fecha.primerDiaMes(1, 2025);
> Fecha f5 = Fecha.ultimoDiaMes(2, 2024);  // 29/02/2024
> ```
> 
> **Ejemplo: Clase Empleado con Factory Methods**
> 
> ```java
> public class Empleado {
>     private String nombre;
>     private String email;
>     private double salario;
>     private String tipo;
>     
>     private Empleado(String nombre, String email, double salario, String tipo) {
>         this.nombre = nombre;
>         this.email = email;
>         this.salario = salario;
>         this.tipo = tipo;
>     }
>     
>     // Factory para empleado temporal
>     public static Empleado temporal(String nombre, String email) {
>         return new Empleado(nombre, email, 500.0, "Temporal");
>     }
>     
>     // Factory para empleado permanente
>     public static Empleado permanente(String nombre, String email, double salario) {
>         if (salario < 450.0) {
>             throw new IllegalArgumentException("Salario debe ser >= SBU");
>         }
>         return new Empleado(nombre, email, salario, "Permanente");
>     }
>     
>     // Factory para gerente
>     public static Empleado gerente(String nombre, String email) {
>         return new Empleado(nombre, email, 2500.0, "Gerente");
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("=== " + tipo + " ===");
>         System.out.println("Nombre: " + nombre);
>         System.out.println("Email: " + email);
>         System.out.println("Salario: $" + salario);
>     }
> }
> 
> // USO - Muy expresivo y claro
> Empleado e1 = Empleado.temporal("Juan Pérez", "juan@empresa.com");
> Empleado e2 = Empleado.permanente("Ana López", "ana@empresa.com", 1200.0);
> Empleado e3 = Empleado.gerente("Carlos Silva", "carlos@empresa.com");
> ```

### 3️⃣ Método main() - El Punto de Entrada

> [!success]- 🚀 Iniciando la Aplicación
> 
> **Concepto:** El método `main` es el **punto de entrada** de toda aplicación Java
> 
> **Firma obligatoria:**
> 
> ```java
> public static void main(String[] args) {
>     // Código de inicio
> }
> ```
> 
> **¿Por qué es estático?**
> 
> - La JVM debe poder **llamarlo sin crear objetos**
> - Es el **primer método** que se ejecuta
> - **No existe ningún objeto** cuando se inicia el programa
> 
> **Ejemplo completo:**
> 
> ```java
> public class Aplicacion {
>     // Atributos estáticos para configuración
>     private static String nombreApp = "Mi Aplicación";
>     private static String version = "1.0.0";
>     private static boolean modoDebug = false;
>     
>     public static void main(String[] args) {
>         // 1. Mostrar banner
>         mostrarBanner();
>         
>         // 2. Procesar argumentos
>         procesarArgumentos(args);
>         
>         // 3. Inicializar sistema
>         if (!inicializarSistema()) {
>             System.err.println("❌ Error al inicializar");
>             System.exit(1);
>         }
>         
>         // 4. Ejecutar lógica principal
>         ejecutarAplicacion();
>         
>         // 5. Finalizar
>         System.out.println("\n✅ Aplicación finalizada correctamente");
>     }
>     
>     private static void mostrarBanner() {
>         System.out.println("╔══════════════════════════════╗");
>         System.out.println("║  " + nombreApp + " v" + version + "  ║");
>         System.out.println("╚══════════════════════════════
> 		System.out.println("╚══════════════════════════════╝\n");
>     
>     private static void procesarArgumentos(String[] args) {
>         System.out.println("📋 Argumentos recibidos: " + args.length);
>         
>         for (int i = 0; i < args.length; i++) {
>             System.out.println("  arg[" + i + "]: " + args[i]);
>             
>             // Activar modo debug si se pasa --debug
>             if (args[i].equals("--debug")) {
>                 modoDebug = true;
>                 System.out.println("🐛 Modo debug activado");
>             }
>         }
>     }
>     
>     private static boolean inicializarSistema() {
>         System.out.println("\n⚙️  Inicializando sistema...");
>         
>         try {
>             // Simular inicialización
>             Thread.sleep(500);
>             System.out.println("  ✓ Base de datos conectada");
>             
>             Thread.sleep(300);
>             System.out.println("  ✓ Archivos de configuración cargados");
>             
>             Thread.sleep(200);
>             System.out.println("  ✓ Sistema listo");
>             
>             return true;
>         } catch (InterruptedException e) {
>             return false;
>         }
>     }
>     
>     private static void ejecutarAplicacion() {
>         System.out.println("\n🚀 Ejecutando aplicación principal...\n");
>         
>         // Aquí iría la lógica principal
>         // Ejemplo: Crear objetos y trabajar con ellos
>         Usuario usuario = new Usuario("admin");
>         usuario.mostrarInfo();
>         
>         if (modoDebug) {
>             System.out.println("\n[DEBUG] Estado del sistema:");
>             System.out.println("  - Memoria usada: " + obtenerMemoriaUsada() + " MB");
>         }
>     }
>     
>     private static long obtenerMemoriaUsada() {
>         Runtime runtime = Runtime.getRuntime();
>         return (runtime.totalMemory() - runtime.freeMemory()) / 1024 / 1024;
>     }
> }
> 
> // Clase auxiliar
> class Usuario {
>     private String nombre;
>     
>     public Usuario(String nombre) {
>         this.nombre = nombre;
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("👤 Usuario: " + nombre);
>     }
> }
> ```
> 
> **Ejemplo: Procesamiento de argumentos avanzado**
> 
> ```java
> public class ProcesadorArchivos {
>     private static String archivoEntrada;
>     private static String archivoSalida;
>     private static boolean verbose = false;
>     
>     public static void main(String[] args) {
>         if (args.length == 0) {
>             mostrarAyuda();
>             return;
>         }
>         
>         // Procesar argumentos
>         for (int i = 0; i < args.length; i++) {
>             switch (args[i]) {
>                 case "-i":
>                 case "--input":
>                     if (i + 1 < args.length) {
>                         archivoEntrada = args[++i];
>                     }
>                     break;
>                     
>                 case "-o":
>                 case "--output":
>                     if (i + 1 < args.length) {
>                         archivoSalida = args[++i];
>                     }
>                     break;
>                     
>                 case "-v":
>                 case "--verbose":
>                     verbose = true;
>                     break;
>                     
>                 case "-h":
>                 case "--help":
>                     mostrarAyuda();
>                     return;
>                     
>                 default:
>                     System.out.println("⚠️  Argumento desconocido: " + args[i]);
>             }
>         }
>         
>         // Validar argumentos requeridos
>         if (archivoEntrada == null) {
>             System.err.println("❌ Error: Archivo de entrada requerido");
>             mostrarAyuda();
>             System.exit(1);
>         }
>         
>         // Ejecutar procesamiento
>         procesarArchivo();
>     }
>     
>     private static void mostrarAyuda() {
>         System.out.println("Uso: java ProcesadorArchivos [opciones]");
>         System.out.println("\nOpciones:");
>         System.out.println("  -i, --input <archivo>    Archivo de entrada (requerido)");
>         System.out.println("  -o, --output <archivo>   Archivo de salida");
>         System.out.println("  -v, --verbose            Modo detallado");
>         System.out.println("  -h, --help               Mostrar esta ayuda");
>     }
>     
>     private static void procesarArchivo() {
>         if (verbose) {
>             System.out.println("📂 Procesando: " + archivoEntrada);
>         }
>         
>         // Lógica de procesamiento...
>         System.out.println("✅ Procesamiento completado");
>         
>         if (archivoSalida != null && verbose) {
>             System.out.println("💾 Guardado en: " + archivoSalida);
>         }
>     }
> }
> 
> // Ejecución desde terminal:
> // java ProcesadorArchivos -i datos.txt -o resultado.txt -v
> ```

---

## 🔄 Bloques Estáticos de Inicialización

> [!info]- 🎬 Código que se Ejecuta al Cargar la Clase
> 
> **Concepto:** Bloques de código que se ejecutan **una sola vez** cuando la clase se carga en memoria
> 
> **Sintaxis:**
> 
> ```java
> public class MiClase {
>     // Atributo estático
>     private static int valor;
>     
>     // Bloque estático
>     static {
>         // Código de inicialización
>         valor = 100;
>         System.out.println("Clase cargada");
>     }
> }
> ```
> 
> **Orden de ejecución:**
> 
> ```java
> public class OrdenInicializacion {
>     // 1. Inicialización directa de atributos estáticos
>     private static int a = inicializarA();
>     
>     // 2. Bloque estático (en orden de aparición)
>     static {
>         System.out.println("Bloque estático 1");
>         b = 20;
>     }
>     
>     private static int b;
>     
>     // 3. Otro bloque estático
>     static {
>         System.out.println("Bloque estático 2");
>         c = a + b;
>     }
>     
>     private static int c;
>     
>     private static int inicializarA() {
>         System.out.println("Inicializando A");
>         return 10;
>     }
>     
>     public static void main(String[] args) {
>         System.out.println("Método main");
>         System.out.println("a=" + a + ", b=" + b + ", c=" + c);
>     }
> }
> 
> // SALIDA:
> // Inicializando A
> // Bloque estático 1
> // Bloque estático 2
> // Método main
> // a=10, b=20, c=30
> ```
> 
> **Ejemplo práctico: Cargar configuración**
> 
> ```java
> public class ConfiguracionDB {
>     private static String url;
>     private static String usuario;
>     private static String password;
>     private static int maxConexiones;
>     
>     // Bloque estático para cargar configuración
>     static {
>         System.out.println("🔧 Cargando configuración de base de datos...");
>         
>         try {
>             // Simular lectura de archivo de configuración
>             cargarDesdeArchivo();
>             
>             // Validar configuración
>             if (url == null || usuario == null) {
>                 throw new IllegalStateException("Configuración incompleta");
>             }
>             
>             System.out.println("✅ Configuración cargada exitosamente");
>             
>         } catch (Exception e) {
>             System.err.println("❌ Error al cargar configuración: " + e.getMessage());
>             // Valores por defecto
>             url = "jdbc:mysql://localhost:3306/default";
>             usuario = "root";
>             password = "";
>             maxConexiones = 10;
>         }
>     }
>     
>     private static void cargarDesdeArchivo() {
>         // Simular lectura de config.properties
>         url = "jdbc:mysql://localhost:3306/midb";
>         usuario = "admin";
>         password = "secreto";
>         maxConexiones = 50;
>     }
>     
>     // Getters
>     public static String getUrl() {
>         return url;
>     }
>     
>     public static String getUsuario() {
>         return usuario;
>     }
>     
>     public static int getMaxConexiones() {
>         return maxConexiones;
>     }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         // Al hacer la primera referencia a la clase, se ejecuta el bloque estático
>         String url = ConfiguracionDB.getUrl();
>         System.out.println("Conectando a: " + url);
>     }
> }
> ```
> 
> **Ejemplo: Inicialización de colecciones estáticas**
> 
> ```java
> public class DiasLaborables {
>     // Mapa de días laborables por país
>     private static final Map<String, Set<String>> DIAS_LABORABLES;
>     
>     // Inicialización en bloque estático
>     static {
>         DIAS_LABORABLES = new HashMap<>();
>         
>         // Ecuador
>         Set<String> diasEC = new HashSet<>();
>         diasEC.add("LUNES");
>         diasEC.add("MARTES");
>         diasEC.add("MIERCOLES");
>         diasEC.add("JUEVES");
>         diasEC.add("VIERNES");
>         DIAS_LABORABLES.put("EC", diasEC);
>         
>         // Arabia Saudita (Domingo-Jueves)
>         Set<String> diasSA = new HashSet<>();
>         diasSA.add("DOMINGO");
>         diasSA.add("LUNES");
>         diasSA.add("MARTES");
>         diasSA.add("MIERCOLES");
>         diasSA.add("JUEVES");
>         DIAS_LABORABLES.put("SA", diasSA);
>         
>         System.out.println("📅 Calendario de días laborables cargado");
>     }
>     
>     public static boolean esLaborable(String pais, String dia) {
>         Set<String> dias = DIAS_LABORABLES.get(pais);
>         return dias != null && dias.contains(dia.toUpperCase());
>     }
>     
>     public static Set<String> obtenerDiasLaborables(String pais) {
>         Set<String> dias = DIAS_LABORABLES.get(pais);
>         return dias != null ? new HashSet<>(dias) : new HashSet<>();
>     }
> }
> ```

---

## 📊 Static vs Instancia: Comparación Completa

> [!example]- ⚖️ Diferencias Fundamentales
> 
> **Tabla comparativa:**
> 
> |Característica|Miembro Estático|Miembro de Instancia|
> |---|---|---|
> |**Pertenece a**|La clase|Cada objeto|
> |**Copias en memoria**|Una sola|Una por objeto|
> |**Acceso**|`Clase.miembro`|`objeto.miembro`|
> |**Requiere objeto**|No|Sí|
> |**Inicialización**|Al cargar la clase|Al crear objeto|
> |**Uso común**|Utilidades, constantes, contadores|Estado específico del objeto|
> |**Palabra clave `this`**|❌ No disponible|✅ Disponible|
> 
> **Ejemplo completo que ilustra las diferencias:**
> 
> ```java
> public class Producto {
>     // ============================================
>     // ATRIBUTOS ESTÁTICOS (Compartidos)
>     // ============================================
>     private static int totalProductosCreados = 0;
>     private static final double IVA = 0.12;
>     private static String nombreTienda = "Mi Tienda";
>     private static double descuentoGlobal = 0.0;
>     
>     // ============================================
>     // ATRIBUTOS DE INSTANCIA (Únicos por objeto)
>     // ============================================
>     private String codigo;
>     private String nombre;
>     private double precioBase;
>     private int stock;
>     private boolean activo;
>     
>     // ============================================
>     // BLOQUE ESTÁTICO
>     // ============================================
>     static {
>         System.out.println("🏪 Clase Producto cargada");
>         System.out.println("   Tienda: " + nombreTienda);
>         System.out.println("   IVA: " + (IVA * 100) + "%");
>     }
>     
>     // ============================================
>     // CONSTRUCTOR (inicializa atributos de instancia)
>     // ============================================
>     public Producto(String codigo, String nombre, double precioBase, int stock) {
>         this.codigo = codigo;
>         this.nombre = nombre;
>         this.precioBase = precioBase;
>         this.stock = stock;
>         this.activo = true;
>         
>         // Incrementa contador estático
>         totalProductosCreados++;
>         
>         System.out.println("✅ Producto #" + totalProductosCreados + " creado: " + nombre);
>     }
>     
>     // ============================================
>     // MÉTODOS ESTÁTICOS
>     // ============================================
>     
>     // Puede acceder SOLO a miembros estáticos
>     public static void aplicarDescuentoGlobal(double descuento) {
>         if (descuento >= 0 && descuento <= 100) {
>             descuentoGlobal = descuento;
>             System.out.println("🎉 Descuento global aplicado: " + descuento + "%");
>         }
>     }
>     
>     public static int getTotalProductos() {
>         return totalProductosCreados;
>     }
>     
>     public static void cambiarNombreTienda(String nuevoNombre) {
>         nombreTienda = nuevoNombre;
>         System.out.println("🏪 Tienda renombrada a: " + nuevoNombre);
>     }
>     
>     public static double calcularIVA(double monto) {
>         return monto * IVA;
>     }
>     
>     // ❌ ERROR: Método estático NO puede acceder a this
>     public static void metodoErroneoPorThis() {
>         // System.out.println(this.nombre); // ¡COMPILACIÓN FALLA!
>         // System.out.println(nombre);      // ¡COMPILACIÓN FALLA!
>     }
>     
>     // ============================================
>     // MÉTODOS DE INSTANCIA
>     // ============================================
>     
>     // Puede acceder a miembros estáticos Y de instancia
>     public double calcularPrecioFinal() {
>         double precioConIVA = precioBase + (precioBase * IVA);  // ✅ Accede a static
>         double descuento = precioConIVA * (descuentoGlobal / 100);  // ✅ Accede a static
>         return precioConIVA - descuento;
>     }
>     
>     public void vender(int cantidad) {
>         if (cantidad <= 0) {
>             System.out.println("❌ Cantidad inválida");
>             return;
>         }
>         
>         if (cantidad > this.stock) {  // ✅ Usa this
>             System.out.println("❌ Stock insuficiente para " + this.nombre);
>             return;
>         }
>         
>         this.stock -= cantidad;  // ✅ Modifica atributo de instancia
>         System.out.println("✅ Vendidos " + cantidad + " de " + this.nombre);
>         System.out.println("   Stock restante: " + this.stock);
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("\n━━━ INFORMACIÓN DEL PRODUCTO ━━━");
>         System.out.println("Tienda: " + nombreTienda);  // ✅ Accede a static
>         System.out.println("Código: " + this.codigo);
>         System.out.println("Nombre: " + this.nombre);
>         System.out.println("Precio base: $" + this.precioBase);
>         System.out.println("Precio final: $" + String.format("%.2f", calcularPrecioFinal()));
>         System.out.println("Stock: " + this.stock);
>         System.out.println("Estado: " + (this.activo ? "Activo" : "Inactivo"));
>         System.out.println("Descuento global: " + descuentoGlobal + "%");  // ✅ Accede a static
>         System.out.println("Total productos en sistema: " + totalProductosCreados);  // ✅ Accede a static
>     }
>     
>     // Getters y Setters de instancia
>     public String getNombre() {
>         return this.nombre;
>     }
>     
>     public int getStock() {
>         return this.stock;
>     }
> }
> 
> // ============================================
> // PROGRAMA DE PRUEBA
> // ============================================
> public class TestProducto {
>     public static void main(String[] args) {
>         System.out.println("╔═══════════════════════════════════╗");
>         System.out.println("║  DEMO: STATIC VS INSTANCIA        ║");
>         System.out.println("╚═══════════════════════════════════╝\n");
>         
>         // ✅ Acceso a método estático SIN crear objetos
>         System.out.println("Total productos iniciales: " + Producto.getTotalProductos());
>         
>         // Aplicar descuento global (afecta a TODOS los productos)
>         Producto.aplicarDescuentoGlobal(10.0);
>         
>         System.out.println("\n--- CREANDO PRODUCTOS ---");
>         
>         // Crear productos (cada uno es independiente)
>         Producto p1 = new Producto("P001", "Laptop", 800.0, 10);
>         Producto p2 = new Producto("P002", "Mouse", 15.0, 50);
>         Producto p3 = new Producto("P003", "Teclado", 45.0, 30);
>         
>         System.out.println("\n--- INFORMACIÓN INDIVIDUAL ---");
>         
>         // Cada producto tiene sus propios datos
>         p1.mostrarInfo();
>         p2.mostrarInfo();
>         
>         System.out.println("\n--- OPERACIONES ---");
>         
>         // Vender (modifica solo el producto específico)
>         p1.vender(2);
>         p2.vender(5);
>         
>         // Cambiar nombre de tienda (afecta a TODOS)
>         System.out.println("\n--- CAMBIO GLOBAL ---");
>         Producto.cambiarNombreTienda("SuperTech Store");
>         
>         System.out.println("\n--- DESPUÉS DEL CAMBIO ---");
>         p1.mostrarInfo();  // Muestra nuevo nombre de tienda
>         p3.mostrarInfo();  // También muestra nuevo nombre
>         
>         System.out.println("\n--- RESUMEN FINAL ---");
>         System.out.println("Total productos creados: " + Producto.getTotalProductos());
>         System.out.println("Stock Laptop: " + p1.getStock());  // 8 (vendimos 2)
>         System.out.println("Stock Mouse: " + p2.getStock());   // 45 (vendimos 5)
>         System.out.println("Stock Teclado: " + p3.getStock()); // 30 (sin cambios)
>     }
> }
> ```
> 
> **Visualización de memoria:**
> 
> ```
> ┌─────────────────────────────────────────┐
> │         ÁREA ESTÁTICA (Clase)           │
> ├─────────────────────────────────────────┤
> │ totalProductosCreados = 3               │
> │ IVA = 0.12  (final)                     │
> │ nombreTienda = "SuperTech Store"        │
> │ descuentoGlobal = 10.0                  │
> └─────────────────────────────────────────┘
>                    ↑
>         Compartido por todos
>                    ↓
> ┌─────────────┐  ┌─────────────┐  ┌─────────────┐
> │  Objeto p1  │  │  Objeto p2  │  │  Objeto p3  │
> ├─────────────┤  ├─────────────┤  ├─────────────┤
> │codigo="P001"│  │codigo="P002"│  │codigo="P003"│
> │nombre="..." │  │nombre="..." │  │nombre="..." │
> │precio=800.0 │  │precio=15.0  │  │precio=45.0  │
> │stock=8      │  │stock=45     │  │stock=30     │
> │activo=true  │  │activo=true  │  │activo=true  │
> └─────────────┘  └─────────────┘  └─────────────┘
>    Heap             Heap             Heap
> ```

---

## 🎯 Casos de Uso Comunes

> [!tip]- 💼 Cuándo Usar Static
> 
> **1. Constantes globales:**
> 
> ```java
> public class Constantes {
>     public static final double PI = 3.141592653589793;
>     public static final int DIAS_SEMANA = 7;
>     public static final String VERSION = "1.0.0";
> }
> ```
> 
> **2. Contadores globales:**
> 
> ```java
> public class Transaccion {
>     private static long contadorTransacciones = 0;
>     private final long id;
>     
>     public Transaccion() {
>         this.id = ++contadorTransacciones;
>     }
> }
> ```
> 
> **3. Métodos de utilidad:**
> 
> ```java
> public class StringUtils {
>     private StringUtils() {} // No instanciable
>     
>     public static boolean esVacio(String str) {
>         return str == null || str.trim().isEmpty();
>     }
>     
>     public static String capitalizar(String str) {
>         if (esVacio(str)) return str;
>         return str.substring(0, 1).toUpperCase() + 
>                str.substring(1).toLowerCase();
>     }
> }
> ```
> 
> **4. Factory methods:**
> 
> ```java
> public class Conexion {
>     private Conexion() {}
>     
>     public static Conexion crear(String tipo) {
>         // Lógica para crear conexión según tipo
>         return new Conexion();
>     }
> }
> ```
> 
> **5. Singleton pattern:**
> 
> ```java
> public class ConfiguracionSistema {
>     private static ConfiguracionSistema instancia;
>     
>     private ConfiguracionSistema() {}
>     
>     public static ConfiguracionSistema obtenerInstancia() {
>         if (instancia == null) {
>             instancia = new ConfiguracionSistema();
>         }
>         return instancia;
>     }
> }
> ```
> 
> **6. Caché compartida:**
> 
> ```java
> public class CacheUsuarios {
>     private static Map<String, Usuario> cache = new HashMap<>();
>     
>     public static void agregar(String id, Usuario usuario) {
>         cache.put(id, usuario);
>     }
>     
>     public static Usuario obtener(String id) {
>         return cache.get(id);
>     }
> }
> ```

---

## ⚠️ Errores Comunes y Soluciones

> [!warning]- 🚫 Problemas Típicos con Static
> 
> **1. Intentar acceder a miembros de instancia desde método estático:**
> 
> ```java
> public class Ejemplo {
>     private int valor = 10;
>     
>     // ❌ ERROR
>     public static void metodoEstatico() {
>         System.out.println(valor);  // ¡No compila!
>         // Error: non-static variable cannot be referenced from a static context
>     }
>     
>     // ✅ SOLUCIÓN 1: Hacer el método de instancia
>     public void metodoInstancia() {
>         System.out.println(valor);  // OK
>     }
>     
>     // ✅ SOLUCIÓN 2: Pasar objeto como parámetro
>     public static void metodoEstatico(Ejemplo obj) {
>         System.out.println(obj.valor);  // OK
>     }
>     
>     // ✅ SOLUCIÓN 3: Hacer el atributo estático (si tiene sentido)
>     private static int valorEstatico = 10;
>     public static void otroMetodoEstatico() {
>         System.out.println(valorEstatico);  // OK
>     }
> }
> ```
> 
> **2. Uso incorrecto de `this` en contexto estático:**
> 
> ```java
> public class Usuario {
>     private String nombre;
>     
>     // ❌ ERROR
>     public static void saludar() {
>         System.out.println("Hola " + this.nombre);  // ¡No compila!
>         // Error: 'this' cannot be referenced from a static context
>     }
>     
>     // ✅ SOLUCIÓN
>     public void saludarInstancia() {
>         System.out.println("Hola " + this.nombre);  // OK
>     }
> }
> ```
> 
> **3. Abuso de variables estáticas mutables:**
> 
> ```java
> // ❌ MAL - Estado compartido peligroso
> public class Calculadora {
>     public static double resultado;  // ¡Peligroso!
>     
>     public static void sumar(double a, double b) {
>         resultado = a + b;  // Todos comparten el mismo resultado
>     }
> }
> 
> // Problema:
> Calculadora.sumar(5, 3);  // resultado = 8
> Calculadora.sumar(10, 2); // resultado = 12 (¡se perdió el anterior!)
> 
> // ✅ MEJOR - Sin estado compartido
> public class Calculadora {
>     public static double sumar(double a, double b) {
>         return a + b;  // Retorna el resultado sin guardarlo
>     }
> }
> ```
> 
> **4. Confusión entre acceso por clase vs instancia:**
> 
> ```java
> public class Contador {
>     private static int cuenta = 0;
>     
>     public static void incrementar() {
>         cuenta++;
>     }
> }
> 
> // ⚠️ FUNCIONA PERO NO RECOMENDADO
> Contador c1 = new Contador();
> c1.incrementar();  // Acceso a través de instancia (confuso)
> 
> // ✅ MEJOR - Usar nombre de clase
> Contador.incrementar();  // Deja claro que es estático
> ```
> 
> **5. Olvidar inicializar variables estáticas:**
> 
> ```java
> // ❌ PROBLEMA
> public class Config {
>     private static Properties props;  // null por defecto
>     
>     public static String getProperty(String key) {
>         return props.getProperty(key);  // ¡NullPointerException!
>     }
> }
> 
> // ✅ SOLUCIÓN - Bloque estático
> public class Config {
>     private static Properties props;
>     
>     static {
>         props = new Properties();
>         // Cargar propiedades...
>     }
>     
>     public static String getProperty(String key) {
>         return props.getProperty(key);  // Seguro
>     }
> }
> ```
> 
> **6. Import static excesivo:**
> 
> ```java
> // ❌ ABUSO - Dificulta lectura
> import static java.lang.Math.*;
> import static java.lang.System.*;
> import static Constantes.*;
> 
> public class Calculadora {
>     public void calcular() {
>         double x = sqrt(PI * pow(E, 2));  // ¿De dónde vienen?
>         out.println(x);
>     }
> }
> 
> // ✅ MEJOR - Explícito y claro
> import java.lang.Math;
> 
> public class Calculadora {
>     public void calcular() {
>         double x = Math.sqrt(Math.PI * Math.pow(Math.E, 2));
>         System.out.println(x);
>     }
> }
> ```

---

## 🎨 Ejemplo Completo: Sistema de Biblioteca con Static

> [!example]- 📚 Implementación Práctica
> 
> ```java
> import java.time.LocalDateTime;
> import java.time.format.DateTimeFormatter;
> 
> /**
>  * Sistema de Biblioteca que demuestra el uso correcto de static
>  */
> public class SistemaBiblioteca {
>     
>     // ============================================
>     // CLASE LIBRO
>     // ============================================
>     public static class Libro {
>         // Atributos estáticos (compartidos)
>         private static int totalLibros = 0;
>         private static final int ISBN_LENGTH = 13;
>         
>         // Atributos de instancia (únicos)
>         private final String isbn;
>         private final String titulo;
>         private String autor;
>         private boolean disponible;
>         private int vecesPrestado;
>         
>         // Constructor
>         public Libro(String isbn, String titulo, String autor) {
> 
>             if (!validarISBN(isbn)) {
>                 throw new IllegalArgumentException("ISBN inválido");
>             }
>             
>             this.isbn = isbn;
>             this.titulo = titulo;
>             this.autor = autor;
>             this.disponible = true;
>             this.vecesPrestado = 0;
>             
>             totalLibros++;
>         }
>         
>         // Método estático de validación
>         public static boolean validarISBN(String isbn) {
>             return isbn != null && 
>                    isbn.replaceAll("-", "").length() == ISBN_LENGTH;
>         }
>         
>         // Getter estático
>         public static int getTotalLibros() {
>             return totalLibros;
>         }
>         
>         // Métodos de instancia
>         public boolean prestar() {
>             if (!disponible) {
>                 return false;
>             }
>             disponible = false;
>             vecesPrestado++;
>             return true;
>         }
>         
>         public void devolver() {
>             disponible = true;
>         }
>         
>         public String getTitulo() {
>             return titulo;
>         }
>         
>         public String getIsbn() {
>             return isbn;
>         }
>         
>         public boolean isDisponible() {
>             return disponible;
>         }
>         
>         public int getVecesPrestado() {
>             return vecesPrestado;
>         }
>         
>         @Override
>         public String toString() {
>             return String.format("%s - %s [%s]", 
>                 titulo, autor, disponible ? "Disponible" : "Prestado");
>         }
>     }
>     
>     // ============================================
>     // CLASE ESTADÍSTICAS (Solo métodos estáticos)
>     // ============================================
>     public static class Estadisticas {
>         // No se pueden crear instancias
>         private Estadisticas() {
>             throw new UnsupportedOperationException("Clase de utilidad");
>         }
>         
>         // Calcular promedio de préstamos
>         public static double promedioPrestamosPorLibro(Libro[] libros) {
>             if (libros == null || libros.length == 0) {
>                 return 0.0;
>             }
>             
>             int totalPrestamos = 0;
>             for (Libro libro : libros) {
>                 if (libro != null) {
>                     totalPrestamos += libro.getVecesPrestado();
>                 }
>             }
>             
>             return (double) totalPrestamos / libros.length;
>         }
>         
>         // Libro más prestado
>         public static Libro libroMasPrestado(Libro[] libros) {
>             if (libros == null || libros.length == 0) {
>                 return null;
>             }
>             
>             Libro masPrestado = libros[0];
>             for (Libro libro : libros) {
>                 if (libro != null && 
>                     libro.getVecesPrestado() > masPrestado.getVecesPrestado()) {
>                     masPrestado = libro;
>                 }
>             }
>             
>             return masPrestado;
>         }
>         
>         // Contar libros disponibles
>         public static int contarDisponibles(Libro[] libros) {
>             if (libros == null) return 0;
>             
>             int count = 0;
>             for (Libro libro : libros) {
>                 if (libro != null && libro.isDisponible()) {
>                     count++;
>                 }
>             }
>             return count;
>         }
>         
>         // Generar reporte
>         public static void generarReporte(Libro[] libros) {
>             System.out.println("\n╔════════════════════════════════════════╗");
>             System.out.println("║     REPORTE ESTADÍSTICO BIBLIOTECA     ║");
>             System.out.println("╚════════════════════════════════════════╝");
>             
>             System.out.println("\nTotal de libros: " + Libro.getTotalLibros());
>             System.out.println("Libros disponibles: " + contarDisponibles(libros));
>             System.out.println("Libros prestados: " + 
>                 (libros.length - contarDisponibles(libros)));
>             
>             double promedio = promedioPrestamosPorLibro(libros);
>             System.out.printf("Promedio préstamos/libro: %.2f\n", promedio);
>             
>             Libro masPrestado = libroMasPrestado(libros);
>             if (masPrestado != null) {
>                 System.out.println("\nLibro más prestado:");
>                 System.out.println("  → " + masPrestado.getTitulo() + 
>                     " (" + masPrestado.getVecesPrestado() + " veces)");
>             }
>         }
>     }
>     
>     // ============================================
>     // CLASE LOGGER (Singleton con static)
>     // ============================================
>     public static class Logger {
>         // Instancia única (Singleton)
>         private static Logger instancia;
>         
>         // Configuración estática
>         private static boolean habilitado = true;
>         private static final DateTimeFormatter FORMATO_FECHA = 
>             DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
>         
>         // Niveles de log
>         public static final String NIVEL_INFO = "INFO";
>         public static final String NIVEL_WARN = "WARN";
>         public static final String NIVEL_ERROR = "ERROR";
>         
>         // Constructor privado (Singleton)
>         private Logger() {}
>         
>         // Método estático para obtener instancia
>         public static Logger obtenerInstancia() {
>             if (instancia == null) {
>                 instancia = new Logger();
>             }
>             return instancia;
>         }
>         
>         // Métodos estáticos de logging
>         public static void info(String mensaje) {
>             log(NIVEL_INFO, mensaje);
>         }
>         
>         public static void warn(String mensaje) {
>             log(NIVEL_WARN, mensaje);
>         }
>         
>         public static void error(String mensaje) {
>             log(NIVEL_ERROR, mensaje);
>         }
>         
>         private static void log(String nivel, String mensaje) {
>             if (!habilitado) return;
>             
>             String timestamp = LocalDateTime.now().format(FORMATO_FECHA);
>             String icono = obtenerIcono(nivel);
>             
>             System.out.println(String.format("[%s] %s %s: %s", 
>                 timestamp, icono, nivel, mensaje));
>         }
>         
>         private static String obtenerIcono(String nivel) {
>             switch (nivel) {
>                 case NIVEL_INFO:  return "ℹ️";
>                 case NIVEL_WARN:  return "⚠️";
>                 case NIVEL_ERROR: return "❌";
>                 default:          return "📝";
>             }
>         }
>         
>         public static void habilitar() {
>             habilitado = true;
>         }
>         
>         public static void deshabilitar() {
>             habilitado = false;
>         }
>     }
>     
>     // ============================================
>     // CLASE FORMATOUTILS (Utilidades)
>     // ============================================
>     public static class FormatoUtils {
>         // Constructor privado
>         private FormatoUtils() {}
>         
>         // Formatear título de sección
>         public static void imprimirTitulo(String titulo) {
>             String linea = "═".repeat(titulo.length() + 4);
>             System.out.println("\n┌─" + linea + "─┐");
>             System.out.println("│  " + titulo.toUpperCase() + "  │");
>             System.out.println("└─" + linea + "─┘");
>         }
>         
>         // Formatear línea de separación
>         public static void imprimirSeparador() {
>             System.out.println("─".repeat(50));
>         }
>         
>         // Formatear lista de libros
>         public static void imprimirListaLibros(Libro[] libros) {
>             if (libros == null || libros.length == 0) {
>                 System.out.println("  (No hay libros para mostrar)");
>                 return;
>             }
>             
>             for (int i = 0; i < libros.length; i++) {
>                 if (libros[i] != null) {
>                     System.out.printf("  %d. %s\n", i + 1, libros[i]);
>                 }
>             }
>         }
>     }
>     
>     // ============================================
>     // CLASE CONFIGURACION (Constantes)
>     // ============================================
>     public static class Configuracion {
>         // Constructor privado
>         private Configuracion() {}
>         
>         // Constantes de la aplicación
>         public static final String NOMBRE_BIBLIOTECA = "Biblioteca Central";
>         public static final String VERSION = "2.0.0";
>         public static final int MAX_LIBROS = 1000;
>         public static final int DIAS_PRESTAMO = 14;
>         
>         // Mensajes
>         public static final String MSG_PRESTAMO_EXITOSO = "✅ Préstamo realizado exitosamente";
>         public static final String MSG_DEVOLUCION_EXITOSA = "✅ Devolución realizada exitosamente";
>         public static final String MSG_LIBRO_NO_DISPONIBLE = "❌ Libro no disponible";
>         public static final String MSG_LIBRO_NO_ENCONTRADO = "❌ Libro no encontrado";
>         
>         // Método para mostrar configuración
>         public static void mostrarConfiguracion() {
>             System.out.println("\n╔═══════════════════════════════════╗");
>             System.out.println("║       CONFIGURACIÓN SISTEMA       ║");
>             System.out.println("╚═══════════════════════════════════╝");
>             System.out.println("Nombre: " + NOMBRE_BIBLIOTECA);
>             System.out.println("Versión: " + VERSION);
>             System.out.println("Capacidad máxima: " + MAX_LIBROS + " libros");
>             System.out.println("Días de préstamo: " + DIAS_PRESTAMO + " días");
>         }
>     }
>     
>     // ============================================
>     // CLASE GESTORBIBLIOTECA
>     // ============================================
>     public static class GestorBiblioteca {
>         // Atributos estáticos
>         private static int totalPrestamosRealizados = 0;
>         private static int totalDevolucionesRealizadas = 0;
>         
>         // Atributos de instancia
>         private Libro[] catalogo;
>         private int cantidadLibros;
>         
>         // Bloque estático de inicialización
>         static {
>             Logger.info("Sistema de biblioteca inicializado");
>         }
>         
>         // Constructor
>         public GestorBiblioteca() {
>             this.catalogo = new Libro[Configuracion.MAX_LIBROS];
>             this.cantidadLibros = 0;
>             Logger.info("Gestor de biblioteca creado");
>         }
>         
>         // Agregar libro al catálogo
>         public boolean agregarLibro(Libro libro) {
>             if (cantidadLibros >= Configuracion.MAX_LIBROS) {
>                 Logger.warn("Catálogo lleno, no se puede agregar: " + libro.getTitulo());
>                 return false;
>             }
>             
>             catalogo[cantidadLibros++] = libro;
>             Logger.info("Libro agregado: " + libro.getTitulo());
>             return true;
>         }
>         
>         // Buscar libro por ISBN
>         public Libro buscarPorISBN(String isbn) {
>             for (int i = 0; i < cantidadLibros; i++) {
>                 if (catalogo[i].getIsbn().equals(isbn)) {
>                     return catalogo[i];
>                 }
>             }
>             return null;
>         }
>         
>         // Realizar préstamo
>         public boolean realizarPrestamo(String isbn) {
>             Libro libro = buscarPorISBN(isbn);
>             
>             if (libro == null) {
>                 Logger.error(Configuracion.MSG_LIBRO_NO_ENCONTRADO + ": " + isbn);
>                 return false;
>             }
>             
>             if (!libro.prestar()) {
>                 Logger.warn(Configuracion.MSG_LIBRO_NO_DISPONIBLE + ": " + libro.getTitulo());
>                 return false;
>             }
>             
>             totalPrestamosRealizados++;
>             Logger.info(Configuracion.MSG_PRESTAMO_EXITOSO + ": " + libro.getTitulo());
>             return true;
>         }
>         
>         // Realizar devolución
>         public boolean realizarDevolucion(String isbn) {
>             Libro libro = buscarPorISBN(isbn);
>             
>             if (libro == null) {
>                 Logger.error(Configuracion.MSG_LIBRO_NO_ENCONTRADO + ": " + isbn);
>                 return false;
>             }
>             
>             libro.devolver();
>             totalDevolucionesRealizadas++;
>             Logger.info(Configuracion.MSG_DEVOLUCION_EXITOSA + ": " + libro.getTitulo());
>             return true;
>         }
>         
>         // Obtener catálogo
>         public Libro[] obtenerCatalogo() {
>             Libro[] resultado = new Libro[cantidadLibros];
>             System.arraycopy(catalogo, 0, resultado, 0, cantidadLibros);
>             return resultado;
>         }
>         
>         // Métodos estáticos para estadísticas globales
>         public static int getTotalPrestamos() {
>             return totalPrestamosRealizados;
>         }
>         
>         public static int getTotalDevoluciones() {
>             return totalDevolucionesRealizadas;
>         }
>         
>         public static void resetearEstadisticas() {
>             totalPrestamosRealizados = 0;
>             totalDevolucionesRealizadas = 0;
>             Logger.info("Estadísticas reseteadas");
>         }
>     }
>     
>     // ============================================
>     // PROGRAMA PRINCIPAL
>     // ============================================
>     public static void main(String[] args) {
>         // Mostrar banner inicial
>         System.out.println("╔══════════════════════════════════════════════╗");
>         System.out.println("║  SISTEMA DE BIBLIOTECA - DEMO STATIC         ║");
>         System.out.println("║  Ejemplo completo de uso de static en Java   ║");
>         System.out.println("╚══════════════════════════════════════════════╝");
>         
>         // Mostrar configuración (usando constantes estáticas)
>         Configuracion.mostrarConfiguracion();
>         
>         // Crear gestor de biblioteca
>         FormatoUtils.imprimirTitulo("Inicializando Sistema");
>         GestorBiblioteca gestor = new GestorBiblioteca();
>         
>         // Agregar libros al catálogo
>         FormatoUtils.imprimirTitulo("Agregando Libros");
>         
>         gestor.agregarLibro(new Libro(
>             "978-0-13-468599-1",
>             "Effective Java",
>             "Joshua Bloch"
>         ));
>         
>         gestor.agregarLibro(new Libro(
>             "978-0-13-464266-0",
>             "Clean Code",
>             "Robert C. Martin"
>         ));
>         
>         gestor.agregarLibro(new Libro(
>             "978-0-13-597834-0",
>             "Design Patterns",
>             "Gang of Four"
>         ));
>         
>         gestor.agregarLibro(new Libro(
>             "978-0-13-485670-4",
>             "Refactoring",
>             "Martin Fowler"
>         ));
>         
>         // Mostrar catálogo usando método estático de formato
>         FormatoUtils.imprimirTitulo("Catálogo Completo");
>         Libro[] catalogo = gestor.obtenerCatalogo();
>         FormatoUtils.imprimirListaLibros(catalogo);
>         
>         // Información usando atributo estático
>         System.out.println("\n📊 Total de libros en el sistema: " + Libro.getTotalLibros());
>         
>         // Realizar préstamos
>         FormatoUtils.imprimirTitulo("Realizando Préstamos");
>         gestor.realizarPrestamo("978-0-13-468599-1");
>         gestor.realizarPrestamo("978-0-13-464266-0");
>         gestor.realizarPrestamo("978-0-13-464266-0"); // Intento duplicado
>         
>         // Mostrar estadísticas usando métodos estáticos
>         FormatoUtils.imprimirSeparador();
>         System.out.println("📈 Préstamos realizados: " + GestorBiblioteca.getTotalPrestamos());
>         System.out.println("📈 Devoluciones realizadas: " + GestorBiblioteca.getTotalDevoluciones());
>         
>         // Generar reporte usando clase de utilidad estática
>         Estadisticas.generarReporte(gestor.obtenerCatalogo());
>         
>         // Realizar devoluciones
>         FormatoUtils.imprimirTitulo("Realizando Devoluciones");
>         gestor.realizarDevolucion("978-0-13-468599-1");
>         
>         // Estadísticas finales
>         FormatoUtils.imprimirTitulo("Estadísticas Finales");
>         System.out.println("📈 Total préstamos: " + GestorBiblioteca.getTotalPrestamos());
>         System.out.println("📈 Total devoluciones: " + GestorBiblioteca.getTotalDevoluciones());
>         
>         // Reporte final
>         Estadisticas.generarReporte(gestor.obtenerCatalogo());
>         
>         // Demostrar validación estática
>         FormatoUtils.imprimirTitulo("Validación de ISBN (Método Estático)");
>         String[] isbnsTest = {
>             "978-0-13-468599-1",
>             "123-456",
>             "978-0-13-XXXXX-1"
>         };
>         
>         for (String isbn : isbnsTest) {
>             boolean valido = Libro.validarISBN(isbn);
>             System.out.println("ISBN: " + isbn + " → " + 
>                 (valido ? "✅ Válido" : "❌ Inválido"));
>         }
>         
>         // Mensaje final
>         System.out.println("\n╔══════════════════════════════════════════════╗");
>         System.out.println("║  DEMO COMPLETADA EXITOSAMENTE                ║");
>         System.out.println("║  Conceptos demostrados:                      ║");
>         System.out.println("║  • Atributos estáticos                       ║");
>         System.out.println("║  • Métodos estáticos                         ║");
>         System.out.println("║  • Constantes (static final)                 ║");
>         System.out.println("║  • Bloques estáticos                         ║");
>         System.out.println("║  • Clases de utilidad                        ║");
>         System.out.println("║  • Singleton pattern                         ║");
>         System.out.println("║  • Factory methods                           ║");
>         System.out.println("╚══════════════════════════════════════════════╝");
>     }
> }
> ```

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica con Static
> 
> **Nivel Básico:**
> 
> 1. **Contador de Estudiantes:** Crear clase `Estudiante` con contador estático que lleve el registro de cuántos estudiantes se han creado
> 2. **Conversión de Unidades:** Clase `Conversor` con métodos estáticos para convertir entre Celsius/Fahrenheit, kilómetros/millas
> 3. **Generador de IDs:** Clase con método estático que genere IDs únicos incrementales
> 
> **Nivel Intermedio:**
> 
> 4. **Sistema de Configuración:** Clase `Config` con constantes estáticas y método para cargar configuración desde archivo simulado
> 5. **Validador de Datos:** Clase con métodos estáticos para validar emails, teléfonos, cédulas, contraseñas
> 6. **Calculadora Científica:** Clase con métodos estáticos para operaciones matemáticas avanzadas
> 7. **Factory de Empleados:** Implementar factory methods para crear diferentes tipos de empleados
> 
> **Nivel Avanzado:**
> 
> 8. **Sistema de Cache:** Implementar cache estática con límite de tamaño y política LRU (Least Recently Used)
> 9. **Singleton Thread-Safe:** Implementar patrón Singleton que sea seguro en entornos multi-hilo
> 10. **Pool de Conexiones:** Sistema de pool de conexiones usando atributos y métodos estáticos
> 11. **Sistema de Logs:** Logger completo con niveles, formato, y escritura a archivo (simulado)

---

## 📊 Comparación: ¿Cuándo usar static?

> [!tip]- ✅ Guía de Decisión
> 
> ```
> ┌─────────────────────────────────────────────────────┐
> │        ¿Necesitas crear objetos con estado?         │
> └────────────────┬────────────────────────────────────┘
>                  │
>         ┌────────┴────────┐
>         │                 │
>        SÍ                NO
>         │                 │
>         ▼                 ▼
>   ┌─────────┐      ┌─────────────┐
>   │ INSTANCIA│      │ ¿El valor es│
>   │          │      │  compartido?│
>   └─────────┘      └──────┬──────┘
>                           │
>                  ┌────────┴────────┐
>                  │                 │
>                 SÍ                NO
>                  │                 │
>                  ▼                 ▼
>           ┌──────────┐      ┌─────────────┐
>           │  STATIC  │      │  ¿Es una    │
>           │          │      │ utilidad?   │
>           └──────────┘      └──────┬──────┘
>                                    │
>                           ┌────────┴────────┐
>                           │                 │
>                          SÍ                NO
>                           │                 │
>                           ▼                 ▼
>                    ┌─────────────┐    ┌──────────┐
>                    │   STATIC    │    │INSTANCIA │
>                    │ (Utility)   │    │          │
>                    └─────────────┘    └──────────┘
> ```
> 
> **Tabla de decisión:**
> 
> |Escenario|Usar Static|Usar Instancia|
> |---|---|---|
> |Constantes globales|✅|❌|
> |Funciones de utilidad|✅|❌|
> |Contador compartido|✅|❌|
> |Estado del objeto|❌|✅|
> |Comportamiento específico|❌|✅|
> |Factory methods|✅|❌|
> |Configuración global|✅|❌|
> |Datos específicos|❌|✅|
> |Singleton|✅|Ambos|
> |Cache compartida|✅|❌|

---

## ⚡ Rendimiento y Memoria

> [!info]- 💾 Consideraciones de Memoria
> 
> **Uso de memoria:**
> 
> ```java
> public class Comparacion {
>     // ESTÁTICO - Una sola copia en memoria
>     private static int contadorEstatico = 0;
>     
>     // INSTANCIA - Una copia por objeto
>     private int contadorInstancia = 0;
> }
> 
> // Crear 1000 objetos:
> for (int i = 0; i < 1000; i++) {
>     new Comparacion();
> }
> 
> // Memoria usada:
> // - contadorEstatico: 4 bytes (una sola vez)
> // - contadorInstancia: 4000 bytes (1000 copias)
> ```
> 
> **Ventajas de rendimiento:**
> 
> - ✅ **Acceso más rápido:** No requiere dereferencia de objeto
> - ✅ **Menos memoria:** Una sola copia compartida
> - ✅ **Sin overhead:** No necesita instanciación
> 
> **Desventajas:**
> 
> - ⚠️ **Estado global:** Puede causar problemas en concurrencia
> - ⚠️ **Acoplamiento:** Dependencia directa de la clase
> - ⚠️ **Testing difícil:** No se puede mockear fácilmente
> 
> **Ejemplo de medición:**
> 
> ```java
> public class MedicionMemoria {
>     public static void main(String[] args) {
>         Runtime runtime = Runtime.getRuntime();
>         
>         // Medir memoria antes
>         runtime.gc();
>         long memoriaInicial = runtime.totalMemory() - runtime.freeMemory();
>         
>         // Crear objetos
>         Object[] objetos = new Object[100000];
>         for (int i = 0; i < objetos.length; i++) {
>             objetos[i] = new Producto();
>         }
>         
>         // Medir memoria después
>         long memoriaFinal = runtime.totalMemory() - runtime.freeMemory();
>         long memoriaUsada = (memoriaFinal - memoriaInicial) / 1024;
>         
>         System.out.println("Memoria usada: " + memoriaUsada + " KB");
>         System.out.println("Promedio por objeto: " + 
>             (memoriaUsada / objetos.length) + " bytes");
>     }
> }
> 
> class Producto {
>     private static int totalProductos = 0; // Compartido
>     private String nombre; // 8 bytes (referencia)
>     private double precio; // 8 bytes
>     
>     public Producto() {
>         totalProductos++;
>     }
> }
> ```

---

## 🔗 Conexión con Próximos Temas

> [!quote]- 🌟 Continuando el Aprendizaje
> 
> **Has aprendido:**
> 
> - ✅ Diferencia entre miembros estáticos y de instancia
> - ✅ Atributos estáticos (variables de clase)
> - ✅ Métodos estáticos (métodos de clase)
> - ✅ Constantes con `static final`
> - ✅ Bloques estáticos de inicialización
> - ✅ Cuándo usar `static` y cuándo no
> - ✅ Patrones comunes (Singleton, Factory, Utilities)
> 
> **Próximos temas relacionados:**
> 
> - **[[04 - Herencia]]** - Cómo funcionan los miembros estáticos en jerarquías de clases
> - **[[05 - Polimorfismo]]** - Los métodos estáticos NO son polimórficos
> - **[[06 - Clases Abstractas]]** - Métodos estáticos en clases abstractas
> - **[[07 - Interfaces]]** - Métodos estáticos en interfaces (Java 8+)
> - **[[08 - Packages]]** - Organización de clases de utilidad estáticas
> - **[[Modificador Final]]** - Combinación de `static final` para constantes
> - **[[Patrones de Diseño]]** - Singleton, Factory, Strategy usando static

---

## 📚 Resumen Final

> [!summary]- 🎯 Puntos Clave
> 
> **Conceptos esenciales:**
> 
> 1. **`static`** indica que un miembro pertenece a la **clase**, no a las instancias
>     
> 2. **Atributos estáticos:**
>     
>     - Una sola copia en memoria
>     - Compartidos por todos los objetos
>     - Acceso: `NombreClase.atributo`
> 3. **Métodos estáticos:**
>     
>     - No requieren objeto para ser llamados
>     - No pueden acceder a miembros de instancia
>     - Ideales para utilidades y factories
> 4. **Constantes:**
>     
>     - `static final` para valores inmutables compartidos
>     - Convención: MAYÚSCULAS_CON_GUION_BAJO
> 5. **Bloques estáticos:**
>     
>     - Se ejecutan una vez al cargar la clase
>     - Útiles para inicialización compleja
> 6. **Cuándo usar static:**
>     
>     - ✅ Constantes globales
>     - ✅ Métodos de utilidad
>     - ✅ Contadores compartidos
>     - ✅ Factory methods
>     - ✅ Configuración global
>     - ❌ Estado específico de objetos
>     - ❌ Cuando se necesita polimorfismo
> 7. **Reglas de oro:**
>     
>     - Los métodos estáticos NO pueden usar `this`
>     - Los métodos estáticos NO pueden acceder a miembros de instancia
>     - Los métodos de instancia SÍ pueden acceder a miembros estáticos
>     - Preferir acceso por nombre de clase, no por instancia
>     - Encapsular variables estáticas mutables con `private`

---

**Tags:** #java #static #poo #modificadores #metodos-estaticos #atributos-estaticos #constantes #singleton #factory #utility-classes #bloques-estaticos #variables-clase