import os

with open("datos.json", "w") as archivo:
    archivo.write(
        """{
            "Nombre": "Angel Mansilla",
            "Edad": 19,
            "Fecha_nacimiento": "28/08/2005",
            "Modulos": [
                "SGE - Sistema Gestor de Empresas",
                "PSYP - Programacion de Servicios y Procesos",
                "AAD - Acceso a Datos",
                "PMDM - Programacion Multimedia y Dispositivos Moviles",
                "DI - Desarrollo de Interfaces"
            ]
        }"""
    )

with open("datos.json", "r") as archivo:
    print(archivo.read())

try:
    os.remove("datos.json")
    print(f"El archivo seleccionado ha sido eliminado.")
except FileNotFoundError:
    print(f"El archivo seleccionado no existe.")
except Exception as e:
    print(f"Ocurrió un error al intentar eliminar el archivo: {e}")