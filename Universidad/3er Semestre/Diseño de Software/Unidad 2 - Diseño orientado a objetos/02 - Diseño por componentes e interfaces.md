---
dg-publish: true
tags: [CCPG1042, unidad2, componentes, interfaces, diseno-software]
---

# 🧩 Diseño por Componentes e Interfaces

## 🎯 Introducción

> [!info] 💡 ¿Por Qué tu Clase Necesita un Contrato?
>
> El **diseño por componentes** baja la arquitectura a piezas construibles: cada componente expone una **interfaz** (contrato) y esconde su interior. Así dos personas programan en paralelo sin pisarse — y el día que cambias la implementación, nadie se entera.
>
> **Importancia histórica:** la crisis de los 2000 fue de integración — sistemas enormes donde cambiar una librería rompía diez módulos. De ahí nacieron los estándares de componentes (.NET, JEE, servicios web): programar contra contratos, no contra código ajeno.
>
> **Relevancia actual:** microservicios, paquetes npm, APIs REST — todo es "componente + interfaz". Tu proyecto se evalúa igual: ¿puedo cambiar una pieza sin romper las demás?
>
> **Analogía del mundo real:** piensa en enchufes eléctricos:
>
> - **Sin interfaz** → Cada aparato trae cable pelado distinto (todo acoplado).
> - **Con interfaz** → Enchufe estándar: conectas sin saber cómo genera la planta.
> - **Contrato** → Voltaje + forma prometidos; si cambian, avisan (versionan).
>
> | Razón | Sin Interfaces | Con Interfaces |
> |---|---|---|
> | **Paralelo** | Esperan a que el otro termine | Programan contra el contrato |
> | **Cambio interno** | Rompe a todos | Invisible si respeta contrato |
> | **Pruebas** | Necesitan todo real | Mocks del contrato (Unidad 5) |
> | **Reutilización** | Copiar-pegar | Importar componente |

> [!note] 🗺️ Diagrama — Introducción
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u2-03-01-graph.svg]]
>
> **Se lee así:** Es un árbol con raíz «Cliente» y un rombo «¿Contrato?». La rama roja «✘ Código directo» baja a dos consecuencias: «Bloqueado» y «Cambio rompe todo»; la rama verde «✔ Interfaz» baja a otras dos: «Paralelo real» y «Cambio invisible».
>
> **Por qué importa:** Convierte el argumento en dos pares de consecuencias opuestas: sin contrato el cliente espera y cualquier cambio se propaga; con contrato el equipo avanza en paralelo y los cambios se quedan dentro de la pieza.
>
> **Ejemplo:** En el SIEL, un `GestorActas` usado directo bloquea al frontend cuando cambia el formato del acta; detrás de `IRegistroActas` el frontend avanza mientras el backend rehace su implementación.

---

## 🧵 Anatomía del Componente (Pressman cap. 11)

### 🎭 Contrato, Provisión y Requerimiento

> [!note] 📋 Definición — Las Tres Caras
>
> - **Provee:** qué servicios ofrece (`ReportePDF.generar(datos)`).
> - **Requiere:** qué necesita para funcionar (fuente de `datos` válida).
> - **Oculta:** qué nadie debe tocar (caché interna, queries crudas).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u2-03-02-graph.svg]]
>
> **Se lee así:** Una caja central «Componente» con dos flechas: hacia la derecha sale «✔ Provee: qué ofrece» y hacia la caja entra «✔ Requiere: qué necesita». Es un diagrama de tres nodos, sin nada más dentro.
>
> **Por qué importa:** Reduce el componente a dos preguntas que se responden antes de codificar —qué promete y qué necesita—; lo que no aparece en ninguna de las dos caras es justamente lo que queda oculto.
>
> **Ejemplo:** `ReportePDF` provee `generar()` y `vistaPrevia()` y requiere una fuente de datos válida; su caché interna y sus queries crudas no están en ninguna de las dos caras, y por eso nadie debe verlas.
>
> **Principios de diseño de interfaces:**
>
> 1. **Pequeña:** 3-5 operaciones cohesivas, no 20.
> 2. **Estable:** cambia por versión, nunca en silencio.
> 3. **Explícita:** parámetros y errores documentados (qué falla y cómo).
> 4. **Sustituible:** dos implementaciones intercambiables sin tocar clientes.

### 🔍 Patrones de Estructura Interna

> [!example] 🧪 Tres Formas Sanas
>
> | Patrón | Idea | Cuándo |
> |---|---|---|
> | **Fachada** | Una cara simple ante un subsistema complejo | `TiendaFacade.comprar()` orquesta pagos+stock+envío |
> | **Delegación** | Repartir a ayudantes internos | Validador → Reglas individuales |
> | **Composición** | Armar de piezas pequeñas | `Pedido` contiene `Líneas` + `Descuento` |
>
> ```java
> // ✅ FACHADA: el cliente ve 1 método, el subsistema sigue complejo
> class TiendaFacade {
>     Resultado comprar(Carrito c, Pago p) {
>         stock.reservar(c);
>         pagos.cobrar(p);
>         return envios.programar(c);
>     }
> }
> ```

