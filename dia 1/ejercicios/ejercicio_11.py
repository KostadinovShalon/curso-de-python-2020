# 11. Escribe un programa que aproxime el valor de la constante de Euler (e = 2.71828...)

# e = 2.718281828459045235360...
# Hay muchas formas de calcular e. Una de ellas es mediante la serie e = 1 + 1/1! + 1/2! + 1/3! } 1/4! + ...
# Usaremos la serie anterior para aproximar e

n = 100
e = 1
for i in range(1, n - 1):
    fact = i
    for j in range(i - 1, 0, -1):
        fact *= j
    e += 1 / fact

print(f"El numero e = {e} usando 100 elementos de la serie")

# Aunque igual podemos obtenerlo por su definicion
# e = (1 + 1/n)^n , cuando n tiende a infinito
n = 10000000
e = (1 + 1/n) ** n
print(f"El numero e = {e} usando su definicion con n = {n}")

# Por que la segunda forma no es tan buena???
