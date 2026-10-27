---
dg-publish: true
tags: [CCPG1042, unidad2, uml, clases, diseno-software]
---

# 📐 UML: Clases, Objetos y Relaciones

## 🎯 Introducción

> [!info] 💡 ¿Por Qué UML Sigue Vivo?
>
> **UML 2.0** es el idioma común para dibujar diseño: una caja significa lo mismo en ESPOL que en cualquier empresa. Sin él, cada diagrama inventa su notación y nadie se entiende — y el docente lo evalúa en S4 tal cual.
>
> **Importancia histórica:** UML nació en los 90 unificando los métodos rivales de Booch, Rumbaugh y Jacobson ("los tres amigos"). La versión 2.0 (Stevens) modernizó secuencias, máquinas de estado y componentes — lo que estudias es el estándar que sobrevivió 30 años.
>
> **Relevancia actual:** aunque el código se genera solo a veces desde UML, el diagrama sigue siendo el medio más denso para discutir diseño en equipo y en entrevistas técnicas.
>
> **Analogía del mundo real:** piensa en planos eléctricos:
>
> - **Sin estándar** → Cada electricista dibuja el enchufe a su manera (cortocircuito seguro).
> - **Con UML** → Clase, flecha y rombo significan siempre lo mismo.
> - **Clase vs objeto** → Plano de casa vs casa construida.
>
> | Razón | Dibujo Libre | UML 2.0 |
> |---|---|---|
> | **Lectura** | Adivinar símbolos | Notación estándar |
> | **Equipo** | Cada quien su estilo | Un solo idioma |
> | **Evaluación** | Diagrama ambiguo | Diagrama calificable |

![[../Diagramas/dsw-u2-04-01-class.svg]]

---

## 🧵 La Caja y sus Relaciones (Stevens caps. 5-6)

### 🎭 Leer un Diagrama en 1 Minuto

> [!note] 📋 Definición — Anatomía de la Caja
>
> | Compartimento | Contenido | Ejemplo |
> |---|---|---|
> | **Arriba** | Nombre (sustantivo del dominio) | Estudiante |
> | **Medio** | Atributos (`-` privado, `+` público, `#` protegido) | `- carnet` |
> | **Abajo** | Operaciones | `+ inscribirse` |
>
> **Notación completa para el papel:** atributos `visibilidad nombre : Tipo` (ej. `- codigo : String`); operaciones `nombre(param : Tipo) : retorno` (ej. `+ cancelar() : boolean`). El esquema sin tipos sirve para pensar; el entregable lleva tipos.
>
> **Clase abstracta:** su nombre va en *cursiva* (en papel, o etiqueta `{abstract}` si la cursiva no sale legible); **no se instancia** — solo existe como pariente que reparte atributos y operaciones a sus herederos, y sus operaciones pueden figurar vacías `{abstract}` de igual forma (Stevens ch. 5).
>
> | Relación | Símbolo | Significado | Ejemplo |
> |---|---|---|---|
> | **Asociación** | línea + multiplicidad | Usa / conoce a | Estudiante `*` — `*` Curso |
> | **Agregación** | rombo blanco | Tiene, pero sobrevive sin él | Equipo ◇— Jugador |
> | **Composición** | rombo negro | Dueño: si muere, mueren partes | Casa ◆— Habitación |
> | **Generalización** | flecha hueca | Es-un (herencia) | Estudiante ─▷ Persona |
> | **Dependencia** | flecha punteada | Usa temporalmente | Reporte - -▷ Datos |
> | **Interfaz** | círculo/paleta | Contrato realizable | `<<interface>> Pagable` |
>
> **Multiplicidades que sí usarás:** `1`, `0..1`, `1..*`, `*`. Ante la duda agregación vs composición: "¿la parte sobrevive sin el todo?". Si la relación necesita atributos o ciclo de vida propio, nace una **clase-entre** colgando de la línea (ej. `Matricula` entre Estudiante y Curso).

