Proceso sin_titulo
    Definir precio_por_metro_cuadrado como Real
    Definir ancho_pared como Real
    Definir alto_pared como Real
    Definir area_pared como Real
    Definir costo_mano_obra como Real
	
    Escribir "Ingrese el precio fijo por metro cuadrado: "
    Leer precio_por_metro_cuadrado
	
    Escribir "Ingrese el ancho de la pared (en metros): "
    Leer ancho_pared
	
    Escribir "Ingrese el alto de la pared (en metros): "
    Leer alto_pared
	
    area_pared = ancho_pared * alto_pared
	
    costo_mano_obra = area_pared * precio_por_metro_cuadrado
	
    Escribir "El costo de mano de obra para pintar la pared es: " + costo_mano_obra + " pesos"
Fin	
FinProceso
