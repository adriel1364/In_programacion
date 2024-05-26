Proceso sin_titulo
	Definir cantidad_de_unidades Como Entero
	Definir es_jubilado Como Lógico
	
	Escribir "Ingrese la cantidad de unidades de leche:"
	Leer cantidad_de_unidades
	Escribir "Ingrese S si es jubilado o N si no es jubilado:"
	Leer es_jubilado
	es_jubilado = es_jubilado en minúsculas == 's'
	
	Función calcular_pago(cantidad_de_unidades, es_jubilado)
    Definir precio_unitario Como Real
    Definir descuento Como Real
	
    precio_unitario = 1000
    descuento = 0
	
    Si 12 < cantidad_de_unidades <= 24 Entonces
        descuento = 0.10
    Sino Si cantidad_de_unidades > 24 Entonces
			descuento = 0.15
		Fin Si
		
		Si es_jubilado Entonces
			descuento += 0.10
		Fin Si
		
		Definir precio_total Como Real
		Definir precio_con_descuento Como Real
		
		precio_total = cantidad_de_unidades * precio_unitario
		precio_con_descuento = precio_total - (precio_total * descuento)
		
		Devolver precio_con_descuento
	Fin Función
	
	total_a_pagar = calcular_pago(cantidad_de_unidades, es_jubilado)
	
	Escribir "El total a pagar es:", total_a_pagar, "pesos"

FinProceso
