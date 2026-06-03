# 🔬 Equipos del Laboratorio — FESD

> [!info]- 📌 Sobre esta nota Esta nota cubre todos los equipos que se usan en las prácticas del Laboratorio de Electrónica. Sirve como referencia rápida antes de cada práctica.
> 
> |Equipo|Función principal|
> |---|---|
> |Tablero Universal|Armar circuitos sin soldar|
> |Protoboard|Probar circuitos en etapa inicial|
> |Fuente DC|Alimentar circuitos con voltaje continuo|
> |LCR|Medir R, C, L con precisión|
> |Multímetro|Medir voltaje, corriente, resistencia, etc.|
> |Generador de Funciones|Generar señales AC de distintas formas|
> |Osciloscopio|Visualizar señales en el tiempo|

---

## 🟦 Tablero Universal

> [!note]- 📐 ¿Qué es y cómo funciona?
> 
> El tablero universal es la herramienta más básica para implementar cualquier circuito electrónico. Tiene filas y columnas de puntos de conexión con la siguiente lógica:
> 
> - **Primera y última fila** (marcadas con línea blanca): todos sus puntos son equipotenciales → se usan para VCC y GND.
> - **Puntos grandes**: aislados entre sí eléctricamente.
> - **Puntos pequeños alrededor de un punto grande**: comparten potencial con él (arriba, abajo, izquierda, derecha).
> 
> ```mermaid
> graph LR
>     A[Punto Grande] --- B[↑ pequeño]
>     A --- C[↓ pequeño]
>     A --- D[← pequeño]
>     A --- E[→ pequeño]
>     style A fill:#fff4e1
> ```
> 
> > ⚠️ Los puntos grandes están **aislados entre sí**. No confundir con el protoboard.
> 
> ![[Pasted image 20260525231332.png]]

---

## 🟩 Protoboard

> [!note]- 🔌 ¿Qué es y cómo funciona?
> 
> El protoboard es muy similar al tablero universal y se usa para la **primera etapa de prueba** de cualquier proyecto electrónico. Su lógica de conexión es:
> 
> - **Regletas centrales (5 puntos)**: continuidad **horizontal** — los 5 puntos de cada regleta están conectados entre sí.
> - **Regletas laterales (2 columnas)**: continuidad **vertical** — se usan para VCC (+) y GND (−).
> 
> **Conexiones correctas vs. incorrectas:**
> 
> |Situación|Resultado|
> |---|---|
> |Resistencia con pines en **distintas** regletas|✅ Correcto|
> |Resistencia con ambos pines en la **misma** regleta|❌ Cortocircuito|
> 
> > 💡 Usar el programa **Fritzing** para simular conexiones antes de armar físicamente.
> 
> ![[Pasted image 20260525231403.png]]

---

## ⚡ Fuente DC

> [!tip]- 🔋 ¿Qué es y cómo se usa?
> 
> ![[Pasted image 20260525231457.png]]
> La fuente DC (modelo **GW INSTEK GPS-4303**) entrega corriente continua para alimentar circuitos. Tiene **4 canales** independientes:
> 
> |Canal|Voltaje|Corriente máx.|
> |---|---|---|
> |CH1 y CH2|0 – 30 V|0 – 3 A|
> |CH3|0 – 5.2 V|1 A|
> |CH4|8 – 15 V|1 A|
> 
> **Secuencia de encendido (importante):**
> 
> 1. Presionar el botón **circular grande** → enciende solo el panel frontal para calibrar.
>     
> 2. Ajustar voltaje y corriente deseados **sin conectar el circuito**.
>     
> 3. Conectar el circuito.
>     
> 4. Presionar el botón **rectangular (OUTPUT)** → la fuente entrega energía al circuito.
>     
> 
> > ⚠️ Nunca energizar el circuito antes de calibrar. Puede dañar componentes o causar accidentes.
> 
> **Modo dual (+Vcc / −Vcc):**
> 
> Para obtener voltaje simétrico (ej. +15V y −15V):
> 
> - Conectar un cable entre el **positivo de CH3** y el **negativo de CH1** → ese nodo es la **referencia (0V)**.
> - El positivo de CH1 será **+Vcc**.
> - El negativo de CH3 será **−Vcc**.
> - No usar la bornera GND como referencia en modo dual.
> 
> |Cable|Color convención|Nodo|
> |---|---|---|
> |Verde|Referencia (0V)|CH3(+) — CH1(−)|
> |Rojo|+Vcc|CH1(+)|
> |Azul|−Vcc|CH3(−)|
> ![[Pasted image 20260525231619.png]]

---

## 🔩 LCR

> [!note]- 📏 ¿Qué es y cómo se usa?
> 
> ![[Pasted image 20260525231710.png]]
> El **LCR** (modelo GW INSTEK) es un medidor de impedancias de alta precisión. Mide:
> 
> |Magnitud|Símbolo|Unidad|
> |---|---|---|
> |Resistencia|R|Ω|
> |Capacitancia|C|F|
> |Inductancia|L|H|
> 
> **Uso básico:**
> 
> 1. Encender el LCR.
>     
> 2. Conectar el componente mediante las **pinzas**.
>     
> 3. Leer el valor en la pantalla.
>     
> 
> > 💡 En el curso se usa principalmente para medir **inductancia de bobinas**.

