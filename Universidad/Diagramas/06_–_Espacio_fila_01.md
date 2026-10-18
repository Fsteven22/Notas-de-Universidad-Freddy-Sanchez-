graph TB
    A[Matriz A: m×n]
    B[Row A ⊆ ℝⁿ]
    C[Col A ⊆ ℝᵐ]
    A --> B
    A --> C
    B --> D[dim = r]
    C --> E[dim = r]
    D -.mismo rango.- E
    style B fill:#c8e6c9
    style C fill:#bbdefb
    style D fill:#fff9c4
    style E fill:#fff9c4
