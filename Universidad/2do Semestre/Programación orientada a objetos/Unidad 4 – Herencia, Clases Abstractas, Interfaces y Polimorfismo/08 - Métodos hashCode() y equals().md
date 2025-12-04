# 🔢 Métodos `hashCode()` y `equals()`

## 🎯 Introducción

> [!info]- 💡 ¿Qué son `equals()` y `hashCode()`? Son dos métodos fundamentales de la clase `Object` que **definen cómo se comparan objetos** y cómo se organizan en colecciones hash.
> 
> **Analogía:** Como huellas digitales
> 
> - **`equals()`**: Compara si dos personas son la misma (comparación detallada)
> - **`hashCode()`**: Código de identificación rápida (número único)
> 
> **Objetivos principales:**
> 
> - **Comparar objetos** por contenido, no por referencia
> - **Organizar objetos** en HashMap, HashSet, etc.
> - **Mantener contrato** entre ambos métodos
> - **Optimizar búsquedas** en colecciones

---

## 📋 El Método `equals()`

### 🔍 Comparación por Referencia vs Contenido

> [!example]- 🎯 El Problema Básico **Comportamiento por defecto:**
> 
> ```java
> public class Persona {
>     private String nombre;
>     private int edad;
>     
>     public Persona(String nombre, int edad) {
>         this.nombre = nombre;
>         this.edad = edad;
>     }
> }
> 
> // Problema: equals() heredado compara referencias
> Persona p1 = new Persona("Ana", 25);
> Persona p2 = new Persona("Ana", 25);
> 
> System.out.println(p1 == p2);         // false (diferentes referencias)
> System.out.println(p1.equals(p2));    // false (usa equals() de Object)
> 
> // ¡Mismo contenido pero diferentes objetos!
> ```
> 
> **Solución: Sobrescribir `equals()`:**
> 
> ```java
> public class Persona {
>     private String nombre;
>     private int edad;
>     
>     @Override
>     public boolean equals(Object obj) {
>         // 1. Verificar si es la misma referencia
>         if (this == obj) return true;
>         
>         // 2. Verificar si es null
>         if (obj == null) return false;
>         
>         // 3. Verificar si es la misma clase
>         if (getClass() != obj.getClass()) return false;
>         
>         // 4. Hacer casting y comparar atributos
>         Persona otra = (Persona) obj;
>         return edad == otra.edad && 
>                nombre.equals(otra.nombre);
>     }
> }
> 
> // Ahora funciona correctamente
> Persona p1 = new Persona("Ana", 25);
> Persona p2 = new Persona("Ana", 25);
> System.out.println(p1.equals(p2));  // true ✅
> ```

### ✅ Contrato de `equals()`

> [!success]- 📜 Las 5 Reglas Obligatorias **1. Reflexivo:** `x.equals(x)` debe ser `true`
> 
> ```java
> Persona p = new Persona("Ana", 25);
> p.equals(p);  // true ✅
> ```
> 
> **2. Simétrico:** Si `x.equals(y)` es `true`, entonces `y.equals(x)` es `true`
> 
> ```java
> p1.equals(p2) == p2.equals(p1);  // true ✅
> ```
> 
> **3. Transitivo:** Si `x.equals(y)` y `y.equals(z)`, entonces `x.equals(z)`
> 
> ```java
> if (p1.equals(p2) && p2.equals(p3)) {
>     p1.equals(p3);  // true ✅
> }
> ```
> 
> **4. Consistente:** Múltiples llamadas retornan el mismo resultado
> 
> ```java
> p1.equals(p2);  // true
> p1.equals(p2);  // true (siempre igual si no cambian)
> ```
> 
> **5. Null:** `x.equals(null)` debe ser `false`
> 
> ```java
> p1.equals(null);  // false ✅
> ```

### 🎨 Patrones de Implementación

