

print('Escolha o código e a quantidade do seu lanche:')
print('H = Hamburguer\nC = Cheese Burguer\nB = Cheese Bacon\nF = Cheese Frango')
print('Se já terminou, digite x')

PRECO_H = 5
PRECO_C = 6
PRECO_B = 7
PRECO_F = 4
resultado = 0

while pedido != 'x':
    pedido = input('Qual o seu pedido? ').upper()
    quantidade = int(input('Qual a quantidade? '))
    
    if (pedido == 'X'):
        break
    if (pedido == 'H'):
        resultado += PRECO_H * quantidade
    elif (pedido == 'C'):
        resultado += PRECO_C * quantidade
    elif (pedido == 'B'):
        resultado += PRECO_B * quantidade
    elif (pedido == 'F'):
        resultado += PRECO_F * quantidade

 
print(resultado)