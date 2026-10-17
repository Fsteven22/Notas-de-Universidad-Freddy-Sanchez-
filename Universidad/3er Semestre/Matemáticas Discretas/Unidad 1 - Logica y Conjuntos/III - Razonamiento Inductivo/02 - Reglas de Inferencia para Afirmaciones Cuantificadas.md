---
dg-publish: true
---

# 🔢 [[01 - Reglas de Inferencia|Reglas de Inferencia]] para Afirmaciones Cuantificadas

## 🎯 Introducción

> [!info] 💡 ¿Por qué necesitamos reglas cuantificadas?
> 
> Cuando las proposiciones involucran [[02 - Cuantificadores|cuantificadores]] $\forall$ y $\exists$, las reglas proposicionales no son suficientes. Necesitamos reglas que permitan **pasar entre lo universal y lo particular**, y entre lo existencial y lo concreto.
> 
> Estas reglas combinan naturalmente con las reglas proposicionales para construir argumentos más complejos.
>
> ![[../../Diagramas/dis-u1-09-01-graph.svg]]
>
> **En esta nota:** las 4 reglas con su restricción (el testigo existencial debe ser **nuevo**, no usado antes), combinadas con MP/MT, y el error clásico: generalizar desde un caso particular.
>

---

## 📋 Tabla de Reglas para Cuantificadores

> [!note] 📖 Definición — Reglas de inferencia cuantificadas
> 
> | Regla | Nombre |
> |---|---|
> | $\forall x \in D : P(x) \Rightarrow P(d),\ \text{si } d \in D$ | **Particularización Universal** |
> | $P(d),\ \text{para toda } d \in D \Rightarrow \forall x \in D : P(x)$ | **Generalización Universal** |
> | $\exists x \in D : P(x) \Rightarrow P(d),\ \text{para alguna } d \in D$ | **Particularización Existencial** |
> | $P(d),\ \text{para alguna } d \in D \Rightarrow \exists x \in D : P(x)$ | **Generalización Existencial** |
![[ChatGPT Image 2 jun 2026, 01_40_53 1.png]]

---


> [!note] 🔍 Mapa — Las 4 direcciones
>
> ![[../../Diagramas/dis-u1-09-02-graph.svg]]
>
> **Se lee así:** universal baja a caso, casos suben a universal; existencial exige testigo fresco.

## 🔍 Reglas Detalladas

### 1 — Particularización Universal

> [!tip] ⚙️ Descripción
> 
> Si $\forall x \in D : P(x)$ es verdadera, entonces $P(x)$ es verdadera para **cada** $x$ en el dominio de discurso $D$. En particular, si $d \in D$ entonces $P(d)$ es verdadera.
> 
> $$\frac{\forall x \in D : P(x)}{\therefore\ P(d), \quad \text{si } d \in D}$$
> 
> > [!example] 🟢 Ejemplo
> >
> > Esta es la regla más usada al inicio de demostraciones: tomamos un elemento particular del dominio y le aplicamos la propiedad universal.

---

### 2 — Generalización Universal

> [!tip] ⚙️ Descripción
> 
> Si $P(d)$ es verdadera para **todo** $d \in D$ (sin imponer restricciones especiales sobre $d$), entonces $\forall x \in D : P(x)$ es verdadera.
> 
> $$\frac{P(d), \quad \text{para toda } d \in D}{\therefore\ \forall x \in D : P(x)}$$
> 
⚠️ El elemento $d$ debe ser **arbitrario**: no puede tener propiedades especiales que no compartan todos los elementos del dominio.

---

### 3 — Particularización Existencial

> [!tip] ⚙️ Descripción
> 
> Si $\exists x \in D : P(x)$ es verdadera, podemos dar nombre a ese elemento y llamarlo $d$.
> 
> $$\frac{\exists x \in D : P(x)}{\therefore\ P(d), \quad \text{para alguna } d \in D}$$

---

### 4 — Generalización Existencial

> [!tip] ⚙️ Descripción
> 
> Si existe un elemento concreto $d \in D$ tal que $P(d)$ es verdadera, entonces existe al menos un $x$ en $D$ que cumple $P$.
> 
> $$\frac{P(d), \quad \text{para alguna } d \in D}{\therefore\ \exists x \in D : P(x)}$$

---

## 📝 Ejemplos

> [!example] 📝 Ejemplo 1 — Argumento con cuantificadores y reglas proposicionales
> 
> Demuestre que el siguiente argumento es válido:
> 
> **Hipótesis:** Antoine Griezmann, un jugador del Atlético de Madrid, es un goleador. Todos los goleadores pueden ganar mucho dinero.
> 
> **Conclusión:** Algún jugador del Atlético de Madrid puede ganar mucho dinero.
> 
> **Solución:**
> 
> Sea $D$ el conjunto de todos los jugadores. Definimos:
> - $P(x)$: $x$ es un jugador del Atlético de Madrid
> - $Q(x)$: $x$ es un goleador
> - $R(x)$: $x$ puede ganar mucho dinero
> 
> Sea $d$ = Antoine Griezmann. El argumento se representa:
> 
> $$\frac{P(d) \wedge Q(d) \qquad \forall x \in D : Q(x) \to R(x)}{\therefore\ \exists x \in D : P(x) \wedge R(x)}$$
> 
> **Demostración paso a paso:**
> 
> | Paso | Proposición | Justificación |
> |:---:|---|---|
> | 1 | $Q(d) \to R(d)$ | Particularización Universal sobre $\forall x : Q(x) \to R(x)$ |
> | 2 | $Q(d)$ | Simplificación de $P(d) \wedge Q(d)$ |
> | 3 | $R(d)$ | Modus Ponens (pasos 1, 2) |
> | 4 | $P(d)$ | Simplificación de $P(d) \wedge Q(d)$ |
> | 5 | $P(d) \wedge R(d)$ | Conjunción (pasos 4, 3) |
> | 6 | $\exists x \in D : P(x) \wedge R(x)$ | Generalización Existencial (paso 5) |
> 
> Concluimos que el argumento es **válido**. $\blacksquare$

