graph TD
    A[Punto A] -->|"Distancia directa d(A,C)"| C[Punto C]
    A -->|"d(A,B)"| B[Punto B]
    B -->|"d(B,C)"| C
    
    Note1["d(A,C) ≤ d(A,B) + d(B,C)"]
    
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#e1ffe1
    style Note1 fill:#ffe1e1
