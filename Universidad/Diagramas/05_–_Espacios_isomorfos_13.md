flowchart TD
    A[¿V ≅ W?] --> B{¿Mismo campo?}
    B -->|No| C[❌ NO son isomorfos]
    B -->|Sí| D{¿dim V = dim W?}
    
    D -->|No| C
    D -->|Sí| E[✅ SÍ son isomorfos]
    
    E --> F[Construir isomorfismo explícito]
    F --> G[1. Elegir base de V: ℬ_V]
    G --> H[2. Elegir base de W: ℬ_W]
    H --> I[3. Definir T: v_i ↦ w_i]
    I --> J[4. Extender linealmente]
    J --> K[5. Verificar biyectividad]
    
    style C fill:#ffe1e1
    style E fill:#e1ffe1
    style K fill:#ccffcc
