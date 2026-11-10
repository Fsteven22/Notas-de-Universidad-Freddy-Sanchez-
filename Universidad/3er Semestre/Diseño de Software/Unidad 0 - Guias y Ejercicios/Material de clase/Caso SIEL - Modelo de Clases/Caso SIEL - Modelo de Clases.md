---
dg-publish: true
tags: [CCPG1042, unidad2, siel, modelo-de-clases]
---

# 🏛️ Caso SIEL — Modelo de Clases: lo necesario y nada más (capturas)

> [!info] ℹ️ Qué es esto
>
> Transcripción completa de las 8 capturas del deck de **Modelo de Clases**, segunda lección del caso **SIEL** (Sistema de Elecciones) para Control03. Fuentes: Stevens cap. 5 · Pressman & Maxim, Apéndice 1. Deck: *Bloque 2 · minutos 60 a 107*.
>
> El ejemplo resumido vive en [[03 - UML clases, objetos y relaciones]]; aquí queda el desarrollo completo con las capturas.

## 🧭 Portada — qué cubre

> [!note] 💡 Portada — qué cubre
>
> Bloque 2 · Modelado de clases en UML a partir del enunciado de SIEL:
> identificar clases (sustantivos), tarjetas CRC, atributos/operaciones y
> visibilidad, asociaciones y multiplicidades, agregación/composición/
> dependencia, notas y generalización.

> [!note] 🖼️ captura del deck — Portada — qué cubre
>
> ![[Modelo de clases.png]]
>
> **Se lee así:** la lámina es el filtro de entrada del bloque —"Identificar clases por sustantivos" (Stevens cap. 5)— con el método de tres pasos: **1** subrayar los sustantivos, **2** descartar los malos, **3** quedan las clases. La tabla da los seis criterios de descarte con su ejemplo del SIEL y el porqué: redundante ("elector" y "ciudadano"), vago ("información", "datos"), evento u operación ("día de la elección", "revisión"), atributo ("votos nulos", "lugar de votación"), metalenguaje ("sistema", "SIEL") y fuera de alcance ("campaña publicitaria"). Cierra con la pregunta típica de examen: "¿Cuál de estas NO sería una buena clase?".
>
> **Por qué importa:** fija el criterio con el que se filtra el enunciado antes de dibujar nada; de él dependen las tarjetas CRC y todas las clases que salen después. Ojo con el archivo: `Modelo de clases.png` guarda esta lámina de sustantivos, no la portadilla del bloque.
>
> **Ejemplo:** "votos nulos" se descarta por ser atributo y "día de la elección" por ser evento, aunque ambos aparezcan citados en el enunciado.

## 🔍 Identificar clases por sustantivos (Stevens cap. 5)

> [!note] 📖 Identificar clases por sustantivos (Stevens cap. 5)
>
> Flujo: **1 · Subraya los sustantivos → 2 · Descarta los malos → 3 · Quedan las clases**.
>
> **Se lee así:** la lámina de origen resume el método de Stevens cap. 5 en tres pasos —subrayar todos los sustantivos del enunciado, descartar los que no califican, quedarse con los que quedan— y da en tabla los seis criterios de descarte con su ejemplo del SIEL; la pregunta de examen que se repite es "¿Cuál de estas NO sería una buena clase?".
>
> **Por qué importa:** es el filtro de entrada del modelado: lo que no sobrevive a estos seis criterios nunca debe llegar al diagrama de clases, y el motivo del descarte es lo que se pregunta en el parcial.
>
> **Ejemplo:** "elector" y "ciudadano" se descartan por redundantes —nombran lo mismo, así que queda uno—, mientras que `Candidatura` o `Acta` sobreviven y pasan a tarjetas CRC.

