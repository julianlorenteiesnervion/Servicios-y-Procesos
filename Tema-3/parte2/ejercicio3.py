"""
Ejercicio 3: Cola carnicería
La carnicería tiene 4 empleados, por lo que puede atender a 4 clientes a la vez.
Se usa Semaphore(4) para controlar el acceso.
Se lanzan 10 hilos. Tiempo aleatorio de atención entre 1 y 10 segundos.
"""

import threading
import time
import random


class Cliente(threading.Thread):

    semaforo = threading.Semaphore(4)

    def __init__(self, nombre: str):
        super().__init__(name=nombre)

    def run(self):
        print(f"{self.name} está esperando en la cola de la carnicería")

        with Cliente.semaforo:
            print(f"  -> El cliente {self.name} está siendo atendido")
            tiempo = random.randint(1, 10)
            time.sleep(tiempo)
            print(f"  <- El cliente {self.name} ha terminado en la carnicería ({tiempo}s)")


def main():
    nombres = ["Ana", "Pedro", "Lucía", "Carlos", "María",
               "Andrés", "Sofía", "Diego", "Elena", "Pablo"]

    hilos = []
    for nombre in nombres:
        hilo = Cliente(nombre)
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("\nTodos los clientes han sido atendidos.")


if __name__ == "__main__":
    main()
