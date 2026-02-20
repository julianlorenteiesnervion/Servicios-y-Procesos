"""
Ejercicio 4: Cuenta vocales con hilos
"""

import threading
import os

VOCALES = ['a', 'e', 'i', 'o', 'u']
FICHERO_TEXTO = os.path.join(os.path.dirname(__file__), 'texto.txt')


class HiloContadorVocales(threading.Thread):

    resultados = {}

    def __init__(self, vocal: str, contenido: str):
        super().__init__(name=f"Hilo-{vocal}")
        self.vocal = vocal
        self.contenido = contenido

    def run(self):
        cantidad = self.contenido.count(self.vocal)
        HiloContadorVocales.resultados[self.vocal] = cantidad
        print(f"{self.name}: la vocal '{self.vocal}' aparece {cantidad} veces")


def leer_fichero(ruta: str) -> str:
    """Lee el contenido de un fichero y lo devuelve en minúsculas."""
    with open(ruta, 'r', encoding='utf-8') as f:
        return f.read().lower()


def imprimir_resultados(resultados: dict):
    """Imprime los resultados de forma formateada."""
    print("\n" + "=" * 40)
    print("RESULTADOS DEL CONTEO DE VOCALES")
    print("=" * 40)
    total = 0
    for vocal in VOCALES:
        cantidad = resultados.get(vocal, 0)
        total += cantidad
        print(f"  Vocal '{vocal}': {cantidad} ocurrencias")
    print("-" * 40)
    print(f"  TOTAL: {total} vocales")
    print("=" * 40)


def main():
    contenido = leer_fichero(FICHERO_TEXTO)

    hilos = []
    for vocal in VOCALES:
        hilo = HiloContadorVocales(vocal, contenido)
        hilos.append(hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()

    imprimir_resultados(HiloContadorVocales.resultados)


if __name__ == "__main__":
    main()
