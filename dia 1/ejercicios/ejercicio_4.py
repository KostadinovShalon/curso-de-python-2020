# 4. Escribe un programa que devuelva la suma de los digitos de un numero

x = -6868
resto_x = x  # Variable auxiliar para guardar el residuo sin tener que modificar x
suma = 0

# Primero vamos a checar cuantas posiciones tiene el numero.
# Por simplicidad, vamos a considerar numeros enteros unicamente, pero seria un buen ejercicio probar con flotantes
if x < 0:
    total_digitos = len(str(abs(x)))
else:
    total_digitos = len(str(x))

# Otra forma seria tener un while infinito y checar cuando la division entera sea cero
# total_digitos = 1
# while True:
#     # OOPS algo que no mencione, la division entera de un numero negativo con otro positivo es -1 (cosas de Python)
#     # Por lo tanto solo checamos el valor absoluto
#     if abs(x) // (10 ** (total_digitos + 1)) == 0:
#         break
#     total_digitos += 1

for posicion in range(total_digitos, -1, -1):
    suma += abs(resto_x) // (10 ** posicion)
    resto_x = abs(resto_x) % (10 ** posicion)

print(f"La suma de los digitos de {x} es {suma}")
