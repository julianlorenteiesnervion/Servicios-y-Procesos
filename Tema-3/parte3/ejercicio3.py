"""
Ejercicio 3: Paso de peatones
Simulador de paso de peatones con semáforo.
Varios hilos representan peatones que esperan en una barrera para cruzar.
Un temporizador simula el cambio de luz del semáforo, liberando periódicamente
la barrera para permitir el cruce.

Sincronización:
- Event() para simular el semáforo (verde/rojo).
- Lock() para controlar el acceso al cruce.
"""

import threading
import time
import random

NUM_PEATONES = 10
CICLOS_SEMAFORO = 3  # Número de veces que el semáforo cambia a verde


class Semaforo(threading.Thread):
    """Controla el ciclo del semáforo."""

    evento_verde = threading.Event()

    def __init__(self, ciclos: int):
        super().__init__(name="Semáforo", daemon=True)
        self.ciclos = ciclos

    def run(self):
        for i in range(self.ciclos):
            # Semáforo en rojo para peatones
            print("\n🔴 Semáforo en ROJO para peatones - Esperen")
            Semaforo.evento_verde.clear()
            time.sleep(random.randint(3, 6))

            # Semáforo en verde para peatones
            print("\n🟢 Semáforo en VERDE para peatones - ¡Crucen!")
            Semaforo.evento_verde.set()
            time.sleep(random.randint(4, 7))

        # Último ciclo: dejar en verde para que crucen los que queden
        Semaforo.evento_verde.set()


class Peaton(threading.Thread):

    lock = threading.Lock()

    def __init__(self, nombre: str):
        super().__init__(name=nombre)

    def run(self):
        # El peatón llega al paso de peatones en un momento aleatorio
        time.sleep(random.uniform(0, 8))
        print(f"  {self.name} ha llegado al paso de peatones")

        # Espera a que el semáforo esté en verde
        Semaforo.evento_verde.wait()

        with Peaton.lock:
            print(f"  🚶 {self.name} está cruzando la calle")

        tiempo_cruce = random.uniform(1, 3)
        time.sleep(tiempo_cruce)
        print(f"  ✅ {self.name} ha cruzado la calle ({tiempo_cruce:.1f}s)")


def main():
    semaforo = Semaforo(CICLOS_SEMAFORO)
    semaforo.start()

    nombres = ["Ana", "Pedro", "Lucía", "Carlos", "María",
               "Andrés", "Sofía", "Diego", "Elena", "Pablo"]

    peatones = []
    for nombre in nombres:
        peaton = Peaton(nombre)
        peatones.append(peaton)

    for peaton in peatones:
        peaton.start()

    for peaton in peatones:
        peaton.join()

    print("\nTodos los peatones han cruzado.")


if __name__ == "__main__":
    main()
