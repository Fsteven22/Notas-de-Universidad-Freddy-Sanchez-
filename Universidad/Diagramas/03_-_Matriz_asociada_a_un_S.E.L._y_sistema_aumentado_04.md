graph TB
    A[Sistema 3×3] --> B{¿Los planos<br/>se intersectan?}
    B -->|Sí| C{¿En cuántos puntos?}
    B -->|No| D[Sin solución<br/>planos paralelos]
    C -->|Uno| E[Solución única<br/>punto]
    C -->|Infinitos| F{¿Forma?}
    F -->|Recta| G[Infinitas en recta]
    F -->|Plano| H[Infinitas en plano]
    style E fill:#e1ffe1
    style D fill:#ffe1e1
    style G fill:#fff4e1
    style H fill:#fff4e1
