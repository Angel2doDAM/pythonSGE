#Crear tupla
mi_tupla = (10, 20, 30, 40) 
print(mi_tupla)
# Salida: (10, 20, 30, 40)

#Clonar tupla
nueva_tupla = mi_tupla + (50,) 
print(nueva_tupla)
# Salida: (10, 20, 30, 40, 50)

#Eliminar elemento de tupla
mi_lista = list(mi_tupla)  # Convertir en lista
mi_lista.remove(30)  # Eliminar elemento
mi_tupla = tuple(mi_lista)  # Convertir de nuevo en tupla
print(mi_tupla)
# Salida: (10, 20, 40)

#Modificar elemento de tupla
mi_lista = list(mi_tupla)  # Convertir en lista
mi_lista[1] = 25  # Modificar el segundo elemento
mi_tupla = tuple(mi_lista)  # Convertir de nuevo en tupla
print(mi_tupla)
# Salida: (10, 25, 40)
