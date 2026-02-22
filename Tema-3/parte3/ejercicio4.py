"""
Ejercicio 4: Pedidos de un almacén
Simulador de procesamiento de pedidos en un almacén.
Varios hilos (trabajadores) preparan pedidos.

Sincronización:
- Barrier() para que todos los trabajadores comiencen a trabajar al mismo tiempo.
- Event() para indicar si hay un pedido disponible para preparar.
  Cuando se empieza a preparar un pedido, el evento se pone a "no seteado".
  Tras un tiempo, se genera otro pedido y se vuelve a "setear".
"""

import threading
import time
import random

NUM_TRABAJADORES = 5
NUM_PEDIDOS = 8


class GeneradorPedidos(threading.Thread):
    """Genera pedidos periódicamente señalizando con un Event."""

    evento_pedido = threading.Event()
    lock = threading.Lock()
    pedido_actual = 0
    pedidos_totales = NUM_PEDIDOS
    todos_generados = False

    def __init__(self):
        super().__init__(name="Generador", daemon=True)

    def run(self):
        for i in range(1, self.pedidos_totales + 1):
            # Simula un tiempo entre la llegada de pedidos
            time.sleep(random.uniform(1, 3))

            with GeneradorPedidos.lock:
                GeneradorPedidos.pedido_actual = i
                print(f"\n📦 ¡Nuevo pedido #{i} disponible!")
                GeneradorPedidos.evento_pedido.set()

        # Marcar que se han generado todos los pedidos
        time.sleep(1)
        GeneradorPedidos.todos_generados = True
        GeneradorPedidos.evento_pedido.set()  # Despertar a los que esperen


class Trabajador(threading.Thread):

    barrera = threading.Barrier(NUM_TRABAJADORES + 1)  # +1 por el hilo principal
    pedidos_completados = 0
    lock_pedidos = threading.Lock()

    def __init__(self, nombre: str):
        super().__init__(name=nombre)

    def run(self):
        print(f"{self.name} está listo")
        Trabajador.barrera.wait()

        while True:
            # Esperar a que haya un pedido disponible
            GeneradorPedidos.evento_pedido.wait()

            if GeneradorPedidos.todos_generados:
                with Trabajador.lock_pedidos:
                    if Trabajador.pedidos_completados >= GeneradorPedidos.pedidos_totales:
                        print(f"  {self.name} ha terminado su turno")
                        return

            # Intentar tomar el pedido
            with GeneradorPedidos.lock:
                if not GeneradorPedidos.evento_pedido.is_set():
                    continue  # Otro trabajador ya tomó el pedido

                pedido = GeneradorPedidos.pedido_actual
                GeneradorPedidos.evento_pedido.clear()  # Marcar como "no disponible"

            # Preparar el pedido
            tiempo = random.uniform(1, 4)
            print(f"  🔧 {self.name} está preparando el pedido #{pedido} ({tiempo:.1f}s)")
            time.sleep(tiempo)
            print(f"  ✅ {self.name} ha completado el pedido #{pedido}")

            with Trabajador.lock_pedidos:
                Trabajador.pedidos_completados += 1
                if Trabajador.pedidos_completados >= GeneradorPedidos.pedidos_totales:
                    # Despertar a todos los que estén esperando
                    GeneradorPedidos.todos_generados = True
                    GeneradorPedidos.evento_pedido.set()
                    print(f"\n  {self.name} ha terminado su turno")
                    return


def main():
    generador = GeneradorPedidos()

    trabajadores = []
    nombres = ["Trabajador-Ana", "Trabajador-Pedro", "Trabajador-Lucía",
               "Trabajador-Carlos", "Trabajador-María"]

    for nombre in nombres:
        trabajador = Trabajador(nombre)
        trabajadores.append(trabajador)

    # Iniciar los trabajadores
    for t in trabajadores:
        t.start()

    # Esperar a que todos estén listos
    Trabajador.barrera.wait()
    print("\n¡Todos los trabajadores están listos! Comienza la jornada.\n")

    # Iniciar el generador de pedidos
    generador.start()

    for t in trabajadores:
        t.join()

    print(f"\nJornada terminada. Pedidos completados: {Trabajador.pedidos_completados}")


if __name__ == "__main__":
    main()
