Proceso sin_titulo
	INICIO
    nombres <- lista vacía
    MIENTRAS VERDADERO
        ESCRIBIR "Ingrese el nombre de una persona o escriba 'fin' para terminar: "
        LEER nombre
        SI nombre = "fin" ENTONCES
            SALIR DEL BUCLE
        FIN SI
        AGREGAR nombre A nombres
    FIN MIENTRAS
	
    PARA CADA nombre EN nombres HACER
        ESCRIBIR nombre
    FIN PARA
FIN
FinProceso
