class Capitulo:
    def __init__(self, numero: int, titulo: str):
        self.__numero = numero
        self.__titulo = titulo
    
    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, valor: int):
        self.__numero = valor
    
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, valor: str):
        self.__titulo = valor