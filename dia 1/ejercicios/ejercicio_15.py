# 15. Pidele al usuario que ingrese una lista de palabras y le digas cual fue la mas larga. Recuerda que deben de ser
# palabras, por lo que frases no cuentan!

palabra_mas_larga = ""

while True:
    palabra = input("Introduzca una palabra [O introduzca * para salir]: ")
    if palabra == "*":
        break
    palabra_valida = True
    for caracter in palabra:
        if caracter == ' ':
            palabra_valida = False
            print("No cuentan frases!! Intenta de nuevo")
            break
    if palabra_valida:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
print(f"La palabra mas larga introducida fue {palabra_mas_larga}")