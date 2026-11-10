---
dg-publish: true
tags: [CCPG1042, unidad1, solid, principios]
---

# 🖐️ Principios SOLID

## 🎯 Introducción

> [!info] 💡 ¿Por Qué 5 Reglas Valen un Parcial?
>
> **SOLID** son 5 principios de diseño orientado a objetos que convierten "código que funciona" en "diseño que aguanta cambios". El docente les dedica una semana completa: si tus clases los violan, los patrones llegan tarde.
>
> Robert C. Martin los reunió en los años 2000 (artículo *Design Principles and Design Patterns* y libro *Agile Software Development*), y Michael Feathers propuso el acrónimo **SOLID**. Los ingredientes son anteriores: Bertrand Meyer formuló el abierto/cerrado (1988) y Barbara Liskov la sustitución (1987). Hoy se explican con detalle en *Clean Architecture* (caps. 7 a 11).
>
> Son **principios, no leyes**: guían decisiones, y aplicarlos sin criterio también es un error (ver "Problemas Comunes").
>
> **Analogía del mundo real:** piensa en un taller mecánico:
>
> - **S** → Cada mecánico, una especialidad (no el mismo hace frenos y pinta).
> - **O** → Agregas un elevador nuevo sin demoler el taller (abierto a extensión).
> - **L** → Cualquier mecánico certificado hace el trabajo base (sustituible).
> - **I** → Manual por puesto, no un tomo para todos (interfaces justas).
> - **D** → Pides "un elevador", no "el Hidráulico-3000" (dependes de abstracciones).
>
> | Principio | 1 línea | Huele mal cuando... |
> |---|---|---|
> | **S**RP | Una razón para cambiar | La clase hace 3 cosas |
> | **O**CP | Abierto a extender, cerrado a modificar | Cada variante edita la misma clase |
> | **L**SP | La derivada sustituye a la base | Un `override` rompe el contrato |
> | **I**SP | Interfaces pequeñas por rol | Clientes obligados a implementar métodos inútiles |
> | **D**IP | Depende de abstracciones | `new Concreta()` regado por todos lados |

> [!note] 🗺️ Diagrama — Introducción
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u1-05-01-graph.svg]]
>
> **Se lee así:** El diagrama parte de "Clase con problemas" y pregunta "¿SOLID?". La respuesta se desglosa en cinco comprobaciones: *S: una misión*, *O: extiende sin editar*, *L: sustituye sin romper*, *I: interfaces justas* y *D: abstracciones*. No hay un nodo final: son cinco criterios de diagnóstico, no una secuencia.
>
> **Por qué importa:** cada letra del acrónimo es una pregunta que se le puede hacer a cualquier clase, y es la forma en que la nota va a diagnosticar cada una de las cinco violaciones.
>
> **Ejemplo:** en el proyecto de ESPOL, el `Main.java` de nómina que la nota usa como caso integrador tiene una respuesta distinta para cada letra, y por eso sirve como ejemplo de los cinco principios juntos.

---

## 🔗 SOLID en el Contexto de la Unidad

> [!note] 📋 De Cohesión y Acoplamiento a SOLID
>
> SOLID no aparece de la nada: es la **versión concreta, para objetos**, de las dos reglas de [[02 - Principios de diseño, cohesión y acoplamiento]] y vive dentro del paradigma estudiado en [[03 - Paradigmas de programación y diseño]].
>
> | Principio | Se apoya en... | Idea de fondo |
> |---|---|---|
> | **SRP** | Alta cohesión funcional | Cada clase, una misión |
> | **OCP** | Ocultamiento de información | Esconde detrás de una interfaz lo que cambia |
> | **LSP** | Contratos y polimorfismo | Herencia solo si respeta el comportamiento prometido |
> | **ISP** | Bajo acoplamiento | No dependas de lo que no usas |
> | **DIP** | Bajo acoplamiento + abstracción | Apunta tus dependencias hacia interfaces |

> [!info] 📖 El deck de cátedra: por qué SOLID (04p, pp. 3-12)
> El deck abre con **código limpio** (Robert C. Martin, "Uncle Bob") y luego muestra el problema que SOLID viene a resolver. Esta es la motivation literal de la diapositiva.
>
> **Se lee así:** El arranque del deck es el "código limpio": Robert C. Martin (Uncle Bob) empezó el debate de los principios SOLID a finales de los 1980, el grupo se consolidó en los 2000 y pasó a llamarse SOLID en 2004. El objetivo que el deck enuncia para estos principios es la creación de estructuras de software que toleren cambios, sean entendibles y sean la base de componentes que puedan ser reutilizables. Y el problema que resuelven aparece en la diapositiva "Bad Coding": rigidez (un cambio afecta muchas partes), fragilidad (fallos en lugares donde no debería) e inmovilidad (el código no se puede reusar fuera de su contexto original).
>
> **Por qué importa:** el deck no expone cinco reglas sueltas, sino una causa y cinco respuestas: los males del código enredado son el motivo y SOLID es el remedio.
>
> **Ejemplo:** en el proyecto de ESPOL, el trío de males sirve de diagnóstico: si un cambio de requisitos toca tres archivos, hay rigidez; si un fallo aparece donde no lo tocaste, hay fragilidad.

> [!note] 🖼️ captura 04p-p10 — SOLID en el Contexto de la Unidad
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Principios/dsw-04p-p10.png]]
>
> **Se lee así:** La diapositiva "Bad Coding…" describe el código espagueti: "In spaghetti code, the relations between the pieces of code are so tangled that it is nearly impossible to add or change something without unpredictably breaking something somewhere else". Es el punto de partida del deck: el problema que SOLID viene a resolver.
>
> **Por qué importa:** enuncia por qué existen los principios: no es purismo de estilo, es que las relaciones enredadas hacen que cualquier cambio rompa algo en otro lugar sin que se pueda anticipar.
>
> **Ejemplo:** en el proyecto de ESPOL, cuando agregar un método nuevo obliga a revisar cinco clases porque todas se llaman entre sí, se está frente a ese mismo código espagueti.

> [!note] 💡 El trío de males del deck (p. 11)
>
> **El trío de males del deck (p. 11):**

> [!note] 📊 Tabla — SOLID en el Contexto de la Unidad
>
> | Mal | Qué significa en el deck |
> |---|---|
> | **Rigidez** | Un cambio afecta muchas partes |
> | **Fragilidad** | Fallos en lugares donde no debería |
> | **Inmovilidad** | No se puede reusar el código fuera de su contexto |

> [!note] 💡 Y la salida
>
> **Y la salida:** SOLID — *S* Single Responsibility, *O* Open-Closed, *L* Liskov Substitution, *I* Interface Segregation, *D* Dependency Inversion. Los principios "nos dicen cómo ordenar nuestras funciones y estructuras de datos en clases".

---

## 🧵 Los 5 Principios, Uno por Uno

### 🎯 S — Single Responsibility Principle (SRP)

> [!note] 🎯 SRP — Una clase, una razón para cambiar
>
> - **Definición:** una clase tiene una, y solo una, razón para cambiar. Martin lo refina en *Clean Architecture*: un módulo debe ser responsable ante **un solo actor** (una sola persona o área que puede pedir cambios).
> - **Equivalente en la unidad:** cohesión funcional.
> - **Código malo:** `class Factura { calcularTotal(); guardarEnBD(); imprimir(); }`: tres actores distintos (contabilidad, TI, ventas) que pueden pedir cambios en la misma clase.
> - **Código bueno:** `Factura`, `RepositorioFactura`, `ImpresorFactura`, cada una con una misión.
> - **Test de 10 s:** describe la clase sin usar "y".
> - **Violación típica:** `Manager`, `Util`, `Helper` con 30 métodos estáticos; la "Clase Dios".
> - **Malentendido común:** SRP **no** significa "una clase con un solo método". Significa un solo motivo de cambio.
> - **Caso clásico (freeCodeCamp/Sabalete 2022):** `Factura` con `calculaTotal()` + `imprimeFactura()` + `guardarArchivo()` = 3 razones para cambiar (cálculo, formato, persistencia). Remedio: `FacturaImpresion` + `FacturaPersistencia` separadas. Si ves impresión o guardado dentro de lógica de negocio, es SRP roto.
>
> [!example]- 💻 Código — SRP antes y después
>
> ```java
> // ❌ SRP ROTO — tres actores pueden pedir cambios sobre la misma clase
> class Factura {
>     double calcularTotal() { /* regla de contabilidad */ return 0; }
>     void guardar()         { /* SQL: cambia si cambia la BD */ }
>     String imprimir()      { /* formato: cambia si cambia el diseño */ return ""; }
> }
> // ---
> // ✅ SRP — cada clase responde a un solo actor
> class Factura {
>     double calcularTotal() { /* solo regla de negocio */ return 0; }
> }
> class RepositorioFactura {
>     void guardar(Factura f) { /* solo persistencia */ }
> }
> class ImpresorFactura {
>     String imprimir(Factura f) { /* solo presentación */ return ""; }
> }
> ```
>
> Si cambia el formato de impresión, solo tocas `ImpresorFactura`: no hay riesgo de romper el cálculo del total.

