import multiprocessing


def sum_between(a: int, b: int) -> int:
    """Devuelve la suma de todos los enteros entre a y b (incluyendo ambos)."""
    if a > b:
        a, b = b, a
    n = b - a + 1
    return (n * (a + b)) // 2


def worker(a: int, b: int) -> None:
    result = sum_between(a, b)
    print(f"{multiprocessing.current_process().name}: suma entre {a} y {b} = {result}")


if __name__ == '__main__':
    # Pares a sumar; incluye un par con orden invertido
    ranges = [(1, 10), (10, 1), (5, 5), (-3, 3)]

    processes = []
    for i, (a, b) in enumerate(ranges, start=1):
        p = multiprocessing.Process(target=worker, args=(a, b), name=f"P{i}")
        p.start()
        processes.append(p)

    # Esperar a que todos los procesos terminen
    for p in processes:
        p.join()

    print("Todos los procesos han terminado.")
