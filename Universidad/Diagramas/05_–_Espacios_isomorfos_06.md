graph LR
    A["(2, -3, 5)<br/>∈ ℝ³"] -->|T| B["2 - 3x + 5x²<br/>∈ 𝒫₂ ℝ"]
    B -->|T⁻¹| A
    C["(a, b, c)"] -->|T| D["a + bx + cx²"]
    D -->|T⁻¹| C
    style A fill:#e1f5ff
    style B fill:#ffe1f5
