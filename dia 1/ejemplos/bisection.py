# Este algoritmo encuentra una solución limitando los valores posibles a un rango cada vez más pequeño
# Dado un rango, se encuentra el punto medio y se verifica si la solución esta entre el inicio y
# el punto medio o entre el punto medio y el inicio.
# Luego, se toma el punto medio como nuevo inicio o final según sea el caso y se vuelve a encontrar otro punto medio
# Así sucesivamente hasta que el intervalo sea lo suficientemente pequeño.

x = 12
eps = 0.01
n = 0
low = 0
high = max(1.0, x)  # Se agrega este max porque si x < 1, la raíz sigue estando en el intervalo de 0 a 1
ans = 0
while abs(ans ** 2 - x) >= eps:  # Mientras no se haya llegado a la precisión requerida
    print(f"low = {low}, high = {high}, ans = {ans}")
    n += 1
    if ans ** 2 < x:  # Si el punto medio al cuadrado es menor que equis significa que el resultado esta en el intervalo superior
        low = ans
    else:  # Si la raíz cuadrada es mayor, significa que está en el intervalo inferior.
        high = ans
    ans = (high + low) / 2  # Nueva aproximación de la raíz

print(f"num guesses: {n}")
print(f"{ans} is close for square root of {x}")
