# 🎨 Enumeraciones (`enum`) en Java

## 🎯 Introducción

> [!info]- 💡 ¿Qué son las Enumeraciones? Una **enumeración** (`enum`) es un tipo de dato especial que representa un **conjunto fijo de constantes**.
> 
> **Analogía:** Como los días de la semana
> 
> - Solo hay 7 días: Lunes, Martes, Miércoles, etc.
> - No puedes inventar un octavo día
> - Son valores predefinidos y conocidos
> 
> **Ventajas sobre constantes simples:**
> 
> - ✅ **Type-safe:** El compilador valida los valores
> - ✅ **Legibles:** Código más expresivo y claro
> - ✅ **Mantenibles:** Cambios centralizados
> - ✅ **Comportamiento:** Pueden tener métodos y atributos
> - ✅ **Espacio de nombres:** Evita colisiones

---

## 📝 Sintaxis Básica

### Declaración Simple

> [!example]- 🔤 Enum Básico
> 
> ```java
> // Declaración de enum
> public enum DiaSemana {
>     LUNES, MARTES, MIERCOLES, JUEVES, VIERNES, SABADO, DOMINGO
> }
> 
> // Uso básico
> public class Main {
>     public static void main(String[] args) {
>         // Declarar variable enum
>         DiaSemana dia = DiaSemana.LUNES;
>         
>         System.out.println("Día: " + dia);  // "Día: LUNES"
>         
>         // Comparación
>         if (dia == DiaSemana.LUNES) {
>             System.out.println("¡Inicio de semana!");
>         }
>         
>         // Switch con enum
>         switch (dia) {
>             case LUNES:
>                 System.out.println("Día laboral");
>                 break;
>             case SABADO:
>             case DOMINGO:
>                 System.out.println("Fin de semana");
>                 break;
>             default:
>                 System.out.println("Día normal");
>         }
>     }
> }
> ```
> 
> **Comparación con constantes:**
> 
> ```java
> // ❌ SIN ENUM - Propenso a errores
> public class DiaSemana {
>     public static final int LUNES = 1;
>     public static final int MARTES = 2;
>     // ...
> }
> 
> int dia = 99;  // ❌ Valor inválido compilado sin error
> if (dia == DiaSemana.LUNES) { /* ... */ }
> 
> // ✅ CON ENUM - Type-safe
> public enum DiaSemana {
>     LUNES, MARTES, MIERCOLES // ...
> }
> 
> DiaSemana dia = DiaSemana.LUNES;  // ✅ Solo valores válidos
> // dia = 99;  // ❌ Error de compilación
> ```

---

## 🎯 Métodos Integrados

> [!success]- 🛠️ Métodos que Todo Enum Tiene Todos los enums heredan de `java.lang.Enum` y tienen métodos útiles:
> 
> ```java
> public enum Color {
>     ROJO, VERDE, AZUL, AMARILLO
> }
> 
> public class Main {
>     public static void main(String[] args) {
>         Color color = Color.ROJO;
>         
>         // 1. name() - Retorna el nombre como String
>         System.out.println(color.name());  // "ROJO"
>         
>         // 2. ordinal() - Retorna la posición (índice)
>         System.out.println(color.ordinal());  // 0 (primera posición)
>         System.out.println(Color.AZUL.ordinal());  // 2
>         
>         // 3. values() - Retorna array con todos los valores
>         Color[] colores = Color.values();
>         System.out.println("Colores disponibles:");
>         for (Color c : colores) {
>             System.out.println("- " + c);
>         }
>         
>         // 4. valueOf(String) - Convierte String a enum
>         Color colorDesdeTexto = Color.valueOf("VERDE");
>         System.out.println(colorDesdeTexto);  // VERDE
>         
>         // ⚠️ Cuidado: lanza IllegalArgumentException si no existe
>         try {
>             Color invalido = Color.valueOf("MORADO");
>         } catch (IllegalArgumentException e) {
>             System.out.println("Color no existe");
>         }
>         
>         // 5. toString() - Similar a name()
>         System.out.println(color.toString());  // "ROJO"
>         
>         // 6. compareTo() - Compara por ordinal
>         int comparacion = Color.ROJO.compareTo(Color.AZUL);
>         System.out.println(comparacion);  // Negativo (ROJO < AZUL)
>     }
> }
> ```

---

## 🎨 Enums con Atributos y Métodos

### Enum con Constructor y Atributos

> [!example]- 📦 Enums Más Complejos
> 
> ```java
> public enum Planeta {
>     // Constantes con valores
>     MERCURIO(3.303e23, 2.4397e6),
>     VENUS(4.869e24, 6.0518e6),
>     TIERRA(5.976e24, 6.37814e6),
>     MARTE(6.421e23, 3.3972e6),
>     JUPITER(1.9e27, 7.1492e7),
>     SATURNO(5.688e26, 6.0268e7),
>     URANO(8.686e25, 2.5559e7),
>     NEPTUNO(1.024e26, 2.4746e7);
>     
>     // Atributos privados
>     private final double masa;   // en kilogramos
>     private final double radio;  // en metros
>     
>     // Constante universal
>     private static final double G = 6.67300E-11;
>     
>     // Constructor (SIEMPRE privado en enums)
>     Planeta(double masa, double radio) {
>         this.masa = masa;
>         this.radio = radio;
>     }
>     
>     // Getters
>     public double getMasa() { return masa; }
>     public double getRadio() { return radio; }
>     
>     // Método calculado
>     public double gravedadSuperficial() {
>         return G * masa / (radio * radio);
>     }
>     
>     public double pesoSuperficial(double masaObjeto) {
>         return masaObjeto * gravedadSuperficial();
>     }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         double pesoEnTierra = 75.0;  // kg
>         
>         System.out.println("Tu peso en diferentes planetas:");
>         for (Planeta p : Planeta.values()) {
>             double peso = p.pesoSuperficial(pesoEnTierra);
>             System.out.printf("%s: %.2f kg%n", p, peso);
>         }
>         
>         // Acceder a atributos específicos
>         System.out.println("\nDatos de la Tierra:");
>         System.out.println("Masa: " + Planeta.TIERRA.getMasa());
>         System.out.println("Radio: " + Planeta.TIERRA.getRadio());
>         System.out.println("Gravedad: " + Planeta.TIERRA.gravedadSuperficial());
>     }
> }
> ```

