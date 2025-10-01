# Vectores 🧭

> [!quote] _"Los vectores son el lenguaje del espacio. Sin ellos, la física sería como tratar de describir una sinfonía sin notas musicales."_ - David Halliday

---

## 📋 Conceptos Fundamentales

> [!info]- 🎯 **Definición de Vector** Un vector es una cantidad que posee tanto magnitud (tamaño) como dirección en el espacio. Se representa gráficamente como una flecha que apunta en la dirección del vector, con longitud proporcional a su magnitud.
> 
> **Características principales:**
> 
> - **Magnitud:** |**v**| o ||**v**|| - longitud del vector (escalar positivo)
> - **Dirección:** Orientación en el espacio (ángulo respecto a referencias)
> - **Sentido:** Hacia dónde apunta la flecha
> - **Punto de aplicación:** Donde se origina (en algunos contextos)
> 
> **Notación:**
> 
> - Vector: **v**, $\vec{v}$, o v̅
> - Magnitud: |**v**|, ||**v**||, o v

> [!info]- 📏 **Escalares vs Vectores**
> 
> |Escalares|Vectores|
> |---|---|
> |Solo magnitud|Magnitud + dirección|
> |Masa, temperatura, tiempo|Velocidad, fuerza, desplazamiento|
> |Se suman aritméticamente|Se suman vectorialmente|
> |5 + 3 = 8|**a** + **b** ≠|
> 
> **Ejemplos:**
> 
> - **Escalares:** 25°C, 5 kg, 10 segundos
> - **Vectores:** 60 km/h hacia el norte, 10 N hacia arriba

## 🔢 Representaciones de Vectores

> [!tip]- 📐 **Representación Gráfica** Un vector se dibuja como una flecha donde:
> 
> - La **longitud** representa la magnitud
> - La **dirección** de la flecha indica la dirección
> - El **origen** es el punto de partida
> - La **punta** es el punto final
> 
> **Sistemas de coordenadas:**
> 
> - **2D:** Plano cartesiano (x, y)
> - **3D:** Espacio cartesiano (x, y, z)
> - **Polar:** (r, θ) en 2D
> - **Esférico:** (r, θ, φ) en 3D

> [!tip]- 🧮 **Representación por Componentes** En 2D: $$\vec{v} = v_x\hat{i} + v_y\hat{j}$$ En 3D: $$\vec{v} = v_x\hat{i} + v_y\hat{j} + v_z\hat{k}$$
> 
> **Vectores unitarios:**
> 
> - $\hat{i}$: dirección +x
> - $\hat{j}$: dirección +y
> - $\hat{k}$: dirección +z
> 
> **Magnitud desde componentes:** $$|\vec{v}| = \sqrt{v_x^2 + v_y^2 + v_z^2}$$
> 
> **Ángulo de dirección (2D):** $$\theta = \arctan\left(\frac{v_y}{v_x}\right)$$

## ➕ Operaciones con Vectores

> [!warning]- 🔧 **Suma de Vectores**
> 
> **Método gráfico - Regla del paralelogramo:**
> 
> 1. Dibujar ambos vectores desde el mismo origen
> 2. Completar el paralelogramo
> 3. La diagonal es el vector resultante
> 
> **Método gráfico - Regla punta-cola:**
> 
> 4. Dibujar el primer vector
> 5. Desde la punta del primero, dibujar el segundo
> 6. El vector del origen inicial a la punta final es la suma
> 
> **Método analítico:** $$\vec{A} + \vec{B} = (A_x + B_x)\hat{i} + (A_y + B_y)\hat{j} + (A_z + B_z)\hat{k}$$
> 
> **Propiedades:**
> 
> - Conmutativa: $\vec{A} + \vec{B} = \vec{B} + \vec{A}$
> - Asociativa: $(\vec{A} + \vec{B}) + \vec{C} = \vec{A} + (\vec{B} + \vec{C})$

> [!warning]- ➖ **Resta de Vectores** La resta es equivalente a sumar el vector opuesto: $$\vec{A} - \vec{B} = \vec{A} + (-\vec{B})$$
> 
> **Método analítico:** $$\vec{A} - \vec{B} = (A_x - B_x)\hat{i} + (A_y - B_y)\hat{j} + (A_z - B_z)\hat{k}$$

> [!warning]- ✖️ **Multiplicación por Escalar** Multiplicar un vector por un escalar cambia solo su magnitud: $$k\vec{A} = kA_x\hat{i} + kA_y\hat{j} + kA_z\hat{k}$$
> 
> **Efectos:**
> 
> - Si k > 1: el vector se alarga
> - Si 0 < k < 1: el vector se acorta
> - Si k < 0: el vector cambia de sentido
> - Si k = -1: vector opuesto

## 📊 Productos de Vectores

