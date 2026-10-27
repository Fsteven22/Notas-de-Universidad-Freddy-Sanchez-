---
dg-publish: true
tags: [IDIG2012, unidad3, ia-etica, prompts, redaccion]
---

# 🤖 IA Ética y Prompts para Redacción

## 🎯 Introducción

> [!info] 💡 ¿Por Qué la IA es Asistente y no Autora?
>
> La **IA optimiza** redacción, tiempos y automatización (sílabo 3.4), pero el criterio, la verificación y la firma son tuyos. En ESPOL el uso no declarado o sin verificar es deshonestidad académica: cero puntos.
>
> **Analogía del mundo real:** Piensa en un copiloto de código:
>
> - **Sin ética** → Aceptas el diff sin leer y rompes producción
> - **Con ética** → Revisas, testeas, atribuyes y firmas el commit
> - **Sin prompt** → "Hazme el informe" y recibes humo genérico
> - **Con prompt** → Rol + contexto + formato + fuentes y recibes borrador útil
>
> | Razón | Uso Ingenuo | Uso Ético Pro |
> |---|---|---|
> | **Calidad** | Genérico e inventa citas | Borrador verificable + APA real |
> | **Tiempo** | Reescribes todo igual | Ahorras 40% en estructura y estilo |
> | **Riesgo** | Plagio / datos falsos | Declarado y verificado |
> | **Evaluación** | Cero por deshonestidad | Participación 4 S6 a favor |

![[Diagramas/03_-_IA_ética_y_prompts_para_redacción_01.svg]]

---

## 🤖 Qué es la IA y Qué Herramientas Recomiendan

> [!info] 💡 Definición de la Cátedra (UNESCO, 2021)
>
> La IA son **sistemas capaces de replicar funciones de la inteligencia humana**: percepción, aprendizaje, razonamiento, resolución de problemas, comunicación y generación de contenido creativo.
>
> El objetivo instructional de la clase es concreto: **aplicar criterios éticos** al decidir si usarla en un trabajo académico, orientada al uso responsable de la tecnología.

> [!note] 🔧 IA Recomendadas en Comunicación
>
> | Para qué | Herramienta | Qué aporta | Advertencia de la cátedra |
> |---|---|---|---|
> | Parafrasear, corregir gramática, traducir | Asistente con IA conversacional | Trabaja en más de 30 idiomas | La extensión de Chrome y el detector de IA en versión gratuita **no son fiables** |
> | Buscar y responder preguntas | Asistente con búsqueda | 5 búsquedas gratis, se recargan cada 4 h | No confíes del todo en su **chequeo de plagio** |
> | Investigar artículos | **Scispace** | Asistente de investigación con Copilot sobre cada artículo | Las fuentes con las que interactúa son reales |
> | Resumir lo que ya leíste | **Explain Paper** | Subrayas y pide el resumen del fragmento | Trabaja en inglés (usa DeepL como traductor) |
> | Buscar más literatura | **Litmaps**, **Semantic Scholar**, bases del CIB | Mapas de literatura y repositorios | Revisa que el artículo exista antes de citarlo |
>
> **Regla práctica:** la IA te ahorra la *búsqueda*, no la *verificación*.

![[Diagramas/03_-_IA_ética_y_prompts_para_redacción_03.svg]]

---

## 🧵 Prompts que Sí Sirven (Actividad S6)

### 🎭 Estructura Completa: 6 Elementos + Verificación

