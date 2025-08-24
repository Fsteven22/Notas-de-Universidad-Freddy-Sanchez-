# 🧩 Plugins y Complementos

> [!quote] 🚀 "Los plugins no son solo herramientas, son superpoderes que transforman tu espacio de trabajo en Obsidian." - anónimo

---

## 🛠️ Plugins que ya tienes

### **Advanced Tables**
> [!info]- **Descripción y Utilidad**
> Este plugin mejora enormemente la experiencia de trabajar con tablas en Obsidian. Con una sintaxis de Markdown sencilla, te permite crear, editar y manipular tablas de forma eficiente. Es ideal para organizar datos, planes de estudio, calendarios o cualquier tipo de información estructurada que necesites en tus notas.
> 
> Sus principales ventajas son:
> * **Formato automático**: Alinea las columnas y filas de forma automática.
> * **Navegación sencilla**: Te permite moverte entre celdas con la tecla `Tab`.
> * **Manipulación rápida**: Puedes insertar, borrar o mover filas y columnas con atajos de teclado.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado en la configuración. (Ya lo tienes activo según la imagen).
> 2.  **Creación**: Simplemente escribe la sintaxis de una tabla en Markdown y presiona `Tab`. El plugin la formateará automáticamente.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Crear una tabla para planificar tu semana de estudio.
>
> ```markdown
> | Día     | Mañana                    | Tarde                     |
> |---------|---------------------------|---------------------------|
> | Lunes   | [Estudio: Python]         | [Estudio: Markdown]       |
> | Martes  | [Estudio: Línea de Comandos]| [Proyecto: Automatización]|
> | Miércoles | [Estudio: Zettelkasten]   | [Proyecto: Código]        |
> ```
> > - Escribe la primera línea, presiona `Enter` y luego `Tab`. El plugin hará el formato por ti.
> > - Para añadir una nueva fila, presiona `Enter` al final de la última celda.
> > - Usa `Ctrl + Enter` para añadir una fila nueva en cualquier lugar de la tabla.

---

### **Better Word Count**
> [!info]- **Descripción y Utilidad**
> Este plugin reemplaza y mejora la función de conteo de palabras nativa de Obsidian. A diferencia de la función estándar, que solo cuenta palabras en todo el documento, este plugin te permite contar palabras, caracteres, y otros datos **solo en el texto que tengas seleccionado**. Además, puede mostrar estadísticas sobre todo el vault, ayudándote a tener una visión general de tu producción de escritura. Es una herramienta esencial para escritores, estudiantes y cualquier persona que necesite monitorear su progreso de escritura.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado en la configuración.
> 2.  **Uso Básico**: Selecciona cualquier parte del texto en tu nota. El conteo de palabras de esa selección aparecerá en la barra de estado de Obsidian.
> 3.  **Ajustes**: Dentro de la configuración del plugin, puedes elegir qué estadísticas mostrar (palabras, caracteres, oraciones, etc.) y personalizar la barra de estado para que se adapte a tus necesidades.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Contar las palabras de una sección de tu nota para cumplir con un límite de caracteres.
>
> **Tu nota:**
> ```markdown
> # Mi Resumen de Zettelkasten
> 
> El método Zettelkasten se basa en la idea de crear notas atómicas, cada una con una sola idea. Estas notas se interconectan entre sí para formar una red de conocimiento que crece orgánicamente.
> 
> El proceso de creación incluye tres tipos de notas: volátiles, bibliográficas y permanentes. La clave está en el enlace activo entre ellas, lo que fomenta la creatividad.
> ```
> > - Selecciona la primera frase: "El método Zettelkasten se basa en la idea de crear notas atómicas, cada una con una sola idea."
> > - La barra de estado te mostrará el conteo solo de esa frase.
> > - Esto te ayuda a revisar y editar de manera más eficiente, sin necesidad de contar manualmente.

---

