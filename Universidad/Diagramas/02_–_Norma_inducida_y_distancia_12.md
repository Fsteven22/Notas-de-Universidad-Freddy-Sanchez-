graph TD
    subgraph "Caso 1: Igualdad (Colineales)"
    A1[u] --> B1[u+v]
    A1 --> C1[v]
    C1 --> B1
    end
    
    subgraph "Caso 2: Desigualdad estricta"
    A2[u] --> B2[u+v]
    A2 -.-> C2[v]
    C2 -.-> B2
    end
    
    subgraph "Caso 3: Vectores opuestos"
    A3[u] --> B3[0]
    A3 --> C3[-u]
    C3 --> B3
    end
    
    style B1 fill:#e1ffe1
    style B2 fill:#fff4e1
    style B3 fill:#ffe1e1
