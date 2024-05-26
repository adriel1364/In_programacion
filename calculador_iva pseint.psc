Proceso sin_titulo
	INICIO
    ESCRIBIR "Ingrese el precio del producto: "
    LEER precio_del_producto
    iva <- precio_del_producto * 0.21
    iva_redondeado <- redondear(iva, 1)
    precio_final_producto <- precio_del_producto + iva_redondeado
    ESCRIBIR "El precio del producto con el IVA incluido es: " + CONVERTIR_A_TEXTO(precio_final_producto) + " pesos"
FIN
FinProceso
