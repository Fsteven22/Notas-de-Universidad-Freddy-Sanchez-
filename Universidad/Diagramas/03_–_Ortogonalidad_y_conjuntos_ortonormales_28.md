graph TD
    A[ℝⁿ] --> B[Subespacio W]
    A --> C[Complemento W^⊥]
    B -.->|⊥| C
    B -.->|dim = k| D[Dimensión]
    C -.->|dim = n-k| D
    B --> E[Base: v₁, ..., vₖ]
    C --> F[Base: u₁, ..., uₙ₋ₖ]
    style A fill:#e1f5ff
    style B fill:#e1ffe1
    style C fill:#fff4e1
