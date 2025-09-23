# Función que determina si un número es primo
def isPrime(number):
    # Variable para contar los divisores del número que ha entrado por parámetro de entrada
    divisors = 0

    # Bucle para contar los divisores del número
    for i in range(1, number + 1):
        if number % i == 0:
            divisors += 1
    
    # Un número es primo si tiene exactamente dos divisores: 1 y él mismo
    return divisors == 2

# Solicitar al usuario que introduzca un número
number = int(input("Introduce un número: "))

# Mostrar si el número es primo o no
print(f"El número {number} {'es' if isPrime(number) else 'no es'} primo.")