### Enum con Múltiples Atributos

> [!tip]- 🎯 Ejemplo Práctico: Sistema de Pizzas
> 
> ```java
> public enum TamañoPizza {
>     PEQUEÑA("Pequeña", 8, 6.99, 1),
>     MEDIANA("Mediana", 12, 9.99, 2),
>     GRANDE("Grande", 16, 12.99, 3),
>     FAMILIAR("Familiar", 20, 16.99, 4);
>     
>     private final String nombre;
>     private final int pulgadas;
>     private final double precioBase;
>     private final int porciones;
>     
>     TamañoPizza(String nombre, int pulgadas, double precioBase, int porciones) {
>         this.nombre = nombre;
>         this.pulgadas = pulgadas;
>         this.precioBase = precioBase;
>         this.porciones = porciones;
>     }
>     
>     public String getNombre() { return nombre; }
>     public int getPulgadas() { return pulgadas; }
>     public double getPrecioBase() { return precioBase; }
>     public int getPorciones() { return porciones; }
>     
>     public double calcularArea() {
>         double radio = pulgadas / 2.0;
>         return Math.PI * radio * radio;
>     }
>     
>     public double precioPorPorcion() {
>         return precioBase / porciones;
>     }
>     
>     @Override
>     public String toString() {
>         return String.format("%s (%d\", $%.2f)", nombre, pulgadas, precioBase);
>     }
> }
> 
> public enum TipoIngrediente {
>     PEPPERONI("Pepperoni", 1.50, 80),
>     CHAMPIÑONES("Champiñones", 1.00, 20),
>     ACEITUNAS("Aceitunas", 1.00, 15),
>     PIMIENTO("Pimiento", 0.75, 10),
>     CEBOLLA("Cebolla", 0.75, 5),
>     EXTRA_QUESO("Extra Queso", 2.00, 100);
>     
>     private final String nombre;
>     private final double precioExtra;
>     private final int calorias;
>     
>     TipoIngrediente(String nombre, double precioExtra, int calorias) {
>         this.nombre = nombre;
>         this.precioExtra = precioExtra;
>         this.calorias = calorias;
>     }
>     
>     public String getNombre() { return nombre; }
>     public double getPrecioExtra() { return precioExtra; }
>     public int getCalorias() { return calorias; }
> }
> 
> // Clase que usa los enums
> public class Pizza {
>     private TamañoPizza tamaño;
>     private TipoIngrediente[] ingredientes;
>     private int totalIngredientes;
>     
>     public Pizza(TamañoPizza tamaño) {
>         this.tamaño = tamaño;
>         this.ingredientes = new TipoIngrediente[10];
>         this.totalIngredientes = 0;
>     }
>     
>     public void agregarIngrediente(TipoIngrediente ingrediente) {
>         if (totalIngredientes < ingredientes.length) {
>             ingredientes[totalIngredientes] = ingrediente;
>             totalIngredientes++;
>             System.out.println("✓ " + ingrediente.getNombre() + " agregado");
>         }
>     }
>     
>     public double calcularPrecio() {
>         double precio = tamaño.getPrecioBase();
>         for (int i = 0; i < totalIngredientes; i++) {
>             precio += ingredientes[i].getPrecioExtra();
>         }
>         return precio;
>     }
>     
>     public int calcularCalorias() {
>         int calorias = 200 * tamaño.getPorciones();  // Base
>         for (int i = 0; i < totalIngredientes; i++) {
>             calorias += ingredientes[i].getCalorias();
>         }
>         return calorias;
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("\n=== PIZZA ===");
>         System.out.println("Tamaño: " + tamaño);
>         System.out.println("Ingredientes:");
>         for (int i = 0; i < totalIngredientes; i++) {
>             System.out.println("  - " + ingredientes[i].getNombre());
>         }
>         System.out.println("Precio total: $" + String.format("%.2f", calcularPrecio()));
>         System.out.println("Calorías totales: " + calcularCalorias());
>     }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         Pizza miPizza = new Pizza(TamañoPizza.GRANDE);
>         miPizza.agregarIngrediente(TipoIngrediente.PEPPERONI);
>         miPizza.agregarIngrediente(TipoIngrediente.CHAMPIÑONES);
>         miPizza.agregarIngrediente(TipoIngrediente.EXTRA_QUESO);
>         
>         miPizza.mostrarInfo();
>     }
> }
> ```

---

## 🎭 Enums con Métodos Abstractos

> [!warning]- ⚙️ Comportamiento Específico por Constante Cada constante puede tener su propia implementación de un método:
> 
> ```java
> public enum Operacion {
>     SUMA {
>         @Override
>         public double aplicar(double x, double y) {
>             return x + y;
>         }
>     },
>     RESTA {
>         @Override
>         public double aplicar(double x, double y) {
>             return x - y;
>         }
>     },
>     MULTIPLICACION {
>         @Override
>         public double aplicar(double x, double y) {
>             return x * y;
>         }
>     },
>     DIVISION {
>         @Override
>         public double aplicar(double x, double y) {
>             if (y == 0) {
>                 throw new ArithmeticException("División por cero");
>             }
>             return x / y;
>         }
>     };
>     
>     // Método abstracto que cada constante debe implementar
>     public abstract double aplicar(double x, double y);
> }
> 
> // USO:
> public class Calculadora {
>     public static void main(String[] args) {
>         double a = 10, b = 5;
>         
>         System.out.println("Operaciones con " + a + " y " + b + ":");
>         for (Operacion op : Operacion.values()) {
>             double resultado = op.aplicar(a, b);
>             System.out.println(op + ": " + resultado);
>         }
>         
>         // Uso específico
>         double suma = Operacion.SUMA.aplicar(15, 25);
>         System.out.println("\n15 + 25 = " + suma);
>     }
> }
> ```

