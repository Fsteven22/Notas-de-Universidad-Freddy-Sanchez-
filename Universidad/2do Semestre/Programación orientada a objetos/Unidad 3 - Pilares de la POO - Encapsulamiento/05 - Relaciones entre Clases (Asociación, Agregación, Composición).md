# 🔗 Relaciones entre Clases en Java

## 🎯 Introducción

> [!info]- 💡 ¿Qué son las Relaciones entre Clases? En POO, las clases no existen aisladas. Se **relacionan** entre sí para modelar sistemas complejos del mundo real.
> 
> **Analogía:** Como las personas en una organización
> 
> - **Asociación:** Una persona _conoce_ a otra
> - **Agregación:** Un equipo _tiene_ miembros (pueden existir independientemente)
> - **Composición:** Un corazón _pertenece_ a una persona (no puede existir sin ella)
> 
> **Tipos principales:**
> 
> - **Asociación:** Relación básica entre clases
> - **Agregación:** "Tiene un" - relación débil (todo-parte independiente)
> - **Composición:** "Está compuesto de" - relación fuerte (todo-parte dependiente)

---

## 1️⃣ Asociación (Association)

> [!example]- 🤝 Relación Básica entre Clases **Concepto:** Una clase _usa_ o _interactúa_ con otra clase
> 
> **Características:**
> 
> - Relación más general y flexible
> - Los objetos son **independientes**
> - Puede ser unidireccional o bidireccional
> - No implica propiedad
> 
> **Ejemplo simple:**
> 
> ```java
> public class Estudiante {
>     private String nombre;
>     private String codigo;
>     
>     public Estudiante(String nombre, String codigo) {
>         this.nombre = nombre;
>         this.codigo = codigo;
>     }
>     
>     // Método que usa un Curso
>     public void inscribirse(Curso curso) {
>         System.out.println(nombre + " se inscribió en " + curso.getNombre());
>     }
>     
>     public String getNombre() { return nombre; }
> }
> 
> public class Curso {
>     private String nombre;
>     private String codigo;
>     
>     public Curso(String nombre, String codigo) {
>         this.nombre = nombre;
>         this.codigo = codigo;
>     }
>     
>     public String getNombre() { return nombre; }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         Estudiante ana = new Estudiante("Ana López", "E001");
>         Curso java = new Curso("Programación Java", "CS101");
>         
>         // Asociación: Estudiante usa Curso
>         ana.inscribirse(java);  // "Ana López se inscribió en Programación Java"
>         
>         // Ambos objetos siguen existiendo independientemente
>     }
> }
> ```
> 
> **Asociación Bidireccional:**
> 
> ```java
> public class Profesor {
>     private String nombre;
>     private Curso cursoAsignado;  // Profesor conoce su Curso
>     
>     public void asignarCurso(Curso curso) {
>         this.cursoAsignado = curso;
>         curso.setProfesor(this);  // El curso también conoce al profesor
>     }
> }
> 
> public class Curso {
>     private String nombre;
>     private Profesor profesor;  // Curso conoce su Profesor
>     
>     public void setProfesor(Profesor prof) {
>         this.profesor = prof;
>     }
> }
> ```

---

## 2️⃣ Agregación (Aggregation)