### **Dataview**
> [!info]- **Descripción y Utilidad**
> **Dataview** es uno de los plugins más potentes y versátiles de Obsidian. No es solo un plugin, sino un motor de consultas que te permite tratar tus notas como si fueran una base de datos. Con Dataview, puedes crear vistas dinámicas de tus notas, organizándolas y filtrándolas según sus metadatos (etiquetas, propiedades de frontmatter, etc.). Es ideal para crear dashboards, listas de tareas de varios proyectos, resúmenes automáticos de notas o cualquier vista personalizada que necesites.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado. No requiere una configuración avanzada para el uso básico.
> 2.  **Sintaxis de Consulta**: Dataview utiliza una sintaxis de consulta propia que se escribe directamente en tus notas. Hay dos tipos principales de vistas: `list` y `table`.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Crear una tabla que muestre todas las notas que tienen la etiqueta `#proyecto` y su estado.
>
> **Tus notas:**
> ```markdown
> # Mi Proyecto de Desarrollo Web
> ---
> tags: [proyecto, webdev]
> estado: En progreso
> ---
> 
> # Ideas de Marketing
> ---
> tags: [brainstorming]
> estado: En espera
> ---
> 
> # Proyecto de Base de Datos
> ---
> tags: [proyecto, backend]
> estado: Terminado
> ```
> 
> **Tu consulta con Dataview:**
>
> ```markdown
> ```dataview
> TABLE estado
> FROM #proyecto
> ```
> ```
> 
> **El resultado será una tabla como esta:**
> 
> | File                 | estado      |
> |----------------------|-------------|
> | Mi Proyecto de...    | En progreso |
> | Proyecto de Base...  | Terminado   |
>
> > - El código `TABLE estado` le dice a Dataview que cree una tabla con una columna llamada "estado".
> > - La línea `FROM #proyecto` le indica que busque todas las notas que tengan la etiqueta `#proyecto`.
> > - De esta forma, puedes tener un resumen de todos tus proyectos en una sola nota, y se actualizará automáticamente cada vez que edites las notas.

---

### **Excalidraw**
> [!info]- **Descripción y Utilidad**
> **Excalidraw** integra una pizarra digital en Obsidian, permitiéndote crear diagramas, bocetos, mapas mentales y dibujos directamente dentro de tus notas. Es ideal para cuando necesitas un formato más visual para representar ideas, estructuras de datos, flujos de trabajo, o simplemente para hacer un brainstorming de forma libre. Las ventajas de Excalidraw son que puedes crear tus gráficos a mano alzada y que las notas que haces se pueden enlazar con otras notas de Obsidian.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado en la configuración de Obsidian.
> 2.  **Creación**: Hay dos formas principales de usarlo:
>     * Usa el atajo de teclado (`Ctrl + P` y busca "New Excalidraw drawing").
>     * Crea un archivo nuevo con la extensión `.excalidraw` (ej. `diagrama.excalidraw`).
> 3.  **Uso Básico**: Dentro del lienzo, tienes herramientas para dibujar, escribir texto, crear formas y dibujar a mano alzada.
> 4.  **Integración**: Puedes arrastrar y soltar notas de Obsidian en el lienzo de Excalidraw, lo que crea un enlace visual a esa nota. Esto es perfecto para el método Zettelkasten y para visualizar tus conexiones.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Crear un diagrama de flujo simple de tu método de estudio.
>
> 1.  Crea un nuevo dibujo de Excalidraw.
> 2.  Dibuja cajas y flechas para representar tu flujo de trabajo (ej. "Captura de idea" → "Procesamiento" → "Conexión").
> 3.  Arrastra y suelta tus notas relevantes de Obsidian en cada una de las cajas del diagrama para que puedas navegar fácilmente entre ellas.
> 4.  Esto te dará una vista general de tu sistema y cómo cada pieza se relaciona con las demás.

---

