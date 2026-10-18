flowchart LR
    A[Subespacio W] --> B[Elegir base]
    B --> C[Formar matriz A<br/>columnas = base]
    C --> D[Calcular A^T A]
    D --> E[Invertir: A^T A ^-1]
    E --> F[P = A A^T A ^-1 A^T]
    G[Vector y] --> H[Multiplicar: \hat{y} = Py]
    F --> H
    H --> I[Proyección \hat{y} ∈ W]
    style C fill:#e1ffe1
    style F fill:#fff4e1
    style I fill:#e1f5ff
