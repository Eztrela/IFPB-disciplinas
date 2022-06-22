import random

N = int(input('Informe o valor de N: '))
matriz_a = [[None]*N for i in range(N)]
matriz_b = [[None]*N for i in range(N)]

for i in range(N):
    for j in range(N):
        matriz_a[i][j] = random.randint(1,20)


for i in range(N):
    for j in range(N):
        if (i == j):
            matriz_b[i][j] = 0
        elif(i == N -1 -j):
            print('Entrei aqui')
            matriz_b[i][j] = 0  
        else:
            matriz_b[i][j] = matriz_a[i][j] + i + j
'''       
for i in range(N):
    for j in range(N):
        if(i == N -1 -j):
            print('Entrei aqui')
            matriz_b[i][j] = 0
'''
print(f'Matriz A: ')
for i in range(N):
    for j in range(N):
        print(f'{matriz_a[i][j]}',end=' ')
    print()

print(f'Matriz B: ')
for i in range(N):
    for j in range(N):
        print(f'{matriz_b[i][j]}',end=' ')
    print()