### **Kanban**
> [!info]- **Descripción y Utilidad**
> **Kanban** es un plugin que te permite crear tableros de gestión de proyectos y tareas directamente dentro de tus notas de Obsidian. Se basa en el método Kanban, que organiza el flujo de trabajo en columnas (ej. "Pendiente", "En progreso", "Terminado"). Es ideal para planificar proyectos, hacer seguimiento de tareas, gestionar un backlog de ideas o simplemente visualizar el estado de tu trabajo de forma clara y concisa.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado.
> 2.  **Creación**: Crea una nueva nota con la extensión `.md` y añade el siguiente código en la parte superior para indicar que es un tablero Kanban.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Organizar las tareas de un proyecto de estudio.
>
> **Tu tablero Kanban:**
>
> ```kanban
> ---
> kanban-plugin: basic
> ---
> 
> ## Pendiente
> - [ ] Leer capítulo 3 de "Automatización de Tareas"
> - [ ] Instalar plugin "Luhman"
> 
> ## En progreso
> - [ ] Escribir resumen de "Zettelkasten"
> 
> ## Terminado
> - [x] Crear nota "Plugins y Complementos"
> - [x] Configurar "Dataview"
> ```
>
> > - El código `kanban` en la parte superior le dice a Obsidian que renderice esta nota como un tablero.
> > - Cada encabezado `##` se convierte en una columna del tablero.
> > - Las listas de tareas (`- [ ]`) se convierten en tarjetas que puedes arrastrar y soltar entre las columnas.

---

### **Mehrmaid**
> [!info]- **Descripción y Utilidad**
> **Mehrmaid** es un plugin que mejora los diagramas de Mermaid al permitirte incluir sintaxis de Markdown dentro de ellos. Esto significa que puedes dar formato a los textos de tus nodos (como negritas, cursivas o enlaces) sin romper la estructura del diagrama. Es una herramienta poderosa para crear gráficos más detallados y visualmente atractivos en tus notas.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado en la configuración.
> 2.  **Uso Básico**: Dentro de un bloque de código Mermaid, usa los caracteres de Markdown que ya conoces para dar formato al texto de tus nodos.
> 3.  **Sintaxis**: Por ejemplo, para poner un texto en negrita, usa `**Texto en negrita**` dentro de un nodo.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Resaltar un nodo importante en un diagrama de flujo de estudio.
>
> **Tu diagrama de Mermaid con Mehrmaid:**
>
> ```mermaid
> graph TD
>    A[**Captura de Idea**] --> B[Procesamiento]
>    B --> C[***Conexión***]
> ```
>
> > - El nodo `A` aparecerá con el texto en **negrita**.
> > - El nodo `C` aparecerá con el texto en ***negrita y cursiva***, lo que lo hace destacar aún más.

---

### **Natural Language Dates**
> [!info]- **Descripción y Utilidad**
> Este plugin te permite crear enlaces a fechas de forma intuitiva, utilizando un lenguaje natural. En lugar de escribir el formato de fecha completo (ej. `YYYY-MM-DD`), puedes escribir frases como "mañana", "próximo lunes", o "en dos semanas" y el plugin las convierte automáticamente en un enlace a la nota diaria correspondiente. Es una herramienta de ahorro de tiempo fundamental para agilizar la creación de tareas, recordatorios y referencias a eventos futuros en tus notas.
>
> > [!tip]- **Integración Clave:** Este plugin es esencial para el plugin **Calendar** y **Review**, que ya tienes instalados. Por ejemplo, el plugin **Review** utiliza este plugin para entender cuándo programar la revisión de una nota.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado en la configuración.
> 2.  **Uso Básico**: Escribe el texto de una fecha de forma natural, por ejemplo: `[[tomorrow]]`.
> 3.  **Conversión**: Cuando guardas o sales de la nota, el plugin convierte automáticamente el texto en el formato de fecha que tengas configurado. Si tienes la configuración estándar, `[[tomorrow]]` se convertirá en `[[2025-08-12]]`.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Crear una tarea para el próximo viernes y un recordatorio para el próximo mes en una nota.
>
> **Tu nota:**
>
> ```markdown
> # Tareas importantes
> - [ ] Terminar de escribir el artículo [[next friday]]
> - [ ] Empezar a planificar el próximo proyecto [[in one month]]
> ```
>
> > - El plugin convertirá `[[next friday]]` y `[[in one month]]` en enlaces con el formato de fecha correspondiente (ej. `[[2025-08-15]]` y `[[2025-09-11]]`), lo que te permitirá hacer clic y saltar directamente a la nota de ese día.

