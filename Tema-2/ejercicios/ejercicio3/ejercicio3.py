from multiprocessing import Process, Pool, Queue
import os

# Método para leer un fichero y guarde los números en cola
def readFileAndPutInQueue(file_name, queue):
    # Abrimos el archivo para leerlo
    with open(file_name, 'r') as file:
        # Recorremos el archivo
        for line in file:
            # Verificamos que haya algo en la línea
            if (line.strip() != ""):
               # Si hay algo, casteamos a entero (ya que son números) y quitamos los espacios
               queue.put(int(line.strip()))
    # Cuando ya no haya más números en el archivo, ponemos None para indicar que ya no hay más números
    queue.put(None)

# Método para sumar desde cola
def sumFromQueue(queue):

    # Inicializamos la suma en 0
    total = 0

    # Obtenemos el primer número
    number = queue.get()

    # Mientras haya números en la cola
    while number is not None:

        # Sumamos al total
        total += number

        # Obtenemos el siguiente
        number = queue.get()
       
    print(f"La suma de los números en el archivo es {total}")

if __name__ == "__main__":

    os.chdir("Tema-2/ejercicios/ejercicio3")

    cola = Queue()

    # Proceso que leerá del archivo y lo pondrá en la cola
    p1 = Process(target=readFileAndPutInQueue, args=("numbers.txt", cola,))

    # Proceso que sacará de la cola los números para sumarlos
    p2 = Process(target=sumFromQueue, args=(cola,))

    # Iniciamos los procesos
    p1.start()
    p2.start()

    # Acabamos con el proceso 1
    p1.join()

    # Acabamos con el proceso 2
    p2.join()
