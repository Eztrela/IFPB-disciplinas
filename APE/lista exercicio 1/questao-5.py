nome = input('Digite o nome seguido do sobrenome separado por virgula: ').split('","')

print (f'{nome[1][0:len(nome[1])-1]}, {nome[0][1:len(nome[0])]}')
print (f'{nome[1].strip(""")}, {nome[0][1:len(nome[0])]}')