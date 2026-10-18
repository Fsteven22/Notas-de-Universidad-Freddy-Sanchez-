graph TD
    A[Sistema Ax = b] --> B{¿Tiene solución exacta?}
    B -->|Sí| C[Resolver normalmente]
    B -->|No| D[b no está en ColA]
    D --> E[Buscar \hat{x} que minimize<br/>||b - Ax||]
    E --> F[Proyectar b sobre ColA]
    F --> G[A\hat{x} = proj_ColA b]
    G --> H[Solución de<br/>mínimos cuadrados]
    style D fill:#ffe1e1
    style G fill:#e1ffe1
    style H fill:#fff4e1
