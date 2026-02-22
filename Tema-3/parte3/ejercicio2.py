"""
Ejercicio 2: Escape Room
5 personas encerradas en una sala de Escape Room.
Deben adivinar un código de 4 cifras para abrir la puerta.
Una vez adivinado, deben juntarse los 5 para salir juntos.

Sincronización:
- Event() para señalizar que la clave ha sido adivinada.
- Barrier(5) para esperar a que todos estén juntos antes de salir.
- Lock() para proteger la escritura de quién ha acertado.
"""

import threading
import random
import time


class Persona(threading.Thread):

    codigo_secreto = random.randint(0, 9999)
    codigo_adivinado = threading.Event()
    barrera_salida = threading.Barrier(5)
    lock = threading.Lock()

    def __init__(self, nombre: str):
        super().__init__(name=nombre)
        self.ha_acertado = False

    def run(self):
        intentos = 0

        # Intentar adivinar el código hasta que alguien lo consiga
        while not Persona.codigo_adivinado.is_set():
            intento = random.randint(0, 9999)
            intentos += 1

            if intento == Persona.codigo_secreto:
                with Persona.lock:
                    if not Persona.codigo_adivinado.is_set():
                        Persona.codigo_adivinado.set()
                        self.ha_acertado = True
                        print(f"🔓 ¡{self.name} ha adivinado el código {intento:04d} en {intentos} intentos!")
                break

        if not self.ha_acertado:
            print(f"  {self.name} sabe que el código ha sido descubierto (hizo {intentos} intentos)")

        # Esperar a que todos estén juntos para salir
        print(f"  {self.name} está esperando al resto del grupo")
        Persona.barrera_salida.wait()
        print(f"  🚪 {self.name} ha salido de la sala")


def main():
    print(f"Código secreto generado: {Persona.codigo_secreto:04d}")
    print("-" * 50)

    nombres = ["Ana", "Pedro", "Lucía", "Carlos", "María"]

    hilos = []
    for nombre in nombres:
        hilo = Persona(nombre)
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("-" * 50)
    print("¡Todos han escapado de la sala!")


if __name__ == "__main__":
    main()
