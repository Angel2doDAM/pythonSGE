mi_lista = [0,1,2,3,5,6,7]
print(mi_lista)

#insertar en la lista
mi_lista.append(8)
print(mi_lista)

#insertar en la lista en una posicion especifica
mi_lista.insert(4,4)
print(mi_lista)

# Borrar un elemento específico con remove()
mi_lista.remove(5)  # Elimina la primera ocurrencia del valor 5
print( mi_lista)

# Borrar un elemento en una posición específica con pop()
eliminado = mi_lista.pop(2)  # Elimina el elemento en el índice 2
print(eliminado) #Con pop tienes la posibilidad de mostrar el valor eliminado
print( mi_lista)

# Borrar un elemento con del
del mi_lista[4]  # Elimina el elemento en el índice 4
print( mi_lista)