---

## 🎯 Casos de Uso Comunes

### 1️⃣ Estados de una Orden

> [!example]- 📦 Gestión de Estados
> 
> ```java
> public enum EstadoOrden {
>     PENDIENTE("Pendiente", false, false),
>     PROCESANDO("En proceso", false, false),
>     ENVIADO("Enviado", true, false),
>     ENTREGADO("Entregado", true, true),
>     CANCELADO("Cancelado", false, true);
>     
>     private final String descripcion;
>     private final boolean esRastreable;
>     private final boolean esFinal;
>     
>     EstadoOrden(String descripcion, boolean esRastreable, boolean esFinal) {
>         this.descripcion = descripcion;
>         this.esRastreable = esRastreable;
>         this.esFinal = esFinal;
>     }
>     
>     public String getDescripcion() { return descripcion; }
>     public boolean esRastreable() { return esRastreable; }
>     public boolean esFinal() { return esFinal; }
>     
>     public boolean puedeTransicionarA(EstadoOrden nuevoEstado) {
>         if (this.esFinal) return false;
>         if (this == CANCELADO) return false;
>         return true;
>     }
> }
> 
> public class Orden {
>     private String id;
>     private EstadoOrden estado;
>     
>     public Orden(String id) {
>         this.id = id;
>         this.estado = EstadoOrden.PENDIENTE;
>     }
>     
>     public void cambiarEstado(EstadoOrden nuevoEstado) {
>         if (estado.puedeTransicionarA(nuevoEstado)) {
>             System.out.println("Cambiando de " + estado + " a " + nuevoEstado);
>             this.estado = nuevoEstado;
>         } else {
>             System.out.println("❌ No se puede cambiar de " + estado + " a " + nuevoEstado);
>         }
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("\nOrden: " + id);
>         System.out.println("Estado: " + estado.getDescripcion());
>         System.out.println("Rastreable: " + (estado.esRastreable() ? "Sí" : "No"));
>     }
> }
> ```

### 2️⃣ Niveles de Log

> [!note]- 📝 Sistema de Logging
> 
> ```java
> public enum NivelLog {
>     DEBUG(1, "DEBUG", "\u001B[36m"),    // Cyan
>     INFO(2, "INFO", "\u001B[32m"),      // Green
>     WARNING(3, "WARN", "\u001B[33m"),   // Yellow
>     ERROR(4, "ERROR", "\u001B[31m"),    // Red
>     FATAL(5, "FATAL", "\u001B[35m");    // Magenta
>     
>     private final int prioridad;
>     private final String etiqueta;
>     private final String color;
>     private static final String RESET = "\u001B[0m";
>     
>     NivelLog(int prioridad, String etiqueta, String color) {
>         this.prioridad = prioridad;
>         this.etiqueta = etiqueta;
>         this.color = color;
>     }
>     
>     public boolean esMasImportanteQue(NivelLog otro) {
>         return this.prioridad > otro.prioridad;
>     }
>     
>     public String formatear(String mensaje) {
>         return color + "[" + etiqueta + "] " + mensaje + RESET;
>     }
> }
> 
> public class Logger {
>     private NivelLog nivelMinimo;
>     
>     public Logger(NivelLog nivelMinimo) {
>         this.nivelMinimo = nivelMinimo;
>     }
>     
>     public void log(NivelLog nivel, String mensaje) {
>         if (nivel.esMasImportanteQue(nivelMinimo) || nivel == nivelMinimo) {
>             System.out.println(nivel.formatear(mensaje));
>         }
>     }
>     
>     public static void main(String[] args) {
>         Logger logger = new Logger(NivelLog.INFO);
>         
>         logger.log(NivelLog.DEBUG, "Esto no se muestra");
>         logger.log(NivelLog.INFO, "Aplicación iniciada");
>         logger.log(NivelLog.WARNING, "Memoria baja");
>         logger.log(NivelLog.ERROR, "Error de conexión");
>     }
> }
> ```

### 3️⃣ Días de la Semana con Lógica

> [!success]- 📅 Calendario Inteligente
> 
> ```java
> public enum DiaSemana {
>     LUNES(1, "Lunes", true),
>     MARTES(2, "Martes", true),
>     MIERCOLES(3, "Miércoles", true),
>     JUEVES(4, "Jueves", true),
>     VIERNES(5, "Viernes", true),
>     SABADO(6, "Sábado", false),
>     DOMINGO(7, "Domingo", false);
>     
>     private final int numero;
>     private final String nombre;
>     private final boolean esLaboral;
>     
>     DiaSemana(int numero, String nombre, boolean esLaboral) {
>         this.numero = numero;
>         this.nombre = nombre;
>         this.esLaboral = esLaboral;
>     }
>     
>     public boolean esLaboral() { return esLaboral; }
>     public boolean esFinDeSemana() { return !esLaboral; }
>     
>     public DiaSemana siguiente() {
>         DiaSemana[] dias = values();
>         return dias[(this.ordinal() + 1) % dias.length];
>     }
>     
>     public DiaSemana anterior() {
>         DiaSemana[] dias = values();
>         int index = (this.ordinal() - 1 + dias.length) % dias.length;
>         return dias[index];
>     }
>     
>     public int diasHasta(DiaSemana otro) {
>         int diferencia = otro.numero - this.numero;
>         if (diferencia < 0) diferencia += 7;
>         return diferencia;
>     }
>     
>     @Override
>     public String toString() {
>         return nombre;
>     }
>     
>     public static void main(String[] args) {
>         DiaSemana hoy = DiaSemana.MIERCOLES;
>         
>         System.out.println("Hoy es: " + hoy);
>         System.out.println("Es laboral: " + hoy.esLaboral());
>         System.out.println("Mañana es: " + hoy.siguiente());
>         System.out.println("Ayer fue: " + hoy.anterior());
>         System.out.println("Días hasta el viernes: " + 
>                            hoy.diasHasta(DiaSemana.VIERNES));
>     }
> }
> ```

