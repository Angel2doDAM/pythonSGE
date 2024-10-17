# Importo la LIBRERÍA json para manejar archivos en formato JSON
import json

# Defino una CLASE para administrar las tareas
class AdministradorDeTareas:
    
    # FUNCIÓN constructor (__init__) que inicializa el objeto y carga las tareas desde un archivo JSON
    def __init__(self, file_name="tareas.json"):
        self.file_name = file_name
        self.tareas = self.cargarTareas()  # Llamo a cargarTareas para inicializar la LISTA de tareas

    # FUNCIÓN para cargar tareas desde un archivo JSON
    def cargarTareas(self):
        # Inta abrir el archivo y leer su contenido
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)  # Carga el contenido del archivo JSON
        except (FileNotFoundError, json.JSONDecodeError):  # Si ocurre un error, se maneja con esta EXCEPCION
            return []  # Retorna una LISTA vacía

    # FUNCIÓN para guardar la LISTA de tareas en un archivo JSON
    def guardarTareas(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tareas, file)  # Guarda la LISTA de tareas en formato JSON

    # FUNCIÓN para añadir una nueva tarea
    def aniadirTarea(self, nombreTarea):
        self.tareas.append({"name": nombreTarea, "completed": False})  # Añado un DICCIONARIO con el nombre y estado de la tarea
        self.guardarTareas()  # Guarda las tareas actualizadas en el archivo JSON
        print(f"Tarea '{nombreTarea}' añadida con éxito.")

    # FUNCIÓN para eliminar una tarea
    def eliminarTarea(self, numeroTarea):
        
        # VARIABLE contador para identificar la tarea por su número
        contador : int = 1
        # Ordeno las tareas por nombre usando una FUNCIÓN LAMBDA
        sorted_tasks = sorted(self.tareas, key=lambda x: x["name"])  # Ordeno la LISTA de tareas alfabéticamente
        
        # BUCLE for para recorrer las tareas ordenadas
        for tarea in sorted_tasks:
            if (contador == numeroTarea):  # CONDICIONAL para identificar la tarea por el número dado
                tarea["name"] = "TareaParaEliminar"  # Cambia el nombre de la tarea a un valor especial para eliminarla
                break  # Sale del bucle cuando encuentra la tarea
            contador += 1  # Incrementa el contador para la siguiente tarea
        
        # Filtro la LISTA de tareas eliminando la tarea marcada
        self.tareas = [tarea for tarea in self.tareas if tarea["name"] != "TareaParaEliminar"]
        self.guardarTareas()  # Guarda las tareas actualizadas
        print(f"Tarea eliminada con éxito.")

    # FUNCIÓN para alternar el estado de una tarea (completada o incompleta)
    def alternarTareas(self, numeroTarea):

        contador : int = 1  # Inicializo un contador para encontrar la tarea correcta
        # Ordena las tareas alfabéticamente por nombre usando una FUNCIÓN LAMBDA
        sorted_tasks = sorted(self.tareas, key=lambda x: x["name"])
        
        # BUCLE para encontrar la tarea por número
        for tarea in sorted_tasks:
            if (contador == numeroTarea):  # CONDICIONAL para encontrar la tarea
                nombreAlterar = tarea["name"]  # Guardo el nombre de la tarea a modificar
                break  # Rompe el BUCLE cuando encuentras la tarea
            contador += 1

        # BUCLE para alternar el estado de la tarea en la LISTA original
        for tarea in self.tareas:
            if tarea["name"] == nombreAlterar:  # CONDICIONAL para encontrar la tarea por nombre
                if tarea["completed"] == False:  # Si la tarea no está completada, la marco como completada
                    tarea["completed"] = True
                    self.guardarTareas()  # Guarda los cambios
                    print(f"Tarea '{nombreAlterar}' marcada como completada.")
                elif tarea["completed"] == True:  # Si está completada, la marco como incompleta
                    tarea["completed"] = False
                    self.guardarTareas()  # Guarda los cambios
                    print(f"Tarea '{nombreAlterar}' marcada como incompleta.")
            else:
                print("Tarea no encontrada")  # Si no encontra la tarea, muestra un mensaje de error

    # FUNCIÓN para mostrar todas las tareas
    def mostrarTarea(self):
        contador : int = 1  # Contador para numerar las tareas
        if not self.tareas:  # CONDICIONAL para verificar si la LISTA de tareas está vacía
            print("No hay tareas pendientes.")
        else:
            # Ordeno las tareas por nombre usando una FUNCIÓN LAMBDA
            sorted_tasks = sorted(self.tareas, key=lambda x: x["name"])
            # BUCLE para mostrar todas las tareas
            for tarea in sorted_tasks:
                status = "Completada" if tarea["completed"] else "Pendiente"
                print(f"Tarea{contador}: {tarea['name']} - Estado: {status}")
                contador += 1  # Incremento el contador para la siguiente tarea


