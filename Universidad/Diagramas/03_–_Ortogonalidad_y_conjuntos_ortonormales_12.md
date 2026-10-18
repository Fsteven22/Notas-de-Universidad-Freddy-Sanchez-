flowchart LR
    A[Imagen Original<br/>n × n píxeles] --> B[Transformar a<br/>base ortonormal]
    B --> C[Obtener<br/>coeficientes]
    C --> D[Descartar<br/>coeficientes pequeños]
    D --> E[Reconstruir<br/>imagen comprimida]
    style A fill:#e1f5ff
    style C fill:#e1ffe1
    style E fill:#fff4e1
