from socket import NI_NUMERICHOST


contador = 0
soma = 0
while(contador < 30 ):
    numero = int(input('digite o numero' ))
    soma += numero
    contador +=1

print(f'a soma dos numeros é {soma}')