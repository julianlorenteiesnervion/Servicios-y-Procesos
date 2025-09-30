# Declaramos la lista
numbers = [0] * 10

# Le preguntamos al usuario 10 números reales
for i in range(10):
    numbers[i] = float(input("Introduce un número real: "))

# Mostramos el número mínimo y máximo
print("El número mínimo es:", min(numbers))
print("El número máximo es:", max(numbers))
