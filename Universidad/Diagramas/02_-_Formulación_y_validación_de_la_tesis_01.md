graph TD
    T[Tesis propuesta] --> F1{"¿Es debatible?"}
    F1 -->|No, es un hecho| X1[Rechazar]
    F1 -->|Sí| F2{"¿Es específica?"}
    F2 -->|No, es una generalización absoluta| X2[Rechazar]
    F2 -->|Sí| F3{"¿Es aseverativa?"}
    F3 -->|No, es pregunta retórica| X3[Rechazar]
    F3 -->|Sí| F4{"¿Tiene certeza enunciativa?"}
    F4 -->|No, es condicional hipotético| X4[Rechazar]
    F4 -->|Sí| F5{"¿Estructura gramatical completa?"}
    F5 -->|No, es frase nominal/infinitivo| X5[Rechazar]
    F5 -->|Sí| OK[Tesis válida]
