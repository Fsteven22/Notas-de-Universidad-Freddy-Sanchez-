graph TB
    A[Espacio Abstracto V<br/>dim V = n] -->|isomorfismo de coordenadas| B[ℝⁿ<br/>espacio concreto]
    C[Vector v ∈ V] -->|v _ℬ| D[Vector de coordenadas<br/> c₁, c₂, ..., cₙ ]
    E[Operaciones en V<br/>abstractas] -.->|se traducen a| F[Operaciones en ℝⁿ<br/>concretas]
    A --> C
    B --> D
    A --> E
    B --> F
    style A fill:#ffe1f5
    style B fill:#e1f5ff
    style E fill:#fff4e1
    style F fill:#e1ffe1
