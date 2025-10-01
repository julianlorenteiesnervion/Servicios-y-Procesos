# Clase CuentaCorriente
# Atributos: dni, nombre, saldo
class CuentaCorriente:
    # Constructores
    def __init__(self, dni, saldo):
        self.dni = dni
        self.nombre = ""
        self.saldo = saldo

    def __init__(self, dni, nombre, saldo):
        self.dni = dni
        self.nombre = nombre
        self.saldo = saldo

    # Métodos
    # Método para sacar dinero
    # Devuelve True si se ha podido sacar el dinero, False en caso contrario
    def sacar_dinero(self, dinero):
        result = False

        if (dinero <= self.saldo):
            self.saldo -= dinero
            result = True

        return result
    
    # Método para ingresar dinero
    def ingresar_dinero(self, dinero):
        self.saldo += dinero

    # Método para mostrar los datos de la cuenta
    def __str__(self):
        return f"DNI: {self.dni}, Nombre: {self.nombre}, Saldo: {self.saldo}"
    
    # Métodos para comparar la igualdad de dos cuentas por DNI
    def __eq__(self, other):
        return self.dni == other.dni
    
    # Método para comparar el orden de dos cuentas por DNI
    def __lt__(self, other):
        return self.dni < other.dni
    
def main():
    # Crear dos cuentas
    cuenta1 = CuentaCorriente("12345678A", "Juan Pérez", 1000)
    cuenta2 = CuentaCorriente("87654321B", "María Gómez", 500)

    # Mostrar las cuentas
    print(cuenta1)
    print(cuenta2)

    # Ingresar dinero en la cuenta1
    cuenta1.ingresar_dinero(200)
    print("Después de ingresar 200 en cuenta1:")
    print(cuenta1)

    # Sacar dinero de la cuenta2
    if cuenta2.sacar_dinero(600):
        print("Después de sacar 600 de cuenta2:")
    else:
        print("No se pudo sacar 600 de cuenta2 (saldo insuficiente).")
    print(cuenta2)

    # Comparar las cuentas
    if cuenta1 == cuenta2:
        print("Las cuentas son iguales.")
    else:
        print("Las cuentas son diferentes.")

    if cuenta1 < cuenta2:
        print("Cuenta1 es menor que Cuenta2.")
    else:
        print("Cuenta1 no es menor que Cuenta2.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()