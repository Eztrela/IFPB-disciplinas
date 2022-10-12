senha = 'abcd'
erros = 0
while (erros < 3):
    s_digitada = input('Digite a senha: ')
    if(s_digitada == senha):
        print('Senha Correta')
    else:
        print('Senha Incorreta')
        erros += 1