> [!info] 📖 El deck de cátedra: el ejemplo de SRP (04p, pp. 15-17)
> El deck lo plantea como pregunta de examen: *"¿Se viola el principio SRP? ¿Cuántas responsabilidades tiene esta clase?"* — la misma pregunta que el docente hace en el control.
>
> **Se lee así:** El deck enuncia SRP como "a class should have one and only one reason to change, meaning that a class should have only one job", y luego muestra la clase `Employee` con sus cuatro atributos, sus getters y setters y dos métodos de negocio —`isPromotionDueThisYear()` y `calcIncomeTaxForCurrentYear()`— para formular la pregunta de examen. La solución que propone después es mantener `Employee` con la responsabilidad de manejar la información del empleado y usar los servicios de las demás clases.
>
> **Por qué importa:** el deck recorre SRP en tres tiempos (definición, contraejemplo, solución), y el contraejemplo no es una clase "con muchos métodos", sino una clase con dos actores distintos pidiendo cambios.
>
> **Ejemplo:** en el control de ESPOL, frente a `Employee`, la respuesta esperada es "dos responsabilidades: promoción e impuesto", no "tiene getters y setters".

> [!note] 🖼️ captura 04p-p15 — Los 5 Principios, Uno por Uno
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Principios/dsw-04p-p15.png]]
>
> **Se lee así:** La diapositiva muestra una clase `Employee` con `employeeld`, `name`, `address` y `dateOfJoining`, con getters y setters para todos los atributos privados, y dos responsabilidades de negocio: `isPromotionDueThisYear()` (lógica de promoción) y `calcIncomeTaxForCurrentYear()` (lógica de impuesto). Debajo, la pregunta del deck: "¿Se viola el principio SRT? ¿Cuántas responsabilidades tiene esta clase?".
>
> **Por qué importa:** el deck no afirma la violación, la plantea como pregunta de examen: el trabajo del estudiante es contar las responsabilidades, no memorizar la definición.
>
> **Ejemplo:** en el control de ESPOL, frente a esta misma clase, la respuesta esperada es "dos responsabilidades: la promoción y el impuesto", no "tiene getters y setters".

> [!note] 🖼️ captura 04p-p17 — Los 5 Principios, Uno por Uno
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Principios/dsw-04p-p17.png]]
>
> **Se lee así:** La diapositiva "Implementación con SRP" conserva la clase `Employee` con sus datos (`employeeld`, `name`, `address`, `dateOfJoining`), y según el texto del deck esa clase mantiene su responsabilidad de manejar la información del empleado y usa los servicios de las demás clases en lugar de implementar ella misma las otras responsabilidades.
>
> **Por qué importa:** muestra que la solución de SRP no es partir la clase en trozos, sino dejar cada clase con su información y delegar lo demás a servicios ajenos.
>
> **Ejemplo:** en un proyecto de ESPOL, el `Empleado` guarda sus datos y delega el cálculo de sueldo y el guardado en un repositorio, tal como hace la solución del deck.

> [!note] 💡 Solución del deck (p. 17)
>
> **Solución del deck (p. 17):** la clase `Employee` mantiene su responsabilidad de manejar la información del empleado y **usa los servicios de las demás clases**. Es el mismo movimiento que esta nota: la lógica queda en un lado, la persistencia en otro.

### 🔓 O — Open/Closed Principle (OCP)

> [!note] 🔓 OCP — Abierto a extensión, cerrado a modificación
>
> - **Definición:** puedes **agregar** comportamiento nuevo sin **editar** el código que ya funciona (Meyer, 1988).
> - **Mecanismo:** abstracción + polimorfismo (interfaz con varias implementaciones).
> - **Código malo:** `if (tipo.equals("pdf")) ... else if (tipo.equals("html")) ...`: cada variante nueva edita la misma clase.
> - **Código bueno:** `interface Formato { generar(datos); }` + `ReportePdf`, `ReporteHtml`, `ReporteCsv` (variante nueva = archivo nuevo, cero ediciones).
> - **Test de 10 s:** ¿una nueva variante es un archivo nuevo sin tocar lo existente?
> - **Violación típica:** `switch`/`if` en cascada en la lógica de negocio.
> - **Matiz importante:** el sistema nunca queda 100 % cerrado. Eliges **frente a qué tipo de cambio** quieres protegerte (el que ya viste ocurrir o es muy probable) y dejas el resto simple.
>
> [!example]- 💻 Código — OCP con descuentos
>
> ```java
> // ❌ OCP ROTO — cada tipo de cliente nuevo obliga a editar este método
> double aplicar(String tipo, double precio) {
>     if (tipo.equals("ESTUDIANTE")) return precio * 0.80;
>     else if (tipo.equals("JUBILADO")) return precio * 0.70;
>     return precio;
> }
> // ---
> // ✅ OCP — agregar "EMPLEADO" es una clase nueva, sin tocar nada existente
> interface Descuento { double aplicar(double precio); }
> // ---
> class DescuentoEstudiante implements Descuento {
>     public double aplicar(double precio) { return precio * 0.80; }
> }
> class DescuentoJubilado implements Descuento {
>     public double aplicar(double precio) { return precio * 0.70; }
> }
> // ---
> class Caja {
>     double cobrar(double precio, Descuento d) { return d.aplicar(precio); }
> }
> ```
>
> El `if` no desaparece mágicamente: se mueve a **un solo lugar** (por ejemplo una fábrica o la configuración) donde se decide qué `Descuento` usar. La lógica de negocio queda estable.

> [!info] 📖 El deck de cátedra: el ejemplo de OCP (04p, pp. 20-23)
> *"Objects or entities should be open for extension, but closed for modification"*. El deck calcula el área de varias figuras geométricas y pregunta **"¿Se cumple el OCP?"**.
>
> **Se lee así:** El deck construye el ejemplo en dos diapositivas: primero un `AreaCalculator` con un método por forma (`calculateRectangleArea`, `calculateCircleArea`) y la pregunta "¿Se cumple el OCP?"; después la solución, una interfaz `Shape` con `calculateArea()` que `Rectangle` y `Circle` implementan. El cierre del deck lo resume: el código queda abierto para extensión porque muchas más formas pueden agregarse sin modificar el código existente, y queda cerrado para modificación porque `AreaCalculator` ejecuta su función con independencia de las formas que se agreguen.
>
> **Por qué importa:** el ejemplo geométrico del deck es el mismo que la nota usa con descuentos: la clave es que el cliente final (`AreaCalculator`) no cambia, no que desaparezca el `if`.
>
> **Ejemplo:** en un proyecto de ESPOL, el `CalculadoraArea` del deck se traduce tal cual a un módulo de descuentos: agregar un tipo de descuento es una clase nueva, no un método nuevo en el calculador.

> [!note] 🖼️ captura 04p-p21 — Los 5 Principios, Uno por Uno
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Principios/dsw-04p-p21.png]]
>
> **Se lee así:** La diapositiva muestra el diseño que NO cumple OCP: una clase `Circle` con su radio y un `AreaCalculator` con un método por forma (`calculateRectangleArea(Rectangle)` y `calculateCircleArea(Circle)`). La pregunta del deck, en la esquina superior, es "¿Se cumple el OCP?".
>
> **Por qué importa:** el problema es visible en la firma: cada variante nueva obliga a agregar un método al calculador, o sea a editar el código que ya funcionaba.
>
> **Ejemplo:** en un proyecto de ESPOL, un `CalculadoraArea` con un método por figura obligaría a tocarlo cada vez que se agrega un triángulo.

> [!note] 🖼️ captura 04p-p22 — Los 5 Principios, Uno por Uno
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Principios/dsw-04p-p22.png]]
>
> **Se lee así:** La diapositiva "Cumpliendo OCP" muestra la corrección: una interfaz `Shape` con `calculateArea()`, y las clases `Rectangle` (con `length` y `width`) y `Circle` (con `radius`) implementándola. Cada forma conoce su propio cálculo y todas responden al mismo contrato.
>
> **Por qué importa:** el cliente ya no menciona formas concretas: agregar un triángulo es una clase nueva que implementa `Shape`, sin editar ni el calculador ni las formas existentes.
>
> **Ejemplo:** en un proyecto de ESPOL, el módulo de reportes que calcula áreas de piezas queda intacto cuando se incorpora una pieza hexagonal.

