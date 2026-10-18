graph TB
    subgraph "Espacio V"
    V1[v₁] 
    V2[v₂]
    V3[v₃]
    V4[Base de V]
    end
    
    subgraph "Transformación T"
    T[Isomorfismo<br/>T: V → W]
    end
    
    subgraph "Espacio W"
    W1[w₁ = T v₁]
    W2[w₂ = T v₂]
    W3[w₃ = T v₃]
    W4[Base de W]
    end
    
    V1 --> T --> W1
    V2 --> T --> W2
    V3 --> T --> W3
    V4 -.->|se mapea a| W4
    
    style T fill:#e1ffe1
    style V4 fill:#e1f5ff
    style W4 fill:#ffe1f5
