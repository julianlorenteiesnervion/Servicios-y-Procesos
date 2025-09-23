# Variable para guardar el número ingresado
number = 0

# Variable para guardar la suma de los números positivos
sum = 0

# Bucle para pedir números hasta que se ingrese uno negativo
while number >= 0:
    # Si el número es positivo, se suma a la variable sum
    sum += number

    # Se pide un nuevo número
    number = int(input("Ingrese un numero: "))

# Se muestra la suma de los números positivos
print("La suma de los números positivos es: " + str(sum))