n = int(input("Digite o valor da ordem: "))

matriz_a = [[None]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        matriz_a[i][j] =int(input(f'Digite o valor de matriz{[i]}{[j]}  '))

      
# Variaveis      
magico = True
soma_d_princ = 0
soma_d_secund = 0


#somando elementos da diagonal principal e secundaria
for i in range(n):
  soma_d_princ += matriz_a[i][i]
  soma_d_secund += matriz_a[i][n-1-i]

if(soma_d_princ != soma_d_secund):
  magico = False

else:
  #soma elementos de cada linha e verifica se é igual a soma_d_princ
  for i in range(n):
    soma_lin = 0
    soma_col = 0
    for j in range(n):
      soma_lin += matriz_a[i][j]
      soma_col += matriz_a[j][i]
    if (soma_lin != soma_d_princ):
      magico = False
      break
    if (soma_col != soma_d_secund):
      magico = False
      break

print(f'É magico?')
print('Sim' if magico else 'Não')
    

  
  
