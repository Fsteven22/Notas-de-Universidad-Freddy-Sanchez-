---
dg-publish: true
tags: [MATG1045, unidad5, razones-de-cambio-relacionadas, derivacion-implicita, regla-cadena, velocidad, fluidos, geometria-dinamica, modelado]
---

# 🔗 Razones de Cambio Relacionadas

## 🎯 Introducción

> [!info] 💡 Qué estudia esta nota
>
> Las **razones de cambio relacionadas** estudian cómo la velocidad de cambio de una variable se conecta con la de otra a través de una ecuación que las vincula. Si dos cantidades cambian con el tiempo y están ligadas por una fórmula, derivar esa fórmula respecto al tiempo entrega la relación entre sus velocidades.
>
> **Por qué importa:** es la aplicación más "traducible" de la derivación implícita: casi cualquier problema del mundo real —una escalera que se desliza, un tanque que se llena, un avión que pasa— es una ecuación con varias variables que hay que derivar en el tiempo.
>
> **Ejemplo:** una escalera de 10 m se apoya en una pared; si la base se aleja a 2 m/s, la ecuación $x^2 + y^2 = 100$ derivada en el tiempo revela que la punta baja a 1.5 m/s cuando la base está a 6 m.

> [!warning] ⚠️ Las tres trampas de este tipo de problemas
>
> 1. **Sustituir números antes de derivar:** si sustituyes $x = 6$ antes de derivar, la ecuación pierde la variable $x$ y su derivada desaparece. **Deriva primero, sustituye después.**
> 2. **Olvidar la regla de la cadena:** cada variable dependiente del tiempo aporta su factor $\frac{d}{dt}$; derivar $x^2$ sin escribir $2x\frac{dx}{dt}$ es el error más común.
> 3. **Interpretar mal el signo:** $\frac{dy}{dt} = -1.5$ m/s no es "un error negativo": indica que la altura **baja** a 1.5 m/s.
>
> **Por qué importa:** los tres errores son de procedimiento, no de cálculo; se corrigen con la metodología DERIVA y el checklist de verificación de esta nota.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Razón de cambio relacionada
>
> Si dos variables $x$ e $y$ están relacionadas por una ecuación $f(x, y) = 0$ y ambas cambian con respecto al tiempo $t$, entonces al derivar la ecuación respecto a $t$ se obtiene la **regla de la cadena aplicada al tiempo**:
>
> $$\frac{d}{dt}\big[f(x,y)\big] = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} = 0.$$
>
> Cada factor $\frac{dx}{dt}$ o $\frac{dy}{dt}$ es una **razón de cambio**; el problema consiste en que unas son conocidas y otra es la incógnita.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Razones_de_Cambio_Relacionadas_03.svg]]
>
> **Se lee así:** el diagrama arranca con la ecuación que vincula las variables y avanza por la derivación en el tiempo hasta la regla de la cadena, donde un rombo pregunta cuál de las dos razones se busca. Cada rama mete una razón como dato, ambas se juntan en la sustitución de los valores del instante y el flujo termina despejando la incógnita con verificación de unidades y signo.
>
> **Por qué importa:** el orden del diagrama es la defensa contra el error clásico: la sustitución llega **después** de la derivada. Además recuerda que solo una razón es incógnita; si metes dos desconocidas, el problema está mal planteado.
>
> **Ejemplo:** en $x^2 + y^2 = 100$, la regla da $2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$; conocido $\frac{dx}{dt} = 2$ en $x = 6$, $y = 8$, el diagrama lleva a $\frac{dy}{dt} = -1.5$ m/s.

