---
dg-publish: true
---

# ⚖️ Tutorial S10: Leyes de Newton

## 🧠 Contexto
>[!info] Empecemos con un: 
> **Enfoque Principal**: Aplicación de las tres leyes de Newton para analizar el movimiento de sistemas complejos.

Este tutorial aborda situaciones donde es necesario aplicar las **tres leyes de Newton** de manera integrada para resolver problemas de dinámica. Se enfoca principalmente en sistemas con múltiples objetos, fuerzas complejas y diferentes superficies.

### 🎯 Sistemas de Estudio

```mermaid
mindmap
  root)⚖️ Leyes de Newton(
    📐 Planos Inclinados
      Con fricción
      Sin fricción
      Múltiples masas
    🔗 Poleas
      Sistemas conectados
      Cuerdas y tensiones
      Aceleraciones vinculadas
    📦 Sistemas Conectados
      Múltiples objetos
      Fuerzas internas
      Análisis independiente
    💪 Fuerzas Externas
      Empuje y tracción
      Componentes vectoriales
      Equilibrio dinámico
```

---

## 📌 Variables del Sistema

|Variable|Símbolo|Unidad|Descripción|
|---|---|---|---|
|Masa|$m$|kg|Cantidad de materia|
|Aceleración|$a$|m/s²|Cambio de velocidad|
|Gravedad|$g$|9.8 m/s²|Aceleración gravitacional|
|Fuerza Normal|$N$|N|Perpendicular a superficie|
|Fricción|$f$|N|Oposición al movimiento|
|Tensión|$T$|N|Fuerza en cuerdas/cables|
|Peso|$W$|N|$W = mg$|
|Coeficiente fricción|$\mu$|-|Estático ($\mu_s$) o cinético ($\mu_k$)|

---

## 📐 Formulación General

### ⚖️ Segunda Ley de Newton - Forma Vectorial

$$\sum \vec{F} = m \vec{a}$$

### 🧮 Descomposición por Ejes

#### 📏 Eje X (Horizontal)

$$\sum F_x = m a_x$$

#### 📏 Eje Y (Vertical)

$$\sum F_y = m a_y$$

### 🔥 Fuerza de Fricción

$$f = \mu N$$

**Donde**:

- $\mu_s$: Coeficiente de fricción estática (objeto en reposo)
- $\mu_k$: Coeficiente de fricción cinética (objeto en movimiento)

### 🎯 Las Tres Leyes Fundamentales

```mermaid
graph TD
    A[⚖️ Leyes de Newton] --> B[1️⃣ Primera Ley<br/>📍 Inercia]
    A --> C[2️⃣ Segunda Ley<br/>🚀 F = ma]
    A --> D[3️⃣ Tercera Ley<br/>↔️ Acción-Reacción]
    
    B --> E[Objeto en reposo o<br/>velocidad constante<br/>ΣF = 0]
    C --> F[Aceleración proporcional<br/>a fuerza neta<br/>a = F/m]
    D --> G[Fuerzas en pares<br/>Misma magnitud<br/>Direcciones opuestas]
```

---

## 🧪 Aplicación Práctica

### 🎯 Tipos de Problemas Característicos

```mermaid
flowchart TD
    A[📚 Problemas Típicos] --> B[📐 Plano Inclinado + Fricción]
    A --> C[🔗 Sistema Polea + 2 Masas]
    A --> D[📦 Cajas Empujadas]
    A --> E[🔄 Sistemas Múltiples]
    
    B --> F[Descomponer peso<br/>Calcular normal<br/>Aplicar fricción]
    C --> G[DCL independientes<br/>Vincular aceleraciones<br/>Resolver sistema]
    D --> H[Componentes de fuerza<br/>Fricción resultante<br/>Aceleración neta]
    E --> I[Análisis por separado<br/>Relacionar ecuaciones<br/>Solución conjunta]
```

---

## 🎯 Metodología de Diagramas de Cuerpo Libre (DCL)

### 📐 Ejemplo: Bloque en Plano Inclinado

