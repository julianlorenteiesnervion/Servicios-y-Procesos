"""
Proceso 1: Lee el fichero salarios.txt y envía al Proceso 2 (a través de un Pipe)
las líneas cuyo departamento coincida con el departamento recibido.
Las líneas enviadas contienen toda la información MENOS el departamento.

Parámetros de entrada:
- departamento (str): nombre del departamento a filtrar.
- conn_envio: extremo de escritura del Pipe hacia el Proceso 2.

Solo recibe el departamento y la conexión del Pipe.
El nombre del fichero (salarios.txt) es fijo y conocido, no es necesario pasarlo.
Se envía None como centinela para indicar fin de datos.
"""

import os


def filtrar_por_departamento(departamento: str, conn_envio) -> None:
    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_fichero = os.path.join(carpeta, "salarios.txt")

    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            # Formato: Nombre;Apellido;Salario;Departamento
            partes = linea.split(';')
            # Comprobamos si el departamento de la línea coincide con el buscado
            if partes[3] == departamento:
                # Enviamos la línea sin el departamento: Nombre;Apellido;Salario
                linea_sin_depto = f"{partes[0]};{partes[1]};{partes[2]}"
                conn_envio.send(linea_sin_depto)

    # Centinela para indicar fin de datos
    conn_envio.send(None)
    conn_envio.close()
