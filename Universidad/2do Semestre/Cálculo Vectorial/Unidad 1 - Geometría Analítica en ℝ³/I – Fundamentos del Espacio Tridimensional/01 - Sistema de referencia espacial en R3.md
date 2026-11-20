---
dg-publish: true
tags: [MATG1046, unidad1, geometría-analítica, sistema-de-referencia, R3, octantes, coordenadas-cartesianas]
---

# 📐 Sistema de Referencia Espacial en ℝ³

## 🎯 Introducción

> [!info] 💡 Introducción al Espacio ℝ³
>
> El **espacio euclidiano tridimensional** ℝ³ es la extensión natural del plano cartesiano ℝ² a tres dimensiones. Representa el espacio físico en el que vivimos y es fundamental para la geometría analítica, física, ingeniería y computación gráfica.
>
> **¿Dónde se usa?**
>
> - **Geográfico:** latitud, longitud y altitud.
> - **Arquitectura:** ancho, largo y alto de un edificio.
> - **Videojuegos:** coordenadas X, Y, Z de un personaje.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Sistema_de_referencia_espacial_en_R3.svg]]
>
> **Se lee así:** un cuadro raíz «Sistema de referencia en R³» con cuatro ramas: **Origen O y ejes x, y, z**, **Vectores unitarios** $\hat{i}, \hat{j}, \hat{k}$, **Punto P = (x, y, z)** y la orientación de **sistema derecho** ($\hat{i} \times \hat{j} = \hat{k}$).
>
> **Por qué importa:** es la base sobre la que se construye todo el curso — sin distinguir ejes, vectores unitarios y sentido de giro, las operaciones del capítulo (producto punto/cruz, rectas, planos) no tienen sentido geométrico.
>
> **Ejemplo:** ubica sobre tu mano derecha los tres ejes: pulgar $X$, índice $Y$, dedo medio $Z$ — ese es el orden de un sistema derecho.
>
> **Importancia histórica:**
>
> - **René Descartes (1637):** sistema de coordenadas cartesianas.
> - **Pierre de Fermat (1636):** geometría analítica independiente.
> - **Leonard Euler (1748):** formalización del espacio tridimensional.
> - **Hermann Grassmann (1844):** álgebra de espacios vectoriales.

---

## 📋 Definiciones Formales

### 1️⃣ Espacio ℝ³ — el conjunto de ternas

> [!note] 📋 Definición — Espacio ℝ³
>
> $$\mathbb{R}^3 = \{(x, y, z) \mid x, y, z \in \mathbb{R}\}$$
>
> Es el **producto cartesiano** ℝ × ℝ × ℝ, el conjunto de todas las ternas ordenadas de números reales.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Sistema_de_referencia_espacial_en_R3_01.svg]]
>
> **Se lee así:** de izquierda a derecha: **Elementos Básicos** (origen O=(0,0,0), ejes X/Y/Z, planos XY/XZ/YZ) → tres grupos de **Octantes** agrupados por hemisferio (I +++ el más usado; II–IV superior z>0; V–VIII inferior z<0).
>
> **Por qué importa:** la figura muestra de un vistazo las 8 regiones y su orden de signos.
>
> **Ejemplo:** el cuerpo V (+, +, −) es la mitad inferior del primer octante.

### 2️⃣ Punto en ℝ³ — coordenadas con signo

> [!note] 📋 Definición — Punto en ℝ³
>
> Un punto P en ℝ³ se denota **P = (x, y, z)**, donde:
>
> - **x:** coordenada en el eje X (abscisa).
> - **y:** coordenada en el eje Y (ordenada).
> - **z:** coordenada en el eje Z (cota o altitud).
>
> Cada coordenada es la **distancia con signo** desde el origen hasta la proyección del punto sobre cada eje.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Sistema_de_referencia_espacial_en_R3_01.svg]]
>
> **Se lee así:** el mismo mapa de ejes y planos permite ubicar cualquier terna: proyección sobre XY y luego subir z.
>
> **Ejemplo:** sobre ejes: A=(5,0,0), B=(0,−3,0), C=(0,0,7); en planos: D=(2,4,0) en XY, E=(1,0,3) en XZ, F=(0,2,−5) en YZ.

### 3️⃣ Octante — cada región del espacio

> [!note] 📋 Definición — Octante
>
> Los tres planos coordenados dividen ℝ³ en **ocho regiones** llamadas **octantes**, análogas a los cuadrantes del plano y clasificadas por el signo de cada coordenada.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Sistema_de_referencia_espacial_en_R3_01.svg]]
>
> **Se lee así:** la figura agrupa los octantes por hemisferio: I–IV con z>0 y V–VIII con z<0, con su orden de signos.
>
> **Ejemplo:** el octante I es (+,+,+); el octante VII es (−,−,−).
>
> **Nota:** los puntos sobre planos o ejes no pertenecen a ningún octante.

---

## 🛠️ Tabla Resumen de Octantes

