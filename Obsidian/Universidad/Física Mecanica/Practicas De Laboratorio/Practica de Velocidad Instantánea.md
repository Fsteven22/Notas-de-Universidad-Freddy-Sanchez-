## 🚀 Práctica: Velocidad Instantánea

### 📘 Contexto
Esta práctica se enfoca en determinar la velocidad de un cuerpo en un instante específico de su trayectoria, especialmente si se mueve con aceleración constante. La idea es ver cómo la velocidad media se acerca a la velocidad instantánea cuando el intervalo de tiempo es muy, muy pequeño.

---

### 📌 Variables Comunes
- **Posición** ($X_i$, $X_e$, $X_o$): Ubicaciones del carrito en la pista.
- **Desplazamiento** (\(\Delta x\)): Cambio en la posición.  
- **Tiempo** (\(t\)): Duración de un evento o movimiento.  
- **Velocidad instantánea** (\(v\)): La velocidad en un punto y momento exacto.  
- **Incertidumbre** (\(\delta x\), \(\delta t\), \(\delta \Delta x\)): Margen de error en las mediciones.

---

### ⚙️ Partes del Equipo (según diagrama y tabla de mediciones)
1. **Control / Interfaz digital** (identificado como '1'): unidad que interactúa con los sensores y el contador.  
2. **Sensores ópticos** ('2' y '3' en diagrama): detectan el paso de un objeto interrumpiendo un haz láser.  
3. **Contador digital** ('3' en imagen): cronometra los tiempos detectados por los sensores.  
4. **Pista y carrito** ('4' en diagrama, '1' en imagen): base de la trayectoria, inclinable para generar aceleración.  
5. **Placa obturadora** ('4' en imagen): se fija al carrito y activa los sensores.  
6. **Nivel digital** ('5'): mide el ángulo de inclinación de la pista.  
7. **Fin de carrera** ('6'): tope que evita que el carrito se caiga.  
8. **Cuña / Soporte** ('7'): inclinación de la pista.

---

### 🧾 Uso de Instrumentos y Mediciones
- Mediciones directas: ancho y altura del carrito, ángulo de inclinación.  
- **Tabla 3**: registra posiciones ($(X_i$), $(X_o$)), desplazamiento ($(\Delta x$)) y tiempo ($(t$)).  
- **Tabla 4**: clasifica variables  
  - *Directas*: ángulo, longitud, tiempo.  
  - *Indirectas*: aceleración, velocidad media, velocidad instantánea.

---

### 🧠 Explicación Teórica
La velocidad instantánea se define como:

$$
v = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t}
$$

Se representa como la pendiente de la línea tangente a la curva de posición vs. tiempo en un punto específico.

---

### 🧪 Explicación Práctica
Se simula un movimiento con aceleración constante. Midiendo tiempos en segmentos cada vez más pequeños ($(\Delta x$) reduce), la velocidad media:

$$
v_{\text{media}} = \frac{\Delta x}{\Delta t}
$$

se acerca a la velocidad instantánea en el tramo central.

---

### 🔗 Relación con Otros Temas
- **Cinemática**: desplazamiento, tiempo y velocidad media.  
- **Cálculo**: concepto experimental de derivada.  
- **Aceleración**: relacionada con la variación de la velocidad instantánea a lo largo del tiempo.

---

### 📊 Gráficas
1. **Posición vs. Tiempo**: curva para movimiento con aceleración constante (MRUV). La pendiente de la **tangente** en un punto = velocidad instantánea.  
2. **Velocidad vs. Tiempo**: recta si la aceleración es constante; su pendiente = aceleración.

---
## 🧪 Taller Previo – Velocidad Instantánea

### 1. ¿Qué es la velocidad instantánea?
Es la velocidad que tiene un cuerpo en un instante de tiempo determinado. Se obtiene como el límite de la velocidad media cuando el intervalo de tiempo tiende a cero:

$v = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t}$

---

### 2. ¿Cómo se mide experimentalmente la velocidad instantánea?
Se mide como la velocidad media cuando el intervalo de tiempo $\Delta t$ es muy pequeño:

$v_{\text{inst}} \approx \frac{\Delta x}{\Delta t}$

---

### 3. ¿Qué es el tiempo promedio?
Es el valor medio entre dos tiempos:

$t_{\text{prom}} = \frac{t_1 + t_2}{2}$

---

### 4. ¿Cómo se mide el tiempo en esta práctica?
Se mide con un sensor óptico que detecta cuándo una placa conectada al carrito interrumpe el haz de luz. El sistema registra el tiempo durante el cual la señal es bloqueada.

---

### 5. ¿Qué significa "variación de la posición"?
Es la diferencia de posición entre dos puntos:

$\Delta x = x_2 - x_1$

---

### 6. ¿Qué es una gráfica posición vs. tiempo?
Es una gráfica donde:
- El eje horizontal representa el tiempo $t$
- El eje vertical representa la posición $x$

Si el movimiento es acelerado, la gráfica será una curva (parábola).

---

### 7. ¿Qué se interpreta como pendiente de la tangente a la curva $x$ vs. $t$?
La pendiente de la tangente representa la velocidad instantánea:

$v = \frac{dx}{dt}$

---

### 8. ¿Qué representa el área bajo la curva de velocidad vs. tiempo?
Representa el desplazamiento realizado en ese intervalo de tiempo:

$\Delta x = \int_{t_1}^{t_2} v(t)\,dt$

---

### 9. ¿Qué representa la pendiente de la curva velocidad vs. tiempo?
Representa la aceleración:

$a = \frac{dv}{dt}$

---

### 10. ¿Qué expresa el modelo de movimiento uniformemente acelerado?
Modelo de posición:

$x(t) = x_0 + v_0 t + \frac{1}{2} a t^2$

Modelo de velocidad:

$v(t) = v_0 + a t$

---

### 11. ¿Cuál es el objetivo de esta práctica?
Determinar la velocidad instantánea de un cuerpo que se mueve con aceleración constante, usando mediciones de tiempo y posición con sensores ópticos.

---

### 12. ¿Qué conclusiones se obtienen de este modelo?
- Se puede estimar la velocidad instantánea con intervalos pequeños.
- La forma de la curva $x$ vs. $t$ permite analizar el movimiento.
- La aceleración se obtiene de la pendiente de la gráfica $v$ vs. $t$.

