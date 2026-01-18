# 📐 Integrales Triples en Regiones Generales

## 🎯 Introducción

> [!info]- 💡 ¿Qué son las Integrales Triples? Las **integrales triples** son una extensión natural de las integrales dobles al espacio tridimensional. Permiten calcular volúmenes, masas, centros de masa y otros conceptos físicos en regiones del espacio **R³**.
> 
> **Analogía práctica:** Imagina un escultor trabajando con un bloque de mármol:
> 
> - **Integral simple** → Medir una línea (1D)
> - **Integral doble** → Calcular el área de una superficie plana (2D)
> - **Integral triple** → Determinar el volumen de una región sólida (3D)
> 
> **¿Por qué son importantes?**
> 
> |Aspecto|Descripción|Ejemplo de Uso|
> |---|---|---|
> |**Volumen**|Calcular espacio ocupado por sólidos|Tanques, edificios, contenedores|
> |**Masa**|Determinar masa con densidad variable|Objetos no homogéneos|
> |**Centro de masa**|Encontrar punto de equilibrio|Diseño estructural, física|
> |**Momento de inercia**|Resistencia a la rotación|Ingeniería mecánica|
> |**Aplicaciones físicas**|Temperatura, presión, concentración|Termodinámica, fluidos|

```mermaid
graph TB
    A[Integral Triple] --> B[Volumen de región D]
    A --> C[Masa con densidad ρ]
    A --> D[Momento respecto a planos]
    A --> E[Centro de masa]
    
    B --> F[∫∫∫_D dV]
    C --> G[∫∫∫_D ρ(x,y,z) dV]
    D --> H[∫∫∫_D z·ρ dV]
    E --> I[x̄ = M_yz/m]
    
    style A fill:#e1f5ff
    style B fill:#e1ffe1
    style C fill:#fff4e1
    style D fill:#ffe1f5
    style E fill:#f5e1ff
```

---

## 🔲 Tipos de Regiones en R³

### 📦 Regiones Tipo I (Proyección en xy)

> [!example]- 🎲 Regiones con z acotado
> 
> Una región **Tipo I** tiene la forma:
> 
> $$D = {(x,y,z) : (x,y) \in R_{xy}, \quad u_1(x,y) \leq z \leq u_2(x,y)}$$
> 
> **Interpretación:** La región está "atrapada" entre dos superficies $z = u_1(x,y)$ (inferior) y $z = u_2(x,y)$ (superior).
> 
> ```mermaid
> graph TD
>     A[Región Tipo I] --> B[Proyección R_xy en plano xy]
>     B --> C[Superficie inferior: z = u₁x,y]
>     B --> D[Superficie superior: z = u₂x,y]
>     
>     C --> E[Integrar primero en z]
>     D --> E
>     E --> F[Luego integrar sobre R_xy]
>     
>     style A fill:#e1f5ff
>     style E fill:#e1ffe1
>     style F fill:#fff4e1
> ```
> 
> **Fórmula de integración:**
> 
> $$\iiint_D f(x,y,z),dV = \iint_{R_{xy}} \left[\int_{u_1(x,y)}^{u_2(x,y)} f(x,y,z),dz\right] dA$$
> 
> **Ejemplo visual:**
> 
> |Componente|Descripción|Expresión|
> |---|---|---|
> |**Proyección**|Región en plano xy|$0 \leq x \leq 1, \quad 0 \leq y \leq 1$|
> |**Superficie inferior**|Plano base|$z = 0$|
> |**Superficie superior**|Paraboloide|$z = 1 - x^2 - y^2$|
> |**Región completa**|Sólido entre superficies|$D: 0 \leq z \leq 1-x^2-y^2$|
> 
> **Ejemplo concreto:**
> 
> Calcular $\displaystyle \iiint_D z,dV$ donde $D$ es la región acotada por $z = 0$ y $z = 4 - x^2 - y^2$ sobre el cuadrado $[0,1] \times [0,1]$.
> 
> **Solución paso a paso:**
> 
> $$\begin{align} \iiint_D z,dV &= \int_0^1 \int_0^1 \left[\int_0^{4-x^2-y^2} z,dz\right] dy,dx \[1em] &= \int_0^1 \int_0^1 \left[\frac{z^2}{2}\right]_0^{4-x^2-y^2} dy,dx \[1em] &= \int_0^1 \int_0^1 \frac{(4-x^2-y^2)^2}{2},dy,dx \[1em] &= \frac{1}{2}\int_0^1 \int_0^1 (16 - 8x^2 - 8y^2 + x^4 + 2x^2y^2 + y^4),dy,dx \end{align}$$
> 
> **Visualización del orden de integración:**
> 
> ```mermaid
> flowchart LR
>     A[z: u₁ → u₂] --> B[y: c → d]
>     B --> C[x: a → b]
>     
>     A -.-> D[Interior]
>     C -.-> E[Exterior]
>     
>     style A fill:#ffe1e1
>     style B fill:#fff4e1
>     style C fill:#e1ffe1
> ```

