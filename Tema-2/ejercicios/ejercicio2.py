from multiprocessing import Process, Pool

# Método para sumar números desde el 1 hasta el número introducido por parámetro de entrada
def addUntil(number):
    result = 0

    for i in range(1, number + 1):
        result += i

    print(result)

if __name__ == "__main__":

    number = int(input("Introduce un número: "))

    # Piscina
    with Pool(processes=4) as pool:
        pool.map(addUntil, [number])
