# Función que imprime un triángulo de asteriscos de una longitud dada
def printTriangle(length):
    # Cantidad de espacios en blanco antes del primer asterisco de la fila
    firstSpace = length - 1

    # Cantidad de asteriscos en la fila
    starsCount = 1

    # Iterar sobre cada fila del triángulo
    for i in range(1, length + 1):

        # Imprimir los espacios en blanco antes del primer asterisco
        for j in range(firstSpace):
            print(" ", end="")
        
        # Decrementar la cantidad de espacios en blanco para la siguiente fila
        firstSpace -= 1

        # Imprimimos los asteriscos de la fila
        for k in range(starsCount):
            print("* ", end="")

        # Incrementar la cantidad de asteriscos para la siguiente fila
        starsCount += 1

        # Salto de línea después de cada fila
        print()

# Solicitar al usuario la longitud del triángulo
length = int(input("Introduce la longitud del triángulo: "))

# Llamar a la función para imprimir el triángulo
printTriangle(length)