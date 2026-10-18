graph TD
    A[Distancia d·,·] --> B[M1: d·u,v ≥ 0]
    A --> C[M2: d·u,v = 0 ⟺ u = v]
    A --> D[M3: d·u,v = d·v,u]
    A --> E[M4: Desigualdad triangular]
    B --> F[✅ De N1]
    C --> G[✅ De N2]
    D --> H[✅ De simetría de ‖·‖]
    E --> I[✅ De N4]
    style A fill:#e1ffe1
