flowchart TD
    A[🚀 Inicio] --> B[📝 Inicialización de Variables]
    B --> C{🔍 ¿Condición es True?}
    
    C -->|❌ False| D[🏁 Fin del Bucle]
    C -->|✅ True| E[📋 Ejecutar Bloque de Código]
    
    E --> F{❓ ¿Hay Break?}
    F -->|✅ Sí| D
    F -->|❌ No| G{❓ ¿Hay Continue?}
    
    G -->|✅ Sí| H[⏭️ Saltar al Final del Bloque]
    G -->|❌ No| I[🔄 Continuar Ejecución]
    
    H --> J[🔧 Actualización de Variables]
    I --> J
    J --> C
    
    D --> K[⏭️ Continuar Programa]
    
    style A fill:#e3f2fd
    style B fill:#f3e5f5
    style C fill:#fff3e0
    style D fill:#e8f5e8
    style E fill:#e1f5fe
    style F fill:#ffecb3
    style G fill:#ffecb3
    style H fill:#ffcdd2
    style I fill:#e8f5e8
    style J fill:#f3e5f5
    style K fill:#e3f2fd
