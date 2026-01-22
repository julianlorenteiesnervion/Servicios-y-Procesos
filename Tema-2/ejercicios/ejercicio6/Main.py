import multiprocessing
from multiprocessing import Pool
from typing import List, Tuple


def sum_between(a: int, b: int) -> int:
    """Devuelve la suma de todos los enteros entre a y b (incluyendo ambos)."""
    if a > b:
        a, b = b, a
    n = b - a + 1
    return (n * (a + b)) // 2


def worker(a: int, b: int) -> str:
    """Calcula la suma y devuelve una línea con el resultado."""
    result = sum_between(a, b)
    return f"{multiprocessing.current_process().name}: suma entre {a} y {b} = {result}"


if __name__ == '__main__':
    # Pares a sumar; incluye un par con orden invertido
    ranges: List[Tuple[int, int]] = [(1, 10), (10, 1), (5, 5), (-3, 3)]

    # Crear un Pool y ejecutar los workers en paralelo usando starmap
    with Pool(processes=min(len(ranges), multiprocessing.cpu_count())) as pool:
        results = pool.starmap(worker, ranges)

    # Mostrar resultados en el proceso principal
    for line in results:
        print(line)

    print("Todos los procesos del pool han terminado.")
