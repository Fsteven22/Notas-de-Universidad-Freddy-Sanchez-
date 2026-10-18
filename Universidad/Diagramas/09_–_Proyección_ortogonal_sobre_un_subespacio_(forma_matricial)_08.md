graph TB
    A[Vector b] --> B[Proyectar sobre Col A ]
    B --> C[b̂ = Pb]
    C --> D[Resolver A\hat{x} = b̂]
    D --> E[\hat{x} = A^T A ^-1 A^T b]
    F[Error: z = b - b̂] -.-> G[z ⊥ Col A ]
    G -.-> H[A^T z = 0]
    H -.-> E
    style C fill:#e1ffe1
    style E fill:#fff4e1
