#──────────────────────────────────────────────────┐

import os

#──────────────────────────────────────────────────┤

# Crear y escribir en un archivo en la raíz del proyecto
with open("archivo.txt", "w") as archivo:
    archivo.write("1. Nombre; Ángel Mansilla Herguedas.\n")
    archivo.write("2. Edad; 19 años.\n")
    archivo.write("3. Lenguaje usado; Python.")

#──────────────────────────────────────────────────┤

# Crear y escribir en un archivo en una carpeta específica

# Declarar la ruta del archivo
ruta_absoluta = "C:/Users/angel.manher/Desktop/archivo.txt"
ruta_relativa = "../../archivo.txt" #ambas funcionan, pero esta es mas simple

#Crear o editar el archivo en la ruta anterior
with open(ruta_absoluta, "w") as archivo:
    archivo.write("1. Nombre; Ángel Mansilla Herguedas.\n")
    archivo.write("2. Edad; 19 años.\n")
    archivo.write("3. Lenguaje usado; Python.")

#──────────────────────────────────────────────────┤

# Leer y mostrar el contenido del archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

#──────────────────────────────────────────────────┤

try:
    os.remove(ruta_absoluta)
    print(f"El archivo '{ruta_absoluta}' ha sido eliminado.")
except FileNotFoundError:
    print(f"El archivo '{ruta_absoluta}' no existe.")
except Exception as e:
    print(f"Ocurrió un error al intentar eliminar el archivo: {e}")

try:
    os.remove("archivo.txt")
    print(f"El archivo seleccionado ha sido eliminado.")
except FileNotFoundError:
    print(f"El archivo seleccionado no existe.")
except Exception as e:
    print(f"Ocurrió un error al intentar eliminar el archivo: {e}")

#──────────────────────────────────────────────────┘