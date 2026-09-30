---
dg-publish: true
---

# 🧪 Práctica 5 — Funcionamiento de Filtros Activos

## 🎯 Introducción

> [!info] 💡 ¿Por qué esta práctica es importante?
>
> Los **filtros activos** usan OPAMPs para selectar frecuencias deseadas y atenuar ruido. En esta práctica construyes un filtro activo y un acondicionador de señal, midiendo la respuesta en frecuencia y la ganancia en cada punto.
>
> ```mermaid
> graph TD
>     A[Práctica 5] --> B[Procedimiento 1<br/>Filtro activo LM358]
>     A --> C[Procedimiento 2<br/>Acondicionador de señal]
>     B --> D[Respuesta en frecuencia<br/>10 KHz – 1 MHz]
>     C --> E[Mapeo 0-10V → -5V a +5V]
>     style A fill:#fff4e1
>     style B fill:#e1f5ff
>     style C fill:#e1ffe1
> ```

---

## ⚠️ Seguridad

> [!danger]
> - Trabaja con fuente DC dual ±15 V.
> - Manipula conexiones solo con la fuente apagada.
> - Verifica polaridad de alimentación del LM358 antes de energizar.

---

## 🧰 Materiales

> [!note] 📦 Procedimiento 1 — Filtro Activo
>
> | Material | Especificación |
> |---|---|
> | Fuente DC | Dual ±15 V |
> | Multímetro | FLUKE 179 |
> | Osciloscopio | GW INSTEK |
> | Generador de funciones |  |
> | Op-Amp | LM358 (U1, U2) |
> | Resistencias | R1=10 KΩ, R2=10 KΩ, R3=10 KΩ, R4=1 KΩ |
> | Capacitor | C1=10 nF |
>
> [!note] 📦 Procedimiento 2 — Acondicionador de Señal
>
> | Material | Especificación |
> |---|---|
> | Op-Amp | LM358 (U1, U2) |
> | Resistencias | R1=10 KΩ, R2=5 KΩ, R3=R4=R5=10 KΩ |
> | Potenciómetro | R6=10 KΩ |

---

## 📖 Introducción Teórica

> [!note] 🔵 OPAMP — Amplificador Operacional
>
> Circuito integrado con 2 entradas (+) no inversora y (-) inversora, y 1 salida. Entrada de alta impedancia, salida de baja impedancia, ganancia de lazo abierto idealmente infinita.
>
> |Configuración|Fórmula|Propiedades|
> |---|---|---|
> |**Inversor**|$V_o/V_{in} = -R_F/R_1$|Desfase 180°, ganancia negativa|
> |**No inversor**|$V_o/V_{in} = 1 + R_F/R_1$|En fase, ganancia ≥ 1|
> |**Sumador inversor**|$V_o = -R_F(R_1^{-1}v_1 + R_2^{-1}v_2 + \ldots)$|Suma ponderada invertida|
> |**Restador**|$V_o = (R_4/(R_3+R_4))((R_1+R_2)/R_1)v_2 - (R_2/R_1)v_1$|Si R4=R2 y R1=R3, resta directa|
>
> [!note] 🟢 Filtros pasivos RC
>
> **Filtro pasa alto** — permite frecuencias mayores a $f_L$:
>
> $$f_L = \frac{1}{2\pi R C}$$
>
> **Filtro pasa bajo** — permite frecuencias menores a $f_H$:
>
> $$f_H = \frac{1}{2\pi R C}$$
>
> Los filtros activos agregan un OPAMP para ganancia y aislamiento de impedancia.

---

## ⚙️ Procedimiento 1 — Filtro Activo