---

## 🗺️ Diagrama de Decisión: ¿Fachada, Delegación o Directo?

> [!note] 🗺️ Diagrama — ️ Diagrama de Decisión: ¿Fachada, Delegación o Directo
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u2-03-03-flow.svg]]
>
> **Se lee así:** Un flowchart que arranca en «Necesito usar un subsistema» y pregunta «¿Cuántos pasos le toma al cliente?». Si el ideal fuera un solo paso, la rama lleva a «Fachada: un método orquesta»; si ya es uno, la segunda pregunta («¿La lógica cabe en una clase?») deriva a «Delegación/composición» o a «Directo, sin ceremonia».
>
> **Por qué importa:** Ordena las tres opciones por coste: la fachada solo se justifica cuando la entrada del cliente es caro; si el subsistema ya es de un paso, una capa extra es ceremonia.
>
> **Ejemplo:** En la tienda del curso, `TiendaFacade.comprar()` sí vale la pena; en un validador de una sola regla, un wrapper solo añade indirección.

> [!tip] 💡 Lectura del diagrama
>
> La fachada no es obligatoria — es para subsistemas que duelen de usar. Si el subsistema ya es simple, usarlo directo evita capas inútiles.

---

## ⚠️ Problemas Comunes y Soluciones

> [!danger] ❌ Error 1: Interfaces Obesas ("God Interface")
>
> **Síntomas:** una interfaz de 25 métodos donde todo cambio la rompe y nadie se atreve a versionarla:
>
> ```java
> interface ISistema { // ❌ EL ERROR ESTÁ AQUÍ: 25 métodos, 4 roles mezclados
>     void generarReporte(); void pagarFactura(); void enviarCorreo();
>     // ... 22 métodos más de reportes, pagos y envíos
> }
> ```
>
> **Solución:**
>
> - Divide por rol: `IReportes`, `IPagos`, `IEnvios`.
> - Regla: si un cliente usa menos del 50% de la interfaz, está obesa.

> [!danger] ❌ Error 2: Filtrar Detalles Internos (viola **ocultamiento**)
>
> **Síntomas:** la interfaz expone códigos de error de la BD interna:
>
> ```java
> // ❌ EL ERROR ESTÁ AQUÍ: el cliente ve entrañas de Oracle
> interface Pagos {
>     void cobrar(double m) throws SQLExceptionORA00001; // filtra el motor
> }
> ```
>
> **Solución:** traduce errores internos a errores del dominio en la frontera del componente.

> [!danger] ❌ Error 3: Fachada que Hace Todo (viola **SRP + delegación**)
>
> **Síntomas:** la fachada acumula lógica de negocio en vez de orquestar:
>
> ```java
> // ❌ EL ERROR ESTÁ AQUÍ: la fachada calcula, valida y persiste
> class TiendaFacade {
>     Resultado comprar(Carrito c, Pago p) {
>         double total = 0; // ❌ lógica de negocio aquí
>         for (Linea l : c.lineas()) total += l.precio();
>         // ... + validación + persistencia, todo adentro
>         return null;
>     }
> }
> ```
>
> **Solución:** orquesta, no implementa — si la fachada crece, esconde un diseño pendiente.

---

## 🎯 Mejores Prácticas

> [!tip] 🏆 Checklist de Componentes
>
> **1. Diseña la interfaz en equipo antes del sprint**
>
> Firmas + errores + ejemplo de uso en 1 página. El código viene después.
>
> **2. Un componente, un dueño**
>
> Cada componente tiene responsable en Git: menos conflictos, más calidad.
>
> **3. Interfaz pequeña y versionada**
>
> 3-5 operaciones; cambios compatibles o versión nueva, nunca silencio.
>
> **4. Mapea a UML (puente a Stevens)**
>
> Componente = clase con estereotipo «component»; interfaz = círculo/paleta UML.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Nivel 1 — Básico
>
> **1.** Define componente con sus tres caras (provee, requiere, oculta) y da un ejemplo.
>
> **2.** ¿Qué significan los 4 principios de interfaces (pequeña, estable, explícita, sustituible)?
>
> **3.** Diferencia fachada, delegación y composición con un ejemplo de cada uno.
>
> **4.** ¿Por qué una interfaz con 25 métodos es un problema? ¿Cómo la dividirías?
>
> **5.** Dibuja el mini-diagrama cliente→interfaz→2 implementaciones de un servicio de notificaciones.
>
> > [!success]- ✅ Respuestas — Nivel 1
> >
> > - **1.** Unidad desplegable accedida solo por interfaces; provee servicios, requiere insumos, oculta interior.
> > - **2.** Pocas operaciones cohesivas; cambios versionados; errores documentados; implementaciones intercambiables.
> > - **3.** Fachada: cara simple (TiendaFacade). Delegación: reparte a ayudantes. Composición: arma de piezas (Pedido+Líneas).
> > - **4.** Nadie la implementa completa y todo cambio la rompe; dividir por rol (IReportes, IPagos...).
> > - **5.** `Notificador → INotificador ← {Email, SMS}`: el cliente conoce solo la interfaz.

