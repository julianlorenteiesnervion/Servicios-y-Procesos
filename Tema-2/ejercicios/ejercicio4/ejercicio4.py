from multiprocessing import Process, Pipe
import os


def lector(send_conn, filepath):
    """Lee números de un fichero y los envía por la tubería.
    Cuando termina envía None para indicar fin.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if not s:
                    continue
                try:
                    num = float(s) if ("." in s) else int(s)
                except ValueError:
                    # Ignorar líneas no numéricas
                    continue
                send_conn.send(num)
    finally:
        send_conn.send(None)
        send_conn.close()


def sumador(recv_conn):
    """Recibe números por la tubería y los suma hasta recibir None."""
    total = 0
    while True:
        n = recv_conn.recv()
        if n is None:
            break
        total += n
    recv_conn.close()
    print(f"Suma total: {total}")


if __name__ == "__main__":
    base = os.path.dirname(__file__)
    numeros_file = os.path.join(base, "numeros.txt")

    # Si no existe, crear un fichero de ejemplo
    if not os.path.exists(numeros_file):
        with open(numeros_file, "w", encoding="utf-8") as f:
            for i in range(1, 11):
                f.write(f"{i}\n")

    send_conn, recv_conn = Pipe()

    p_lector = Process(target=lector, args=(send_conn, numeros_file))
    p_sumador = Process(target=sumador, args=(recv_conn,))

    p_sumador.start()
    p_lector.start()

    p_lector.join()
    p_sumador.join()

    print("Procesos finalizados.")
