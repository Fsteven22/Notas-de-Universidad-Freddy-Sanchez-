flowchart TD
    A[Vector y] --> B{¿Base de W?}
    B -->|Ortogonal| C[Usar fórmula directa]
    B -->|No ortogonal| D[Ortonormalizar<br/>Gram-Schmidt]
    C --> E[\hat{y} = Σ y·uᵢ/uᵢ·uᵢ uᵢ]
    D --> F[Obtener base ortonormal]
    F --> E
    E --> G[Calcular z = y - \hat{y}]
    G --> H[Verificar: \hat{y} · z = 0]
    style A fill:#e1f5ff
    style E fill:#e1ffe1
    style H fill:#fff4e1
