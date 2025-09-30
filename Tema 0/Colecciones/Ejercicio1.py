import random

# Inicializamos una lista vacía
numeros = [0] * 10

# Creamos una lista con 10 números aleatorios entre 1 y 100
for i in range(10):
    numeros[i] = random.randint(1, 100)

# Mostramos la lista
print("Lista:", numeros)
