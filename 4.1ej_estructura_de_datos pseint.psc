Proceso sin_titulo
	INICIO
    nombres_unicos <- lista vacía
	
    MIENTRAS longitud de nombres_unicos < 10 HACER
        ESCRIBIR "Ingrese solo nombre: "
        LEER nombre
        SI nombre EN nombres_unicos ENTONCES
            ESCRIBIR "Ese nombre ya ha sido ingresado. Por favor, ingrese un nombre diferente."
        SINO
            AGREGAR nombre A nombres_unicos
        FIN SI
    FIN MIENTRAS
	
    ESCRIBIR "Los nombres ingresados son:"
    PARA CADA nombre EN nombres_unicos HACER
        ESCRIBIR nombre
    FIN PARA
FIN
FinProceso