> [!tip] 🧹 Filtro de descarte (Stevens cap. 5)
>
> | Se descarta si es… | Ejemplo en el SIEL | Por qué |
> |---|---|---|
> | **Redundante** | "elector" y "ciudadano" | Nombran lo mismo: queda uno |
> | **Vago** | "información", "datos" | No tiene límites claros |
> | **Evento u operación** | "día de la elección", "revisión" | Es algo que ocurre, no algo que perdura |
> | **Atributo** | "votos nulos", "lugar de votación" | Es un dato de otra clase |
> | **Metalenguaje** | "sistema", "SIEL" | Habla del modelo, no del dominio |
> | **Fuera de alcance** | "campaña publicitaria" | El sistema no la gestiona |

> [!warning] 🎯 Pregunta típica de examen
>
> "¿Cuál de estas NO sería una buena clase?"

> [!note] 🖼️ captura del deck — Identificar clases por sustantivos (Stevens cap. 5)
>
> ![[Modelo de clases-7.png]]
>
> **Se lee así:** es la portadilla del bloque: "BLOQUE 2 · MINUTOS 60 A 107 — Modelo de clases: lo necesario y nada más", con las dos fuentes que se citan en toda la sesión (Stevens cap. 5 · Pressman & Maxim, apéndice 1). No aporta notación: solo anuncia el alcance del bloque y dónde empieza.
>
> **Por qué importa:** es la lámina que ordena las siguientes: de ella se deduce que el bloque va de "sustantivos → clases → relaciones" y que cada tema se apoya en una fuente concreta. Ojo con el archivo: aunque esta portadilla es la que corresponde a la sección "Portada — qué cubre" de arriba, el archivo que ahí se ve (`Modelo de clases.png`) guarda en realidad la lámina del filtro de sustantivos.
>
> **Ejemplo:** el "minuto 60 a 107" es el tramo del video de clase que corresponde a este material de modelado de clases.

## ✅ Un buen modelo y las tarjetas CRC

> [!info] 💡 Un buen modelo y las tarjetas CRC
>
> **Un buen modelo de clases…**
>
> - ✔ **soporta los casos de uso**: cada paso tiene una clase que responde;
> - ✔ **refleja el dominio**: usa el vocabulario de los usuarios;
> - ✔ **modela lo necesario** y nada más.

> [!example] 🗂️ Tarjeta CRC de ejemplo — *Candidatura*
>
> | Candidatura — Tarjeta CRC |
> |---|
> | **Responsabilidades** |
> | · Conocer su dignidad y su organización |
> | · Conocer a sus candidatos |
> | · Saber si fue aprobada o rechazada |
> | · Informar su total de votos |
> | **Colaboradores** |
> | · Dignidad · OrganizacionPolitica · Candidato · Acta |

> [!tip] Validar con un escenario
>
> "El funcionario califica una candidatura". Recorre los pasos: ¿qué tarjeta
> sabe cada cosa? Si nadie responde, falta una responsabilidad o una clase.

> [!note] 🖼️ captura del deck — Un buen modelo y las tarjetas CRC
>
> ![[Modelo de clases-1.png]]
>
> **Se lee así:** la lámina muestra las tres condiciones de un buen modelo (soporta los casos de uso —cada paso tiene una clase que responde—, refleja el dominio usando el vocabulario de los usuarios, y modela lo necesario y nada más) junto a la tarjeta CRC de `Candidatura`: cuatro responsabilidades (conocer su dignidad y su organización, conocer a sus candidatos, saber si fue aprobada o rechazada, informar su total de votos) y cuatro colaboradores (`Dignidad`, `OrganizacionPolitica`, `Candidato`, `Acta`). Cierra con el método de validación: narrar el escenario "el funcionario califica una candidatura" y preguntar qué tarjeta sabe cada cosa.
>
> **Por qué importa:** la tarjeta CRC es el filtro que evita el modelo inflado: si nadie responde un paso del escenario, falta una responsabilidad o falta una clase, y eso se detecta antes de dibujar el diagrama.
>
> **Ejemplo:** al narrar "el funcionario califica una candidatura", `Candidatura` sabe si fue aprobada o rechazada y `Acta` aparece como colaboradora de los votos.

