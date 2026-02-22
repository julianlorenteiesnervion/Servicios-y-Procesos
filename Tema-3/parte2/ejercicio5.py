"""
Ejercicio 5: Estudiantes y Libros
4 estudiantes comparten 9 libros. Cada estudiante selecciona 2 libros al azar.
Si alguno de los dos no está libre, espera hasta que se libere.
Los usa durante 3-5 segundos y luego los devuelve a la vez.
Se usa Semaphore(9) para controlar los libros disponibles y Lock para la selección.
"""

import threading
import time
import random

LIBROS = [f"Libro-{i + 1}" for i in range(9)]


class Estudiante(threading.Thread):

    lock = threading.Lock()
    libros_disponibles = list(range(9))  # Índices de libros disponibles

    def __init__(self, nombre: str):
        super().__init__(name=nombre)

    def coger_libros(self) -> list:
        """Intenta coger 2 libros. Espera si no hay suficientes disponibles."""
        while True:
            with Estudiante.lock:
                if len(Estudiante.libros_disponibles) >= 2:
                    libros_elegidos = random.sample(Estudiante.libros_disponibles, 2)
                    for libro in libros_elegidos:
                        Estudiante.libros_disponibles.remove(libro)
                    return libros_elegidos
            # Si no hay suficientes libros, espera un poco y reintenta
            time.sleep(0.1)

    def devolver_libros(self, libros: list):
        """Devuelve los 2 libros a la vez."""
        with Estudiante.lock:
            for libro in libros:
                Estudiante.libros_disponibles.append(libro)

    def run(self):
        libros = self.coger_libros()
        nombres_libros = [LIBROS[i] for i in libros]
        print(f"{self.name} ha cogido: {nombres_libros[0]} y {nombres_libros[1]}")

        tiempo = random.randint(3, 5)
        time.sleep(tiempo)

        self.devolver_libros(libros)
        print(f"{self.name} ha devuelto: {nombres_libros[0]} y {nombres_libros[1]} ({tiempo}s de uso)")


def main():
    nombres = ["Estudiante-Ana", "Estudiante-Pedro", "Estudiante-Lucía", "Estudiante-Carlos"]

    hilos = []
    for nombre in nombres:
        hilo = Estudiante(nombre)
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("\nTodos los estudiantes han utilizado sus libros.")


if __name__ == "__main__":
    main()
