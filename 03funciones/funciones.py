
"""def nombre_funcion(parametros):
    BLOQUE / CONJUNTO DE INSTRUCCIONES

nombre_funcion(mi_parametro)"""

def greet():
    print("Hola!!!, bienvenidos al curso 24/25")

greet()

#------------------------------------------------------

def return_greet():
    return "Hola!!!, bienvenidos al curso 24/25" #No funca este, es kk

return_greet

#------------------------------------------------------

def variable_arg_greet(*names):
    for name in names:
        print(f"Buenos dias, {name}")

variable_arg_greet("Uno", "Dos", "Tres")

#------------------------------------------------------

print(len("cuentanumeroletras"))
print(type(23))
