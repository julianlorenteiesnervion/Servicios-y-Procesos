"""
Proceso 2: Lee las temperaturas de un fichero DD-MM.txt y escribe en maximas.txt
la fecha y la temperatura máxima separadas por dos puntos (:).

Parámetros de entrada:
- dia (int): número del día.
- mes (int): número del mes.
- lock (Lock): lock compartido entre procesos para escritura segura en maximas.txt.
"""

import os
from multiprocessing import Lock


def calcular_maxima(dia: int, mes: int, lock: Lock) -> None:
    carpeta = os.path.dirname(os.path.abspath(__file__))
    nombre_fichero = f"{dia:02d}-{mes:02d}.txt"
    ruta_lectura = os.path.join(carpeta, nombre_fichero)
    ruta_maximas = os.path.join(carpeta, "maximas.txt")

    # Leemos todas las temperaturas del fichero del día
    with open(ruta_lectura, 'r', encoding='utf-8') as f:
        temperaturas = [float(linea.strip()) for linea in f if linea.strip()]

    # Obtenemos la temperatura máxima
    temp_maxima = max(temperaturas)
    fecha = f"{dia:02d}-{mes:02d}"

    # Escribimos en maximas.txt de forma segura con Lock
    with lock:
        with open(ruta_maximas, 'a', encoding='utf-8') as f:
            f.write(f"{fecha}:{temp_maxima}\n")
