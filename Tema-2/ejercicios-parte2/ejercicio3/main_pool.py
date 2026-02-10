"""
Ejercicio 3: Gestión de notas de alumnos con multiprocessing (versión Pool)
- Proceso 1: Genera 6 notas aleatorias y las guarda en un fichero
- Proceso 2: Lee las notas y calcula la media, guardándola en medias.txt
- Proceso 3: Lee medias.txt y obtiene la nota máxima con el alumno
"""

import multiprocessing
import random
import time
import os

# Constantes
CANTIDAD_ALUMNOS = 10
CANTIDAD_NOTAS = 6
NOTA_MIN = 1.0
NOTA_MAX = 10.0
DIRECTORIO_BASE = os.path.dirname(__file__)
FICHERO_MEDIAS = os.path.join(DIRECTORIO_BASE, 'medias.txt')
DIRECTORIO_NOTAS = os.path.join(DIRECTORIO_BASE, 'notas')


# ============================================
# FUNCIONES DE UTILIDAD
# ============================================

def crear_directorio_si_no_existe(directorio: str):
    """Crea un directorio si no existe."""
    if not os.path.exists(directorio):
        os.makedirs(directorio)


def generar_nota_aleatoria() -> float:
    """Genera una nota aleatoria entre 1 y 10 con decimales."""
    return round(random.uniform(NOTA_MIN, NOTA_MAX), 2)


def obtener_ruta_alumno(numero_alumno: int) -> str:
    """Obtiene la ruta del fichero de un alumno."""
    return os.path.join(DIRECTORIO_NOTAS, f'Alumno{numero_alumno}.txt')


def obtener_nombre_alumno(numero_alumno: int) -> str:
    """Obtiene el nombre del alumno."""
    return f'Alumno{numero_alumno}'


# ============================================
# PROCESO 1: GENERAR NOTAS
# ============================================

def generar_notas() -> list:
    """Genera una lista de notas aleatorias."""
    return [generar_nota_aleatoria() for _ in range(CANTIDAD_NOTAS)]


def guardar_notas_en_fichero(notas: list, ruta_fichero: str):
    """Guarda las notas en un fichero, una por línea."""
    with open(ruta_fichero, 'w', encoding='utf-8') as f:
        for nota in notas:
            f.write(f'{nota}\n')


def proceso_1_generar_notas(numero_alumno: int) -> str:
    """
    Proceso 1: Genera 6 notas aleatorias y las guarda en un fichero.
    Retorna la ruta del fichero creado.
    """
    ruta_fichero = obtener_ruta_alumno(numero_alumno)
    notas = generar_notas()
    guardar_notas_en_fichero(notas, ruta_fichero)
    print(f"[Proceso 1] Notas generadas para Alumno{numero_alumno}: {notas}")
    return ruta_fichero


# ============================================
# PROCESO 2: CALCULAR MEDIA
# ============================================

def leer_notas_de_fichero(ruta_fichero: str) -> list:
    """Lee las notas de un fichero."""
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        return [float(linea.strip()) for linea in f.readlines()]


def calcular_media(notas: list) -> float:
    """Calcula la media de una lista de notas."""
    return round(sum(notas) / len(notas), 2)


def proceso_2_calcular_media(args: tuple) -> tuple:
    """
    Proceso 2: Lee las notas de un fichero y calcula la media.
    Retorna una tupla (nombre_alumno, media).
    """
    ruta_fichero, nombre_alumno = args
    notas = leer_notas_de_fichero(ruta_fichero)
    media = calcular_media(notas)
    print(f"[Proceso 2] Media calculada para {nombre_alumno}: {media}")
    return (nombre_alumno, media)


def guardar_medias_en_fichero(medias: list, ruta_fichero: str):
    """Guarda las medias en un fichero."""
    with open(ruta_fichero, 'w', encoding='utf-8') as f:
        for nombre, media in medias:
            f.write(f'{media} {nombre}\n')
    print(f"[Proceso 2] Medias guardadas en {ruta_fichero}")


# ============================================
# PROCESO 3: OBTENER MÁXIMA
# ============================================

def leer_medias_de_fichero(ruta_fichero: str) -> list:
    """Lee las medias de un fichero. Formato: 'media nombre_alumno'"""
    medias = []
    with open(ruta_fichero, 'r', encoding='utf-8') as f:
        for linea in f.readlines():
            partes = linea.strip().split(' ')
            media = float(partes[0])
            nombre = partes[1]
            medias.append((nombre, media))
    return medias


def obtener_media_maxima(medias: list) -> tuple:
    """Obtiene la media máxima y el alumno correspondiente."""
    return max(medias, key=lambda x: x[1])


def proceso_3_obtener_maxima():
    """
    Proceso 3: Lee el fichero de medias y obtiene la nota máxima.
    """
    medias = leer_medias_de_fichero(FICHERO_MEDIAS)
    nombre, nota_maxima = obtener_media_maxima(medias)
    
    print("\n" + "=" * 50)
    print("RESULTADO FINAL")
    print("=" * 50)
    print(f"  Alumno con mejor media: {nombre}")
    print(f"  Nota media máxima: {nota_maxima}")
    print("=" * 50)


# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def limpiar_fichero_medias():
    """Limpia el fichero de medias si existe."""
    if os.path.exists(FICHERO_MEDIAS):
        os.remove(FICHERO_MEDIAS)


def main():
    """Función principal del programa usando Pool."""
    print("=" * 50)
    print("EJERCICIO 3: GESTIÓN DE NOTAS (VERSIÓN POOL)")
    print("=" * 50)
    
    # Preparar entorno
    crear_directorio_si_no_existe(DIRECTORIO_NOTAS)
    limpiar_fichero_medias()
    
    # Medir tiempo de ejecución
    tiempo_inicio = time.time()
    
    # ========================================
    # FASE 1: Generar notas (10 procesos concurrentes)
    # ========================================
    print("\n[FASE 1] Generando notas de alumnos...")
    
    with multiprocessing.Pool(processes=CANTIDAD_ALUMNOS) as pool:
        numeros_alumnos = list(range(1, CANTIDAD_ALUMNOS + 1))
        rutas_ficheros = pool.map(proceso_1_generar_notas, numeros_alumnos)
    
    # ========================================
    # FASE 2: Calcular medias (10 procesos concurrentes)
    # ========================================
    print("\n[FASE 2] Calculando medias...")
    
    # Preparar argumentos: (ruta_fichero, nombre_alumno)
    args_proceso_2 = [
        (obtener_ruta_alumno(i), obtener_nombre_alumno(i))
        for i in range(1, CANTIDAD_ALUMNOS + 1)
    ]
    
    with multiprocessing.Pool(processes=CANTIDAD_ALUMNOS) as pool:
        resultados_medias = pool.map(proceso_2_calcular_media, args_proceso_2)
    
    # Guardar todas las medias en el fichero
    guardar_medias_en_fichero(resultados_medias, FICHERO_MEDIAS)
    
    # ========================================
    # FASE 3: Obtener nota máxima
    # ========================================
    print("\n[FASE 3] Obteniendo nota máxima...")
    proceso_3_obtener_maxima()
    
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    
    print(f"\nTiempo total de ejecución: {tiempo_total:.4f} segundos")


if __name__ == '__main__':
    main()
