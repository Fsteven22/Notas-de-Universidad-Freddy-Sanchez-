graph TD
    A[Necesito calcular Q^-1] --> B{¿Q es ortogonal?}
    B -->|No| C[Algoritmo general<br/>Eliminación gaussiana<br/>O n³ operaciones]
    B -->|Sí| D[Simplemente transponer<br/>O n² operaciones]
    C --> E[Lento y costoso]
    D --> F[✅ Rápido y eficiente]
    style C fill:#ffe1e1
    style D fill:#e1ffe1
    style E fill:#ffe1e1
    style F fill:#e1ffe1