```mermaid
graph TD
    A[📦 Bloque en plano θ] --> B[🌍 Peso mg]
    A --> C[📏 Normal N]
    A --> D[🔥 Fricción f]
    A --> E[🔗 Tensión T]
    
    B --> F[📐 Componentes del peso]
    F --> G[📏 Perpendicular: mg cos θ]
    F --> H[📐 Paralela: mg sin θ]
    
    style A fill:#e1f5fe
    style F fill:#fff3e0
```

### 🧮 Ecuaciones Asociadas

#### 📏 Componentes del Peso

- **Perpendicular al plano**: $W_{\perp} = mg \cos(\theta)$
- **Paralela al plano**: $W_{\parallel} = mg \sin(\theta)$

#### ⚖️ Equilibrio Perpendicular

$$N = mg \cos(\theta)$$

#### 🚀 Ecuación de Movimiento (Paralela)

$$ma = mg \sin(\theta) - f - T$$

---

## 📌 Estrategia de Resolución

```mermaid
flowchart TD
    A[📋 1. Identificar sistema] --> B[🎯 2. DCL para cada objeto]
    B --> C[📐 3. Definir ejes coordenados]
    C --> D[🧮 4. Descomponer fuerzas]
    D --> E[⚖️ 5. Aplicar ΣF = ma]
    E --> F[🔗 6. Relacionar aceleraciones]
    F --> G[📊 7. Resolver sistema]
    G --> H[✅ 8. Verificar resultado]
    
    style A fill:#e8f5e8
    style H fill:#e8f5e8
```

---

## 🧠 Ejemplos de Aplicación

### 🚗 Ejemplo 1: Fuerza Resultante Simple

**🎯 Problema**: Bloque de 5 kg empujado con 30 N en superficie sin fricción.

```mermaid
graph LR
    A[📦 Bloque 5 kg] --> B[💪 F = 30 N]
    B --> C[🚀 a = ?]
    
    style A fill:#e1f5fe
    style C fill:#e8f5e8
```

**🔧 Solución**: $$F = ma \Rightarrow a = \frac{F}{m} = \frac{30}{5} = 6 \text{ m/s}^2$$

**✅ Resultado**: $a = 6 \text{ m/s}^2$

---

### 🧱 Ejemplo 2: Plano Inclinado Sin Fricción

**🎯 Problema**: Bloque 10 kg en plano inclinado 30°, sin fricción.

```mermaid
graph TD
    A["📦 m = 10 kg"] --> B["📐 θ = 30°"]
    B --> C["🌍 Componente paralela<br/>mg sin θ"]
    C --> D["🚀 a = ?"]
    
    style A fill:#e1f5fe
    style D fill:#e8f5e8
```

**🔧 Solución**:

1. **Componente paralela del peso**: $$W_{\parallel} = mg \sin(\theta) = 10 \times 9.8 \times \sin(30°) = 49 \text{ N}$$
    
2. **Segunda ley de Newton**: $$a = \frac{F}{m} = \frac{49}{10} = 4.9 \text{ m/s}^2$$
    

**✅ Resultado**: $a = 4.9 \text{ m/s}^2$

---

### 🧲 Ejemplo 3: Sistema de Masas Conectadas

**🎯 Problema**: Dos bloques conectados por cuerda y polea. $m_1 = 4$ kg (horizontal), $m_2 = 2$ kg (colgante).

```mermaid
graph TD
    A["📦 m₁ = 4 kg<br/>(sobre mesa)"] --> B["🔗 Cuerda"]
    B --> C["⚙️ Polea"]
    C --> D["📦 m₂ = 2 kg<br/>(colgante)"]
    
    A --> E["🔗 Tensión T →"]
    D --> F["🌍 Peso m₂g ↓<br/>🔗 Tensión T ↑"]
    
    style A fill:#e1f5fe
    style D fill:#e1f5fe
```

**🔧 Análisis por DCL**:

#### 📦 Para $m_1$ (horizontal):

$$T = m_1 a \quad \text{...(1)}$$

#### 📦 Para $m_2$ (vertical):

$$m_2 g - T = m_2 a \quad \text{...(2)}$$

