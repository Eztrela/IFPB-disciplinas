N = int(input('Informe o valor de N: '))
M = 0
F = 0
for i in range(N):
    sexo = input('informe o sexo: ').lower()
    if(sexo == 'm'):
        M += 1
    elif(sexo == 'f'):
        F += 1

pm = (M/N)*100
pf = (F/N)*100

print(f'o percentual de homens foi de {pm:.2f}% e de mulheres foi de {pf:.2f}%')