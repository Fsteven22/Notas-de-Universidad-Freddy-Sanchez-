graph TB
    A[ℝⁿ] --> B[Fila A<br/>dim = r]
    A --> C[Nul A<br/>dim = n-r]
    D[ℝᵐ] --> E[Col A<br/>dim = r]
    D --> F[Nul A^T<br/>dim = m-r]
    B -.->|A| E
    C -.->|A| F
    B ---|⊥| C
    E ---|⊥| F
    style B fill:#e1ffe1
    style C fill:#ffe1e1
    style E fill:#e1f5ff
    style F fill:#fff4e1
