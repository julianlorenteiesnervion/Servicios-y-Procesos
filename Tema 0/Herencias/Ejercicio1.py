# Clase padre Animal
class Animal:
    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas

    def habla(self):
        return ""
    
    def __str__(self):
        return f"Me llamo {self.nombre}, tengo {self.patas} patas y sueno así: {self.habla()}."

# Clase hija Gato
class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, 4)
    
    def habla(self):
        return "Miau"
    
    def __str__(self):
        return "Soy un gato. " + super().__str__()

# Clase hija Perro
class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, 4)
    
    def habla(self):
        return "Guau"
    
    def __str__(self):
        return "Soy un perro. " + super().__str__()

# Función principal para probar las clases
def main():
    gato = Gato("Michi")
    perro = Perro("Firulais")
    
    print(gato)
    print(perro)

if __name__ == "__main__":
    main()