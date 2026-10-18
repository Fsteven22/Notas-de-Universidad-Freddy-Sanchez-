graph TD
    A[Vectores originales<br/>v₁, v₂, v₃] --> B[Paso 1: Mantener v₁<br/>normalizar → u₁]
    B --> C[Paso 2: Proyectar v₂<br/>eliminar componente en u₁]
    C --> D[Paso 3: Proyectar v₃<br/>eliminar componentes en u₁, u₂]
    D --> E[Resultado: Base<br/>ortonormal]
    style B fill:#e1f5ff
    style C fill:#fff4e1
    style E fill:#e1ffe1
