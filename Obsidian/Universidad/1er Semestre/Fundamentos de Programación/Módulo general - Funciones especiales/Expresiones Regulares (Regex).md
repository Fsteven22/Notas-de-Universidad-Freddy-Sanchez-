---

### **Expresiones Regulares (Regex)**

---

### Contexto

Las Expresiones Regulares, comúnmente abreviadas como Regex o Regexp, son secuencias de caracteres que forman un patrón de búsqueda. Son una herramienta increíblemente poderosa para manipular cadenas de texto: permiten buscar, reemplazar y validar texto de maneras muy complejas y eficientes. Son fundamentales en tareas como la validación de formatos (correos electrónicos, números de teléfono), el análisis de logs, el procesamiento de texto y la extracción de información específica de grandes volúmenes de datos.

### Fórmula/Procedimiento

En Python, las expresiones regulares se trabajan principalmente con el módulo `re`.

#### **1. Importar el Módulo `re`:**

Python

```
import re
```

#### **2. Funciones Comunes del Módulo `re`:**

- **`re.search(patron, cadena)`**:
    
    - Busca el primer lugar donde el `patron` coincide en la `cadena`.
        
    - Devuelve un objeto `Match` si encuentra una coincidencia, `None` si no la encuentra.
        
    - Métodos del objeto `Match`:
        
        - `match.group()`: Devuelve la parte de la cadena que coincidió con el patrón.
            
        - `match.start()`: Índice inicial de la coincidencia.
            
        - `match.end()`: Índice final (exclusivo) de la coincidencia.
            
- **`re.match(patron, cadena)`**:
    
    - Busca una coincidencia del `patron` solo al _principio_ de la `cadena`.
        
    - Devuelve un objeto `Match` o `None`.
        
- **`re.findall(patron, cadena)`**:
    
    - Encuentra _todas_ las coincidencias no superpuestas del `patron` en la `cadena`.
        
    - Devuelve una `lista` de cadenas con todas las coincidencias.
        
- **`re.sub(patron, reemplazo, cadena)`**:
    
    - Reemplaza _todas_ las ocurrencias del `patron` en la `cadena` con el `reemplazo`.
        
    - Devuelve la cadena modificada.
        

#### **3. Metacaracteres Comunes (Elementos del Patrón):**

- `.` (punto): Cualquier carácter (excepto salto de línea).
    
- `*`: Cero o más ocurrencias del carácter/grupo anterior.
    
- `+`: Una o más ocurrencias del carácter/grupo anterior.
    
- `?`: Cero o una ocurrencia del carácter/grupo anterior.
    
- `{n}`: Exactamente `n` ocurrencias.
    
- `{n,m}`: Entre `n` y `m` ocurrencias (inclusive).
    
- `[]`: Conjunto de caracteres. Coincide con _cualquier_ carácter dentro de los corchetes.
    
    - Ej: `[abc]` (a, b, o c), `[0-9]` (cualquier dígito), `[a-zA-Z]` (cualquier letra).
        
- `^`: Inicio de la cadena.
    
- `$`: Fin de la cadena.
    
- `|`: OR lógico (ej: `gato|perro` coincidirá con "gato" o "perro").
    
- `()`: Grupo de captura (para extraer partes del patrón) o para agrupar expresiones.
    
- `\` (barra invertida): Carácter de escape. Se usa para escapar metacaracteres (ej: `\.` para un punto literal) o para caracteres especiales.
    

#### **4. Secuencias Especiales (con `\`):**

- `\d`: Cualquier dígito (0-9). Equivalente a `[0-9]`.
    
- `\D`: Cualquier carácter que NO sea un dígito.
    
- `\w`: Cualquier carácter alfanumérico (letras, números y guion bajo). Equivalente a `[a-zA-Z0-9_]`.
    
- `\W`: Cualquier carácter que NO sea alfanumérico.
    
- `\s`: Cualquier carácter de espacio en blanco (espacio, tabulador, salto de línea).
    
- `\S`: Cualquier carácter que NO sea un espacio en blanco.
    
- `\b`: Límite de palabra (inicio o fin de una palabra).
    
- `\B`: No es un límite de palabra.
    

#### **5. Cadenas Crudas (Raw Strings `r''`):**

- Es **altamente recomendado** usar cadenas crudas (prefijo `r`) para patrones de Regex, como `r'\d+'`. Esto evita que Python interprete las barras invertidas (`\`) como secuencias de escape de cadena de texto (ej. `\n` es salto de línea), permitiendo que Regex las use para sus propios propósitos (ej. `\n` para un salto de línea literal en Regex).
    

### Explicación Teórica

Las expresiones regulares se basan en el concepto de lenguajes formales y autómatas finitos. Son una notación compacta para describir "lenguajes" o conjuntos de cadenas que siguen un patrón. Cuando usas Regex, compilas un patrón que el motor de expresiones regulares interpreta para buscar coincidencias. La sintaxis de Regex es un lenguaje en sí mismo, muy conciso, que permite definir patrones complejos con pocos caracteres, optimizado para operaciones de búsqueda y manipulación de texto a gran escala.

### Explicación Imaginativa

Imagina que tienes un "detector de patrones súper inteligente".

- Tú le das al detector un "plano" de lo que quieres encontrar (el **patrón Regex**).
    
- `.` (punto): Es como decir "encuentra cualquier cosa que se vea como un carácter aquí".
    
- `*` (asterisco): Es como decir "encuentra esto, no importa cuántas veces se repita, incluso si no aparece ninguna vez".
    
- `+` (más): Es como decir "encuentra esto, pero tiene que aparecer al menos una vez".
    
- `[]` (corchetes): Es como dar una lista de "ingredientes" y decir "encuentra cualquiera de estos".
    
- `\d` (barra d): Es un atajo para decir "encuentra cualquier número".
    
- `re.search()`: Es como decirle al detector: "Dame la primera cosa que coincida con este plano".
    
- `re.findall()`: Es como decirle: "Dame una lista de _todas_ las cosas que coincidan con este plano".
    
- `re.sub()`: Es como decirle: "Cada vez que encuentres algo que coincida con este plano, reemplázalo con esto otro".
    

### Relación

Las expresiones regulares son una herramienta indispensable para cualquier programador que trabaje con texto. Complementan y amplían las capacidades de las operaciones de cadenas básicas de Python. Son cruciales para:

- **Limpieza de datos:** Eliminar caracteres no deseados, normalizar formatos.
    
- **Extracción de datos:** Sacar información específica (ej., números, fechas, URLs) de texto no estructurado.
    
- **Validación de entrada:** Asegurar que los datos ingresados por el usuario cumplen con un formato específico antes de procesarlos.
    
- Parsing (análisis): Descomponer cadenas complejas en sus componentes significativos.
    
    Su dominio abre un abanico enorme de posibilidades para automatizar y optimizar tareas de manipulación de texto.
    

### Gráfico (Representación conceptual)

```
                       Entrada (Cadena de Texto)
                            "Esto es un email: usuario@dominio.com, y un número: 123-456-7890."
                                     |
                                     V
