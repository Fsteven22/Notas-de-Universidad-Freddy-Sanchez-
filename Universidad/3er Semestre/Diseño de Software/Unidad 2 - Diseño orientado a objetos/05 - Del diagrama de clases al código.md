---
dg-publish: true
tags: [CCPG1042, unidad2, uml, codigo, diseno-software]
---

# 🔧 Del diagrama de clases al código

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Traducir el Diagrama?
>
> El diagrama de clases es el **contrato** entre el diseño y el código: si la relación no se puede escribir, es que el modelo está mal. El deck `04bImplementaciónDesdeDiseno.pdf` (30 p., MSc. Jurado / Dr. Mera, 2024) es la última sesión de la Unidad 2 y su objetivo es explícito: **"traducir un diagrama de clase en código fuente y viceversa"**, y lo mismo con un diagrama de secuencia.
>
> **Analogía del mundo real:** el diagrama es el plano del edificio y el código son los ladrillos. El plano no se puede pintar: cada línea tiene que acabar en una llamada a método.
>
> | Lo que ves en el diagrama | Lo que escribes en el código |
> |---|---|
> | **Asociación** | un atributo que apunta al otro objeto |
> | **Agregación / Composición** | quién crea y quién destruye al otro |
> | **Generalización** | `extends` + clase abstracta |
> | **Realización** | `implements` + interface |
> | **Dependencia** | un `import` o un parámetro |
> | **Clase de asociación** | una clase propia con sus atributos |

![[../Diagramas/dsw-u2-06-01-flow.svg]]

> [!tip] 💡 La regla del deck
> "Recordar cómo ir de un diagrama de clase a código fuente **y viceversa**". El viceversa importa: si el código ya está escrito, el diagrama se **genera** — y si no coincide, el diagrama estaba mal.

---

## 🧵 Las 7 relaciones del diagrama de clases

> [!note] 📖 Tabla del deck (pp. 4-5)
> "Las clases deben estar relacionadas con otras". El deck agrupa las relaciones en diagramas de clases así:
>
> | # | Relación | En el diagrama | En el código |
> |---|---|---|---|
> | 1 | **Asociación simple / directa** | línea entre clases | atributo de referencia |
> | 2 | **Agregación** | rombo **blanco** | referencia al todo, el parte sobrevive |
> | 3 | **Composición** | rombo **negro** | el todo crea y destruye al parte |
> | 4 | **Herencia / Generalización** | flecha con triángulo hueco | `extends`, clase abstracta |
> | 5 | **Realización** | flecha punteada a interface | `implements` |
> | 6 | **Dependencia** | flecha punteada a clase | `import` o parámetro |
> | 7 | **Clase de asociación** | clase colgando de la línea | clase propia que se instancia al ejecutar la relación |

![[Archivos/04b-p5-tabla-relaciones.png]]

---

## 🔗 1. Asociación: la relación más común

> [!info] 📖 Qué es
> Dos clases que **se conocen**: una guarda una referencia a la otra. No implica propiedad: el `Cliente` conoce su `CuentaBancaria`, y viceversa no es obligatorio.

En el diagrama se dibuja como una línea con multiplicidad; en el código es un **atributo**.

![[Archivos/04b-p9-codigo-asociacion.png]]

> [!example] 🔧 Asociación en Java
> ```java
> class Cliente {
>     private String nombre;
>     private CuentaBancaria cuenta;          // asociación: guarda la referencia
> // ---
>     public Cliente(String nombre, CuentaBancaria cuenta) {
>         this.nombre = nombre;
>         this.cuenta = cuenta;
>     }
> // ---
>     public String getNombre() { return nombre; }
>     public CuentaBancaria getCuenta() { return cuenta; }
> }
> // ---
> class CuentaBancaria {
>     private String numero;
>     private double saldo;
> // ---
>     public CuentaBancaria(String numero, double saldo) {
>         this.numero = numero;
>         this.saldo = saldo;
>     }
> // ---
>     public double getSaldo() { return saldo; }
> }
> ```