---

## 🎨 Ejemplo Completo: Sistema de Tarjetas

> [!example]- 🃏 Baraja de Cartas
> 
> ```java
> // Enum para Palo
> public enum Palo {
>     CORAZONES("♥", "Rojo"),
>     DIAMANTES("♦", "Rojo"),
>     TREBOLES("♣", "Negro"),
>     PICAS("♠", "Negro");
>     
>     private final String simbolo;
>     private final String color;
>     
>     Palo(String simbolo, String color) {
>         this.simbolo = simbolo;
>         this.color = color;
>     }
>     
>     public String getSimbolo() { return simbolo; }
>     public String getColor() { return color; }
> }
> 
> // Enum para Rango
> public enum Rango {
>     DOS(2), TRES(3), CUATRO(4), CINCO(5), SEIS(6), 
>     SIETE(7), OCHO(8), NUEVE(9), DIEZ(10),
>     JOTA(10), REINA(10), REY(10), AS(11);
>     
>     private final int valor;
>     
>     Rango(int valor) {
>         this.valor = valor;
>     }
>     
>     public int getValor() { return valor; }
> }
> 
> // Clase Carta que usa los enums
> public class Carta {
>     private final Rango rango;
>     private final Palo palo;
>     
>     public Carta(Rango rango, Palo palo) {
>         this.rango = rango;
>         this.palo = palo;
>     }
>     
>     public int getValor() {
>         return rango.getValor();
>     }
>     
>     @Override
>     public String toString() {
>         return rango + " de " + palo.getSimbolo();
>     }
> }
> 
> // Clase Baraja
> public class Baraja {
>     private Carta[] cartas;
>     private int cartasRestantes;
>     
>     public Baraja() {
>         int totalCartas = Palo.values().length * Rango.values().length;
>         this.cartas = new Carta[totalCartas];
>         this.cartasRestantes = 0;
>         
>         // Crear todas las cartas
>         for (Palo palo : Palo.values()) {
>             for (Rango rango : Rango.values()) {
>                 cartas[cartasRestantes] = new Carta(rango, palo);
>                 cartasRestantes++;
>             }
>         }
>         
>         System.out.println("✓ Baraja creada con " + cartasRestantes + " cartas");
>     }
>     
>     public void mezclar() {
>         for (int i = cartas.length - 1; i > 0; i--) {
>             int j = (int)(Math.random() * (i + 1));
>             Carta temp = cartas[i];
>             cartas[i] = cartas[j];
>             cartas[j] = temp;
>         }
>         System.out.println("✓ Baraja mezclada");
>     }
>     
>     public Carta repartir() {
>         if (cartasRestantes > 0) {
>             cartasRestantes--;
>             return cartas[cartasRestantes];
>         }
>         return null;
>     }
>     
>     public int getCartasRestantes() {
>         return cartasRestantes;
>     }
>     
>     public static void main(String[] args) {
>         System.out.println("╔═══════════════════════════════╗");
>         System.out.println("║   SISTEMA DE CARTAS - ENUM    ║");
>         System.out.println("╚═══════════════════════════════╝\n");
>         
>         Baraja baraja = new Baraja();
>         baraja.mezclar();
>         
>         System.out.println("\nRepartiendo 5 cartas:");
>         for (int i = 0; i < 5; i++) {
>             Carta carta = baraja.repartir();
>             System.out.println((i+1) + ". " + carta + " (Valor: " + carta.getValor() + ")");
>         }
>         
>         System.out.println("\nCartas restantes: " + baraja.getCartasRestantes());
>     }
> }
> ```

---

## ⚠️ Mejores Prácticas

> [!tip]- ✅ Recomendaciones
> 
> **1. Usar enum en lugar de constantes:**
> 
> ```java
> // ❌ MAL
> public class Estado {
>     public static final int ACTIVO = 1;
>     public static final int INACTIVO = 2;
>     public static final int SUSPENDIDO = 3;
> }
> 
> // ✅ BIEN
> public enum Estado {
>     ACTIVO, INACTIVO, SUSPENDIDO
> }
> ```
> 
> **2. Agregar atributos descriptivos:**
> 
> ```java
> public enum Prioridad {
>     BAJA("Baja", 1),
>     MEDIA("Media", 2),
>     ALTA("Alta", 3),
>     CRITICA("Crítica", 4);
>     
>     private final String descripcion;
>     private final int nivel;
>     
>     Prioridad(String descripcion, int nivel) {
>         this.descripcion = descripcion;
>         this.nivel = nivel;
>     }
>     
>     public String getDescripcion() { return descripcion; }
>     public int getNivel() { return nivel; }
> }
> ```
> 
> **3. Implementar métodos útiles:**
> 
> ```java
> public enum TipoArchivo {
>     PDF(".pdf", "application/pdf"),
>     WORD(".docx", "application/vnd.openxmlformats"),
>     EXCEL(".xlsx", "application/vnd.openxmlformats");
>     
>     private final String extension;
>     private final String mimeType;
>     
>     TipoArchivo(String extension, String mimeType) {
>         this.extension = extension;
>         this.mimeType = mimeType;
>     }
>     
>     public static TipoArchivo porExtension(String ext) {
>         for (TipoArchivo tipo : values()) {
>             if (tipo.extension.equalsIgnoreCase(ext)) {
>                 return tipo;
>             }
>         }
>         return null;
>     }
> }
> ```
> 
> **4. Usar switch expresivo:**
> 
> ```java
> public String getMensaje(DiaSemana dia) {
>     return switch (dia) {
>         case LUNES -> "¡Inicio de semana!";
>         case VIERNES -> "¡Casi fin de semana!";
>         case SABADO, DOMINGO -> "¡Fin de semana!";
>         default -> "Día normal";
>     };
> }
> ```
> 
> **5. No usar ordinal() para lógica:**
> 
> ```java
> // ❌ MAL - Frágil, depende del orden
> if (estado.ordinal() > 2) { /* ... */ }
> 
> // ✅ BIEN - Usar atributos explícitos
> if (estado.getPrioridad() > Prioridad.MEDIA.getPrioridad()) { /* ... */ }
> ```

