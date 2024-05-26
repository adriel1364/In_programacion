
"""EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo

que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El

cliente le indica que necesita conocer el costo de mano de obra para pintar una

pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro

cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para

pintar la pared."""

# EMPEZAMOS
precio_por_metro_cuadrado = float(input("Ingrese el precio fijo por metro cuadrado: "))

ancho_pared = float(input("Ingrese el ancho de la pared (en metros): "))
alto_pared = float(input("Ingrese el alto de la pared (en metros): "))


area_pared = ancho_pared * alto_pared


costo_mano_obra = area_pared * precio_por_metro_cuadrado


print(f"El costo de mano de obra para pintar la pared es: {costo_mano_obra} pesos")