## 📦 Una clase: nombre, atributos y operaciones (Pressman Ap. 1)

> [!note] 💻 Código — Una clase: nombre, atributos y operaciones (Pressman Ap. 1)
>
> ```
> ┌──────────────────────────────────────────┐
> │               Candidatura                 │
> ├──────────────────────────────────────────┤
> │ - codigo: String                          │
> │ - estado: EstadoCalificacion              │
> │ # fechaInscripcion: Date                  │
> ├──────────────────────────────────────────┤
> │ + calificar(aprobada: Boolean)            │
> │ + totalVotos(): Integer                   │
> │ ~ validarRequisitos(): Boolean            │
> └──────────────────────────────────────────┘
> Compartimentos: nombre · atributos (visibilidad nombre: tipo) · operaciones
> ```

> [!note] 🔍 Visibilidad
>
> | Símbolo | Significa |
> |---|---|
> | `+` | Pública: cualquiera la usa |
> | `-` | Privada: solo la propia clase |
> | `#` | Protegida: la clase y sus subclases |
> | `~` | Paquete: clases del mismo paquete |

> [!note] Clase abstracta
>
> Su nombre va en **cursiva** (ej.: *Dignidad*).

> [!note] 🖼️ captura del deck — Una clase: nombre, atributos y operaciones (Pressman Ap. 1)
>
> ![[Modelo de clases-2.png]]
>
> **Se lee así:** la lámina dibuja una clase completa de UML con sus tres compartimentos: el nombre (`Candidatura`), los atributos con su visibilidad y tipo (`- codigo: String`, `- estado: EstadoCalificacion`, `# fechaInscripcion: Date`) y las operaciones (`+ calificar(aprobada: Boolean)`, `+ totalVotos(): Integer`, `~ validarRequisitos(): Boolean`). A la derecha está la tabla de los cuatro símbolos de visibilidad (`+` pública, `-` privada, `#` protegida, `~` paquete) y la regla de que la clase abstracta se escribe en cursiva.
>
> **Por qué importa:** la visibilidad decide qué se puede tocar desde fuera y qué queda encapsulado; sin ella el diagrama dice qué existe pero no qué es seguro usar, y el código sale abierto por los cuatro lados.
>
> **Ejemplo:** `totalVotos()` es pública porque cualquiera consulta el total, mientras que `codigo` y `estado` son privados para que solo la propia clase los cambie.

## 🔗 Asociaciones: nombre, multiplicidad y roles (Stevens cap. 5)

> [!note] 💻 Código — Asociaciones: nombre, multiplicidad y roles (Stevens cap. 5)
>
> ```
> OrganizacionPolitica 1 ── inscribe ── 0..* Candidatura
> (auspiciante)                      (candidaturas)
> ```

> [!note] 🔢 Glosario de multiplicidades
>
> | Multiplicidad | Significa |
> |---|---|
> | `1` | exactamente uno |
> | `0..1` | cero o uno |
> | `0..*` (o `*`) | cero o más |
> | `1..*` | uno o más |

> [!example] Se lee en ambos sentidos
>
> Una `OrganizacionPolitica` inscribe `0..*` candidaturas; **cada** `Candidatura`
> tiene exactamente `1` auspiciante.
>
> **Pregunta de chat:** ¿cómo se lee "un Cliente tiene 0..\* Reservas"?
> **Lectura:** un Cliente tiene cero o más Reservas — y cada Reserva pertenece
> a exactamente un Cliente.

