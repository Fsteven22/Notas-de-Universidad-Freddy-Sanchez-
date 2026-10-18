flowchart TD
    A[Problema: min ||Ax - b||] --> B[Factorizar A = QR]
    B --> C[Sustituir: min ||QRx - b||]
    C --> D[Multiplicar por Qᵀ]
    D --> E[min ||Rx - Qᵀb||]
    E --> F[Resolver Rx = Qᵀb<br/>sistema triangular]
    F --> G[Solución x*]
    style F fill:#fff4e1
    style G fill:#e1ffe1
