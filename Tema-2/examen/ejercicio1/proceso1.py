"""
Proceso 1: Genera 24 temperaturas aleatorias entre 0 y 20 con dos decimales
y las escribe en un fichero con nombre DD-MM.txt.

Parámetros de entrada:
- dia (int): número del día (1-31).
- mes (int): número del mes (12 para diciembre).
"""

import random
import os


def generar_temperaturas(dia: int, mes: int) -> None:
    
    # Construimos el nombre del fichero con formato DD-MM.txt
    nombre_fichero = f"{dia:02d}-{mes:02d}.txt"

    # Obtenemos la ruta absoluta de la carpeta donde está este script
    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_fichero = os.path.join(carpeta, nombre_fichero)

    # Generamos 24 temperaturas aleatorias entre 0.00 y 20.00
    with open(ruta_fichero, 'w', encoding='utf-8') as f:
        for _ in range(24):
            temperatura = round(random.uniform(0, 20), 2)
            f.write(f"{temperatura}\n")
