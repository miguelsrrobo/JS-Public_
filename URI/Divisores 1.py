numero = int(input())
b = numero
while b != 0:
    if numero % b == 0:
        print(int(numero/b))
    b -= 1