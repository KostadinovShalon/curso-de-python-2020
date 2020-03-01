# Un string es básicamente un texto. En inglés significa cadena. Es llamado así porque
# es una cadena de caracteres. En otros lenguajes de programación los caracteres son un tipo de dato diferente
# a los strings. Un string es un texto encerrado entre comillas simples o dobles
texto = "Este es un texto muy bonito"
texto2 = 'Este es otro texto muy bonito pero con comillas sencillas. No hay diferencia!'

# En Python la única forma de representar un caracter es básicamente como una cadena de un solo caracter
char = 'a'

# Los textos se pueden concatenar usando el operador +
nombre = "Miguel"
apellido = "Farías"  # En Python se pueden usar los caracteres de Unicode por default
nombre_completo = nombre + apellido
print(nombre_completo)  # Al imprimir saldrá MiguelFarías
# Podemos concatenar variables string con literales string (o sea, expresiones sin estar asignadas a una variable)
print(nombre + " " + apellido)  # Esto imprimirá Miguel Farías porque concatenamos una literal que es un espacio

# Las cadenas también se pueden multiplicar, esto genera una repetición de la cadena
print(nombre * 5)  # Esto imprimirá MiguelMiguelMiguelMiguelMiguel

# No se pueden concatenar strings con otras variables
edad = 25
print("Hola " + nombre + ", tienes " + edad + " años")  # generará error

# Para concatenar una variable que no sea string, podemos convertirla envolviendola dentro de str()
print("Hola " + nombre + ", tienes " + str(edad) + " años")

# Hacer este tipo de conversión se le conoce como "casting".
edad_en_texto = "25"
edad_en_numero = int(edad_en_texto)  # Convierte a entero
x = float(2)  # Convierte a flotante
y = int(3.14)  # Convierte a enter, en este caso, a 3
z = float("3.14")  # Convierte a flotante
q = int("Esto no es un entero!")  # Genera error porque no se puede hacer la conversión

# En Python 3, se pueden crear textos usando los valores de las variables sin tener que explicitamente
# concatenar con +, agregando la letra f antes de la definición de la cadena, por ejemplo:
nombre_con_saludo = f"Hola {nombre} {apellido}, sé que tú tienes {edad} años."
print(nombre_con_saludo)
# En el ejemplo anterior, podemos usar las variables sin convertirlos en string.
# Dentro del formato anterior, podemos introducir otras cadenas dentro de las llaves usando otro tipo de comillas:
nombre_con_saludo = f"Hola {nombre + ' ' + apellido}, sé que tú tienes {edad} años."
otra_forma = f'Hola {nombre + " " + apellido}, sé que tú tienes {edad} años.'

# Longitud de una cadena
# Podemos conocer la longitud de una cadena, esto es, la cantidad de caracteres, usando la función len()
t1 = "Este es un text con muchos caracteres"
print(f"La variable texto tiene {len(t1)} caracteres")

t2 = "No sé por qué escribo tantos textos!"
if len(t1) > len(t2):
    print("El primer texto es más largo que el segundo")
elif len(t1) < len(t2):
    print("El segundo texto es más largo que el primero")
else:
    print("Ambos textos son de la misma longitud")

# Indexación
# Podemos acceder a un caracter específico de una cadena indicando su índice
# La sintazis es: cadena[índice].
# Los índices en Python empiezan desde 0.
print(f"El primer caracter de t1 es {t1[0]}")
print(f"El octavo caracter de t2 es {t2[7]}")
# Los índices pueden indicarse con respecto al último caracter con números negativos
print(f"El último caracter de t1 es {t1[-1]}")
print(f"El tercer último caracter de t2 es {t2[-3]}")

# Slicing
# Podemos obtener una subcadena  de una cadena con la sintaxis:
# cadena[inicio:final+1]
# O sea, si queremos la subcadena del segundo al quinto caracter usamos
subcadena = texto[1:5]  # Como empieza en el segundo, y los índices son desde 0, pues empezamos en 1
# Como terminmos en el quinto caracter, o sea, el índice 4, tenemos que poner 4 + 1 = 5 como el final.

# Si vamos a iniciar desde el primer caracter, podemos omitir el 0
subcadena = texto[0:3]  # es lo mismo que:
subcadena = texto[:3]

# De igual manera podemos elegir los caracteres desde el principio hasta el final omitiendo segundo límite
# Una forma de ir desde el segundo caracter hasta el último caracter es
subcadena = texto[1:len(texto) - 1]
# Una forma más entendible es
subcadena = texto[1:]

# INPUT
# Podemos hacer que el usuario introduzca valores usando la función input(texto que aparecerá)
nombre = input("Introduzca su nombre: ")
apellido = input("Introduzca su apellido: ")
print(f"Hola {nombre} {apellido}")

# Los valores introducidos por el input son siempre cadenas. Se puede hacer un casting al valor que se requiera
edad = int(input("Introduzca su edad: "))
anio_de_nacimiento = 2020 - edad
print(f"Tu naciste entre {anio_de_nacimiento - 1} y {anio_de_nacimiento}")

pi = 3.1416
radio = float(input("Radio: "))
print(f"Área: {pi * radio ** 2}")
