"""
Ejercicio 3: Número oculto
"""

import threading
import random


class HiloAdivinador(threading.Thread):

    numero_oculto = random.randint(0, 100)
    acertado = False

    def __init__(self, nombre: str):
        super().__init__(name=nombre)

    def run(self):
        intentos = 0
        while not HiloAdivinador.acertado:
            numero = random.randint(0, 100)
            intentos += 1

            if numero == HiloAdivinador.numero_oculto:
                HiloAdivinador.acertado = True
                print(f"¡{self.name} ha acertado el número {numero} en {intentos} intentos!")
                return

            if HiloAdivinador.acertado:
                print(f"{self.name} se detiene porque otro hilo ya acertó. Intentos: {intentos}")
                return

        print(f"{self.name} se detiene porque otro hilo ya acertó. Intentos: {intentos}")


def main():
    print(f"Número oculto generado: {HiloAdivinador.numero_oculto}")
    print("-" * 50)

    hilos = []
    for i in range(10):
        hilo = HiloAdivinador(f"Hilo-{i}")
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("-" * 50)
    print("Todos los hilos han finalizado.")


if __name__ == "__main__":
    main()