---

## 📊 Enum vs Otras Alternativas

> [!note]- 🔍 Comparación
> 
> |Característica|Constantes int|String|Enum|
> |---|---|---|---|
> |**Type-safe**|❌|❌|✅|
> |**Legibilidad**|⚠️ Media|✅ Buena|✅ Excelente|
> |**Validación**|❌|❌|✅|
| **Métodos propios** | ❌ | ❌ | ✅ |
> | **Switch exhaustivo** | ❌ | ❌ | ✅ | | **Memoria** | ✅ Mínima | ⚠️ Media | ⚠️ Media | | **Mantenibilidad** | ❌ Baja | ⚠️ Media | ✅ Alta |
> 
> **Ejemplo comparativo:**
> 
> ```java
> // ❌ CON CONSTANTES INT
> public class EstadoPedido {
>     public static final int PENDIENTE = 0;
>     public static final int ENVIADO = 1;
>     public static final int ENTREGADO = 2;
> }
> 
> int estado = 99;  // ❌ Valor inválido - compila sin error
> if (estado == EstadoPedido.PENDIENTE) { }
> 
> // ❌ CON STRINGS
> String estado = "pendiente";
> if (estado.equals("PENDIENTE")) { }  // ❌ Case-sensitive
> if (estado.equals("enviado")) { }    // ❌ Typo no detectado
> 
> // ✅ CON ENUM
> EstadoPedido estado = EstadoPedido.PENDIENTE;
> if (estado == EstadoPedido.PENDIENTE) { }  // ✅ Type-safe
> // estado = EstadoPedido.INVALIDO;  // ❌ Error en compilación
> ```

---

## 🎓 Ejercicios Propuestos

> [!example]- 💪 Práctica con Enums
> 
> **Nivel Básico:**
> 
> 1. **Enum Mes:** Crear enum `Mes` con:
>     - Nombre en español
>     - Número de días
>     - Estación del año
>     - Método `esBisiesto(int año)`
> 2. **Enum Moneda:** Crear enum con:
>     - Diferentes monedas (USD, EUR, etc.)
>     - Tasa de cambio
>     - Método para convertir entre monedas
> 3. **Enum TipoVehiculo:** Con:
>     - Categorías (Auto, Moto, Camión)
>     - Capacidad de pasajeros
>     - Consumo promedio
> 
> **Nivel Intermedio:**
> 
> 4. **Sistema de Semáforo:**
>     
>     ```java
>     enum EstadoSemaforo {    VERDE, AMARILLO, ROJO}
>     ```
>     
>     - Agregar duración en segundos
>     - Método `siguiente()`
>     - Método `puedeAvanzar()`
> 5. **Enum Rol de Usuario:**
>     - Diferentes roles (ADMIN, USER, GUEST)
>     - Permisos específicos
>     - Método `tienePermiso(String accion)`
> 6. **Sistema de Calificaciones:**
>     - Enum con notas (A, B, C, D, F)
>     - Rango numérico
>     - Método `desdeNota(double nota)`
> 
> **Nivel Avanzado:**
> 
> 7. **Sistema de Reservas de Hotel:**
>     
>     ```java
>     enum TipoHabitacion {
>         SIMPLE(1, 50.0),
>         DOBLE(2, 80.0),
>         SUITE(4, 150.0);
>         
>         // Agregar temporadas (alta/baja)
>         // Método calcularPrecio(int noches, Temporada temp)
>     }
>     ```
>     
> 8. **Máquina de Estados:**
>     
>     - Crear enum para estados de una máquina expendedora
>     - Implementar transiciones válidas
>     - Métodos abstractos por estado
> 9. **Sistema de Ajedrez:**
>     
>     - Enum para tipos de pieza
>     - Cada pieza con movimientos válidos
>     - Método `puedeMoverse(Posicion origen, Posicion destino)`
> 10. **Calculadora de Impuestos:**
>     
>     - Enum con rangos de ingresos
>     - Porcentaje de impuesto por rango
>     - Método `calcularImpuesto(double ingreso)`

---

## 🔧 Casos Especiales

### EnumSet y EnumMap

