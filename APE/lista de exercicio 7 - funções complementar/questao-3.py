def leitura(N):
  vetor = []
  for i in range(N):
    vetor.append(int(input(f'Digite um valor: ')))
  return vetor
def media(vetor):
  soma = 0
  for num in vetor:
    soma += num
  return soma/len(vetor)

def contador(vetor, num):
  return vetor.count(num)

vetor = leitura(5)
buscado =  int(input(f'digite o valor a ser buscado no vetor: '))
print(media(vetor))
print(f'O numero {buscado} apareceu {contador(vetor,buscado)} no vetor')