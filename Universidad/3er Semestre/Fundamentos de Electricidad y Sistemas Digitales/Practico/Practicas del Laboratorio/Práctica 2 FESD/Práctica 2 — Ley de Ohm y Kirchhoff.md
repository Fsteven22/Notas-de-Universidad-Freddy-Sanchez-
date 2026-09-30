---
dg-publish: true
---

# 🧪 Práctica 2 — Ley de Ohm y Leyes de Kirchhoff

## 🎯 Introducción

> [!info] 💡 ¿Por qué esta práctica es importante?
>
> Esta práctica valida experimentalmente las leyes que viste en teoría: **Ley de Ohm** ($V=IR$), **KCL** ($\sum I = 0$ en nodos) y **KVL** ($\sum V = 0$ en mallas). Además aplicas los métodos de **divisor de tensión** y **divisor de corriente** para dimensionar redes eléctricas.
>
> ```mermaid
> graph TD
>     A[Práctica 2] --> B[Procedimiento 1<br/>Ley de Ohm]
>     A --> C[Procedimiento 2<br/>Divisor de corriente + KCL]
>     A --> D[Procedimiento 3<br/>Divisor de tensión + KVL]
>     B --> E[Medir I vs R]
>     C --> F[Medir I por rama]
>     D --> G[Medir V por elemento]
>     style A fill:#fff4e1
>     style B fill:#e1f5ff
>     style C fill:#e1ffe1
>     style D fill:#f5e1ff
> ```

---

## ⚠️ Seguridad

> [!danger]
> - Trabaja con fuente DC a 10–15 V.
> - Manipula conexiones **solo con la fuente apagada** (OUTPUT off).
> - No exceder 1 A por resistencia.

---

## 🧰 Materiales

> [!note] 📦 Materiales necesarios
>
> | Material | Especificación |
> |---|---|
> | Fuente de Voltaje | Dual DC, CH1 |
> | Multímetro | FLUKE 179 |
> | Resistencias | 100 KΩ, 10 KΩ, 5 KΩ, 1 KΩ, 560 Ω, 2.2 KΩ |
> | Cables | banana–banana |

---

## 📖 Introducción Teórica

> [!note] 🔵 Elementos activos y pasivos
>
> - **Activos:** fuentes de voltaje y de corriente (suministran energía al circuito).
> - **Pasivos:** resistencias, capacitores e inductores (almacenan o disipan energía).
>
> Las resistencias disipan calor, los capacitores almacenan energía en su campo eléctrico, y los inductores en campos magnéticos. Se conectan en **serie** o en **paralelo**.
>
> [!note] 🔵 Ley de Ohm — La relación fundamental
>
> $$\boxed{V = R \cdot I}$$
>
> Donde $V$ es la diferencia de potencial (V), $R$ la resistencia (Ω) e $I$ la corriente (A).
>
> Formas derivadas:
>
> $$I = \frac{V}{R} \qquad\qquad R = \frac{V}{I}$$
>
> |Comportamiento|Descripción|
> |---|---|
> |**Elemento lineal**|Cumple $V = IR$ para todo rango|
> |**Elemento no lineal**|No cumple $V = IR$ (diodos, transistores)|
>
> [!note] 🟢 KCL — Ley de Corrientes de Kirchhoff
>
> $$\boxed{\sum_{k=1}^{n} I_k = 0}$$
>
> La suma algebraica de todas las corrientes que entran y salen de un nodo es cero. Corriente que entra = positiva, que sale = negativa.
>
> [!note] 🟡 KVL — Ley de Voltajes de Kirchhoff
>
> $$\boxed{\sum_{k=1}^{n} V_k = 0}$$
>
> La suma algebraica de todos los voltajes a lo largo de una malla cerrada es cero.
>
> [!note] 🔢 Divisor de Tensión
>
> Para resistencias en serie, el voltaje en $R_1$:
>
> $$V_{R1} = V_{total} \cdot \frac{R_1}{R_1 + R_2}$$
>
> [!note] 🔢 Divisor de Corriente
>
> Para resistencias en paralelo, la corriente por $R_1$:
>
> $$I_{R1} = I_{total} \cdot \frac{R_2}{R_1 + R_2}$$

---

## ⚙️ Procedimiento 1 — Ley de Ohm

> [!tip] 🔧 Pasos
>
> 1. Armar circuito conectando el amperímetro en serie con la resistencia.
> 2. Usar resistencia de 100 KΩ, fuente CH1 a 10 Vdc, 1 A.
> 3. Energizar (presionar OUTPUT) y medir corriente con el amperímetro.
> 4. Cambiar resistencia a 10 KΩ, 5 KΩ y 1 KΩ. Repetir medición.
>
> [!note] 📊 Tabla 1 — Resultados del Procedimiento 1
>
> |Resistencia|Amperaje (mA)|Teórico $I = V/R$ (mA)|Error %|
> |---|---|---|---|
> |100 KΩ| | | |
> |10 KΩ| | | |
> |5 KΩ| | | |
> |1 KΩ| | | |
>
> [!question]- ❓ Análisis
>
> - ¿Cuál es la relación que tiene la corriente con los cambios de resistencia?
> - ¿Se cumple $V = IR$ para cada medición?

