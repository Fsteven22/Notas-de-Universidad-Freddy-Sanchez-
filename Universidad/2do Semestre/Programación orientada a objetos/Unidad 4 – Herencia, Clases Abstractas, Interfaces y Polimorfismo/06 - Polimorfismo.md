# 🎭 Polimorfismo en Java

## 🎯 Introducción

> [!info]- 💡 ¿Qué es el Polimorfismo? El **polimorfismo** (del griego "muchas formas") es la capacidad de un objeto de tomar diferentes formas. Permite que una referencia de tipo padre apunte a objetos de tipos hijos, y que cada uno responda de manera diferente al mismo mensaje.
> 
> **Analogía:** Como un control remoto universal
> 
> - **Control (referencia padre):** Botón "reproducir"
> - **Dispositivos (objetos hijos):** TV reproduce video, radio reproduce audio, consola reproduce juego
> - **Mismo botón, diferente comportamiento:** Cada dispositivo responde a su manera
> 
> **Ventajas principales:**
> 
> - **Flexibilidad:** Escribir código que funciona con múltiples tipos
> - **Extensibilidad:** Agregar nuevos tipos sin modificar código existente
> - **Mantenibilidad:** Código más limpio y organizado
> - **Reutilización:** Mismo código para diferentes implementaciones

---

## 🔍 Tipos de Polimorfismo

### 1️⃣ Polimorfismo en Tiempo de Compilación (Estático)

> [!example]- ⚡ Sobrecarga de Métodos (Method Overloading) **Concepto:** Múltiples métodos con el **mismo nombre** pero **diferentes parámetros** en la misma clase.
> 
> ```java
> public class Calculadora {
>     // Mismo nombre, diferentes parámetros
>     
>     // Versión 1: dos enteros
>     public int sumar(int a, int b) {
>         System.out.println("Sumando dos enteros");
>         return a + b;
>     }
>     
>     // Versión 2: tres enteros
>     public int sumar(int a, int b, int c) {
>         System.out.println("Sumando tres enteros");
>         return a + b + c;
>     }
>     
>     // Versión 3: dos doubles
>     public double sumar(double a, double b) {
>         System.out.println("Sumando dos doubles");
>         return a + b;
>     }
>     
>     // Versión 4: array de enteros
>     public int sumar(int[] numeros) {
>         System.out.println("Sumando array");
>         int total = 0;
>         for (int n : numeros) {
>             total += n;
>         }
>         return total;
>     }
>     
>     // Versión 5: varargs (número variable de argumentos)
>     public int sumar(int... numeros) {
>         System.out.println("Sumando varargs");
>         int total = 0;
>         for (int n : numeros) {
>             total += n;
>         }
>         return total;
>     }
> }
> 
> // USO
> Calculadora calc = new Calculadora();
> 
> calc.sumar(5, 3);              // Llama versión 1
> calc.sumar(5, 3, 2);           // Llama versión 2
> calc.sumar(5.5, 3.2);          // Llama versión 3
> calc.sumar(new int[]{1,2,3});  // Llama versión 4
> calc.sumar(1, 2, 3, 4, 5);     // Llama versión 5
> ```
> 
> **Reglas de sobrecarga:**
> 
> - ✅ Diferente número de parámetros
> - ✅ Diferente tipo de parámetros
> - ✅ Diferente orden de parámetros
> - ❌ Solo diferente tipo de retorno (no es válido)
> - ❌ Solo diferente modificador de acceso (no es válido)
> 
> **Ejemplos comunes en Java:**
> 
> ```java
> // println está sobrecargado
> System.out.println("Texto");
> System.out.println(123);
> System.out.println(3.14);
> System.out.println(true);
> 
> // String.valueOf está sobrecargado
> String.valueOf(123);
> String.valueOf(3.14);
> String.valueOf(true);
> String.valueOf(new char[]{'a', 'b'});
> ```

### 2️⃣ Polimorfismo en Tiempo de Ejecución (Dinámico)

> [!success]- 🎯 Sobreescritura de Métodos (Method Overriding) **Concepto:** Una subclase proporciona su propia implementación de un método heredado de la clase padre.
> 
> ```java
> // Clase padre
> public class Animal {
>     protected String nombre;
>     
>     public Animal(String nombre) {
>         this.nombre = nombre;
>     }
>     
>     // Método que será sobreescrito
>     public void hacerSonido() {
>         System.out.println(nombre + " hace un sonido");
>     }
>     
>     public void comer() {
>         System.out.println(nombre + " está comiendo");
>     }
> }
> 
> // Clases hijas sobreescriben el método
> public class Perro extends Animal {
>     public Perro(String nombre) {
>         super(nombre);
>     }
>     
>     @Override  // Anotación recomendada
>     public void hacerSonido() {
>         System.out.println(nombre + " dice: ¡Guau guau!");
>     }
> }
> 
> public class Gato extends Animal {
>     public Gato(String nombre) {
>         super(nombre);
>     }
>     
>     @Override
>     public void hacerSonido() {
>         System.out.println(nombre + " dice: ¡Miau miau!");
>     }
> }
> 
> public class Vaca extends Animal {
>     public Vaca(String nombre) {
>         super(nombre);
>     }
>     
>     @Override
>     public void hacerSonido() {
>         System.out.println(nombre + " dice: ¡Muuu!");
>     }
> }
> 
> // ✨ POLIMORFISMO EN ACCIÓN
> public class Granja {
>     public static void main(String[] args) {
>         // Referencia tipo padre, objetos tipo hijo
>         Animal animal1 = new Perro("Firulais");
>         Animal animal2 = new Gato("Michi");
>         Animal animal3 = new Vaca("Lola");
>         
>         // Mismo método, diferente comportamiento
>         animal1.hacerSonido();  // ¡Guau guau!
>         animal2.hacerSonido();  // ¡Miau miau!
>         animal3.hacerSonido();  // ¡Muuu!
>         
>         // Array polimórfico
>         Animal[] animales = {
>             new Perro("Rex"),
>             new Gato("Garfield"),
>             new Vaca("Clarabella"),
>             new Perro("Scooby")
>         };
>         
>         System.out.println("\n🎵 Concierto de animales:");
>         for (Animal a : animales) {
>             a.hacerSonido();  // Cada uno hace su sonido
>         }
>     }
> }
> ```
> 
> **Reglas de sobreescritura:**
> 
> - ✅ Misma firma (nombre y parámetros)
> - ✅ Mismo tipo de retorno (o subtipo - covariant return)
> - ✅ No puede ser más restrictivo (acceso)
> - ✅ Puede lanzar menos excepciones (no más)
> - ❌ No se puede sobreescribir métodos `final`
> - ❌ No se puede sobreescribir métodos `static`
> - ❌ No se puede sobreescribir métodos `private`

