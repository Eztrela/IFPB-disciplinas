H = 5
C = 6
B = 7
F = 4
total = 0.0
pedido = input('Diga ocodigo do seu pedido (H C B F): ').upper()
while pedido != 'X':
    quantidade = int(input(f'Digite a Quantidade de {pedido}: '))
    if pedido == 'H':
        total += quantidade * H
    elif pedido == 'C':
        total += quantidade * C
    elif pedido == 'B':
        total += quantidade * B
    else:
        total += quantidade * F
    pedido = input('Diga ocodigo do seu pedido (H C B F): ').upper()
    
print(f'Total A pagar: R$ {total:.2f}')    