> [!note] 📊 Clasificación Completa
>
> | Octante | Signo X | Signo Y | Signo Z | Condiciones | Ejemplo |
> |---|---|---|---|---|---|
> | **I** | + | + | + | x>0, y>0, z>0 | (2,3,4) |
> | **II** | − | + | + | x<0, y>0, z>0 | (−1,2,5) |
> | **III** | − | − | + | x<0, y<0, z>0 | (−3,−1,2) |
> | **IV** | + | − | + | x>0, y<0, z>0 | (4,−2,3) |
> | **V** | + | + | − | x>0, y>0, z<0 | (1,3,−2) |
> | **VI** | − | + | − | x<0, y>0, z<0 | (−2,1,−4) |
> | **VII** | − | − | − | x<0, y<0, z<0 | (−1,−3,−5) |
> | **VIII** | + | − | − | x>0, y<0, z<0 | (3,−1,−2) |
>
> **Recordar:** el octante I es el más usado; un punto con una coordenada 0 vive en un plano coordenado, no en un octante.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Identificar octantes

> [!example] 📋 Planteamiento
>
> Identifica en qué octante está cada punto: A = (3, 5, 2), B = (−2, 4, −1), C = (1, −3, 6), D = (−4, −5, −2).
>
> > [!success]- ✅ Solución
> >
> > A = (+,+,+) → **Octante I**; B = (−,+,−) → **Octante VI**; C = (+,−,+) → **Octante IV**; D = (−,−,−) → **Octante VII**.

### ✏️ Ejercicio 2 — Puntos en planos coordenados

> [!example] 📋 Planteamiento
>
> ¿Cuáles puntos están sobre planos coordenados? E = (2, 0, 5), F = (0, −3, 4), G = (1, 2, 0).
>
> > [!success]- ✅ Solución
> >
> > E → **Plano XZ** (y=0); F → **Plano YZ** (x=0); G → **Plano XY** (z=0).

### ✏️ Ejercicio 3 — Condiciones de región

> [!example] 📋 Planteamiento
>
> Determina las condiciones para estar: (a) en el octante III; (b) sobre el eje Y positivo; (c) en el plano XZ con z < 0.
>
> > [!success]- ✅ Solución
> >
> > (a) x<0, y<0, z>0; (b) x=0, z=0, y>0; (c) y=0, z<0.

### ✏️ Ejercicio 4 — Región en el espacio

> [!example] 📋 Planteamiento
>
> Describe la región donde x² + y² < 4 y z > 0.
>
> > [!success]- ✅ Solución
> >
> > Cilindro circular de radio 2 centrado en el eje Z, solo la parte sobre el plano XY (z>0). Octantes incluidos: partes de I, II, III y IV.

---

## 🎓 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino ℝ³ como ℝ × ℝ × ℝ y como conjunto de ternas ordenadas.
> - [ ] Ubico un punto P = (x, y, z) proyectando a los ejes en orden.
> - [ ] Reconozco octantes por el signo de cada coordenada.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Describo las restricciones que definen un octante o un plano coordenado.
> - [ ] Muevo del plano XY al espacio completo sin perder el orden de las coordenadas.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - J. Stewart, *Calculus*, cap. 12 «Vectors and the Geometry of Space»: introducción al espacio tridimensional.
> - Syllabus oficial MATG1046 «Cálculo Vectorial», ESPOL — Unidad 1 (Geometría Analítica en ℝ³).
> - Apuntes del curso MATG1046 y las figuras de la materia (`Unidad 0 - Guias y Ejercicios/Diagramas/`).

---

## 🔁 Repaso SR

#flashcards/calcvec-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué es ℝ³?::El producto cartesiano ℝ×ℝ×ℝ: todas las ternas ordenadas de números reales.
> - ¿Cuántos octantes hay y qué los delimita?::Ocho, por los signos (±,±,±) de (x,y,z); los delimitan los planos coordenados.
> - ¿Sistema derecho?::\(\hat{i}, \hat{j}, \hat{k}\) en el orden de la mano derecha: $\hat{i}\times\hat{j}=\hat{k}$.
> - ¿Un punto sobre un plano coordenado está en un octante?::No; los octantes excluyen planos y ejes.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[02 - Vectores en R3]] — operaciones con magnitudes dirigidas.
> - [[01 - Rectas en R3]] — objetos lineales unidimensionales.
> - [[02 - Planos en R3]] — objetos lineales bidimensionales.
>
> **Coordenadas alternativas:**
>
> - **Cilíndricas (ρ, φ, z):** x = ρcos φ, y = ρsin φ, z = z.
> - **Esféricas (r, θ, φ):** x = r sin θ cos φ, y = r sin θ sin φ, z = r cos θ.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Cálculo Vectorial]]
> - Siguiente: [[02 - Vectores en R3]] — ℝ³ deja de ser solo espacio y se vuelve espacio vectorial.
> - Repaso: revisa los octantes por hemisferio (I–IV z>0, V–VIII z<0).

---

**Tags:** #MATG1046 #unidad1 #geometría-analítica #sistema-de-referencia #R3 #octantes #cálculo-vectorial
