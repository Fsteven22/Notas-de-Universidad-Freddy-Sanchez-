graph LR
    A[Señal original] --> B[Muestrear]
    B --> C[Vectores de datos]
    C --> D[Gram-Schmidt]
    D --> E[Base ortogonal]
    E --> F[Coeficientes]
    F --> G[Comprimir/<br/>Filtrar]
    G --> H[Reconstruir]
    style D fill:#fff4e1
    style E fill:#e1ffe1
