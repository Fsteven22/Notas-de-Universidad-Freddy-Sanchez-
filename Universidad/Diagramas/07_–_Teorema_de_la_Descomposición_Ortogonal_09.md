graph TB
    A[Vector b<br/>fuera de Col A ] --> B[Proyectar sobre Col A ]
    B --> C[b̂ = proj_Col A  b]
    C --> D[Resolver A\hat{x} = b̂]
    D --> E[\hat{x} solución de<br/>mínimos cuadrados]
    F[‖Ax - b‖] --> G[Minimizado cuando<br/>Ax = b̂]
    style C fill:#e1ffe1
    style E fill:#fff4e1
