def is_even(number):
    return number % 2 == 0

number = int(input("Ingrese un numero: "))

print("El numero " + str(number) + " es " + ("par" if is_even(number) else "impar"))