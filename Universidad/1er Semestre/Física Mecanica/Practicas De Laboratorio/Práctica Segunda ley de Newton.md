# 🧪 Práctica: Segunda Ley de Newton

## 📚 Contexto

La práctica de la **Segunda Ley de Newton** busca comprobar experimentalmente esta ley fundamental de la física. El objetivo es verificar que, al aplicar distintas fuerzas netas sobre un sistema (con masa constante), se produce una aceleración directamente proporcional a la fuerza neta e inversamente proporcional a la masa. Se espera demostrar que la relación fuerza neta-aceleración es lineal cuando la masa es constante.

---

## ⚙️ Variables Comunes

- **Fuerza Neta** (_F_ o _Fₙₑₜₐ_): Suma vectorial de todas las fuerzas sobre un objeto o sistema. Causa de la aceleración.
    
- **Masa** (_m_): Cantidad de inercia del objeto, resistencia a cambiar su estado de movimiento.
    
- **Aceleración** (_a_): Cambio de velocidad por unidad de tiempo, efecto de la fuerza neta.
    
- **Tiempo** (_t_): Tiempo que tarda el objeto en recorrer una distancia o cambiar velocidad.
    
- **Distancia/Desplazamiento** (Δ_x_): Distancia recorrida por el objeto.
    
- **Incertidumbre** (δ_m_, δ_t_, δ_Δx_): Margen de error en las mediciones.
    

---

## 🛠️ Fórmulas / Procedimiento

### a. Partes del Equipo (según TABLA SEGUNDA LEY DE NEWTON.pdf e imagen)

|Número|Componente|Descripción|
|---|---|---|
|1|Control / Interfaz digital|Unidad principal que interactúa con sensores|
|2|Sensores ópticos|Detectan paso del objeto al interrumpir haz láser|
|3|Contador digital|Cronometra tiempos entre señales|
|4|Placa obturadora|Pieza unida al carrito que activa sensores|
|5|Carrito|Objeto que se mueve en la pista|
|6|Polea|Permite que cuerda con masas aplique fuerza|
|7|Pista de aire / riel|Superficie de baja fricción|
|8|Nivelador / Pata ajustable|Ajusta horizontalidad de la pista|

### b. Uso de Instrumentos y Mediciones Directas (Tabla 2)

Llenar Tabla 2 con:

- Ancho del carrito (medido con instrumento adecuado)
    
- Longitud de la placa (medida)
    
- Masa del carrito + placa (balanza)
    
- Masa total del sistema (carrito + placa + masas adicionales)
    

### c. Mediciones de la Práctica (Tabla 3)

Registrar:

- Masa colgante (_m₍colg₎ ± δm_)
    
- Tiempos (_t₁ ± δt_, _t₂ ± δt_, etc.)
    
- Intervalos de tiempo (Δ_t₁_, Δ_t₂_)
    

### d. Tipo de Mediciones (Tabla 4)

- **Directas:** Masa, ancho carrito, tiempo
    
- **Indirectas:** Aceleración, velocidad, fuerza neta (calculadas)
    

### e. Notas Importantes

Registrar observaciones o imprevistos durante la toma de datos.

---

## 📖 Explicación Teórica

La Segunda Ley de Newton establece que la aceleración (_a_) es proporcional a la fuerza neta (￼￼Fₙₑₜₐ￼￼) e inversamente proporcional a la masa (_

Fₙₑₜₐ = m * a  

O despejando la aceleración:

a = Fₙₑₜₐ / m

Si la masa es constante, duplicar la fuerza neta duplica la aceleración; duplicar la masa reduce la aceleración a la mitad.

---

## 🔬 Explicación Práctica

En el laboratorio, se usa un carrito en pista de baja fricción conectado a una cuerda que pasa por una polea con masas colgantes que generan la fuerza neta. Se varía la masa colgante para cambiar la fuerza neta, se miden los tiempos para calcular aceleración y se grafica fuerza neta vs. aceleración. Si la masa es constante, se espera una línea recta cuya pendiente representa la masa del sistema.

---

## 🔗 Relación con Otros Temas

- Cinemática: aceleración calculada con distancia y tiempo
    
- Fuerzas: análisis de tensión, peso, fricción
    
- Diagramas de cuerpo libre: para identificar fuerzas
    
- Linealización de datos: relación lineal _Fₙₑₜₐ = ma_
    
- Propagación de errores: para incertidumbres en aceleración y fuerza
    

---

## 📊 Gráficas

Gráfica principal:  
**Fuerza Neta (Fₙₑₜₐ) [Y] vs Aceleración (a) [X]**  
Debe ser línea recta que pasa por el origen. La pendiente es la masa total (_m_).

---

# 📝 Ejemplo de Aplicación: Taller 3 - Incertidumbres y Comparación Teórico-Experimental

## 🔍 Contexto

Estudiantes determinan experimentalmente la **tensión de ruptura (F)** de un cable metálico rotando un objeto de masa conocida (m=0.50±0.01 kg) hasta romper el cable. Se registran longitud (_L_) y período de giro (_T_).

---

## 📐 Modelo Matemático

La tensión de ruptura _F_ está dada por:

$T = sqrt[ (F - mg) / (4 π² m) ] * sqrt(L)$  

Los estudiantes linealizan graficando _T_ vs _L^(1/2)_.

---

## ❓ Preguntas y Respuestas Clave

1. **Incertidumbres en puntos seleccionados (_P_a_, _P_b_):**
    
    - Incertidumbre en _X_ (para _L^(1/2)_) calculada por propagación de errores.
        
    - Incertidumbre en _Y_ (para _T_) directa.
        
2. **Pendiente e intercepto:** Calculados con reglas de cifras significativas y análisis.
    
3. **Ecuación empírica: _** $Y = mexp * X + b_exp$
    

Donde _Y = T_, _X = L^(1/2)_.

4. **Incertidumbre de pendiente e intercepto:** Cálculo detallado para evaluar fiabilidad.
    
5. **Variable de interés (Tensión de ruptura):** Se despeja _F_ igualando pendiente experimental con teórica.
    
6. **Incertidumbre y error porcentual:** Se calcula para validar precisión y exactitud.
    

---

## 📚 Explicación Teórica del Taller

Aplica propagación de errores en regresión lineal, linealización y comparación teórico-experimental mediante error porcentual.

---

## 🧪 Explicación Práctica del Taller

Capacita a estudiantes para:

- Cuantificar calidad de resultados
    
- Extraer parámetros físicos rigurosamente
    
- Evaluar validez experimental con valores teóricos
    

---

## 🔗 Relación con Otros Temas (Taller)

- Medición y errores
    
- Cifras significativas
    
- Graficación de datos
    
- Análisis de regresión lineal
    

---

## 📈 Gráficas (Taller)

Gráfica linealizada: _T_ vs _L^(1/2)_.  
Línea recta usada para calcular tensión de ruptura _F_.

---
