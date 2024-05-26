"""Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos
la unidad. Si el cliente compra más de 12  unidades (y hasta 24 unidades),
el costo tiene un descuento del 10%. Si compra más de 24 unidades, el 
descuento es del 15%. Además posee la promoción a los jubilados.
La promoción de jubilados es sumarle un 10% de descuento (si posee otros 
descuentos, se suma los descuentos).
Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.
"""
# EMPEZAMOS
print("******************** DESPENSA EL BICHO ********************")

cantidad_de_unidades = int(input("Ingrese la cantidad de unidades de leche: "))
es_jubilado = input("Ingrese S si es jubilado o N si no es jubilado: ").lower() == 's'

def calcular_pago(cantidad_de_unidades, es_jubilado):
    precio_unitario = 1000
    descuento = 0

    if 12 < cantidad_de_unidades <= 24:
        descuento = 0.10
    elif cantidad_de_unidades > 24:
        descuento = 0.15
    
    if es_jubilado:
        descuento += 0.10

    precio_total = cantidad_de_unidades * precio_unitario
    precio_con_descuento = precio_total - (precio_total * descuento)
    
    return precio_con_descuento


total_a_pagar = calcular_pago(cantidad_de_unidades, es_jubilado)

print(f"El total a pagar es: {total_a_pagar} pesos")