> [!tip] 🔧 Pasos
>
> 1. Armar circuito con LM358, resistencias y capacitor.
> 2. Usar fuente DC a 5 V como representación del transmisor universal.
> 3. Configurar generador de funciones: seno sinusoidal 2 Vpp para el ruido.
> 4. Variar frecuencia desde 10 KHz hasta 1 MHz.
> 5. Conectar puntas del osciloscopio en nodos "Vsum" y "Vo".
> 6. Completar la tabla.
>
> [!note] 📊 Tabla 2 — Respuesta del filtro
>
> |Frecuencia ruido|$V_{o(pp)}$|$V_{sum(pp)}$|Ganancia normalizada ($V_o/V_{sum}$)|Ganancia (dB)|$V_{sum}$ (DC)|$V_o$ (DC)|
> |---|---|---|---|---|---|---|
> |10 KHz| | | | | | |
> |50 KHz| | | | | | |
> |100 KHz| | | | | | |
> |1 MHz| | | | | | |
>
> [!question]- ❓ Análisis
>
> - ¿Qué tipo de filtro se está utilizando y cuál es su frecuencia de corte?
> - ¿Cuál es la ganancia aproximada en dB en la región pasa banda?
> - ¿Por qué existe un voltaje DC durante todo el barrido de frecuencia?

---

## ⚙️ Procedimiento 2 — Acondicionador de Señal

> [!tip] 🔧 Pasos
>
> 1. Armar circuito acondicionador con LM358.
> 2. Fuente DC dual ±15 V.
> 3. Ajustar potenciómetro R6 para obtener salida en rango -5 V a 5 V cuando el transmisor trabaje en 0 V a 10 V.
> 4. Completar la tabla.
>
> [!note] 📊 Tabla 1 — Acondicionador
>
> |$V_{in}$|$V_o$|
> |---|---|
> |0 V|-5 V|
> |1 V| |
> |2 V| |
> |4 V| |
> |5 V| |
> |7 V| |
> |8 V| |
> |10 V|5 V|
>
> [!question]- ❓ Análisis
>
> - ¿A cuánto se debe ajustar R6 para cumplir las especificaciones?
> - Escribir la función de transferencia $V_o = f(V_{in})$ y graficarla.
> - Analizar la funcionalidad de R2 y R6 en la transferencia.

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
> - [ ] Identifico las entradas (+) y (-) del LM358 y verifico la conexión correcta en el montaje.
> - [ ] Uso fuente dual ±15 V para alimentar el OPAMP y verifico los voltajes con el multimetro.
> - [ ] Calculo $f_c = 1/(2\pi RC)$ con los valores R y C del filtro y la comparo con la frecuencia medida.
>
> [!note] Nivel Intermedio
> - [ ] Observo en el osciloscopio cómo el filtro atenúa frecuencias altas de ruido en Vo vs Vsum.
> - [ ] Calculo la ganancia en dB usando $20 \cdot \log(V_o/V_{sum})$ y la registro en la tabla.
> - [ ] Ajusto el potenciómetro R6 del acondicionador para mapear 0–10 V a -5 V a +5 V.
>
> [!note] Nivel Avanzado
> - [ ] Verifico la linealidad de la función de transferencia del acondicionador con al menos 5 puntos.
> - [ ] Dibujo la gráfica Vo vs Vin e identifico pendiente y punto medio.
> - [ ] Explico por qué el voltaje DC persiste en todo el barrido de frecuencia del filtro.
>
> [!quote] 🔗 Conexiones
> - Teoría: [[02 - Aplicaciones de los OPAMs - Minimización de Ruido]], [[03 - Configuraciones Lineales Básicas del OPAM]] y [[04 - Integrador, Derivador y Circuitos No Lineales]]
> - Previa: [[Práctica 4 — Fuentes Lineales]]
> - Siguiente: [[Práctica 6 — Logica Combinatoria y Arduino]]

---

---

## 📎 Guía oficial (Garden)

![[PRÁCTICA # 5FUNCIONAMIENTO DE FILTROS ACTIVOS.pdf]]
**Tags:** #practica #laboratorio #EYAG1037 #FESD #ESPOL #unidad3 #OPAMP #filtro #LM358
