# ♿ Accesibilidad y WCAG

## 🎯 Introducción

> [!info]- 💡 ¿Qué es la Accesibilidad?
> 
> La **accesibilidad** es la posibilidad que tengan todas las personas _sin_ que medien **exclusiones de ningún tipo**, como ser culturales, físicas o técnicas, para acceder a un servicio o llegar a visitar un lugar o utilizar un objeto.
> 
> ```mermaid
> graph TD
>     A[Accesibilidad] --> B[Física]
>     A --> C[Digital / TIC]
>     B --> B1[Rampas para sillas de ruedas]
>     B --> B2[Baños adaptados]
>     C --> C1[WCAG]
>     C --> C2[Tecnologías de apoyo]
>     C2 --> D1[Teclados Braille]
>     C2 --> D2[Magnificadores de pantalla]
>     C2 --> D3[Conversores texto-voz]
>     C2 --> D4[Conversores voz-texto]
>     C2 --> D5[Pantallas adaptadas]
> 
>     style B fill:#e1f5ff
>     style C fill:#e1ffe1
>     style C2 fill:#fff4e1
> ```

---

## 📖 Tecnologías de Apoyo

> [!note]- 🖥️ Herramientas para personas con necesidades especiales
> 
> Aplicadas a tecnologías de la información:
> 
> |Tecnología|Descripción|
> |---|---|
> |**Teclados Braille**|Para personas con discapacidad visual|
> |**Magnificadores de pantalla**|Amplifican el contenido en pantalla|
> |**Asistentes personales**|Ayudan a operar el dispositivo por voz o gestos|
> |**Conversores texto a voz**|Leen en voz alta el contenido digital|
> |**Conversores voz a texto**|Dictan texto para personas con movilidad reducida|
> |**Pantallas adaptadas**|Interfaces ajustadas a distintas discapacidades|

---

## 📜 WCAG — Web Content Accessibility Guidelines

> [!note]- 📋 ¿Qué es WCAG?
> 
> Las **WCAG** (Web Content Accessibility Guidelines) son las directrices de accesibilidad para el contenido web del **W3C** (World Wide Web Consortium).
> 
> Establecen los **requisitos de accesibilidad que debe cumplir el contenido web** para que pueda ser utilizado por todas las personas, con o sin discapacidad, de forma autónoma o mediante productos de apoyo tecnológico.
> 
> 🔗 https://www.w3.org/TR/WCAG20/

> [!note]- 🏆 Niveles de conformidad WCAG
> 
> WCAG define tres niveles de conformidad que indican qué tan accesible es un sitio web:
> 
> |Nivel|Nombre|Significado|
> |---|---|---|
> |**A**|Mínimo|Requisitos básicos sin los cuales algunos usuarios no pueden acceder al contenido en absoluto|
> |**AA**|Intermedio|Elimina las barreras de acceso más significativas — es el nivel exigido por la mayoría de legislaciones, incluyendo Ecuador|
> |**AAA**|Óptimo|El mayor nivel de accesibilidad posible; no siempre es alcanzable para todo tipo de contenido|
> 
> > 💡 Un sitio que cumple nivel **AA** también cumple automáticamente el nivel **A**. Cada nivel es acumulativo.

> [!important]- 🧱 Los 4 Principios WCAG
> 
> Toda la estructura de WCAG se organiza bajo **4 principios fundamentales**. El contenido web debe ser:
> 
> ```mermaid
> graph TD
>     W["WCAG 2.0"] --> P1["1: Perceptible"]
>     W --> P2["2: Operable"]
>     W --> P3["3: Comprensible"]
>     W --> P4["4: Robusto"]
> 
>     P1 --> P1a["Alternativas de texto"]
>     P1 --> P1b["Contenido multimedia"]
>     P1 --> P1c["Adaptable"]
>     P1 --> P1d["Distinguible"]
> 
>     P2 --> P2a["Teclado accesible"]
>     P2 --> P2b["Tiempo suficiente"]
>     P2 --> P2c["Sin convulsiones"]
>     P2 --> P2d["Navegable"]
> 
>     P3 --> P3a["Legible"]
>     P3 --> P3b["Predecible"]
>     P3 --> P3c["Asistencia de entrada"]
> 
>     P4 --> P4a["Compatible"]
> 
>     style W fill:#e1f5ff
>     style P1 fill:#e1ffe1
>     style P2 fill:#fff4e1
>     style P3 fill:#ffe1f5
>     style P4 fill:#f5e1ff
> ```

> [!note]- 👁️ Principio 1 — Perceptible
> 
> La información y los componentes de la interfaz deben presentarse de forma que los usuarios puedan **percibirlos** — ningún contenido debe ser invisible para todos sus sentidos.
> 
> |Pauta|Descripción|
> |---|---|
> |**1.1 Alternativas de texto**|Todo contenido no textual (imágenes, íconos, gráficos) debe tener una alternativa en texto que describa su función o significado|
> |**1.2 Contenido multimedia**|El contenido de audio y video debe tener alternativas: **subtítulos** para el audio, **audiodescripción** para el video, y **transcripciones** para contenido solo-audio o solo-video|
> |**1.3 Adaptable**|El contenido debe poder presentarse de distintas formas (por ejemplo, con un lector de pantalla) sin perder información ni estructura|
> |**1.4 Distinguible**|Debe ser fácil ver y escuchar el contenido — contraste suficiente, texto redimensionable hasta el 200%, audio controlable|

