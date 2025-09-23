# Le pedimos al usuario un número
number = int(input("Ingrese un numero: "))

# Contador para los números desde 1 hasta el número ingresado
counter = 1

# Mientras el contador sea menor o igual al número ingresado, imprimimos el contador y lo incrementamos
while counter <= number:
    print(counter)
    counter += 1
