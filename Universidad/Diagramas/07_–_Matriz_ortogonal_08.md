graph TB
    A[Matriz Ortogonal Q] --> B[Preserva normas<br/>Qv = v]
    A --> C[Preserva productos<br/>Qu · Qv = u · v]
    B --> D[Preserva distancias<br/>d Qu,Qv = d u,v]
    C --> E[Preserva ángulos<br/>∠ Qu,Qv = ∠ u,v]
    D --> F[🎯 Isometría]
    E --> F
    style A fill:#e1f5ff
    style F fill:#e1ffe1
