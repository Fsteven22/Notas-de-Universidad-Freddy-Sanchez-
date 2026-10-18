flowchart TD
    A[Matriz A] --> B[Calcular valores propios]
    B --> C[Calcular espacios propios]
    C --> D{Σ dim(E_λᵢ) = n?}
    D -->|Sí| E[A es diagonalizable]
    D -->|No| F[A NO es diagonalizable]
    E --> G[Formar P con vectores propios]
    E --> H[Formar D con valores propios]
    G --> I[A = PDP⁻¹]
    H --> I
    style A fill:#e1f5ff
    style E fill:#e1ffe1
    style F fill:#ffe1e1
    style I fill:#fff4e1
