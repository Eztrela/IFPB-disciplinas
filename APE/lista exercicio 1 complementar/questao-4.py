inicio = int(input('Hodometro antes da viagem: '))
fim = int(input('Hodometro depois da viagem: '))
gasto_combustivel = int(input('Quantos litros de combustivel foram gastos: '))
preco_combustivel = int(input('Qual o preco do combustivel: '))
tanque = int(input('Qual a capacidade do tanque de combustivel do veiculo: '))
viagem = fim - inicio
consumo = viagem/gasto_combustivel

print(f'{viagem} Km foram percorridos')
print(f'{viagem/gasto_combustivel} km/l de media de consumo')
print(f'{consumo * tanque} Km de autonomia')
print(f'R$ {gasto_combustivel * preco_combustivel} foram gastos em combustivel nesta viagem')