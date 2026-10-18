graph TD
    A[Posición cámara] --> B[Vector hacia<br/>objetivo: forward]
    B --> C[Vector up<br/>aproximado]
    C --> D[Gram-Schmidt:<br/>ortogonalizar]
    D --> E[forward, right, up<br/>base ortonormal]
    E --> F[Matriz de vista]
    style D fill:#fff4e1
    style E fill:#e1ffe1
