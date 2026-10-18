---
dg-publish: true
---

# 📐 UML y Diagrama de Clases

## 🎯 Introducción

> [!info] 💡 ¿Qué es UML?
> 
> **UML** (Unified Modeling Language - Lenguaje Unificado de Modelado) es un **lenguaje visual estandarizado** para representar, diseñar y documentar sistemas orientados a objetos.
> 
> **Analogía del mundo real:** Así como los arquitectos usan planos antes de construir un edificio, los desarrolladores usan UML para diseñar software antes de programarlo.
> 
> **¿Por qué es importante?**
> 
> |Beneficio|Descripción|Ventaja|
> |---|---|---|
> |**Comunicación**|Lenguaje común entre desarrolladores|Todos entienden lo mismo|
> |**Diseño previo**|Planificar antes de codificar|Menos errores y retrabajos|
> |**Documentación**|Representación visual del sistema|Más fácil de entender que código|
> |**Análisis**|Identificar problemas de diseño|Corregir antes de implementar|

![[Diagramas/02_-_UML_y_diagrama_de_clases_01.svg]]

> [!note] 🎯 Enfoque de este Tema
> 
> Nos centraremos en el **Diagrama de Clases**, el más importante para POO y el que usarás en tus proyectos de Java.

---

## 📦 Diagrama de Clases: Conceptos Básicos

### 🔲 Representación de una Clase

> [!tip] 📋 Estructura de una Clase en UML
> 
> Una clase se representa como un **rectángulo dividido en 3 secciones**:
> 
> ![[Diagramas/02_-_UML_y_diagrama_de_clases_02.svg]]
> 
> **Secciones:**
> 
> |Sección|Contenido|Ejemplo|
> |---|---|---|
> |**Superior**|Nombre de la clase|`CuentaBancaria`|
> |**Media**|Atributos (variables)|`- saldo: double`|
> |**Inferior**|Métodos (funciones)|`+ depositar(monto: double): boolean`|

### 🔐 Modificadores de Visibilidad

> [!info] 🎨 Símbolos de Acceso
> 
> |Símbolo|Modificador|Significado|Uso|
> |---|---|---|---|
> |**-**|private|Solo accesible dentro de la clase|✅ Atributos|
> |**+**|public|Accesible desde cualquier lugar|✅ Métodos públicos|
> |**#**|protected|Accesible en la clase y subclases|Herencia|
> |**~**|default|Accesible en el mismo paquete|Uso interno|
> 
> **Regla general:**
> 
> - Atributos: `-` (private)
> - Getters/Setters y métodos públicos: `+` (public)
> - Métodos auxiliares: `-` (private)

### 📝 Sintaxis de Atributos y Métodos

> [!example] ✍️ Formato Completo
> 
> **Atributos:**
> 
> ```
> [visibilidad] nombreAtributo: tipo [= valorPorDefecto]
> ```
> 
> **Métodos:**
> 
> ```
> [visibilidad] nombreMétodo(parámetro: tipo): tipoRetorno
> ```
> 
> **Ejemplos:**
> 
> ![[Diagramas/02_-_UML_y_diagrama_de_clases_03.svg]]
> 
> **Equivalente en Java:**
> 
> ```java
> public class CuentaBancaria {
>     private double saldo = 0.0;
>     private String titular;
>     private String numeroCuenta;
>     
>     public CuentaBancaria(String titular) { }
>     public double getSaldo() { }
>     public boolean depositar(double monto) { }
>     public boolean retirar(double monto) { }
>     private boolean validarMonto(double monto) { }
> }
> ```

---

## 🔗 Relaciones entre Clases

### 📊 Tipos de Relaciones

> [!tip] 🌐 Relaciones Fundamentales
> 
> |Relación|Símbolo|Significado|Ejemplo|
> |---|---|---|---|
> |**Herencia**|`<|--`|"ES-UN"|
> |**Implementación**|`<|..`|Implementa interfaz|
> |**Asociación**|`--`|Usa o conoce|Persona tiene Dirección|
> |**Agregación**|`o--`|"TIENE-UN" (débil)|Departamento tiene Empleados|
> |**Composición**|`*--`|"TIENE-UN" (fuerte)|Coche tiene Motor|
> |**Dependencia**|`..>`|Usa temporalmente|Método usa otra clase|

### 🏛️ Herencia

