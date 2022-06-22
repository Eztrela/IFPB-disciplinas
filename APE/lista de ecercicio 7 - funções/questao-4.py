def soma(vetor):
  soma = 0
  for numero in vetor:
    soma += numero
  return soma

numeros = map(int,input(f'Digite numeros separados por espaço').split())

print(soma(numeros))