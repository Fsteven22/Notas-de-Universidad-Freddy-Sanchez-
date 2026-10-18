graph TB
    A[ℝⁿ] --> B[Aplicar P]
    B --> C{Resultado}
    C --> D[Im P = W<br/>rango = dim W ]
    C --> E[Nul P = W⊥<br/>nulidad = n - dim W ]
    F[Teorema del rango:<br/>rango + nulidad = n] -.-> C
    style D fill:#e1ffe1
    style E fill:#fff4e1
    style F fill:#e1f5ff
