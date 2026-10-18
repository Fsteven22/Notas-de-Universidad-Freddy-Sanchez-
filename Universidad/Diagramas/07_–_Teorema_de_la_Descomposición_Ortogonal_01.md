graph TB
    A[Vector y en ℝⁿ] --> B[Descomposición Ortogonal]
    B --> C[\hat{y} componente en W]
    B --> D[z componente en W⊥]
    
    C --> E[\hat{y} ∈ W]
    D --> F[z ⊥ W]
    
    E --> G[y = \hat{y} + z]
    F --> G
    
    G --> H[Única descomposición]
    
    style A fill:#e1f5ff
    style C fill:#e1ffe1
    style D fill:#fff4e1
    style H fill:#ffe1e1
