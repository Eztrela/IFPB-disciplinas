num = int(input('Digite o valor de N:'))
soma = 0 
for numero in range(1,num+1):
    print(f'\nNa iteração {numero} o numero assumiu o valor: {numero}.')
    soma += numero
    print(f'E a soma esta com valor acumulado de {soma}.')

print(soma)