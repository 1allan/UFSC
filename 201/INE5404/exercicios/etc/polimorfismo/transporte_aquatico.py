from transporte import Transporte

class TransporteAquatico(Transporte):

    def __init__(self,
                 nome,
                 altura,
                 comprimento,
                 carga,
                 velocidade,
                 boca,
                 calado):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.boca = boca
        self.calado = calado

    def __str__(self):
        infos_gerais = super().__str__()
        return f'{infos_gerais}\nBoca: {self.boca}\nCalado: {self.calado}'
