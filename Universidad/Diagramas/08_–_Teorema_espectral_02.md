graph LR
    A[Espacio Original] -->|Q^T| B[Sistema de<br/>Ejes Principales]
    B -->|Λ escalar| C[Escalado en<br/>Ejes Principales]
    C -->|Q| D[Regreso al<br/>Espacio Original]
    E[Transformación A] -.equivale a.-> F[Rotar + Escalar + Rotar]
    style B fill:#e1ffe1
    style C fill:#fff4e1
    style E fill:#e1f5ff
