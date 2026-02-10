"""
Ejercicio 4: Filtrado de películas por año con multiprocessing
- Proceso 1: Lee un fichero de películas y envía las del año indicado
- Proceso 2: Recibe las películas y las guarda en un fichero peliculasXXXX.txt
"""

import multiprocessing
from multiprocessing.connection import Connection
import time
import os
from datetime import datetime

# Constantes
DIRECTORIO_BASE = os.path.dirname(__file__)
SENTINEL = "FIN"
ANIO_ACTUAL = datetime.now().year


# ============================================
# FUNCIONES DE UTILIDAD
# ============================================

def validar_anio(anio: str) -> bool:
    """Valida que el año sea un número válido y menor al actual."""
    try:
        anio_int = int(anio)
        return anio_int < ANIO_ACTUAL and anio_int > 1800
    except ValueError:
        return False


def parsear_linea_pelicula(linea: str) -> tuple:
    """Parsea una línea del fichero y devuelve (nombre, año)."""
    partes = linea.strip().split(';')
    if len(partes) == 2:
        nombre = partes[0].strip()
        try:
            anio = int(partes[1].strip())
            return (nombre, anio)
        except ValueError:
            return None
    return None


def obtener_ruta_fichero_salida(anio: int) -> str:
    """Obtiene la ruta del fichero de salida para un año."""
    return os.path.join(DIRECTORIO_BASE, f'peliculas{anio}.txt')


# ============================================
# PROCESO 1: FILTRAR PELÍCULAS POR AÑO
# ============================================

def leer_fichero_peliculas(ruta_fichero: str) -> list:
    """Lee el fichero de películas y devuelve una lista de tuplas (nombre, año)."""
    peliculas = []
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        for linea in f.readlines():
            pelicula = parsear_linea_pelicula(linea)
            if pelicula:
                peliculas.append(pelicula)
    return peliculas


def filtrar_peliculas_por_anio(peliculas: list, anio: int) -> list:
    """Filtra las películas por el año indicado."""
    return [p for p in peliculas if p[1] == anio]


def proceso_1_filtrar_peliculas(ruta_fichero: str, anio: int,
                                 pipe_salida: Connection):
    """
    Proceso 1: Lee el fichero de películas y envía las del año indicado.
    """
    print(f"[Proceso 1] Leyendo fichero: {ruta_fichero}")
    print(f"[Proceso 1] Filtrando películas del año: {anio}")
    
    peliculas = leer_fichero_peliculas(ruta_fichero)
    peliculas_filtradas = filtrar_peliculas_por_anio(peliculas, anio)
    
    print(f"[Proceso 1] Películas encontradas: {len(peliculas_filtradas)}")
    
    # Enviar cada película al proceso 2
    for nombre, anio_pelicula in peliculas_filtradas:
        print(f"[Proceso 1] Enviando: {nombre} ({anio_pelicula})")
        pipe_salida.send((nombre, anio_pelicula))
    
    # Enviar señal de finalización
    pipe_salida.send(SENTINEL)
    pipe_salida.close()
    print("[Proceso 1] Finalizado")


# ============================================
# PROCESO 2: GUARDAR PELÍCULAS EN FICHERO
# ============================================

def guardar_peliculas_en_fichero(peliculas: list, ruta_fichero: str):
    """Guarda las películas en un fichero."""
    with open(ruta_fichero, 'w', encoding='utf-8') as f:
        for nombre, anio in peliculas:
            f.write(f'{nombre};{anio}\n')


