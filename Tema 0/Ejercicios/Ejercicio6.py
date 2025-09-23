# Función para calcular el factorial de un número
def factorial(number):
    # Multiplicador para el bucle
    multiplier = number - 1

    # Variable para almacenar el resultado del factorial
    factorial = number

    # Mientras el multiplicador sea mayor que 0
    while multiplier > 0:
        # Multiplicar el factorial por el multiplicador y decrementar el multiplicador
        factorial *= multiplier
        multiplier -= 1

    # Devolver el resultado del factorial
    return factorial

# Solicitar al usuario que ingrese un número
number = int(input("Ingrese un numero: "))

# Imprimir el resultado del factorial
print("El factorial de " + str(number) + " es " + str(factorial(number)))