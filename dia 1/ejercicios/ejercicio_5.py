# 5. Escribe un programa que le pida al usuario un numero y lo imprima con los digitos al reves.

# POR SIMPLICIDAD, VAMOS A DEJARLO EN ENTEROS

x = int(input("Introduzca un numero: "))
es_negativo = x < 0  # Variable que nos dira si es negativo para agregar el signo al final
x = str(abs(x))  # Convertimos a string para acceder a sus valores. Usamos absoluto para no contar el signo

salida = ""
for i in range(len(x)):
    salida += x[-1 - i]  # Vamos agregando caracter por caracter pero al reves

# Otra forma seria
# for i in range(-1, -len(x) - 1, -1):
#     salida += x[i]

if es_negativo:
    salida = "-" + salida

print(f"{x} con los digitos al reves es {salida}")