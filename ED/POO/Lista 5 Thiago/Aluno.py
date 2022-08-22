class Aluno:
    def __init__(self, matricula:int, nome:str, notas:list) -> None:
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas
    @property
    def nome(self) -> str:
        return self.__nome
    
    @property
    def matricula(self) -> str:
        return self.__matricula

    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome
    
    def media(self) -> float:
        soma = 0
        for nota in self.__notas:
            soma += nota
        media = soma/len(self.__notas)
        return media
    
    def adiciona_nota(self, nota):
        self.__notas.append(nota)