### 📊 Regiones Tipo II (Proyección en xz)

> [!example]- 🔄 Regiones con y acotado
> 
> Una región **Tipo II** tiene la forma:
> 
> $$D = {(x,y,z) : (x,z) \in R_{xz}, \quad v_1(x,z) \leq y \leq v_2(x,z)}$$
> 
> **Fórmula de integración:**
> 
> $$\iiint_D f(x,y,z),dV = \iint_{R_{xz}} \left[\int_{v_1(x,z)}^{v_2(x,z)} f(x,y,z),dy\right] dA$$
> 
> **Características:**
> 
> |Aspecto|Tipo I|Tipo II|
> |---|---|---|
> |**Proyección**|Plano xy|Plano xz|
> |**Variable acotada**|z entre superficies|y entre superficies|
> |**Primera integración**|$\int ... dz$|$\int ... dy$|
> |**Uso típico**|Sólidos "verticales"|Sólidos "laterales"|
> 
> **Ejemplo:** Región entre cilindros $y = x^2$ e $y = 4$, acotada por $0 \leq z \leq 3$.
> 
> $$D: {(x,y,z) : -2 \leq x \leq 2, , 0 \leq z \leq 3, , x^2 \leq y \leq 4}$$
> 
> $$\iiint_D f(x,y,z),dV = \int_{-2}^{2} \int_0^3 \left[\int_{x^2}^{4} f(x,y,z),dy\right] dz,dx$$

### 📐 Regiones Tipo III (Proyección en yz)

> [!example]- 🔀 Regiones con x acotado
> 
> Una región **Tipo III** tiene la forma:
> 
> $$D = {(x,y,z) : (y,z) \in R_{yz}, \quad w_1(y,z) \leq x \leq w_2(y,z)}$$
> 
> **Fórmula de integración:**
> 
> $$\iiint_D f(x,y,z),dV = \iint_{R_{yz}} \left[\int_{w_1(y,z)}^{w_2(y,z)} f(x,y,z),dx\right] dA$$
> 
> **Comparación visual:**
> 
> ```mermaid
> graph TB
>     A[Región D] --> B[Tipo I: z acotado]
>     A --> C[Tipo II: y acotado]
>     A --> D[Tipo III: x acotado]
>     
>     B --> E[Proyección xy<br/>∫∫ ∫ ... dz dA]
>     C --> F[Proyección xz<br/>∫∫ ∫ ... dy dA]
>     D --> G[Proyección yz<br/>∫∫ ∫ ... dx dA]
>     
>     style B fill:#e1ffe1
>     style C fill:#fff4e1
>     style D fill:#f5e1ff
> ```

---

## 🔄 Órdenes de Integración

### 🎲 Los Seis Órdenes Posibles

> [!note]- 🔀 Permutaciones de dx dy dz
> 
> Para una región general, existen **6 órdenes** de integración posibles:
> 
> |Orden|Notación|Primera integración|Última integración|
> |---|---|---|---|
> |1|$dx,dy,dz$|x (más interno)|z (más externo)|
> |2|$dx,dz,dy$|x|y|
> |3|$dy,dx,dz$|y|z|
> |4|$dy,dz,dx$|y|x|
> |5|$dz,dx,dy$|z|y|
> |6|$dz,dy,dx$|z|x|
> 
> **Estructura general:**
> 
> $$\int_a^b \int_{c(z)}^{d(z)} \int_{e(y,z)}^{f(y,z)} g(x,y,z),dx,dy,dz$$
> 
> ```mermaid
> graph LR
>     A[Interior<br/>dx] --> B[Medio<br/>dy]
>     B --> C[Exterior<br/>dz]
>     
>     A -.-> D[Límites pueden<br/>depender de y, z]
>     B -.-> E[Límites pueden<br/>depender de z]
>     C -.-> F[Límites<br/>constantes]
>     
>     style A fill:#ffe1e1
>     style B fill:#fff4e1
>     style C fill:#e1ffe1
> ```
> 
> **Ejemplo con múltiples órdenes:**
> 
> Sea $D$ el tetraedro con vértices $(0,0,0)$, $(1,0,0)$, $(0,1,0)$, $(0,0,1)$.
> 
> El plano que pasa por $(1,0,0)$, $(0,1,0)$, $(0,0,1)$ es: $x + y + z = 1$
> 
> **Orden 1:** $dz,dy,dx$
> 
> $$\int_0^1 \int_0^{1-x} \int_0^{1-x-y} f(x,y,z),dz,dy,dx$$
> 
> **Orden 2:** $dy,dz,dx$
> 
> $$\int_0^1 \int_0^{1-x} \int_0^{1-x-z} f(x,y,z),dy,dz,dx$$
> 
> **Orden 3:** $dx,dy,dz$
> 
> $$\int_0^1 \int_0^{1-z} \int_0^{1-y-z} f(x,y,z),dx,dy,dz$$

### 🎯 Elección del Mejor Orden

