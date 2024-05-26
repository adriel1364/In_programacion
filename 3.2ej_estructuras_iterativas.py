"2 - Mostrar sólo los números pares desde 0 hasta el número ingresado (input). Nota: para saber si un número es par hacer i % 2 == 0)"

# EMPEZAMOS
numero = int(input('Ingrese un numero entero positivo: '))

for i in range(2, numero+1, 2):
    print(i,end=" ")
     
print("Esos son los numeros PARES que estan desde el 0 al numero que elegiste.")
  
    