### 🔍 Revisión Rápida de tu Diagrama

> [!example] 🧪 Checklist de 4 Preguntas
>
> 1. ¿Toda clase tiene al menos 1 relación? (suelta = sobra o falta)
> 2. ¿Los nombres son sustantivos del dominio? (nada de `Manejador2`)
> 3. ¿Herencia significa "es-un" real? (Estudiante es Persona ✅; Curso es Lista ❌)
> 4. ¿Multiplicidad en AMBOS extremos de cada asociación?

---

## 📚 El deck de cátedra (04a) en detalle

> [!info] 📖 De dónde sale esta sección
> `04aLenguajeUnificadoModelado.pdf` (50 p., MSc. Jurado / Dr. Mera, 2024) es el deck oficial de la Unidad 2. Aquí va lo que el deck explica y que tu nota de clase solo rozaba.

### 🔎 Por qué existe UML (p. 4)

> En los años ochenta y noventa se propusieron **varias notaciones distintas** para describir diseños orientados a objetos. El lenguaje de modelado unificado es la **integración de esas notaciones**: describe notaciones para varios modelos que pueden producirse durante el análisis y el diseño OO, y hoy es un **estándar de facto** para el modelado OO.

### 🎓 Visibilidad con las palabras exactas del deck (p. 12)

> | Símbolo | Significado en el deck | Quién lo alcanza |
> |---|---|---|
> | `+` | público: cualquier cliente de la clase puede acceder a los miembros públicos | cualquiera |
> | `#` | protegido: los miembros de la clase **o cualquier subclase** pueden acceder a los protegidos | la clase y su jerarquía |
> | `-` | privado: solo los miembros de la **misma clase** | la propia clase |

> [!tip] Detalle que se evalúa
> `#` no es "privado con permiso": es visible **para toda la jerarquía**. Y `-` no protege contra otras clases: protege contra todo lo que no sea la propia clase.

### 🧬 Clases de análisis (p. 13)

> [!note] 📖 Definición del deck
> Una **clase de análisis** abstrae una o más clases y/o subsistemas en el diseño del sistema.

Sus cuatro rasgos según el deck:

- Se enfoca en el **manejo de requisitos funcionales** (no en la persistencia).
- Define **responsabilidades**: subconjuntos coherentes de comportamiento definidos por la clase.
- Define **atributos**.
- Expresa las **relaciones** en las que participa la clase.

> [!warning] ⚠️ La confusión clásica
> Una clase de análisis describe *qué* responsabilidades tiene el sistema antes de decidir *cómo* se implementa. Si la mezclas con las tablas de la base, tu diagrama deja de ser diseño y pasa a ser un modelo de datos — es el error 1 de esta nota.

### 🧠 Identificar clases: las dos heurísticas (pp. 14, 16-17)

**Deck — Data-Driven Design** (heurísticas de Shlaer y Mellor; Booch, p. 14): una clase es una cosa **tangible** o del mundo real (libro, copia, curso), un **rol** (miembro de la biblioteca, estudiante, director de estudios), un **evento** (llegada, salida, solicitud) o una **interacción** (reunión, intersección).

**Tu clase — análisis sustantivo/verbo** (p. 16): subrayas los **sustantivos** → candidatos a clase; los **verbos** → operaciones o relaciones. El **first-cut** (p. 17) es ese primer borrador con nombres de clases y sus relaciones, que después se refina.

> [!example] 🧠 Cómo se combinan (caso SIEL)
>
> | Fuente | Qué aporta | Qué hacer con los eventos |
> |---|---|---|
> | **Deck (p. 14)** | 4 familias: tangible, rol, evento, interacción | Un evento **sí puede ser clase** si tiene identidad y estado propio (`Solicitud`, `Acta`) |
> | **Clase (Stevens)** | Filtro de descarte: redundante, vago, evento, atributo, metalenguaje, fuera de alcance | Un evento **sin estado propio** es operación, no clase (`DiaDeLaEleccion`) |

