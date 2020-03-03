# 7. Un numero perfecto es aquel cuya suma de sus factores es igual a si mismo. Por ejemplo,
# los factores del 6 son 1, 2 y 3, y como 1 + 2 + 3 = 6, entonces 6 es un numero perfecto.
# Escribe un programa que encuentre los primeros 5 numeros perfectos.

import time

tic = time.perf_counter()
n = 0
x = 1
while n < 5:
    suma_de_factores = 0
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            suma_de_factores += i
    if suma_de_factores == x:
        print(x)
        n += 1
    x += 1
toc = time.perf_counter()

print(f"Tiempo: {toc - tic} s")

# Si no pudiste encontrar el quinto... Pues vamos a hacer trampa
# Un numero perfecto se puede construir de la siguiente formula
# m x (m + 1) / 2
# Donde m es un numero de Mersenne.
# Un numero de Mesernne tiene la forma 2^n - 1, donde n es primo
# Sin embargo, 2^n - 1 no es garantia de que va a ser primo. Un numero de Mersenne
# es aquel que sigue la formula anterior Y ES PRIMO ademas.

# Ahora vamos a hacer lo mismo pero en vez de encontrar numeros perfectos encontraremos numeros de Mersenne

tic = time.perf_counter()
n = 0
x = 2
while n < 5:
    es_primo = True
    for numero in range(2, x // 2 + 1):  # Entre 2 porque ninguno numero n es divisible entre (n / 2) + k, con k > 1
        if x % numero == 0:  # Si encuentro un divisor, no es primo
            es_primo = False
            break
    if es_primo:
        posible_mersenne = 2 ** x - 1
        es_numero_de_mersenne = True
        for numero in range(2, posible_mersenne // 2 + 1):
            if posible_mersenne % numero == 0:
                es_numero_de_mersenne = False
                break
        if es_numero_de_mersenne:
            print(posible_mersenne * (posible_mersenne + 1) // 2)
            n += 1
    x += 1
toc = time.perf_counter()
print(f"Tiempo: {toc - tic} s")
