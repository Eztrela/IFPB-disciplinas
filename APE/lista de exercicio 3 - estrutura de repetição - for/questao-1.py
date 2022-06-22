import math

for numero in range(50,301,5):
    raiz = math.sqrt(numero)
    cubo = numero ** 3
    print(f'{numero:10.2f}|{raiz:10.2f}|{cubo:15.2f}')