> [!tip]- 🔍 Estrategias de Selección
> 
> **Criterios para elegir el orden:**
> 
> |Criterio|Descripción|Ejemplo|
> |---|---|---|
> |**Simplicidad**|Límites más sencillos|Constantes > Lineales > No lineales|
> |**Integrabilidad**|Función más fácil de integrar primero|$\int e^{z^2} dz$ es difícil, mejor último|
> |**Simetría**|Aprovechar simetría de la región|Esfera → coordenadas esféricas|
> |**Eficiencia**|Menos cálculos intermedios|Evitar integrales complicadas|
> 
> **Proceso de decisión:**
> 
> ```mermaid
> flowchart TD
>     A[Analizar región D] --> B{¿Límites<br/>simples?}
>     B -->|Sí| C[Usar ese orden]
>     B -->|No| D{¿Función<br/>complicada?}
>     
>     D -->|Sí| E[Integrar primero<br/>variable que simplifica]
>     D -->|No| F{¿Simetría<br/>especial?}
>     
>     F -->|Esférica| G[Coordenadas<br/>esféricas]
>     F -->|Cilíndrica| H[Coordenadas<br/>cilíndricas]
>     F -->|No| I[Probar órdenes<br/>hasta encontrar mejor]
>     
>     style C fill:#e1ffe1
>     style E fill:#fff4e1
>     style G fill:#e1f5ff
>     style H fill:#f5e1ff
> ```
> 
> **Ejemplo práctico:**
> 
> Calcular $\displaystyle \iiint_D e^{z^2},dV$ donde $D: 0 \leq x \leq 1, , 0 \leq y \leq x, , 0 \leq z \leq x+y$
> 
> **❌ Orden malo:** $dx,dy,dz$ (requiere integrar $e^{z^2}$ primero - ¡imposible!)
> 
> **✅ Orden bueno:** $dz,dy,dx$
> 
> $$\begin{align} \iiint_D e^{z^2},dV &= \int_0^1 \int_0^x \int_0^{x+y} e^{z^2},dz,dy,dx \[0.5em] \end{align}$$
> 
> Al integrar en $z$ primero, aunque $e^{z^2}$ no tiene primitiva elemental, podemos usar sustitución $u = z^2$ cuando sea necesario, o evaluar numéricamente.

---

## 📏 Cálculo de Volúmenes

### 📦 Volumen de Regiones Sólidas

> [!success]- 🎯 Fórmula Fundamental
> 
> El **volumen** de una región $D$ se calcula con:
> 
> $$V(D) = \iiint_D 1,dV = \iiint_D dx,dy,dz$$
> 
> **Interpretación:** Sumamos "infinitos cubitos infinitesimales" $dV = dx,dy,dz$
> 
> ```mermaid
> graph TB
>     A[Región D] --> B[Dividir en<br/>elementos dV]
>     B --> C[dV = dx·dy·dz]
>     C --> D[Sumar todos<br/>los elementos]
>     D --> E[V = ∫∫∫_D dV]
>     
>     style A fill:#e1f5ff
>     style C fill:#fff4e1
>     style E fill:#e1ffe1
> ```
> 
> **Ejemplo 1:** Volumen de un paralelepípedo
> 
> $$D = [0,a] \times [0,b] \times [0,c]$$
> 
> $$V = \int_0^a \int_0^b \int_0^c 1,dz,dy,dx = \int_0^a \int_0^b c,dy,dx = \int_0^a bc,dx = abc$$
> 
> **Ejemplo 2:** Volumen bajo un paraboloide
> 
> Región $D$ acotada por $z = 4 - x^2 - y^2$ y $z = 0$, con $(x,y)$ en el círculo $x^2 + y^2 \leq 4$.
> 
> $$V = \iint_{x^2+y^2 \leq 4} \int_0^{4-x^2-y^2} 1,dz,dA = \iint_{x^2+y^2 \leq 4} (4-x^2-y^2),dA$$
> 
> Usando coordenadas polares: $x = r\cos\theta, , y = r\sin\theta, , dA = r,dr,d\theta$
> 
> $$\begin{align} V &= \int_0^{2\pi} \int_0^2 (4-r^2),r,dr,d\theta \[0.5em] &= \int_0^{2\pi} \int_0^2 (4r - r^3),dr,d\theta \[0.5em] &= \int_0^{2\pi} \left[2r^2 - \frac{r^4}{4}\right]_0^2 d\theta \[0.5em] &= \int_0^{2\pi} (8 - 4),d\theta = 4 \cdot 2\pi = 8\pi \end{align}$$

### 🔺 Volumen de Tetraedros

