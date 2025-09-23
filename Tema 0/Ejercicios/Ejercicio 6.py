def factorial(number):
    multiplier = number - 1

    factorial = number

    while multiplier > 0:
        factorial *= multiplier
        multiplier -= 1

    return factorial

number = int(input("Ingrese un numero: "))

print("El factorial de " + str(number) + " es " + str(factorial(number)))