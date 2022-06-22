while (True):
    nome = input()
    nascimento = int(input())
    ingresso = int(input())

    idade = 2021 - nascimento
    tempo_empregado = 2021 - ingresso
    if(idade >= 65):
        print('Pode Requerer Aposentadoria')
    elif(tempo_empregado >= 30):
        print('Pode Requerer Aposentadoria')
    elif(tempo_empregado >= 25 and idade >= 60):
        print('Pode Requerer Aposentadoria')
    else:
        print('Não Pode Requerer Aposentadoria')


    decisao = input('Deseja Fazer nova verificação?(S/N)').lower()
    if(decisao == 'n'):
        break