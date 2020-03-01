# Aqui incluyo mas ejemplos de while y for

# Programa que calcule e imprima la suma de todos los multiplos de 7 desde 1 a 100
# Con while:
x = 1
suma = 0
while x <= 100:
    if x % 7 == 0:
        suma += x
    x += 1
print(suma)

# Con for
suma = 0
for i in range(1, 101):
    if i % 7 == 0:
        suma += i
print(suma)

# Otra forma con el for
suma = 0
for i in range(0, 101, 7):
    suma += i
print(suma)

# Otra forma que es mas "pythonic" y veremos mas adelante
suma = sum(i for i in range(0, 101, 7))
print(suma)