---

## 🏋️ Ejercicios Propuestos

> [!question] 📋 Ejercicios de la clase
> 
> Determine la validez de los siguientes argumentos:
> 
> **1.** Todo científico honesto contribuye al progreso del conocimiento. Toda persona tiene reconocimiento público o no contribuye al progreso del conocimiento. Existe al menos un científico honesto. Por lo tanto, existe al menos un científico honesto que tiene reconocimiento público.
> 
> **2.** Si vamos a Galápagos, gastaremos mucho dinero. Si vamos a Quilotoa, sufriremos por el frío. Vamos a Galápagos o a Quilotoa. En consecuencia, gastaremos mucho dinero o sufriremos por el frío.
> 
> **3.** Todo lector estudioso consulta fuentes confiables. Algunos lectores consultan fuentes poco confiables. Todo lector que consulta fuentes confiables aumenta su conocimiento. Por lo tanto, todos los lectores aumentan su conocimiento.

---

## 📊 Comparación de las 4 Reglas

> [!success] 🗂️ Resumen rápido
> 
> | Regla | Dirección | Cuantificador | Uso típico |
> |---|---|---|---|
> | **Particularización Universal** | $\forall \to$ particular | $\forall$ | Aplicar una propiedad a un elemento concreto |
> | **Generalización Universal** | particular $\to \forall$ | $\forall$ | Concluir que algo vale para todos |
> | **Particularización Existencial** | $\exists \to$ particular | $\exists$ | Nombrar un elemento que sabemos que existe |
> | **Generalización Existencial** | particular $\to \exists$ | $\exists$ | Afirmar que al menos uno existe |

---

## ⚠️ Errores Comunes y Principios

> [!danger] ❌ Error 1: Generalizar desde un elemento con historia (viola **arbitrariedad en GU**)
>
> - ❌ **EL ERROR ESTÁ AQUÍ:** probar $P(c)$ para una $c$ con supuestos previos y concluir $\forall x\,P(x)$.
> - ✅ Así sí: la generalización universal exige una $c$ **arbitraria**, sin propiedades asumidas.

> [!danger] ❌ Error 2: Particularizar $\forall$ fuera del dominio (viola **dominio de discurso**)
>
> - ❌ **EL ERROR ESTÁ AQUÍ:** de $\forall x \in \mathbb{N}\,P(x)$ concluir $P(-3)$.
> - ✅ Así sí: la particularización solo instancia elementos **del dominio** declarado.

> [!danger] ❌ Error 3: Reutilizar el nombre del testigo $\exists$ (viola **frescura del testigo**)
>
> - ❌ **EL ERROR ESTÁ AQUÍ:** de $\exists x\,P(x)$ y $\exists x\,Q(x)$ concluir $P(c) \wedge Q(c)$ con la misma $c$.
> - ✅ Así sí: cada existencial da su propio testigo ($c_1$, $c_2$) — podrían ser distintos.

---

## 📊 Resumen Visual

![[../../Diagramas/dis-u1-09-03-graph.svg]]

---

## 📋 Resumen Ejecutivo

> [!summary] 📋 Lo Esencial
>
> - 4 direcciones: $\forall$→caso (particularización), casos→$\forall$ (generalización), $\exists$→testigo, testigo→$\exists$.
> - Testigo existencial **nuevo**: no usado antes en la prueba.
> - Se combinan con MP/MT proposicionales; no generalizar desde un caso.

---

## ✅ Metas de Aprendizaje

> [!note] 🎯 Nivel Básico
>
> - [ ] Aplico las 4 reglas (PU, GU, PE, GE) en la dirección correcta.
> - [ ] Particularizo $\forall$ solo dentro del dominio declarado.
> - [ ] Doy testigo fresco en cada particularización existencial.

> [!note] 🎯 Nivel Intermedio
>
> - [ ] Generalizo a $\forall$ solo desde elemento arbitrario.
> - [ ] Combino reglas proposicionales y cuantificadas en una demostración.

---

## 🔁 Repaso SR (flashcards)

#flashcards/discretas-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿4 reglas cuantificadas?::PU, GU, PE, GE (universal/existencial × particular/general).
> - ¿Testigo nuevo por qué?::Si ya se usó, la prueba colapsa (particularización existencial).
> - ¿Error típico?::Generalizar $\forall$ desde un solo caso.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Matemáticas Discretas]]
> - Anterior: [[01 - Reglas de Inferencia]] · Siguiente: [[03 - Inducción Matemática]]
> - Base: [[02 - Cuantificadores]]

---

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - Rosen, *Discrete Mathematics and Its Applications* — cap. 1 (inferencia con cuantificadores).
> - Material de clase MATG1051: las 4 reglas y restricciones del testigo.

---

**Tags:** #matematicas-discretas #logica-predicados #cuantificadores #particularizacion-universal #generalizacion-existencial #reglas-de-inferencia #MATG1051
