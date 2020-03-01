# Este programa lee 5 numeros del usuario e imprime una grafica de barras horizontal

grafica = ""  # Inicializo como si fuera una cadena de texto vacia
caracter_de_la_grafica = "*"
for i in range(5):
    x = int(input(f"Introduzca el valor {i}: "))
    grafica += "x" + str(i + 1) + ": " + caracter_de_la_grafica * x + "\n"  # Aqui estoy concatenando un salto de linea, que se representa por \n
print(grafica)
