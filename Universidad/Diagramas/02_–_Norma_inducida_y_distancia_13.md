flowchart TD
    A["Objetivo: ||u + v|| ≤ ||u|| + ||v||"] --> B[Elevar al cuadrado]
    B --> C["||u + v||² ≤ ||u|| + ||v||²"]
    C --> D[Expandir usando<br/>producto interno]
    D --> E["||u||² + 2⟨u,v⟩ + ||v||²"]
    D --> F["||u||² + 2||u||||v|| + ||v||²"]
    E --> G[Simplificar]
    F --> G
    G --> H["⟨u,v⟩ ≤ ||u||||v||"]
    H --> I[Aplicar<br/>Cauchy-Schwarz]
    I --> J[Demostración<br/>completa ✓]
    style A fill:#e1f5ff
    style I fill:#fff4e1
    style J fill:#e1ffe1
