mi_set = {1, 2, 3} # Crear el set
print(mi_set)
# Salida: {1, 2, 3}

mi_set.add(4)  # Agregar el número 4 al set
print(mi_set)
# Salida: {1, 2, 3, 4}

# Intentar agregar un valor ya existente no lo duplicará
mi_set.add(2)
print(mi_set)
# Salida: {1, 2, 3, 4}

# Borrar un elemento existente con remove()
mi_set.remove(3)
print(mi_set)
# Salida: {1, 2, 4}

# Usar discard(), que no da error si el elemento no existe
mi_set.discard(10)
print(mi_set)
# Salida: {1, 2, 4}  # No cambia, ya que 10 no está en el set

# Eliminar un elemento aleatorio con pop()
elemento_eliminado = mi_set.pop()
print("Elemento eliminado:", elemento_eliminado)
print(mi_set)
# Salida: Elemento eliminado: (cualquiera de los elementos)
#         Set resultante: {2, 4} o similar

# Borrar todos los elementos con clear()
mi_set.clear()
print(mi_set)
# Salida: set()  # Set vacío
