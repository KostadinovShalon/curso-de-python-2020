# Aproximaremos la raíz cuadrada de un número buscando incrementalmente todos los números posibles

x = 12
eps = 1e-2  # Esta es otra forma de representar 0.01
step = eps ** 2  # Nuestro tamaño de incremento será el valor de eps al cuadrado
n = 0  # Vamos a llevar la cuenta de cuantos intentos se han hecho
ans = 0.0

# Checaremos que nuestro algoritmo sea menos que un valor aproximado epsilon
# En teoría, si ans^2 = x, entonces ans^2 - x = 0. Una buena aproximación se
# puede obtener si ans^2 - x < epsilon, donde epsilon define qué tan precisa debe de ser la raíz.
# La segunda condición del whie, ans^2 <= x nos sirve para no buscar valores de más.
while abs(ans**2 - x) >= eps and ans ** 2 <= x:
    ans += step
    n += 1
print(f"num Gueses: {n}")
if abs(ans**2 - x) >= eps:  # Se llegó al final del while y no se encontró un valor
    print(f"FAILED for x = {x}")
else:
    print(f"{ans} is close for square root of {x}")

# Se podría hacer el algoritmo anterior con un for? Inténtalo.