+---------------------------------------------------------------------------------+
|                         Motor de Expresiones Regulares                          |
|                               (Módulo 're' en Python)                           |
+---------------------------------------------------------------------------------+
          ^                                       ^                                    ^
          |                                       |                                    |
          |       Patrón Regex                  |         Patrón Regex               |        Patrón Regex
          |  (ej. r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')            |   (ej. r'\d{3}-\d{3}-\d{4}')        |  (ej. r'un')
          |                                       |                                    |
          |                                       |                                    |
          V                                       V                                    V
+-----------------------+   +-----------------------+   +-----------------------+
|  re.search()          |   |  re.findall()         |   |  re.sub()             |
|  (Primera Coincidencia)|   |  (Todas las Coincidencias)|   |  (Reemplazar)         |
+-----------------------+   +-----------------------+   +-----------------------+
          |                                       |                                    |
          V                                       V                                    V
    Objeto Match               Lista de Coincidencias          Cadena Modificada
    (ej. 'usuario@dominio.com') (ej. ['usuario@dominio.com', '123-456-7890']) (ej. "Esto es UN email...")
```

_(Este gráfico ilustra cómo el motor de expresiones regulares, usando diferentes funciones, procesa una cadena de entrada con un patrón Regex para encontrar, extraer o reemplazar texto.)_

### Ejemplo de Aplicación

Aquí tienes ejemplos de comandos y su uso con Expresiones Regulares en Python:

- **Validar un formato básico de correo electrónico:**
    
    ```python
    import re
    
    def validar_email(email):
        # Patrón simple para un email: texto@texto.texto
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(patron, email): # re.match busca al inicio de la cadena
            print(f"'{email}' es un correo electrónico válido.")
        else:
            print(f"'{email}' NO es un correo electrónico válido.")
    
    validar_email("test@example.com") # Válido
    validar_email("invalid-email")     # No válido
    validar_email("otro.test@sub.dominio.co") # Válido
    # Salida:
    # 'test@example.com' es un correo electrónico válido.
    # 'invalid-email' NO es un correo electrónico válido.
    # 'otro.test@sub.dominio.co' es un correo electrónico válido.
    ```
    
- **Extraer todos los números de teléfono de una cadena:**
    
    ```python
    import re
    
    texto = "Mi número es 123-456-7890. El de Juan es (555) 123-4567. Y este es 987.654.3210."
    # Patrón para números de teléfono (varios formatos)
    patron_telefono = r"\b(?:\d{3}[-.\s]?\d{3}[-.\s]?\d{4}|\(\d{3}\)\s?\d{3}-\d{4})\b"
    telefonos_encontrados = re.findall(patron_telefono, texto)
    print("Teléfonos encontrados:", telefonos_encontrados)
    # Salida: Teléfonos encontrados: ['123-456-7890', '(555) 123-4567', '987.654.3210']
    ```
    
- **Reemplazar espacios múltiples por uno solo:**
    
    ```python
    import re
    
    frase = "Este    es   un  ejemplo   con     muchos  espacios."
    frase_limpia = re.sub(r"\s+", " ", frase) # '\s+' coincide con uno o más espacios en blanco
    print("Frase original:", frase)
    print("Frase limpia:", frase_limpia)
    # Salida:
    # Frase original: Este    es   un  ejemplo   con     muchos  espacios.
    # Frase limpia: Este es un ejemplo con muchos espacios.
    ```
    
- **Buscar la primera ocurrencia y extraer un grupo (año):**
    
    ```python
    import re
    
    linea_log = "INFO: Proceso iniciado en 2023-07-14. Error en 2024-01-20."
    # Patrón para encontrar una fecha YYYY-MM-DD y capturar el año
    patron_fecha_año = r".*?(\d{4})-\d{2}-\d{2}" # Captura el primer grupo de 4 dígitos (año)
    
    coincidencia = re.search(patron_fecha_año, linea_log)
    if coincidencia:
        año_encontrado = coincidencia.group(1) # group(1) accede al primer grupo de captura
        print(f"Primer año encontrado en el log: {año_encontrado}")
    else:
        print("No se encontraron años en el formato YYYY-MM-DD.")
    # Salida: Primer año encontrado en el log: 2023
    ```
