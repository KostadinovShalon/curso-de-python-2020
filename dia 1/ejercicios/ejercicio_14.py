# 14. Escribe un programa que le pida al usuario que ingrese una cadena de texto y checa si dentro del texto ingresado
# se encuentre la frase "no se". Por ejemplo, "El iguano se comio una mosca" si contiene la frase "no se".

frase_a_encontrar = "no se"
texto = input("Introduzca un texto: ")

if len(texto) < len(frase_a_encontrar) or (len(texto) == len(frase_a_encontrar) and texto != frase_a_encontrar):
    print(f'No se encontro la frase "{frase_a_encontrar}" en "{texto}"')
else:
    posiciones_posibles = len(texto) - len(frase_a_encontrar) + 1
    encontrado = False
    for i in range(posiciones_posibles):
        if texto[i:i + len(frase_a_encontrar)] == frase_a_encontrar:
            print(f'Se encontro la frase "{frase_a_encontrar}" dentro de "{texto}"')
            encontrado = True
            break
    if not encontrado:
        print(f'No se encontro la frase "{frase_a_encontrar}" en "{texto}"')


# Una forma mucho mas sencilla de hacer lo anterior en Python es
if frase_a_encontrar in texto:
    print(f'Se encontro la frase "{frase_a_encontrar}" dentro de "{texto}"')
else:
    print(f'No se encontro la frase "{frase_a_encontrar}" en "{texto}"')