> [!note] 💡 El cierre del deck (p. 23)
>
> **El cierre del deck (p. 23):** con el diseño correcto, *"el código queda abierto para extensión pues muchas más formas pueden agregarse sin modificar el código existente y cada forma… "*. Esa frase es el OCP resumido en una línea.

### 🔄 L — Liskov Substitution Principle (LSP)

> [!note] 🔄 LSP — La derivada sustituye a la base sin romper nada
>
> - **Definición:** donde se espera un objeto de la clase base, debe poder usarse uno de la clase derivada **sin que el programa se comporte mal** (Liskov, 1987).
> - **Reglas del contrato:**
>
> | Elemento | Qué puede hacer la subclase | Violación |
> |---|---|---|
> | **Precondiciones** | Pedir lo mismo o **menos** | Exigir **más** que la base |
> | **Postcondiciones** | Prometer lo mismo o **más** | Prometer **menos** que la base |
> | **Invariantes** | Mantenerlas | Romperlas |
> | **Excepciones** | Lanzar las ya previstas | Lanzar excepciones nuevas e inesperadas |
>
> - **Código malo:** `Cuadrado extends Rectangulo` y sobrescribe `setAncho()` cambiando también el alto: rompe lo que `Rectangulo` prometía.
> - **Código bueno:** `Rectangulo` y `Cuadrado` como tipos independientes bajo una interfaz `Figura` con `area()`.
> - **Test de 10 s:** ¿puedes usar la subclase donde va la base y todo sigue en verde?
> - **Violación típica:** `override` que lanza `UnsupportedOperationException`, métodos que hacen `instanceof` para saber con qué subclase tratan.
> - **Idea clave:** que la relación "es un" exista en el mundo real no basta; debe existir en el **comportamiento**.
>
> [!example]- 💻 Código — LSP con Rectángulo y Cuadrado
>
> ```java
> // ❌ LSP ROTO
> class Rectangulo {
>     protected int ancho, alto;
>     void setAncho(int a) { ancho = a; }
>     void setAlto(int h)  { alto = h; }
>     int area()           { return ancho * alto; }
> }
> class Cuadrado extends Rectangulo {
>     @Override void setAncho(int a) { ancho = a; alto = a; }  // cambia también el alto
>     @Override void setAlto(int h)  { ancho = h; alto = h; }
> }
> // ---
> void probar(Rectangulo r) {
>     r.setAncho(5);
>     r.setAlto(4);
>     assert r.area() == 20;   // con Cuadrado da 16 → el cliente "se rompe"
> }
> // ---
> // ✅ LSP — no hay herencia forzada; ambas cumplen un contrato común
> interface Figura { int area(); }
> record Rectangulo(int ancho, int alto) implements Figura {
>     public int area() { return ancho * alto; }
> }
> record Cuadrado(int lado) implements Figura {
>     public int area() { return lado * lado; }
> }
> ```

> [!info] 📖 El deck de cátedra: el ejemplo de LSP (04p, pp. 26-30)
> *"Derived classes must be completely substitutable for their base classes."* El deck usa un pato: `IDuck` con `Swim()`, y `ElectricDuck` que además necesita encenderse.
>
> **Se lee así:** El deck enuncia LSP como "derived classes must be completely substitutable for their base classes" y pone el ejemplo del pato eléctrico: `ElectricDuck.Swim()` solo nada si está encendido, de modo que `MakeDuckSwim(IDuck duck)` puede recibir un pato que no nada. El deck descarta uno de sus dos parches: el `if (duck is ElectricDuck) TurnOn()` en el cliente queda marcado como problema de OCP, mientras que mover el encendido dentro del propio `Swim()` mantiene el contrato y deja al cliente igual.
>
> **Por qué importa:** muestra que LSP y OCP se vigilan mutuamente: el parche que arregla la sustitución en el cliente rompe la extensión, y solo se resuelve dentro de la implementación.
>
> **Ejemplo:** en un proyecto de ESPOL, una `Ventana` que solo se abre si hay sesión activa debería resolverlo por dentro, igual que hace `ElectricDuck`, y no con un `instanceof` en cada vista.

> [!note] 🖼️ captura 04p-p26 — Los 5 Principios, Uno por Uno
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Principios/dsw-04p-p26.png]]
>
> **Se lee así:** La diapositiva muestra el código del contraejemplo: `interface IDuck { void Swim(); }`, `class Duck implements IDuck` que nada, y `class ElectricDuck implements IDuck` cuyo `Swim()` hace `if (!IsTurnedOn) return;` y solo nada si está encendido. Es la interfaz la que promete "nadar", pero una implementación puede no hacerlo.
>
> **Por qué importa:** el problema no está en `ElectricDuck`, está en la promesa de `IDuck`: el cliente que recibe un `IDuck` no tiene forma de saber que le puede tocar un pato apagado.
>
> **Ejemplo:** en un proyecto de ESPOL, una interfaz `Impresora` con `imprimir()` y una implementación `ImpresoraApagada` que no imprime es la misma mentira de contrato.

> [!note] 💡 El problema que el deck plantea (p. 27)
>
> **El problema que el deck plantea (p. 27):** `void MakeDuckSwim(IDuck duck) { duck.Swim(); }` — *"se viola LSP, porque una clase derivada puede lanzar una excepción que la clase base no contemplaba"*. Es el mismo error que esta nota señala con `Cuadrado extends Rectangulo`.
>
> **Los dos intentos de solución del deck (pp. 28-30):** (1) hacer `if (duck is ElectricDuck) ((ElectricDuck)duck).TurnOn();` antes de nadar — el `instanceof` que esta nota marca como olor; (2) mover la lógica al `Swim()` de `ElectricDuck` (`if (!IsTurnedOn) TurnOnDuck();`) — el workaround que el deck prefiere.

### ✂️ I — Interface Segregation Principle (ISP)

> [!note] ✂️ ISP — Interfaces pequeñas por rol
>
> - **Definición:** ningún cliente debería depender de métodos que no usa.
> - **Equivalente en la unidad:** bajo acoplamiento aplicado a interfaces.
> - **Código malo:** `ISistema` con 25 métodos; las clases implementan `throw new UnsupportedOperationException()` en 20 de ellos.
> - **Código bueno:** `IPagos`, `IEnvios`, `IReportes` (3-5 métodos cohesivos por rol).
> - **Test de 10 s:** ¿algún cliente implementa métodos vacíos? Divide la interfaz.
> - **Violación típica:** la "interfaz única para todo el sistema" o interfaces que crecen cada vez que alguien necesita "un método más".
> - **Beneficio:** cambiar un método que no te importa deja de obligarte a recompilar y retestear.
>
> [!example]- 💻 Código — ISP con trabajadores y robots
>
> ```java
> // ❌ ISP ROTO — Robot no come ni duerme
> interface Trabajador {
>     void trabajar();
>     void comer();
>     void dormir();
> }
> class Robot implements Trabajador {
>     public void trabajar() { /* ok */ }
>     public void comer()    { throw new UnsupportedOperationException(); }
>     public void dormir()   { throw new UnsupportedOperationException(); }
> }
> // ---
> // ✅ ISP — cada rol, su interfaz; cada clase implementa solo lo que le aplica
> interface Trabajable { void trabajar(); }
> interface Alimentable { void comer(); }
> interface Descansable { void dormir(); }
> // ---
> class Humano implements Trabajable, Alimentable, Descansable { /* los tres */ }
> class Robot  implements Trabajable { /* solo trabaja */ }
> ```

> [!info] 📖 El deck de cátedra: el ejemplo de ISP (04p, pp. 32-37)
> *"Make fine-grained interfaces with specific methods. Clients should not be forced to depend upon interfaces that they don't use."* El deck parte de una interfaz `Messenger` que muestra una variedad de mensajes.
>
> **Se lee así:** El deck enuncia ISP como "make fine-grained interfaces with specific methods; clients should not be forced to depend upon interfaces that they don't use" y lo lleva hasta el extremo con la pregunta "¿Problema?" sobre una interfaz con Volar, Correr, Nadar, Comer, Cantar, Graznar, Planear, Caminar, Hablar y Poner huevo. La solución que propone es segmentar: la interfaz `Messenger` del cajero automático se divide en interfaces por cliente, y para la App de depósitos se usa solo una interfaz con los métodos que sí va a utilizar.
>
> **Por qué importa:** el caso del cajero muestra el patrón completo de ISP: el problema aparece cuando un cliente nuevo (la App de depósitos) tiene que depender de una interfaz que le sobra, y se resuelve separando por cliente, no por método suelto.
>
> **Ejemplo:** en un proyecto de ESPOL, si el cliente de consola implementa una interfaz de mensajes con diez métodos, está pagando el costo de ISP roto que el deck señala con "¿Problema?".

