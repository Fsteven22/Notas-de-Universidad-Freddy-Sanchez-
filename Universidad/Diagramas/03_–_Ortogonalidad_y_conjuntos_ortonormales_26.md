graph TD
    A[Vector y] --> B[Proyección \hat{y} ∈ W]
    A --> C[Componente z ∈ W^⊥]
    B --> D["\hat{y} = Σ⟨y,uᵢ⟩uᵢ"]
    C --> E["z = y - \hat{y}"]
    D -.->|⊥| E
    style A fill:#e1f5ff
    style B fill:#e1ffe1
    style C fill:#fff4e1
