menor = 0
maior = 0
contador = 0

while(True):
    numero = int(input('Digite o numero: '))
    contador += 1
    if (contador == 1):
        maior = numero
        menor = numero
    if numero == 0:
        break
    else:
        if(numero > maior):
            maior = numero
        if(numero < menor):
            menor = numero
        
print(f'o maior numero é {maior} e o menor é {menor}')