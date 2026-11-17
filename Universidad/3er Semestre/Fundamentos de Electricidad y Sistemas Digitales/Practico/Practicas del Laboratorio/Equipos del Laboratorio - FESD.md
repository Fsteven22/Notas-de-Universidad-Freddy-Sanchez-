---
tags: [EYAG1037, laboratorio]
dg-publish: true
---

# 🔬 Equipos del Laboratorio — FESD

> [!info] 📌 Sobre esta nota Esta nota cubre todos los equipos que se usan en las prácticas del Laboratorio de Electrónica. Sirve como referencia rápida antes de cada práctica.
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

> [!note] 📐 ¿Qué es y cómo funciona?
> 
> El tablero universal es la herramienta más básica para implementar cualquier circuito electrónico. Tiene filas y columnas de puntos de conexión con la siguiente lógica:
> 
> - **Primera y última fila** (marcadas con línea blanca): todos sus puntos son equipotenciales → se usan para VCC y GND.
> - **Puntos grandes**: aislados entre sí eléctricamente.
> - **Puntos pequeños alrededor de un punto grande**: comparten potencial con él (arriba, abajo, izquierda, derecha).
> 
> ![[../../Teórico/Unidad 0 - Guías y Ejercicios/Diagramas/Equipos_del_Laboratorio_-_FESD_01.svg]]
> 
> **Se lee así:** El diagrama muestra un punto grande del tablero y los cuatro puntos pequeños que se conectan a él: los puntos pequeños alrededor de un punto grande comparten su potencial. Es la regla de conexiones más básica del tablero universal.
> 
> **Por qué importa:** Tener claro qué puntos están unidos entre sí antes de armar evita cortos accidentales y «conexiones fantasma»: nodos que parecen correctos en el tablero pero no están eléctricamente unidos.
>
> > ⚠️ Los puntos grandes están **aislados entre sí**. No confundir con el protoboard.
> 
> ![[../../Teórico/Unidad 0 - Guías y Ejercicios/Figuras/Pasted image 20260525231332.png]]
> 
> **Se lee así:** La foto muestra el tablero universal real («Figura 1»): una placa azul con una rejilla de puntos negros de conexión y el rótulo «Universal Assembly Board», con las filas de los extremos marcadas para VCC y GND.
> 
> **Por qué importa:** Reconocer el tablero real (y no confundirlo con el protoboard, del apartado siguiente) es lo que te permite planificar dónde irá cada nodo antes de insertar componentes.

---

## 🟩 Protoboard

> [!note] 🔌 ¿Qué es y cómo funciona?
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
> ![[../../Teórico/Unidad 0 - Guías y Ejercicios/Figuras/Pasted image 20260525231403.png]]
> 
> **Se lee así:** La foto muestra el protoboard del laboratorio («Figura 3: Protoboard»): el Proto-Board PB-105 de Global Specialties, con las regletas blancas de 5 puntos al centro y las borneras de alimentación V1–V4 con tierra al medio en el borde superior.
> 
> **Por qué importa:** Ver el instrumento real te ayuda a no confundir las regletas centrales con las laterales de alimentación — el error clásico de este equipo, que ya advierte la tabla de conexiones correctas/incorrectas.

---

## ⚡ Fuente DC

> [!tip] 🔋 ¿Qué es y cómo se usa?
> 
> ![[../../Teórico/Unidad 0 - Guías y Ejercicios/Figuras/Pasted image 20260525231457.png]]
> 
> **Se lee así:** La foto muestra el panel frontal de la fuente DC GW INSTEK GPS-4303 («Figura 6»): el visor doble A/V en la parte superior, las perillas de CURRENT y VOLTAGE por canal, el botón rectangular de OUTPUT y las borneras de cada uno de sus 4 canales en la parte inferior.
> 
> **Por qué importa:** Localizar de un vistazo el botón de OUTPUT, el selector de canal y las borneras es el prerrequisito de la secuencia de encendido (calibrar sin conectar → conectar → OUTPUT) que evita energizar el circuito antes de tiempo.
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
>
> ![[../../Teórico/Unidad 0 - Guías y Ejercicios/Figuras/Pasted image 20260525231619.png]]
> 
> **Se lee así:** La figura muestra el cableado sobre la fuente GPS-4303 para obtener salidas duales e independientes («Figura 7»): los visores marcan el voltaje/corriente de los canales y los cables de colores van de las borneras a +Vcc1 (rojo, CH1(+)), 0V de referencia (verde, nodo común CH3(+)–CH1(−)) y −Vcc1 (azul, CH3(−)), además de las salidas independientes +Vcc2 (rojo) y 0V ref.2 (negro).
> 
> **Por qué importa:** Es el montaje en el que está basada la tabla de colores verde/rojo/azul del modo dual (+15 V / −15 V): usar la bornera GND como referencia en vez de ese nodo común entrega un ±Vcc equivocado y el circuito no arranca como esperas.