> [!note] 🖼️ captura 04p-p33 — Los 5 Principios, Uno por Uno
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Principios/dsw-04p-p33.png]]
>
> **Se lee así:** La diapositiva plantea el caso: existe una interfaz `Messenger` que permite mostrar una variedad de mensajes cuando un usuario interactúa con un cajero automático, con métodos como `askForCard`, `tellInvalidCard`, `askForPin`, `tellInvalidPin`, `askForAccount`, `tellNotEnoughMoneyInAccount`, `tellAmountDeposited` y `tellBalance`. Se quiere crear una App que muestre mensajes cuando se efectúe un Depósito, y la diapositiva pregunta "¿Problema?".
>
> **Por qué importa:** la App de depósitos solo necesita `tellAmountDeposited` y `tellBalance`, pero al depender de `Messenger` queda atada a la tarjeta, al PIN y a los retiros.
>
> **Ejemplo:** en un proyecto de ESPOL, un módulo de notificaciones que declara diez métodos obliga al cliente de consola a implementar los que no usa.

> [!note] 🖼️ captura 04p-p34 — Los 5 Principios, Uno por Uno
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Principios/dsw-04p-p34.png]]
>
> **Se lee así:** La diapositiva propone la solución: "Dividamos la interfaz, así una clase no es forzada a implementar lo que no necesita". El código divide `Messenger` en `LoginMessenger` (con `askForCard`, `tellInvalidCard`, `askForPin`, `tellInvalidPin`) y `WithdrawalMessenger` (con `tellNotEnoughMoneyInAccount` y `askForFeeConfirmation`), y una clase `EnglishMessenger` implementa ambas.
>
> **Por qué importa:** la clave no es solo partir la interfaz, es partirla *por cliente*: cada interfaz reúne lo que un tipo de usuario realmente usa.
>
> **Ejemplo:** en un proyecto de ESPOL, un cajero de depósitos implementa solo la interfaz de mensajes de depósito y no necesita los de retiro.

> [!note] 💡 La pregunta provocadora del deck (p. 36)
>
> **La pregunta provocadora del deck (p. 36):** una interfaz con Volar · Correr · Nadar · Comer · Cantar · Graznar · Planear · Caminar · Hablar · Poner huevo — **"¿Problema?"**. Si tienes que implementar diez comportamientos para ser un "Worker", el problema es la interfaz, no la clase.

### 🔗 D — Dependency Inversion Principle (DIP)

> [!note] 🔗 DIP — Depende de abstracciones, no de concreciones
>
> - **Definición:** los módulos de alto nivel (reglas de negocio) **no dependen** de los de bajo nivel (BD, correo, pagos); **ambos dependen de abstracciones**. Además, la abstracción pertenece al módulo de alto nivel, no al de bajo.
> - **Equivalente en la unidad:** bajo acoplamiento + abstracción.
> - **Código malo:** `PedidoService` hace `new PagoConTarjeta()` directamente.
> - **Código bueno:** `PedidoService` depende de la interfaz `Pago`, que recibe por constructor (o fábrica).
> - **Test de 10 s:** ¿los constructores reciben interfaces?
> - **Violación típica:** `new Concreto()` regado por el código: impide probar con mocks y cambiar de proveedor implica reescribir.
> - **No confundir:** **DIP** es el principio (la dirección de las dependencias). **Inyección de dependencias (DI)** es una *técnica* para cumplirlo (Spring, constructores). Se puede cumplir DIP sin ningún framework.

> [!note] 🗺️ Diagrama — Los 5 Principios, Uno por Uno
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u1-05-02-graph.svg]]
>
> **Se lee así:** El diagrama tiene dos subgráficas. En "Sin DIP", `PedidoService (alto nivel)` apunta directo a `PagoConTarjeta (bajo nivel)`: la dependencia va del negocio hacia lo concreto. En "Con DIP", `PedidoService (alto nivel)` apunta a `interface Pago`, y tanto `PagoConTarjeta` como `PagoPayPal` apuntan a esa misma interfaz con la etiqueta "implementa".
>
> **Por qué importa:** la diferencia entre las dos subgráficas es la dirección de la flecha: en la versión correcta las dependencias apuntan a la abstracción, que pertenece al módulo de alto nivel.
>
> **Ejemplo:** en un proyecto de ESPOL, `PedidoService` recibe un `Pago` por constructor: cambiar de tarjeta a PayPal es cambiar la implementación, no el servicio.

> [!info] 📖 El deck de cátedra: el ejemplo de DIP (04p, pp. 39-43)
> *"Depend on abstractions, not on concretions. High-level modules should not depend on low-level modules. Both should depend on abstractions."*
>
> **Se lee así:** El deck enuncia DIP y de inmediato propone tomar ventaja de las interfaces; después muestra el incumplimiento con la clase `House` que instancia `new Door()` y `new Window()` en su propio constructor, y el cumplimiento con un `House` que recibe `IDoor` e `IWindow` por constructor. El par del deck es un antes y un después sobre la misma clase: lo único que cambia es de dónde vienen las piezas.
>
> **Por qué importa:** el ejemplo del deck muestra que DIP no exige una abstracción previa ni un framework: basta con que la clase de alto nivel reciba sus dependencias desde afuera.
>
> **Ejemplo:** en un proyecto de ESPOL, el `ServicioPedido` de la nota es el `House` del deck: con `Pago` recibido por constructor, la prueba puede inyectar un `PagoFalso` sin tarjetas reales ni red.

> [!note] 🖼️ captura 04p-p40 — Los 5 Principios, Uno por Uno
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Principios/dsw-04p-p40.png]]
>
> **Se lee así:** La diapositiva "Incumpliendo DIP" muestra la clase `House` con los campos `private Door _door` y `private Window _window`, y un constructor que hace `_door = new Door();` y `_window = new Window();`. La casa es el módulo de alto nivel y decide, ella misma, qué piezas concretas usar.
>
> **Por qué importa:** el problema es que la creación de los detalles quedó dentro de la clase de alto nivel: no hay forma de entregarle otra puerta sin reescribirla.
>
> **Ejemplo:** en un proyecto de ESPOL, un `ServicioPedido` que hace `new PagoConTarjeta()` en su constructor tiene exactamente esta forma, y por eso no se puede probar con un pago falso.

> [!note] 🖼️ captura 04p-p43 — Los 5 Principios, Uno por Uno
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Principios/dsw-04p-p43.png]]
>
> **Se lee así:** La diapositiva cierra el deck con el título "SOLID" y una sola frase: "Software Development is not a Jenga game". No hay código ni texto adicional: es la frase con la que el docente resume todo el bloque.
>
> **Por qué importa:** la metáfora encaja con lo que mostró el deck: en Jenga cada pieza sostiene a las de arriba, así que quitar una obliga a rehacer las demás; un diseño con SOLID busca que cada cambio se quede en su pieza.
>
> **Ejemplo:** en un proyecto de ESPOL, esa es la razón para partir la clase `GestorTodo` antes de que una modificación obligue a mover veinte archivos.

> [!note] 💡 El par del deck (pp. 40-41)
>
> **El par del deck (pp. 40-41):** `House` que instancia `new Door()` y `new Window()` (DIP incumplido) frente a `House` que recibe `IDoor` e `IWindow` por constructor (DIP cumplido). Es literalmente el patrón de inyección por constructor que se muestra más abajo en esta nota.

> [!example]- 💻 Código — DIP con inyección por constructor y prueba con un falso
>
> ```java
> // ❌ DIP ROTO — PedidoService conoce y crea la clase concreta
> class PedidoService {
>     private final PagoConTarjeta pago = new PagoConTarjeta();
>     void confirmar(Pedido p) { pago.cobrar(p.total()); }
> }
> // ---
> // ✅ DIP — depende de la abstracción, que recibe desde afuera
> interface Pago { void cobrar(double monto); }
> // ---
> class PedidoService {
>     private final Pago pago;
>     PedidoService(Pago pago) { this.pago = pago; }
>     void confirmar(Pedido p) { pago.cobrar(p.total()); }
> }
> // ---
> // 🧪 En una prueba unitaria, sustituyes el pago real por un falso
> class PagoFalso implements Pago {
>     double ultimoMonto;
>     public void cobrar(double monto) { ultimoMonto = monto; }
> }
> // new PedidoService(new PagoFalso()).confirmar(pedido); → sin tarjetas reales ni red
> ```

---

## 🎨 SRP + OCP: Los que Más Evalúan

