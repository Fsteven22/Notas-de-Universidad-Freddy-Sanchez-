graph TD
    A[🗂️ Diccionario] --> B{Métodos de Iteración}
    
    B --> C[🔑 .keys()]
    B --> D[📦 .values()] 
    B --> E[🧩 .items()]
    
    C --> C1["for clave in dict.keys()"]
    C --> C2["Solo necesitas las claves"]
    C --> C3["Verificaciones, filtros"]
    
    D --> D1["for valor in dict.values()"]
    D --> D2["Cálculos estadísticos"]
    D --> D3["Suma, promedio, máx/mín"]
    
    E --> E1["for clave, valor in dict.items()"]
    E --> E2["Acceso completo a datos"]
    E --> E3["Análisis complejos"]
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#f1f8e9
    
    style E fill:#c8e6c9
    style E1 fill:#a5d6a7
    style E2 fill:#a5d6a7
    style E3 fill:#a5d6a7
