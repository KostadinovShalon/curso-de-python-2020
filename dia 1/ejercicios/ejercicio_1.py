# 1. Un numero primo es aquel que solo puede ser divido entre 1 o si mismo. Escribe un programa que encuentre e
# imprima los primeros n numeros primos.

n = 20  # Total de primos
total_primos = 0  # Contador para saber cuantos primos ya imprimomos
x = 2  # Empezamos en 2 porque 1 no es primo por definicion
output = ""  # Cadena que vamos a usar para imprimir. Tambien podriamos imprimir cada vez que encontremos uno numoer
# pero se imprimirian en una columna. Aqui hare un ejemplo de como dar un poco de formato

while total_primos < n:
    es_primo = True  # Variable que me indica si el numero es primo
    for numero in range(2, x // 2 + 1):  # Entre 2 porque ninguno numero n es divisible entre (n / 2) + k, con k > 1
        if x % numero == 0:  # Si encuentro un divisor, no es primo
            es_primo = False
            break  # Aunque tenemos un for dentro de un while, el break aplica al loop mas cercano (en este caso el for)
    if es_primo:
        output += f"{x}\t"  # Si encontramos un primo, lo concatenamos a la salida. \t es un tabulador
        total_primos += 1
        if total_primos % 10 == 0:
            # Ademas, no quiero imprimirlos en una sola fila. Voy a agregar una nueva linea, o sea, un \n
            # cada 10 primos
            output += "\n"
    x += 1
print(output)