---

## 🎯 Ejemplo Completo: Sistema de Notificaciones

> [!example]- 📬 Polimorfismo en la Práctica
> 
> ```java
> // ========================
> // CLASE ABSTRACTA BASE
> // ========================
> public abstract class Notificacion {
>     protected String destinatario;
>     protected String mensaje;
>     protected String prioridad;
>     
>     public Notificacion(String destinatario, String mensaje, String prioridad) {
>         this.destinatario = destinatario;
>         this.mensaje = mensaje;
>         this.prioridad = prioridad;
>     }
>     
>     // Método abstracto - cada tipo lo implementa diferente
>     public abstract boolean enviar();
>     
>     // Método concreto - común para todos
>     public void registrarEnvio() {
>         System.out.println("📝 Registro: Notificación enviada a " + destinatario);
>     }
>     
>     // Método que puede ser sobreescrito
>     public String obtenerResumen() {
>         return String.format("[%s] Para: %s", prioridad, destinatario);
>     }
>     
>     // Getters
>     public String getDestinatario() { return destinatario; }
>     public String getMensaje() { return mensaje; }
>     public String getPrioridad() { return prioridad; }
> }
> 
> // ========================
> // IMPLEMENTACIONES CONCRETAS
> // ========================
> public class NotificacionEmail extends Notificacion {
>     private String asunto;
>     
>     public NotificacionEmail(String destinatario, String mensaje, 
>                             String prioridad, String asunto) {
>         super(destinatario, mensaje, prioridad);
>         this.asunto = asunto;
>     }
>     
>     @Override
>     public boolean enviar() {
>         System.out.println("\n📧 Enviando EMAIL:");
>         System.out.println("   Para: " + destinatario);
>         System.out.println("   Asunto: " + asunto);
>         System.out.println("   Mensaje: " + mensaje);
>         System.out.println("   ✅ Email enviado correctamente");
>         registrarEnvio();
>         return true;
>     }
>     
>     @Override
>     public String obtenerResumen() {
>         return super.obtenerResumen() + " | Asunto: " + asunto;
>     }
> }
> 
> public class NotificacionSMS extends Notificacion {
>     private String telefono;
>     
>     public NotificacionSMS(String destinatario, String mensaje, 
>                           String prioridad, String telefono) {
>         super(destinatario, mensaje, prioridad);
>         this.telefono = telefono;
>     }
>     
>     @Override
>     public boolean enviar() {
>         // SMS tiene límite de caracteres
>         String mensajeCorto = mensaje.length() > 160 
>             ? mensaje.substring(0, 157) + "..." 
>             : mensaje;
>         
>         System.out.println("\n📱 Enviando SMS:");
>         System.out.println("   Para: " + destinatario + " (" + telefono + ")");
>         System.out.println("   Mensaje: " + mensajeCorto);
>         System.out.println("   ✅ SMS enviado correctamente");
>         registrarEnvio();
>         return true;
>     }
> }
> 
> public class NotificacionPush extends Notificacion {
>     private String aplicacion;
>     private String icono;
>     
>     public NotificacionPush(String destinatario, String mensaje, 
>                            String prioridad, String aplicacion) {
>         super(destinatario, mensaje, prioridad);
>         this.aplicacion = aplicacion;
>         this.icono = "🔔";
>     }
>     
>     @Override
>     public boolean enviar() {
>         System.out.println("\n🔔 Enviando PUSH NOTIFICATION:");
>         System.out.println("   App: " + aplicacion);
>         System.out.println("   Usuario: " + destinatario);
>         System.out.println("   " + icono + " " + mensaje);
>         
>         if (prioridad.equals("ALTA")) {
>             System.out.println("   🔴 Notificación prioritaria - Con sonido");
>         } else {
>             System.out.println("   🔵 Notificación silenciosa");
>         }
>         
>         System.out.println("   ✅ Push enviado correctamente");
>         registrarEnvio();
>         return true;
>     }
> }
> 
> public class NotificacionWhatsApp extends Notificacion {
>     private String telefono;
>     
>     public NotificacionWhatsApp(String destinatario, String mensaje,
>                                String prioridad, String telefono) {
>         super(destinatario, mensaje, prioridad);
>         this.telefono = telefono;
>     }
>     
>     @Override
>     public boolean enviar() {
>         System.out.println("\n💬 Enviando WHATSAPP:");
>         System.out.println("   Para: " + destinatario + " (" + telefono + ")");
>         System.out.println("   Mensaje: " + mensaje);
>         System.out.println("   ✅ WhatsApp enviado correctamente");
>         registrarEnvio();
>         return true;
>     }
> }
> 
> // ========================
> // GESTOR DE NOTIFICACIONES
> // ========================
> public class GestorNotificaciones {
>     // ✨ Polimorfismo - acepta cualquier tipo de notificación
>     public void enviarNotificacion(Notificacion notificacion) {
>         System.out.println("\n╔════════════════════════════════════╗");
>         System.out.println("║  PROCESANDO NOTIFICACIÓN           ║");
>         System.out.println("╚════════════════════════════════════╝");
>         System.out.println(notificacion.obtenerResumen());
>         
>         boolean exito = notificacion.enviar();
>         
>         if (exito) {
>             System.out.println("✅ Notificación procesada exitosamente");
>         } else {
>             System.out.println("❌ Error al procesar notificación");
>         }
>     }
>     
>     // Enviar múltiples notificaciones
>     public void enviarMasivo(Notificacion[] notificaciones) {
>         System.out.println("\n🚀 ENVIANDO NOTIFICACIONES MASIVAS");
>         System.out.println("Total: " + notificaciones.length);
>         
>         int exitosas = 0;
>         for (Notificacion n : notificaciones) {
>             if (n.enviar()) {
>                 exitosas++;
>             }
>         }
>         
>         System.out.println("\n📊 Resultado: " + exitosas + "/" + 
>                          notificaciones.length + " enviadas");
>     }
>     
>     // Filtrar por prioridad
>     public void enviarPorPrioridad(Notificacion[] notificaciones, 
>                                    String prioridad) {
>         System.out.println("\n🎯 ENVIANDO NOTIFICACIONES PRIORIDAD: " + prioridad);
>         
>         for (Notificacion n : notificaciones) {
>             if (n.getPrioridad().equals(prioridad)) {
>                 n.enviar();
>             }
>         }
>     }
> }
> 
> // ========================
> // PROGRAMA PRINCIPAL
> // ========================
> public class SistemaNotificaciones {
>     public static void main(String[] args) {
>         GestorNotificaciones gestor = new GestorNotificaciones();
>         
>         // Crear diferentes tipos de notificaciones
>         Notificacion email = new NotificacionEmail(
>             "usuario@example.com",
>             "Bienvenido a nuestro sistema. Gracias por registrarte.",
>             "MEDIA",
>             "Bienvenida al sistema"
>         );
>         
>         Notificacion sms = new NotificacionSMS(
>             "Juan Pérez",
>             "Tu código de verificación es: 123456. Válido por 5 minutos.",
>             "ALTA",
>             "+593987654321"
>         );
>         
>         Notificacion push = new NotificacionPush(
>             "maria_garcia",
>             "Tienes un nuevo mensaje de Carlos",
>             "ALTA",
>             "ChatApp"
>         );
>         
>         Notificacion whatsapp = new NotificacionWhatsApp(
>             "Ana López",
>             "Tu pedido #12345 ha sido enviado y llegará mañana.",
>             "MEDIA",
>             "+593991234567"
>         );
>         
>         // ✨ POLIMORFISMO - Todas tratadas como Notificacion
>         gestor.enviarNotificacion(email);
>         gestor.enviarNotificacion(sms);
>         gestor.enviarNotificacion(push);
>         gestor.enviarNotificacion(whatsapp);
>         
>         // Array polimórfico
>         Notificacion[] notificaciones = {
>             new NotificacionEmail("user1@mail.com", "Oferta especial", 
>                                  "BAJA", "Promoción"),
>             new NotificacionSMS("User2", "Código: 789", "ALTA", "+123456"),
>             new NotificacionPush("user3", "Nueva actualización", 
>                                 "MEDIA", "MyApp"),
>             new NotificacionWhatsApp("User4", "Recordatorio", 
>                                     "ALTA", "+789012")
>         };
>         
>         // Envío masivo
>         gestor.enviarMasivo(notificaciones);
>         
>         // Filtrar por prioridad
>         gestor.enviarPorPrioridad(notificaciones, "ALTA");
>         
>         // Demostrar polimorfismo con instanceof
>         System.out.println("\n🔍 ANÁLISIS DE TIPOS:");
>         for (Notificacion n : notificaciones) {
>             System.out.print(n.getDestinatario() + " -> ");
>             
>             if (n instanceof NotificacionEmail) {
>                 System.out.println("Es un Email");
>             } else if (n instanceof NotificacionSMS) {
>                 System.out.println("Es un SMS");
>             } else if (n instanceof NotificacionPush) {
>                 System.out.println("Es un Push");
>             } else if (n instanceof NotificacionWhatsApp) {
>                 System.out.println("Es un WhatsApp");
>             }
>         }
>     }
> }
> ```

