N = int(input('informe o valor de N: '))
result = 1
for i in range(1,N+1):
    result *= i
print(f'o fatorial de {N}! é igual a: {result}')   