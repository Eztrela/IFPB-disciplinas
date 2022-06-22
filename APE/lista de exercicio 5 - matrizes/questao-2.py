import random

N = int(input('Informe o valor de N: '))
matriz = [[None]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        matriz[i][j] = random.randint(1,20)

print(f'Matriz Lida: ')
for i in range(N):
    for j in range(N):
        print(f'{matriz[i][j]}',end=' ')
    print()

print(f'Elementos da diagonal Principal sao: ', end = ' ')
for i in range(N):
    print(f'{matriz[i][i]}', end = ' ')
