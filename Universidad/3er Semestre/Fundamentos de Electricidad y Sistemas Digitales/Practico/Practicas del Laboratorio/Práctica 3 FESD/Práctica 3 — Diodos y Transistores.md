---
dg-publish: true
---

# 🧪 Práctica 3 — Funcionamiento de Diodos y Transistores

## 🎯 Introducción

> [!info] 💡 ¿Por qué esta práctica es importante?
>
> El **diodo** y el **transistor BJT** son los componentes activos base de la electrónica. En esta práctica validas experimentalmente:
> - La **polarización directa e inversa** del diodo (rectificación de un semiciclo).
> - El BJT como **switch electrónico** (corte vs saturación).
> - Un **sensor de luz** con LDR que acciona un LED mediante un transistor.
>
> ```mermaid
> graph TD
>     A[Práctica 3] --> B[Procedimiento 1<br/>Diodo 1N4007]
>     A --> C[Procedimiento 2<br/>BJT 2N3904]
>     A --> D[Procedimiento 3<br/>Sensor LDR]
>     B --> E[Rectificación senoidal]
>     C --> F[Switch: corte/saturación]
>     D --> G[Sensibilidad de luz]
>     style A fill:#fff4e1
>     style B fill:#e1f5ff
>     style C fill:#e1ffe1
>     style D fill:#f5e1ff
> ```

---

## ⚠️ Seguridad

> [!danger]
> - Trabaja con fuente DC a 12 V.
> - Manipula conexiones solo con la fuente apagada.
> - No invertir polaridad del diodo ni del transistor.

---

## 🧰 Materiales

> [!note] 📦 Materiales necesarios
>
> | Material | Especificación |
> |---|---|
> | D1 | 1N4007 |
> | Q1 | 2N3904 (NPN) |
> | Relé | 12 V |
> | LED | Verde / rojo |
> | Pulsador |  |
> | Potenciómetro | 5 KΩ |
> | LDR |  |
> | Resistencias | 1 KΩ, 1 MΩ, 680 Ω, 5 KΩ |

---

## 📖 Introducción Teórica

> [!note] 🔵 Diodo — Polarización directa e inversa
>
> El diodo es un elemento semiconductor con **ánodo** (A) y **cátodo** (K).
>
> |Condición|Comportamiento|Ecuación|
> |---|---|---|
> |**Directa** ($V_A > V_K$)|Conduce, actúa como cortocircuito|$V_D \approx 0.7\text{ V}$ (silicio)|
> |**Inversa** ($V_A < V_K$)|Bloquea, actúa como circuito abierto|$I \approx 0$|
>
> En una señal senoidal, el diodo solo deja pasar el **semiciclo positivo** → rectificación.
>
> [!note] 🟢 Transistor BJT — Switch electrónico
>
> El BJT tiene 3 terminales: **Base** (B), **Colector** (C), **Emisor** (E). Configuración NPN.
>
> |Modo|Condición|Comportamiento|
> |---|---|---|
> |**Corte**|$V_{BE} < 0.7\text{ V}$|Switch abierto, $I_C = 0$|
> |**Saturación**|$V_{BE} \gg 0.7\text{ V}$|Switch cerrado, $V_{CE(sat)} \approx 0.2\text{ V}$|
>
> En esta práctica solo se usa corte y saturación (no zona lineal).

---

## ⚙️ Procedimiento 1 — Polarización de Diodo

> [!tip] 🔧 Pasos
>
> 1. Armar circuito con D1 (1N4007) y resistencia en serie.
> 2. Generador de funciones: señal cuadrada, 10 Vpp, 60 Hz.
> 3. Conectar CH1 (entrada) y CH2 (salida) en el osciloscopio.
> 4. Observar la forma de onda de salida.
>
> [!note] 📊 Tabla 1 — Salida del diodo
>
> |Condición|$V_{max}$ (V)|$V_{min}$ (V)|Observación|
> |---|---|---|---|
> |Polarización directa| | |Solo pasa semiciclo positivo|
> |Polarización inversa| | |Se bloquea el semiciclo negativo|
>
> [!question]- ❓ Análisis
>
> - ¿Qué es el tiempo de recuperación inversa de un diodo?
> - Dibujar 2 períodos de la onda de salida si la entrada cambia a seno de 10 Vpp.