> [!note] 🖼️ captura del deck — Asociaciones: nombre, multiplicidad y roles (Stevens cap. 5)
>
> ![[Modelo de clases-3.png]]
>
> **Se lee así:** la lámina muestra una asociación completa con sus tres piezas: nombre (`inscribe`), multiplicidad bilateral (`OrganizacionPolitica 1` — `Candidatura 0..*`) y roles (el que inscribe es `auspiciante`, lo que se inscribe son `candidaturas`). Junto a ella va el glosario de multiplicidades (exactamente uno, cero o uno, cero o más, uno o más) y la regla de leer en ambos sentidos: una organización política inscribe cero o más candidaturas, y cada candidatura tiene exactamente un auspiciante. Cierra con la pregunta para el chat: ¿cómo se lee "un Cliente tiene 0..* Reservas"?
>
> **Por qué importa:** nombre, roles y multiplicidad son la parte del diagrama que se malinterpreta más; sin la flecha de multiplicidad, el modelo deja de decir cuántos objetos hay de cada lado y el código generado inventa reglas que nadie pidió.
>
> **Ejemplo:** con `1` en el lado de la organización y `0..*` en el lado de las candidaturas, queda claro que una candidatura sin auspiciante no puede existir.

## 🧷 Agregación, composición, dependencia y notas (Pressman Ap. 1)

> [!info] 🧷 Notación de relación en el diagrama
>
> | Relación | Notación | Lectura en SIEL |
> |---|---|---|
> | **Agregación** | Rombo **vacío** en el todo (`Candidatura 1..2 ─◇─ Candidato`) | La parte existe sola: el candidato sigue existiendo si la candidatura se rechaza |
> | **Composición** | Rombo **lleno** en el todo (`Acta 1..* ─◆─ ConteoVotos`) | La parte muere con el todo: si se elimina el acta, sus conteos desaparecen |
> | **Dependencia** | Línea **punteada** con flecha y estereotipo (`ValidadorActa ⤳ "use" Padron`) | Una clase usa a otra de forma temporal |
> | **Nota** | Esquina **doblada** unida con línea punteada | ("Los votos nulos no suman a ninguna candidatura") — comentario sobre el elemento |

> [!note] 🖼️ captura del deck — Agregación, composición, dependencia y notas (Pressman Ap. 1)
>
> ![[Modelo de clases-4.png]]
>
> **Se lee así:** la lámina compara las cuatro notaciones de relación con su lectura en el SIEL: agregación con rombo **vacío** en el todo (la parte existe sola: el candidato sigue existiendo si la candidatura se rechaza), composición con rombo **lleno** (la parte muere con el todo: si se elimina el acta, sus conteos desaparecen), dependencia con línea punteada, flecha y estereotipo `«use»` (un uso temporal de una clase en otra) y nota con la esquina doblada unida por línea punteada (comentario sobre un elemento: "los votos nulos no suman a ninguna candidatura").
>
> **Por qué importa:** el rombo lleno y el rombo vacío se parecen pero significan cosas opuestas —ciclo de vida—; distinguirlos mal es el error que más cuesta en el diagrama de clases, porque después el código crea objetos huérfanos.
>
> **Ejemplo:** `Acta 1..* ─◆─ ConteoVotos` es composición: borrada el acta, se borran sus conteos; `Candidatura 1..2 ─◇─ Candidato` es agregación: rechazado el candidato, la candidatura sigue en pie.

## 🎲 Actividad 3 (individual · 7 min): Caza los sustantivos del SIEL

> [!note] 📋 Actividad 3 (individual · 7 min): Caza los sustantivos del SIEL
>
> 1. Relee el enunciado y anota **todos** los sustantivos.
> 2. Marca cada uno: **clase** o **descarte**, con el motivo.
> 3. Responde en el chat: **P1 _**, **P2 _**.

