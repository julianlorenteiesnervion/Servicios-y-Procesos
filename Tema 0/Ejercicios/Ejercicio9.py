# Función que imprime todos los números entre dos números dados (inclusive)
def printNumbers(from_num, to_num):
    for i in range(from_num, to_num + 1):
        print(i)

# Método main para ejecutar el programa
def main():
    # Solicitar al usuario los números inicial y final
    from_num = int(input("Introduce el número inicial: "))
    to_num = int(input("Introduce el número final: "))

    # Llamar a la función para imprimir los números en el rango dado
    printNumbers(from_num, to_num)

# Ejecutar el método main
if __name__ == "__main__":
    main()