> [!example]- 📐 Caso Especial Importante
> 
> Un **tetraedro** con vértices en $(0,0,0)$, $(a,0,0)$, $(0,b,0)$, $(0,0,c)$ está acotado por el plano:
> 
> $$\frac{x}{a} + \frac{y}{b} + \frac{z}{c} = 1$$
> 
> **Volumen del tetraedro:**
> 
> $$V = \int_0^a \int_0^{b(1-x/a)} \int_0^{c(1-x/a-y/b)} 1,dz,dy,dx$$
> 
> $$\begin{align} V &= \int_0^a \int_0^{b(1-x/a)} c\left(1-\frac{x}{a}-\frac{y}{b}\right) dy,dx \[0.5em] &= \int_0^a c\left(1-\frac{x}{a}\right) \int_0^{b(1-x/a)} \left(1-\frac{y}{b(1-x/a)}\right) dy,dx \[0.5em] &= \int_0^a c\left(1-\frac{x}{a}\right) \cdot \frac{b(1-x/a)}{2},dx \[0.5em] &= \frac{bc}{2} \int_0^a \left(1-\frac{x}{a}\right)^2 dx = \frac{abc}{6} \end{align}$$
> 
> **Fórmula general:**
> 
> $$\boxed{V_{\text{tetraedro}} = \frac{1}{6}abc}$$
> 
> |Sólido|Fórmula de volumen|Observación|
> |---|---|---|
> |**Cubo**|$V = a^3$|Caso especial: $a=b=c$|
> |**Paralelepípedo**|$V = abc$|Base rectangular|
> |**Tetraedro**|$V = \frac{abc}{6}$|$\frac{1}{6}$ del paralelepípedo|
> |**Pirámide**|$V = \frac{1}{3}Ah$|Base cualquiera|

---

## ⚖️ Aplicaciones Físicas

### 🏋️ Masa y Densidad

> [!info]- 📊 Masa con Densidad Variable
> 
> Si $\rho(x,y,z)$ es la **densidad** en el punto $(x,y,z)$, la **masa total** es:
> 
> $$m = \iiint_D \rho(x,y,z),dV$$
> 
> **Unidades:**
> 
> |Magnitud|Símbolo|Unidades típicas|
> |---|---|---|
> |**Densidad**|$\rho$|kg/m³, g/cm³|
> |**Volumen**|$dV$|m³, cm³|
> |**Masa**|$m$|kg, g|
> 
> **Casos especiales:**
> 
> ```mermaid
> graph TD
>     A[Densidad ρx,y,z] --> B{Tipo}
>     
>     B -->|Constante| C[ρ = k]
>     B -->|Variable| D[ρ = fx,y,z]
>     
>     C --> E[m = k·Volumen]
>     D --> F[m = ∫∫∫_D ρ dV]
>     
>     style C fill:#e1ffe1
>     style D fill:#fff4e1
> ```
> 
> **Ejemplo 1:** Densidad constante
> 
> Si $\rho = 5$ g/cm³ y $V = 100$ cm³:
> 
> $$m = \rho \cdot V = 5 \times 100 = 500 \text{ g}$$
> 
> **Ejemplo 2:** Densidad variable
> 
> Cubo $D = [0,1]^3$ con densidad $\rho(x,y,z) = x + y + z$:
> 
> $$\begin{align} m &= \int_0^1 \int_0^1 \int_0^1 (x+y+z),dz,dy,dx \[0.5em] &= \int_0^1 \int_0^1 \left[xz + yz + \frac{z^2}{2}\right]_0^1 dy,dx \[0.5em] &= \int_0^1 \int_0^1 \left(x + y + \frac{1}{2}\right) dy,dx \[0.5em] &= \int_0^1 \left[xy + \frac{y^2}{2} + \frac{y}{2}\right]_0^1 dx \[0.5em] &= \int_0^1 \left(x + 1\right) dx = \left[\frac{x^2}{2} + x\right]_0^1 = \frac{3}{2} \end{align}$$

### 📍 Centro de Masa

