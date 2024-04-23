import os
import datetime as dt

# Obteniendo el directorio actual
directorio_actual = os.getcwd()


# Función para escribir en el diario
def accion_escribir():
    # Obtiene la fecha y hora actual
    fecha_y_hora_actual = dt.datetime.now()
    # Genera un nombre de archivo único basado en la fecha y la hora actual
    archivos_txt = fecha_y_hora_actual.strftime("%Y_%m_%d-%H_%M_%S") + ".txt"
    # Abre el archivo en modo de escritura
    with open(archivos_txt, "w", encoding="UTF-8") as archivo:
        while True:
            escribir = input("Ingrese una linea de texto (escriba 'salir' para terminar): ")
            if escribir.lower() == "salir":
                break
            else:
                # Escribe la línea de texto en el archivo
                archivo.write(escribir + "\n")


# Función para leer el diario
def accion_leer():
    global directorio_actual

    # Lista las carpetas disponibles en el directorio actual
    contenido_directorio = os.listdir(directorio_actual)
    carpetas = [nombre for nombre in contenido_directorio if os.path.isdir(os.path.join(directorio_actual, nombre))]

    if carpetas:
        # Muestra las carpetas disponibles
        print("Carpetas disponibles")
        for i, carpeta in enumerate(carpetas, 1):
            print(f"{i}, {carpeta}")

        # Solicita al usuario seleccionar una carpeta
        opcion = int(input("Ingrese el número de la carpeta a la que desea ingresar: ")) - 1
        if 0 <= opcion < len(carpetas):
            carpeta_seleccionada = carpetas[opcion]
            ruta_carpeta = os.path.join(directorio_actual, carpeta_seleccionada)

            # Lista los archivos de texto disponibles en la carpeta seleccionada
            archivos_txt = [nombre for nombre in os.listdir(ruta_carpeta) if nombre.endswith(".txt")]

            if archivos_txt:
                # Muestra los archivos de texto disponibles
                print("Diarios disponibles")
                for i, archivo in enumerate(archivos_txt, 1):
                    print(f"{i}.- {archivo}")

                # Solicita al usuario seleccionar un archivo para leer
                opcion = int(input("Ingrese el número del archivo que desea leer: ")) - 1
                if 0 <= opcion < len(archivos_txt):
                    archivo_seleccionado = archivos_txt[opcion]
                    archivo_path = os.path.join(ruta_carpeta, archivo_seleccionado)
                    # Verifica si el archivo existe
                    if os.path.exists(archivo_path):
                        # Lee y muestra el contenido del archivo
                        with open(archivo_path, "r", encoding="UTF-8") as archivo:
                            contenido = archivo.read()
                            print(f"Contenido de {archivo_seleccionado}:\n{contenido}")
                    else:
                        print("El archivo no existe")
                else:
                    print("Opción de archivo inválida")
            else:
                print("No hay archivos disponibles para leer en esta carpeta")
        else:
            print("Opción de carpeta inválida")
    else:
        print("No hay carpetas disponibles para leer")



# Función para crear una nueva carpeta
def crear_carpetas():
    global directorio_actual

    # Solicita al usuario ingresar el nombre de la carpeta
    nombre_carpeta = input("Ingrese el nombre de las carpeta: ")
    ruta_carpeta = os.path.join(directorio_actual, nombre_carpeta)

    # Verificamos si la carpeta ya existe, en caso contrario la crea
    if not os.path.exists(ruta_carpeta):
        try:
            os.mkdir(ruta_carpeta)
            print("Carpeta creada exitosamente.")
        except OSError as error:
            print(f"No se pudo crear la carpeta: {error}")
    else:
        print("La carpeta ya existe")


# Función para mostrar el menú de opciones dentro de la carpeta
def menu_carpeta(nombre_carpeta):

    # Cambiamos al directorio de la carpeta seleccionada
    ruta_carpeta = os.path.join(directorio_actual, nombre_carpeta)
    os.chdir(ruta_carpeta)

    while True:
        print("------------------------------------------------")
        print(f"     {nombre_carpeta.upper()}        ")
        print("------------------------------------------------")
        print("|    Opciones que puedes realizar              |")
        print("|    1.- Escribir en el diario                 |")
        print("|    2.- Leer el diario                        |")
        print("|    0.- Volver al menú principal              |")
        print("------------------------------------------------")
        op = int(input("Opción: "))

        if op == 0:
            os.chdir(directorio_actual)
            break
        elif op == 1:
            accion_escribir()
        elif op == 2:
            accion_leer()
        else:
            print("Ingrese una opción valida")


# Función para mostrar las carpetas disponibles y permitir que el usuario seleccione una
def lista_de_carpetas():
    global directorio_actual

    # Obtenemos una lista de todos los archivos y carpetas del directorio
    contenido_directorio = os.listdir(directorio_actual)

    # Filtramos la lista para mostrar solo las carpetas
    carpetas = [nombre for nombre in contenido_directorio if os.path.isdir(os.path.join(directorio_actual, nombre))]

    # Imprimir el nombre de todas las carpetas
    for carpeta in carpetas:
        print(carpeta)

    # Solicita al usuario ingresar el nombre de la carpeta
    nombre_carpeta = input("Ingrese el nombre de la carpeta a la que desea acceder: ")
    if nombre_carpeta in carpetas:
        # Llama a la función menu_carpeta() con el nombre de la carpeta seleccionada
        menu_carpeta(nombre_carpeta)
    else:
        print(f"La carpeta {nombre_carpeta}, no existe")


while True:
    print("------------------------------------------------")
    print("|           BIENVENIDO A DIARIO ONLINE         |")
    print("------------------------------------------------")
    print("------------------------------------------------")
    print("|    ¿Qué deseas realizar el día de hoy?       |")
    print("|    1.- Crear una núeva carpeta               |")
    print("|    2.- Entrar a una carpeta                  |")
    print("|    0.- Salir                                 |")
    print("------------------------------------------------")
    op = int(input("Opción: "))

    if op == 0:
        break
    elif op == 1:
        crear_carpetas()
    elif op == 2:
        print("Estas son las carpetas disponibles actualmente: ")
        lista_de_carpetas()
    else:
        print("Ingrese una opción valida")