> [!info]- 🗂️ Colecciones Especializadas para Enums
> 
> **EnumSet - Set optimizado para enums:**
> 
> ```java
> import java.util.EnumSet;
> 
> public enum DiaSemana {
>     LUNES, MARTES, MIERCOLES, JUEVES, VIERNES, SABADO, DOMINGO
> }
> 
> public class HorarioTrabajo {
>     private EnumSet<DiaSemana> diasLaborales;
>     
>     public HorarioTrabajo() {
>         // Crear set con días específicos
>         diasLaborales = EnumSet.of(
>             DiaSemana.LUNES, 
>             DiaSemana.MARTES, 
>             DiaSemana.MIERCOLES,
>             DiaSemana.JUEVES, 
>             DiaSemana.VIERNES
>         );
>         
>         // O usar rango
>         // diasLaborales = EnumSet.range(DiaSemana.LUNES, DiaSemana.VIERNES);
>     }
>     
>     public boolean esDiaLaboral(DiaSemana dia) {
>         return diasLaborales.contains(dia);
>     }
>     
>     public void agregarDia(DiaSemana dia) {
>         diasLaborales.add(dia);
>     }
>     
>     public static void main(String[] args) {
>         HorarioTrabajo horario = new HorarioTrabajo();
>         
>         System.out.println("¿Sábado es laboral? " + 
>                            horario.esDiaLaboral(DiaSemana.SABADO));
>         System.out.println("¿Lunes es laboral? " + 
>                            horario.esDiaLaboral(DiaSemana.LUNES));
>         
>         // Operaciones de conjunto
>         EnumSet<DiaSemana> finDeSemana = EnumSet.of(
>             DiaSemana.SABADO, 
>             DiaSemana.DOMINGO
>         );
>         
>         EnumSet<DiaSemana> todosDias = EnumSet.allOf(DiaSemana.class);
>         System.out.println("Total de días: " + todosDias.size());
>     }
> }
> ```
> 
> **EnumMap - Map optimizado para enums como keys:**
> 
> ```java
> import java.util.EnumMap;
> 
> public enum Producto {
>     LAPTOP, MOUSE, TECLADO, MONITOR
> }
> 
> public class Inventario {
>     private EnumMap<Producto, Integer> stock;
>     private EnumMap<Producto, Double> precios;
>     
>     public Inventario() {
>         stock = new EnumMap<>(Producto.class);
>         precios = new EnumMap<>(Producto.class);
>         
>         // Inicializar stock
>         stock.put(Producto.LAPTOP, 10);
>         stock.put(Producto.MOUSE, 50);
>         stock.put(Producto.TECLADO, 30);
>         stock.put(Producto.MONITOR, 15);
>         
>         // Inicializar precios
>         precios.put(Producto.LAPTOP, 899.99);
>         precios.put(Producto.MOUSE, 29.99);
>         precios.put(Producto.TECLADO, 59.99);
>         precios.put(Producto.MONITOR, 299.99);
>     }
>     
>     public int getStock(Producto producto) {
>         return stock.getOrDefault(producto, 0);
>     }
>     
>     public double getPrecio(Producto producto) {
>         return precios.getOrDefault(producto, 0.0);
>     }
>     
>     public boolean vender(Producto producto, int cantidad) {
>         int stockActual = getStock(producto);
>         if (stockActual >= cantidad) {
>             stock.put(producto, stockActual - cantidad);
>             System.out.println("✓ Vendidos " + cantidad + " " + producto);
>             return true;
>         }
>         System.out.println("❌ Stock insuficiente de " + producto);
>         return false;
>     }
>     
>     public void mostrarInventario() {
>         System.out.println("\n=== INVENTARIO ===");
>         for (Producto p : Producto.values()) {
>             System.out.printf("%s: %d unidades - $%.2f%n", 
>                               p, getStock(p), getPrecio(p));
>         }
>     }
>     
>     public static void main(String[] args) {
>         Inventario inv = new Inventario();
>         inv.mostrarInventario();
>         
>         inv.vender(Producto.LAPTOP, 2);
>         inv.vender(Producto.MOUSE, 100);  // Stock insuficiente
>         
>         inv.mostrarInventario();
>     }
> }
> ```

---

## 🎯 Enum con Interfaces

> [!success]- 🔌 Enums Implementando Interfaces Los enums pueden implementar interfaces para mayor flexibilidad:
> 
> ```java
> // Interface común
> interface Calculable {
>     double calcular(double valor);
> }
> 
> // Enum implementando interface
> public enum TipoDescuento implements Calculable {
>     SIN_DESCUENTO {
>         @Override
>         public double calcular(double valor) {
>             return valor;
>         }
>     },
>     ESTUDIANTE {
>         @Override
>         public double calcular(double valor) {
>             return valor * 0.85;  // 15% descuento
>         }
>     },
>     TERCERA_EDAD {
>         @Override
>         public double calcular(double valor) {
>             return valor * 0.70;  // 30% descuento
>         }
>     },
>     EMPLEADO {
>         @Override
>         public double calcular(double valor) {
>             return valor * 0.50;  // 50% descuento
>         }
>     },
>     BLACK_FRIDAY {
>         @Override
>         public double calcular(double valor) {
>             return valor * 0.60;  // 40% descuento
>         }
>     };
>     
>     public String formatearDescuento(double precioOriginal) {
>         double precioFinal = calcular(precioOriginal);
>         double descuento = precioOriginal - precioFinal;
>         return String.format("Precio: $%.2f -> $%.2f (Ahorro: $%.2f)", 
>                              precioOriginal, precioFinal, descuento);
>     }
> }
> 
> public class Ticket {
>     private String evento;
>     private double precioBase;
>     private TipoDescuento descuento;
>     
>     public Ticket(String evento, double precioBase, TipoDescuento descuento) {
>         this.evento = evento;
>         this.precioBase = precioBase;
>         this.descuento = descuento;
>     }
>     
>     public double getPrecioFinal() {
>         return descuento.calcular(precioBase);
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("\n=== TICKET ===");
>         System.out.println("Evento: " + evento);
>         System.out.println("Tipo: " + descuento);
>         System.out.println(descuento.formatearDescuento(precioBase));
>     }
>     
>     public static void main(String[] args) {
>         Ticket t1 = new Ticket("Concierto Rock", 100.0, TipoDescuento.ESTUDIANTE);
>         Ticket t2 = new Ticket("Teatro", 80.0, TipoDescuento.TERCERA_EDAD);
>         Ticket t3 = new Ticket("Cine", 15.0, TipoDescuento.BLACK_FRIDAY);
>         
>         t1.mostrarInfo();
>         t2.mostrarInfo();
>         t3.mostrarInfo();
>     }
> }
> ```

---

## 🎨 Patrón Singleton con Enum

