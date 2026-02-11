"""
Proceso 3: Lee las temperaturas de un fichero DD-MM.txt y escribe en minimas.txt
la fecha y la temperatura mínima separadas por dos puntos (:).

Parámetros de entrada:
- dia (int): número del día.
- mes (int): número del mes.
- lock (Lock): lock compartido entre procesos para escritura segura en minimas.txt.
"""

import os
from multiprocessing import Lock


def calcular_minima(dia: int, mes: int, lock: Lock) -> None:
    carpeta = os.path.dirname(os.path.abspath(__file__))
    nombre_fichero = f"{dia:02d}-{mes:02d}.txt"
    ruta_lectura = os.path.join(carpeta, nombre_fichero)
    ruta_minimas = os.path.join(carpeta, "minimas.txt")

    # Leemos todas las temperaturas del fichero del día
    with open(ruta_lectura, 'r', encoding='utf-8') as f:
        temperaturas = [float(linea.strip()) for linea in f if linea.strip()]

    # Obtenemos la temperatura mínima
    temp_minima = min(temperaturas)
    fecha = f"{dia:02d}-{mes:02d}"

    # Escribimos en minimas.txt de forma segura con Lock
    with lock:
        with open(ruta_minimas, 'a', encoding='utf-8') as f:
            f.write(f"{fecha}:{temp_minima}\n")
