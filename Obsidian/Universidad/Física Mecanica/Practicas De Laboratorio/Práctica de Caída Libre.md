## 🔧 Práctica: Caída Libre

### 🌍 Contexto

El objetivo es determinar experimentalmente el valor de la aceleración de la gravedad ($g$) al simular la caída libre de un cuerpo en laboratorio. Se busca verificar que:

- Un cuerpo en caída libre tiene aceleración constante.
    
- Su valor coincide con la gravedad terrestre ($g \approx 9.8,m/s^2$).
    

### 📊 Variables Comunes

- **Altura ($h$ o $X_f$)**: Distancia desde donde se suelta el objeto hasta el impacto. Variable independiente.
    
- **Tiempo ($t$)**: Tiempo que tarda en caer. Variable dependiente.
    
- **Posición inicial ($X_0$)**: Se toma comúnmente como 0.
    
- **Velocidad inicial ($V_0$)**: Para caída libre, $V_0 = 0$.
    
- **Aceleración ($a$)**: Se busca que sea la gravedad ($g$).
    
- **Incertidumbres ($\Delta h$, $\delta t$)**: Errores asociados a las mediciones.
    

### ⚖️ Procedimiento y Formulación

#### a. 🛏️ Partes del Equipo

1. **Soporte universal**: Sostiene disparador y sensor.
    
2. **Nueces / Abrazaderas**: Ajustan componentes al soporte.
    
3. **Contador digital**: Registra el tiempo entre señales.
    
4. **Esfera y disparador**: Permiten iniciar la caída y medir el tiempo.
    
5. **Sensor de recepción**: Detecta el impacto final.
    
6. **Flexómetro / Cinta**: Mide la altura de caída.
    
7. **Base del soporte**: Da estabilidad.
    
8. **Fuente de poder / Interfaz**: Alimenta componentes electrónicos.
    

#### b. 🔢 Mediciones Directas (Tabla 2)

- **Diámetro de la esfera**: Medido con calibrador.
    
- **Masa de la esfera**: Con balanza.
    
- **Radio del cilindro (si aplica)**: Instrumento adecuado.
    

#### c. ⌚ Mediciones de la Práctica (Tabla 3)

- **Altura ($h \pm \Delta h$)**: Desde donde se suelta la esfera.
    
- **Tiempo ($t \pm \delta t$)**: Duración de la caída.
    

#### d. 📊 Tipo de Mediciones (Tabla 4)

- **Directas**: Diámetro, masa, tiempo, altura.
    
- **Indirectas**: Pendiente (gráfica), gravedad (a partir de $h$ y $t$).
    

#### e. 📌 Notas Importantes

Registrar observaciones y situaciones imprevistas durante la toma de datos.

### 🧐 Explicación Teórica

La caída libre es un MRUV (Movimiento Rectilíneo Uniformemente Variado) con aceleración constante, donde la única fuerza es la gravedad:

$X_f = \frac{1}{2} a t^2 \Rightarrow h = \frac{1}{2} g t^2$

Objetivo: Comprobar que $a = g$.

### 🎓 Explicación Práctica

Se mide el tiempo que tarda en caer una esfera desde distintas alturas. Al graficar $h$ vs. $t$, se obtiene una curva. Para linealizar:

- Graficar $h$ vs. $t^2$
    
- La pendiente será $\frac{1}{2} g$ → permite hallar $g$ experimentalmente.
    

### 🍒 Relación con Otros Temas

- **Cinemática**: MRUV.
    
- **Gravedad**: Se determina su valor.
    
- **Energía**: Potencial gravitatoria se convierte en cinética.
    
- **Linealización de datos**: Relación cuadrática convertida a lineal ($h$ vs. $t^2$).
    

### 📈 Gráficas

- **$h$ vs. $t$**: Curva (parabólica).
    
- **$h$ vs. $t^2$**: Línea recta, pendiente $= \frac{1}{2} g$.
    

---

## 📖 Taller 2: Trabajo Previo - Linealización por Cambio de Variable

### 🌍 Contexto del Experimento

Estudiantes analizan la tensión de ruptura ($F$) de un cable al hacer girar un objeto de masa conocida ($m$). Registran:

- Longitud del cable ($L$)
    
- Periodo de giro ($T$)
    

#### Datos:

- Masa: $0.50 \pm 0.01,kg$
    

|L (m) ± 0.0005|T (s) ± 0.01|
|---|---|
|0.0800|0.17|
|0.3500|0.38|
|0.5000|0.42|
|0.7500|0.50|
|0.9500|0.56|

Modelo matemático:

$F = mg + \frac{4\pi^2 mL}{T^2}$

### 🤔 Preguntas y Respuestas

#### 1. Modelo $T = f(L)$

Despejando $T$:

$T^2 = \frac{4\pi^2 mL}{F - mg}$

$T = 2\pi \sqrt{\frac{mL}{F - mg}}$

#### 2. Graficar $T$ vs $L$

- Usar software
    
- Se espera curva
    

#### 3. ¿Relación lineal?

No. Es una relación de tipo raíz cuadrada.

#### a. Linealización: $T^2$ vs $L$

- Nueva variable dependiente: $Y = T^2$
    
- Nueva variable independiente: $X = L$
    
- Relación lineal: $T^2 = m L + b$ donde $m = \frac{4\pi^2 m}{F - mg}$ y $b = 0$
    

#### 4. Relación entre nuevas variables

Lineal directa: $T^2 \propto L$

#### 5. Comparación con $y = mx + b$

- **Pendiente**: $m = \frac{4\pi^2 m}{F - mg}$
    
- **Intercepto**: $b = 0$
    

#### 6. Tabla linealizada

|Observación|L (m) ± 0.0005|T (s) ± 0.01|T^2 (s^2)|
|---|---|---|---|
|1|0.0800|0.17|0.0289|
|2|0.3500|0.38|0.1444|
|3|0.5000|0.42|0.1764|
|4|0.7500|0.50|0.2500|
|5|0.9500|0.56|0.3136|

#### 7. Gráfica en hoja milimetrada

- Ejes: $T^2$ (Y), $L$ (X)
    
- Escala adecuada
    
- Trazar puntos, ejes y tendencia
    

#### 8. Otro método de linealización

- **Logarímico**:
    
    - Si $y = Ax^n$, usar: $\log(y)$ vs $\log(x)$
        
    - Si $y = Ae^{Bx}$, usar: $\ln(y)$ vs $x$
        

### 🧮 Explicación Teórica

Linealizar datos permite usar técnicas sencillas de análisis (rectas) para estudiar relaciones no lineales.

### 📅 Explicación Práctica

Se transforma una curva en una recta para facilitar el cálculo de constantes usando regresión lineal.

### 📊 Relación con Otros Temas

- **Dinámica circular**
    
- **Leyes de Newton**
    
- **Linealización** (clave del taller)
    
- **Propagación de errores y cifras significativas**
    

### 📈 Gráficas del Taller

- **Original ($T$ vs $L$)**: Curva
    
- **Linealizada ($T^2$ vs $L$)**: Línea recta, pendiente relacionada con $F$
    

---