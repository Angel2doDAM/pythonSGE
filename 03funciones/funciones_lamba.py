#──────────────────────────────────────────────────┐
# Lambda que suma dos números
suma = lambda x, y: x + y

# Uso de la función
resultado = suma(3, 5)
print(resultado)  # Salida: 8

#──────────────────────────────────────────────────┤

# Lambda que hace el cuadrado de un numero
cuadrado = lambda x: x**2

# Uso de la función
resultado = cuadrado(3)
print(resultado)  # Salida: 9

#──────────────────────────────────────────────────┤

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Usando una función lambda para multiplicar cada número por 2
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # Salida: [2, 4, 6, 8, 10]

#──────────────────────────────────────────────────┤

# Lista de números
numeros = [1, 2, 3, 4, 5, 6]

# Usando una lambda para filtrar los números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4, 6]

#──────────────────────────────────────────────────┤

# Lista de tuplas
personas = [("Ana", 30), ("Juan", 20), ("Pedro", 25)]

# Ordenar por la edad (segundo elemento de la tupla)
ordenado = sorted(personas, key=lambda persona: persona[1])
print(ordenado)
# Salida: [('Juan', 20), ('Pedro', 25), ('Ana', 30)]
#──────────────────────────────────────────────────┘