---

## 🎨 Casting y Tipos

> [!tip]- 🔄 Conversión de Tipos
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
>         System.out.println("Guau guau!");
>     }
>     
>     @Override
>     public void comer() {
>         System.out.println("Perro comiendo croquetas");
>     }
> }
> 
> public class Gato extends Animal {
>     public void maullar() {
>         System.out.println("Miau!");
>     }
> }
> 
> // ========================
> // UPCASTING Y DOWNCASTING
> // ========================
> public class TestCasting {
>     public static void main(String[] args) {
>         // ✅ UPCASTING (Implícito - Siempre seguro)
>         Perro perro = new Perro();
>         Animal animal = perro;  // Hijo -> Padre (automático)
>         
>         animal.comer();  // ✅ Funciona (método de Animal)
>         // animal.ladrar();  // ❌ Error - Animal no tiene ladrar()
>         
>         // ✅ DOWNCASTING (Explícito - Puede fallar)
>         Animal animal2 = new Perro();  // Realmente es un Perro
>         
>         // Verificar tipo antes de hacer cast
>         if (animal2 instanceof Perro) {
>             Perro p = (Perro) animal2;  // Padre -> Hijo (manual)
>             p.ladrar();  // ✅ Ahora sí funciona
>         }
>         
>         // ❌ DOWNCASTING INCORRECTO
>         Animal animal3 = new Gato();
>         
>         // Esto compila pero falla en ejecución
>         try {
>             Perro p2 = (Perro) animal3;  // ClassCastException
>             p2.ladrar();
>         } catch (ClassCastException e) {
>             System.out.println("❌ Error: No se puede convertir Gato a Perro");
>         }
>         
>         // ✅ USO CORRECTO DE instanceof
>         Animal[] animales = {
>             new Perro(),
>             new Gato(),
>             new Perro(),
>             new Animal()
>         };
>         
>         for (Animal a : animales) {
>             a.comer();  // Todos pueden comer
>             
>             // Comportamiento específico según tipo
>             if (a instanceof Perro) {
>                 ((Perro) a).ladrar();
>             } else if (a instanceof Gato) {
>                 ((Gato) a).maullar();
>             }
>         }
>     }
> }
> ```

---

## 🏗️ Polimorfismo con Interfaces

> [!example]- 🔌 Múltiples Formas con Interfaces
> 
> ```java
> // Interface
> interface Reproducible {
>     void reproducir();
>     void pausar();
>     void detener();
> }
> 
> // Diferentes implementaciones
> public class ReproductorVideo implements Reproducible {
>     private String archivo;
>     
>     public ReproductorVideo(String archivo) {
>         this.archivo = archivo;
>     }
>     
>     @Override
>     public void reproducir() {
>         System.out.println("▶️  Reproduciendo video: " + archivo);
>     }
>     
>     @Override
>     public void pausar() {
>         System.out.println("⏸️  Video pausado");
>     }
>     
>     @Override
>     public void detener() {
>         System.out.println("⏹️  Video detenido");
>     }
> }
> 
> public class ReproductorAudio implements Reproducible {
>     private String cancion;
>     
>     public ReproductorAudio(String cancion) {
>         this.cancion = cancion;
>     }
>     
>     @Override
>     public void reproducir() {
>         System.out.println("🎵 Reproduciendo audio: " + cancion);
>     }
>     
>     @Override
>     public void pausar() {
>         System.out.println("⏸️  Audio pausado");
>     }
>     
>     @Override
>     public void detener() {
>         System.out.println("⏹️  Audio detenido");
>     }
> }
> 
> public class ReproductorPodcast implements Reproducible {
>     private String episodio;
>     private int minuto;
>     
>     public ReproductorPodcast(String episodio) {
>         this.episodio = episodio;
>         this.minuto = 0;
>     }
>     
>     @Override
>     public void reproducir() {
>         System.out.println("🎙️  Reproduciendo podcast: " + episodio);
>         System.out.println("   Minuto: " + minuto);
>     }
>     
>     @Override
>     public void pausar() {
>         System.out.println("⏸️  Podcast pausado en minuto " + minuto);
>     }
>     
>     @Override
>     public void detener() {
>         minuto = 0;
>         System.out.println("⏹️  Podcast detenido");
>     }
> }
> 
> // ✨ POLIMORFISMO CON INTERFACES
> public class ListaReproduccion {
>     private Reproducible[] elementos;
>     private int cantidad;
>     
>     public ListaReproduccion(int capacidad) {
>         elementos = new Reproducible[capacidad];
>         cantidad = 0;
>     }
>     
>     public void agregar(Reproducible elemento) {
>         if (cantidad < elementos.length) {
>             elementos[cantidad] = elemento;
>             cantidad++;
>             System.out.println("✅ Elemento agregado a la lista");
>         }
>     }
>     
>     public void reproducirTodo() {
>         System.out.println("\n🎬 REPRODUCIENDO LISTA COMPLETA");
>         System.out.println("Total elementos: " + cantidad);
>         
>         for (int i = 0; i < cantidad; i++) {
>             System.out.println("\n--- Elemento " + (i + 1) + " ---");
>             elementos[i].reproducir();
>             
>             // Simular reproducción
>             try {
>                 Thread.sleep(1000);
>             } catch (InterruptedException e) {
>                 e.printStackTrace();
>             }
>         }
>         
>         System.out.println("\n✅ Lista reproducida completamente");
>     }
> }
> 
> // USO
> public class TestReproductor {
>     public static void main(String[] args) {
>         ListaReproduccion lista = new ListaReproduccion(10);
>         
>         // Agregar diferentes tipos - todos son Reproducible
>         lista.agregar(new ReproductorVideo("película.mp4"));
>         lista.agregar(new ReproductorAudio("canción.mp3"));
>         lista.agregar(new ReproductorPodcast("Episodio 42"));
>         lista.agregar(new ReproductorVideo("serie_s01e01.mkv"));
>         
>         lista.reproducirTodo();
>     }
> }
> ```

---

## 💡 Ventajas del Polimorfismo

> [!success]- 🎯 Beneficios Prácticos
> 
> **1. Código más flexible y extensible:**
> 
> ```java
> // Sin polimorfismo - código rígido
> public void procesarPagoTarjeta(PagoTarjeta pago) { }
> public void procesarPagoPayPal(PagoPayPal pago) { }
> public void procesarPagoEfectivo(PagoEfectivo pago) { }
> // Agregar nuevo método de pago = modificar código
> 
> // Con polimorfismo - código flexible
> public void procesarPago(MetodoPago pago) {
>     pago.procesar();
> }
> // Agregar nuevo método de pago = NO modificar código
> ```
> 
> **2. Reduce duplicación de código:**
> 
> ```java
> // Array polimórfico
> Figura[] figuras = {
>     new Circulo(5),
>     new Rectangulo(4, 6),
>     new Triangulo(3, 4, 5)
> };
> 
> // Un solo bucle para todas
> double areaTotal = 0;
> for (Figura f : figuras) {
>     areaTotal += f.calcularArea();
> }
> ```
> 
> **3. Facilita el testing:**
> 
> ```java
> interface BaseDatos {
>     void guardar(String datos);
> }
> 
> // Producción
> class MySQLDatabase implements BaseDatos {
>     public void guardar(String datos) {
>         // Guardar en MySQL real
>     }
> }
> 
> // Testing - Mock
> class MockDatabase implements BaseDatos {
>     public void guardar(String datos) {
>         // Simular guardado para pruebas
>     }
> }
> 
> // Código usa la interface - funciona con ambas
> public void procesar(BaseDatos db) {
>     db.guardar("datos");
> }
> ```
> 
> **4. Principio Open/Closed:**
> 
> ```java
> // Abierto para extensión (agregar nuevas clases)
> // Cerrado para modificación (no cambiar código existente)
> 
> abstract class Reporte {
>     public abstract void generar();
> }
> 
> // Agregar nuevo tipo de reporte
> class ReportePDF extends Reporte {
>     public void generar() { /* PDF */ }
> }
> 
> class ReporteExcel extends Reporte {
>     public void generar() { /* Excel */ }
> }
> 
> // Generador no cambia al agregar nuevos tipos
> public void generarReporte(Reporte reporte) {
>     reporte.generar();
> }
> ```

---

## 🎭 Polimorfismo vs Sobrecarga

> [!info]- 📊 Diferencias Clave
> 
> |Aspecto|Polimorfismo (Override)|Sobrecarga (Overload)|
> |---|---|---|
> |**Momento**|Tiempo de ejecución|Tiempo de compilación|
> |**Firma**|Misma firma|Diferente firma|
> |**Herencia**|Requiere herencia|En misma clase|
> |**Método**|Sobreescribe padre|Múltiples versiones|
> |**Binding**|Dinámico (runtime)|Estático (compile-time)|
> |**Tipo retorno**|Mismo (o covariante)|Puede diferir|
> 
> **Ejemplo combinado:**
> 
> ```java
> class Animal {
>     // Sobrecarga en misma clase
>     public void mover() {
>         System.out.println("Animal moviéndose");
>     }
>     
>     public void mover(int distancia) {
>         System.out.println("Animal moviéndose " + distancia + " metros");
>     }
> }
> 
> class Perro extends Animal {
>     // Polimorfismo - sobreescribe método padre
> 	    
> 
> 
> @Override
> public void mover() {
>     System.out.println("Perro corriendo");
> }
> 
> // Sobrecarga - agrega nueva versión
> public void mover(String direccion) {
>     System.out.println("Perro corriendo hacia " + direccion);
> }
> 
> 
> }
> ```
>// USO Animal animal = new Perro(); animal.mover(); // Polimorfismo: "Perro corriendo" animal.mover(10); // Sobrecarga: hereda del padre
Perro perro = new Perro(); perro.mover(); // Polimorfismo perro.mover(5); // Sobrecarga (heredada) perro.mover("norte"); // Sobrecarga (nueva)

---

## 🔗 Ligadura Dinámica (Dynamic Binding)

> [!note]- ⚡ Cómo Funciona Internamente **Concepto:** Java decide en **tiempo de ejecución** qué método llamar basándose en el tipo **real** del objeto, no en el tipo de la referencia.
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
>         System.out.println("Guau!");
>     }
> }
> 
> public class Gato extends Animal {
>     @Override
>     public void hacerSonido() {
>         System.out.println("Miau!");
>     }
> }
> 
> // ========================
> // LIGADURA DINÁMICA
> // ========================
> public class TestBinding {
>     public static void main(String[] args) {
>         // Tipo de referencia: Animal
>         // Tipo real: Perro
>         Animal animal1 = new Perro();
>         
>         // Tipo de referencia: Animal
>         // Tipo real: Gato
>         Animal animal2 = new Gato();
>         
>         // ✨ Java decide EN EJECUCIÓN basándose en tipo REAL
>         animal1.hacerSonido();  // "Guau!" - método de Perro
>         animal2.hacerSonido();  // "Miau!" - método de Gato
>         
>         // Cambiar objeto en tiempo de ejecución
>         Animal animal = null;
>         
>         int random = (int)(Math.random() * 2);
>         if (random == 0) {
>             animal = new Perro();
>         } else {
>             animal = new Gato();
>         }
>         
>         // No sabemos hasta ejecutar qué sonido hará
>         animal.hacerSonido();  // Decidido en runtime
>     }
>     
>     // Método que aprovecha ligadura dinámica
>     public static void hacerHablar(Animal animal) {
>         // No sabemos qué tipo es hasta que se ejecuta
>         animal.hacerSonido();
>     }
> }
> ```
> 
> **Proceso interno:**
> 
> ```java
> Animal animal = new Perro();
> animal.hacerSonido();
> 
> // 1. Java mira el TIPO REAL del objeto (Perro)
> // 2. Busca el método hacerSonido() en Perro
> // 3. Si existe, lo ejecuta
> // 4. Si no existe, busca en Animal (padre)
> // 5. Continúa subiendo en la jerarquía hasta encontrarlo
> ```

