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

> [!note] 🗺️ Diagrama — Introducción
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u2-06-01-flow.svg]]
>
> **Se lee así:** Un flowchart con un nodo de entrada «Relación en el diagrama de clases» que abre un rombo «¿Qué relación?» con siete salidas —Asociación (atributo de referencia + getter/setter), Clase de asociación (clase propia con sus atributos), Agregación (referencia al todo, el parte sobrevive), Composición (el todo CREA el parte y lo destruye), Generalización (`extends`, clase abstracta), Realización (`implements`, interface) y Dependencia (import/parámetro sin estado guardado)— y las siete convergen en una caja final «Código fuente».
>
> **Por qué importa:** Es el mapa de traducción completo de la unidad: cada relación del diagrama tiene una salida única en Java, y todas terminan en el mismo entregable.
>
> **Ejemplo:** En tu proyecto, `Factura` y `Cliente` entran por la rama «Asociación» y salen como `private Cliente cliente;` dentro de `Factura`.

> [!tip] 💡 La regla del deck
>
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
>
> **Se lee así:** La tabla traduce las siete relaciones del deck a su forma en código, y lo hace con tres preguntas: ¿quién crea?, ¿sobrevive? y ¿guarda datos? Cada fila da el símbolo del diagrama y la construcción de Java que le corresponde.
>
> **Por qué importa:** Es la tabla que hay que memorizar para el examen: si no puedes pasar de una fila a la otra, no sabes traducir el diagrama.
>
> **Ejemplo:** La fila 5 (Realización) es la que explica por qué `CuentaBancaria implements Impresion` necesita dos métodos implementados y no un atributo.

> [!note] 🖼️ captura 04b-p5 — Las 7 relaciones del diagrama de clases
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p5-tabla-relaciones.png]]
>
> **Se lee así:** Lámina de 04b, p. 5: un esquema-resumen titulado «Relaciones en DC» que reagrupa las siete relaciones del deck en familias —asociación simple y asociación directa, agregación, composición, herencia/generalización, realización y dependencia— cada una con su símbolo junto al nombre.
>
> **Por qué importa:** Ordena las relaciones por familias (asociaciones, parte/todo, jerarquía, contrato y uso), que es justo la forma en que se memorizan para el examen.
>
> **Ejemplo:** Al leer tu diagrama decides primero la familia: ¿es parte/todo, jerarquía, contrato o solo uso temporal?

---

## 🔗 1. Asociación: la relación más común

> [!info] 📖 Qué es
> Dos clases que **se conocen**: una guarda una referencia a la otra. No implica propiedad: el `Cliente` conoce su `CuentaBancaria`, y viceversa no es obligatorio.
>
> **Se lee así:** La lámina de 04b, p. 8 titula la relación «Asociación» y la p. 9 la lleva al código: la línea del diagrama se convierte en un atributo que guarda la referencia.
>
> **Por qué importa:** Aclarar que la asociación no implica propiedad evita el error de pensar que el `Cliente` es «dueño» de la `CuentaBancaria` y de asignarle su ciclo de vida.
>
> **Ejemplo:** En `Cliente` del banco, `private CuentaBancaria cuenta;` dice «conozco una cuenta», no «la cuenta existe porque yo existo».

> [!info] 💡 1. Asociación: la relación más común
>
> En el diagrama se dibuja como una línea con multiplicidad; en el código es un **atributo**.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p9-codigo-asociacion.png]]
>
> **Se lee así:** Lámina de 04b, p. 9: dos clases Java lado a lado —`Cliente` con `id`, `direccion` y un `ArrayList<CuentaBancaria> cuentas`, y `CuentaBancaria` con `nro_cuenta`, `saldo` y sus getters/setters— mostrando que la línea del diagrama se materializa como un atributo.
>
> **Por qué importa:** Es la traducción literal de la asociación, con la colección que corresponde a la multiplicidad `*`.
>
> **Ejemplo:** `Factura` con `private Cliente cliente;` y `Cliente` con `private List<Factura> facturas` reproducen exactamente esta lámina.

