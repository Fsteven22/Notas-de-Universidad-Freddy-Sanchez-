flowchart TD
    A[Matriz A n×n] --> B[Calcular todos los valores propios]
    B --> C[Para cada λᵢ]
    C --> D[Calcular MA λᵢ]
    C --> E[Calcular MG λᵢ]
    D --> F{¿MG = MA?}
    E --> F
    F -->|Para todos λᵢ| G[A es DIAGONALIZABLE]
    F -->|Existe λᵢ con MG < MA| H[A NO es diagonalizable]
    G --> I[Existe base de vectores propios]
    H --> J[Insuficientes vectores propios]
    style A fill:#e1f5ff
    style G fill:#e1ffe1
    style H fill:#ffe1e1