> [!tip] Multiplicidad → tipo del atributo
> - `1` → una referencia: `private CuentaBancaria cuenta;`
> - `0..*` o `*` → una colección: `private List<Factura> facturas = new ArrayList<>();`
> - `0..1` → referencia **anulable** (`null` = "todavía no"): `private CuentaBancaria cuenta;`

---

## 🧷 2. Clase de asociación: la relación que tiene datos

> [!info] 📖 Qué dice el deck (p. 10)
> "La **clase de asociación se instancia al ejecutar la relación** entre `Cliente` y `CuentaBancaria`. `RealizarTransaccion()` **asocia** los clientes y las cuentas."

O sea: la relación **es un objeto**. Nace una clase propia con sus atributos, y la línea del diagrama se convierte en un atributo de esa clase.

![[Archivos/04b-p4-relaciones.png]]

> [!example] 🔧 Clase de asociación en Java
> ```java
> class Transaccion {                      // la clase de asociación
>     private Cliente cliente;
>     private CuentaBancaria cuenta;
>     private double monto;
>     private LocalDate fecha;
> // ---
>     public Transaccion(Cliente cliente, CuentaBancaria cuenta, double monto) {
>         this.cliente = cliente;
>         this.cuenta = cuenta;
>         this.monto = monto;
>     }
> }
> // ---
> class Cliente {
>     private List<Transaccion> transacciones = new ArrayList<>();
> // ---
>     public void RealizarTransaccion(CuentaBancaria cuenta, double monto) {
>         transacciones.add(new Transaccion(this, cuenta, monto));   // la relación se instancia
>     }
> }
> ```

> [!note] 🔗 Patrón que ya usas
> Es exactamente el `Prestamo` entre `Copia` y `Socio` de la Biblioteca, o la `Inscripcion` entre `OrganizacionPolitica` y `Candidatura` del SIEL. La relación con datos **nace como clase**.

---

## 🔄 3. Bidireccionalidad: quién conoce a quién

> [!info] 📖 Qué es
> Una asociación puede ser **unidireccional** (A conoce a B, B no conoce a A) o **bidireccional** (A conoce a B y B conoce a A). El deck dedica cuatro páginas (pp. 11-14) a las variantes, porque **es el punto donde los diagramas se contradicen con el código**.

![[Archivos/04b-p11-bidireccionalidad.png]]

> [!example] 🔧 Las dos formas
> ```java
> // Unidireccional: Cliente -> CuentaBancaria
> class Cliente {
>     private CuentaBancaria cuenta;
> }
> // ---
> // Bidireccional: cada lado tiene su referencia
> class Cliente {
>     private List<CuentaBancaria> cuentas = new ArrayList<>();
> // ---
>     public void abrir(CuentaBancaria cuenta) {
>         cuentas.add(cuenta);
>         cuenta.setTitular(this);           // se mantiene el otro lado
>     }
> }
> // ---
> class CuentaBancaria {
>     private Cliente titular;
> // ---
>     public void setTitular(Cliente titular) { this.titular = titular; }
> }
> ```

> [!danger] ❌ El error que el deck evita
> Poner la relación **solo en el diagrama** y no en el código, o al revés: el diagrama muestra `1 ── *` y el código guarda una sola referencia. **La multiplicidad es un contrato del código**: si dice `*`, el atributo es una colección.

---

## 🔢 4. Múltiples relaciones y recursividad

> [!info] 📖 Del deck (pp. 15-16)
> - **Múltiples relaciones:** dos clases pueden estar unidas por **más de una** asociación a la vez (p. ej. `Empleado` ↔ `Empresa`: *trabaja para* y *es dirigida por*). Cada una necesita su propio atributo.
> - **Recursividad:** una clase se relaciona **consigo misma** (un empleado es jefe de otro empleado). En código, el atributo apunta al mismo tipo.

> [!example] 🔧 Ejemplo
> ```java
> class Empleado {
>     private String nombre;
>     private Empresa empresa;        // relación 1: trabaja para
>     private Empleado jefe;           // relación 2: es dirigida por  (recursiva)
>     private List<Empleado> subordinados = new ArrayList<>();
> }
> ```

---

## 🧬 5. Generalización: `extends` y clase abstracta