> [!tip] Lectura del diagrama del deck
> ![[Archivos/04a-p14-heuristicas.png]]
>
> ![[Archivos/04a-p16-sustantivo-verbo.png]]

### 🔗 Multiplicidad de una asociación (p. 19)

![[Archivos/04a-p19-multiplicidad.png]]

> [!note] Regla de la cátedra
> La multiplicidad se escribe **en el extremo de la clase que cuenta**, no en el de la que es contada: `Estudiante 1 ── * Curso` significa "un estudiante tiene muchos cursos".

### 🧷 Clases de asociación (p. 22)

> [!warning] Regla del docente, textual
> "Se usa para adjuntar atributos a una asociación en lugar de las clases que asocia" y "**la línea de asociación de clase debe tener el mismo nombre**".

En el SIEL: la relación `OrganizacionPolitica ── inscribe ── Candidatura` lleva atributos (fecha, estado de la candidatura) → nace `Inscripcion` **colgando de la línea**, con el mismo nombre de relación.

![[Archivos/04a-p22-clase-asociacion.png]]

### 🧬 Generalización y herencia (p. 23)

![[Archivos/04a-p23-generalizacion.png]]

### 🏫 El ejemplo del deck: AcademicChoice (pp. 6-7, 25)

El sistema de registro académico que usa el docente: el estudiante gestiona inscripción de materias, paralelos y horarios; cada paralelo tiene estados (**abierto / en lista de espera / cerrado por falta de cupos**); el sistema valida prerrequisitos y conflictos de horario; los administradores fijan políticas (fechas límite, periodos especiales por grupo).

![[Archivos/04a-p25-diagrama-clases.png]]

> [!example] 🔍 Para comparar con tu SIEL
> Mismo esqueleto: actor externo + **estado** de la entidad + **políticas** de un administrador. Si tu diagrama del SIEL no tiene quién administra las políticas (reparto de actas, anulación de-results), le falta el actor `Administrador`.

### 🖼️ Figuras del deck (capítulos 11-25)

> [!example]- 🖼️ Elementos de clase, visibilidad y notación de relaciones
> ![[Archivos/04a-p11-clase-uml.png]]
>
> ![[Archivos/04a-p12-visibilidad.png]]
>
> ![[Archivos/04a-p18-notacion-relaciones.png]]

---

## 🏛️ Ejemplo de la Clase: el modelo de clases del SIEL

> [!note] 📋 Caso trabajado en la clase de modelo de clases (transcripción completa con capturas: [[Unidad 0 - Guias y Ejercicios/Material de clase/SIEL - Modelo de Clases/SIEL - Modelo de Clases|SIEL - Modelo de Clases]])
>
> **1 · Identificar clases por sustantivos** (Stevens ch. 5): subraya los sustantivos → descarta los malos → quedan las clases.
>
> | Se descarta si es… | Ejemplo en el SIEL | Por qué |
> |---|---|---|
> | **Redundante** | "elector" y "ciudadano" | Nombran lo mismo |
> | **Vago** | "información", "datos" | Sin límites claros |
> | **Evento u operación** | "día de la elección" | Ocurre, no perdura |
> | **Atributo** | "votos nulos" | Dato de otra clase |
> | **Metalenguaje** | "sistema", "SIEL" | Habla del modelo, no del dominio |
> | **Fuera de alcance** | "campaña publicitaria" | El sistema no la gestiona |
>
> **2 · Tarjeta CRC de `Candidatura`:** responsabilidades (conocer su dignidad y organización, conocer a sus candidatos, saber si fue aprobada o rechazada, informar su total de votos) ↔ colaboradores (`Dignidad`, `OrganizacionPolitica`, `Candidato`, `Acta`). Se valida narrando el escenario "el funcionario califica una candidatura": ¿qué tarjeta responde cada paso?
>
> **3 · Asociaciones con nombre y multiplicidad bilateral:** `OrganizacionPolitica 1 ── inscribe ── 0..* Candidatura` (roles: auspiciante / candidaturas) — una organización inscribe cero o más candidaturas; cada candidatura tiene exactamente un auspiciante.
>
> **4 · Rombos, dependencia y nota en SIEL:** agregación `Candidatura 1..2 ─◇─ Candidato` (el candidato sobrevive si la candidatura se rechaza); composición `Acta 1..* ─◆─ ConteoVotos` (los conteos mueren con el acta); dependencia punteada `ValidadorActa ⤳ "use" Padron` (uso temporal); nota "los votos nulos no suman a ninguna candidatura".
>
> **5 · Generalización "es un":** *Dignidad* (abstracta, cursiva) △─ `Alcaldia`, `Prefectura` — una Alcaldía ES una Dignidad; una `Candidatura` apunta a `1` Dignidad y por sustituibilidad sirve cualquiera de sus subclases.

