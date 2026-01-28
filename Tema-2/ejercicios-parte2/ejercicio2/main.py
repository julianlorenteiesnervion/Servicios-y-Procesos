"""
Ejercicio 2: Procesos encadenados con IPs
- Proceso 1: Genera 10 direcciones IP aleatorias
- Proceso 2: Filtra las IPs de clase A, B o C
- Proceso 3: Imprime las IPs filtradas con su clase
"""

import multiprocessing
from multiprocessing.connection import Connection
import random
import time

# Constantes
CANTIDAD_IPS = 10
SENTINEL = "FIN"


# ============================================
# FUNCIONES DE UTILIDAD PARA IPs
# ============================================

def generar_octeto() -> int:
    """Genera un octeto aleatorio (0-255)."""
    return random.randint(0, 255)


def generar_ip() -> str:
    """Genera una dirección IP aleatoria."""
    octetos = [generar_octeto() for _ in range(4)]
    return '.'.join(map(str, octetos))


def obtener_primer_octeto(ip: str) -> int:
    """Obtiene el primer octeto de una IP."""
    return int(ip.split('.')[0])


def es_clase_a(primer_octeto: int) -> bool:
    """Verifica si la IP es de clase A (1-126)."""
    return 1 <= primer_octeto <= 126


def es_clase_b(primer_octeto: int) -> bool:
    """Verifica si la IP es de clase B (128-191)."""
    return 128 <= primer_octeto <= 191


def es_clase_c(primer_octeto: int) -> bool:
    """Verifica si la IP es de clase C (192-223)."""
    return 192 <= primer_octeto <= 223


def obtener_clase_ip(ip: str) -> str:
    """Determina la clase de una IP."""
    primer_octeto = obtener_primer_octeto(ip)
    
    if es_clase_a(primer_octeto):
        return 'A'
    elif es_clase_b(primer_octeto):
        return 'B'
    elif es_clase_c(primer_octeto):
        return 'C'
    else:
        return 'Otra'


def es_ip_valida_abc(ip: str) -> bool:
    """Verifica si la IP pertenece a clase A, B o C."""
    clase = obtener_clase_ip(ip)
    return clase in ['A', 'B', 'C']


# ============================================
# PROCESOS
# ============================================

def proceso_1_generar_ips(pipe_salida: Connection):
    """
    Proceso 1: Genera 10 direcciones IP aleatorias y las envía al Proceso 2.
    """
    print("[Proceso 1] Generando IPs aleatorias...")
    
    for i in range(CANTIDAD_IPS):
        ip = generar_ip()
        print(f"[Proceso 1] IP generada #{i+1}: {ip}")
        pipe_salida.send(ip)
    
    # Enviar señal de finalización
    pipe_salida.send(SENTINEL)
    pipe_salida.close()
    print("[Proceso 1] Finalizado")


def proceso_2_filtrar_ips(pipe_entrada: Connection, pipe_salida: Connection):
    """
    Proceso 2: Filtra las IPs de clase A, B o C y las envía al Proceso 3.
    """
    print("[Proceso 2] Filtrando IPs de clase A, B, C...")
    
    while True:
        ip = pipe_entrada.recv()
        
        if ip == SENTINEL:
            break
            
        if es_ip_valida_abc(ip):
            clase = obtener_clase_ip(ip)
            print(f"[Proceso 2] IP válida: {ip} (Clase {clase})")
            pipe_salida.send(ip)
        else:
            print(f"[Proceso 2] IP descartada: {ip}")
    
    # Enviar señal de finalización
    pipe_salida.send(SENTINEL)
    pipe_entrada.close()
    pipe_salida.close()
    print("[Proceso 2] Finalizado")


def proceso_3_imprimir_ips(pipe_entrada: Connection):
    """
    Proceso 3: Imprime las IPs recibidas junto con su clase.
    """
    print("[Proceso 3] Esperando IPs para imprimir...")
    
    ips_recibidas = []
    
    while True:
        ip = pipe_entrada.recv()
        
        if ip == SENTINEL:
            break
            
        clase = obtener_clase_ip(ip)
        ips_recibidas.append((ip, clase))
    
    pipe_entrada.close()
    
    # Imprimir resultados finales
    imprimir_resultados_ips(ips_recibidas)
    print("[Proceso 3] Finalizado")


def imprimir_resultados_ips(ips: list):
    """Imprime los resultados de las IPs de forma formateada."""
    print("\n" + "=" * 50)
    print("DIRECCIONES IP DE CLASE A, B, C")
    print("=" * 50)
    
    if not ips:
        print("  No se encontraron IPs de clase A, B o C")
    else:
        for ip, clase in ips:
            print(f"  {ip:<20} -> Clase {clase}")
    
    print("-" * 50)
    print(f"  Total de IPs válidas: {len(ips)}")
    print("=" * 50)


# ============================================
# FUNCIÓN PRINCIPAL
# ============================================

def crear_pipes():
    """Crea los pipes para comunicación entre procesos."""
    # Pipe entre Proceso 1 y Proceso 2
    pipe_1_2_recv, pipe_1_2_send = multiprocessing.Pipe(duplex=False)
    
    # Pipe entre Proceso 2 y Proceso 3
    pipe_2_3_recv, pipe_2_3_send = multiprocessing.Pipe(duplex=False)
    
    return pipe_1_2_recv, pipe_1_2_send, pipe_2_3_recv, pipe_2_3_send


def crear_procesos_encadenados(pipe_1_2_recv, pipe_1_2_send, pipe_2_3_recv, pipe_2_3_send):
    """Crea los tres procesos encadenados."""
    p1 = multiprocessing.Process(
        target=proceso_1_generar_ips,
        args=(pipe_1_2_send,)
    )
    
    p2 = multiprocessing.Process(
        target=proceso_2_filtrar_ips,
        args=(pipe_1_2_recv, pipe_2_3_send)
    )
    
    p3 = multiprocessing.Process(
        target=proceso_3_imprimir_ips,
        args=(pipe_2_3_recv,)
    )
    
    return p1, p2, p3


def main():
    """Función principal del programa."""
    print("=" * 50)
    print("EJERCICIO 2: PROCESOS ENCADENADOS CON IPs")
    print("=" * 50)
    
    # Medir tiempo de ejecución
    tiempo_inicio = time.time()
    
    # Crear pipes para comunicación
    pipe_1_2_recv, pipe_1_2_send, pipe_2_3_recv, pipe_2_3_send = crear_pipes()
    
    # Crear procesos
    p1, p2, p3 = crear_procesos_encadenados(
        pipe_1_2_recv, pipe_1_2_send,
        pipe_2_3_recv, pipe_2_3_send
    )
    
    # Lanzar procesos en orden
    print("\nIniciando procesos...\n")
    p1.start()
    p2.start()
    p3.start()
    
    # Cerrar los extremos de los pipes en el proceso principal
    pipe_1_2_send.close()
    pipe_1_2_recv.close()
    pipe_2_3_send.close()
    pipe_2_3_recv.close()
    
    # Esperar a que terminen todos los procesos
    p1.join()
    p2.join()
    p3.join()
    
    tiempo_fin = time.time()
    tiempo_total = tiempo_fin - tiempo_inicio
    
    print(f"\nTiempo total de ejecución: {tiempo_total:.4f} segundos")


if __name__ == '__main__':
    main()