# FUNCIÓN principal con MANEJO DE EXCEPCIONES para la interacción con el usuario
def main():
    administrador = AdministradorDeTareas()  # Creo una instancia u objeto de AdministradorDeTareas
    contadorLetras = 0  # Contador para manejar errores por entrada de texto en lugar de números
    contadorNumeros = 0  # Contador para manejar errores al seleccionar números inválidos

    # BUCLE principal del programa que se ejecuta hasta que el usuario decida salir
    while True:
        print("\nOpciones:")
        print("1. Añadir tarea")
        print("2. Eliminar tarea")
        print("3. Alternar entre completada y sin completar")
        print("4. Mostrar tareas")
        print("5. Salir")

        # Intenta convertir la entrada del usuario en un número entero para seleccionar una opción
        try:
            option = int(input("Elige una opción: "))  # Solicita al usuario que elija una opción
        except ValueError:  # Si no se ingresa un número, capturamos el error
            if contadorLetras > 1:  # Si el usuario comete el error más de dos veces muestra este mensaje:
                print("\nEres muu tonto")
                print("No te mereces mi paciencia")
                print("Adiós\n")
                quit()  # Cierra el programa "por enfado"
            else:
                print("\nPor favor, ingresa un número entero, el resto de caracteres están prohibidos en este programa en concreto.")
                print("Te doy otra oportunidad a ver si lo has pillado:")
                contadorLetras += 1  # Incremento el contador de errores por texto
                continue  # Vuelve al inicio del BUCLE

        # CONDICIONALES para manejar la opción elegida por el usuario
        if option == 1:  # Opción para añadir una tarea
            nombreTarea = input("Introduce el nombre de la tarea: ")  # Pide el nombre de la tarea
            administrador.aniadirTarea(nombreTarea)  # Llamo al método para añadir la tarea
        elif option == 2:  # Opción para eliminar una tarea
            numeroTarea = input("Introduce el número de la tarea a eliminar \nSe recomienda ver primero la lista de tareas \nTambién puedes cancelar con '0': ")
            administrador.eliminarTarea(int(numeroTarea))  # Llamo al método para eliminar la tarea
        elif option == 3:  # Opción para alternar el estado de una tarea
            nombreTarea = input("Introduce el número de la tarea a alterar \nSe recomienda ver primero la lista de tareas \nTambién puedes cancelar con '0': ")
            administrador.alternarTareas(int(nombreTarea))  # Llamo al método para alternar el estado
        elif option == 4:  # Opción para mostrar todas las tareas
            administrador.mostrarTarea()  # Llamo al método para mostrar las tareas
        elif option == 5:  # Opción para salir del programa
            print("Saliendo del programa...\n")
            break  # Rompe el BUCLE principal para terminar el programa
        else:  # Si el usuario introduce un número no válido
            if contadorNumeros > 1:  # Si el error se repite más de dos veces muestra el siguiente mensaje:
                print("\nEres muu tonto")
                print("No te mereces mi paciencia")
                print("Adiós\n")
                quit()  # Cierra el programa "por enfado"
            else:
                print("\nEs muy simple, solo números del 1 al 5, pues vas tu y seleccionas el", option)
                print("Me quitas las ganas de vivir :,-)")
                print("Por favor, esta vez introduce un número válido:")
                contadorNumeros += 1  # Incremento el contador de errores por número inválido y vuelve al inicio del BUCLE while


# Ejecuto el programa principal
if __name__ == "__main__":
    main()  # Llama a la FUNCIÓN principal para iniciar el programa
