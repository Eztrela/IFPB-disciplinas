#Inicialização
from re import I
from pilhaEncadeada import *


numeros = [4,5,6,90,56,31,42,57]
numeros2 = [7,8,9,9,9,10,16,82,58]
pilha = pilhaEncadeada()
pilha2 = pilhaEncadeada()
for n in numeros:
    pilha.empilha(n)
print(pilha)
for n in numeros2:
    pilha2.empilha(n)

print(pilha.tamanho())

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

# print(f'Pilha antes: {pilha}')
# pilha.inverte()
# print(f'Pilha depois: {pilha}')
# pilha.empilha(33)
#print(f'Pilha 2 : {pilha2}')
# print(f'')
# CONCATENAÇÃO UNÁRIA
#pilha.concatenar(pilha2)
#print(f'Pilha : {pilha}')

# CONTATENAÇÃO BINÁRIA
#newpilha = pilha.doubleconcatenar(pilha, pilha2)
#print(f'Pilha : {newpilha}')

#Subtopo
print(pilha.subTopo())
print(pilha.obtemBase())
print(pilha.tamanho())
print(f'Pilha : {pilha}')
print(f'Desempilhado 4 vezes? : {pilha.desempilha_n(4)}')
print(f'Pilha : {pilha}')

pilha.desempilha()
pilha.desempilha_n(3)
print(pilha)
pilha.esvazia()
print(pilha)
 
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
def prioridade(operador):
    dic = { '(':1 ,'+':2 , '-':2 , '*':3, '/':3 , '^':4}
    return dic[operador]

def convertePosFixa(expressao:str)->str:
    pilha = pilhaEncadeada()
    out = ''
    for i in expressao:
        if(i not in '+-*/()^'):
            out += f'{i}'
        elif( i == '('):
            pilha.empilha(i)
        elif(i == ')'):
            while (pilha.topo() != '('):
                out += f'{pilha.desempilha()}'
            pilha.desempilha() 
        else:
            while(not pilha.estaVazia() and prioridade(pilha.topo()) >= prioridade(i)):
                out += f'{pilha.desempilha()}'
            pilha.empilha(i)
            
        
    while(not pilha.estaVazia()):
        out += f'{pilha.desempilha()}'
    return out

print(convertePosFixa('A-(B^C^(D*E))'))
# ABCD/*+E-

