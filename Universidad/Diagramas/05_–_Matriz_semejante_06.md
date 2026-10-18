flowchart TD
    A[Matriz A] --> B[Calcular valores propios]
    B --> C[Encontrar vectores propios]
    C --> D{¿n vectores<br/>independientes?}
    D -->|Sí| E[Formar P con vectores propios]
    D -->|No| F[NO diagonalizable]
    E --> G[D = P⁻¹AP<br/>diagonal]
    style A fill:#e1f5ff
    style G fill:#e1ffe1
    style F fill:#ffe1e1