---

## 🎨 Patrones de Diseño con Polimorfismo

> [!example]- 🏗️ Factory Pattern
> 
> ```java
> // Interface común
> interface Vehiculo {
>     void fabricar();
>     double calcularPrecio();
> }
> 
> // Implementaciones concretas
> class Auto implements Vehiculo {
>     @Override
>     public void fabricar() {
>         System.out.println("🚗 Fabricando auto...");
>     }
>     
>     @Override
>     public double calcularPrecio() {
>         return 20000;
>     }
> }
> 
> class Moto implements Vehiculo {
>     @Override
>     public void fabricar() {
>         System.out.println("🏍️  Fabricando moto...");
>     }
>     
>     @Override
>     public double calcularPrecio() {
>         return 5000;
>     }
> }
> 
> class Camion implements Vehiculo {
>     @Override
>     public void fabricar() {
>         System.out.println("🚚 Fabricando camión...");
>     }
>     
>     @Override
>     public double calcularPrecio() {
>         return 50000;
>     }
> }
> 
> // ✨ Factory - Crea objetos polimórficamente
> class FabricaVehiculos {
>     public static Vehiculo crearVehiculo(String tipo) {
>         switch (tipo.toLowerCase()) {
>             case "auto":
>                 return new Auto();
>             case "moto":
>                 return new Moto();
>             case "camion":
>                 return new Camion();
>             default:
>                 throw new IllegalArgumentException("Tipo desconocido: " + tipo);
>         }
>     }
> }
> 
> // USO
> public class TestFactory {
>     public static void main(String[] args) {
>         String[] pedidos = {"auto", "moto", "camion", "auto"};
>         
>         double totalVentas = 0;
>         
>         for (String tipo : pedidos) {
>             // Factory crea el objeto correcto
>             Vehiculo vehiculo = FabricaVehiculos.crearVehiculo(tipo);
>             
>             // Polimorfismo - todos tratados igual
>             vehiculo.fabricar();
>             double precio = vehiculo.calcularPrecio();
>             totalVentas += precio;
>             
>             System.out.println("   Precio: $" + precio);
>         }
>         
>         System.out.println("\n💰 Total ventas: $" + totalVentas);
>     }
> }
> ```

