"""
EJERCICIO 2 - Examen Unidad 2 - Julián Lorente Marroco 2º DAM

"""

from multiprocessing import Process, Pipe
from proceso1 import filtrar_por_departamento
from proceso2 import filtrar_por_salario
from proceso3 import escribir_empleados


if __name__ == '__main__':
    # Pedimos al usuario el departamento y el salario mínimo
    departamento = input("Introduce el nombre del departamento: ")
    salario_minimo = int(input("Introduce el salario mínimo: "))

    # Creamos los dos Pipes para la comunicación entre procesos
    # Pipe 1: Proceso 1 (envía) → Proceso 2 (recibe)
    conn1_recepcion, conn1_envio = Pipe()
    # Pipe 2: Proceso 2 (envía) → Proceso 3 (recibe)
    conn2_recepcion, conn2_envio = Pipe()

    # Lanzamos los procesos en orden inverso para que los receptores estén listos
    p3 = Process(target=escribir_empleados, args=(conn2_recepcion,))
    p2 = Process(target=filtrar_por_salario, args=(salario_minimo, conn1_recepcion, conn2_envio))
    p1 = Process(target=filtrar_por_departamento, args=(departamento, conn1_envio))

    p3.start()
    p2.start()
    p1.start()

    # Cerramos los extremos de los pipes que no usamos en el Main
    # para evitar que los procesos se queden bloqueados esperando datos
    conn1_envio.close()
    conn1_recepcion.close()
    conn2_envio.close()
    conn2_recepcion.close()

    # Esperamos a que terminen todos los procesos
    p1.join()
    p2.join()
    p3.join()

    print("Se ha generado el fichero empleados.txt correctamente.")
