class Transporte:

    def __init__(self, nome, altura, comprimento, carga, velocidade):
        self.nome = nome
        self.altura = altura
        self.comprimento = comprimento
        self.carga = carga
        self.velocidade = velocidade

    def __str__(self):
        return f'Nome: {self.nome}\nAltura: {self.altura}\nComprimento: {self.comprimento}\nCarga: {self.carga}\nVelocidade: {self.velocidade}'