> [!tip]- 🏆 La Mejor Forma de Implementar Singleton Usar enum es la forma más simple y segura de implementar el patrón Singleton:
> 
> ```java
> public enum ConfiguracionApp {
>     INSTANCE;  // La única instancia
>     
>     private String nombreApp;
>     private String version;
>     private boolean modoDebug;
>     
>     // Constructor privado (implícito en enum)
>     ConfiguracionApp() {
>         this.nombreApp = "MiApp";
>         this.version = "1.0.0";
>         this.modoDebug = false;
>     }
>     
>     // Métodos de negocio
>     public void cargarConfiguracion() {
>         System.out.println("Cargando configuración...");
>         // Lógica de carga
>     }
>     
>     public void mostrarInfo() {
>         System.out.println("=== CONFIGURACIÓN ===");
>         System.out.println("App: " + nombreApp);
>         System.out.println("Versión: " + version);
>         System.out.println("Debug: " + modoDebug);
>     }
>     
>     // Getters y setters
>     public String getNombreApp() { return nombreApp; }
>     public void setNombreApp(String nombre) { this.nombreApp = nombre; }
>     
>     public boolean isModoDebug() { return modoDebug; }
>     public void setModoDebug(boolean debug) { this.modoDebug = debug; }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         // Acceder a la única instancia
>         ConfiguracionApp config = ConfiguracionApp.INSTANCE;
>         config.mostrarInfo();
>         
>         // Modificar configuración
>         config.setModoDebug(true);
>         
>         // Desde otra parte del código
>         ConfiguracionApp config2 = ConfiguracionApp.INSTANCE;
>         config2.mostrarInfo();  // Mismo objeto, modo debug = true
>         
>         // Verificar que es la misma instancia
>         System.out.println("\n¿Misma instancia? " + (config == config2));  // true
>     }
> }
> ```
> 
> **Ventajas del Singleton con Enum:**
> 
> - ✅ Thread-safe sin sincronización
> - ✅ Protección contra serialización
> - ✅ Protección contra reflexión
> - ✅ Código más simple y limpio
> - ✅ Garantizado por la JVM

---

## 🌟 Ejemplo Completo: Sistema de Gestión de Pedidos

> [!example]- 🛒 Aplicación Real con Múltiples Enums
> 
> ```java
> // =============================
> // ENUMS DEL SISTEMA
> // =============================
> 
> enum EstadoPedido {
>     RECIBIDO("Recibido", false, true),
>     PREPARANDO("En preparación", false, true),
>     LISTO("Listo para envío", false, true),
>     EN_CAMINO("En camino", true, true),
>     ENTREGADO("Entregado", false, false),
>     CANCELADO("Cancelado", false, false);
>     
>     private final String descripcion;
>     private final boolean notificarCliente;
>     private final boolean puedeCancelar;
>     
>     EstadoPedido(String desc, boolean notificar, boolean cancelable) {
>         this.descripcion = desc;
>         this.notificarCliente = notificar;
>         this.puedeCancelar = cancelable;
>     }
>     
>     public String getDescripcion() { return descripcion; }
>     public boolean debeNotificar() { return notificarCliente; }
>     public boolean puedeCancelar() { return puedeCancelar; }
> }
> 
> enum MetodoPago {
>     EFECTIVO("Efectivo", 0, false),
>     TARJETA_DEBITO("Tarjeta de Débito", 0, true),
>     TARJETA_CREDITO("Tarjeta de Crédito", 3.5, true),
>     TRANSFERENCIA("Transferencia", 0, true),
>     PAYPAL("PayPal", 4.0, true);
>     
>     private final String nombre;
>     private final double comision;  // Porcentaje
>     private final boolean requiereVerificacion;
>     
>     MetodoPago(String nombre, double comision, boolean verificacion) {
>         this.nombre = nombre;
>         this.comision = comision;
>         this.requiereVerificacion = verificacion;
>     }
>     
>     public double calcularTotal(double subtotal) {
>         return subtotal * (1 + comision / 100);
>     }
>     
>     public String getNombre() { return nombre; }
>     public boolean requiereVerificacion() { return requiereVerificacion; }
> }
> 
> enum Prioridad {
>     NORMAL("Normal", 0, 3),
>     URGENTE("Urgente", 5.0, 1),
>     EXPRESS("Express", 10.0, 0);
>     
>     private final String nombre;
>     private final double costoAdicional;
>     private final int diasEntrega;
>     
>     Prioridad(String nombre, double costo, int dias) {
>         this.nombre = nombre;
>         this.costoAdicional = costo;
>         this.diasEntrega = dias;
>     }
>     
>     public String getNombre() { return nombre; }
>     public double getCostoAdicional() { return costoAdicional; }
>     public int getDiasEntrega() { return diasEntrega; }
> }
> 
> // =============================
> // CLASE PEDIDO
> // =============================
> 
> class Pedido {
>     private static int contadorId = 1;
>     
>     private final int id;
>     private String cliente;
>     private double subtotal;
>     private EstadoPedido estado;
>     private MetodoPago metodoPago;
>     private Prioridad prioridad;
>     
>     public Pedido(String cliente, double subtotal, 
>                   MetodoPago pago, Prioridad prioridad) {
>         this.id = contadorId++;
>         this.cliente = cliente;
>         this.subtotal = subtotal;
>         this.metodoPago = pago;
>         this.prioridad = prioridad;
>         this.estado = EstadoPedido.RECIBIDO;
>         
>         System.out.println("✓ Pedido #" + id + " creado");
>     }
>     
>     public void cambiarEstado(EstadoPedido nuevoEstado) {
>         if (estado == nuevoEstado) {
>             System.out.println("⚠️ El pedido ya está en estado: " + nuevoEstado.getDescripcion());
>             return;
>         }
>         
>         System.out.println("Pedido #" + id + ": " + 
>                            estado.getDescripcion() + " → " + 
>                            nuevoEstado.getDescripcion());
>         
>         this.estado = nuevoEstado;
>         
>         if (nuevoEstado.debeNotificar()) {
>             notificarCliente();
>         }
>     }
>     
>     public boolean cancelar() {
>         if (estado.puedeCancelar()) {
>             cambiarEstado(EstadoPedido.CANCELADO);
>             System.out.println("✓ Pedido #" + id + " cancelado");
>             return true;
>         }
>         System.out.println("❌ No se puede cancelar en estado: " + 
>                            estado.getDescripcion());
>         return false;
>     }
>     
>     private void notificarCliente() {
>         System.out.println("📧 Notificación enviada a " + cliente);
>     }
>     
>     public double calcularTotal() {
>         double total = subtotal + prioridad.getCostoAdicional();
>         total = metodoPago.calcularTotal(total);
>         return total;
>     }
>     
>     public void mostrarResumen() {
>         System.out.println("\n╔════════════════════════════════╗");
>         System.out.println("║     RESUMEN PEDIDO #" + id + "         ║");
>         System.out.println("╚════════════════════════════════╝");
>         System.out.println("Cliente: " + cliente);
>         System.out.println("Estado: " + estado.getDescripcion());
>         System.out.println("Prioridad: " + prioridad.getNombre() + 
>                            " (" + prioridad.getDiasEntrega() + " días)");
>         System.out.println("Método de pago: " + metodoPago.getNombre());
>         System.out.println("Subtotal: $" + String.format("%.2f", subtotal));
>         System.out.println("Costo prioridad: $" + 
>                            String.format("%.2f", prioridad.getCostoAdicional()));
>         System.out.println("TOTAL: $" + String.format("%.2f", calcularTotal()));
>     }
>     
>     public EstadoPedido getEstado() { return estado; }
> }
> 
> // =============================
> // SISTEMA DE GESTIÓN
> // =============================
> 
> public class SistemaGestionPedidos {
>     public static void main(String[] args) {
>         System.out.println("╔════════════════════════════════════════╗");
>         System.out.println("║   SISTEMA DE GESTIÓN DE PEDIDOS       ║");
>         System.out.println("╚════════════════════════════════════════╝\n");
>         
>         // Crear pedidos con diferentes configuraciones
>         Pedido pedido1 = new Pedido(
>             "Ana López",
>             100.0,
>             MetodoPago.TARJETA_CREDITO,
>             Prioridad.NORMAL
>         );
>         
>         Pedido pedido2 = new Pedido(
>             "Carlos Ruiz",
>             250.0,
>             MetodoPago.EFECTIVO,
>             Prioridad.EXPRESS
>         );
>         
>         // Procesar pedido 1
>         System.out.println("\n--- PROCESANDO PEDIDO 1 ---");
>         pedido1.cambiarEstado(EstadoPedido.PREPARANDO);
>         pedido1.cambiarEstado(EstadoPedido.LISTO);
>         pedido1.cambiarEstado(EstadoPedido.EN_CAMINO);
>         pedido1.mostrarResumen();
>         
>         // Procesar pedido 2
>         System.out.println("\n--- PROCESANDO PEDIDO 2 ---");
>         pedido2.cambiarEstado(EstadoPedido.PREPARANDO);
>         pedido2.cancelar();  // Intentar cancelar
>         pedido2.mostrarResumen();
>         
>         // Mostrar todos los métodos de pago disponibles
>         System.out.println("\n--- MÉTODOS DE PAGO DISPONIBLES ---");
>         for (MetodoPago metodo : MetodoPago.values()) {
>             System.out.println("• " + metodo.getNombre() + 
>                                (metodo.requiereVerificacion() ? 
>                                 " (requiere verificación)" : ""));
>         }
>         
>         // Mostrar opciones de prioridad
>         System.out.println("\n--- OPCIONES DE PRIORIDAD ---");
>         for (Prioridad p : Prioridad.values()) {
>             System.out.printf("• %s: +$%.2f (%d días)%n",
>                               p.getNombre(),
>                               p.getCostoAdicional(),
>                               p.getDiasEntrega());
>         }
>     }
> }
> ```

