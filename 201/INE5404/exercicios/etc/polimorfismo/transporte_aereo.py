from transporte import Transporte

class TransporteAereo(Transporte):

    def __init__(self,
                 nome,
                 altura,
                 comprimento,
                 carga,
                 velocidade,
                 autonomia,
                 envergadura):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.autonomia = autonomia
        self.envergadura = envergadura

    def __str__(self):
        infos_gerais = super().__str__()
        return f'{infos_gerais}\nAutonomia: {self.autonomia}\nEnvergadura: {self.envergadura}'
