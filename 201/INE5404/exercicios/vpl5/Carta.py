from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        self.__personagem = personagem

    def valor_total_carta(self):
        soma = 0
        soma += self.__personagem.energia
        soma += self.__personagem.habilidade
        soma += self.__personagem.velocidade
        soma += self.__personagem.resistencia

        return soma

    @property
    def personagem(self):
        return self.__personagem
