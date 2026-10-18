graph TD
    A[Vector v] --> B[Descomponer respecto a u]
    B --> C[Componente paralela<br/>proj_u v]
    B --> D[Componente perpendicular<br/>perp_u v]
    C --> E["Fórmula: (⟨v,u⟩/||u||²)u"]
    D --> F["Fórmula: v - proj_u v"]
    E --> G[En la dirección de u]
    F --> H[Ortogonal a u]
    G --> I["||proj_u v|| = |⟨v,u⟩|/||u||"]
    H --> J["⟨perp_u v, u⟩ = 0"]
    style C fill:#e1ffe1
    style D fill:#fff4e1
    style I fill:#e1f5ff
    style J fill:#f0e1ff