> [!success]- 🎯 Coordenadas del Centro de Masa
> 
> El **centro de masa** $(\bar{x}, \bar{y}, \bar{z})$ de un sólido $D$ con densidad $\rho$ es:
> 
> $$\bar{x} = \frac{M_{yz}}{m}, \quad \bar{y} = \frac{M_{xz}}{m}, \quad \bar{z} = \frac{M_{xy}}{m}$$
> 
> Donde:
> 
> $$\begin{align} m &= \iiint_D \rho(x,y,z),dV \quad \text{(masa total)} \[0.5em] M_{yz} &= \iiint_D x\cdot\rho(x,y,z),dV \quad \text{(momento respecto a plano yz)} \[0.5em] M_{xz} &= \iiint_D y\cdot\rho(x,y,z),dV \quad \text{(momento respecto a plano xz)} \[0.5em] M_{xy} &= \iiint_D z\cdot\rho(x,y,z),dV \quad \text{(momento respecto a plano xy)} \end{align}$$
> 
> **Interpretación:**
> 
> ```mermaid
> graph TB
>     A[Sólido D] --> B[Calcular masa m]
>     A --> C[Calcular momentos]
>     
>     C --> D[M_yz = ∫∫∫ x·ρ dV]
>     C --> E[M_xz = ∫∫∫ y·ρ dV]
>     C --> F[M_xy = ∫∫∫ z·ρ dV]
>     
>     B --> G[Centro de masa]
>     D --> G
>     E --> G
>     F --> G
>     
>     G --> H[x̄, ȳ, z̄]
>     
>     style A fill:#e1f5ff
>     style G fill:#e1ffe1
> ```
> 
> **Ejemplo:** Tetraedro con densidad constante
> 
> Tetraedro $D$ con vértices $(0,0,0)$, $(1,0,0)$, $(0,1,0)$, $(0,0,1)$ y $\rho = 1$.
> 
> Por simetría (densidad constante y región simétrica):
> 
> $$\bar{x} = \bar{y} = \bar{z} = \frac{1}{4}$$
> 
> **Verificación:**
> 
> $$m = \frac{1}{6}(1)(1)(1) = \frac{1}{6}$$
> 
> $$M_{xy} = \int_0^1 \int_0^{1-x} \int_0^{1-x-y} z,dz,dy,dx = \int_0^1 \int_0^{1-x} \frac{(1-x-y)^2}{2},dy,dx$$
> 
> Después de calcular (largo proceso):
> 
> $$M_{xy} = \frac{1}{24} \quad \Rightarrow \quad \bar{z} = \frac{M_{xy}}{m} = \frac{1/24}{1/6} = \frac{1}{4}$$

### 🔄 Momento de Inercia

> [!note]- 🌀 Resistencia a la Rotación
> 
> El **momento de inercia** mide la resistencia de un cuerpo a rotar alrededor de un eje.
> 
> **Respecto a los ejes coordenados:**
> 
> $$\begin{align} I_x &= \iiint_D (y^2 + z^2)\rho(x,y,z),dV \quad \text{(eje x)} \[0.5em] I_y &= \iiint_D (x^2 + z^2)\rho(x,y,z),dV \quad \text{(eje y)} \[0.5em] I_z &= \iiint_D (x^2 + y^2)\rho(x,y,z),dV \quad \text{(eje z)} \end{align}$$
> 
> **Respecto al origen:**
> 
> $$I_0 = \iiint_D (x^2 + y^2 + z^2)\rho(x,y,z),dV$$
> 
> **Relación:**
> 
> $$\boxed{I_0 = \frac{1}{2}(I_x + I_y + I_z)}$$
> 
> |Magnitud|Significado físico|Unidades|
> |---|---|---|
> |**$I_x, I_y, I_z$**|Inercia respecto a eje|kg·m²|
> |**$I_0$**|Inercia respecto al origen|kg·m²|
> |**$(y^2+z^2)$**|Distancia² al eje x|m²|

---

## 🔁 Cambio de Variables

### 🗺️ Transformaciones Generales

