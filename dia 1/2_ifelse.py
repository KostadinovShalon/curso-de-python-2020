# A veces queremos hacer ciertas acciones únicamente cuando se cumplan ciertas condiciones.
# Para ello usamos la instrucción "if". Su sintaxis es:
# if condicion:
#     escribir instrucciones

x = 1
if x > 1:
    print("X es mayor que 1")

# IMPORTANTE: cuando se escribe un if, las instrucciones que vamos a seguir dentro del if
# tienen que estar cuatro espacios (o un tab) de la columna de donde inicia el if. Esta extra espacio
# se le conoce como identación. A diferencia de otros lenguajes de programación, en Python no hay las llaves {}
# para señalar los bloques de instrucción del if. Cuando queramos "salir" del if, solo regresamos al mismo nivel
# de identación. Por ejemplo

condicion = True
if condicion:
    print("Aqui estoy dentro del IF!")
    print("Aqui sigo adentro")
print("Aqui ya no!")

# Si queremos realizar una acción únicamente si no se cumple la condición del if, usamos el "else". Su sintaxis es:
# if condicion:
#     código si se cumple la condición
# else:
#     código si no se cumple la condición

x = 18
if x % 2 == 0:  # Aquí estoy checando que el residuo de la división entre 2 sea cero. O sea, que sea par
    print("X es par")
else:
    print("X es impar")

# Si se quieren checar múltiples condiciones, podemos usar la instrucción "elif". Además, también podemos
# tener if dentro de otro if. Solo recuerden que la identación nos indica en dónde se está ejecutando
# el programa. Por ejemplo, este código detecta si un número es divisible entre 2 y 3.

if x % 2 == 0:  # Checo si es divisible entre 2
    if x % 3 == 0:  # Como ya se que es divisible entre 2, checo ahora el 3
        print("X es divisible entre 2 y 3")
    else:  # Aqui ya sabia que era divisible entre 2 pero ahora se que no entre tres
        print("X es divisible entre 2")
elif x % 3 == 0:  # Voy a checar esta condición únicamente si no fue divisible entre 2
    print("X es divisible entre 3")
else:  # Como no se cumplieron las condiciones de arriba, entonces ahora sé que no es divisible entre 2 o 3
    print("X no es divisible ni entre 2 ni entre 3")

# Se pueden usar laos elif que se quieran y el else es opcional. Otra forma de escribir el código anterior es
if x % 2 == 0 and x % 3 == 0:
    print("X es divisible entre 2 y 3")
elif x % 2 == 0:
    print("X es divisible entre 2")
elif x % 3 == 0:
    print("X es divisible entre 3")

# La única diferencia es que no estoy escribiendo nada si no resulta ser divisible ni entre 2 o 3.
# Otro ejemplo, sea [a, b] un rango, queremos saber si x está dentro del rango, fuera del rango o en los bordes:

a, b = 1, 5
x = 3
if x == a or x == b:
    print("X está en los bordes del rango")
elif a < x < b:
    print("X está dentro del intervalo")
else:
    print("X está fuera del rango")
