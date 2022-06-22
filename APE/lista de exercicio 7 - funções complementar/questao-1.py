def vogal(letra):
  if letra in 'aeiouAeiou':
    return True
  else:
    return False

frase = input(f'Digite uma frase: ')
cont_vogais = 0
for letra in frase:
  if(vogal(letra)):
    cont_vogais +=1

print(f'A quantidade de Vogais na frase é {cont_vogais}')