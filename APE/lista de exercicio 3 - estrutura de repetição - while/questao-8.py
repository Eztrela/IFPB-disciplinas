total = 0

while(True):
    codigo = input('Informe o codigo: ').lower()
    if (codigo == 'x'):
        break
    quantidade = int(input('Informe a quantidade: '))
    
    if (codigo == 'h'):
        total += quantidade * 5
    elif (codigo == 'c'):
        total += quantidade * 6
    elif (codigo == 'b'):
        total += quantidade * 7
    elif (codigo == 'f'):
        total += quantidade * 4

print(f'Total a pagar: R$ {total:.2f}')