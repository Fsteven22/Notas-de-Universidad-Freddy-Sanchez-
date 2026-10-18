flowchart TD
    A[Transformación T] --> B{"det[T] ≠ 0?"}
    B -->|Sí| C[✅ Invertible]
    B -->|No| D[❌ No invertible]
    C --> E["Existe [T]⁻¹"]
    D --> F[Información perdida]
    style C fill:#e1ffe1
    style D fill:#ffe1e1
