#Crear diccionario
mi_diccionario = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Madrid"
}

print(mi_diccionario)
# Salida: {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Madrid'}

# Usando una nueva clave
mi_diccionario["pais"] = "España"
print(mi_diccionario)
# Salida: {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Madrid', 'pais': 'España'}

# Usando update() para agregar múltiples pares clave-valor
mi_diccionario.update({"telefono": "123456789"})
print(mi_diccionario)
# Salida: {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Madrid', 'pais': 'España', 'telefono': '123456789'}

# Usando del para eliminar un par clave-valor
del mi_diccionario["telefono"]
print(mi_diccionario)
# Salida: {'nombre': 'Alice', 'edad': 30, 'ciudad': 'Madrid', 'pais': 'España'}

# Usando pop() para eliminar un par clave-valor y obtener su valor
eliminado = mi_diccionario.pop("edad")
print(mi_diccionario)
# Salida: {'nombre': 'Alice', 'ciudad': 'Madrid', 'pais': 'España'}
print("Edad eliminada:", eliminado)
# Salida: Edad eliminada: 30

# Usando popitem() para eliminar el último par clave-valor agregado
ultimo_elemento = mi_diccionario.popitem()
print(mi_diccionario)
# Salida: {'nombre': 'Alice', 'ciudad': 'Madrid'}
print("Último elemento eliminado:", ultimo_elemento)
# Salida: Último elemento eliminado: ('pais', 'España')

# Actualizar el valor de una clave existente
mi_diccionario["nombre"] = "Bob"
print(mi_diccionario)
# Salida: {'nombre': 'Bob', 'ciudad': 'Madrid'}

# Usando update() para actualizar varios pares clave-valor
mi_diccionario.update({"ciudad": "Barcelona", "edad": 25})
print(mi_diccionario)
# Salida: {'nombre': 'Bob', 'ciudad': 'Barcelona', 'edad': 25}

# Restablecer el diccionario
mi_diccionario = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Madrid"
}
#El diccionario está como al inicio

# Ordenar las claves
claves_ordenadas = sorted(mi_diccionario.keys())
print("Claves ordenadas:", claves_ordenadas)
# Salida: Claves ordenadas: ['ciudad', 'edad', 'nombre']

# Convertir todos los valores a cadenas y ordenarlos
valores_ordenados_todas_cadenas = sorted(str(valor) for valor in mi_diccionario.values())
print("Valores ordenados como cadenas:", valores_ordenados_todas_cadenas)
# Salida: Valores ordenados como cadenas: ['30', 'Alice', 'Madrid']
