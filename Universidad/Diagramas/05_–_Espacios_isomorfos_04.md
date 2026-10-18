graph LR
    A[V] -->|T| B[W]
    B -->|T⁻¹| A
    A -.->|T⁻¹ ∘ T = I_V| A
    B -.->|T ∘ T⁻¹ = I_W| B
    style A fill:#e1f5ff
    style B fill:#ffe1f5