---

### **Pandoc Plugin**
> [!info]- **Descripción y Utilidad**
> El **Pandoc Plugin** es una herramienta de exportación que te permite convertir tus notas de Obsidian en una gran variedad de formatos. Utiliza el conversor de documentos universal Pandoc, por lo que puedes transformar tus archivos de Markdown en documentos como PDF, DOCX, ePub o HTML, entre otros. Esto es extremadamente útil para generar informes, crear documentos finales para compartir con otras personas o simplemente para tener copias de seguridad en otros formatos.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado en la configuración.
> 2.  **Instalación de Pandoc**: Necesitas tener Pandoc instalado en tu sistema operativo, ya que el plugin actúa como una interfaz para este programa.
> 3.  **Uso Básico**: Abre la paleta de comandos (`Ctrl + P`) y busca "Pandoc". Verás opciones para exportar el documento actual a diferentes formatos.
> 4.  **Configuración Avanzada**: En la configuración del plugin, puedes personalizar la ruta de Pandoc, elegir el formato de salida predeterminado, y configurar plantillas y metadatos para tus exportaciones.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Exportar una nota de estudio completa a un documento de Word para imprimirla o enviarla.
>
> 1.  Abre la nota que quieres exportar.
> 2.  Abre la paleta de comandos (`Ctrl + P`).
> 3.  Escribe "Pandoc" y selecciona la opción "Export current file to docx".
> 4.  Se creará una copia de tu nota en formato `.docx` en la misma carpeta, lista para ser usada en Microsoft Word o Google Docs.

---

### **Periodic Notes**
> [!info]- **Descripción y Utilidad**
> **Periodic Notes** es un plugin que automatiza la creación y gestión de notas recurrentes. En lugar de solo tener notas diarias, puedes tener notas semanales, mensuales, trimestrales y anuales que se crean automáticamente. Es una herramienta poderosa para llevar un registro consistente de tus actividades, proyectos y reflexiones a largo plazo. Es ideal para la revisión semanal, la planificación mensual o para registrar tus metas anuales de forma estructurada.
>
> > [!tip]- **Integración Clave:** Este plugin funciona de la mano con **Calendar**. Por ejemplo, al hacer clic en un día en el calendario, se abrirá la nota diaria, pero al hacer clic en la semana o el mes, abrirá la nota periódica correspondiente.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado en la configuración.
> 2.  **Configuración**: Dentro de la configuración del plugin, puedes definir el formato de fecha para cada tipo de nota (diaria, semanal, etc.) y la carpeta donde se guardarán. Por ejemplo, puedes configurar que tus notas semanales se guarden en una carpeta llamada `03 - Revisiones/Semanales`.
> 3.  **Uso Básico**: Puedes usar la paleta de comandos (`Ctrl + P`) para crear rápidamente una nota diaria, semanal o mensual.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Tener un formato consistente para tus revisiones semanales.
>
> 4.  Ve a la configuración del plugin **Periodic Notes**.
> 5.  En la sección de "Weekly Notes", activa la opción y configura la ruta y el formato.
> 6.  En una nota, usa el siguiente código para crear un enlace a tu nota semanal: `[[{{date:YYYY-MM}}-W{{date:ww}}]]`. Esto creará un enlace a una nota como `2024-08-W32`.
> 7.  Al hacer clic, se abrirá una nota semanal donde puedes hacer un resumen de tus logros, desafíos y planes para la siguiente semana.