> [!example] 📋 Nivel 2 — Intermedio
>
> **6.** Diseña la interfaz de un componente de reportes PDF con 4 operaciones máximas, incluyendo sus errores.
>
> **7.** Un `GestorUsuarios` hace login, reportes, envíos de correo y backup. Aplica SRP + interfaces: ¿en qué piezas queda?
>
> **8.** Explica con un caso cuándo una fachada deja de ayudar y se vuelve God Facade. ¿Cómo la detectas?
>
> **9.** ¿Cómo probarías `TiendaFacade.comprar()` sin tocar pagos ni envíos reales? (Conecta con Unidad 5.)
>
> **10.** Tu equipo discute si exponer el código de error SQL `ORA-00001` en la API. Argumenta con "leaky abstraction".
>
> > [!success]- ✅ Respuestas — Nivel 2
> >
> > - **6.** Ej.: `generar(datos)->pdf | ErrorDatos`, `vistaPrevia(datos)`, `plantillas()->lista`, `programarEnvio(pdf,destino)` — 4 cohesivas con errores del dominio.
> > - **7.** `IAuth`, `IReportes`, `INotificador`, `IRespaldo` + fachada opcional solo si orquestarlas duele.
> > - **8.** Cuando acumula reglas de negocio en vez de orquestar; se detecta porque cambiar 1 flujo toca siempre la fachada.
> > - **9.** Mocks de `IPagos` e `IEnvios` inyectados por constructor (DIP): verificas orquestación sin red.
> > - **10.** Filtra el detalle interno: la API devuelve `DUPLICADO` del dominio; el ORA queda en logs internos.

> [!example] 📋 Nivel 3 — Avanzado
>
> **11.** Diseña versionado de una API de pagos v1→v2 sin romper clientes v1: ¿qué cambia, qué se congela, cómo conviven?
>
> **12.** Argumenta cuándo NO crear una fachada aunque el subsistema tenga 10 clases.
>
> **13.** Un componente A requiere 8 servicios distintos para funcionar. Diagnostica con cohesión/acoplamiento y propón rediseño.
>
> **14.** Compara "programar contra interfaces" con el paradigma de componentes del deck (4 etapas): ¿dónde encaja cada principio?
>
> **15.** Diseña el contrato completo (firmas + errores + ejemplo) de un componente de autenticación para tu proyecto.
>
> > [!success]- ✅ Respuestas — Nivel 3
> >
> > - **11.** v1 congelada (solo fixes críticos), v2 con el cambio, ambas conviven por versión en ruta; deprecar v1 con fecha.
> > - **12.** Si los clientes usan subconjuntos disjuntos y simples: fachada agregaría acoplamiento sin valor; exponer módulos directos es mejor.
> > - **13.** Acoplamiento eferente altísimo + probable baja cohesión: partir A por misiones y agrupar dependencias por rol.
> > - **14.** Análisis→interfaces candidatas; modificación→ajustar contratos; diseño→fachadas donde duela; integración→versionado.
> > - **15.** Respuesta libre guiada: `autenticar(cred)->token | ErrorCredenciales`, `renovar(token)`, `revocar(token)` + ejemplo de uso.

---

## 📋 Resumen Ejecutivo

> [!summary] 📋 Lo Esencial
>
> - Un **componente** provee, requiere y oculta — accedido solo por **interfaces**.
> - Interfaces **pequeñas, estables, explícitas y sustituibles**.
> - **Fachada** para subsistemas que duelen; si no duele, directo.
> - Todo cambio de contrato se **versiona**, nunca en silencio.

---

## ✅ Metas de Aprendizaje

> [!note] 🎯 Nivel Básico
>
> - [ ] Defino componente con sus tres caras y doy un ejemplo.
> - [ ] Explico los 4 principios de interfaces con ejemplo.
> - [ ] Diferencio fachada, delegación y composición.

> [!note] 🎯 Nivel Intermedio
>
> - [ ] Diseño una interfaz pequeña con errores del dominio.
> - [ ] Detecto God Interface y God Facade y propongo división.
> - [ ] Explico cómo testear con mocks vía DIP.

> [!note] 🎯 Nivel Avanzado
>
> - [ ] Versiono una API sin romper clientes.
> - [ ] Diagnostico acoplamiento eferente y rediseño.
> - [ ] Diseño un contrato completo listo para implementar.

---

## 📊 Resumen Visual

> [!note] 🗺️ Diagrama — Resumen Visual
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u2-03-04-mind.svg]]
>
> **Se lee así:** Mapa mental con raíz «Componentes» y tres ramas: «Contrato» (Provee, Requiere, Oculta), «Principios» (Pequeña, Estable, Sustituible) y «Patrones» (Fachada, Delegación). No incluye «Composición», que sí aparece explicada en la sección de patrones.
>
> **Por qué importa:** Es el índice de la nota: si puedes recitar las tres ramas y sus hojas, tienes todo lo que el docente pregunta sobre diseño por componentes.
>
> **Ejemplo:** En tu proyecto de curso, el resumen debe aplicar las tres ramas: contrato firmado (provee/requiere/oculta), interfaz versionada y una fachada solo donde el flujo duele.

