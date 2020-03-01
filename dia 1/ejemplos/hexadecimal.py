# En un numero hexadecimal, cada posicion del numero esta multiplicado por 16^posicion
# Los digitos son del 0 al 9 y A, B, C, D, E, F, valiendo 10, 11, 12, 13, 14, y 15
# Por ejemplo, el numero hexadecimal E4 = 14 x (16 ^ 1) + 4 x (16 ^ 0) = 14 x 16 + 4 x 1 = 224 + 4 = 228
# Otro ejemplo: hexadecimal: 123, en decimal es: 1x(16^2) + 2x(16^1) + 3x(16^0) =  1x256 + 2x16 + 3x1 = 291

# Vamos a crear un programa que pida un numero hexadecimal al usuario e imprima su version decimal
numero = input("Introduzca un numero hexadecimal: ")

posicion = len(numero) - 1  # El digito mas a la izquierda de un numero hexadecimal estara multiplicado por 16^digitos-1

decimal = 0
for digito in numero:  # Los string son secuencias, asi que pueden ser usados en los ciclos for y leer cada caracter

    # Cuando una instruccion es muy larga, la podemos "romper" con un backslash \
    # Veremos mas adelante como hacer este if mas corto
    if digito == 'A' or digito == 'B' or digito == 'C' or digito == 'D' or digito == 'E' or digito == 'F' or \
            digito == 'a' or digito == 'b' or digito == 'c' or digito == 'd' or digito == 'e' or digito == 'f':
        if digito == 'A' or digito == 'a':
            valor_numerico = 10
        elif digito == 'B' or digito == 'b':
            valor_numerico = 11
        elif digito == 'C' or digito == 'c':
            valor_numerico = 12
        elif digito == 'D' or digito == 'd':
            valor_numerico = 13
        elif digito == 'E' or digito == 'e':
            valor_numerico = 14
        else:
            valor_numerico = 15
    else:
        valor_numerico = int(digito)  # NOTA: si una variable esta declarada en todos los posibles casos de una secuencia
        # de if-else (incluidos anidados), entonces no tenemos que inicializarlo
    decimal += valor_numerico * 16 ** posicion
    posicion -= 1

print(f"{numero} en decimal es {decimal}")

# Para convertir de decimal a hexadecimal hacemos division y modulo

# Primero tenemos que encontrar cuantas posiciones tendra el numero hexadecimal
# Una manera de hacerlo es con un ciclo y encontrar a que potencia tenemos que elevar el 16 para que sea mayor que el
# decimal
numero = int(input("Introduzca un numero decimal: "))

posiciones = 1
while True:
    if 16 ** posiciones > numero:  # Si 16^posiciones es mayor, entonces encontramos cuandos digitos tendra el hex
        break
    posiciones += 1

hexadecimal = ""
resto = numero
for p in range(posiciones, 0, -1):  # Quiero ir decrementando de numero de posiciones hasta 0, en pasos de -1 en -1
    digito = resto // (16 ** (p - 1))  # La division entera nos da el valor del digito
    resto = resto % (16 ** (p - 1))  # El residuo nos da lo que debemos de seguir convirtiendo
    if digito == 10:
        hexadecimal += "A"
    elif digito == 11:
        hexadecimal += "B"
    elif digito == 12:
        hexadecimal += "C"
    elif digito == 13:
        hexadecimal += "D"
    elif digito == 14:
        hexadecimal += "E"
    elif digito == 15:
        hexadecimal += "F"
    else:
        hexadecimal += str(digito)

print(f"{numero} en hexadecimal es {hexadecimal}")
