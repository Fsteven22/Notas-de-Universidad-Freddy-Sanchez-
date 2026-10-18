graph LR
    A["Sólido"] --> B{"Caras<br/>planas?"}
    B -->|Sí| C["Poliedro<br/>Euler"]
    B -->|No| D["Redondo<br/>revolución"]
    C --> E["Prisma/Pirámide<br/>Regular"]
    D --> E
    style C fill:#e1ffe1
    style D fill:#e1f5ff
