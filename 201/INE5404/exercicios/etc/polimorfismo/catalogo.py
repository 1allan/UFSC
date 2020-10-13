from transporte_aereo import TransporteAereo
from transporte_aquatico import TransporteAquatico
from transporte_terrestre import TransporteTerrestre

transportes = {
    'aereo': TransporteAereo,
    'aquatico': TransporteAquatico,
    'terrestre': TransporteTerrestre
}


class Catalogo:

    def __init__(self):
        self.veiculos = []

    def inserir(self):
        tipo = input ('Tipo do transporte (aereo, aquatico, terrestre):\n').trim().lower()
        args = [input('Nome: '), input('Altura: '), input('Comprimento: '), 
        input('Carga: '), input('Velocidade: ')]
        
        if tipo in transportes.keys():
            if tipo == 'aereo':
                args += [input('Autonomia: '), input('Envergadura: ')]
            elif tipo == 'aquatico':
                args += [input('Boca: '), input('Calado: ')]
            elif tipo == 'terrestre':
                args += [input('Motor: '), input('Rodas: ')]
            else:
                return
            self.veiculos.append(transportes[tipo](*args))


    def mostrar(self):
        for veiculo in self.veiculos:
            print('Tipo:', type(veiculo).__name__)
            print(veiculo, '\n')


if __name__ == '__main__':
    catalogo = Catalogo()
    while True:
        opt = input('1. Inserir veículo\n2. Mostrar veículos')

        if opt == '1':
            catalogo.inserir()
        elif opt == '2':
            catalogo.mostrar()
        else:
            break