graph TD
    A[🗂️ Diccionario] --> B{Operaciones Básicas}
    
    B --> C[🔍 Acceso]
    B --> D[➕ Modificación] 
    B --> F[🗑️ Eliminación]
    B --> G[🔍 Búsqueda]
    
    C --> C1("dict[clave]")
    C --> C2("dict.get(clave)")
    C --> C3("clave in dict")
    
    D --> D1("dict[clave] = valor")
    D --> D2("Añadir/Modificar")
    
    F --> F1("del dict[clave]")
    F --> F2("dict.pop(clave)")
    F --> F3("dict.clear()")
    
    G --> G1("Por clave: rápida O(1)")
    G --> G2("Por valor: lenta O(n)")
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style F fill:#ffebee
    style G fill:#f0f4c3
