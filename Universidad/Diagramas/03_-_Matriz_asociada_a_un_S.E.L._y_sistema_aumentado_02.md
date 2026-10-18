graph LR
    A[Matriz Aumentada<br/>A|b] --> B[Operaciones elementales]
    B --> C[Eliminación Gaussiana]
    B --> D[Gauss-Jordan]
    C --> E[Forma escalonada]
    D --> F[Forma escalonada reducida]
    E --> G[Resolver sistema]
    F --> G
    style A fill:#e1f5ff
    style G fill:#e1ffe1