def proceso_2_guardar_peliculas(anio: int,
                                 pipe_entrada: Connection):
    """
    Proceso 2: Recibe las películas y las guarda en un fichero.
    """
    print(f"[Proceso 2] Esperando películas para guardar...")
    
    peliculas_recibidas = []
    
    while True:
        mensaje = pipe_entrada.recv()
        
        if mensaje == SENTINEL:
            break
        
        nombre, anio_pelicula = mensaje
        peliculas_recibidas.append((nombre, anio_pelicula))
        print(f"[Proceso 2] Recibida: {nombre}")
    
    pipe_entrada.close()
    
    # Guardar las películas en el fichero
    if peliculas_recibidas:
        ruta_salida = obtener_ruta_fichero_salida(anio)
        guardar_peliculas_en_fichero(peliculas_recibidas, ruta_salida)
        imprimir_resultado(peliculas_recibidas, ruta_salida, anio)
    else:
        print(f"\n[Proceso 2] No se encontraron películas del año {anio}")
    
    print("[Proceso 2] Finalizado")


def imprimir_resultado(peliculas: list, ruta_fichero: str, anio: int):
    """Imprime el resultado final."""
    print("\n" + "=" * 60)
    print(f"PELÍCULAS DEL AÑO {anio}")
    print("=" * 60)
    
    for nombre, _ in peliculas:
        print(f"  • {nombre}")
    
    print("-" * 60)
    print(f"  Total: {len(peliculas)} películas")
    print(f"  Guardadas en: {ruta_fichero}")
    print("=" * 60)


# ============================================
# FUNCIONES PARA LA GESTIÓN DE PROCESOS
# ============================================

def crear_pipe():
    """Crea un pipe para comunicación entre procesos."""
    return multiprocessing.Pipe(duplex=False)


def crear_procesos(ruta_fichero: str, anio: int, pipe_recv, pipe_send):
    """Crea los dos procesos."""
    p1 = multiprocessing.Process(
        target=proceso_1_filtrar_peliculas,
        args=(ruta_fichero, anio, pipe_send)
    )
    
    p2 = multiprocessing.Process(
        target=proceso_2_guardar_peliculas,
        args=(anio, pipe_recv)
    )
    
    return p1, p2


def solicitar_anio() -> int:
    """Solicita al usuario un año válido."""
    while True:
        anio_str = input(f"Introduce un año (menor a {ANIO_ACTUAL}): ")
        
        if validar_anio(anio_str):
            return int(anio_str)
        else:
            print(f"Error: Introduce un año válido menor a {ANIO_ACTUAL}")


def solicitar_ruta_fichero() -> str:
    """Solicita al usuario la ruta del fichero de películas."""
    while True:
        ruta = input("Introduce la ruta del fichero de películas (Enter para usar por defecto): ").strip()
        
        if ruta == "":
            ruta_defecto = os.path.join(DIRECTORIO_BASE, 'peliculas.txt')
            if os.path.exists(ruta_defecto):
                print(f"Usando fichero por defecto: {ruta_defecto}")
                return ruta_defecto
            else:
                print(f"Error: No se encontró el fichero por defecto: {ruta_defecto}")
        elif os.path.exists(ruta):
            return ruta
        else:
            print(f"Error: No se encontró el fichero: {ruta}")


# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def main():
    """Función principal del programa."""
    print("=" * 60)
    print("EJERCICIO 4: FILTRADO DE PELÍCULAS POR AÑO")
    print("=" * 60)
    
    # Solicitar datos al usuario
    ruta_fichero = solicitar_ruta_fichero()
    anio = solicitar_anio()
    
    print(f"\nProcesando películas del año {anio}...")
    print("-" * 60)
    
    # Medir tiempo de ejecución
    tiempo_inicio = time.time()
    
    # Crear pipe para comunicación
    pipe_recv, pipe_send = crear_pipe()
    
    # Crear procesos
    p1, p2 = crear_procesos(ruta_fichero, anio, pipe_recv, pipe_send)
    
    # Iniciar procesos
    p1.start()
    p2.start()
    
    # Cerrar extremos del pipe en el proceso principal
    pipe_send.close()
    pipe_recv.close()
    
    # Esperar a que terminen
    p1.join()
    p2.join()
    
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    
    print(f"\nTiempo total de ejecución: {tiempo_total:.4f} segundos")


if __name__ == '__main__':
    main()
