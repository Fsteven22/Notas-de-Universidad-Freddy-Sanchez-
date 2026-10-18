graph TB
    subgraph "Vector Original"
    A1[e₁ = 1,0] 
    A2[e₂ = 0,1]
    end
    subgraph "Rotación θ"
    B[Aplicar Rotación]
    end
    subgraph "Vectores Rotados"
    C1["T(e₁) = cos(θ), sin(θ)"]
    C2["T(e₂) = -sin(θ), cos(θ)"]
    end
    A1 --> B
    A2 --> B
    B --> C1
    B --> C2
    style B fill:#fff4e1
