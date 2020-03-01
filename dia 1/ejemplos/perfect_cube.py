# Vamos a encontrar la raíz cúbica de un cubo perfecto

x = int(input("Introduzca un entero: "))
raiz = 0

# abs es el valor absoluto. Aquí vamos a incrementar raiz de 1 en 1 mientras raiz^3 < x
# se usa el valor absoluto porque en la raíz cúbica se conserva el signo y solo se necesita
# checar el valor
while raiz ** 3 < abs(x):
    raiz += 1

if raiz ** 3 != abs(x):  # Si el valor de raíz al cubo no es el mismo que x, entonces no es un cubo perfecto
    print(f"{x} no es un cubo perfecto")
else:
    if x < 0:  # Aquí se hace la corrección del signo
        raiz = -raiz
    print(f"La raíz cúbica de {x} es {raiz}")

# Mismo algoritmo con for

for raiz in range(abs(x) + 1):
    if raiz ** 3 >= x:
        break

# La variable raiz sigue estando definida fuera del for con el último valor obtenido
if raiz ** 3 != abs(x):
    print(f"{x} no es un cubo perfecto")
else:
    if x < 0:
        raiz = -raiz
    print(f"La raíz cúbica de {x} es {raiz}")