**🧮 Resolución del sistema**: Sustituyendo (1) en (2): $$m_2 g - m_1 a = m_2 a$$ $$m_2 g = a(m_1 + m_2)$$ $$a = \frac{m_2 g}{m_1 + m_2} = \frac{2 \times 9.8}{4 + 2} = 3.27 \text{ m/s}^2$$

**✅ Resultado**: $a = 3.27 \text{ m/s}^2$

**🔗 Tensión en la cuerda**: $$T = m_1 a = 4 \times 3.27 = 13.08 \text{ N}$$

---

## 💡 Recomendaciones Clave

### ✅ Buenas Prácticas

```mermaid
graph TD
    A[🎯 Estrategia Exitosa] --> B[📐 Dibuja DCL SIEMPRE]
    A --> C[📏 Define ejes claros]  
    A --> D[🧮 Descompón correctamente]
    A --> E[🔍 Verifica signos]
    A --> F[📝 Símbolos consistentes]
    
    style A fill:#e8f5e8
```

- **📐 DCL primero**: Nunca apliques fórmulas sin dibujar el diagrama
- **📏 Ejes coherentes**: Define x, y de manera consistente para todo el problema
- **🧮 Descomposición**: En planos inclinados, descompón peso correctamente
- **🔍 Signos**: Revisa dirección de aceleración antes de asignar signos
- **📝 Consistencia**: Usa los mismos símbolos en todo el desarrollo

### ❌ Errores Comunes a Evitar

```mermaid
graph TD
    A[⚠️ Errores Frecuentes] --> B[❌ No dibujar DCL]
    A --> C[❌ Confundir masa y peso]
    A --> D[❌ Mal manejo de signos]
    A --> E[❌ Olvidar vincular aceleraciones]
    A --> F[❌ Aplicar 3ª ley en mismo DCL]
    
    style A fill:#ffebee
```

---

## 🧠 Conceptos Fundamentales para Recordar

### 🎯 Principios Clave

> **🔑 Regla de Oro**: Las Leyes de Newton se aplican a cada objeto por separado.

#### 📋 Puntos Esenciales:

- **🎯 Análisis independiente**: Cada objeto tiene su propio DCL y ecuaciones
- **↔️ Tercera ley**: No se aplica dentro del mismo DCL, sino entre objetos
- **🔗 Sistemas múltiples**: Analiza cada cuerpo por separado, luego relaciona
- **⚖️ Equilibrio**: $\sum F = 0$ para objetos en reposo o velocidad constante
- **🚀 Aceleración**: Siempre en dirección de la fuerza neta

### 🌟 Jerarquía de Análisis

```mermaid
flowchart TD
    A[🌟 Sistema Completo] --> B[📦 Objeto 1]
    A --> C[📦 Objeto 2]
    A --> D[📦 Objeto n]
    
    B --> E[📐 DCL₁]
    C --> F[📐 DCL₂]  
    D --> G[📐 DCLₙ]
    
    E --> H[⚖️ ΣF₁ = m₁a₁]
    F --> I[⚖️ ΣF₂ = m₂a₂]
    G --> J[⚖️ ΣFₙ = mₙaₙ]
    
    H --> K[🔗 Relacionar aceleraciones]
    I --> K
    J --> K
    
    K --> L[📊 Sistema de ecuaciones]
    L --> M[✅ Solución]
```

---

## 🔗 Conexiones con Otros Temas

- [[Trabajo y Energía]]
- [[Principios de Conservación de la Energía]]
- [[Fuerzas y Diagramas de Cuerpo Libre]]
- [[Cinemática Traslacional]]

---

## 📌 Resumen Ejecutivo
>[!success] Recapitulando los conceptos.
Las **Leyes de Newton** proporcionan el framework fundamental para el análisis dinámico:
>
>- **1️⃣ Primera Ley**: Inercia → $\sum F = 0$ para equilibrio
>- **2️⃣ Segunda Ley**: Dinámica → $\sum F = ma$ para aceleración
>- **3️⃣ Tercera Ley**: Acción-reacción → Fuerzas en pares
>
>**🎯 Metodología clave**: DCL → Descomponer → Aplicar → Relacionar → Resolver
>
>¿Listo para aplicar lo aprendido? 💪✨
