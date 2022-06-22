num1 =  int(input())
num2 =  int(input())
cont = 1
descartar = num1
atualizar = num2
aux = 0
while (True):
    aux = atualizar
    atualizar %= descartar
    descartar = aux
    if (atualizar == 0):
        break

print(f'O MDC entre {num1} e {num2} é: {descartar}')
    