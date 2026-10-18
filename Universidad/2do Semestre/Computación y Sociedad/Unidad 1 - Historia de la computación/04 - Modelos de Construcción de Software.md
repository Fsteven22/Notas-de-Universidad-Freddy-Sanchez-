---
dg-publish: true
---

# 🏗️ Modelos de Construcción de Software

## 🎯 Introducción

> [!info] 💡 ¿Cómo se construye el software de forma organizada?
>
> Desarrollar software no es simplemente escribir código. Requiere planificación, análisis, diseño, pruebas y mantenimiento. Los **modelos de construcción de software** son marcos de trabajo que definen cómo organizar estas etapas para producir software de calidad de forma predecible.
>
> ![[Diagramas/04_-_Modelos_de_Construcción_de_Software_01.svg]]

---

## 🌊 Modelo Cascada

> [!note] 🌊 El modelo clásico secuencial
>
> El **Modelo Cascada** es el más antiguo y tradicional. Las fases se ejecutan de forma **secuencial y lineal**: cada etapa debe completarse antes de pasar a la siguiente, como el agua cayendo en cascada.
>
> ![[Diagramas/04_-_Modelos_de_Construcción_de_Software_02.svg]]
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

> [!note] 🌀 Iterativo con análisis de riesgos
>
> El **Modelo Espiral** combina elementos del modelo cascada con la naturaleza iterativa del prototipado. Cada vuelta de la espiral representa una fase del proyecto, con especial énfasis en el **análisis de riesgos** en cada iteración.
>
> ![[Diagramas/04_-_Modelos_de_Construcción_de_Software_03.svg]]
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

> [!note] 📈 Entrega por partes funcionales
>
> El **Modelo Incremental** divide el desarrollo en **incrementos**, cada uno de los cuales añade funcionalidad al sistema. El cliente recibe versiones parciales del producto que ya son funcionales y usables.
>
> ![[Diagramas/04_-_Modelos_de_Construcción_de_Software_04.svg]]
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

> [!important] 🔄 Iterativo, colaborativo y adaptable
>
> **SCRUM** es el marco de trabajo ágil más popular. Organiza el desarrollo en ciclos cortos llamados **sprints** (generalmente de 2 a 4 semanas), al final de los cuales se entrega un incremento funcional del producto.
>
> ![[Diagramas/04_-_Modelos_de_Construcción_de_Software_05.svg]]
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

> [!note] 📐 Definición formal de Software
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

> [!summary] 📊 ¿Cuándo usar cada modelo?
>
> | Modelo | Requisitos | Riesgo | Participación del cliente | Ideal para |
> |---|---|---|---|---|
> | **Cascada** | Estables y bien definidos | Bajo | Al inicio y al final | Proyectos simples y predecibles |
> | **Espiral** | Cambiantes o inciertos | Alto | En cada iteración | Proyectos grandes y complejos |
> | **Incremental** | Parcialmente definidos | Medio | En cada entrega | Proyectos con entregas parciales |
> | **SCRUM** | Evolutivos y cambiantes | Variable | Continua | Proyectos de software modernos |

---

**Tags:** #software #modelos #cascada #espiral #incremental #scrum #ágil #desarrollo #unidad1 #EYAG1037