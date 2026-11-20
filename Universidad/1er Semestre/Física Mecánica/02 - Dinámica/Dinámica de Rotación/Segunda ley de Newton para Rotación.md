---
dg-publish: true
tags: [FISG1001, unidad2, fisica-mecanica, dinamica, segunda-ley-de-newton-para-rotacion]
---

# ⚙️ Variante Rotacional de la Segunda Ley de Newton

> [!info] 🎯 Definición Fundamental La **variante rotacional de la Segunda Ley de Newton** es el principio fundamental que rige el movimiento de rotación. Establece que el **torque neto** que actúa sobre un objeto rígido es directamente proporcional a su **momento de inercia** y a la **aceleración angular** que produce. Es la versión rotacional de la fórmula $\sum F = ma$.

---

## 🔧 Variables y Magnitudes

> [!tip] 📏 Magnitudes Principales
>
> - **Torque neto** ($\sum \tau$): Suma de todos los torques en N⋅m
> - **Momento de inercia** ($I$): Resistencia rotacional en kg⋅m²
> - **Aceleración angular** ($\alpha$): Cambio de velocidad angular en rad/s²
> - **Fuerza tangencial** ($F_t$): Componente tangencial de la fuerza en N
> - **Radio** ($r$): Distancia desde el eje de rotación en m
> - **Aceleración tangencial** ($a_t$): Aceleración en el borde del objeto en m/s²

---

## 🧮 Fórmulas Fundamentales

> [!note] 📐 Ecuaciones Clave
>
> ### Ley Principal
>
> $$\sum \tau = I\alpha$$
>
> ### Relaciones con Movimiento Lineal
>
> - **Torque por fuerza tangencial**: $\tau = rF_t$
> - **Aceleración angular-tangencial**: $\alpha = \frac{a_t}{r}$
> - **Velocidad angular-tangencial**: $\omega = \frac{v_t}{r}$
>
> ### Analogía con Movimiento Lineal
>
> |**Lineal**|**Rotacional**|
> |---|---|
> |$\sum F = ma$|$\sum \tau = I\alpha$|
> |Fuerza ($F$)|Torque ($\tau$)|
> |Masa ($m$)|Momento de inercia ($I$)|
> |Aceleración ($a$)|Aceleración angular ($\alpha$)|

---

## 🎓 Marco Teórico

> [!abstract] 🧠 Principios Fundamentales
>
> **Relación Causa-Efecto:**
>
> - **Causa**: Torque neto ($\sum \tau$)
> - **Efecto**: Aceleración angular ($\alpha$)
> - **Resistencia**: Momento de inercia ($I$)
>
> **Proporcionalidad Directa:**
>
> - Mayor torque → mayor aceleración angular
> - Mayor momento de inercia → menor aceleración angular (para mismo torque)
>
> **Equivalencia Conceptual:** El momento de inercia es la "masa rotacional" que determina qué tan difícil es cambiar el estado de rotación de un objeto.

---

## 🔗 Diagrama Conceptual

> [!abstract] 📊 Mapa de Relaciones
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Segunda_ley_de_Newton_para_Rotación_01.svg]]
>
> **Se lee así:** La ecuación `τ neto = Iα` leída por roles: el **torque neto** es la causa, la **aceleración angular** es el efecto y el **momento de inercia I** es la resistencia. De ahí se deduce que **mayor τ → mayor α** (proporcionalidad directa) y que **mayor I → menor α**, porque I es la masa rotacional: dificulta cambiar la rotación. El diagrama cierra con la analogía `F · m · a` ↔ `τ · I · α`.
>
> **Por qué importa:** Establece la analogía lineal-rotacional como equivalencia exacta, no como semejanza: todo lo que se resolvió con `F = ma` se resuelve con `τ = Iα` cambiando las tres piezas. Es el marco mental de toda la unidad.

---

## 🛠️ Metodología de Resolución

