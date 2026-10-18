graph TB
    A[Estructuras de Datos] --> B[📝 Listas - Mutables]
    A --> C[🔒 Tuplas - Inmutables]
    
    B --> D[Métodos de Modificación]
    B --> E[Casos de Uso Dinámicos]
    
    C --> F[Operaciones de Solo Lectura]
    C --> G[Casos de Uso Estáticos]
    
    D --> D1[append - Agregar]
    D --> D2[remove - Eliminar]
    D --> D3[sort - Ordenar]
    
    E --> E1[🛒 Inventarios]
    E --> E2[📊 Logs]
    E --> E3[💾 Caches]
    
    F --> F1[Indexing - Acceso]
    F --> F2[Slicing - Rebanado]
    F --> F3[count - Contar]
    
    G --> G1[🌍 Coordenadas]
    G --> G2[⚙️ Configuraciones]
    G --> G3[🔢 Constantes]
    
    style A fill:#e1f5fe
    style B fill:#e8f5e8
    style C fill:#fff3e0
    style D fill:#f3e5f5
    style F fill:#fce4ec
