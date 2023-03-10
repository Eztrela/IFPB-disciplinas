valor = int(input('Digite o numero inteiro para conversão: '))

bin = ''

while(valor >= 1):
    bin += str(valor % 2)
    valor = valor // 2
    print(valor)

print(bin[::-1])
