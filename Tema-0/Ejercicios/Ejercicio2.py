# Función para imprimir el array de números
def printArray(array):
    # Construir el mensaje de salida
    message = "Los números ordenados son: "

    # Concatenar cada número al mensaje
    for i in array:
        message += str(i) + " "

    # Imprimir el mensaje final
    print(message)

# Le preguntamos al usuario por el primer número
number1 = int(input("Ingrese el primer numero: "))

# Le preguntamos al usuario por el segundo número
number2 = int(input("Ingrese el segundo numero: "))

# Creamos un array con los números ingresados y lo ordenamos
numbers = [number1, number2]

# Ordenamos el array y lo imprimimos con la función
printArray(sorted(numbers))