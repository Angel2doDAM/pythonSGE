print(f"Suma: 8 + 14 = {8 + 14}") #Esta línea escribe en la terminal el texto "Suma: 8 + 14 = " seguido del resultado de una suma "8+14"=(22), la f del inicio formatea todo el contenido de los parentesis, asi no hace falta separar el texto del resto

nombre = input("Escribe tu nombre: ") #Con esta línea ingresamos lo escrito por teclado dentro de la variable "nombre"

#--------------------------------------------------------------------
#Operadores de comparación:
a = 10
b = 5

print(a == b)   #False (10 no es igual a 5)
print(a != b)   #True  (10 es diferente de 5)
print(a > b)    #True  (10 es mayor que 5)
print(a < b)    #False (10 no es menor que 5)
print(a >= b)   #True  (10 es mayor o igual a 5)
print(a <= b)   #False (10 no es menor o igual a 5)

#--------------------------------------------------------------------
#Operadores de lógica:

x = True
y = False

print(x and y)   #False (ambos deben ser True)
print(x or y)    #True  (con uno True es suficiente)
print(not x)     #False (invierte el valor de x)

#--------------------------------------------------------------------
#Operadores de asignación:

a = 5

a += 3   # a=a+3 → 5+3=8
print(a)  # 8

a -= 2   # a=a-2 → 8-2=6
print(a)  # 6

a *= 4   # a=a*4 → 6*4=24
print(a)  # 24

a /= 2   # a=a/2 → 24/2=12.0
print(a)  # 12.0 (resultado es float)

a //= 3  # a=a//3 → 12//3=4 (división entera)
print(a)  # 4

a %= 3   # a=a%3 → 4%3=1 (resto de la división)
print(a)  # 1

a **= 2  # a=a**2 → 1**2=1 (elevado)
print(a)  # 1