> [!note] 📋 Definición — Metodología DERIVA
>
> El procedimiento estándar para resolver cualquier problema de razones relacionadas, en seis pasos:
>
> 1. **D**efinir todas las variables y sus unidades.
> 2. **E**stablecer la ecuación que relaciona las variables.
> 3. **R**elacionar mediante derivación implícita respecto al tiempo.
> 4. **I**dentificar los datos conocidos y lo que se busca.
> 5. **V**alores: sustituir los datos en el instante específico.
> 6. **A**nálisis: resolver para la incógnita y verificar unidades.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Razones_de_Cambio_Relacionadas_01.svg]]
>
> **Se lee así:** es una cadena recta de rectángulos numerados, sin decisiones, que reproduce los seis pasos de la nota: definir variables, dibujar el diagrama, establecer la ecuación, derivar implícitamente, identificar datos conocidos, sustituir valores, resolver para la incógnita y verificar la respuesta. El orden importa porque cada caja se apoya en la anterior.
>
> **Por qué importa:** el diagrama pone el dibujo y la ecuación antes que el cálculo, lo que elimina el error más frecuente (sustituir números antes de derivar). La última caja, la verificación, te obliga a revisar unidades y signo antes de entregar la respuesta.
>
> **Ejemplo:** con la escalera de 10 m defines $x$ y $y$, usas $x^2 + y^2 = 100$, derivas $x\frac{dx}{dt} + y\frac{dy}{dt} = 0$ y con $x = 6$, $y = 8$ obtienes $\frac{dy}{dt} = -1.5$ m/s.

---

## 🏃 Problemas de velocidad y persecución

> [!example] 🪜 Ejemplo guía: escalera deslizante
>
> **Enunciado:** una escalera de 10 m se apoya contra una pared vertical. Si la base se aleja de la pared a 2 m/s, ¿a qué velocidad baja la parte superior cuando la base está a 6 m de la pared?
>
> 1. **Variables:** $x$ = distancia de la base a la pared, $y$ = altura de la punta, $L = 10$ m (constante).
> 2. **Ecuación:** $x^2 + y^2 = L^2 = 100$.
> 3. **Derivación en el tiempo:** $2x\frac{dx}{dt} + 2y\frac{dy}{dt} = 0$, es decir $x\frac{dx}{dt} + y\frac{dy}{dt} = 0$.
> 4. **Datos del instante:** $\frac{dx}{dt} = 2$ m/s, $x = 6$ m, y $y = \sqrt{100 - 36} = 8$ m.
> 5. **Sustitución:** $6(2) + 8\frac{dy}{dt} = 0$ → $\frac{dy}{dt} = -\frac{12}{8} = -1.5$ m/s.
>
> **Respuesta:** la punta baja a 1.5 m/s (el signo negativo indica descenso).
>
> **Por qué importa:** es el problema-tipo de la nota: Pitágoras + regla de la cadena + sustitución al final. Todos los de geometría dinámica siguen este mismo esqueleto.

> [!example] 🚗 Persecución en línea recta
>
> **Enunciado:** el auto A va al este a 60 km/h y está a 200 m de la intersección; el auto B va al norte a 80 km/h y está a 150 m de la intersección. ¿A qué velocidad se acercan entre sí?
>
> - Relación: $d^2 = x_A^2 + x_B^2$; derivando, $2d\frac{dd}{dt} = 2x_A\frac{dx_A}{dt} + 2x_B\frac{dx_B}{dt}$.
> - Datos: $\frac{dx_A}{dt} = -60$ km/h, $\frac{dx_B}{dt} = -80$ km/h (negativos porque se acercan), $x_A = 0.2$ km, $x_B = 0.15$ km.
> - Distancia: $d = \sqrt{0.2^2 + 0.15^2} = 0.25$ km.
> - Cálculo: $\frac{dd}{dt} = \frac{0.2(-60) + 0.15(-80)}{0.25} = \frac{-12 - 12}{0.25} = -96$ km/h.
>
> **Respuesta:** los autos se acercan a 96 km/h.
>
> **Por qué importa:** la distancia entre dos objetos sigue el teorema de Pitágoras; el signo negativo aquí es correcto porque la distancia entre ellos disminuye.

