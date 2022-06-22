import random
#recebendo ordem
n = int(input("Digite o valor da ordem: "))

#criando matriz
matriz_a = [[None]*n for i in range(n)]

#preenchendo matriz com valores aleatorios
for i in range(n):
    for j in range(n):
        matriz_a[i][j] = random.randint(1,5)

#variaveis
soma = 0
soma_principal = 0
soma_secundaria = 0

#somando elementos das diagonais
for i in range(n):
  soma_principal = matriz_a[i][i]
  soma_secundaria = matriz_a[i][n-1-i]

#mostrando resultado da soma das diagonais
print(f'A soma dos elementos da diagonal principal é = {soma_principal}')
print(f'A soma dos elementos da diagonal secundaria é = {soma_secundaria}')
    
#somadno e mostrando elementos das linahs e colunas
for i in range(n):
  soma_linhas = 0
  soma_colunas = 0
  for j in range(n):
    soma_linhas += matriz_a[i][j]
    soma_colunas += matriz_a[j][i]
  print(f'A soma dos elementos da linha {i} é = {soma_linhas}')
  print(f'A soma dos elementos da coluna {i} é = {soma_colunas}')
    
  