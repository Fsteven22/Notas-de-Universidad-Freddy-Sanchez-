# 🏗️ Modelos de Construcción de Software

## 🎯 Introducción

> [!info]- 💡 ¿Cómo se construye el software de forma organizada?
>
> Desarrollar software no es simplemente escribir código. Requiere planificación, análisis, diseño, pruebas y mantenimiento. Los **modelos de construcción de software** son marcos de trabajo que definen cómo organizar estas etapas para producir software de calidad de forma predecible.
>
> ```mermaid
> graph TD
>     A[Necesidad del cliente] --> B{¿Qué modelo usar?}
>     B --> C[Cascada]
>     B --> D[Espiral]
>     B --> E[Incremental]
>     B --> F[Ágil / SCRUM]
>
>     style C fill:#e1f5ff
>     style D fill:#e1ffe1
>     style E fill:#fff4e1
>     style F fill:#f5e1ff
> ```

---

## 🌊 Modelo Cascada

> [!note]- 🌊 El modelo clásico secuencial
>
> El **Modelo Cascada** es el más antiguo y tradicional. Las fases se ejecutan de forma **secuencial y lineal**: cada etapa debe completarse antes de pasar a la siguiente, como el agua cayendo en cascada.
>
> ```mermaid
> graph TD
>     A[Requerimientos del Sistema] --> B[Requerimientos del Software]
>     B --> C[Diseño Preliminar y Detallado]
>     C --> D[Codificación y Depuración]
>     D --> E[Test y Pruebas]
>     E --> F[Operación y Mantenimiento]
>
>     style A fill:#e1f5ff
>     style B fill:#e1ffe1
>     style C fill:#fff4e1
>     style D fill:#f5e1ff
>     style E fill:#ffe1e1
>     style F fill:#e1ffe1
> ```
>
> ### Fases del modelo
>
> | Fase | Actividades principales |
> |---|---|
> | **Requerimientos del sistema** | Investigación inicial, identificación de necesidades, encuestas |
> | **Requerimientos del software** | Estudio de viabilidad, análisis, especificación |
> | **Diseño** | Especificación de diseño preliminar y detallado |
> | **Codificación** | Desarrollo y depuración del código, aplicación |
> | **Validación** | Test y pruebas previas a la operación |
> | **Operación y mantenimiento** | Instalación, explotación y soporte continuo |
>
> ### Ventajas y desventajas
>
> | ✅ Ventajas | ❌ Desventajas |
> |---|---|
> | Simple y fácil de entender | Rígido ante cambios de requisitos |
> | Fases bien definidas | El cliente no ve el producto hasta el final |
> | Buena documentación | Los errores se detectan tarde |
> | Ideal para proyectos con requisitos estables | No apto para proyectos complejos o cambiantes |

---

## 🌀 Modelo Espiral

> [!note]- 🌀 Iterativo con análisis de riesgos
>
> El **Modelo Espiral** combina elementos del modelo cascada con la naturaleza iterativa del prototipado. Cada vuelta de la espiral representa una fase del proyecto, con especial énfasis en el **análisis de riesgos** en cada iteración.
>
> ```mermaid
> graph TD
>     A[Determinación de<br/>Objetivos y Alternativas] --> B[Análisis de Riesgos<br/>y Evaluación]
>     B --> C[Desarrollo y<br/>Verificación del Producto]
>     C --> D[Planificación de<br/>la siguiente fase]
>     D --> A
>
>     style A fill:#e1f5ff
>     style B fill:#ffe1e1
>     style C fill:#e1ffe1
>     style D fill:#fff4e1
> ```
>
> ### Cuadrantes de cada iteración
>
> | Cuadrante | Actividad |
> |---|---|
> | **1 - Planificación** | Determinación de objetivos, alternativas y restricciones |
> | **2 - Análisis de riesgos** | Evaluación de alternativas, identificación y resolución de riesgos |
> | **3 - Desarrollo** | Desarrollo del producto del nivel actual: diseño, código, pruebas |
> | **4 - Revisión** | Planificación de la siguiente fase con el cliente |
>
> ### Ventajas y desventajas
>
> | ✅ Ventajas | ❌ Desventajas |
> |---|---|
> | Gestión explícita de riesgos | Complejo de gestionar |
> | Flexible ante cambios | Costoso en proyectos pequeños |
> | El cliente participa en cada vuelta | Requiere experiencia en análisis de riesgos |
> | Apto para proyectos grandes y complejos | Puede generar demasiada documentación |

---

## 📈 Modelo Incremental

