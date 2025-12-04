# 💻 Sistemas Operativos

> [!quote] 🧠 "El sistema operativo es el director de orquesta que hace que todas las partes de la computadora trabajen en armonía." - anónimo

---

> [!info]- ## 📝 Fundamentos: ¿Qué es un Sistema Operativo?
> Un **Sistema Operativo (SO)** es un software fundamental que actúa como intermediario entre el hardware de una computadora y el usuario. Su principal objetivo es proporcionar un entorno en el que el usuario pueda ejecutar programas de manera conveniente y eficiente. Administra y coordina los recursos del sistema, como la memoria, la CPU, los dispositivos de entrada/salida y el almacenamiento, para asegurar un funcionamiento óptimo. Sin un SO, un ordenador no podría ejecutar ningún programa de usuario, ya que no sabría cómo interactuar con el hardware.

---

> [!tip]- ## 📊 Funciones Clave de un Sistema Operativo
> | Función | Descripción | Ejemplo |
> | :--- | :--- | :--- |
> | **Gestión de Procesos** | Administra el ciclo de vida de los programas (creación, ejecución, terminación). | Multitarea en Windows o macOS. |
> | **Gestión de Memoria** | Asigna y desasigna la memoria principal a los procesos. | Memoria virtual para ejecutar programas grandes. |
> | **Gestión de Archivos** | Organiza y gestiona los datos en el disco duro. | El sistema de carpetas de Windows (NTFS) o Linux (ext4). |
> | **Gestión de E/S** | Controla los dispositivos de entrada y salida (ratón, teclado, impresoras). | Conectar una memoria USB y que el sistema la reconozca. |
> | **Seguridad** | Protege los recursos del sistema del acceso no autorizado. | Permisos de usuario para archivos y carpetas. |

---

> [!example]- ## 💻 Tipos de Sistemas Operativos
> Los sistemas operativos se clasifican de diversas formas, dependiendo de su enfoque, capacidad y uso.
>
> ### **Por el número de tareas**
>
> * **Monotarea**: Solo puede ejecutar una tarea a la vez. No es común en los sistemas modernos.
> * **Multitarea**: Permite al usuario ejecutar múltiples programas de forma simultánea. La gran mayoría de los SO actuales, como **Windows**, **macOS** y **Linux**, son multitarea.
>
> ### **Por el número de usuarios**
>
> * **Monousuario**: Solo permite que un usuario interactúe con el sistema en un momento dado.
> * **Multiusuario**: Permite que varios usuarios utilicen el mismo sistema al mismo tiempo, ya sea de forma remota o local. Los SO de servidores son un claro ejemplo.
>
> ### **Por su propósito**
>
> * **De Tiempo Real (Real-Time OS)**: Diseñados para aplicaciones que requieren una respuesta inmediata en un tiempo predecible. Se usan en sistemas de control industrial, robótica y equipos médicos.
> * **Integrados (Embedded OS)**: SO minimalistas diseñados para dispositivos específicos con recursos limitados, como electrodomésticos, routers o cajeros automáticos.
> * **De Red (Network OS)**: Optimizados para la gestión de recursos de red, seguridad y conectividad entre diferentes dispositivos.

---

> [!example]- ## 📈 Estructura del Sistema Operativo
> La estructura del SO se puede visualizar como una serie de capas, donde cada capa tiene una función específica y se comunica con la capa adyacente.
>
> ```mermaid
> graph TD
>     Hardware[Hardware - CPU, RAM, Dispositivos] --> Kernel[Kernel - Corazón del SO];
>     Kernel --> Shell[Shell - Intérprete de Comandos];
>     Shell --> Aplicaciones[Aplicaciones y Programas de Usuario];
> ```
>
> * **Hardware**: La base física de la computadora.
> * **Kernel**: El núcleo del SO, que se encarga de la gestión de los recursos y la comunicación directa con el hardware.
> * **Shell**: La interfaz con el usuario, que puede ser gráfica (GUI) o de línea de comandos (CLI).
> * **Aplicaciones**: El software que el usuario ejecuta para realizar tareas específicas.

---

> [!tip]- ## ✅ Técnica de Estudio
>
> ### 🧠 **Método de Preguntas y Respuestas**
>
> Para dominar este tema, utiliza el método de `preguntas y respuestas` basado en los callouts. Mantén los callouts cerrados y úsalos para autoevaluarte. Por ejemplo, lee el título del callout "Funciones Clave" y trata de recordar de memoria las 5 funciones antes de desplegarlo. Esto reforzará tu memoria a largo plazo de forma muy efectiva.

---

> [!link]- ## 📚 Referencias y Tags
>
> ### 🔗 Notas Relacionadas
>
> * [[Línea de Comandos (CLI)]]
> * [[Gestión de Proyectos]]
> * [[Hardware]]
>
> ### 📚 Notas Complementarias
>
> * [[Productividad Digital]]
> * [[Análisis de Tiempo]]
> * [[Conectando Notas en Obsidian]]
>
> ---
>
> #sistemasOperativos #informatica #aprendizaje #tecnologia #kernel