> [!example] 🌥️ Sombra de una persona caminando
>
> **Enunciado:** una persona de 1.8 m camina a 1.5 m/s alejándose de un poste de luz de 6 m. ¿A qué velocidad crece la punta de su sombra?
>
> - Por triángulos semejantes: $\frac{6}{x+s} = \frac{1.8}{s}$, donde $x$ es la distancia al poste y $s$ la sombra.
> - Simplificando: $6s = 1.8x + 1.8s$ → $4.2s = 1.8x$ → $s = \frac{3}{7}x$.
> - Derivando: $\frac{ds}{dt} = \frac{3}{7}\frac{dx}{dt} = \frac{3}{7}(1.5) \approx 0.64$ m/s.
> - Punta de la sombra: $\frac{dx}{dt} + \frac{ds}{dt} = 1.5 + 0.64 = 2.14$ m/s.
>
> **Respuesta:** la punta de la sombra avanza a 2.14 m/s.
>
> **Por qué importa:** aquí hay dos velocidades y hay que sumarlas: la sombra crece **y** se desplaza con la persona. Distinguir "longitud de sombra" de "posición de la punta" es lo que decide el resultado.

---

## 🌊 Problemas de fluidos

> [!tip] 🧪 Características de los problemas de fluidos
>
> - **Conservación de volumen:** lo que entra es lo que sale (o la variación neta).
> - **Relaciones geométricas:** la forma del recipiente ata radio y altura.
> - **Velocidad de flujo:** $\frac{dV}{dt}$ es constante o se da como dato.
>
> **Por qué importa:** la clave es reducir el volumen a **una sola variable** (normalmente la altura del agua) antes de derivar.

> [!example] 🛢️ Tanque cónico
>
> **Enunciado:** un tanque cónico invertido (vértice hacia abajo) tiene radio superior 3 m y altura 6 m. Se llena con agua a 2 m³/min. ¿A qué velocidad sube el nivel cuando el agua tiene 4 m de profundidad?
>
> - Variables: $h$ = altura del agua, $r$ = radio de la superficie libre.
> - Semejanza de triángulos: $\frac{r}{h} = \frac{3}{6} = \frac{1}{2}$ → $r = \frac{h}{2}$.
> - Volumen: $V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi\left(\frac{h}{2}\right)^2 h = \frac{\pi h^3}{12}$.
> - Derivada en el tiempo: $\frac{dV}{dt} = \frac{\pi h^2}{4}\frac{dh}{dt}$.
> - En $h = 4$: $2 = \frac{\pi \cdot 16}{4}\frac{dh}{dt} = 4\pi\frac{dh}{dt}$.
>
> **Respuesta:** $\frac{dh}{dt} = \frac{1}{2\pi} \approx 0.159$ m/min.
>
> **Por qué importa:** fíjate en que la velocidad de subida **no es constante**: aunque entre agua a ritmo fijo, $\frac{dh}{dt}$ depende de $h^2$, así que el nivel sube más rápido al principio (cuando el cono es angosto).

---

## 📐 Problemas geométricos dinámicos

> [!example] 🔺 Área de un triángulo equilátero variable
>
> **Enunciado:** los lados de un triángulo equilátero aumentan a razón de 3 cm/min. ¿A qué velocidad aumenta el área cuando el lado mide 10 cm?
>
> - Área: $A = \frac{\sqrt{3}}{4}s^2$; dato: $\frac{ds}{dt} = 3$ cm/min.
> - Derivada: $\frac{dA}{dt} = \frac{\sqrt{3}}{4}(2s)\frac{ds}{dt} = \frac{\sqrt{3}\,s}{2}\frac{ds}{dt}$.
> - En $s = 10$: $\frac{dA}{dt} = \frac{\sqrt{3} \cdot 10}{2}(3) = 15\sqrt{3} \approx 25.98$ cm²/min.
>
> **Respuesta:** el área crece a $15\sqrt{3} \approx 25.98$ cm²/min.

> [!example] 🎈 Superficie de un globo esférico
>
> **Enunciado:** un globo se infla y su radio aumenta a 5 cm/min. ¿A qué velocidad aumenta la superficie cuando el radio es 20 cm?
>
> - Superficie: $S = 4\pi r^2$; dato: $\frac{dr}{dt} = 5$ cm/min.
> - Derivada: $\frac{dS}{dt} = 8\pi r\frac{dr}{dt}$.
> - En $r = 20$: $\frac{dS}{dt} = 8\pi(20)(5) = 800\pi \approx 2513.3$ cm²/min.
>
> **Respuesta:** la superficie crece a $800\pi \approx 2513.3$ cm²/min.
>
> **Por qué importa:** los dos problemas anteriores comparten el patrón "una fórmula + derivada en el tiempo + sustituir el instante"; solo cambia la fórmula geométrica.