> [!example]- 🎯 Strategy Pattern
> 
> ```java
> // Interface para estrategias
> interface EstrategiaOrdenamiento {
>     void ordenar(int[] array);
> }
> 
> // Diferentes estrategias
> class BubbleSort implements EstrategiaOrdenamiento {
>     @Override
>     public void ordenar(int[] array) {
>         System.out.println("🔵 Ordenando con Bubble Sort...");
>         // Implementación de bubble sort
>         for (int i = 0; i < array.length - 1; i++) {
>             for (int j = 0; j < array.length - i - 1; j++) {
>                 if (array[j] > array[j + 1]) {
>                     int temp = array[j];
>                     array[j] = array[j + 1];
>                     array[j + 1] = temp;
>                 }
>             }
>         }
>         System.out.println("✅ Ordenamiento completado");
>     }
> }
> 
> class QuickSort implements EstrategiaOrdenamiento {
>     @Override
>     public void ordenar(int[] array) {
>         System.out.println("⚡ Ordenando con Quick Sort...");
>         quickSort(array, 0, array.length - 1);
>         System.out.println("✅ Ordenamiento completado");
>     }
>     
>     private void quickSort(int[] arr, int low, int high) {
>         if (low < high) {
>             int pi = partition(arr, low, high);
>             quickSort(arr, low, pi - 1);
>             quickSort(arr, pi + 1, high);
>         }
>     }
>     
>     private int partition(int[] arr, int low, int high) {
>         int pivot = arr[high];
>         int i = (low - 1);
>         for (int j = low; j < high; j++) {
>             if (arr[j] < pivot) {
>                 i++;
>                 int temp = arr[i];
>                 arr[i] = arr[j];
>                 arr[j] = temp;
>             }
>         }
>         int temp = arr[i + 1];
>         arr[i + 1] = arr[high];
>         arr[high] = temp;
>         return i + 1;
>     }
> }
> 
> // Contexto que usa la estrategia
> class OrdenadorDatos {
>     private EstrategiaOrdenamiento estrategia;
>     
>     public void setEstrategia(EstrategiaOrdenamiento estrategia) {
>         this.estrategia = estrategia;
>     }
>     
>     public void ordenarDatos(int[] datos) {
>         if (estrategia == null) {
>             System.out.println("❌ No hay estrategia definida");
>             return;
>         }
>         
>         System.out.println("📊 Datos originales: ");
>         mostrarArray(datos);
>         
>         estrategia.ordenar(datos);
>         
>         System.out.println("📊 Datos ordenados: ");
>         mostrarArray(datos);
>     }
>     
>     private void mostrarArray(int[] arr) {
>         for (int num : arr) {
>             System.out.print(num + " ");
>         }
>         System.out.println();
>     }
> }
> 
> // USO
> public class TestStrategy {
>     public static void main(String[] args) {
>         int[] datos1 = {64, 34, 25, 12, 22, 11, 90};
>         int[] datos2 = {5, 2, 9, 1, 5, 6};
>         
>         OrdenadorDatos ordenador = new OrdenadorDatos();
>         
>         // Cambiar estrategia dinámicamente
>         System.out.println("=== CONJUNTO 1 ===");
>         ordenador.setEstrategia(new BubbleSort());
>         ordenador.ordenarDatos(datos1.clone());
>         
>         System.out.println("\n=== CONJUNTO 2 ===");
>         ordenador.setEstrategia(new QuickSort());
>         ordenador.ordenarDatos(datos2.clone());
>     }
> }
> ```

