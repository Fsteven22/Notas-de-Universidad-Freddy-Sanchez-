graph TD
    A[💻 Programa Python] --> B{Crear Variable}
    B --> C[📦 Asignar Valor]
    C --> D[🏷️ Python Infiere Tipo]
    D --> E{Tipo de Dato}
    
    E --> F[🔢 int<br/>Enteros]
    E --> G[📊 float<br/>Decimales]
    E --> H[📝 str<br/>Texto]
    E --> I[✅ bool<br/>Verdadero/Falso]
    
    F --> J[🧮 Operaciones Matemáticas]
    G --> J
    H --> K[📜 Manipulación de Texto]
    I --> L[⚖️ Lógica y Decisiones]
    
    J --> M[💾 Almacenar en Memoria]
    K --> M
    L --> M
    
    style A fill:#e1f5fe
    style E fill:#fff3e0
    style M fill:#e8f5e8
