graph LR
    A["Datos<br/>tabla m x n"] --> B["Matriz<br/>A = (a_ij)"]
    B --> C{"¿Cuadrada?"}
    C -->|"Sí"| D["Diagonal / Id / Sim<br/>det e inversa"]
    C -->|No| E["Rectangular<br/>solo + y por escalar"]
