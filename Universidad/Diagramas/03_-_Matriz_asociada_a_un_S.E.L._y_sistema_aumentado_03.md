graph TD
    A[Sistema Ax = b] --> B{Comparar m y n}
    B -->|m = n| C[Sistema Cuadrado]
    B -->|m < n| D[Subdeterminado]
    B -->|m > n| E[Sobredeterminado]
    C --> F{det A ≠ 0?}
    F -->|Sí| G[Solución única<br/>x = A⁻¹b]
    F -->|No| H[Infinitas o ninguna]
    D --> I[Infinitas soluciones<br/>o ninguna]
    E --> J[Generalmente<br/>sin solución exacta]
    style C fill:#e1ffe1
    style D fill:#fff4e1
    style E fill:#ffe1e1
