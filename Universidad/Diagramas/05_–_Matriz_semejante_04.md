graph TB
    A[Relación de Equivalencia]
    A --> B[Reflexiva<br/>A ~ A]
    A --> C[Simétrica<br/>A ~ B ⟹ B ~ A]
    A --> D[Transitiva<br/>A ~ B, B ~ C ⟹ A ~ C]
    B --> E[Particiona matrices<br/>en clases de equivalencia]
    C --> E
    D --> E
    style A fill:#e1f5ff
    style E fill:#e1ffe1
