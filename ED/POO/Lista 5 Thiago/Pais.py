class Pais:
    def __init__(self, nome:str, nome_capital:str, dimensao:float, paises_fronteira:list) -> None:
        self.__nome = nome
        self.__nome_capital = nome_capital
        self.__dimensao = dimensao
        self.__paises_fronteira = paises_fronteira