> [!info] 🖼️ Tipos de problema geométrico y su razón de cambio
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Razones_de_Cambio_Relacionadas_02.svg]]
>
> **Se lee así:** es un árbol de dos niveles: de la casilla de problemas geométricos dinámicos salen cuatro ramas —área, perímetro, ángulos y volúmenes— y cada una baja a un recuadro con el tipo de figura o de movimiento típico. De ahí, una última flecha lleva a la casilla con la razón de cambio que pide ese tipo de problema, como $\frac{dA}{dt}$ o $\frac{d\theta}{dt}$.
>
> **Por qué importa:** la estructura te dice qué escribir en la línea de la derivada: cada rama termina en una razón distinta. Te sirve para identificar de entrada si te piden área, perímetro, ángulo o volumen, y evita que busques una velocidad lineal donde la pregunta es angular.
>
> **Ejemplo:** en el problema del observador y el avión se pide la velocidad angular, así que tomas la rama de ángulos variables y su salida $\frac{d\theta}{dt}$ es exactamente la incógnita.

> [!example] ✈️ Observador y avión
>
> **Enunciado:** un avión vuela horizontalmente a 150 m/s y a 1000 m de altura. Un observador en tierra lo sigue con binoculares. ¿A qué velocidad angular giran cuando el avión está a 1200 m horizontalmente del observador?
>
> - Variables: $x$ = distancia horizontal, $\theta$ = ángulo de elevación; relación: $\tan\theta = \frac{1000}{x}$.
> - Derivada en el tiempo: $\sec^2\theta \frac{d\theta}{dt} = -\frac{1000}{x^2}\frac{dx}{dt}$.
> - En $x = 1200$: $\tan\theta = \frac{5}{6}$, así que $\sec^2\theta = 1 + \frac{25}{36} = \frac{61}{36}$.
> - Sustitución: $\frac{d\theta}{dt} = -\frac{1000(150)}{1200^2 \cdot \frac{61}{36}} \approx -0.0615$ rad/s.
>
> **Respuesta:** el binocular gira a $\approx 0.0615$ rad/s (el signo negativo indica que el ángulo disminuye según la convención elegida).
>
> **Por qué importa:** aquí la razón de cambio es **angular**: las unidades son rad/s, no m/s. Es justo la distinción que recuerda el árbol de tipos.

---

## ⚙️ Aplicaciones en física e ingeniería

> [!example] 🫁 Ley de Boyle-Mariotte
>
> **Enunciado:** para un gas ideal a temperatura constante, $PV = k$. Si la presión disminuye a 50 Pa/s cuando $V = 20$ m³ y $P = 100$ Pa, ¿a qué velocidad cambia el volumen?
>
> - Constante: $k = PV = 100 \times 20 = 2000$.
> - Derivada en el tiempo (producto): $P\frac{dV}{dt} + V\frac{dP}{dt} = 0$.
> - Datos: $\frac{dP}{dt} = -50$ Pa/s, $P = 100$ Pa, $V = 20$ m³.
> - Cálculo: $100\frac{dV}{dt} + 20(-50) = 0$ → $\frac{dV}{dt} = \frac{1000}{100} = 10$ m³/s.
>
> **Respuesta:** el volumen crece a 10 m³/s (el gas se expande al bajar la presión).

