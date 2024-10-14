print("Hola \n"
+ "Bienvenido a tu agenda \n")

agenda={"angel":"642401515"}

opcion=0
while opcion != 6:
    print("Elije la opción a realizar: \n"
    + "1._ Buscar contacto \n"
    + "2._ Insertar contacto \n"
    + "3._ Actualizar contacto \n"
    + "4._ Eliminar contacto \n"
    + "5._ Mostrar todos en ascendente \n"
    + "6._ Salir")

    def elegir_opcion(opcion):
        match opcion:
            case 1:
                nombre = int(input("Introduce el nombre:"))
                for contacto in agenda:
                    if nombre in contacto:
                        print(agenda[nombre])
            case 2:
                return "Has elegido la opción 2"
            case 3:
                return "Has elegido la opción 3"
            case _:
                return "Opción no válida"

    opcion = int(input())
    elegir_opcion(opcion)