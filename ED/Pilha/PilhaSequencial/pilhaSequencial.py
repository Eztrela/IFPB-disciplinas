class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class pilhaSequencial:
    def __init__(self):
        self.__dados = []
    
    def estaVazia(self):
        return len(self.__dados) == 0
    
    def tamanho(self)->int:
        return len(self.__dados)

    def __len__(self)->int:
        return len(self.__dados)
    
    def elemento(self, posicao:int)->any:
        try:
            assert posicao > 0 and posicao <= len(self.__dados)
            return self.__dados[posicao-1]
        except AssertionError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')
    
    def busca(self, valor:any)->int:
        for i in range(len(self.__dados)):
            if(self.__dados[i] == valor):
                return i+1
        raise PilhaException(f'Valor {valor} não está na pilha')

    def modificar(self, posicao:int, valor:any):
        try:
            assert posicao > 0 and posicao <= len(self.__dados)
            self.__dados[posicao-1] = valor
        except AssertionError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')
    
    def empilha(self, valor: any):
        self.__dados.append(valor)
    
    def desempilha(self)->any:
        try:
            assert len(self.__dados) > 0
            return self.__dados.pop()
        except AssertionError:
            raise PilhaException(f'A pilha está Vazia impossivel desempilhar')

    def __str__(self) -> str:
        s = ''
        for num in self.__dados:
            s += f'{num} '
        return s

    def esvazia(self):
        while not self.estaVazia():
            self.desempilha()

    def inverte(self):
        self.__dados.reverse()