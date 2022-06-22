def media(nota1, nota2, nota3):
  return (nota1+nota2+nota3)/3

def conceito(media):
  if (media >= 8):
    print(f'O conceito do aluno foi A')
  elif (media >= 5):
    print(f'O conceito do aluno foi B')
  else:
    print(f'O conceito do aluno foi C')

nota1 = float(input(f'Digite o numero 1: '))
nota2 = float(input(f'Digite o numero 1: '))
nota3 = float(input(f'Digite o numero 1: '))

media = media(nota1,nota2,nota3)
print(f'a media do aluno foi: {media}')
conceito(media)