---

## ⚙️ Procedimiento 2 — Transistor BJT como Switch

> [!tip] 🔧 Pasos
>
> 1. Armar circuito con Q1 (2N3904), relé, LED y pulsador.
> 2. Medir $V_x$, $V_{BE}$ y $V_{CE}$ con pulsador **SIN** presionar.
> 3. Medir las mismas variables con pulsador **PRESIONADO**.
> 4. Completar la tabla.
>
> [!note] 📊 Tabla 2 — Mediciones del BJT
>
> |Variable|Pulsador sin presionar|Pulsador presionado|Modo|
> |---|---|---|---|
> |$V_x$| | | |
> |$V_{BE}$| | |Corte / Saturación|
> |$V_{CE}$| | |Corte / Saturación|
>
> [!question]- ❓ Análisis
>
> - ¿Qué función cumple el diodo D1 en el circuito del Procedimiento 2?
> - Según el datasheet del 2N3904, ¿cuáles son los voltajes $V_{CE(sat)}$ máximos y en qué condiciones?

---

## ⚙️ Procedimiento 3 — Sensor de Luz con LDR

> [!tip] 🔧 Pasos
>
> 1. Armar circuito con LDR, potenciómetro y transistor.
> 2. Ajustar potenciómetro al 0% con LDR sin iluminar → LED encendido.
> 3. Acercar linterna a LDR hasta que se apague el LED. Ajustar potenciómetro hasta re-encender.
> 4. Alejar linterna y observar comportamiento.
>
> [!question]- ❓ Análisis
>
> - ¿Cómo influye el ajuste del potenciómetro para el accionamiento de la carga (LED)?
> - ¿Cómo cambia el parámetro $V_{BE}$ al variar la luz?

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
> - [ ] Identifico el ánodo y cátodo del diodo 1N4007 y verifico la polaridad en el montaje.
> - [ ] Uso el osciloscopio para observar la rectificación de un semiciclo en la salida del diodo.
> - [ ] Distinguo la diferencia entre entrada (cuadrada) y salida (rectificada) en CH1 vs CH2.
>
> [!note] Nivel Intermedio
> - [ ] Identifico terminales B, C, E del 2N3904 y verifico la orientación NPN en el circuito.
> - [ ] Mido $V_{BE}$ y determino si el transistor está en corte ($V_{BE} < 0.7\text{ V}$) o saturación.
> - [ ] Explico por qué $V_{CE(sat)}$ es aprox. 0.2 V cuando el transistor conduce completamente.
>
> [!note] Nivel Avanzado
> - [ ] Reconozco la función de protección del diodo 1N4007 en el circuito del relé.
> - [ ] Monto el circuito con LDR y ajusto el potenciómetro para controlar la sensibilidad del LED.
> - [ ] Relaciono el comportamiento del sensor de luz con la región de operación del BJT (corte vs saturación).
>
> [!quote] 🔗 Conexiones
> - Teoría: [[01 - Semiconductores y Bandas de Energía]], [[02 - El Diodo - Unión P-N]] y [[03 - Transistor BJT]]
> - Previa: [[Práctica 2 — Ley de Ohm y Kirchhoff]]
> - Siguiente: [[Práctica 4 — Fuentes Lineales]]

---

---

## 📎 Guía oficial (Garden)

![[Práctica #3 Funcionamiento de Diodos y Transistores.pdf]]
**Tags:** #practica #laboratorio #EYAG1037 #FESD #ESPOL #unidad2 #diodo #BJT #transistor
