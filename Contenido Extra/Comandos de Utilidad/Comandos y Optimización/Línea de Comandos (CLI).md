# 💻 Línea de Comandos (CLI)

> [!quote] ⌨️ "La línea de comandos es el control remoto del ordenador. Es poderosa, rápida y te da el control total si sabes qué botones pulsar." - anónimo

---

> [!info]- ## 🖥️ Fundamentos: ¿Por qué usar la CLI?
> 
> ### ¿Qué es la Línea de Comandos?
> 
> La **línea de comandos (CLI)** es una interfaz basada en texto para interactuar con el sistema operativo. En lugar de usar el ratón y los iconos, escribes comandos para ejecutar tareas. Es la forma más poderosa y eficiente de trabajar, especialmente para tareas repetitivas y de administración.
> 
> ### Ventajas vs. Interfaz Gráfica (GUI)
> 
> |Característica|Línea de Comandos (CLI)|Interfaz Gráfica (GUI)|
> |---|---|---|
> |**Velocidad**|Muy rápida para usuarios experimentados.|Más lenta para tareas repetitivas.|
> |**Automatización**|Ideal para scripts y automatización de tareas.|Difícil o imposible de automatizar.|
> |**Recursos**|Muy bajo consumo de recursos.|Alto consumo de recursos.|
> |**Precisión**|Control total y preciso sobre el sistema.|Control limitado a lo que ofrece la interfaz.|
> |**Curva de Aprendizaje**|Más empinada, requiere memorizar comandos.|Muy baja, es intuitiva.|
> 
> ### El "prompt"
> 
> ```mermaid
> flowchart TD
>     A[Prompt] --> B{Comando};
>     B --> C[Argumento 1];
>     B --> D[Argumento 2];
>     C --> E[Bandera - Flag -a];
>     
>     style A fill:#E67E22,stroke:#A05616,stroke-width:2px,color:#fff
>     style B fill:#3498DB,stroke:#005193,stroke-width:2px,color:#fff
>     style C fill:#2ECC71,stroke:#009146,stroke-width:2px,color:#fff
>     style D fill:#2ECC71,stroke:#009146,stroke-width:2px,color:#fff
>     style E fill:#9B59B6,stroke:#643A7C,stroke-width:2px,color:#fff
> ```
> 
> > - **Comando:** La instrucción principal que quieres ejecutar (ej. `ls`).
> > - **Argumento:** La información sobre qué debe hacer el comando (ej. `ls /home`).
> > - **Bandera (Flag):** Modifica el comportamiento del comando (ej. `ls -a` para mostrar archivos ocultos).
> 
> ---
>
> [!success]- ## 🛠️ Comandos Esenciales para Empezar
> 
> ### Comandos de Navegación y Gestión de Archivos
> 
> |Comando|Descripción|Ejemplo|
> |---|---|---|
> |`ls` / `dir`|Lista los archivos y directorios.|`ls -l`|
> |`cd`|Cambia de directorio.|`cd /var/www`|
> |`pwd`|Muestra la ruta del directorio actual.|`pwd`|
> |`mkdir`|Crea un nuevo directorio.|`mkdir nuevo_proyecto`|
> |`touch`|Crea un archivo vacío.|`touch index.html`|
> |`rm` / `del`|Elimina un archivo o directorio.|`rm archivo.txt`|
> |`cp`|Copia archivos o directorios.|`cp archivo.txt /destino`|
> |`mv`|Mueve o renombra archivos.|`mv viejo.txt nuevo.txt`|
> 
> > [!example]- ### Caso de Uso: Preparar un Proyecto de Desarrollo Web
> > 
> > **Objetivo:** Crear la estructura básica de un proyecto en una carpeta llamada `mi-web`.
> > 
> > ```bash
> > # 1. Crear el directorio principal
> > mkdir mi-web
> > 
> > # 2. Moverse al nuevo directorio
> > cd mi-web
> > 
> > # 3. Crear los archivos base
> > touch index.html
> > touch styles.css
> > touch script.js
> > 
> > # 4. Crear una carpeta para las imágenes
> > mkdir assets
> > mkdir assets/images
> > 
> > # 5. Listar para verificar la estructura
> > ls -R
> > 
> > # Output:
> > # assets
> > # index.html
> > # script.js
> > # styles.css
> > 
> > # assets:
> > # images
> > ```
> 
> ---
>
> [!warning]- ## ⚠️ Mejores Prácticas y Riesgos
> 
> ### Consejos de Seguridad
> 
> - **Cuidado con `rm -rf`**: Es un comando muy destructivo. Elimina archivos de forma recursiva y forzada sin preguntar. Úsalo con extrema precaución.
> - **Entender el comando**: Antes de presionar "Enter", revisa el comando. Un pequeño error puede tener consecuencias graves, como eliminar datos importantes.
> - **Backups**: Siempre haz copias de seguridad de tus datos importantes antes de realizar operaciones destructivas en la CLI.
> 
> ### Atajos y Trucos Esenciales
> 
> |Atajo|Descripción|
> |---|---|
> |`Tab`|Autocompleta comandos y nombres de archivos.|
> |`↑` / `↓`|Navega por el historial de comandos.|
> |`Ctrl + C`|Cancela el comando en ejecución.|
> |`Ctrl + L`|Limpia la pantalla (lo mismo que `clear`).|
> |`Ctrl + R`|Busca en el historial de comandos.|
> 
> ---
>
> [!brain]- ## 🎯 Técnica de Estudio: El Método del "Hombre"
> 
> ### Aprende Usando el Manual Integrado
> 
> La mayoría de los sistemas basados en Unix (Linux, macOS) tienen un manual integrado al que puedes acceder directamente desde la terminal.
> 
> 1.  **Abre el Manual:** Escribe `man` seguido del comando que quieres aprender.
> 2.  **Lee la Descripción:** La primera sección explica qué hace el comando.
> 3.  **Explora las Banderas:** La sección de "OPTIONS" o "FLAGS" lista todas las opciones disponibles.
> 4.  **Ejemplos:** A menudo hay ejemplos al final.
> 
> Ejemplo: `man ls` te mostrará una descripción detallada del comando `ls` y sus opciones.
> 
> ```mermaid
> flowchart LR
>     A[man] --> B[ls]
>     A --> C[cd]
>     A --> D[cp]
> ```

---

> [!quote]- ## 📚 Referencias y Recursos
> 
> > [!quote] 📄 [Recursos sobre Git y GitHub]([[Git y GitHub]])
> > La línea de comandos es la herramienta principal para usar Git.
> 
> > [!quote] 🔗 [Guía de Desarrollo Web]([[Desarrollo Web]])
> > Muchos frameworks y herramientas de desarrollo web se gestionan a través de la CLI.
> 
> > [!quote] 🛠️ [Automatizaciones Digitales]([[Automatizaciones Digitales]])
> > Los scripts de la línea de comandos son la base de la automatización.
> 
> > [!quote] 🎨 [Python]([[Python]])
> > El lenguaje Python es ideal para crear scripts y herramientas de la línea de comandos.
> 
> ---
>
> [!link]- ## 🔗 Notas Recomendadas y Prerrequisitos
> 
> ### Prerrequisitos
> 
> - [[Módulo 4.1 Condicional]]
> - [[Sistemas Operativos]]
> 
> ### Notas Complementarias
> 
> - [[Automatización de Flujos de Trabajo]]
> 
> - [[Seguridad Digital Personal]]
> 
> ---
> 
> #cli #lineaDeComandos #terminal #bash #zsh #linux #comandos #productividad #desarrollo #devops
