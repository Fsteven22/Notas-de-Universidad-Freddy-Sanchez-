flowchart LR
    A[Imagen original<br/>8×8 píxeles] --> B[Aplicar DCT<br/>64 coeficientes]
    B --> C[Cuantizar<br/>reducir precisión]
    C --> D[Codificar<br/>Huffman]
    D --> E[Imagen comprimida]
    F[Descomposición<br/>ortogonal] -.-> B
    G[Retener solo<br/>componentes grandes] -.-> C
    style B fill:#e1ffe1
    style C fill:#fff4e1