> [!example] 🚰 Flujo en tubería cónica
>
> **Enunciado:** en el extremo ancho de una tubería ($r_1 = 5$ cm) el agua corre a 2 m/s y acelera a 0.1 m/s². En el extremo angosto ($r_2 = 2$ cm), ¿cuál es la aceleración?
>
> - Ecuación de continuidad: $A_1 v_1 = A_2 v_2$ → $\pi(0.05)^2 v_1 = \pi(0.02)^2 v_2$.
> - Relación: $v_2 = \left(\frac{0.05}{0.02}\right)^2 v_1 = 6.25\, v_1$.
> - En el instante dado: $v_2 = 6.25(2) = 12.5$ m/s.
> - Derivada: $\frac{dv_2}{dt} = 6.25\frac{dv_1}{dt} = 6.25(0.1) = 0.625$ m/s².
>
> **Respuesta:** la aceleración en el extremo angosto es 0.625 m/s².
>
> **Por qué importa:** la conservación de masa convierte una relación entre velocidades en una relación entre aceleraciones al derivar: misma constante, un orden más.

> [!example] ⚡ Circuito RC
>
> **Enunciado:** en un circuito RC, $\frac{Q}{C} + R\frac{dQ}{dt} = V_0$ con $C = 0.01$ F, $R = 100$ Ω, $V_0 = 12$ V; en $t = 0$ la corriente es 0.1 A. ¿A qué velocidad cambia la corriente?
>
> - Corriente: $I = \frac{dQ}{dt}$; ecuación: $100Q + 100 I = 12$... simplificando: $\frac{Q}{0.01} + 100I = 12$ → $100Q + I = 0.12$.
> - Derivando respecto al tiempo: $100\frac{dQ}{dt} + \frac{dI}{dt} = 0$ → $100I + \frac{dI}{dt} = 0$.
> - En $t = 0$: $100(0.1) + \frac{dI}{dt} = 0$ → $\frac{dI}{dt} = -10$ A/s.
>
> **Respuesta:** la corriente cae a 10 A/s al inicio.
>
> **Por qué importa:** aquí la variable $Q$ no aparece sola: se deriva dos veces para llegar a la aceleración de la corriente. Es el caso donde más se confunde qué derivar.

> [!example] 🌈 Prisma rotatorio (ley de Snell dinámica)
>
> **Enunciado:** un rayo incide en un prisma de índice $n = 1.5$. Si el ángulo de incidencia aumenta a 0.02 rad/s cuando $\theta_1 = 30°$, ¿a qué velocidad cambia $\theta_2$?
>
> - Ley de Snell: $\operatorname{sen}\theta_1 = 1.5\operatorname{sen}\theta_2$ → $\operatorname{sen}\theta_2 = \frac{1}{3}$, $\theta_2 \approx 19.47°$.
> - Derivando: $\cos\theta_1 \frac{d\theta_1}{dt} = 1.5\cos\theta_2 \frac{d\theta_2}{dt}$.
> - Con $\cos\theta_2 = \sqrt{1 - \frac{1}{9}} = \frac{2\sqrt{2}}{3}$: $\frac{\sqrt{3}}{2}(0.02) = 1.5 \cdot \frac{2\sqrt{2}}{3}\frac{d\theta_2}{dt}$.
> - Cálculo: $\frac{d\theta_2}{dt} \approx 0.0122$ rad/s.
>
> **Respuesta:** el ángulo de refracción cambia a $\approx 0.0122$ rad/s.

> [!example] ⏱️ Péndulo simple
>
> **Enunciado:** un péndulo de longitud $L = 2$ m oscila. Cuando $\theta = 0.5$ rad y $\frac{d\theta}{dt} = -0.3$ rad/s, ¿cuál es la velocidad del extremo?
>
> - Posición: $x = L\operatorname{sen}\theta$, $y = L\cos\theta$.
> - Velocidades: $\frac{dx}{dt} = L\cos\theta \frac{d\theta}{dt}$, $\frac{dy}{dt} = -L\operatorname{sen}\theta \frac{d\theta}{dt}$.
> - En el instante: $\frac{dx}{dt} = 2\cos(0.5)(-0.3) \approx -0.527$ m/s y $\frac{dy}{dt} = -2\operatorname{sen}(0.5)(-0.3) \approx 0.287$ m/s.
> - Magnitud: $v = \sqrt{0.527^2 + 0.287^2} \approx 0.6$ m/s.
>
> **Respuesta:** la velocidad del extremo es $\approx 0.6$ m/s.
>
> **Por qué importa:** la razón angular $\frac{d\theta}{dt}$ se traduce en velocidades lineales con la geometría del péndulo; la velocidad total es la magnitud del vector velocidad.