---

## ⚙️ Procedimiento 2 — Divisor de Corriente

> [!tip] 🔧 Pasos
>
> 1. Armar circuito con 3 resistencias en paralelo.
> 2. Fuente a 10 V, 1 A. Medir corriente por cada resistencia.
> 3. Verificar **KCL**: las corrientes por rama deben sumar la corriente total.
> 4. Cambiar fuente a 15 V, 1 A y repetir mediciones.
> 5. Contrastar con el método de divisor de corriente.
>
> [!note] 📊 Tabla 2 — Resultados del Procedimiento 2
>
> |Resistencia|10 V, 1 A (mA)|15 V, 1 A (mA)|Divisor de corriente teórico|
> |---|---|---|---|
> |1 KΩ| | | |
> |2.2 KΩ| | | |
> |560 Ω| | | |
>
> [!question]- ❓ Análisis
>
> - ¿Qué pasaría con la fuente de 10 V 1 A si se conectan más cargas en paralelo?
> - ¿Cuál es la resistencia equivalente vista por la fuente?
> - ¿Se cumple KCL ($\sum I_{rama} = I_{total}$)?

---

## ⚙️ Procedimiento 3 — Divisor de Tensión

> [!tip] 🔧 Pasos
>
> 1. Armar circuito con resistencias en serie.
> 2. Medir voltaje en cada resistencia con el voltímetro.
> 3. Verificar **KVL**: los voltajes deben sumar el total de la fuente.
> 4. Contrastar con el método de divisor de tensión.
>
> [!note] 📊 Tabla 3 — Resultados del Procedimiento 3
>
> |Resistencia|Voltaje medido (V)|Divisor de tensión teórico (V)|
> |---|---|---|
> |1 KΩ| | |
> |2.2 KΩ| | |
> |560 Ω| | |
>
> [!question]- ❓ Análisis
>
> - ¿Qué pasaría con la fuente de 10 V 1 A si se conectan más cargas en serie?
> - ¿Se cumple KVL ($\sum V_{elementos} = V_{fuente}$)?

---

## 📝 Notas personales

> [!question]- 🤔 Mis observaciones
>
> - Diferencias teórico vs medido:
> - Errores encontrados:
> - Dudas para el informe:

---

## 📄 Informe

> Usa [[FORMATO INFORME DE PRÁCTICA.pdf]] y [[Formato Pre-prácticas.pdf]] para entregar. Simulaciones en Proteus.

## Metas de Aprendizaje

> [!note] Nivel Básico
> - [ ] Identifico la fuente, el amperímetro en serie y la resistencia en el diagrama de montaje.
> - [ ] Conecto la fuente apagada y verifico polaridad antes de energizar.
> - [ ] Cambio el rango del amperímetro entre mA y 10A según la corriente estimada.
>
> [!note] Nivel Intermedio
> - [ ] Explico la Ley de Ohm ($V=IR$) y uso $R=V/I$ para predecir corriente con R de 100 KΩ.
> - [ ] Leo la corriente en los 4 valores de resistencia y confirmo que crece cuando R disminuye.
> - [ ] Identifico un nodo y cuento corrientes que entran y salen para verificar KCL.
>
> [!note] Nivel Avanzado
> - [ ] Mido corriente por cada resistencia en paralelo y confirmo que la suma es igual a la total.
> - [ ] Uso el divisor de corriente para predecir la fracción por cada rama y la comparo con lo medido.
> - [ ] Mido voltajes en serie y confirmo que suman el voltaje de la fuente (KVL).
>
> [!quote] 🔗 Conexiones
> - Teoría: [[05 - Leyes de Ohm y Kirchhoff]], [[04 - Circuitos en Serie Paralelo y Mixtos]] y [[06 - Teoremas de Analisis de Circuitos]]
> - Previa: [[Práctica 1 — Manejo de Equipos del Laboratorio]]
> - Equipos: [[Equipos del Laboratorio - FESD]]
> - Siguiente: [[Práctica 3 — Diodos y Transistores]]

---

---

## 📎 Guía oficial (Garden)

![[Práctica 2 Ley de Ohm y Leyes de Kirchof.pdf]]
**Tags:** #practica #laboratorio #EYAG1037 #FESD #ESPOL #unidad1 #leyDeOhm #kirchhoff
