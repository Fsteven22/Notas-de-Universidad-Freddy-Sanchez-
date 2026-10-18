graph TD
    A[Matriz Original] --> B[Algoritmo de Gauss]
    B --> C[Forma Escalonada FE]
    C --> D{¿Necesitas más?}
    D -->|Solo rango| E[Contar pivotes]
    D -->|Soluciones explícitas| F[Gauss-Jordan]
    F --> G[Forma Escalonada Reducida FER]
    
    C --> H[Características de FE]
    H --> H1[Filas nulas al final]
    H --> H2[Pivotes desplazados derecha]
    H --> H3[Ceros debajo de pivotes]
    
    G --> I[Características de FER]
    I --> I1[Todo de FE]
    I --> I2[Pivotes = 1]
    I --> I3[Ceros arriba de pivotes]
    I --> I4[Columnas pivote puras]
    
    E --> J[Aplicaciones]
    G --> J
    J --> J1[Calcular rango]
    J --> J2[Clasificar sistemas]
    J --> J3[Resolver sistemas]
    J --> J4[Bases de espacios]
    J --> J5[Dependencia lineal]
    
    style A fill:#e3f2fd
    style C fill:#fff9c4
    style G fill:#c8e6c9
    style J fill:#ffebee
    style E fill:#f3e5f5