---

## 🗺️ Diagrama de Decisión: ¿Qué Relación Uso?

![[../Diagramas/dsw-u2-04-02-flow.svg]]

> [!tip] 💡 Lectura del diagrama
>
> La herencia queda fuera a propósito: solo si hay un "es-un" genuino. El 90% de las herencias apresuradas debieron ser asociaciones o composición.

---

## ⚠️ Problemas Comunes y Soluciones

> [!danger] ❌ Error 1: Modelar la Base de Datos como Clases
>
> **Síntomas:** el diagrama mezcla persistencia con dominio:
>
> ```java
> // ❌ EL ERROR ESTÁ AQUÍ: clases que son tablas, no conceptos
> class TablaUsuario { /* ... */ }
> class ConexionBD { /* ... */ }
> class Estudiante { /* ... */ } // la única que sí es del dominio
> ```
>
> **Solución:**
>
> - Clases = conceptos del problema (Persona, Matrícula), no tablas.
> - La persistencia va en otra capa (ver nota de arquitectura).

> [!danger] ❌ Error 2: Herencia por Pereza ("es-un" Falso)
>
> **Síntomas:** herencia usada solo para reusar 1 método:
>
> ```java
> // ❌ EL ERROR ESTÁ AQUÍ: un Curso NO ES una Lista
> class Curso extends Lista { /* ... */ }
> class Estudiante extends Usuario { /* ... */ } // solo si hay sustitución real
> ```
>
> **Solución:** usa el diagrama de decisión — asociación o composición casi siempre ganan; hereda solo con "es-un" real y sustitución válida (LSP, nota U1-04).

> [!danger] ❌ Error 3: Multiplicidades de Un Solo Lado (viola **multiplicidad bilateral**)
>
> **Síntomas:** un extremo mudo que deja la cardinalidad adivinada: `Estudiante — * Curso` sin nada del otro lado.
>
> **Completo y marcado:** `Estudiante — * Curso` ❌ (falta extremo) vs `Estudiante 1..* — * Curso` ✅ (ambos extremos).
>
> **Solución:** siempre ambos extremos (`1..*` y `*`); si no sabes el número, escribe `*` y anota el supuesto.

---

## 🎯 Mejores Prácticas

