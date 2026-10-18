graph LR
    A["A(0,0)"] -->|"d(A,B) = 5"| B["B(3,4)"]
    B -->|"d(B,C) = 5"| C["C(6,0)"]
    A -.->|"d(A,C) = 6"| C
    Note["6 ≤ 5 + 5<br/>6 ≤ 10 ✓"]
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style C fill:#e1ffe1
    style Note fill:#e1ffe1