> [!note] 🎨 Del Esqueleto RCFV a la Estructura de Cátedra
>
> El esqueleto **RCFV** (Rol, Contexto, Formato, Verificación) es el mínimo que ya usabas. La cátedra lo amplía a **6 elementos**, y la verificación queda como control posterior:
>
> | # | Elemento | Qué define | Qué pasa si falta | En RCFV |
> |---|---|---|---|---|
> | 1 | **La persona** | Desde qué rol responde el modelo | Tono de blog genérico | = Rol |
> | 2 | **La tarea** | Qué acción exacta se pide | Responde otra cosa | — |
> | 3 | **El contexto** | Para quién, con qué datos y para qué | Genérico, sin audiencia | = Contexto |
> | 4 | **El formato** | Cómo se entrega (lista, tabla, 400 palabras) | Bloque de texto corrido | = Formato |
> | 5 | **El tono** | Registro: formal, técnico, amigable | Registro inadecuado | — |
> | 6 | **El ejemplo** | Una muestra de lo que cuentas como buena respuesta | Formato impredecible | — |
> | + | **Verificación** | Qué fuente respalda qué afirmación | Citas inventadas | = Verificación |
>
> **Plantilla copiable para tus informes:**
>
> Persona: actúa como editor académico de ingeniería.
> Tarea: redacta un informe expositivo sobre [tema].
> Contexto: para [audiencia] en ESPOL, usando solo [pega tus 3 fuentes].
> Formato: intro 5 líneas + 3 hallazgos numerados + cierre con recomendación.
> Tono: formal y académico.
> Ejemplo: [pega un fragmento de tu borrador con el estilo esperado].
> Verificación: al final lista qué afirmación viene de qué fuente y marca [verificar] lo no respaldado.
>
> | Parte | Qué logra | Error común |
> |---|---|---|
> | **Persona / Rol** | Tono experto | Sin rol → tono blog |
> | **Tarea** | Encaja la respuesta con lo pedido | Sin verbo → respuesta difusa |
> | **Contexto** | Ajusta audiencia | Sin audiencia → genérico |
> | **Formato** | Estructura evaluable | Sin formato → bloque informe |
> | **Tono** | Registro adecuado al canal | Sin tono → registro plano |
> | **Ejemplo** | Calibra el estilo esperado | Sin ejemplo → inventa formato |
> | **Verificación** | Evita alucinaciones | Sin pedir fuentes → citas falsas |

![[Diagramas/03_-_IA_ética_y_prompts_para_redacción_04.svg]]

> [!tip] 💡 Seis Consejos de la Cátedra para un Buen Prompt
>
> 1. **Instrucciones claras y directas** — "haz esto" funciona mejor que "¿podrías hacerme?".
> 2. **Divide solicitudes complejas** — el modelo procesa mejor tareas separadas.
> 3. **Usa "debes" o "tu tarea es"** — transmite la importancia del requerimiento.
> 4. **Repite lo fundamental** — si es innegociable, ponlo dos veces en el prompt.
> 5. **Permite que pregunte** — si tiene dudas, que te pida información para afinar.
> 6. **Da un ejemplo** — muestra qué consideras una buena respuesta.

> [!example] 🧪 Prompt Completo Anotado (plantilla de la cátedra)
>
> > "Piensa como un asistente con 10 años de experiencia; organiza una reunión de dos horas para revisar proyectos, discutir desafíos y planificar nuevas iniciativas del servicio universitario. Incluye al director, responsables y técnicos. Crea una agenda profesional y clara con los temas, responsables y resultados esperados. Por ejemplo: 'Agenda: Reunión de Planificación del Servicio Universitario, duración: 2 horas, fecha: [Colocar fecha], lugar: Sala de Juntas, Edificio Central'."
>
> | Elemento | Dónde está en el prompt |
> |---|---|
> | **La persona** | "Piensa como un asistente con 10 años de experiencia" |
> | **La tarea** | "organiza una reunión de dos horas" |
> | **El contexto** | "revisar proyectos, discutir desafíos... incluye al director, responsables y técnicos" |
> | **El formato** | "una agenda profesional y clara con temas, responsables y resultados esperados" |
> | **El tono** | "profesional" |
> | **El ejemplo** | "Agenda: Reunión de Planificación del Servicio Universitario..." |

### 🔍 Ciclo de Verificación en 10 Minutos

> [!example] 🧪 Protocolo Participación 4 (S6, sincrónico TAF)
>
> 1. Genera borrador con RCFV (3 min)
> 2. Subraya cada dato numérico y busca su fuente real (4 min)
> 3. Elimina lo no respaldado o márcalo [verificar] (2 min)
> 4. Reescribe cierre con tus palabras + declara: "Borrador asistido con IA, verificado con [fuentes]"

---

## 🛡️ Ética y Políticas ESPOL

> [!success] 🏆 Reglas No Negociables
>
> - **Autoría:** toda idea ajena citada; plagio = 0 (Políticas 7.3).
> - **Declaración:** si usaste IA, dilo en el informe y en clase.
> - **Evidencia:** ninguna cita IA sin fuente primaria abierta.
> - **Datos:** no subas datos sensibles de terceros a herramientas públicas.
>
> Frase de declaración: "Se usó IA para estructura y estilo; el contenido
> fue verificado con [fuentes APA] y la redacción final es propia."

### 🤝 Protocolo de Uso Ético de la IA

