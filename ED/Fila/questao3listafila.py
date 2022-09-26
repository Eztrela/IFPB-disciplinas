class Reidomocoto:
    def __init__(self):
        self.__pedido = Fila()
        self.__pagamento = Fila()
        self.__encomenda = Fila()
        self.__atendido = None

    def insercao(self, cliente: str):
        self.__pedido.enfileira(cliente)

    def rmPedido(self):
        self.__pagamento.enfileira(self.__pedido.desenfileira())

    def rmPagamento(self):
        self.__encomenda.enfileira(self.__pagamento.desenfileira())

    def rmEncomenda(self) -> str:
        return self.__encomenda.desenfileira()

    def execute(self):
        decisao = ''
        while True:
            decisao = input(f'''Rei do Mocotó - Atendimento
Pedidos : {self.__pedido}
Pagamentos : {self.__pagamento}
Encomendas : {self.__encomenda}
Atendido : {self.__atendido}
=============
1. Inserir na fila de pedido
2. Remover da fila de pedido
3. Remover da fila de pagamento
4. Remover da fila de Encomenda
5. Sair
=============
''')
            try:
                if decisao == '1':
                    self.insercao(input('Nome : '))

                elif decisao == '2':
                    assert not self.__pedido.estaVazia()
                    print(f'Cliente {self.rmPedido()} transferido para Pagamento.')
                    

                elif decisao == '3':
                    assert not self.__pagamento.estaVazia()
                    print(f'Cliente {self.rmPagamento()} transferido para Encomenda.')

                elif decisao == '4':
                    assert not self.__pedido.estaVazia()
                    self.__atendido = self.rmEncomenda()
                    print(f'Cliente {self.__atendido} atendido.')

                elif decisao == '5':
                    break
            except AssertionError:
                print(f'Fila vazia.')

        print(f'FIM DA EXECUÇÃO')

reidomocoto = Reidomocoto()
reidomocoto.execute()