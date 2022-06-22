nome = input('Digite o nome do aluno: ')
notas = map(float, input('Quais as notas do aluno: ').split(' '))

print(f'O aluno {nome} obteve media aritmetrica de {sum(notas)/3:.2f}')