> [!example] 🔧 Asociación en Java
>
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
>
> - `1` → una referencia: `private CuentaBancaria cuenta;`
> - `0..*` o `*` → una colección: `private List<Factura> facturas = new ArrayList<>();`
> - `0..1` → referencia **anulable** (`null` = "todavía no"): `private CuentaBancaria cuenta;`

---

## 🧷 2. Clase de asociación: la relación que tiene datos

> [!info] 📖 Qué dice el deck (p. 10)
> "La **clase de asociación se instancia al ejecutar la relación** entre `Cliente` y `CuentaBancaria`. `RealizarTransaccion()` **asocia** los clientes y las cuentas."
>
> **Se lee así:** La lámina de 04b, p. 10 lleva la frase textual del deck y el dibujo de la relación con su clase de asociación colgando de la línea.
>
> **Por qué importa:** Aclara quién crea el objeto de la relación: no el diagrama ni el framework, sino el método del cliente que ejecuta la relación.
>
> **Ejemplo:** En el SIEL, el método que inscribe una candidatura es el que instancia el objeto `Inscripcion` con su fecha y su estado.

> [!info] 💡 2. Clase de asociación: la relación que tiene datos
>
> O sea: la relación **es un objeto**. Nace una clase propia con sus atributos, y la línea del diagrama se convierte en un atributo de esa clase.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p4-relaciones.png]]
>
> **Se lee así:** Lámina de 04b, p. 4: la frase «Las clases deben estar relacionadas con otras» sobre los siete casos numerados del deck, cada uno con su notación —dependencia (línea punteada), asociación (línea), asociación dirigida (flecha abierta), agregación (rombo blanco), composición (rombo negro), generalización (triángulo hueco) y realización (punteada con triángulo hueco).
>
> **Por qué importa:** Es la lámina que define las siete relaciones que esta nota traduce a código: el símbolo del diagrama es la partida para saber qué palabra reservada toca.
>
> **Ejemplo:** El rombo negro de `Pedido ◆— LineaPedido` es lo que te dice que el `Pedido` hace `new LineaPedido(...)`.

> [!example] 🔧 Clase de asociación en Java
>
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
>
> Es exactamente el `Prestamo` entre `Copia` y `Socio` de la Biblioteca, o la `Inscripcion` entre `OrganizacionPolitica` y `Candidatura` del SIEL. La relación con datos **nace como clase**.

---

## 🔄 3. Bidireccionalidad: quién conoce a quién

> [!info] 📖 Qué es
> Una asociación puede ser **unidireccional** (A conoce a B, B no conoce a A) o **bidireccional** (A conoce a B y B conoce a A). El deck dedica cuatro páginas (pp. 11-14) a las variantes, porque **es el punto donde los diagramas se contradicen con el código**.
>
> **Se lee así:** Las pp. 11-14 del deck recorren las variantes de la bidireccionalidad y su código: la p. 11 muestra el caso «Bidireccional con multiplicidad 0..1» entre `Cliente` y `CtaCte`, con el nombre de rol `+dueño` y el atributo `public Cliente dueño;` en la cuenta.
>
> **Por qué importa:** Cuatro páginas para un solo tema dicen que es donde más se equivocan los equipos: la flecha doble del diagrama son dos atributos, y hay que mantenerlos sincronizados.
>
> **Ejemplo:** En `Cliente.abrir(cuenta)`, además de agregar la cuenta a la lista hay que hacer `cuenta.setTitular(this)`; si no, el diagrama y el código dejan de contarse.

