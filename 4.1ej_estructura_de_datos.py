"1 - Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos."

# EMPEZAMOS
nombres_unicos = []


while len(nombres_unicos) < 10:
    nombre = input("Ingrese solo nombre: ")
    
    
    if nombre in nombres_unicos:
        print("Ese nombre ya ha sido ingresado. Por favor, ingrese un nombre diferente.")
    else:
        nombres_unicos.append(nombre)

print("Los nombres ingresados son:")
for nombre in nombres_unicos:
    print(nombre)