> [!tip]- 🔄 Jacobiano en R³
> 
> Para una transformación $T: (u,v,w) \to (x,y,z)$:
> 
> $$x = x(u,v,w), \quad y = y(u,v,w), \quad z = z(u,v,w)$$
> 
> El **Jacobiano** es:
> 
> $$J = \frac{\partial(x,y,z)}{\partial(u,v,w)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \[0.3em] \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \[0.3em] \frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w}
> \end{vmatrix}$$
> 
> **Fórmula de cambio:**
> 
> $$\iiint_D f(x,y,z),dV = \iiint_{D'} f(x(u,v,w), y(u,v,w), z(u,v,w)) |J|,du,dv,dw$$
> 
> ```mermaid
> graph LR
>     A[Región D'<br/>en uvw] --> B[Transformación T]
>     B --> C[Región D<br/>en xyz]
>     
>     A -.-> D[dV' = du dv dw]
>     C -.-> E[dV = J du dv dw]
>     
>     style A fill:#fff4e1
>     style C fill:#e1ffe1
>     style E fill:#ffe1e1
> ```

### 🌐 Coordenadas Cilíndricas

> [!example]- 📏 Sistema Cilíndrico
> 
> **Transformación:**
> 
> $$\begin{cases} x = r\cos\theta \ y = r\sin\theta \ z = z \end{cases}$$
> 
> **Jacobiano:**
> 
> $$J = \begin{vmatrix} \cos\theta & -r\sin\theta & 0 \ \sin\theta & r\cos\theta & 0 \ 0 & 0 & 1 \end{vmatrix} = r(\cos^2\theta + \sin^2\theta) = r$$
> 
> **Elemento de volumen:**
> 
> $$\boxed{dV = r,dr,d\theta,dz}$$
> 
> **Rangos típicos:**
> 
> $$0 \leq r < \infty, \quad 0 \leq \theta < 2\pi, \quad -\infty < z < \infty$$
> 
> **Cuándo usar:**
> 
> |Situación|Ejemplo|
> |---|---|
> |Simetría respecto al eje z|Cilindros, conos|
> |Ecuaciones con $x^2 + y^2$|Paraboloides, hiperboloides|
> |Límites circulares en xy|Regiones cilíndricas|
> 
> **Ejemplo:** Volumen de cilindro $x^2 + y^2 \leq a^2$, $0 \leq z \leq h$
> 
> $$V = \int_0^{2\pi} \int_0^a \int_0^h r,dz,dr,d\theta = 2\pi \cdot \frac{a^2}{2} \cdot h = \pi a^2 h$$

### 🔮 Coordenadas Esféricas

> [!example]- 🌍 Sistema Esférico
> 
> **Transformación:**
> 
> $$\begin{cases} x = \rho\sin\phi\cos\theta \ y = \rho\sin\phi\sin\theta \ z = \rho\cos\phi \end{cases}$$
> 
> **Variables:**
> 
> - $\rho$ = distancia al origen (radio)
> - $\phi$ = ángulo desde eje z positivo (polar)
> - $\theta$ = ángulo en plano xy (azimutal)
> 
> **Jacobiano:**
> 
> $$|J| = \rho^2\sin\phi$$
> 
> **Elemento de volumen:**
> 
> $$\boxed{dV = \rho^2\sin\phi,d\rho,d\phi,d\theta}$$
> 
> **Rangos típicos:**
> 
> $$0 \leq \rho < \infty, \quad 0 \leq \phi \leq \pi, \quad 0 \leq \theta < 2\pi$$
> 
> ```mermaid
> graph TB
>     A[Coordenadas Esféricas] --> B[ρ: radio]
>     A --> C[φ: ángulo polar]
>     A --> D[θ: ángulo azimutal]
>     
>     B --> E[Distancia al origen<br/>0 ≤ ρ < ∞]
>     C --> F[Desde eje z<br/>0 ≤ φ ≤ π]
>     D --> G[En plano xy<br/>0 ≤ θ < 2π]
>     
>     style A fill:#e1f5ff
>     style B fill:#e1ffe1
>     style C fill:#fff4e1
>     style D fill:#ffe1f5
> ```
> 
> **Cuándo usar:**
> 
> |Situación|Ejemplo|
> |---|---|
> |Simetría esférica|Esferas, conos|
> |Ecuaciones con $x^2+y^2+z^2$|Esferas concéntricas|
> |Problemas desde un punto|Campo gravitacional|
> 
> **Ejemplo:** Volumen de esfera $x^2 + y^2 + z^2 \leq a^2$
> 
> $$\begin{align} V &= \int_0^{2\pi} \int_0^{\pi} \int_0^a \rho^2\sin\phi,d\rho,d\phi,d\theta \[0.5em] &= \int_0^{2\pi} d\theta \int_0^{\pi} \sin\phi,d\phi \int_0^a \rho^2,d\rho \[0.5em] &= 2\pi \cdot [-\cos\phi]_0^{\pi} \cdot \frac{a^3}{3} \[0.5em] &= 2\pi \cdot 2 \cdot \frac{a^3}{3} = \frac{4\pi a^3}{3} \end{align}$$

---

## 📊 Tabla Comparativa de Sistemas

> [!note]- 🔍 Comparación Completa
> 
> |Sistema|Transformación|Jacobiano|Elemento dV|Uso principal|
> |---|---|---|---|---|
> |**Cartesiano**|$x, y, z$|1|$dx,dy,dz$|General|
> |**Cilíndrico**|$r\cos\theta, r\sin\theta, z$|$r$|$r,dr,d\theta,dz$|Simetría en z|
> |**Esférico**|$\rho\sin\phi\cos\theta,\ldots$|$\rho^2\sin\phi$|$\rho^2\sin\phi,d\rho,d\phi,d\theta$|Simetría radial|
> 
> **Relaciones entre sistemas:**
> 
> ```mermaid
> graph TD
>     A[Cartesianas<br/>x, y, z] --> B[Cilíndricas<br/>r, θ, z]
>     A --> C[Esféricas<br/>ρ, φ, θ]
>     
>     B -.-> D[x² + y² = r²]
>     C -.-> E[x² + y² + z² = ρ²]
>     
>     style A fill:#e1f5ff
>     style B fill:#fff4e1
>     style C fill:#f5e1ff
> ```

---

## 🎓 Estrategias de Resolución

### 📝 Metodología Paso a Paso

> [!success]- ✅ Proceso Sistemático
> 
> **Paso 1: Identificar la región D**
> 
> - Leer y comprender las desigualdades
> - Graficar la región (al menos mentalmente)
> - Identificar superficies límite
> 
> **Paso 2: Clasificar la región**
> 
> - ¿Es Tipo I, II, o III?
> - ¿Tiene simetría especial?
> - ¿Conviene cambio de coordenadas?
> 
> **Paso 3: Elegir el orden de integración**
> 
> - Analizar simplicidad de límites
> - Considerar dificultad del integrando
> - Verificar que es factible
> 
> **Paso 4: Establecer los límites**
> 
> - Exterior: constantes
> - Medio: función de exterior
> - Interior: función de medio y exterior
> 
> **Paso 5: Integrar**
> 
> - De adentro hacia afuera
> - Simplificar en cada paso
> - Verificar resultado final
> 
> ```mermaid
> flowchart TD
>     A[Leer problema] --> B[Identificar región D]
>     B --> C{¿Simetría?}
>     
>     C -->|Cilíndrica| D[Usar coord. cilíndricas]
>     C -->|Esférica| E[Usar coord. esféricas]
>     C -->|No| F[Cartesianas]
>     
>     D --> G[Establecer límites]
>     E --> G
>     F --> G
>     
>     G --> H[Integrar paso a paso]
>     H --> I[Simplificar resultado]
>     I --> J{¿Tiene sentido?}
>     
>     J -->|No| K[Revisar cálculos]
>     J -->|Sí| L[Solución final]
>     
>     K --> H
>     
>     style C fill:#fff4e1
>     style L fill:#e1ffe1
> ```

---

## 💡 Ejemplos Resueltos Completos

### 📌 Ejemplo 1: Volumen entre Superficies

> [!example]- 📐 Región entre Paraboloides
> 
> **Problema:** Calcular el volumen de la región $D$ acotada por:
> 
> - Superior: $z = 8 - x^2 - y^2$
> - Inferior: $z = x^2 + y^2$
> 
> **Solución:**
> 
> **Paso 1:** Encontrar la intersección
> 
> $$8 - x^2 - y^2 = x^2 + y^2$$ $$8 = 2(x^2 + y^2)$$ $$x^2 + y^2 = 4$$
> 
> Proyección en xy: círculo de radio 2.
> 
> **Paso 2:** Usar coordenadas cilíndricas
> 
> $$0 \leq r \leq 2, \quad 0 \leq \theta \leq 2\pi, \quad r^2 \leq z \leq 8-r^2$$
> 
> **Paso 3:** Plantear integral
> 
> $$V = \int_0^{2\pi} \int_0^2 \int_{r^2}^{8-r^2} r,dz,dr,d\theta$$
> 
> **Paso 4:** Integrar en z
> 
> $$V = \int_0^{2\pi} \int_0^2 r[z]_{r^2}^{8-r^2},dr,d\theta$$ $$= \int_0^{2\pi} \int_0^2 r(8-r^2-r^2),dr,d\theta$$ $$= \int_0^{2\pi} \int_0^2 r(8-2r^2),dr,d\theta$$
> 
> **Paso 5:** Integrar en r
> 
> $$V = \int_0^{2\pi} \left[4r^2 - \frac{r^4}{2}\right]_0^2 d\theta$$ $$= \int_0^{2\pi} (16 - 8),d\theta = 8 \cdot 2\pi = 16\pi$$
> 
> **Respuesta:** $V = 16\pi$ unidades cúbicas

### 📌 Ejemplo 2: Centro de Masa

> [!example]- ⚖️ Hemisferio con Densidad Variable
> 
> **Problema:** Encontrar el centro de masa del hemisferio superior $x^2+y^2+z^2 \leq a^2$, $z \geq 0$, con densidad $\rho(x,y,z) = z$.
> 
> **Solución:**
> 
> Por simetría: $\bar{x} = \bar{y} = 0$ (solo calcular $\bar{z}$)
> 
> **Coordenadas esféricas:**
> 
> $$0 \leq \rho \leq a, \quad 0 \leq \phi \leq \pi/2, \quad 0 \leq \theta \leq 2\pi$$ $$z = \rho\cos\phi, \quad dV = \rho^2\sin\phi,d\rho,d\phi,d\theta$$
> 
> **Masa total:**
> 
> $$\begin{align} m &= \int_0^{2\pi} \int_0^{\pi/2} \int_0^a (\rho\cos\phi)\rho^2\sin\phi,d\rho,d\phi,d\theta \[0.5em] &= 2\pi \int_0^{\pi/2} \cos\phi\sin\phi,d\phi \int_0^a \rho^3,d\rho \[0.5em] &= 2\pi \cdot \frac{1}{2}[\sin^2\phi]_0^{\pi/2} \cdot \frac{a^4}{4} \[0.5em] &= 2\pi \cdot \frac{1}{2} \cdot \frac{a^4}{4} = \frac{\pi a^4}{4} \end{align}$$
> 
> **Momento $M_{xy}$:**
> 
> $$\begin{align} M_{xy} &= \int_0^{2\pi} \int_0^{\pi/2} \int_0^a z \cdot z \cdot \rho^2\sin\phi,d\rho,d\phi,d\theta \[0.5em] &= \int_0^{2\pi} \int_0^{\pi/2} \int_0^a (\rho\cos\phi)^2 \rho^2\sin\phi,d\rho,d\phi,d\theta \[0.5em] &= 2\pi \int_0^{\pi/2} \cos^2\phi\sin\phi,d\phi \int_0^a \rho^4,d\rho \[0.5em] &= 2\pi \cdot \frac{1}{3}[\cos^3\phi]_{\pi/2}^0 \cdot \frac{a^5}{5} \[0.5em] &= 2\pi \cdot \frac{1}{3} \cdot \frac{a^5}{5} = \frac{2\pi a^5}{15} \end{align}$$
> 
> **Centro de masa:**
> 
> $$\bar{z} = \frac{M_{xy}}{m} = \frac{2\pi a^5/15}{\pi a^4/4} = \frac{2a}{15} \cdot \frac{4}{1} = \frac{8a}{15}$$
> 
> **Respuesta:** $(\bar{x}, \bar{y}, \bar{z}) = \left(0, 0, \frac{8a}{15}\right)$

---

## 🎯 Ejercicios Propuestos

> [!question]- 💪 Práctica Guiada
> 
> ### Nivel Básico
> 
> **1.** Calcular $\displaystyle \iiint_D xyz,dV$ donde $D = [0,1] \times [0,2] \times [0,3]$
> 
> **2.** Volumen del sólido acotado por $z = 0$, $z = 4$, $x = 0$, $y = 0$, $x + y = 2$
> 
> **3.** Evaluar $\displaystyle \int_0^1 \int_0^{1-x} \int_0^{1-x-y} 6,dz,dy,dx$
> 
> ### Nivel Intermedio
> 
> **4.** Volumen del sólido acotado por $z = x^2 + y^2$ y $z = 2 - x^2 - y^2$
> 
> **5.** Masa del cubo $[0,1]^3$ con densidad $\rho(x,y,z) = x + y + z$
> 
> **6.** Centro de masa del tetraedro con vértices $(0,0,0)$, $(2,0,0)$, $(0,3,0)$, $(0,0,1)$ y densidad constante
> 
> ### Nivel Avanzado
> 
> **7.** Volumen de la región dentro del cilindro $x^2 + y^2 = 4$ entre $z = 0$ y $z = x + 3$
> 
> **8.** Momento de inercia de la esfera $x^2+y^2+z^2 \leq a^2$ con densidad $\rho = k$ respecto al eje z
> 
> **9.** Calcular $\displaystyle \iiint_D e^{(x^2+y^2+z^2)^{3/2}},dV$ donde $D$ es la bola $x^2+y^2+z^2 \leq 1$

---

## 📚 Resumen y Fórmulas Clave

> [!note]- 📖 Compendio Rápido
> 
> ### Tipos de Regiones
> 
> |Tipo|Proyección|Forma|Primera integral|
> |---|---|---|---|
> |**I**|xy|$u_1(x,y) \leq z \leq u_2(x,y)$|$\int ... dz$|
> |**II**|xz|$v_1(x,z) \leq y \leq v_2(x,z)$|$\int ... dy$|
> |**III**|yz|$w_1(y,z) \leq x \leq w_2(y,z)$|$\int ... dx$|
> 
> ### Cambios de Coordenadas
> 
> **Cilíndricas:** $$x = r\cos\theta, \quad y = r\sin\theta, \quad z = z$$ $$dV = r,dr,d\theta,dz$$
> 
> **Esféricas:** $$x = \rho\sin\phi\cos\theta, \quad y = \rho\sin\phi\sin\theta, \quad z = \rho\cos\phi$$ $$dV = \rho^2\sin\phi,d\rho,d\phi,d\theta$$
> 
> ### Aplicaciones Físicas
> 
> $$\begin{align} \text{Volumen:} \quad & V = \iiint_D 1,dV \[0.5em] \text{Masa:} \quad & m = \iiint_D \rho,dV \[0.5em] \text{Centro de masa:} \quad & \bar{x} = \frac{1}{m}\iiint_D x\rho,dV \[0.5em] \text{Momento de inercia:} \quad & I_z = \iiint_D (x^2+y^2)\rho,dV \end{align}$$

---

## 🔗 Conexión con Próximos Temas

> [!quote]- 🌟 Progresión del Aprendizaje
> 
> ```mermaid
> mindmap
>   root((Integrales<br/>Triples))
>     Fundamentos
>       Regiones Tipo I-III
>       Órdenes integración
>       Límites variables
>     Cambio Variables
>       Cilíndricas
>       Esféricas
>       Jacobiano
>     Aplicaciones
>       Volumen
>       Masa
>       Centro masa
>       Momento inercia
>     Próximos Temas
>       Teorema Divergencia
>       Teorema Stokes
>       Campos vectoriales
> ```
> 
> **Roadmap:**
> 
> |Nivel|Tema|Conexión|
> |---|---|---|
> |**Actual**|Integrales triples generales|Base del cálculo vectorial 3D|
> |**Siguiente**|Campos vectoriales|Usar integrales para flujo|
> |**Avanzado**|Teoremas fundamentales|Green, Stokes, Divergencia|
> |**Aplicado**|Ecuaciones diferenciales|Física matemática|

---

**Tags:** #calculo-vectorial #integrales-triples #coordenadas-cilindricas #coordenadas-esfericas #centro-masa #momento-inercia #jacobiano #cambio-variables #volumen #aplicaciones-fisicas