---

## 🎯 Ejemplo Avanzado: Sistema de Formas Geométricas

> [!example]- 📐 Polimorfismo Completo
> 
> ```java
> // ========================
> // CLASE ABSTRACTA BASE
> // ========================
> public abstract class Forma {
>     protected String color;
>     protected boolean relleno;
>     
>     public Forma(String color, boolean relleno) {
>         this.color = color;
>         this.relleno = relleno;
>     }
>     
>     // Métodos abstractos - cada forma los implementa
>     public abstract double calcularArea();
>     public abstract double calcularPerimetro();
>     public abstract void dibujar();
>     
>     // Método concreto común
>     public void mostrarInfo() {
>         System.out.println("Color: " + color);
>         System.out.println("Relleno: " + (relleno ? "Sí" : "No"));
>         System.out.println("Área: " + String.format("%.2f", calcularArea()));
>         System.out.println("Perímetro: " + String.format("%.2f", calcularPerimetro()));
>     }
>     
>     // Getters y Setters
>     public String getColor() { return color; }
>     public void setColor(String color) { this.color = color; }
>     public boolean isRelleno() { return relleno; }
>     public void setRelleno(boolean relleno) { this.relleno = relleno; }
> }
> 
> // ========================
> // FORMAS CONCRETAS
> // ========================
> public class Circulo extends Forma {
>     private double radio;
>     
>     public Circulo(String color, boolean relleno, double radio) {
>         super(color, relleno);
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
>     
>     @Override
>     public void dibujar() {
>         String simbolo = isRelleno() ? "●" : "○";
>         System.out.println("\n" + simbolo + " CÍRCULO " + simbolo);
>         mostrarInfo();
>     }
>     
>     public double getRadio() { return radio; }
> }
> 
> public class Rectangulo extends Forma {
>     private double ancho;
>     private double alto;
>     
>     public Rectangulo(String color, boolean relleno, double ancho, double alto) {
>         super(color, relleno);
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
>     public double calcularPerimetro() {
>         return 2 * (ancho + alto);
>     }
>     
>     @Override
>     public void dibujar() {
>         String simbolo = isRelleno() ? "■" : "□";
>         System.out.println("\n" + simbolo + " RECTÁNGULO " + simbolo);
>         mostrarInfo();
>         System.out.println("Dimensiones: " + ancho + " x " + alto);
>     }
>     
>     public double getAncho() { return ancho; }
>     public double getAlto() { return alto; }
> }
> 
> public class Triangulo extends Forma {
>     private double lado1;
>     private double lado2;
>     private double lado3;
>     
>     public Triangulo(String color, boolean relleno, 
>                     double lado1, double lado2, double lado3) {
>         super(color, relleno);
>         if (!esTrianguloValido(lado1, lado2, lado3)) {
>             throw new IllegalArgumentException("Lados no forman un triángulo válido");
>         }
>         this.lado1 = lado1;
>         this.lado2 = lado2;
>         this.lado3 = lado3;
>     }
>     
>     private boolean esTrianguloValido(double a, double b, double c) {
>         return (a + b > c) && (a + c > b) && (b + c > a);
>     }
>     
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
>     @Override
>     public void dibujar() {
>         String simbolo = isRelleno() ? "▲" : "△";
>         System.out.println("\n" + simbolo + " TRIÁNGULO " + simbolo);
>         mostrarInfo();
>         System.out.println("Lados: " + lado1 + ", " + lado2 + ", " + lado3);
>     }
> }
> 
> // ========================
> // GESTOR DE FORMAS
> // ========================
> public class GestorFormas {
>     private Forma[] formas;
>     private int cantidad;
>     
>     public GestorFormas(int capacidad) {
>         formas = new Forma[capacidad];
>         cantidad = 0;
>     }
>     
>     public void agregarForma(Forma forma) {
>         if (cantidad < formas.length) {
>             formas[cantidad] = forma;
>             cantidad++;
>             System.out.println("✅ Forma agregada");
>         } else {
>             System.out.println("❌ Capacidad máxima alcanzada");
>         }
>     }
>     
>     // ✨ Polimorfismo - trabaja con cualquier forma
>     public void dibujarTodas() {
>         System.out.println("\n╔════════════════════════════════════╗");
>         System.out.println("║     DIBUJANDO TODAS LAS FORMAS     ║");
>         System.out.println("╚════════════════════════════════════╝");
>         
>         for (int i = 0; i < cantidad; i++) {
>             formas[i].dibujar();
>         }
>     }
>     
>     public double calcularAreaTotal() {
>         double total = 0;
>         for (int i = 0; i < cantidad; i++) {
>             total += formas[i].calcularArea();
>         }
>         return total;
>     }
>     
>     public double calcularPerimetroTotal() {
>         double total = 0;
>         for (int i = 0; i < cantidad; i++) {
>             total += formas[i].calcularPerimetro();
>         }
>         return total;
>     }
>     
>     public void mostrarEstadisticas() {
>         System.out.println("\n📊 ESTADÍSTICAS");
>         System.out.println("Total de formas: " + cantidad);
>         System.out.printf("Área total: %.2f\n", calcularAreaTotal());
>         System.out.printf("Perímetro total: %.2f\n", calcularPerimetroTotal());
>         
>         // Contar tipos
>         int circulos = 0, rectangulos = 0, triangulos = 0;
>         
>         for (int i = 0; i < cantidad; i++) {
>             if (formas[i] instanceof Circulo) {
>                 circulos++;
>             } else if (formas[i] instanceof Rectangulo) {
>                 rectangulos++;
>             } else if (formas[i] instanceof Triangulo) {
>                 triangulos++;
>             }
>         }
>         
>         System.out.println("\nDistribución:");
>         System.out.println("  Círculos: " + circulos);
>         System.out.println("  Rectángulos: " + rectangulos);
>         System.out.println("  Triángulos: " + triangulos);
>     }
>     
>     public void filtrarPorColor(String color) {
>         System.out.println("\n🎨 FORMAS DE COLOR: " + color);
>         boolean encontrado = false;
>         
>         for (int i = 0; i < cantidad; i++) {
>             if (formas[i].getColor().equalsIgnoreCase(color)) {
>                 formas[i].dibujar();
>                 encontrado = true;
>             }
>         }
>         
>         if (!encontrado) {
>             System.out.println("No se encontraron formas de ese color");
>         }
>     }
>     
>     public Forma encontrarMayorArea() {
>         if (cantidad == 0) return null;
>         
>         Forma mayor = formas[0];
>         for (int i = 1; i < cantidad; i++) {
>             if (formas[i].calcularArea() > mayor.calcularArea()) {
>                 mayor = formas[i];
>             }
>         }
>         return mayor;
>     }
> }
> 
> // ========================
> // PROGRAMA PRINCIPAL
> // ========================
> public class SistemaFormas {
>     public static void main(String[] args) {
>         GestorFormas gestor = new GestorFormas(10);
>         
>         // Crear diferentes formas
>         Forma circulo1 = new Circulo("Rojo", true, 5.0);
>         Forma rectangulo1 = new Rectangulo("Azul", false, 4.0, 6.0);
>         Forma triangulo1 = new Triangulo("Verde", true, 3.0, 4.0, 5.0);
>         Forma circulo2 = new Circulo("Amarillo", false, 3.0);
>         Forma rectangulo2 = new Rectangulo("Rojo", true, 5.0, 5.0);
>         
>         // Agregar al gestor
>         gestor.agregarForma(circulo1);
>         gestor.agregarForma(rectangulo1);
>         gestor.agregarForma(triangulo1);
>         gestor.agregarForma(circulo2);
>         gestor.agregarForma(rectangulo2);
>         
>         // Dibujar todas (polimorfismo)
>         gestor.dibujarTodas();
>         
>         // Estadísticas
>         gestor.mostrarEstadisticas();
>         
>         // Filtrar por color
>         gestor.filtrarPorColor("Rojo");
>         
>         // Encontrar mayor área
>         Forma mayor = gestor.encontrarMayorArea();
>         System.out.println("\n🏆 FORMA CON MAYOR ÁREA:");
>         if (mayor != null) {
>             mayor.dibujar();
>         }
>         
>         // Demostrar polimorfismo directo
>         System.out.println("\n🎯 POLIMORFISMO DIRECTO:");
>         Forma[] formas = {
>             new Circulo("Morado", true, 2.5),
>             new Rectangulo("Naranja", false, 3.0, 4.0),
>             new Triangulo("Rosa", true, 2.0, 3.0, 4.0)
>         };
>         
>         for (Forma f : formas) {
>             // Mismo código, diferentes comportamientos
>             f.dibujar();
>         }
>     }
> }
> ```