---

## 🟡 Multímetro

> [!tip]- 📐 ¿Qué es y cómo se usa?
> 
> ![[Pasted image 20260525231749.png]]
> El **multímetro FLUKE 179** mide múltiples variables eléctricas. Se opera con una **perilla selectora** y las borneras correctas según la medición.
> 
> **Borneras:**
> 
> |Medición|Bornera +|Bornera −|
> |---|---|---|
> |Voltaje / Resistencia / Continuidad|V / Ω|COM|
> |Corriente ≤ 400 mA|mA|COM|
> |Corriente ≤ 10 A|10A|COM|
> 
> **Variables que puede medir:**
> 
> |Posición|Variable|
> |---|---|
> |V~|Tensión CA (30 mV – 1000 V)|
> |V—|Tensión CC (1 mV – 1000 V)|
> |mV—|Tensión CC en milivoltios|
> |Ω|Resistencia (0.1 Ω – 50 MΩ)|
> |⊣⊢|Capacitancia (1 nF – 9999 µF)|
> |)))|Continuidad (señal acústica < 25 Ω)|
> |→\||Prueba de diodos|
> |mA / A|Corriente AC y DC|
> 
> **Botones especiales:**
> 
> - **HOLD**: congela la lectura en pantalla (útil para valores oscilantes).
>     
> - **Botón amarillo**: alterna entre dos funciones del mismo selector (blanco/amarillo).
>     
> 
> > ⚠️ Al terminar, siempre regresar la perilla a **OFF** para no gastar la batería.
> > 
> > ⚠️ No exceder los 400 mA en la bornera mA — quema el fusible interno.
> 
> ![[Pasted image 20260525231848.png]]

---

## 📡 Generador de Funciones

> [!tip]- 〰️ ¿Qué es y cómo se usa?
> 
> ![[Pasted image 20260525231935.png]]
> El generador de funciones produce señales AC de distintas formas. Disponibles en el lab:
> 
> |Modelo|Frecuencia|Amplitud máx.|
> |---|---|---|
> |**Meterman**|0.1 Hz – 10 MHz|24 Vpp|
> |**GW INSTEK**|0.1 Hz – 10 MHz|24 Vpp|
> 
> **Formas de onda disponibles:**
> 
> - Sinusoidal ~
> - Triangular △
> - Cuadrada □
> 
> **Parámetros configurables:** frecuencia, amplitud (Vpp), offset, duty cycle, fase.
> 
> **Uso del Meterman:**
> 
> - La atenuación se ajusta presionando o halando la perilla **AMPLITUDE**.
> 
> **Uso del GW INSTEK:**
> 
> - Configurar con los **botones numéricos**.
> - La salida se toma de la bornera **MAIN**.
> - Presionar **OUTPUT** para habilitar la salida.
> - Usar cable **BNC – lagarto** en el puerto de **50 Ω**.
> 
> **Cable BNC – lagarto:**
> 
> |Lagarto|Color|Función|
> |---|---|---|
> |Rojo|+|Señal positiva|
> |Negro|−|Referencia (GND)|

---

## 📺 Osciloscopio

> [!tip]- 📈 ¿Qué es y cómo se usa?
> 
> ![[Pasted image 20260525232051.png]]
> El **osciloscopio GW INSTEK GDS-820C** es un instrumento de medición gráfico que muestra señales en el dominio del tiempo.
> 
> **Especificaciones:**
> 
> - Ancho de banda: **150 MHz**
> - Muestreo: **25 GSa/s** (1 muestra cada 40 ps)
> - Sensibilidad vertical: **2 mV/div – 5 V/div**
> - Sensibilidad horizontal: **1 ns/div – 10 s/div**
> - Canales: **CH1** y **CH2**
> 
> **Controles principales:**
> 
> |Control|Función|
> |---|---|
> |POSITION (vertical)|Desplaza la gráfica verticalmente|
> |VOLTS/DIV|Ajusta la escala de amplitud por canal|
> |MATH|Operaciones entre señales (suma, resta, FFT)|
> |TIME/DIV|Ajusta la escala temporal (ambos canales)|
> |POSITION (horizontal)|Desplaza la gráfica horizontalmente|
> |AUTOSET|Ajuste automático de escalas|
> |MEASURE|Muestra parámetros automáticos de la señal|
> |CURSOR|Coloca cursores manuales en la gráfica|
> 
> **Parámetros visibles con MEASURE:** Vpp, Vmin, Vmax, VRMS, frecuencia, período, duty cycle, tiempo de subida/bajada.
> 
> **Verificar puntas de prueba:**
> 
> 1. Conectar la punta en la ranura bajo las teclas F1–F5.
>     
> 2. Debe aparecer una **señal rectangular**.
>     
> 3. Si no aparece → la punta está fallando.
>     
> 
> > 💡 El lagarto de la punta de prueba se conecta siempre a la **referencia (GND)** del circuito.

---

**Tags:** #laboratorio #equipos #EYAG1037 #FESD #ESPOL #practica1