---

## ❓ Preguntas Frecuentes

> [!question]- 🤔 FAQs sobre Enums
> 
> **1. ¿Puedo heredar de un enum?**
> 
> ```java
> // ❌ NO - Los enums son implícitamente final
> // public enum MiEnum extends OtroEnum { }  // Error de compilación
> 
> // ✅ Pero pueden implementar interfaces
> public enum MiEnum implements MiInterface { }
> ```
> 
> **2. ¿Puedo crear instancias de enum con `new`?**
> 
> ```java
> // ❌ NO - El constructor es siempre privado
> // DiaSemana dia = new DiaSemana();  // Error
> 
> // ✅ Solo usar constantes predefinidas
> DiaSemana dia = DiaSemana.LUNES;
> ```
> 
> **3. ¿Los enums consumen más memoria que constantes int?**
> 
> - Sí, ligeramente más memoria
> - Pero las ventajas (type-safety, legibilidad) superan el costo
> - Para la mayoría de aplicaciones, la diferencia es insignificante
> 
> **4. ¿Cuándo NO usar enums?**
> 
> - Cuando los valores no son fijos (vienen de BD)
> - Cuando hay demasiados valores (miles)
> - Cuando los valores cambian frecuentemente
> 
> **5. ¿Puedo serializar enums?**
> 
> ```java
> // ✅ SÍ - Serialización automática y segura
> DiaSemana dia = DiaSemana.LUNES;
> // La serialización usa el nombre, no el ordinal
> ```

---

## 🔗 Conexión con Próximos Temas

> [!quote]- 🌟 Continuando el Aprendizaje **Has aprendido:**
> 
> - ✅ Qué son las enumeraciones y por qué usarlas
> - ✅ Sintaxis básica y métodos integrados
> - ✅ Enums con atributos, constructores y métodos
> - ✅ Patrones avanzados (métodos abstractos, interfaces)
> - ✅ EnumSet y EnumMap
> - ✅ Casos de uso reales
> 
> **Próximos temas relacionados:**
> 
> - **[[Collections]]** - Usar enums con colecciones
> - **[[Switch Expression]]** - Pattern matching con enums
> - **[[Interfaces]]** - Enums implementando contratos
> - **[[Serialización]]** - Persistir enums
> - **[[Design Patterns]]** - Patrones con enums (Strategy, State)

---

**Tags:** #java #enum #enumeraciones #type-safe #constantes #poo #buenas-practicas