---

### **Quiet Outline**
> [!info]- **Descripción y Utilidad**
> **Quiet Outline** es un plugin que mejora el panel de esquema (outline) nativo de Obsidian. Su principal utilidad es hacer que el esquema sea más poderoso y discreto. Evita que el panel se expanda automáticamente, lo que es muy útil en notas largas con muchos encabezados. Además, permite que los títulos se rendericen con formato Markdown y añade soporte para búsquedas dentro del propio esquema, facilitando la navegación en notas extensas.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado en la configuración.
> 2.  **Uso Básico**: Abre el panel del esquema. Notarás que no se expande automáticamente, y puedes buscar un encabezado específico directamente en la barra de búsqueda del panel.
> 3.  **Configuración**: En los ajustes del plugin, puedes configurar si deseas que los encabezados se rendericen como Markdown, y ajustar otros detalles de la interfaz para que se adapte a tu preferencia.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Navegar de forma eficiente en una nota de estudio larga.
>
> **Tu nota:**
>
> ```markdown
> # Mi Guía de Automatización
> 
> ## ⚙️ Fundamentos de la Automatización
> 
> ### Tipos de Automatización
> 
> ### Regla 3-2-1
> 
> ## 🛠️ Herramientas y Plataformas
> 
> ### Zapier
> 
> ### Python y APIs
> 
> ```
>
> > - Con el plugin **Quiet Outline**, el panel del esquema mostrará la jerarquía de los encabezados sin estar expandido por defecto.
> > - Si buscas "Herramientas" en la barra de búsqueda del esquema, el plugin filtrará la vista para mostrarte solo los encabezados relevantes, permitiéndote saltar directamente a la sección que necesitas.

---

### **Review**
> [!info]- **Descripción y Utilidad**
> **Review** es un plugin que te ayuda a implementar el sistema de **repetición espaciada**. En lugar de revisar tus notas de forma aleatoria, te permite programar la revisión de una nota para una fecha futura. Esto es ideal para memorizar conceptos, repasar información clave y asegurarte de que la información se retenga a largo plazo. Es un aliado perfecto para estudiantes y para quienes usan el método Zettelkasten.
>
> > [!tip]- **Integración Clave:** Este plugin requiere el plugin **Natural Language Dates** para funcionar, ya que utiliza su sintaxis para entender la fecha de revisión que le indiques.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado.
> 2.  **Uso Básico**: Abre la paleta de comandos (`Ctrl + P`), busca "Review: Review this note on a date".
> 3.  **Programación**: El plugin te preguntará por una fecha. Puedes usar lenguaje natural (ej. "en 3 días", "próxima semana") o una fecha específica.
> 4.  **Funcionamiento**: El plugin añadirá un enlace a la nota actual en la nota diaria correspondiente a la fecha que programaste, bajo un encabezado específico que puedes configurar.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Programar la revisión de tu nota sobre "Zettelkasten" para dentro de una semana.
>
> 1.  Abre tu nota "Zettelkasten".
> 2.  Abre la paleta de comandos (`Ctrl + P`) y selecciona la opción "Review this note on a date".
> 3.  Escribe "en 1 semana" y presiona `Enter`.
> 4.  El plugin creará un enlace a tu nota de "Zettelkasten" en la nota diaria que corresponde a la fecha de la próxima semana, recordándote que es momento de repasar el tema.

---

