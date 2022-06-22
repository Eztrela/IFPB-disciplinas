import random
matriz_a = [[None]*3 for i in range(2)]
matriz_b = [[None]*3 for i in range(2)]
matriz_c = [[None]*3 for i in range(2)]

for i in range(2):
    for j in range(3):
        matriz_a[i][j] = random.randint(1,50)
        matriz_b[i][j] = random.randint(1,50)
        matriz_c[i][j] = matriz_a[i][j] + matriz_a[i][j]

print(f'Matriz A: ')
for i in range(2):
    for j in range(3):
        print(f'{matriz_a[i][j]}',end=' ')
    print()

print()
print(f'Matriz B: ')
for i in range(2):
    for j in range(3):
        print(f'{matriz_b[i][j]}',end=' ')
    print()

print()
print(f'Matriz C: ')
for i in range(2):
    for j in range(3):
        print(f'{matriz_c[i][j]}',end=' ')
    print()
