class Perecedero(Producto):
    def __init__(self, nombre, precio, dias_a_caducar):
        super().__init__(nombre, precio)
        self.dias_a_caducar = dias_a_caducar

    def calcular(self, cantidad):
        precio_final = self.precio

        if self.dias_a_caducar == 1:
            precio_final /= 4
        elif self.dias_a_caducar == 2:
            precio_final /= 3
        elif self.dias_a_caducar == 3:
            precio_final /= 2
        
        return precio_final * cantidad
