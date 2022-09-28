IDADE_MINIMA = 65
T_SERVICO = 30
controle = "S"
while controle != 'N':
    nome = input("Digite o nome: ")
    ano_nascimento = int(input("Digite o ano de nasciumento: "))
    ano_ingresso = int(input("Digite o ano de ingresso"))
    idade = 2022 - ano_nascimento
    tempo_trabalhado = 2022 - ano_ingresso
    print(f'{nome} tem {idade} anos de idade e {tempo_trabalhado} anos de trabalho')
    if(idade >= IDADE_MINIMA or tempo_trabalhado >= T_SERVICO or (tempo_trabalhado >= 25 and idade >= 60)):
        print(f'\n{nome} Pode Requerer Aposentadoria')
    else:
        print(f'{nome} Não pode Requerer Aposentadoria')
    
    controle = input(f'\nDeseja continuar executando?\n').upper()