> [!info] 🔄 Procedimiento Sistemático
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Segunda_ley_de_Newton_para_Rotación_02.svg]]
>
> **Se lee así:** El **procedimiento rotacional** en cuatro pasos: elegir el **eje de rotación**, hacer el **DCL con todas las fuerzas**, calcular el **torque de cada una** (`τ = rF sinθ`) y **sumar los torques con signo** para aplicar `τ = Iα` y resolver. El diagrama añade tres **casos clásicos**: el volante (I grande frena los cambios de ω), el yo-yo (el peso da torque por la cuerda) y la rueda acelerando (torque motor menos fricción).
>
> **Por qué importa:** La única diferencia real con el método lineal es el paso 3: no se suman fuerzas, se suman **torques**, y cada uno con su signo según el sentido de giro. Todo lo demás (eje, DCL, verificar) es idéntico.

---

## 🌍 Aplicaciones Prácticas

> [!example] 🎯 Casos de Estudio
>
> ### ⚡ Volante de Inercia
>
> - **Función**: Suavizar rotación en motores
> - **Principio**: Alto momento de inercia → resistente a cambios de velocidad angular
> - **Aplicación**: $I$ grande requiere $\tau$ grande para cambiar $\alpha$
>
> ### 🪀 Yo-yo Desenrollándose
>
> - **Fuerzas**: Peso del yo-yo y tensión de la cuerda
> - **Torques**: Peso no causa torque, tensión sí
> - **Resultado**: Aceleración angular controlada por la tensión
>
> ### 🚗 Rueda Acelerando
>
> - **Torque motor**: Aplicado en el eje
> - **Resistencia**: Momento de inercia de la rueda
> - **Efecto**: Aceleración angular proporcional al torque del motor

---

## 📊 Ejercicios Resueltos

> [!warning] 🧮 Problema 1: Péndulo Físico **Enunciado**: Un péndulo físico con momento de inercia $I$ se suelta desde un ángulo $\theta$. Encontrar la aceleración angular inicial.
>
> > [!success] ✅ Solución **Análisis de torque**: El peso actúa a distancia $L$ del eje $$\tau = -mgL\sin\theta$$
> > 
> > **Aplicación de la Segunda Ley**: $$\sum \tau = I\alpha$$ $$-mgL\sin\theta = I\alpha$$
> > 
> > **Aceleración angular inicial**: $$\alpha = -\frac{mgL\sin\theta}{I}$$
> > 
> > El signo negativo indica rotación hacia la posición de equilibrio.
>

> [!warning] 🧮 Problema 2: Cilindro en Plano Inclinado **Enunciado**: Cilindro sólido de masa $M$ y radio $R$ rueda sin deslizar por un plano inclinado de ángulo $\theta$. Encontrar la aceleración del centro de masa.
>
> > [!success] ✅ Solución **Fuerzas sobre el cilindro**:
> > 
> > - Peso: $Mg$ (hacia abajo)
> > - Normal: $N$ (perpendicular al plano)
> > - Fricción: $f$ (hacia arriba del plano)
> > 
> > **Ecuación lineal** ($\sum F = ma$): $$Mg\sin\theta - f = Ma$$
> > 
> > **Ecuación rotacional** ($\sum \tau = I\alpha$): $$fR = I\alpha = \frac{1}{2}MR^2\alpha$$
> > 
> > **Condición de rodadura**: $a = \alpha R$ $$f = \frac{1}{2}Ma$$
> > 
> > **Sustituyendo en ecuación lineal**: $$Mg\sin\theta - \frac{1}{2}Ma = Ma$$ $$Mg\sin\theta = \frac{3}{2}Ma$$
> > 
> > **Aceleración del centro de masa**: $$a = \frac{2g\sin\theta}{3}$$

---

## 📈 Análisis Gráfico

