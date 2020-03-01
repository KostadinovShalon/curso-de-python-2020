# El while es un ciclo que va a repetir un código siempre que se cumpla una condición. Sintaxis:
# while condición:
#     código que se va a ejecutar

# En este ejemplo vamos a imprimir la tabla del 7

base = 7
n = 1
while n <= 10:  # El código se va a repetir siempre que n sea menor o igual que 10
    valor = base * n
    print(f"{base}\tx\t{n}\t=\t{valor}")  # \t es un tabulador
    n = n + 1  # Incrementamos n en 1. Si no lo incrementáramos el ciclo se repetiría indefinidamente

# Cuando queremos modificar una variable basados en su valor actual podemos escribir
# la notación simplificada que es la operación seguida de un igual
n += 1  # Es lo mismo que n = n + 1
n -= 3  # Es lo mismo que n = n - 3
n *= 2  # Es lo mismo que n = n * 2

# Vamos a imprimir los valores de la serie 1/1, 1/2, 1/4, 1/8, ..., 1/2^n mayores de 0.0000001
n = 1
while n > 0.0000001:
    print(n)
    n /= 2

# Break
# Podemos terminar un ciclo usando la sentencia break
# Encontrar un número divisible entre 11 y 12
x = 1
while True:  # Esto es un ciclo infinito, únicamente sale con el break
    if x % 11 == 0 and x % 12 == 0:
        print(f"{x} es divisible entre 11 y 12")
        break
    x = x + 1

# Los ciclos infinitos se pueden usar para correr un programa indefinidamente hasta que el usuario quiera
print("Introduzca un entero para obtener sus factores o un número negativo para salir")
while True:
    a = int(input("Entero: "))
    if a < 0:
        print("Saliendo")
        break
    else:
        n = 1
        while n <= a:  # Se pueden anidar whiles dentro de whiles!
            if a % n == 0:
                print(n)
            n += 1

