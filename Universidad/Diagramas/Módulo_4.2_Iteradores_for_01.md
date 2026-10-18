flowchart TD
    A[🎯 Secuencia<br/>Lista, String, Range] --> B{🔄 ¿Hay elementos?}
    B -->|Sí| C[📦 Tomar siguiente elemento]
    C --> D[🎯 Asignar a variable temporal]
    D --> E[⚡ Ejecutar bloque de código]
    E --> F{🛑 ¿break?}
    F -->|Sí| H[🏁 Fin del bucle]
    F -->|No| G{⏭️ ¿continue?}
    G -->|Sí| B
    G -->|No| B
    B -->|No| H
    
    style A fill:#e1f5fe
    style E fill:#f3e5f5
    style H fill:#e8f5e8
