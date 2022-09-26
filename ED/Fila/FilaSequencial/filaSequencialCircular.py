class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class filaSequencialCircular:
    def __init__(self):
        self.__tamanho = 20
        self.__dados = [None for i in range(self.__tamanho)]
        self.__ocupados = 0
        self.__inicio = 0
        self.__final = -1
    
    def estaVazia(self):
        return self.__ocupados == 0
    
    def tamanho(self)->int:
        return self.__ocupados

    def __len__(self)->int:
        return self.__ocupados
    
    def elemento(self, posicao:int)->any:
        try:
            assert posicao > 0 and posicao <= self.__ocupados
            cont = self.__inicio
            for i in range(posicao-1):
                cont = (cont + 1) % self.__tamanho
            return self.__dados[cont]
        except AssertionError:
            raise FilaException(f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')
    
    def busca(self, valor:any)->int:
        cont = self.__inicio
        for i in range(self.__ocupados):
            if (self.__dados[cont] == valor):
                return i+1
            print(cont)
            cont = (cont + 1) % self.__tamanho
        raise FilaException(f'Valor {valor} não está na pilha')

    def modificar(self, posicao:int, valor:any):
        try:
            assert posicao > 0 and posicao <= self.__ocupados
            cont = self.__inicio
            for i in range(posicao-1):
                cont = (cont + 1) % self.__tamanho
            self.__dados[cont] = valor
        except AssertionError:
            raise FilaException(f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')
    
    def enfileira(self, valor: any):
        try:
            assert self.__ocupados < self.__tamanho 
            self.__final = (self.__final + 1) % self.__tamanho # o maior valor que self.__final vai assumir é self.__tamanho-1
            self.__dados[self.__final] =  valor
            self.__ocupados += 1
        except AssertionError:
            raise FilaException('A fila está Cheia impossível Enfileirar')
    
    def desenfileira(self)->any:
        try:
            assert not self.estaVazia()
            inicio = self.__dados[self.__inicio]
            self.__inicio = (self.__inicio + 1) % self.__tamanho
            self.__ocupados -= 1
            return inicio
        except AssertionError:
            raise FilaException(f'A pilha está Vazia impossivel desempilhar')

    def __str__(self) -> str:
        s = ''
        for num in range(self.__ocupados):
            s += f'{self.__dados[(self.__inicio + num)%self.__tamanho]} '
        return s

    def esvazia(self):
        while not self.estaVazia():
            self.desenfileira()
            

    def inverte(self):
        self.__dados.reverse()
        aux = self.__inicio
        self.__inicio = self.__tamanho - self.__final - 1
        self.__final = self.__tamanho - aux - 1