### **Settings Search**
> [!info]- **Descripción y Utilidad**
> **Settings Search** es un plugin muy sencillo pero increíblemente útil. Su única función es añadir una barra de búsqueda global a la configuración de Obsidian. Conforme tu lista de plugins y opciones de configuración crece, puede ser difícil encontrar la configuración específica que buscas. Este plugin resuelve ese problema, permitiéndote encontrar cualquier ajuste de forma instantánea.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado.
> 2.  **Uso Básico**: Ve a la configuración de Obsidian. En la parte superior, verás una nueva barra de búsqueda.
> 3.  **Búsqueda**: Escribe el nombre del plugin o de la opción de configuración que quieres encontrar (ej. "temas", "dataview", "plantillas"). Los resultados se filtrarán en tiempo real.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Encontrar la configuración de tu plugin **Periodic Notes** de forma rápida.
>
> 4.  Abre la configuración de Obsidian (`Ctrl + ,`).
> 5.  En la barra de búsqueda de la parte superior, escribe "Periodic Notes".
> 6.  La lista de plugins se filtrará automáticamente para mostrarte solo el plugin **Periodic Notes**, lo que te permitirá acceder a sus ajustes de inmediato sin tener que desplazarte por toda la lista.

---

### **Tag Wrangler**
> [!info]- **Descripción y Utilidad**
> **Tag Wrangler** es un plugin que te da un control total sobre las etiquetas (`#etiquetas`) en tu vault de Obsidian. Sus funciones principales son: **renombrar**, **combinar**, y **eliminar** etiquetas de forma masiva en todos tus archivos. Es una herramienta esencial para mantener tu sistema de notas limpio y organizado, evitando la duplicación de etiquetas y corrigiendo errores tipográficos en un solo lugar.
>
> > [!tip]- **Control Total:** Al renombrar una etiqueta con este plugin, se actualizará automáticamente en **todas las notas** donde la hayas usado, lo que te ahorra la tarea manual de buscar y reemplazar.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado.
> 2.  **Uso Básico**: En la barra lateral derecha, ve al panel de etiquetas.
> 3.  **Renombrar**: Haz clic derecho en una etiqueta y selecciona la opción "Rename tag". Escribe el nuevo nombre y el plugin se encargará de actualizarla en todas tus notas.
> 4.  **Combinar**: Si tienes dos etiquetas similares (ej. `#proyecto-web` y `#proyectos-web`), haz clic derecho en una de ellas y selecciona "Merge with...". Luego, elige la otra etiqueta con la que quieras combinarla.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Corregir una etiqueta mal escrita en tu vault.
>
> 1.  Te das cuenta de que has usado la etiqueta `#proyect` en algunas notas en lugar de `#proyecto`.
> 2.  Abre el panel de etiquetas en Obsidian.
> 3.  Busca la etiqueta `#proyect`, haz clic derecho sobre ella y selecciona "Rename tag".
> 4.  Escribe `#proyecto` y presiona `Enter`.
> 5.  El plugin buscará todas las notas con `#proyect` y las actualizará a `#proyecto` de forma automática, manteniendo la coherencia en tus etiquetas.

---

### **Templater**
> [!info]- **Descripción y Utilidad**
> **Templater** es uno de los plugins más poderosos para la automatización en Obsidian. Te permite crear plantillas dinámicas que puedes insertar en tus notas con un atajo de teclado o un comando. Estas plantillas pueden contener variables, funciones y código JavaScript para insertar de forma automática la fecha, la hora, el título de la nota, y mucho más. Es la herramienta clave para crear formatos consistentes en tus notas diarias, plantillas de proyectos, o notas permanentes para el método Zettelkasten.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado.
> 2.  **Configuración**: En los ajustes del plugin, debes especificar la carpeta donde se guardan tus plantillas (ej. `00 - Plantillas/`).
> 3.  **Creación de Plantilla**: En la carpeta de plantillas, crea un archivo (`Plantilla_Diaria.md`) con el contenido dinámico que necesites. Por ejemplo, `--- fecha: {{date}} --- # Notas del día`.
> 4.  **Uso Básico**: Para insertar la plantilla, abre la paleta de comandos (`Ctrl + P`) y busca "Templater: Insert template". O usa el atajo de teclado por defecto (`Ctrl + Shift + E`).

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Crear una plantilla para tus notas de proyectos que incluya la fecha de creación y un estado inicial.
>
> 1.  Crea un archivo llamado `Plantilla_Proyecto.md` en tu carpeta de plantillas con el siguiente contenido:
> 
>     ```markdown
>     ---
>     fecha_creacion: <% tp.date.now("YYYY-MM-DD") %>
>     estado: "En progreso"
>     ---
>     # Proyecto: <% tp.file.title %>
>     
>     ## Tareas
>     - [ ] 
>     
>     ## Notas
>     
>     ```
>
> 2.  Cuando crees una nueva nota para un proyecto (ej. "Proyecto de App Móvil"), inserta esta plantilla.
> 3.  El plugin llenará automáticamente la fecha y el título, dándote un formato consistente para cada uno de tus proyectos.