---

## 🧠 Técnicas de estudio

> [!tip] 🎓 Mnemotecnias: RELACIONA y RAPID
>
> **RELACIONA:** **R**ecurre al diagrama siempre · **E**cuación que vincule las variables · **L**a derivada implícita aplicar · **A**ntes de sustituir, derivar · **C**uidado con los signos de dirección · **I**dentifica lo conocido y lo buscado · **O**rganiza los datos por momento · **N**o sustituyas números al principio · **A**naliza si la respuesta tiene sentido.
>
> **RAPID:** **R**ead — leer qué cambia · **A**ssign — asignar variables · **P**icture — dibujar el diagrama · **I**mplicit — derivar implícitamente · **D**etermine — sustituir y resolver.

> [!example] 📋 Plantilla de análisis
>
> **🎯 Objetivo:** ¿qué razón de cambio busco?
>
> **📋 Variables:** variable 1 = \_\_\_\_\_ (unidades \_\_\_\_\_), variable 2 = \_\_\_\_\_ (unidades \_\_\_\_\_), razón conocida $\frac{d\_\_\_}{dt} = \_\_\_\_\_$, razón buscada $\frac{d\_\_\_}{dt} = ?$
>
> **📐 Diagrama:** esquema con variables etiquetadas.
>
> **⚖️ Ecuación relacionante:** \_\_\_\_\_
>
> **🔄 Derivación en el tiempo:** $\frac{d}{dt}[\text{ecuación}] = $ \_\_\_\_\_
>
> **📊 Datos en el instante:** valores de variables y razones conocidas.
>
> **✅ Verificación:** unidades correctas · signo lógico · orden de magnitud razonable.

> [!warning] 🧮 Patrones de derivación que conviene tener a mano
>
> - **Pitágoras:** $x^2 + y^2 = c^2$ → $x\frac{dx}{dt} + y\frac{dy}{dt} = 0$.
> - **Área del triángulo:** $A = \frac{1}{2}bh$ → $\frac{dA}{dt} = \frac{1}{2}\left(b\frac{dh}{dt} + h\frac{db}{dt}\right)$.
> - **Volumen del cilindro:** $V = \pi r^2 h$ → $\frac{dV}{dt} = \pi\left(2rh\frac{dr}{dt} + r^2\frac{dh}{dt}\right)$.
> - **Producto en general:** derivar un producto exige la regla del producto **en el tiempo**, con un factor $\frac{d}{dt}$ en cada factor.
>
> **Por qué importa:** si la fórmula es de memoria, el problema se reduce a derivar bien y sustituir al final.

> [!note] ✅ Checklist de verificación
>
> - **Análisis dimensional:** ¿las unidades de la respuesta son las que pide el enunciado (m/s, rad/s, cm²/min)?
> - **Análisis de signos:** ¿el signo indica la dirección lógica del movimiento?
> - **Casos límite:** ¿qué pasa cuando una variable es 0 o muy grande?
> - **Sentido físico:** ¿la magnitud es razonable para el contexto?
>
> **Por qué importa:** un resultado con unidades equivocadas o un signo al revés suele delatar un error de planteamiento, no de aritmética.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Una escalera de 10 m se apoya en una pared. La base se aleja a 2 m/s. ¿A qué velocidad baja la punta cuando la base está a 6 m de la pared?
>
> > [!success]- ✅ Solución
> >
> > Ecuación: $x^2 + y^2 = 100$; derivada en el tiempo: $x\frac{dx}{dt} + y\frac{dy}{dt} = 0$.
> >
> > En $x = 6$: $y = \sqrt{100 - 36} = 8$ m; con $\frac{dx}{dt} = 2$:
> >
> > $$6(2) + 8\frac{dy}{dt} = 0 \quad \Rightarrow \quad \frac{dy}{dt} = -1.5 \text{ m/s}.$$
> >
> > **Respuesta:** la punta baja a 1.5 m/s (el signo negativo indica descenso).

