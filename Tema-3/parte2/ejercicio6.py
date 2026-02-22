"""
Ejercicio 6: Problema de los filósofos de Dijkstra
5 filósofos sentados en una mesa redonda. Cada uno necesita 2 palillos para comer.
El filósofo i usa los palillos i (izquierda) e (i+1) % 5 (derecha).

Solución para evitar interbloqueo:
- Los filósofos pares cogen primero el palillo izquierdo y luego el derecho.
- Los filósofos impares cogen primero el palillo derecho y luego el izquierdo.
Esto rompe la espera circular y evita el interbloqueo.

¿Se llega a producir un interbloqueo?
No, gracias a la asimetría en el orden de adquisición de palillos.

¿Podría algún filósofo no comer nunca?
Sí, es teóricamente posible (starvation/inanición): si los vecinos de un filósofo
siempre consiguen sus palillos antes que él, podría quedarse esperando
indefinidamente, aunque en la práctica es muy improbable.
"""

import threading
import time
import random

NUM_FILOSOFOS = 5
NUM_COMIDAS = 3  # Cada filósofo come este número de veces


class Filosofo(threading.Thread):

    palillos = [threading.Lock() for _ in range(NUM_FILOSOFOS)]

    def __init__(self, num: int, nombre: str):
        super().__init__(name=nombre)
        self.num = num
        self.palillo_izquierdo = Filosofo.palillos[num]
        self.palillo_derecho = Filosofo.palillos[(num + 1) % NUM_FILOSOFOS]

    def pensar(self):
        print(f"🤔 {self.name} está pensando...")
        time.sleep(random.uniform(1, 3))

    def comer(self):
        print(f"🍝 {self.name} está comiendo")
        time.sleep(random.uniform(1, 3))

    def run(self):
        for i in range(NUM_COMIDAS):
            self.pensar()

            # Asimetría para evitar interbloqueo:
            # Los pares cogen izquierdo primero, los impares cogen derecho primero
            if self.num % 2 == 0:
                primero = self.palillo_izquierdo
                segundo = self.palillo_derecho
            else:
                primero = self.palillo_derecho
                segundo = self.palillo_izquierdo

            with primero:
                print(f"  {self.name} ha cogido el primer palillo")
                with segundo:
                    print(f"  {self.name} ha cogido el segundo palillo")
                    self.comer()
                    print(f"  {self.name} suelta ambos palillos")

        print(f"✅ {self.name} ha terminado de comer {NUM_COMIDAS} veces")


def main():
    nombres = ["Platón", "Aristóteles", "Sócrates", "Descartes", "Kant"]

    hilos = []
    for i, nombre in enumerate(nombres):
        hilo = Filosofo(i, nombre)
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("\nTodos los filósofos han comido.")


if __name__ == "__main__":
    main()