> [!tip]- 📝 Implementación Completa **Ejemplo: Clase Estudiante**
> 
> ```java
> public class Estudiante {
>     private String codigo;
>     private String nombre;
>     private double promedio;
>     
>     public Estudiante(String codigo, String nombre, double promedio) {
>         this.codigo = codigo;
>         this.nombre = nombre;
>         this.promedio = promedio;
>     }
>     
>     @Override
>     public boolean equals(Object obj) {
>         // ① Mismo objeto
>         if (this == obj) return true;
>         
>         // ② Null check
>         if (obj == null) return false;
>         
>         // ③ Verificar clase
>         if (getClass() != obj.getClass()) return false;
>         
>         // ④ Casting y comparación
>         Estudiante otro = (Estudiante) obj;
>         
>         // Comparar atributos importantes
>         if (!codigo.equals(otro.codigo)) return false;
>         if (!nombre.equals(otro.nombre)) return false;
>         
>         // Comparar doubles con tolerancia
>         return Math.abs(promedio - otro.promedio) < 0.001;
>     }
> }
> ```
> 
> **Comparando solo campos clave:**
> 
> ```java
> public class Producto {
>     private String sku;        // Identificador único
>     private String nombre;
>     private double precio;
>     private int stock;
>     
>     @Override
>     public boolean equals(Object obj) {
>         if (this == obj) return true;
>         if (obj == null || getClass() != obj.getClass()) return false;
>         
>         Producto otro = (Producto) obj;
>         // Solo comparar SKU (campo único)
>         return sku.equals(otro.sku);
>     }
> }
> ```

---

## #️⃣ El Método `hashCode()`

### 🔢 ¿Qué es un Hash Code?

> [!info]- 🎲 Código Numérico de Identificación **Propósito:** Generar un número entero que representa al objeto
> 
> ```java
> Persona p1 = new Persona("Ana", 25);
> System.out.println(p1.hashCode());  // Ej: 1735600054
> 
> Persona p2 = new Persona("Ana", 25);
> System.out.println(p2.hashCode());  // Debe ser igual si equals() es true
> ```
> 
> **Uso principal:** Organizar objetos en **estructuras hash**
> 
> ```java
> HashSet<Persona> personas = new HashSet<>();
> personas.add(p1);
> 
> // Usa hashCode() para encontrar rápidamente
> personas.contains(p2);  // Busca por hash primero
> ```

### ⚖️ Contrato entre `equals()` y `hashCode()`

> [!warning]- 🔗 Regla de Oro: SIEMPRE Sobrescribir Ambos **Reglas obligatorias:**
> 
> 1️⃣ **Si `equals()` es true → `hashCode()` debe ser igual**
> 
> ```java
> if (obj1.equals(obj2)) {
>     obj1.hashCode() == obj2.hashCode();  // OBLIGATORIO
> }
> ```
> 
> 2️⃣ **Si `hashCode()` es diferente → `equals()` debe ser false**
> 
> ```java
> if (obj1.hashCode() != obj2.hashCode()) {
>     obj1.equals(obj2);  // false
> }
> ```
> 
> 3️⃣ **Si `hashCode()` es igual → `equals()` PUEDE ser true o false**
> 
> ```java
> // Colisión permitida (pero indeseable)
> obj1.hashCode() == obj2.hashCode();
> obj1.equals(obj2);  // Puede ser true o false
> ```
> 
> **❌ Error común:**
> 
> ```java
> public class Persona {
>     private String nombre;
>     
>     @Override
>     public boolean equals(Object obj) {
>         // Implementado correctamente
>         if (obj == null || getClass() != obj.getClass()) return false;
>         Persona otra = (Persona) obj;
>         return nombre.equals(otra.nombre);
>     }
>     
>     // ❌ NO sobrescribir hashCode() rompe el contrato
> }
> 
> // Consecuencias:
> Set<Persona> set = new HashSet<>();
> Persona p1 = new Persona("Ana");
> Persona p2 = new Persona("Ana");
> 
> set.add(p1);
> set.add(p2);  // Se agregan ambos (debería ser uno solo)
> System.out.println(set.size());  // 2 ❌ (debería ser 1)
> ```

### 🎨 Implementación de `hashCode()`

