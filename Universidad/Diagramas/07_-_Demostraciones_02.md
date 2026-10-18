flowchart TD
    A["Que quiero demostrar?"] --> B{"Es para todo n natural?"}
    B -->|"Si"| C["Induccion<br/>(simple o fuerte)"]
    B -->|"No"| D{"La tesis es P a Q?"}
    D -->|"Conexion directa clara"| E["Directa"]
    D -->|"Negar Q da mas info"| F["Contrapositiva"]
    D -->|"Tesis niega existencia<br/>o posibilidad"| G["Contradiccion"]
    D -->|"Hay particion natural<br/>de casos"| H["Casos"]
    A --> I{"Es existencial: existe x?"}
    I -->|"Puedo exhibir x"| J["Constructiva"]
    I -->|"Solo pruebo que existe"| K["No constructiva"]
