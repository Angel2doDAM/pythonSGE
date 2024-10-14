edad = int(input("Introduce tu edad: ")) #Introduce por teclado un número para una variable llamada "edad"

if edad < 18: #Comprueba si la variable (edad) es menor de 18
    print("Eres menor de edad.") #Si es menor de 18 muestra por pantalla el mensaje entre comillas
elif edad >= 18 and edad < 65: #Si no es mayor a 18 años, comprueba si es nemor o igual a 18 t menor a 65
    print("Eres un adulto.") #En caso de ser un número entre 18 y 64 (incluyendo estos) escribe el mensaje entre comillas
else: #Si nada de lo anterior se cumple entra en esta excepción
    print("Eres una persona mayor.") #En caso de no cumplir cualquier condición anterior muestra el mensaje entre comillas

#------------------------------------------------------------------------------------------------------------------------------------

def elegir_opcion(opcion):
    match opcion:
        case 1:
            return "Has elegido la opción 1"
        case 2:
            return "Has elegido la opción 2"
        case 3:
            return "Has elegido la opción 3"
        case _:
            return "Opción no válida"

opcion = int(input("Elige una opción (1-3): "))
resultado = elegir_opcion(opcion)
print(resultado)
