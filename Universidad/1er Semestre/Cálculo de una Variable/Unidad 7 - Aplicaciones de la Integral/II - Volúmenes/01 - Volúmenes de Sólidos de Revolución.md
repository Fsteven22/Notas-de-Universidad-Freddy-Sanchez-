---
dg-publish: true
tags: [MATG1045, unidad7, volumenes-de-solidos-de-revolucion, cálculo, integrales, volúmenes, sólidos-revolución, geometría, aplicaciones-integrales, métodos-integración, disco, arandelas]
---

# 🌪 Volúmenes de Sólidos de Revolución ️

> [!info]+ **Definición Fundamental** Los **sólidos de revolución** son figuras tridimensionales generadas al rotar una región plana alrededor de un eje. El cálculo de sus volúmenes requiere técnicas específicas de integración que aprovechan la simetría rotacional.
>
> 📐 **Concepto clave**: Cada método aprovecha una geometría específica (discos, arandelas, o cilindros) para aproximar el volumen total.

## 💿 Método del Disco

> [!tip]+ **Fundamento del Método**
>
> ### Principio Básico
>
> Cuando una función $f(x) \geq 0$ se rota alrededor del eje $x$, genera discos perpendiculares al eje de rotación.
>
> ### Fórmula General
>
> $$V = \pi \int_a^b [f(x)]^2 , dx$$
>
> ### Elementos del Disco
>
> |Elemento|Descripción|Medida|
> |---|---|---|
> |🎯 Centro|En el eje de rotación|$(x, 0)$|
> |📏 Radio|Distancia de la función al eje|$f(x)$|
> |📐 Área|Área del disco circular|$\pi [f(x)]^2$|
> |📊 Grosor|Diferencial del eje|$dx$|
>

> [!example]+ **Ejemplo Práctico** **Problema**: Encontrar el volumen del sólido generado al rotar $f(x) = \sqrt{x}$ alrededor del eje $x$ en $[0, 4]$.
>
> **Solución**: $$V = \pi \int_0^4 (\sqrt{x})^2 , dx = \pi \int_0^4 x , dx = \pi \left[\frac{x^2}{2}\right]_0^4 = 8\pi$$

> [!info] 🖼️ Método del Disco
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Volúmenes_de_Sólidos_de_Revolución_01.svg]]
>
> **Se lee así:** Seis rectángulos en línea recta, sin ninguna decisión: la función entra en la rotación alrededor de un eje, esa rotación genera **discos**, el disco toma como radio el valor de la función, su área resulta $\pi[f(x)]^2$ y al integrar esa área aparece el volumen. Cada caja es el eslabón siguiente, así que la fórmula se construye paso a paso.
>
> **Por qué importa:** El método del disco se entiende como una suma de círculos, no como una fórmula que sale de la nada. Así justificas cada factor: el $\pi$ del círculo, el cuadrado del radio y el $dx$ como **grosor del disco**.
>
> **Ejemplo:** Al rotar $f(x) = \sqrt{x}$ alrededor del eje $x$ en $[0, 4]$ la nota aplica el método del disco y obtiene $V = \pi \int_0^4 (\sqrt{x})^2 dx = 8\pi$.

## 🍩 Método de las Arandelas

> [!warning]+ **Diferencia Clave con Discos** Las **arandelas** se forman cuando hay una cavidad interior en el sólido de revolución. Esto ocurre cuando rotamos una región entre dos funciones.
>

> [!info]+ **Configuración de Arandelas**
>
> ### Cuando usar este método
>
> - Rotación de una región entre dos curvas: $f(x) \geq g(x) \geq 0$
> - La región no toca el eje de rotación
>
> ### Fórmula General
>
> $$V = \pi \int_a^b \left([f(x)]^2 - [g(x)]^2\right) dx$$
>
> ### Componentes
>
> |Elemento|Valor|Significado|
> |---|---|---|
> |🔴 Radio exterior|$R = f(x)$|Función superior|
> |🔵 Radio interior|$r = g(x)$|Función inferior|
> |🍩 Área arandela|$\pi(R^2 - r^2)$|Diferencia de áreas|
>

