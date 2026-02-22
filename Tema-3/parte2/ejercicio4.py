"""
Ejercicio 4: Carnicería y Charcutería
La carnicería tiene 4 empleados y la charcutería 2.
Todos los clientes pasan por ambas secciones (en cualquier orden).
Si una sección está llena pero la otra tiene hueco, el cliente va a la que esté libre.
Se lanzan 10 hilos.
"""

import threading
import time
import random


class Cliente(threading.Thread):

    semaforo_carniceria = threading.Semaphore(4)
    semaforo_charcuteria = threading.Semaphore(2)

    def __init__(self, nombre: str):
        super().__init__(name=nombre)

    def atender_carniceria(self):
        with Cliente.semaforo_carniceria:
            tiempo = random.randint(1, 5)
            print(f"{self.name} está siendo atendido en CARNICERÍA ({tiempo}s)")
            time.sleep(tiempo)
            print(f"{self.name} ha terminado en CARNICERÍA")

    def atender_charcuteria(self):
        with Cliente.semaforo_charcuteria:
            tiempo = random.randint(1, 5)
            print(f"{self.name} está siendo atendido en CHARCUTERÍA ({tiempo}s)")
            time.sleep(tiempo)
            print(f"{self.name} ha terminado en CHARCUTERÍA")

    def run(self):
        print(f"{self.name} ha llegado a la tienda")

        # Intenta ir primero a la sección que tenga hueco disponible
        # Elige orden aleatorio para evitar que todos vayan al mismo sitio
        if random.choice([True, False]):
            self.atender_carniceria()
            self.atender_charcuteria()
        else:
            self.atender_charcuteria()
            self.atender_carniceria()

        print(f"*** {self.name} ha sido atendido en ambas secciones ***")


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

    print("\nTodos los clientes han sido atendidos en ambas secciones.")


if __name__ == "__main__":
    main()
