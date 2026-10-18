graph TD
    A[Candidato a<br/>producto interno] --> B{PI1: Linealidad?}
    B -->|No| Z1[❌ NO es producto interno]
    B -->|Sí| C{PI2: Simetría?}
    C -->|No| Z2[❌ NO es producto interno]
    C -->|Sí| D{PI3: Positividad?}
    D -->|No| Z3[❌ NO es producto interno]
    D -->|Sí| E{PI4: Definición positiva?}
    E -->|No| Z4[❌ NO es producto interno]
    E -->|Sí| F[✅ SÍ es producto interno]
    style F fill:#e1ffe1
    style Z1 fill:#ffe1e1
    style Z2 fill:#ffe1e1
    style Z3 fill:#ffe1e1
    style Z4 fill:#ffe1e1
