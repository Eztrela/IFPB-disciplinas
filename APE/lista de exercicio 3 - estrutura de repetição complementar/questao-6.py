senha_correta = 'abcd'
tentativas = 0

while (tentativas < 3):
    senha_digitada = input('Digite a sua senha: ')
    if(senha_correta == senha_digitada):
        print('Senha Correta')
    else:
        print('Senha Incorreta Tente Novamente')
        tentativas += 1