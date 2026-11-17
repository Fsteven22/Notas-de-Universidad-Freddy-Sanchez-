---
dg-publish: true
tags: [EYAG1037, unidad1, electricidad]
---

# 🔌 Principios de Generación de Energía Eléctrica

## 🎯 Introducción

> [!info]- 💡 ¿Cómo se genera la electricidad?
>
> La **generación de energía eléctrica** es el proceso de convertir otras formas de energía (mecánica, química, solar, térmica) en energía eléctrica utilizable. Este proceso es la base del suministro eléctrico en hogares, industrias y dispositivos electrónicos.
>
> **Analogía del mundo real:**
>
> - Generar electricidad es como llenar un tanque de agua: necesitas una fuente (río, lluvia, pozo) que convierta algo disponible en algo utilizable.
> - Cada tipo de generación usa una "fuente" diferente: sol, viento, agua, combustible.
>
> ![[../Unidad 0 - Guías y Ejercicios/Diagramas/02_-_Principios_de_Generacion_de_Energia_Electrica_01.svg]]
>
> ![[../Unidad 0 - Guías y Ejercicios/Figuras/ChatGPT Image 19 may 2026, 22_52_00.png]]
>
> **Principio universal:** Toda generación eléctrica se basa en la **Ley de Faraday** o en la **conversión directa de energía** (electroquímica, fotovoltaica).

---

## 🧲 Campo Magnético e Inducción — Orsted y Faraday

> [!note]- 📐 La Base de la Generación Mecánica
>
> **Hans Orsted (1820):** descubrió que una corriente eléctrica circulando por un conductor produce un campo magnético a su alrededor.
> 
> La **Ley de Faraday** establece que una fuerza electromotriz (fem) se induce en un conductor cuando el flujo magnético que lo atraviesa cambia con el tiempo.
>
> $$\mathcal{E} = -N \cdot \frac{d\Phi}{dt}$$
>
> Donde:
> - $\mathcal{E}$ = Fuerza electromotriz inducida (Voltios, V)
> - $N$ = Número de vueltas de la bobina
> - $\Phi$ = Flujo magnético (Webers, Wb)
> - $t$ = Tiempo (segundos, s)
>
> ![[../Unidad 0 - Guías y Ejercicios/Diagramas/02_-_Principios_de_Generacion_de_Energia_Electrica_02.svg]]
> 
> **Se lee así:** Flujograma en cadena de cuatro bloques: el movimiento mecánico provoca una variación del flujo magnético, esa variación induce una FEM ($\mathcal{E} = -N \cdot d\Phi/dt$) y la FEM produce corriente eléctrica en el circuito.
> 
> **Por qué importa:** Fija la causalidad de la generación electromagnética en un orden estricto — sin movimiento no hay $\Delta\Phi$, sin $\Delta\Phi$ no hay FEM y sin FEM no hay corriente —, el guion mental para analizar cualquier generador.
>
> **Regla de la mano derecha:**
> Apunta los dedos en la dirección del movimiento del conductor → el pulgar indica la dirección de la corriente inducida.

> [!note] 🖼️ Campo Magnético e Inducción — Orsted y Faraday
>
> ![[../Unidad 0 - Guías y Ejercicios/Figuras/ChatGPT Image 19 may 2026, 22_34_16.png]]
> 
> **Se lee así:** Infografía de la Ley de Faraday: muestra un imán acercándose a una bobina de $N$ espiras con un medidor que registra la FEM inducida, la ecuación $\mathcal{E} = -N \cdot d\Phi_B/dt$ con el significado de cada símbolo, el flujo $\Phi_B = \vec{B} \cdot \vec{A} = BA\cos\theta$ y los tres escenarios (imán que se acerca, que se aleja o que está quieto) con su efecto sobre la FEM. Cierra con la dirección de la FEM según la Ley de Lenz, aplicaciones (generadores, transformadores, micrófonos dinámicos, cargadores inalámbricos) y un resumen del proceso.
> 
> **Por qué importa:** Condensa en una sola lámina todo el argumento de la nota: sin cambio de flujo no hay FEM y el signo negativo es la Ley de Lenz. Conviene usarla como verificación rápida antes de aplicar $\mathcal{E} = -N \cdot d\Phi/dt$ en un problema.