> [!success] 🔍 Comparación Final
>
> | Aspecto | Sin Contrato | Con Contrato |
> |---|---|---|
> | **Paralelo** | ❌ Bloqueado | ✅ Por interfaces |
> | **Cambio** | Rompe clientes | Versionado |
> | **Tests** | Requieren sistema | Mocks aislados |
> | **Uso Recomendado** | Nunca en equipo | ✅ **Estándar de proyecto** |

---

## 🚀 Próximos Pasos

> [!quote] 🌟 Continuando
>
> **Has aprendido:**
>
> ✅ Contrato provee/requiere/oculta + 4 principios
> ✅ Fachada, delegación y cuándo no usarlos
> ✅ Versionado y testing con mocks
>
> **Próximo tema:**
>
> | Tema | Qué verás | Por qué importa |
> |---|---|---|
> | **UML: clases y objetos** | Atributos, operaciones, relaciones | El idioma para dibujar todo lo anterior |

---

## 🔁 Repaso SR (flashcards)

#flashcards/diseno-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Componente en 3 verbos?::Provee + requiere + oculta — accedido solo por interfaces.
> - ¿Interfaces cómo?::Pequeñas, estables, explícitas y sustituibles.
> - ¿Fachada cuándo?::Para el subsistema que duele; si no duele, directo.
> - ¿Cambio de contrato?::Se versiona, nunca en silencio.
> - ¿Por qué solo por interfaces?::Para ocultar implementación y poder sustituir.

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../Diseño de Software|Diseño de Software]]
> - Anterior: [[01 - Diseño arquitectónico y estilos]]
> - Siguiente: [[03 - UML clases, objetos y relaciones]]
> - Syllabus: [[../Bienvenida y Syllabus Diseño de Software|Bienvenida y Syllabus Diseño de Software]]

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - R. Pressman, B. Maxim, *Software Engineering: A Practitioner's Approach*, 9th ed., cap. 11.
> - Deck docente (paradigma de componentes, 4 etapas, COTS).
> - Sílabo CCPG1042, Unidad 2: diseño orientado a objetos (7h).

