"""
Ejercicio 1: Hilos trabajadores
"""

import threading
import time
import random

NOMBRES = ["Carlos", "María", "Pedro", "Lucía", "Andrés"]


class HiloTrabajador(threading.Thread):

    def __init__(self, nombre: str):
        super().__init__(name=nombre)

    def run(self):
        while True:
            print(f"Soy {self.name} y estoy trabajando")
            tiempo = random.randint(1, 10)
            time.sleep(tiempo)
            print(f"Soy {self.name} y he terminado de trabajar")


def main():
    hilos = []
    for nombre in NOMBRES:
        hilo = HiloTrabajador(nombre)
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()


if __name__ == "__main__":
    main()