---

### **Dataview**
> [!info]- **Descripción y Utilidad**
> **Dataview** es uno de los plugins más potentes y versátiles de Obsidian. No es solo un plugin, sino un motor de consultas que te permite tratar tus notas como si fueran una base de datos. Con Dataview, puedes crear vistas dinámicas de tus notas, organizándolas y filtrándolas según sus metadatos (etiquetas, propiedades de frontmatter, etc.). Es ideal para crear dashboards, listas de tareas de varios proyectos, resúmenes automáticos de notas o cualquier vista personalizada que necesites.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado. No requiere una configuración avanzada para el uso básico.
> 2.  **Sintaxis de Consulta**: Dataview utiliza una sintaxis de consulta propia que se escribe directamente en tus notas. Hay dos tipos principales de vistas: `list` y `table`.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Crear una tabla que muestre todas las notas que tienen la etiqueta `#proyecto` y su estado.
>
> **Tus notas:**
> ```markdown
> # Mi Proyecto de Desarrollo Web
> ---
> tags: [proyecto, webdev]
> estado: En progreso
> ---
> 
> # Ideas de Marketing
> ---
> tags: [brainstorming]
> estado: En espera
> ---
> 
> # Proyecto de Base de Datos
> ---
> tags: [proyecto, backend]
> estado: Terminado
> ```
> 
> **Tu consulta con Dataview:**
>
> ```markdown
> ```dataview
> TABLE estado
> FROM #proyecto
> ```
> ```
> 
> **El resultado será una tabla como esta:**
> 
> | File                 | estado      |
> |----------------------|-------------|
> | Mi Proyecto de...    | En progreso |
> | Proyecto de Base...  | Terminado   |
>
> > - El código `TABLE estado` le dice a Dataview que cree una tabla con una columna llamada "estado".
> > - La línea `FROM #proyecto` le indica que busque todas las notas que tengan la etiqueta `#proyecto`.
> > - De esta forma, puedes tener un resumen de todos tus proyectos en una sola nota, y se actualizará automáticamente cada vez que edites las notas.

---

### **ZettelFlow**
> [!info]- **Descripción y Utilidad**
> **ZettelFlow** es un plugin diseñado para ayudarte a crear y gestionar tus notas al estilo **Zettelkasten** usando el lienzo (Canvas) de Obsidian. Te permite diseñar flujos de trabajo personalizados que se adaptan a tu forma de pensar, lo que hace que el proceso de creación de notas permanentes sea más intuitivo y visual. Con ZettelFlow, no solo escribes notas, sino que también visualizas cómo tus ideas se conectan y progresan.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado en la configuración de Obsidian.
> 2.  **Configuración del Flujo**: En los ajustes del plugin, puedes definir tus propios "flujos". Un flujo es una serie de pasos que sigues para crear una nota, por ejemplo: `Idea` -> `Captura` -> `Procesamiento` -> `Conexión`.
> 3.  **Uso Básico**: Para crear una nueva nota con un flujo, usa la paleta de comandos (`Ctrl + P`) y busca "ZettelFlow: Create new Zettel". El plugin te guiará a través de los pasos que has configurado.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Crear una nota permanente a partir de una idea rápida, asegurando que se enlace con otras notas.
>
> 4.  Configura un flujo en ZettelFlow con los siguientes pasos:
> 
>     - **1. Captura de Idea**: Crea una nota con la idea principal.
>     - **2. Desarrollo**: Escribe la idea con tus propias palabras.
>     - **3. Enlace**: Busca notas relacionadas y crea enlaces.
>     - **4. Tags**: Añade etiquetas relevantes.
> 
> 5.  Cuando tengas una nueva idea, inicia el flujo con el comando "ZettelFlow: Create new Zettel".
> 6.  El plugin te guiará por cada uno de los pasos, asegurando que no te saltes ninguno y que tu nueva nota permanente esté bien estructurada y conectada con tu base de conocimiento.

