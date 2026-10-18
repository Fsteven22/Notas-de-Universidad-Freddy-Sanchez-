flowchart LR
    A[Modelo 3D<br/>Vértices] --> B[Rotación Q₁<br/>Matriz ortogonal]
    B --> C[Escalado S]
    C --> D[Traslación T]
    D --> E[Proyección<br/>Pantalla 2D]
    F[Ortogonalidad] -.-> B
    F -.-> G[✅ Sin deformación<br/>✅ Inversión rápida]
    style B fill:#e1ffe1
    style F fill:#e1f5ff
