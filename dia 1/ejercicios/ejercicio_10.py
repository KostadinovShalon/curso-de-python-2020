# 10. El factorial de un numero esta dado por la multiplicacion de si mismo con todos los numeros naturales menores. Se
# representa con un signo de admiracion y se podria definir como n! = n(n-1)(n-2)... Por ejemplo, 5! = 5x4x3x2x1 = 120.
# Escribe un programa que encuentre el factorial de un numero.

n = 6

factorial = n
for i in range(n - 1, 0, -1):
    factorial *= i
print(f"El factorial de {n} es {factorial}")
