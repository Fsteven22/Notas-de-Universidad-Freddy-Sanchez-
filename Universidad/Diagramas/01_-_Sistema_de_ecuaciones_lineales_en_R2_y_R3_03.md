graph TD
    A[Solución de S.E.L.<br/>en ℝ² y ℝ³] --> B[En ℝ²<br/>2 ecuaciones, 2 incógnitas]
    A --> C[En ℝ³<br/>3 ecuaciones, 3 incógnitas]
    
    B --> B1[Compatible Determinado<br/>Rectas se intersectan<br/>1 punto]
    B --> B2[Incompatible<br/>Rectas paralelas<br/>No hay solución]
    B --> B3[Indeterminado<br/>Rectas coincidentes<br/>∞ soluciones: una recta]
    
    C --> C1[Compatible Determinado<br/>3 planos → 1 punto<br/>Solución única]
    C --> C2[Incompatible<br/>No hay punto común<br/>Sin solución]
    C --> C3[Indeterminado<br/>3 planos → recta o plano<br/>∞ soluciones]
    
    style A fill:#e3f2fd
    style B fill:#fff3e0
    style C fill:#e8f5e9
    style B1 fill:#c8e6c9
    style B2 fill:#ffcdd2
    style B3 fill:#fff9c4
    style C1 fill:#a5d6a7
    style C2 fill:#ef9a9a
    style C3 fill:#ffe082
