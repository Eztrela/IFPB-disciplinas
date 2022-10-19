""" Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor
inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V. """

K = int(input('Valor de K: '))
n = 5
cont = 0
vetor = [None]*n
for indice in range(n):
    vetor[indice] = int(input('Digite um número: '))
    if vetor[indice] == K:
        cont += 1

print(f'A quantidade de ocorrências de K dentro de V é {cont}.')





'''
v = [1, 2, 5, 7, 8]
      0  1  2  3  4


v[0] = 1
 
'''