---

## ⚠️ Errores Comunes

> [!warning]- 🚫 Problemas Frecuentes
> 
> **1. Olvidar @Override:**
> 
> ```java
> class Animal {
>     public void hacerSonido() { }
> }
> 
> class Perro extends Animal {
>     // ❌ Error de tipeo - NO sobreescribe (método nuevo)
>     public void hacerSonidoo() {  // Typo
>         System.out.println("Guau");
>     }
>     
>     // ✅ Con @Override detecta el error
>     @Override
>     public void hacerSonido() {  // Correcto
>         System.out.println("Guau");
>     }
> }
> ```
> 
> **2. Confundir sobrecarga con sobreescritura:**
> 
> ```java
> class Padre {
>     public void metodo(int x) {
>         System.out.println("Padre: " + x);
>     }
> }
> 
> class Hijo extends Padre {
>     // ❌ NO es sobreescritura - es sobrecarga (diferente parámetro)
>     public void metodo(double x) {
>         System.out.println("Hijo: " + x);
>     }
> }
> 
> Hijo h = new Hijo();
> h.metodo(5);     // Llama al método del padre (int)
> h.metodo(5.0);   // Llama al método del hijo (double)
> ```
> 
> **3. Casting incorrecto:**
> 
> ```java
> Animal animal = new Gato();
> 
> // ❌ No verificar tipo antes de cast
> Perro perro = (Perro) animal;  // ClassCastException
> 
> // ✅ Verificar con instanceof
> if (animal instanceof Perro) {
>     Perro perro = (Perro) animal;
>     perro.ladrar();
> }
> ```
> 
> **4. Modificadores incompatibles:**
> 
> ```java
> class Padre {
>     public void metodo() { }
> }
> 
> class Hijo extends Padre {
>     // ❌ ERROR - No puede ser más restrictivo
>     private void metodo() { }  // Error de compilación
>     
>     // ✅ Puede ser igual o menos restrictivo
>     public void metodo() { }   // OK
> }
> ```

