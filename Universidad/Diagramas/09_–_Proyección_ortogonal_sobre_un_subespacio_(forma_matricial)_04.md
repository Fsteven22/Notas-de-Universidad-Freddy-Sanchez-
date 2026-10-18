graph LR
    A[Vector a<br/>n×1] --> B[a^T<br/>1×n]
    A --> C[aa^T<br/>n×n]
    B --> C
    C --> D[Matriz de rango 1]
    D --> E[Todas las filas<br/>son múltiplos]
    style C fill:#e1ffe1
    style D fill:#fff4e1
