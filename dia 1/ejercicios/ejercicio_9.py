# 9. Escribe un programa que convierta de romano a decimal.

numero_romano = "MDCCLXXXII"
numero_decimal = 0

posiciones_leidas = 0

while posiciones_leidas < len(numero_romano):
    valor = numero_romano[posiciones_leidas]
    if valor == "M":
        if posiciones_leidas + 1 < len(numero_romano):
            if numero_romano[posiciones_leidas + 1] == "M":
                if posiciones_leidas + 2 < len(numero_romano):
                    if numero_romano[posiciones_leidas + 2] == "M":
                        numero_decimal += 3000
                        posiciones_leidas += 3
                    else:
                        numero_decimal += 2000
                        posiciones_leidas += 2
                else:
                    numero_decimal += 2000
                    posiciones_leidas += 2
            else:
                numero_decimal += 1000
                posiciones_leidas += 1
        else:
            numero_decimal += 1000
            posiciones_leidas += 1
    elif valor == "D":
        numero_decimal += 500
        posiciones_leidas += 1
    elif valor == "C":
        if posiciones_leidas + 1 < len(numero_romano):
            if numero_romano[posiciones_leidas + 1] == "C":
                if posiciones_leidas + 2 < len(numero_romano):
                    if numero_romano[posiciones_leidas + 2] == "C":
                        numero_decimal += 300
                        posiciones_leidas += 3
                    else:
                        numero_decimal += 200
                        posiciones_leidas += 2
                else:
                    numero_decimal += 200
                    posiciones_leidas += 2
            elif numero_romano[posiciones_leidas + 1] == "M":
                numero_decimal += 900
                posiciones_leidas += 2
            elif numero_romano[posiciones_leidas + 1] == "D":
                numero_decimal += 400
                posiciones_leidas += 2
            else:
                numero_decimal += 100
                posiciones_leidas += 1
        else:
            numero_decimal += 100
            posiciones_leidas += 1
    elif valor == "L":
        numero_decimal += 50
        posiciones_leidas += 1
    elif valor == "X":
        if posiciones_leidas + 1 < len(numero_romano):
            if numero_romano[posiciones_leidas + 1] == "X":
                if posiciones_leidas + 2 < len(numero_romano):
                    if numero_romano[posiciones_leidas + 2] == "X":
                        numero_decimal += 30
                        posiciones_leidas += 3
                    else:
                        numero_decimal += 20
                        posiciones_leidas += 2
                else:
                    numero_decimal += 20
                    posiciones_leidas += 2
            elif numero_romano[posiciones_leidas + 1] == "C":
                numero_decimal += 90
                posiciones_leidas += 2
            elif numero_romano[posiciones_leidas + 1] == "L":
                numero_decimal += 40
                posiciones_leidas += 2
            else:
                numero_decimal += 10
                posiciones_leidas += 1
        else:
            numero_decimal += 10
            posiciones_leidas += 1
    elif valor == "V":
        numero_decimal += 5
        posiciones_leidas += 1
    elif valor == "I":
        if posiciones_leidas + 1 < len(numero_romano):
            if numero_romano[posiciones_leidas + 1] == "I":
                if posiciones_leidas + 2 < len(numero_romano):
                    if numero_romano[posiciones_leidas + 2] == "I":
                        numero_decimal += 3
                        posiciones_leidas += 3
                    else:
                        numero_decimal += 2
                        posiciones_leidas += 2
                else:
                    numero_decimal += 2
                    posiciones_leidas += 2
            elif numero_romano[posiciones_leidas + 1] == "X":
                numero_decimal += 9
                posiciones_leidas += 2
            elif numero_romano[posiciones_leidas + 1] == "V":
                numero_decimal += 4
                posiciones_leidas += 2
            else:
                numero_decimal += 1
                posiciones_leidas += 1
        else:
            numero_decimal += 1
            posiciones_leidas += 1
    else:
        print("NUMERO INCORRECTO")
        break

print(f"{numero_romano} = {numero_decimal}")
