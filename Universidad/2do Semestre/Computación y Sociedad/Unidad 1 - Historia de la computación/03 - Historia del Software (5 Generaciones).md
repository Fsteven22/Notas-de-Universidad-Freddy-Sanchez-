# 💾 Historia del Software — Las 5 Generaciones

## 🎯 Introducción

> [!info]- 💡 ¿Cómo evolucionó la forma de programar?
>
> A medida que el hardware se volvió más potente, la forma de comunicarse con las máquinas también tuvo que evolucionar. Lo que comenzó como secuencias de ceros y unos se transformó progresivamente en lenguajes cada vez más cercanos al lenguaje humano.
>
> ```mermaid
> graph LR
>     A[Lenguaje máquina<br/>1951-1959] --> B[Lenguajes de<br/>alto nivel<br/>1959-1965]
>     B --> C[Sistemas operativos<br/>1965-1971]
>     C --> D[Programación<br/>estructurada<br/>1971-1989]
>     D --> E[POO y WWW<br/>1990-presente]
>
>     style A fill:#ffe1e1
>     style B fill:#fff4e1
>     style C fill:#e1ffe1
>     style D fill:#e1f5ff
>     style E fill:#f5e1ff
> ```

---

## 1️⃣ Primera Generación (1951 – 1959)

> [!note]- 🖥️ Lenguaje máquina y ensamblador
>
> Los primeros programas fueron escritos directamente en **lenguaje de máquina**: secuencias de ceros y unos que la CPU podía ejecutar directamente. Este proceso era extremadamente tedioso y propenso a errores.
>
> Como solución surgieron los **lenguajes ensambladores**, que reemplazaban los códigos binarios por nemotécnicos más legibles.
>
> ```
> ; Ejemplo ensamblador
> MOV AX, 5      ; mover el valor 5 al registro AX
> ADD AX, 3      ; sumar 3 al valor en AX
> INT 21h        ; llamada al sistema
> ```
>
> | Concepto | Descripción |
> |---|---|
> | **Lenguaje máquina** | Binario puro (0s y 1s), ejecutable directo por la CPU |
> | **Ensamblador** | Nemotécnicos (ADD, MOV, INT) traducidos a binario |
> | **Traductor** | Programa que convierte ensamblador a lenguaje máquina |
> | **Programadores de sistemas** | Quienes creaban herramientas para facilitar la programación |
>
> ```mermaid
> graph LR
>     A[Instrucciones en<br/>ensamblador] --> B[Programa<br/>ensamblador]
>     B --> C[Instrucciones en<br/>lenguaje máquina]
>
>     style A fill:#e1f5ff
>     style B fill:#e1ffe1
>     style C fill:#fff4e1
> ```
>
> > ⚠️ La programación en lenguaje máquina **demandaba mucho tiempo y era propensa a errores**, lo que impulsó la búsqueda de mejores herramientas.

---

## 2️⃣ Segunda Generación (1959 – 1965)

> [!note]- 📝 Lenguajes de alto nivel
>
> A medida que el hardware se hizo más potente, se necesitaban herramientas más expresivas. Surgieron los **lenguajes de alto nivel**, que permitían escribir instrucciones usando declaraciones en inglés, mucho más cercanas al pensamiento humano.
>
> | Lenguaje | Propósito | Año aprox. |
> |---|---|---|
> | **FORTRAN** | Cálculo numérico científico e ingeniería | 1954 |
> | **COBOL** | Aplicaciones empresariales y comerciales | 1959 |
> | **LISP** | Inteligencia artificial e investigación | 1958 |
>
> ```mermaid
> graph TD
>     A[High-level language<br/>FORTRAN · COBOL · LISP]
>     B[Assembly language]
>     C[Machine language]
>
>     A --> B --> C
>
>     style A fill:#fff4e1
>     style B fill:#e1f5ff
>     style C fill:#e1ffe1
> ```
>
> > 💡 Un compilador traduce el código de alto nivel a lenguaje máquina, permitiendo que el programador se enfoque en resolver el problema y no en los detalles del hardware.

---

## 3️⃣ Tercera Generación (1965 – 1971)

> [!note]- ⚙️ Sistemas operativos y software de sistemas
>
> Durante esta generación se hizo evidente que el **humano estaba ralentizando el proceso de computación**: la CPU quedaba ociosa mientras los programadores preparaban las siguientes instrucciones.
>
> La solución fue poner los recursos de la computadora **bajo el control de la propia computadora**, creando programas que determinaran qué otros programas se ejecutarían y cuándo. Este tipo de programa se llama **sistema operativo**.
>
> | Innovación | Descripción |
> |---|---|
> | **Sistema operativo** | Administra recursos y decide qué programas se ejecutan |
> | **SPSS** | Paquete Estadístico para Ciencias Sociales, escrito en FORTRAN |
> | **Usuarios no programadores** | Por primera vez, personas sin conocimiento técnico usaban computadoras |
>
> ```mermaid
> graph TD
>     A[Application packages]
>     B[Systems software]
>     C[High-level languages]
>     D[Assembly languages]
>     E[Machine language]
>
>     A --> B --> C --> D --> E
>
>     style A fill:#fff4e1
>     style B fill:#e1f5ff
>     style C fill:#e1ffe1
>     style D fill:#f5e1ff
>     style E fill:#ffe1e1
> ```
>
> > 💡 Los programadores de sistemas comenzaron a crear **herramientas de software para que otros las usaran**, naciendo así la distinción entre desarrolladores y usuarios finales.

