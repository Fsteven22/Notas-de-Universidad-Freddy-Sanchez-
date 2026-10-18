graph LR
    A[Emisor] --> B[Codifica mensaje]
    B --> C[Canal]
    C --> D[Receptor]
    D --> E[Decodifica y responde]
    E --> A
    F[Codigo compartido] --> B
    G[Contexto] --> C
    H[Ruido] --> D
