# Declaramos una lista de longitud 10
numbers = [0] * 10

# Le preguntamos al usuario que introduzca 10 números
for i in range(10):
    numbers[i] = int(input("Introduce un número: "))

# Ordenamos la lista de mayor a menor
numbers.sort(reverse = True)

# Mostramos la lista ordenada
print(numbers)