---
## 🔄 Ley de Lenz

> [!warning]- 🔄 Ley de Lenz — El Signo Negativo de Faraday
>
> La **Ley de Lenz** establece que la corriente inducida siempre tiene una dirección tal que su campo magnético **se opone al cambio de flujo** que la originó. Es el significado físico del signo negativo en la ecuación de Faraday.
>
> $$\mathcal{E} = -N \cdot \frac{d\Phi}{dt} \quad \leftarrow \text{el "−" es la Ley de Lenz}$$
>
> **Enunciado simple:**
>
> > "La naturaleza se resiste a los cambios en el flujo magnético."
>
> ![[../Unidad 0 - Guías y Ejercicios/Diagramas/02_-_Principios_de_Generacion_de_Energia_Electrica_03.svg]]
> 
> **Se lee así:** Diagrama de dos ramas: si el flujo magnético **aumenta**, la corriente inducida crea un campo que se opone al aumento (campo inducido en sentido contrario al externo); si el flujo magnético **disminuye**, la corriente crea un campo que se opone a la disminución (campo inducido en el mismo sentido).
> 
> **Por qué importa:** Es la plantilla operativa de la Ley de Lenz: identificar si $\Phi$ aumenta o disminuye decide de un vistazo la dirección del campo inducido y, con la regla de la mano derecha, el sentido de la corriente.
>
> **Procedimiento para determinar la dirección de la corriente inducida:**
>
> | Paso | Acción |
> |---|---|
> | **1** | Identificar la dirección del campo magnético externo $\vec{B}$ |
> | **2** | Determinar si el flujo $\Phi = \vec{B} \cdot \vec{A}$ aumenta o disminuye |
> | **3** | El campo inducido debe **oponerse** al cambio: si $\Phi$ sube → $\vec{B}_{ind}$ apunta en contra; si baja → $\vec{B}_{ind}$ apunta igual |
> | **4** | Aplicar la regla de la mano derecha al campo inducido → esa es la dirección de la corriente |
>
> **Consecuencias prácticas:**
>
> | Aplicación | Efecto de Lenz |
> |---|---|
> | **Freno magnético** | Imán cayendo por tubo de cobre se frena (corrientes de Foucault opuestas al movimiento) |
> | **Transformador** | La corriente secundaria genera flujo opuesto al primario (regulación natural) |
> | **Motor** | La FEM de retroceso (back-EMF) limita la corriente cuando el motor acelera |
> | **Inductor** | Se opone a cambios bruscos de corriente → protege circuitos |
>
> **Ejemplo:**
>
> > Un imán de barra se acerca a una bobina con su polo Norte apuntando hacia ella.
> > El flujo $\Phi$ **aumenta**. Por Lenz, la bobina genera un campo que **se opone** al imán → la cara de la bobina más cercana se comporta como polo **Norte** (repele al imán). La corriente inducida circula en sentido antihorario vista desde el imán.
> > 

> [!note] 🖼️ Ley de Lenz
>
> ![[../Unidad 0 - Guías y Ejercicios/Figuras/ChatGPT Image 19 may 2026, 22_41_47.png]]
> 
> **Se lee así:** Infografía de la Ley de Lenz: enuncia que la corriente inducida genera un campo magnético que se opone a la variación del flujo que la produce y lo liga al signo − de Faraday. Desarrolla los dos casos — flujo que aumenta (imán se acerca) y flujo que disminuye (imán se aleja) — mostrando en cada uno el sentido de $I$ y del campo inducido frente al externo, y cierra con la idea clave: es conservación de la energía, con una regla visual rápida para orientar el campo inducido.
> 
> **Por qué importa:** Es el paso que más errores causa al resolver inducción: fijar el sentido de la corriente por "se opone al cambio" evita invertir el signo y fallar la dirección de la corriente inducida en los ejercicios de Lenz.