---

### **Luhman**
> [!info]- **Descripción y Utilidad**
> El plugin **Luhman** está diseñado para ayudarte a implementar el método Zettelkasten de la forma más purista posible. Su principal utilidad es generar identificadores únicos (IDs) para tus notas, siguiendo el sistema de Luhmann. Cada nota tiene un ID que no solo la hace única, sino que también indica su posición en la estructura del conocimiento. Esto te permite construir una red de ideas que es tanto jerárquica como interconectada.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado en la configuración.
> 2.  **Configuración**: Dentro de los ajustes de Luhman, puedes definir la longitud del ID y el formato que prefieras (ej. números, letras, o una combinación).
> 3.  **Uso Básico**: Para crear una nota con un ID, abre la paleta de comandos (`Ctrl + P`) y busca "Luhman: Create new Zettel with ID". El plugin generará un ID único y creará la nota con ese nombre de archivo.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Crear una nota sobre el método Zettelkasten y una nota de seguimiento que se conecte con ella.
>
> 4.  Crea una nota con el ID `01` y el título `Zettelkasten`.
> 5.  Crea una segunda nota sobre "Notas Atómicas" con el ID `01a`. Este ID indica que esta nota es una continuación o un concepto secundario de la nota principal `01`.
> 6.  Dentro de la nota `01a`, puedes enlazar de nuevo a la nota principal con un enlace simple `[[01 - Zettelkasten]]`.
> 7.  Esto crea una estructura donde sabes que la nota `01a` está directamente relacionada con la nota `01` en tu jerarquía de conocimiento.

---

### **Text expand**
> [!info]- **Descripción y Utilidad**
> **Text expand** es un plugin muy sencillo y práctico que te permite crear abreviaciones de texto que se expanden automáticamente. Por ejemplo, puedes configurar que al escribir `[[dt` se expanda a `[[{{date}}]]`. Es ideal para insertar frases, nombres, fechas o cualquier fragmento de texto que uses con frecuencia. Esto te ayuda a acelerar la escritura y a mantener la consistencia en tus notas.

> [!success]- **Cómo Configurar y Usar**
>
> 1.  **Activación**: Asegúrate de que el plugin esté activado en la configuración.
> 2.  **Creación de Abreviaciones**: Dentro de la configuración del plugin, puedes definir tus propias abreviaciones y el texto completo al que quieres que se expandan.
> 3.  **Uso Básico**: En cualquier nota, escribe la abreviación que configuraste. El plugin detectará el texto y lo reemplazará por la frase o el fragmento de texto completo.

> [!example]- **Ejemplo Práctico de Uso**
> **Objetivo:** Crear una abreviación para insertar un formato de nota bibliográfica que uses a menudo.
>
> 4.  Ve a la configuración de **Text expand** y añade una nueva abreviación.
> 5.  **Abreviación**: `[[bib`
> 6.  **Texto completo**:
> 
>     ```markdown
>     # [[Título del Libro]]
>     **Autor:** >     **Fecha de Lectura:** >     **Notas Clave:**
>     - 
>     ```
>
> 7.  Cuando estés creando una nueva nota, simplemente escribe `[[bib` y el plugin insertará automáticamente todo el formato de la plantilla, listo para que lo rellenes.

---

