from entidades.Producto import *
from entidades.Perecedero import *
from entidades.NoPerecedero import *

def main():
    """
    Función principal para probar las clases de productos.
    """

    # 1. Creamos una lista con varios productos de diferentes tipos
    lista_productos = [
        Perecedero("Leche", 1.20, 1),        # Con gran descuento (precio / 4)
        Perecedero("Yogur", 1.50, 2),        # Con descuento medio (precio / 3)
        Perecedero("Queso", 3.00, 3),         # Con descuento bajo (precio / 2)
        Perecedero("Pan de molde", 2.40, 10), # Sin descuento
        NoPerecedero("Arroz", 0.90, "Grano"),
        NoPerecedero("Lentejas", 1.10, "Legumbre")
    ]

    # 2. Calculamos el coste de comprar 5 unidades de cada producto
    cantidad_a_comprar = 5
    print(f"🛒 Calculando el coste de comprar {cantidad_a_comprar} unidades de cada producto:\n")

    total_compra = 0
    for producto in lista_productos:
        coste_producto = producto.calcular(cantidad_a_comprar)
        total_compra += coste_producto
        # Mostramos el cálculo para cada producto
        print(f"Producto: {producto.nombre} | Precio final por {cantidad_a_comprar} unidades: ${coste_producto:.2f}")

    print("-------------------------------------------------")
    print(f"💰 El coste total de la compra es: ${total_compra:.2f}\n")


    # 3. Demostración de los métodos __str__ y __lt__
    print("--- Demostración de otros métodos ---\n")
    
    prod1 = NoPerecedero("Sal", 0.75, "Condimento")
    prod2 = Perecedero("Manzanas", 2.10, 5)

    # Prueba de __str__ (se llama automáticamente con print)
    print(f"Impresión del objeto 1: {prod1}")
    print(f"Impresión del objeto 2: {prod2}\n")

    # Prueba de __lt__ (menor que)
    print(f"¿Es el precio de '{prod1.nombre}' menor que el de '{prod2.nombre}'? -> {prod1 < prod2}")
    print(f"¿Es el precio de '{prod2.nombre}' menor que el de '{prod1.nombre}'? -> {prod2 < prod1}")


# Punto de entrada para ejecutar el script
if __name__ == "__main__":
    main()