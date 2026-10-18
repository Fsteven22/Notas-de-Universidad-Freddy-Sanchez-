graph TB
    A[Valor propio λ] --> B[Multiplicidad Algebraica MA]
    A --> C[Multiplicidad Geométrica MG]
    
    B --> D[Del polinomio característico]
    C --> E[Del espacio propio E_λ]
    
    D --> F[Raíces repetidas]
    E --> G[Vectores LI]
    
    H[Relación] --> I[1 ≤ MG ≤ MA]
    I --> J{MG = MA?}
    J -->|Para todos λ| K[Diagonalizable]
    J -->|Existe λ con MG < MA| L[NO diagonalizable]
    
    style A fill:#e1f5ff
    style K fill:#e1ffe1
    style L fill:#ffe1e1