> [!info] 📖 Del deck (p. 18)
> "En el diagrama de clases el nombre de la clase está **en cursiva**; esto se traduce como **clase abstracta**".

![[Archivos/04b-p18-generalizacion.png]]

> [!example] 🔧 Generalización en Java
> ```java
> abstract class Figura {                 // <- el nombre en cursiva del diagrama
>     protected String color;
> // ---
>     public abstract double area();      // operación abstracta: cada subclase la implementa
> }
> // ---
> class Circulo extends Figura {
>     private double radio;
> // ---
>     @Override
>     public double area() { return Math.PI * radio * radio; }
> }
> ```

> [!note] El mapeo completo
> | En el diagrama | En el código |
> |---|---|
> | nombre en **cursiva** | `abstract class` |
> | operación en *cursiva* | `abstract` (sin cuerpo) |
> | triángulo hueco | `extends` |
> | **generalización** entre interfaces | `extends` (y `implements` si la clase implementa la interface) |

---

## 🔌 6. Realización: `implements` y el contrato

> [!info] 📖 Del deck (p. 19)
> "**Impresión** es una Interface. **CuentaBancaria** implementa esa interface y por lo tanto desarrolla los métodos `ImprimirRecibo()` y `EstadoCuenta()`".

![[Archivos/04b-p20-realizacion.png]]

> [!example] 🔧 Realización en Java
> ```java
> interface Impresion {
>     void ImprimirRecibo();
>     String EstadoCuenta();
> }
> // ---
> class CuentaBancaria implements Impresion {
>     private double saldo;
> // ---
>     @Override
>     public void ImprimirRecibo() { /* ... */ }
> // ---
>     @Override
>     public String EstadoCuenta() { return "saldo: " + saldo; }
> }
> ```

> [!tip] Por qué importa
> La interface **no tiene interior que mostrar** en el diagrama (por eso se dibuja como paleta o círculo): solo promete operaciones. Quien la usa depende del **contrato**, no de la clase concreta — es el mismo criterio que ya usabas en la nota de componentes e interfaces (U2-02).

---

## 🔗 7. Dependencia: el `import` disfrazado

> [!info] 📖 Del deck (p. 21)
> "Indica que los **cambios sobre la clase B pueden afectar a la clase A**. `ClassA` **usa los servicios** de `ClassB`. En Java se podría representar con un `import`."

![[Archivos/04b-p22-dependencia.png]]

> [!example] 🔧 Dependencia en Java
> ```java
> import java.time.LocalDate;      // <- dependencia: ClassA usa los servicios de ClassB
> // ---
> class Reporte {
>     private LocalDate fecha;      // ... y solo mientras dura la llamada
> }
> ```

> [!danger] ❌ Dependencia que se disfraza de asociación
> Si guardas el objeto de la clase B en un **atributo**, ya no es dependencia: es una **asociación**. La dependencia es de **uso temporal**: un parámetro, un `import`, una variable local que muere al salir del método.

---

## 🧱 8. Composición y agregación: quién manda

> [!info] 📖 Del deck (pp. 23-24)
> El deck las llama "ejemplificación" y las muestra con los mismos ejemplos del curso: la **composición** es el rombo negro, la **agregación** el rombo blanco.

![[Archivos/04b-p23-composicion.png]]

![[Archivos/04b-p24-agregacion.png]]

> [!example] 🔧 La diferencia en el código
> ```java
> // COMPOSICIÓN: el todo crea el parte y lo destruye con él
> class Pedido {
>     private List<LineaPedido> lineas = new ArrayList<>();
> // ---
>     public void agregarProducto(Producto p, int cantidad) {
>         lineas.add(new LineaPedido(p, cantidad));   // el Pedido CREA la línea
>     }
> }   // al morir el Pedido, mueren sus líneas
> // ---
> // AGREGACIÓN: el parte existe antes y sobrevive
> class Equipo {
>     private List<Jugador> jugadores = new ArrayList<>();
> // ---
>     public void fichar(Jugador j) { jugadores.add(j); }   // el Jugador ya existía
> }
> ```

