# 16. Escribe un programa que imprima una grafica de barras de las vocales en una oracion. Por ejemplo, para la oracion:
# "me gusta tomar clases de Python en la universidad" debe de imprimir:
#     a: *****
#     e: *****
#     i: **
#     o: **
#     u: **

texto = input("Introduzca una oracion: ")

a = 0
e = 0
i = 0
o = 0
u = 0

for caracter in texto:
    if caracter == "a" or caracter == "A":
        a += 1
    if caracter == "e" or caracter == "E":
        e += 1
    if caracter == "i" or caracter == "I":
        i += 1
    if caracter == "o" or caracter == "O":
        o += 1
    if caracter == "u" or caracter == "U":
        u += 1

print(f"a: {'*' * a}")
print(f"e: {'*' * e}")
print(f"i: {'*' * i}")
print(f"o: {'*' * o}")
print(f"u: {'*' * u}")