> [!example]+ **Ejemplo de Arandelas** **Problema**: Volumen del sólido generado rotando la región entre $f(x) = x + 2$ y $g(x) = x^2$ alrededor del eje $x$ en $[-1, 2]$.
>
> **Solución**: $$V = \pi \int_{-1}^2 \left[(x+2)^2 - (x^2)^2\right] dx$$ $$= \pi \int_{-1}^2 \left[x^2 + 4x + 4 - x^4\right] dx$$

> [!info] 🖼️ Método de las Arandelas
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Volúmenes_de_Sólidos_de_Revolución_02.svg]]
>
> **Se lee así:** La región entre curvas se abre en dos ramas paralelas, una que identifica la **función exterior** y otra la interior. Cada rama produce su propio radio y ambas desembocan en la misma caja central, donde el anillo se modela como la diferencia entre el área del disco grande y la del hueco. Solo entonces se integra esa diferencia para dar el volumen.
>
> **Por qué importa:** La arandela es la generalización del disco cuando hay una cavidad, y su fórmula se obtiene **restando dos áreas**, no inventándola. Identificar bien qué función da el radio exterior evita el error de invertir los radios y perder el signo.
>
> **Ejemplo:** Rotando la región entre $f(x) = x + 2$ y $g(x) = x^2$ alrededor del eje $x$ en $[-1, 2]$, la nota usa $V = \pi \int_{-1}^{2} [(x+2)^2 - (x^2)^2] dx$.

## 🥤 Método de las Capas Cilíndricas

> [!tip]+ **Cuándo es Más Eficiente** Este método es especialmente útil cuando:
>
> - La rotación es alrededor del eje $y$
> - Es complicado expresar $x$ en función de $y$
> - La región tiene forma "vertical" natural
>

> [!info]+ **Fundamento del Método**
>
> ### Visualización
>
> Imaginamos **cilindros concéntricos** de grosor infinitesimal, como capas de una cebolla.
>
> ### Fórmula General (rotación alrededor del eje y)
>
> $$V = 2\pi \int_a^b x \cdot f(x) , dx$$
>
> ### Componentes del Cilindro
>
> |Elemento|Valor|Descripción|
> |---|---|---|
> |🎯 Radio|$x$|Distancia al eje y|
> |📏 Altura|$f(x)$|Altura de la función|
> |🔄 Circunferencia|$2\pi x$|Perímetro del cilindro|
> |📐 Área lateral|$2\pi x \cdot f(x)$|Superficie del cilindro|
> |📏 Grosor|$dx$|Diferencial|
>

> [!example]+ **Ejemplo de Capas Cilíndricas** **Problema**: Volumen del sólido generado rotando $f(x) = x^2$ alrededor del eje $y$ en $[0, 2]$.
>
> **Solución**: $$V = 2\pi \int_0^2 x \cdot x^2 , dx = 2\pi \int_0^2 x^3 , dx$$ $$= 2\pi \left[\frac{x^4}{4}\right]_0^2 = 2\pi \cdot 4 = 8\pi$$

> [!info] 🖼️ Método de las Capas Cilíndricas
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Volúmenes_de_Sólidos_de_Revolución_03.svg]]
>
> **Se lee así:** La función entra en la rotación alrededor del eje $y$, que produce **cilindros concéntricos**, y desde ahí el flujo se bifurca: una rama da el radio y otra la altura. Ambas vuelven a juntarse en la caja de la circunferencia, que multiplicada por la altura da el área lateral del cilindro, y esa área lateral es la que finalmente se integra para obtener el volumen.
>
> **Por qué importa:** Las capas cilíndricas son el método natural cuando se rota alrededor del eje $y$, y te ahorran despejar $x$ en función de $y$. Ver la circunferencia $2\pi x$ como la fuente del factor te evita **olvidar ese $2\pi$**, el error más común.
>
> **Ejemplo:** Rotando $f(x) = x^2$ alrededor del eje $y$ en $[0, 2]$, la nota arma $V = 2\pi \int_0^2 x \cdot x^2 dx$ y llega a $8\pi$.

