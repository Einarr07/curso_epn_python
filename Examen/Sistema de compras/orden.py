from datetime import datetime
from television import Television
from lavadora import Lavadora
from cocina import Cocina


class Orden:
    def __init__(self, nombre_cliente):
        self.nombre_cliente = nombre_cliente
        self.fecha_creacion = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.productos = []

    def añadir_producto(self, producto, cantidad):
        self.productos.append({"producto": producto, "cantidad": cantidad})

    def total(self):
        total = 0
        for item in self.productos:
            total += item["producto"].precio * item["cantidad"]
        return total

    def imprimir_recibo(self):
        print("***************************************************")
        print(f"fecha: {self.fecha_creacion}")
        print(f"Nombre cliente: {self.nombre_cliente}")
        print("************************************************")
        print("Producto \t\t\t\t Cantidad")
        print("************************************************")
        for item in self.productos:
            print(f"{str(item['producto'])} \t\t\t\t {item['cantidad']}")
        print("************************************************")
        print(f"Total \t\t\t\t\t {self.total()}")


televisor1 = Television(200, "LG", 32)
lavadora1 = Lavadora(800, "Samsung", 22)
cocina1 = Cocina(500, "LG", 4, "electrica")

orden = Orden("879 Congo")
orden.añadir_producto(televisor1, 2)
orden.añadir_producto(lavadora1, 1)
orden.añadir_producto(cocina1, 3)
orden.imprimir_recibo()

