vendas = int(input())
comissao = vendas * 0.05

if(comissao >= 1200):
    print(f'a comissao do funcionario foi acima do minimo')
else:
    print(f'a comissao do funcionario nao ultrapassou o minimo determinado')
