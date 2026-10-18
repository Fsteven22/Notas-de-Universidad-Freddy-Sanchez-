flowchart LR
    A[Vector en base B] -->|P| B[Vector en base E]
    B -->|"[T]_E"| C[Transformado en E]
    C -->|P⁻¹| D[Resultado en base B]
    A -.->|"[T]_B"| D
    style A fill:#e1ffe1
    style B fill:#fff4e1
    style C fill:#fff4e1
    style D fill:#e1ffe1
