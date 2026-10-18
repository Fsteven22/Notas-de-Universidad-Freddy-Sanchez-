graph TB
    A[Vector y en ℝⁿ] --> B[Matriz de Proyección P]
    B --> C[\hat{y} = Py]
    
    D[Subespacio W] --> E[Base: columnas de A]
    E --> F[Calcular P = A A^T A ^-1 A^T]
    F --> B
    
    C --> G[Proyección sobre W]
    
    style A fill:#e1f5ff
    style B fill:#e1ffe1
    style C fill:#fff4e1
    style F fill:#ffe1e1
