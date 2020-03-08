from q2_veiculo_allansoares import Veiculo

class Caminhao(Veiculo):
    def __init__(self, chassi, placa, modelo, marca, preco, eixos, carga):
        super().__init__(chassi, placa, modelo, marca, preco)
        self.eixos = eixos
        self.carga = carga
        
    def calcular_preco(self):
        custo_prod = 0
        if self.eixos >= 2:
            custo_prod = self.preco * .20
        
        return self.preco * 1.5 + custo_prod
    
    def info(self): 
        print(f'Chassi: {self.chassi}')
        print(f'Placa: {self.placa}')
        print(f'Modelo: {self.modelo}')
        print(f'Preço: {self.preco}R$')
        print(f'Eixos: {self.eixos}')
        print(f'Carga máxima: {self.carga}')