> [!note]- 📈 Entrega por partes funcionales
>
> El **Modelo Incremental** divide el desarrollo en **incrementos**, cada uno de los cuales añade funcionalidad al sistema. El cliente recibe versiones parciales del producto que ya son funcionales y usables.
>
> ```mermaid
> graph LR
>     A[Incremento 1<br/>Funcionalidad básica] --> B[Entrega 1]
>     B --> C[Incremento 2<br/>+ Funcionalidades] --> D[Entrega 2]
>     D --> E[Incremento n<br/>Producto completo] --> F[Entrega final]
>
>     style A fill:#e1f5ff
>     style C fill:#e1ffe1
>     style E fill:#fff4e1
>     style B fill:#f5e1ff
>     style D fill:#f5e1ff
>     style F fill:#f5e1ff
> ```
>
> ### Fases de cada incremento
>
> | Fase | Descripción |
> |---|---|
> | **Comunicación** | Levantamiento de requisitos del incremento |
> | **Planeación** | Definición del alcance y recursos |
> | **Modelado** | Análisis y diseño de la funcionalidad |
> | **Construcción** | Código y pruebas |
> | **Despliegue** | Entrega y retroalimentación del cliente |
>
> ### Ventajas y desventajas
>
> | ✅ Ventajas | ❌ Desventajas |
> |---|---|
> | El cliente recibe valor desde el principio | Requiere buena planificación inicial |
> | Más flexible que cascada | Puede ser difícil integrar incrementos |
> | Errores se detectan pronto | La arquitectura puede degradarse con el tiempo |
> | Reduce el riesgo de fracaso total | No siempre claro cuándo termina el proyecto |

---

## 🔄 Desarrollo Ágil — SCRUM

> [!important]- 🔄 Iterativo, colaborativo y adaptable
>
> **SCRUM** es el marco de trabajo ágil más popular. Organiza el desarrollo en ciclos cortos llamados **sprints** (generalmente de 2 a 4 semanas), al final de los cuales se entrega un incremento funcional del producto.
>
> ```mermaid
> graph LR
>     A[INICIO<br/>Product Backlog] --> B[Sprint Planning]
>     B --> C[Sprint<br/>1-4 semanas]
>     C --> D{¿Aceptado?}
>     D -->|Sí| E[Puesta en<br/>producción]
>     D -->|No| F[Ajustes y<br/>reincorporación]
>     F --> B
>     C --> G[Revisión y<br/>Retrospectiva]
>     G --> B
>
>     style A fill:#fff4e1
>     style C fill:#e1ffe1
>     style D fill:#f5e1ff
>     style E fill:#e1f5ff
>     style F fill:#ffe1e1
> ```
>
> ### Roles en SCRUM
>
> | Rol | Responsabilidad |
> |---|---|
> | **Product Owner** | Define y prioriza el backlog del producto |
> | **Scrum Master** | Facilita el proceso y elimina impedimentos |
> | **Development Team** | Desarrolla el incremento en cada sprint |
>
> ### Eventos SCRUM
>
> | Evento | Propósito |
> |---|---|
> | **Sprint Planning** | Planificar el trabajo del sprint |
> | **Daily Scrum** | Sincronización diaria del equipo (15 min) |
> | **Sprint Review** | Demostrar el incremento al cliente |
> | **Sprint Retrospective** | Mejorar el proceso del equipo |
>
> ### Ventajas y desventajas
>
> | ✅ Ventajas | ❌ Desventajas |
> |---|---|
> | Alta adaptabilidad al cambio | Difícil de escalar en proyectos muy grandes |
> | Entregas frecuentes de valor | Requiere equipo comprometido y maduro |
> | Colaboración continua con el cliente | El alcance puede crecer sin control |
> | Detección temprana de problemas | No siempre hay documentación suficiente |

---

## 📐 ¿Qué es el Software según IEEE?

> [!note]- 📐 Definición formal de Software
>
> Según el **IEEE** (*Institute of Electrical and Electronics Engineers*),
> el software se denomina como:
>
> > *"La suma total de los programas de cómputo, procedimientos, reglas,
> > la documentación asociada y los datos que pertenecen a un sistema
> > de cómputo."*
>
> Esta definición es importante porque deja claro que el software no es
> solo el código ejecutable, sino también toda la documentación, los datos
> y los procedimientos que lo acompañan.
>
> | Componente | Descripción |
> |---|---|
> | **Programas** | Código ejecutable |
> | **Procedimientos** | Instrucciones de uso y operación |
> | **Reglas** | Normas que rigen el desarrollo y uso |
> | **Documentación** | Manuales, especificaciones, diagramas |
> | **Datos** | Información que el software procesa o almacena |

---

## 📊 Comparación General

> [!summary]- 📊 ¿Cuándo usar cada modelo?
>
> | Modelo | Requisitos | Riesgo | Participación del cliente | Ideal para |
> |---|---|---|---|---|
> | **Cascada** | Estables y bien definidos | Bajo | Al inicio y al final | Proyectos simples y predecibles |
> | **Espiral** | Cambiantes o inciertos | Alto | En cada iteración | Proyectos grandes y complejos |
> | **Incremental** | Parcialmente definidos | Medio | En cada entrega | Proyectos con entregas parciales |
> | **SCRUM** | Evolutivos y cambiantes | Variable | Continua | Proyectos de software modernos |

---

**Tags:** #software #modelos #cascada #espiral #incremental #scrum #ágil #desarrollo #unidad1 #EYAG1037