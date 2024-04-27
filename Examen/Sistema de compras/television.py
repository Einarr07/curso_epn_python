from electrodomestico import Electrodomesticos


class Television(Electrodomesticos):
    def __init__(self, precio, marca, tamaño):
        super().__init__(precio, marca)
        self.tamaño = tamaño

    def __str__(self):
        return f"Televisión marca: {self.marca}\nTamaño: {self.tamaño}\nPrecio: {self.precio}"

