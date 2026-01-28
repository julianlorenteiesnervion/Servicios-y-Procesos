import multiprocessing
from multiprocessing import Process, Pipe


def sum_between(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    n = b - a + 1
    return (n * (a + b)) // 2


def reader(conn, filename: str) -> None:
    """Lee pares de números desde `filename` y los envía por la pipe.
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
            conn.send((a, b))
    conn.send(None)
    conn.close()


def worker(conn) -> None:
    """Recibe pares de la pipe y calcula la suma hasta recibir `None`."""
    while True:
        item = conn.recv()
        if item is None:
            break
        a, b = item
        result = sum_between(a, b)
        print(f"{multiprocessing.current_process().name}: suma entre {a} y {b} = {result}")
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    filename = 'Tema-2/ejercicios/ejercicio8/numeros.txt'

    p_reader = Process(target=reader, args=(parent_conn, filename), name='Lector')
    p_worker = Process(target=worker, args=(child_conn,), name='Sumador')

    p_reader.start()
    p_worker.start()

    p_reader.join()
    p_worker.join()

    print('Comunicación por tuberías finalizada.')