> [!tip] La prueba del curso, en código
> - **Composición** → el constructor del todo **crea** a los partes (`new LineaPedido(...)`).
> - **Agregación** → el constructor del todo **recibe** partes que ya existían (`fichar(j)`).
>
> ¿El parte sobrevive si muere el todo? Si no → composición. Si sí → agregación. La misma prueba de la nota U2-03, aplicada al código.

---

## 🎬 9. Del diagrama de secuencia al código

> [!info] 📖 Del deck (p. 25 y p. 28)
> El deck cierra con "traducir un diagrama de secuencia en código fuente y viceversa". El mapeo es directo:
>
> | En el diagrama de secuencia | En el código |
> |---|---|
> | **lifeline** de un objeto | una instancia (un atributo) |
> | **activation** | la pila de llamadas: el objeto está ejecutando un método |
> | **mensaje** | una llamada a método (y su retorno, si la flecha es punteada) |
> | **mensaje asíncrono** | un `ExecutorService.submit(...)` o un evento |
> | **destroy** | el objeto se descarta: `=null` o sale del ámbito |

> [!example] 🔧 Una secuencia y su código
> ```java
> // lifeline: Estudiante -> Sistema -> Pago
> class Sistema {
>     void registrar(Estudiante e, double monto) {
>         if (validar(e)) {              // frame alt/opt
>             cobro(monto);             // mensaje síncrono
>             e.confirmar();            // mensaje de retorno
>         }
>     }
> }
> ```

---

## ⚠️ Problemas Comunes y Soluciones

> [!danger] ❌ Error 1: El diagrama promete más de lo que el código cumple
>
> **Síntomas:** el diagrama dice `Empleado 1 ── * Proyecto` y la clase tiene `private Proyecto proyecto;` (una sola referencia).
>
> **Solución:** la multiplicidad es un contrato: `*` → `List<Proyecto> proyectos`. Si el código no puede cumplir lo que el diagrama dice, cambia el diagrama o cambia el código — pero no ambos a la mitad.

> [!danger] ❌ Error 2: Confundir agregación con composición en el código
>
> **Síntomas:** el todo **crea** a los partes y además los guarda en una colección que sobrevive → el diagrama dice rombo blanco, pero el código es composición.
>
> **Solución:** decide por la **prueba de supervivencia** y escribe el constructor en consecuencia: `new` dentro = composición; recibe instancias existentes = agregación.

> [!danger] ❌ Error 3: Dependencia que en realidad es asociación
>
> **Síntomas:** la flecha punteada en el diagrama, pero el código guarda el objeto en un atributo permanente.
>
> **Solución:** o cambias el diagrama a asociación, o el código a uso temporal (parámetro o local). Un `import` no es evidencia de dependencia con una clase **propia**: en Java, importar es usar tipos de otro paquete.

> [!danger] ❌ Error 4: Interface con estado propio
>
> **Síntomas:** la interface "Impresión" guarda saldo y contadores.
>
> **Solución:** la interface es **contrato de comportamiento**; el estado va en la clase que la implementa. Si la interface necesita datos, se los recibe como parámetro.

---

## 🎯 Mejores Prácticas

> [!tip] 🏆 Checklist de traducción
>
> 1. **Una relación, un atributo.** Si el diagrama tiene dos líneas entre las mismas clases, el código tiene dos atributos.
> 2. **Multiplicidad primero.** Decide colección o referencia antes de escribir la clase.
> 3. **Visibilidad coherente.** El `-` del diagrama es `private` + getter; el `+` es `public`.
> 4. **El que crea, es dueño.** Composición = `new` dentro; agregación =_instances que ya existen.
> 5. **Nombre de la relación = nombre del atributo** en la clase de asociación (regla del deck, p. 22).

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Nivel 1 — Básico
>
> **1.** Escribe la clase `Factura` que se relaciona con `Cliente` (1 cliente → `0..*` facturas). ¿Qué tipo de atributo usas?
> **2.** Convierte la composición `Pedido ◆— LineaPedido` en Java. ¿Quién crea la línea?
> **3.** ¿Qué palabra reservada aparece por la generalización y cuál por la realización?
>
> > [!success]- ✅ Respuestas — Nivel 1
> > >
> > - **1.** `private List<Factura> facturas = new ArrayList<>();` — `*` o `0..*` → colección.
> > - **2.** El `Pedido`: `lineas.add(new LineaPedido(p, cantidad));` dentro del constructor o del método de agregado.
> > - **3.** `extends` (generalización) e `implements` (realización).