---

## 4️⃣ Cuarta Generación (1971 – 1989)

> [!note]- 🏗️ Programación estructurada y explosión del software
>
> En los años 70 se introdujeron mejores técnicas de programación llamadas **programación estructurada**, basadas en tres estructuras de control fundamentales:
>
> | Estructura | Descripción |
> |---|---|
> | **Secuencia** | Instrucciones ejecutadas una tras otra |
> | **Selección** | Bifurcación según una condición (SI/NO) |
> | **Iteración** | Repetición de un bloque mientras se cumpla una condición |
>
> **Ventajas de la programación estructurada:**
> - Programas más sencillos y rápidos de desarrollar
> - Reducción de costos de mantenimiento
> - Mejor documentación interna
> - Código más fácil de entender
>
> ### Lenguajes destacados
>
> | Lenguaje | Característica principal |
> |---|---|
> | **Pascal** | Diseñado para enseñanza de programación estructurada |
> | **Modula-2** | Evolución de Pascal para proyectos más grandes |
> | **C** | Permite mezclar ensamblador; base del sistema UNIX |
> | **C++** | C con orientación a objetos; estándar de la industria |
> | **BASIC** | Actualizado a versiones estructuradas para PCs |
>
> ### Sistema operativos y aplicaciones
>
> | Producto | Relevancia |
> |---|---|
> | **PC-DOS / MS-DOS** | Estándar para ordenadores personales IBM y compatibles |
> | **Macintosh OS** | Introdujo el ratón y la interfaz gráfica de usuario (GUI) |
> | **Lotus 1-2-3** | Primera hoja de cálculo comercialmente exitosa |
> | **WordPerfect** | Uno de los primeros procesadores de texto reales |
> | **dBase IV** | Sistema de administración de bases de datos para PCs |
> | **UNIX** | Desarrollado en AT&T, estándar en entornos universitarios |

---

## 5️⃣ Quinta Generación (1990 – presente)

> [!note]- 🌐 Orientación a objetos, Microsoft y la WWW
>
> La quinta generación se destaca por tres eventos fundamentales:
>
> | Evento | Descripción |
> |---|---|
> | **Ascenso de Microsoft** | Dominó el mercado del software de escritorio con Windows |
> | **Programación orientada a objetos (POO)** | Se convirtió en el paradigma de elección para grandes proyectos |
> | **World Wide Web (WWW)** | Transformó Internet en una plataforma de información global |
>
> ### Lenguajes clave
>
> | Lenguaje | Creador | Relevancia |
> |---|---|---|
> | **Java** | Sun Microsystems | POO multiplataforma, compitió con C++ |
> | **Visual Basic .NET** | Microsoft | Plataforma .NET para desarrollo rápido |
> | **Visual C++ .NET** | Microsoft | C++ para la plataforma .NET |
> | **Python** | Guido van Rossum | Simplicidad y versatilidad, ampliamente usado hoy |
>
> > 💡 Los programas se agruparon en **suites** (conjuntos de aplicaciones relacionadas), como Microsoft Office, que reunía procesador de texto, hoja de cálculo y presentaciones en un solo paquete.
> >
> ### 🐍 Caso especial — Python
>
> **Python**, creado por **Guido van Rossum** en 1991, es uno de los lenguajes
> más representativos de esta generación. Se destaca por su simplicidad y
> versatilidad, siendo hoy ampliamente usado en ciencia de datos, inteligencia
> artificial y desarrollo web.
>
> | Dato | Detalle |
> |---|---|
> | **Creador** | Guido van Rossum |
> | **Año** | 1991 |
> | **Característica** | Sintaxis simple, multiplataforma, de propósito general |
> | **Uso actual** | IA, ciencia de datos, web, automatización |
>
> > 💡 Python ha tenido múltiples versiones mayores — la rama **2.x** y la
> > rama **3.x** coexistieron durante años hasta que Python 2 fue
> > oficialmente descontinuado en 2020.
> 

---

## 📅 Línea de Tiempo de Lenguajes

> [!summary]- 📅 Evolución de los lenguajes de programación
>
> ```mermaid
> timeline
>     title Lenguajes de Programación
>     1954 : FORTRAN — cálculo científico
>     1959 : COBOL — aplicaciones empresariales
>     1958 : LISP — inteligencia artificial
>     1964 : BASIC — programación para principiantes
>     1970 : Pascal — enseñanza de programación estructurada
>     1972 : C — sistemas operativos y bajo nivel
>     1983 : C++ — POO + bajo nivel
>     1991 : Java — POO multiplataforma
>     1991 : Visual Basic / C++ .NET — plataforma Microsoft
> ```

---

## 📊 Resumen General

> [!summary]- 📊 Las 5 generaciones de un vistazo
>
> | Generación | Período | Innovación clave | Lenguajes representativos |
> |---|---|---|---|
> | **1ª** | 1951–1959 | Lenguaje máquina y ensamblador | Binario, Assembly |
> | **2ª** | 1959–1965 | Lenguajes de alto nivel | FORTRAN, COBOL, LISP |
> | **3ª** | 1965–1971 | Sistemas operativos | FORTRAN, software de sistemas |
> | **4ª** | 1971–1989 | Programación estructurada | Pascal, C, C++, BASIC |
> | **5ª** | 1990–hoy | POO y WWW | Java, Python, .NET |

---

**Tags:** #historia #software #generaciones #lenguajes #fortran #cobol #pascal #java #python #POO #WWW #unidad1 #EYAG1037