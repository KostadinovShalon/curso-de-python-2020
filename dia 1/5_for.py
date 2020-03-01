# El for es otro ciclo similar al while. Las diferencias es que en el for se trata de procesar todos
# los casos en un conjunto ordenado, mientras que el while es un ciclo que seguirá mientras se cumpla una condición,
# la cual puede ser indefinida.
# La sintaxis del for es
# for variable in secuencia:
#     codigo

for i in range(0, 10):
    print(f"{i}^2 = {i**2}")

# En este caso la secuencia es representada por la función range.
# La sintaxis es, dependiendo del número de parámetros que se le pasen:
# range(final + 1)  -> secuencia que va desde 0 hasta final
# range(inicio, final + 1)  -> secuencia que va desde inicio hasta final + 1
# range(inicio, final + 1, incremento)  -> secuencia que va desde inicio hasta final + 1 dando pasos definidos por incremento

print("Múltiplos de 4 hasta el 100")
for i in range(1, 101):
    if i % 4 == 0:
        print(i)

# La secuencia también puede ser representada por una lista. Las listas, que veremos más adelante
# se representan por elementos separados por coma en paréntesis cuadrados

for i in [1, 3, 5, 7, 9]:
    print(f"{i}^3 = {i ** 3}")

# Las secuencias definidas por las listas pueden ser de cualquier tipo
for elemento in [1, 8, "que onda", 0.213, None, 2 == 2]:
    print(elemento)

# Otro ejemplo
print("Introduzca un entero para obtener sus factores o un número negativo para salir")
while True:
    a = int(input("Entero: "))
    if a < 0:
        print("Saliendo")
        break
    else:
        for n in range(a):  # Podríamos hacer el range de 1 hasta a + 1, pero también podemos sumar 1 a n
            if a % (n + 1) == 0:
                print(n + 1)

# La secuencia igual puede ser una cadena.
# Imprimiremos los caracteres de un texto
texto = "Esto es un texto!"
for caracter in texto:
    print(caracter)

# Sumar todos los dígitos del 1 al 9

suma = 0
for i in '123456789':
    suma += int(i)
print(suma)