# Print Statement
print("Hello World!")

# 4 Tipos de dato elementales
print(1)  # integers
print(3.1416)  # floats
print(2 < 3)  # Bools. Los booleanos solo son True o False
print(None)  # Elemento nulo

# Variables
# Una variable es simplemente un nombre que guarda un valor
# En Python no tenemos que especificar el tipo de dato ya que este es dinámico
# Una variable se declara de la siguiente forma
r = 3

# Si hago una asignación de la misma variable más adelante, su valor anterior se perderá.
# Es importante notar que puedo cambiar el tipo de valor de una variable
r = 1 > 2  # Ahora r es una variable de tipo booleana

# También existen las asignaciones múltiples
a, b = 1, 2
x, y, z, q = 0, .1, None, True

# Las variables son case-sensitive, esto es, que R y r son variables diferentes. En Python, lo estandar
# es que todas las variables esten en minuscula y si son palabras compuestas esten separadas por guion bajo
# Las variables pueden tener numeros pero no empezar con numero
variable = 1
VARIABLE = 2
otra_variable = 2
esta_es_otra_variable_que_estoy_creando_porque_quiero = variable + otra_variable
NuNcAeScRiBaSaSiTuSvArIaBlEs = False
miPrimeraVariable = 3.4  # esto es conocido como camel-case. Es muy usado en otros lenguajes de programación
MiPrimeraVariable = 3.5  # esto como Pascal-case. Ambos son usados pero en Python se recomienda minúsculas


# Operaciones matemáticas
x + y  # Suma
x - y  # Resta
x * y  # Multiplicación
x / y  # División
x // y  # División entera (o sea, el resultado es un entero, sin decimales: 5 // 3 = 1
x ** y  # Exponenciación, o sea, x elevado a la y
x % y  # Módulo: esta operación nos da el residuo de la división de x entre y. O sea, 5 % 3 = 2

# Python respeta la jerarquía de operaciones y paréntesis, incluso para las variables booleanas

# Comparaciones. Los resultados de todas las comparaciones son siempre un booleano (True o False)
x > y  # Mayor que
x < y  # Menor que
x >= y  # Mayor o igual que
x <= y  # Menor o igual que
x == y  # Checa si son iguales
x != y  # Checa si no son iguales

# Expresiones booleanas compuestas
# Podemos checar diferentes condiciones booleanas al mismo tiempo al usar los tres operadores booleanos básicos:
# and: será verdadero si todas las condiciones son verdaderas
# or: será verdadero si al menos una condición es verdara
# not: invierte el valor boolean
x > 3 and x != 6  # Será verdadero únicamente si x es mayor que tres Y no es igual que seis
x >= 1 or x < -3  # Será verdadero si x es mayor o igual que 1 o si x es menor que -3
not x < 3  # Será verdadero si x no es menor que 3

# Se pueden construir comparaciones complejas con esta sintaxis, como por ejemplo
not (x < 3 and x != 1) and (not y == 1 or (y == x and y ** x <= 1))

# Si se quiere checar si un número está entre un rango de valores, se puede usar la expresión simplificada
# En vez de hacer x > a and x <= b, podemos escribir:
a < x <= b  # Se puede usar mayor, mayor igual, menor o menor igual.
