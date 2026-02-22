"""
Ejercicio 2: Cola panadería
Simula la cola de una panadería con un solo dependiente.
Los clientes son atendidos de uno en uno usando Lock().
El dependiente tarda entre 1 y 5 segundos en atender a cada cliente.
"""

import threading
import time
import random


class Cliente(threading.Thread):

    lock = threading.Lock()

    def __init__(self, nombre: str):
        super().__init__(name=nombre)

    def run(self):
        print(f"{self.name} está esperando a ser atendido")

        with Cliente.lock:
            print(f"  -> {self.name} está siendo atendido por el dependiente")
            tiempo = random.randint(1, 5)
            time.sleep(tiempo)
            print(f"  <- {self.name} ha sido atendido ({tiempo}s)")


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
