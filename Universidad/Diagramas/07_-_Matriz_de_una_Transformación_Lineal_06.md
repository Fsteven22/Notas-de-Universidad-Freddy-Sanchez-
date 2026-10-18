flowchart TD
    A[Vector v] --> B[Multiplicar fila 1 por v]
    B --> C[Resultado = componente 1]
    A --> D[Multiplicar fila 2 por v]
    D --> E[Resultado = componente 2]
    C --> F[Vector transformado]
    E --> F
    style A fill:#e1ffe1
    style F fill:#ffe1f5