---
## ⚡ DC vs AC — Edison vs Tesla

> [!note]- 🏭 La Guerra de las Corrientes
>
> A finales del siglo XIX, dos sistemas compitieron por convertirse en el estándar mundial:
>
> | Característica | Corriente Continua (DC) | Corriente Alterna (AC) |
> |---|---|---|
> | **Defensor** | Thomas Edison | Nikola Tesla / Westinghouse |
> | **Forma de onda** | Constante (plana) | Senoidal |
> | **Transmisión** | Difícil a larga distancia | ✅ Eficiente con transformadores |
> | **Transformación** | No es fácil de transformar | ✅ Fácil cambiar voltaje |
> | **Ganador** | ❌ | ✅ Estándar mundial actual |
>
> **¿Por qué ganó AC?** Los transformadores permiten elevar el voltaje para transmitir con bajas pérdidas y luego reducirlo para uso doméstico — algo imposible con DC en esa época.

---
## 🏭 Tipos de Generadores Eléctricos

> [!tip]- ⚙️ Generador AC vs Generador DC
>
> **Generador de Corriente Alterna (Alternador):**
>
> ![[../Unidad 0 - Guías y Ejercicios/Diagramas/02_-_Principios_de_Generacion_de_Energia_Electrica_04.svg]]
> 
> **Se lee así:** Diagrama de tres pasos: un rotor (imán) gira dentro del estátor (bobinas) y esa rotación entrega una salida AC senoidal.
> 
> **Por qué importa:** Ancla el principio del alternador — el movimiento relativo imán-bobina de Faraday materializado en un rotor que gira —, que es justo lo que explica por qué su salida es senoidal y no continua.
>
> **Generador de Corriente Continua (Dínamo):**
>
> ![[../Unidad 0 - Guías y Ejercicios/Diagramas/02_-_Principios_de_Generacion_de_Energia_Electrica_05.svg]]
>
> | Característica | Alternador (AC) | Dínamo (DC) |
> |---|---|---|
> | **Salida** | Corriente alterna senoidal | Corriente continua |
> | **Mantenimiento** | Bajo | Alto (escobillas) |
> | **Eficiencia** | ✅ Alta | Media |
> | **Uso típico** | Plantas eléctricas, automóviles | Tracción eléctrica, carga de baterías |

> [!note] 🖼️ Tipos de Generadores Eléctricos
>
> ![[../Unidad 0 - Guías y Ejercicios/Figuras/ChatGPT Image 19 may 2026, 22_46_01.png]]
> 
> **Se lee así:** Infografía comparativa de los dos tipos de generadores: el alternador (AC), con rotor imán que gira, forma de onda senoidal, frecuencia típica de 50/60 Hz y uso en redes, industrias y hogares; y el dínamo (DC), con conmutador rectificador, forma de onda constante y uso en baterías, cargadores y electrónica. Incluye fotografías, diagramas de funcionamiento, formas de onda y una comparación rápida AC vs DC.
> 
> **Por qué importa:** Hace visible la diferencia que resume la tabla de la nota — senoidal vs constante y el papel del conmutador —, justo lo que evalúan las metas al pedir diferenciar alternador y dínamo.

---
## 🔁 Proceso General de Generación

> [!info]- 🏭 De la Fuente a tu Enchufe
>
> ![[../Unidad 0 - Guías y Ejercicios/Diagramas/02_-_Principios_de_Generacion_de_Energia_Electrica_06.svg]]
>
> **Se lee así:** el proceso completo: materia prima → turbina → generador → transformador elevador → red de transmisión → transformador reductor → consumidor.
>
> **Por qué importa:** explica por qué hay plantas, por qué el voltaje sube para viajar y baja para el consumo, y dónde cortar primero cuando falla el suministro.

---
## 🌊 Fuentes de Generación Eléctrica

### 💧 Hidroeléctrica

