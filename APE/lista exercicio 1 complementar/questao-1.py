nome = input('Digite o nome do vendedor: ')
carros_vendidos = int(input('Digite o numero de carros vendidos: '))
vendas = int(input('Digite o valor total das vendas desse vendedor: '))

salario =float(1000 + (carros_vendidos * 200) + (vendas * 0.05))

print(f'O vendedor {nome} teve o salario de R$ {salario:.2f}')