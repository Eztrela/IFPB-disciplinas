contador = 0
soma = 0

while(True):
    numero = int(input('Digite o numero: '))
    if (numero == 999):
        break
    else:
        soma += numero
        contador += 1

media = soma / contador

print(f'a media é: {media}')
