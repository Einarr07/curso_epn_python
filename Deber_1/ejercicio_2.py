print("--------------------------------")
print("| Este programa calcula tu IMC |")
print("--------------------------------")


def imc(peso, altura, nombre):
    imc = round(peso / altura**2, 2)
    print(f"Tu IMC es: {imc}")
    if  imc < 18.5:
        print(f"{nombre}, tienes un peso menor al que deberías")
    elif 18.5 <= imc <= 24.9:
        print(f"{nombre}, tiense un peso saludable")
    elif 25 <= imc <= 29.9:
        print(f"{nombre}, tienes sobre peso, deberías comenzar con una dieta saludable")
    else:
        print(f"{nombre}, sufres de obesidad, visita un doctor")


nombre = input("Ingresa tu nombre: ")
peso = float(input("Ingrese su peso en KG: "))
altura = float(input("Ingrese su altura en metros: "))

imc(peso,altura, nombre)