> [!tip] 🏆 Checklist UML de Clases
>
> **1. 7±2 clases por diagrama**
>
> Más = divide en paquetes por tema.
>
> **2. Nombres del dominio, no técnicos**
>
> Matrícula, no MatriculaManagerBean.
>
> **3. Valida con escenarios**
>
> Narra "Ana se inscribe": ¿el diagrama permite cada paso? (puente a casos de uso).
>
> **4. Visibilidades con intención**
>
> `-` por defecto; `+` solo lo contratado; `#` solo para herencia real.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Nivel 1 — Básico
>
> **1.** Dibuja la caja UML de `CuentaBancaria` con 2 atributos (uno privado) y 2 operaciones (una pública).
>
> **2.** Diferencia agregación de composición con un ejemplo propio de cada una.
>
> **3.** ¿Qué significan `-`, `+` y `#`? ¿Cuál debe ser el valor por defecto y por qué?
>
> **4.** Corrige: `Perro extends ListaMascotas` — ¿qué está mal y por qué diagrama?
>
> **5.** Pon multiplicidad a: Profesor–Materia, Estudiante–Carnet.
>
> > [!success]- ✅ Respuestas — Nivel 1
> >
> > - **1.** Nombre arriba, atributos en medio con `-`, operaciones abajo con `+`.
> > - **2.** Agregación: la parte sobrevive (Equipo–Jugador). Composición: muere con el todo (Casa–Habitación).
> > - **3.** Privado, público, protegido. `-` por defecto: oculta por defecto (encapsulamiento, nota U1-02).
> > - **4.** "Es-un" falso (un perro no ES una lista): debe ser asociación o tenencia, no herencia.
> > - **5.** Profesor `1` — `*` Materia (un docente, varias materias); Estudiante `1` — `1` Carnet.

> [!example] 📋 Nivel 2 — Intermedio
>
> **6.** Modela Biblioteca–Libro–Socio con clases, relaciones y multiplicidades en ambos extremos.
>
> **7.** Un `Informe` usa datos de `Estudiante` solo para leerlos. ¿Asociación, dependencia o agregación? Justifica.
>
> **8.** Diseña `Pedido–Línea–Producto` decidiendo agregación vs composición en cada par.
>
> **9.** Convierte tu diagrama de la nota U2-02 (TiendaFacade) en clases UML con estereotipos.
>
> **10.** Explica por qué una interfaz UML (`<<interface>>`) se dibuja como círculo/paleta y no como caja.
>
> > [!success]- ✅ Respuestas — Nivel 2
> >
> > - **6.** Biblioteca `1`—`*` Libro (catálogo), Socio `*`—`*` Préstamo (vía intermedia si detalla), Libro con `codigo` PK conceptual.
> > - **7.** Dependencia (punteada): uso temporal de lectura, sin posesión ni ciclo de vida compartido.
> > - **8.** Pedido◆—Línea (composición: sin pedido no hay línea); Línea—Producto (asociación: el producto sobrevive).
> > - **9.** Clases `TiendaFacade`, `Stock`, `Pagos`, `Envíos` + `<<interface>>` donde haya contrato; asociaciones según llamadas.
> > - **10.** Porque no tiene interior que mostrar: solo promete operaciones; la paleta/círculo comunica "contrato, sin estructura".

> [!example] 📋 Nivel 3 — Avanzado
>
> **11.** Modela un sistema de reservas (cliente, reserva, habitación, pago) completo: 5-7 clases, herencia solo si hay "es-un" real, todo con multiplicidad.
>
> **12.** Argumenta con LSP (U1-04) cuándo una jerarquía Persona→Estudiante→Becario deja de ser válida y cómo la refactorizarías.
>
> **13.** Un diagrama tiene 18 clases planas. Aplica paquetes + la regla 7±2: ¿cómo lo divides y qué criterios usas?
>
> **14.** Compara modelar `Matrícula` como clase vs como asociación con atributos: ¿cuándo gana cada opción?
>
> **15.** Diseña el diagrama de clases de tu proyecto de curso (mínimo: 5 clases, 1 herencia real, 1 composición, todo con multiplicidad).
>
> > [!success]- ✅ Respuestas — Nivel 3
> >
> > - **11.** Respuesta libre guiada: Cliente–Reserva–Habitación–Pago; herencia solo si aparece (ej. Pago→PagoTarjeta con sustitución válida).
> > - **12.** Cuando Becario rompe contratos de Estudiante (ej. no puede matricularse igual): pasar a composición o rol separado.
> > - **13.** Por tema (dominio, pagos, reportes); criterio: alta cohesión interna + pocas flechas entre paquetes.
> > - **14.** Clase si tiene identidad y ciclo propio (carnet, historial); asociación con atributos si solo existe entre los dos extremos.
> > - **15.** Autocorrección con el checklist de 4 preguntas de esta nota.

