from abc import ABC, abstractmethod


class Abstrata(ABC):
    def __init__(self):
        self.var = "teste"

    @abstractmethod
    def teste(self):
        pass

    def print1(self):
        print("isso é um teste")


# class Teste(Abstrata):
#     def __init__(self):
#         self.teste2 = ""


# teste = Teste().print1()