> [!note] 🎨 Código Integrado y Chequeos de 10 Segundos
>
> ```java
> // ❌ SRP+OCP rotos: una clase, tres misiones, if por variante
> class Reporte {
>     String generar(String tipo) {
>         if (tipo.equals("pdf")) { /* ... */ }
>         else { /* ... */ }
>     }
>     void guardarEnDisco() { /* ... */ }
>     void enviarPorMail()  { /* ... */ }
> }
> // ---
> // ✅ SRP+OCP: misiones separadas, variante = clase nueva
> interface Formato { String generar(Datos d); }
> class ReportePdf implements Formato {
>     public String generar(Datos d) { /* ... */ return ""; }
> }
> class ServicioReporte {
>     String emitir(Datos d, Formato f) { return f.generar(d); }
> }
> ```
>
> | Principio | Chequeo de 10 segundos |
> |---|---|
> | **SRP** | Describe la clase sin usar "y" |
> | **OCP** | Nueva variante = archivo nuevo, cero ediciones |
> | **LSP** | Prueba la derivada donde va la base: ¿todo sigue verde? |
> | **ISP** | ¿Algún cliente implementa métodos vacíos? Divide |
> | **DIP** | ¿Los constructores reciben interfaces? Bien |

---

## 🧭 Cómo se Refuerzan Entre Sí

> [!tip] 🔄 Los Cinco no Son Independientes
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u1-05-03-graph.svg]]
>
> **Se lee así:** El diagrama coloca a OCP en el centro y muestra las flechas que llegan a él: desde SRP ("clases enfocadas"), desde ISP ("interfaces justas"), desde DIP ("depender de abstracciones") y desde LSP ("implementaciones confiables"). Además hay una flecha de LSP a DIP, porque LSP es lo que garantiza que la abstracción de DIP no mienta.
>
> **Por qué importa:** da el orden de ataque que usa la nota: SRP primero (piezas pequeñas), luego DIP e ISP (cómo se conectan) y LSP (que el intercambio sea real); OCP es el resultado.
>
> **Ejemplo:** en un proyecto de ESPOL, un módulo con una clase por responsabilidad y constructores que reciben interfaces ya tiene camino a OCP; si además las derivadas respetan el contrato, el sistema crece sin editar lo existente.
>
> - **OCP es el objetivo**: un sistema que crece agregando código, no editándolo.
> - **SRP** da las piezas pequeñas; **DIP** y **ISP** definen cómo se conectan; **LSP** garantiza que cualquier pieza intercambiable de verdad lo sea.
> - Sin LSP, la abstracción de OCP/DIP miente: la interfaz dice una cosa y la implementación hace otra.

---

## 🗺️ Diagrama de Decisión: ¿Qué Principio Estoy Violando?

> [!note] 🗺️ Diagrama — ️ Diagrama de Decisión: ¿Qué Principio Estoy Violando
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u1-05-04-flow.svg]]
>
> **Se lee así:** Es un embudo de cuatro preguntas que van descartando un principio a la vez. Primero "¿Cambia por más de una razón o actor?": si es "Sí", es SRP y se divide por responsabilidad. Si es "No", "¿Agregar una variante obliga a editar if/switch?": si es "Sí", es OCP y se extrae una interfaz con una clase por variante. Si tampoco, "¿Una subclase no puede usarse donde va la base?": si es "Sí", es LSP y se revisa el contrato o se evita la herencia. Y si tampoco, "¿Hay métodos vacíos o UnsupportedOperation?": si es "Sí", es ISP y se divide la interfaz por rol; si es "No", "¿Hay new Concreta() en la lógica de negocio?": si es "Sí", es DIP y se recibe interfaz por constructor; si es "No", el diseño está sano.
>
> **Por qué importa:** es el diagnóstico en cascada que la nota propone: cada pregunta descarta una causa antes de pasar a la siguiente, así que no se "arreglan" cinco problemas a la vez.
>
> **Ejemplo:** en el `Main.java` de nómina que la nota usa como caso integrador, la primera pregunta ya salta a SRP, mientras que un `new MySql()` dentro de `ServicePerson` cae en la última rama, DIP.

> [!note] 👃 Olores de Código → Principio
>
> | Olor | Principio probable | Arreglo típico |
> |---|---|---|
> | Clase de 800 líneas, nombre `Manager` | SRP | Dividir por responsabilidad |
> | `switch` o `if/else` sobre un tipo | OCP | Polimorfismo / Strategy |
> | `instanceof` o *casts* frecuentes | LSP | Revisar jerarquía o usar composición |
> | `UnsupportedOperationException` en `override` | LSP / ISP | Dividir interfaz o no heredar |
> | Interfaz de 20+ métodos | ISP | Segregar por rol |
> | `new` de clases concretas en servicios | DIP | Inyectar interfaces |
> | Pruebas que requieren BD o red reales | DIP | Abstraer y usar falsos |
> | Un cambio pequeño rompe 5 clases | SRP / OCP / DIP | Revisar fronteras y dependencias |

---

## 📖 Casos del Libro (lectura Control02: págs. 57–59 + resto)

> [!quote] 📖 R. C. Martin, *Clean Architecture*, Parte III (págs. impresas 57–59 y caps. 7–11)
>
> - **Tesis de la Parte III:** los ladrillos bien hechos no bastan — con buenos ladrillos también se construye un desastre. SOLID ordena funciones y datos en clases; su meta son estructuras de nivel medio que **toleren el cambio, sean fáciles de entender y sirvan de base a componentes reutilizables**. Historia: Martin los reunió desde fines de los 80 (debates en USENET); hacia 2004 Michael Feathers propuso reordenarlos para formar el acrónimo **SOLID**.
> - **SRP, corolario de Conway:** la mejor estructura refleja la organización social — cada módulo, una sola razón para cambiar = **un solo actor**. No significa "una función por clase": significa separar el código del que dependen actores distintos.
>
> **Se lee así:** La Parte III de *Clean Architecture* es la lectura que pide el Control 02 y es la que da el marco: los principios no se aplican uno por uno, se leen como un argumento sobre la estructura de nivel medio. El texto de la nota traduce la tesis central —estructuras que toleren el cambio, sean fáciles de entender y sirvan de base a componentes reutilizables— y el corolario de Conway, que un módulo responde a un solo actor, que es la formulación final del SRP.
>
> **Por qué importa:** fija la vara de la lectura: el objetivo no es tener clases "bonitas", sino estructuras que aguanten el cambio; sin ese marco, los cinco principios se leen como una lista de reglas sueltas.
>
> **Ejemplo:** en el proyecto de ESPOL, el `Employee` de nómina sirve como ejemplo de SRP en versión final: cálculo de sueldo, reporte de horas y guardado responden a tres actores (CFO, COO y CTO), y por eso hay que separarlos.

### 🧪 Los 6 casos que el control puede citar