> [!note]- ⌨️ Principio 2 — Operable
> 
> Los componentes de la interfaz y la navegación deben ser **operables** — los usuarios deben poder interactuar con la página.
> 
> |Pauta|Descripción|
> |---|---|
> |**2.1 Accesible por teclado**|Toda funcionalidad debe poder usarse con solo el teclado, sin requerir mouse — esencial para personas con discapacidad motriz|
> |**2.2 Tiempo suficiente**|Los usuarios deben tener tiempo suficiente para leer y usar el contenido; los límites de tiempo deben poder ajustarse o desactivarse|
> |**2.3 Sin convulsiones**|El contenido no debe destellar más de 3 veces por segundo, para evitar ataques en personas con epilepsia fotosensible|
> |**2.4 Navegable**|El sitio debe proporcionar formas de ayudar a los usuarios a navegar, encontrar contenido y saber dónde se encuentran (títulos de página, encabezados, foco visible)|

> [!note]- 💡 Principio 3 — Comprensible
> 
> La información y la operación de la interfaz deben ser **comprensibles** — los usuarios deben poder entender tanto el contenido como cómo funciona la página.
> 
> |Pauta|Descripción|
> |---|---|
> |**3.1 Legible**|El texto debe ser legible y comprensible — el idioma de la página debe estar identificado en el código para que los lectores de pantalla lo pronuncien correctamente|
> |**3.2 Predecible**|Las páginas deben aparecer y funcionar de manera predecible — sin cambios inesperados de contexto al recibir foco o al ingresar datos|
> |**3.3 Asistencia en la entrada**|Los formularios deben ayudar a los usuarios a evitar y corregir errores — con etiquetas claras, instrucciones y mensajes de error descriptivos|

> [!note]- 🔧 Principio 4 — Robusto
> 
> El contenido debe ser lo suficientemente **robusto** para ser interpretado de forma fiable por una amplia variedad de agentes de usuario, incluyendo tecnologías de apoyo.
> 
> |Pauta|Descripción|
> |---|---|
> |**4.1 Compatible**|El contenido debe maximizar la compatibilidad con navegadores y tecnologías de apoyo actuales y futuras — el código HTML debe ser válido y bien estructurado para que los lectores de pantalla puedan interpretarlo correctamente|

> [!note]- 📋 Criterios específicos del PDF (WCAG 2.0)
> 
> Estos son los criterios concretos mencionados en el material del curso — todos pertenecen al **Principio 1 (Perceptible)**:
> 
> |Criterio|Nivel|Descripción|
> |---|---|---|
> |**Solo audio / Solo video (pregrabado)**|A|El contenido de solo audio o solo video debe tener una alternativa textual equivalente, como una transcripción|
> |**Subtítulos (pregrabado)**|A|Todo audio sincronizado con video debe incluir subtítulos que describan el diálogo y los sonidos relevantes|
> |**Audiodescripción o alternativa textual (pregrabado)**|A|El video debe ofrecer audiodescripción o alternativa en texto que explique lo que ocurre visualmente|
> |**Cambio de tamaño de texto**|AA|El texto debe poder redimensionarse hasta el 200% sin perder contenido ni funcionalidad|
> |**Etiquetas e instrucciones**|A|Los formularios deben tener etiquetas claras para que los usuarios entiendan qué se espera que ingresen|

---

## 🇪🇨 Marco Legal en Ecuador

> [!warning]- ⚖️ Reglamento ecuatoriano de accesibilidad web
> 
> Ecuador adoptó las **Directrices de accesibilidad para el contenido web del W3C**.
> 
> El reglamento está **vigente desde el 8 de agosto de 2016** y establece:
> 
> - **8 de agosto de 2018** — Todos los sitios web ecuatorianos que presten un servicio público deben ser accesibles **WCAG 2.0 nivel A**
> - **8 de agosto de 2020** — Todos los sitios web ecuatorianos que presten un servicio público deben ser accesibles **WCAG 2.0 nivel AA**
> 
> 🔗 http://accesibilidadweb.dlsi.ua.es/?menu=ecuador

---

## ❓ Reflexión

> [!question]- 🤔 ¿Qué pasa con personas con necesidades especiales?
> 
> En el contexto digital, muchas personas quedan excluidas si los sistemas no están diseñados de forma accesible:
> 
> - Personas con discapacidad visual que no pueden leer pantallas sin lector
> - Personas con discapacidad motriz que no pueden usar un teclado convencional
> - Personas sordas que no pueden consumir contenido de audio sin subtítulos
> 
> La accesibilidad no es opcional — en Ecuador, **es un requisito legal** para servicios públicos digitales.

---

**Tags:** #computacion-y-sociedad #unidad2 #accesibilidad #WCAG #W3C #discapacidad #implicaciones-sociales #ESPOL