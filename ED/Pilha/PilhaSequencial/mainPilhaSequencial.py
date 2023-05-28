#Inicialização
from pilhaSequencial import *


numeros = [4,5,6,90,56,31,42,57]
numeros2 = [7,8,9,9,9,10,16,82,58]
pilha = pilhaSequencial()
pilha2 = pilhaSequencial()
for n in numeros:
    pilha.empilha(n)
for n in numeros2:
    pilha2.empilha(n)

print(f'Pilha: {pilha}')

#Testando modificação
pilha.modificar(3, 69420)
print(f'Pilha : {pilha}')

#Testando pesquisas
print(pilha.elemento(3))
print(pilha.busca(57))
print(pilha.busca(4))
print(pilha.busca(69420))

#print(f'Topo : {pilha.dados[-1]}')

#Testando desempilhamento (somente do topo)
print(pilha.desempilha())

#print(f'Pilha : {pilha}')

print(f'Pilha antes: {pilha}')
pilha.inverte()
print(f'Pilha depois: {pilha}')
#print(f'Pilha 2 : {pilha2}')

# CONCATENAÇÃO UNÁRIA
#pilha.concatenar(pilha2)
#print(f'Pilha : {pilha}')

# CONTATENAÇÃO BINÁRIA
#newpilha = pilha.doubleconcatenar(pilha, pilha2)
#print(f'Pilha : {newpilha}')
'''

TESTES DO PROF ALEX

string = 'Instituto Federal da Paraiba'
pilha.esvazia()
print(string)
for s in string:
    pilha.empilha(s)
print()

while(not pilha.estaVazia()):
   print(pilha.desempilha(),end='')



try:
    print
    print(pilha.busca(90))
except PilhaException as pe:
    print(pe)
'''
#converte para binario usando pilha
def binario(alvo: int):
    bin = pilhaSequencial()
    i = alvo
    if alvo == 0:
        out = '0'
    else:                    
        while i != 0:
            bin.empilha(i % 2)
            i = i // 2                    
        out = ''
        while not bin.estaVazia():
            out+=f'{bin.desempilha()}'

    print(f'{alvo} em binário é {out}!')

binario(0)
binario(1)
binario(5)
binario(10)
binario(256)
binario(511)
binario(512)

def binario(valor:int):
    