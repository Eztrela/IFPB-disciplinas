n = int(input("Digite o valor da ordem: "))

matriz_a = [[None]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        matriz_a[i][j] =int(input(f'Digite o valor de matriz{[i]}{[j]}'))

permutacao = True

for i in range(n):
  soma = 0
  for j in range(n):
    if (matriz_a[i][j] == 1):
      soma += 1
      print (soma)
  if (soma >= 2 or soma <= 0):
    permutacao = False
    break

for i in range(n):
  soma = 0
  for j in range(n):
    if (matriz_a[j][i] == 1):
      soma += 1
      print (soma)
  if (soma >= 2 or soma <= 0):
    permutacao = False
    break
    
if (permutacao):
  print(f'a matriz é uma matriz permutação')
else:
  print(f'a matriz não é uma matriz permutação')