> [!example] 📋 Planteamiento
>
> Una persona de 1.8 m camina a 1.5 m/s alejándose de un poste de 6 m. ¿A qué velocidad crece su sombra?
>
> > [!success]- ✅ Solución
> >
> > Semejanza: $\frac{6}{x+s} = \frac{1.8}{s}$ → $s = \frac{3}{7}x$.
> >
> > Derivando: $\frac{ds}{dt} = \frac{3}{7}(1.5) \approx 0.64$ m/s.
> >
> > **Respuesta:** la sombra crece a $\approx 0.64$ m/s (la punta, sumando el desplazamiento, va a 2.14 m/s).

> [!example] 📋 Planteamiento
>
> Un tanque cónico invertido (radio 3 m, altura 6 m) se llena a 2 m³/min. ¿A qué velocidad sube el nivel con 4 m de agua?
>
> > [!success]- ✅ Solución
> >
> > Semejanza: $r = h/2$; volumen: $V = \frac{\pi h^3}{12}$.
> >
> > Derivada: $\frac{dV}{dt} = \frac{\pi h^2}{4}\frac{dh}{dt}$; en $h = 4$:
> >
> > $$2 = \frac{\pi \cdot 16}{4}\frac{dh}{dt} = 4\pi\frac{dh}{dt} \quad \Rightarrow \quad \frac{dh}{dt} = \frac{1}{2\pi} \approx 0.159 \text{ m/min}.$$
> >
> > **Respuesta:** el nivel sube a $\approx 0.159$ m/min.

> [!example] 📋 Planteamiento
>
> Los lados de un triángulo equilátero crecen a 3 cm/min. ¿A qué velocidad crece el área cuando el lado mide 10 cm?
>
> > [!success]- ✅ Solución
> >
> > $A = \frac{\sqrt{3}}{4}s^2$ → $\frac{dA}{dt} = \frac{\sqrt{3}\,s}{2}\frac{ds}{dt}$.
> >
> > En $s = 10$: $\frac{dA}{dt} = \frac{\sqrt{3} \cdot 10}{2}(3) = 15\sqrt{3} \approx 25.98$ cm²/min.
> >
> > **Respuesta:** el área crece a $15\sqrt{3} \approx 25.98$ cm²/min.

> [!example] 📋 Planteamiento
>
> Un gas ideal a temperatura constante tiene $P = 100$ Pa y $V = 20$ m³; la presión baja a 50 Pa/s. ¿A qué velocidad cambia el volumen?
>
> > [!success]- ✅ Solución
> >
> > $PV = 2000$ → derivando el producto: $P\frac{dV}{dt} + V\frac{dP}{dt} = 0$.
> >
> > $$100\frac{dV}{dt} + 20(-50) = 0 \quad \Rightarrow \quad \frac{dV}{dt} = \frac{1000}{100} = 10 \text{ m³/s}.$$
> >
> > **Respuesta:** el volumen crece a 10 m³/s (el gas se expande).

> [!example] 📋 Planteamiento
>
> Un avión vuela a 150 m/s y 1000 m de altura. ¿A qué velocidad angular gira el observador cuando la distancia horizontal es 1200 m?
>
> > [!success]- ✅ Solución
> >
> > $\tan\theta = \frac{1000}{x}$ → $\sec^2\theta \frac{d\theta}{dt} = -\frac{1000}{x^2}\frac{dx}{dt}$.
> >
> > En $x = 1200$: $\tan\theta = \frac{5}{6}$ y $\sec^2\theta = \frac{61}{36}$.
> >
> > $$\frac{d\theta}{dt} = -\frac{1000 \cdot 150}{1200^2 \cdot \frac{61}{36}} = -\frac{150000 \cdot 36}{1440000 \cdot 61} \approx -0.0615 \text{ rad/s}.$$
> >
> > **Respuesta:** la velocidad angular es $\approx 0.0615$ rad/s.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino las variables de un problema de razones relacionadas y escribo su ecuación vinculante.
> - [ ] Derivo una ecuación respecto al tiempo aplicando la regla de la cadena a cada variable.
> - [ ] Sustituyo los datos **después** de derivar y resuelvo para la incógnita.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo problemas de escalera, sombra y persecución con la metodología DERIVA.
> - [ ] Modelo problemas de fluidos reduciendo el volumen a una sola variable antes de derivar.
> - [ ] Interpreto el signo y las unidades de la razón de cambio pedida (m/s, rad/s, cm²/min).

