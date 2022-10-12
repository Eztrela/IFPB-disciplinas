matricula = int(input('Digite sua matricula: '))
while matricula != 0:
    nome = input('Digite seu nome: ')
    nota1 = int(input('Digite sua nota 1: '))
    nota2 = int(input('Digite sua nota 2: '))
    media = (nota1 + nota2) / 2
    if media >= 7:
        print(f'O Aluno de matricula: {matricula} nome {nome} obteve media {media} e foi Aprovado')
    else:

        print(f'O Aluno de matricula: {matricula} nome {nome} obteve media {media} e foi Reprovado')
    matricula = int(input('Digite sua matricula: '))