---

## 📚 Resumen Ejecutivo

> [!quote]- 🌟 Puntos Clave **Has aprendido:**
> 
> - ✅ Polimorfismo en tiempo de compilación (sobrecarga)
> - ✅ Polimorfismo en tiempo de ejecución (sobreescritura)
> - ✅ Ligadura dinámica y cómo funciona
> - ✅ Casting y uso de instanceof
> - ✅ Polimorfismo con interfaces
> - ✅ Patrones de diseño (Factory, Strategy)
> - ✅ Ventajas del polimorfismo
> - ✅ Errores comunes y cómo evitarlos
> 
> **Principios clave:**
> 
> - 🎯 **"Programar para interfaces, no implementaciones"**
> - 🎯 **"Un tipo, múltiples formas"**
> - 🎯 **"Mismo mensaje, diferentes respuestas"**
> 
> **Cuándo usar:**
> 
> - ✅ Código que trabaja con múltiples tipos relacionados
> - ✅ Necesitas extensibilidad sin modificar código existente
> - ✅ Quieres reducir duplicación de código
> - ✅ Implementas patrones de diseño
> 
> **Próximos temas:**
> 
> - **[[07 - Excepciones]]** - Manejo polimórfico de errores
> - **[[08 - Colecciones]]** - Polimorfismo con estructuras de datos
> - **[[09 - Genéricos]]** - Polimorfismo paramétrico

---

**Tags:** #java #poo #polimorfismo #override #overload #herencia #interfaces #dynamic-binding #casting #instanceof #design-patterns #factory #strategy