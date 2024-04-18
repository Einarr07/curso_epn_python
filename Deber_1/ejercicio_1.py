print("-------------------------------------------------")
print("|Este programa calcula el factorial de un número|")
print("-------------------------------------------------")


def calcular_el_factorial(num):
    resultado = 1
    for i in range(1, num + 1):
        resultado *= i
    return resultado


num = int(input("Ingrese el número para calcular su factorial: "))

print(f"El factorial de {num}, es: {calcular_el_factorial(num)}")