> [!tip] 📊 Gráfica Torque vs Aceleración Angular
>
> **Relación Lineal**: Para momento de inercia constante $$\tau = I\alpha$$
>
> **Características de la gráfica**:
>
> - **Tipo**: Línea recta que pasa por el origen
> - **Pendiente**: Igual al momento de inercia ($I$)
> - **Intercepto**: Cero (sin torque → sin aceleración angular)
>
> **Interpretación**:
>
> - Pendiente mayor → mayor momento de inercia → más difícil de acelerar
> - Pendiente menor → menor momento de inercia → más fácil de acelerar

---

## 🔗 Conexiones Temáticas

> [!note] 🌐 Relaciones Conceptuales
>
> ### [[Torque y Equilibrio Rotacional]]
>
> - **Dependencia**: La ley requiere calcular el torque neto
> - **Relación**: $\tau$ es la causa de la aceleración angular
>
> ### [[Momento de Inercia]]
>
> - **Papel**: Constante de proporcionalidad en la ley
> - **Significado**: Resistencia al cambio de rotación
>
> ### [[Cinemática Rotacional]]
>
> - **Aplicación**: Una vez conocida $\alpha$, se calcula $\omega$ y $\theta$
> - **Ecuaciones**: $\omega = \omega_0 + \alpha t$, $\theta = \omega_0 t + \frac{1}{2}\alpha t^2$
>
> ### Dinámica Lineal
>
> - **Analogía directa**: $\sum F = ma$ ↔ $\sum \tau = I\alpha$
> - **Conexión**: Movimiento de traslación y rotación simultáneos
>
> ### [[1er Semestre/Física Mecánica/01 - Cinemática/Cinemática Rotacional.md]]
>
> - **Relación**: El trabajo rotacional $W = \tau \Delta\theta$ cambia la energía cinética
> - **Conexión**: $K_{rot} = \frac{1}{2}I\omega^2$

---

## ⚖️ Casos Especiales

> [!abstract] 🎯 Condiciones Particulares
>
> ### Equilibrio Rotacional
>
> **Condición**: $\sum \tau = 0$ **Resultado**: $\alpha = 0$ (velocidad angular constante)
>
> ### Rotación Uniforme
>
> **Condición**: $\alpha = 0$ **Implicación**: $\sum \tau = 0$ (torques balanceados)
>
> ### Aceleración Angular Constante
>
> **Condición**: $\sum \tau = \text{constante}$ **Resultado**: Movimiento uniformemente acelerado

---

## 📝 Síntesis Clave

> [!summary] 🎯 Puntos Esenciales
>
> - **Ley fundamental**: $\sum \tau = I\alpha$ (equivalente rotacional de $F = ma$)
> - **Causa-efecto**: Torque neto causa aceleración angular
> - **Resistencia**: Momento de inercia determina la respuesta
> - **Metodología**: Diagrama libre → torques → momento de inercia → aplicar ley
> - **Aplicación universal**: Base de toda la dinámica rotacional

---

## 📚 Referencias y Enlaces

> [!quote]  🏷️ Sistema de Organización
>
>
>
> ### 🔗 Notas Relacionadas
>
> - Momento de Torsión (Torque)
> - [[Momento de Inercia]]
> - [[Cinemática Rotacional]]
> - [[1er Semestre/Física Mecánica/Practicas De Laboratorio/Práctica Segunda ley de Newton.md]]
> - [[1er Semestre/Física Mecánica/01 - Cinemática/Cinemática Rotacional.md]]
> - [[Centro de masa (CM)]]
> - [[Torque y Equilibrio Rotacional#Equilibrio Rotacional|Equilibrio Rotacional]]
>
> ### 📖 Temas Avanzados
>
> - Movimiento de Rodadura
> - Sistemas de Múltiples Cuerpos
> - Conservación del Momento Angular
> - Análisis de Máquinas Rotativas
 
 ### Tags

 #fisica #mecanica #segunda-ley-newton #dinamica-rotacional #torque #momento-inercia

**Tags:** #FISG1001 #fisica-mecanica #unidad2 #segunda-ley-de-newton-para-rotacion