> [!success]- 📦 "Tiene un" - Relación Débil **Concepto:** Una clase _contiene_ otra, pero las partes pueden existir independientemente
> 
> **Características:**
> 
> - Relación "todo-parte"
> - Las partes **pueden existir sin el todo**
> - Las partes pueden pertenecer a varios "todos"
> - Se implementa con referencias
> 
> **Ejemplo: Departamento y Empleados**
> 
> ```java
> public class Empleado {
>     private String nombre;
>     private String id;
>     
>     public Empleado(String nombre, String id) {
>         this.nombre = nombre;
>         this.id = id;
>     }
>     
>     public String getNombre() { return nombre; }
> }
> 
> public class Departamento {
>     private String nombre;
>     private Empleado[] empleados;
>     private int totalEmpleados;
>     
>     public Departamento(String nombre, int capacidad) {
>         this.nombre = nombre;
>         this.empleados = new Empleado[capacidad];
>         this.totalEmpleados = 0;
>     }
>     
>     // Agrega empleado existente (no lo crea)
>     public void agregarEmpleado(Empleado emp) {
>         if (totalEmpleados < empleados.length) {
>             empleados[totalEmpleados] = emp;
>             totalEmpleados++;
>             System.out.println(emp.getNombre() + " agregado a " + nombre);
>         }
>     }
>     
>     public void mostrarEmpleados() {
>         System.out.println("\nEmpleados de " + nombre + ":");
>         for (int i = 0; i < totalEmpleados; i++) {
>             System.out.println("- " + empleados[i].getNombre());
>         }
>     }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         // Empleados creados independientemente
>         Empleado juan = new Empleado("Juan Pérez", "E001");
>         Empleado maria = new Empleado("María García", "E002");
>         
>         Departamento ventas = new Departamento("Ventas", 10);
>         ventas.agregarEmpleado(juan);
>         ventas.agregarEmpleado(maria);
>         
>         // Si eliminamos el departamento, los empleados siguen existiendo
>         ventas = null;  // Departamento destruido
>         System.out.println(juan.getNombre());  // ✅ Juan sigue existiendo
>     }
> }
> ```
> 
> **Otro ejemplo: Biblioteca y Libros**
> 
> ```java
> public class Libro {
>     private String titulo;
>     private String isbn;
>     
>     public Libro(String titulo, String isbn) {
>         this.titulo = titulo;
>         this.isbn = isbn;
>     }
>     
>     public String getTitulo() { return titulo; }
> }
> 
> public class Biblioteca {
>     private String nombre;
>     private Libro[] catalogo;
>     private int totalLibros;
>     
>     public Biblioteca(String nombre, int capacidad) {
>         this.nombre = nombre;
>         this.catalogo = new Libro[capacidad];
>         this.totalLibros = 0;
>     }
>     
>     // Agregación: recibe libros ya creados
>     public void agregarLibro(Libro libro) {
>         if (totalLibros < catalogo.length) {
>             catalogo[totalLibros] = libro;
>             totalLibros++;
>         }
>     }
> }
> 
> // Los libros existen antes de la biblioteca
> Libro libro1 = new Libro("Don Quijote", "123");
> Biblioteca biblio = new Biblioteca("Central", 100);
> biblio.agregarLibro(libro1);
> ```

---

## 3️⃣ Composición (Composition)

> [!warning]- 🔒 "Está Compuesto de" - Relación Fuerte **Concepto:** Una clase _contiene_ otra, y las partes **no pueden existir sin el todo**
> 
> **Características:**
> 
> - Relación "todo-parte" muy fuerte
> - Las partes **no pueden existir independientemente**
> - Las partes se crean y destruyen con el todo
> - Se implementa creando objetos en el constructor
> 
> **Ejemplo: Casa y Habitaciones**
> 
> ```java
> public class Habitacion {
>     private String tipo;
>     private double area;
>     
>     public Habitacion(String tipo, double area) {
>         this.tipo = tipo;
>         this.area = area;
>     }
>     
>     public String getTipo() { return tipo; }
>     public double getArea() { return area; }
> }
> 
> public class Casa {
>     private String direccion;
>     private Habitacion[] habitaciones;  // Composición
>     
>     public Casa(String direccion) {
>         this.direccion = direccion;
>         
>         // Las habitaciones se crean CON la casa
>         this.habitaciones = new Habitacion[4];
>         habitaciones[0] = new Habitacion("Sala", 25.0);
>         habitaciones[1] = new Habitacion("Cocina", 15.0);
>         habitaciones[2] = new Habitacion("Dormitorio 1", 20.0);
>         habitaciones[3] = new Habitacion("Baño", 8.0);
>         
>         System.out.println("Casa creada con sus habitaciones");
>     }
>     
>     public void mostrarHabitaciones() {
>         System.out.println("\nHabitaciones de " + direccion + ":");
>         for (Habitacion hab : habitaciones) {
>             System.out.println("- " + hab.getTipo() + ": " + hab.getArea() + "m²");
>         }
>     }
>     
>     public double getAreaTotal() {
>         double total = 0;
>         for (Habitacion hab : habitaciones) {
>             total += hab.getArea();
>         }
>         return total;
>     }
> }
> 
> // USO:
> public class Main {
>     public static void main(String[] args) {
>         Casa miCasa = new Casa("Av. Principal 123");
>         miCasa.mostrarHabitaciones();
>         System.out.println("Área total: " + miCasa.getAreaTotal() + "m²");
>         
>         // Si destruimos la casa, las habitaciones también se destruyen
>         miCasa = null;  // Casa y habitaciones destruidas
>     }
> }
> ```
> 
> **Ejemplo: Persona y Corazón**
> 
> ```java
> public class Corazon {
>     private int latidosPorMinuto;
>     
>     public Corazon() {
>         this.latidosPorMinuto = 70;
>         System.out.println("Corazón creado (latidos: " + latidosPorMinuto + "/min)");
>     }
>     
>     public void latir() {
>         System.out.println("Latiendo a " + latidosPorMinuto + " pulsaciones/min");
>     }
>     
>     public void acelerar() {
>         latidosPorMinuto += 20;
>     }
> }
> 
> public class Persona {
>     private String nombre;
>     private Corazon corazon;  // Composición: el corazón es parte de la persona
>     
>     public Persona(String nombre) {
>         this.nombre = nombre;
>         this.corazon = new Corazon();  // Se crea CON la persona
>         System.out.println("Persona " + nombre + " creada");
>     }
>     
>     public void hacerEjercicio() {
>         System.out.println(nombre + " está haciendo ejercicio");
>         corazon.acelerar();
>         corazon.latir();
>     }
>     
>     // No hay setter para corazon - no se puede cambiar
> }
> 
> // USO:
> Persona ana = new Persona("Ana");
> ana.hacerEjercicio();
> // El corazón no puede existir fuera de la persona
> ```