> [!note] 📋 Nivel Avanzado
>
> - [ ] Trato problemas de ángulos variables (observador-avión) derivando funciones trigonométricas en el tiempo.
> - [ ] Aplico la conservación de masa (continuidad) para relacionar velocidades y aceleraciones en tuberías.
> - [ ] Verifico cada respuesta con el checklist de unidades, signo y sentido físico.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 4: razones de cambio relacionadas.
> - R. Larson, *Cálculo* (Cengage), cap. 3: problemas de tasa de cambio relacionada.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 3: la regla de la cadena en el tiempo.
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]] — la técnica de derivación que sostiene esta nota.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — el fundamento de cada factor $\frac{dx}{dt}$.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/01 - Tasas de Cambio|01 - Tasas de Cambio]] — las tasas promedio e instantáneas de partida.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u5

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es la regla clave de un problema de razones relacionadas?::Derivar la ecuación vinculante respecto al tiempo con la regla de la cadena, y sustituir los datos **después** de derivar.
> - ¿Qué dice la metodología DERIVA?::Definir variables, establecer la ecuación, derivar respecto al tiempo, identificar datos, sustituir valores del instante y analizar/verificar la respuesta.
> - ¿Por qué la velocidad de subida del tanque cónico no es constante?::Porque $\frac{dV}{dt} = \frac{\pi h^2}{4}\frac{dh}{dt}$: la razón $\frac{dh}{dt}$ depende de $h$, y al llenarse el cono se ensancha.
> - ¿Cómo se distingue una razón angular de una lineal?::Por las unidades: rad/s para ángulos, m/s para longitudes; el árbol de tipos de la nota indica qué razón pide cada problema.
> - ¿Qué hacer si el resultado da signo negativo?::Interpretarlo: un signo negativo significa que la cantidad disminuye (la punta baja, la presión cae, el ángulo se cierra), no que haya error.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 4 - Derivadas/III - Derivadas Especiales/01 - Derivación Implícita|01 - Derivación Implícita]] — la técnica de derivar sin despejar que aquí se aplica en el tiempo.
> - [[Unidad 4 - Derivadas/II - Reglas de Derivación/02 - Regla de la Cadena|02 - Regla de la Cadena]] — el mecanismo que produce cada factor $\frac{dx}{dt}$.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/01 - Tasas de Cambio|01 - Tasas de Cambio]] — qué es una tasa de cambio y cómo se interpreta.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/03 - Aproximaciones Lineales y Diferenciales|03 - Aproximaciones Lineales y Diferenciales]] — predecir cambios pequeños con la razón de cambio.
> - [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/01 - Problemas de Optimización|01 - Problemas de Optimización]] — cuando además hay que maximizar o minimizar la cantidad modelada.
> - [[Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/01 - Volúmenes de Sólidos de Revolución|01 - Volúmenes de Sólidos de Revolución]] — la otra cara: acumular para recuperar volúmenes.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero el problema guía de la escalera hasta que el patrón "Pitágoras → derivar en el tiempo → sustituir al final" salga sin pensarlo.
> - Después salta a los problemas de fluidos y de ángulos: son los que más se parecen a los del parcial.
> - Cuando domines los tipos, resuelve los seis ejercicios propuestos sin mirar la plantilla.
> - En cada ejercicio, escribe **qué razón de cambio buscas, en qué unidades** y **qué ecuación la vincula** antes de tocar una derivada.

---

**Tags:** #MATG1045 #unidad5 #razones-de-cambio-relacionadas #derivacion-implicita #regla-cadena #velocidad #fluidos #geometria-dinamica #modelado
