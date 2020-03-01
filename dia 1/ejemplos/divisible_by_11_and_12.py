# Primeros n números divisibles entre 11 y 12
x = 1
n = 5
found = 1

while True:
    if x%11 == 0 and x % 12 == 0:
        print(x)
        if found == n:
            break
        found = found + 1
    x = x + 1