> [!note] 🖼️ captura 04b-p11 — 3. Bidireccionalidad: quién conoce a quién
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p11-bidireccionalidad.png]]
>
> **Se lee así:** Lámina de 04b, p. 11: el caso «Bidireccional con multiplicidad 0..1» dibujado con `Cliente` y `CtaCte` unidos por una línea con flecha en ambos sentidos, el nombre de rol `+dueño` sobre el lado de la cuenta, y el código donde cada clase guarda la referencia al otro (`public Cliente dueño;` dentro de `CtaCte`).
>
> **Por qué importa:** La bidireccionalidad no es solo la flecha: son dos atributos que hay que mantener sincronizados, y el deck le dedica cuatro páginas por eso.
>
> **Ejemplo:** En `Cliente.abrir(cuenta)` del curso, además de agregar la cuenta a la lista hay que hacer `cuenta.setTitular(this)`.

> [!example] 🔧 Las dos formas
>
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
>
> Poner la relación **solo en el diagrama** y no en el código, o al revés: el diagrama muestra `1 ── *` y el código guarda una sola referencia. **La multiplicidad es un contrato del código**: si dice `*`, el atributo es una colección.

---

## 🔢 4. Múltiples relaciones y recursividad

> [!info] 📖 Del deck (pp. 15-16)
> - **Múltiples relaciones:** dos clases pueden estar unidas por **más de una** asociación a la vez (p. ej. `Empleado` ↔ `Empresa`: *trabaja para* y *es dirigida por*). Cada una necesita su propio atributo.
> - **Recursividad:** una clase se relaciona **consigo misma** (un empleado es jefe de otro empleado). En código, el atributo apunta al mismo tipo.
>
> **Se lee así:** La p. 15 del deck titula «Múltiples relaciones» y la p. 16 «Asociación con recursividad»: en ambos casos el diagrama muestra una relación que se sale de la forma clase–clase habitual.
>
> **Por qué importa:** Las dos relaciones son las que más se olvidan al escribir el código: si hay dos líneas entre las mismas clases, hacen falta dos atributos, y si la relación es consigo misma, el atributo es del mismo tipo.
>
> **Ejemplo:** `Empleado` guarda `private Empresa empresa;` y `private Empleado jefe;`: son dos atributos distintos, y el segundo apunta al mismo tipo que la clase.

> [!example] 🔧 Ejemplo
>
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
>
> **Se lee así:** La p. 18 del deck titula «Generalización» y muestra la frase textual junto al código: `public abstract class CuentaBancaria implements Impresion` y `public final class Ahorros extends CuentaBancaria`.
>
> **Por qué importa:** Es la regla que conecta la notación con el lenguaje: si el nombre va en cursiva, en Java la clase es `abstract` y no se instancia.
>
> **Ejemplo:** `Dignidad` en cursiva en tu diagrama del SIEL se traduce como `abstract class Dignidad`, que nadie instancia directamente.

> [!note] 🖼️ captura 04b-p18 — 5. Generalización: `extends` y clase abstracta
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p18-generalizacion.png]]
>
> **Se lee así:** Lámina de 04b, p. 18: el código de la jerarquía del deck —`public abstract class CuentaBancaria implements Impresion` y `public final class Ahorros extends CuentaBancaria` con sus atributos (`nro_cuenta`, `interes_anual`, `saldo`) y métodos— más el recordatorio de que en el diagrama de clases el nombre de la clase abstracta va en cursiva.
>
> **Por qué importa:** El nombre en cursiva del diagrama es el que te dice que la clase va `abstract`; sin leerlo, la herencia se implementa como una clase concreta que se puede instanciar.
>
> **Ejemplo:** `Dignidad` en cursiva en tu diagrama del SIEL se traduce como `abstract class Dignidad`, que nadie instancia directamente.

> [!example] 🔧 Generalización en Java
>
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
>
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
>
> **Se lee así:** La p. 19 del deck titula «Ejemplo - Realización» y resume en dos viñetas que `Impresión` es una interface y que `CuentaBancaria` la implementa desarrollando `ImprimirRecibo()` y `EstadoCuenta()`; la p. 20 dibuja el código con la interface al lado de la clase.
>
> **Por qué importa:** Separa las dos mitades de la realización: la interface declara el contrato y la clase lo desarrolla. Por eso en el diagrama la interface no tiene compartimentos.
>
> **Ejemplo:** `<<interface>> Pagable` con `+pagar(monto : double) : Comprobante` es el contrato que la `Factura` del curso implementa.

