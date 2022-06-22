nome = input('Digite seu nome: ').upper().split()
resultado = nome[-1]+ ', '
for i in range(len(nome)-1):
  resultado += nome[i][0]+'. '
print(resultado.rstrip())