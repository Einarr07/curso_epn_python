def editor_de_texto():

    archivo_creado = input("Ingrese el nombre del archivo: ")
    print("----------------------------")
    print("|Archivo creado exitosamente|")
    print("----------------------------")

    print("Ya puedes escribir")
    print("Si deseas dejar de escribir, debes dejar 3 lineas en blanco, en otras palabras debes dar 3 enter")
    with open(archivo_creado, "w") as archivo:
        lineas_en_blanco = 0
        while True:
            linea = input()
            if not linea.strip():
                lineas_en_blanco += 1
            else:
                lineas_en_blanco = 0

            archivo.write(linea + "\n")

            if lineas_en_blanco >= 3:
                break

    print(f"El archivo '{archivo_creado}' ha sido creado o sobrescrito con el contenido ingresado.")


# Llamar a la función editor_de_texto
editor_de_texto()
