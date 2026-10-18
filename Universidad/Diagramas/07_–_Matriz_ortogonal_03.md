graph TD
    A[Matriz Ortogonal Q] --> B[Q^T Q = I]
    A --> C[Q Q^T = I]
    A --> D[Q^-1 = Q^T]
    A --> E[Columnas ortonormales]
    A --> F[Filas ortonormales]
    A --> G[det Q = ±1]
    B -.-> H[Todas son<br/>equivalentes]
    C -.-> H
    D -.-> H
    E -.-> H
    F -.-> H
    G -.-> H
    style A fill:#e1f5ff
    style H fill:#e1ffe1
