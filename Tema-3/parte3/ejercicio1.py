"""
Ejercicio 1: Carrera
Simula una carrera con 10 participantes. Todos parten de la misma línea de salida.
Una vez están todos colocados, se hace una cuenta atrás desde 3 y salen todos a la vez.
Se calcula cuánto tarda cada uno en terminar la carrera.

Sincronización: Barrier(10) para que todos esperen en la línea de salida,
y Event() para el pistoletazo de salida tras la cuenta atrás.
"""

import threading
import time
import random


class Corredor(threading.Thread):

    barrera = threading.Barrier(11)  # 10 corredores + hilo principal
    evento_salida = threading.Event()

    def __init__(self, nombre: str):
        super().__init__(name=nombre)
        self.tiempo_carrera = 0

    def run(self):
        print(f"{self.name} se ha colocado en la línea de salida")
        # Espera a que todos los corredores estén en la línea de salida
        Corredor.barrera.wait()

        # Espera al pistoletazo de salida
        Corredor.evento_salida.wait()

        inicio = time.time()
        # Simula la carrera con un tiempo aleatorio entre 3 y 10 segundos
        tiempo_corriendo = random.uniform(3, 10)
        time.sleep(tiempo_corriendo)
        fin = time.time()

        self.tiempo_carrera = fin - inicio
        print(f"🏁 {self.name} ha terminado la carrera en {self.tiempo_carrera:.2f} segundos")


def cuenta_atras():
    """Realiza la cuenta atrás y da el pistoletazo de salida."""
    print("\n¡Todos los corredores están listos!")
    for i in range(3, 0, -1):
        print(f"  {i}...")
        time.sleep(1)
    print("  ¡¡¡YA!!!\n")
    Corredor.evento_salida.set()


def main():
    nombres = ["Ana", "Pedro", "Lucía", "Carlos", "María",
               "Andrés", "Sofía", "Diego", "Elena", "Pablo"]

    hilos = []
    for nombre in nombres:
        hilo = Corredor(nombre)
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    # Esperar a que todos estén en la línea de salida
    Corredor.barrera.wait()

    # Cuenta atrás en el hilo principal
    cuenta_atras()

    for hilo in hilos:
        hilo.join()

    # Clasificación final
    hilos.sort(key=lambda h: h.tiempo_carrera)
    print("\n" + "=" * 40)
    print("CLASIFICACIÓN FINAL")
    print("=" * 40)
    for posicion, hilo in enumerate(hilos, 1):
        print(f"  {posicion}º - {hilo.name}: {hilo.tiempo_carrera:.2f}s")
    print("=" * 40)


if __name__ == "__main__":
    main()
