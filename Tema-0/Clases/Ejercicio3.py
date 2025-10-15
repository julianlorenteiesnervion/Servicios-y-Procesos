from math import sqrt

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setXY(self, x, y):
        self.x = x
        self.y = y

    def desplaza(self, dx, dy):
        self.x += dx
        self.y += dy

    def distancia(self, otro_punto):
        return sqrt((self.x - otro_punto.x) ** 2 + (self.y - otro_punto.y) ** 2)

    def __str__(self):
        return f"({self.x}, {self.y})"

def main():
    p1 = Punto(3, 4)
    p2 = Punto(0, 0)

    print(f"Punto 1: {p1}")
    print(f"Punto 2: {p2}")

    distancia_inicial = p1.distancia(p2)
    print(f"Distancia inicial entre p1 y p2: {distancia_inicial}")

    p1.desplaza(1, -1)
    print(f"Punto 1 después de desplazar: {p1}")

    distancia_final = p1.distancia(p2)
    print(f"Distancia final entre p1 y p2: {distancia_final}")

if __name__ == "__main__":
    main()