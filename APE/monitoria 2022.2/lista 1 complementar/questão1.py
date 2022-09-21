#Constantes
salarioBase = 1000
comissao = 200
comissao2 = 0.05


#Leitura da Entrada dos dados
nome = input('Qual o nome do usuario? ')
carrosVendidos = int(input('Quantos carros foram vendidos: '))
totalVendas = float(input('Qual o valor total da venda: '))

#Expressão que realiza o calculo do salario total do vendedor e armazena na variavel salario
salario = salarioBase + (carrosVendidos * comissao) + (comissao2 * totalVendas)

#Exibe o Salario Total
print(f'O salario total mensal do vendedor foi de: {salario}')

'''
fixo = 1000.00
com = 200.00
perc = 5/100

vendedor = input('Nome do vendedor: ')
numcarros = int(input('Número de carros vendidos: '))
totvendas = float(input('Valor total das vendas: R$ '))

salario = fixo + numcarros*com + totvendas*perc

print(f'Salário: R$ {salario:.2f}')
'''
