""" Escreva um programa que leia um vetor V contendo N elementos inteiros (N será
lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver,
informe em que posição (índice).
Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K
aparece. """

k = int(input('Valor de K: '))
n = int(input('Valor de N: '))
vetor = [None]*n
apariçoes = [None]*n
aparece = False
for indice in range(n):
    vetor[indice] = int(input('Digite um número: '))
    if vetor[indice] == k:
        aparece = True
        apariçoes[indice] = indice

print(vetor)
print(apariçoes)

print('O valor de K aparece na posição ', end='')
for i in range(n):
    if apariçoes[i] != None:
        print(f'{i + 1}', end=' ')        

if aparece == False:
    print('O valor de K não aparece no vetor.')   

