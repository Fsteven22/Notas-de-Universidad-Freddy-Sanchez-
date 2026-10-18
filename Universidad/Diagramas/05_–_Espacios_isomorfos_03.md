flowchart TD
    A[¿V ≅ W?] --> B{¿dim V = dim W?}
    B -->|No| C[❌ NO son isomorfos<br/>GARANTIZADO]
    B -->|Sí| D{¿Mismo campo?}
    D -->|No| C
    D -->|Sí| E[✅ SÍ son isomorfos<br/>existe isomorfismo]
    E --> F[Construir T explícitamente]
    F --> G[Elegir bases]
    G --> H[Definir T en base]
    H --> I[Extender linealmente]
    style C fill:#ffe1e1
    style E fill:#e1ffe1
    style B fill:#fff4e1
