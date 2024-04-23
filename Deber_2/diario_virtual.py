import os
import datetime as dt

# Obteniendo el directorio actual
directorio_actual = os.getcwd()

# Códigos de color ANSI
colors = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'underline': '\033[4m',
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bg_black': '\033[40m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
    'bg_magenta': '\033[45m',
    'bg_cyan': '\033[46m',
    'bg_white': '\033[47m'
}


# Función para escribir en el diario
def accion_escribir():
    # Obtiene la fecha y hora actual
    fecha_y_hora_actual = dt.datetime.now()
    # Genera un nombre de archivo único basado en la fecha y la hora actual
    archivos_txt = fecha_y_hora_actual.strftime("%Y_%m_%d-%H_%M_%S") + ".txt"
    # Abre el archivo en modo de escritura
    with open(archivos_txt, "w", encoding="UTF-8") as archivo:
        while True:
            escribir = input(f"{colors['cyan']}Ingrese una linea de texto (escriba 'salir' para terminar): {colors['reset']}")
            if escribir.lower() == "salir":
                break
            else:
                # Escribe la línea de texto en el archivo
                archivo.write(escribir + "\n")


# Función para leer el diario
def accion_leer(nombre_carpeta):
    # Construye la ruta completa a la carpeta específica
    ruta_carpeta = os.path.join(directorio_actual, nombre_carpeta)

    # Lista los archivos de texto disponibles en la carpeta
    archivos_txt = [nombre for nombre in os.listdir(ruta_carpeta) if nombre.endswith(".txt")]

    if archivos_txt:
        # Muestra los archivos de texto disponibles en la carpeta
        print(f"{colors['cyan']}Diarios disponibles en la carpeta:{colors['reset']}")
        for i, archivo in enumerate(archivos_txt, 1):
            print(f"{i}.- {archivo}")

        # Solicita al usuario seleccionar un archivo para leer
        opcion = int(input(f"{colors['cyan']}Ingrese el número del archivo que desea leer: {colors['reset']}")) - 1
        if 0 <= opcion < len(archivos_txt):
            archivo_seleccionado = archivos_txt[opcion]
            archivo_path = os.path.join(ruta_carpeta, archivo_seleccionado)
            # Verifica si el archivo existe
            if os.path.exists(archivo_path):
                # Lee y muestra el contenido del archivo
                with open(archivo_path, "r", encoding="UTF-8") as archivo:
                    contenido = archivo.read()
                    print(f"{colors['yellow']}Contenido de {archivo_seleccionado}:{colors['reset']}\n{contenido}")
            else:
                print(f"{colors['red']}El archivo no existe{colors['reset']}")
        else:
            print(f"{colors['red']}Opción de archivo inválida{colors['reset']}")
    else:
        print(f"{colors['red']}No hay archivos disponibles para leer en esta carpeta{colors['reset']}")


# Función para crear una nueva carpeta
def crear_carpetas():
    global directorio_actual

    # Solicita al usuario ingresar el nombre de la carpeta
    nombre_carpeta = input(f"{colors['cyan']}Ingrese el nombre de las carpeta: {colors['reset']}")
    ruta_carpeta = os.path.join(directorio_actual, nombre_carpeta)

    # Verificamos si la carpeta ya existe, en caso contrario la crea
    if not os.path.exists(ruta_carpeta):
        try:
            os.mkdir(ruta_carpeta)
            print(f"{colors['green']}Carpeta {nombre_carpeta} creada exitosamente.{colors['reset']}")
        except OSError as error:
            print(f"{colors['red']}No se pudo crear la carpeta: {error}{colors['reset']}")
    else:
        print(f"{colors['red']}La carpeta ya existe{colors['reset']}")


# Función para mostrar el menú de opciones dentro de la carpeta
def menu_carpeta(nombre_carpeta):

    # Cambiamos al directorio de la carpeta seleccionada
    ruta_carpeta = os.path.join(directorio_actual, nombre_carpeta)
    os.chdir(ruta_carpeta)

    while True:
        print("------------------------------------------------")
        print(f"{nombre_carpeta.upper():^50}")
        print("------------------------------------------------")
        print("|    Opciones que puedes realizar              |")
        print("|    1.- Escribir en el diario                 |")
        print("|    2.- Leer el diario                        |")
        print("|    0.- Volver al menú principal              |")
        print("------------------------------------------------")
        op = int(input(f"{colors['cyan']}Opción: {colors['reset']}"))

        if op == 0:
            os.chdir(directorio_actual)
            break
        elif op == 1:
            accion_escribir()
        elif op == 2:
            accion_leer(nombre_carpeta)
        else:
            print(f"{colors['red']}Ingrese una opción valida{colors['reset']}")


# Función para mostrar las carpetas disponibles y permitir que el usuario seleccione una
def lista_de_carpetas():
    global directorio_actual

    # Obtenemos una lista de todos los archivos y carpetas del directorio
    contenido_directorio = os.listdir(directorio_actual)

    # Filtramos la lista para mostrar solo las carpetas
    carpetas = [nombre for nombre in contenido_directorio if os.path.isdir(os.path.join(directorio_actual, nombre))]

    # Imprimir el nombre de todas las carpetas
    for carpeta in carpetas:
        print(f"{colors['cyan']}--> {carpeta}{colors['reset']}")

    # Solicita al usuario ingresar el nombre de la carpeta
    nombre_carpeta = input(f"{colors['cyan']}Ingrese el nombre de la carpeta a la que desea acceder: {colors['reset']}")
    if nombre_carpeta in carpetas:
        # Llama a la función menu_carpeta() con el nombre de la carpeta seleccionada
        menu_carpeta(nombre_carpeta)
    else:
        print(f"{colors['red']}La carpeta {nombre_carpeta}, no existe{colors['reset']}")


# Menú principal
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
    op = int(input(f"{colors['cyan']}Opción: {colors['reset']}"))

    if op == 0:
        break
    elif op == 1:
        crear_carpetas()
    elif op == 2:
        print(f"{colors['cyan']}Estas son las carpetas disponibles actualmente: {colors['reset']}")
        lista_de_carpetas()
    else:
        print(f"{colors['red']}Ingrese una opción valida{colors['reset']}")

