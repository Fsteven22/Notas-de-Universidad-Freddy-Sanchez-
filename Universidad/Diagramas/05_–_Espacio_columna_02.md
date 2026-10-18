graph TB
    subgraph "ℝⁿ (dominio)"
        A[Row A<br/>dim = r]
        B[Nul A<br/>dim = n-r]
    end
    subgraph "ℝᵐ (codominio)"
        C[Col A<br/>dim = r]
        D[Nul Aᵀ<br/>dim = m-r]
    end
    A -.ortogonal.- B
    C -.ortogonal.- D
    A -->|A mapea| C
    B -->|A aniquila| E[0⃗]
    style A fill:#c8e6c9
    style B fill:#ffccbc
    style C fill:#c8e6c9
    style D fill:#ffccbc
