# 🛠️ Hardware

> [!quote] 🧠 "El software es lo que creas, el hardware es lo que puedes tocar y sentir." - anónimo

---

> [!info]  
> ## 📝 Fundamentos: ¿Qué es el Hardware?  
> El **Hardware** se refiere a todos los componentes físicos y tangibles de una computadora, desde los circuitos internos hasta los periféricos externos.  
> Es la base material sobre la cual se ejecuta el software. A diferencia de los programas que son intangibles, el hardware es la parte que podemos ver y tocar, y sin la cual ningún sistema informático podría funcionar.

---

> [!tip]  
> ## 📊 Componentes Principales  
> Los componentes se pueden dividir en dos categorías principales: internos y externos.
>
> [!tip]+ **Componentes Internos**  
> | Componente                  | Función Principal                                 |  
> | :------------------------- | :----------------------------------------------- |  
> | **CPU (Unidad Central de Procesamiento)** | El "cerebro" del ordenador. Ejecuta las instrucciones del software. |  
> | **RAM (Memoria de Acceso Aleatorio)**      | Memoria temporal para los programas que se están ejecutando.          |  
> | **Placa Madre (Motherboard)**               | El circuito principal que conecta todos los componentes.              |  
> | **Disco Duro (HDD/SSD)**                    | Almacenamiento permanente de datos, archivos y programas.             |  
> | **Tarjeta Gráfica (GPU)**                   | Procesamiento de gráficos y video para la visualización.              |
>
> [!tip]+ **Componentes Externos (Periféricos)**  
> | Componente                | Función Principal                    | Tipo                     |  
> | :----------------------- | :--------------------------------- | :----------------------- |  
> | **Teclado y Ratón**       | Entrada de datos e interacciones.  | Dispositivos de Entrada  |  
> | **Monitor**               | Muestra la interfaz gráfica y la información visual. | Dispositivos de Salida   |  
> | **Impresora**             | Convierte datos digitales en copias físicas. | Dispositivos de Salida   |  
> | **Auriculares y Micrófono** | Entrada y salida de audio.        | Dispositivos de Entrada/Salida |

---

> [!example]  
> ## 📈 Cómo se conectan los componentes  
> Todos los componentes internos se comunican a través de la placa madre, que es el centro nervioso de la computadora.

```mermaid
graph TD
    subgraph Placa Madre
        CPU[CPU] -- Conecta a --> RAM[Memoria RAM]
        CPU --> GPU[Tarjeta Gráfica]
        CPU --> HDD[Disco Duro]
        CPU --> USB[Puertos USB]
    end
    GPU --> Monitor[Monitor]
    USB --> Teclado[Teclado y Ratón]
    USB --> USB_2[Otros Periféricos]
````

---

> [!tip]
> 
> ## ✅ Técnica de Estudio
> 
> ### 🧠 Método de la Analogía
> 
> Utiliza analogías para recordar las funciones de los componentes. Por ejemplo:
> 
> - **CPU** es el cerebro que da las órdenes.
>     
> - **RAM** es el escritorio de trabajo, donde tienes los documentos que usas ahora.
>     
> - **Disco Duro** es el archivador, donde guardas todo permanentemente.
>     
> - **Placa Madre** es la red de carreteras que conecta todo.
>     
> 
> Esto te ayudará a asimilar y recordar cada componente de forma más intuitiva.

---

> [!link]
> 
> ## 📚 Referencias y Tags
>
> ### 🔗 Notas Relacionadas
> 
> - [[Sistemas Operativos]]
>     
> - [[Línea de Comandos (CLI)]]
>     
> - [[Gestión de Proyectos]]
>     
>
> ### 📚 Notas Complementarias
> 
> - [[Productividad Digital]]
>     
> - [[Conectando Notas en Obsidian]]
>     

---

#hardware #informatica #aprendizaje #tecnologia #componentes

