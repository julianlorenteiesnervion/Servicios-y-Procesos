class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __str__(self):
        return f"Empleado {self.nombre}"
    
class Operario(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " -> Operario"
    
class Directivo(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " -> Directivo"
    
class Oficial(Operario):
    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " -> Oficial"
    
class Tecnico(Operario):
    def __init__(self, nombre):
        super().__init__(nombre)

    def __str__(self):
        return super().__str__() + " -> Técnico"
    
def main():
    empleados = [
        Empleado("Rafa"),
        Directivo("Mario"),
        Operario("Alfonso"),
        Oficial("Luis"),
        Tecnico("Pablo")
    ]

    for empleado in empleados:
        print(empleado)

if __name__ == "__main__":
    main()