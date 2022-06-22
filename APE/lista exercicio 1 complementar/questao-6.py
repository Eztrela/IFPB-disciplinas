saque = int(input('digite um valor a ser sacado: '))

notas_50 = 0
notas_10 = 0
notas_5 = 0
notas_1 = 0

notas_50 = saque//50
saque = saque % 50
notas_10 = saque//10
saque = saque % 10
notas_5 = saque//5
saque = saque % 5
notas_1 = saque


print(  f'{notas_50} notas de B$ 50\n'
        f'{notas_10} notas de B$ 10\n'
        f'{notas_5} notas de B$  5\n'
        f'{notas_1} notas de B$  1')