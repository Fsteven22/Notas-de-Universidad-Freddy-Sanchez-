graph LR
    A[Espacio<br/>Original] -->|P⁻¹¹| B[Espacio de<br/>Vectores Propios]
    B -->|D escala| C[Transformación<br/>Simple]
    C -->|P| D[Vuelta al<br/>Espacio Original]
    A -.->|A transforma<br/>complicado| D
    style B fill:#e1ffe1
    style C fill:#fff4e1