> [!info]- 🔴 **Producto Punto (Escalar)** El producto punto de dos vectores es un escalar: $$\vec{A} \cdot \vec{B} = |\vec{A}||\vec{B}|\cos\theta$$
> 
> **Método por componentes:** $$\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z$$
> 
> **Aplicaciones:**
> 
> - Encontrar el ángulo entre vectores: $$\cos\theta = \frac{\vec{A} \cdot \vec{B}}{|\vec{A}||\vec{B}|}$$
> - Proyección de **A** sobre **B**: $$\text{proj}_B A = \frac{\vec{A} \cdot \vec{B}}{|\vec{B}|}$$
> - Trabajo: $$W = \vec{F} \cdot \vec{d}$$
> 
> **Propiedades:**
> 
> - Si $\vec{A} \cdot \vec{B} = 0$, entonces $\vec{A} \perp \vec{B}$
> - $\vec{A} \cdot \vec{A} = |\vec{A}|^2$

> [!info]- ✖️ **Producto Cruz (Vectorial)** El producto cruz de dos vectores es otro vector perpendicular a ambos: $$\vec{A} \times \vec{B} = |\vec{A}||\vec{B}|\sin\theta,\hat{n}$$
> 
> **Método por componentes (determinante):** $$\vec{A} \times \vec{B} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \ A_x & A_y & A_z \ B_x & B_y & B_z \end{vmatrix}$$
> 
> $$\vec{A} \times \vec{B} = (A_yB_z - A_zB_y)\hat{i} - (A_xB_z - A_zB_x)\hat{j} + (A_xB_y - A_yB_x)\hat{k}$$
> 
> **Aplicaciones:**
> 
> - Torque: $$\vec{\tau} = \vec{r} \times \vec{F}$$
> - Campo magnético: $$\vec{F} = q\vec{v} \times \vec{B}$$
> - Área de paralelogramo: $$A = |\vec{A} \times \vec{B}|$$
> 
> **Propiedades:**
> 
> - Anti-conmutativo: $\vec{A} \times \vec{B} = -\vec{B} \times \vec{A}$
> - Si $\vec{A} \times \vec{B} = 0$, entonces $\vec{A} \parallel \vec{B}$

## 🧠 Técnica de Estudio: Método VAMOS

> [!tip]- 🎓 **Estrategia de Aprendizaje: Mnemotecnia VAMOS** Para problemas con vectores usa el método **VAMOS**:
> 
> **V - Visualizar** el problema gráficamente **A - Analizar** qué tipo de operación se necesita **M - Método** elegir entre gráfico o analítico **O - Operación** ejecutar los cálculos **S - Sentido** verificar que el resultado tenga sentido físico
> 
> **Reglas mnemotécnicas:**
> 
> - **"Suma cabeza-cola":** Para sumar vectores gráficamente
> - **"Producto punto = cos":** Para ángulos y proyecciones
> - **"Producto cruz = sin":** Para perpendiculares y áreas
> - **"Mano derecha":** Para dirección del producto cruz

## 📋 Aplicaciones en Física

> [!example]- 🎯 **Cinemática Vectorial**
> 
> ```mermaid
> graph TD
>    A[Vectores en Cinemática] --> B[Posición]
>    A --> C[Velocidad]
>    A --> D[Aceleración]
>    
>    B --> E["r⃗(t) = x(t)î + y(t)ĵ"]
>    C --> F["v⃗ = dr⃗/dt"]
>    D --> G["a⃗ = dv⃗/dt = d²r⃗/dt²"]
>    
>    H[Movimiento Proyectil] --> I["v⃗₀ = v₀cos(θ)î + v₀sin(θ)ĵ"]
>    H --> J["r⃗(t) = (v₀cos(θ)t)î + (v₀sin(θ)t - ½gt²)ĵ"]
>    
>    style A fill:#e1f5fe
>    style H fill:#f3e5f5
> ```

> [!example]- ⚖️ **Dinámica Vectorial** **Segunda Ley de Newton:** $$\sum \vec{F} = m\vec{a}$$
> 
> **En componentes:**
> 
> - $$\sum F_x = ma_x$$
> - $$\sum F_y = ma_y$$
> - $$\sum F_z = ma_z$$
> 
> **Equilibrio estático:** $$\sum \vec{F} = 0 \implies \sum F_x = 0, \sum F_y = 0, \sum F_z = 0$$

## 🧪 Problemas Resueltos

> [!example]- 💡 **Problema 1: Suma de Vectores** Dados $\vec{A} = 3\hat{i} + 4\hat{j}$ y $\vec{B} = -2\hat{i} + 5\hat{j}$, encontrar $\vec{A} + \vec{B}$ y su magnitud.
> 
> **Solución:** $$\vec{A} + \vec{B} = (3-2)\hat{i} + (4+5)\hat{j} = \hat{i} + 9\hat{j}$$
> 
> **Magnitud:** $$|\vec{A} + \vec{B}| = \sqrt{1^2 + 9^2} = \sqrt{82} = 9.06$$

