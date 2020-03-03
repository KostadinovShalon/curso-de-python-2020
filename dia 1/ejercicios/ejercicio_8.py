# 8. Escribe un programa que convierta un numero decimal del 1 al 3999 a romano. Pista: checar el programa
# hexadecimal.py en los ejemplos.

n = 1209

um = n // 1000
r = n % 1000

c = r // 100
r = r % 100

d = r // 10
u = r % 10

romano = ""
if um > 0:
    romano += "M" * um
if c > 0:
    if 1 <= c <= 3:
        romano += "C" * c
    elif c == 4:
        romano += "CD"
    elif 5 <= c <= 8:
        romano += "D" + "C" * (c - 5)
    else:
        romano += "CM"
if d > 0:
    if 1 <= d <= 3:
        romano += "X" * d
    elif d == 4:
        romano += "XL"
    elif 5 <= d <= 8:
        romano += "L" + "X" * (d - 5)
    else:
        romano += "XC"
if u > 0:
    if 1 <= u <= 3:
        romano += "I" * u
    elif u == 4:
        romano += "IV"
    elif 5 <= u <= 8:
        romano += "V" + "I" * (u - 5)
    else:
        romano += "IX"
print(f"{n} en romano es {romano}")