> [!example] 👨‍👩‍👧 Jerarquía de Clases
> 
> **Símbolo:** Flecha con triángulo vacío `<|--`
> 
> ![[Diagramas/02_-_UML_y_diagrama_de_clases_04.svg]]
> 
> **Lectura:** "Perro hereda de Animal" o "Perro ES-UN Animal"

### 🔌 Implementación de Interfaces

> [!example] 📜 Interfaces
> 
> **Símbolo:** Flecha punteada con triángulo `<|..`
> 
> ![[Diagramas/02_-_UML_y_diagrama_de_clases_05.svg]]
> 
> **Nota:** Las interfaces se marcan con `<<interface>>`

### 🔗 Asociación

> [!example] 🤝 Relación Básica
> 
> **Símbolo:** Línea simple `--`
> 
> Indica que una clase **conoce** o **usa** otra clase.
> 
> ![[Diagramas/02_-_UML_y_diagrama_de_clases_06.svg]]
> 
> **Multiplicidad:**
> 
> - `1` : Uno
> - `*` o `0..*` : Muchos (cero o más)
> - `1..*` : Uno o más
> - `0..1` : Cero o uno

### 🔷 Agregación

> [!example] 📦 "Tiene-Un" (Débil)
> 
> **Símbolo:** Rombo vacío `o--`
> 
> Las partes pueden existir **independientemente** del todo.
> 
> ![[Diagramas/02_-_UML_y_diagrama_de_clases_07.svg]]
> 
> **Característica:** Si el Departamento se elimina, los Empleados siguen existiendo.

### 🔶 Composición

> [!example] 🏗️ "Tiene-Un" (Fuerte)
> 
> **Símbolo:** Rombo lleno `*--`
> 
> Las partes **NO pueden existir** sin el todo.
> 
> ![[Diagramas/02_-_UML_y_diagrama_de_clases_08.svg]]
> 
> **Característica:** Si el Coche se destruye, su Motor específico también se destruye.

### ⚡ Dependencia

> [!example] 🔄 Uso Temporal
> 
> **Símbolo:** Flecha punteada `..>`
> 
> Una clase **usa** temporalmente otra (parámetro, variable local).
> 
> ![[Diagramas/02_-_UML_y_diagrama_de_clases_09.svg]]

---

## 🎨 Elementos Especiales

### 🔸 Clases Abstractas

> [!example] 🏗️ Clases No Instanciables
> 
> Se representan con el nombre en **cursiva** o con `<<abstract>>`.
> 
> ![[Diagramas/02_-_UML_y_diagrama_de_clases_10.svg]]
> 
> **Nota:** Los métodos abstractos se marcan con `*` o en _cursiva_.

### 🔹 Atributos y Métodos Estáticos

> [!example] ⚡ Miembros de Clase
> 
> Se **subrayan** para indicar que son `static`.
> 
> ![[Diagramas/02_-_UML_y_diagrama_de_clases_11.svg]]
> 
> **Nota:** `$` indica miembro estático (algunos diagramadores usan subrayado).

### 📦 Enumeraciones

> [!example] 🎯 Tipos Enumerados
> 
> ![[Diagramas/02_-_UML_y_diagrama_de_clases_12.svg]]

---

## 📚 Ejemplos Completos

### 🏦 Sistema Bancario

> [!example] 💳 Diagrama Completo
> 
> ![[Diagramas/02_-_UML_y_diagrama_de_clases_13.svg]]

### 🎓 Sistema Universitario

> [!example] 📖 Gestión Académica
> 
> ![[Diagramas/02_-_UML_y_diagrama_de_clases_14.svg]]

### 🛒 Sistema de Comercio

> [!example] 🏪 E-commerce
> 
> ![[Diagramas/02_-_UML_y_diagrama_de_clases_15.svg]]

---

## 🎯 Buenas Prácticas

> [!success] ✅ Recomendaciones para Diagramas UML
> 
> **1. Claridad sobre completitud:**
> 
> - No incluyas TODOS los métodos getter/setter si son obvios
> - Enfócate en los métodos importantes de la lógica
> 
> **2. Nivel de detalle apropiado:**
> 
> - **Alto nivel:** Solo nombres de clases y relaciones principales
> - **Detallado:** Atributos y métodos principales
> - **Completo:** Todo (para documentación final)
> 
> **3. Organización visual:**
> 
> - Clases relacionadas cerca una de otra
> - Superclases arriba, subclases abajo
> - Interfaces a la izquierda o arriba
> 
> **4. Nomenclatura consistente:**
> 
> - Clases: `PascalCase`
> - Atributos y métodos: `camelCase`
> - Constantes: `UPPER_SNAKE_CASE`
> 
> **5. Uso de colores (opcional):**
> 
> - Verde: Clases principales
> - Azul: Clases auxiliares
> - Amarillo: Interfaces
> - Rojo: Clases abstractas
>