> [!success]- 📐 Fórmulas Comunes **Método 1: Usar `Objects.hash()` (Recomendado)**
> 
> ```java
> import java.util.Objects;
> 
> public class Persona {
>     private String nombre;
>     private int edad;
>     private String email;
>     
>     @Override
>     public int hashCode() {
>         return Objects.hash(nombre, edad, email);
>     }
> }
> ```
> 
> **Método 2: Algoritmo manual (31 × hash + campo)**
> 
> ```java
> @Override
> public int hashCode() {
>     int result = 17;  // Número primo inicial
>     result = 31 * result + nombre.hashCode();
>     result = 31 * result + edad;
>     result = 31 * result + email.hashCode();
>     return result;
> }
> ```
> 
> **Método 3: Solo campos clave**
> 
> ```java
> public class Producto {
>     private String sku;  // Identificador único
>     private String nombre;
>     private double precio;
>     
>     @Override
>     public int hashCode() {
>         return sku.hashCode();  // Solo el campo único
>     }
>     
>     @Override
>     public boolean equals(Object obj) {
>         if (this == obj) return true;
>         if (obj == null || getClass() != obj.getClass()) return false;
>         Producto otro = (Producto) obj;
>         return sku.equals(otro.sku);
>     }
> }
> ```

---

## 🎯 Ejemplo Completo: Sistema de Biblioteca

> [!example]- 📚 Implementación Práctica
> 
> ```java
> import java.util.*;
> 
> public class Libro {
>     private String isbn;
>     private String titulo;
>     private String autor;
>     
>     public Libro(String isbn, String titulo, String autor) {
>         this.isbn = isbn;
>         this.titulo = titulo;
>         this.autor = autor;
>     }
>     
>     // Getters
>     public String getIsbn() { return isbn; }
>     public String getTitulo() { return titulo; }
>     public String getAutor() { return autor; }
>     
>     // equals() basado en ISBN (identificador único)
>     @Override
>     public boolean equals(Object obj) {
>         if (this == obj) return true;
>         if (obj == null || getClass() != obj.getClass()) return false;
>         Libro otro = (Libro) obj;
>         return isbn.equals(otro.isbn);
>     }
>     
>     // hashCode() consistente con equals()
>     @Override
>     public int hashCode() {
>         return isbn.hashCode();
>     }
>     
>     @Override
>     public String toString() {
>         return titulo + " - " + autor + " (ISBN: " + isbn + ")";
>     }
> }
> 
> // Clase Socio
> class Socio {
>     private String numeroSocio;
>     private String nombre;
>     private String email;
>     
>     public Socio(String numeroSocio, String nombre, String email) {
>         this.numeroSocio = numeroSocio;
>         this.nombre = nombre;
>         this.email = email;
>     }
>     
>     @Override
>     public boolean equals(Object obj) {
>         if (this == obj) return true;
>         if (obj == null || getClass() != obj.getClass()) return false;
>         Socio otro = (Socio) obj;
>         return numeroSocio.equals(otro.numeroSocio);
>     }
>     
>     @Override
>     public int hashCode() {
>         return numeroSocio.hashCode();
>     }
>     
>     @Override
>     public String toString() {
>         return nombre + " (" + numeroSocio + ")";
>     }
> }
> 
> // Programa de prueba
> class TestBiblioteca {
>     public static void main(String[] args) {
>         // Crear libros
>         Libro l1 = new Libro("978-1", "Java Básico", "Autor A");
>         Libro l2 = new Libro("978-1", "Java Básico", "Autor A");  // Mismo ISBN
>         Libro l3 = new Libro("978-2", "Java Avanzado", "Autor B");
>         
>         // Probar equals()
>         System.out.println("=== EQUALS ===");
>         System.out.println("l1 == l2: " + (l1 == l2));           // false
>         System.out.println("l1.equals(l2): " + l1.equals(l2));   // true ✅
>         System.out.println("l1.equals(l3): " + l1.equals(l3));   // false
>         
>         // Probar hashCode()
>         System.out.println("\n=== HASHCODE ===");
>         System.out.println("l1.hashCode(): " + l1.hashCode());
>         System.out.println("l2.hashCode(): " + l2.hashCode());
>         System.out.println("Mismo hash: " + (l1.hashCode() == l2.hashCode()));  // true ✅
>         
>         // HashSet (no permite duplicados)
>         System.out.println("\n=== HASHSET ===");
>         Set<Libro> biblioteca = new HashSet<>();
>         biblioteca.add(l1);
>         biblioteca.add(l2);  // No se agrega (duplicado)
>         biblioteca.add(l3);
>         
>         System.out.println("Tamaño: " + biblioteca.size());  // 2 ✅
>         System.out.println("Contiene l2: " + biblioteca.contains(l2));  // true ✅
>         
>         // HashMap (clave: Libro, valor: cantidad)
>         System.out.println("\n=== HASHMAP ===");
>         Map<Libro, Integer> inventario = new HashMap<>();
>         inventario.put(l1, 5);
>         inventario.put(l2, 3);  // Reemplaza el valor de l1
>         inventario.put(l3, 2);
>         
>         System.out.println("Inventario:");
>         inventario.forEach((libro, cant) -> 
>             System.out.println("  " + libro + ": " + cant + " copias")
>         );
>     }
> }
> ```

