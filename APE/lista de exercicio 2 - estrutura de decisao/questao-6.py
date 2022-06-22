nome = input()
conceito = input()

if(conceito == 'A'):
    print(f'o aluno {nome} é fortemente recomendado para a vaga')
elif(conceito == 'B'or conceito == 'C'):
    print(f'o aluno {nome} é recomendado para a vaga')
else:
    print(f'o aluno {nome} nao é recomendado para a vaga')