> [!example] 📋 Nivel 2 — Intermedio
>
> **4.** El diagrama tiene `Empresa 1 ── * Empleado` y `Empleado 1 ── 1 Empresa`. ¿Cuántos atributos y de qué tipo? ¿Es bidireccional?
> **5.** Explica por qué `import java.util.List;` **no** es una dependencia UML entre tus clases.
> **6.** Una interface `Paginable` declara `int total()`. La clase `Factura` la implementa y además guarda `private double saldo`. ¿Qué está mal y cómo lo corriges?
>
> > [!success]- ✅ Respuestas — Nivel 2
> > >
> > - **4.** Dos atributos: `private List<Empleado> empleados` en `Empresa` y `private Empresa empresa` en `Empleado`. Sí es bidireccional: ambos lados se referencian.
> > - **5.** Porque importar es usar tipos de otro **paquete**; no hay relación entre tus clases. La dependencia UML es entre clases de tu modelo, y se ve como parámetro o uso temporal.
> > - **6.** Nada está mal: la interface declara solo el contrato (`total()`), y el estado (`saldo`) vive en la clase que la implementa. La interface no debe guardar estado.

> [!example] 📋 Nivel 3 — Avanzado
>
> **7.** Modela `Factura ◆— LineaFactura` con `LineaFactura` usando el **nombre de la relación** como atributo, y luego invierte el diseño para que la línea sea una clase de asociación. ¿Qué cambia en el diagrama y en el código?
> **8.** Un diagrama de secuencia tiene 4 lifelines y 12 mensajes, dos de ellos con frame `opt`. Escribe la firma de los métodos que la secuencia sugiere y di cuáles serían opcionales.
> **9.** Tu código ya está escrito y el diagrama nunca se hizo. Reconstruye el diagrama de clases: ¿qué artefactos del código usas y cómo reconoces la relación entre dos clases?
>
> > [!success]- ✅ Respuestas — Nivel 3
> > >
> > - **7.** En composición, la línea es un atributo de la factura (`private List<LineaFactura> lineas`) y se crea dentro. Como clase de asociación, la línea cuelga de la línea del diagrama (`Factura ── LineaFactura ── Producto`) y es una clase propia con sus atributos; el código queda igual en estructura, pero la relación pasa a ser un objeto con nombre.
> > - **8.** Una firma por mensaje dirigido a otra lifeline; los dos del frame `opt` son métodos cuyo cuerpo solo actúa "si se cumple la condición" (p. ej. `aplicarDescuento()` opcional dentro de `cobrar()`).
> > - **9.** Mapeas: atributos → clases y atributos; dos clases unidas por un atributo de una a la otra → asociación; `extends`/`implements` → generalización/realización; creación de objetos dentro del constructor → composición.

> [!example] 📋 Extra Control03 (formato papel)
>
> **10.** Escribe en papel el código de la relación `Cliente 1 ── 0..* Transaccion` con `Transaccion` como clase de asociación, y di en una frase quién instancia la `Transaccion`.
>
> > [!success]- ✅ Respuestas — Extra
> > >
> > - **10.** `Transaccion` con atributos `cliente`, `cuenta`, `monto` y `fecha`; en `Cliente`, `private List<Transaccion> transacciones`. La instancia la crea el **método del Cliente** que ejecuta la relación (p. ej. `RealizarTransaccion()`), tal como dice el deck (p. 10).

---

## 📋 Resumen Ejecutivo