> [!question] Preguntas de la actividad (con respuesta sugerida)
>
> **P1 · ¿Cuál NO sería una buena clase?** a) Candidatura · b) VotosNulos ·
> c) Parroquia · d) OrganizacionPolitica
>
> **Respuesta sugerida: b) VotosNulos** — es un *atributo* ("votos nulos" es un
> dato de otra clase; además la nota del deck aclara: no suman a ninguna
> candidatura).
>
> **P2 · ¿Cuál NO sería una buena clase?** a) JRV · b) Acta ·
> c) DiaDeLaEleccion · d) Candidato
>
> **Respuesta sugerida: c) DiaDeLaEleccion** — es un *evento* ("es algo que
> ocurre, no algo que perdura").

> [!note] 🖼️ captura del deck — Actividad 3 (individual · 7 min): Caza los sustantivos del SIEL
>
> ![[Modelo de clases-5.png]]
>
> **Se lee así:** la lámina es la actividad 3 en versión en papel: tres pasos (releer el enunciado y anotar todos los sustantivos, marcar cada uno como clase o descarte con su motivo, responder en el chat las dos preguntas) y las dos preguntas de opción múltiple — P1: `Candidatura`, `VotosNulos`, `Parroquia`, `OrganizacionPolitica`; P2: `JRV`, `Acta`, `DiaDeLaEleccion`, `Candidato` — de las que hay que señalar cuál NO sería una buena clase.
>
> **Por qué importa:** es la práctica del filtro de la lámina anterior sobre el enunciado completo del SIEL, y a la vez el formato de pregunta que el docente replica en el examen; el motivo del descarte importa tanto como la respuesta.
>
> **Ejemplo:** `VotosNulos` es la opción de P1 que se descarta por ser un atributo, y `DiaDeLaEleccion` la de P2 por ser un evento.

## 🌿 Generalización: la relación "es un" (Stevens cap. 5 · Pressman Ap. 1)

> [!note] 💻 Código — Generalización: la relación "es un" (Stevens cap. 5 · Pressman Ap. 1)
>
> ```
>         ‹abstract› Dignidad            (nombre en cursiva = abstracta)
>                    △
>                    │
>             ┌──────┴──────┐
>         Alcaldia       Prefectura
> ```

> [!note] 💡 Generalización: la relación "es un" (Stevens cap. 5 · Pressman…
>
> - **"Es un"**: una Alcaldía **es una** Dignidad. Si la frase suena rara, no es
>   generalización.
> - **Herencia**: la subclase recibe atributos, operaciones y asociaciones de la
>   superclase.
> - **Sustituibilidad**: donde se espera una Dignidad, sirve una Alcaldía o una
>   Prefectura — una `Candidatura` apunta a `1` Dignidad, sea cual sea.
> - Triángulo hueco apuntando a la superclase.

> [!note] 🖼️ captura del deck — Generalización: la relación "es un" (Stevens cap. 5 · Pressman Ap. 1)
>
> ![[Modelo de clases-6.png]]
>
> **Se lee así:** la lámina cierra el bloque con la generalización: el triángulo hueco apunta a la superclase abstracta `Dignidad` (nombre en cursiva) y de ahí cuelgan `Alcaldía` y `Prefectura`. En texto define las tres palabras clave: "es un" (una Alcaldía **es una** Dignidad; si la frase suena rara, no es generalización), herencia (la subclase recibe atributos, operaciones y asociaciones de la superclase) y sustituibilidad (donde se espera una Dignidad sirve una Alcaldía o una Prefectura).
>
> **Por qué importa:** la sustituibilidad es la razón de ser de la generalización: permite que `Candidatura` se apunte a `1` Dignidad sin saber cuál es, y evita duplicar la misma asociación en cada subclase.
>
> **Ejemplo:** con el modelo generalizado, `Candidatura` relaciona con `1` Dignidad y da igual si ese objeto es una Alcaldía o una Prefectura.

---

> [!note] 📋 Generalización: la relación "es un" (Stevens cap. 5 · Pressman Ap. 1)
>
> - Mapa de contenido: [[../../../Diseño de Software|Diseño de Software]]
> - Complemento: [[Caso SIEL - Casos de Uso]]
> - Deck oficial de la cátedra: [[../../Diapositivas/04aLenguajeUnificadoModelado.pdf|04a Lenguaje unificado de modelado]] — explica la notación (elementos de clase, `+`/`#`/`-`, multiplicidad, clases de asociación, generalización) con el ejemplo de *AcademicChoice*; estas capturas son el caso **SIEL** aplicado.

**Tags:** #CCPG1042 #unidad2 #siel #modelo-de-clases
