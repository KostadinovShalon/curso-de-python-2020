# 6. El Teorema Fundamental de la Aritmetica establece que todos los numeros se pueden descomponer en factores
# primos. Escribe un programa que encuentre todos los factores primos de un numero.
# OJO: el 1 no es primo! (y mucho menos el 0)

x = 2

print(f"Factores primos de {x}: ")
for factor in range(2, x // 2 + 1):  # Entre 2 porque ninguno numero n es divisible entre (n // 2) + k, con k > 1
    if x % factor == 0:
        # checamos si es primo con el mismo codigo del ejercicio 1
        es_primo = True
        for numero in range(2, factor):
            if factor % numero == 0:
                es_primo = False
                break
        if es_primo:
            print(factor)


# El codigo de arriba cumple con lo que se indica, pero mas adelante veremos con listas y recursividad como
# descomponer un numero en sus factores primos.
# Por ejemplo, 168 = 2 x 2 x 2 x 3 x 7
