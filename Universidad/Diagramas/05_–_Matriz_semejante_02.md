flowchart LR
    A[Vector v<br/>en base estándar] -->|A| B[Av<br/>transformado<br/>base estándar]
    C[Vector v'<br/>en nueva base] -->|B| D[Bv'<br/>transformado<br/>nueva base]
    A -->|P⁻¹| C
    B -->|P⁻¹| D
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#e1ffe1
    style D fill:#ffe1f5
