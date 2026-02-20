"""
Ejercicio 2: Contador compartido
"""

import threading


class HiloContador(threading.Thread):

    variable_compartida = 0

    def __init__(self, num: int, nombre: str):
        super().__init__(name=nombre)
        self.num = num

    def run(self):
        while HiloContador.variable_compartida < 1000:
            HiloContador.variable_compartida += 1
            print(f"{self.name} incrementa el contador a {HiloContador.variable_compartida}")

        print(f"{self.name} ha terminado")


def main():
    hilos = []
    for i in range(10):
        hilo = HiloContador(i, f"Hilo-{i}")
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print(f"\nValor final del contador: {HiloContador.variable_compartida}")
    print("Nota: el valor puede ser distinto de 1000 debido a condiciones de carrera.")


if __name__ == "__main__":
    main()
