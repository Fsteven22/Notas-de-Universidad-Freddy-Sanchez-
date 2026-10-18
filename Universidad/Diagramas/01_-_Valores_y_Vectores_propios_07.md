graph LR
    A[Matriz A<br/>n×n] --> B{¿n vectores propios<br/>linealmente independientes?}
    B -->|Sí| C[A es diagonalizable]
    B -->|No| D[A no es diagonalizable]
    C --> E[Base de vectores<br/>propios]
    E --> F[Representación<br/>simplificada]
    style C fill:#e1ffe1
    style D fill:#ffe1e1
    style F fill:#e1f5ff
