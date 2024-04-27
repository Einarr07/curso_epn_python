print("-------------------------------------------------")
print("|Este programa calcula el factorial de un número|")
print("-------------------------------------------------")


def calcular_el_factorial(num):
    try:
        if num >= 0:
            resultado = 1
            for i in range(1, num + 1):
                resultado *= i
            return resultado
        else:
            print("Solo puedes ingresar números positivos")
    except Exception as e:
        print("Solo puedes ingresar valores enteros positivos")
        print(f"Error: {e}")


while True:
    try:
        num = int(input("Ingrese el número para calcular su factorial: "))
        print(f"El factorial de {num}, es: {calcular_el_factorial(num)}")
        break
    except ValueError:
        print("Por favor, ingrese un valor entero.")
