while(True):
    matricula = int(input('Digite a matricula do aluno: '))
    if (matricula == 0):
        break
    nome = input('Digite o nome do aluno: ')
    nota1 = int(input('Digite a nota do aluno na avaliaçao 1: '))
    nota2 = int(input('Digite a nota do aluno na avaliaçao 2: '))
    media = (nota1+nota2)/2

    if (media >= 7):
        print(f'o aluno(a) de matricula: {matricula} e nome: {nome}, possui media igual a: {media} portanto está aprovado(a)')
    else:
        print(f'o aluno(a) de matricula: {matricula} e nome: {nome}, possui media igual a: {media} portanto estáreprovado(a)')