> [!example] 💡 Employee, Merges y Facade (SRP, cap. 7)
>
> - **Employee (nómina):** `calculatePay()` (contabilidad→CFO), `reportHours()` (RRHH→COO), `save()` (DBA→CTO) en una sola clase = 3 actores acoplados.
> - **Síntoma 1, duplicación accidental:** `calculatePay` y `reportHours` comparten `regularHours()`; el CFO pide un ajuste, el desarrollador lo cambia sin ver el otro uso y RRHH reporta cifras malas por millones.
> - **Síntoma 2, merges:** DBA y RRHH modifican la misma clase a la vez → colisión y riesgo para CTO y COO.
> - **Soluciones:** separar datos (`EmployeeData` sin métodos) de funciones en 3 clases que no se conocen; o **Facade** (`EmployeeFacade` que instancia y delega); o conservar el método clave en `Employee` y usarla como fachada.
> - **Proyección:** SRP reaparece como Principio de Cierre Común (componentes) y como Eje de Cambio (fronteras arquitectónicas).
>
> [!example] 💡 Reporte financiero web→impresora (OCP, cap. 8)
>
> - **Experimento mental:** resumen financiero en web (rojo = negativos) que ahora debe salir en impresora B/N paginada (paréntesis = negativos). Buena arquitectura: **cero líneas viejas modificadas**.
> - **Cómo:** SRP separa cálculo de presentación; DIP organiza dependencias en una dirección: si el componente A debe protegerse de cambios en B, **B depende de A**. El **Interactor** (reglas de negocio, máximo nivel) queda protegido de Base de Datos, Controlador, Presentadores y Vistas.
> - **Conclusión OCP:** particionar en componentes y ordenarlos en jerarquía que proteja lo de alto nivel. Ojo con dependencias transitivas (violan el "no dependas de lo que no usas": anticipo del ISP).
>
> [!example] 💡 License/Billing, Square y taxis Acme (LSP, cap. 9)
>
> - **Caso bueno:** `License.calcFee()` usada por `Billing` con `PersonalLicense` y `BusinessLicense` intercambiables: la app no depende de cuál subtipo recibe.
> - **Square/Rectangle (violación canónica):** `Square` no es subtipo válido de `Rectangle` porque alto y ancho mutan juntos; `r.setW(5); r.setH(2); assert(area==10)` falla si `r` es un cuadrado. Defenderse con `if` en el cliente = prueba de que no son sustituibles.
> - **Taxis Acme (LSP arquitectónico):** todas las compañías deben respetar el mismo REST (`destination`); Acme manda `dest` y el sistema se contamina con `if (uri.startsWith("acme.com"))` + tabla de configuración por URI. Moraleja: una violación de sustituibilidad ensucia la arquitectura con mecanismos extra.
>
> [!example] 💡 OPS/User1-3 y framework con base de datos (ISP, cap. 10)
>
> - **Caso base:** `User1` solo usa `op1` de `OPS`, pero en Java su código depende también de `op2`/`op3` → un cambio ajeno lo obliga a recompilar y redesplegar. Remedio: segregar en interfaces (`U1Ops`...).
> - **Lenguajes dinámicos (Ruby, Python):** sin declaraciones `import`, no hay dependencia de código fuente que fuerce recompilación — por eso acoplan menos. Pero ISP sigue valiendo a nivel arquitectura.
> - **Caso arquitectónico:** sistema S incluye framework F atado a base de datos D con funciones que nadie usa; un cambio o una falla en lo no usado tumba F y S. Lección: depender de algo con lastre innecesario trae problemas inesperados (puente con el Principio de Reutilización Común, cap. 13).
>
> [!example] 💡 String estable, 4 prácticas y la línea curva (DIP, cap. 11)
>
> - **Matiz clave:** no toda dependencia concreta es mala. `String` es concreta pero estable y controlada: se tolera. El enemigo es lo concreto **volátil** (lo que desarrollas y cambia siempre).
> - **Interfaces menos volátiles:** cambiar una interfaz rompe implementaciones; cambiar implementaciones rara vez rompe interfaces. Diseñar = agregar funcionalidad sin tocar interfaces.
> - **4 prácticas:** no referirse a clases concretas volátiles (usa interfaces); no derivar de ellas (la herencia es la relación más rígida); no sobrescribir funciones concretas (hazlas abstractas con múltiples implementaciones); no mencionar nada concreto y volátil.
> - **Abstract Factory:** `Application` usa `ConcreteImpl` vía interfaz `Service`, pero la crea vía `ServiceFactory` (interfaz) implementada por `ServiceFactoryImpl`. La **línea curva** separa lo abstracto de lo concreto: las dependencias de código la cruzan hacia lo abstracto, mientras el control fluye al revés — de ahí el nombre *inversión*.
> - **Componente concreto (`main`):** las violaciones DIP no se eliminan, se concentran en pocos componentes separados del resto. La línea curva anticipa las fronteras arquitectónicas y la **Regla de Dependencia** de los capítulos siguientes.

### 🧪 Caso integrador Main.java (práctica Control02)

> [!example] 💡 Nómina ds2026 — las 5 violaciones en un solo archivo ([[../Unidad 0 - Guias y Ejercicios/Material de clase/Main.java]])
>
> - **SRP:** `Employee` calcula bono + genera PDF + manda email (3 razones para cambiar).
> - **OCP:** `BonusReport.describe()` decide con cadena `instanceof` — cada tipo nuevo obliga a modificarlo.
> - **LSP:** `TemporaryEmployee.calculateBonus()` y `manage()` lanzan `UnsupportedOperationException` — no sustituye a `Employee`.
> - **ISP:** `EmployeeTasks` obliga `manage()` a quien no gerencia (los temporales la heredan rota).
> - **DIP:** `ServicePerson` hace `new MySql()` adentro — depende de lo concreto volátil.
>
> > [!success]- ✅ Prueba en vivo (compilado y ejecutado con `javac`/`java`)
> >
> > `Payroll.totalBonus()` itera `List<Employee>` y revienta con Luis: `Exception in thread "main" java.lang.UnsupportedOperationException: Temp earns no bonus at ds2026.TemporaryEmployee.calculateBonus(Main.java:62)`. El programa compila perfecto y muere en ejecución — esa es exactamente la firma de una violación LSP: el subtipo no aguanta el contrato del padre.
> >
> > Arreglos en 1 línea cada uno: bonus polimórfico sin excepción (LSP) · interfaces `Workable`/`Manageable` separadas (ISP) · `BonusReport` por polimorfismo, no `instanceof` (OCP) · `EmployeeRepository` inyectado en `ServicePerson` (DIP) · `PayslipService` y `EmailService` fuera de `Employee` (SRP).

### 🧪 Casos de las slides Semana 4 (Jurado/Mera — los que el docente proyectó)

> [!example] 💡 Bad Coding, áreas, pato, Messenger y House
>
> - **Bad Coding (por qué existe SOLID):** **rigidez** (un cambio afecta muchas partes), **fragilidad** (fallos donde no debería), **inmovilidad** (código irreusable fuera de su contexto).
> - **OCP, áreas:** `calculateArea()` por forma + `AreaCalculator` que ejecuta sin conocer las formas — agregar un triángulo no toca código existente (abierto a extensión, cerrado a modificación).
> - **LSP, pato eléctrico:** `ElectricDuck.Swim()` apagado no nada (o lanza excepción que la base no) → viola LSP. Parche con `if (duck is ElectricDuck) ...TurnOn()` → viola OCP (cada pato nuevo toca el cliente). Solución: que `Swim()` auto-encienda (`TurnOnDuck()` adentro) y cumpla el contrato siempre.
> - **ISP, Messenger/cajero + habilidades del pato:** interfaz `Messenger` con todo lo mostrable obliga a la App de depósitos a depender de lo que no usa → segregar por cliente. La lista (volar, correr, nadar, comer, cantar, graznar, planear, caminar, hablar, poner huevo) es el test: ningún cliente necesita las 10.
> - **DIP, House:** `House` con `new Door()` + `new Window()` adentro (incumple: depende de lo concreto volátil) vs `House(IDoor, IWindow)` inyectadas (cumple: depende de abstracciones).
> - **Auto-test (Puntos para recordar de las slides):** ¿características del código limpio? · ¿qué es SOLID? · ¿objetivo de cada principio? · ¿un ejemplo por principio? · ¿cuántas capas tiene MVC y qué hace cada una?
>
> 📎 Slides: `04PrincipiosDiseñoAplicadosDesarrollo_MVC-1.pdf` (Unidad 0). Lecturas que dejan: Martin *Clean Architecture* caps. 7–11, Pressman & Maxim cap. 17 (WebApp), Martin *Clean Code* cap. 1.

---

## ⚠️ Problemas Comunes y Soluciones

> [!danger] ❌ Error 1: SOLID como Decoración
>
> **Síntomas:** nombras los principios en el informe, pero el código tiene "Managers dioses" y `new` por doquier.
>
> ```java
> // ❌ EL ERROR ESTÁ AQUÍ: SOLID solo existe en el informe, no en el código
> class GestorTodo { // SRP roto: matricula + cobra + reporta
>     void matricular() { /* ... */ }
>     void cobrar() { /* ... */ }
>     void generarReporte() { /* ... */ }
> }
> class ServicioPago {
>     private final PagoConTarjeta pago = new PagoConTarjeta(); // DIP roto
> }
> ```
>
> **Solución:**
>
> - 1 principio por semana de práctica: SRP esta semana en tu proyecto.
> - El *code review* pregunta "¿qué principio protege este cambio?".
>
> [!danger] ❌ Error 2: Sobreingeniería, interfaz para todo (viola **simplicidad/YAGNI**)
>
> **Síntomas:** una interfaz con una única implementación "por si acaso":
>
> ```java
> // ❌ EL ERROR ESTÁ AQUÍ: abstracción sin segunda variante que la justifique
> interface Sumador { int sumar(int a, int b); }
> class SumadorUnico implements Sumador {
>     public int sumar(int a, int b) { return a + b; }
> }
> ```
>
> **Solución:** aplica el principio cuando hay **evidencia de variación** (ya cambió o cambiará seguro). Regla práctica: abstrae a la segunda variante, no a la primera.
>
> [!danger] ❌ Error 3: Interpretar SRP como "un método por clase" (viola **SRP real: razones de cambio**)
>
> **Síntomas:** cientos de clases diminutas donde seguir un flujo exige abrir 10 archivos:
>
> ```java
> // ❌ EL ERROR ESTÁ AQUÍ: partir por métodos, no por razones de cambio
> class ValidadorNombre { boolean ok(String n) { /* ... */ return true; } }
> class ValidadorEdad { boolean ok(int e) { /* ... */ return true; } }
> class ValidadorCorreo { boolean ok(String c) { /* ... */ return true; } }
> // ...todo cambia junto cuando cambia "qué es un usuario válido"
> ```
>
> **Solución:** SRP se mide por **razones de cambio**, no por número de métodos. Una clase con 10 métodos cohesivos que cambian juntos cumple SRP.
>
> [!danger] ❌ Error 4: Herencia solo para reutilizar código (viola **LSP**)
>
> **Síntomas:** la subclase hereda métodos que no tienen sentido para ella:
>
> ```java
> // ❌ EL ERROR ESTÁ AQUÍ: Pila NO ES un ArrayList (expone get(i), remove(i)...)
> class Pila extends ArrayList<String> {
>     void push(String s) { add(s); }
> }
> ```
>
> **Solución:** prefiere **composición** sobre herencia. Si no puedes decir "toda `B` se comporta como una `A` en todos los contextos", no heredes (LSP).
>
> [!danger] ❌ Error 5: DIP sin dueño de la abstracción (viola **DIP**)
>
> **Síntomas:** la interfaz vive en el paquete de la BD y el negocio sigue atado a infraestructura:
>
> ```java
> // ❌ EL ERROR ESTÁ AQUÍ: el negocio importa al paquete de la BD
> package bd;
> interface Repositorio { void guardar(Pedido p); } // vive en infraestructura
> package negocio;
> import bd.Repositorio; // el negocio depende de la BD
> class ServicioPedido {
>     ServicioPedido(Repositorio r) { /* ... */ }
> }
> ```
>
> **Solución:** la interfaz pertenece al **módulo de alto nivel** (lo que necesita el negocio); la implementación concreta vive en la capa de infraestructura.

