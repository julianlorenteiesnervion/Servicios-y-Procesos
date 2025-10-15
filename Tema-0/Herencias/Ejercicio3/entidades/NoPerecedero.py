from .Producto import *

class NoPerecedero(Producto):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def calcular(self, cantidad):
        return self.precio * cantidad