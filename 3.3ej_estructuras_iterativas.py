"3 - Pedir que el usuario ingrese (input) nombre de personas y mostrarlos hasta que el valor de lo que ingresa sea “fin”"

# EMPEZAMOS

nombres = []
while True:
    nombre = input("Ingrese el nombre de una persona o escriba 'fin' para terminar: ")
    if nombre.lower() == 'fin':
        break
    nombres.append(nombre)


for nombre in nombres:
    print(nombre)
    
    
    
  
    