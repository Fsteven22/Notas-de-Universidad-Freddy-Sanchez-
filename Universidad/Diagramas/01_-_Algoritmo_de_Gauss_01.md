graph TD
    A[Sistema de Ecuaciones] --> B[Formar Matriz Ampliada]
    
    B --> C{Fase 1: Eliminación}
    
    C --> D[Columna 1:<br/>Crear ceros debajo del pivote]
    D --> E[Columna 2:<br/>Crear ceros debajo del pivote]
    E --> F[Continuar...<br/>hasta la última columna]
    
    F --> G[Forma Escalonada Obtenida]
    
    G --> H{Análisis}
    
    H -->|Fila 0...0 b, b≠0| I[❌ Incompatible<br/>Sin solución]
    
    H -->|pivotes = n| J[✓ Compatible Determinado<br/>Solución única]
    
    H -->|pivotes < n| K[∞ Compatible Indeterminado<br/>Infinitas soluciones]
    
    J --> L[Fase 2:<br/>Sustitución Regresiva]
    K --> M[Fase 2:<br/>Sustitución con parámetros]
    
    L --> N[Solución Única]
    M --> O[Solución Paramétrica]
    
    style A fill:#e3f2fd
    style B fill:#fff9c4
    style C fill:#ffebee
    style G fill:#c8e6c9
    style H fill:#fff9c4
    style I fill:#ffcdd2
    style J fill:#bbdefb
    style K fill:#ffe0b2
    style N fill:#a5d6a7
    style O fill:#ffcc80