> [!example]- 🏔️ Energía del Agua
>
> Convierte la energía **potencial del agua** en energía eléctrica mediante turbinas.
>
> ![[../Unidad 0 - Guías y Ejercicios/Diagramas/02_-_Principios_de_Generacion_de_Energia_Electrica_07.svg]]
>
> | Aspecto | Detalle |
> |---|---|
> | **Principio** | Energía potencial → cinética → eléctrica |
> | **Ventaja** | Renovable, sin emisiones, regulable |
> | **Desventaja** | Impacto ambiental, dependiente de lluvia |
> | **Ejemplo Ecuador** | Coca Codo Sinclair (~1 500 MW) |
> 
> ![[../Unidad 0 - Guías y Ejercicios/Figuras/Pasted image 20260519224024.png]]
> 
> **Se lee así:** Esquema de una central hidroeléctrica con sus partes numeradas: el embalse (1) acumula el agua, la presa (2) la regula, la tubería forzada (3) la conduce a presión, la turbina (4) convierte la energía potencial/cinética en giro mecánico, el generador eléctrico (5) la convierte en electricidad y la red eléctrica (6) la transporta.
> 
> **Por qué importa:** Ordena la cadena potencial → cinética → mecánica → eléctrica en pasos visibles, que es exactamente el principio de la tabla de la nota y la razón de que sea regulable pero dependiente de la lluvia.

### 🔥 Termoeléctrica

> [!example]- 🌡️ Energía del Calor
>
> Quema combustibles fósiles (gas, petróleo, carbón) para producir vapor que mueve turbinas.
>
> ![[../Unidad 0 - Guías y Ejercicios/Diagramas/02_-_Principios_de_Generacion_de_Energia_Electrica_08.svg]]
>
> | Aspecto | Detalle |
> |---|---|
> | **Principio** | Energía química → térmica → mecánica → eléctrica |
> | **Ventaja** | Alta disponibilidad, regulable a demanda |
> | **Desventaja** | Emisiones CO₂, uso de recursos no renovables |
> | **Eficiencia típica** | 33–45 % |
> 
> ![[../Unidad 0 - Guías y Ejercicios/Figuras/Pasted image 20260519224111.png]]
> 
> **Se lee así:** Esquema de una central termoeléctrica: el quemador calienta el agua en el generador de vapor (con chimenea y emisión de CO₂), el chorro de vapor mueve la turbina acoplada al alternador, el condensador enfría el vapor de nuevo a agua líquida usando agua del río, y el alternador entrega la energía a la red eléctrica.
> 
> **Por qué importa:** Muestra de dónde salen las emisiones y la dependencia de agua de una térmica convencional: el punto débil que señala la tabla (CO₂, recursos no renovables) está en la caldera, no en el generador.

### ☀️ Solar Fotovoltaica

> [!example]- 🌞 Energía del Sol
>
> Convierte directamente la luz solar en electricidad mediante el **efecto fotoeléctrico** en celdas semiconductoras de silicio.
>
> ![[../Unidad 0 - Guías y Ejercicios/Diagramas/02_-_Principios_de_Generacion_de_Energia_Electrica_09.svg]]
>
> | Aspecto | Detalle |
> |---|---|
> | **Principio** | Efecto fotovoltaico (fotón → par electrón-hueco) |
> | **Ventaja** | Renovable, sin emisiones, modular, bajo mantenimiento |
> | **Desventaja** | Intermitente (depende del sol), costo inicial alto |
> | **Eficiencia típica** | 15–22 % (paneles comerciales) |
> 
> ![[../Unidad 0 - Guías y Ejercicios/Figuras/Pasted image 20260519224443.png]]
> 
> **Se lee así:** Infografía de una planta fotovoltaica que numera el recorrido de la energía: (1) el sol emite radiación electromagnética, (2) los paneles de celdas absorben los fotones y liberan electrones (corriente continua, efecto fotoeléctrico), (3) los inversores transforman la DC en AC, (4) los transformadores elevan la tensión a media tensión (hasta 36 kV) y (5) las líneas de transmisión la distribuyen para el consumo.
> 
> **Por qué importa:** Aclara la cadena completa — DC en el panel, AC tras el inversor, media tensión tras el transformador — y por qué una instalación solar no puede verterse a la red sin inversores ni transformadores.

