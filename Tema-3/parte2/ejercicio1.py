"""
Ejercicio 1: Número oculto con Lock
Igual que el ejercicio de la PARTE 1 pero utilizando Lock() para asegurarse
de que una vez que se averigüe el número, el resto de hilos no generan de nuevo.
"""

import threading
import random


class HiloAdivinador(threading.Thread):

    numero_oculto = random.randint(0, 100)
    acertado = False
    lock = threading.Lock()

    def __init__(self, nombre: str):
        super().__init__(name=nombre)

    def run(self):
        intentos = 0
        while True:
            with HiloAdivinador.lock:
                if HiloAdivinador.acertado:
                    print(f"{self.name} se detiene porque otro hilo ya acertó. Intentos: {intentos}")
                    return

                numero = random.randint(0, 100)
                intentos += 1

                if numero == HiloAdivinador.numero_oculto:
                    HiloAdivinador.acertado = True
                    print(f"¡{self.name} ha acertado el número {numero} en {intentos} intentos!")
                    return


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
