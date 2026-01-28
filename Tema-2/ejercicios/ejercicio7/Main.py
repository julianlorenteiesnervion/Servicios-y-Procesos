import multiprocessing
from multiprocessing import Process, Queue


def sum_between(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    n = b - a + 1
    return (n * (a + b)) // 2


def reader(queue: Queue, filename: str) -> None:
    """Lee pares de números desde `filename` y los pone en la cola.
    Envía `None` al final como centinela para indicar fin de datos.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            try:
                a = int(parts[0])
                b = int(parts[1])
            except ValueError:
                continue
            queue.put((a, b))
    queue.put(None)


def worker(queue: Queue) -> None:
    """Toma pares de la cola y calcula la suma hasta recibir `None`."""
    while True:
        item = queue.get()
        if item is None:
            break
        a, b = item
        result = sum_between(a, b)
        print(f"{multiprocessing.current_process().name}: suma entre {a} y {b} = {result}")


if __name__ == '__main__':
    q = Queue()
    filename = 'Tema-2/ejercicios/ejercicio7/numeros.txt'

    p_reader = Process(target=reader, args=(q, filename), name='Lector')
    p_worker = Process(target=worker, args=(q,), name='Sumador')

    p_reader.start()
    p_worker.start()

    p_reader.join()
    p_worker.join()

    print('Comunicación por colas finalizada.')
