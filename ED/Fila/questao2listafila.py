class Clinica:
    
    def __init__(self):
        self.__queue = Fila()
        self.__atendidos = 0
    
    def execute(self):
        decisao = ''
        while True:
            decisao = input('''Clinica Medica - Atendimento
=============
1. Incluir paciente
2. Realizar chamada
3. Consultar a posição atual
4. Listar a quantidade de pacientes atendidos
5. Sair
=============
''')
            try:
                if decisao == '1':
                    self.__queue.enfileira([input('Nome : '),input('CPF : '),input('Plano de Saúde(opcional) : ')])

                elif decisao == '2':
                    assert not self.__queue.estaVazia()
                    print(f'Paciente {self.__queue.desenfileira()} chamado.')
                    self.__atendidos += 1

                elif decisao == '3':
                    print(f'Próximo paciente a ser atendido : {self.__queue.frente()}')

                elif decisao == '4':
                    print(f'{self.__atendidos} pacientes foram atendidos.')

                elif decisao == '5':
                    break
            except AssertionError:
                print(f'Fila de atendimento vazia.')

        print(f'FIM DA EXECUÇÃO')

clinica = Clinica()
clinica.execute()