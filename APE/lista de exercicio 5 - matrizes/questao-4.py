import random

matriz = [[None]*4 for i in range(20)]

for i in range(20):
    soma_notas = 0
    for j in range(4):
        if (j < 3):
            matriz[i][j] = random.randint(1,10)
            soma_notas += matriz[i][j]
        else:
            matriz[i][j] = soma_notas/3

print(f'Notas Alunos: ')
for i in range(20):
    for j in range(4):
        print(f'{matriz[i][j]:5.2f}',end=' ')
    print()
soma_medias = 0
for i in range(20):
    soma_medias += matriz[i][3]

media_geral = soma_medias/20

print(f'A media geral da turma {media_geral}')

alunos_aprovados = 0

for i in range(20):
    if(matriz[i][3] >= media_geral):
        alunos_aprovados += 1

print(f'O numero de alunos com media acima da media geral da turma é {alunos_aprovados} Alunos')