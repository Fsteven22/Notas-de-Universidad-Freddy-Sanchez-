flowchart TD
    A[🚀 Programa Principal] --> B{📞 Llamada a Función}
    B --> C[📥 Recibir Argumentos]
    C --> D[🎯 Asignar a Parámetros]
    D --> E[⚙️ Ejecutar Código de la Función]
    E --> F{📤 ¿Hay return?}
    F -->|Sí| G[↩️ Devolver Valor]
    F -->|No| H[↩️ Devolver None]
    G --> I[📨 Continuar Programa Principal]
    H --> I
    
    E --> J[🔧 Variables Locales]
    J -.-> K[🗑️ Se destruyen al terminar]
    
    style A fill:#e3f2fd
    style E fill:#f3e5f5
    style G fill:#e8f5e8
    style H fill:#fff3e0
    style J fill:#fce4ec
