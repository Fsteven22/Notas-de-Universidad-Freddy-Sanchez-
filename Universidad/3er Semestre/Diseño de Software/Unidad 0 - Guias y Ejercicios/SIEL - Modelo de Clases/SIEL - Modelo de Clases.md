---
dg-publish: true
tags: [CCPG1042, unidad2, siel, modelo-de-clases]
---

# 🏛️ SIEL — Modelo de Clases: lo necesario y nada más (capturas)

> [!info] ℹ️ Qué es esto
> Transcripción completa de las 8 capturas del deck de **Modelo de Clases**, segunda lección del caso **SIEL** (Sistema de Elecciones) para Control03. Fuentes: Stevens cap. 5 · Pressman & Maxim, Apéndice 1. Deck: *Bloque 2 · minutos 60 a 107*.
>
> El ejemplo resumido vive en [[03 - UML clases, objetos y relaciones]]; aquí queda el desarrollo completo con las capturas.

## 🧭 Portada — qué cubre

> Bloque 2 · Modelado de clases en UML a partir del enunciado de SIEL:
> identificar clases (sustantivos), tarjetas CRC, atributos/operaciones y
> visibilidad, asociaciones y multiplicidades, agregación/composición/
> dependencia, notas y generalización.

![[Modelo de clases.png]]

## 🔍 Identificar clases por sustantivos (Stevens cap. 5)

Flujo: **1 · Subraya los sustantivos → 2 · Descarta los malos → 3 · Quedan las clases**.

| Se descarta si es… | Ejemplo en el SIEL | Por qué |
|---|---|---|
| **Redundante** | "elector" y "ciudadano" | Nombran lo mismo: queda uno |
| **Vago** | "información", "datos" | No tiene límites claros |
| **Evento u operación** | "día de la elección", "revisión" | Es algo que ocurre, no algo que perdura |
| **Atributo** | "votos nulos", "lugar de votación" | Es un dato de otra clase |
| **Metalenguaje** | "sistema", "SIEL" | Habla del modelo, no del dominio |
| **Fuera de alcance** | "campaña publicitaria" | El sistema no la gestiona |

> [!warning] 🎯 Pregunta típica de examen
> "¿Cuál de estas NO sería una buena clase?"

![[Modelo de clases-7.png]]

## ✅ Un buen modelo y las tarjetas CRC

**Un buen modelo de clases…**

- ✔ **soporta los casos de uso**: cada paso tiene una clase que responde;
- ✔ **refleja el dominio**: usa el vocabulario de los usuarios;
- ✔ **modela lo necesario** y nada más.

**Tarjeta CRC de ejemplo** (*Candidatura*):

| Candidatura — Tarjeta CRC |
|---|
| **Responsabilidades** |
| · Conocer su dignidad y su organización |
| · Conocer a sus candidatos |
| · Saber si fue aprobada o rechazada |
| · Informar su total de votos |
| **Colaboradores** |
| · Dignidad · OrganizacionPolitica · Candidato · Acta |

> [!tip] Validar con un escenario
> "El funcionario califica una candidatura". Recorre los pasos: ¿qué tarjeta
> sabe cada cosa? Si nadie responde, falta una responsabilidad o una clase.

![[Modelo de clases-1.png]]

## 📦 Una clase: nombre, atributos y operaciones (Pressman Ap. 1)

```
┌──────────────────────────────────────────┐
│               Candidatura                 │
├──────────────────────────────────────────┤
│ - codigo: String                          │
│ - estado: EstadoCalificacion              │
│ # fechaInscripcion: Date                  │
├──────────────────────────────────────────┤
│ + calificar(aprobada: Boolean)            │
│ + totalVotos(): Integer                   │
│ ~ validarRequisitos(): Boolean            │
└──────────────────────────────────────────┘
Compartimentos: nombre · atributos (visibilidad nombre: tipo) · operaciones
```

**Visibilidad:**

| Símbolo | Significa |
|---|---|
| `+` | Pública: cualquiera la usa |
| `-` | Privada: solo la propia clase |
| `#` | Protegida: la clase y sus subclases |
| `~` | Paquete: clases del mismo paquete |

> [!note] Clase abstracta
> Su nombre va en **cursiva** (ej.: *Dignidad*).

![[Modelo de clases-2.png]]

## 🔗 Asociaciones: nombre, multiplicidad y roles (Stevens cap. 5)

```
OrganizacionPolitica 1 ── inscribe ── 0..* Candidatura
(auspiciante)                      (candidaturas)
```

**Glosario de multiplicidades:**

| Multiplicidad | Significa |
|---|---|
| `1` | exactamente uno |
| `0..1` | cero o uno |
| `0..*` (o `*`) | cero o más |
| `1..*` | uno o más |

> [!example] Se lee en ambos sentidos
> Una `OrganizacionPolitica` inscribe `0..*` candidaturas; **cada** `Candidatura`
> tiene exactamente `1` auspiciante.
>
> **Pregunta de chat:** ¿cómo se lee "un Cliente tiene 0..\* Reservas"?
> **Lectura:** un Cliente tiene cero o más Reservas — y cada Reserva pertenece
> a exactamente un Cliente.

![[Modelo de clases-3.png]]

## 🧷 Agregación, composición, dependencia y notas (Pressman Ap. 1)

| Relación | Notación | Lectura en SIEL |
|---|---|---|
| **Agregación** | Rombo **vacío** en el todo (`Candidatura 1..2 ─◇─ Candidato`) | La parte existe sola: el candidato sigue existiendo si la candidatura se rechaza |
| **Composición** | Rombo **lleno** en el todo (`Acta 1..* ─◆─ ConteoVotos`) | La parte muere con el todo: si se elimina el acta, sus conteos desaparecen |
| **Dependencia** | Línea **punteada** con flecha y estereotipo (`ValidadorActa ⤳ "use" Padron`) | Una clase usa a otra de forma temporal |
| **Nota** | Esquina **doblada** unida con línea punteada | ("Los votos nulos no suman a ninguna candidatura") — comentario sobre el elemento |

![[Modelo de clases-4.png]]

## 🎲 Actividad 3 (individual · 7 min): Caza los sustantivos del SIEL

1. Relee el enunciado y anota **todos** los sustantivos.
2. Marca cada uno: **clase** o **descarte**, con el motivo.
3. Responde en el chat: **P1 _**, **P2 _**.

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

![[Modelo de clases-5.png]]

## 🌿 Generalización: la relación "es un" (Stevens cap. 5 · Pressman Ap. 1)

```
        ‹abstract› Dignidad            (nombre en cursiva = abstracta)
                   △
                   │
            ┌──────┴──────┐
        Alcaldia       Prefectura
```

- **"Es un"**: una Alcaldía **es una** Dignidad. Si la frase suena rara, no es
  generalización.
- **Herencia**: la subclase recibe atributos, operaciones y asociaciones de la
  superclase.
- **Sustituibilidad**: donde se espera una Dignidad, sirve una Alcaldía o una
  Prefectura — una `Candidatura` apunta a `1` Dignidad, sea cual sea.
- Triángulo hueco apuntando a la superclase.

![[Modelo de clases-6.png]]

---

- Mapa de contenido: [[Diseño de Software]]
- Índice Unidad 2: [[00 - Índice Unidad 2]]
- Complemento: [[SIEL - Casos de Uso]]

**Tags:** #CCPG1042 #unidad2 #siel #modelo-de-clases
