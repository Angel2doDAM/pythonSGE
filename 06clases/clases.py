class Programmer:

    #Crear un atributo fuera de init (opcional)
    surname: str = None

    def __init__(self, name: str, age: int, languages: list):
        self.name = name
        self.age = age
        self.languages = languages

# Las funciones de una clase deben acabar recibiéndose a si mismo

    def print(self):
        print(f"Nombre: {self.name} |Apellidos: {self.surname} |Edad: {self.age} |Idiomas: {self.languages}")

my_programmer = Programmer("Prueba", 54, ["Python", "Java", "Javascript"])

my_programmer.print()