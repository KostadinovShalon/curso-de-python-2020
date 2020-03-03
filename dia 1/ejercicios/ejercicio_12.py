# 12. Implementa el metodo de Newton-Raphson para estimar la raiz cuadrada de un numero con una precision especifica.

# Para aproximar la raiz de alguna funcion, el metodo de Newton-Raphson dice lo siguiente
# x = x - f(x)/f'(x)

# En la expresion anterior, las x del lado derecho corresponden a un valor previo (o sea, otra aproximacion

# Si queremos obtener la raiz cuadrada de un numero k, equivale a encontrar la raiz del polinomio
# f(x) = x^2 - k
# La derivada de la funcion anterior es f'(x) = 2x. Por lo tanto el algoritmo quedaria
# x = x - (x^2 - k)/(2x)
# donde x seria la raiz de k

k = 145
eps = 0.01
x = k // 2  # Aproximaremos diciendo que la raiz es igual a la mitad de k
while abs(x ** 2 - k) >= eps:
    x = x - (x ** 2 - k)/(2 * x)

print(f"El valor aproximado de la raiz de {k} es {x}")