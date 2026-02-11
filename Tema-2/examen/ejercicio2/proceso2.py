"""
Proceso 2: Recibe líneas del Proceso 1 a través de un Pipe y filtra aquellas
cuyo salario sea mayor o igual que el salario mínimo recibido.
Las líneas que cumplen la condición se envían al Proceso 3 por otro Pipe.

Parámetros de entrada:
- salario_minimo (int): salario mínimo para filtrar.
- conn_recepcion: extremo de lectura del Pipe desde el Proceso 1.
- conn_envio: extremo de escritura del Pipe hacia el Proceso 3.
"""


def filtrar_por_salario(salario_minimo: int, conn_recepcion, conn_envio) -> None:
    while True:
        linea = conn_recepcion.recv()
        # Si recibimos None, es que el Proceso 1 ha terminado de enviar datos
        if linea is None:
            break
        # Formato recibido: Nombre;Apellido;Salario
        partes = linea.split(';')
        salario = int(partes[2])

        # Solo enviamos al Proceso 3 si el salario cumple el mínimo
        if salario >= salario_minimo:
            conn_envio.send(linea)

    # Fin de datos
    conn_envio.send(None)
    conn_recepcion.close()
    conn_envio.close()
