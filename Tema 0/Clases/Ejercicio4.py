class Articulo:

    IVA = 21

    def __init__(self, nombre, precio, cuantos_quedan):
        self.nombre = nombre
        self.precio = precio
        self.cuantos_quedan = cuantos_quedan

    def get_pvp(self):
        return self.precio * (1 + Articulo.IVA / 100)
    
    def get_pvp_con_descuento(self, descuento):
        return self.get_pvp() * (1 - descuento / 100)

    def vender(self, cantidad):
        result = False

        if self.cuantos_quedan >= cantidad:
            self.cuantos_quedan -= cantidad
            result = True
        
        return result

    def almacenar(self, cantidad):
        self.cuantos_quedan += cantidad

    def __str__(self):
        return f"Artículo: {self.nombre}, Precio: {self.precio}€, IVA: {Articulo.IVA}%, Stock: {self.cuantos_quedan}"
    
    def __eq__(self, other):
        return self.nombre == other.nombre
    
    def __lt__(self, other):
        return self.nombre < other.nombre

def main():
    articulo1 = Articulo("Camiseta", 20, 100)
    articulo2 = Articulo("Pantalón", 40, 50)

    print(articulo1)
    print(articulo2)

    print(f"PVP Camiseta: {articulo1.get_pvp()}€")
    print(f"PVP Pantalón con 10% de descuento: {articulo2.get_pvp_con_descuento(10)}€")

    if articulo1.vender(10):
        print("Venta de 10 camisetas realizada.")
    else:
        print("No hay suficiente stock para vender 10 camisetas.")

    articulo2.almacenar(20)
    print(f"Nuevo stock de pantalones: {articulo2.cuantos_quedan}")

    print(f"¿Son iguales los artículos? {'Sí' if articulo1 == articulo2 else 'No'}")
    print(f"¿Camiseta es menor que Pantalón? {'Sí' if articulo1 < articulo2 else 'No'}")

if __name__ == "__main__":
    main()