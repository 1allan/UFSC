from q2_veiculo_allansoares import Veiculo

class Carro(Veiculo):
    def __init__(self, chassi, placa, modelo, marca, preco, assentos, tipo):
        super().__init__(chassi, placa, modelo, marca, preco)
        self.assentos = assentos
        self.tipo = tipo
        
    def calcular_preco(self):
        custo_prod = 0
        
        if self.tipo.upper() == 'SUV':
            custo_prod = self.preco * 0.15
        
        return self.preco * 1.1 + custo_prod
    
    def info(self):
        print(f'Chassi: {self.chassi}')
        print(f'Placa: {self.placa}')
        print(f'Modelo: {self.modelo}')
        print(f'Preço: {self.preco}R$')
        print(f'Assentos: {self.assentos}')
        print(f'Tipo: {self.tipo}')