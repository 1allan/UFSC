from abc import abstractmethod
from animal import Animal


class Mamifero(Animal):
    def __init__(self, volumeSom: int, tamanhoPasso: int):
        super().__init__(tamanhoPasso)
        self.__volumeSom = volumeSom

    @property
    def volumeSom(self):
        return self.__volumeSom

    @volumeSom.setter
    def volumeSom(self, volumeSom: int):
        self.__volumeSom = volumeSom

    @abstractmethod
    def produzirSom(self):
        pass
