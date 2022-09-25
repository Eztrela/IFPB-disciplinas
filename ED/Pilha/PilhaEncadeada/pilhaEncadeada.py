from pickle import EXT4


class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class no:
    def __init__(self, carga:any):
        self.prox = None
        self.carga = carga
    
    def __str__(self):
        return str(self.carga)

class pilhaEncadeada:
    def __init__(self):
        self.__topo = None
        self.__tamanho = 0
    
    def estaVazia(self):
        return self.__topo == None
    
    def tamanho(self)->int:
        return self.__tamanho

    def __len__(self)->int:
        return self.__tamanho
    
    def elemento(self, posicao:int)->any:
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            cont = self.__tamanho
            cursor = self.__topo
            while(cont > posicao):
                cursor = cursor.prox
                cont -= 1
            return cursor.carga

        except AssertionError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')
    
    def busca(self, valor:any)->int:
        cont = self.__tamanho
        cursor = self.__topo
        while (cursor != None):
            if (cursor.carga == valor):
                return cont
            cursor = cursor.prox
            cont -= 1
        raise PilhaException(f'Valor {valor} não está na pilha')

    def modificar(self, posicao:int, valor:any):
        try:
            assert posicao > 0 and posicao <= self.__tamanho
            cont = self.__tamanho
            cursor = self.__topo
            while(cont > posicao):
                cursor = cursor.prox
                cont -= 1
            cursor.carga = valor

        except AssertionError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')
    
    def empilha(self, valor:any):
        novo = no(valor)
        novo.prox = self.__topo
        self.__topo = novo
        self.__tamanho += 1
        
    
    def desempilha(self)->any:
        try:
            assert not self.estaVazia()
            topo = self.__topo
            self.__topo = self.__topo.prox
            self.__tamanho -= 1
            return topo.carga
            
        except AssertionError:
            raise PilhaException(f'A pilha está Vazia impossivel desempilhar')

    def __str__(self):
        s = ''
        cursor = self.__topo
        while(cursor != None):
            s += f'{cursor.carga} '
            cursor = cursor.prox
        return s

    def inverte(self):
        try:
            assert not self.estaVazia()
            pilhaAuxiliar = pilhaEncadeada()

            while(not self.estaVazia()):
                pilhaAuxiliar.empilha(self.desempilha())
            self.__topo = pilhaAuxiliar.__topo
            self.__tamanho = pilhaAuxiliar.__tamanho
        except AssertionError:
            raise PilhaException(f'A pilha está Vazia')
    
    def subTopo(self)->int:
        cursor = self.__topo
        if self.estaVazia():
            raise PilhaException(f'A pilha está Vazia')
        elif cursor.prox == None:
            raise PilhaException(f'A pilha so possui um elemento')
        return self.__topo.prox.carga
    
    def desempilha_n(self, vezes):
        try:
            assert vezes > 0 and vezes <= self.__tamanho
            for i in range(vezes):
                print(self.desempilha())
            return True
        except AssertionError:
            return False
    
    def esvazia(self):
        while(not self.estaVazia()):
            self.desempilha()

    def obtemBase(self):
        cursor = self.__topo
        while(cursor.prox != None):
            cursor = cursor.prox
        return cursor.carga

    @classmethod
    def doubleconcatenar(cls, pilha1: object, pilha2: object):
        out = pilhaEncadeada()
        t = pilhaEncadeada()

        while not pilha1.estaVazia():
            t.empilha(pilha1.desempilha())
        while not t.estaVazia():
            out.empilha(t.desempilha())

        while not pilha2.estaVazia():
            t.empilha(pilha2.desempilha())
        while not t.estaVazia():
            out.empilha(t.desempilha())
            
        return out

    def topo(self):
        return self.__topo.carga