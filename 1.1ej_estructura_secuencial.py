"""EJERCICIO 1: Un estudiante está cursando 5 materias, tiene la nota de cada

materia y quiere saber cuál es su promedio."""

# EMPEZAMOS
nota_1 = int(input("Ingrese la nota de la matera 1: "))
nota_2 = int(input("Ingrese la nota de la matera 2: "))
nota_3 = int(input("Ingrese la nota de la matera 3: "))
nota_4 = int(input("Ingrese la nota de la matera 4: "))
nota_5 = int(input("Ingrese la nota de la matera 5: "))

promedio = (nota_1+nota_2+nota_3+nota_4+nota_5)/5 


print(f"El promedio de las 5 materias es:{promedio} ")