> [!example]- 💡 **Problema 2: Producto Punto** Si $\vec{A} = 2\hat{i} + 3\hat{j}$ y $\vec{B} = 4\hat{i} - \hat{j}$, encontrar el ángulo entre ellos.
> 
> **Solución:** **Producto punto:** $$\vec{A} \cdot \vec{B} = (2)(4) + (3)(-1) = 8 - 3 = 5$$
> 
> **Magnitudes:** $$|\vec{A}| = \sqrt{4 + 9} = \sqrt{13}$$ $$|\vec{B}| = \sqrt{16 + 1} = \sqrt{17}$$
> 
> **Ángulo:** $$\cos\theta = \frac{5}{\sqrt{13}\sqrt{17}} = \frac{5}{\sqrt{221}}$$ $$\theta = \arccos\left(\frac{5}{\sqrt{221}}\right) = 69.1°$$

> [!example]- 💡 **Problema 3: Producto Cruz** Para $\vec{A} = 2\hat{i} + 3\hat{j} + \hat{k}$ y $\vec{B} = \hat{i} - 2\hat{j} + 3\hat{k}$, encontrar $\vec{A} \times \vec{B}$.
> 
> **Solución:** $$\vec{A} \times \vec{B} = \begin{vmatrix} \hat{i} & \hat{j} & \hat{k} \ 2 & 3 & 1 \ 1 & -2 & 3 \end{vmatrix}$$
> 
> $$= \hat{i}(3 \cdot 3 - 1 \cdot (-2)) - \hat{j}(2 \cdot 3 - 1 \cdot 1) + \hat{k}(2 \cdot (-2) - 3 \cdot 1)$$
> 
> $$= \hat{i}(9 + 2) - \hat{j}(6 - 1) + \hat{k}(-4 - 3)$$
> 
> $$= 11\hat{i} - 5\hat{j} - 7\hat{k}$$

## 🎯 Sistemas de Coordenadas

> [!info]- 📐 **Coordenadas Cartesianas vs Polares**
> 
> **Conversiones 2D (Cartesiano ↔ Polar):**
> 
> - Cartesiano a Polar:
> - $$r = \sqrt{x^2 + y^2}$$
> - $$\theta = \arctan\left(\frac{y}{x}\right)$$
> - Polar a Cartesiano:
> - $$x = r\cos\theta$$
> - $$y = r\sin\theta$$
> 
> **Vectores unitarios:**
> 
> - Cartesianos: $\hat{i}, \hat{j}, \hat{k}$ (constantes)
> - Polares: $\hat{r}, \hat{\theta}$ (variables con posición)
> - Cilíndricas: $\hat{r}, \hat{\theta}, \hat{z}$
> - Esféricas: $\hat{r}, \hat{\theta}, \hat{\phi}$

## 🔍 Referencias y Conexiones

> [!quote]- 📚 **Referencias a otras notas**
> 
> - [[Fuerzas y Diagramas de Cuerpo Libre]] - Aplicación directa de vectores
> - [[Cinemática Traslacional]] - Vectores posición, velocidad, aceleración
> - [[Cinemática Rotacional]] - Vectores angulares y momento angular
> - [[Trigonometría]] - Base para descomposición de vectores
> - [[Producto Cruz]] - Análisis profundo del producto vectorial

## 📖 Notas Recomendadas para Complementar

> [!info]- 🎯 **Prerrequisitos y Temas Relacionados**
> 
> **Prerrequisitos esenciales:**
> 
> - [[Funciones Trigonométricas]] - Para ángulos y componentes
> - [[Álgebra]] - Para operaciones algebraicas
> - [[Geometría]] - Para interpretación geométrica
> - [[Funciones]] - Para vectores como funciones del tiempo
> 
> **Temas complementarios:**
> 
> - [[Campos Vectoriales]] - Vectores que varían en el espacio
> - [[Derivadas Vectoriales]] - Tasas de cambio de vectores
> - [[Integrales Vectoriales]] - Integración de campos vectoriales
> - [[Transformaciones de Coordenadas]] - Cambios entre sistemas

## 🔧 Herramientas de Verificación

> [!tip]- ✅ **Cómo Verificar Operaciones Vectoriales**
> 
> **Verificación de suma/resta:**
> 
> 1. **Método alternativo:** Usar método gráfico para verificar analítico
> 2. **Verificar magnitud:** ¿Es razonable comparada con vectores originales?
> 3. **Verificar dirección:** ¿Apunta donde esperamos?
> 
> **Verificación de productos:**
> 
> 4. **Producto punto = 0:** ¿Los vectores son realmente perpendiculares?
> 5. **Producto cruz = 0:** ¿Los vectores son realmente paralelos?
> 6. **Regla mano derecha:** ¿La dirección del producto cruz es correcta?
> 
> **Análisis dimensional:**
> 
> - Vector posición: [L]
> - Vector velocidad: [L][T]⁻¹
> - Vector fuerza: [M][L][T]⁻²

---

**Tags:** #matematicas #vectores #algebra-vectorial #producto-punto #producto-cruz #geometria-analitica #fisica-vectorial #coordenadas #componentes