## 📊 Comparación de Métodos

> [!info]+ **Tabla Comparativa**
>
> |Aspecto|Disco 💿|Arandelas 🍩|Capas Cilíndricas 🥤|
> |---|---|---|---|
> |**Geometría**|Círculos sólidos|Círculos con agujero|Cilindros huecos|
> |**Rotación típica**|Eje x|Eje x|Eje y|
> |**Fórmula**|$\pi\int[f(x)]^2dx$|$\pi\int([f(x)]^2-[g(x)]^2)dx$|$2\pi\int x·f(x)dx$|
> |**Cuándo usar**|Una función, eje x|Entre dos funciones|Rotación eje y|
> |**Ventaja**|Más simple|Maneja cavidades|Evita inversión de función|

## 🎯 Técnicas de Estudio

> [!tip]+ **Mnemotecnia para Recordar Fórmulas**
>
> ### Regla "DCA" (Disco-Capas-Arandelas)
>
> - 🥏 **D**isco: "**D**iámetro al cuadrado" → $\pi[f(x)]^2$
> - 🥤 **C**apas: "**C**ircunferencia por altura" → $2\pi x \cdot f(x)$
> - 🍩 **A**randelas: "**A**fuera menos adentro" → $\pi(R^2 - r^2)$
>
> ### Estrategia de Visualización
>
> 1. 👁️ **Visualiza** la región original
> 2. 🔄 **Rota** mentalmente alrededor del eje
> 3. 🔍 **Identifica** la forma geométrica resultante
> 4. 📐 **Aplica** la fórmula correspondiente
>

> [!warning]+ **Errores Comunes a Evitar**
>
> - ❌ Olvidar el $\pi$ en métodos de disco y arandelas
> - ❌ Confundir radio interior y exterior en arandelas
> - ❌ No considerar el $2\pi$ en capas cilíndricas
> - ❌ Usar límites incorrectos de integración

## 📚 Referencias

> [!quote]+ **Enlaces a Notas Relacionadas**
>
> - [[Unidad 6 - Integrales/Técnicas de Integración/01 - Cambio de Variable en Integrales.md#Integrales Definidas|Integrales Definidas]] - Base matemática fundamental
> - Aplicaciones de la Integral - Contexto más amplio
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida.md|01 - Métodos de Integración Definida.md]] - Técnicas necesarias para resolver
> - Geometría Analítica - Para visualización espacial
> - Funciones y sus Gráficas - Interpretación de las regiones

## 📖 Notas Recomendadas para Complementar

> [!info]+ **Prerrequisitos Esenciales**
>
> - [[02 – Aplicaciones de la Diferencial y la Hessiana#📚 Ejemplos: Cálculo de Diferenciales]] - Derivadas y funciones
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral.md|02 - Propiedades de la Integral.md]] - Antiderivadas básicas

> [!quote] ❝ Notas Recomendadas para Complementar
>
> - [[../../../../2do Semestre/Cálculo Vectorial/Cálculo Vectorial|Cálculo Vectorial]] - Derivadas y funciones
> - Integrales Indefinidas - Antiderivadas básicas
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo.md|04 - Teorema Fundamental del Cálculo.md]] - Conexión derivada-integral
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/02 - Área entre Curvas.md|02 - Área entre Curvas.md]] - Fundamentos de regiones
>
> **Temas Complementarios**
>
> - [[02 - Coordenadas polares]] - Para casos más complejos
> - [[03 - Superficies de revolución]] - Extensión natural
> - Momentos y Centros de Masa - Otras aplicaciones
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/03 - Derivadas Paramétricas.md#Longitud de Arco|Longitud de Arco]] - Medidas en curvas

---

**Tags:** #MATG1045 #unidad7 #volumenes-de-solidos-de-revolucion #cálculo #integrales #volúmenes #sólidos-revolución #geometría #aplicaciones-integrales #métodos-integración #disco #arandelas #capas-cilíndricas #visualización-3d
