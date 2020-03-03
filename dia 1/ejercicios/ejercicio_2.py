# 2. Pedirle al usuario que ingrese un numero del 1 al 10 e imprimir la tabla de multiplicar de dicho numero. Si el
# usuario ingresa un numero no valido, indicarlo.

x = int(input("Introduzca un numero del 1 al 10: "))
if 1 <= x <= 10:
    for i in range(11):
        print(f"{x}\tx\t{i}\t=\t{x * i}")  # Usamos tabuladores para que tenga forma de tabla y se vea mejor
else:
    print("Solo se aceptan numeros del 1 al 10")