> [!info] 💡 Por Qué Existe un Protocolo
>
> La ESPOL reconoce a la Inteligencia Artificial como **herramienta para mejorar la enseñanza**, siempre que se use de manera honesta y responsable. Este protocolo orienta el uso de la IA en la asignatura de Comunicación.
>
> **Analogía del mundo real:** es el equivalente a una autorización de uso de laboratorio:
>
> - **Sin protocolo** → entras, usas todo, respondes por los daños
> - **Con protocolo** → sabes qué puedes, qué debes declarar y qué no tocas
>
> | Razón | Sin protocolo | Con protocolo |
> |---|---|---|
> | **Autoría** | La IA firma tu trabajo | Tú firmas, la IA asiste |
> | **Confianza** | El docente desconfía | Transparentas el uso |
> | **Calidad** | Datos sin verificar | Datos con fuente comprobada |
>
> Elaborado por **Mariuxi León Molina, Ph.D.** para la asignatura IDIG2012.

![[Diagramas/03_-_IA_ética_y_prompts_para_redacción_05.svg]]

> [!success] 🏆 Me comprometo a
>
> 1. **Complementar** el pensamiento crítico, la creatividad y la integridad académica con la IA.
> 2. **Aprovechar con honestidad** los beneficios de la IA, siendo mi responsabilidad cerciorarme de ello.
> 3. **Usar debidamente** la IA, para evitar resultados dañinos, inequitativos, discriminatorios o peligrosos.
> 4. **Ejercer discreción** al utilizar plataformas de IA, teniendo en cuenta la ética de los datos que comparto y solicito.

> [!note] 📋 Para el efecto, me comprometo a
>
> **Verificar** la precisión y relevancia de la información otorgada por la IA, validándola con fuentes confiables.
>
> **Aportar** con mi pensamiento y conocimiento: la IA es una herramienta de apoyo y no realiza mi trabajo.
>
> **Monitorear** lo generado por la IA para garantizar la precisión de los datos y su alineación con las asignaciones académicas.
>
> **No depender** de sus resultados, ya que la IA puede contener un sesgo algorítmico.
>
> **Priorizar** la generación de confianza ante el docente y minimizar los errores que surjan al apoyarme en la IA.

### ✅ Usos Éticos de la IA en Comunicación

> [!tip] 🎯 Lo que sí se puede hacer
>
> | Categoría | Uso legítimo | Ejemplo en la carrera |
> |---|---|---|
> | **Inspiración** | Generar textos con enganche | Primera versión de una introducción que luego reescribes |
> | **Discurso** | Guía para la mejora del discurso | Revisar conectores y concisión de un párrafo |
> | **Idiomas** | Apoyo en la traducción | Leer una fuente en inglés que aún no dominas |
> | **Análisis** | Procesar productos textuales grandes | Extraer patrones de un corpus de mensajes |

![[Diagramas/03_-_IA_ética_y_prompts_para_redacción_07.svg]]

### 🎓 Qué Buscan los Profesores

> [!quote] 🌟 En otras palabras
>
> "Cuestionaré, compararé, contrastaré y mejoraré **toda** información que provenga de la IA."
>
> Eso es un flujo de 4 pasos antes de entregar cualquier tarea:
>
> | Paso | Pregunta que te haces | Acción concreta |
> |---|---|---|
> | **Cuestionar** | ¿Esto es cierto o es lo que el modelo quería que pareciera? | Contrasta con una fuente académica |
> | **Comparar** | ¿Lo dice otra fuente independiente? | Busca una segunda fuente en la biblioteca o CIB |
> | **Contrastar** | ¿Choca con mis datos o con el contexto? | Revisa que las cifras coincidan con tus fuentes |
> | **Mejorar** | ¿Mi versión final está mejor que el borrador? | Reescribe con tus palabras y tu criterio |

![[Diagramas/03_-_IA_ética_y_prompts_para_redacción_06.svg]]

### 🌱 Principio de Contribución Social

> [!info] 🌐 Alineación con la Materia
>
> Garantizaré que el uso de las herramientas de IA esté **alineado con los intereses de la materia** y con el esfuerzo que también requiere de mi parte.
>
> La meta última de mi aprendizaje y de mi institución es comprender la importancia de la **honestidad intelectual**, la **investigación rigurosa** y el **respeto por las contribuciones de otros**. La IA es una herramienta valiosa para este propósito, y debo utilizarla como parte de un enfoque integral que incluya educación, comunicación y principios sólidos.

### 🧾 Checklist Antes de Entregar

> [!danger] ❌ Errores que Costan la Evaluación
>
> - Usar IA sin declarar el uso → se trata como deshonestidad académica.
> - Aceptar citas, datos o referencias generadas sin abrir la fuente.
> - Entregar un texto con la voz del modelo en lugar de la tuya.
> - Subir datos sensibles de terceros a herramientas públicas.
> - Confiar en el detector de plagio o en el detector de IA de la extensión del navegador: la cátedra advierte que la versión gratuita no es fiable.

