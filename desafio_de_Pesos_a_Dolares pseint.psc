Proceso sin_titulo
	INICIO
    ESCRIBIR "Ingrese la cantidad de pesos argentinos: "
    LEER cantidad_pesos
    ESCRIBIR "Ingrese a cu�ntos pesos argentinos equivale 1 d�lar: "
    LEER tipo_de_cambio
    convertimos <- cantidad_pesos * tipo_de_cambio
    ESCRIBIR "Los " + CONVERTIR_A_TEXTO(cantidad_pesos) + " pesos argentinos que usted tiene."
    ESCRIBIR "Son " + CONVERTIR_A_TEXTO(convertimos) + " d�lares estadounidenses"
FIN
FinProceso
