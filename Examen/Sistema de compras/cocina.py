from electrodomestico import Electrodomesticos


class Cocina(Electrodomesticos):
    def __init__(self, precio, marca, numero_hornillas, tipo):
        super().__init__(precio, marca)
        self.numero_hornillas = numero_hornillas
        self.tipo = tipo

    def __str__(self):
        return (f"Televisión marca: {self.marca}\nNúmero de hornillas: {self.numero_hornillas}\n"
                f"Tipo: {self.tipo}\nPrecio: {self.precio}")