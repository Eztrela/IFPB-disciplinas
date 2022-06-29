N = int(input())
nomes = [None]*N


for i in range(N):
    nomes[i] = input().upper()

print('\n')
contador = 0


for i in range(N):
    if(nomes.count(nomes[i]) <= 1):
        print(nomes[i])
    elif(nomes.index(nomes[i]) == i):
        print(nomes[i])
    
    


'''
for i in range(N):
    nome = input().upper()
    if(nome not in nomes):
        nomes.append(nome)
for nome in nomes:
    print(nome)
'''