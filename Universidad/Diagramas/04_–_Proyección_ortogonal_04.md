flowchart TD
    A[Vector v a proyectar] --> B{¿Base de W es ortogonal?}
    B -->|Sí| C[Usar fórmula directa]
    B -->|No| D[Ortonormalizar base<br/>Gram-Schmidt]
    D --> C
    C --> E[Para cada uᵢ en base:]
    E --> F[Calcular cᵢ = ⟨v,uᵢ⟩/||uᵢ||²]
    F --> G[Sumar: proj_W v = Σ cᵢuᵢ]
    G --> H[Resultado en W]
    style C fill:#e1ffe1
    style G fill:#e1f5ff
    style H fill:#fff4e1