---

## 🎯 Mejores Prácticas

> [!tip] 🏆 Checklist
>
> **1. SRP primero, el resto después** — Sin una misión por clase, OCP/LSP no tienen dónde apoyarse.
>
> **2. DIP en constructores desde el día 1** — Recibe interfaces: tus pruebas con mocks (Unidad 5) te lo agradecerán.
>
> **3. OCP donde ya viste variación** — No predigas el futuro entero; protégete de los cambios probables.
>
> **4. Revisa LSP con pruebas del contrato** — La misma batería de pruebas debe pasar para la base y para cada derivada.
>
> **5. Divide interfaces cuando duela** — Si dos clientes usan partes distintas de una interfaz, sepárala.
>
> **6. Usa los principios como preguntas de revisión** — "¿Qué actor cambia esto? ¿Qué pasa si agrego otra variante? ¿Esta subclase es sustituible?"

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Nivel 1 — Básico
>
> **1.** Escribe el nombre completo y la idea central de cada letra de SOLID.
>
> **2.** Una clase `Usuario` valida contraseñas, guarda en BD y envía correos de bienvenida. ¿Qué principio viola y cómo la dividirías?
>
> **3.** Un método tiene `if (tipo == "A") ... else if (tipo == "B") ...` y cada mes se agrega un tipo. ¿Qué principio se viola?
>
> **4.** ¿Qué indica que una clase implemente `throw new UnsupportedOperationException()` en varios métodos?
>
> **5.** ¿Qué significa que `PedidoService` haga `new PagoConTarjeta()` en su constructor? ¿Qué principio rompe?
>
> > [!success]- ✅ Respuestas — Nivel 1
> >
> > - **1.** SRP (una razón para cambiar), OCP (abierto a extensión, cerrado a modificación), LSP (la derivada sustituye a la base), ISP (interfaces pequeñas por rol), DIP (depender de abstracciones).
> > - **2.** SRP (tres razones de cambio). Dividir en `ValidadorContraseña`, `RepositorioUsuario` y `NotificadorBienvenida`.
> > - **3.** OCP: cada tipo nuevo obliga a editar el método. Solución: interfaz + una clase por tipo.
> > - **4.** Violación de ISP (la interfaz es demasiado grande) o de LSP (la subclase no cumple lo que prometía la base).
> > - **5.** Viola DIP: depende de una clase concreta. Debe recibir una interfaz `Pago` por constructor.
>
> [!example] 📋 Nivel 2 — Intermedio
>
> **6.** Explica por qué `Cuadrado extends Rectangulo` viola LSP aunque "un cuadrado es un rectángulo" en geometría.
>
> **7.** Refactoriza en prosa una interfaz `IEmpleado` con `calcularSalario()`, `programarReunion()`, `generarReporteMedico()` y `manejarVehiculo()` para cumplir ISP.
>
> **8.** ¿Qué diferencia hay entre DIP e inyección de dependencias?
>
> **9.** Da un ejemplo propio donde un `override` fortalezca una precondición y explica por qué rompe LSP.
>
> **10.** Un compañero dice: "mi clase cumple SRP porque solo tiene un método de 300 líneas". ¿Qué le respondes?
>
> **10b.** En el caso Employee del libro: el equipo del CFO pide ajustar `regularHours()` y el desarrollador lo cambia sin notar que `reportHours()` también la usa. ¿Qué síntoma de violación SRP es y qué actores salen afectados?
>
> **10c.** Martin dice que depender de `String` (concreta) se tolera. ¿Por qué, y qué criterio distingue una dependencia concreta tolerable de una prohibida?
>
> > [!success]- ✅ Respuestas — Nivel 2
> >
> > - **6.** En geometría los cuadrados son rectángulos inmutables; en código, `Rectangulo` promete que alto y ancho se modifican por separado. `Cuadrado` rompe esa promesa, así que un cliente que usa `Rectangulo` falla al recibir un `Cuadrado`.
> > - **7.** Separar por rol: `Pagable` (`calcularSalario`), `Convocable` (`programarReunion`), `ConHistorialMedico` (`generarReporteMedico`), `Conductor` (`manejarVehiculo`). Cada clase implementa solo los roles que le aplican.
> > - **8.** DIP es el principio de diseño (el negocio depende de abstracciones). DI es una técnica (pasar las dependencias desde afuera) que ayuda a cumplirlo.
> > - **9.** Ej.: la base `Descuento.aplicar(precio)` acepta cualquier precio ≥ 0; una derivada lanza excepción si el precio < 100. Un cliente que le pasaba 50 ahora falla: exige más que la base.
> > - **10.** Un solo método no garantiza una sola responsabilidad. El método de 300 líneas casi seguro mezcla varias tareas (viola cohesión y SRP); se debe dividir por responsabilidad.
> > - **10b.** Síntoma 1: duplicación accidental. El cambio pedido por el CFO (contabilidad) corrompe silenciosamente los reportes de la COO (RRHH): código de actores distintos en proximidad, acoplados por algoritmo compartido.
> > - **10c.** Porque `String` es estable: cambia rara vez y bajo control estricto, así que nadie teme sus cambios. Criterio: se tolera lo concreto **estable** (plataforma, SO); se evita lo concreto **volátil** (módulos en desarrollo activo con cambios frecuentes).
>
> [!example] 📋 Nivel 3 — Avanzado
>
> **11.** Argumenta por qué OCP depende de que se cumplan SRP, LSP y DIP.
>
> **12.** Diseña (en prosa) un módulo de notificaciones (correo, SMS, push) que cumpla OCP y DIP.
>
> **13.** Da un caso en que aplicar OCP de forma excesiva empeora el diseño.
>
> **14.** Explica cómo DIP facilita las pruebas unitarias con un ejemplo propio.
>
> **15.** Un sistema tiene `Ave` con `volar()`, y `Pingüino extends Ave`. Analiza el problema con LSP y propón al menos dos soluciones.
>
> **16.** Caso taxis Acme: un compañero propone resolver lo de `dest` vs `destination` con `if (driver.getDispatchUri().startsWith("acme.com"))`. ¿Por qué Martin dice que ningún arquitecto serio lo permitiría? Da 2 razones del libro.
>
> **17.** En el experimento del reporte financiero: ¿por qué el Interactor queda como el componente más protegido y qué jerarquía de protección se forma sobre él?
>
> > [!success]- ✅ Respuestas — Nivel 3
> >
> > - **11.** Para extender sin editar necesitas piezas pequeñas (SRP), un punto de variación abstracto al que apunten los clientes (DIP) y que cada implementación sea sustituible de verdad (LSP). Sin ellos, extender obliga a modificar.
> > - **12.** `interface Notificador { void enviar(Mensaje m); }` con `NotificadorCorreo`, `NotificadorSms`, `NotificadorPush`. `ServicioPedidos` recibe un `Notificador` por constructor. Agregar WhatsApp = clase nueva; el servicio no cambia.
> > - **13.** Crear interfaces y jerarquías para una variación que nunca llegará (p. ej. `IFormatoFecha` con una sola implementación) añade indirección sin beneficio.
> > - **14.** En lugar de `new ServicioCorreo()`, el servicio recibe `Notificador`; en la prueba pasas un `NotificadorFalso` que solo guarda el mensaje. La prueba corre en milisegundos sin red.
> > - **15.** `Pingüino` no puede volar, así que `volar()` lanzaría error o no haría nada: rompe LSP. Soluciones: (a) separar interfaces `Ave` y `AveVoladora`; (b) usar composición con un `ComportamientoDeVuelo` (Strategy); (c) quitar `volar()` de la base.
> > - **16.** (1) Mete la palabra "acme" en el código: abre la puerta a errores misteriosos y brechas de seguridad. (2) No escala: si Acme compra Purple Taxi habría que agregar otro `if` por marca. La salida seria es aislar con un módulo de creación de comandos + base de configuración por URI.
> > - **17.** Porque contiene las reglas de negocio (la preocupación central; lo demás es periférico). Jerarquía: Interactor (más protegido) > Controlador > Presentadores > Vistas (menos protegidas); las dependencias apuntan siempre hacia lo más protegido.

