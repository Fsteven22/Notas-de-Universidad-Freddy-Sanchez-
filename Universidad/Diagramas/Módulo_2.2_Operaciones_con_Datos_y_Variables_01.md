graph LR
    A["📥 Dato Original"] --> B{"🔄 Operación"}
    B --> C["📤 Dato Resultado"]

    D["123 como str"] --> E["int"]
    E --> F["123 como int"]

    G["5 como int"] --> H["sumar 3"]
    H --> I["8 como int"]

    J["True como bool"] --> K["and False"]
    K --> L["False como bool"]

    M["Hola como str"] --> N["concatenar Mundo"]
    N --> O["HolaMundo como str"]

    style A fill:#e3f2fd
    style B fill:#fff3e0
    style C fill:#e8f5e8
