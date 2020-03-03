# 3. Modifica el programa anterior para que el usuario pueda seguir ingresando numeros e imprima si
# son divisibles entre 4 o 7, hasta que introduzca la tecla 's' y salga del programa.
# Pista: usa un while y un break.

while True:
    x = input("Introduzca un numero del 1 al 10 [o presione 's' para salir]: ")#
    if x == 's' or x == 'S':
        print("BYE!")
        break
    x = int(x)
    if x % 4 == 0 or x % 7 == 0:
        print("Es divisible entre 4 o 7!")
    if 1 <= x <= 10:
        for i in range(11):
            print(f"{x}\tx\t{i}\t=\t{x * i}")  # Usamos tabuladores para que tenga forma de tabla y se vea mejor
    else:
        print("Solo se aceptan numeros del 1 al 10")
