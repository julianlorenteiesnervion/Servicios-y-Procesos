"""
EJERCICIO 1 - Examen Unidad 2 - Julián Lorente Marroco 2º DAM
"""

from multiprocessing import Process, Lock
from proceso1 import generar_temperaturas
from proceso2 import calcular_maxima
from proceso3 import calcular_minima
import os

if __name__ == '__main__':
    MES = 12       # Diciembre
    DIAS = 31      # 31 días en diciembre
    carpeta = os.path.dirname(os.path.abspath(__file__))

    # Limpiamos ficheros de resultados anteriores si existen
    for nombre in ("maximas.txt", "minimas.txt"):
        ruta = os.path.join(carpeta, nombre)
        if os.path.exists(ruta):
            os.remove(ruta)

    # Generamos los 31 ficheros de temperaturas de forma simultánea
    procesos_generacion = []
    for dia in range(1, DIAS + 1):
        p = Process(target=generar_temperaturas, args=(dia, MES))
        p.start()
        procesos_generacion.append(p)

    # Esperamos a que todos los ficheros estén escritos antes de continuar
    for p in procesos_generacion:
        p.join()

    print("Se han generado los 31 ficheros de temperaturas.")

    # Lanzamos simultáneamente los procesos de máximas y mínimas
    # Creamos un Lock para cada fichero compartido, se pasa a cada proceso
    # para que se asegure de que no hay conflictos al escribir en los ficheros maximas.txt y minimas.txt
    lock_max = Lock()
    lock_min = Lock()

    procesos_analisis = []
    for dia in range(1, DIAS + 1):
        # Proceso 2 – máximas
        p_max = Process(target=calcular_maxima, args=(dia, MES, lock_max))
        p_max.start()
        procesos_analisis.append(p_max)

        # Proceso 3 – mínimas
        p_min = Process(target=calcular_minima, args=(dia, MES, lock_min))
        p_min.start()
        procesos_analisis.append(p_min)

    # Esperamos a que terminen todos los procesos de análisis
    for p in procesos_analisis:
        p.join()

    print("Se han generado los ficheros maximas.txt y minimas.txt.")