### 💨 Eólica

> [!example]- 🌬️ Energía del Viento
>
> Convierte la energía **cinética del viento** en electricidad mediante aerogeneradores.
>
> | Aspecto | Detalle |
> |---|---|
> | **Principio** | Energía cinética del viento → mecánica → eléctrica |
> | **Ventaja** | Renovable, sin emisiones, bajo costo operativo |
> | **Desventaja** | Intermitente, impacto visual y acústico |
> | **Potencia** | $P = \frac{1}{2} \rho A v^3$ (depende del cubo de la velocidad del viento) |
> 
> ![[../Unidad 0 - Guías y Ejercicios/Figuras/Pasted image 20260519224744.png]]
> 
> **Se lee así:** Ilustración de un parque eólico: una hilera de aerogeneradores instalados sobre una cresta de colinas recogen el viento y su producción baja por una red eléctrica común hasta una subestación o punto de conexión, desde donde se inyecta a las torres de transmisión.
> 
> **Por qué importa:** Representa el lado del recurso de $P = \frac{1}{2} \rho A v^3$: si el viento no es sostenido en el sitio, la potencia cae con el cubo de la velocidad y con ella la viabilidad del proyecto, la intermitencia que señala la tabla.

### ☢️ Nuclear

> [!example]- ⚛️ Fisión Nuclear
>
> Utiliza el calor generado por la **fisión de átomos de uranio** para producir vapor y mover turbinas.
>
> | Aspecto | Detalle |
> |---|---|
> | **Principio** | Fisión nuclear → calor → vapor → turbina → generador |
> | **Ventaja** | Alta densidad energética, sin emisiones de CO₂ |
> | **Desventaja** | Residuos radiactivos, alto costo, riesgos de seguridad |
> | **Eficiencia típica** | ~33 % |
> 
> ![[../Unidad 0 - Guías y Ejercicios/Figuras/Pasted image 20260519224818.png]]
> 
> **Se lee así:** Esquema (fuente: Foro Nuclear) del interior de una central nuclear: en el edificio de contención, el reactor calienta el agua y genera vapor en el generador de vapor; el vapor mueve la turbina acoplada al generador; el vapor se condensa en el condensador, enfriado por agua de refrigeración, y la torre de refrigeración expulsa el calor sobrante a la atmósfera.
> 
> **Por qué importa:** Muestra que la nuclear es otra termoeléctrica que solo cambia la fuente de calor — la fisión reemplaza a la caldera de combustible fósil —, lo que explica su alta densidad energética sin CO₂ y, a la vez, sus exigencias de contención y gestión de residuos.

---

## ⚖️ Comparación General de Fuentes

> [!warning]- 📊 Cuadro Comparativo
>
> | Fuente | Renovable | Emisiones CO₂ | Costo operativo | Disponibilidad | Uso en Ecuador |
> |---|---|---|---|---|---|
> | **Hidroeléctrica** | ✅ | Muy bajas | Bajo | Alta (depende de lluvia) | ✅ Predominante |
> | **Termoeléctrica** | ❌ | Altas | Alto | ✅ Constante | Complementaria |
> | **Solar** | ✅ | Nulas | Muy bajo | Media (sol) | Creciente |
> | **Eólica** | ✅ | Nulas | Muy bajo | Media (viento) | Limitada |
> | **Nuclear** | ❌/✅ | Nulas | Alto | ✅ Constante | No aplica |

---
## 🏗️ Sistema Eléctrico de Potencia

> [!tip]- 🔌 Etapas y Voltajes Típicos
>
> ![[../Unidad 0 - Guías y Ejercicios/Diagramas/02_-_Principios_de_Generacion_de_Energia_Electrica_10.svg]]
>
> | Etapa | Voltaje típico | Función |
> |---|---|---|
> | **Generación** | 13.8 kV | Alternador en la planta |
> | **Transmisión** | 230 – 500 kV | Transporte de energía a larga distancia |
> | **Subtransmisión** | 69 kV | Conexión a ciudades/industrias |
> | **Distribución** | 13.8 kV | Redes urbanas y rurales |
> | **Consumo** | 110 V / 220 V | Hogares y comercios |