> [!warning] ⚠️ Errores Comunes
> 
> **❌ Evitar:**
> 
> 1. **Sobrecargar el diagrama** - Demasiadas clases en un solo diagrama
> 2. **Falta de relaciones** - Clases aisladas sin mostrar cómo se conectan
> 3. **Inconsistencia** - Mezclar niveles de detalle
> 4. **Omitir multiplicidad** - No mostrar cardinalidad en asociaciones
> 5. **Relaciones incorrectas** - Usar composición cuando es agregación
> 
> **✅ Hacer:**
> 
> 6. **Dividir en diagramas** - Un diagrama por subsistema
> 7. **Mostrar relaciones clave** - Las que realmente importan
> 8. **Mantener consistencia** - Mismo nivel en todo el diagrama
> 9. **Indicar multiplicidad** - 1, *, 0..1, etc.
> 10. **Elegir relación correcta** - Entender diferencia entre agregación y composición

---

## 📊 Comparativa de Relaciones

> [!info] 🔍 Guía Rápida de Decisión
> 
> |Pregunta|Sí →|No →|
> |---|---|---|
> |¿Clase B ES-UN tipo de Clase A?|**Herencia** `<|--`|
> |¿Clase B implementa interfaz A?|**Implementación** `<|..`|
> |¿Clase A contiene Clase B y B no puede existir sin A?|**Composición** `*--`|Siguiente pregunta|
> |¿Clase A contiene Clase B pero B puede existir independiente?|**Agregación** `o--`|Siguiente pregunta|
> |¿Clase A solo usa temporalmente Clase B?|**Dependencia** `..>`|**Asociación** `--`|

![[Diagramas/02_-_UML_y_diagrama_de_clases_16.svg]]

---

## 🛠️ Herramientas para UML

> [!tip] 🔧 Software Recomendado
> 
> |Herramienta|Tipo|Características|Recomendado Para|
> |---|---|---|---|
> |**PlantUML**|Texto|Código → Diagrama|Programadores|
> |**Draw.io**|Visual|Gratuito, online|Principiantes|
> |**StarUML**|Visual|Profesional|Proyectos grandes|
> |**Lucidchart**|Visual|Colaborativo, online|Equipos|
> |**Visual Paradigm**|Visual|Completo, generación código|Empresas|
> |**Mermaid**|Texto|Integrado en Markdown|Documentación|

---

## 📋 Resumen Visual

![[Diagramas/02_-_UML_y_diagrama_de_clases_17.svg]]

> [!quote] 💡 Recuerda
> 
> **"Un buen diagrama UML vale más que mil líneas de documentación"**
> 
> - Diseña **antes** de codificar
> - Mantén los diagramas **actualizados** con el código
> - Usa el **nivel de detalle** apropiado para tu audiencia
> - Los diagramas son para **comunicar**, no para impresionar

---

## 🎯 Checklist de Diseño

> [!success] ✅ Antes de Implementar
> 
> **Diseño de clases:**
> 
> - [ ] ¿Están identificadas todas las clases necesarias?
> - [ ] ¿Los nombres de clases son descriptivos?
> - [ ] ¿Los atributos tienen el modificador correcto (private)?
> - [ ] ¿Los métodos públicos exponen solo lo necesario?
> 
> **Relaciones:**
> 
> - [ ] ¿Las herencias representan relaciones "ES-UN" válidas?
> - [ ] ¿Las composiciones vs agregaciones están bien diferenciadas?
> - [ ] ¿La multiplicidad está indicada correctamente?
> - [ ] ¿No hay dependencias circulares problemáticas?
> 
> **Organización:**
> 
> - [ ] ¿El diagrama es legible y claro?
> - [ ] ¿Las interfaces están claramente marcadas?
> - [ ] ¿Las clases abstractas son identificables?
> - [ ] ¿El nivel de detalle es consistente?

---

**Tags:** #uml #diagrama-clases #diseño #modelado #poo #relaciones #herencia #composicion #agregacion #arquitectura