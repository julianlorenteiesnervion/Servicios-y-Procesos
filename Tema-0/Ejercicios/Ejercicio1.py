# Función que determina si un numero es par o impar
def is_even(number):
    return number % 2 == 0

# Solicitar al usuario que ingrese un numero
number = int(input("Ingrese un numero: "))

# Mostrar el resultado
print("El numero " + str(number) + " es " + ("par" if is_even(number) else "impar"))