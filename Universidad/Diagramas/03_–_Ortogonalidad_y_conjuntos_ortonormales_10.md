flowchart TD
    A[¿Necesitas base ortonormal?] --> B{Tamaño del problema}
    B -->|Pequeño n<20| C[Gram-Schmidt clásico<br/>Simple y suficiente]
    B -->|Mediano 20-100| D[Gram-Schmidt modificado<br/>Más estable]
    B -->|Grande n>100| E[Factorización QR<br/>Householder/Givens]
    C --> F{¿Precisión crítica?}
    F -->|Sí| G[Usar MGS o QR]
    F -->|No| H[CGS es OK]
    style C fill:#e1ffe1
    style D fill:#fff4e1
    style E fill:#e1f5ff
