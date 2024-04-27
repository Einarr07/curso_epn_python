from electrodomestico import Electrodomesticos


class Lavadora(Electrodomesticos):
    def __init__(self, precio, marca, capacidad_carga):
        super().__init__(precio, marca)
        self.capacidad_carga = capacidad_carga

    def __str__(self):
        return f"Lavadora marca {self.marca}\nCapacidad de carga: {self.capacidad_carga}\nPrecio: {self.precio}"

