# Función que devuelve True si el número es par y False si es impar
def isEven(num):
    return num % 2 == 0

# Declaramos una lista de longitud 8
numbers = [0] * 8

# Le preguntamos al usuario por 8 números
for i in range(8):
    numbers[i] = int(input("Introduce un número: "))

# Recorremos la lista y mostramos si cada número es par o impar
for number in numbers:
    print(f"{number} : {'Par' if isEven(number) else 'Impar'}")
