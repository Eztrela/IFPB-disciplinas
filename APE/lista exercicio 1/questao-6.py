cotacao = int(input('Digite o valor da cotacao US$ '))
valor_converter = int(input('Digite o valor a ser convertido US$ '))

print( f'O usuario possui US$ {valor_converter:.2f}, e converteu utilizando a cotacao de US$ 1,00 para R${cotacao:.2f},' 
        'e obteve R${cotacao*valor_converter:.2f} como resultado da conversao')
