graph TB
    A[🎯 Selección de Datos] --> B[📊 Columnas]
    A --> C[📋 Filas]
    A --> D[🔍 Filtros]
    
    B --> E[🔤 Por nombre]
    B --> F[📝 Múltiples]
    B --> G[🔍 Por tipo]
    
    C --> H[.loc - etiquetas]
    C --> I[.iloc - posición]
    
    D --> J[❓ Condicionales]
    D --> K[🔗 Combinados]
    
    style A fill:#e8f5e8,stroke:#388e3c,stroke-width:3px
    style H fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    style I fill:#fce4ec,stroke:#c2185b,stroke-width:2px
