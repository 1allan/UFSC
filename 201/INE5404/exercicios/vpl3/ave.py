from abc import abstractmethod
from animal import Animal


class Ave(Animal):
    def __init__(self, tamanhoPasso: int, alturaVoo: int):
        super().__init__(tamanhoPasso)
        self.__alturaVoo = alturaVoo

    @property
    def alturaVoo(self):
        return self.__alturaVoo

    @alturaVoo.setter
    def alturaVoo(self, alturaVoo: int):
        self.__alturaVoo = alturaVoo

    @abstractmethod
    def mover(self):
        return 'ANIMAL: DESLOCOU {} VOANDO' .format(super().tamanhoPasso)

    @abstractmethod
    def produzirSom(self):
        pass
