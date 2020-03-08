class Veiculo:
    def __init__(self, chassi, placa, modelo, marca, preco=30000):
        self.chassi = chassi
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.preco = preco
        
    
    def calcular_preco(self):
        return self.preco
    
    def info(self):
        print(f'Chassi: {self.chassi}')
        print(f'Placa: {self.placa}')
        print(f'Modelo: {self.modelo}')
        print(f'Preço: {self.preco}R$')