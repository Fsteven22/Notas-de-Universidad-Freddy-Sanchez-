flowchart TD
    A[🎯 Entrada del Usuario] --> B{📝 ¿Entrada vacía?}
    B -->|Sí| C[❌ Error: Campo requerido]
    B -->|No| D{🔍 ¿Formato correcto?}
    
    D -->|No| E[❌ Error: Formato inválido]
    D -->|Sí| F{📏 ¿Longitud válida?}
    
    F -->|No| G[❌ Error: Longitud incorrecta]
    F -->|Sí| H{🎯 ¿Rango válido?}
    
    H -->|No| I[❌ Error: Fuera de rango]
    H -->|Sí| J{🔒 ¿Reglas de negocio?}
    
    J -->|No| K[❌ Error: Regla violada]
    J -->|Sí| L[✅ Entrada válida]
    
    C --> M{🔄 ¿Reintentar?}
    E --> M
    G --> M
    I --> M
    K --> M
    
    M -->|Sí| A
    M -->|No| N[🛑 Finalizar]
    
    L --> O[📦 Procesar datos]
    
    style L fill:#e8f5e8
    style O fill:#e8f5e8
    style C fill:#ffebee
    style E fill:#ffebee
    style G fill:#ffebee
    style I fill:#ffebee
    style K fill:#ffebee