> [!note] 🖼️ captura 04b-p20 — 6. Realización: `implements` y el contrato
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p20-realizacion.png]]
>
> **Se lee así:** Lámina de 04b, p. 20: la interface `Impresion` con sus dos métodos (`ImprimirRecibo()` y `EstadoCuenta()`) al lado de la clase `CuentaBancaria implements Impresion`, con los cuerpos todavía como «TODO implement here».
>
> **Por qué importa:** La interface declara el contrato y la clase lo desarrolla: por eso en el diagrama la interface no tiene compartimentos que mostrar.
>
> **Ejemplo:** `<<interface>> Pagable` con `+pagar(monto : double) : Comprobante` es el contrato que la `Factura` del curso implementa.

> [!example] 🔧 Realización en Java
>
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
>
> La interface **no tiene interior que mostrar** en el diagrama (por eso se dibuja como paleta o círculo): solo promete operaciones. Quien la usa depende del **contrato**, no de la clase concreta — es el mismo criterio que ya usabas en la nota de componentes e interfaces (U2-02).

---

## 🔗 7. Dependencia: el `import` disfrazado

> [!info] 📖 Del deck (p. 21)
> "Indica que los **cambios sobre la clase B pueden afectar a la clase A**. `ClassA` **usa los servicios** de `ClassB`. En Java se podría representar con un `import`."
>
> **Se lee así:** La p. 21 del deck titula «Dependencia» y da las tres viñetas textuales (los cambios en B pueden afectar a A, A usa los servicios de B y en Java se podría representar con un `import`); la p. 22 lo muestra en código.
>
> **Por qué importa:** Define la dependencia como un vínculo de uso, no de estado: quien depende no guarda al otro, solo lo usa mientras dura la llamada.
>
> **Ejemplo:** `Reporte` usa `LocalDate` como parámetro o variable local; si lo guardara en un atributo, ya no sería dependencia sino asociación.

> [!note] 🖼️ captura 04b-p22 — 7. Dependencia: el `import` disfrazado
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p22-dependencia.png]]
>
> **Se lee así:** Lámina de 04b, p. 22: el ejemplo de dependencia con `import authentication.MetodoAutenticacion;` y la clase `Login` que declara `private string user`, `private string pass` y un método `ValidarCredenciales(MetodoAutenticacion metodo)` que recibe el tipo como parámetro.
>
> **Por qué importa:** La dependencia se ve en el `import` y en el parámetro: el objeto usado no queda guardado en ningún atributo.
>
> **Ejemplo:** Si `Login` guardara `private MetodoAutenticacion metodo;` ya no sería dependencia sino asociación — el error 3 de esta nota.

> [!example] 🔧 Dependencia en Java
>
> ```java
> import java.time.LocalDate;      // <- dependencia: ClassA usa los servicios de ClassB
> // ---
> class Reporte {
>     private LocalDate fecha;      // ... y solo mientras dura la llamada
> }
> ```

> [!danger] ❌ Dependencia que se disfraza de asociación
>
> Si guardas el objeto de la clase B en un **atributo**, ya no es dependencia: es una **asociación**. La dependencia es de **uso temporal**: un parámetro, un `import`, una variable local que muere al salir del método.

---

## 🧱 8. Composición y agregación: quién manda

