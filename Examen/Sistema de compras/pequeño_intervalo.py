from television import Television
from lavadora import Lavadora
from cocina import Cocina

print("----------------------------------------------")
print("|Estos son los electrodomesticos en intervalo|")
print("----------------------------------------------")


televisor1 = Television(200,"LG",32)
televisor2 = Television(300, "Samsung",15)

lavadora1 = Lavadora(800, "Samsung", 22)
lavadora2 = Lavadora(650, "Whirlpool", 25)

cocina1 = Cocina(500, "LG", 4, "electrica")
cocina2 = Cocina(300, "GE", 4, "no electrica")

print(televisor1)
print("-----------")
print(televisor2)
print("-----------")
print(lavadora1)
print("-----------")
print(lavadora2)
print("-----------")
print(cocina1)
print("-----------")
print(cocina2)