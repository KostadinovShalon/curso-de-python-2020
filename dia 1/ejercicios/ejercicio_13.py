# 13. Un triangulo rectangulo puede tener sus tres lados como numeros enteros. Si a y b son los catetos y c la
# hipotenusa, se cumple que a^2 + b^2 = c^2. Si tanto a, b y c son enteros, se dice que a, b y c son una tercia
# pitagorica. Por ejemplo, 3^2 + 4^2 = 5^2. Escribe un programa que encuentre todas las tercias pitagoricas, con los
# numeros menores que 500.

# Usaremos la fuerza bruta, o sea, vamos a probar todos los posibles numeros en un triple for anidado

for a in range(1, 501):
    for b in range(1, 501):
        for c in range(1, 501):
            if a ** 2 + b ** 2 == c ** 2:
                print(f"{a}, {b}, {c}")

# En realidad el codigo anterior mostraria resultados repetidos porque marca a, b, c como una terna diferente
# de b, a, c. Podemos hacer algunas modificaciones imponiendo b > a. Ademas, sabemos que a + b > c debido a la
# desigualdad del triangulo
for a in range(1, 501):
    for b in range(a + 1, 501):
        for c in range(a + b + 1):
            if a ** 2 + b ** 2 == c ** 2:
                print(f"{a}, {b}, {c}")