---
  
## 📊 Resumen Visual 
> [!note] 🖼️ Resumen Visual
>
> ![[../Unidad 0 - Guías y Ejercicios/Diagramas/02_-_Principios_de_Generacion_de_Energia_Electrica_11.svg]]
>
> **Se lee así:** mapa mental «Generación Eléctrica»: principio base (Ley de Faraday, efecto fotovoltaico, reacción química), tipos de generador (alternador AC, dínamo DC), fuentes (hidro, termo, solar, eólica, nuclear) y sistema de potencia (generación → transmisión → distribución → consumo).
>
> **Por qué importa:** es el índice de la unidad de generación: cubre principio, máquinas, fuentes y el camino hasta el enchufe para repasar antes del examen.

## 📚 Referencias

> [!quote]- 📖 Fuentes consultadas
>
> [1] A. Hermosa Donante, *Electrónica Aplicada*, 1.ª ed. Mexico: Alfaomega Grupo Editor, 2013, pp. 1–30. ISBN-13: 9786077074045.
>
> [2] A. R. Hambley, *Electrical Engineering: Principles and Applications*, 7th ed. Hoboken, NJ, USA: Pearson, 2018, pp. 53–90.
>
> [3] J. J. Grainger y W. D. Stevenson, *Power Systems Analysis*, 4th ed. New York, USA: McGraw-Hill, 1994, pp. 1–35.
>
> [4] C. K. Alexander y M. N. O. Sadiku, *Fundamentals of Electric Circuits*, 6th ed. New York, USA: McGraw-Hill, 2016, pp. 39–70.
>
> [5] M. A. El-Sharkawi, *Electric Energy: An Introduction*, 3rd ed. Boca Raton, FL, USA: CRC Press, 2012, pp. 1–60.

## ✅ Metas de Aprendizaje
> [!note] Nivel Basico
>
> - [ ] Enuncio la Ley de Faraday E = -N·dF/dt y explico el rol del flujo magnetico.
> - [ ] Distingo entre energia primaria y energia electrica con ejemplos (hidro, solar, eolica).
> - [ ] Diferencio un alternador (AC) de un dinamo (DC) y por que gano AC.
>

> [!note] Nivel Intermedio
>
> - [ ] Aplico la Ley de Lenz para determinar la direccion de la corriente inducida.
> - [ ] Describo el proceso generacion -> transmision -> distribucion -> consumo con voltajes tipicos.
> - [ ] Comparo fuentes hidro, termo, solar, eolica y nuclear en renovabilidad y costo.
>

> [!note] Nivel Avanzado
>
> - [ ] Analizo el experimento de Orsted y predigo el campo inducido por una corriente.
> - [ ] Estimo la potencia eolica P = 1/2 rho A v3 y discuto su dependencia cubica.
> - [ ] Justifico la eleccion de una fuente segun disponibilidad y contexto de Ecuador.
>

---

## 🔗 Conexiones

> [!quote] 🔗 Conexiones
>
> - Previo: [[01 - Conceptos Fundamentales de la Electricidad]] — carga y campo base para induccion
> - Siguiente: [[03 - Elementos Basicos de un Circuito Electrico]] — del generador a los componentes
> - Relacionado: [[04 - Circuitos en Serie Paralelo y Mixtos]] — donde aplicas la energia generada

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../../Fundamentos de Electricidad y Sistemas Digitales|⚡ Mapa de contenido]]
> - Índice de la materia: [[../../Índice de Contenido|Índice de Contenido]]
> - Siguiente: [[03 - Elementos Basicos de un Circuito Electrico]]
> - Syllabus: [[../../Bienvenida y Syllabus Fundamentos de Electricidad y Sistemas Digitales|👋 Bienvenida y Syllabus]]

**Tags:** #generacion #electricidad #orsted #faraday #lenz #induccion #hidroelectrica #solar #eolica #termoelectrica #nuclear #EYAG1037 #FESD #ESPOL #unidad1
