class Data:
    def __init__(self,dia:int,mes:int,ano:int):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    
    @property
    def dia(self) -> int:
        return self.__dia
            
    @property
    def mes(self) -> int:
        return self.__mes
    
    @property
    def ano(self) -> int:
        return self.__ano
    
    @dia.setter
    def dia(self, dia:int):
        self.__dia = dia
    
    @mes.setter
    def mes(self, mes:int):
        self.__mes = mes
        
    @ano.setter
    def ano(self, ano:int):
        self.__ano = ano

    def __str__(self)->str:
        # data_completa = str(self.__dia) + '/' + str(self.__mes) + '/' + str(self.__ano)
        return f'{self.__dia}/{self.__mes:2}/{self.ano}'