flowchart TD
    A[🚀 Inicio del Programa] --> B{🔍 Condición IF}
    
    B -->|✅ True| C[📋 Ejecutar Bloque IF]
    B -->|❌ False| D{🔍 ¿Hay ELIF?}
    
    D -->|✅ Sí| E{🔍 Condición ELIF}
    D -->|❌ No| F{🔍 ¿Hay ELSE?}
    
    E -->|✅ True| G[📋 Ejecutar Bloque ELIF]
    E -->|❌ False| H{🔍 ¿Más ELIF?}
    
    H -->|✅ Sí| E
    H -->|❌ No| F
    
    F -->|✅ Sí| I[📋 Ejecutar Bloque ELSE]
    F -->|❌ No| J[⏭️ Continuar Programa]
    
    C --> J
    G --> J  
    I --> J
    
    J --> K[🏁 Fin]
    
    style A fill:#e3f2fd
    style B fill:#fff3e0
    style D fill:#fff3e0
    style E fill:#fff3e0
    style F fill:#fff3e0
    style H fill:#fff3e0
    style C fill:#e8f5e8
    style G fill:#e8f5e8
    style I fill:#ffebee
    style J fill:#f3e5f5
    style K fill:#e1f5fe
