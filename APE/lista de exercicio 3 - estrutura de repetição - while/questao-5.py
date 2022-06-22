while(True):
    numero = int(input('Digite um numero '))
    if (numero % 2 == 0):
        print(f'o numero {numero} é par')
    else:
        print(f'o numero {numero} é impar')

    resposta = input('Deseja Continuar? s/n')

    if (resposta == 'n'):
        break