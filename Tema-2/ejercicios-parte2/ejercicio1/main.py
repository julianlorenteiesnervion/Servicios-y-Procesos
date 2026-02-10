"""
Ejercicio 1: Contador de vocales con multiprocessing
Crea un proceso que cuente las vocales de un fichero de texto.
Lanza el proceso de forma paralela para las 5 vocales.
"""

import multiprocessing
import time
import os

# Constantes
VOCALES = ['a', 'e', 'i', 'o', 'u']
FICHERO_TEXTO = os.path.join(os.path.dirname(__file__), 'texto.txt')


def leer_fichero(ruta: str) -> str:
    """Lee el contenido de un fichero y lo devuelve en minúsculas."""
    with open(ruta, 'r', encoding='utf-8') as f:
        return f.read().lower()


def contar_vocal(vocal: str, ruta_fichero: str, resultado: multiprocessing.Queue):
    """
    Cuenta las ocurrencias de una vocal en un fichero.
    Guarda el resultado en la cola compartida.
    """
    contenido = leer_fichero(ruta_fichero)
    cantidad = contenido.count(vocal)
    resultado.put((vocal, cantidad))


def crear_procesos(vocales: list, ruta_fichero: str, cola_resultados: multiprocessing.Queue) -> list:
    """Crea un proceso por cada vocal."""
    procesos = []
    for vocal in vocales:
        proceso = multiprocessing.Process(
            target=contar_vocal,
            args=(vocal, ruta_fichero, cola_resultados)
        )
        procesos.append(proceso)
    return procesos


def iniciar_procesos(procesos: list):
    """Inicia todos los procesos."""
    for proceso in procesos:
        proceso.start()


def esperar_procesos(procesos: list):
    """Espera a que todos los procesos terminen."""
    for proceso in procesos:
        proceso.join()


def obtener_resultados(cola: multiprocessing.Queue, cantidad: int) -> dict:
    """Obtiene los resultados de la cola y los devuelve como diccionario."""
    resultados = {}
    for _ in range(cantidad):
        vocal, cantidad_vocal = cola.get()
        resultados[vocal] = cantidad_vocal
    return resultados


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
    """Función principal del programa."""
    print("Iniciando conteo de vocales con multiprocessing...")
    print(f"Fichero: {FICHERO_TEXTO}")
    
    # Crear cola para resultados
    cola_resultados = multiprocessing.Queue()
    
    # Medir tiempo de ejecución
    tiempo_inicio = time.time()
    
    # Crear, iniciar y esperar procesos
    procesos = crear_procesos(VOCALES, FICHERO_TEXTO, cola_resultados)
    iniciar_procesos(procesos)
    esperar_procesos(procesos)
    
    # Obtener y mostrar resultados
    resultados = obtener_resultados(cola_resultados, len(VOCALES))
    
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    
    imprimir_resultados(resultados)
    print(f"\nTiempo de ejecución: {tiempo_total:.4f} segundos")


if __name__ == '__main__':
    main()
