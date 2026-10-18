flowchart TD
    A[Matriz A] --> B[Calcular valores<br/>propios λ]
    B --> C[Calcular vectores<br/>propios v]
    C --> D{¿n vectores LI?}
    D -->|Sí| E[Formar matriz P<br/>columnas = vectores propios]
    D -->|No| F[❌ No diagonalizable]
    E --> G[Formar matriz D<br/>diagonal = λ]
    G --> H[✓ A = PDP⁻¹¹]
    style D fill:#fff4e1
    style F fill:#ffe1e1
    style H fill:#e1ffe1