---

## 📊 Tabla Comparativa

> [!tip]- 🔍 Diferencias Clave
> 
> |Característica|Asociación|Agregación|Composición|
> |---|---|---|---|
> |**Relación**|"Usa"|"Tiene"|"Está compuesto de"|
> |**Fuerza**|Débil|Media|Fuerte|
> |**Independencia**|Total|Sí|No|
> |**Creación**|Externa|Externa|Interna|
> |**Destrucción**|Independiente|Independiente|Conjunta|
> |**Ejemplo**|Estudiante-Curso|Departamento-Empleado|Casa-Habitación|
> 
> **Código de ejemplo comparativo:**
> 
> ```java
> // ASOCIACIÓN - Objetos independientes que interactúan
> Estudiante est = new Estudiante("Ana");
> Curso curso = new Curso("Java");
> est.inscribirse(curso);  // Asociación temporal
> 
> // AGREGACIÓN - El todo contiene partes independientes
> Departamento dept = new Departamento("Ventas");
> Empleado emp = new Empleado("Juan");  // Creado fuera
> dept.agregarEmpleado(emp);  // emp puede existir sin dept
> 
> // COMPOSICIÓN - Las partes se crean con el todo
> Casa casa = new Casa("Av. 123");  // Crea habitaciones internamente
> // Las habitaciones no pueden existir fuera de la casa
> ```

---

## 🎨 Ejemplo Completo: Sistema Universitario

> [!example]- 🎓 Implementación con las Tres Relaciones
> 
> ```java
> // ===================================
> // COMPOSICIÓN: Universidad y Facultades
> // ===================================
> class Facultad {
>     private String nombre;
>     private String codigo;
>     
>     public Facultad(String nombre, String codigo) {
>         this.nombre = nombre;
>         this.codigo = codigo;
>     }
>     
>     public String getNombre() { return nombre; }
> }
> 
> // ===================================
> // AGREGACIÓN: Carrera y Profesores
> // ===================================
> class Profesor {
>     private String nombre;
>     private String especialidad;
>     
>     public Profesor(String nombre, String especialidad) {
>         this.nombre = nombre;
>         this.especialidad = especialidad;
>     }
>     
>     public String getNombre() { return nombre; }
>     public String getEspecialidad() { return especialidad; }
> }
> 
> class Carrera {
>     private String nombre;
>     private Profesor[] profesores;
>     private int totalProfesores;
>     
>     public Carrera(String nombre, int capacidad) {
>         this.nombre = nombre;
>         this.profesores = new Profesor[capacidad];
>         this.totalProfesores = 0;
>     }
>     
>     // Agregación: profesores creados externamente
>     public void agregarProfesor(Profesor prof) {
>         if (totalProfesores < profesores.length) {
>             profesores[totalProfesores] = prof;
>             totalProfesores++;
>             System.out.println("✓ " + prof.getNombre() + " agregado a " + nombre);
>         }
>     }
>     
>     public String getNombre() { return nombre; }
> }
> 
> // ===================================
> // ASOCIACIÓN: Estudiante e inscripción
> // ===================================
> class Estudiante {
>     private String nombre;
>     private String codigo;
>     
>     public Estudiante(String nombre, String codigo) {
>         this.nombre = nombre;
>         this.codigo = codigo;
>     }
>     
>     // Asociación: usa Carrera temporalmente
>     public void inscribirse(Carrera carrera) {
>         System.out.println(nombre + " se inscribió en " + carrera.getNombre());
>     }
>     
>     public String getNombre() { return nombre; }
> }
> 
> // ===================================
> // CLASE PRINCIPAL: Universidad
> // ===================================
> public class Universidad {
>     private String nombre;
>     private Facultad[] facultades;  // Composición
>     
>     public Universidad(String nombre) {
>         this.nombre = nombre;
>         
>         // Composición: facultades creadas con la universidad
>         this.facultades = new Facultad[3];
>         facultades[0] = new Facultad("Ingeniería", "ING");
>         facultades[1] = new Facultad("Medicina", "MED");
>         facultades[2] = new Facultad("Derecho", "DER");
>         
>         System.out.println("Universidad " + nombre + " creada con sus facultades\n");
>     }
>     
>     public void mostrarFacultades() {
>         System.out.println("Facultades de " + nombre + ":");
>         for (Facultad fac : facultades) {
>             System.out.println("- " + fac.getNombre());
>         }
>     }
>     
>     public static void main(String[] args) {
>         System.out.println("╔════════════════════════════════════╗");
>         System.out.println("║  SISTEMA UNIVERSITARIO - RELACIONES║");
>         System.out.println("╚════════════════════════════════════╝\n");
>         
>         // COMPOSICIÓN
>         Universidad uni = new Universidad("ESPOL");
>         uni.mostrarFacultades();
>         
>         // AGREGACIÓN
>         System.out.println("\n--- AGREGACIÓN ---");
>         Profesor prof1 = new Profesor("Dr. García", "Programación");
>         Profesor prof2 = new Profesor("Dra. López", "Bases de Datos");
>         
>         Carrera sistemas = new Carrera("Ingeniería en Sistemas", 10);
>         sistemas.agregarProfesor(prof1);
>         sistemas.agregarProfesor(prof2);
>         
>         // ASOCIACIÓN
>         System.out.println("\n--- ASOCIACIÓN ---");
>         Estudiante est1 = new Estudiante("Ana Pérez", "E001");
>         Estudiante est2 = new Estudiante("Carlos Ruiz", "E002");
>         
>         est1.inscribirse(sistemas);
>         est2.inscribirse(sistemas);
>         
>         System.out.println("\n✓ Sistema ejecutado correctamente");
>     }
> }
> ```

