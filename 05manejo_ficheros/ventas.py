import os

with open("archivo.txt", "w") as archivo:
    archivo.write("Productos disponibles:")

print("Bienvenido a 'Ingresar_nombre_de_empresa'\n")
opcion = 0
while opcion != 8:
    print("\nEstas son todas las cosas que puedes hacer:\n")
    print(
        "1.	Añadir producto \n"
        "2.	Consultar producto \n"
        "3.	Actualizar producto \n"
        "4.	Borrar producto \n"
        "5.	Mostrar todos los productos \n"
        "6.	Calcular venta total \n"
        "7.	Calcular venta por producto \n"
        "8.	Salir\n"
    )



    opcion = int(input("Escribe la opción a realizar: \n"))

    def elegir_opcion(opcion):
        match opcion:
            case 1:
                name = input("Nombre:")
                cantidad = input("Cantidad:")
                precio = input("Precio:")
                return "Has elegido la opción 1"
            case 2:
                name = input("Nombre:")
                with open("archivo.txt", "r") as archivo:
                    for line in archivo.readlines():
                        if line.split(", ")[0] == name:
                            print(line)
                            break
            case 3:
                name = input("Nombre:")
                cantidad = input("Cantidad:")
                precio = input("Precio:")
                with open("archivo.txt", "r") as archivo:


                return "Has elegido la opción 3"
            case 4:
                name = input("Nombre:")
                with open("archivo.txt", "r") as archivo:

            case 5:
                with open("archivo.txt", "r") as archivo:
                    contenido = archivo.read()
                    print(contenido)

            case 6:
                total = 0
                with open("archivo.txt", "r") as archivo:
                    for line in archivo.readlines):
                        components = line.split(", ")
                        

            case 7:
                return "Has elegido la opción 3"

            case 8:
                try:
                    os.remove("archivo.txt")
                    print(f"El archivo seleccionado ha sido eliminado.")
                except FileNotFoundError:
                    print(f"El archivo seleccionado no existe.")
                except Exception as e:
                    print(f"Ocurrió un error al intentar eliminar el archivo: {e}")
                print("Adiós")
                SystemExit
            case _:
                return "Opción no válida"

    elegir_opcion(opcion)
