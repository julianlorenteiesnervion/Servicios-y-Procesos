# Clase Libro con atributos y métodos para gestionar préstamos y devoluciones
class Libro:
    # Constructor de la clase
    def __init__(self, titulo, autor, ejemplares, ejemplares_prestados):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares = ejemplares
        self.ejemplares_prestados = ejemplares_prestados

    # Método para verificar si el libro es prestable
    def es_prestable(self):
        return self.ejemplares > self.ejemplares_prestados
    
    # Método para realizar un préstamo
    def prestamo(self):
        result = False

        if self.es_prestable():
            self.ejemplares_prestados += 1
            result = True
        
        return result
    
    # Método para realizar una devolución
    def devolucion(self):
        result = False

        if self.ejemplares_prestados > 0:
            self.ejemplares_prestados -= 1
            result = True
        
        return result
    
    # Métodos para imprimir y comparar libros
    def __str__(self):
        return f'Título: {self.titulo}, Autor: {self.autor}, Ejemplares: {self.ejemplares}, Ejemplares prestados: {self.ejemplares_prestados}'
    
    def __eq__(self, other):
        return self.titulo == other.titulo and self.autor == other.autor
    
    def __lt__(self, other):
        return self.autor < other.autor
    
# Función principal para probar la clase Libro
def main():
    libro1 = Libro("El Quijote", "Miguel de Cervantes", 5, 2)
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 3, 1)
    libro3 = Libro("El Quijote", "Miguel de Cervantes", 4, 0)

    print(libro1)
    print(libro2)

    print(f'¿Se puede prestar el libro1? {libro1.es_prestable()}')
    print(f'¿Se puede prestar el libro2? {libro2.es_prestable()}')

    print(f'Préstamo del libro1: {libro1.prestamo()}')
    print(f'Préstamo del libro2: {libro2.prestamo()}')

    print(libro1)
    print(libro2)

    print(f'Devolución del libro1: {libro1.devolucion()}')
    print(f'Devolución del libro2: {libro2.devolucion()}')

    print(libro1)
    print(libro2)

    print(f'¿El libro1 es igual al libro3? {libro1 == libro3}')
    print(f'¿El libro1 es menor que el libro2? {libro1 < libro2}')

# Ejecutar la función principal
if __name__ == "__main__":
    main()