> [!info] 📖 Del deck (pp. 23-24)
> El deck las llama "ejemplificación" y las muestra con los mismos ejemplos del curso: la **composición** es el rombo negro, la **agregación** el rombo blanco.
>
> **Se lee así:** Dos láminas contiguas del deck (pp. 23-24) tituladas «Ejemplificación de composición» y «Ejemplificación de Agregación», ambas con la clase `Automovil`: en la primera el constructor hace `new Estereo()` y `new Motor()`; en la segunda hay un constructor vacío y un método `ensamblar(Estereo e, Motor m)`.
>
> **Por qué importa:** El deck no explica la diferencia: la muestra en el código. El contraste entre las dos láminas es exactamente la prueba de supervivencia aplicada al constructor.
>
> **Ejemplo:** `Pedido` con `new LineaPedido(...)` dentro se parece a la p. 23; `Equipo.fichar(jugador)` se parece a la p. 24.

> [!note] 🖼️ captura 04b-p23 — 8. Composición y agregación: quién manda
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p23-composicion.png]]
>
> **Se lee así:** Lámina de 04b, p. 23: el ejemplo `Automovil` con los atributos `Estereo estereo` y `Motor motor`, y un constructor que hace `estereo = new Estereo();` y `motor = new Motor();` —las dos piezas creadas dentro del propio todo— sobre el diagrama con rombo negro.
>
> **Por qué importa:** El `new` dentro del constructor es la señal inequívoca de composición: el todo es dueño y el parte nace con él.
>
> **Ejemplo:** En el curso, `Pedido` con `lineas.add(new LineaPedido(p, cantidad))` es exactamente esta lámina.

> [!note] 🖼️ captura 04b-p24 — 8. Composición y agregación: quién manda
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p24-agregacion.png]]
>
> **Se lee así:** Lámina de 04b, p. 24: el mismo `Automovil` pero con un constructor vacío y un método `ensamblar(Estereo e, Motor m)` que recibe las piezas ya hechas y las guarda; el diagrama marca la relación como agregación, con rombo blanco.
>
> **Por qué importa:** El contraste con la lámina anterior es la lección: en agregación el todo recibe partes que ya existían, y por eso el parte sobrevive.
>
> **Ejemplo:** `Equipo.fichar(jugador)` recibe un `Jugador` que ya existía, mientras que `Pedido` crea sus líneas.

> [!example] 🔧 La diferencia en el código
>
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
>
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
>
> **Se lee así:** La p. 25 del deck anuncia el cierre («Traduciendo un diagrama de secuencia en código fuente y viceversa») y la p. 28 lista los dos puntos para recordar: ir del diagrama de clase al código y del diagrama de secuencia al código, en ambos sentidos.
>
> **Por qué importa:** El «viceversa» es la parte que se examina: si el código ya existe, el diagrama se genera y cualquier diferencia revela que el modelo estaba mal.
>
> **Ejemplo:** De los tres mensajes de tu secuencia de inscripción salen tres firmas: `inscribirse(curso)`, `verificarCupo(curso)` y `confirmarInscripcion()`.

> [!example] 🔧 Una secuencia y su código
>
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

## 🗺️ Diagrama de Decisión: ¿Qué Relación Pongo?

> [!note] 🗺️ Diagrama — Diagrama de Decisión: ¿Qué Relación Pongo?
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u2-06-03-flow.svg]]
>
> **Se lee así:** el diagrama es una ** cascada de preguntas** que arranca en «Dos clases se
> relacionan» y va bajando por seis decisiones hasta llegar al código Java. La primera pregunta
> («¿El todo CREA y DESTRUYE al parte?») separa **composición** de todo lo demás; la segunda
> («¿Solo comparten el dato? ¿el parte sobrevive?») separa **agregación**; la tercera busca un tipo
> más específico (**generalización**); la cuarta un contrato (**realización**); la quinta un uso
> puntual sin guardar estado (**dependencia**); y la última, si la relación lleva datos propios
> (**clase de asociación**) o es simple (**asociación**). Cada respuesta lleva escrita la forma
> exacta en Java: `extends`, `implements`, `import`, rombo negro, rombo blanco.
>
> **Por qué importa:** las 7 relaciones del deck no se distinguen por instincto sino por **tres
> preguntas concretas**: ¿quién crea?, ¿sobrevive?, ¿guarda datos? Un diagrama bien hecho sale de
> recorrer esta cascada en orden; si te saltas a «es composición» sin responder, el código y el
> diagrama van a discrepar — y ese es el error 1 de la sección siguiente.
>
> **Ejemplo:** para modelar `Factura → Cliente`, la cascada dice: el cliente ya existe y lo
> recibe la factura (**agregación**), no lo crea ni lo destruye (**no** composición), y la relación
> no lleva atributos propios (**no** clase de asociación) → asociación o agregación simple, con
> `private Cliente cliente;` en la factura.
>
> **Atajo cuando el tiempo aprieta:** la respuesta corta es la **prueba de supervivencia**: si el
> objeto desaparece cuando muere el otro, es composición; si sobrevive, es agregación.

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
>
> - [ ] Traduzco asociación, generalización y realización a código.
> - [ ] Elijo referencia o colección según la multiplicidad.

