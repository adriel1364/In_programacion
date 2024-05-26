""" Convertidor de pesos argentinos a dolar estadunidense"""

# EMPEZAMOS
print("******************** CASA DE CAMBIO EL BICHO ********************")

cantidad_pesos = int(input('Ingrese la cantidad de pesos argentinos: '))
tipo_de_cambio = int(input('Ingrese a cuantos pesos argentinos equivale 1 dolar: '))

convertimos =cantidad_pesos * tipo_de_cambio

print(f"Los {cantidad_pesos} pesos argentinos que usted tiene.")
print(f"Son {convertimos} dolares estadunidense")