---

## 🔩 LCR

> [!note] 📏 ¿Qué es y cómo se usa?
> 
> ![[../../Teórico/Unidad 0 - Guías y Ejercicios/Figuras/Pasted image 20260525231710.png]]
> 
> **Se lee así:** La foto muestra el medidor LCR GW INSTEK LCR-816 («Figura 9: LCR»): pantalla LCD a la izquierda, teclado numérico y de funciones a la derecha, y las borneras para las pinzas de conexión en la parte inferior derecha.
> 
> **Por qué importa:** Identificar el equipo y sus borneras de pinzas es lo que permite medir inductancia de bobinas (su uso principal en el curso) sin dudar en el momento de conectarlo.
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

> [!tip] 📐 ¿Qué es y cómo se usa?
> 
> ![[../../Teórico/Unidad 0 - Guías y Ejercicios/Figuras/Pasted image 20260525231749.png]]
> 
> **Se lee así:** La foto muestra el multímetro FLUKE 179 de frente («Figura 10»): perilla selectora central con las posiciones de V, mV, Ω/capacitancia, continuidad, prueba de diodos y mA/A, los botones HOLD / MIN MAX / RANGE y las borneras inferiores (400 mA, 10 A, V/Ω y COM).
> 
> **Por qué importa:** Saber qué bornera corresponde a cada medición (mA o 10 A según la corriente, COM siempre como retorno) es lo que evita quemar el fusible interno — o el equipo — antes de conectarlo al circuito.
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
> ![[../../Teórico/Unidad 0 - Guías y Ejercicios/Figuras/Pasted image 20260525231848.png]]
> 
> **Se lee así:** La tabla reproduce las posiciones del selector del FLUKE 179 y su función de medición con rangos: V~/Hz (tensión CA), V—/Hz (tensión CC), m—V/temperatura, Ω/capacitancia, continuidad y prueba de diodos, mA y A con sus topes, y la nota al pie de que la CA se acopla en valor eficaz (RMS) hasta 1 kHz.
> 
> **Por qué importa:** Comparar esta tabla con la del apartado es el chequeo rápido para saber exactamente qué mide cada posición de la perilla antes de conectar — e interiorizar que los valores de CA son RMS.

---

## 📡 Generador de Funciones

> [!tip] 〰️ ¿Qué es y cómo se usa?
> 
> ![[../../Teórico/Unidad 0 - Guías y Ejercicios/Figuras/Pasted image 20260525231935.png]]
> 
> **Se lee así:** La foto muestra el generador de funciones METERMAN FG2C («Figura 92»): pantalla digital verde a la izquierda, teclado de frecuencias (×100, 10, 1K, 100, 10, 1) y perillas de FREQUENCY, SWEEP/RATE, MODULATION, DUTY/CMOD, OFFSET y AMPL, con la salida OUTPUT de 50 Ω al lado derecho.
> 
> **Por qué importa:** Identificar la salida de 50 Ω y la perilla AMPL (cuya atenuación se ajusta presionando o halando) es lo que permite sacar una señal con la amplitud correcta en vez de pelear con un nivel que no corresponde a lo esperado.
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

> [!tip] 📈 ¿Qué es y cómo se usa?
> 
> ![[../../Teórico/Unidad 0 - Guías y Ejercicios/Figuras/Pasted image 20260525232051.png]]
> 
> **Se lee así:** La foto muestra el panel frontal del osciloscopio GW INSTEK GDS-820C («Figura 15»): pantalla a la izquierda con las teclas F1–F5 al lado derecho, controles de VERTICAL (POSITION, VOLTS/DIV y MATH) y HORIZONTAL (POSITION, TIME/DIV), y las entradas CH1 y CH2 en la parte inferior.
> 
> **Por qué importa:** Reconocer la ubicación de VOLTS/DIV, TIME/DIV y MATH te permite ajustar la escala de la señal y aplicar AUTOSET/MEASURE/CURSOR sin improvisar cuando la traza no se ve como esperabas.
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