> [!tip] ✅ Checklist de 5 puntos
>
> 1. ¿Verifiqué cada dato con una fuente que abrí yo?
> 2. ¿Reescribí el cierre con mis palabras?
> 3. ¿Declaré el uso de IA con la frase acordada?
> 4. ¿Armé la referencia APA desde el PDF real, no desde el chat?
> 5. ¿Guardé el prompt usado, por si me lo piden?

---

## ⚠️ Problemas Comunes y Soluciones

> [!danger] ❌ Error: Citas APA Inventadas por la IA (viola **verificación de fuentes**)
>
> **Síntomas:** referencias con DOI falso o páginas que no existen.
>
> **Ejemplo completo:**
>
> - ❌ **EL ERROR ESTÁ AQUÍ:** bibliografía entregada con "Pérez, J. (2022). *Escucha y cerebro*. Revista NeuroCom, 4(2), 12-20. https://doi.org/10.xxxx/falso" — el DOI no resuelve y la revista no existe.
> - ✅ Así sí: pedir a la IA solo estructura y armar cada referencia desde el PDF real abierto, cruzando 1 búsqueda académica.
>
> **Solución:**
>
> - Pide a la IA solo estructura, nunca bibliografía final
> - Arma tu APA desde PDFs reales de Unidad 0 / biblioteca
> - Cruza con 1 búsqueda académica antes de entregar

---

## 🎯 Mejores Prácticas

> [!tip] 🏆 Checklist S6-S7
>
> **1. IA para estilo, tú para evidencia**
>
> IA: conectores, concisión, variantes de título.
> Tú: datos, citas, juicio y firma.
>
> **2. Guarda tus prompts**
>
> Anexa el prompt usado: muestra método y te defiende en revisión.
>
> **3. Conecta con PAC y Taller 3**
>
> Lo verificado hoy es lo que expones mañana sin leer diapositivas.

---

## 📊 Resumen Visual

![[Diagramas/03_-_IA_ética_y_prompts_para_redacción_02.svg]]

> [!success] 🔍 Comparación Final
>
> | Aspecto | Sin Método | Con 6 Elementos + Verificación |
> |---|---|---|
> | **Borrador** | ❌ Humo | ✅ Estructurado |
> | **Citas** | Inventadas | Reales APA |
> | **Uso Recomendado** | Nunca académico | ✅ **Estándar ético** |

---

## 🚀 Próximos Pasos

> [!quote] 🌟 Continuando
>
> **Has aprendido:**
>
> ✅ Estructura de 6 elementos (persona, tarea, contexto, formato, tono, ejemplo) + verificación
> ✅ Herramientas de IA para comunicación y sus límites
> ✅ Reglas éticas, declaración de uso y el protocolo ESPOL
> ✅ Antídoto contra citas inventadas
>
> **Siguiente lectura:**
>
> | Tema | Qué verás | Por qué importa |
> |---|---|---|
> | **Uso ético de la IA** | Compromisos firmados, usos lícitos y el flujo de questioning | Te lo piden en cada tarea con IA |

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Comunicación]]
> - Índice Unidad 3: [[00 - Índice Unidad 3]]
> - Anterior: [[02 - Informes técnicos y ejecutivos, síntesis y paráfrasis]]
> - Siguiente: [[04 - Precisión y claridad en la redacción]]
> - Protocolo institucional: [[../Unidad 0 - Guias y Ejercicios/Uso ético de la IA.pdf|PDF Uso ético de la IA]]
> - Syllabus: [[Bienvenida y Syllabus Comunicación]]
> - Base MOOC: [[Preuniversitario/MOOC de Comunicación/Comunicación Efectiva|MOOC de Comunicación]]
> - APA correcto al citar: [[06 - Normas APA, citación y referencias]]

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - Sílabo IDIG2012, Unidad 3.4: IA ética para redacción y automatización.
> - Planificación PAO 2-2026 S6: IA + prompts + Participación 4 (TAF).
> - **[1]** UNESCO, *IA y educación. Guía para políticas*, 2021.
> - **[2]** Políticas PAO 2-2026, §7.3: ética y deshonestidad académica.
> - **[3]** Universidad Pontificia Comillas, *Guía práctica de aplicación de la IA*, 2024.
> - **[4]** UNITEC, *200+1 prompts para educación: guía para docentes innovadores*, 2024.
> - PDF de clase (29 p.): [[../Unidad 0 - Guias y Ejercicios/Uso ético de la IA.pdf|Uso ético de herramientas de IA]] — D. Vega, A. Carranza y M. León.

---

**Tags:** #IDIG2012 #unidad3 #ia-etica #prompts #redaccion