---

## ⚠️ Errores Comunes

> [!warning]- 🚫 Violaciones del Contrato **1. Sobrescribir solo `equals()`:**
> 
> ```java
> // ❌ MAL
> public class Persona {
>     private String nombre;
>     
>     @Override
>     public boolean equals(Object obj) {
>         // ... implementación correcta
>     }
>     // ❌ Falta hashCode()
> }
> 
> // Problema:
> Set<Persona> set = new HashSet<>();
> set.add(new Persona("Ana"));
> set.add(new Persona("Ana"));  // Se agregan ambos ❌
> ```
> 
> **2. Usar campos mutables:**
> 
> ```java
> // ❌ MAL
> public class Persona {
>     private String nombre;  // Mutable
>     
>     @Override
>     public boolean equals(Object obj) {
>         Persona otra = (Persona) obj;
>         return nombre.equals(otra.nombre);
>     }
>     
>     @Override
>     public int hashCode() {
>         return nombre.hashCode();
>     }
> }
> 
> // Problema:
> Set<Persona> set = new HashSet<>();
> Persona p = new Persona("Ana");
> set.add(p);
> p.setNombre("María");  // Cambia el hash ❌
> set.contains(p);  // false (no se encuentra) ❌
> ```
> 
> **3. No verificar null:**
> 
> ```java
> // ❌ MAL
> @Override
> public boolean equals(Object obj) {
>     Persona otra = (Persona) obj;  // NullPointerException si obj es null
>     return nombre.equals(otra.nombre);
> }
> ```

---

## ✅ Buenas Prácticas

> [!tip]- 🌟 Recomendaciones **1. Usar solo campos inmutables:**
> 
> ```java
> public class Persona {
>     private final String dni;  // Inmutable
>     private String nombre;     // Mutable pero no se usa en equals/hashCode
>     
>     @Override
>     public boolean equals(Object obj) {
>         Persona otra = (Persona) obj;
>         return dni.equals(otra.dni);  // Solo campo inmutable
>     }
>     
>     @Override
>     public int hashCode() {
>         return dni.hashCode();
>     }
> }
> ```
> 
> **2. Usar `Objects.equals()` y `Objects.hash()`:**
> 
> ```java
> import java.util.Objects;
> 
> @Override
> public boolean equals(Object obj) {
>     if (this == obj) return true;
>     if (!(obj instanceof Persona)) return false;
>     Persona otra = (Persona) obj;
>     return Objects.equals(nombre, otra.nombre) &&
>            edad == otra.edad;
> }
> 
> @Override
> public int hashCode() {
>     return Objects.hash(nombre, edad);
> }
> ```
> 
> **3. Siempre usar `@Override`:**
> 
> ```java
> @Override  // Detecta errores de firma
> public boolean equals(Object obj) { 
>     // ...
> }
> ```

---

## 🎓 Ejercicios

> [!example]- 💪 Práctica **Nivel Básico:**
> 
> 1. Implementar `equals()` y `hashCode()` para clase `Punto(x, y)`
> 2. Clase `Rectangulo` comparando por dimensiones
> 3. Clase `Email` comparando por dirección (ignorar mayúsculas)
> 
> **Nivel Intermedio:** 4. Clase `Estudiante` con código único 5. Clase `Producto` con SKU único 6. Usar HashSet para evitar duplicados
> 
> **Nivel Avanzado:** 7. Sistema de caché con HashMap usando objetos personalizados 8. Implementar búsqueda rápida en colecciones grandes

---

**Tags:** #java #equals #hashcode #comparacion #colecciones #hashmap #hashset #contrato