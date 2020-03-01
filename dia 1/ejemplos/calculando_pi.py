# Pi se puede aproximar por medio de la siguiente serie
#  π = 4 - 4/3 + 4/5 - 4/7 = 4/9 - 4/11 + ...
# Escribiremos un programa para calcularlo

# Definimos n como el numero de elementos de la sumatoria

n = 100
pi = 0
for i in range(n):  # i va a ir de 0 a n - 1
    # Nos podemos dar cuenta que cada elemento de la serie es 4 dividido entre un numero impar
    # Ademas, cada elemento se alterna entre suma o resta. Los elementos en posiciones nones son positivos
    # y en posiciones pares negativos
    # Un numero impar se puede definir como 2p + 1, donde p es un entero.
    # Por ejemplo, 2(0) + 1 = 1; 2(1) + 1 = 3; 2(2) + 1 = 5, etc.
    # El problema del signo alternante podria hacerse con un if

    # if i % 2 == 0:
    #     pi += 4 / (2 * i + 1)
    # else
    #     pi -= 4 / (2 * 1 + 1)

    # Sin embargo el codigo anterior redundancia (hay codigo que se repite). Podria hacerse de la siguiente manera
    termino = 4 / (2 * i + 1)
    if i % 2 == 0:
        pi += termino
    else:
        pi -= termino

# Otra forma de hacerlo sin usar el if/else es usando el hecho de que un numero elevado a una potencia par es positivo
# y elevado a una potencia impar mantiene su signo. Por lo tanto -1 elevado a una par es 1 y a una impar es -1
pi = 0
for i in range(n):
    pi += 4 / (2 * 1 + 1) * (-1) ** i

# De igual manera, una forma mas "pythonic" seria
pi = sum(f4 / (2 * 1 + 1) * (-1) ** i for i in range(n))
