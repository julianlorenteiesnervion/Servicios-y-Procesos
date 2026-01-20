from multiprocessing import Process

# Método para sumar números desde el 1 hasta el número introducido por parámetro de entrada
def addUntil(number):
    result = 0

    for i in range(1, number + 1):
        result += i

    print(result)

if __name__ == "__main__":

    number = int(input("Introduce un número: "))

    # Creación del proceso
    process = Process(target = addUntil, args = [number])

    # Iniciar el proceso
    process.start()

    # Esperar a que termine el proceso
    process.join()
