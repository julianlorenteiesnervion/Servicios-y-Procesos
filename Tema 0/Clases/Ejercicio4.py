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