---

## 📋 Resumen Ejecutivo

> [!summary] 📋 Lo Esencial
>
> - **SOLID** es la versión concreta, para objetos, de "alta cohesión + bajo acoplamiento".
> - **SRP:** una razón (un actor) para cambiar. **OCP:** agrega variantes sin editar lo existente. **LSP:** la derivada cumple el contrato de la base. **ISP:** interfaces pequeñas por rol. **DIP:** el negocio depende de abstracciones, no de detalles.
> - Los cinco **se refuerzan**: SRP da piezas pequeñas, DIP e ISP las conectan bien, LSP las hace intercambiables y OCP es el resultado.
> - Son **guías, no dogmas**: aplícalos donde hay variación real para evitar la sobreingeniería.
> - Cada principio tiene un **chequeo de 10 segundos** y un **olor de código** que lo delata.

---

## ✅ Metas de Aprendizaje

> [!note] 🎯 Nivel Básico
>
> - [ ] Enuncio los cinco principios con mis propias palabras.
> - [ ] Reconozco una violación típica de cada principio en un fragmento de código.
> - [ ] Aplico el chequeo de 10 segundos a una clase dada.
>
> [!note] 🎯 Nivel Intermedio
>
> - [ ] Refactorizo código con `if/switch` hacia polimorfismo (OCP).
> - [ ] Divido una interfaz grande por roles (ISP) y una clase con varios actores (SRP).
> - [ ] Explico por qué `Cuadrado extends Rectangulo` viola LSP.
> - [ ] Relaciono cada caso del libro (Employee, reporte financiero, Square, Acme, OPS, Factory) con su principio.
>
> [!note] 🎯 Nivel Avanzado
>
> - [ ] Diseño un módulo con DIP e inyección por constructor, probable con falsos.
> - [ ] Explico cómo SRP, ISP, DIP y LSP habilitan OCP.
> - [ ] Decido cuándo **no** aplicar un principio para evitar sobreingeniería.

---

## 📊 Resumen Visual

> [!note] 🗺️ Diagrama — Resumen Visual
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u1-05-05-mind.svg]]
>
> **Se lee así:** El mapa mental recorre los cinco principios con su eslogan: *SRP* → una misión, un actor; *OCP* → extiende sin editar, polimorfismo; *LSP* → sustituye sin romper, contrato; *ISP* → interfaces por rol, sin métodos vacíos; *DIP* → abstracciones, inyección por constructor. Cierra con *errores comunes*: decoración, sobreingeniería y herencia por reutilización.
>
> **Por qué importa:** cada principio queda asociado a una técnica concreta (polimorfismo, contrato, inyección por constructor) y a un error típico, que es justo lo que pide el control.
>
> **Ejemplo:** para el control de ESPOL, este mapa sirve como checklist: si un principio no tiene técnica ni error asociado, todavía no lo has estudiado.

> [!success] 🔍 Comparación Final
>
> | Aspecto | Sin SOLID | Con SOLID |
> |---|---|---|
> | **Cambio** | ❌ En cascada | ✅ Local |
> | **Tests** | Pegados a BD, red y concreciones | Mocks fáciles |
> | **Extensión** | Editar código existente | Agregar código nuevo |
> | **Equipo** | Conflictos en las mismas clases | Cada quien su módulo |
> | **Uso Recomendado** | Prototipo desechable | ✅ **Todo diseño OO que va a evolucionar** |

---

---

## 🔁 Repaso SR (flashcards)

#flashcards/diseno-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition (Control02: miércoles 23:59)
>
> - ¿Meta de SOLID en 3 puntos (Parte III)?::Estructuras de nivel medio que toleren el cambio, fáciles de entender y reutilizables en componentes.
> - ¿Quién armó el acrónimo y cuándo?::Martin reunió los principios desde los 80 (USENET); Feathers propuso el orden S.O.L.I.D. hacia 2004.
> - ¿SRP en versión final + confusión típica?::Un módulo responde a un solo actor; NO significa una función por clase.
> - ¿Caso clásico Factura (Sabalete)?::calculaTotal + imprimeFactura + guardarArchivo = 3 razones; se parte en FacturaImpresion y FacturaPersistencia.
> - ¿Employee: 3 métodos y sus actores?::calculatePay (CFO), reportHours (COO), save (CTO); compartir regularHours causó cifras millonarias erradas.
> - ¿2 síntomas de violar SRP?::Duplicación accidental y merges por actores distintos en el mismo archivo.
> - ¿OCP en 1 frase + experimento?::Abierto a extensión, cerrado a modificación; reporte web→impresora con cero líneas viejas tocadas.
> - ¿Regla de protección entre componentes?::Si A se protege de B, B depende de A; el Interactor (reglas de negocio) es lo más protegido.
> - ¿Square/Rectangle por qué viola LSP?::Alto y ancho del cuadrado mutan juntos; el assert de área falla y el cliente necesita ifs.
> - ¿Moraleja de los taxis Acme?::Una interfaz no sustituible (dest vs destination) contamina la arquitectura con casos especiales.
> - ¿ISP en Java vs Python?::En Java, importar OPS te ata a op2/op3 (recompilas por cambios ajenos); en dinámicos no hay dependencia fuente, pero el principio vale a nivel arquitectura.
> - ¿DIP: qué se tolera y qué no?::Se tolera lo concreto estable (String); se evita lo concreto volátil con 4 prácticas (interfaces, no heredar, no sobrescribir, no nombrar).
> - ¿Línea curva del Abstract Factory?::Separa abstracto de concreto; dependencias hacia lo abstracto, control en sentido contrario = inversión.

## 🚀 Próximos Pasos

> [!quote] 🌟 Continuando
>
> **Has aprendido:**
>
> ✅ Los 5 principios con definición, mecanismo, chequeo de 10 segundos y código antes/después
> ✅ Cómo se relacionan entre sí y con cohesión/acoplamiento
> ✅ Los errores típicos al aplicarlos (decoración y sobreingeniería)
>
> **Próximo tema Unidad 2:**
>
> | Tema | Qué verás | Por qué importa |
> |---|---|---|
> | **Diseño arquitectónico** | Estilos y vistas (S1 del deck) | Donde SOLID se vuelve sistema |

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../Diseño de Software|Diseño de Software]]
> - Anterior: [[03 - Paradigmas de programación y diseño]]
> - Relacionado: [[02 - Principios de diseño, cohesión y acoplamiento]]
> - Syllabus: [[../Bienvenida y Syllabus Diseño de Software|Bienvenida y Syllabus Diseño de Software]]

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - Deck docente 01bDisenoSoftware (S3): SOLID.
> - R. C. Martin, *Clean Architecture*, Parte III, págs. impresas 57–59 (resumen ejecutivo SOLID) + caps. 7 a 11 (SRP, OCP, LSP, ISP, DIP). Lectura Control02.
> - D. Sabalete, "SOLID explicado en español sencillo", freeCodeCamp ES, 2022 (caso Factura/Libro + anti-patrones por principio).
> - LabEx, "Preguntas y respuestas de entrevista Java" (Q&A SOLID/POO; Factory/Singleton/Strategy reservados para Unidad 3 Patrones).
> - R. C. Martin, *Agile Software Development: Principles, Patterns, and Practices*, Prentice Hall, 2002 (origen de SOLID).
> - B. Meyer, *Object-Oriented Software Construction*, Prentice Hall, 1988 (principio abierto/cerrado).
> - B. Liskov, *Data Abstraction and Hierarchy*, OOPSLA, 1987; B. Liskov y J. Wing, *A Behavioral Notion of Subtyping*, 1994.

---

**Tags:** #CCPG1042 #unidad1 #solid #principios #diseno-software