> [!note] 🎯 Nivel Intermedio
>
> - [ ] Distingo composición de agregación en el constructor.
> - [ ] Implemento una clase de asociación con sus atributos.

> [!note] 🎯 Nivel Avanzado
>
> - [ ] Reconstruyo un diagrama de clases a partir del código.
> - [ ] Traduzco una secuencia a firmas de métodos, marcando los opcionales.

---

## 📊 Resumen Visual

> [!note] 🗺️ Diagrama — Resumen Visual
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u2-06-02-mind.svg]]
>
> **Se lee así:** Mapa mental con raíz «Del diagrama al código» y siete ramas —una por relación—: Asociación (atributo de referencia, getter y setter, multiplicidad a colección), Clase de asociación (clase propia, atributos de la relación, se instancia al ejecutar la relación), Agregación (referencia al todo, el parte sobrevive), Composición (el todo crea el parte, el todo lo destruye), Generalización (`extends`, clase abstracta en cursiva), Realización (`implements`, interface con contrato) y Dependencia (import o parámetro, sin estado guardado).
>
> **Por qué importa:** Es el índice de la unidad: las siete ramas son las siete relaciones del deck y cada hoja es la construcción de Java que le toca.
>
> **Ejemplo:** Para tu proyecto, recorre las ramas y marca en cuáles caes: si tu relación es parte/todo, la rama de agregación o la de composición decide quién escribe el `new`.

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
> - Mapa de contenido: [[../Diseño de Software|Diseño de Software]]
> - Anterior: [[04 - UML casos de uso, secuencia y actividad]]
> - Syllabus: [[../Bienvenida y Syllabus Diseño de Software|Bienvenida y Syllabus Diseño de Software]]

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - Deck de cátedra: [[../Unidad 0 - Guias y Ejercicios/Diapositivas/04bImplementaciónDesdeDiseno.pdf|04b Proceso de implementación a partir de un diseño]] (30 p., Unidad 2) — relaciones en diagramas de clases (pp. 4-5), asociación y su código (pp. 8-9), clase de asociación (p. 10), bidireccionalidad (pp. 11-14), generalización (pp. 17-18), realización (pp. 19-20), dependencia (pp. 21-22), composición y agregación (pp. 23-24) y secuencia a código (p. 25).
> - Deck de la misma sesión: [[../Unidad 0 - Guias y Ejercicios/Diapositivas/04aLenguajeUnificadoModelado.pdf|04a Lenguaje unificado de modelado]] — la notación que este nota traduce.
> - P. Stevens, R. Pooley, *Using UML*, 2nd ed. — notación UML base.
> - R. Pressman, B. Maxim, *Software Engineering: A Practitioner's Approach* — Apéndice 1 (notación de clases).
> - Capturas de la clase: [[Caso SIEL - Modelo de Clases]] y [[Caso SIEL - Casos de Uso]].

---

**Tags:** #CCPG1042 #unidad2 #uml #codigo #diseno-software
