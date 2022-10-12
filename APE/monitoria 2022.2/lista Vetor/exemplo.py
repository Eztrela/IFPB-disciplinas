tamanho = int(input())

ind = 0
nome = [None]*tamanho
while True:
    x = int(input())
    if x == 0:
        break
    nome[ind] = x
    ind += 1

indice = 0
while nome[indice] != None:
    indice += 1
print(indice - 1)
print(nome)