> [!info] Láminas del material de clase
>
> Renderizados del deck de la unidad, en orden de presentación.
>
> Aquí van las láminas de los cuatro decks de la sesión —02b (paradigma de componentes), 04a (lenguaje unificado de modelado), 04b (implementación desde el diseño) y 04p (arquitectura MVC)—; cada una va seguida de su lectura, con el deck y la página de origen.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Paradigmas/dsw-02b-p33.png]]
>
> **Se lee así:** Lámina de 02b, p. 33: una tabla de dos columnas «Component characteristic / Description» con cinco filas —Composable, Deployable, Documented, Independent y Standardized— y cada fila explica la característica en el texto del deck (por ejemplo, Composable: todas las interacciones externas deben ocurrir por interfaces públicamente definidas).
>
> **Por qué importa:** Es la definición operativa de componente del deck: «composable» es exactamente lo que obliga a que toda interacción externa pase por la interfaz.
>
> **Ejemplo:** Tu `ReportePDF` es componible si todo entra por `IReportes`, y es desplegable si se publica y se versiona por separado.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Paradigmas/dsw-02b-p34.png]]
>
> **Se lee así:** Lámina de 02b, p. 34: la figura 16.12 del libro, un `Adaptor` que enlaza un `sensor` con un `Data collector`; a la derecha se listan las operaciones que pide el sensor (`get data`, `sensorData`) y las que ofrece el collector (`addSensor`, `removeSensor`, `startSensor`, `stopSensor`, `testSensor`, `initialize`, `report`, `listAll`).
>
> **Por qué importa:** Componer componentes no es «llamar a otro»: es encajar dos interfaces que no son iguales mediante una pieza que traduce de un contrato al otro.
>
> **Ejemplo:** Si tu portal de notas usa un componente de notificaciones y otro de almacenamiento, el `Adaptor` es la pieza que traduce entre ambos contratos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Paradigmas/dsw-02b-p38.png]]
>
> **Se lee así:** Lámina de 02b, p. 38: dos figuras —«CBSE with reuse» y el «component identification process»— más un outline de cinco pasos: identificar componentes candidatos según los requerimientos descubiertos, modificar los requerimientos del sistema, diseño arquitectónico, componer los componentes para crear el sistema y, al final, la búsqueda y validación de componentes.
>
> **Por qué importa:** Es el proceso del paradigma de componentes: el componente no se diseña primero, se busca y después se acomodan los requerimientos al componente disponible.
>
> **Ejemplo:** En tu proyecto, antes de escribir el módulo de reportes buscas una librería que ya lo resuelva y solo entonces ajustas el requerimiento a lo que ella ofrece.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Paradigmas/dsw-02b-p40.png]]
>
> **Se lee así:** Lámina de 02b, p. 40: define el modelo de componentes como «definición de estándares para implementación, documentación y despliegue», afirma que los estándares aseguran que los componentes puedan interoperar y que el middleware de ejecución soporte su operación, y lista tres ejemplos: Enterprise Java Beans (EJB), el modelo .NET de Microsoft y CORBA.
>
> **Por qué importa:** Explica por qué el contrato necesita un estándar detrás: sin modelo de componentes, dos piezas que «hablan» igual no se pueden componer.
>
> **Ejemplo:** Tu API REST sigue el mismo espíritu de EJB, .NET y CORBA: un estándar que garantiza que un cliente y un servidor intercambiables funcionen juntos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p11-clase-uml.png]]
>
> **Se lee así:** Lámina de 04a, p. 11: un diagrama de la clase `Book` con sus tres compartimentos (nombre, atributos `#title : String` y `#available : Boolean = true`, y operaciones `<<constructor>> create()`, `+copiesOnShelf() : Int`, `+borrow(c : Copy)`), con anotaciones que explican cada adorno: la visibilidad `+ - # ~`, el nombre en cursiva si la clase es abstracta, el tipo del atributo, el valor inicial y la firma de la operación.
>
> **Por qué importa:** Cada elemento de la caja significa algo; dibujar la caja sin conocer los adornos es perder la mitad de la información.
>
> **Ejemplo:** En el SIEL, `Candidatura` se dibuja con `-totalVotos : int` y `+aprobada() : boolean`, y el `#` lo reservas para lo que hereda de `Dignidad`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p12-visibilidad.png]]
>
> **Se lee así:** Lámina de 04a, p. 12: tres viñetas con los signos `+`, `#` y `-` y su definición textual —`+` público: cualquier cliente de la clase puede acceder a los miembros públicos; `#` protegido: los miembros de la clase o cualquier subclase pueden acceder a los protegidos; `-` privado: solo los miembros de la misma clase.
>
> **Por qué importa:** Fija el alcance real de cada visibilidad: `#` es para toda la jerarquía, no «privado con permiso».
>
> **Ejemplo:** En `Acta`, `-votos : List<Integer>` es privado, `#padron : Padron` lo usan `Acta` y sus subclases, y `+registrar() : Comprobante` es público.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p14-heuristicas.png]]
>
> **Se lee así:** Lámina de 04a, p. 14: «Enfoque 1: Data-Driven Design» con las heurísticas de Shlaer y Mellor / Booch y cuatro familias de candidatos a clase —cosas tangibles o del mundo real (libro, copia, curso), roles (miembro de la biblioteca, estudiante, director de estudios), eventos (llegada, salida, solicitud) e interacciones (reunión, intersección).
>
> **Por qué importa:** Da un filtro reutilizable para decidir qué sustantivo del enunciado merece una caja, en vez de dibujar clases por intuición.
>
> **Ejemplo:** En el SIEL, `Acta` entra como evento con identidad propia, mientras que «el día de la elección» es un evento sin estado y queda como fecha.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p16-sustantivo-verbo.png]]
>
> **Se lee así:** Lámina de 04a, p. 16: dos párrafos de requerimientos de una biblioteca escritos en prosa —«Books and journals» y «Borrowing»—: la biblioteca contiene libros y revistas, puede tener varias copias, los préstamos de los miembros duran tres semanas, un miembro puede llevar hasta seis ítems a la vez y el personal hasta doce, y solo el personal puede llevarse revistas.
>
> **Por qué importa:** Es el insumo real del análisis sustantivo/verbo: los sustantivos dan clases y los verbos dan operaciones, y solo funciona sobre texto así.
>
> **Ejemplo:** Con el mismo método, el enunciado del SIEL produce `Candidatura`, `Acta` y `Candidato` como clases y `inscribir`, `calificar`, `registrar` como operaciones.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p18-notacion-relaciones.png]]
>
> **Se lee así:** Lámina de 04a, p. 18: un catálogo de la notación de relaciones en UML con los cinco trazos del manual de referencia (bidireccional/binaria, unidireccional, composición, asociación con nombre y flecha unidireccional simple), y en cada extremo se pueden anotar el nombre del rol, las características y la multiplicidad.
>
> **Por qué importa:** El mismo trazo significa cosas distintas según los adornos; sin ellos, dos diagramas con la misma línea dicen relaciones diferentes.
>
> **Ejemplo:** En `OrganizacionPolitica 1 ── inscribe ── 0..* Candidatura`, el nombre de rol «auspicia» y la multiplicidad `0..*` son los que dicen quién puede tener qué.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p19-multiplicidad.png]]
>
> **Se lee así:** Lámina de 04a, p. 19: la definición de multiplicidad («número de objetos que pueden participar en una relación en un momento dado») sobre un diagrama de biblioteca con `LibraryPatron`, `Copy` y `Journal`, donde la línea «is copy of» lleva `1` en el patrón y `1..*` en la copia, y las líneas «borrows/returns» llevan `0`.
>
> **Por qué importa:** Muestra la regla que el docente evalúa: la multiplicidad va en el extremo de la clase que cuenta.
>
> **Ejemplo:** En el diagrama del SIEL, `Candidatura 1` junto a `0..* Actas` dice que una candidatura tiene cero o más actas y que cada acta pertenece a una sola candidatura.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p22-clase-asociacion.png]]
>
> **Se lee así:** Lámina de 04a, p. 22: las dos frases de la regla («se usa para adjuntar atributos a una asociación en lugar de las clases que asocia» y «la línea de asociación de clase debe tener el mismo nombre») sobre un ejemplo `Student` — is taking → `Module`, donde la línea se convierte en una clase de asociación con el atributo `mark : int`.
>
> **Por qué importa:** Los atributos de una relación no se cuelgan de una de las dos clases: nacen en una clase que queda pegada a la línea.
>
> **Ejemplo:** `OrganizacionPolitica` — inscribe → `Candidatura` con atributos de fecha y estado produce la clase `Inscripcion` colgando de la línea.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p23-generalizacion.png]]
>
> **Se lee así:** Lámina de 04a, p. 23: «Generalización y Herencia» la presenta como «un tipo especial de asociación» y explica que la subclase hereda los atributos y operaciones de la superclase y puede extenderla; el ejemplo usa `LibraryPatron` y `Copy` con `Researcher` y `Journal`.
>
> **Por qué importa:** Justifica la herencia como reutilización de estructura, no como herencia de datos sueltos: la flecha hueca significa «todo lo del padre, más lo mío».
>
> **Ejemplo:** En el SIEL, `Alcaldia` y `Prefectura` heredan de `Dignidad` y no repiten el cálculo de votos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p25-diagrama-clases.png]]
>
> **Se lee así:** Lámina de 04a, p. 25: un diagrama de clases de ejemplo (Office, Person, PersonnelRecord) con anotaciones que apuntan a cada elemento del diagrama —multiplicidad, atributos, operaciones, una interface, una agregación y una dependencia.
>
> **Por qué importa:** Es la lámina de referencia de la notación completa: cada flecha del ejemplo está rotulada con el nombre del concepto, así se lee sin el manual.
>
> **Ejemplo:** Tu diagrama del SIEL debería rotular lo mismo: multiplicidad en ambos extremos, interface marcada con `<<interface>>`, rombo de agregación y flecha punteada de dependencia.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p33-elementos-secuencia.png]]
>
> **Se lee así:** Lámina de 04a, p. 33: un diagrama de secuencia con sus cuatro elementos rotulados —los objetos sobre su línea de vida (life-line), la activation (el objeto activo, la barra vertical), el mensaje (la flecha) y la X de destroy al final de la línea.
>
> **Por qué importa:** Nombra las cuatro piezas de la notación de secuencia, que es lo que el docente pide recordar en la lámina final del deck.
>
> **Ejemplo:** En tu secuencia de inscripción, `Sistema` es la lifeline, la barra marca la activation mientras corre `verificarCupo` y la X marca el objeto que se descarta.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p39-alt.png]]
>
> **Se lee así:** Lámina de 04a, p. 39: la tabla de operadores del frame `alt` con las columnas sender/receiver y la columna Guard, donde cada traza lleva su condición entre corchetes (`[condición!]`, `[condición?]`, `[else]`), y al pie la frase «fragmento alternativo múltiple: solo se ejecuta el que cuya condición sea verdadera».
>
> **Por qué importa:** Deja explícito que las trazas de un `alt` son excluyentes: es la diferencia entre un `if/else` y un bloque que puede disparar dos ramas.
>
> **Ejemplo:** En el `alt` de registrar acta, la traza «votos > padrón → revisión» y la traza «votos ≤ padrón → registrada» no pueden ejecutarse las dos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p40-opt.png]]
>
> **Se lee así:** Lámina de 04a, p. 40: el frame `opt` dibujado con el mensaje principal y, debajo, un segundo mensaje entre corchetes con la condición; la lámina resume que «opt es opcional, el fragmento se ejecuta solo si la condición es verdadera» y que equivale a un `alt` con una sola traza.
>
> **Por qué importa:** Convierte el `<<extend>>` del diagrama de casos en algo verificable: el parche opcional es exactamente un `opt`.
>
> **Ejemplo:** El `<<extend>>` «Aplicar descuento» se dibuja como `opt` con guard `[aplica descuento]` en la secuencia del cobro.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p42-biblioteca.png]]
>
> **Se lee así:** Lámina de 04a, p. 42: la secuencia de la biblioteca con las lifeline de `Member`, `BookBorrower` y el libro, y los mensajes numerados `1: okToBorrow`, `2: borrow` y la respuesta `2.1: borrowed`.
>
> **Por qué importa:** Es el ejemplo canónico del deck: muestra una guarda («¿puede prestarse?») antes del mensaje que cambia el estado, que es el patrón de toda validación.
>
> **Ejemplo:** Tu secuencia de inscripción repite el patrón: `1: okToInscribir` (guard de prerrequisitos y cupo) y luego `2: inscribir` con su retorno.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p43-restricciones-tiempo.png]]
>
> **Se lee así:** Lámina de 04a, p. 43: la misma secuencia de biblioteca con anotaciones de restricción de tiempo sobre los mensajes —una curly `{C-A < 5 sec}` junto al mensaje y otra `{borrowed - borrowed < 1 sec}` sobre la respuesta.
>
> **Por qué importa:** El tiempo es una restricción que se anota en el propio mensaje, no un comentario aparte: por eso se la lleva al código y a las pruebas.
>
> **Ejemplo:** Si tu portal de notas exige responder los resultados en menos de 2 segundos, esa restricción se anota sobre el mensaje de retorno de la secuencia.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/UML/dsw-04a-p44-tipos-interaccion.png]]
>
> **Se lee así:** Lámina de 04a, p. 44: una tabla de tipos de interacción con su símbolo y su significado —llamada síncrona (el emisor pierde el control hasta que el receptor termina), retorno (no es un mensaje nuevo sino la respuesta de uno anterior), flat (el mensaje no espera respuesta) y asíncrona (el emisor sigue activo)— con la advertencia de que algunas versiones de UML usan el mismo símbolo para flat y asíncrona.
>
> **Por qué importa:** Distingue «el receptor contesta» de «el emisor sigue trabajando»: es lo que separa un `Future.get()` de un `ExecutorService.submit()` en el código.
>
> **Ejemplo:** Al enviar el acta a revisión, el mensaje es asíncrono: el sistema registra y sigue, sin esperar respuesta.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p11-bidireccionalidad.png]]
>
> **Se lee así:** Lámina de 04b, p. 11: el caso «Bidireccional con multiplicidad 0..1» dibujado con `Cliente` y `CtaCte` unidos por una línea con flecha en ambos sentidos, el nombre de rol `+dueño` sobre el lado de la cuenta, y el código donde cada clase guarda la referencia al otro (`public Cliente dueño;` dentro de `CtaCte`).
>
> **Por qué importa:** La bidireccionalidad no es solo la flecha: son dos atributos que hay que mantener sincronizados, y el deck le dedica cuatro páginas por eso.
>
> **Ejemplo:** En `Cliente.abrir(cuenta)` del curso, además de agregar la cuenta a la lista hay que hacer `cuenta.setTitular(this)`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p18-generalizacion.png]]
>
> **Se lee así:** Lámina de 04b, p. 18: el código de la jerarquía del deck —`public abstract class CuentaBancaria implements Impresion` y `public final class Ahorros extends CuentaBancaria` con sus atributos y métodos— más el recordatorio de que en el diagrama de clases el nombre de la clase abstracta va en cursiva.
>
> **Por qué importa:** El nombre en cursiva del diagrama es el que te dice que la clase va `abstract`; sin leerlo, la herencia se implementa como una clase concreta que se puede instanciar.
>
> **Ejemplo:** `Dignidad` en cursiva en tu diagrama del SIEL se traduce como `abstract class Dignidad`, que nadie instancia directamente.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p20-realizacion.png]]
>
> **Se lee así:** Lámina de 04b, p. 20: la interface `Impresion` con sus dos métodos (`ImprimirRecibo()` y `EstadoCuenta()`) al lado de la clase `CuentaBancaria implements Impresion`, con los cuerpos todavía como «TODO implement here».
>
> **Por qué importa:** La interface declara el contrato y la clase lo desarrolla: por eso en el diagrama la interface no tiene compartimentos que mostrar.
>
> **Ejemplo:** `<<interface>> Pagable` con `+pagar(monto : double) : Comprobante` es el contrato que la `Factura` del curso implementa.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p22-dependencia.png]]
>
> **Se lee así:** Lámina de 04b, p. 22: el ejemplo de dependencia con `import authentication.MetodoAutenticacion;` y la clase `Login` que declara `private string user`, `private string pass` y un método `ValidarCredenciales(MetodoAutenticacion metodo)` que recibe el tipo como parámetro.
>
> **Por qué importa:** La dependencia se ve en el `import` y en el parámetro: el objeto usado no queda guardado en ningún atributo.
>
> **Ejemplo:** Si `Login` guardara `private MetodoAutenticacion metodo;` ya no sería dependencia sino asociación — el error 3 de la nota 05.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p23-composicion.png]]
>
> **Se lee así:** Lámina de 04b, p. 23: el ejemplo `Automovil` con los atributos `Estereo estereo` y `Motor motor`, y un constructor que hace `estereo = new Estereo();` y `motor = new Motor();` —las dos piezas creadas dentro del propio todo— sobre el diagrama con rombo negro.
>
> **Por qué importa:** El `new` dentro del constructor es la señal inequívoca de composición: el todo es dueño y el parte nace con él.
>
> **Ejemplo:** En el curso, `Pedido` con `lineas.add(new LineaPedido(p, cantidad))` es exactamente esta lámina.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p24-agregacion.png]]
>
> **Se lee así:** Lámina de 04b, p. 24: el mismo `Automovil` pero con un constructor vacío y un método `ensamblar(Estereo e, Motor m)` que recibe las piezas ya hechas y las guarda; el diagrama marca la relación como agregación, con rombo blanco.
>
> **Por qué importa:** El contraste con la lámina anterior es la lección: en agregación el todo recibe partes que ya existían, y por eso el parte sobrevive.
>
> **Ejemplo:** `Equipo.fichar(jugador)` recibe un `Jugador` que ya existía, mientras que `Pedido` crea sus líneas.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p4-relaciones.png]]
>
> **Se lee así:** Lámina de 04b, p. 4: la frase «Las clases deben estar relacionadas con otras» sobre los siete casos numerados del deck, cada uno con su notación —dependencia (línea punteada), asociación (línea), asociación dirigida (flecha abierta), agregación (rombo blanco), composición (rombo negro), generalización (triángulo hueco) y realización (punteada con triángulo hueco).
>
> **Por qué importa:** Es la lámina que define las siete relaciones que la nota 05 traduce a código: el símbolo del diagrama es la partida para saber qué palabra reservada toca.
>
> **Ejemplo:** El rombo negro de `Pedido ◆— LineaPedido` es lo que te dice que el `Pedido` hace `new LineaPedido(...)`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p5-tabla-relaciones.png]]
>
> **Se lee así:** Lámina de 04b, p. 5: un esquema-resumen titulado «Relaciones en DC» que reagrupa las siete relaciones del deck en familias: asociación simple y asociación directa, agregación, composición, herencia/generalización, realización y dependencia.
>
> **Por qué importa:** Ordena las relaciones por familias (asociaciones, parte/todo, jerarquía, contrato y uso), que es justo la forma en que se memorizan para el examen.
>
> **Ejemplo:** Al leer tu diagrama decides primero la familia: ¿es parte/todo, jerarquía, contrato o solo uso temporal?
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Implementacion/dsw-04b-p9-codigo-asociacion.png]]
>
> **Se lee así:** Lámina de 04b, p. 9: dos clases Java lado a lado —`Cliente` con `id`, `direccion` y un `ArrayList<CuentaBancaria> cuentas`, y `CuentaBancaria` con `nro_cuenta`, `saldo` y sus getters/setters— mostrando que la línea del diagrama se materializa como un atributo.
>
> **Por qué importa:** Es la traducción literal de la asociación, con la colección que corresponde a la multiplicidad `*`.
>
> **Ejemplo:** `Factura` con `private Cliente cliente;` y `Cliente` con `private List<Factura> facturas` reproducen exactamente esta lámina.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Principios/dsw-04p-p45.png]]
>
> **Se lee así:** Lámina de 04p, p. 45: el origen de MVC —en 1988 se propuso un diseño de tres capas que desacople interfaz, navegación y comportamiento— y la definición de MVC como patrón arquitectural que desacopla la interfaz de usuario de la funcionalidad de la aplicación y del contenido de información.
>
> **Por qué importa:** Da el «por qué» del MVC: no es una moda de nombres, es la respuesta de 1988 al problema de que la interfaz, la navegación y los datos cambiaran juntos.
>
> **Ejemplo:** En el portal de notas de la ESPOL, cambiar el formulario de «Consultar resultados» no debe tocar `Candidatura`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Principios/dsw-04p-p47.png]]
>
> **Se lee así:** Lámina de 04p, p. 47: la figura clásica del MVC con tres cajas —Controller (maneja las peticiones del usuario, selecciona el comportamiento del modelo y la vista de respuesta), Model (encapsula la funcionalidad y los objetos de contenido e incorpora los estados de la WebApp) y View (prepara los datos del modelo y presenta la vista elegida por el controlador)— con las flechas de petición de comportamiento, de actualización y de datos externos.
>
> **Por qué importa:** La dirección de las flechas muestra el desacople: el controlador manda, el modelo no sabe que hay vistas y la vista no le habla al modelo.
>
> **Ejemplo:** En tu portal de notas, `ConsultaController` pide los datos a `NotaService` y entrega la respuesta a `VistaResultados`, sin que la vista hable con el modelo.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Principios/dsw-04p-p48.png]]
>
> **Se lee así:** Lámina de 04p, p. 48: la descripción textual de la figura MVC en cinco viñetas —las peticiones las maneja el controlador, el controlador selecciona el objeto vista, transmite la petición de comportamiento al modelo, el modelo accede a la base de datos o a archivos, y los datos se formatean en la vista y se devuelven al browser.
>
> **Por qué importa:** Es la lectura paso a paso de la figura anterior: el diagrama se entiende como el recorrido de una petición.
>
> **Ejemplo:** El flujo de «consultar resultados» de tu portal de notas es esta viñeta a viñeta.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Principios/dsw-04p-p49.png]]
>
> **Se lee así:** Lámina de 04p, p. 49: un ejemplo de arquitectura de 4 capas con cajas rotuladas por estereotipo —`<<UI>>` (Student Administration), `<<component>>` (Student, Seminar Schedule) e `<<infrastructure>>` (Management, Facilities, Security, Persistence)—, cortesía del Dr. Rami Bahsoon.
>
> **Por qué importa:** Muestra que las piezas del MVC se pueden separar en capas con roles explícitos: UI arriba, componentes en medio, infraestructura abajo.
>
> **Ejemplo:** Tu proyecto de curso puede rotular sus cajas igual: `<<UI>>` para el portal web, `<<component>>` para los módulos de negocio e `<<infrastructure>>` para la base de datos.

---

**Tags:** #CCPG1042 #unidad2 #componentes #interfaces #diseno-software
