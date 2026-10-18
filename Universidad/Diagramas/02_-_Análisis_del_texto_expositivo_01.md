graph TD
    A[Leer el parrafo completo] --> B[Buscar la oracion que resume el parrafo]
    B --> C{Al inicio, al final o implicita}
    C -->|Al inicio| D[Idea central - oracion tematica inicial]
    C -->|Al final| E[Idea central - oracion de cierre]
    C -->|Implicita| F[Idea central - inferida por el lector]
    D --> G[Clasificar el resto como ideas de apoyo]
    E --> G
    F --> G
    G --> H[Verificar - cada apoyo se conecta con la idea central]
