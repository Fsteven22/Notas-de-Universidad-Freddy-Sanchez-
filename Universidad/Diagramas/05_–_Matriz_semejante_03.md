flowchart LR
    A[Base original] -->|P⁻¹| B[Nueva base]
    B -->|Aplicar A<br/>como B| C[Transformación]
    C -->|P| D[Regresar a<br/>base original]
    A -.->|Directamente<br/>aplicar A| D
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#e1ffe1
    style D fill:#ffe1f5
