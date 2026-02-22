"""
Ejercicio 7: Productor-Consumidor
Problema clásico de productores y consumidores usando queue.Queue.
Se implementa con una cola de tamaño máximo 1.

Si un consumidor intenta obtener un dato y no hay ninguno, espera.
Si un productor intenta insertar y la cola está llena, espera.

¿Cambiaría mucho la solución si el máximo a almacenar son 5 elementos?
No cambiaría la lógica, solo el parámetro maxsize de la cola.
Con maxsize=5 los productores pueden producir más datos antes de bloquearse,
mejorando el rendimiento al reducir los bloqueos entre productor y consumidor.
Se incluye la versión con maxsize=5 comentada al final.
"""

import threading
import time
import random
import queue


class Productor(threading.Thread):

    def __init__(self, nombre: str, cola: queue.Queue, num_items: int):
        super().__init__(name=nombre)
        self.cola = cola
        self.num_items = num_items

    def run(self):
        for i in range(self.num_items):
            dato = f"{self.name}-dato-{i + 1}"
            self.cola.put(dato)  # Se bloquea si la cola está llena
            print(f"{self.name} ha producido: {dato} (cola: {self.cola.qsize()})")
            time.sleep(random.uniform(0.1, 1))

        print(f"{self.name} ha terminado de producir")


class Consumidor(threading.Thread):

    def __init__(self, nombre: str, cola: queue.Queue, num_items: int):
        super().__init__(name=nombre)
        self.cola = cola
        self.num_items = num_items

    def run(self):
        for i in range(self.num_items):
            dato = self.cola.get()  # Se bloquea si la cola está vacía
            print(f"  🛒 {self.name} ha consumido: {dato} (cola: {self.cola.qsize()})")
            time.sleep(random.uniform(0.5, 2))
            self.cola.task_done()

        print(f"{self.name} ha terminado de consumir")


def main():
    # Cola con capacidad máxima de 1 dato
    cola = queue.Queue(maxsize=1)

    NUM_ITEMS_POR_PRODUCTOR = 5

    productores = [
        Productor("Productor-1", cola, NUM_ITEMS_POR_PRODUCTOR),
        Productor("Productor-2", cola, NUM_ITEMS_POR_PRODUCTOR),
    ]

    consumidores = [
        Consumidor("Consumidor-1", cola, NUM_ITEMS_POR_PRODUCTOR),
        Consumidor("Consumidor-2", cola, NUM_ITEMS_POR_PRODUCTOR),
    ]

    for hilo in productores + consumidores:
        hilo.start()

    for hilo in productores + consumidores:
        hilo.join()

    print(f"\nTodos los productores y consumidores han terminado.")
    print(f"Elementos restantes en la cola: {cola.qsize()}")


if __name__ == "__main__":
    main()

# VERSIÓN CON COLA DE TAMAÑO 5:
# Solo hay que cambiar la línea:
#   cola = queue.Queue(maxsize=1)
# por:
#   cola = queue.Queue(maxsize=5)
#
# La lógica del programa no cambia en absoluto. La diferencia es que los
# productores pueden almacenar hasta 5 datos antes de bloquearse, lo que
# reduce la frecuencia de bloqueos y mejora el rendimiento general.
