# Importamos las librerías necesarias
import json

# Clase AdministradorDeTareas para gestionar las tareas
class AdministradorDeTareas:
    def __init__(self, file_name="tareas.json"):
        self.file_name = file_name
        self.tareas = self.cargarTareas()  # Cargamos las tareas desde el archivo JSON

    # Función para cargar tareas desde el archivo JSON
    def cargarTareas(self):
        try:
            with open(self.file_name, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Si el archivo no existe o está vacío, retornamos una lista vacía

    # Función para guardar las tareas en el archivo JSON
    def guardarTarea(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tareas, file)

    # Función para agregar una nueva tarea
    def aniadirTarea(self, nombreTarea):
        self.tareas.append({"name": nombreTarea, "completed": False})
        self.guardarTarea()
        print(f"Tarea '{nombreTarea}' añadida con éxito.")

    # Función para eliminar una tarea por nombre
    def eliminarTarea(self, task_name):
        self.tareas = [task for task in self.tareas if task["name"] != task_name]
        self.guardarTarea()
        print(f"Tarea '{task_name}' eliminada con éxito.")

    # Función para marcar una tarea como completada
    def alternarTareas(self, nombreTarea):
        for task in self.tareas:
            if task["name"] == nombreTarea:
                if task["completed"] == False:
                    task["completed"] = True
                    self.guardarTarea()
                    print(f"Tarea '{nombreTarea}' marcada como completada.")
                elif task["completed"] == True:
                    task["completed"] = False
                    self.guardarTarea()
                    print(f"Tarea '{nombreTarea}' marcada como incompleta.")
            else:
                print("Tarea no encontrada")

    # Función para mostrar las tareas
    def mostrarTarea(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            # Usamos una función lambda para ordenar las tareas por nombre
            sorted_tasks = sorted(self.tareas, key=lambda x: x["name"])
            for task in sorted_tasks:
                status = "Completada" if task["completed"] else "Pendiente"
                print(f"Tarea: {task['name']} - Estado: {status}")

# Función principal con manejo de excepciones
def main():
    administrador = AdministradorDeTareas()
    contadorLetras = 0
    contadorNumeros = 0

    while True:
        
        print("\nOpciones:")
        print("1. Añadir tarea")
        print("2. Eliminar tarea")
        print("3. Alternar entre completada y sin completar")
        print("4. Mostrar tareas")
        print("5. Salir")

        try:
            option = int(input("Elige una opción: "))
        except ValueError:
            if contadorLetras > 1:
                print("\nEres muu tonto")
                print("No te mereces mi paciencia")
                print("Adiós\n")
                quit()
            else:
                print("\nPor favor, ingresa un número entero, el resto de caracteres están prohibidos en este programa en concreto.")
                print("Te doy otra oportunidad a ver si lo has pillado:")
                contadorLetras+=1
                continue

        if option == 1:
            nombreTarea = input("Introduce el nombre de la tarea: ")
            administrador.aniadirTarea(nombreTarea)
        elif option == 2:
            nombreTarea = input("Introduce el nombre de la tarea a eliminar: ")
            administrador.eliminarTarea(nombreTarea)
        elif option == 3:
            nombreTarea = input("Introduce el nombre de la tarea a completar: ")
            administrador.alternarTareas(nombreTarea)
        elif option == 4:
            administrador.mostrarTarea()
        elif option == 5:
            print("Saliendo del programa...\n")
            break
        else:
            if contadorNumeros > 1:
                print("\nEres muu tonto")
                print("No te mereces mi paciencia")
                print("Adiós\n")
                quit()
            else:
                print("\nEs muy simple, solo números del 1 al 5, pues vas tu y seleccionas el", option)
                print("Me quitas las ganas de vivir :,-)")
                print("Por favor, esta vez introduce un número válido:")
                contadorNumeros+=1

# Ejecutamos el programa principal
if __name__ == "__main__":
    main()