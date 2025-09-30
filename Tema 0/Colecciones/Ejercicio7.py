# Métodos para gestionar una agenda de contactos usando un diccionario
def addContact(name, phoneNumber):
    contacts[name] = phoneNumber

def getContact(name):
    return contacts.get(name, "Contacto no encontrado.")

def deleteContact(name):
    if name in contacts:
        del contacts[name]

# Diccionario para almacenar los contactos
contacts = {}

# Imprimimos el menú con las opciones disponibles
print("1. Añadir contacto\n2. Buscar contacto\n3. Eliminar contacto\n4. Salir")

option = input("Seleccione una opción (1-4): ")

while option != "4":

    if option == "1": # Añadir contacto
        name = input("Ingrese el nombre del contacto: ")

        phoneNumber = input("Ingrese el número de teléfono: ")

        addContact(name, phoneNumber)

        print(f"Contacto {name} añadido.")

    elif option == "2": # Buscar contacto
        name = input("Ingrese el nombre del contacto a buscar: ")

        print(getContact(name))

    elif option == "3": # Eliminar contacto
        name = input("Ingrese el nombre del contacto a eliminar: ")

        deleteContact(name)

        print(f"Contacto {name} eliminado.")

    elif option == "4": # Salir
        print("Saliendo del programa.")
    else: # Opción no válida
        print("Opción no válida. Por favor, intente de nuevo.")

    # Imprimimos el menú con las opciones disponibles
    print("1. Añadir contacto\n2. Buscar contacto\n3. Eliminar contacto\n4. Salir")

    option = input("Seleccione una opción (1-4): ")

print("Fin del programa.")