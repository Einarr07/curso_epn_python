piramide = int(input("Para generar una media piramide ingrese 1 número: "))

for i in range(piramide + 1):
    result = i * "*"
    print(result)

# Piramide completa
altura = int(input("\nPara generar una pirámide completa, ingrese la altura: "))

# Iterar sobre cada nivel de la pirámide
for i in range(1, altura + 1):
    # Calcular la cantidad de espacios en blanco necesarios en cada nivel
    espacios = " " * (altura - i)
    # Calcular la cantidad de asteriscos necesarios en cada nivel
    asteriscos = "*" * (2 * i - 1)
    # Imprimir la línea del nivel actual de la pirámide
    print(espacios + asteriscos)
