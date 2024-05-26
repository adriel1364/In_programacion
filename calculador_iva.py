"""
Desarrollar un programa secuencial que permita ingresar un precio
calcular el IVA y mostrar el precio final de lista de un producto
Ejemplo: Si un producto vale $100 y el IVA es 21, el precio de lista es $121
"""

# EMPEZAMOS
print("******************** CALCULADOR DE IVA ********************")

precio_del_producto = float(input("Ingrese el precio del producto: "))
iva = precio_del_producto * 0.21
iva_redondeado=round(iva,1)
precio_final_producto = precio_del_producto + iva_redondeado

print(f"El precio del producto con el IVA incluido es:{precio_final_producto} pesos")
