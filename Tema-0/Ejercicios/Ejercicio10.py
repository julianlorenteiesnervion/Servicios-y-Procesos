# Función que devuelve el número más grande entre dos números
def maxNumber(number1, number2):
    biggest = number1

    if number2 > number1:
        biggest = number2
    
    return biggest

# Solicitar al usuario que introduzca dos números
number1 = int(input("Introduce un número: "))
number2 = int(input("Introduce otro número: "))

# Mostrar el número más grande
print("El número más grande es:", maxNumber(number1, number2))