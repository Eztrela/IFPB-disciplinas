def matriz(N):
  matriz = []
  for i in range(N):
    linha = []
    for j in range(N):
      linha.append(int(input(f'Digite o numero da matriz{[i]}{[j]}: ')))
    matriz.append(linha)
  return matriz

def imprime_matriz(m):
  for i in range(len(m)):
    for j in range(len(m[0])):
      print(f'{m[i][j]}', end = ' ')
    print('\n')

def soma_matrizes(matriz1, matriz2):
  matriz_result = [[None]*len(matriz1) for i in range(len(matriz1[0]))]
  for i in range(len(matriz1)):
    for j in range(len(matriz1[0])):
      matriz_result[i][j] = matriz1[i][j] + matriz2[i][j]
  return matriz_result


ordem = int(input(f'Digite a Ordem das matrizes: '))
matriz1 = matriz(ordem)
matriz2 = matriz(ordem)

print(f'\nMatriz 1 : \n')
imprime_matriz(matriz1)

print(f'Matriz 2 : \n')
imprime_matriz(matriz2)
print(f'Matriz Soma: \n')
imprime_matriz(soma_matrizes(matriz1, matriz2))