> [!summary] 📋 Lo Esencial
>
> - Cada relación del diagrama tiene **una traducción fija** en código: atributo, `extends`, `implements`, `import` o clase propia.
> - **Multiplicidad = tipo del atributo**: `1` → referencia, `*` → colección.
> - **Composición = el todo crea**; **agregación = el todo recibe** lo que ya existía.
> - La **clase de asociación** se instancia **al ejecutar la relación**.
> - La **generalización** se reconoce por el nombre **en cursiva** → clase abstracta.
> - La **dependencia** es de uso temporal; si la guardas en un atributo, es asociación.

---

## ✅ Metas de Aprendizaje

> [!note] 🎯 Nivel Básico
> - [ ] Traduzco asociación, generalización y realización a código.
> - [ ] Elijo referencia o colección según la multiplicidad.

> [!note] 🎯 Nivel Intermedio
> - [ ] Distingo composición de agregación en el constructor.
> - [ ] Implemento una clase de asociación con sus atributos.

> [!note] 🎯 Nivel Avanzado
> - [ ] Reconstruyo un diagrama de clases a partir del código.
> - [ ] Traduzco una secuencia a firmas de métodos, marcando los opcionales.

---

## 📊 Resumen Visual

![[../Diagramas/dsw-u2-06-02-mind.svg]]

---

## 🚀 Próximos Pasos

> [!quote] 🌟 Continuando
>
> **Has aprendido:**
>
> ✅ Cada relación del diagrama traducida a código
> ✅ Multiplicidad como tipo del atributo
> ✅ Composición vs agregación en el constructor
>
> **Próximo tema Unidad 3:**
>
> | Tema | Qué verás | Por qué importa |
> |---|---|---|
> | **Patrones de diseño** | Soluciones probadas con Shalloway | Dejas de reinventar la rueda |

---

## 🔁 Repaso SR (flashcards)

#flashcards/diseno-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Asociación en código?::Un atributo que guarda la referencia al otro objeto (con getter/setter si es privada).
> - ¿Multiplicidad `*`?::El atributo es una colección (`List<...>`), no una referencia simple.
> - ¿Composición en código?::El todo **crea** a los partes (`new` dentro) y muere con ellos: rombo negro.
> - ¿Agregación en código?::El todo **recibe** partes que ya existían: rombo blanco.
> - ¿Clase de asociación?::Clase propia para los datos de la relación; se instancia al ejecutar la relación.
> - ¿Generalización?::`extends`; el nombre en cursiva del diagrama = `abstract class`.
> - ¿Realización?::`implements`; la interface es solo contrato (`ImprimirRecibo()`, `EstadoCuenta()`).
> - ¿Dependencia?::Uso temporal: parámetro o `import`. Si la guardas en un atributo, es asociación.
> - ¿Secuencia → código?::Cada lifeline es una instancia, cada mensaje una llamada a método, cada `opt`/`alt` una condición.

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Diseño de Software]]
> - Índice Unidad 2: [[00 - Índice Unidad 2]]
> - Anterior: [[04 - UML casos de uso, secuencia y actividad]]
> - Syllabus: [[Bienvenida y Syllabus Diseño de Software]]

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - Deck de cátedra: [[../Unidad 0 - Guias y Ejercicios/Diapositivas/04bImplementaciónDesdeDiseno.pdf|04b Proceso de implementación a partir de un diseño]] (30 p., Unidad 2) — relaciones en diagramas de clases (pp. 4-5), asociación y su código (pp. 8-9), clase de asociación (p. 10), bidireccionalidad (pp. 11-14), generalización (pp. 17-18), realización (pp. 19-20), dependencia (pp. 21-22), composición y agregación (pp. 23-24) y secuencia a código (p. 25).
> - Deck de la misma sesión: [[../Unidad 0 - Guias y Ejercicios/Diapositivas/04aLenguajeUnificadoModelado.pdf|04a Lenguaje unificado de modelado]] — la notación que este nota traduce.
> - P. Stevens, R. Pooley, *Using UML*, 2nd ed. — notación UML base.
> - R. Pressman, B. Maxim, *Software Engineering: A Practitioner's Approach* — Apéndice 1 (notación de clases).
> - Capturas de la clase: [[SIEL - Modelo de Clases]] y [[SIEL - Casos de Uso]].

---

**Tags:** #CCPG1042 #unidad2 #uml #codigo #diseno-software
