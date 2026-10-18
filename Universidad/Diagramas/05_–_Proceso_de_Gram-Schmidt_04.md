graph TD
    A[Vectores linealmente<br/>independientes] --> B{Gram-Schmidt}
    B -->|Paso 1| C["Vectores<br/>ORTOGONALES"]
    C -->|Paso 2| D["Vectores<br/>ORTONORMALES"]
    C --> E[Perpendiculares<br/>uᵢ · uⱼ = 0]
    D --> F["Perpendiculares<br/>Y unitarios<br/>||uᵢ|| = 1"]
    style C fill:#fff4e1
    style D fill:#e1ffe1
