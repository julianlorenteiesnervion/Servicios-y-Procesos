# Métodos para la gestión del diccionario de productos
# Método para añadir un producto
def add_product(name):
    if name in products:
        result = False
    else:
        products[name] = 0
        result = True
    
    return result

# Método para vender x cantidad un producto
def sell_product(name, quantity):
    if name in products:
        products[name] += quantity
        result = True
    else:
        result = False
    
    return result

# Método para obtener las ventas de un producto
def get_sales(name):
    if name in products:
        sales = products[name]
    else:
        sales = -1
    
    return sales

# Diccionario para almacenar los productos
products = {}

# Programa principal
option = int(input("Seleccione una opción\n1. Añadir producto\n2. Vender producto\n3. Consultar ventas\n4. Salir\n"))

while option != 4:
    if option == 1:
        product_name = input("Ingrese el nombre del producto a añadir: ")

        if add_product(product_name):
            print(f"Producto '{product_name}' añadido correctamente.")

        else:
            print(f"El producto '{product_name}' ya existe.")
    
    elif option == 2:
        product_name = input("Ingrese el nombre del producto a vender: ")
        quantity = int(input("Ingrese la cantidad a vender: "))

        if sell_product(product_name, quantity):
            print(f"Se han vendido {quantity} unidades de '{product_name}'.")

        else:
            print(f"El producto '{product_name}' no existe.")
    
    elif option == 3:
        product_name = input("Ingrese el nombre del producto para consultar ventas: ")

        sales = get_sales(product_name)

        if sales != -1:
            print(f"Ventas totales de '{product_name}': {sales}")

        else:
            print(f"El producto '{product_name}' no existe.")
    
    else:
        print("Opción no válida. Intente de nuevo.")
    
    option = int(input("\nSeleccione una opción\n1. Añadir producto\n2. Vender producto\n3. Consultar ventas\n4. Salir\n"))

print("Saliendo del programa...")