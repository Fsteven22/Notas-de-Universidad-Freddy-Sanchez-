graph LR
    A[Emisor] --> B[Mensaje]
    B --> C[Canal]
    C --> D[Receptor]
    D --> E[Retroalimentacion]
    E --> A
    F[Codigo] --> B
    G[Contexto] --> D
    H[Ruido] --> C
