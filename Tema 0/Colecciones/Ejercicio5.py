import random

# Declaramos una lista de tamaño 100
numbers = [0] * 100

# Rellenamos la lista con números aleatorios entre 1 y 10
for i in range(100):
    numbers[i] = random.randint(1, 10)

# Pedimos al usuario un número
number = int(input("Introduce un número: "))

# Contamos y mostramos cuántas veces aparece el número en la lista
print(f"El número {number} aparece {numbers.count(number)} veces en la lista.")