---

## 🎯 Cuándo Usar Cada Relación

> [!note]- 📋 Guía de Decisión
> 
> **Usa ASOCIACIÓN cuando:**
> 
> - ✅ Los objetos solo necesitan interactuar temporalmente
> - ✅ No hay relación de propiedad
> - ✅ Ejemplo: Estudiante-Curso, Cliente-Pedido
> 
> **Usa AGREGACIÓN cuando:**
> 
> - ✅ Hay una relación "todo-parte"
> - ✅ Las partes pueden existir independientemente
> - ✅ Las partes pueden compartirse
> - ✅ Ejemplo: Equipo-Jugadores, Biblioteca-Libros
> 
> **Usa COMPOSICIÓN cuando:**
> 
> - ✅ Hay una relación "todo-parte" muy fuerte
> - ✅ Las partes NO pueden existir sin el todo
> - ✅ El ciclo de vida está ligado
> - ✅ Ejemplo: Casa-Habitaciones, Persona-Órganos

---

## 💡 Consejos Prácticos

> [!tip]- ⚡ Mejores Prácticas
> 
> **1. Preferir Composición sobre Herencia:**
> 
> ```java
> // ❌ Mal uso de herencia
> class Pato extends Motor { }  // ¿Un pato ES un motor?
> 
> // ✅ Usar composición
> class Pato {
>     private Motor motor;  // Un pato TIENE un motor
> }
> ```
> 
> **2. Encapsular relaciones:**
> 
> ```java
> public class Departamento {
>     private Empleado[] empleados;  // Private
>     
>     public void agregarEmpleado(Empleado emp) {
>         // Método controlado
>     }
>     
>     // ❌ No exponer array directamente
>     // public Empleado[] getEmpleados() { return empleados; }
> }
> ```
> 
> **3. Validar en agregación/composición:**
> 
> ```java
> public void agregarEmpleado(Empleado emp) {
>     if (emp == null) {
>         throw new IllegalArgumentException("Empleado no puede ser null");
>     }
>     // Agregar...
> }
> ```

---

## 🔗 Conexión con Próximos Temas

> [!quote]- 🌟 Continuando el Aprendizaje **Has aprendido:**
> 
> - ✅ Asociación, Agregación y Composición
> - ✅ Cuándo usar cada tipo de relación
> - ✅ Implementación práctica de relaciones
> 
> **Próximos temas:**
> 
> - **[[Herencia]]** - Relación "es un"
> - **[[Interfaces]]** - Contratos entre clases
> - **[[Polimorfismo]]** - Flexibilidad en relaciones
> - **[[Collections]]** - Manejar múltiples relaciones

---

**Tags:** #java #poo #relaciones #asociacion #agregacion #composicion #uml #diseño