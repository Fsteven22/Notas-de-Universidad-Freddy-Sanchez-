flowchart TD
    A[Matriz A n×n] --> B{¿Diagonalizable?}
    
    B -->|Sí| C[Tiene n vectores propios<br/>linealmente independientes]
    B -->|No| D[No tiene suficientes<br/>vectores propios]
    
    C --> E[Formar P con vectores propios]
    E --> F[D = P⁻¹AP diagonal]
    
    D --> G[No existe descomposición<br/>A = PDP⁻¹]
    
    style A fill:#e1f5ff
    style C fill:#e1ffe1
    style F fill:#e1ffe1
    style D fill:#ffe1e1
    style G fill:#ffe1e1