> [!example] 📋 Extra Control03 (formato papel)
>
> **16.** Dibuja la caja completa de `Biblioteca` con 3 atributos tipados (uno `#`) y 2 operaciones con tipo de retorno.
>
> **17.** Modela Biblioteca–Copia–Socio con una composición y una clase-entre `Prestamo`, multiplicidades en ambos extremos.
>
> > [!success]- ✅ Respuestas — Extra
> >
> > - **16.** Caja de 3 compartimentos; cada atributo `visibilidad nombre : Tipo` (ej. `- ciudad : String`, `# horario : String`); cada operación con `(...) : retorno`.
> > - **17.** Biblioteca ◆ `1` ── `1..*` Copia (sin biblioteca no hay copia); Copia `1` ── `0..*` Socio con clase-entre `Prestamo` colgando de la línea (fecha, estado).

> [!example] 📋 Extra clase SIEL (caza de sustantivos)
>
> **18.** Relee el enunciado del SIEL (nota U2-04) y caza todos los sustantivos: ¿cuáles quedan como clases y cuáles descartas, con el motivo?
>
> **19.** ¿Cuál NO sería una buena clase y por qué: **P1** a) Candidatura · b) VotosNulos · c) Parroquia · d) OrganizacionPolitica — **P2** a) JRV · b) Acta · c) DiaDeLaEleccion · d) Candidato?
>
> > [!success]- ✅ Respuestas — Extra SIEL
> >
> > - **18.** Clases que quedan: OrganizacionPolitica, Candidatura, Dignidad (→ Alcaldía, Prefectura), Candidato, Acta, JRV, Funcionario electoral, Ciudadano, Observador, Padrón, Parroquia/Cantón/Provincia. Descartes: "elector/ciudadano" (redundante), "información/datos" (vago), "día de la elección" (evento), "votos nulos" (atributo), "sistema/SIEL" (metalenguaje), "lugar de votación" (atributo de ciudadano).
> > - **19.** P1: **b) VotosNulos** — atributo (dato de otra clase; no suman a ninguna candidatura). P2: **c) DiaDeLaEleccion** — evento (algo que ocurre, no algo que perdura).

---

## 📋 Resumen Ejecutivo

> [!summary] 📋 Lo Esencial
>
> - UML es el **idioma estándar**: caja (clase), rombo (relación en ER) / flechas tipadas en clases.
> - **6 relaciones** con su símbolo; multiplicidad **siempre en ambos extremos**.
> - Herencia solo con **"es-un" real**; lo demás es asociación o composición.
> - Valida narrando **escenarios** ("Ana se inscribe").

---

## ✅ Metas de Aprendizaje

> [!note] 🎯 Nivel Básico
> - [ ] Dibujo la caja UML con visibilidades correctas.
> - [ ] Distingo las 6 relaciones con ejemplo propio.
> - [ ] Pongo multiplicidad en ambos extremos siempre.

> [!note] 🎯 Nivel Intermedio
> - [ ] Modelo un dominio chico (biblioteca, reservas) completo y consistente.
> - [ ] Decido agregación vs composición con la prueba de supervivencia.
> - [ ] Detecto herencias falsas y las corrijo.

> [!note] 🎯 Nivel Avanzado
> - [ ] Divido diagramas grandes en paquetes con criterio.
> - [ ] Diseño el diagrama de clases de mi proyecto con herencia real.
> - [ ] Conecto clases con casos de uso (siguiente nota).

---

## 📊 Resumen Visual

![[../Diagramas/dsw-u2-04-03-mind.svg]]

> [!success] 🔍 Comparación Final
>
> | Aspecto | Dibujo Libre | UML Clases |
> |---|---|---|
> | **Ambigüedad** | ❌ Alta | ✅ Notación única |
> | **Verificación** | Imposible | Escenarios |
> | **Herencia** | Por pereza | Solo "es-un" |
> | **Uso Recomendado** | Borrador 5 min | ✅ **Entregable de diseño** |

