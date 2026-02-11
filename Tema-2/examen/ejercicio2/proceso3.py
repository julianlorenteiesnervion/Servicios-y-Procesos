"""
Proceso 3: Recibe líneas del Proceso 2 a través de un Pipe y las escribe
en el fichero empleados.txt con el formato: Apellido Nombre, Salario

Parámetros de entrada:
- conn_recepcion: extremo de lectura del Pipe desde el Proceso 2.
"""

import os


def escribir_empleados(conn_recepcion) -> None:
    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_fichero = os.path.join(carpeta, "empleados.txt")

    with open(ruta_fichero, 'w', encoding='utf-8') as f:
        while True:
            linea = conn_recepcion.recv()
            # Si recibimos None, es que el Proceso 2 ha terminado de enviar datos
            if linea is None:
                break
            # Formato recibido: Nombre;Apellido;Salario
            partes = linea.split(';')
            nombre = partes[0]
            apellido = partes[1]
            salario = partes[2]

            # Escribimos con el formato pedido: Apellido Nombre, Salario
            f.write(f"{apellido} {nombre}, {salario}\n")

    conn_recepcion.close()
