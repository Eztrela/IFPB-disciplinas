maior = 0
for i in range(5):
    numero = int(input('Digite o numero: '))
    if (i == 0):
        maior = numero
    if(numero > maior):
        maior = numero

print(f'{maior} é o maior dentre os digitados')