---

## 🚀 Próximos Pasos

> [!quote] 🌟 Continuando
>
> **Has aprendido:**
>
> ✅ Caja UML y las 6 relaciones con criterio de elección
> ✅ Revisión anti-errores y diagrama de decisión
> ✅ Validación por escenarios
>
> **Próximo tema:**
>
> | Tema | Qué verás | Por qué importa |
> |---|---|---|
> | **UML comportamiento** | Casos de uso, secuencia, actividad | Muestran la película, no solo la foto |
> | **Del diagrama al código** | Traducir cada relación a Java | El modelo se vuelve software que corre |

---

## 🔁 Repaso SR (flashcards)

#flashcards/diseno-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Multiplicidad dónde?::Siempre en ambos extremos de la relación.
> - ¿Herencia cuándo?::Solo con "es-un" real; lo demás es asociación o composición.
> - ¿Cómo validas un diagrama?::Narrando escenarios ("Ana se inscribe").
> - ¿Rombo vs flechas?::Rombo en ER; en clases, flechas tipadas.
> - ¿Caja UML qué es?::Una clase (nombre + atributos + operaciones).
> - ¿Atributo completo?::`visibilidad nombre : Tipo`; la operación añade `(params) : retorno`.
> - ¿Cuándo clase-entre?::Cuando la relación tiene atributos o ciclo de vida propio (ej. `Prestamo` entre Copia y Socio).
> - ¿Cómo se marca una clase abstracta?::Nombre en cursiva (o etiqueta `{abstract}` en papel); no se instancia, solo hereda.
> - ¿Qué significa visibilidad `#`?::Protegida: visible para la clase y sus herederos.
> - ¿Cómo se identifican las clases de un enunciado?::Subraya los sustantivos y descarta: redundantes, vagos, eventos, atributos, metalenguaje y fuera de alcance (Stevens ch. 5).
> - ¿Qué lleva una tarjeta CRC y cómo se valida?::Responsabilidades (quién hace qué) y colaboradores (con quién); se valida narrando el escenario y viendo si cada paso tiene tarjeta que responda.

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Diseño de Software]]
> - Índice Unidad 2: [[00 - Índice Unidad 2]]
> - Anterior: [[02 - Diseño por componentes e interfaces]]
> - Siguiente: [[04 - UML casos de uso, secuencia y actividad]]
> - Syllabus: [[Bienvenida y Syllabus Diseño de Software]]

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - P. Stevens, R. Pooley, *Using UML*, 2nd ed., caps. 5-6 (clases y objetos).
> - G. Booch, J. Rumbaugh, I. Jacobson — UML 2.0 (unificación de métodos, años 90).
> - Sílabo CCPG1042, Unidad 2: diseño orientado a objetos (7h).
> - Deck de cátedra: [[../Unidad 0 - Guias y Ejercicios/Diapositivas/04aLenguajeUnificadoModelado.pdf|04a Lenguaje unificado de modelado]] (50 p.) — elementos de una clase, visibilidad `+`/`#`/`-`, clases de análisis, notación de relaciones, multiplicidad, clases de asociación y generalización; y [[../Unidad 0 - Guias y Ejercicios/Diapositivas/04bImplementaciónDesdeDiseno.pdf|04b Proceso de implementación desde un diseño]] (30 p.) — asociación, bidireccionalidad, generalización, realización, dependencia, agregación y composición en código.
> - Capturas de la clase: [[SIEL - Modelo de Clases]] (caso SIEL: tarjetas CRC, atributos y operaciones, relaciones) y [[SIEL - Casos de Uso]].
> - Traducción de estas relaciones a código: [[05 - Del diagrama de clases al código]].

---

**Tags:** #CCPG1042 #unidad2 #uml #clases #diseno-software
