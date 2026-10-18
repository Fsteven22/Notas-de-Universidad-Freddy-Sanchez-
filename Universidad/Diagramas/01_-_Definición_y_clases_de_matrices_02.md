graph TD
    A["Matriz A de orden m x n"] --> B{"¿m = n?"}
    B -->|No| C["Rectangular:<br/>fila, columna o general"]
    B -->|Sí| D{"¿Ceros fuera<br/>de la diagonal?"}
    D -->|Sí| E["Diagonal<br/>¿unos? → Identidad"]
    D -->|No| F{"¿A^T = A?"}
    F -->|Sí| G["Simétrica"]
    F -->|No| H{"¿A^T = -A?"}
    H -->|Sí| I["Antisimétrica"]
    H -->|No| J{"¿Ceros arriba<br/>o abajo?"}
    J -->|Sí| K["Triangular"]
    J -->|No| L["Cuadrada general"]
