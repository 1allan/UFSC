from transporte import Transporte

class TransporteTerrestre(Transporte):

    def __init__(self,
                 nome,
                 altura,
                 comprimento,
                 carga,
                 velocidade,
                 motor,
                 rodas):
        super().__init__(nome, altura, comprimento, carga, velocidade)
        self.motor = motor
        self.rodas = rodas
    
    def __str__(self):
        infos_gerais = super().__str__()
        return f'{infos_gerais}\nMotor: {self.motor}\nRodas: {self.rodas}'

    